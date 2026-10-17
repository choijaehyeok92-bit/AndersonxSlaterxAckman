"""L7 판단 로그·실적 갱신·교정 — 하네스가 나아지고 있는지 알 수 있는 유일한 장치.

research/<TICKER>/journal.jsonl에 한 줄씩 덧붙인다 (지우지 않는다).
  judgment  판정·표·KPI(확률 붙은 예측)·반증 조건·기본 시나리오 추정치, 직전 판단 대비 바뀐 점
  update    새 실적으로 KPI 적중·반증 조건·추정 대비 실제를 대조 → 유지 / 약화 / 훼손
  decision  사람이 정한 비중과 이유 (하네스는 비중을 정하지 않는다)
"""
import json, math
from . import core, facts
from .judge import status

KEEP = ("basis", "verdict", "score", "agents", "kpis", "gated", "iv")


def entries(d):
    p = d / "journal.jsonl"
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def append(d, e):
    with open(d / "journal.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")
    return e


def log(d, r):
    """판정을 기록한다. 직전 판단과 내용이 같으면 쓰지 않는다."""
    an, es = r["analysis"], entries(d)
    v = an.get("valuation")
    js = [e for e in es if e["type"] == "judgment"]
    slater = next((x["metrics"] for x in r["agents"] if x["agent"] == "slater"), {})
    e = dict(type="judgment", id=f"J{len(js) + 1}", date=core.today(), as_of=r["as_of"], basis=core.basis(d, "model"),
             verdict=r["verdict"], label=r["label"], score=r["score"], gated=r.get("gated"),
             agents={x["agent"]: dict(stance=x["stance"], final=x["final"], conviction=x["conviction"], override=x["override"])
                     for x in r["agents"]},
             price=(an.get("market") or {}).get("price"), iv={k: round(s["iv"], 4) for k, s in v["scenarios"].items()} if v else None,
             expected_irr=v["expected"]["irr"] if v else None, kpis=r["kpis"], breaks=r["breaks"],
             must_be_true=[x for x in slater.get("must_be_true", []) if x.get("metric")],
             projection={x["period"]: dict(revenue=x["revenue"], fcf=x["fcf"]) for x in v["scenarios"]["base"]["rows"]} if v else None,
             sources=[s["id"] for s in r["sources"]], sizing=r["sizing"].get("suggested"))
    prev = js[-1] if js else None
    if prev and core.digest({k: prev.get(k) for k in KEEP}) == core.digest({k: e.get(k) for k in KEEP}):
        return None
    e["changes"] = changes(prev, e, r)
    return append(d, e)


def changes(prev, e, r):  # "왜 바꿨는가" — 나중에 판단의 질을 평가하려면 이게 남아 있어야 한다
    if not prev:
        return ["첫 판단"]
    out = [f"판정 {prev['label']} → {e['label']}"] if prev["verdict"] != e["verdict"] else []
    for x in r["agents"]:
        p = prev["agents"].get(x["agent"])
        if p and (p["final"], p["conviction"]) != (x["final"], x["conviction"]):
            o = x["opinion"]
            why = o.get("change_reason") or next(iter(o.get("concessions") or []), "")
            out.append(f"{x['name']} {core.STANCE[p['final']][0]}({p['conviction']}) → {core.STANCE[x['final']][0]}({x['conviction']})"
                       + (f": {why}" if why else ""))
    new = [s for s in e["sources"] if s not in set(prev.get("sources", []))]
    if new:
        out.append(f"새 근거 {', '.join(new[:12])}{' …' if len(new) > 12 else ''}")
    if prev.get("iv") and e.get("iv") and prev["iv"].get("base") and abs(e["iv"]["base"] / prev["iv"]["base"] - 1) > 0.10:
        out.append(f"기본 시나리오 IV {prev['iv']['base']:,.2f} → {e['iv']['base']:,.2f}")
    return out or ["근거·모델 갱신 — 판정 유지"]


def update(d):
    """새 실적이 들어오면 직전 판단을 대조한다. 판정을 다시 내리지는 않는다 — 훼손·약화면 재토론."""
    es = entries(d)
    js = [e for e in es if e["type"] == "judgment"]
    if not js:
        raise ValueError("판단 로그(journal.jsonl) 없음 — 먼저 judge")
    j, ev = js[-1], core.load(d / "evidence.json")
    fx = facts.Facts(ev)
    kp = []
    for k in j.get("kpis", []):
        hit, actual = status(fx, k)
        kp.append({**k, "actual": actual, "status": "대기" if hit is None else "적중" if hit else "빗나감"})
    br = []
    for b in j.get("breaks", []):
        hit, actual = status(fx, b) if b.get("metric") else (None, None)
        br.append({**b, "actual": actual, "status": "수동 확인" if not b.get("metric") else "자료 없음" if hit is None
                   else "충족 — 훼손" if hit else "미충족"})
    mbt = []
    for x in j.get("must_be_true", []):
        ok, actual = status(fx, x)
        mbt.append({**x, "actual": actual, "status": "broken" if ok is False else x.get("status")})
    dev = []
    for period, p in (j.get("projection") or {}).items():
        rev, ocf, capex = fx.value("revenue", period), fx.value("ocf", period), fx.value("capex", period)
        if rev is not None:
            dev.append(dict(period=period, metric="revenue", model=p["revenue"], actual=rev, diff=rev / p["revenue"] - 1))
        if ocf is not None and capex is not None and p["fcf"]:
            dev.append(dict(period=period, metric="fcf", model=p["fcf"], actual=ocf - abs(capex), diff=(ocf - abs(capex)) / p["fcf"] - 1))
    broken = [b for b in br if b["status"].startswith("충족")] + [x for x in mbt if x["status"] == "broken"]
    weak = [k for k in kp if k["status"] == "빗나감"] + [x for x in dev if x["metric"] == "revenue" and x["diff"] < -0.10]
    e = dict(type="update", date=core.today(), as_of=ev.get("as_of"), ref=j["id"], status="훼손" if broken else "약화" if weak else "유지",
             kpis=kp, breaks=br, must_be_true=mbt, deviations=dev)
    last = next((x for x in reversed(es) if x["type"] == "update"), None)
    same = last and core.digest({k: last.get(k) for k in ("ref", "as_of", "kpis", "breaks", "deviations")}) == \
        core.digest({k: e.get(k) for k in ("ref", "as_of", "kpis", "breaks", "deviations")})
    return e if same else append(d, e)


def decide(d, size, note=""):
    js = [e for e in entries(d) if e["type"] == "judgment"]
    if not js:
        raise ValueError("판단 로그 없음 — 먼저 judge")
    if not 0 <= size <= 1:
        raise ValueError("size는 0~1 (예: 0.02 = 2%)")
    return append(d, dict(type="decision", date=core.today(), ref=js[-1]["id"], verdict=js[-1]["label"],
                          suggested=js[-1].get("sizing"), size=size, note=note))


def calibrate(dirs):
    """확신도 p라고 한 예측이 실제로 몇 % 맞았는가 + 하네스가 '반대'를 내기는 하는가."""
    preds, latest, flips = [], {}, {}
    for d in dirs:
        es = entries(d)
        js = [e for e in es if e["type"] == "judgment"]
        if not js:
            continue
        latest[d.name] = js[-1]
        flips[d.name] = sum(a["verdict"] != b["verdict"] for a, b in zip(js, js[1:]))
        for j in js:
            ups = [u for u in es if u["type"] == "update" and u.get("ref") == j["id"]]
            res = {k["id"]: k for k in ups[-1]["kpis"]} if ups else {}
            for k in j.get("kpis", []):  # 판단 당시 이미 결과가 나온 KPI는 예측이 아니다
                if k.get("status") == "대기" and res.get(k["id"], {}).get("status") in ("적중", "빗나감"):
                    preds.append(dict(ticker=d.name, judgment=j["id"], kpi=k["id"], p=k["p"], hit=res[k["id"]]["status"] == "적중"))
    buckets = {}
    for x in preds:
        b = min(int(x["p"] * 10), 9) / 10
        buckets.setdefault(b, []).append(x)
    verdicts = {}
    for j in latest.values():
        verdicts[j["verdict"]] = verdicts.get(j["verdict"], 0) + 1
    judged = sum(n for k, n in verdicts.items() if k != "INCOMPLETE")
    out = dict(cmd="calibrate", predictions=len(preds),
               brier=sum((x["p"] - x["hit"]) ** 2 for x in preds) / len(preds) if preds else None,
               buckets=[dict(range=f"{b:.0%}~{b + 0.1:.0%}", n=len(xs), mean_p=sum(x["p"] for x in xs) / len(xs),
                             hit_rate=sum(x["hit"] for x in xs) / len(xs)) for b, xs in sorted(buckets.items())],
               verdicts=verdicts, for_share=verdicts.get("FOR", 0) / judged if judged else None, flips=flips, warnings=[])
    if len(preds) < 20:
        out["warnings"].append(f"해소된 예측 {len(preds)}개 — 20개 미만은 교정을 해석하기 이르다")
    if judged >= 5 and out["for_share"] > 0.8:
        out["warnings"].append(f"판정 종목의 {out['for_share']:.0%}가 찬성 — 필터가 작동하지 않을 수 있다")
    out["warnings"] += [f"{t}: 판정이 {n}번 바뀌었다 — journal의 changes로 이유를 점검" for t, n in flips.items() if n >= 3]
    return out


def calibrate_md(c):
    brier = "—" if c["brier"] is None else f"{c['brier']:.3f}"
    out = [f"# 교정 — 해소된 예측 {c['predictions']}개", "", f"Brier 점수 {brier} (0이 완벽, 항상 50%라고 하면 0.25)", ""]
    if c["buckets"]:
        out += ["| 말한 확률 | n | 평균 p | 실제 적중률 |", "|---|---|---|---|"]
        out += [f"| {b['range']} | {b['n']} | {b['mean_p']:.0%} | {b['hit_rate']:.0%} |" for b in c["buckets"]]
        out.append("")
    out.append("최신 판정 분포: " + (", ".join(f"{k} {n}" for k, n in c["verdicts"].items()) or "없음")
               + ("" if c["for_share"] is None else f" — 찬성 비율 {c['for_share']:.0%}"))
    out += [f"- ⚠ {w}" for w in c["warnings"]]
    return "\n".join(out) + "\n"

"""오케스트레이션 — 게이트형 단방향 파이프라인과 하네스 자체의 시험(재현성·오류 주입).

  수집 → 리서치 → [게이트 0 근거] → 사업·경영진·회계(병렬) → [게이트 1 회계] → 모델 → 페르소나 1라운드·레드팀(병렬)
  → 2라운드(병렬) → 검증 → 판정
역할마다 별도 프로세스라 맥락이 섞이지 않는다. 끝난 단계는 건너뛰되, 앞 단계가 다시 돌면 뒤 단계도 모두 다시 돈다.
"""
import json, random, re, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from . import calc, collect, core, facts, judge, prompts

TIMEOUT = 1800


def outfile(d, role, rnd=1):
    return d / (f"{role}.{rnd}.json" if role in core.AGENTS else "model.json" if role == "modeler" else f"{role}.json")


def check(role, rnd, o):  # 최소 형식 — 어기면 한 번 다시 묻는다
    if not isinstance(o, dict):
        return "JSON 객체가 아니다"
    need = {"business": ("unit_economics", ("proven", "unclear", "deteriorating")), "management": ("alignment", judge.ALIGN),
            "forensic": ("grade", judge.GRADES)}
    if role in core.AGENTS:
        if o.get("stance") not in core.STANCE:
            return "stance는 for|against|abstain"
        if not o.get("arguments" if rnd == 1 else "rebuttals"):
            return f"{'arguments' if rnd == 1 else 'rebuttals'} 필요"
    elif role in need and o.get(need[role][0]) not in need[role][1]:
        return f"{need[role][0]}는 {'|'.join(need[role][1])}"
    elif role == "modeler" and not {"bear", "base", "bull"} <= set(o.get("scenarios") or {}):
        return "scenarios에 bear·base·bull 필요"
    elif role == "redteam" and not o.get("premortem"):
        return "premortem 필요"
    elif role == "verifier" and not isinstance(o.get("checks"), list):
        return "checks 목록 필요"
    return None


def call(cli, text):  # 프롬프트를 stdin으로 넘기고 stdout의 마지막 JSON 블록을 꺼낸다
    r = subprocess.run(cli, shell=True, input=text, capture_output=True, encoding="utf-8", timeout=TIMEOUT)
    if r.returncode:
        raise RuntimeError(f"`{cli}` 종료 코드 {r.returncode}: {r.stderr.strip()[-500:]}")
    blocks = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", r.stdout, re.S)
    return json.loads(blocks[-1] if blocks else r.stdout[r.stdout.find("{"):r.stdout.rfind("}") + 1])


def ask(cli, text, role="", rnd=1):
    try:
        out = call(cli, text)
        err = check(role, rnd, out) if role else None
    except ValueError as e:
        out, err = None, f"JSON 파싱 실패 — {e}"
    if err:
        out = call(cli, text + f"\n\n## 이전 출력의 문제\n{err}\n스키마에 맞는 JSON 객체 하나만 다시 출력하라.")
        if role and (err := check(role, rnd, out)):
            raise ValueError(f"{core.ROLES.get(role, role)} 출력 형식 오류: {err}")
    return out


def expected(d, role):
    return prompts.claims(d)[1] if role == "verifier" else core.basis(d, core.STAGE[role])


def stage(d, cli, roles, rnd, dirty, label, log):
    def fresh(r):
        p = outfile(d, r, rnd)
        return p.exists() and core.load(p).get("basis", expected(d, r)) == expected(d, r)
    todo = [r for r in roles if dirty or not fresh(r)]
    log(f"{label}: {', '.join(core.ROLES[r] for r in todo) or '완료됨'}")
    if not todo:
        return dirty
    texts = {r: prompts.prompt(r, d, rnd) for r in todo}  # 병렬 역할끼리 서로의 출력을 보지 않도록 먼저 만든다
    with ThreadPoolExecutor() as ex:
        outs = dict(zip(todo, ex.map(lambda r: ask(cli, texts[r], r, rnd), todo)))
    for r, o in outs.items():
        core.save(outfile(d, r, rnd), {**o, "agent": r, "basis": expected(d, r)})
    return True


def run(d, ticker, cli, force=False, name=None, lang="en", as_of=None, log=None):
    log = log or (lambda s: print(s, file=sys.stderr, flush=True))
    dirty = force
    if force or not (d / "evidence.json").exists():
        r = collect.collect(d, ticker, name, lang, as_of)
        log(f"[1/8] 수집 근거 +{r['added']} (총 {r['total']}) · 공시 재무 사실 {r['facts']}개 " + " ".join(r["errors"]))
        dirty = True
    if dirty or not core.load(d / "evidence.json").get("researched"):
        log("[2/8] 리서치 …")
        m = collect.merge(d, ask(cli, prompts.prompt("researcher", d), "researcher"))
        log(f"      사실 +{m['facts_added']}" + "".join(f"\n      제외: {x}" for x in m["rejected"]))
        dirty = True
    ev = core.load(d / "evidence.json")
    if miss := calc.sufficiency(ev, calc.analyze(ev)):
        log(f"[게이트 0] 근거 부족 — 멈춤: {'; '.join(miss)}")
        return judge.judge(d)
    dirty = stage(d, cli, list(core.MODULES), 1, dirty, "[3/8] 사업·경영진·회계 품질", log)
    if core.load(d / "forensic.json").get("grade") == "red_flag":
        log("[게이트 1] 회계 품질 red_flag — 모델·토론을 하지 않는다")
        return judge.judge(d)
    dirty = stage(d, cli, ["modeler"], 1, dirty, "[4/8] 모델 가정", log)
    dirty = stage(d, cli, [*core.AGENTS, "redteam"], 1, dirty, "[5/8] 1라운드·레드팀", log)
    dirty = stage(d, cli, list(core.AGENTS), 2, dirty, "[6/8] 2라운드", log)
    stage(d, cli, ["verifier"], 1, dirty, "[7/8] 독립 검증", log)
    log("[8/8] 판정")
    return judge.judge(d)


# ── 하네스 시험 ──

def summary(r):
    v = r["analysis"].get("valuation") or {}
    return dict(verdict=r["verdict"], label=r["label"], agents={x["agent"]: x["final"] for x in r["agents"]},
                forensic=(r["modules"].get("forensic") or {}).get("grade"),
                iv_base=v.get("scenarios", {}).get("base", {}).get("iv"), expected_irr=v.get("expected", {}).get("irr"))


def repro(d, cli, runs=2, log=None):
    """같은 근거·같은 기준일로 N번 돌려 결론과 핵심 숫자의 편차를 잰다. 편차가 크면 판단이 아니라 소음이다."""
    if not core.load(d / "evidence.json").get("researched"):
        raise ValueError("리서치가 끝난 evidence.json이 필요하다 — 근거를 고정해야 재현성을 잴 수 있다")
    out = []
    for i in range(1, runs + 1):
        rd = d / "repro" / f"run{i}"
        if rd.exists():
            shutil.rmtree(rd)
        rd.mkdir(parents=True)
        shutil.copy(d / "evidence.json", rd / "evidence.json")  # 사용자 견해·판단 로그는 복사하지 않는다
        out.append(summary(run(rd, d.name, cli, log=log)))
    spread = lambda xs: (max(xs) - min(xs)) if len(xs) > 1 else 0.0
    ivs = [x["iv_base"] for x in out if x["iv_base"]]
    irr = [x["expected_irr"] for x in out if x["expected_irr"] is not None]
    agree = lambda k: len({json.dumps(x[k], sort_keys=True) for x in out}) == 1
    r = dict(cmd="repro", runs=out, verdict_agree=agree("verdict"), agents_agree=agree("agents"), forensic_agree=agree("forensic"),
             iv_spread=spread(ivs) / (sum(ivs) / len(ivs)) if ivs else None, irr_spread=spread(irr) if irr else None)
    r["ok"] = r["verdict_agree"] and r["agents_agree"]
    core.save(d / "repro.json", r)
    return r


def corrupt(point, k):  # 주장의 첫 단위 숫자를 k배로 바꾼다
    for m in facts.NUM.finditer(point):
        dollar, whole, frac, scale, unit = m.groups()
        if not (dollar or scale or unit):
            continue
        new = float(whole.replace(",", "") + (frac or "")) * k
        dec = len((frac or ".")[1:])
        s = f"{new:,.{dec}f}" if "," in whole else f"{new:.{dec}f}"
        return point[:m.start(2)] + s + point[m.end(3) if frac else m.end(2):], s
    return None, None


def audit(d, cli, n=5, seed=0):
    """오류 주입 — 주장 속 숫자를 일부러 틀리게 바꾸고 검증자(LLM)와 기계 대조(코드)가 잡아내는지 본다."""
    ev, model = core.load(d / "evidence.json"), core.load(d / "model.json", {})
    (fx, (cl, key)), vf = (facts.Facts(ev), prompts.claims(d)), core.load(d / "verifier.json", {})
    before = {c.get("id"): c.get("verdict") for c in vf.get("checks", [])} if vf.get("basis") == key else {}
    an = calc.analyze(ev, model or None)
    everything = facts.pool(fx.src.values(), fx.facts.values(), an["ref"], an["ref_pct"])
    rng = random.Random(seed)
    cand = [c for c in cl if c["cites"] and not c["point"].lstrip().startswith("추정") and corrupt(c["point"], 1.5)[0]]
    picked = {c["id"] for c in rng.sample(cand, min(n, len(cand)))}
    mutated = []
    for c in cl:
        if c["id"] in picked:
            k = rng.choice((0.6, 1.5, 2.0))
            c = {**c, "point": corrupt(c["point"], k)[0], "injected": k}
        mutated.append(c)
    text = "\n\n".join(["<!-- council role=verifier round=1 -->", core.doc("verifier"),
                        f"## 지금 할 일\n{prompts.TASK['verifier']}", "## 검증할 주장", prompts.verifier_view(d, mutated, ev, fx)])
    got = {x.get("id"): x.get("verdict") for x in ask(cli, text, "verifier").get("checks", [])}
    flagged = lambda c: got.get(c["id"]) in ("contradicted", "unsupported")
    details = []
    for c in mutated:
        if "injected" in c:
            mech, warn = judge.mechanical(c, fx, an["ref"], everything, facts.doctrine(c["role"]) + tuple(facts.loose(model)), an["ref_pct"])
            details.append(dict(id=c["id"], role=c["role"], point=c["point"], factor=c["injected"], verifier=got.get(c["id"]),
                                code="실패 처리" if mech else "경고" if warn else "놓침"))
    caught = sum(flagged(c) for c in mutated if "injected" in c)
    r = dict(cmd="audit", injected=len(details), caught_by_verifier=caught,
             caught_by_code=sum(x["code"] != "놓침" for x in details),
             clean=len(mutated) - len(details), details=details,
             flagged_clean=sum(flagged(c) for c in mutated if "injected" not in c),  # 주입하지 않은 주장 중 지적 (원래 결함일 수 있다)
             false_alarms=sum(flagged(c) for c in mutated if "injected" not in c and before.get(c["id"]) == "supported") if before else None)
    r["ok"] = bool(details) and caught / len(details) >= 0.8
    core.save(d / "audit.json", r)
    return r

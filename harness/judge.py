"""L5·L6 판정 — 말이 아니라 규칙이 집계한다.

게이트(근거 충분성 → 회계 품질 → 모델) → 페르소나 레드라인(코드 계산 지표로) → 주장 검증(기계 대조 + 독립 검증자)
→ 가중 표결. 지표는 코드 계산값이 페르소나가 쓴 값을 이긴다.
"""
from . import calc, core, facts, prompts, rules
from .core import items

OPS = {"<": lambda a, b: a < b, "<=": lambda a, b: a <= b, ">": lambda a, b: a > b, ">=": lambda a, b: a >= b}
GRADES, ALIGN, MOAT = ("clean", "watch", "red_flag"), ("aligned", "mixed", "misaligned"), ("proven", "claimed")
VERDICTS = ("supported", "unsupported", "contradicted", "leap")


def opinion(d, a):  # 최종 의견 = 1라운드에 2라운드를 덮어쓴 것 (metrics·case는 필드 단위)
    r1, r2 = core.load(d / f"{a}.1.json"), core.load(d / f"{a}.2.json", {})
    m = {**r1.get("metrics", {}), **r2.get("metrics", {})}
    if "must_be_true" in m:
        m["must_be_true"] = items(m["must_be_true"], "claim")
    return {**r1, **r2, "metrics": m, "case": {**(r1.get("case") or {}), **(r2.get("case") or {})} or None,
            "thesis_breaks": items(r2.get("thesis_breaks") or r1.get("thesis_breaks"), "note"),
            "rebuttals": items(r2.get("rebuttals"), "point"), "opening": r1.get("stance"), "round": 2 if r2 else 1}


def status(fx, x):
    """조건 {metric, op, value, period?}을 현재 사실에 대어 본다 → (조건 성립 여부 | None, 실제 값)."""
    if not x.get("metric") or x.get("op") not in OPS or not isinstance(x.get("value"), (int, float)):
        return None, None
    f = fx.get(x["metric"], x.get("period")) or fx.get(x["metric"], x.get("period"), basis="market")
    return (None, None) if f is None else (OPS[x["op"]](f["value"], x["value"]), f["value"])


def breaks(fx, items, who):
    out = []
    for x in items or []:
        hit, actual = status(fx, x)
        out.append(dict(who=who, metric=x.get("metric"), op=x.get("op"), value=x.get("value"), period=x.get("period"),
                        note=x.get("note", ""), actual=actual,
                        status="수동 확인" if not x.get("metric") else "자료 없음" if hit is None else "충족 — 훼손" if hit else "미충족"))
    return out


def stale(d, name, out, stage):
    b = out.get("basis")
    return [] if not b or b == core.basis(d, stage) else [f"{name}: 입력(근거·모델)이 바뀐 뒤 갱신되지 않음 — 다시 실행 (basis {b})"]


def judge(d):
    ev, model = core.load(d / "evidence.json"), core.load(d / "model.json", {})
    fx = facts.Facts(ev)
    ops = {a: opinion(d, a) for a in core.AGENTS if (d / f"{a}.1.json").exists()}
    an = calc.analyze(ev, model or None, {a: o["case"] for a, o in ops.items()})
    mods = {m: core.load(d / f"{m}.json") for m in core.MODULES if (d / f"{m}.json").exists()}
    redteam = core.load(d / "redteam.json", {})
    notes = [f"{t} 유형 근거 없음 — 리서치 보강 필요" for t in ("filing", "call") if t not in {s["type"] for s in fx.src.values()}]
    notes += an["warnings"]
    for m, o in mods.items():
        notes += stale(d, core.ROLES[m], o, "evidence")
    if model:
        notes += stale(d, "모델러", model, "modules")
    if redteam:
        notes += stale(d, "레드팀", redteam, "model")
    r = dict(cmd="judge", ticker=ev.get("ticker", d.name), name=ev.get("name", d.name), as_of=fx.as_of, gates=[], gated=None,
             verdict="INCOMPLETE", label="판정 불가", votes={k: 0 for k in core.STANCE}, score=0.0, agents=[], notes=notes,
             analysis=an, modules=mods, model=model, redteam=redteam, breaks=[], kpis=[], user_view=None,
             verification=dict(checked=False, total=0, counts={}, flagged=[]), sources=list(fx.src.values()),
             sizing=dict(suggested=0.0, why="판정 전"))

    def stop(name, why, verdict="INCOMPLETE", label=None):
        r["gates"].append(dict(name=name, ok=False, why=why))
        r.update(verdict=verdict, label=label or f"판정 불가 — {name}", gated="; ".join(why), ok=False)
        r["user_view"] = contrast(d, r)
        return r

    miss = calc.sufficiency(ev, an)
    if miss:
        return stop("근거 충분성", miss)
    r["gates"].append(dict(name="근거 충분성", ok=True, why=[]))
    # 게이트 1: 회계 품질 — 걸리면 모델·토론을 하지 않는다
    fo = mods.get("forensic")
    if not fo:
        return stop("회계 품질", ["forensic.json 없음 — 회계 품질 검토 전에는 밸류에이션·토론을 하지 않는다"])
    if fo.get("grade") not in GRADES:
        raise ValueError(f"forensic.grade는 {'|'.join(GRADES)} 중 하나")
    reds = [f["key"] for f in an["forensic"] if f["severity"] == "red"]
    if reds and fo["grade"] == "clean":
        notes.append(f"코드 red 신호({', '.join(reds)})가 있는데 forensic이 clean — watch로 낮춘다")
        fo = {**fo, "grade": "watch"}
        mods["forensic"] = fo
    told = {x.get("key") for x in items(fo.get("flags"), "point")}
    notes += [f"회계 품질 신호 {f['key']}를 forensic이 해명하지 않음" for f in an["forensic"] if f["key"] not in told]
    if fo["grade"] == "red_flag":
        return stop("회계 품질", [fo.get("summary") or "red_flag"], "AGAINST", "게이트 탈락: 회계 품질 — 반대")
    r["gates"].append(dict(name="회계 품질", ok=True, why=[fo["grade"]]))
    for m, o, field, allowed in (("business", mods.get("business"), "unit_economics", ("proven", "unclear", "deteriorating")),
                                 ("management", mods.get("management"), "alignment", ALIGN)):
        if not o:
            notes.append(f"{core.MODULES[m]} 분석({m}.json) 없음")
        elif o.get(field) not in allowed:
            raise ValueError(f"{m}.{field}는 {'|'.join(allowed)} 중 하나")
    for x in items((mods.get("business") or {}).get("moat"), "point"):
        types = {fx.src[c]["type"] for c in x.get("cites", []) if c in fx.src}
        hard = any(c in fx.facts or c.startswith("C:") for c in x.get("cites", [])) or types & {"filing", "data", "call"}
        if x.get("evidence") == "proven" and not hard:
            notes.append(f"해자 '{x.get('type')}'를 '입증'이라 했지만 회사 발표·보도만 인용 — 점유율·이탈률·가격 같은 공시 숫자가 필요")
    # 게이트 2: 모델
    if not model or not an["valuation"]:
        return stop("모델", ["model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고"])
    r["gates"].append(dict(name="모델", ok=True, why=[]))
    if not ops:
        return stop("토론", ["페르소나 의견(<agent>.1.json) 없음"])
    # 주장 검증 — 기계 대조(인용·숫자 추적) + 독립 검증자(verifier.json)
    cl, key = prompts.claims(d)
    vf = core.load(d / "verifier.json", {})
    if vf and vf.get("basis") not in (None, key):
        notes.append(f"verifier.json이 최신 주장과 맞지 않음 — 검증 결과를 쓰지 않는다 (basis {vf.get('basis')} ≠ {key})")
        vf = {}
    if not vf:
        notes.append("독립 검증(verifier.json) 없음 — 기계 대조만 반영")
    seen = {c.get("id"): c for c in vf.get("checks", [])}
    ref = an["ref"]
    everything = facts.pool(fx.src.values(), fx.facts.values(), ref, an["ref_pct"])
    shared = tuple(facts.loose(model))
    for c in cl:
        o = ops.get(c["role"], {})
        own = facts.loose([o.get("metrics"), o.get("case"), o.get("thesis_breaks")])
        allowed = facts.doctrine(c["role"]) + tuple(own) + (shared if c["role"] in ("modeler", "redteam") else ())
        c["mech"], c["warn"] = mechanical(c, fx, ref, everything, allowed, an["ref_pct"])
        v = seen.get(c["id"], {})
        c["verdict"] = "unsupported" if c["mech"] else v.get("verdict") if v.get("verdict") in VERDICTS else None
        c["reason"] = c["mech"] or v.get("reason", "")
    counts = {k: sum(c["verdict"] == k for c in cl) for k in VERDICTS}
    r["verification"] = dict(checked=True, total=len(cl), counts={**counts, "미검증": sum(c["verdict"] is None for c in cl)},
                             flagged=[c for c in cl if c["verdict"] in ("unsupported", "contradicted", "leap")])
    for c in cl:
        if c["role"] not in core.AGENTS and c["verdict"] in ("unsupported", "contradicted"):
            notes.append(f"{core.ROLES[c['role']]} {c['where']} 검증 실패({c['verdict']}): {c['reason']}")
        elif c["role"] not in core.AGENTS and c["warn"]:
            notes.append(f"{core.ROLES[c['role']]} {c['warn']}")
    rows = []
    for a, o in ops.items():
        stance = o.get("stance")
        if stance not in core.STANCE or o["opening"] not in core.STANCE:
            raise ValueError(f"{a}: stance는 {'|'.join(core.STANCE)} 중 하나")
        m, warn = dict(o.get("metrics", {})), []
        warn += stale(d, "1라운드", core.load(d / f"{a}.1.json"), "model")
        for k, val in an["personas"][a].items():
            if k in ("case", "leveraged", "error"):
                continue
            mine = m.get(k)
            if isinstance(mine, (int, float)) and not isinstance(mine, bool) and isinstance(val, (int, float)) and val \
                    and not isinstance(val, bool) and abs(mine / val - 1) > 0.2:
                warn.append(f"{k}: 페르소나가 쓴 {mine:g} 대신 코드 계산값 {val:.3g} 사용")
            m[k] = val
        if an["personas"][a].get("error"):
            warn.append(an["personas"][a]["error"])
        if a == "ackman" and an["personas"][a].get("leveraged"):
            if m.get("capital_markets_dependent") is False:
                warn.append(f"코드 판정: 순부채/EBITDA > {rules.LEVERAGE:g} 또는 FCF 음수·현금 소진 3년 미만 → 자본시장 의존")
            m["capital_markets_dependent"] = True
        if a == "slater":
            mbt = []
            for x in m.get("must_be_true", []):
                ok, actual = status(fx, x)
                if ok is False and x.get("status") != "broken":
                    warn.append(f"참이어야 하는 것 '{x.get('claim')}' — 실제 {actual:g}로 깨짐 (코드 판정)")
                    x = {**x, "status": "broken"}
                mbt.append(x)
            m["must_be_true"] = mbt
        fails = [msg for ok, msg in rules.RED_LINES[a] if not ok(m)]
        mine = [c for c in cl if c["role"] == a]
        args = [c for c in mine if c["where"].startswith("arguments")]
        bad = [c for c in args if c["verdict"] in ("unsupported", "contradicted")]
        verify_fail = bool(args) and len(bad) / len(args) >= rules.VERIFY_FAIL
        warn += rules.soft(a, m)
        warn += [f"{c['where']} {c['verdict']}: {c['reason'] or c['point'][:40]}" for c in mine
                 if c["verdict"] in ("unsupported", "contradicted", "leap")]
        warn += [c["warn"] for c in mine if c["warn"]]
        if o["round"] == 2:
            told = {x.get("to") for x in o.get("rebuttals", [])}
            need = [b for b in core.AGENTS if b != a and b in ops] + (["redteam"] if redteam else [])
            warn += [f"{core.ROLES[b]}에 대한 반론 없음" for b in need if b not in told]
            warn += stale(d, "2라운드", core.load(d / f"{a}.2.json"), "model")
        tb = breaks(fx, o["thesis_breaks"], core.AGENTS[a])
        if not any(b["metric"] for b in tb):
            warn.append("기계로 판정할 수 있는 반증 조건(thesis_breaks의 metric·op·value) 없음")
        warn += [f"반증 조건이 이미 충족됨: {b['note'] or b['metric']} (실제 {b['actual']:g})" for b in tb if b["status"].startswith("충족")]
        r["breaks"] += tb
        final, override = stance, None
        if stance == "for" and fails:
            final, override = "against", "redline"
        elif verify_fail and stance != "abstain":
            final, override = "abstain", "verify"
        rows.append(dict(agent=a, name=core.AGENTS[a], opening=o["opening"], stance=stance, final=final, override=override,
                         conviction=min(max(int(o.get("conviction", 3)), 1), 5), red_lines=fails, warnings=warn, metrics=m,
                         verify=dict(total=len(args), failed=len(bad)), opinion=o))
    r["breaks"] += breaks(fx, [p["signal"] for p in items(redteam.get("premortem"), "point") if isinstance(p.get("signal"), dict)], "레드팀")
    r["kpis"] = kpis(fx, model)
    w = {x["agent"]: rules.WEIGHTS[x["agent"]] / sum(rules.WEIGHTS[y["agent"]] for y in rows) for x in rows}
    tally = sum(w[x["agent"]] * core.STANCE[x["final"]][1] for x in rows)
    verdict = "FOR" if tally > 1e-9 else "AGAINST" if tally < -1e-9 else "SPLIT"
    word = {"FOR": "찬성", "AGAINST": "반대", "SPLIT": "보류"}[verdict]
    label = f"만장일치 {word}" if len({x["final"] for x in rows}) == 1 else "팽팽" if verdict == "SPLIT" else f"{word} 우세"
    r.update(verdict=verdict, label=label, agents=rows, votes={k: sum(x["final"] == k for x in rows) for k in core.STANCE},
             score=round(sum(w[x["agent"]] * core.STANCE[x["final"]][1] * x["conviction"] / 5 for x in rows), 2), ok=verdict == "FOR")
    r["sizing"] = sizing(r, an, rows)
    r["user_view"] = contrast(d, r)
    return r


def mechanical(c, fx, ref, everything, allowed, pct=None):
    """기계 대조 → (실패 이유 | None, 경고 | None).
    실패: 인용 없음 · 없는 근거 · 기준일 이후 근거 · 어디에도 없는 숫자(출처 없는 숫자).
    경고: 근거에는 있지만 인용하지 않은 숫자 — 그 숫자가 있는 ID를 알려 준다."""
    if not c["cites"]:
        return "인용 없음", None
    bad = [x for x in c["cites"] if not facts.CITE.match(str(x)) or not (x in fx.src or x in fx.facts or x in ref)]
    if bad:
        return f"없는 근거 인용: {', '.join(map(str, bad))}", None
    if late := [x for x in c["cites"] if x in fx.future]:
        return f"기준일 이후 근거 인용: {', '.join(late)}", None
    cited = facts.pool([fx.src[x] for x in c["cites"] if x in fx.src], [fx.facts[x] for x in c["cites"] if x in fx.facts],
                       {x: ref[x] for x in c["cites"] if x in ref}, pct)
    miss = facts.trace(c["point"], cited, everything, allowed)
    orphan = [n for n, w in miss if not w]
    elsewhere = [f"{n}({'·'.join(w[:3])})" for n, w in miss if w]
    return (f"출처 없는 숫자 {', '.join(orphan)} — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)" if orphan else None,
            f"{c['where']}: 인용하지 않은 근거의 숫자 {', '.join(elsewhere)} — cites에 추가" if elsewhere else None)


def kpis(fx, model):
    out = []
    for i, k in enumerate(model.get("kpis") or [], 1):
        if not (isinstance(k, dict) and k.get("metric") and k.get("period") and k.get("op") in OPS and isinstance(k.get("value"), (int, float))
                and isinstance(k.get("p"), (int, float)) and 0 < k["p"] < 1):
            continue
        hit, actual = status(fx, k)
        out.append(dict(id=f"K{i}", **{x: k.get(x) for x in ("metric", "period", "op", "value", "p", "why")},
                        actual=actual, status="대기" if hit is None else "적중" if hit else "빗나감"))
    return out


def sizing(r, an, rows):
    """비중 참고값 — 요구수익률(할인율)을 넘는 초과수익에 1/4 켈리. 최종 비중은 사람이 정한다."""
    sw = next((x["metrics"].get("starter_weight") for x in rows if x["agent"] == "slater"), None)
    v = an["valuation"]
    e, hurdle = v["expected"], (1 + v["discount_rate"]) ** v["years"] - 1
    if r["verdict"] != "FOR":
        return dict(suggested=0.0, why=f"{r['label']} — 신규 비중 없음", starter_weight=sw)
    excess = e["mean_return"] - hurdle
    if excess <= 0 or e["variance"] <= 0:
        return dict(suggested=0.0, starter_weight=sw,
                    why=f"확률 가중 기대 연 수익률 {e['irr']:+.1%}가 요구수익률 {v['discount_rate']:.0%} 이하 — 찬성이어도 가격이 보상하지 않는다")
    f = min(rules.KELLY * excess / e["variance"], rules.MAX_WEIGHT)
    return dict(suggested=f, starter_weight=sw,
                why=f"{rules.KELLY:g} 켈리 — {v['years']}년 초과수익 {excess:+.0%}(요구수익률 {v['discount_rate']:.0%} 차감), 분산 {e['variance']:.2f}, 상한 {rules.MAX_WEIGHT:.0%}")


def contrast(d, r):
    """사용자 견해는 분석이 끝난 뒤에만 꺼내 비교한다. 어떤 프롬프트에도 들어가지 않는다."""
    uv = core.load(d / "view.json", {})
    if not uv:
        return None
    lines = []
    word = {"for": "찬성", "against": "반대", "abstain": "보류"}
    if uv.get("stance") in word:
        same = (uv["stance"] == "for") == (r["verdict"] == "FOR")
        lines.append(f"사용자 {word[uv['stance']]} vs 하네스 {r['label']} — {'일치' if same else '불일치: 하네스 근거를 먼저 읽는다'}")
    v = (r["analysis"].get("valuation") or {}).get("expected")
    if isinstance(uv.get("expected_return"), (int, float)) and v:
        gap = uv["expected_return"] - v["irr"]
        lines.append(f"사용자 기대 연 수익률 {uv['expected_return']:+.0%} vs 모델 확률 가중 {v['irr']:+.1%}"
                     + (" — 차이가 크다: 확증 편향 점검" if abs(gap) >= 0.10 else ""))
    lines += [f"사용자 주장 (하네스가 검증하지 않음): {c}" for c in uv.get("claims", [])]
    return dict(lines=lines, view=uv)

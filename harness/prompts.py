"""프롬프트 — 역할마다 볼 수 있는 것만 넣는다 (정보 차단).

대화형 CLI·서브에이전트·헤드리스 실행이 모두 이 함수가 만든 같은 텍스트를 쓴다.
사용자 견해(view.json)는 어떤 프롬프트에도 들어가지 않는다 — 아첨을 구조적으로 막는다.
"""
import hashlib, json
from . import calc, core, facts, report

TASK = {
    "researcher": "아래 evidence에 보강할 것만 JSON 객체 하나로 출력하라: {\"sources\": [...], \"facts\": [...], \"drop\": [...], \"gaps\": [...]}.",
    "business": "사업·단위경제·산업 구조·해자를 분석하고 스키마의 JSON 객체 하나만 출력하라.",
    "management": "경영진·보상·자본배분·가이던스 신뢰도를 분석하고 스키마의 JSON 객체 하나만 출력하라.",
    "forensic": "회계 품질을 판정하라. 코드 신호(flags)를 하나도 빠짐없이 해명하고 스키마의 JSON 객체 하나만 출력하라.",
    "modeler": "드라이버·시나리오 가정·variant perception·KPI를 제안하라. 계산은 코드가 한다. 스키마의 JSON 객체 하나만 출력하라.",
    "redteam": "이 종목이 5년 뒤 −60%가 되었다고 가정하고 사전 부검을 써라. 스키마의 JSON 객체 하나만 출력하라.",
    "verifier": "아래 주장 하나하나를 그 주장이 인용한 자료만으로 판정하라. 스키마의 JSON 객체 하나만 출력하라.",
}


KIND = {  # 검증자에게 주장의 종류만 알려 준다 — 누가 썼는지·입장은 가린 채
    "premortem": "사전 부검 — '5년 뒤 −60%가 되었다'고 가정한 가상 시나리오", "scenarios": "시나리오 가정과 그 근거",
    "rebuttals": "반론 — 다른 분석가의 주장을 언급할 수 있다", "variant": "시장과 다르게 보는 점과 그 근거",
    "weakest": "모델 가정 비판"}


def block(title, obj):
    return f"## {title}\n```json\n{json.dumps(obj, ensure_ascii=False, indent=1)}\n```"


def previous(d, role):  # 판단 로그(L7)에서 이 역할이 알아야 할 직전 판단 — 증분 갱신용
    from .journal import entries
    js = [e for e in entries(d) if e["type"] == "judgment"]
    if not js:
        return None
    j, ups = js[-1], [e for e in entries(d) if e["type"] == "update" and e["date"] >= js[-1]["date"]]
    status = ups[-1]["status"] if ups else None
    if role == "modeler":
        return dict(date=j["date"], verdict=j["label"], kpis=j.get("kpis"), projection=j.get("projection"),
                    update=ups[-1] if ups else None)
    if role in core.AGENTS:
        a = j["agents"].get(role, {})
        return dict(date=j["date"], stance=a.get("stance"), final=a.get("final"), conviction=a.get("conviction"),
                    thesis_breaks=[b for b in j.get("breaks", []) if b.get("who") == core.AGENTS[role]], update_status=status)
    return None


def prompt(role, d, rnd=1):
    ev, model = core.load(d / "evidence.json"), core.load(d / "model.json", {})
    fx = facts.Facts(ev)
    mods = {m: core.load(d / f"{m}.json", {}) for m in core.MODULES}
    head = (f"<!-- council role={role} round={rnd} -->\ncouncil.py가 보낸 단일 역할 작업이다. 진행자 워크플로(AGENTS.md)를 "
            "돌리거나 파일을 만들지 말고, 아래 역할로서 JSON만 답하라.")
    if role == "verifier":
        cl, key = claims(d)
        return "\n\n".join([head, core.doc("verifier"), f"## 지금 할 일\n{TASK[role]}\nbasis: `{key}` — 출력의 \"basis\"에 그대로 적는다.",
                            "## 검증할 주장", verifier_view(d, cl, ev, fx)])
    if role == "researcher":
        an = calc.analyze(ev)
        todo = calc.sufficiency(ev, an) + an["warnings"]
        return "\n\n".join([head, core.doc("researcher"), f"## 지금 할 일\n{TASK[role]}",
                            "## 지금 비어 있는 것 (코드 점검)\n" + "\n".join(f"- {t}" for t in todo or ["없음"]),
                            f"## evidence — {ev.get('name')} ({ev.get('ticker')}) · 기준일 {ev.get('as_of')}\n" + report.evidence_md(ev, fx, urls=True)])
    stage = core.STAGE[role]
    key = core.basis(d, stage)
    parts = [head]
    if role in core.AGENTS:
        parts += [core.doc("debate"), core.doc(role), f"## 지금 할 일\n너는 {core.AGENTS[role]}이다. {rnd}라운드를 수행하고 "
                                                      f"그 라운드 스키마의 JSON 객체 하나만 출력하라."]
    else:
        parts += [core.doc(role), f"## 지금 할 일\n{TASK[role]}"]
    parts[-1] += f"\nbasis: `{key}` — 출력의 \"basis\"에 그대로 적는다."
    an = calc.analyze(ev, model if stage == "model" else None)
    parts += [f"## evidence — {ev.get('name')} ({ev.get('ticker')}) · 기준일 {ev.get('as_of')}\n" + report.evidence_md(ev, fx),
              "## 코드 계산값 (L3 — 숫자는 여기서 가져오고 C:키로 인용한다)\n" + report.analysis_md(an, valuation=stage == "model")]
    if stage in ("modules", "model"):  # 모듈 결과는 모델러·페르소나·레드팀만 본다. 모듈끼리는 서로 모른다
        parts += [block(f"{core.MODULES[m]} 분석 ({m}.json)", o) for m, o in mods.items() if o]
    if stage == "model":
        parts.append(block("모델 가정 (model.json)", model))
    if role in core.AGENTS and rnd == 2:  # 반론 라운드에서만 다른 페르소나의 1라운드와 레드팀을 본다
        parts += [block(f"{core.AGENTS[a]}의 1라운드{' (너 자신)' if a == role else ''}", core.load(d / f"{a}.1.json")) for a in core.AGENTS]
        if (d / "redteam.json").exists():
            parts.append(block("레드팀 사전 부검 (redteam.json)", core.load(d / "redteam.json")))
    prev = previous(d, role) if rnd == 1 else None
    if prev:
        parts.append(block("직전 판단 (판단 로그) — 얽매이지 말고, 달라졌다면 change_reason에 새 근거 ID로 이유를 쓴다", prev))
    return "\n\n".join(parts)


# ── 검증 대상 주장: 작성자·입장을 지우고 내용 해시 순으로 섞는다 ──

def claims(d):
    out = []

    def add(role, where, point, cites):
        if point:
            out.append(dict(role=role, where=where, point=str(point), kind=KIND.get(where.split("[")[0].split(".")[0], ""),
                            cites=[str(c) for c in cites or []] if isinstance(cites, list) else []))

    def each(o, k):  # 객체 대신 문자열이 와도 주장으로 받는다 (인용이 없으니 검증에서 실패한다)
        return enumerate(x if isinstance(x, dict) else {"point": str(x)} for x in (o.get(k) or []))
    for m in core.MODULES:
        o = core.load(d / f"{m}.json", {})
        for k in ("findings", "flags", "moat"):
            for i, x in each(o, k):
                add(m, f"{k}[{i}]", x.get("point"), x.get("cites"))
    mo = core.load(d / "model.json", {})
    for k, s in (mo.get("scenarios") or {}).items():
        if isinstance(s, dict):
            add("modeler", f"scenarios.{k}", s.get("rationale"), s.get("cites"))
    vp = mo.get("variant") if isinstance(mo.get("variant"), dict) else {}
    add("modeler", "variant", " — ".join(x for x in (vp.get("ours"), vp.get("why")) if x), vp.get("cites"))
    for a in core.AGENTS:
        for rnd, keys in ((1, ("arguments", "risks")), (2, ("rebuttals",))):
            o = core.load(d / f"{a}.{rnd}.json", {})
            for k in keys:
                for i, x in each(o, k):
                    add(a, f"{k}[{i}]", x.get("point"), x.get("cites"))
    rt = core.load(d / "redteam.json", {})
    for k in ("premortem", "weakest"):
        for i, x in each(rt, k):
            add("redteam", f"{k}[{i}]", x.get("point"), x.get("cites"))
    out.sort(key=lambda c: hashlib.sha256((c["point"] + c["role"] + c["where"]).encode("utf-8")).hexdigest())
    for i, c in enumerate(out, 1):
        c["id"] = f"V{i}"
    return out, core.digest([(c["point"], c["cites"]) for c in out])


def cited(c, ev, fx, ref):  # 주장이 인용한 자료의 내용
    src = {s["id"]: s for s in ev.get("sources", [])}
    lines = []
    for x in c["cites"]:
        if x in src:
            s = src[x]
            lines.append(f"- {x} [{s['type']}] {s.get('title', '')} ({s.get('date', '')}): {s.get('note', '')}")
        elif x in fx.facts:
            f = fx.facts[x]
            lines.append(f"- {x} {f['metric']} {f.get('period') or f['end']} = {f['value']:g} {f['unit']} ({f['basis']}, {f['source']})")
        elif x in ref:
            lines.append(f"- {x} = {ref[x]:.6g} (코드 계산)")
        else:
            lines.append(f"- {x}: (존재하지 않는 근거)")
    return "\n".join(lines) or "- (인용 없음)"


def verifier_view(d, cl, ev, fx):
    ref = calc.analyze(ev, core.load(d / "model.json", {}) or None)["ref"]
    return "\n\n".join(f"### {c['id']}\n주장: {c['point']}\n" + (f"유형: {c['kind']}\n" if c.get("kind") else "")
                       + f"인용:\n{cited(c, ev, fx, ref)}" for c in cl)

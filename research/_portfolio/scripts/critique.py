"""의장 투자 철학 비평 라운드 — 네 페르소나 + 레드팀이 서로 보지 않고 각자 별도 프로세스에서 비평한다.
숫자는 코드 계산값(하네스 판정·v4 비중 라운드)만 쓴다. 종목에 대한 의장 견해(view.json)는 넣지 않는다.
사용: python3 -I critique.py AGENT  →  research/_portfolio/philosophy/critique.<agent>.json"""
import sys, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from harness import core, judge, pipeline

a = sys.argv[1]
NAME = {**core.AGENTS, "redteam": "레드팀"}
PH = ROOT / "research/_portfolio/philosophy"
V4 = ROOT / "research/_portfolio/v4"
R = json.loads((V4 / "risk.json").read_text())
C = json.loads((V4 / "committee.json").read_text())
T = ["UBER", "MELI", "CRDO", "NVDA", "SHOP", "AMZN", "PLTR", "IOT", "CBRS", "PONY"]
K = {"for": "찬", "against": "반", "abstain": "보", "conditional": "조"}
money = lambda v: "—" if v is None else f"{v:,.2f}"
pct = lambda v: "—" if v is None else f"{v:+.1%}"


def checklist(t):  # 종목 탭 원고의 매수 전 10문항 판정
    s = (ROOT / f"research/_deep/tabs4/{t}.md").read_text(encoding="utf-8")
    part = s[s.find("매수 전 10문항"):s.find("### 출처")]
    out = []
    for line in part.splitlines():
        cells = [c.strip().strip("*") for c in line.split("|")]
        if len(cells) > 3 and re.match(r"\d+", cells[1]):
            v = cells[2] if re.search("예|아니오|보류", cells[2]) else cells[3]
            out.append("예" if v.startswith("예") else "아니오" if "아니오" in v else "보류")
    no = [str(i + 1) for i, v in enumerate(out) if v == "아니오"]
    return f"예{out.count('예')}·아니오{len(no)}·보류{out.count('보류')}" + (f" (아니오: {','.join(no)}번)" if no else "")


rows = ["| 종목 | 4인 판정 (앤·슬·애·클 최종 표) | 위원회 비중 | 주가 | 확률가중 IV | 기대 연수익(5년) | 손실 확률 | 1/4 켈리 | 앤더슨 10년 배수 | 5년 매출 배수 | 최근 ROIC | 최근 FCF 마진 | SBC/매출 | 순부채/EBITDA | 클라만: 단단한 가치까지 하락폭 · 조건 가격 | 1년 변동성 | 체크리스트 |",
        "|" + "---|" * 17]
for t in T:
    r = judge.judge(core.folder(t)); an = r["analysis"]; v = (an.get("valuation") or {}).get("expected") or {}
    ag = {x["agent"]: x for x in r["agents"]}; m = an.get("market") or {}
    hist = [h for h in an.get("history") or [] if h.get("period", "").startswith("FY") and "Q" not in h.get("period", "") and "H" not in h.get("period", "")]
    last = hist[-1] if hist else {}
    km, am = ag["klarman"]["metrics"], ag["anderson"]["metrics"]
    f = lambda x, p=True: "—" if x is None else (f"{x:.1%}" if p else f"{x:.2f}")
    rows.append(f"| {t} | {r['label']} ({' '.join(K[ag[x]['final']] for x in core.AGENTS)}) | {C['committee']['w'][t]:.1f}% | {money(m.get('price'))} | {money(v.get('iv'))} | {pct(v.get('irr'))} | "
                f"{v.get('p_loss', 0):.0%} | {(r.get('sizing') or {}).get('suggested', 0):.1%} | {f(am.get('upside_10y'), False)}배 | {f(am.get('revenue_5y'), False)}배 | "
                f"{f(last.get('roic'))} ({last.get('period', '—')}) | {f(last.get('fcf_margin'))} | {f(last.get('sbc_to_revenue'))} | {f(m.get('net_debt_to_ebitda'), False)} | "
                f"{f(km.get('downside'))} · {money(km.get('buy_below'))} | {R['vol'][t]:.0%} | {checklist(t)} |")
cm = C["committee"]
facts = f"""- 위원회안(SCHD 40% + 10종목 60%) 1년 변동성 {cm['vol']:.1%}, SCHD 단독 {R['vol']['SCHD']:.0%}. SCHD 위험 기여 {cm['rc']['SCHD']:.1%}.
- 하네스 기대 연수익이 요구수익률 10% 미만인 종목에 {cm['below_req']:.1f}% (주가 > 확률가중 IV: AMZN·SHOP·PLTR·IOT·CBRS·PONY). 기대 연수익 12% 이상은 UBER·MELI 둘, 1/4 켈리 참고값이 양수인 것은 UBER·MELI·CRDO·NVDA 넷.
- 묶음: AI 하드웨어(NVDA·CRDO·CBRS) {cm['groups']['ai_hw']['w']:.1f}%(위험 {cm['groups']['ai_hw']['rc']:.0%}), AI 자본조달(+AMZN) {cm['groups']['ai_capex']['w']:.1f}%(위험 {cm['groups']['ai_capex']['rc']:.0%}), 자율주행(UBER·PONY) {cm['groups']['av']['w']:.1f}%, 커머스·신용(MELI·SHOP) {cm['groups']['commerce']['w']:.1f}%.
- 체크리스트에서 '아니오'가 하나도 없는 종목은 UBER·MELI·NVDA 셋뿐이다(위 표). 의장 규칙은 '하나라도 아니오면 매수하지 않는다'다.
- 하락폭이 음수면 단단한 가치가 주가보다 높다는 뜻이다(MELI). 주의: MELI의 FCF 마진·단단한 가치는 고객 자금이 섞인 GAAP 영업현금흐름 기준이라 부풀려져 있다(회사 조정 FCF는 2026 상반기 1.58억 달러). PLTR ROIC는 투하자본이 작아 왜곡된 값이다. NVDA 순현금은 단기 투자 누락으로 낮게 잡혔다.
- 하네스 판정은 실행마다 흔들렸다: AMZN 앤더슨 10년 배수 4.83 → 5.47 → 4.90배(5배 선을 넘나듦), CBRS 확률가중 IV 42.84 → 65.66."""

philosophy = (PH / "chair_2026-10-18.md").read_text(encoding="utf-8")
ask_persona = """너의 철학(위 페르소나 정의)의 관점에서 의장의 투자 철학을 비평한다. 칭찬보다 쓸모 있는 반론이 목적이다.
- 의장 철학의 문장을 직접 인용하며 동의하는 것과 동의하지 않는 것을 가른다. 동의할 때도 조건을 붙여라.
- 철학 안의 긴장·모순, 의장이 앞서 밝힌 규칙(체크리스트·12% 허들·10년 4배·가격 원칙)과의 충돌, 빠진 것(매도 규율, 비중 결정, 분류 기준 등)을 찾는다.
- 이 철학을 지금 포트폴리오에 적용하면 무엇이 드러나는지 아래 표의 숫자로 보인다. 표에 없는 숫자를 새로 계산하거나 지어내지 않는다.
- 너 자신의 철학이 의장보다 약한 지점이 있으면 그것도 한 줄 인정한다.
- 철학을 더 날카롭게 만들 구체적 수정 문구(규칙)를 제안한다 — 측정 가능한 문턱이 있으면 좋다."""
ask_redteam = """투자 의견은 쓰지 않는다. **의장이 이 철학을 10년 동안 충실히 따랐는데 결과가 SCHD 단독보다 크게 나빴다**고 가정하고, 가장 그럴듯한 이유를 메커니즘으로 쓴다.
- 서로 다른 실패 경로 3~4개. 각각 그 일이 시작되었다면 먼저 움직였을 숫자(선행 신호)와, 철학 문장 중 그 실패를 허용한 구절을 함께 쓴다.
- 이 철학의 판단 단계 중 가장 약한 고리(예: 두 분류 사이의 경계, '제값'의 정의, '증거가 쌓일수록 늘린다')를 지목한다.
- 아래 표의 숫자만 쓴다. 표에 없는 숫자를 지어내지 않는다."""
schema = f"""다음 JSON 객체 하나만 출력한다(한국어):
{{"agent": "{a}", "one_line": "한 줄 총평",
  "agree": [{{"quote": "의장 철학 인용", "why": "왜 동의하는가 + 조건"}}],
  "disagree": [{{"quote": "의장 철학 인용", "why": "왜 동의하지 않는가", "evidence": "근거(표의 숫자·사례)"}}],
  "tensions": [{{"between": "충돌하는 두 원칙/규칙", "why": "어떻게 충돌하는가"}}],
  "missing": ["빠진 것"],
  "portfolio_check": [{{"subject": "종목·묶음", "finding": "이 철학을 적용하면 드러나는 것(표의 숫자로)"}}],
  "own_weakness": "너 자신의 철학이 의장보다 약한 지점 한 줄",
  "amendments": [{{"rule": "제안하는 규칙 문구", "why": "이유"}}],
  "failure_paths": [{{"path": "(레드팀만) 실패 경로와 메커니즘", "signal": "선행 신호", "allowed_by": "그 실패를 허용한 철학 구절"}}],
  "weakest_link": "(레드팀만) 가장 약한 고리",
  "question_for_chair": "의장에게 묻는 질문 하나"}}
레드팀이 아니면 failure_paths·weakest_link는 비워 둔다. 레드팀은 agree·disagree를 비워도 된다. 각 목록 2~5개, 항목마다 1~3문장."""
text = "\n\n".join([
    f"<!-- council role={a} round=critique -->\ncouncil.py가 보낸 단일 역할 작업이다. 진행자 워크플로를 돌리거나 파일을 만들지 말고, 아래 역할로서 JSON만 답하라.",
    "## 너의 페르소나 정의 (종목 판정용 출력 형식·metrics·case 절은 이번 과제와 무관하다)\n\n" + core.doc(a),
    "## 지금 할 일 — 의장 투자 철학 비평\n\n" + (ask_redteam if a == "redteam" else ask_persona),
    "## 의장의 투자 철학 (원문)\n\n" + philosophy,
    "## 지금 포트폴리오 — 코드 계산값 (2026-10-16 종가, 하네스 4인 판정과 비중 라운드)\n\n" + "\n".join(rows) + "\n\n" + facts,
    schema])
(PH / f"prompt.{a}.md").write_text(text, encoding="utf-8")
for attempt in (1, 2):
    out = pipeline.call("claude -p", text if attempt == 1 else text + "\n\n## 이전 출력의 문제\nJSON 형식이 아니었다. 위 스키마의 JSON 객체 하나만 다시 출력하라.")
    if isinstance(out, dict) and out.get("one_line"):
        break
out["agent"] = a
(PH / f"critique.{a}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(a, out.get("one_line"))

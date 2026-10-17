"""비중 라운드 — 의장이 고른 9종목을 SCHD 40%와 조합할 때, 각 페르소나가 별도 프로세스로 60% 주식 슬리브 배분안을 낸다.
숫자는 코드가 계산한 값(risk.json)만 쓴다. 사용: python3 -I sizing.py AGENT"""
import sys, json
sys.path.insert(0, "/home/claude/choijaehyeok92-bit/andersonxslaterxackman")
from harness import core, pipeline

a = sys.argv[1]
S = "/tmp/claude-0/-home-claude/0ad0b3ce-a0a5-5165-a749-6f1797b3b26d/scratchpad"
R = json.load(open("/home/claude/choijaehyeok92-bit/andersonxslaterxackman/research/_portfolio/risk.json"))
T = ["UBER", "MELI", "NVDA", "AMZN", "CRDO", "PLTR", "CBRS", "SHOP", "IOT"]
K = {"for": "찬성", "against": "반대", "abstain": "보류"}
rows = ["| 종목 | 하네스 판정 | 너의 최종 표(확신) | 레드라인 | 주가 | 확률가중 IV | 기대 연수익(5년) | 손실 확률 | 하네스 1/4 켈리 참고 | 1년 변동성 | NVDA 상관 | SCHD 상관 |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|"]
theses = []
for t in T:
    h = R["harness"][t]; me = h["agents"][a]
    rows.append(f"| {t} | {h['label']} (찬{h['votes']['for']}·반{h['votes']['against']}·보{h['votes']['abstain']}) | {K[me['final']]} ({me['conviction']}) | {', '.join(me['red_lines']) or '없음'} | {h['price']} | "
                f"{h['iv']:.2f} | {h['irr']:+.1%} | {h['p_loss']:.0%} | {h['kelly_ref']:.1%} | {R['vol'][t]:.0%}"
                f"{' (상장 후 ' + str(R['n'][t]) + '거래일)' if R['n'][t] < 200 else ''} | {R['corr'][t + '-NVDA']:.2f} | {R['corr'][t + '-SCHD']:.2f} |")
    o1 = core.load(core.folder(t) / f"{a}.1.json", {})
    theses.append(f"- **{t}**: {(o1.get('thesis') or '')[:420]}")
corr = ", ".join(f"{x}-{y} {R['corr'][x + '-' + y]:.2f}" for x, y in [("NVDA", "CRDO"), ("NVDA", "CBRS"), ("CRDO", "CBRS"), ("PLTR", "SHOP"), ("UBER", "MELI"), ("AMZN", "SHOP")])
text = "\n\n".join([
    f"<!-- council role={a} round=sizing -->\ncouncil.py가 보낸 단일 역할 작업이다. 진행자 워크플로를 돌리거나 파일을 만들지 말고, 아래 역할로서 JSON만 답하라.",
    core.doc(a),
    f"""## 지금 할 일 — 비중 라운드 (판정 이후)

투자위원회 의장이 토의를 마치고 '확신을 갖고 담을 수 있는' 9종목을 골랐다: {', '.join(T)}.
의장은 전체 포트폴리오를 **SCHD 40% + 이 9종목 60%**로 구성하려 한다. 너는 {core.AGENTS[a]}로서 60% 주식 슬리브의 종목별 비중(전체 포트폴리오 대비 %)을 제안한다.

규칙:
- 너의 철학과 너의 기존 판단(아래 표의 네 표·확신·레드라인)에 충실하라. 의장이 골랐다고 해서 확신이 없는 종목에 큰 비중을 주지 않는다. 너의 기준으로 담지 않을 종목은 0~1%의 관찰 비중을 줄 수 있다.
- 9종목 비중의 합은 정확히 60.0%여야 한다. 한 종목은 15% 이하.
- 네가 보기에 60%를 다 주식에 쓰는 것이 맞지 않다면, 그 생각은 `would_rather`에 적되(예: "X%는 SCHD나 현금이 낫다") 비중 합은 60%로 맞춘다.
- 숫자는 아래 표(코드 계산값)만 쓴다. 새로 계산한 값을 사실처럼 쓰지 않는다. 변동성·상관을 비중에 반영하라(특히 같은 AI 하드웨어 묶음 NVDA·CRDO·CBRS의 상관).
- 한국어로, 종목별 이유는 1~2문장.

## 코드 계산값 (2026-10-16 종가 기준, 변동성·상관은 최근 1년 일간 수익률)
""" + "\n".join(rows) + f"\n\n주요 상관: {corr}. SCHD 1년 변동성 {R['vol']['SCHD']:.0%}.\n\n## 너의 1라운드 논지 요약\n" + "\n".join(theses),
    f"""다음 JSON 객체 하나만 출력한다:
{{"agent": "{a}", "weights": {{"UBER": 0.0, "MELI": 0.0, "NVDA": 0.0, "AMZN": 0.0, "CRDO": 0.0, "PLTR": 0.0, "CBRS": 0.0, "SHOP": 0.0, "IOT": 0.0}},
  "reasons": {{"UBER": "...", "...": "..."}}, "tiers": {{"핵심": [...], "주력": [...], "관찰": [...]}},
  "would_rather": "60%를 다 주식에 쓰는 것에 대한 의견 한두 문장", "portfolio_note": "포트폴리오 전체 위험에 대한 한두 문장",
  "trim_rules": ["비중을 줄일 구체적 조건 2~3개"]}}"""])
for attempt in (1, 2):
    out = pipeline.call("claude -p", text if attempt == 1 else text + "\n\n## 이전 출력의 문제\n비중 합이 60.0이 아니거나 형식이 틀렸다. 다시 출력하라.")
    w = out.get("weights") or {}
    if set(w) == set(T) and abs(sum(w.values()) - 60) < 0.05 and max(w.values()) <= 15.0001:
        break
out["agent"] = a
core.save(core.ROOT / "research" / "_portfolio" / f"sizing.{a}.json", out)
print(a, {k: round(v, 1) for k, v in out["weights"].items()}, round(sum(out["weights"].values()), 2))

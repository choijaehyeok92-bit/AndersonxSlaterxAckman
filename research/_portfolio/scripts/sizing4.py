"""비중 라운드(4인) — 의장의 9종목 + PONY를 SCHD 40%와 조합. 페르소나마다 별도 프로세스로 60% 주식 슬리브 배분안과
조건 가격(buy_below)에서의 단계적 추가 계획을 낸다. 숫자는 코드 계산값(v4/risk.json)만 쓴다. 사용: python3 -I sizing4.py AGENT"""
import sys, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from harness import core, pipeline

a = sys.argv[1]
V4 = ROOT / "research/_portfolio/v4"
R = json.loads((V4 / "risk.json").read_text())
T = ["UBER", "MELI", "CRDO", "NVDA", "SHOP", "AMZN", "PLTR", "IOT", "CBRS", "PONY"]
K = {"for": "찬성", "against": "반대", "abstain": "보류", "conditional": "조건부 찬성"}
money = lambda v: "—" if v is None else f"{v:,.2f}"
rows = ["| 종목 | 위원회 판정(4인) | 너의 입장 → 집계된 표(확신) | 너의 레드라인 위반 | 너의 조건 가격 | 주가 | 확률가중 IV | 기대 연수익(5년) | 손실 확률 | 1/4 켈리 참고 | 1년 변동성 | NVDA 상관 | SCHD 상관 |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
theses, ladders = [], []
for t in T:
    h = R["harness"][t]; me = h["agents"][a]
    rows.append(f"| {t} | {h['label']} (찬{h['votes']['for']}·반{h['votes']['against']}·보{h['votes']['abstain']}) | {K[me['stance']]} → {K[me['final']]} ({me['conviction']}) | "
                f"{', '.join(me['red_lines']) or '없음'} | {money(me['buy_below'])} | {h['price']} | {money(h['iv'])} | {h['irr']:+.1%} | {h['p_loss']:.0%} | {h['kelly_ref']:.1%} | "
                f"{R['vol'][t]:.0%}{' (상장 후 ' + str(R['n'][t]) + '거래일)' if R['n'][t] < 200 else ''} | {R['corr'][t + '-NVDA']:.2f} | {R['corr'][t + '-SCHD']:.2f} |")
    if len(h["ladder"]) > 1:
        ladders.append(f"- {t}: " + " → ".join(f"{money(s['price'])} {s['label']}" + (f"({', '.join(s['who'])})" if s["who"] else "") for s in h["ladder"]))
    o1 = core.load(core.folder(t) / f"{a}.1.json", {})
    theses.append(f"- **{t}**: {(o1.get('thesis') or '')[:420]}")
pairs = [("NVDA", "CRDO"), ("NVDA", "CBRS"), ("CRDO", "CBRS"), ("NVDA", "PONY"), ("UBER", "PONY"), ("PLTR", "SHOP"), ("UBER", "MELI"), ("AMZN", "SHOP")]
corr = ", ".join(f"{x}-{y} {R['corr'][x + '-' + y]:.2f}" for x, y in pairs)
text = "\n\n".join([
    f"<!-- council role={a} round=sizing -->\ncouncil.py가 보낸 단일 역할 작업이다. 진행자 워크플로를 돌리거나 파일을 만들지 말고, 아래 역할로서 JSON만 답하라.",
    core.doc(a),
    f"""## 지금 할 일 — 비중 라운드 (4인 판정 이후)

투자위원회 의장이 토의를 마치고 '확신을 갖고 담을 수 있는' 9종목(UBER·MELI·CRDO·NVDA·SHOP·AMZN·PLTR·IOT·CBRS)을 골랐고, 여기에 PONY를 추가해 10종목으로 비중을 정하려 한다.
의장은 전체 포트폴리오를 **SCHD 40% + 이 10종목 60%**로 구성하려 한다. 위원회는 이제 4인(앤더슨·슬레이터·애크먼·클라만)이다.
너는 {core.AGENTS[a]}로서 60% 주식 슬리브의 종목별 비중(전체 포트폴리오 대비 %)을 제안한다.

규칙:
- 너의 철학과 너의 기존 판단(아래 표의 입장·표·확신·레드라인·조건 가격)에 충실하라. 의장이 골랐다고 해서 확신이 없는 종목에 큰 비중을 주지 않는다. 너의 기준으로 담지 않을 종목은 0~1%의 관찰 비중을 줄 수 있다.
- 10종목 비중의 합은 정확히 60.0%여야 한다. 한 종목은 15% 이하.
- 네가 보기에 60%를 다 주식에 쓰는 것이 맞지 않다면, 그 생각은 `would_rather`에 적되(예: "X%는 SCHD나 현금이 낫다") 비중 합은 60%로 맞춘다.
- `conditional_adds`: 주가가 조건 가격(너의 것이든 다른 위원의 것이든, 아래 표·사다리에 있는 값)까지 내려오면 비중을 늘리고 싶은 종목이 있으면 적는다 — 가격, 늘릴 비중(%p), 그 비중을 어디서 가져오는지(SCHD 또는 다른 종목). 없으면 빈 목록.
- 숫자는 아래 표(코드 계산값)만 쓴다. 새로 계산한 값을 사실처럼 쓰지 않는다. 변동성·상관을 비중에 반영하라(AI 하드웨어 NVDA·CRDO·CBRS, 자율주행 UBER·PONY의 상관과 논리적 연결 포함).
- 한국어로, 종목별 이유는 1~2문장.

## 코드 계산값 (2026-10-16 종가 기준, 변동성·상관은 최근 1년 일간 수익률)
""" + "\n".join(rows) + f"\n\n주요 상관: {corr}. SCHD 1년 변동성 {R['vol']['SCHD']:.0%}.\n\n## 조건부 사다리 — 주가가 위원의 조건 가격까지 내려오면 위원회 판정이 어떻게 바뀌는가 (코드 계산)\n" + "\n".join(ladders)
    + "\n\n## 너의 1라운드 논지 요약\n" + "\n".join(theses),
    f"""다음 JSON 객체 하나만 출력한다:
{{"agent": "{a}", "weights": {{{", ".join(f'"{t}": 0.0' for t in T)}}},
  "reasons": {{"UBER": "...", "...": "..."}}, "tiers": {{"핵심": [...], "주력": [...], "관찰": [...]}},
  "conditional_adds": [{{"ticker": "UBER", "price": 0.0, "add": 0.0, "from": "SCHD", "why": "..."}}],
  "would_rather": "60%를 다 주식에 쓰는 것에 대한 의견 한두 문장", "portfolio_note": "포트폴리오 전체 위험에 대한 한두 문장",
  "trim_rules": ["비중을 줄일 구체적 조건 2~3개"]}}"""])
for attempt in (1, 2):
    out = pipeline.call("claude -p", text if attempt == 1 else text + "\n\n## 이전 출력의 문제\n비중 합이 60.0이 아니거나 형식이 틀렸다. 다시 출력하라.")
    w = out.get("weights") or {}
    if set(w) == set(T) and abs(sum(w.values()) - 60) < 0.05 and max(w.values()) <= 15.0001:
        break
out["agent"] = a
(V4 / f"sizing.{a}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(a, {k: round(v, 1) for k, v in out["weights"].items()}, round(sum(out["weights"].values()), 2))

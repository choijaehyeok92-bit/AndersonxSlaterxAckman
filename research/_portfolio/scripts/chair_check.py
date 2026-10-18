"""의장 가격 원칙(2026-10-18) 점검 — '제값'은 분류에 따라 다르게 본다.
할인형은 안전마진, 아웃라이어형은 상방이 얼마나 열려 있는지. 숫자는 하네스 코드 계산값만 쓴다(시나리오별 10년 배수는 calc.persona로 다시 계산).
사용: python3 -I chair_check.py [TICKER …] → research/_portfolio/philosophy/chair_check[.<TICKERS>].json · .md
(종목을 주면 그 종목만 — 위원회 비중이 없는 새 종목은 비중 칸이 —)"""
import sys, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from harness import core, judge, calc

T = sys.argv[1:] or ["UBER", "MELI", "CRDO", "NVDA", "SHOP", "AMZN", "PLTR", "IOT", "CBRS", "PONY"]
SUF = "." + "_".join(T) if sys.argv[1:] else ""
C = json.loads((ROOT / "research/_portfolio/v4/committee.json").read_text())["committee"]["w"]
OUT = ROOT / "research/_portfolio/philosophy"
rows = []
for t in T:
    d = core.folder(t)
    r = judge.judge(d); an = r["analysis"]; v = an["valuation"]["expected"]; p = an["market"]["price"]
    model = core.load(d / "model.json", {})
    probs = {k: s.get("p") for k, s in (model.get("scenarios") or {}).items()}
    multi, rev5 = {}, {}
    for case in ("bear", "base", "bull"):
        a = calc.analyze(core.load(d / "evidence.json"), model, {"anderson": {"from": case}})
        pm = (a.get("personas") or {}).get("anderson") or {}
        multi[case], rev5[case] = pm.get("upside_10y"), pm.get("revenue_5y")
    pw = sum((probs.get(k) or 0) * (multi[k] or 0) for k in multi)
    ag = {x["agent"]: x for x in r["agents"]}
    rows.append(dict(ticker=t, weight=C.get(t), price=p, iv=v["iv"], mos_pw=1 - p / v["iv"], irr=v["irr"], p_loss=v["p_loss"],
                     mos_ackman=ag["ackman"]["metrics"].get("mos"), mos_klarman=ag["klarman"]["metrics"].get("mos"),
                     probs=probs, multiple_10y=multi, multiple_10y_pw=pw, revenue_5y=rev5,
                     fcf_positive=(an.get("market") or {}).get("fcf_positive")))
(OUT / f"chair_check{SUF}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1))
f = lambda x: "—" if x is None else f"{x:.2f}배"
pc = lambda x: "—" if x is None else f"{x:+.1%}"
L = ["| 종목 | 위원회 비중 | 주가 / 확률가중 IV | 안전마진(확률가중 IV 대비) | 애크먼·클라만 안전마진 | 기대 연수익 | 10년 배수 약세 · 기본 · 강세 (강세 확률) | 확률가중 10년 배수 | 5년 매출 배수 기본 · 강세 |",
     "|---|---|---|---|---|---|---|---|---|"]
for x in rows:
    m = x["multiple_10y"]
    L.append(f"| {x['ticker']} | {'—' if x['weight'] is None else format(x['weight'], '.1f') + '%'} | {x['price']:,.2f} / {x['iv']:,.2f} | {pc(x['mos_pw'])} | {pc(x['mos_ackman'])} · {pc(x['mos_klarman'])} | {pc(x['irr'])} | "
             f"{f(m['bear'])} · {f(m['base'])} · {f(m['bull'])} ({(x['probs'].get('bull') or 0):.0%}) | {f(x['multiple_10y_pw'])} | {f(x['revenue_5y']['base'])} · {f(x['revenue_5y']['bull'])} |")
(OUT / f"chair_check{SUF}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))

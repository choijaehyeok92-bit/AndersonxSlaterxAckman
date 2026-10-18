"""4인 위원회(클라만 포함) 실행 결과 요약 — 오전 3인 재실행 대비. 사용: python3 research/_deep/summary4.py [TICKER ...]"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from harness import core, judge

K = {"for": "찬", "against": "반", "abstain": "보", "conditional": "조"}
PREV = {}  # 오전 3인 재실행 (rerun_summary.md)
txt = (Path(__file__).parent / "rerun_summary.md").read_text(encoding="utf-8")
for t, lab in re.findall(r"## (\w+)\n\n- 판정: .*?→ \*\*(.+?)\*\*", txt):
    PREV[t] = lab
T = sys.argv[1:] or ["NVDA", "MELI", "UBER", "AMZN", "SHOP", "CRDO", "PLTR", "IOT", "CBRS", "PONY"]
money = lambda v: "—" if v is None else f"${v:,.2f}"
pct = lambda v: "—" if v is None else f"{v:+.1%}"
print("| 종목 | 오전(3인) | 지금(4인) | 표 앤·슬·애·클 | 주가 | 확률가중 IV | 기대 연수익 | 손실확률 | 켈리 | 클라만: 단단한 가치 · 하락폭 · 조건 가격 |")
print("|---|---|---|---|---|---|---|---|---|---|")
detail = []
for t in T:
    r = judge.judge(core.folder(t))
    an = r["analysis"]; v = (an.get("valuation") or {}).get("expected") or {}
    ag = {a["agent"]: a for a in r["agents"]}
    votes = " ".join(f"{K[ag[a]['final']]}{'(' + K[ag[a]['stance']] + ')' if ag[a]['stance'] != ag[a]['final'] else ''}" for a in core.AGENTS if a in ag)
    km = ag.get("klarman", {}).get("metrics", {})
    kl = f"{money(km.get('hard_value'))} · {pct(-km['downside']) if km.get('downside') is not None else '—'} · {money(km.get('buy_below'))}"
    print(f"| {t} | {PREV.get(t, '팽팽(3인, 10-17)' if t == 'PONY' else '—')} | **{r['label']}** | {votes} | {money(an['market']['price'])} | {money(v.get('iv'))} | "
          f"{pct(v.get('irr'))} | {v.get('p_loss', 0):.0%} | {(r.get('sizing') or {}).get('suggested', 0):.1%} | {kl} |")
    lines = [f"### {t}"]
    for a in core.AGENTS:
        x = ag.get(a)
        if not x:
            continue
        bb = x["metrics"].get("buy_below")
        lines.append(f"- {core.AGENTS[a]}: 입장 {K[x['stance']]} → 표 {K[x['final']]} (확신 {x['conviction']})"
                     + (f" · 조건 가격 {money(bb)}" if bb else "") + (f" · 레드라인: {', '.join(x['red_lines'])}" if x["red_lines"] else ""))
    lad = r.get("ladder") or []
    if len(lad) > 1:
        lines.append("- 조건부 사다리: " + " → ".join(f"{money(s['price'])}({s['change']:+.0%}) {s['label']}"
                                                  + (f" [{', '.join(s['who'])}]" if s['who'] else "") for s in lad))
    detail.append("\n".join(lines))
print()
print("\n\n".join(detail))

"""4인 위원회 종목 데이터 시트 → research/_deep/v4/<TICKER>.md (하네스 판정 + v4 비중 라운드). 사용: python3 research/_deep/sheet4.py
판정 이력 줄과 3인·9종목 비중은 기존 시트에서 가져온다(이전 실행의 기록이라 다시 계산할 수 없다)."""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from harness import core, judge

V4 = ROOT / "research/_portfolio/v4"
OUT = Path(__file__).parent / "v4"
R = json.loads((V4 / "risk.json").read_text())
C = json.loads((V4 / "committee.json").read_text())
A = ["anderson", "slater", "ackman", "klarman"]
S = {a: json.loads((V4 / f"sizing.{a}.json").read_text()) for a in A}
T = ["UBER", "MELI", "CRDO", "NVDA", "SHOP", "AMZN", "PLTR", "IOT", "CBRS", "PONY"]
K = {"for": "찬성", "against": "반대", "abstain": "보류", "conditional": "조건부 찬성"}
FIXED = {"SHOP": "애크먼 표 반대 → 보류(찬2·반1·보1 → 찬2·반0·보2, 판정은 찬성 우세 그대로)",
         "PLTR": "팽팽(찬1·반1·보2) → 찬성 우세(찬1·반0·보3)", "IOT": "팽팽(찬1·반1·보2) → 찬성 우세(찬1·반0·보3)"}
money = lambda v: "—" if v is None else f"${v:,.2f}"
votes = lambda v: f"찬{v['for']}·반{v['against']}·보{v['abstain']}"
cm = C["committee"]
groups = " / ".join(f"{n} {cm['groups'][g]['w']:.1f}%" for g, n in
                    [("ai_hw", "AI 하드웨어(NVDA·CRDO·CBRS)"), ("av", "자율주행(UBER·PONY)"), ("ai_capex", "AI 자본조달(NVDA·CRDO·CBRS·AMZN)"), ("commerce", "커머스(MELI·SHOP)")])
for t in T:
    old = (OUT / f"{t}.md").read_text(encoding="utf-8")
    hist = re.search(r"^- 판정 이력: .*$", old, re.M).group(0)
    hist = re.sub(r" · 4인 첫 집계는 .*$", "", hist)
    prev = re.search(r"\*\*[\d.]+%\*\* \(([^)]*)\)", old).group(1)
    if t in FIXED:
        hist += f" · 4인 첫 집계는 부동소수점 버그(애크먼 조건 가격 경계)로 {FIXED[t].split(' → ')[0]}였고, 수정 후 {FIXED[t].split(' → ', 1)[1]}"
    r = judge.judge(core.folder(t))
    an = r["analysis"]; v = (an.get("valuation") or {}).get("expected") or {}
    ag = {x["agent"]: x for x in r["agents"]}
    L = [f"# {t} — 4인 위원회 데이터 (2026-10-18, 하네스 코드 계산값)", "",
         f"- 4인 판정: **{r['label']}** ({votes(r['votes'])}) · 주가 {money(an['market']['price'])} (2026-10-16) · 확률가중 IV {money(v.get('iv'))} · "
         f"기대 연수익(5년) {v.get('irr', 0):+.1%} · 손실확률 {v.get('p_loss', 0):.0%} · 1/4켈리 참고 {(r.get('sizing') or {}).get('suggested', 0):.1%}", hist]
    for a in A:
        x = ag[a]; bb = x["metrics"].get("buy_below")
        L.append(f"- {core.AGENTS[a]}: 입장 {K[x['stance']]} → 집계된 표 {K[x['final']]} (확신 {x['conviction']})" + (f" · 조건 가격 {money(bb)}" if bb else "")
                 + (f" · 레드라인 위반: {', '.join(x['red_lines'])}" if x["red_lines"] else " · 레드라인 위반 없음") + (f" · 바뀐 이유: {x['override']}" if x.get("override") else ""))
    km = ag["klarman"]["metrics"]
    L.append(f"- 클라만 계산값: 단단한 가치 {money(km.get('hard_value'))} (근거: {km.get('hard_basis')}; 주당 순현금 {money(km.get('net_cash_ps'))}, 유형 순자산 {money(km.get('tangible_book_ps'))}, "
             f"무성장 가치 {money(km.get('no_growth_ps'))}) · 성장이 틀릴 때 하락폭 {km.get('downside', 0):.1%} · 주가 중 성장 프리미엄 {km.get('growth_premium', 0):.1%} · "
             f"보수적 내재가치 {money(km.get('intrinsic_value'))} · 안전마진 {km.get('mos', 0):.1%} · 52주 최저 {money(km.get('low_52w'))} · 지난 52주에 조건 가격 이하 거래: {km.get('traded_below_52w')}")
    lad = r.get("ladder") or []
    if len(lad) > 1:
        L.append("- 조건부 사다리: " + " → ".join(f"{money(s['price'])}({s['change']:+.0%}) {s['label']} ({votes(s['votes'])})" + (f" [{', '.join(s['who'])}]" if s["who"] else "") for s in lad))
    L.append(f"- 위원회 비중(4인 동일가중, 전체 포트폴리오 대비, SCHD 40% 별도): **{cm['w'][t]:.1f}%** ({prev}) · 4인 안: "
             + " / ".join(f"{core.AGENTS[a]} {S[a]['weights'][t]:.1f}" for a in A))
    L.append(f"- 위험: 1년 변동성 {R['vol'][t]:.0%}{' (상장 후 ' + str(R['n'][t]) + '거래일)' if R['n'][t] < 200 else ''} · 위원회안 위험 기여 {cm['rc'][t]:.1%} · "
             f"NVDA 상관 {R['corr'][t + '-NVDA']:.2f} · SCHD 상관 {R['corr'][t + '-SCHD']:.2f} · 묶음: {groups}")
    for a in A:
        L.append(f"  - {core.AGENTS[a]} 비중 이유: {S[a]['reasons'].get(t, '—')}")
    adds = [x for x in C["adds"] if x["ticker"] == t]
    if adds:
        L.append("- 조건 가격에서의 추가 계획: " + "; ".join(f"{money(x['price'])}에서 " + ", ".join(f"{core.AGENTS[d['agent']]} +{d['add']:.1f}%p" for d in x["detail"]) for x in adds))
    (OUT / f"{t}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(t, r["label"], cm["w"][t])

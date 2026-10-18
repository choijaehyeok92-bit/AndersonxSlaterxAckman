"""4인 위원회 비중 라운드 입력 — 10종목+SCHD 1년 일간 변동성·상관(2025-10-17~2026-10-16, Yahoo)과 하네스 판정값 → v4/risk.json"""
import json, urllib.request, math, sys, datetime as dt
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from harness import core, judge
T = ["UBER", "MELI", "CRDO", "NVDA", "SHOP", "AMZN", "PLTR", "IOT", "CBRS", "PONY", "SCHD"]
def series(s):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?range=2y&interval=1d"
    r = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read())["chart"]["result"][0]
    out = {dt.datetime.fromtimestamp(t, dt.UTC).strftime("%Y-%m-%d"): c for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c}
    return {d: c for d, c in out.items() if "2025-10-16" <= d <= "2026-10-16"}
P = {t: series(t) for t in T}
out = {"vol": {}, "corr": {}, "n": {}, "window": "2025-10-16~2026-10-16 일간 종가"}
for t in T:
    ds = sorted(P[t]); r = [P[t][b] / P[t][a] - 1 for a, b in zip(ds, ds[1:])]
    m = sum(r) / len(r); out["vol"][t] = math.sqrt(sum((x - m) ** 2 for x in r) / (len(r) - 1)) * math.sqrt(252); out["n"][t] = len(r)
for a in T:
    for b in T:
        ds = sorted(set(P[a]) & set(P[b])); ra = [P[a][y] / P[a][x] - 1 for x, y in zip(ds, ds[1:])]; rb = [P[b][y] / P[b][x] - 1 for x, y in zip(ds, ds[1:])]
        ma, mb = sum(ra) / len(ra), sum(rb) / len(rb)
        cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb)); va = sum((x - ma) ** 2 for x in ra); vb = sum((y - mb) ** 2 for y in rb)
        out["corr"][f"{a}-{b}"] = cov / math.sqrt(va * vb)
H = {}
for t in T[:-1]:
    r = judge.judge(core.folder(t)); v = r["analysis"].get("valuation") or {}; e = v.get("expected") or {}
    H[t] = dict(label=r["label"], votes=r["votes"], iv=e.get("iv"), price=(r["analysis"].get("market") or {}).get("price_quote"),
                irr=e.get("irr"), p_loss=e.get("p_loss"), kelly_ref=(r.get("sizing") or {}).get("suggested"),
                ladder=[dict(price=s["price"], label=s["label"], who=s["who"]) for s in r.get("ladder") or []],
                agents={a["agent"]: dict(final=a["final"], stance=a["stance"], conviction=a["conviction"], red_lines=a["red_lines"],
                                         buy_below=(a.get("metrics") or {}).get("buy_below"),
                                         hard_value=(a.get("metrics") or {}).get("hard_value")) for a in r["agents"]})
out["harness"] = H
(ROOT / "research/_portfolio/v4/risk.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str))
for t in T: print(t, f"vol {out['vol'][t]:.0%} n={out['n'][t]}", f"corrSCHD {out['corr'][t+'-SCHD']:.2f} corrNVDA {out['corr'][t+'-NVDA']:.2f}")

"""4인 위원회 종합안 + 코드 위험 점검 → v4/committee.json"""
import json
from pathlib import Path
V4 = Path(__file__).resolve().parents[1] / "v4"
R = json.loads((V4 / "risk.json").read_text())
T = ["UBER", "MELI", "CRDO", "NVDA", "SHOP", "AMZN", "PLTR", "IOT", "CBRS", "PONY"]
A = ["anderson", "slater", "ackman", "klarman"]
S = {a: json.loads((V4 / f"sizing.{a}.json").read_text()) for a in A}
W = {t: sum(S[a]["weights"][t] for a in A) / len(A) for t in T}
r = {t: round(W[t] * 2) / 2 for t in T}
diff = round((60 - sum(r.values())) * 2)
for t in sorted(T, key=lambda t: (W[t] - r[t]) * (1 if diff > 0 else -1), reverse=True)[:abs(diff)]:
    r[t] += 0.5 if diff > 0 else -0.5
X = T + ["SCHD"]
vol, corr = R["vol"], R["corr"]
def risk(w):
    x = {k: w.get(k, 0) / 100 for k in X}
    cov = lambda i, j: corr[f"{i}-{j}"] * vol[i] * vol[j]
    var = sum(x[i] * x[j] * cov(i, j) for i in X for j in X)
    return var ** 0.5, {i: x[i] * sum(x[j] * cov(i, j) for j in X) / var for i in X}
G = {"ai_hw": ("NVDA", "CRDO", "CBRS"), "av": ("UBER", "PONY"), "ai_capex": ("NVDA", "CRDO", "CBRS", "AMZN"), "commerce": ("MELI", "SHOP")}
def stats(w):
    full = {**w, "SCHD": 100 - sum(w.values())}
    v, rc = risk(full); h = R["harness"]
    return dict(w=full, vol=v, rc=rc, groups={g: dict(w=sum(full[t] for t in ts), rc=sum(rc[t] for t in ts)) for g, ts in G.items()},
                below_req=sum(full[t] for t in T if (h[t]["irr"] or -1) < 0.10), kelly_pos=[t for t in T if (h[t]["kelly_ref"] or 0) > 0])
adds = {}
for a in A:
    for c in S[a].get("conditional_adds") or []:
        k = (c["ticker"], round(float(c["price"]), 2)); adds.setdefault(k, []).append(dict(agent=a, add=c["add"], why=c.get("why", "")))
out = dict(proposals={a: stats(S[a]["weights"]) for a in A}, committee=stats(r), committee_raw=W,
           kelly=stats({t: (R["harness"][t]["kelly_ref"] or 0) * 100 for t in T}), equal=stats({t: 6.0 for t in T}),
           adds=[dict(ticker=k[0], price=k[1], agents=[x["agent"] for x in v], add_avg=sum(x["add"] for x in v) / len(A), detail=v)
                 for k, v in sorted(adds.items(), key=lambda kv: (kv[0][0], -kv[0][1]))])
(V4 / "committee.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
for a in A:
    o = out["proposals"][a]; print(a, {t: o["w"][t] for t in T}, f"vol {o['vol']:.1%}", {g: round(x['w'], 1) for g, x in o["groups"].items()})
for k in ("committee", "kelly", "equal"):
    o = out[k]; print(k, {t: round(o["w"][t], 2) for t in X}, f"vol {o['vol']:.1%} below10 {o['below_req']:.1f}", {g: (round(x['w'], 1), f"{x['rc']:.0%}") for g, x in o["groups"].items()})
    print("  rc", {t: f"{o['rc'][t]:.1%}" for t in X})
print("adds:"); [print(" ", x["ticker"], x["price"], x["agents"], round(x["add_avg"], 2)) for x in out["adds"]]

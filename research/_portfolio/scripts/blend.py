"""위원회 종합안 + 코드 위험 점검. 세 배분안을 동일 가중(WEIGHTS 기본)으로 평균하고, 변동성·상관으로 포트폴리오 위험을 계산한다."""
import json, pathlib
P = pathlib.Path("/home/claude/choijaehyeok92-bit/andersonxslaterxackman/research/_portfolio")
R = json.loads((P / "risk.json").read_text())
T = ["UBER", "MELI", "NVDA", "AMZN", "CRDO", "PLTR", "CBRS", "SHOP", "IOT"]
A = ["anderson", "slater", "ackman"]
S = {a: json.loads((P / f"sizing.{a}.json").read_text()) for a in A}
W = {t: sum(S[a]["weights"][t] for a in A) / 3 for t in T}
# 0.5% 단위로 반올림하되 합 60 유지 (가장 큰 반올림 오차부터 조정)
r = {t: round(W[t] * 2) / 2 for t in T}
diff = round((60 - sum(r.values())) * 2)
for t in sorted(T, key=lambda t: (W[t] - r[t]) * (1 if diff > 0 else -1), reverse=True)[:abs(diff)]:
    r[t] += 0.5 if diff > 0 else -0.5
X = T + ["SCHD"]
vol, corr = R["vol"], R["corr"]
def risk(w):  # w: 퍼센트, SCHD 포함
    x = {k: w.get(k, 0) / 100 for k in X}
    cov = lambda i, j: corr[f"{i}-{j}"] * vol[i] * vol[j]
    var = sum(x[i] * x[j] * cov(i, j) for i in X for j in X)
    mc = {i: x[i] * sum(x[j] * cov(i, j) for j in X) / var for i in X}
    return var ** 0.5, mc
def stats(w, label):
    full = {**w, "SCHD": 100 - sum(w.values())}
    v, mc = risk(full)
    h = R["harness"]
    exp = sum(full[t] / 100 * h[t]["irr"] for t in T)
    return {"label": label, "w": full, "vol": v, "rc": mc, "ai_hw": sum(full[t] for t in ("NVDA", "CRDO", "CBRS")),
            "max": max(T, key=lambda t: full[t]), "irr_equity_part": exp,
            "below_req": sum(full[t] for t in T if h[t]["irr"] < 0.10), "neg_kelly": sum(full[t] for t in T if h[t]["kelly_ref"] <= 0)}
out = {"proposals": {a: stats(S[a]["weights"], a) for a in A}, "committee": stats(r, "committee"), "committee_raw": W,
       "kelly": stats({t: R["harness"][t]["kelly_ref"] * 100 for t in T}, "harness_kelly"),
       "equal": stats({t: 60 / 9 for t in T}, "equal"),
       "schd_only": {"vol": vol["SCHD"]}}
(P / "committee.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
for k in ("anderson", "slater", "ackman"):
    o = out["proposals"][k]; print(k, {t: o["w"][t] for t in T}, f"vol {o['vol']:.1%} ai {o['ai_hw']:.1f}")
for k in ("committee", "kelly", "equal"):
    o = out[k]; print(k, {t: round(o["w"][t], 2) for t in X}, f"vol {o['vol']:.1%} ai {o['ai_hw']:.1f} below10 {o['below_req']:.1f} negK {o['neg_kelly']:.1f} irr*w {o['irr_equity_part']:.2%}")
    print("  rc", {t: f"{o['rc'][t]:.0%}" for t in X})

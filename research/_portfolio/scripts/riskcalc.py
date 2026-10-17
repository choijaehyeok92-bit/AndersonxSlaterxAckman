import json, urllib.request, math, sys, datetime as dt
sys.path.insert(0, "/home/claude/choijaehyeok92-bit/andersonxslaterxackman")
from harness import core, judge
T = ["UBER","MELI","NVDA","AMZN","CRDO","PLTR","CBRS","SHOP","IOT","SCHD"]
def series(s):
    u=f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?period1=1760572800&period2=1792195200&interval=1d"
    r=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30).read())["chart"]["result"][0]
    return {dt.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"):c for t,c in zip(r["timestamp"],r["indicators"]["quote"][0]["close"]) if c}
P={t:series(t) for t in T}
def rets(t, days):
    return {d: P[t][d]/P[t][p]-1 for p,d in zip(days, days[1:])}
out={"vol":{}, "corr":{}, "n":{}}
for t in T:
    ds=sorted(P[t]); r=[P[t][b]/P[t][a]-1 for a,b in zip(ds,ds[1:])]
    m=sum(r)/len(r); sd=math.sqrt(sum((x-m)**2 for x in r)/(len(r)-1))
    out["vol"][t]=sd*math.sqrt(252); out["n"][t]=len(r)
for a in T:
    for b in T:
        ds=sorted(set(P[a])&set(P[b])); ra=[P[a][y]/P[a][x]-1 for x,y in zip(ds,ds[1:])]; rb=[P[b][y]/P[b][x]-1 for x,y in zip(ds,ds[1:])]
        ma,mb=sum(ra)/len(ra),sum(rb)/len(rb)
        cov=sum((x-ma)*(y-mb) for x,y in zip(ra,rb)); va=sum((x-ma)**2 for x in ra); vb=sum((y-mb)**2 for y in rb)
        out["corr"][f"{a}-{b}"]=cov/math.sqrt(va*vb)
H={}
for t in T[:-1]:
    r=judge.judge(core.folder(t)); v=r["analysis"].get("valuation") or {}; e=v.get("expected") or {}
    H[t]=dict(label=r["label"], votes=r["votes"], iv=e.get("iv"), price=(r["analysis"].get("market") or {}).get("price_quote"),
              irr=e.get("irr"), p_loss=e.get("p_loss"), variance=e.get("variance"), kelly_ref=(r.get("sizing") or {}).get("suggested"),
              agents={a["agent"]:dict(final=a["final"], stance=a["stance"], conviction=a["conviction"], red_lines=a["red_lines"],
                       starter=(a.get("metrics") or {}).get("starter_weight")) for a in r["agents"]})
out["harness"]=H
json.dump(out, open("risk.json","w"), ensure_ascii=False, indent=1, default=str)
for t in T: print(t, f"vol {out['vol'][t]:.0%} n={out['n'][t]}", f"corrSCHD {out['corr'][t+'-SCHD']:.2f}", f"corrNVDA {out['corr'][t+'-NVDA']:.2f}")
for t,h in H.items(): print(t, h["label"], f"irr {h['irr']:.3f} ploss {h['p_loss']} kelly {h['kelly_ref']:.3f}", {k:(v['final'],v['conviction'],v['starter']) for k,v in h['agents'].items()})

"""L3 결정론적 계산 — LLM은 가정을 제안하고, 숫자는 여기서만 만든다.

입력: evidence.json의 사실(facts) + model.json의 가정. 출력: analysis(재무 이력·시장 배수·회계 품질 신호·
가이던스 적중률·역DCF·시나리오 가치·수익률 분해·민감도·컨센서스 대비·기저율·페르소나 지표).
모든 계산값은 ref에 'C:키'로 실려 에이전트가 인용할 수 있다.
"""
import math, re
from datetime import date
from . import core, rules
from .facts import RATIO, Facts

FLOWS = ("revenue", "cost_of_revenue", "gross_profit", "operating_income", "net_income", "pretax_income", "income_tax",
         "ocf", "capex", "sbc", "rnd", "d_and_a", "interest_expense", "buybacks", "dividends", "capitalized_software",
         "non_gaap_net_income", "non_gaap_operating_income", "adjusted_ebitda")
STOCKS = ("cash", "short_term_investments", "debt", "debt_current", "receivables", "inventory", "deferred_revenue",
          "total_assets", "equity", "goodwill")
ANNUAL, QUARTER = re.compile(r"^FY\d{4}$"), re.compile(r"^FY\d{4}Q[1-4]$")
DEFAULT_CASE = {"anderson": {"from": "bull"}, "slater": {"from": "base"}, "ackman": {"from": "base"}}
BASE_RATES = core.ROOT / "data" / "base_rates.json"   # council.py baserate가 만든다
MARGINS = (0.10, 0.15, 0.20, 0.25, 0.30)               # 역DCF 목표 FCF 마진 격자 — 모델과 무관하게 고정된 인용 키


def div(a, b):
    return a / b if a is not None and b else None


def chg(a, b):
    return a / b - 1 if a is not None and b is not None and b > 0 else None


def days(a, b):
    return (date.fromisoformat(a) - date.fromisoformat(b)).days


def days_of(stock, flow):  # 매출채권 회수일수(DSO)·재고일수(DIO)
    x = div(stock, flow)
    return None if x is None else x * 365


def rate(spec, t):  # 성장률 지정: 숫자(매년 같음) 또는 연도별 목록(끝값이 이후에도 이어진다)
    if isinstance(spec, list):
        return float(spec[min(t, len(spec)) - 1]) if spec else 0.0
    return float(spec or 0)


def currency(fx):
    units = [f["unit"] for f in fx.facts.values() if f["metric"] == "revenue" and re.match(r"^[A-Z]{3}$", f["unit"])]
    return max(sorted(set(units)), key=units.count) if units else None


def fx_rate(fx, a, b):  # a 통화 1단위 → b 통화. fx 사실의 단위는 'b/a'(a당 b) 또는 'a/b'
    if a == b:
        return 1.0
    for basis in ("market", "reported"):
        if v := fx.value("fx", basis=basis, unit=f"{b}/{a}"):
            return v
        if v := fx.value("fx", basis=basis, unit=f"{a}/{b}"):
            return 1 / v
    return None


# ── 재무 이력 ──

def history(fx, cur):
    periods = sorted({f["period"] for f in fx.facts.values() if f["metric"] == "revenue" and f["basis"] == "reported"
                      and ANNUAL.match(f.get("period") or "") and f["unit"] == cur},
                     key=lambda p: fx.get("revenue", p, unit=cur)["end"])
    rows, prev = [], None
    for p in periods:
        r = {"period": p, "end": fx.get("revenue", p, unit=cur)["end"]}
        r.update({m: fx.value(m, p, unit=cur) for m in FLOWS + STOCKS})
        r["diluted_shares"] = fx.value("diluted_shares", p, unit="shares")
        r["capex"] = abs(r["capex"]) if r["capex"] is not None else None
        if r["gross_profit"] is None and r["cost_of_revenue"] is not None:
            r["gross_profit"] = r["revenue"] - r["cost_of_revenue"]
        cash = None if r["cash"] is None else r["cash"] + (r["short_term_investments"] or 0)
        debt = (r["debt"] or 0) + (r["debt_current"] or 0)
        fcf = None if r["ocf"] is None or r["capex"] is None else r["ocf"] - r["capex"]
        ebitda = None if r["operating_income"] is None or r["d_and_a"] is None else r["operating_income"] + r["d_and_a"]
        tax = div(r["income_tax"], r["pretax_income"])
        tax = min(max(tax, 0), 0.5) if tax is not None else 0.21
        ic = None if r["equity"] is None else r["equity"] + debt - (cash or 0)
        yoy = prev if prev and 330 <= days(r["end"], prev["end"]) <= 400 else None
        g = lambda k: chg(r[k], yoy[k]) if yoy else None
        r.update(
            cash_total=cash, debt_total=debt, fcf=fcf, ebitda=ebitda,
            net_cash=None if cash is None else cash - debt,
            revenue_growth=g("revenue"), gross_margin=div(r["gross_profit"], r["revenue"]),
            operating_margin=div(r["operating_income"], r["revenue"]), fcf_margin=div(fcf, r["revenue"]),
            fcf_conversion=div(fcf, r["net_income"]) if (r["net_income"] or 0) > 0 else None,
            sbc_to_revenue=div(r["sbc"], r["revenue"]),
            sbc_to_ocf=div(r["sbc"], r["ocf"]) if (r["ocf"] or 0) > 0 else None,
            fcf_after_sbc=None if fcf is None or r["sbc"] is None else fcf - r["sbc"],
            roic=div(r["operating_income"] * (1 - tax), ic) if r["operating_income"] is not None and (ic or 0) > 0 else None,
            net_debt_to_ebitda=div(debt - (cash or 0), ebitda) if (ebitda or 0) > 0 else None,
            share_change=g("diluted_shares"), dso=days_of(r["receivables"], r["revenue"]),
            dio=days_of(r["inventory"], r["cost_of_revenue"]),
            receivables_growth=g("receivables"), inventory_growth=g("inventory"), deferred_revenue_growth=g("deferred_revenue"),
            accruals_ratio=(r["net_income"] - r["ocf"]) / ((r["total_assets"] + yoy["total_assets"]) / 2)
            if yoy and None not in (r["net_income"], r["ocf"], r["total_assets"], yoy["total_assets"]) else None,
            goodwill_to_assets=div(r["goodwill"], r["total_assets"]),
            capitalized_to_revenue=div(r["capitalized_software"], r["revenue"]),
        )
        rows.append(r)
        prev = r
    return rows


def ttm(fx, cur, rows):  # 최근 4개 분기가 연속이고 마지막 연간보다 새로우면 TTM, 아니면 마지막 연간
    qs = sorted({f["period"] for f in fx.facts.values() if f["metric"] == "revenue" and f["basis"] == "reported"
                 and QUARTER.match(f.get("period") or "") and f["unit"] == cur}, key=lambda p: fx.get("revenue", p, unit=cur)["end"])[-4:]
    ends = [fx.get("revenue", q, unit=cur)["end"] for q in qs]
    if len(qs) == 4 and 250 <= days(ends[-1], ends[0]) <= 300 and (not rows or ends[-1] > rows[-1]["end"]):
        out = {"period": f"TTM({qs[-1]})", "end": ends[-1]}
        for m in FLOWS:
            vals = [fx.value(m, q, unit=cur) for q in qs]
            out[m] = None if None in vals else sum(abs(v) if m == "capex" else v for v in vals)
        out["fcf"] = None if out["ocf"] is None or out["capex"] is None else out["ocf"] - out["capex"]
        out["ebitda"] = None if out["operating_income"] is None or out["d_and_a"] is None else out["operating_income"] + out["d_and_a"]
        out["fcf_margin"] = div(out["fcf"], out["revenue"])
        return out
    return dict(rows[-1]) if rows else None


def balance(fx, cur):
    """가장 최근 재무상태표 날짜(분기 포함)의 현금·차입금. 그 날짜에 없는 항목은 0 — 상환 후 사라진 차입금 태그의
    옛 값을 끌어오지 않는다."""
    rep = [f for f in fx.facts.values() if f["basis"] == "reported" and f["unit"] == cur]
    last = max((f["end"] for f in rep if f["metric"] in ("cash", "total_assets")), default=None)

    def at(m):
        fs = [f for f in rep if f["metric"] == m and f["end"] == last]
        return fx.pick(fs)["value"] if fs else None
    cash = at("cash")
    dil, out = fx.value("diluted_shares", unit="shares"), fx.value("shares_outstanding", unit="shares")
    ref = out or fx.value("shares_outstanding", basis="market", unit="shares")
    shares = ref if dil and ref and dil < 0.01 * ref else dil or out  # 천 주 단위로 잘못 태그된 희석 주식 수는 쓰지 않는다
    return dict(cash=None if cash is None else cash + (at("short_term_investments") or 0),
                debt=(at("debt") or 0) + (at("debt_current") or 0), shares=shares, date=last)


def market(fx, cur, t, bal):
    pf, notes = fx.get("price", basis="market"), []
    if not pf or "/" not in pf["unit"]:
        return None, ["주가 사실 없음 (metric=price, basis=market, 단위 USD/share 또는 USD/ADR)"]
    pc, per = pf["unit"].split("/")
    price = pf["value"]
    if per == "ADR":
        ratio = fx.value("adr_ratio", basis="market") or fx.value("adr_ratio")
        if not ratio:
            return None, ["ADR 주가인데 adr_ratio(ADR 1주 = 보통주 몇 주, 단위 shares/ADR) 사실 없음"]
        price /= ratio
    if (k := fx_rate(fx, pc, cur)) is None:
        return None, [f"주가 통화 {pc} ≠ 재무 통화 {cur} — fx 사실 필요 (단위 {cur}/{pc})"]
    price *= k
    if not bal["shares"]:
        return None, ["주식 수 사실 없음 (diluted_shares 또는 shares_outstanding)"]
    if days(fx.as_of, pf["end"]) > 10:
        notes.append(f"주가 기준일 {pf['end']}이 as_of({fx.as_of})보다 {days(fx.as_of, pf['end'])}일 오래됨")
    cap = price * bal["shares"]
    net_cash = (bal["cash"] or 0) - bal["debt"]
    if bal["cash"] is None:
        notes.append("현금 사실 없음 — 순현금 0으로 계산")
    ev = cap - net_cash
    g = lambda k: (t or {}).get(k)
    fcf, ebitda = g("fcf"), g("ebitda")
    return dict(price=price, price_quote=pf["value"], price_unit=pf["unit"], price_date=pf["end"], price_fact=pf["id"],
                shares=bal["shares"], market_cap=cap, cash=bal["cash"] or 0, debt=bal["debt"], net_cash=net_cash, ev=ev,
                fcf_yield=div(fcf, cap), p_fcf=div(cap, fcf) if (fcf or 0) > 0 else None,
                ev_revenue=div(ev, g("revenue")), pe=div(cap, g("net_income")) if (g("net_income") or 0) > 0 else None,
                ev_ebit=div(ev, g("operating_income")) if (g("operating_income") or 0) > 0 else None,
                fcf_positive=None if fcf is None else fcf > 0,
                net_debt_to_ebitda=div(-net_cash, ebitda) if (ebitda or 0) > 0 else None,
                runway_years=div(bal["cash"] or 0, -fcf) if fcf is not None and fcf < 0 else None), notes


# ── L4 회계 품질 신호: 판정이 아니라 forensic 역할이 반드시 해명해야 할 질문 목록 ──

def forensic(rows, fx):
    F, out, last = rules.FORENSIC, [], rows[-1] if rows else {}
    add = lambda key, sev, val, msg, period=None: out.append(dict(key=key, severity=sev, value=val, message=msg, period=period))
    l3 = rows[-3:]
    if any((r["net_income"] or 0) > 0 and (r["ocf"] if r["ocf"] is not None else 1) < 0 for r in l3):
        add("ocf_negative", "red", None, "순이익은 흑자인데 영업현금흐름이 음수인 해가 있다")
    ni, ocf = [r["net_income"] for r in l3], [r["ocf"] for r in l3]
    if l3 and None not in ni + ocf and sum(ni) > 0 and sum(ocf) / sum(ni) < F["ocf_to_ni"]:
        add("ocf_to_ni", "watch", sum(ocf) / sum(ni), f"최근 {len(l3)}년 영업현금흐름/순이익 {sum(ocf) / sum(ni):.2f} < {F['ocf_to_ni']}")
    checks = [("accruals", last.get("accruals_ratio"), F["accruals"], "발생액 비율(순이익-영업현금흐름)/평균 총자산"),
              ("sbc_to_revenue", last.get("sbc_to_revenue"), F["sbc_to_revenue"], "SBC/매출"),
              ("sbc_to_ocf", last.get("sbc_to_ocf"), F["sbc_to_ocf"], "SBC/영업현금흐름 — FCF의 상당 부분이 주식 보상"),
              ("goodwill", last.get("goodwill_to_assets"), F["goodwill"], "영업권/총자산 — 인수 의존")]
    for k, gap_of, label in (("receivables_gap", "receivables_growth", "매출채권"), ("inventory_gap", "inventory_growth", "재고")):
        gaps = [(r[gap_of] - r["revenue_growth"], r["period"]) for r in rows[-2:]  # 최근 2년 중 더 나쁜 해
                if r.get(gap_of) is not None and r.get("revenue_growth") is not None]
        if gaps:
            gap, period = max(gaps)
            checks.append((k, gap, F["wc_gap"], f"{period} {label} 증가율 - 매출 증가율", period))
    for key, val, thr, label, *period in checks:
        if val is not None and val > thr:
            add(key, "watch", val, f"{label} {val:.1%} > {thr:.0%}", *period)
    if (last.get("deferred_revenue_growth") or 0) < -0.10 and (last.get("revenue_growth") or 0) > 0.10:
        add("deferred_revenue", "watch", last["deferred_revenue_growth"], "매출은 늘었는데 이연매출이 10% 넘게 줄었다 — 매출 당겨쓰기 의심")
    sh = [r["diluted_shares"] for r in rows[-4:] if r["diluted_shares"]]
    if len(sh) >= 2 and (cagr := (sh[-1] / sh[0]) ** (1 / (len(sh) - 1)) - 1) > F["dilution"]:
        add("dilution", "watch", cagr, f"희석 주식 수 연 {cagr:.1%} 증가 > {F['dilution']:.0%}")
    caps = [r["capitalized_to_revenue"] for r in rows[-3:] if r["capitalized_to_revenue"] is not None]
    if len(caps) >= 2 and caps[-1] - caps[0] > F["capitalized"]:
        add("capitalized", "watch", caps[-1] - caps[0], f"자본화 소프트웨어/매출 {caps[0]:.1%}→{caps[-1]:.1%} — 비용의 자산화")
    for adj, gaap in (("non_gaap_net_income", "net_income"), ("non_gaap_operating_income", "operating_income"),
                      ("adjusted_ebitda", "ebitda")):
        a, b = last.get(adj), last.get(gaap)
        if a and b is not None and (a - b) / abs(a) > F["non_gaap_gap"]:
            add(f"non_gaap:{adj}", "watch", (a - b) / abs(a), f"{adj}가 GAAP {gaap}보다 {(a - b) / abs(a):.0%} 크다")
    for s in fx.src.values():
        if s["type"] == "filing" and core.ITEMS["4.02"] in (s.get("title") or ""):
            add("restatement", "red", None, f"재무제표 정정 공시 {s['id']} ({s.get('date')})")
        if s["type"] == "filing" and core.ITEMS["4.01"] in (s.get("title") or ""):
            add("auditor_change", "watch", None, f"감사인 변경 공시 {s['id']} ({s.get('date')})")
    return out


def guidance(fx):  # 과거 가이던스 vs 실제 — 경영진 신뢰도의 코드 계산
    out = []
    for f in fx.facts.values():
        a = f["basis"] == "guidance" and f.get("period") and fx.get(f["metric"], f["period"], unit=f["unit"])
        if not a:
            continue
        lo, hi = f.get("low", f["value"]), f.get("high", f["value"])
        if lo == hi:
            lo, hi = lo - abs(lo) * 0.01, hi + abs(hi) * 0.01
        out.append(dict(metric=f["metric"], period=f["period"], guided=f["value"], actual=a["value"], cites=[f["id"], a["id"]],
                        result="beat" if a["value"] > hi else "hit" if a["value"] >= lo else "miss"))
    return out


# ── 기저율 (outside view) ──

def base_rate(cagr, years, start_usd):
    t = core.load(BASE_RATES, {})
    h = t.get("horizons", {}).get(str(years))
    if not h or cagr is None:
        return None
    b = next((b for b in h["buckets"] if start_usd is not None and b["min"] <= start_usd < (b["max"] or math.inf)), h["all"])
    pts = sorted((float(k), v) for k, v in b["share_at_least"].items())
    if cagr <= pts[0][0]:
        share = pts[0][1]
    elif cagr >= pts[-1][0]:
        share = pts[-1][1]
    else:
        (x0, y0), (x1, y1) = next((p, q) for p, q in zip(pts, pts[1:]) if p[0] <= cagr <= q[0])
        share = y0 + (y1 - y0) * (cagr - x0) / (x1 - x0)
    return dict(cagr=cagr, years=years, share=share, capped=cagr > pts[-1][0], bucket=b["label"], n=b["n"],
                source=t.get("source", ""))


# ── 시나리오 모델: 드라이버 → 매출 → FCF → 현금·주식 수 → 출구 가치 ──

def project(base, model, sc, years=None, shift=0.0, mult_k=1.0):
    n0 = int(model.get("years", rules.HORIZON))
    n = int(years or n0)
    growth = sc.get("growth", {})
    names = list(base["drivers"])
    if not isinstance(growth, dict):  # 드라이버가 하나일 때의 줄임 표기
        growth = {names[0]: growth}
    lvl, rev, cash, shares, rows = dict(base["drivers"]), base["revenue"], base["cash"], base["shares"], []
    m0, mT = base["margin"], float(sc["fcf_margin"])
    for t in range(1, n + 1):
        if "revenue_growth" in sc:
            rev *= (1 + rate(sc["revenue_growth"], t)) * (1 + shift)
        else:
            for k in lvl:
                lvl[k] *= 1 + rate(growth.get(k), t)
            rev = base["revenue"] * math.prod(lvl[k] / base["drivers"][k] for k in lvl) * (1 + shift) ** t
        m = m0 + (mT - m0) * min(t, n0) / n0
        fcf = rev * m
        cash += fcf
        shares *= 1 + float(sc.get("share_change", base["share_change"]))
        rows.append(dict(period=f"FY{base['year'] + t}", revenue=rev, fcf_margin=m, fcf=fcf, shares=shares,
                         cash=cash, net_cash=cash - base["debt"]))
    last, mult = rows[-1], float(sc["exit_multiple"]) * mult_k
    equity = mult * max(last["fcf"], 0) + last["net_cash"]
    value = max(equity, 0) / last["shares"]
    r, p = float(model.get("discount_rate", rules.DISCOUNT)), base["price"]
    return dict(rows=rows, years=n, value=value, iv=value / (1 + r) ** n, multiple=mult,
                revenue_cagr=(rows[-1]["revenue"] / base["revenue"]) ** (1 / n) - 1,
                irr=(value / p) ** (1 / n) - 1 if value > 0 else -1.0, cash_min=min([base["cash"]] + [x["cash"] for x in rows]),
                decomposition=decompose(base, rows, n, mult, value))


def decompose(base, rows, n, mult, value):
    """연 수익률(로그) = 매출 성장 + 마진 변화 + 멀티플 변화 + 주식 수 변화 + 현금 축적. 합은 total과 같다."""
    last, p0, ln = rows[-1], base["price"], math.log
    nc0 = base["cash"] - base["debt"]
    eop0, eopN = p0 * base["shares"] - nc0, mult * last["fcf"]
    if eop0 <= 0 or eopN <= 0 or value <= 0 or 1 + last["net_cash"] / eopN <= 0 or 1 + nc0 / eop0 <= 0:
        return None
    out = {"revenue": ln(last["revenue"] / base["revenue"]) / n}
    if base["margin"] > 0:
        out["margin"] = ln(last["fcf_margin"] / base["margin"]) / n
        out["multiple"] = ln(mult / (eop0 / (base["margin"] * base["revenue"]))) / n
    else:  # 지금 FCF가 음수면 마진과 멀티플을 P/S로 묶는다
        out["margin_multiple"] = ln((eopN / last["revenue"]) / (eop0 / base["revenue"])) / n
    out["shares"] = -ln(last["shares"] / base["shares"]) / n
    out["cash"] = (ln(1 + last["net_cash"] / eopN) - ln(1 + nc0 / eop0)) / n
    out["total"] = ln(value / p0) / n
    return out


def reverse_dcf(ev, rev0, m0, mT, r=rules.DISCOUNT, gT=rules.TERMINAL_G, n=rules.REVERSE_YEARS):
    """현재 EV를 정당화하려면 매출이 n년간 연 몇 % 커져야 하는가 (FCF 마진은 m0→mT 선형, 이후 영구성장 gT)."""
    if not ev or ev <= 0 or not rev0 or rev0 <= 0 or mT <= 0 or m0 is None:
        return None

    def value(g):
        pv, rev = 0.0, rev0
        for t in range(1, n + 1):
            rev *= 1 + g
            pv += rev * (m0 + (mT - m0) * t / n) / (1 + r) ** t
        return pv + rev * mT * (1 + gT) / (r - gT) / (1 + r) ** n

    lo, hi = -0.5, 2.0
    if value(lo) > ev or value(hi) < ev:
        return None
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if value(mid) < ev else (lo, mid)
    return (lo + hi) / 2


# ── 전체 분석 ──

def setup(fx, model, an, warn):  # 시나리오 계산의 출발점
    rows, mkt = an["history"], an["market"]
    if not rows or not mkt or rows[-1]["fcf_margin"] is None:
        warn.append("시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요")
        return None
    last = rows[-1]
    drivers = {}
    for d in model.get("drivers") or [{"name": "revenue", "start": last["revenue"]}]:
        s = d.get("start")
        if not d.get("name") or d["name"] in drivers:
            warn.append(f"드라이버 이름이 없거나 중복: {d}")
            return None
        if isinstance(s, str):
            if s not in fx.facts:
                warn.append(f"드라이버 {d.get('name')}: 시작값 {s}가 유효한 사실이 아님")
                return None
            s = fx.facts[s]["value"]
        elif not d.get("cites") and d.get("name") != "revenue":
            warn.append(f"드라이버 {d.get('name')}: 숫자 시작값에 cites 없음")
        if not isinstance(s, (int, float)) or s <= 0:
            warn.append(f"드라이버 {d.get('name')}: 시작값은 양수")
            return None
        drivers[d["name"]] = float(s)
    prod = math.prod(drivers.values())
    if len(drivers) > 1 and abs(prod / last["revenue"] - 1) > 0.10:
        warn.append(f"드라이버 곱 {prod:,.0f}이 기준 매출 {last['revenue']:,.0f}과 {prod / last['revenue'] - 1:+.0%} 어긋남 — 성장률만 쓰고 수준은 보고 매출에 맞춘다")
    sh = [r["diluted_shares"] for r in rows[-4:] if r["diluted_shares"]]
    return dict(year=int(last["period"][2:6]), revenue=last["revenue"], margin=last["fcf_margin"],
                cash=mkt["cash"], debt=mkt["debt"], shares=mkt["shares"], price=mkt["price"], drivers=drivers,
                share_change=(sh[-1] / sh[0]) ** (1 / (len(sh) - 1)) - 1 if len(sh) >= 2 else 0.0)


def valuation(fx, model, an, warn):
    sc = model.get("scenarios") or {}
    if not {"bear", "base", "bull"} <= sc.keys():
        warn.append("model.json scenarios에 bear·base·bull 필요")
        return None, None
    base = setup(fx, model, an, warn)
    if not base:
        return None, None
    sc = {k: sc[k] for k in ("bear", "base", "bull")}
    for k, s in sc.items():
        missing = [f for f in ("p", "fcf_margin", "exit_multiple") if not isinstance(s.get(f), (int, float))]
        if missing:
            warn.append(f"시나리오 {k}: {', '.join(missing)} 필요")
            return None, base
        if isinstance(s.get("growth"), dict) and (extra := set(s["growth"]) - set(base["drivers"])):
            warn.append(f"시나리오 {k}: growth의 {', '.join(sorted(extra))}가 drivers에 없다 — 무시")
    total = sum(s["p"] for s in sc.values())
    if total <= 0:
        warn.append("시나리오 확률 합이 0 이하")
        return None, base
    if abs(total - 1) > 0.01:
        warn.append(f"시나리오 확률 합 {total:.2f} ≠ 1 — 정규화")
    try:
        return scenarios(fx, model, sc, base, total), base
    except (TypeError, ValueError, KeyError, ZeroDivisionError, OverflowError) as e:  # model.json은 LLM이 쓴다
        warn.append(f"시나리오 계산 실패 — {type(e).__name__}: {e}")
        return None, base


def scenarios(fx, model, sc, base, total):
    res = {k: {**project(base, model, s), "p": s["p"] / total} for k, s in sc.items()}
    p0, n = base["price"], res["base"]["years"]
    ev_v = sum(x["p"] * x["value"] for x in res.values())
    rets = {k: x["value"] / p0 - 1 for k, x in res.items()}
    mu = sum(res[k]["p"] * v for k, v in rets.items())
    var = sum(res[k]["p"] * (v - mu) ** 2 for k, v in rets.items())
    out = dict(years=n, discount_rate=float(model.get("discount_rate", rules.DISCOUNT)), scenarios=res,
               expected=dict(value=ev_v, iv=sum(x["p"] * x["iv"] for x in res.values()), irr=(ev_v / p0) ** (1 / n) - 1 if ev_v > 0 else -1.0,
                             p_loss=sum(x["p"] for x in res.values() if x["value"] < p0), mean_return=mu, variance=var),
               sensitivity=dict(shifts=[-0.05, 0.0, 0.05], multiples=[0.75, 1.0, 1.25],
                                irr=[[project(base, model, sc["base"], shift=s, mult_k=k)["irr"] for k in (0.75, 1.0, 1.25)]
                                     for s in (-0.05, 0.0, 0.05)]))
    rows = {r["period"]: r for r in res["base"]["rows"]}
    out["consensus"] = [dict(metric=f["metric"], period=f["period"], consensus=f["value"], model=rows[f["period"]][f["metric"]],
                             diff=rows[f["period"]][f["metric"]] / f["value"] - 1, cites=[f["id"]])
                        for f in fx.facts.values() if f["basis"] == "consensus" and f["metric"] in ("revenue", "fcf")
                        and f.get("period") in rows and f["value"]]
    return out


def persona(an, base, model, a, case=None):
    """페르소나가 고른 가정(case)으로 코드가 지표를 계산한다 — 페르소나가 숫자를 지어낼 여지를 없앤다."""
    case = {**DEFAULT_CASE[a], **(case or {})}
    mkt = an["market"] or {}
    out = {"case": case}
    if a == "ackman":
        out.update(price=mkt.get("price"), fcf_positive=mkt.get("fcf_positive"), net_debt_to_ebitda=mkt.get("net_debt_to_ebitda"),
                   leveraged=bool((mkt.get("net_debt_to_ebitda") or 0) > rules.LEVERAGE
                                  or (mkt.get("fcf_positive") is False and (mkt.get("runway_years") or 0) < 3)))
    if not base:
        return out
    if case["from"] not in ("bear", "base", "bull") or case["from"] not in (model.get("scenarios") or {}):
        out["error"] = f"case.from '{case['from']}'는 bear·base·bull 중 하나"
        return out
    sc = {**model["scenarios"][case["from"]], **{k: v for k, v in case.items() if k not in ("from", "years")}}
    try:
        if a == "anderson":  # LTGG Q10·Q1 — 기간은 10년·5년으로 고정
            r10, r5 = project(base, model, sc, 10), project(base, model, sc, 5)
            out.update(upside_10y=r10["value"] / base["price"], revenue_5y=r5["rows"][-1]["revenue"] / base["revenue"])
        elif a == "slater":
            res = project(base, model, sc, case.get("years"))
            out.update(cash_survives=res["cash_min"] >= 0, cash_min=res["cash_min"], runway_years=mkt.get("runway_years"))
        else:
            res = project(base, model, sc, case.get("years"))
            out.update(intrinsic_value=res["iv"], mos=1 - base["price"] / res["iv"] if res["iv"] > 0 else None)
    except (TypeError, ValueError, KeyError, ZeroDivisionError, OverflowError) as e:
        out["error"] = f"case 계산 실패 — {type(e).__name__}: {e}"
    return out


def analyze(ev, model=None, cases=None):
    fx = Facts(ev)
    warn = list(fx.warnings)
    cur = currency(fx)
    rows = history(fx, cur) if cur else []
    t = ttm(fx, cur, rows) if cur else None
    mkt, notes = market(fx, cur, t, balance(fx, cur)) if cur else (None, ["매출 사실 없음 — 재무 통화를 정할 수 없다"])
    warn += notes
    an = dict(ticker=ev.get("ticker"), as_of=fx.as_of, currency=cur, history=rows, ttm=t, market=mkt,
              forensic=forensic(rows, fx), guidance=guidance(fx), valuation=None, reverse_dcf=None, base_rates=[],
              personas={}, warnings=warn)
    g = an["guidance"]
    an["guidance_hit_rate"] = sum(x["result"] != "miss" for x in g) / len(g) if g else None
    base = None
    if model:
        an["valuation"], base = valuation(fx, model, an, warn)
    # 역DCF — 현재 가격이 가정하는 성장. 목표 FCF 마진 격자마다 계산하고, 모델이 있으면 기본 시나리오 마진의 값을 C:implied_cagr로 집는다
    if mkt and t and t.get("revenue") and t.get("fcf_margin") is not None:
        pick = ((model or {}).get("scenarios") or {}).get("base", {}).get("fcf_margin")
        pick = round(float(pick), 4) if isinstance(pick, (int, float)) and not isinstance(pick, bool) and pick > 0 else None
        grid = sorted(set(MARGINS) | ({pick} if pick else set()))
        an["reverse_dcf"] = dict(margin=pick, years=rules.REVERSE_YEARS, discount_rate=rules.DISCOUNT,
                                 terminal_growth=rules.TERMINAL_G, ev=mkt["ev"], revenue=t["revenue"],
                                 implied_cagr=reverse_dcf(mkt["ev"], t["revenue"], t["fcf_margin"], pick) if pick else None,
                                 grid={m: reverse_dcf(mkt["ev"], t["revenue"], t["fcf_margin"], m) for m in grid})
    usd = rows[-1]["revenue"] * k if rows and cur and (k := fx_rate(fx, cur, "USD")) else None
    rd = an["reverse_dcf"] or {}
    if rd.get("implied_cagr") is not None:
        an["base_rates"].append(dict(key="implied", label="시장 내재 성장 (역DCF)", **(base_rate(rd["implied_cagr"], rd["years"], usd) or
                                                                                 dict(cagr=rd["implied_cagr"], years=rd["years"], share=None))))
    v = an["valuation"]
    if v:
        for k in ("base", "bull"):
            rws = v["scenarios"][k]["rows"]
            cg = (rws[-1]["revenue"] / base["revenue"]) ** (1 / len(rws)) - 1
            br = base_rate(cg, len(rws), usd) or dict(cagr=cg, years=len(rws), share=None)
            an["base_rates"].append(dict(key=k, label=f"{k} 시나리오 매출 성장", **br))
            if k == "base" and br.get("share") is not None and br["share"] < rules.RARE:
                warn.append(f"기본 시나리오 매출 연 {cg:.0%} 성장은 기저율상 {br['share']:.0%}의 기업만 달성 — 근거를 보강하거나 가정을 낮춘다")
        if v["consensus"] and all(abs(c["diff"]) < rules.VARIANT_GAP for c in v["consensus"]):
            warn.append("모델이 컨센서스와 사실상 같다 — variant perception이 없다면 알파도 없다")
        if not v["consensus"]:
            warn.append("컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)")
    if not any(x["share"] is not None for x in an["base_rates"]) and an["base_rates"]:
        warn.append("기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다")
    for a in core.AGENTS:
        an["personas"][a] = persona(an, base, model or {}, a, (cases or {}).get(a))
    an["ref"], an["ref_pct"] = refs(an, fx)
    return an


def refs(an, fx):
    """인용 가능한 계산값 'C:키' → 값, 그리고 퍼센트로 읽어야 하는 키 목록.
    에이전트가 자연스럽게 쓰는 별칭(C:지표@기간 = 보고 사실, C:신호@기간)도 받아 준다 — 값은 사실·계산 그대로다."""
    out, pct = {}, set()
    for r in an["history"]:  # 재무 이력의 모든 숫자 (표에 없는 키도 인용할 수 있다)
        out.update({f"C:{k}@{r['period']}": v for k, v in r.items() if isinstance(v, (int, float)) and not isinstance(v, bool)})
    for f in fx.facts.values():
        if f["basis"] == "reported" and f.get("period") and f"C:{f['metric']}@{f['period']}" not in out:
            out[f"C:{f['metric']}@{f['period']}"] = f["value"]
            if f["unit"] == "ratio":
                pct.add(f"C:{f['metric']}@{f['period']}")
    for f in an["forensic"]:
        if isinstance(f["value"], (int, float)):
            out[f"C:{f['key']}"] = f["value"]
            if f.get("period"):
                out[f"C:{f['key']}@{f['period']}"] = f["value"]
    for k in ("price", "shares", "market_cap", "net_cash", "ev", "fcf_yield", "p_fcf", "ev_revenue", "pe", "ev_ebit",
              "net_debt_to_ebitda", "runway_years"):
        if (an["market"] or {}).get(k) is not None:
            out[f"C:{k}"] = an["market"][k]
    t = an["ttm"] or {}
    out.update({f"C:{k}@ttm": t[k] for k in ("revenue", "fcf", "fcf_margin", "net_income") if t.get(k) is not None})
    rd = an["reverse_dcf"] or {}
    if rd.get("implied_cagr") is not None:
        out["C:implied_cagr"] = rd["implied_cagr"]
    out.update({f"C:implied_cagr@m{m * 100:g}": g for m, g in (rd.get("grid") or {}).items() if g is not None})
    v = an["valuation"]
    out["C:discount_rate"] = v["discount_rate"] if v else rules.DISCOUNT
    if v:
        for k, s in v["scenarios"].items():
            out.update({f"C:value@{k}": s["value"], f"C:iv@{k}": s["iv"], f"C:irr@{k}": s["irr"], f"C:p@{k}": s["p"],
                        f"C:revenue@{k}": s["rows"][-1]["revenue"], f"C:fcf@{k}": s["rows"][-1]["fcf"],
                        f"C:revenue_cagr@{k}": s["revenue_cagr"], f"C:fcf_margin@{k}": s["rows"][-1]["fcf_margin"],
                        f"C:exit_multiple@{k}": s["multiple"]})
        out.update({"C:expected_irr": v["expected"]["irr"], "C:expected_iv": v["expected"]["iv"], "C:p_loss": v["expected"]["p_loss"]})
        out.update({f"C:consensus_diff@{c['metric']}@{c['period']}": c["diff"] for c in v["consensus"]})
    if an["guidance_hit_rate"] is not None:
        out["C:guidance_hit_rate"] = an["guidance_hit_rate"]
    for x in an["base_rates"]:
        if x.get("share") is not None:
            out[f"C:base_rate@{x['key']}"] = x["share"]
    for a, m in an["personas"].items():
        out.update({f"C:{k}@{a}": v for k, v in m.items() if isinstance(v, (int, float))})  # bool도 인용은 된다
    pct |= {k for k in out if k[2:].split("@")[0] in RATIO}
    return out, sorted(pct)


def sufficiency(ev, an):
    """게이트 0 — 근거 충분성. 비어 있으면 판정하지 않는다."""
    miss = []
    if not any(s.get("type") == "filing" for s in ev.get("sources", [])):
        miss.append("공시(filing) 근거 없음")
    if len(an["history"]) < rules.MIN_REVENUE_YEARS:
        miss.append(f"연간 매출 사실 {len(an['history'])}개 < {rules.MIN_REVENUE_YEARS}개")
    if not an["market"]:
        miss.append("주가·주식 수 없음 — 시장 가격과 비교할 수 없다")
    return miss

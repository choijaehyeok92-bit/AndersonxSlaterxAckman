"""L1 증거 수집 — 1차 자료를 코드가 직접 가져온다. 모든 항목에 원본 위치(url)와 수집 시각(retrieved)을 붙인다.

미국: SEC EDGAR 공시 목록 + XBRL 재무(companyfacts). 한국: DART OpenAPI(DART_API_KEY 필요). 공통: Google News RSS.
as_of(기준일)를 주면 그날까지 제출된 자료만 가져온다 — 과거 시점 재현(point-in-time) 테스트용.
"""
import io, json, math, os, re, time, zipfile, xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
from . import core

FORMS = {"10-K", "10-Q", "8-K", "20-F", "6-K", "40-F", "DEF 14A", "S-1", "F-1"}
FILING_DAYS, NEWS_DAYS, MAX_FILINGS, MAX_NEWS, ANNUAL_YEARS, QUARTERS = 400, 90, 30, 20, 5, 5
NEWS_LANG = {"en": "hl=en-US&gl=US&ceid=US:en", "ko": "hl=ko&gl=KR&ceid=KR:ko"}
UA = os.environ.get("SEC_USER_AGENT", "AndersonxSlaterxAckman research admin@example.com")  # SEC: '이름 이메일'
DART = "https://opendart.fss.or.kr/api"
G, I = "us-gaap:", "ifrs-full:"
XBRL = {  # metric → (단위 종류, 태그 우선순위). 회사마다 태그가 달라 앞의 것부터 기간별로 채운다
    "revenue": ("money", [G + "RevenueFromContractWithCustomerExcludingAssessedTax", G + "Revenues", G + "SalesRevenueNet",
                          G + "RevenueFromContractWithCustomerIncludingAssessedTax", I + "Revenue"]),
    "cost_of_revenue": ("money", [G + "CostOfRevenue", G + "CostOfGoodsAndServicesSold", I + "CostOfSales"]),
    "gross_profit": ("money", [G + "GrossProfit", I + "GrossProfit"]),
    "operating_income": ("money", [G + "OperatingIncomeLoss", I + "ProfitLossFromOperatingActivities"]),
    "net_income": ("money", [G + "NetIncomeLoss", I + "ProfitLossAttributableToOwnersOfParent"]),
    "pretax_income": ("money", [G + "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
                                I + "ProfitLossBeforeTax"]),
    "income_tax": ("money", [G + "IncomeTaxExpenseBenefit", I + "IncomeTaxExpenseContinuingOperations"]),
    "ocf": ("money", [G + "NetCashProvidedByUsedInOperatingActivities", I + "CashFlowsFromUsedInOperatingActivities"]),
    "capex": ("money", [G + "PaymentsToAcquirePropertyPlantAndEquipment", I + "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"]),
    "sbc": ("money", [G + "ShareBasedCompensation", G + "AllocatedShareBasedCompensationExpense"]),
    "rnd": ("money", [G + "ResearchAndDevelopmentExpense", I + "ResearchAndDevelopmentExpense"]),
    "d_and_a": ("money", [G + "DepreciationDepletionAndAmortization", G + "DepreciationAndAmortization",
                          I + "DepreciationAndAmortisationExpense"]),
    "interest_expense": ("money", [G + "InterestExpense"]),
    "buybacks": ("money", [G + "PaymentsForRepurchaseOfCommonStock"]),
    "dividends": ("money", [G + "PaymentsOfDividendsCommonStock", G + "PaymentsOfDividends"]),
    "capitalized_software": ("money", [G + "PaymentsToDevelopSoftware"]),
    "cash": ("money", [G + "CashAndCashEquivalentsAtCarryingValue", I + "CashAndCashEquivalents"]),
    "short_term_investments": ("money", [G + "ShortTermInvestments", G + "MarketableSecuritiesCurrent"]),
    "debt": ("money", [G + "LongTermDebtNoncurrent", G + "LongTermDebt", I + "NoncurrentPortionOfNoncurrentBorrowings"]),
    "debt_current": ("money", [G + "LongTermDebtCurrent", G + "DebtCurrent", I + "CurrentPortionOfNoncurrentBorrowings"]),
    "receivables": ("money", [G + "AccountsReceivableNetCurrent", I + "TradeAndOtherCurrentReceivables"]),
    "inventory": ("money", [G + "InventoryNet", I + "Inventories"]),
    "deferred_revenue": ("money", [G + "ContractWithCustomerLiabilityCurrent", G + "DeferredRevenueCurrent"]),
    "total_assets": ("money", [G + "Assets", I + "Assets"]),
    "equity": ("money", [G + "StockholdersEquity", I + "EquityAttributableToOwnersOfParent"]),
    "goodwill": ("money", [G + "Goodwill", I + "Goodwill"]),
    "diluted_shares": ("shares", [G + "WeightedAverageNumberOfDilutedSharesOutstanding", I + "WeightedAverageShares"]),
    "shares_outstanding": ("shares", ["dei:EntityCommonStockSharesOutstanding"]),
}
STOCK_METRICS = {"cash", "short_term_investments", "debt", "debt_current", "receivables", "inventory", "deferred_revenue",
                 "total_assets", "equity", "goodwill", "shares_outstanding"}
DART_ACCOUNTS = {  # DART 표준계정 → metric
    "revenue": ["ifrs-full_Revenue", "ifrs_Revenue"], "cost_of_revenue": ["ifrs-full_CostOfSales", "ifrs_CostOfSales"],
    "gross_profit": ["ifrs-full_GrossProfit", "ifrs_GrossProfit"], "operating_income": ["dart_OperatingIncomeLoss"],
    "net_income": ["ifrs-full_ProfitLossAttributableToOwnersOfParent", "ifrs_ProfitLossAttributableToOwnersOfParent", "ifrs-full_ProfitLoss"],
    "pretax_income": ["ifrs-full_ProfitLossBeforeTax"], "income_tax": ["ifrs-full_IncomeTaxExpenseContinuingOperations"],
    "ocf": ["ifrs-full_CashFlowsFromUsedInOperatingActivities", "ifrs_CashFlowsFromUsedInOperatingActivities"],
    "capex": ["ifrs-full_PurchaseOfPropertyPlantAndEquipment", "ifrs_PurchaseOfPropertyPlantAndEquipment"],
    "cash": ["ifrs-full_CashAndCashEquivalents", "ifrs_CashAndCashEquivalents"], "inventory": ["ifrs-full_Inventories"],
    "receivables": ["ifrs-full_TradeAndOtherCurrentReceivables", "dart_ShortTermTradeReceivable"],
    "total_assets": ["ifrs-full_Assets", "ifrs_Assets"], "goodwill": ["ifrs-full_Goodwill"],
    "equity": ["ifrs-full_EquityAttributableToOwnersOfParent", "ifrs_EquityAttributableToOwnersOfParent", "ifrs-full_Equity"],
}
DART_KEEP = re.compile(r"사업보고서|반기보고서|분기보고서|주요사항보고서|잠정|실적|기업설명회|최대주주|임원")


def fetch(url):
    with urlopen(Request(url, headers={"User-Agent": UA}), timeout=30) as r:
        return r.read()


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── SEC ──

def sec_filings(cik, as_of):
    r = json.loads(fetch(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))["filings"]["recent"]
    since = (date.fromisoformat(as_of) - timedelta(FILING_DAYS)).isoformat()
    return [dict(type="filing", title=" ".join([f, *(core.ITEMS[i] for i in items.split(",") if i in core.ITEMS)]), date=d,
                 url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}", accn=acc)
            for f, d, acc, doc, items in zip(r["form"], r["filingDate"], r["accessionNumber"], r["primaryDocument"], r["items"])
            if f in FORMS and since <= d <= as_of][:MAX_FILINGS]


def sec_facts(cik, cf, as_of):
    """companyfacts → 표준 사실. 연간 5개·분기 5개(최근 2년 Q4는 연간 − Q1~Q3로 계산). 정정된 값(최신 제출)을 쓴다."""
    recs, own = {}, {}
    for metric, (kind, tags) in XBRL.items():
        for pri, tt in enumerate(tags):
            tax, tag = tt.split(":")
            for u, rs in cf.get("facts", {}).get(tax, {}).get(tag, {}).get("units", {}).items():
                if (u != "shares") if kind == "shares" else not re.match(r"^[A-Z]{3}$", u):
                    continue
                for r in rs:
                    if r.get("form", "").split("/")[0] not in ("10-K", "10-Q", "20-F", "40-F") or r.get("filed", "9") > as_of:
                        continue
                    recs.setdefault(metric, []).append({**r, "unit": u, "pri": pri})
                    if r.get("start") and tax != "dei":  # 제출서의 '자기 기간' = 그 제출서 기간 데이터의 마지막 종료일
                        o = own.setdefault(r["accn"], dict(fy=r.get("fy"), fp=r.get("fp"), form=r["form"], filed=r["filed"], end=r["end"]))
                        o["end"] = max(o["end"], r["end"])
    labels = {}
    for o in sorted(own.values(), key=lambda o: o["filed"]):
        if o["fy"] and o["fp"] in ("FY", "Q1", "Q2", "Q3"):
            labels.setdefault(o["end"], f"FY{o['fy']}" + ("" if o["fp"] == "FY" else o["fp"]))
    span = lambda r: (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days if r.get("start") else None
    kind_of = lambda r: ("instant" if r.get("start") is None else "annual" if 340 <= span(r) <= 380
                         else "quarter" if 80 <= span(r) <= 100 else None)
    best = {}
    for metric, rs in recs.items():
        for r in rs:
            k = kind_of(r)
            if k and (metric in STOCK_METRICS) == (k == "instant"):
                key = (metric, k, r["end"])
                if key not in best or (r["pri"], -_ord(r["filed"])) < (best[key]["pri"], -_ord(best[key]["filed"])):
                    best[key] = r
    annual = sorted({e for (m, k, e) in best if k == "annual"})[-ANNUAL_YEARS:]
    quarter = sorted({e for (m, k, e) in best if k == "quarter" and re.match(r"^FY\d{4}Q[1-3]$", labels.get(e, ""))})[-QUARTERS:]
    label = lambda e: labels.get(e) if re.match(r"^FY\d{4}$", labels.get(e, "")) else f"FY{e[:4]}"
    out = []
    fact = lambda m, r, period, **kw: dict(metric=m, value=r["val"], unit=r["unit"], period=period, end=r["end"],
                                           basis="reported", origin="sec", accn=r["accn"], form=r["form"], filed=r["filed"], **kw)
    for (m, k, e), r in sorted(best.items()):
        if k == "annual" and e in annual:
            out.append(fact(m, r, label(e)))
        elif k == "quarter" and e in quarter:
            out.append(fact(m, r, labels[e]))
        elif k == "instant" and m == "shares_outstanding":
            if e == max(e2 for (m2, k2, e2) in best if m2 == m):
                out.append(fact(m, r, None))
        elif k == "instant" and (e in annual or e in quarter):
            out.append(fact(m, r, label(e) if e in annual else labels[e]))
    for e in annual[-2:]:  # Q4 = 연간 − Q1~Q3 (흐름 지표만)
        fy = label(e)
        for m in sorted({m for (m, k, e2) in best if k == "annual" and e2 == e and m not in STOCK_METRICS and m != "diluted_shares"}):
            qv = [r for (m2, k2, e2), r in best.items() if m2 == m and k2 == "quarter" and labels.get(e2, "").startswith(fy + "Q")]
            if len({labels[r["end"]] for r in qv}) == 3:
                a = best[(m, "annual", e)]
                out.append({**fact(m, a, fy + "Q4"), "value": a["val"] - sum(r["val"] for r in qv), "derived": True,
                            "note": "Q4 = 연간 − Q1~Q3 (코드 계산)"})
    return out


def _ord(d):  # 'YYYY-MM-DD' → 정렬용 정수
    return int(d.replace("-", "")) if d else 0


def sec(ticker, as_of):
    tickers = json.loads(fetch("https://www.sec.gov/files/company_tickers.json")).values()
    hit = next((v for v in tickers if v["ticker"] == ticker.upper().replace(".", "-")), None)
    if hit is None:
        return [], [], None
    cik = int(hit["cik_str"])
    filings = sec_filings(cik, as_of)
    facts = sec_facts(cik, json.loads(fetch(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")), as_of)
    known = {s["accn"] for s in filings}
    for f in facts:  # 사실의 출처 = 그 숫자가 실린 제출서
        if f["accn"] not in known:
            known.add(f["accn"])
            filings.append(dict(type="filing", title=f"{f['form']} (XBRL)", date=f["filed"], accn=f["accn"],
                                url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{f['accn'].replace('-', '')}/{f['accn']}-index.htm"))
    return filings, facts, hit.get("title")


# ── DART (한국) ──

def amount(s):
    s = str(s or "").replace(",", "").strip()
    return int(s) if re.fullmatch(r"-?\d+", s) else None


def dart(ticker, as_of, key):
    z = zipfile.ZipFile(io.BytesIO(fetch(f"{DART}/corpCode.xml?crtfc_key={key}")))
    corp = next((c for c in ET.fromstring(z.read(z.namelist()[0])).iter("list")
                 if (c.findtext("stock_code") or "").strip() == ticker), None)
    if corp is None:
        return [], [], None
    code, d = corp.findtext("corp_code"), date.fromisoformat(as_of)
    q = lambda api, **kw: json.loads(fetch(f"{DART}/{api}.json?" + urlencode(dict(crtfc_key=key, corp_code=code, **kw))))
    lst = q("list", bgn_de=(d - timedelta(FILING_DAYS)).strftime("%Y%m%d"), end_de=d.strftime("%Y%m%d"), page_count=100)
    url = lambda no: f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={no}"
    iso = lambda no: f"{no[:4]}-{no[4:6]}-{no[6:8]}"
    sources = [dict(type="filing", title=x["report_nm"].strip(), date=iso(x["rcept_no"]), url=url(x["rcept_no"]))
               for x in lst.get("list", []) if DART_KEEP.search(x.get("report_nm", ""))][:MAX_FILINGS]
    facts, years = [], []
    for y in range(d.year - 1, d.year - 8, -1):
        if len(years) == 2 or (years and y > years[-1] - 3):
            continue
        for div in ("CFS", "OFS"):  # 연결 우선, 없으면 별도
            r = q("fnlttSinglAcntAll", bsns_year=y, reprt_code="11011", fs_div=div)
            rows = [x for x in r.get("list", []) if x.get("rcept_no", "9")[:8] <= d.strftime("%Y%m%d")]
            if r.get("status") == "000" and rows:
                break
        else:
            continue
        years.append(y)
        no = rows[0]["rcept_no"]
        sources.append(dict(type="filing", title=f"사업보고서 ({y}.12) 재무제표 {'연결' if div == 'CFS' else '별도'}", date=iso(no), url=url(no)))
        for m, ids in DART_ACCOUNTS.items():
            row = next((x for i in ids for x in rows if x.get("account_id") == i), None)
            for col, yy in (("thstrm_amount", y), ("frmtrm_amount", y - 1), ("bfefrmtrm_amount", y - 2)):
                v = amount(row.get(col)) if row else None
                if v is not None:
                    facts.append(dict(metric=m, value=abs(v) if m == "capex" else v, unit=row.get("currency") or "KRW",
                                      period=f"FY{yy}", end=f"{yy}-12-31", basis="reported", origin="dart", src_url=url(no),
                                      scope="consolidated" if div == "CFS" else "separate", note="12월 결산 가정"))
    if years:
        try:
            st = q("stockTotqySttus", bsns_year=years[0], reprt_code="11011")
            row = next((x for x in st.get("list", []) if x.get("se") == "보통주"), None)
            if row and amount(row.get("distb_stock_co")):
                no = st["list"][0].get("rcept_no") or ""
                facts.append(dict(metric="shares_outstanding", value=amount(row["distb_stock_co"]), unit="shares",
                                  end=f"{years[0]}-12-31", basis="reported", origin="dart", src_url=sources[-1]["url"] if not no else url(no),
                                  note="유통주식수(발행 − 자기주식)"))
        except (OSError, ValueError, KeyError):
            pass
    seen = set()
    sources = [s for s in sources if not (s["url"] in seen or seen.add(s["url"]))]
    # 기간이 겹치면 최신 보고서 값을 쓴다 (앞 연도 보고서의 같은 기간 값은 버림)
    keep = {}
    for f in facts:
        keep.setdefault((f["metric"], f.get("period"), f["end"]), f)
    return sources, list(keep.values()), corp.findtext("corp_name")


# ── 뉴스 ──

def news(query, lang, as_of):
    window = f"when:{NEWS_DAYS}d" if as_of >= core.today() else \
        f"after:{(date.fromisoformat(as_of) - timedelta(NEWS_DAYS)).isoformat()} before:{as_of}"
    xml = fetch(f"https://news.google.com/rss/search?q={quote(f'{query} {window}')}&{NEWS_LANG[lang]}")
    return [dict(type="news", title=i.findtext("title"), url=i.findtext("link"), note=i.findtext("source") or "",
                 date=parsedate_to_datetime(i.findtext("pubDate")).date().isoformat())
            for i in ET.fromstring(xml).iter("item")][:MAX_NEWS]


# ── 병합: 근거는 URL로, 수집 사실은 (지표·기간·종료일)로 묶어 ID를 유지한다 — 재수집해도 인용이 깨지지 않는다 ──

def _next(items, prefix):
    return max([int(x["id"][1:]) for x in items if re.fullmatch(prefix + r"\d+", str(x.get("id")))] + [0])


def collect(d, ticker, name=None, lang="en", as_of=None):
    path, as_of = d / "evidence.json", as_of or core.today()
    ev = core.load(path, {"ticker": ticker.upper(), "name": name or ticker.upper(), "sources": [], "facts": []})
    ev.setdefault("facts", [])
    kr = bool(re.fullmatch(r"\d{6}", ticker))
    found, facts, errors = [], [], []
    jobs = [("DART", lambda: dart(ticker, as_of, os.environ["DART_API_KEY"]))] if kr else [("SEC", lambda: sec(ticker, as_of))]
    jobs.append(("뉴스", lambda: (news(name or ev.get("name") or ticker, lang, as_of), [], None)))
    for label, job in jobs:
        try:
            s, f, official = job()
            found += s
            facts += f
            if official and ev.get("name") in (None, ev["ticker"]):
                ev["name"] = name or official
        except KeyError as e:
            errors.append(f"{label} 수집 실패 — 환경변수 {e} 없음" if label == "DART" else f"{label} 수집 실패 — KeyError: {e}")
        except (OSError, ValueError, ET.ParseError, zipfile.BadZipFile) as e:
            errors.append(f"{label} 수집 실패 — {type(e).__name__}: {e}")
    urls, before, n = {s["url"]: s["id"] for s in ev["sources"]}, len(ev["sources"]), _next(ev["sources"], "S")
    for s in found:
        if s["url"] not in urls:
            n += 1
            urls[s["url"]] = f"S{n}"
            ev["sources"].append({"id": f"S{n}", **s, "retrieved": now()})
    by_accn = {s.get("accn"): s["id"] for s in ev["sources"] if s.get("accn")}
    key = lambda f: (f["metric"], f.get("period"), f["end"], f.get("origin"))
    old = {key(f): f["id"] for f in ev["facts"] if f.get("origin") in ("sec", "dart")}
    if facts:  # 새로 수집한 사실로 이전 수집분을 교체 (리서처가 넣은 사실은 그대로)
        ev["facts"] = [f for f in ev["facts"] if f.get("origin") not in ("sec", "dart")]
    m = _next(ev["facts"] + [{"id": i} for i in old.values()], "F")
    for f in facts:
        src = by_accn.get(f.pop("accn", None)) or urls.get(f.pop("src_url", None))
        for k in ("form", "filed"):
            f.pop(k, None)
        if not src:
            continue
        if not (fid := old.get(key(f))):
            m += 1
            fid = f"F{m}"
        ev["facts"].append({"id": fid, **{k: v for k, v in f.items() if v is not None}, "source": src})
    ev["facts"].sort(key=lambda f: int(f["id"][1:]))
    ev.update(as_of=as_of, collected=now())
    core.save(path, ev)
    return dict(path=str(path), added=len(ev["sources"]) - before, total=len(ev["sources"]),
                facts=sum(f.get("origin") in ("sec", "dart") for f in ev["facts"]), errors=errors)


def merge(d, add):
    """리서처 보강분 병합. 수집된 공시·사실은 바꾸거나 지울 수 없다 — 사실층은 코드가 지킨다."""
    from .facts import Facts
    path = d / "evidence.json"
    ev = core.load(path)
    ev.setdefault("facts", [])
    urls, n, remap = {s["url"]: s["id"] for s in ev["sources"]}, _next(ev["sources"], "S"), {}
    for s in add.get("sources", []):
        if not s.get("url"):
            continue
        if s["url"] in urls:
            remap[s.get("id")] = urls[s["url"]]
            continue
        n += 1
        remap[s.get("id")] = urls[s["url"]] = f"S{n}"
        ev["sources"].append({**s, "id": f"S{n}", "retrieved": s.get("retrieved") or now()})
    used = {f.get("source") for f in ev["facts"]}
    drop = set(add.get("drop", [])) - used
    ev["sources"] = [s for s in ev["sources"] if not (s["id"] in drop and s["type"] == "news")]
    sig = lambda f: (f.get("metric"), f.get("period"), f.get("end"), f.get("basis", "reported"), f.get("value"), f.get("source"))
    have, m, added = {sig(f) for f in ev["facts"]}, _next(ev["facts"], "F"), 0
    for f in add.get("facts", []):
        f = {k: v for k, v in f.items() if k not in ("id", "origin", "derived")}
        f["source"] = remap.get(f.get("source"), f.get("source"))
        if sig(f) in have:
            continue
        m += 1
        added += 1
        ev["facts"].append({"id": f"F{m}", **f, "origin": "research"})
    if "gaps" in add:
        ev["gaps"] = add["gaps"]
    ev["researched"] = core.today()
    rejected = [w for w in Facts(ev).warnings if w.startswith("사실 ")]
    core.save(path, ev)
    return dict(path=str(path), sources=len(ev["sources"]), facts_added=added, rejected=rejected)


# ── 기저율 표: SEC XBRL frames로 매출 성장 분포를 코드가 직접 계산한다 ──

REVENUE_TAGS = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet",
                "RevenueFromContractWithCustomerIncludingAssessedTax"]
BUCKETS = [(0, 5e8, "매출 5억 달러 미만"), (5e8, 2e9, "5억~20억 달러"), (2e9, 1e10, "20억~100억 달러"),
           (1e10, 5e10, "100억~500억 달러"), (5e10, None, "500억 달러 이상")]
THRESHOLDS = (-0.10, 0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50)


def baserate(first=2010, last=2024, horizons=(5, 10), min_revenue=5e7, pause=0.15):
    rev = {}
    for y in range(first, last + 1):
        merged = {}
        for tag in REVENUE_TAGS:  # 앞 태그 우선
            try:
                data = json.loads(fetch(f"https://data.sec.gov/api/xbrl/frames/us-gaap/{tag}/USD/CY{y}.json"))["data"]
            except HTTPError as e:
                if e.code == 404:
                    continue
                raise
            for x in data:
                merged.setdefault(x["cik"], x["val"])
            time.sleep(pause)
        rev[y] = merged

    def summary(label, lo, hi, gs):
        gs = sorted(gs)
        return dict(label=label, min=lo, max=hi, n=len(gs), median=gs[len(gs) // 2] if gs else None,
                    share_at_least={f"{t:.2f}": sum(g >= t for g in gs) / len(gs) for t in THRESHOLDS} if gs else {})

    out = {}
    for h in horizons:
        pairs = [(rev[y][c], (rev[y + h][c] / rev[y][c]) ** (1 / h) - 1) for y in rev if y + h in rev
                 for c in rev[y] if rev[y][c] >= min_revenue and rev[y + h].get(c, 0) > 0]
        out[str(h)] = dict(buckets=[s for lo, hi, lab in BUCKETS if (s := summary(lab, lo, hi, [g for v, g in pairs
                                                                                               if lo <= v < (hi or math.inf)]))["n"]],
                           all=summary("전체", 0, None, [g for _, g in pairs]))
    table = dict(source="SEC XBRL frames API — us-gaap 매출 태그 연간(CY) 프레임", generated=core.today(), years=[first, last],
                 min_revenue=min_revenue, horizons=out,
                 method="시작 연도 y와 y+h에 모두 매출을 공시한 기업의 연평균 성장률. 시작 연도를 겹쳐 모두 모은다.",
                 caveats=["생존 편향 — 두 시점 모두 공시한 기업만 남아 상향 편향된다",
                          "명목 달러, 인수·매각 미조정", "XBRL 태그 커버리지 차이로 일부 기업 누락"])
    from .calc import BASE_RATES
    core.save(BASE_RATES, table)
    return table

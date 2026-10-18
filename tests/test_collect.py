import io, json, os, shutil, tempfile, unittest, zipfile
from pathlib import Path
from unittest import mock
from urllib.error import HTTPError
from harness import calc, collect, core
from harness.facts import Facts

RSS = (b"<rss><channel><item><title>Test beats - Reuters</title><link>https://news.example/1</link>"
       b"<pubDate>Thu, 15 Oct 2026 10:00:00 GMT</pubDate><source url='x'>Reuters</source></item></channel></rss>")


def rec(start, end, val, accn, fy, fp, form, filed):
    return {**({"start": start} if start else {}), "end": end, "val": val, "accn": accn, "fy": fy, "fp": fp, "form": form, "filed": filed}


K24, K25 = ("A-24-K", 2024, "FY", "10-K", "2025-02-20"), ("A-25-K", 2025, "FY", "10-K", "2026-02-20")
Q = {n: (f"A-25-Q{n}", 2025, f"Q{n}", "10-Q", d) for n, d in ((1, "2025-05-01"), (2, "2025-08-01"), (3, "2025-11-01"))}
COMPANYFACTS = {"facts": {
    "us-gaap": {
        "Revenues": {"units": {"USD": [
            rec("2024-01-01", "2024-12-31", 100, *K24), rec("2024-01-01", "2024-12-31", 101, *K25),   # 정정된 값(최신 제출)이 이긴다
            rec("2025-01-01", "2025-12-31", 200, *K25),
            rec("2025-01-01", "2025-03-31", 40, *Q[1]), rec("2025-04-01", "2025-06-30", 45, *Q[2]),
            rec("2025-01-01", "2025-06-30", 85, *Q[2]), rec("2025-07-01", "2025-09-30", 50, *Q[3]),       # 반기 누적은 버린다
            rec("2026-01-01", "2026-03-31", 60, "A-26-Q1", 2026, "Q1", "10-Q", "2026-05-01")]}},       # 기준일 이후 제출
        "RevenueFromContractWithCustomerExcludingAssessedTax": {"units": {"USD": [rec("2025-01-01", "2025-12-31", 199, *K25)]}},
        "CashAndCashEquivalentsAtCarryingValue": {"units": {"USD": [rec(None, "2025-12-31", 30, *K25), rec(None, "2025-09-30", 25, *Q[3])]}},
        "WeightedAverageNumberOfDilutedSharesOutstanding": {"units": {"shares": [rec("2025-01-01", "2025-12-31", 10, *K25)]}}},
    "dei": {"EntityCommonStockSharesOutstanding": {"units": {"shares": [rec(None, "2026-02-10", 11, *K25)]}}}}}
SUBMISSIONS = {"filings": {"recent": {"form": ["8-K", "10-K", "4", "10-Q", "10-K"],
                                      "filingDate": ["2026-03-10", "2026-02-20", "2026-02-21", "2025-11-01", "2019-01-01"],
                                      "accessionNumber": ["A-26-8", "A-25-K", "A-26-4", "A-25-Q3", "A-19-K"],
                                      "primaryDocument": ["e.htm", "k.htm", "f4.xml", "q3.htm", "old.htm"],
                                      "items": ["4.02,9.01", "", "", "", ""]}}}


def sec_fetch(url):
    if "company_tickers" in url:
        return json.dumps({"0": {"cik_str": 123, "ticker": "TEST", "title": "Test Corp"}}).encode()
    if "submissions" in url:
        return json.dumps(SUBMISSIONS).encode()
    if "companyfacts" in url:
        return json.dumps(COMPANYFACTS).encode()
    return RSS


class Sec(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp()) / "TEST"
        self.addCleanup(shutil.rmtree, self.d.parent)

    def test_xbrl_facts_and_filings(self):
        with mock.patch.object(collect, "fetch", sec_fetch):
            r = collect.collect(self.d, "TEST", as_of="2026-04-30")
        ev = core.load(self.d / "evidence.json")
        fx = Facts(ev)
        self.assertEqual((r["errors"], ev["name"], ev["as_of"]), ([], "Test Corp", "2026-04-30"))
        got = {(f["metric"], f.get("period")): f["value"] for f in ev["facts"]}
        self.assertEqual({k: v for k, v in got.items() if k[0] == "revenue"},
                         {("revenue", "FY2024"): 101, ("revenue", "FY2025"): 199, ("revenue", "FY2025Q1"): 40,
                          ("revenue", "FY2025Q2"): 45, ("revenue", "FY2025Q3"): 50, ("revenue", "FY2025Q4"): 199 - 135})
        self.assertEqual((got[("cash", "FY2025")], got[("cash", "FY2025Q3")], got[("diluted_shares", "FY2025")],
                          got[("shares_outstanding", None)]), (30, 25, 10, 11))
        q4 = next(f for f in ev["facts"] if f.get("period") == "FY2025Q4")
        self.assertTrue(q4["derived"])
        titles = {s["title"] for s in ev["sources"]}
        self.assertIn("8-K 재무제표 정정", titles)                       # 8-K 4.02 → 회계 품질 red 신호
        self.assertNotIn("4", {s["title"] for s in ev["sources"]})       # 관심 없는 서식(Form 4) 제외
        self.assertTrue(all(s.get("retrieved") for s in ev["sources"]))  # 수집 시각
        src = {s["id"]: s for s in ev["sources"]}
        self.assertTrue(src[next(f for f in ev["facts"] if f["metric"] == "revenue" and f["period"] == "FY2025")["source"]]["url"].endswith("k.htm"))
        self.assertEqual(fx.warnings, [])
        self.assertEqual([f["key"] for f in calc.forensic([], fx)], ["restatement"])

    def test_ttm_columns_total_revenue_and_ytd_quarters(self):
        cf = {"facts": {"us-gaap": {
            "RevenueFromContractWithCustomerExcludingAssessedTax": {"units": {"USD": [
                rec("2025-01-01", "2025-12-31", 70, *K25), rec("2025-01-01", "2025-03-31", 15, *Q[1]),
                rec("2025-04-01", "2025-06-30", 17, *Q[2]), rec("2025-07-01", "2025-09-30", 18, *Q[3])]}},
            "Revenues": {"units": {"USD": [rec("2025-01-01", "2025-12-31", 100, *K25)]}},           # 총매출이 5% 넘게 크다 → 총매출
            "NetCashProvidedByUsedInOperatingActivities": {"units": {"USD": [
                rec("2025-01-01", "2025-12-31", 40, *K25), rec("2024-07-01", "2025-06-30", 33, *Q[2]),  # 10-Q의 TTM 열 → 연간 아님
                rec("2025-01-01", "2025-03-31", 8, *Q[1]), rec("2025-01-01", "2025-06-30", 19, *Q[2]),
                rec("2025-01-01", "2025-09-30", 29, *Q[3])]}}}}}
        got = {(f["metric"], f["period"]): f for f in collect.sec_facts(1, cf, "2026-04-30")}
        self.assertEqual(got[("revenue", "FY2025")]["value"], 100)
        self.assertEqual(got[("ocf", "FY2025")]["value"], 40)
        self.assertNotIn(("ocf", "FY2024"), got)
        self.assertEqual([got[("ocf", f"FY2025Q{n}")]["value"] for n in (1, 2, 3, 4)], [8, 11, 10, 11])
        self.assertTrue(got[("ocf", "FY2025Q2")]["derived"] and not got[("ocf", "FY2025Q1")].get("derived"))

    def test_drops_mis_scaled_diluted_shares(self):
        cf = {"facts": {"us-gaap": {
            "Revenues": {"units": {"USD": [rec("2025-01-01", "2025-12-31", 100, *K25)]}},
            "WeightedAverageNumberOfDilutedSharesOutstanding": {"units": {"shares": [rec("2025-01-01", "2025-12-31", 174264, *K25)]}}},
            "dei": {"EntityCommonStockSharesOutstanding": {"units": {"shares": [rec(None, "2026-02-10", 180434756, *K25)]}}}}}
        got = {f["metric"] for f in collect.sec_facts(1, cf, "2026-04-30")}
        self.assertIn("shares_outstanding", got)
        self.assertNotIn("diluted_shares", got)

    def test_recollect_keeps_ids_and_research_facts(self):
        with mock.patch.object(collect, "fetch", sec_fetch):
            collect.collect(self.d, "TEST", as_of="2026-04-30")
            ids = {(f["metric"], f.get("period")): f["id"] for f in core.load(self.d / "evidence.json")["facts"]}
            collect.merge(self.d, {"facts": [{"metric": "nrr", "value": 1.2, "unit": "ratio", "period": "FY2025", "end": "2025-12-31", "source": "S1"}]})
            r = collect.collect(self.d, "TEST", as_of="2026-04-30")
        ev = core.load(self.d / "evidence.json")
        self.assertEqual(r["added"], 0)
        self.assertEqual({(f["metric"], f.get("period")): f["id"] for f in ev["facts"] if f.get("origin") == "sec"}, ids)
        self.assertEqual([f["metric"] for f in ev["facts"] if f.get("origin") == "research"], ["nrr"])

    def test_news_window_follows_as_of(self):
        urls = []
        with mock.patch.object(collect, "fetch", lambda u: urls.append(u) or RSS):
            collect.news("Test", "en", "2025-01-31")
            collect.news("Test", "en", core.today())
        self.assertIn("before%3A2025-01-31", urls[0])
        self.assertIn("when%3A90d", urls[1])

    def test_offline(self):
        with mock.patch.object(collect, "fetch", side_effect=OSError("blocked")):
            r = collect.collect(self.d, "TEST")
        self.assertEqual((r["total"], len(r["errors"])), (0, 2))


def dart_fetch(url):
    if "corpCode" in url:
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as z:
            z.writestr("CORPCODE.xml", "<result><list><corp_code>00164779</corp_code><corp_name>에스케이하이닉스</corp_name>"
                                       "<stock_code>000660</stock_code></list></result>")
        return buf.getvalue()
    if "list.json" in url:
        return json.dumps({"status": "000", "list": [{"rcept_no": "20260315000123", "report_nm": "사업보고서 (2025.12)"},
                                                     {"rcept_no": "20260320000999", "report_nm": "주주총회소집공고"}]}).encode()
    if "fnlttSinglAcntAll" in url and "bsns_year=2025" in url and "fs_div=CFS" in url:
        row = lambda aid, a, b, c: dict(rcept_no="20260315000123", account_id=aid, thstrm_amount=a, frmtrm_amount=b,
                                        bfefrmtrm_amount=c, currency="KRW")
        return json.dumps({"status": "000", "list": [row("ifrs-full_Revenue", "1,000", "900", "800"),
                                                     row("ifrs-full_PurchaseOfPropertyPlantAndEquipment", "-50", "-40", ""),
                                                     row("dart_OperatingIncomeLoss", "120", "-10", "30")]}).encode()
    if "stockTotqySttus" in url:
        return json.dumps({"status": "000", "list": [{"se": "보통주", "distb_stock_co": "728,002,365", "rcept_no": "20260315000123"}]}).encode()
    if "opendart" in url:
        return json.dumps({"status": "013", "message": "조회된 데이터가 없습니다."}).encode()
    return RSS


class Dart(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp()) / "000660"
        self.addCleanup(shutil.rmtree, self.d.parent)

    def test_dart(self):
        with mock.patch.object(collect, "fetch", dart_fetch), mock.patch.dict(os.environ, {"DART_API_KEY": "k"}):
            r = collect.collect(self.d, "000660", lang="ko", as_of="2026-10-16")
        ev = core.load(self.d / "evidence.json")
        got = {(f["metric"], f.get("period")): f["value"] for f in ev["facts"]}
        self.assertEqual(r["errors"], [])
        self.assertEqual(ev["name"], "에스케이하이닉스")
        self.assertEqual((got[("revenue", "FY2025")], got[("revenue", "FY2023")], got[("capex", "FY2025")],
                          got[("operating_income", "FY2024")], got[("shares_outstanding", None)]), (1000, 800, 50, -10, 728002365))
        self.assertNotIn(("capex", "FY2023"), got)                      # 빈 칸은 사실이 아니다
        self.assertTrue(all(f["unit"] == "KRW" for f in ev["facts"] if f["metric"] == "revenue"))
        self.assertEqual(Facts(ev).warnings, [])

    def test_missing_key(self):
        with mock.patch.object(collect, "fetch", dart_fetch), mock.patch.dict(os.environ, {}, clear=True):
            r = collect.collect(self.d, "000660")
        self.assertIn("DART_API_KEY", r["errors"][0])


class Merge(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp()) / "X"
        self.addCleanup(shutil.rmtree, self.d.parent)
        core.save(self.d / "evidence.json", {"ticker": "X", "as_of": "2026-10-16", "sources": [
            {"id": "S1", "type": "filing", "url": "u1", "date": "2026-02-01"}, {"id": "S2", "type": "news", "url": "u2", "date": "2026-09-01"},
            {"id": "S3", "type": "news", "url": "u3", "date": "2026-09-02"}],
            "facts": [{"id": "F1", "metric": "revenue", "value": 10, "unit": "USD", "period": "FY2025", "end": "2025-12-31", "source": "S1", "origin": "sec"},
                      {"id": "F2", "metric": "revenue", "value": 8, "unit": "USD", "period": "FY2024", "end": "2024-12-31", "source": "S3", "origin": "sec"}]})

    def test_merge_guards_the_fact_layer(self):
        r = collect.merge(self.d, {
            "sources": [{"id": "S2", "type": "call", "title": "어닝콜", "url": "u9", "date": "2026-08-01"},   # 기존 S2와 다른 URL → 새 번호
                        {"id": "S1", "type": "filing", "url": "u1"}],                                    # 이미 있는 근거
            "facts": [{"metric": "nrr", "value": 1.3, "unit": "ratio", "period": "FY2026Q2", "end": "2026-06-30", "source": "S2"},
                      {"metric": "gross_margin", "value": 41, "unit": "ratio", "period": "FY2025", "end": "2025-12-31", "source": "S1"},
                      {"id": "F1", "metric": "revenue", "value": 10, "unit": "USD", "period": "FY2025", "end": "2025-12-31", "source": "S1"}],
            "drop": ["S1", "S2", "S3"], "gaps": ["코호트 없음"]})
        ev = core.load(self.d / "evidence.json")
        self.assertEqual([s["id"] for s in ev["sources"]], ["S1", "S3", "S4"])  # 공시·사실이 쓰는 근거는 못 지운다
        nrr = next(f for f in ev["facts"] if f["metric"] == "nrr")
        self.assertEqual((nrr["source"], nrr["origin"]), ("S4", "research"))
        self.assertEqual(r["facts_added"], 2)                                 # 중복 사실은 건너뛴다
        self.assertIn("ratio 41", r["rejected"][0])
        self.assertEqual((ev["gaps"], ev["researched"]), (["코호트 없음"], core.today()))
        self.assertEqual([f["value"] for f in ev["facts"] if f["id"] == "F1"], [10])


class BaseRate(unittest.TestCase):
    def test_builds_table_from_frames(self):
        frames = {2010: {1: 1e9, 2: 1e8, 3: 1e7}, 2011: {1: 1.1e9}, 2015: {1: 2e9, 2: 1e8}, 2016: {1: 3.3e9}}

        def fake(url):
            if "/Revenues/" not in url:
                raise HTTPError(url, 404, "Not Found", {}, None)
            y = int(url.split("CY")[1][:4])
            return json.dumps({"data": [{"cik": c, "val": v} for c, v in frames.get(y, {}).items()]}).encode()

        path = Path(tempfile.mkdtemp()) / "base_rates.json"
        self.addCleanup(shutil.rmtree, path.parent)
        with mock.patch.object(collect, "fetch", fake), mock.patch.object(calc, "BASE_RATES", path):
            t = collect.baserate(2010, 2016, horizons=(5,), pause=0)
            share = calc.base_rate(0.20, 5, 1e9)["share"]
        a = t["horizons"]["5"]["all"]
        self.assertEqual(a["n"], 3)                                     # 매출 5천만 달러 미만(cik 3)은 제외
        self.assertAlmostEqual(a["share_at_least"]["0.10"], 2 / 3)      # 14.9%·24.6%·0%
        self.assertAlmostEqual(share, 1 / 2)                            # 5억~20억 달러 구간: 14.9%·24.6%
        self.assertTrue(path.exists() and t["caveats"])

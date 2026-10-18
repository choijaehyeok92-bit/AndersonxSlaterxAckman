import math
from unittest import mock
from harness import calc, core, facts
from harness.facts import Facts
from tests.base import Base


class History(Base):
    def test_history_and_market(self):
        an = calc.analyze(core.load(self.d / "evidence.json"))
        last = an["history"][-1]
        self.assertEqual([r["period"] for r in an["history"]], ["FY2022", "FY2023", "FY2024", "FY2025"])
        self.assertAlmostEqual(last["revenue_growth"], 1.2e9 / 7.14e8 - 1)
        self.assertEqual((last["fcf"], last["fcf_after_sbc"], last["net_cash"]), (6e7, -1.5e7, 9e8))
        m = an["market"]
        self.assertEqual((m["market_cap"], m["ev"]), (2.1e10, 2.01e10))
        self.assertAlmostEqual(m["fcf_yield"], 6e7 / 2.1e10)
        self.assertEqual(an["ref"]["C:fcf_margin@FY2025"], 0.05)
        self.assertEqual(an["valuation"], None)  # 모델 전에는 시나리오 계산이 없다
        self.assertEqual(calc.sufficiency(core.load(self.d / "evidence.json"), an), [])

    def test_mis_scaled_diluted_shares_fall_back_to_outstanding(self):
        self.add_facts({"metric": "diluted_shares", "value": 1.0e5, "unit": "shares", "period": "FY2026Q2", "end": "2026-06-30", "source": "S1"},
                       {"metric": "shares_outstanding", "value": 1.0e8, "unit": "shares", "end": "2026-07-01", "basis": "market", "source": "S1"})
        self.assertEqual(calc.analyze(core.load(self.d / "evidence.json"))["market"]["shares"], 1.0e8)

    def test_shares_use_larger_of_weighted_diluted_and_outstanding(self):  # 기간 중 상장 — 가중평균이 현재 주식 수보다 작다
        self.add_facts({"metric": "diluted_shares", "value": 1.5e8, "unit": "shares", "period": "FY2026Q2", "end": "2026-06-30", "source": "S1"},
                       {"metric": "shares_outstanding", "value": 2.4e8, "unit": "shares", "end": "2026-07-01", "basis": "market", "source": "S1"})
        self.assertEqual(calc.analyze(core.load(self.d / "evidence.json"))["market"]["shares"], 2.4e8)

    def test_long_term_investments_count_as_cash(self):
        self.add_facts({"metric": "long_term_investments", "value": 1e8, "unit": "USD", "period": "FY2025", "end": "2025-12-31", "source": "S1"})
        self.assertEqual(calc.analyze(core.load(self.d / "evidence.json"))["market"]["ev"], 2.0e10)

    def test_stale_consensus_is_not_a_variant(self):  # 낡은 컨센서스가 '시장과 다른 시각'을 만들지 않는다
        model = core.load(self.d / "model.json")
        cons = lambda: calc.analyze(core.load(self.d / "evidence.json"), model)["valuation"]
        self.assertEqual([c["period"] for c in cons()["consensus"]], ["FY2026", "FY2027"])
        self.add_facts({"metric": "revenue", "value": 1.8e9, "unit": "USD", "period": "FY2026", "end": "2026-12-31", "source": "S9",
                        "basis": "consensus"})                          # 같은 날 자료 — 나중에 들어온 사실이 앞의 것을 대신한다
        v = cons()
        self.assertEqual([c["cites"] for c in v["consensus"] if c["period"] == "FY2026"], [["F62"]])
        self.assertIn("F57: 같은 revenue FY2026", " ".join(v["stale_consensus"]))
        self.add_facts({"metric": "revenue", "value": 1.9e9, "unit": "USD", "period": "FY2026", "end": "2026-12-31", "source": "S9",
                        "basis": "guidance", "low": 1.85e9, "high": 1.95e9})  # 가이던스 하단보다 낮은 컨센서스 = 실적 반영 전 값
        v = cons()
        self.assertEqual([c["period"] for c in v["consensus"]], ["FY2027"])
        self.assertIn("가이던스 하단", " ".join(v["stale_consensus"]))
        ev = core.load(self.d / "evidence.json")
        ev["sources"].append({"id": "S12", "type": "filing", "title": "3분기 실적", "url": "u12", "date": "2026-10-16"})
        core.save(self.d / "evidence.json", ev)
        self.add_facts({"metric": "revenue", "value": 4e8, "unit": "USD", "period": "FY2026Q3", "end": "2026-09-30", "source": "S12"})
        v = cons()                                                     # 실적 발표(10-16) 전 날짜(10-15)의 컨센서스 → F58도 제외
        self.assertEqual(v["consensus"], [])
        self.assertIn("F58: 컨센서스 날짜 2026-10-15가 최근 실적 발표(FY2026Q3, 2026-10-16) 전", " ".join(v["stale_consensus"]))
        self.assertIn("낡은 컨센서스", " ".join(calc.analyze(core.load(self.d / "evidence.json"), model)["warnings"]))

    def test_annual_consensus_below_quarter_sum_is_stale(self):  # 상반기 실적 + 하반기 분기 컨센서스 > 연간 컨센서스 = 갱신 전 값
        q = lambda i, v, basis: {"metric": "revenue", "value": v, "unit": "USD", "period": f"FY2026Q{i}",
                                 "end": ["2026-03-31", "2026-06-30", "2026-09-30", "2026-12-31"][i - 1], "source": "S9", "basis": basis}
        self.add_facts(q(1, 4.2e8, "reported"), q(2, 4.5e8, "reported"), q(3, 4.8e8, "consensus"), q(4, 5.0e8, "consensus"))
        v = calc.analyze(core.load(self.d / "evidence.json"), core.load(self.d / "model.json"))["valuation"]
        self.assertEqual([c["period"] for c in v["consensus"]], ["FY2027"])  # 1.75e9 < 1.85e9
        self.assertIn("분기 합", " ".join(v["stale_consensus"]))

    def test_unit_lookahead_and_conflicts_are_excluded(self):
        self.fact("F53", value=31)                                     # 31%를 31로 — 단위 오류
        self.add_facts({"metric": "revenue", "value": 9e9, "unit": "USD", "period": "FY2026", "end": "2026-12-31", "source": "S1"},
                       {"metric": "revenue", "value": 1.3e9, "unit": "USD", "period": "FY2025", "end": "2025-12-31", "source": "S7"},
                       {"metric": "nrr", "value": 1.2, "unit": "ratio", "end": "2026-06-30", "source": "S99"})
        fx = Facts(core.load(self.d / "evidence.json"))
        w = " | ".join(fx.warnings)
        for k in ("F53 제외 — ratio 31", "F62 제외 — 기준일(2026-10-16) 이후 실적", "F64 제외 — 출처 S99 없음", "사실 충돌 revenue FY2025"):
            self.assertIn(k, w)
        self.assertEqual(fx.value("revenue", "FY2025"), 1.2e9)          # 충돌하면 1차 자료(filing) 값

    def test_adr_and_currency(self):
        ev = {"ticker": "TSMX", "as_of": "2026-10-16", "sources": [{"id": "S1", "type": "filing", "url": "u1", "date": "2026-04-01"},
                                                                    {"id": "S2", "type": "data", "url": "u2", "date": "2026-10-15"}],
              "facts": [{"id": "F1", "metric": "revenue", "value": 2.0e12, "unit": "TWD", "period": "FY2024", "end": "2024-12-31", "source": "S1"},
                        {"id": "F2", "metric": "revenue", "value": 2.9e12, "unit": "TWD", "period": "FY2025", "end": "2025-12-31", "source": "S1"},
                        {"id": "F3", "metric": "diluted_shares", "value": 2.6e10, "unit": "shares", "period": "FY2025", "end": "2025-12-31", "source": "S1"},
                        {"id": "F4", "metric": "price", "value": 200, "unit": "USD/ADR", "end": "2026-10-15", "basis": "market", "source": "S2"}]}
        an = calc.analyze(ev)
        self.assertIsNone(an["market"])
        self.assertIn("adr_ratio", " ".join(an["warnings"]))
        ev["facts"].append({"id": "F5", "metric": "adr_ratio", "value": 5, "unit": "shares/ADR", "end": "2026-10-15", "basis": "market", "source": "S2"})
        self.assertIn("fx 사실 필요 (단위 TWD/USD)", " ".join(calc.analyze(ev)["warnings"]))
        ev["facts"].append({"id": "F6", "metric": "fx", "value": 32, "unit": "TWD/USD", "end": "2026-10-15", "basis": "market", "source": "S2"})
        m = calc.analyze(ev)["market"]
        self.assertAlmostEqual(m["price"], 200 / 5 * 32)                # ADR 1주 = 보통주 5주, 1달러 = 32대만달러
        self.assertAlmostEqual(m["market_cap"], 1280 * 2.6e10)


class Valuation(Base):
    def setUp(self):
        super().setUp()
        self.ev, self.model = core.load(self.d / "evidence.json"), core.load(self.d / "model.json")

    def test_driver_projection_and_decomposition(self):
        v = calc.analyze(self.ev, self.model)["valuation"]
        b = v["scenarios"]["base"]
        self.assertAlmostEqual(b["rows"][0]["revenue"], 1.2e9 * 1.55)  # 설치 대수 +55%, 단가 그대로
        self.assertAlmostEqual(b["rows"][-1]["fcf_margin"], 0.18)
        self.assertAlmostEqual(b["irr"], (b["value"] / 84) ** (1 / 5) - 1)
        self.assertAlmostEqual(b["iv"], b["value"] / 1.1 ** 5)
        dec = b["decomposition"]
        self.assertAlmostEqual(sum(x for k, x in dec.items() if k != "total"), dec["total"])
        self.assertAlmostEqual(dec["total"], math.log(b["value"] / 84) / 5)
        self.assertAlmostEqual(sum(s["p"] for s in v["scenarios"].values()), 1)
        self.assertEqual([round(c["diff"], 3) for c in v["consensus"]], [0.063, 0.085])
        self.assertAlmostEqual(v["sensitivity"]["irr"][1][1], b["irr"])

    def test_reverse_dcf_roundtrip(self):
        rev0, m0, mT, g = 1e9, 0.05, 0.2, 0.17
        pv, rev = 0, rev0
        for t in range(1, 11):
            rev *= 1 + g
            pv += rev * (m0 + (mT - m0) * t / 10) / 1.1 ** t
        ev = pv + rev * mT * 1.03 / 0.07 / 1.1 ** 10
        self.assertAlmostEqual(calc.reverse_dcf(ev, rev0, m0, mT), g, places=6)
        an = calc.analyze(self.ev, self.model)
        self.assertEqual(an["reverse_dcf"]["margin"], 0.18)            # 목표 마진 = 기본 시나리오
        self.assertAlmostEqual(an["ref"]["C:implied_cagr"], an["reverse_dcf"]["grid"][0.18])

    def test_driver_checks(self):
        self.model["drivers"][1]["start"] = 50000
        self.assertIn("드라이버 곱", " ".join(calc.analyze(self.ev, self.model)["warnings"]))
        self.model["drivers"][0]["start"] = "F999"
        an = calc.analyze(self.ev, self.model)
        self.assertIsNone(an["valuation"])
        self.assertIn("유효한 사실이 아님", " ".join(an["warnings"]))

    def test_persona_cases(self):
        an = calc.analyze(self.ev, self.model, {"anderson": {"from": "base"}, "ackman": {"from": "bear"}})
        p = an["personas"]
        self.assertLess(p["anderson"]["upside_10y"], 5)
        self.assertAlmostEqual(p["anderson"]["revenue_5y"], an["valuation"]["scenarios"]["base"]["rows"][-1]["revenue"] / 1.2e9)
        self.assertAlmostEqual(p["ackman"]["intrinsic_value"], an["valuation"]["scenarios"]["bear"]["iv"])
        self.assertEqual((p["ackman"]["fcf_positive"], p["ackman"]["leveraged"], p["slater"]["cash_survives"]), (True, False, True))
        over = calc.analyze(self.ev, self.model, {"ackman": {"from": "base", "exit_multiple": 40, "fcf_margin": 0.25}})["personas"]["ackman"]
        self.assertGreater(over["intrinsic_value"], p["ackman"]["intrinsic_value"])

    def test_base_rates(self):
        table = {"source": "테스트", "horizons": {"10": {"buckets": [{"label": "작음", "min": 0, "max": 2e9, "n": 100,
                                                                     "share_at_least": {"0.20": 0.10, "0.30": 0.04}}],
                                                         "all": {"label": "전체", "min": 0, "max": None, "n": 500, "share_at_least": {"0.20": 0.05, "0.30": 0.02}}},
                                                  "5": {"buckets": [], "all": {"label": "전체", "min": 0, "max": None, "n": 900,
                                                                               "share_at_least": {"0.10": 0.3, "0.30": 0.06}}}}}
        path = self.tmp / "base_rates.json"
        core.save(path, table)
        with mock.patch.object(calc, "BASE_RATES", path):
            an = calc.analyze(self.ev, self.model)
            self.assertAlmostEqual(calc.base_rate(0.25, 10, 1e9)["share"], 0.07)   # 0.20→0.10, 0.30→0.04 선형 보간
            self.assertEqual(calc.base_rate(0.25, 10, 5e9)["bucket"], "전체")
        br = {b["key"]: b for b in an["base_rates"]}
        self.assertEqual(br["implied"]["bucket"], "작음")              # 매출 12억 달러
        self.assertTrue(br["bull"]["capped"])                          # 표의 끝보다 높은 성장 = '최대'
        self.assertIn("기저율상", " ".join(an["warnings"]))             # 기본 시나리오 31.9%는 드문 성장


class Klarman(Base):
    def test_hard_value_downside_and_buy_below(self):
        ev, model = core.load(self.d / "evidence.json"), core.load(self.d / "model.json")
        an = calc.analyze(ev, model, {"klarman": {"from": "base", "exit_multiple": 20}})
        k = an["personas"]["klarman"]
        self.assertEqual((k["net_cash_ps"], k["tangible_book_ps"], k["no_growth_ps"], k["owner_fcf"]), (3.6, 5.4, 3.6, -1.5e7))
        self.assertEqual((k["hard_value"], k["hard_basis"]), (5.4, "tangible_book_ps"))   # 셋 중 가장 큰 바닥
        self.assertAlmostEqual(k["downside"], 1 - 5.4 / 84)
        self.assertAlmostEqual(k["iv_low"], an["valuation"]["scenarios"]["bear"]["iv"])
        self.assertAlmostEqual(k["iv_high"], an["valuation"]["scenarios"]["base"]["iv"])
        self.assertAlmostEqual(k["buy_below"], min(k["intrinsic_value"] * 0.7, 5.4 / 0.5))  # 안전마진·하방 둘 다 지키는 가격
        self.assertEqual((k["low_52w"], k["traded_below_52w"]), (61, False))
        same = calc.reprice(k, 84)                                     # 지표와 조건부 판정이 같은 식을 쓴다
        self.assertEqual({x: same[x] for x in ("mos", "downside", "growth_premium")}, {x: k[x] for x in ("mos", "downside", "growth_premium")})
        low = calc.reprice(k, k["buy_below"])
        self.assertAlmostEqual(low["downside"], 0.5)

    def test_owner_cash_flow_and_intangibles(self):
        self.fact("F24", value=1e7)                                    # SBC가 작으면 주주 FCF가 양수 → 성장 없는 가치가 커진다
        self.add_facts({"metric": "intangibles", "value": 3e8, "unit": "USD", "period": "FY2025", "end": "2025-12-31", "source": "S1"})
        k = calc.analyze(core.load(self.d / "evidence.json"))["personas"]["klarman"]
        self.assertAlmostEqual(k["no_growth_ps"], (5e7 / 0.10 + 9e8) / 2.5e8)
        self.assertAlmostEqual(k["tangible_book_ps"], (1.35e9 - 3e8) / 2.5e8)  # 무형자산은 유형 순자산에서 뺀다
        self.assertNotIn("buy_below", k)                               # 모델 전에는 내재가치가 없어 조건 가격도 없다


class Forensic(Base):
    def flags(self):
        return {f["key"]: f["severity"] for f in calc.analyze(core.load(self.d / "evidence.json"))["forensic"]}

    def test_example_flag(self):
        self.assertEqual(self.flags(), {"sbc_to_ocf": "watch", "receivables_gap": "watch"})  # FY2024 매출채권 +86% vs 매출 +66%

    def test_red_and_watch_signals(self):
        self.fact("F18", value=-1e7)                                   # 순이익 흑자, 영업현금흐름 적자
        self.fact("F33", value=4e8)                                    # 매출채권 +208% vs 매출 +68%
        ev = core.load(self.d / "evidence.json")
        ev["sources"].append({"id": "S12", "type": "filing", "title": "8-K 재무제표 정정", "url": "u", "date": "2026-09-01"})
        core.save(self.d / "evidence.json", ev)
        f = self.flags()
        self.assertEqual(f, {"ocf_negative": "red", "restatement": "red", "receivables_gap": "watch"})

    def test_guidance_track_record(self):
        self.add_facts({"metric": "revenue", "value": 7.5e8, "unit": "USD", "period": "FY2024", "end": "2024-12-31", "basis": "guidance", "source": "S11"})
        an = calc.analyze(core.load(self.d / "evidence.json"))
        self.assertEqual(sorted(g["result"] for g in an["guidance"]), ["beat", "miss"])
        self.assertEqual(an["guidance_hit_rate"], 0.5)


class Tracing(Base):
    def test_numbers(self):
        got = [(k, v) for k, v, _ in facts.numbers("1.4억 달러, $84, 1,800억, 47%(전년 55%), 3.9%p, 25x, 2030년, Q2, FY2025, 1번 질문", strict=True)]
        self.assertEqual(got, [("raw", 1.4e8), ("raw", 84), ("raw", 1.8e11), ("pct", 47), ("pct", 55), ("pct", 3.9), ("raw", 25)])

    def test_trace_is_unit_aware(self):
        fx = Facts(core.load(self.d / "evidence.json"))
        cited = facts.pool([fx.src["S2"]], [fx.facts["F49"]], {"C:fcf_yield": 0.00286})
        everything = facts.pool(fx.src.values(), fx.facts.values())
        self.assertEqual(facts.trace("집중도 47%, 설치 4.1만 대, FCF 수익률 0.3%", cited, everything), [])
        self.assertEqual(facts.trace("회수기간 16%", cited, everything), [("16%", [])])    # 16은 개월이지 퍼센트가 아니다
        (num, where), = facts.trace("매출 12억 달러", cited, everything)   # 인용 누락 — 그 숫자가 있는 곳을 알려 준다
        self.assertEqual(num, "1.2e+09")
        self.assertIn("F4", where)
        self.assertEqual(facts.trace("추정: 매출 99억 달러", cited, everything), [])


class Forecasts(Base):
    def test_latest_guidance_beats_older_primary_source(self):  # 가이던스 상향: 2차 자료의 최신 값이 옛 1차 자료를 이긴다
        ev = core.load(self.d / "evidence.json")
        ev["sources"].append({"id": "S12", "type": "news", "title": "가이던스 상향 보도", "url": "u12", "date": "2026-10-16"})
        core.save(self.d / "evidence.json", ev)
        self.add_facts({"metric": "revenue", "value": 1.3e9, "unit": "USD", "period": "FY2025", "end": "2025-12-31", "source": "S12",
                        "basis": "guidance", "low": 1.25e9, "high": 1.35e9})
        fx = Facts(core.load(self.d / "evidence.json"))
        self.assertEqual(fx.get("revenue", "FY2025", basis="guidance")["value"], 1.3e9)
        self.assertEqual(fx.get("revenue", "FY2025")["source"], "S1")   # 실적은 그대로 1차 자료 우선

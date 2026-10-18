from unittest import mock
from harness import core, prompts, report, rules
from harness.judge import judge
from tests.base import Base


class Verdict(Base):
    def test_example(self):
        r = judge(self.d)
        self.assertEqual((r["verdict"], r["label"], r["score"], r["votes"]), ("FOR", "찬성 우세", 0.25, {"for": 2, "against": 1, "abstain": 1}))
        self.assertEqual([(x["opening"], x["final"], x["conviction"], x["override"]) for x in r["agents"]],
                         [("for", "for", 5, None), ("for", "for", 3, None), ("against", "against", 3, None),
                          ("conditional", "abstain", 4, "conditional")])   # 클라만: 조건 가격 위 → 보류
        self.assertEqual([g["name"] for g in r["gates"] if g["ok"]], ["근거 충분성", "회계 품질", "모델"])
        self.assertEqual(r["agents"][0]["warnings"], [r["agents"][0]["warnings"][0]])  # 앤더슨: 아마존 유비 = leap 하나
        self.assertIn("leap", r["agents"][0]["warnings"][0])
        self.assertEqual(r["agents"][1]["warnings"] + r["agents"][2]["warnings"], [])
        self.assertEqual(r["agents"][3]["warnings"], ["주가의 96%가 성장에 대한 값 — 성장 없는 가치는 주당 3.60"])
        self.assertEqual([(x["price"], x["label"], x["votes"]["for"], x["who"]) for x in r["ladder"]],
                         [(84, "찬성 우세", 2, []), (10.8, "찬성 우세", 3, ["클라만"])])
        self.assertEqual(len(r["notes"]), 1)                           # 기저율 표 없음
        self.assertEqual(r["verification"]["counts"]["supported"], r["verification"]["total"] - 1)
        self.assertEqual([k["id"] for k in r["kpis"]], ["K1", "K2", "K3", "K4"])
        self.assertEqual(r["sizing"]["suggested"], 0.0)                # 기대 5.7% < 요구수익률 10%
        md = report.render(r)
        for k in ("## 1. Variant perception", "## 2. 시나리오 분포", "## 3. 반증 조건", "## 4. 모니터링 KPI", "## 5. 확신도와 비중",
                  "## 6. 조건부 판정", "조건부 판정: 주가 ≤ 10.80 (-87%) → 찬성 우세 (찬3·반1·보0)", "클라만의 세 질문",
                  "조건 가격 이하로 내려간 적이 없다", "[at_risk] 휴머노이드", "사람이 정한다"):
            self.assertIn(k, md)

    def test_red_lines_use_computed_metrics(self):  # 말로 '찬성'해도 코드 계산이 원칙을 어기면 '반대'
        self.edit("ackman.2.json", stance="for")
        self.edit("anderson.2.json", case={"from": "base"})
        r = judge(self.d)
        self.assertEqual([(x["stance"], x["final"]) for x in r["agents"]],
                         [("for", "against"), ("for", "for"), ("for", "against"), ("conditional", "abstain")])
        self.assertEqual((r["verdict"], r["label"]), ("AGAINST", "반대 우세"))
        self.assertIn("10년 주당가치", r["agents"][0]["red_lines"][0])
        self.assertIn("안전마진", " ".join(r["agents"][2]["red_lines"]))

    def test_persona_numbers_lose_to_code(self):
        self.edit("anderson.1.json", metrics={"founder_led": True, "upside_10y": 30})
        self.edit("ackman.1.json", metrics={**core.load(self.d / "ackman.1.json")["metrics"], "intrinsic_value": 200, "price": 84})
        r = judge(self.d)
        self.assertIn("upside_10y: 페르소나가 쓴 30 대신 코드 계산값", " ".join(r["agents"][0]["warnings"]))
        self.assertAlmostEqual(r["agents"][2]["metrics"]["intrinsic_value"], r["analysis"]["valuation"]["scenarios"]["base"]["iv"])

    def test_slater_red_lines(self):
        mbt = core.load(self.d / "slater.2.json")["metrics"]["must_be_true"]
        for metrics in ({"unit_economics": "deteriorating"}, {"survival_path": False}, {"must_be_true": []},
                        {"must_be_true": [{"claim": "회수기간 18개월 이하", "status": "broken"}]},
                        {"must_be_true": [{"claim": "회수기간 12개월 이하", "metric": "payback_months", "op": "<=", "value": 12, "status": "on_track"}]}):
            self.edit("slater.2.json", metrics=metrics)
            x = judge(self.d)["agents"][1]
            self.assertEqual(x["final"], "against", metrics)
        self.assertIn("실제 16로 깨짐", " ".join(x["warnings"]))         # 마지막 경우: 코드가 broken으로 바꿈
        self.edit("slater.2.json", metrics={"must_be_true": mbt}, case={"from": "bear", "fcf_margin": -0.5})
        x = judge(self.d)["agents"][1]
        self.assertIn("현금 고갈", " ".join(x["red_lines"]))

    def test_ackman_leverage_is_code_checked(self):
        self.add_facts({"metric": "debt", "value": 5e9, "unit": "USD", "period": "FY2025", "end": "2025-12-31", "source": "S1"})
        x = judge(self.d)["agents"][2]
        self.assertTrue(x["metrics"]["capital_markets_dependent"])
        self.assertIn("자본시장 의존", " ".join(x["warnings"]))


class Conditional(Base):  # 클라만 — '이 가격 이하라면 찬성'
    def test_conditional_resolves_by_price(self):
        self.fact("F59", value=10)                                     # 주가가 조건 가격(10.8) 아래로
        r = judge(self.d)
        x = r["agents"][3]
        self.assertEqual((x["final"], x["override"], x["red_lines"]), ("for", None, []))
        self.assertEqual(r["ladder"][0]["votes"], r["votes"])          # 첫 줄 = 본 판정
        with mock.patch.object(rules, "CONDITIONAL_ABOVE", "against"):  # 더 엄격한 규칙으로 바꿀 수 있다
            self.fact("F59", value=84)
            self.assertEqual(judge(self.d)["agents"][3]["final"], "against")

    def test_conditional_cannot_buy_past_non_price_red_lines(self):
        self.add_facts({"metric": "debt", "value": 5e9, "unit": "USD", "period": "FY2025", "end": "2025-12-31", "source": "S1"})
        x = judge(self.d)["agents"][3]                                 # 레버리지는 가격과 무관 — 어떤 가격에도 못 산다
        self.assertEqual((x["final"], x["override"]), ("against", "redline"))
        self.assertIn("레버리지", " ".join(x["red_lines"]))

    def test_ladder_recomputes_price_lines_only(self):
        self.edit("ackman.2.json", stance="conditional")               # 애크먼: 안전마진 가격은 있지만 단순성 레드라인은 가격과 무관
        r = judge(self.d)
        lad = {x["price"]: x for x in r["ladder"]}
        ack = r["agents"][2]["metrics"]["buy_below"]
        self.assertAlmostEqual(ack, r["agents"][2]["metrics"]["intrinsic_value"] * 0.8)
        self.assertEqual(lad[ack]["finals"]["ackman"], "against")
        self.assertEqual(lad[10.8]["finals"], {"anderson": "for", "slater": "for", "ackman": "against", "klarman": "for"})
        self.assertEqual(r["agents"][2]["final"], "against")


class Verification(Base):
    def test_unsourced_numbers_downgrade_vote(self):
        o = core.load(self.d / "slater.1.json")
        o["arguments"][0]["point"] = "회수기간 13개월 — 고객 한 명을 데려오는 비용을 1년 안에 되찾는다"
        o["arguments"][1]["point"] = "순현금 9억 달러, 매출 +70% — 자금줄 리스크가 없다"
        o["arguments"][2]["point"] = "고객 집중도가 55%에서 47%로 내려오는 중 — 총이익률 41.2%"
        core.save(self.d / "slater.1.json", o)
        r = judge(self.d)
        x = r["agents"][1]
        self.assertEqual((x["final"], x["override"], x["verify"]), ("abstain", "verify", {"total": 3, "failed": 2}))
        w = " ".join(x["warnings"])
        self.assertIn("출처 없는 숫자 70%", w)                          # 어디에도 없는 숫자 → 실패
        self.assertIn("출처 없는 숫자 13", w)
        self.assertIn("인용하지 않은 근거의 숫자 41.2%(C:gross_margin@FY2025)", w)  # 있는 숫자 → 경고·인용 안내
        self.assertIn("verifier.json이 최신", " ".join(r["notes"]))     # 주장이 바뀌면 이전 검증은 쓰지 않는다
        self.assertEqual(r["label"], "팽팽")

    def test_verifier_verdicts_and_staleness(self):
        cl, key = prompts.claims(self.d)
        target = next(c for c in cl if c["role"] == "ackman" and c["where"] == "arguments[0]")
        checks = [{"id": c["id"], "verdict": "contradicted" if c["id"] == target["id"] else "supported"} for c in cl]
        core.save(self.d / "verifier.json", {"basis": key, "checks": checks})
        self.assertIn("arguments[0] contradicted", " ".join(judge(self.d)["agents"][2]["warnings"]))
        self.edit("redteam.json", weakest=[])                          # 주장이 바뀌면 검증 결과를 쓰지 않는다
        r = judge(self.d)
        self.assertIn("verifier.json이 최신 주장과 맞지 않음", " ".join(r["notes"]))
        self.assertNotIn("contradicted", " ".join(r["agents"][2]["warnings"]))

    def test_uncited_and_unknown(self):
        self.edit("slater.1.json", arguments=[{"point": "근거 없음"}, {"point": "가짜", "cites": ["S99"]}, {"point": "미래", "cites": ["S1"]}])
        self.edit("slater.2.json", metrics={"must_be_true": [{"claim": "목표주가 200달러", "status": "on_track"}]})
        self.edit("ackman.2.json", rebuttals=[{"to": "anderson", "point": "x", "cites": ["S1"]}])
        r = judge(self.d)
        w = " ".join(r["agents"][1]["warnings"])
        self.assertTrue(all(k in w for k in ("인용 없음", "S99", "가격 기반")))
        self.assertEqual(r["agents"][1]["final"], "abstain")
        self.assertEqual([w for w in r["agents"][2]["warnings"] if "반론 없음" in w], ["슬레이터에 대한 반론 없음", "클라만에 대한 반론 없음", "레드팀에 대한 반론 없음"])

    def test_stale_inputs(self):
        ev = core.load(self.d / "evidence.json")
        ev["sources"].append({"id": "S12", "type": "news", "title": "새 소식", "url": "u12", "date": "2026-10-16"})
        core.save(self.d / "evidence.json", ev)
        r = judge(self.d)
        stale = [n for n in r["notes"] if "갱신되지 않음" in n]
        self.assertEqual(len(stale), 5)                                # 모듈 3 + 모델 + 레드팀
        self.assertIn("1라운드: 입력", " ".join(r["agents"][0]["warnings"]))

    def test_moat_needs_hard_evidence(self):
        b = core.load(self.d / "business.json")
        b["moat"][0]["evidence"] = "proven"                           # 회사 발표(S4)만 인용
        core.save(self.d / "business.json", b)
        self.assertIn("해자 'scale'", " ".join(judge(self.d)["notes"]))

    def test_thesis_breaks_status(self):
        self.edit("slater.1.json", thesis_breaks=[{"note": "수동만"}])
        self.edit("ackman.1.json", thesis_breaks=[{"metric": "price", "op": ">=", "value": 80, "note": "주가 80달러 이상"}])
        r = judge(self.d)
        self.assertIn("기계로 판정할 수 있는 반증 조건", " ".join(r["agents"][1]["warnings"]))
        self.assertIn("반증 조건이 이미 충족됨", " ".join(r["agents"][2]["warnings"]))

    def test_unreported_period_waits_and_threshold_tolerance(self):  # 미래 분기 조건은 직전 분기 값으로 판정하지 않는다
        self.edit("ackman.1.json", thesis_breaks=[
            {"metric": "nrr", "op": "<", "value": 1.5, "note": "FY2026Q3 NRR이 1.5 아래면"},
            {"metric": "nrr", "op": "<", "value": 1.5, "note": "3분기 NRR이 2분기보다 낮아지면"},
            {"metric": "nrr", "op": "<", "value": 1.385, "note": "NRR이 지금 수준(1.38)보다 낮아지면"},   # 0.4% 차이 — 반올림 문턱
            {"metric": "nrr", "op": "<", "value": 1.5, "note": "NRR이 1.5 아래면"},
            {"metric": "nrr", "op": "<", "value": 1.5, "period": "FY2026Q4", "note": "4분기 NRR"}])
        st = [b["status"] for b in judge(self.d)["breaks"] if b["who"] == "애크먼"]
        self.assertEqual(st, ["대기 — FY2026Q3 미발표", "대기 — FY2026Q3 미발표", "미충족", "충족 — 훼손", "대기 — FY2026Q4 미발표"])
        self.edit("slater.2.json", metrics={**core.load(self.d / "slater.2.json")["metrics"], "must_be_true": [
            {"claim": "회수기간 FY2026Q2 수준(15.95개월) 이하 유지", "metric": "payback_months", "op": "<=", "value": 15.95, "status": "on_track"}]})
        x = judge(self.d)["agents"][1]
        self.assertNotIn("이미 반증된 가설", x["red_lines"])                 # 16 vs 15.95 — 0.3% 차이는 깨짐이 아니다


class Gates(Base):
    def test_evidence_gate(self):
        ev = core.load(self.d / "evidence.json")
        core.save(self.d / "evidence.json", {**ev, "facts": [f for f in ev["facts"] if f["metric"] != "price"]})
        r = judge(self.d)
        self.assertEqual((r["verdict"], r["agents"], r["ok"]), ("INCOMPLETE", [], False))
        self.assertIn("주가", r["gated"])

    def test_forensic_gate(self):
        self.edit("forensic.json", grade="red_flag", summary="매출 인식을 믿을 수 없다")
        r = judge(self.d)
        self.assertEqual((r["verdict"], r["label"], r["agents"]), ("AGAINST", "게이트 탈락: 회계 품질 — 반대", []))
        self.assertIn("게이트에서 멈췄다", report.render(r))
        (self.d / "forensic.json").unlink()
        self.assertEqual(judge(self.d)["verdict"], "INCOMPLETE")

    def test_forensic_cannot_ignore_code_red_flags(self):
        self.fact("F18", value=-1e7)
        self.edit("forensic.json", grade="clean")
        r = judge(self.d)
        self.assertEqual(r["modules"]["forensic"]["grade"], "watch")
        n = " ".join(r["notes"])
        self.assertIn("코드 red 신호(ocf_negative)", n)
        self.assertIn("ocf_negative를 forensic이 해명하지 않음", n)

    def test_model_gate(self):
        (self.d / "model.json").unlink()
        r = judge(self.d)
        self.assertEqual((r["verdict"], r["gates"][-1]["name"]), ("INCOMPLETE", "모델"))

    def test_malformed_llm_output_does_not_crash(self):  # 객체 대신 문자열 — 인용이 없으니 검증 실패로만 남는다
        self.edit("slater.1.json", arguments=["문자열 논거"], thesis_breaks=["문자열 조건"])
        self.edit("slater.2.json", rebuttals=["문자열 반론"], metrics={"must_be_true": ["회수기간 유지"]})
        self.edit("redteam.json", premortem=["문자열 부검"])
        self.edit("model.json", kpis=["문자열 KPI"])
        r = judge(self.d)
        x = r["agents"][1]
        self.assertEqual((x["final"], x["verify"]["failed"]), ("abstain", 1))
        self.assertIn("arguments[0] unsupported: 인용 없음", " ".join(x["warnings"]))
        self.assertEqual(r["kpis"], [])
        self.assertIn("문자열 부검", report.render(r))

    def test_bad_input(self):
        self.edit("forensic.json", grade="fine")
        self.assertRaises(ValueError, judge, self.d)
        self.edit("forensic.json", grade="watch")
        self.edit("evidence.json", sources=[{"id": "S1", "type": "blog", "url": "x"}])
        self.assertRaises(ValueError, judge, self.d)


class Barrier(Base):
    def test_user_view_never_reaches_prompts(self):  # 아첨 차단: 사용자 견해는 분석이 끝난 뒤 보고서에서만
        for role in core.ROLES:
            for rnd in ((1, 2) if role in core.AGENTS else (1,)):
                t = prompts.prompt(role, self.d, rnd)
                self.assertNotIn("과대평가된 위협", t, role)
        r = judge(self.d)
        self.assertIn("확증 편향 점검", report.render(r))
        self.assertEqual(r["user_view"]["view"]["stance"], "for")

    def test_information_barriers(self):
        p = {r: prompts.prompt(r, self.d) for r in ("business", "modeler", "redteam", "anderson")}
        self.assertNotIn("회계 품질 분석 (forensic.json)", p["business"])  # 모듈끼리는 서로 모른다
        self.assertIn("회계 품질 분석 (forensic.json)", p["modeler"])
        self.assertNotIn("시나리오 가치", p["modeler"])                     # 모델러는 자기 가정의 결과를 미리 보지 않는다
        for r in ("redteam", "anderson"):                                   # 레드팀·1라운드는 페르소나 결론을 보지 않는다
            self.assertNotRegex(p[r], r"## \S+의 1라운드")
            self.assertNotIn("레드팀 사전 부검 (redteam.json)", p[r])
        p2 = prompts.prompt("anderson", self.d, 2)
        self.assertIn("애크먼의 1라운드", p2)
        self.assertIn("레드팀 사전 부검", p2)
        v = prompts.prompt("verifier", self.d)
        self.assertNotIn('"stance"', v)                                     # 검증자는 입장을 모른다
        self.assertIn("### V1", v)

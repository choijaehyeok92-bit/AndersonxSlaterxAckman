import json
from harness import core, journal
from harness.judge import judge
from tests.base import Base


class Journal(Base):
    def test_log_dedupes_and_explains_changes(self):
        e = journal.log(self.d, judge(self.d))
        self.assertEqual((e["id"], e["verdict"], e["changes"]), ("J1", "FOR", ["첫 판단"]))
        self.assertEqual([k["status"] for k in e["kpis"]], ["대기"] * 4)
        self.assertEqual(list(e["projection"])[:2], ["FY2026", "FY2027"])
        self.assertIsNone(journal.log(self.d, judge(self.d)))           # 같은 판단은 다시 쓰지 않는다
        self.edit("slater.2.json", stance="against", change_reason="새 근거 S6 — 휴머노이드 상용화 시점이 당겨졌다")
        e = journal.log(self.d, judge(self.d))
        self.assertEqual(e["id"], "J2")
        self.assertEqual(e["changes"][0], "판정 찬성 우세 → 반대 우세")
        self.assertIn("슬레이터 찬성(3) → 반대(3): 새 근거 S6", e["changes"][1])
        self.assertEqual(len(journal.entries(self.d)), 2)

    def update_with_results(self):
        journal.log(self.d, judge(self.d))
        ev = core.load(self.d / "evidence.json")
        ev["sources"].append({"id": "S12", "type": "filing", "title": "10-K FY2026", "url": "u12", "date": "2027-02-20"})
        core.save(self.d / "evidence.json", {**ev, "as_of": "2027-03-01"})
        self.add_facts(*[{**f, "source": "S12"} for f in (
            {"metric": "revenue", "value": 1.9e9, "unit": "USD", "period": "FY2026", "end": "2026-12-31"},
            {"metric": "ocf", "value": 2.2e8, "unit": "USD", "period": "FY2026", "end": "2026-12-31"},
            {"metric": "capex", "value": 1.0e8, "unit": "USD", "period": "FY2026", "end": "2026-12-31"},
            {"metric": "installed_base", "value": 47000, "unit": "count", "period": "FY2026", "end": "2026-12-31"},
            {"metric": "nrr", "value": 1.3, "unit": "ratio", "period": "FY2026Q4", "end": "2026-12-31"},
            {"metric": "payback_months", "value": 22, "unit": "months", "period": "FY2026Q4", "end": "2026-12-31"})])
        return journal.update(self.d)

    def test_update_checks_kpis_breaks_and_estimates(self):
        u = self.update_with_results()
        self.assertEqual(u["status"], "훼손")                             # 회수기간 22개월 > 20 — 앤더슨·레드팀 반증 조건
        self.assertEqual([k["status"] for k in u["kpis"]], ["적중", "빗나감", "적중", "대기"])
        hit = [b for b in u["breaks"] if b["status"].startswith("충족")]
        self.assertEqual({b["who"] for b in hit}, {"앤더슨", "레드팀"})
        self.assertEqual([x["status"] for x in u["must_be_true"]][0], "broken")
        dev = {(x["metric"], x["period"]): x["diff"] for x in u["deviations"]}
        self.assertAlmostEqual(dev[("revenue", "FY2026")], 1.9e9 / 1.86e9 - 1)
        self.assertAlmostEqual(dev[("fcf", "FY2026")], 1.2e8 / (1.86e9 * 0.076) - 1)
        self.assertEqual(journal.update(self.d), u)                       # 같은 대조는 다시 쓰지 않는다
        self.assertEqual(sum(e["type"] == "update" for e in journal.entries(self.d)), 1)

    def test_calibration(self):
        self.update_with_results()
        c = journal.calibrate([self.d])
        self.assertEqual(c["predictions"], 3)                             # 판단 당시 '대기'였다가 해소된 KPI만
        self.assertAlmostEqual(c["brier"], ((0.7 - 1) ** 2 + 0.65 ** 2 + (0.8 - 1) ** 2) / 3)
        self.assertEqual([(b["range"], b["n"]) for b in c["buckets"]], [("60%~70%", 1), ("70%~80%", 1), ("80%~90%", 1)])
        self.assertIn("20개 미만", c["warnings"][0])
        self.assertIn("Brier", journal.calibrate_md(c))

    def test_filter_warning(self):  # 하네스가 거의 늘 '찬성'이면 필터가 작동하지 않는다
        dirs = []
        for i in range(5):
            d = self.tmp / f"T{i}"
            d.mkdir()
            journal.append(d, {"type": "judgment", "id": "J1", "date": "2026-10-01", "verdict": "FOR", "kpis": []})
            dirs.append(d)
        c = journal.calibrate(dirs)
        self.assertEqual((c["for_share"], c["verdicts"]), (1.0, {"FOR": 5}))
        self.assertIn("필터가 작동하지 않을 수 있다", " ".join(c["warnings"]))

    def test_human_decision(self):
        self.assertRaises(ValueError, journal.decide, self.d, 0.02)       # 판단 전에는 기록할 수 없다
        journal.log(self.d, judge(self.d))
        e = journal.decide(self.d, 0.015, "작게 시작 — 원가 곡선 확인 후 증액")
        self.assertEqual((e["type"], e["ref"], e["size"], e["suggested"]), ("decision", "J1", 0.015, 0.0))
        self.assertRaises(ValueError, journal.decide, self.d, 1.5)
        self.assertEqual(json.loads((self.d / "journal.jsonl").read_text(encoding="utf-8").splitlines()[-1])["note"],
                         "작게 시작 — 원가 곡선 확인 후 증액")

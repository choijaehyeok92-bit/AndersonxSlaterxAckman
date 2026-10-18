import json
from council import main
from tests.base import Base


class Main(Base):
    def test_exit_codes_and_outputs(self):
        code, out = self.quiet(main, ["judge", str(self.d)])
        self.assertEqual(code, 0)
        self.assertIn("찬성 우세", out)
        self.assertTrue((self.d / "report.md").exists() and (self.d / "journal.jsonl").exists())
        self.edit("slater.2.json", stance="against")
        code, out = self.quiet(main, ["judge", str(self.d), "--json", "--no-log"])
        self.assertEqual((code, json.loads(out)["verdict"]), (1, "AGAINST"))
        self.assertEqual(len((self.d / "journal.jsonl").read_text(encoding="utf-8").splitlines()), 1)  # --no-log는 기록하지 않는다
        self.assertEqual(self.quiet(main, ["judge", str(self.d / "missing")])[0], 2)

    def test_calc_prompt_decide_calibrate(self):
        code, out = self.quiet(main, ["calc", str(self.d), "--case", '{"anderson": {"from": "base"}}', "--json"])
        self.assertEqual(code, 0)
        self.assertLess(json.loads(out)["personas"]["anderson"]["upside_10y"], 5)
        self.assertTrue((self.d / "analysis.json").exists())
        code, out = self.quiet(main, ["prompt", "verifier", str(self.d)])
        self.assertIn("role=verifier", out)
        self.quiet(main, ["judge", str(self.d)])
        code, out = self.quiet(main, ["decide", str(self.d), "--size", "0.02", "--note", "시작"])
        self.assertEqual(code, 0)
        self.assertIn("비중 2.0%", out)
        code, out = self.quiet(main, ["update", str(self.d)])
        self.assertEqual(code, 0)                                         # 새 실적 없음 → 유지
        self.assertIn("유지", out)
        code, out = self.quiet(main, ["calibrate", str(self.d)])
        self.assertIn("해소된 예측 0개", out)

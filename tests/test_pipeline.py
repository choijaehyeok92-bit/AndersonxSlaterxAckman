import shutil, sys
from harness import core, pipeline
from tests.base import EX, Base

OUTPUTS = ("business.json", "management.json", "forensic.json", "model.json", "redteam.json", "verifier.json",
           *(f"{a}.{r}.json" for a in core.AGENTS for r in (1, 2)))


class Run(Base):
    def setUp(self):
        super().setUp()
        for f in OUTPUTS:
            (self.d / f).unlink()
        self.edit("evidence.json", researched=None)

    def test_full_pipeline_with_any_cli(self):  # 프롬프트를 stdin으로 받는 CLI면 무엇이든 — 여기선 가짜 CLI
        cli = self.cli()
        r, _ = self.quiet(pipeline.run, self.d, "NOVA", cli)
        self.assertEqual((r["verdict"], r["score"], r["label"]), ("FOR", 0.25, "찬성 우세"))
        calls = self.called()
        self.assertEqual(calls[0], "researcher.1")
        self.assertEqual(sorted(calls[1:4]), ["business.1", "forensic.1", "management.1"])
        self.assertEqual(calls[4], "modeler.1")
        self.assertEqual(sorted(calls[5:10]), ["ackman.1", "anderson.1", "klarman.1", "redteam.1", "slater.1"])
        self.assertEqual(sorted(calls[10:14]), ["ackman.2", "anderson.2", "klarman.2", "slater.2"])
        self.assertEqual(calls[14:], ["verifier.1"])
        self.assertTrue(core.load(self.d / "evidence.json")["researched"])
        self.assertEqual(core.load(self.d / "forensic.json")["basis"], core.basis(self.d, "evidence"))
        self.assertEqual(r["verification"]["counts"]["contradicted"], 0)
        self.calls.unlink()
        self.quiet(pipeline.run, self.d, "NOVA", cli)                  # 끝난 단계는 건너뛴다
        self.assertEqual(self.called(), [])

    def test_stale_upstream_reruns_downstream(self):
        cli = self.cli()
        self.quiet(pipeline.run, self.d, "NOVA", cli)
        self.calls.unlink()
        self.add_facts({"metric": "nrr", "value": 1.35, "unit": "ratio", "period": "FY2026Q1", "end": "2026-03-31", "source": "S3"})
        self.quiet(pipeline.run, self.d, "NOVA", cli)                  # 사실이 바뀌면 모듈부터 다시 — 사실 → 모델 → 판단
        self.assertEqual(len(self.called()), 14)
        self.assertNotIn("researcher.1", self.called())

    def test_forensic_gate_stops_pipeline(self):
        src = self.tmp / "src"
        shutil.copytree(EX, src)
        core.save(src / "forensic.json", {**core.load(src / "forensic.json"), "grade": "red_flag"})
        r, _ = self.quiet(pipeline.run, self.d, "NOVA", self.cli(src))
        self.assertEqual((r["verdict"], r["agents"]), ("AGAINST", []))
        self.assertNotIn("modeler.1", self.called())                   # 회계를 믿을 수 없으면 모델을 돌리지 않는다
        self.assertFalse((self.d / "model.json").exists())

    def test_evidence_gate_stops_pipeline(self):
        ev = core.load(self.d / "evidence.json")
        core.save(self.d / "evidence.json", {**ev, "facts": [f for f in ev["facts"] if f["metric"] != "price"]})
        r, _ = self.quiet(pipeline.run, self.d, "NOVA", self.cli())
        self.assertEqual((r["verdict"], self.called()), ("INCOMPLETE", ["researcher.1"]))


class Ask(Base):
    def test_retry_once_then_fail(self):
        flaky = self.tmp / "flaky.py"
        flaky.write_text('import sys, pathlib\np = pathlib.Path(sys.argv[1])\nn = int(p.read_text()) if p.exists() else 0\n'
                         'p.write_text(str(n + 1))\nprint("not json" if n == 0 else \'{"grade": "watch"}\')\n', encoding="utf-8")
        cli = f'"{sys.executable}" "{flaky}" "{self.tmp / "n"}"'
        self.assertEqual(pipeline.ask(cli, "x", "forensic"), {"grade": "watch"})
        bad = f'"{sys.executable}" -c "print(\'{{}}\')"'
        self.assertRaises(ValueError, pipeline.ask, bad, "x", "forensic")

    def test_modeler_growth_keys_must_be_drivers(self):
        sc = lambda g: {k: {"p": 0.3, "growth": g, "fcf_margin": 0.2, "exit_multiple": 20} for k in ("bear", "base", "bull")}
        self.assertIn("revenue_growth", pipeline.check("modeler", 1, {"scenarios": sc({"revenue_growth": 0.2})}))
        self.assertIsNone(pipeline.check("modeler", 1, {"scenarios": sc({"revenue": 0.2})}))
        self.assertIsNone(pipeline.check("modeler", 1, {"drivers": [{"name": "units"}], "scenarios": sc({"units": [0.3, 0.2]})}))

    def test_cli_failure(self):
        self.assertRaises(RuntimeError, pipeline.ask, f'"{sys.executable}" -c "import sys; sys.exit(3)"', "x")


class HarnessTests(Base):
    def test_repro(self):
        r, _ = self.quiet(pipeline.repro, self.d, self.cli(), 2)
        self.assertTrue(r["ok"] and r["verdict_agree"] and r["agents_agree"])
        self.assertEqual((r["iv_spread"], r["irr_spread"]), (0.0, 0.0))
        self.assertTrue((self.d / "repro" / "run2" / "verifier.json").exists())
        self.assertFalse((self.d / "repro" / "run1" / "view.json").exists())  # 사용자 견해는 복사하지 않는다

    def test_audit_error_injection(self):
        r = pipeline.audit(self.d, self.cli(), n=5)
        self.assertEqual((r["injected"], r["caught_by_verifier"], r["flagged_clean"], r["false_alarms"]), (5, 5, 0, 0))
        self.assertGreaterEqual(r["caught_by_code"], 4)                  # 틀린 숫자는 인용 자료와 대조해 대부분 잡힌다
        self.assertTrue(r["ok"])
        self.assertEqual(pipeline.corrupt("순매출유지율 138% 유지", 1.5), ("순매출유지율 207% 유지", "207"))
        self.assertEqual(pipeline.corrupt("매출 1,800억 달러", 2)[0], "매출 3,600억 달러")

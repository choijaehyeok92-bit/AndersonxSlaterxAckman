import io, json, shutil, sys, tempfile, unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import date
from pathlib import Path
from unittest import mock
import council
from council import collect, judge, load, main, prompt, render, save

EX = Path(__file__).parent / "examples" / "NOVA"
FAKE_CLI = r'''import re, sys
t = sys.stdin.read()
role, rnd = re.search(r"role=(\w+) round=(\d)", t).groups()
out = (re.search(r"## evidence.json\n```json\n(.*)\n```", t, re.S).group(1) if role == "researcher"
       else open(f"{sys.argv[1]}/{role}.{rnd}.json", encoding="utf-8").read())
print("설명 문장이 앞에 붙어도 된다.\n```json\n" + out + "\n```")
'''


class Base(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp()) / "NOVA"
        shutil.copytree(EX, self.d, ignore=shutil.ignore_patterns("debate.md"))
        self.addCleanup(shutil.rmtree, self.d.parent)

    def edit(self, name, **kw):
        save(self.d / name, {**load(self.d / name), **kw})


class Judge(Base):
    def test_example(self):
        r = judge(self.d)
        self.assertEqual((r["verdict"], r["label"], r["score"]), ("FOR", "찬성 우세", 0.33))
        self.assertEqual([(x["opening"], x["final"], x["conviction"]) for x in r["agents"]],
                         [("for", "for", 5), ("for", "for", 3), ("against", "against", 3)])
        self.assertEqual([x["warnings"] for x in r["agents"]] + [r["notes"]], [[], [], [], []])
        self.assertIn("[at_risk] 휴머노이드", render(r))  # 2라운드 metrics가 1라운드를 덮어씀

    def test_red_line_overrides_words(self):  # 자기 원칙을 어긴 '찬성'은 '반대'로 집계
        self.edit("ackman.2.json", stance="for")
        self.edit("anderson.2.json", metrics={"upside_10y": 4})
        r = judge(self.d)
        self.assertEqual([(x["stance"], x["final"]) for x in r["agents"]],
                         [("for", "against"), ("for", "for"), ("for", "against")])
        self.assertEqual((r["verdict"], r["label"]), ("AGAINST", "반대 우세"))
        self.assertIn("안전마진", " ".join(r["agents"][2]["red_lines"]))

    def test_slater_red_lines(self):
        for metrics in ({"unit_economics": "deteriorating"}, {"survival_path": False}, {"must_be_true": []},
                        {"must_be_true": [{"claim": "회수기간 18개월 이하", "status": "broken"}]}):
            self.edit("slater.2.json", metrics=metrics)
            self.assertEqual(judge(self.d)["agents"][1]["final"], "against", metrics)

    def test_evidence_discipline(self):
        self.edit("slater.1.json", arguments=[{"point": "근거 없음"}, {"point": "가짜", "cites": ["S99"]}])
        self.edit("slater.2.json", metrics={"must_be_true": [{"claim": "목표주가 200달러", "status": "on_track"}]})
        self.edit("ackman.2.json", rebuttals=[{"to": "anderson", "point": "x", "cites": ["S1"]}])
        r = judge(self.d)
        w = " ".join(r["agents"][1]["warnings"])
        self.assertTrue(all(k in w for k in ("근거 없는 주장", "S99", "가격 기반")))
        self.assertEqual(r["agents"][2]["warnings"], ["슬레이터에 대한 반론 없음"])

    def test_unanimous_and_round1_only(self):
        for a in council.AGENTS:
            (self.d / f"{a}.2.json").unlink()
        self.edit("ackman.1.json", stance="abstain")
        r = judge(self.d)
        self.assertEqual((r["label"], r["votes"]), ("찬성 우세", {"for": 2, "against": 0, "abstain": 1}))
        self.edit("anderson.1.json", stance="abstain")
        self.edit("slater.1.json", stance="abstain")
        self.assertEqual(judge(self.d)["label"], "만장일치 보류")

    def test_bad_input(self):
        self.edit("evidence.json", sources=[{"id": "S1", "type": "blog", "url": "x"}])
        self.assertRaises(ValueError, judge, self.d)


class Prompt(Base):
    def test_round_isolation(self):
        p1, p2 = prompt("slater", self.d, 1), prompt("slater", self.d, 2)
        self.assertIn("role=slater round=1", p1)
        self.assertTrue(all(k in p1 for k in ("토론 규칙", "톰 슬레이터", '"id": "S8"')))
        self.assertNotIn("앤더슨의 1라운드", p1)  # 1라운드는 다른 에이전트를 보지 않는다
        self.assertTrue(all(k in p2 for k in ("앤더슨의 1라운드", "애크먼의 1라운드", "슬레이터의 1라운드 (너 자신)")))
        self.assertIn("체크리스트", prompt("researcher", self.d))


class Collect(unittest.TestCase):
    def test_sec_news_merge(self):
        today = date.today().isoformat()
        sub = {"filings": {"recent": {"form": ["8-K", "4", "10-Q", "10-K"], "filingDate": [today, today, today, "2001-01-01"],
                                      "accessionNumber": ["0001-26-1", "0001-26-2", "0001-26-3", "0001-01-4"],
                                      "primaryDocument": ["a.htm", "b.xml", "c.htm", "d.htm"],
                                      "items": ["2.02,9.01", "", "", ""]}}}
        rss = (b"<rss><channel><item><title>Nvidia beats - Reuters</title><link>https://news.example/1</link>"
               b"<pubDate>Thu, 15 Oct 2026 10:00:00 GMT</pubDate><source url='x'>Reuters</source></item></channel></rss>")
        fake = lambda url: (json.dumps({"0": {"cik_str": 1045810, "ticker": "NVDA"}}).encode() if "tickers" in url
                            else json.dumps(sub).encode() if "submissions" in url else rss)
        d = Path(tempfile.mkdtemp()) / "NVDA"
        self.addCleanup(shutil.rmtree, d.parent)
        with mock.patch.object(council, "fetch", fake):
            r = collect(d, "NVDA")
            self.assertEqual((r["added"], collect(d, "NVDA")["added"]), (3, 0))  # 재수집은 중복 없이 병합
        s = load(d / "evidence.json")["sources"]
        self.assertEqual([(x["id"], x["type"], x["title"]) for x in s],
                         [("S1", "filing", "8-K 실적 발표"), ("S2", "filing", "10-Q"), ("S3", "news", "Nvidia beats - Reuters")])
        self.assertEqual(s[0]["url"], "https://www.sec.gov/Archives/edgar/data/1045810/0001261/a.htm")
        self.assertEqual(s[2]["date"], "2026-10-15")

    def test_offline(self):
        d = Path(tempfile.mkdtemp()) / "X"
        self.addCleanup(shutil.rmtree, d.parent)
        with mock.patch.object(council, "fetch", side_effect=OSError("blocked")):
            r = collect(d, "X")
        self.assertEqual((r["total"], len(r["errors"])), (0, 2))


class Run(Base):
    def test_any_cli(self):  # 프롬프트를 stdin으로 받는 CLI면 무엇이든 — 여기선 가짜 CLI
        for f in self.d.glob("*.json"):
            if f.name != "evidence.json":
                f.unlink()
        self.edit("evidence.json", researched=None)
        cli_py = self.d.parent / "fake_cli.py"
        cli_py.write_text(FAKE_CLI, encoding="utf-8")
        with redirect_stderr(io.StringIO()):
            r = council.run(self.d, "NOVA", f'"{sys.executable}" "{cli_py}" "{EX}"')
        self.assertEqual((r["verdict"], r["score"]), ("FOR", 0.33))
        self.assertTrue(load(self.d / "evidence.json")["researched"])
        self.assertEqual(load(self.d / "ackman.2.json"), load(EX / "ackman.2.json"))

    def test_cli_failure(self):
        self.assertRaises(RuntimeError, council.ask, f'"{sys.executable}" -c "import sys; sys.exit(3)"', "x")


class Main(Base):
    def test_exit_codes(self):
        with redirect_stdout(io.StringIO()) as out, redirect_stderr(io.StringIO()):
            self.assertEqual(main(["judge", str(self.d)]), 0)
            self.assertIn("찬성 우세", out.getvalue())
            self.assertTrue((self.d / "debate.md").exists())
            self.edit("slater.2.json", stance="against")
            self.assertEqual(main(["judge", str(self.d), "--json"]), 1)
            self.assertEqual(main(["judge", str(self.d / "missing")]), 2)


if __name__ == "__main__":
    unittest.main()

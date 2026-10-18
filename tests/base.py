import io, shutil, sys, tempfile, unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from harness import core

ROOT = Path(__file__).resolve().parent.parent
EX = ROOT / "examples" / "NOVA"
# 프롬프트를 stdin으로 받는 가짜 CLI: 역할별로 예시 파일을 돌려준다. argv: 예시 폴더, 호출 기록 파일
FAKE_CLI = r'''import json, re, sys
from pathlib import Path
t = sys.stdin.read()
role, rnd = re.search(r"role=(\w+) round=(\d)", t).groups()
src, log = Path(sys.argv[1]), sys.argv[2]
open(log, "a", encoding="utf-8").write(f"{role}.{rnd}\n")
if role == "researcher":
    out = {"sources": [], "facts": [], "gaps": ["가짜 리서처"]}
elif role == "verifier":
    sys.path.insert(0, sys.argv[3])
    from harness import prompts
    orig = {c["point"] for c in prompts.claims(src)[0]}
    out = {"checks": [{"id": i, "verdict": "supported" if p.strip() in orig else "contradicted", "reason": "가짜"}
                      for i, p in re.findall(r"### (V\d+)\n주장: (.*)", t)]}
else:
    name = f"{role}.{rnd}.json" if role in ("anderson", "slater", "ackman", "klarman") else "model.json" if role == "modeler" else f"{role}.json"
    out = json.loads((src / name).read_text(encoding="utf-8"))
print("설명 문장이 앞에 붙어도 된다.\n```json\n" + json.dumps(out, ensure_ascii=False) + "\n```")
'''


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.d = self.tmp / "NOVA"
        shutil.copytree(EX, self.d, ignore=shutil.ignore_patterns("report.md"))

    def edit(self, name, **kw):
        core.save(self.d / name, {**core.load(self.d / name), **kw})

    def fact(self, fid, **kw):  # evidence.json의 사실 하나를 고친다
        ev = core.load(self.d / "evidence.json")
        ev["facts"] = [{**f, **kw} if f["id"] == fid else f for f in ev["facts"]]
        core.save(self.d / "evidence.json", ev)

    def add_facts(self, *facts, **ev_kw):
        ev = core.load(self.d / "evidence.json")
        n = max(int(f["id"][1:]) for f in ev["facts"])
        ev["facts"] += [{"id": f"F{n + i}", **f} for i, f in enumerate(facts, 1)]
        core.save(self.d / "evidence.json", {**ev, **ev_kw})

    def cli(self, src=EX):
        py = self.tmp / "fake_cli.py"
        py.write_text(FAKE_CLI, encoding="utf-8")
        self.calls = self.tmp / "calls.log"
        return f'"{sys.executable}" "{py}" "{src}" "{self.calls}" "{ROOT}"'

    def called(self):
        return self.calls.read_text(encoding="utf-8").split() if self.calls.exists() else []

    def quiet(self, fn, *a, **kw):
        with redirect_stdout(io.StringIO()) as out, redirect_stderr(io.StringIO()):
            r = fn(*a, **kw)
        return r, out.getvalue()

"""공통 — 경로·입출력·역할 이름·입력 해시."""
import hashlib, json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS = {"anderson": "앤더슨", "slater": "슬레이터", "ackman": "애크먼"}          # L5 판단 — 표를 던진다
MODULES = {"business": "사업·산업", "management": "경영진·자본배분", "forensic": "회계 품질"}  # L4 분석
ROLES = {"researcher": "리서처", **MODULES, "modeler": "모델러", **AGENTS, "redteam": "레드팀", "verifier": "검증자"}
STANCE = {"for": ("찬성", 1), "against": ("반대", -1), "abstain": ("보류", 0)}
TYPES = ("filing", "call", "conference", "news", "data")
BASES = ("reported", "guidance", "consensus", "market")
ITEMS = {"1.01": "중요 계약", "2.01": "인수·매각", "2.02": "실적 발표", "4.01": "감사인 변경", "4.02": "재무제표 정정",
         "5.02": "경영진 변동", "7.01": "IR·컨퍼런스 자료", "8.01": "기타 중요 사항"}  # 8-K 항목


def today():
    return date.today().isoformat()


def load(p, default=None):
    if default is not None and not Path(p).exists():
        return default
    return json.loads(Path(p).read_text(encoding="utf-8"))


def save(p, data):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def folder(t):
    return Path(t) if Path(t).is_dir() else ROOT / "research" / t.upper()


def doc(name):
    return (ROOT / "agents" / f"{name}.md").read_text(encoding="utf-8")


def items(xs, key):  # LLM이 객체 대신 문자열을 써도 깨지지 않게 {key: 문자열}로 받는다
    return [x if isinstance(x, dict) else {key: str(x)} for x in (xs if isinstance(xs, list) else [])]


def digest(*objs):  # 입력 지문 — 출력이 어떤 근거·모델 위에서 쓰였는지 (basis 필드는 제외)
    strip = lambda o: {k: v for k, v in o.items() if k != "basis"} if isinstance(o, dict) else o
    raw = json.dumps([strip(o) for o in objs], ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]


def basis(d, stage):
    """단계별 입력 지문. 사실 → 모듈 → 모델 → 판단의 단방향 사슬이라 앞 단계가 바뀌면 뒤 단계가 모두 낡는다."""
    ev = load(d / "evidence.json")
    facts = {k: ev.get(k) for k in ("as_of", "sources", "facts")}
    if stage == "evidence":
        return digest(facts)
    mods = [load(d / f"{m}.json", {}) for m in MODULES]
    if stage == "modules":
        return digest(facts, *mods)
    return digest(facts, *mods, load(d / "model.json", {}))  # "model": 페르소나·레드팀


STAGE = {**{m: "evidence" for m in MODULES}, "modeler": "modules", **{a: "model" for a in AGENTS}, "redteam": "model"}

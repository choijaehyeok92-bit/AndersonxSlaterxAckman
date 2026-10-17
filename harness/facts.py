"""L2 사실 저장소 — 모든 숫자는 값·단위·기간·출처로 저장하고, 출처 없는 숫자는 쓰지 못하게 한다."""
import math, re
from functools import lru_cache
from . import core

PERIOD = re.compile(r"^FY(\d{4})(Q[1-4]|H[12])?$")
UNIT = re.compile(r"^([A-Z]{3}(/share|/ADR|/[A-Z]{3})?|shares(/ADR)?|ratio|count|months|x)$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RANK = {"filing": 0, "call": 1, "conference": 2, "data": 3, "news": 4}  # 같은 값이 여럿이면 1차 자료 우선
CITE = re.compile(r"^(S\d+|F\d+|C:\S+)$")


def sources(ev):  # 근거 검증 → {id: 근거}. 근거 목록이 깨지면 판정 자체를 하지 않는다
    out = {}
    for s in ev.get("sources", []):
        if s.get("type") not in core.TYPES or not s.get("url") or not re.match(r"^S\d+$", str(s.get("id"))) or s["id"] in out:
            raise ValueError(f"근거 {s.get('id')}: id(S숫자)·type({'|'.join(core.TYPES)})·url 필수, id 중복 불가")
        out[s["id"]] = s
    return out


class Facts:
    """검증을 통과한 사실만 담는다. 통과하지 못한 사실은 제외하고 이유를 warnings에 남긴다."""

    def __init__(self, ev):
        self.ev, self.as_of = ev, ev.get("as_of") or core.today()
        self.src, self.facts, self.warnings = sources(ev), {}, []
        self.future = {k for k, s in self.src.items() if (s.get("date") or "") > self.as_of}
        for f in ev.get("facts", []):
            why = self.check(f)
            if why:
                self.warnings.append(f"사실 {f.get('id')} 제외 — {why}")
            else:
                self.facts[f["id"]] = {"basis": "reported", **f}
        groups = {}
        for f in self.facts.values():
            if f["basis"] == "reported":
                groups.setdefault((f["metric"], f.get("period") or f["end"], f["unit"]), []).append(f)
        for (m, p, _), fs in groups.items():
            vals = sorted({f["value"] for f in fs})
            if len(vals) > 1 and abs(vals[-1] - vals[0]) > 0.01 * max(abs(vals[-1]), abs(vals[0])):
                self.warnings.append(f"사실 충돌 {m} {p}: " + ", ".join(f"{f['id']}={f['value']:g}" for f in fs)
                                     + " — 1차 자료 우선으로 하나만 쓴다")

    def check(self, f):
        if not re.match(r"^F\d+$", str(f.get("id"))) or f.get("id") in self.facts:
            return "id는 F숫자, 중복 불가"
        if not re.match(r"^[a-z][a-z0-9_]*$", str(f.get("metric"))):
            return "metric은 snake_case"
        if not isinstance(f.get("value"), (int, float)) or isinstance(f.get("value"), bool) or not math.isfinite(f["value"]):
            return "value는 숫자"
        if not UNIT.match(str(f.get("unit"))):
            return f"unit '{f.get('unit')}' — USD·KRW·USD/share·USD/ADR·shares·shares/ADR·ratio·count·months·x·KRW/USD"
        if not DATE.match(str(f.get("end"))):
            return "end는 YYYY-MM-DD"
        if f.get("source") not in self.src:
            return f"출처 {f.get('source')} 없음 — 출처 없는 숫자는 쓰지 않는다"
        if f.get("basis", "reported") not in core.BASES:
            return f"basis는 {'|'.join(core.BASES)}"
        p = PERIOD.match(f.get("period") or "FY" + f["end"][:4])
        if not p:
            return "period는 FY2025·FY2025Q2 형식"
        if abs(int(p.group(1)) - int(f["end"][:4])) > 1:
            return f"기간 {f['period']}과 종료일 {f['end']} 불일치 — 회계연도 라벨 확인"
        if f["unit"] == "ratio" and abs(f["value"]) > 10:
            return f"ratio {f['value']} — 비율은 0.31처럼 쓴다 (31%를 31로 쓴 단위 오류 의심)"
        if f.get("basis", "reported") in ("reported", "market") and f["end"] > self.as_of:
            return f"기준일({self.as_of}) 이후 실적 — 미래 정보 누출"
        if f["source"] in self.future:
            return f"출처 {f['source']}가 기준일({self.as_of}) 이후 자료"
        return None

    def pick(self, fs):  # 연결 > 별도, 1차 자료 > 직접 보고 > 최신 자료
        fs = sorted(fs, key=lambda f: self.src[f["source"]].get("date") or "", reverse=True)
        return min(fs, key=lambda f: (f.get("scope") == "separate", RANK[self.src[f["source"]]["type"]], f.get("derived", False)))

    def get(self, metric, period=None, basis="reported", unit=None):
        """기간을 주면 그 기간 값, 안 주면 종료일이 가장 늦은 값. 같은 값이 여럿이면 1차 자료."""
        fs = [f for f in self.facts.values() if f["metric"] == metric and f["basis"] == basis
              and (period is None or f.get("period") == period) and (unit is None or f["unit"] == unit)]
        if not fs:
            return None
        if period is None:
            last = max(f["end"] for f in fs)
            fs = [f for f in fs if f["end"] == last]
        if basis in ("guidance", "consensus"):  # 전망치는 자료 유형보다 날짜가 먼저 — 상향·하향된 최신 가이던스가 옛 1차 자료를 이긴다
            top = max(self.src[f["source"]].get("date") or "" for f in fs)
            fs = [f for f in fs if (self.src[f["source"]].get("date") or "") == top]
        return self.pick(fs)

    def value(self, metric, period=None, basis="reported", unit=None):
        f = self.get(metric, period, basis, unit)
        return f["value"] if f else None


# ── 숫자 추적: 주장 속 숫자가 인용한 근거·코드 계산값·페르소나 원칙 중 어디서 왔는지 대조한다 ──
# 숫자는 종류를 나눠 비교한다 — 퍼센트(%·%p)는 비율 사실·비율 계산값과, 나머지는 금액·개수·배수와만.

SCALE = {"조": 1e12, "억": 1e8, "만": 1e4, "천": 1e3, "trillion": 1e12, "billion": 1e9, "million": 1e6,
         "bn": 1e9, "mn": 1e6, "T": 1e12, "B": 1e9, "M": 1e6, "K": 1e3, "k": 1e3}
UNITS = "%p|%|bp|배|x|달러|원|개월|주|명|대|건|곳|개|USD|KRW"
NUM = re.compile(rf"(?<![A-Za-z0-9.,])(\$)?(\d{{1,3}}(?:,\d{{3}})+|\d+)(\.\d+)?\s?({'|'.join(SCALE)})?\s?({UNITS})?(?![A-Za-z])")
RATIO = {"revenue_growth", "gross_margin", "operating_margin", "fcf_margin", "fcf_conversion", "sbc_to_revenue", "sbc_to_ocf",
         "roic", "share_change", "accruals_ratio", "fcf_yield", "implied_cagr", "irr", "expected_irr", "p_loss", "mos",
         "consensus_diff", "guidance_hit_rate", "base_rate", "p", "revenue_cagr", "receivables_growth", "inventory_growth",
         "deferred_revenue_growth", "goodwill_to_assets", "capitalized_to_revenue", "ocf_to_ni", "accruals", "receivables_gap",
         "inventory_gap", "dilution", "capitalized", "goodwill", "deferred_revenue", "discount_rate"}


def numbers(text, strict=False):
    """텍스트 속 숫자 → [(종류 pct|raw, 값, 허용오차)]. strict면 단위·배수가 붙은 숫자만 (연도·'1번 질문' 제외)."""
    out = []
    for m in NUM.finditer(str(text)):
        dollar, whole, frac, scale, unit = m.groups()
        if strict and not (dollar or scale or unit):
            continue
        mult = SCALE.get(scale or "", 1)
        out.append(("pct" if unit in ("%", "%p") else "raw", float(whole.replace(",", "") + (frac or "")) * mult,
                    0.5 * 10 ** -len((frac or ".")[1:]) * mult))
    return out


def loose(x, ref=None):
    """가정·원칙 문서 같은 자유 형식에서 대조용 숫자 → [(종류, 값, 출처)]. 1 이하 소수는 비율로도 본다."""
    if isinstance(x, bool) or x is None:
        return []
    if isinstance(x, (int, float)):
        return [("raw", x, ref)] + ([("pct", x * 100, ref)] if abs(x) <= 1 else [])
    if isinstance(x, dict):
        return [c for k, y in x.items() if k not in ("id", "source", "date", "end", "url", "period") for c in loose(y, ref)]
    if isinstance(x, list):
        return [c for y in x for c in loose(y, ref)]
    return [(k, v, ref) for k, v, _ in numbers(x)] + [("pct", v * 100, ref) for k, v, _ in numbers(x) if k == "raw" and 0 < v < 1]


def pool(src=(), fs=(), refs=None, pct=None):
    """근거 문장·사실 값·계산값 → [(종류, 값, ID)]. 비율 사실과 비율 계산값(pct 목록, 없으면 키 이름)은 퍼센트로 본다."""
    pct = set(pct) if pct is not None else None
    out = [(k, v, s["id"]) for s in src for k, v, _ in numbers(f"{s.get('title', '')} {s.get('note', '')}")]
    for f in fs:
        for v in (f["value"], f.get("low"), f.get("high")):
            if isinstance(v, (int, float)):
                out.append(("pct", v * 100, f["id"]) if f["unit"] == "ratio" else ("raw", v, f["id"]))
    for k, v in (refs or {}).items():
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            ratio = k in pct if pct is not None else k[2:].split("@")[0] in RATIO
            out.append(("pct", v * 100, k) if ratio else ("raw", v, k))
    return out


def hits(kind, v, tol, cands):
    return [r for k, x, r in cands if k == kind and abs(abs(v) - abs(x)) <= max(tol, 0.005 * max(abs(v), abs(x)), 1e-9)]


@lru_cache(maxsize=None)
def doctrine(role):  # 역할 문서에 있는 숫자 (예: 앤더슨의 '5배', 베셈바인더의 '4%')
    names = [role] + (["debate"] if role in core.AGENTS else [])
    return tuple(c for n in names for c in loose(core.doc(n)))


def trace(point, cited, everything, allowed=()):
    """→ [(숫자, 그 숫자가 실제로 있는 ID들)]. 인용한 자료·허용 목록 어디에도 없는 숫자만 돌려준다.
    '추정:'으로 시작하는 주장은 계산 근거를 밝힌 추정이라 대조하지 않는다."""
    if str(point).lstrip().startswith("추정"):
        return []
    out = []
    for kind, v, tol in numbers(point, strict=True):
        if not hits(kind, v, tol, cited) and not hits(kind, v, tol, allowed):
            out.append((f"{v:g}{'%' if kind == 'pct' else ''}", sorted({r for r in hits(kind, v, tol, everything) if r})))
    return out

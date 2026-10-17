"""판정 규칙 — 하네스의 모든 문턱값은 이 파일 하나에 있다.

agents/*.md의 '레드라인'·'게이트'·'검증' 절과 같아야 한다. 규칙을 바꿀 때는 두 곳을 함께 바꾼다.
문턱값 대부분은 하네스 기본값이다 — 투자자 본인이 공표한 수치가 아니다.
"""
import re

WEIGHTS = {"anderson": 1, "slater": 1, "ackman": 1}   # 표결 가중치

# 페르소나 레드라인
UPSIDE, REVENUE_5Y = 5.0, 2.0      # 앤더슨: 10년 주당가치 5배 (LTGG Q10) · 5년 매출 2배 (Q1)
MOS, LEVERAGE = 0.20, 4.0          # 애크먼: 안전마진 20% · 순부채/EBITDA 4배 초과 = 자본시장 의존

# L3 계산 기본값 — 모델러가 model.json에서 바꿀 수 있다
DISCOUNT, TERMINAL_G, HORIZON = 0.10, 0.03, 5   # 할인율 · 역DCF 영구성장률 · 모델 기간(년)
REVERSE_YEARS = 10                              # 역DCF 명시 기간

# 게이트 — 앞 단계에서 걸리면 뒤 단계를 돌리지 않는다
MIN_REVENUE_YEARS = 2              # 근거 충분성: 연간 매출 2개 기간 이상 + 주가 + 주식 수 + 공시 1건 이상

# L4 회계 품질 신호 (코드가 계산 → forensic 역할이 해석)
FORENSIC = {
    "ocf_to_ni": 0.8,          # 3년 누적 영업현금흐름/순이익 하한
    "accruals": 0.10,          # (순이익-영업현금흐름)/평균 총자산 상한 (Sloan 1996)
    "wc_gap": 0.15,            # 매출채권·재고 증가율 - 매출 증가율 상한 (15%p)
    "sbc_to_revenue": 0.10,    # SBC/매출 상한
    "sbc_to_ocf": 0.50,        # SBC/영업현금흐름 상한
    "dilution": 0.03,          # 희석 주식 수 연평균 증가율 상한
    "goodwill": 0.40,          # 영업권/총자산 상한
    "non_gaap_gap": 0.30,      # (Non-GAAP - GAAP)/|Non-GAAP| 상한
    "capitalized": 0.02,       # 자본화 소프트웨어/매출 2년 증가폭 상한 (2%p)
}

# L5·L6 판단 규율
VARIANT_GAP = 0.05       # 모델과 컨센서스·시장 내재 성장의 차이가 이보다 작으면 'variant perception 없음'
RARE = 0.10              # 기본 시나리오 성장률을 달성한 기업 비율이 이보다 낮으면 서사 과적합 경고
VERIFY_FAIL = 0.5        # 논거 중 검증 실패(근거 없음·반박됨) 비율이 이 이상이면 그 표는 '보류'로 집계
KELLY, MAX_WEIGHT = 0.25, 0.10   # 비중 참고값: 1/4 켈리, 상한 10% — 최종 비중은 사람이 정한다

PRICE = re.compile(r"주가|목표\s*주?가|share price|stock price|price target|target price", re.I)


def _fails(m, key, ok):
    return m.get(key) is None or not ok(m[key])


RED_LINES = {  # '찬성'하려면 자기 원칙을 통과해야 한다. m = 페르소나 지표 + 코드 계산값(계산값 우선)
    "anderson": [(lambda m: not _fails(m, "upside_10y", lambda v: v >= UPSIDE),
                  f"10년 주당가치 {UPSIDE:g}배 미만 또는 계산 불가 (LTGG Q10)")],
    "slater": [(lambda m: m.get("unit_economics") != "deteriorating", "단위경제 악화 — CAC 상승·이탈률 악화"),
               (lambda m: m.get("survival_path") is not False, "외부 자본 없이 생존할 경로가 없음"),
               (lambda m: m.get("cash_survives") is not False, "기본 시나리오에서 현금 고갈 (코드 계산)"),
               (lambda m: bool(m.get("must_be_true")), "참이어야 하는 것(must_be_true) 미작성"),
               (lambda m: all(x.get("status") != "broken" for x in m.get("must_be_true", [])), "이미 반증된 가설")],
    "ackman": [(lambda m: m.get("simple_predictable") is True, "단순·예측 가능한 사업이 아님"),
               (lambda m: m.get("fcf_positive") is True, "잉여현금흐름을 만들지 못함 (코드 계산)"),
               (lambda m: m.get("capital_markets_dependent") is False, "레버리지·자본시장 의존"),
               (lambda m: not _fails(m, "mos", lambda v: v >= MOS), f"안전마진 {MOS:.0%} 미만 또는 계산 불가")],
}


def soft(a, m):  # 경고만 하는 원칙
    if a == "anderson" and (m.get("revenue_5y") or 0) < REVENUE_5Y:
        return [f"5년 매출 {m.get('revenue_5y') or 0:.2f}배 < {REVENUE_5Y:g}배 (LTGG Q1)"]
    if a == "slater":  # 점검 항목은 가격이 아니라 운영 지표
        return [f"가격 기반 검증 항목 — 운영 지표로 교체: {x.get('claim')}"
                for x in m.get("must_be_true", []) if PRICE.search(x.get("claim", ""))]
    return []

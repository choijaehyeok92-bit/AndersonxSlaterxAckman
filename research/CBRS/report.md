# Cerebras Systems (CBRS) 리서치 보고서 — 기준일 2026-10-18

**반대 우세** — 찬성 1 · 반대 2 · 보류 0 · 확신 가중 점수 -0.27 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장 내재: 매출 10년 연 43.2% (FCF 마진 15% 수렴 가정) · 기본 시나리오: 5년 연 48.8%
- 시장이 반영한 것: 현재 가격은 FCF 마진 15%를 가정할 때 10년간 연 매출 성장 C:implied_cagr@m15를 요구한다. 컨센서스는 FY2026 core 매출이 가이던스 상향 전 수준(F60)이고 FY2027 컨센서스는 없다. 시장은 2분기 GAAP 매출 부진(F58)과 주가 급락(S9, S20)을 보고 성장의 지속성을 의심하는 쪽이다.
- 우리가 다르게 보는 점: 성장 자체보다 질이 쟁점이다. 우리는 core 지표를 쓰지 않고 GAAP 매출과 SBC 차감 후 FCF로 모델링했다. 기본 시나리오는 경영진 2027 목표(S29)보다 낮게 잡고, 가치의 대부분을 잔여 이행의무(F52)가 매출로 바뀌는 속도에 건다. 가이던스 상향(F54, F55)이 컨센서스(F60)보다 앞서 있다는 점에서 FY2026 core 매출은 컨센서스 위로 본다. 다만 GAAP 마진과 고객 집중이 풀리지 않으면 하방이 크다고 본다.
- 왜 우리가 맞는가: 잔여 이행의무(F52)는 이연매출(F12)보다 훨씬 크다. 계약된 물량이 있으므로 성장률 분포의 하단은 일반적인 고성장 기업보다 높다. 반면 GAAP과 core의 격차(F50, F51) 해명과 인식 시기 공시는 아직 없어 이 가설은 증명되지 않았다. 주가 출처가 엇갈려(F40, F61) 가격 대비 우위는 확정할 수 없다. [F52] [F12] [F50] [F51] [F54] [F55] [F56] [F58] [F60] [C:implied_cagr@m15]
- 촉매: 3분기 실적 발표에서 core 매출이 가이던스(F56)를 충족하는지, GAAP 매출총이익률이 개선되는지, 잔여 이행의무의 인식 일정과 고객 구성이 공시되는지가 계기다.
- 시점: FY2026 3분기 실적 발표 (2026년 11월 전후)와 FY2026 10-K

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **81.99** vs 주가 127.21 · 기대 연 수익률 **+2.6%** · 손실 확률 80%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 30% | 22.91 | 13.00 | -29.0% | 상위 2개 고객 집중(F48)이 현실이 되어 대형 계약의 인식이 늦어지거나 줄어드는 경우다. GAAP 매출총이익률은 14%(F51)에 머물러 core 41%(F50)와의 격차가 해소되지 않는다. 데이터센터 투자(F6 |
| 기본 | 50% | 110.77 | 62.86 | -2.7% | FY2026은 core 매출 가이던스 상향(F54, F55)과 3분기 가이던스(F56)가 뒷받침한다. GAAP 매출은 core보다 낮으므로 core 성장률보다 보수적으로 잡았다. 2027년은 경영진의 '3배 이상'( |
| 강세 | 20% | 411.13 | 233.29 | +26.4% | 잔여 이행의무(F52)가 계약대로 빠르게 매출로 전환되고, 600MW 용량(F53)이 가동된다. 경영진이 말한 2027년 매출 3배(S29)가 실현된다. 규모가 커지면서 GAAP 매출총이익률이 core 수준(F50) |

## 3. 반증 조건 (thesis break)

- [자료 없음] 앤더슨: 3분기 core 매출이 가이던스 하단 미달 — `core_revenue < 2.14e+08` (FY2026Q3)
- [미충족] 앤더슨: 잔여 이행의무가 200억 USD 아래로 감소 — 계약 잔고 훼손 — `remaining_performance_obligations < 2e+10`
- [수동 확인] 앤더슨: 상위 고객의 계약 축소·해지 공시 — 수동 확인
- [자료 없음] 슬레이터: 3분기 core 매출총이익률이 가이던스 하단 미만이면 마진 개선 가설 훼손 — `core_gross_margin < 0.38` (FY2026Q3)
- [자료 없음] 슬레이터: 3분기 core 매출이 가이던스 하단 미만이면 성장 지속성 의심 — `core_revenue < 2.14e+08` (FY2026Q3)
- [수동 확인] 슬레이터: 계약 잔액의 인식 시기와 고객 구성이 공시되면 수동 확인 — 반대 근거가 해소되는지 판단
- [자료 없음] 애크먼: TTM 잉여현금흐름이 양수로 전환되면 FCF 레드라인 재검토 — `fcf > 0`
- [미충족] 애크먼: GAAP 매출총이익률이 35% 이상으로 수렴하면 core와의 격차 가설 약화 — `gaap_gross_margin >= 0.35`
- [미충족] 애크먼: 주가가 50달러 미만이면 안전마진 재평가 — `price < 50`
- [미충족] 레드팀: RPO가 2분기 말 254.0억 USD 아래로 감소 — 계약 인식·취소가 신규 수주를 앞지르기 시작 — `remaining_performance_obligations < 2.54e+10`
- [미충족] 레드팀: GAAP 매출총이익률이 2분기(14%)보다 낮아짐 — 믹스 전환이 마진을 깎는 중 — `gaap_gross_margin < 0.14`
- [충족 — 훼손] 레드팀: 분기 영업현금흐름이 2분기(-5,982만 USD)보다 더 나빠짐 — 투자 부담이 줄지 않음 — `ocf < -5.982e+07`
- [충족 — 훼손] 레드팀: 매출채권이 2분기 말(1.2억 USD)보다 더 늘어남 — 수금이 매출을 따라오지 못함 — `receivables > 1.2e+08`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | core_revenue | FY2026Q3 | >= 2.14e+08 | 80% | 3분기 core 매출이 가이던스 하단(F56)을 지키는지 본다. 기본 시나리오 성장의 첫 관문이다. |
| K2 | core_gross_margin | FY2026Q3 | >= 0.38 | 70% | 가이던스 하단(F57)이다. 마진이 2분기(F50)보다 낮아지는 추세인지 확인한다. |
| K3 | revenue | FY2026Q3 | >= 1.85e+08 | 60% | GAAP 매출이 2분기(F33)보다 늘어 core와의 격차가 줄어드는지 본다. 기본 시나리오는 GAAP 기준이다. |
| K4 | gaap_gross_margin | FY2026Q3 | >= 0.14 | 60% | GAAP 매출총이익률(F51)이 2분기보다 나빠지지 않는지 본다. 격차 해소 가설의 시험이다. |
| K5 | core_revenue | FY2026 | >= 8.8e+08 | 75% | 상향된 연간 가이던스 하단(F54)이다. 경영진 가이던스의 신뢰도를 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.27 · 비중 참고값 0.0% (반대 우세 — 신규 비중 없음) · 슬레이터 시작 비중 0.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 0/5 실패 | founder_led=예, upside_10y=15.20x, revenue_5y=17.13x |
| 슬레이터 | 반대 → 반대 | 3/5 | ✓ | 1/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=0.0%, cash_survives=예, cash_min=50.9억 USD, runway_years=17.2 |
| 애크먼 | 반대 → 반대 | 4/5 | ✗ 단순·예측 가능한 사업이 아님; 잉여현금흐름을 만들지 못함 (코드 계산); 레버리지·자본시장 의존; 안전마진 20% 미만 또는 계산 불가 | 0/5 실패 | simple_predictable=아니오, capital_markets_dependent=예, catalyst=없음 — 3분기 실적과 RPO 인식 공시는 확인 사건일 뿐 가치와 가격의 격차를 좁힐 우리 쪽 행동이 아니다, intrinsic_value=62.9, mos=-102.4%, fcf_positive=아니오 |

- ⚠ 앤더슨: arguments[1] leap: core +103%와 가이던스 상향은 맞다. 그러나 인용 자료에는 이전 성장률이 없어 '성장 가속'이 따라 나오지 않고, '수확체증 초기 구간'은 자료에서 나오지 않는 해석이다.
- ⚠ 앤더슨: rebuttals[1] leap: RPO와 600MW는 맞다. 그러나 인용에는 인식 시기와 해지 조건이 없어 '계약 잔고가 현실이 되고 있다'와 '기다림의 대가가 가격에 나타났다'가 따라 나오지 않는다.
- ⚠ 앤더슨: rebuttals[2]: 인용하지 않은 근거의 숫자 15%(C:fcf_margin@base), 28(C:exit_multiple@base) — cites에 추가
- ⚠ 슬레이터: arguments[4] unsupported: 없는 근거 인용: C:runway_years@FY2025
- ⚠ 슬레이터: rebuttals[1] unsupported: 없는 근거 인용: C:runway_years@FY2025
- ⚠ 슬레이터: rebuttals[0]: 인용하지 않은 근거의 숫자 15(C:exit_multiple@bear·C:upside_10y@anderson) — cites에 추가
- ⚠ 애크먼: rebuttals[0]: 인용하지 않은 근거의 숫자 15(C:exit_multiple@bear·C:upside_10y@anderson) — cites에 추가
- ⚠ 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 사업·산업 findings[7]: 인용하지 않은 근거의 숫자 1.9e+08(C:equity@FY2026Q1·C:revenue@FY2026Q1·F15), 1.72e+09(C:cash@FY2026Q1·F2) — cites에 추가
- ⚠ 레드팀 weakest[2] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): 출처 없는 숫자 36.6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)

## 앤더슨 — 찬성 (3/5)

> Cerebras는 LTGG가 찾는 모양의 기업이다. 비대칭이 크고, 성장 가설이 맞으면 5년 안에 매출이 몇 배가 된다. 2분기 core 매출은 +103%였고 연간 core 가이던스는 올랐다. 잔여 이행의무는 이연매출보다 훨씬 크고, 계약된 데이터센터 용량도 있다. 강세 시나리오에서 10년 뒤 주당 가치는 현재가의 15배를 넘는다. 5배가 될 길이 보이는가라는 10번 질문에는 '그렇다'로 답한다. 약점도 분명하다. 상위 2개 고객 집중도가 높고, GAAP 마진과 core 마진 사이의 격차는 설명되지 않았다. 확률 가중 기대수익률도 높지 않다. 그래서 확신은 3으로 낮추고 작은 비중으로 시작하는 쪽이다. 주가가 출처마다 달라 가격 판단은 유보하지만, 내 질문은 가격이 아니라 10년 뒤 크기다. 매도 논거는 성장 가설의 훼손뿐이다.

**논거**
- 계약된 활주로가 이미 있다. 잔여 이행의무가 254.0억 USD로 이연매출 1.7억 USD보다 훨씬 크고, 계약된 데이터센터 용량은 600MW다. 5년 매출 2배(1번 질문)의 하단을 일반 고성장 기업보다 높게 받쳐 준다. 다만 인식 시기와 해지 조건은 미확인이다. [F52] [F12] [F53]
- 성장 가속이 실제 숫자로 나온다. 2분기 core 매출이 +103%였고 경영진은 연간 core 가이던스를 올렸다. 수확체증 곡선의 초기 구간에서 나타나는 모양이다. [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [F54] [F55]
- 시장이 값에 넣은 성장은 연 43.2%다. 우리 강세 시나리오는 이보다 훨씬 가파른 경로를 요구한다. 그 경로가 열리면 현재가 대비 10년 뒤 주당 가치는 15.20배다. 열 번 중 여러 번 틀려도 한 번의 큰 승리가 포트폴리오를 정하는 구조다. 9번 질문에 대한 답은, 시장이 GAAP 매출 부진 하나를 보고 계약 잔고가 만드는 상방을 깎고 있다는 것이다. [C:implied_cagr@m15] [C:upside_10y@anderson] [F61] [F52]
- 하드웨어 판매에서 자체 데이터센터 기반 클라우드로 옮겨 가는 사업 구조는 반복 매출과 규모 장벽 후보를 만든다. 2분기 GAAP 매출은 컨센서스를 밑돌았지만, 부진은 하드웨어에서 나왔고 클라우드는 상회했다. 이 믹스 이동은 10년 지평에서는 소음이 아니라 방향이다. [S30](https://www.newsquawk.com/headlines/cerebras-cbrs-q2-2026-usd-revenue-1801mln-exp-194mln) [F58] [F33]
- 상장으로 현금이 크게 늘어 자금 조달 위험이 낮아졌다. 대담한 증설을 외부 자금 없이 이어갈 수 있는 구간이다. 이익률 상승 여지(6번 질문)는 core 마진이 41%라는 점에서 열려 있다. 단, GAAP 환산은 증명되지 않았다. [F3] [F50] [F51]

**사전 부검**
- 사전 부검: 상위 2개 고객이 FY2025 매출의 86%였다. 이 고객의 발주가 늦어지거나 줄면 잔여 이행의무가 매출로 바뀌지 않고 성장 가설 자체가 깨진다. 경로의 소음이 아니라 가설의 훼손이다. [F48] [F52] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- 사전 부검: GAAP 매출총이익률 14%와 core 41%의 격차가 규모가 커져도 좁혀지지 않으면 FCF 마진 25%는 오지 않는다. 확률 가중 기대 연 수익률은 낮고 손실 확률이 높다. 강세 시나리오(확률 20%)가 아니면 현재가를 보상하지 못한다. [F51] [F50] [C:expected_irr] [C:p_loss]
- 사전 부검: 가격 근거가 엇갈린다. 10월 13일 종가와 16일 종가가 크게 다른데 원인이 확인되지 않았다. 입력 오류라면 10년 업사이드 배수 자체가 달라진다. 그래서 확신을 3 이상으로 올리지 않는다. [F40] [F61]

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 FCF가 음수이고 설비투자가 영업현금흐름을 크게 넘는다는 점이다. 그러나 이 적자는 600MW 용량을 먼저 짓는 선행 투자의 모양이다. 10년 지평의 질문은 지금의 FCF가 아니라 그 투자가 만드는 매출의 크기다. 순현금이 충분해 외부 자본에 기대지 않고 이 구간을 지날 수 있다. 시장이 값에 넣은 성장은 연 43.2%이고, 계약 잔고가 이연매출을 압도하는 회사가 그 경로를 못 갈 이유는 인식 시기 불명 하나뿐이다. DCF가 현재를 정밀하게 재는 도구라는 점을 인정하더라도, 10년 뒤 크기는 재지 못한다. [C:fcf_margin@FY2025] [C:net_cash] [C:implied_cagr@m15] [F52] [F12]
- → 슬레이터: 슬레이터의 가장 강한 논거는 단위경제 핵심 지표(고객획득비용·순매출유지율·이탈률)가 비어 있어 증거가 없다는 것이다. 이 요구는 존중한다. 하지만 초기 기업의 불투명함을 이유로 증거를 기다리면 가장 가치 있는 구간을 놓친다. 기다림의 대가는 이미 가격에 나타났다. 증거가 쌓이는 동안 상방 시나리오의 계약 잔고는 현실이 되고 있다. 그래서 작게 시작하자는 것이지 크게 걸자는 것이 아니다. 슬레이터의 시작 비중 0은 상방이 열린 비대칭을 포기하는 선택이다. [F52] [F53] [F50] [F51]
- → 레드팀: 레드팀의 첫째 부검(상위 고객의 계약 축소·지연)은 성장 가설 자체를 깨므로 소음이 아니라 가설 훼손이다. 이 위험은 인정하며, 내 반증 조건에 RPO 하락과 고객 계약 축소를 넣은 이유다. 반면 둘째·셋째 부검(GAAP 마진 수렴 지연, 자본 소요 확대)은 경로의 소음에 가깝다. 현금이 크게 늘어 소요 증가를 흡수할 수 있고, 마진 격차는 규모로 풀릴 수 있다. 다만 약한 가정으로 지적된 기본 시나리오의 15% 마진과 28배 배수가 현재 가격과 순환한다는 점은 맞다. 그래서 기대수익률이 아니라 강세 경로의 크기로만 이 종목을 정당화한다. [F48] [F52] [F51] [F50] [F62] [F3] [C:implied_cagr@m15]

**인정한 점**
- 애크먼의 지적대로 기본 시나리오 기대 연 수익률은 +2.6%이고 손실 확률은 80%다. 강세 시나리오(확률 20%)가 아니면 현재가를 보상하지 못하므로, 이 종목은 작은 비중의 비대칭 베팅으로만 정당화된다.
- 슬레이터의 지적대로 GAAP 14%와 core 41%의 격차는 설명되지 않았고 3분기 core 마진 가이던스는 2분기보다 낮다. 마진 개선 가설은 증명되지 않았다.
- 레드팀이 짚은 대로 상위 2개 고객 집중(86%)은 경로의 소음이 아니라 가설 자체의 취약점이다. 3분기 이후 RPO 인식 공시가 나오기 전까지 확신을 3 이상으로 올리지 않는다.
- 주가 출처가 엇갈린다(175.44 대 127.21). 입력이 틀렸다면 10년 업사이드 배수가 달라지므로 가격 판단은 유보한다.


## 슬레이터 — 반대 (3/5)

> 시장이 정의되지 않았고 계약 잔액이 큰 회사라서 슬레이터의 관심 범위에는 든다. 생존도 문제가 아니다. IPO로 현금이 늘어 기본 시나리오에서 현금이 0 아래로 내려가지 않는다. 문제는 증거 수준이다. 단위경제의 핵심 지표(고객획득비용·순매출유지율·이탈률)가 비어 있고, GAAP과 core 매출총이익률의 격차가 설명되지 않았다. 매출은 소수 고객에 쏠려 있고, 계약 잔액이 매출로 바뀌는 시기와 해지 조건도 모른다. 기대수익률은 기본 시나리오에서 마이너스이고 손실 확률이 높다. 현재 가격에서는 증거가 쌓이기 전에 비중을 줄 이유가 없다. 가격 출처가 엇갈려 주가 의존 계산은 신뢰도가 낮지만, 이 판단은 가격보다 증거 부족에서 나온다. 3분기 core 매출과 GAAP 마진, 고객 구성 공시가 가설을 입증하면 작은 비중에서 다시 시작한다.

**논거**
- 기본 시나리오의 연 수익률은 마이너스이고 확률 가중 기대 연 수익률은 +2.6%, 손실 확률은 80%다. 증거가 얇은 단계에서 이 분포는 시작 비중을 정당화하지 못한다. [C:expected_irr] [C:p_loss]
- 단위경제가 입증되지 않았다. 2분기 core 매출총이익률 41%와 GAAP 14%의 격차를 설명하는 자료가 없고, 3분기 core 마진 가이던스는 2분기보다 낮다. 마진이 개선되는지 악화되는지 구분할 수 없다. [F50] [F51] [F57]
- FY2025 상위 2개 고객이 매출의 86%다. 순매출유지율과 이탈률도 없어 '증거로 키운다'는 전제의 증거 자체가 비어 있다. 이 수치는 2차 보도에서 왔으므로 원문 확인이 필요하다. [F48] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- 성장의 지속성은 계약 잔액이 뒷받침한다. 잔여 이행의무가 이연매출보다 훨씬 크다. 다만 인식 시기·고객 구성·해지 조건이 공개되지 않아 아직 계획이지 실적이 아니다. [F52] [F12] [S24](https://news.google.com/rss/articles/CBMikgFBVV95cUxOalM0ejc1WHVWb29zVVZRdEFSVm5aeWhSUDVLVjlUZDAyc1Y2LWhfa1RTTVNXYVM2ZzRSY0Q3cW1pdDN2Q21FeWYybUNwLWRtMl9reTVyb1RDSDdCTmxBRXlselNHTUtfdTY4eG15WDVWQzJxRWxOVlNQdFo1WkRwMkZwQmRKQkotR0xaYlRZc1l1Zw?oc=5)
- 생존은 문제가 아니다. 2분기 말 현금이 크게 늘었고 코드가 계산한 현금 소진 연수가 길다. 그래서 반대 이유는 자본 의존이 아니라 증거 부족과 가격이다. [F3] [C:runway_years@FY2025]

**사전 부검**
- 사전 부검: 반대가 틀렸다면, 3분기 이후 GAAP 마진이 core 수준으로 수렴하고 계약 잔액이 빠르게 매출로 바뀌어 강세 시나리오로 가는 경우다. 이때 증거 대기는 높은 가격표를 치르는 일이 된다. [F52] [F50] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- 사전 부검: 2분기 주가 급락이 단기 부진을 과하게 반영한 것이라면, 가설이 훼손되지 않았는데 가격만 움직인 상황이다. 가격 출처가 엇갈려 가격 우위 판단 자체가 불확실하다. [F40] [F61] [S9](https://news.google.com/rss/articles/CBMingFBVV95cUxPS3RxTUJxMTh2Mk9XSmgxdm1MZDh6MlRtcVl5aFM1bmF1ajVmWlFnUF9nNU0yYjloQ0pON2VSWFZBYTVldmJ0TGI5N2psYlcwZVRuSURZaUM1NkYzVkh4NGVNRUtjd0F0M3RMTno2X0RSNG9VbF91V2lDOUh0OG5nSDJiY2M4cDdrM1lGRnNicldnNXBBQTBDRFVzNHdJQQ?oc=5)
- 사전 부검: 2분기 SBC 급증이 일회성이 아니라면 희석과 FCF 부담이 모델보다 커진다. 그 경우 반대 근거는 더 강해진다. [F37] [F36]

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 계약 잔액이 활주로를 받친다는 것이다. 이 방향에는 동의한다. 그러나 15배가 넘는 10년 업사이드는 강세 시나리오 하나에서 나온다. 그 시나리오는 확률이 가장 낮고, 이연매출보다 훨씬 큰 잔액이 실제 매출로 바뀐다는 전제 위에 서 있다. 확률로 가중하면 기대 연 수익률은 +2.6%이고 손실 확률은 높다. 기본 시나리오의 연 수익률은 마이너스다. 인식 시기와 해지 조건이 공시되기 전까지 잔액은 계획이지 실적이 아니다. 슬레이터의 방식은 증거가 쌓이면 키우는 것이다. 지금은 키울 증거가 없다. [C:expected_irr] [C:p_loss] [F52] [F12]
- → 애크먼: 애크먼은 성장이 현금을 만들지 않고 소모한다고 본다. 이 점은 옳다. 그러나 자본시장 의존이라는 판정에는 동의하지 않는다. 상장으로 현금이 크게 늘었고 코드가 계산한 현금 소진 연수도 길다. 기본 시나리오에서 현금이 0 아래로 내려가지 않는다. 지금 자금이 끊길 위험은 낮다. 내가 반대하는 이유는 생존이 아니라 단위경제 증거의 부족이다. 또 오늘 모델링하기 어렵다는 이유만으로 사업을 버리지도 않는다. 3분기 마진과 고객 구성이 입증되면 작은 비중에서 다시 시작할 수 있다. [F3] [C:runway_years@FY2025] [F50] [F51]
- → 레드팀: 레드팀의 가장 강한 부검은 수금의 질이다. 2분기 매출은 1분기보다 줄었는데 매출채권은 크게 늘었고, 상위 고객이 소수다. 이는 단위경제 증거를 직접 훼손하는 선행 신호다. 이 신호를 반영해 매출채권이 2분기 말보다 늘지 않는다는 조건을 `must_be_true`에 추가한다. 잔여 이행의무가 2분기 말 아래로 줄지 않는다는 조건도 추가한다. 둘 다 계약이 실제로 현금과 매출로 이어지는지 보는 관문이다. [F30] [F31] [F32] [F33] [F48] [F52]

**참이어야 하는 것**
- [at_risk] 3분기 core 매출총이익률이 가이던스 하단 이상이다
- [on_track] 3분기 core 매출이 가이던스 하단 이상이다
- [at_risk] GAAP 매출총이익률이 2분기보다 나빠지지 않는다
- [at_risk] 상위 2개 고객 비중이 FY2025의 86%에서 낮아진다
- [at_risk] 3분기 말 매출채권이 2분기 말보다 늘지 않는다
- [on_track] 잔여 이행의무가 2분기 말 수준 아래로 줄지 않는다

**인정한 점**
- 앤더슨: 믹스가 하드웨어에서 클라우드로 옮겨 가는 방향은 소음이 아니라 구조 변화일 수 있다. 하드웨어 부진과 클라우드 호조가 갈렸다는 보도가 이를 뒷받침한다. 다만 이 변화가 마진에 미치는 영향은 미확인이라 입장은 바꾸지 않는다.
- 애크먼: 기본 시나리오의 FCF 적자가 FY2029까지 이어진다는 지적을 인정한다. 생존은 문제가 아니지만 성장 자금이 현금 창출이 아니라 조달에서 나온다는 점이 증거 부족을 더 무겁게 만든다.
- 레드팀: 기본 시나리오의 FCF 마진 가정이 역DCF 목표 마진과 같은 값이라 순환 위험이 있다는 지적을 인정한다. 그래서 확신을 올리지 않고 시작 비중은 0으로 유지한다.


## 애크먼 — 반대 (4/5)

> Cerebras는 한 문단으로 설명되는 사업이 아니다. 하드웨어 판매와 자체 데이터센터 클라우드가 섞여 있고, 상위 2개 고객이 매출의 대부분이다. 10년 뒤 FCF 범위도 좁힐 수 없다. TTM FCF는 음수이고 설비투자가 영업현금흐름을 크게 넘는다. 성장 자금을 자본시장(IPO)에 의존해 왔다. 기본 시나리오 안전마진은 마이너스이고 확률 가중 기대수익률은 낮으며 손실 확률이 80%다. 성장 자체는 인상적이지만, 단순성·FCF·자본시장 의존·가격 중 어느 기준도 충족하지 못한다. 담지 않는다.

**논거**
- 사업이 단순하지도 예측 가능하지도 않다. 하드웨어와 클라우드 용량 임대가 섞여 있고 매출총이익률이 core 41%, GAAP 14%로 갈려 어느 쪽이 실체인지 알 수 없다. 단위경제는 입증되지 않았다. [F50] [F51] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- 고객 집중이 극단적이다. FY2025 상위 2개 고객이 매출의 86%였다. 계약잔액 254.0억 달러도 인식 시기와 해지 조건이 공시되지 않아 10년 FCF를 추정할 근거가 못 된다. [F48] [F52] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- FCF가 음수이고 자본집약적이다. FY2025 FCF 마진은 -77.0%였고 설비투자는 3.8억 달러, 영업현금흐름은 음수였다. 2분기 영업현금흐름도 음수다. 성장이 현금을 만드는 것이 아니라 소모한다. [C:fcf_margin@FY2025] [F67] [F65] [F64]
- 가격이 보수적 가정을 정당화하지 못한다. 기본 시나리오 현재가치 62.86은 주가 127.21의 절반이고, 기대 연 수익률은 +2.6%, 손실 확률은 80%다. 시장은 연 43.2% 매출 성장을 10년간 요구한다. [C:expected_irr] [C:p_loss] [C:implied_cagr@m15] [F61]
- 순현금 58.2억 달러는 IPO로 채워진 것이다. 생존 위험은 낮아졌지만 이는 자본시장 접근의 결과이며, 기본 시나리오의 FCF 적자가 FY2029까지 이어진다. 현금이 사업의 현금 창출력을 대신하지 못한다. [F3] [C:net_cash] [F2]

**사전 부검**
- 사전 부검: 우리가 틀렸다면 RPO가 예상보다 빨리 매출로 전환되고 600MW 용량이 가동되어 강세 시나리오가 실현된 경우다. 그때 주가는 크게 오르겠지만, 우리는 그 결과를 입증 가능한 단순성 없이 예측할 수 없었다. [F52] [F53] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- 사전 부검: 주가 출처가 엇갈린다(175.44 대 127.21). 실제 가격이 더 낮다면 안전마진이 달라질 수 있으나, 기본 가치 62.86과 FCF 음수 때문에 레드라인 위반은 변하지 않는다. [F40] [F61] [S27](https://weissratings.com/en/instant-news-alerts/cerebras-systems-inc-cbrs-down-4-8-time-to-cash-out) [S31](https://finance.yahoo.com/quote/CBRS/history/)
- 사전 부검: GAAP과 core 마진 격차가 SBC와 IPO 일회성 때문이라면 정상화 마진은 우리가 본 것보다 좋다. 그러나 해명되기 전까지 증거로 쓸 수 없다. [F37] [F51] [F50]

**반론**
- → 앤더슨: 연 43.2% 성장을 시장이 값에 넣었다는 것은 오히려 가격이 이미 큰 성장을 요구한다는 뜻이다. 강세 시나리오 15배는 확률 20%짜리 한 갈래이고, 확률 가중 기대 연 수익률은 +2.6%, 손실 확률은 80%다. 기저율 표도 없어 생존자 편향을 검증하지 못했다. 계약 잔액 254.0억 달러는 이연매출 1.7억 달러에 비해 크지만 인식 시기와 해지 조건이 공시되지 않았으므로 10년 FCF를 추정할 근거가 아니다. [C:implied_cagr@m15] [C:expected_irr] [C:p_loss] [F52] [F12]
- → 슬레이터: 슬레이터의 반대 결론에는 동의하지만 '생존은 문제가 아니다'에는 선을 긋는다. 현금 67.4억 달러는 IPO로 채워진 것이고, 기본 시나리오에서도 FCF 적자가 FY2029까지 이어진다. 생존 경로는 필요조건일 뿐 가격의 정당화가 아니다. 증거가 쌓여 3분기 지표가 맞아도, 기본 시나리오 현재가치 62.86이 주가 127.21의 절반이라는 가격 문제는 남는다. [F3] [F2] [F61] [C:fcf_margin@FY2025]
- → 레드팀: 레드팀의 사전 부검은 FCF 범위를 더 넓힌다. 기본 시나리오의 FCF 마진 15% 가정은 GAAP 단위경제의 뒷받침이 없고 목표 마진이 역DCF와 순환한다. 고객 집중, 마진 격차, 자본 부담, 수금 질 네 가지가 모두 10년 FCF의 하방을 키우므로 필요한 안전마진은 20%보다 더 커야 한다. 현재 안전마진은 마이너스이므로 격차가 훨씬 크다. [C:implied_cagr@m15] [F51] [F48] [F30] [F31]

**인정한 점**
- 앤더슨의 지적대로 계약 잔액 254.0억 달러가 인식 시기를 알 수 없는 채로도 일반적인 고성장 기업보다 성장의 하단을 높게 받친다는 점은 인정한다. 다만 이는 단순성·FCF·자본시장 의존·안전마진 레드라인을 풀어 주지 못하므로 입장은 바뀌지 않는다.
- 슬레이터의 지적대로 주가 출처가 엇갈려(175.44 대 127.21) 안전마진의 정확한 값은 불확실하다. 어느 가격을 써도 기본 가치 62.86에 못 미치고 FCF가 음수라 결론은 같다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Cerebras는 웨이퍼 단위 AI 가속기와 CS-4 시스템을 직접 팔고(하드웨어), 자체 데이터센터에서 추론·학습 용량을 임대하는 클라우드 사업도 한다. 이 사업이 커지고 있다. 2026년 2분기 core 매출은 $209.9M으로 +103%였고(S29), 남은 이행의무(RPO)는 254.0억 USD, 계약된 데이터센터 용량은 600MW다(F52, F53). 하지만 단위경제는 아직 입증되지 않았다. 2분기 core 매출총이익률은 41%인데 GAAP은 14%로 차이가 매우 크다(F50, F51). 이 차이를 설명하는 자료는 없다. 매출은 소수 고객에 쏠려 있다. FY2025 상위 2개 고객 비중이 86%다(F48). 성장을 위해 투자 규모도 크다. FY2025 영업이익률은 -28.6%, FCF 마진은 -77.0%다(C:operating_margin@FY2025, C:fcf_margin@FY2025). IPO로 현금은 67.4억 USD로 늘었다(F3).

- [unit_economics] 2026년 2분기 core 매출총이익률은 41%, GAAP 매출총이익률은 14%다. 3분기 core 매출총이익률 가이던스는 38~40%로, 2분기보다 낮다. FY2025 연간 매출총이익률은 보도 기준 0.39였다. 14%라는 GAAP 수치의 원인(일회성, SBC, 클라우드 감가상각 등)은 아직 설명되지 않았다. 따라서 이익률이 개선 중인지 악화 중인지 판단할 수 없다. [F50] [F51] [F57] [F47] [S2](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrs-20260812.htm)
- [customers] FY2025 상위 2개 고객이 매출의 86%였다(G42·MBZUAI 연계로 보도됨). 고객 CAC, 순매출유지율, 이탈률은 공시에서 확인하지 못했다. 단위경제의 핵심 지표가 비어 있다. 이 집중도는 S-1 원문으로 재확인해야 한다. [F48] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- [runway] RPO는 254.0억 USD이고 2026년 2분기 말 이연매출은 1.7억 USD다. RPO가 이연매출보다 훨씬 크므로 대부분은 아직 청구되지 않은 장기 계약이다. 인식 시기와 해지 가능성이 성장 활주로의 신뢰도를 정한다. 현재 자료에서는 이를 알 수 없다. [F52] [F12] [S2](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrs-20260812.htm) [S24](https://news.google.com/rss/articles/CBMikgFBVV95cUxOalM0ejc1WHVWb29zVVZRdEFSVm5aeWhSUDVLVjlUZDAyc1Y2LWhfa1RTTVNXYVM2ZzRSY0Q3cW1pdDN2Q21FeWYybUNwLWRtMl9reTVyb1RDSDdCTmxBRXlselNHTUtfdTY4eG15WDVWQzJxRWxOVlNQdFo1WkRwMkZwQmRKQkotR0xaYlRZc1l1Zw?oc=5)
- [runway] 매출은 빠르게 늘고 있다. FY2025 매출 성장은 75.7%였고, 2026년 2분기 core 매출은 +103%, GAAP 매출은 +74%였다. 경영진은 2026 core 매출 가이던스를 $880~890M으로 올렸고(기존 $855~865M), 2027년 매출 3배 이상을 계획한다고 했다. 2027 목표는 회사 발언일 뿐 입증된 수치가 아니다. [C:revenue_growth@FY2025] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [F54] [F55]
- [unit_economics] 성장에는 자본이 많이 든다. FY2025 영업현금흐름은 -1,005만 USD, 설비투자는 3.8억 USD로 FCF 마진은 -77.0%였다. 2026년 2분기 영업현금흐름도 음수(-5,982만 USD)다. 클라우드 데이터센터를 직접 짓는 모델이라면 자본집약도가 높고, 하드웨어 판매보다 투하자본수익률이 낮을 수 있다. [F65] [F67] [C:fcf_margin@FY2025] [F64]
- [industry] 2분기 GAAP 매출 $180.1M은 컨센서스 $194M을 밑돌았다. 하드웨어가 부진했고 클라우드는 상회했다. 이는 매출 구성이 하드웨어에서 클라우드로 옮겨 가고 있음을 시사한다. 하지만 어닝콜 원문이 없어 믹스 변화가 이익률에 미치는 영향은 확인하지 못했다. [S30](https://www.newsquawk.com/headlines/cerebras-cbrs-q2-2026-usd-revenue-1801mln-exp-194mln) [F58] [S9](https://news.google.com/rss/articles/CBMingFBVV95cUxPS3RxTUJxMTh2Mk9XSmgxdm1MZDh6MlRtcVl5aFM1bmF1ajVmWlFnUF9nNU0yYjloQ0pON2VSWFZBYTVldmJ0TGI5N2psYlcwZVRuSURZaUM1NkYzVkh4NGVNRUtjd0F0M3RMTno2X0RSNG9VbF91V2lDOUh0OG5nSDJiY2M4cDdrM1lGRnNicldnNXBBQTBDRFVzNHdJQQ?oc=5)
- [industry] 경쟁 구조(NVIDIA, AMD 등), 점유율, 공급자 협상력(칩 제조 위탁·메모리)에 대한 교차 확인 자료는 수집하지 못했다. 산업 내 위치는 회사 발표와 보도로만 추정할 수 있다. AMD와의 협력은 경쟁이면서 동시에 보완 관계일 수 있다. [S18](https://news.google.com/rss/articles/CBMiywFBVV95cUxQSGxfRjlGZUZfR1hack0zbEdZcVJXY1JCaWw4dl9fMFZnQnJHVnVfU3NsZkpVd2hPbjh5Q0dHTVcxYTByelU2b3lMUzVDNk54ZFN4OG1VSko2MXEzV0d3bDdHSTJiRHlrMFZtallYSllLUzdSQ2lVdDVra2ZqY0xPaEV2cmxRaXRIWnhRd19obk82eFBGQXQ1YnpYc2hLY0poOGVsdS1yZ19mVGs0RlFVZ1diV0luRktiNV9Uc05vSHpEbmViQ1NjX1h1UQ?oc=5) [S15](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNjNfbnRoZFloVUFkdDZxWUppbzg1ejVBcTIxVGVxQXZOS0hNZFdPVi02UFVGdU1oR0NPWjBrelZnUnY2bHFDSm1hdDl2a0JDNnBWNV9YQ2ZyT21nOWt6TTdFZjZNMm4tMVUzX3lYQy1QMzMwbmNuSmFZalQycjNZQlhFSTRfa2RYeHVFUnFXSGs0aGRMNGVSOGRR?oc=5)
- [unit_economics] IPO 직후라 재무제표가 크게 바뀌었다. 2026년 2분기 말 자본은 91.5억 USD(1분기 -1.9억), 현금은 67.4억 USD(1분기 17.2억)다. 2분기 순손실은 -4.5억 USD이고 SBC는 3.8억 USD로 1분기보다 급증했다. 이 손실이 IPO 연계 일회성인지 구조적인지에 따라 영업 레버리지 판단이 달라지지만 아직 구분할 수 없다. [F16] [F3] [F24] [F37] [S1](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)
- [claimed] 웨이퍼 단위 칩 설계와 CS-4 신제품, Hot Chips 발표가 기술 차별화의 근거로 제시된다. 하지만 이는 회사 발표와 보도뿐이다. 경쟁사 대비 성능·점유율·가격 프리미엄 같은 시장 데이터는 수집하지 못했다. [S8](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBmMUQxb0dVSUo2UzM1MVE2dExHRlRYUlg2QW1GSktqeTd0WmVldXpKaVFIVUxaWVpwQ0RpQlpnYjBUZWJ4ZmZBWHowMzlRQkdPV0E3VzE3VkxfdjJtUmNBNFE1dFI?oc=5) [S15](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNjNfbnRoZFloVUFkdDZxWUppbzg1ejVBcTIxVGVxQXZOS0hNZFdPVi02UFVGdU1oR0NPWjBrelZnUnY2bHFDSm1hdDl2a0JDNnBWNV9YQ2ZyT21nOWt6TTdFZjZNMm4tMVUzX3lYQy1QMzMwbmNuSmFZalQycjNZQlhFSTRfa2RYeHVFUnFXSGs0aGRMNGVSOGRR?oc=5) [S32](https://news.google.com/rss/articles/CBMijAFBVV95cUxOcUpZSVhkNDcyU0lXNWx4WHF0ZTRweFE2N3pvbU5URlU4SjQtQVRXekhGV0t4TFVWa1A1YTY1U2pwRGExR3EydjI4U3E4ZTRDZzZaX2VMVjhWUXVNUWJBNnBYcmRrYmhmRm5pc3lxcUlVaGp4OG1qUVl1Ym1aa3BDVHlyYWdWRzF1RkpUaA?oc=5)
- [claimed] 600MW 규모의 데이터센터 용량 계약과 RPO 254.0억 USD는 규모 진입장벽 후보다. 다만 두 수치 모두 어닝콜 요약과 보도에서 나온 것이다. RPO의 고객 구성, 인식 시기, 해지 조건은 확인하지 못했다. [F53] [F52] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [S24](https://news.google.com/rss/articles/CBMikgFBVV95cUxOalM0ejc1WHVWb29zVVZRdEFSVm5aeWhSUDVLVjlUZDAyc1Y2LWhfa1RTTVNXYVM2ZzRSY0Q3cW1pdDN2Q21FeWYybUNwLWRtMl9reTVyb1RDSDdCTmxBRXlselNHTUtfdTY4eG15WDVWQzJxRWxOVlNQdFo1WkRwMkZwQmRKQkotR0xaYlRZc1l1Zw?oc=5)
- [claimed] AMD와의 분리형 추론 협력, Gimlet Labs 공급 계약은 생태계 확장 시도다. 하지만 이탈률이나 가격 인상 후 고객 잔존 기록이 없어 전환비용을 입증할 수 없다. [S18](https://news.google.com/rss/articles/CBMiywFBVV95cUxQSGxfRjlGZUZfR1hack0zbEdZcVJXY1JCaWw4dl9fMFZnQnJHVnVfU3NsZkpVd2hPbjh5Q0dHTVcxYTByelU2b3lMUzVDNk54ZFN4OG1VSko2MXEzV0d3bDdHSTJiRHlrMFZtallYSllLUzdSQ2lVdDVra2ZqY0xPaEV2cmxRaXRIWnhRd19obk82eFBGQXQ1YnpYc2hLY0poOGVsdS1yZ19mVGs0RlFVZ1diV0luRktiNV9Uc05vSHpEbmViQ1NjX1h1UQ?oc=5) [S16](https://news.google.com/rss/articles/CBMirgFBVV95cUxOMDgtbmhLenNVQVdOQXJDbmJmck52THdJR3BYWV8zeXdjRFdieFdIdUNlTTNreWNWSy1obHdabzhtakNsQldBeGF6Y0RwLTQ0ZVRzZy11UkFycEx6azI0dWM1enN5NkdHTEg3N1VhajVFZEFqMmlKblo3Y2Zmam1wUTNLS3ZNYTd2b2MxdWNVQzJtdklpVV92WS1wZllQVGVBak9mUEdkeldoWFZRWFE?oc=5)

### 경영진·자본배분 — mixed

경영진의 정렬을 판단할 핵심 증거가 비어 있다. DEF 14A 보상 지표, 내부자 매매, 락업 해제 일정, 가이던스 적중 이력을 확보하지 못했다. 확인되는 것은 세 가지다. 첫째, 상장 후 두 번째 분기에 연간 core 매출 가이던스를 $855~865M에서 $880~890M으로 올렸다. 둘째, 2분기 GAAP 매출은 컨센서스를 밑돌았고 GAAP 매출총이익률(14%)과 core 매출총이익률(41%)의 격차가 크다. 셋째, 2분기 SBC가 급증하고 희석 주식 수가 늘었다. 상장 후 콜이 두 번뿐이라 신뢰도를 통계로 평가할 수 없다. 자본 투입은 FY2025 대규모 설비투자 이후 2분기에도 이어졌고, 그 수익률은 아직 입증되지 않았다. 증거가 부족해 '혼재'로 두며, 이는 정렬이 확인됐다는 뜻이 아니다.

- [compensation] 근거 없음. DEF 14A 보상 지표(장기 vs 단기), 베스팅 기간, 창업자 보상 구조는 수집하지 못했다. 보상이 주주와 같은 방향인지 판단할 수 없다. [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- [insider] 근거 없음. 창업자·경영진 지분, 최근 내부자 매수·매도, 락업 해제 일정은 찾지 못했다. IPO 직후 시기라 락업 해제가 수급에 영향을 줄 수 있으나 일정은 확인되지 않았다. [S5](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035605/closing8-k.htm)
- [guidance] FY2026 core 매출 가이던스를 $855~865M에서 $880~890M으로 상향했고, 3분기 core 매출 가이던스는 $214~216M, core 매출총이익률은 38~40%다. 그러나 가이던스 대비 실적 이력은 상장 후 콜 두 번뿐이라 적중률 계산이 불가능하다(C:guidance_hit_rate는 산출 대상이 없다). 2분기 GAAP 매출 1.8억 달러는 컨센서스 1.94억 달러를 하회했고, 이후 주가는 14~16% 하락했다. [F54] [F55] [F56] [F57] [F33] [F58] [S4](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044941/cbrs-20260623.htm) [S2](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrs-20260812.htm) [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [S9](https://news.google.com/rss/articles/CBMingFBVV95cUxPS3RxTUJxMTh2Mk9XSmgxdm1MZDh6MlRtcVl5aFM1bmF1ajVmWlFnUF9nNU0yYjloQ0pON2VSWFZBYTVldmJ0TGI5N2psYlcwZVRuSURZaUM1NkYzVkh4NGVNRUtjd0F0M3RMTno2X0RSNG9VbF91V2lDOUh0OG5nSDJiY2M4cDdrM1lGRnNicldnNXBBQTBDRFVzNHdJQQ?oc=5) [S20](https://news.google.com/rss/articles/CBMif0FVX3lxTFBJcHVySkhhUXc0UTFTUU44MC1zazJYSFpyMVRkdy1MUG5QSDBOX1dkVmstdi1VWVBZTm91U2ZXYzhXZmlzUlAzT2NNdExXMVZ6eWdyQkQ0eFA0UzU3amczTzYxQkthMTRWOXJGRjZ0bzQyT2F6b1pGbFMwN1hHcTDSAYQBQVVfeXFMTlk2ekExUzkydDVRQ1E3elduc0F5c08tUklVMFJBazUyS1lEZml4alVXSTdxYWpSdVdiVEFuVnMtVnFSTnNOWjZsaldlUlFyMnBEU0pWbkFJektITkdWSnItZS05aFBfRm94X1ZOV1J0Y3FIdXBUdklRLWZJSktrekxYRG8x?oc=5)
- [guidance] 경영진은 2027년 매출 3배 이상 증가와 core 매출총이익률 60%대 이상을 목표로 제시했다. 이는 정량 범위가 없는 회사 발언이고 2차 요약에 근거하므로 입증된 수치가 아니다. 현재 core 매출총이익률 41%, GAAP 14%와 격차가 크다. [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [F50] [F51]
- [dilution] 희석 주식 수가 1분기 6,281만에서 2분기 1.5억으로 늘었다. 2분기에는 IPO 이전 구간이 섞여 있어 기말 주식 수는 더 크며, 발행주식수는 약 2.196억(미확인)이다. SBC는 1분기 959만에서 2분기 3.8억으로 급증했다. 이 급증이 IPO 연계 일회성인지 정상 수준인지 확인되지 않았다. 따라서 SBC 비용 부담과 주주 가치 희석을 구분해 판단할 수 없고, 자사주 매입으로 상쇄한 흔적도 확인되지 않는다. [F13] [F14] [F36] [F37] [F41] [S28](https://www.fool.com/quote/NASDAQ/CBRS)
- [capital_allocation] 설비투자는 FY2024 2,344만에서 FY2025 3.8억으로 늘었고, 2분기에도 4.2억(차감 추정치, 원문 대조 필요)이다. FY2025 영업현금흐름은 -1,005만, FCF 마진은 -77.0%다. 상장으로 현금이 1분기 17.2억에서 2분기 67.4억으로 늘었다. 증설과 데이터센터 용량(계약 600MW)에 베팅하는 구조이며, 투자 수익률 이력은 아직 없다. 인수나 자사주 이력도 확인되지 않았다. [F68] [F67] [F62] [F65] [F2] [F3] [F53] [C:fcf_margin@FY2025]
- [capital_allocation] 고객 집중도가 높다. FY2025 상위 2개 고객이 매출의 86%이고 G42·MBZUAI 연계로 보도됐다. 특수관계 여부와 계약 조건은 미확인이다. 잔여 이행의무 254.0억 달러의 인식 시기와 고객 구성도 확인하지 못했다. 경영진의 고객·계약 공시 신뢰도는 검증할 근거가 부족하다. [F48] [F52] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm) [S24](https://news.google.com/rss/articles/CBMikgFBVV95cUxOalM0ejc1WHVWb29zVVZRdEFSVm5aeWhSUDVLVjlUZDAyc1Y2LWhfa1RTTVNXYVM2ZzRSY0Q3cW1pdDN2Q21FeWYybUNwLWRtMl9reTVyb1RDSDdCTmxBRXlselNHTUtfdTY4eG15WDVWQzJxRWxOVlNQdFo1WkRwMkZwQmRKQkotR0xaYlRZc1l1Zw?oc=5)

### 회계 품질 — watch

코드 회계 신호는 하나도 뜨지 않았지만, 이것은 '문제 없음'의 증거가 아니라 입력이 부족하다는 뜻에 가깝다. 신호 계산에 필요한 연간 순이익과 분기 비교 기간이 없고, 감사의견·감사인, 특수관계(G42·MBZUAI), core 조정 내역도 비어 있다. 보이는 단서는 네 가지다. (1) 2분기 SBC가 매출을 넘는 IPO 연계 일회성 성격이다. (2) GAAP 매출총이익률과 core 매출총이익률의 격차가 크다. (3) 매출은 줄었는데 매출채권이 크게 늘었다. (4) 상위 2개 고객 집중도가 매우 높다. 숫자를 조정해서 봐야 하지만, 숫자를 믿을 수 없다는 증거는 없으므로 red_flag는 쓰지 않고 watch로 판정한다. 가치평가에는 core 지표가 아니라 GAAP 지표와 SBC 차감 후 현금흐름을 써야 한다. FY2025 영업현금흐름은 보도마다 다른 순이익(일회성 비현금 이익 포함)과 같이 읽어야 하므로, S-1 원문으로 확인될 때까지 신뢰도를 낮춰 본다.

- [watch] 회사가 강조하는 core 매출총이익률은 GAAP 매출총이익률과 격차가 매우 크다. 이 격차의 요인(SBC, 감가상각, 데이터센터 비용 배분 등)이 공시되지 않았다. 가이던스와 2027 목표(core 60%대 이상)는 core 기준이므로 GAAP 기준으로 환산하기 전에는 신뢰하지 않는다. [F50] [F51] [F57] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- [watch] 2분기 SBC가 같은 분기 매출을 넘는다. 1분기와 비교하면 IPO 연계(RSU 가득 등)로 보이는 일회성 비용이지만, 이를 확인하는 근거는 없다. 이것이 반복되는지에 따라 정상화 이익이 크게 달라지므로 SBC를 비용으로 보고 FCF를 계산해야 한다. 같은 기간 순손실은 SBC 영향으로 크게 확대됐다. [F36] [F37] [F33] [F24] [F23]
- [watch] 2분기 매출은 1분기보다 줄었는데 매출채권은 약 두 배로 늘었다. 총액 인식 시점의 문제인지 대형 고객의 수금 지연인지 확인되지 않았다. 반대로 재고는 크게 줄었다. 코드 신호는 분기 간 비교만으로는 문턱을 넘지 않았으나, 고객 집중도를 감안하면 수금 위험으로 본다. [F30] [F31] [F32] [F33] [F21] [F22]
- [watch] 상위 2개 고객이 FY2025 매출의 대부분을 차지하고 G42·MBZUAI 연계로 알려져 있다. 특수관계 여부와 계약 조건이 확인되지 않았다. 계약잔액(RPO)은 매출보다 훨씬 커서, 인식 시기와 해지 조건에 따라 매출 신뢰도가 달라진다. [F48] [F52] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- [watch] FY2024 영업현금흐름이 같은 해 매출을 초과했고 FY2025는 음수로 반전했다. 고객 선수금 등 일회성 운전자본이 원인으로 보이나, 원인이 확인되지 않았다. FY2025는 대규모 설비투자가 겹쳐 FCF가 크게 음수다. 이 값은 S-1에 대한 2차 자료와 424B4에서 가져왔으므로 원문 대조가 필요하다. [F65] [F66] [F67] [F68] [F42] [F43] [S33](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)
- [info] 희석 주식 수와 자본이 1분기에서 2분기 사이에 급변했다. 순자본잠식에서 큰 자기자본으로의 전환이 IPO와 우선주 전환의 결과로 보이므로 희석 신호를 그대로 적용하지 않는다. 다만 발행주식수가 출처마다 달라(S28 불일치) 주당 지표는 10-Q 표지로 확인되기 전까지 불확실하다. [F13] [F14] [F15] [F16] [F41] [S28](https://www.fool.com/quote/NASDAQ/CBRS)
- [info] 부채 항목(debt와 debt_current)의 값이 서로 부합하지 않는다. 유동 차입 잔액이 총 차입금보다 크므로, 분류 기준(리스·금융부채 포함 여부)이 다를 가능성이 있다. 순현금 계산에 영향이 있으므로 10-Q 원문으로 확인한다. [F7] [F8] [F9] [F10]
- [watch] 감사의견, 감사인, 핵심감사사항, IPO 전후 재무제표 정정 여부를 확인하지 못했다. 코드의 restatement·auditor_change 신호도 없지만 수집 범위가 8-K 목록에 한정되어 있어 부재의 증거로는 약하다. [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm) [S1](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 소수 고객의 계약이 줄거나 늦어졌다. FY2025 상위 2개 고객이 매출의 86%였고 G42·MBZUAI 연계로 보도됐다. RPO 254.0억 USD는 이연매출 1.7억 USD보다 훨씬 커서 대부분 아직 청구되지 않은 장기 계약이다. 인식 시기와 해지 조건이 공시되지 않았다. 한 고객이 인도 시기를 미루거나 계약 규모를 줄이면 RPO가 매출로 바뀌지 않고, 성장 서사가 무너진다. 고객이 자체 칩이나 NVIDIA·AMD로 옮기면 같은 결과가 나온다. 시장은 매출 성장 대신 현금흐름을 보는 쪽으로 배수를 낮춘다. [F48] [F52] [F12] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm) [S24](https://news.google.com/rss/articles/CBMikgFBVV95cUxOalM0ejc1WHVWb29zVVZRdEFSVm5aeWhSUDVLVjlUZDAyc1Y2LWhfa1RTTVNXYVM2ZzRSY0Q3cW1pdDN2Q21FeWYybUNwLWRtMl9reTVyb1RDSDdCTmxBRXlselNHTUtfdTY4eG15WDVWQzJxRWxOVlNQdFo1WkRwMkZwQmRKQkotR0xaYlRZc1l1Zw?oc=5)
- (20%) GAAP 매출총이익률이 core 수준으로 수렴하지 않았다. 2분기 core는 41%, GAAP은 14%로 격차가 크고 원인이 설명되지 않았다. 3분기 core 가이던스(38~40%)는 2분기보다 낮다. 매출이 클라우드 위주로 옮겨 가면 데이터센터 감가상각이 매출원가로 들어간다. 이 경우 격차는 일시적 요인이 아니라 구조가 된다. 경영진의 2027 core 60%대 목표는 GAAP으로 환산되지 않는다. 마진이 오르지 않으면 FCF 마진 15% 가정이 성립하지 않고, 출구 멀티플도 낮아진다. [F50] [F51] [F57] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- (15%) 성장에 필요한 자본이 예상보다 컸고 현금이 줄었다. FY2025 설비투자가 3.8억 USD로 FCF 마진이 -77.0%였고, 2분기에도 설비투자 4.2억 USD와 영업현금흐름 -5,982만 USD가 이어졌다. 600MW 데이터센터는 건설과 장비 구입을 먼저 하고 매출은 나중에 들어온다. 투자 수익률의 이력이 없다. 매출이 늦어지면 IPO로 들어온 67.4억 USD가 소진되고, 추가 증자나 부채로 조달하게 된다. 이때 희석과 이자 부담이 겹친다. [F62] [F64] [F65] [F67] [F53] [F3] [C:fcf_margin@FY2025]
- (12%) 매출 인식과 수금의 질이 무너졌다. 2분기 매출은 1분기보다 줄었는데 매출채권은 6,263만에서 1.2억 USD로 늘었다. 상위 고객 집중과 특수관계 가능성(G42·MBZUAI)을 보면 매출이 현금으로 바뀌지 않을 수 있다. 감사의견·정정 여부도 확인되지 않았다. 이후 수금 지연, 매출 인식 시기 조정, 재무제표 정정이 나오면 신뢰가 한꺼번에 사라진다. 이는 20배를 넘는 EV/매출 배수가 가장 크게 반응할 사건이다. [F30] [F31] [F32] [F33] [F48] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm) [C:ev_revenue]
- 약한 가정 `base.fcf_margin`: FY2025 FCF 마진 -77.0%에서 5년 안에 +15%로 올라간다는 가정이다. 모델러의 기본 시나리오는 FY2029까지 마진이 음수이고 마지막 해에 한꺼번에 양수가 된다. 이를 뒷받침하는 GAAP 단위경제가 없다. GAAP 매출총이익률은 14%이고 core 목표는 환산되지 않는다. 역DCF가 요구하는 성장(15% 마진 기준 연 43.2%)과 같은 목표 마진을 쓰고 있어, 가정이 현재 가격과 순환한다. [C:fcf_margin@FY2025] [C:implied_cagr@m15] [F51] [F57]
- 약한 가정 `base.exit_multiple`: 출구 P/FCF 28배는 5년 뒤에도 성장 프리미엄이 유지된다는 가정이다. 같은 시나리오에서 마진·멀티플 효과가 연 -36.6%로 수익률을 가장 크게 깎는다. 즉 기본 시나리오의 수익은 매출 성장이 전부 멀티플 압축에 먹힌다. 고객 집중이 풀리지 않으면 시장은 이 멀티플을 주지 않는다. 약세 시나리오 15배와의 격차가 너무 커서 확률 가중 결과가 이 숫자 하나에 좌우된다. [C:expected_irr] [C:p_loss] [F48]
- 약한 가정 `base.revenue_growth`: FY2027 80% 성장은 경영진의 '3배 이상'보다는 낮지만, 2분기 GAAP 매출이 컨센서스를 밑돌고 1분기보다 줄어든 상황에서는 높다. RPO의 인식 시기를 모르는 채 해마다 성장률이 내려가는 곡선만 가정한다. 기저율 표가 없어 검증하지 못했다. [F52] [F58] [F33] [C:base_rate@base]

## 검증 (L6)

주장 70개 — supported 64 · unsupported 4 · contradicted 0 · leap 2 · 미검증 0

- [unsupported] 슬레이터: 생존은 문제가 아니다. 2분기 말 현금이 크게 늘었고 코드가 계산한 현금 소진 연수가 길다. 그래서 반대 이유는 자본 의존이 아니라 증거 부족과 가격이다. — 없는 근거 인용: C:runway_years@FY2025
- [leap] 앤더슨: 성장 가속이 실제 숫자로 나온다. 2분기 core 매출이 +103%였고 경영진은 연간 core 가이던스를 올렸다. 수확체증 곡선의 초기 구간에서 나타나는 모양이다 — core +103%와 가이던스 상향은 맞다. 그러나 인용 자료에는 이전 성장률이 없어 '성장 가속'이 따라 나오지 않고, '수확체증 초기 구간'은 자료에서 나오지 않는 해석이다.
- [unsupported] 슬레이터: 애크먼은 성장이 현금을 만들지 않고 소모한다고 본다. 이 점은 옳다. 그러나 자본시장 의존이라는 판정에는 동의하지 않는다. 상장으로 현금이 크게 늘었고 코드가 계 — 없는 근거 인용: C:runway_years@FY2025
- [unsupported] 레드팀: FY2027 80% 성장은 경영진의 '3배 이상'보다는 낮지만, 2분기 GAAP 매출이 컨센서스를 밑돌고 1분기보다 줄어든 상황에서는 높다. RPO의 인식 시기를 — 없는 근거 인용: C:base_rate@base
- [leap] 앤더슨: 슬레이터의 가장 강한 논거는 단위경제 핵심 지표(고객획득비용·순매출유지율·이탈률)가 비어 있어 증거가 없다는 것이다. 이 요구는 존중한다. 하지만 초기 기업의 불 — RPO와 600MW는 맞다. 그러나 인용에는 인식 시기와 해지 조건이 없어 '계약 잔고가 현실이 되고 있다'와 '기다림의 대가가 가격에 나타났다'가 따라 나오지 않는다.
- [unsupported] 레드팀: 출구 P/FCF 28배는 5년 뒤에도 성장 프리미엄이 유지된다는 가정이다. 같은 시나리오에서 마진·멀티플 효과가 연 -36.6%로 수익률을 가장 크게 깎는다. 즉 — 출처 없는 숫자 36.6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2024 | FY2025 |
|---|---|---|
| 매출 (revenue) | 2.9억 USD | 5.1억 USD |
| 매출 성장 (revenue_growth) | — | 75.7% |
| 영업이익률 (operating_margin) | — | -28.6% |
| 영업현금흐름 (ocf) | 4.5억 USD | -1,005만 USD |
| 설비투자 (capex) | 2,344만 USD | 3.8억 USD |
| FCF (fcf) | 4.3억 USD | -3.9억 USD |
| FCF 마진 (fcf_margin) | 147.6% | -77.0% |

표에 없는 키도 인용할 수 있다: debt_total, non_gaap_net_income, operating_income

### 시장 · FY2025 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 127.21 USD/share (2026-10-16, F61) |
| 희석 주식 수 (shares) | 1.5억 |
| 시가총액 (market_cap) | 192.0억 USD |
| 순현금 (net_cash) | 58.2억 USD |
| EV (ev) | 133.8억 USD |
| FCF 수익률 (fcf_yield) | -2.0% |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 26.24x |
| PER (pe) | — |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | 17.2 |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 역DCF — 현재 가격이 가정하는 것

EV 133.8억 USD를 정당화하려면 매출이 10년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 목표 마진으로 직선 수렴, 할인율 10%, 이후 영구성장 3%.
기본 시나리오 목표 마진 15% 기준: 연 43.2% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 50.7% | C:implied_cagr@m10 |
| 15% | 43.2% | C:implied_cagr@m15 |
| 20% | 38.4% | C:implied_cagr@m20 |
| 25% | 34.8% | C:implied_cagr@m25 |
| 30% | 31.9% | C:implied_cagr@m30 |

### 시나리오 가치 — 5년, 할인율 12% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 30% | 14.1억 USD | 22.5% | 0% | 15x | 22.91 | 13.00 | -29.0% |
| 기본 | 50% | 37.2억 USD | 48.8% | 15% | 28x | 110.77 | 62.86 | -2.7% |
| 강세 | 20% | 87.4억 USD | 76.5% | 25% | 30x | 411.13 | 233.29 | +26.4% |

확률 가중: 주당 가치 144.49 · IV 81.99 · 기대 연 수익률 +2.6% (C:expected_irr) · 손실 확률 80% (C:p_loss) · 현재 주가 127.21

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +39.7% · 마진·멀티플(P/S) -36.6% · 주식 수 변화 -3.9% · 현금 축적 -1.9% = -2.8%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -9.9% | -6.3% | -3.2% |
| +0%p | -6.8% | -2.7% | +0.7% |
| +5%p | -3.4% | +1.1% | +4.9% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 8.2억 USD | -58.6% | -4.8억 USD | 1.6억 | 53.5억 USD |
| FY2027 | 14.7억 USD | -40.2% | -5.9억 USD | 1.6억 | 47.6억 USD |
| FY2028 | 22.0억 USD | -21.8% | -4.8억 USD | 1.7억 | 42.7억 USD |
| FY2029 | 29.7억 USD | -3.4% | -1.0억 USD | 1.8억 | 41.7억 USD |
| FY2030 | 37.2억 USD | 15.0% | 5.6억 USD | 1.8억 | 47.3억 USD |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 43.2% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 48.8% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 76.5% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=15.20x, revenue_5y=17.13x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=50.9억 USD, runway_years=17.2
- 애크먼 case={"from": "base"}: price=127.2, fcf_positive=아니오, leveraged=아니오, intrinsic_value=62.9, mos=-102.4%

### 계산 경고

- 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-08-12 | [10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm) |  |
| S2 | filing | 2026-08-12 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrs-20260812.htm) |  |
| S3 | filing | 2026-06-24 | [10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044981/cbrs-20260331.htm) |  |
| S4 | filing | 2026-06-23 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044941/cbrs-20260623.htm) |  |
| S5 | filing | 2026-05-15 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035605/closing8-k.htm) |  |
| S6 | filing | 2026-04-17 | [S-1](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm) |  |
| S7 | news | 2026-08-31 | [What Does Cerebras Systems (CBRS) CS 4 Launch Mean For Its AI Push? - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxOT09BeDlRRVhLRGl3UnQxLXBzY1JXUEV6ckZ4N0JpZjdKRDBBdmpDT1BNMGgwZkFTVTROV0h1NVplVkdLZ0RVMUZ3WW15Q3J0ay05WmdtRGd1YkFMM2Z5UzBMNnBtTzN6Y0VUNEhMbTI2aWRrNjdVcW05N3Q5a1BkdUpRRGFrM0FtczBoQW1FSXJzUlJ3aVFvdQ?oc=5) | Yahoo Finance |
| S8 | news | 2026-08-18 | [Introducing Cerebras CS-4: The Fastest AI Just Got Faster - Cerebras](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBmMUQxb0dVSUo2UzM1MVE2dExHRlRYUlg2QW1GSktqeTd0WmVldXpKaVFIVUxaWVpwQ0RpQlpnYjBUZWJ4ZmZBWHowMzlRQkdPV0E3VzE3VkxfdjJtUmNBNFE1dFI?oc=5) | Cerebras |
| S9 | news | 2026-08-25 | [Cerebras shares plummet 16% after results fail to impress investors - Reuters](https://news.google.com/rss/articles/CBMingFBVV95cUxPS3RxTUJxMTh2Mk9XSmgxdm1MZDh6MlRtcVl5aFM1bmF1ajVmWlFnUF9nNU0yYjloQ0pON2VSWFZBYTVldmJ0TGI5N2psYlcwZVRuSURZaUM1NkYzVkh4NGVNRUtjd0F0M3RMTno2X0RSNG9VbF91V2lDOUh0OG5nSDJiY2M4cDdrM1lGRnNicldnNXBBQTBDRFVzNHdJQQ?oc=5) | Reuters |
| S10 | news | 2026-10-01 | [Cerebras Systems: This Is Not A Golden Buying Opportunity (NASDAQ:CBRS) - Seeking Alpha](https://news.google.com/rss/articles/CBMingFBVV95cUxQNk5ZWDcya0pXamNfMGIybGhZNGQ4U05LX21iUFVZeDhKd3gtUlR5dWFjXzNSd3FZc1JUQlJCX0NoSWpmNEpWdkZ5UjBQcjZ3dEFxMWF2NF85XzBibThSLXNPeE54SlpwX0FwM1FrQktNT1ZoaU10V3NWb2J1aWNyamlpbTdaTHV5bHRueWpJcFQtNFBxQWNaY01rR19qUQ?oc=5) | Seeking Alpha |
| S11 | news | 2026-08-13 | [Cerebras Systems CEO Andrew Feldman on Q2 earnings: ‘We are pretty proud of the results’ - CNBC](https://news.google.com/rss/articles/CBMijgFBVV95cUxQYkF3cWRoc0l6SnJFYXhUVUtwemJGUWpIUFRYR2REaDJIeWVpVnpnaTQtRWhZUHNEdHpPOWt0c2ptVUlyNWRuWDZvUV9lb1JVSXVhekNFZjhFSDRJT192ZlBocGd0NzkxRkcwMzhmYWlEOUFEV05mbHZXajNUdnlneDRoVl9rUm91Vm13UEFR?oc=5) | CNBC |
| S12 | news | 2026-10-05 | [Cerebras Systems' Tough 2026 Continues: It'll Double Soon According to One of The Biggest Global Banks - 24/7 Wall St.](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNaEpZUi0xamI3SFN4QlNMakxWVkNnTTUtU3BDakQzMmJFVDkwdHppZzl0LUQ1NUdOV0ZQczJhT1FJa0ZJUXlidWUxSDQ4aE5sY1FmQlBHQWJIUFZiNzZEaG44NU4zRFBPUkF1LXJEY1AzR0pJTkFoZE92RzBwUjIyMHhnZE5zSmxJYlZDa3BJV1hTOFNmM2lJTjhhTmJrTlV6QnVKX3B4cWN4WVYyM1FKd3otOE5OOHZiNGlxc0tiYWU4R0ZOX01TVXh0VndUUEQ3Smdxa21kbTJ0UWM?oc=5) | 24/7 Wall St. |
| S13 | news | 2026-09-04 | [Why is Cerebras Systems stock surging today? - Investing.com](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPYkJybUthcmRzWWJfekdnTlJuaWJkOVFBRHJTbUVUMVQwYzRxV0sxWE9CR0x1OHVwTV80d09QMXF6ZDdFX2pQYkFwZVk0ek91TjZxWEUzRGQ0N25hMDl2czJ1QlZETzhVWDRVZENMMTJUX3dqRFRwMDR3V3R5QS1ZX1dzaVI5V0ROWGhUNWd3UV9zdFdaQjBoSGs4dUFmcU1kY0M3TlNJRTg?oc=5) | Investing.com |
| S14 | news | 2026-08-31 | [Cerebras Systems (CBRS) Stock Looks Fairly Valued With Book Value Steady And Growth Risk Unclear - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxQLWI2OVlHSEZpcEVGdzhXQ2xQQ0dQSjN2a0NSdUF0QlFQdHEwcHpSVWVxNXZqWlBmZV9sSU53bjV3eHlDYTFobGZmRDNlTEYyNkV0aEh1TjFMY0RwdGFzT1V0M0k0RGgxM2ZyT3c1RjY4NE82czlrNnB1VnVCX0tMQlhVelRGQnhpOWZTQklfN1hfOVBYZDlXZ180ci1wM2c?oc=5) | Yahoo Finance |
| S15 | news | 2026-08-25 | [Ultrafast Frontier Inference \\| Cerebras Hot Chips 2026 - Cerebras](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNjNfbnRoZFloVUFkdDZxWUppbzg1ejVBcTIxVGVxQXZOS0hNZFdPVi02UFVGdU1oR0NPWjBrelZnUnY2bHFDSm1hdDl2a0JDNnBWNV9YQ2ZyT21nOWt6TTdFZjZNMm4tMVUzX3lYQy1QMzMwbmNuSmFZalQycjNZQlhFSTRfa2RYeHVFUnFXSGs0aGRMNGVSOGRR?oc=5) | Cerebras |
| S16 | news | 2026-09-28 | [Cerebras to supply AI systems to cloud computing startup Gimlet Labs - Reuters](https://news.google.com/rss/articles/CBMirgFBVV95cUxOMDgtbmhLenNVQVdOQXJDbmJmck52THdJR3BYWV8zeXdjRFdieFdIdUNlTTNreWNWSy1obHdabzhtakNsQldBeGF6Y0RwLTQ0ZVRzZy11UkFycEx6azI0dWM1enN5NkdHTEg3N1VhajVFZEFqMmlKblo3Y2Zmam1wUTNLS3ZNYTd2b2MxdWNVQzJtdklpVV92WS1wZllQVGVBak9mUEdkeldoWFZRWFE?oc=5) | Reuters |
| S17 | news | 2026-07-23 | [Final Trades: Abbvie, Transocean, Cerebras Systems and Netflix - CNBC](https://news.google.com/rss/articles/CBMipAFBVV95cUxQa0NWX0Jva09Qc00tX3Fybjd5N2p5X2ZjbklnZlR2cUUzRUpqN1VhV0VXcU9YWExzZVlkMl9iZWVwQ2dzcGNaMnZJcGJDREp4c2Q4aURkc2w3QjdYREVHNEEzcGsycGlpTGV2NVgxbm9oSFd2YzhvVkJhTHFiby01dGxRMnFzMEE0QkZOV0l5MFFqZjRJcTN1eUo1a0N6VnM5SHJzZw?oc=5) | CNBC |
| S18 | news | 2026-07-23 | [AMD and Cerebras Announce Disaggregated AI Inference - Cerebras](https://news.google.com/rss/articles/CBMiywFBVV95cUxQSGxfRjlGZUZfR1hack0zbEdZcVJXY1JCaWw4dl9fMFZnQnJHVnVfU3NsZkpVd2hPbjh5Q0dHTVcxYTByelU2b3lMUzVDNk54ZFN4OG1VSko2MXEzV0d3bDdHSTJiRHlrMFZtallYSllLUzdSQ2lVdDVra2ZqY0xPaEV2cmxRaXRIWnhRd19obk82eFBGQXQ1YnpYc2hLY0poOGVsdS1yZ19mVGs0RlFVZ1diV0luRktiNV9Uc05vSHpEbmViQ1NjX1h1UQ?oc=5) | Cerebras |
| S19 | news | 2026-10-16 | [Cerebras Systems (CBRS) Stock Looks Stretched Following Its 54% Slump - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxOT2FhTUFkZVhBM1RBdm1vS2VXdlpudndaVVNvcTIzSnhXNVRGRHRNYjROZlV5OXNXUmFTZDVsTDQ0Sm93QWhnZ2RQemlDcURXS090a0xOVWJKSlBXMFdlUkg0aERSQWY4UXo4WlBQbFdmOURsdmU1Y3luUnh2eXJSU2VkUFZQd1JnT19zUlB3R08wQ0tqcVZtc1JvdG9venc?oc=5) | Yahoo Finance |
| S20 | news | 2026-08-12 | [Cerebras stock plunges 14% after second earnings report following IPO - CNBC](https://news.google.com/rss/articles/CBMif0FVX3lxTFBJcHVySkhhUXc0UTFTUU44MC1zazJYSFpyMVRkdy1MUG5QSDBOX1dkVmstdi1VWVBZTm91U2ZXYzhXZmlzUlAzT2NNdExXMVZ6eWdyQkQ0eFA0UzU3amczTzYxQkthMTRWOXJGRjZ0bzQyT2F6b1pGbFMwN1hHcTDSAYQBQVVfeXFMTlk2ekExUzkydDVRQ1E3elduc0F5c08tUklVMFJBazUyS1lEZml4alVXSTdxYWpSdVdiVEFuVnMtVnFSTnNOWjZsaldlUlFyMnBEU0pWbkFJektITkdWSnItZS05aFBfRm94X1ZOV1J0Y3FIdXBUdklRLWZJSktrekxYRG8x?oc=5) | CNBC |
| S21 | news | 2026-09-28 | [Cerebras - Cerebras](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNX2piOFVCQm13SEhULVljVDFLTmt0YVJtcnEtR1AxMVc4YlR6aktwcWJPVzVVNnZSU2c2ZUQ1LVVJQ09jVFA5NzBxbndoTFljM1ozV29mWHB3NnZpbmZnd1FGNFhLT1Zlbk5GajR3SFJQTHJ2STNxMGtDbmVhTHZaOXRFM2tib0JkdFRwVWlTWjF4azFEQmRRYVVGdmpwUW1GZ3laTDZ1cmd2OExLUjR4UmpmcGs2UEVnd0RubWpKeTlnU3dfVWpZbg?oc=5) | Cerebras |
| S22 | news | 2026-08-24 | [Cerebras Systems (CBRS) Revenue Surges: Why Did CBRS Stock Crash, and What About AMD? - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxPNFhsamgwSTdhZnk4U1N2X1Z2cUZGV2hSR0tMVzRDN3FVMFhTb25NTGRYSi1MWW9iV0R1VkdLRVYtVm5sekRmOElIY1F2RWlfV0JDUVlsWGZoQnZlcU9UWmljWlhqamR3VHpFWVVpeHhhSmtpMmEybjlKUjN1dEJnNElQejdqa1lJT1kzUlkwQmhXM3BtRXJlQW5nQVpLQ21ULXlR?oc=5) | Yahoo Finance |
| S23 | news | 2026-08-26 | [Can Cerebras Systems (CBRS) Justify Its Valuation After ARK Bought More Shares? - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxON193TXVxMVBxVjZxa3RCNlY0Zlg4N0pjTVAybWdLNHk2UUwzTTJQd0VYaVU0R1hIdEUzcTR1eHRpZW9pajNpQk9wZVNkTk83WjRtdE5YMm50b2hldUxrYnlhVGp2VldTcFlVRVBHNlVYVFd2ZldQZDYycjdZVWlDQjd0c0pMWDBQTVlFTldkS281MHhFbmNwa3ZOblhVckI4MklndDR4aw?oc=5) | Yahoo Finance |
| S24 | news | 2026-10-13 | [Can Cerebras (CBRS) Turn Its $25.4B Backlog Into High-Margin Growth? - Yahoo Finance](https://news.google.com/rss/articles/CBMikgFBVV95cUxOalM0ejc1WHVWb29zVVZRdEFSVm5aeWhSUDVLVjlUZDAyc1Y2LWhfa1RTTVNXYVM2ZzRSY0Q3cW1pdDN2Q21FeWYybUNwLWRtMl9reTVyb1RDSDdCTmxBRXlselNHTUtfdTY4eG15WDVWQzJxRWxOVlNQdFo1WkRwMkZwQmRKQkotR0xaYlRZc1l1Zw?oc=5) | Yahoo Finance |
| S25 | news | 2026-08-12 | [Cerebras Systems CEO Andrew Feldman at All-In We Make AI ‘Blisteringly Fast’ - Yahoo Finance](https://news.google.com/rss/articles/CBMiigFBVV95cUxQSWFJbDFFcFFnWDZiRlRYemRpQjhpcFFUUFJTZ3RNQmI3MGo0RGE2T25QeEdVZl9sVnE1X3hlYWlfdUtBMnVNOEJ6N2NsdWlQWlFCLTRydlNSQV85ajJidVRnLXRrUks0TmdQZjlNMEgyTGVyd2VXbGpjeTZ2ZURIU3M0QXdxRThDUnc?oc=5) | Yahoo Finance |
| S26 | news | 2026-09-30 | [Cramer's Mad Dash: Cerebras Systems - CNBC](https://news.google.com/rss/articles/CBMiggFBVV95cUxNVUpQVFJGd18yU244eVpCSTNYeUpWUXJFMm5QbGQtUVFWSm96Z3dNYW91LWFBQ2RLMmt1bFJ0REl1QVFwVXVERzZzZUZxTERUNmJ3RGlRR0ltTDJCZXpkQktKNlAyTTBQSnNNZmNmZFhDRGxmdndFUDJ6SkkwUkY0eUF3?oc=5) | CNBC |
| S27 | data | 2026-10-13 | [Cerebras Systems Inc. (CBRS) Down 4.8% — Time to Cash Out? (Weiss Ratings)](https://weissratings.com/en/instant-news-alerts/cerebras-systems-inc-cbrs-down-4-8-time-to-cash-out) | CBRS 종가 $175.44 (-4.78%, -$8.80), 52주 고가 $386.34(2026-05-14) 대비 약 54.6% 아래. 기사에 날짜가 없고 '화요일'로만 적혀 있어 2026-10-13(화)로 추정. S19(10-16, '54% 하락')와 수준이 맞지만 실제 기준일은 확인 필요. |
| S28 | data | 2026-10-16 | [Cerebras Systems (NASDAQ:CBRS) quote — Motley Fool / Chartmill 보유 현황](https://www.fool.com/quote/NASDAQ/CBRS) | 발행주식수 약 2.1961억 주 (Fool 시가총액 $51.54B는 주가 $234.82 기준). 날짜는 확인하지 못해 조회 시점으로 둠. chartrow는 1.51억 주(2026-09-18)로 불일치. 2분기 가중 희석주식수 1.5억은 5월 IPO 이전 구간이 섞여 있어 기말 주식수보다 작으며, 2.196억이 기말 기준에 더 가깝다고 판단. 10-Q 표지 주식수로 확인 필요. |
| S29 | call | 2026-08-12 | [Cerebras Systems (CBRS) Q2 2026 earnings summary - Quartr](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) | 2026 Q2 요약(어닝콜 기반, 2차 요약). Core 매출 $209.9M(+103%), GAAP 매출 $180.1M(+74%). Core 매출총이익률 41%, GAAP 14%. Q3 core 매출 가이던스 $214~216M, core 매출총이익률 38~40%. 2026 core 매출 가이던스 $880~890M(기존 $855~865M에서 상향). 2027년 매출은 3배 이상 증가 계획, core 매출총이익률은 60%대 이상을 향한다고 함. 계약된 데이터센터 용량 600MW. 2027 경영진 목표는 회사 발언이지 입증된 수치가 아님. |
| S30 | news | 2026-08-12 | [Cerebras (CBRS) Q2 2026 (USD): Revenue 180.1mln (exp. 194mln) - Newsquawk](https://www.newsquawk.com/headlines/cerebras-cbrs-q2-2026-usd-revenue-1801mln-exp-194mln) | 보도. 2분기 GAAP 매출 $180.1M은 컨센서스 $194M 하회(하드웨어 부진, 클라우드는 상회). 3분기 core 매출 컨센서스(가이던스 이전) $211.9M. 2026 core 매출 컨센서스(가이던스 상향 전) 약 $863.4M. GAAP 매출총이익률은 기대에 크게 못 미침. |
| S31 | data | 2026-10-16 | [Yahoo Finance CBRS historical prices](https://finance.yahoo.com/quote/CBRS/history/) | 2026-10-16 종가 127.21 USD |
| S32 | news | 2026-08-18 | [Cerebras Systems Introduces Superfast AI Accelerator - Investor's Business Daily](https://news.google.com/rss/articles/CBMijAFBVV95cUxOcUpZSVhkNDcyU0lXNWx4WHF0ZTRweFE2N3pvbU5URlU4SjQtQVRXekhGV0t4TFVWa1A1YTY1U2pwRGExR3EydjI4U3E4ZTRDZzZaX2VMVjhWUXVNUWJBNnBYcmRrYmhmRm5pc3lxcUlVaGp4OG1qUVl1Ym1aa3BDVHlyYWdWRzF1RkpUaA?oc=5) | Investor's Business Daily |
| S33 | filing | 2026-09-01 | [Cerebras Systems 424B4 prospectus](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm) | 현금흐름(천 달러): 영업활동 2025 (10,050) · 2024 451,978 / 유형자산 취득 2025 (382,739) · 2024 (23,435) / 매출 2025 509,991 · 2024 290,252 |

# Datadog (DDOG) 리서치 보고서 — 기준일 2026-10-18

**반대 우세** — 찬성 0 · 반대 1 · 보류 2 · 확신 가중 점수 -0.27 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장 내재: 매출 10년 연 26.8% (FCF 마진 27% 수렴 가정) · 기본 시나리오: 5년 연 21.7%
- 시장이 반영한 것: 주가 247.11달러(F215)의 EV는 FCF 마진이 25%로 수렴해도 향후 10년 매출이 연 27.7% 커지는 것을 전제한다(C:implied_cagr@m25). 마진이 20%면 연 30.6%(C:implied_cagr@m20)다. P/FCF는 77.6배(C:p_fcf)이고, 주가는 10월 9일 사상 최고 종가까지 올랐다가 10월 16일 하루에 7.19% 내렸다(S40).
- 우리가 다르게 보는 점: 우리 기본 시나리오는 5년간 성장이 30%에서 16%로 둔화하고 FCF 마진이 27%로 낮아지는 경로다. 시장 가격은 이보다 성장이 훨씬 오래 높게 유지된다는 쪽에 가깝다. 또 보고 FCF는 SBC를 비용으로 보지 않으므로, SBC 차감 FCF(C:fcf_after_sbc@FY2025)와 연 4% 안팎의 희석을 반영하면 주주 몫은 보고 FCF 수익률(1.3%, C:fcf_yield)보다 작다.
- 왜 우리가 맞는가: 첫째, 최대 AI 고객의 사용량 감소(S39, S23)는 사용량 기반 과금의 집중도 위험이 실제로 나타난 것이다. 둘째, 매출이 이 정도 규모에서 10년 가까이 높은 성장을 유지한 기업은 드물다는 점은 기저율로 확인된다. 단, 컨센서스 매출을 찾지 못해(리서처 보고) 시장 추정과의 차이는 컨센서스가 아니라 역DCF로만 비교했다. 따라서 이 variant는 가격에 내재된 가정과 비교한 것이다. [F215] [C:implied_cagr@m25] [C:implied_cagr@m20] [C:p_fcf] [C:fcf_yield] [C:fcf_after_sbc@FY2025] [S40](https://finance.yahoo.com/quote/DDOG/) [S23](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5) [S39](https://www.benzinga.com/node/62160028)
- 촉매: FY2026Q3 실적(AI 고객 감소의 실제 규모, 비AI 성장 속도, 총이익률 추이)과 FY2027 첫 가이던스.
- 시점: FY2026Q3 발표부터 FY2027 가이던스가 나오는 FY2026Q4 발표까지.

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **125.32** vs 주가 247.11 · 기대 연 수익률 **-4.0%** · 손실 확률 80%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 30% | 79.63 | 49.44 | -20.3% | FY2026은 이미 가이던스(F218)로 거의 정해져 있어 성장률 30%는 그대로 둔다. 그 뒤 최대 AI 고객의 사용량 감소(S39, S23)가 다른 대형 AI 고객으로 번지고, 관측 도구 경쟁(Dynatrace, |
| 기본 | 50% | 201.60 | 125.18 | -4.0% | FY2026은 가이던스 상단 부근(F218)에서 시작한다. 이후 성장은 비AI 고객의 20%대 후반 성장(S39)과 RPO 증가(+43%, F225), 청구액 증가(+38%, F226)에 힘입어 완만하게 둔화한다.  |
| 강세 | 20% | 385.68 | 239.48 | +9.3% | AI 고객 감소가 일회성으로 끝나고 AI 워크로드가 늘면서 관측 수요가 커진다. 고객 약 33,400곳(F227)과 ARR 10만 달러 이상 고객 4,720곳(F228)이 플랫폼 교차판매로 계속 늘고, NRR는 낮은 |

## 3. 반증 조건 (thesis break)

- [미충족] 앤더슨: 순매출유지율이 낮은 120%대 아래로 내려가면 기존 고객 확장 가설이 약해진다 — `nrr < 1.15`
- [미충족] 앤더슨: Non-GAAP 총이익률이 77% 아래로 내려가면 규모의 경제 가설이 훼손된다 — `gross_margin_non_gaap < 0.77`
- [수동 확인] 앤더슨: 최대 AI 고객 외에 연 1,000만 달러 이상 AI 고객이 추가로 사용량을 줄였다고 공시·어닝콜에서 확인되면 성장 가설 훼손 — 수동 확인
- [자료 없음] 슬레이터: 3분기 매출이 가이던스 하단 미만이면 AI 고객 감소가 반영 수준보다 크다는 뜻 — `revenue < 1.135e+09` (FY2026Q3)
- [자료 없음] 슬레이터: 10만 달러 이상 고객 수가 현재보다 줄면 대형 고객 침투 가설이 깨진다 — `customers_100k_arr < 4700` (FY2026Q3)
- [자료 없음] 슬레이터: 비GAAP 총이익률이 78% 아래로 내려가면 단위경제 악화 신호 — `gross_margin_non_gaap < 0.78` (FY2026Q3)
- [미충족] 애크먼: 주가가 기본 시나리오 현재가치 125달러의 80% 이하로 내려오면 안전마진 20% 기준이 충족되어 재검토 — `price < 100`
- [자료 없음] 애크먼: Q3 매출이 가이던스 하단 미만이면 성장 둔화가 가속된다는 뜻이므로 반대 입장 강화 — `revenue < 1.135e+09` (FY2026Q3)
- [수동 확인] 애크먼: AI 고객 사용량 감소가 일회성이고 규모가 제한적임이 공시로 확인되면 단순성 평가 재검토 — 수동 확인
- [충족 — 훼손] 레드팀: FY2026Q3 매출이 가이던스 하단 11.35억 달러(F219 범위)를 밑돎 — 가이던스 적중 이력이 깨지고 성장 둔화가 시작됨 — `revenue < 1.135e+09`
- [미충족] 레드팀: ARR 10만 달러 이상 고객 수가 FY2026Q2 4,720곳(F228)보다 줄어듦 — 대형 고객 이탈이 AI 한 곳을 넘어 번지는 중 — `customers_100k_arr < 4720`
- [미충족] 레드팀: FY2026Q3 비GAAP 총이익률이 79%를 밑돎 — 하락 추세가 이어지며 단가·원가 압박이 진행 중 — `gross_margin_non_gaap < 0.79`
- [미충족] 레드팀: FY2026Q3 희석 주식 수가 가이던스 3.78억 주(F217)를 넘음 — 희석이 계획보다 빠름 — `diluted_shares > 3.78e+08`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | revenue | FY2026Q3 | >= 1.14e+09 | 90% | Q3 가이던스 중간값(F219)이다. 지난 분기 가이던스를 넘긴 이력(C:guidance_hit_rate)이 AI 고객 감소를 반영한 가이던스에서도 이어지는지 시험한다. |
| K2 | revenue | FY2026 | >= 4.47e+09 | 80% | 연간 가이던스 상단(F218)을 넘는지 본다. 기본 시나리오의 첫해 성장률 30%와 AI 고객 감소가 가이던스에 충분히 반영됐는지 시험한다. |
| K3 | customers_100k_arr | FY2026Q3 | >= 4850 | 80% | 대형 고객 침투(F228)가 AI 고객 감소와 별개로 이어지는지 시험한다. 기본·강세 시나리오의 교차판매 가설이 여기에 달려 있다. |
| K4 | gross_margin_non_gaap | FY2026Q3 | >= 0.79 | 70% | 총이익률이 79.6%(F232)에서 더 내려가는지 본다. 하락이 이어지면 약세 시나리오의 단위경제 약화와 FCF 마진 22% 경로 쪽으로 기운다. |
| K5 | free_cash_flow | FY2026Q3 | >= 2.5e+08 | 70% | 최근 분기 FCF 2.8억 달러(F224)가 유지되는지 본다. 기본 시나리오의 FCF 마진 27% 수렴 경로를 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.27 · 비중 참고값 0.0% (반대 우세 — 신규 비중 없음) · 슬레이터 시작 비중 1.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 보류 → 보류 | 2/5 | ✗ 10년 주당가치 5배 미만 또는 계산 불가 (LTGG Q10) | 2/5 실패 | founder_led=예, upside_10y=3.59x, revenue_5y=3.22x |
| 슬레이터 | 보류 → 보류 | 3/5 | ✓ | 1/5 실패 | unit_economics=proven, survival_path=예, starter_weight=1.0%, cash_survives=예, cash_min=4.3억 USD |
| 애크먼 | 반대 → 반대 | 4/5 | ✗ 단순·예측 가능한 사업이 아님; 안전마진 20% 미만 또는 계산 불가 | 1/5 실패 | simple_predictable=아니오, capital_markets_dependent=아니오, catalyst=없음, intrinsic_value=125.2, mos=-97.4%, fcf_positive=예, net_debt_to_ebitda=-5.55x |

- ⚠ 앤더슨: arguments[2] unsupported: FY2022 매출 16.8억 달러와 그 사이 총이익률 80% 안팎·FCF 마진 20%대 후반~30%대 초반 유지는 FY2025 값만으로 받쳐지지 않는다.
- ⚠ 앤더슨: arguments[4] unsupported: 없는 근거 인용: C:base_rate@bull, C:revenue_cagr@강세, C:fcf_margin@강세, C:exit_multiple@강세
- ⚠ 앤더슨: risks[1] unsupported: 출처 없는 숫자 19.6%, 20.9%, 4.1% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 앤더슨: arguments[2]: 인용하지 않은 근거의 숫자 1.68e+09(C:revenue@FY2022·F156), 3.43e+09(C:equity@FY2025Q3·C:fcf@bull·C:revenue@FY2025) — cites에 추가
- ⚠ 앤더슨: rebuttals[0]: 인용하지 않은 근거의 숫자 125(C:expected_iv·C:intrinsic_value@ackman·C:iv@base), 97.4%(C:mos@ackman), 32(C:exit_multiple@base), 10%(C:discount_rate) — cites에 추가
- ⚠ 슬레이터: rebuttals[0] unsupported: 없는 근거 인용: C:upside_10y@앤더슨
- ⚠ 슬레이터: rebuttals[1] unsupported: 없는 근거 인용: C:intrinsic_value@애크먼
- ⚠ 슬레이터: arguments[0] unsupported: '매출이 두 배로 커지는 동안 총이익률·FCF 마진을 유지'했다는 주장은 FY2025 값만 인용했고 FY2022 시점의 마진은 없다.
- ⚠ 애크먼: arguments[0] unsupported: 없는 근거 인용: C:intrinsic_value@애크먼
- ⚠ 애크먼: rebuttals[2] unsupported: 출처 없는 숫자 20.9% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: rebuttals[0] unsupported: 없는 근거 인용: C:upside_10y@앤더슨
- ⚠ 애크먼: risks[1] unsupported: 없는 근거 인용: C:return_decomp@base
- ⚠ 애크먼: arguments[3]: 인용하지 않은 근거의 숫자 3%(C:capitalized_to_revenue@FY2021·C:capitalized_to_revenue@FY2025·C:roic@FY2024), 1.3%(C:fcf_yield·C:operating_margin@FY2025·C:share_change@FY2025) — cites에 추가
- ⚠ 애크먼: rebuttals[2]: 인용하지 않은 근거의 숫자 32(C:exit_multiple@base), 32(C:exit_multiple@base) — cites에 추가
- ⚠ 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 회계 품질 flags[0] 검증 실패(unsupported): FY2025 SBC 21.9%와 영업이익률 -1.3%는 맞지만 'FY2021 15.9%에서 21~23% 구간 고정'이라는 과거 추이는 인용 자료에 없다.
- ⚠ 사업·산업 findings[7]: 인용하지 않은 근거의 숫자 7%(S40) — cites에 추가
- ⚠ 회계 품질 flags[2] 검증 실패(unsupported): 희석 4.8%와 가이던스상 주식 수 증가는 맞지만 희석의 원인이 SBC 발행이라는 점과 자사주 매입 흔적이 없다는 점은 인용 자료에 없다.
- ⚠ 사업·산업 findings[4] 검증 실패(unsupported): NRR와 최대 고객 사용량 감소의 가이던스 반영은 맞지만 가이던스 범위 44.5억~44.7억 달러와 '올렸다'는 근거가 없다(인용은 4.46억 단일 값뿐).
- ⚠ 모델러 variant 검증 실패(unsupported): '이 규모에서 10년 가까이 높은 성장을 유지한 기업은 드물다는 점은 기저율로 확인된다'고 했지만 인용된 기저율 자료가 없다.
- ⚠ 경영진·자본배분 findings[5]: 인용하지 않은 근거의 숫자 3%(C:capitalized_to_revenue@FY2021·C:capitalized_to_revenue@FY2025·C:roic@FY2024) — cites에 추가
- ⚠ 사업·산업 moat[1] 검증 실패(unsupported): FY2022 매출 16.8억과 FY2025 34.3억은 맞고 FY2026Q2 79.6%도 맞다. 그러나 성장 기간 동안 총이익률과 FCF 마진을 유지했다는 근거는 FY2025 값뿐이고 80.2%도 인용에 없다.
- ⚠ 회계 품질 findings[0] 검증 실패(unsupported): FY2025 발생액 비율 음수와 OCF가 순이익보다 큰 점은 맞다. 그러나 '모든 연도에서 음수'는 FY2025 값만으로는 확인되지 않는다.
- ⚠ 사업·산업 findings[5] 검증 실패(unsupported): Dynatrace·Cisco(Splunk)·클라우드 3사와 경쟁한다는 내용은 인용된 S24, S25 제목에서 확인되지 않는다.
- ⚠ 레드팀 weakest[0] 검증 실패(unsupported): 현재 P/FCF 77.6배와 손실확률은 맞지만 멀티플 변화 -20.9%라는 수익률 분해 값은 인용에 없다.
- ⚠ 회계 품질 findings[1] 검증 실패(unsupported): FY2025 DSO 78.9일은 맞다. 그러나 FY2021 95.4일, 이연매출이 매출과 함께 늘었다는 추이, 신호 없음은 인용 자료에 없다.
- ⚠ 사업·산업 findings[0] 검증 실패(unsupported): 출처 없는 숫자 0.8% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 moat[2] 검증 실패(unsupported): 인용한 S25, S30은 제목뿐이라 텔레메트리와 통합 생태계가 제품 가치를 키운다는 주장이 확인되지 않는다.
- ⚠ 레드팀 premortem[2] 검증 실패(unsupported): 총이익률 하락 수치는 맞지만 80.2%는 인용에 없다. 경쟁사가 값싸게 제공할 수 있다는 내용도 S25 제목에서 확인되지 않는다.
- ⚠ 사업·산업 moat[0] 검증 실패(unsupported): 출처 없는 숫자 90% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)

## 앤더슨 — 보류 (2/5)

> Datadog는 내가 좋아하는 종류의 기업이다. 창업자가 이끄는 플랫폼이고, 매출은 FY2025에 27.7% 성장했으며, FCF 마진은 29.2%다. RPO가 34.7억 달러(+43%)라 선행 지표도 매출보다 빠르다. 비AI 고객 성장이 20%대 후반으로 가속했다는 점도 기반 사업이 건재하다는 신호다. 문제는 가격이다. 연 수익률 질문은 하지 않는다. 다만 10번 질문, 즉 5배가 될 수 있는 길이 보이느냐에는 답해야 한다. 상방 시나리오를 10년으로 늘려도 주당 가치는 현재 주가의 3.59배에 그치고, 5배 문턱에 못 미친다. 주가는 P/FCF 77.56배이고, 사상 최고 종가권까지 올라 이미 상방 시나리오 일부를 선반영했다. 최대 AI 고객의 사용량 감소는 성장 가설을 깨는 사건이 아니라 경로의 소음으로 본다. 그러나 이 가격에서는 소음을 견딜 여유가 없다. 좋은 회사지만 대담하게 담을 만한 비대칭이 지금은 보이지 않는다. 성장 가설이 훼손되지 않았으므로 반대하지는 않고, 기권한다.

*이전 판단 대비: 입장·확신 불변(기권, 확신 2). 직전 판단 이후 새 근거로 상방 case의 10년 가치가 5배 문턱(3.59배)을 넘지 못한다는 결론이 바뀌지 않았다. 10월 16일 종가 247.11달러(F215)에서도 마찬가지다.*

**논거**
- 질문 1·2 — 5년 안에 매출이 두 배 이상이 될 길은 열려 있다. FY2025 매출은 27.7% 성장했고, RPO는 34.7억 달러로 +43%, 청구액은 11.8억 달러로 +38%다. 선행 지표가 매출 성장보다 빠르다. 상방 case의 5년 매출은 현재 기준 연도의 3.22배다. [C:revenue_growth@FY2025] [F225] [F226] [S39](https://www.benzinga.com/node/62160028)
- 질문 3·5 — 플랫폼 교차판매로 전환비용이 쌓이고 있다. ARR 10만 달러 이상 고객이 전년 약 3,850곳에서 약 4,720곳으로 늘었고, 이들이 ARR의 약 91%를 차지한다. 순매출유지율은 낮은 120%대다. 고객이 늘수록 더 쓰는 구조는 수확체증의 전형이다. [F228] [F231] [F230] [S39](https://www.benzinga.com/node/62160028)
- 질문 6·7 — 규모가 커져도 단위경제가 무너지지 않았다. 매출이 FY2022 16.8억 달러에서 FY2025 34.3억 달러로 커지는 동안 총이익률은 80% 안팎, FCF 마진은 20%대 후반~30%대 초반이었다. 자본 집약도가 낮아 매출 성장이 현금으로 바뀐다. 다만 SBC가 매출의 21.9%라서 주주 몫은 보고 FCF보다 작다. [C:gross_margin@FY2025] [C:fcf_margin@FY2025] [C:sbc_to_revenue@FY2025] [C:fcf_after_sbc@FY2025]
- 질문 9 — 시장은 이 기회를 과소평가하고 있지 않다. 역DCF로 보면 FCF 마진이 25%로 수렴해도 향후 10년 매출이 연 27.7% 성장해야 하고, 마진이 20%이면 연 30.6%가 필요하다. P/FCF는 77.56배다. 시장은 이미 대담한 성장을 가격에 넣었다. 시장이 보지 못하는 것을 내가 본다는 variant가 없다. [C:implied_cagr@m25] [C:implied_cagr@m20] [C:p_fcf] [F215]
- 질문 10 — 5배가 되는 길이 보이지 않는다. 상방 case를 10년으로 늘려도 주당 가치는 주가의 3.59배다. 이 case는 이미 낙관적이다(5년 매출 연성장 26.3%, FCF 마진 31%, 출구 P/FCF 45배). 이 이상을 가정하려면 연 20%대 중반 성장이 10년 이어져야 하는데, 이는 기저율 표로도 확인되지 않은 드문 일이다. 드문 일에 거는 것이 내 철학이지만 드물다는 사실을 숨기지는 않는다. [C:base_rate@bull] [C:revenue_cagr@강세] [C:fcf_margin@강세] [C:exit_multiple@강세]

**사전 부검**
- 사전 부검 — 선도 AI 기업과의 9자리 금액 갱신에서 사용량이 Q3부터 줄어든다. 다른 1,000만 달러 이상 AI 고객(현재 8곳)으로 번지면 성장 가설 자체가 훼손된다. 규모를 회사가 공개하지 않아 크기를 가늠할 수 없다. [S39](https://www.benzinga.com/node/62160028) [S23](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5) [F229]
- 사전 부검 — 멀티플 압축이 성장을 상쇄한다. 기본 시나리오에서 연 수익률 분해는 매출 성장 +19.6%에 멀티플 변화 -20.9%를 더해 총 -4.1%다. 사업이 잘 돼도 주가가 안 오를 수 있다. 이 가격에서는 성장이 기대대로 나와도 보상이 크지 않다. [C:expected_irr] [C:p_fcf] [C:p_loss]
- 사전 부검 — SBC와 희석이 주주 몫을 갉아먹는다. SBC가 영업현금흐름의 71.5%이고 희석 주식 수는 연 4.8% 늘었다. 보고 FCF 기준 성장이 주당 가치로 온전히 전달되지 않는다. [C:sbc_to_ocf@FY2025] [C:dilution] [F216]

**반론**
- → 애크먼: 애크먼은 기본 시나리오 현재가치 125달러를 근거로 안전마진 -97.4%라고 하지만, 이는 5년 뒤 출구 멀티플 32배와 10% 할인율에 기댄 현재를 정밀하게 재는 계산이다. 10년 뒤 크기를 재지 못한다. 단순성·예측 가능성을 이유로 든 사용량 과금의 변동성도 NRR 낮은 120%대와 RPO +43%로 보면 성장 가설을 깨는 신호가 아니라 경로의 소음이다. 내가 기권하는 이유는 안전마진이 아니라, 상방 case조차 5배 문턱에 못 미치기 때문이다. [C:expected_irr] [F225] [F230] [S39](https://www.benzinga.com/node/62160028)
- → 슬레이터: 슬레이터의 '3분기 실적에서 증거가 확인되기 전에는 찬성하지 않는다'는 태도는 가장 가치 있는 구간을 놓칠 위험이 있다. 다만 그의 가장 강한 논거인 단위경제 입증과 외부 자본 불필요는 인정한다. 사업 증거가 이미 충분하다는 점에서 우리는 같은 결론이다. 내가 기다리는 것은 증거가 아니라 5배가 될 길이 보이는 가격이다. [C:gross_margin@FY2025] [C:fcf_margin@FY2025] [F228]
- → 레드팀: 레드팀의 첫 번째 부검(멀티플 붕괴)은 성장 가설 자체를 깨지 않고 가격만 바꾸는 시나리오다. 8월 호실적 뒤 급락은 사업 훼손이 아니라 기대 재조정이었다. 반면 두 번째 부검(AI 고객 집중도 전염)은 1,000만 달러 이상 AI 고객 8곳으로 번지면 성장 가설 자체를 건드리는 경로가 될 수 있어 가장 진지하게 본다. 규모가 비공개라 지금은 소음으로 분류하되 반증 조건에 남긴다. [S26](https://news.google.com/rss/articles/CBMingFBVV95cUxOQmQ3VWJCU1ZoZXg2Y0ZHNHJBalpsT1VRRHFQaHlNTWZNRmlRR3dLY2ZVQ1FJbHFrWGdoVEt0dTVMSTlFZkh5T19oWEpGNUUyOUo1ckpIbEZxWkpyRlJQcFFpeDZ3SnlaNm5LM2pQOUpMd0JXZmVlQ1FZR3lIOWVaMkR5Vk1KSTZlenpLTUNUaGRSTHV2ZWFWQzRqSG1ndw?oc=5) [S35](https://news.google.com/rss/articles/CBMilwFBVV95cUxOdVIwdUZJczN6aGpaVzl5V19FZU5WZnpCVVo3aXVCNkJnNU0zcGI3Y19zd0F3MUlXMTAtOUhTemowaGEzajZybW5jR0IwTUJGaUZqWVk4OGE5Ri04czNvSGt6STBhaXRfX1VPY19sUFJNNElZcWtxTTZPMERWbWxsRWFia00yNGY2YzJqNE1mbjQxS2sxTk1J?oc=5) [S39](https://www.benzinga.com/node/62160028) [F229]

**인정한 점**
- 애크먼이 지적한 SBC 문제는 인정한다. SBC 차감 FCF가 보고 FCF보다 훨씬 작고 희석이 연 4.8%라서, 보고 FCF 기준 성장이 주당 가치로 온전히 전달되지 않는다. 상방 case의 3.59배는 이 희석을 이미 반영한 값이라 5배 문턱과의 거리는 더 벌어진다.
- 레드팀의 AI 고객 집중도 부검에서 규모가 비공개라는 점은 인정한다. 이 불확실성 때문에 확신을 올리지 않고 2로 유지한다.
- 슬레이터의 지적대로 3분기 실적(AI 고객 감소 규모, 비AI 성장 지속)이 성장 가설 점검의 첫 시험이다. 기권을 유지하되 가설이 훼손되지 않는 한 반대로 바꾸지도 않는다.


## 슬레이터 — 보류 (3/5)

> 사업의 증거는 강하다. 단위경제가 입증됐고 외부 자본 없이 계획을 실행할 수 있으며 대형 고객 침투도 계속 늘고 있다. 가설 자체는 깨지지 않았다. 다만 지금 가격은 이 증거가 허용하는 것보다 앞서 있다. 코드가 계산한 기본 시나리오 기대 연 수익률은 마이너스이고, 현재 가격은 매출이 오랫동안 매우 빠르게 커질 것을 전제한다. 최대 AI 고객의 사용량 감소가 처음으로 가이던스에 반영된 것도 변수다. 그 규모는 아직 공개되지 않았다. 슬레이터의 방식은 작게 시작해서 증거가 쌓이면 키우는 것이다. 지금은 시작 비중을 1% 이하로 두고, 3분기 실적에서 AI 고객 감소 규모와 비AI 성장의 지속 여부가 확인되기 전에는 찬성하지 않는다.

**논거**
- 단위경제는 입증됐다. 매출이 두 배로 커지는 동안 총이익률은 80% 안팎, FCF 마진은 20%대 후반~30% 안팎을 유지했다. 규모가 커져도 단위 원가가 악화되지 않았다. [C:gross_margin@FY2025] [C:fcf_margin@FY2025] [C:revenue@FY2022] [C:revenue@FY2025]
- 기회의 지속성에 대한 증거가 있다. ARR 10만 달러 이상 고객 약 4,720곳이 ARR의 약 91%를 차지하고, 고객은 약 33,400곳이다. 선행 지표인 RPO는 34.7억 달러(+43%)로 매출보다 빠르게 늘고 있다. 비AI 고객 매출 성장도 가속했다고 한다. [F227] [F228] [F231] [F225] [S39](https://www.benzinga.com/node/62160028)
- 생존은 문제없다. FCF가 흑자이고 현금 4.3억 달러에 순부채가 없어, 계획 실행에 외부 자본이 필요하지 않다. 2022년의 교훈인 자본시장 의존이 없다. [F24] [C:fcf_margin@FY2025] [C:net_debt_to_ebitda]
- 가격이 증거보다 앞서 있다. 현재 EV는 FCF 마진이 27%로 수렴해도 연 26.8% 성장을 10년간 요구한다. 기본 시나리오의 확률 가중 기대 연 수익률은 -4.0%이고 손실 확률은 80%다. 가설이 틀려서가 아니라 가설이 이미 가격에 반영돼서 비중을 키울 근거가 없다. [C:implied_cagr] [C:expected_irr] [C:p_loss]
- 주주 몫은 보고 FCF보다 작다. SBC가 매출의 21.9%이고 SBC 차감 FCF는 2.5억 달러 수준이다. 이 비용이 줄지 않으면 FCF 수익률로 계산한 수익률은 주주에게 도달하지 않는다. [C:sbc_to_revenue@FY2025] [C:fcf_after_sbc@FY2025] [C:fcf_yield]

**사전 부검**
- 사전 부검 — 최대 AI 고객의 사용량 감소가 다른 대형 AI 고객으로 번지면, 사용량 과금 구조상 집중도 위험이 매출 둔화로 이어진다. 규모가 공개되지 않아 지금은 크기를 알 수 없다. [S39](https://www.benzinga.com/node/62160028) [S23](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5)
- 사전 부검 — 비GAAP 총이익률이 전 분기 80.2%에서 79.6%로 내려갔다. 하락이 이어지면 단위경제 개선이라는 전제가 약해지고 약세 시나리오의 FCF 마진 경로로 기운다. [F232] [S39](https://www.benzinga.com/node/62160028)
- 사전 부검 — 성장이 둔화하면 P/FCF 77.56배가 유지되기 어렵다. 사업이 가설대로 움직여도 멀티플 압축만으로 수익률이 마이너스가 될 수 있다. [C:p_fcf] [C:expected_irr]

**반론**
- → 앤더슨: 앤더슨은 상방 case를 10년으로 늘려도 주가의 3.59배라서 5배 문턱에 못 미친다고 본다. 나는 이 숫자가 사업의 질이 아니라 가격의 문제라는 점에 동의한다. 다만 기권의 근거를 '5배 길이 안 보인다'에만 두면 부족하다. 5배가 성립하려면 무엇이 참이어야 하는지 운영 지표로 역산해야 한다. 4,720곳인 10만 달러 이상 고객이 계속 늘고, 낮은 120%대 NRR이 유지되고, 비AI 성장이 20%대 후반을 지켜야 한다. 이 셋은 아직 계획이 아니라 실적으로 확인되고 있다. 그래서 나는 가설이 깨졌다고 보지 않고 3분기 실적에서 증거가 쌓이는지 지켜본다. [C:upside_10y@앤더슨] [F228] [F230] [S39](https://www.benzinga.com/node/62160028)
- → 애크먼: 애크먼은 사용량 과금과 AI 고객 갱신 때문에 단순성과 예측 가능성 기준을 못 채운다고 반대한다. 가격이 안전마진에 크게 못 미친다는 점은 인정한다. 그러나 오늘 10년 FCF를 좁히기 어렵다는 이유로 정의되지 않은 기회를 버리지는 않는다. 가격이 아니라 가설 기준으로 보면 단위경제는 입증됐고 순현금이라 생존에 외부 자본이 필요 없다. 선행 지표인 RPO는 34.7억 달러로 +43%이고 청구액도 +38%여서 계약 기반이 매출보다 앞서 있다. 반대보다 기권이 증거 수준에 맞는 표다. [C:intrinsic_value@애크먼] [F225] [F226] [S39](https://www.benzinga.com/node/62160028)
- → 레드팀: 레드팀의 가장 강한 부검은 AI 고객 집중도가 다른 대형 고객으로 전염된다는 것이다. 이 신호를 must_be_true와 반증 조건으로 올린다. 10만 달러 이상 고객 수와 3분기 매출 가이던스 하단이 기계 판정 조건이다. 총이익률 신호는 79% 기준이 이미 at_risk로 걸려 있다. 다만 전염 확률 20%와 멀티플 붕괴 확률 30%는 서로 겹쳐서 세지 않도록 해야 한다. 멀티플 붕괴는 사업이 맞아도 일어나는 사건이라서 가설 훼손과 구분한다. [F228] [F219] [F232] [S23](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5)

**참이어야 하는 것**
- [on_track] AI 고객 감소에도 3분기 매출이 가이던스 하단 이상
- [on_track] 10만 달러 이상 고객 수가 계속 늘어난다
- [on_track] 순매출유지율이 120%대 초반을 지킨다
- [at_risk] 비GAAP 총이익률이 79%대를 지킨다
- [on_track] 분기 FCF가 지금 수준을 유지한다

**인정한 점**
- 애크먼의 지적대로 기본 시나리오 기대 연 수익률이 -4.0%이고 손실 확률이 80%이므로, 증거가 쌓이기 전에는 시작 비중을 1% 이하로도 찬성으로 바꿀 근거가 없다. 기권을 유지한다.
- 앤더슨과 레드팀이 짚은 대로 SBC 차감 FCF 기준으로 보면 주주 몫이 보고 FCF 수익률 1.3%보다 작다. 그래서 확신을 3으로 유지하되 올리지 않는다.


## 애크먼 — 반대 (4/5)

> Datadog는 좋은 사업이다. FCF 마진이 29%대이고 순현금 상태라 밸리언트식 레버리지 위험도 없다. 하지만 지금 가격은 이 사업을 내재가치보다 싸게 사는 것과 정반대다. 기본 시나리오의 현재가치는 주당 125달러 안팎인데 주가는 247달러라 안전마진이 크게 마이너스다. 가장 낙관적인 강세 시나리오의 현재가치도 주가에 못 미친다. 사용량 기반 과금과 최대 AI 고객의 갱신 감소 때문에 10년 뒤 FCF를 합리적 범위로 좁히기도 어렵다. 즉 단순성과 예측 가능성 기준을 충족하지 못하고, 가격 기준은 크게 어긋난다. 좋은 회사를 비싸게 사면 나쁜 투자다. 촉매도 없다. 담지 않는다.

*이전 판단 대비: 입장은 직전 판단과 같다. 다만 가격 재검토 조건의 기준을 코드 계산 기본 시나리오 현재가치(C:intrinsic_value@애크먼)의 80%인 100달러로 바로잡았다.*

**논거**
- 가격이 모든 것을 말해 준다. P/FCF는 77.56배, FCF 수익률은 1.3%, EV/매출은 23.00배다. 보수적 가정의 내재가치보다 싸게 사라는 원칙과 정반대 지점이다. 기본 시나리오 주당 현재가치 125.2달러 대비 안전마진은 -97.4%이고, 확률 가중 기대 연 수익률도 마이너스다. [C:p_fcf] [C:fcf_yield] [C:ev_revenue] [C:expected_irr] [C:intrinsic_value@애크먼]
- 역DCF상 시장은 FCF 마진이 25%로 수렴해도 10년간 매출이 연 27.7% 커진다고 가격에 반영했다. 이는 FY2025 매출 성장률 27.7%에 가까운 속도를 10년 내내 유지한다는 뜻이다. 규모가 커진 뒤 이 속도를 유지하는 것은 극히 드문 일이며, 가격에 실수 여지가 없다. [C:implied_cagr@m25] [C:revenue_growth@FY2025]
- 단순성과 예측 가능성 기준을 충족하지 못한다. 사용량 기반 과금이라 선도 AI 고객 한 곳의 갱신에서 사용량이 Q3부터 줄어드는 일이 실제로 생겼고, 회사는 그 규모를 공개하지 않았다. 시나리오 연 수익률이 약세 -20.3%에서 강세 +9.3%까지 벌어지고 손실 확률이 80%라는 점은, 10년 뒤 FCF 범위가 넓다는 것을 보여 준다. [S39](https://www.benzinga.com/node/62160028) [S23](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5) [C:irr@bear] [C:irr@bull] [C:p_loss]
- 보고 FCF는 주주 몫을 과대 표시한다. SBC가 영업현금흐름의 71.5%이고 SBC 차감 FCF는 2.5억 달러로 보고 FCF 10.0억 달러의 4분의 1 수준이다. 희석도 연 4.8%로 문턱 3%를 넘는다. 1.3%의 FCF 수익률은 SBC를 반영하면 더 낮아진다. [C:sbc_to_ocf@FY2025] [C:fcf_after_sbc@FY2025] [C:fcf@FY2025] [C:dilution]
- 재무 건전성은 강점이지만 가격을 정당화하지 못한다. 순현금 4.3억 달러, 순부채/EBITDA -5.55배라 자본시장 의존도는 낮고 FCF 마진은 FY2025에 29.2%다. 이는 필요조건일 뿐이다. 좋은 재무가 높은 가격을 상쇄하지 않는다. [C:net_cash] [C:net_debt_to_ebitda] [C:fcf_margin@FY2025]

**사전 부검**
- 사전 부검: 내가 틀렸다면 AI 고객 감소가 일회성이고 비AI 고객 성장이 20%대 후반으로 가속하는 것이 지속되며 RPO(+43%)가 보여 주는 계약 기반이 실제 매출로 이어졌기 때문일 것이다. 그러면 강세 시나리오 쪽 성장이 이어진다. 다만 그 경우에도 강세 시나리오의 현재가치는 주가에 못 미친다. [S39](https://www.benzinga.com/node/62160028) [F225] [C:iv@bull]
- 사전 부검: 시장이 SBC를 비용으로 보지 않고 높은 멀티플을 계속 부여한다면 내 안전마진 기준은 너무 엄격한 것이 된다. 기본 시나리오의 연 수익률 분해에서 멀티플 변화가 가장 큰 마이너스 기여(-20.9%)이므로, 이 가정이 결과를 좌우한다는 점을 인정한다. [C:p_fcf] [C:return_decomp@base]

**반론**
- → 앤더슨: 앤더슨은 성장 가설이 훼손되지 않았다는 이유로 반대 대신 기권을 택했다. 그러나 그의 상방 case가 10년 뒤 주가의 3.59배에 그치고 5배 문턱에 못 미친다고 스스로 인정했다. 가장 낙관적인 case로도 문턱을 못 넘는 종목은 기권이 아니라 담지 않는 것이다. 역DCF가 요구하는 연 27.7% 10년 성장은 기저율로 확인되지 않은 드문 일이고, 그 가격에는 실수 여지가 없다. [C:implied_cagr@m25] [C:upside_10y@앤더슨] [C:p_fcf]
- → 슬레이터: 슬레이터는 단위경제 입증과 생존 경로를 근거로 증거가 강하다고 본다. 그러나 순현금과 흑자 FCF는 필요조건일 뿐 가격의 정당화가 아니다. 그가 직접 인용한 기본 시나리오 기대 연 수익률 -4.0%와 손실 확률 80%는 증거가 가격에 못 미친다는 뜻이다. 3분기 실적을 기다린다는 입장은 방향이 같지만, 시작 비중 1%도 이 가격에서는 근거가 없다. [C:expected_irr] [C:p_loss] [C:net_debt_to_ebitda]
- → 레드팀: 레드팀의 약한 가정 중 가장 큰 것은 기본 시나리오 출구 P/FCF 32배다. 멀티플 변화가 연 수익률의 -20.9%를 차지하므로, 32배가 틀리면 가장 크게 틀린다. 이는 FCF 범위가 넓다는 뜻이고, 그만큼 더 큰 안전마진이 필요하다. 기본 시나리오 현재가치 125.2달러 대비 안전마진이 -97.4%로 이미 20% 기준에 한참 못 미치므로 범위를 넓혀도 결론은 바뀌지 않는다. 사전 부검은 내 반대를 약화하지 않고 강화한다. [C:p_fcf] [C:expected_irr] [C:p_loss]

**인정한 점**
- 앤더슨과 슬레이터가 지적한 대로 비AI 고객 성장 가속, RPO +43%, 대형 고객 수 증가는 가설을 깨지 않는 실재하는 증거이고, 사업의 질 자체는 인정한다. 그러나 이는 가격 기준을 바꾸지 않는다.
- 레드팀이 짚은 출구 멀티플의 불확실성은 내 기본 시나리오 현재가치의 오차 범위가 크다는 뜻이다. 오차가 어느 방향이든 현재가 247.11달러를 정당화하는 쪽은 강세 시나리오 현재가치 239.48달러조차 못 미친다.


## 분석 모듈 (L4)

### 사업·산업 — proven

Datadog는 클라우드 인프라·애플리케이션·보안 관측(observability) 플랫폼을 SaaS로 구독·사용량 기반으로 판매한다. 고객은 약 3.34만 곳이고(S39), ARR 10만 달러 이상 고객 약 4,720곳이 ARR의 약 91%를 차지한다(F228, F231). 여러 제품을 한 플랫폼에 얹어 파는 교차판매 구조다. 단위경제는 양호하다. FY2025 총이익률 80.0%(C:gross_margin@FY2025), FCF 마진 29.2%(C:fcf_margin@FY2025), 순매출유지율은 낮은 120%대이고 총매출유지율은 90%대 중후반이다(S39). 다만 FY2026Q2 비GAAP 총이익률은 79.6%로 전 분기 80.2%보다 낮아졌고(F232), 사용량 기반 과금이라 최대 AI 고객의 갱신 때 사용량이 Q3부터 줄어든다는 점(S39, S23)이 집중도 리스크로 드러났다. SBC가 매출의 21.9%(C:sbc_to_revenue@FY2025)라서 SBC를 차감하면 FCF 마진은 7%대로 낮아진다(C:fcf_after_sbc@FY2025).

- [unit_economics] FY2025 총이익률은 80.0%로 FY2024의 80.8%보다 0.8%p 낮아졌고, FY2026Q2 비GAAP 총이익률은 79.6%로 전 분기 80.2%보다 낮아졌다. AI 관련 인프라 비용 등이 원인일 수 있지만 근거로 확인되지는 않는다. 아직 악화로 단정할 수준은 아니다. CAC와 코호트 자료도 수집하지 못했다. [C:gross_margin@FY2024] [C:gross_margin@FY2025] [F232]
- [customers] 매출은 FY2026Q2 11.2억 달러로 분기 기준 전년(8.3억 달러)보다 크게 늘었고, 청구액은 11.8억 달러(+38%), RPO는 34.7억 달러(+43%)다. 선행 지표가 매출 성장보다 빠르다. [F164] [F161] [F226] [F225] [S39](https://www.benzinga.com/node/62160028)
- [customers] 고객 집중도 리스크가 실현되고 있다. 선도 AI 기업과의 9자리 금액 갱신에서 사용량이 Q3부터 줄어들고 가이던스에 반영됐다. 규모는 회사가 공개하지 않았고 WSJ 보도뿐이라 크기는 확인되지 않는다. AI 고객은 약 750곳이고 연 100만 달러 이상 31곳, 1,000만 달러 이상 8곳이다. [S39](https://www.benzinga.com/node/62160028) [S23](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5) [F229]
- [customers] 비AI 고객 매출 성장은 20%대 후반으로 가속했다고 한다. 최대 AI 고객 변수를 빼도 기반 사업이 성장한다는 신호다. 다만 자동 전사본에 의존한 값이고 정확한 수치는 아니다. [S39](https://www.benzinga.com/node/62160028)
- [unit_economics] 사용량 기반 과금이라 매출이 고객의 워크로드 변화에 민감하다. 이 때문에 NRR가 낮은 120%대(S39)로 높지만, 최대 고객 하나의 사용량 감소가 가이던스에 반영될 정도로 변동성이 있다. 회사는 FY2026 매출 가이던스를 44.5억~44.7억 달러로 올렸다. [S39](https://www.benzinga.com/node/62160028) [F218]
- [industry] 관측 시장은 Dynatrace, Cisco(Splunk), 클라우드 3사의 자체 도구와 경쟁한다. 경쟁사 마진·점유율 교차 확인은 수집하지 못해 경쟁 강도와 점유율 추이는 판단할 수 없다. 클라우드 3사는 공급자이자 경쟁자다. 이 가치사슬상 위치는 증거로 확인되지 않았다. [S24](https://news.google.com/rss/articles/CBMilgFBVV95cUxQNUJxV3VNWlVEX2NYUk9feUpoME1oNWxTQUxJdWxuNm9fU0laS0NSeUF3YXhFUUVacU5ySEFaQUxkZXVDRWlqYU9FaHZ0MWdSNmZDM092MGJaVUliUFdaczJLZEMtZmUzZGUzaWlkLUMxWDktcFkyLWc4d1lvR1VvMEkyU1dnR2xfc0lyVVM3TjJVc1NBLVE?oc=5) [S25](https://news.google.com/rss/articles/CBMilwFBVV95cUxQaktWOHBrbE1lTjlQOHI4aHYwWDE3NHJWY2tLd0NuTkJEUDFXeUhhUXU2dENqZ1NQTzJzOERqTzJnelZwZ3VwNndya0dOZ0hCSzgzVXhLUU5hbDV1ekpVVnFRMThyTGJjZDFhcGVtZFY2SF9mRXl2ZlgxRHNwWngwRmgwTFJRZ0dGNk4zRzIzUEpWbjZ3TGVF?oc=5)
- [runway] 설비투자와 자본화 소프트웨어는 매출의 4~5%로 자본 집약도가 낮다. FY2025 영업현금흐름 10.5억 달러 대비 설비투자는 4,958만 달러다. 벌어들인 현금의 큰 몫을 R&D(FY2025 15.5억 달러)와 인수로 재투자한다. 영업이익률은 FY2025 -1.3%(GAAP)로, GAAP 수익성은 SBC에 눌려 있다. [S39](https://www.benzinga.com/node/62160028) [C:ocf@FY2025] [C:capex@FY2025] [C:rnd@FY2025] [C:operating_margin@FY2025]
- [unit_economics] 수익의 질에서 SBC가 크다. FY2025 SBC는 매출의 21.9%, 영업현금흐름의 71.5%이고 SBC 차감 FCF는 2.5억 달러(마진 약 7%)다. 희석 주식 수도 연 4.8% 늘었다. 단위경제의 '현금' 우수성은 주주 비용을 일부 가린다. [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [C:fcf_after_sbc@FY2025] [C:dilution]
- [proven] 한 플랫폼에 여러 제품을 쓰는 고객이 늘수록 전환비용이 커진다. 그 흔적은 낮은 120%대 NRR과 90%대 중후반 총매출유지율, 그리고 ARR 10만 달러 이상 고객이 전년 약 3,850곳에서 약 4,720곳으로 늘어난 것이다. RPO는 34.7억 달러로 +43%다. 경쟁사 대비 점유율 자료는 수집하지 못했다. [S39](https://www.benzinga.com/node/62160028) [F228] [F230] [F225]
- [proven] 매출이 FY2022 16.8억 달러에서 FY2025 34.3억 달러로 커지는 동안 총이익률 80% 안팎과 FCF 마진 20%대 중후반을 유지했다. 규모가 늘어도 단위 원가가 악화되지 않았다는 뜻이다. 다만 FY2026Q2 비GAAP 총이익률은 79.6%로 전 분기 80.2%보다 낮아졌다. [C:gross_margin@FY2025] [C:fcf_margin@FY2025] [C:revenue@FY2022] [C:revenue@FY2025] [F232]
- [claimed] 수만 개 고객의 텔레메트리와 통합(integration) 생태계가 제품 가치를 키운다는 주장이 있다. 하지만 이를 가격 결정력이나 점유율로 확인한 공시·시장 자료는 이번 근거에 없다. [S25](https://news.google.com/rss/articles/CBMilwFBVV95cUxQaktWOHBrbE1lTjlQOHI4aHYwWDE3NHJWY2tLd0NuTkJEUDFXeUhhUXU2dENqZ1NQTzJzOERqTzJnelZwZ3VwNndya0dOZ0hCSzgzVXhLUU5hbDV1ekpVVnFRMThyTGJjZDFhcGVtZFY2SF9mRXl2ZlgxRHNwWngwRmgwTFJRZ0dGNk4zRzIzUEpWbjZ3TGVF?oc=5) [S30](https://news.google.com/rss/articles/CBMipAFBVV95cUxNZGNDWU50NGpTRFAtTWFGdW80eFJZQmRRT0d3QkxIODU3cWlzSEdKWVdQVmZyU3NPYnpQQWNmUUg5NGQzMGVQS3hPSnBiNUFicFk3MW1UdDhLZ3otMlpOM05Xd0VSM1k1YkpZcm16bWxhc3E3MnlFT1VvVHZteEc5OXF1X3V2a2xMTmVnMlpPdXR4MmN2VTMtOFlhM2hFRVJ1eWpYaQ?oc=5)

### 경영진·자본배분 — mixed

보상 지표, 내부자 매매, 자사주 매입 이력은 수집된 근거에 없어 정렬 여부를 직접 확인할 수 없다. 확인되는 것은 세 가지다. 첫째, 가이던스 적중률은 100%이지만 표본이 한 분기뿐이다. 둘째, SBC가 매출의 21.9%이고 FCF의 상당 부분(SBC/영업현금흐름 71.5%)을 차지하며 희석 주식 수는 연 4.8% 늘어, 주주 몫을 키우는 방향이라고 보기 어렵다. 셋째, 영업현금흐름을 자사주 매입이 아닌 인수(영업권 증가)에 쓴 정황이 있고, 그 수익률은 검증되지 않았다. 증거가 부족해 정렬은 혼재(mixed)로 둔다.

- [compensation] 근거 없음. DEF 14A(S6, S9)는 수집됐지만 보상 연동 지표와 베스팅 기간은 확인하지 못했다. 단기 EPS 연동인지 장기 가치 지표 연동인지 판단할 수 없다. [S6](https://www.sec.gov/Archives/edgar/data/1561550/000162828026028118/ddog-20260429.htm) [S9](https://www.sec.gov/Archives/edgar/data/1561550/000119312526079146/d700416ddef14a.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매매는 수집되지 않았다. 2026-03-02 8-K '경영진 변동'(S8)이 있으나 내용은 확인하지 못했다. 보도(S20)는 창업자들의 주식 차익을 다루지만 매도 규모와 시점은 검증되지 않았다. [S8](https://www.sec.gov/Archives/edgar/data/1561550/000162828026013236/ddog-20260226.htm) [S20](https://news.google.com/rss/articles/CBMitAFBVV95cUxNd1lMVWdzblhuVjJqMFZXMVUyT1kyNENFc0xFNWxaZHBla2tXdFZ5TDlWUlVtRWNYamJORk8zbXhDYmd1cVpQWTNWaTlGV21Hb01ncWlRTmROTFdoQW1sbk5FYmxOUHNaV1FUbjFwUEdXQkhvaDBaLWxtYjQ2SFdUV2dIV1phX1psdXpzanJaMlRNN1RQaHQtUzF4MEV1TGRDOTRUeEx5SjhtN0RGaWc3MVM1QlM?oc=5)
- [guidance] 코드가 대조한 가이던스 적중률은 100%이지만 근거는 FY2026Q2 매출 가이던스 한 건뿐이다(가이던스 10.8억 → 실제 11.2억, beat). 과거 분기 가이던스 이력이 없어 신뢰도를 일반화할 수 없다. 보수적 가이던스를 설정하는 관행인지도 이 표본으로는 구분되지 않는다. [C:guidance_hit_rate] [F220] [F164]
- [guidance] 선도 AI 고객과의 갱신에서 사용량이 Q3부터 줄어든다는 점을 경영진이 가이던스에 반영하고 규모는 공개하지 않았다. 위험을 선제적으로 알린 점은 긍정적이다. 다만 비중과 감소 폭을 밝히지 않아 가이던스의 보수성을 판단하기 어렵다. 고객 집중도는 확인되지 않았다. [S39](https://www.benzinga.com/node/62160028) [S23](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5)
- [dilution] SBC는 FY2025에 매출의 21.9%이고 영업현금흐름의 71.5%에 해당한다. 코드는 SBC/매출, SBC/영업현금흐름, 희석 세 가지를 모두 watch 신호로 표시했다. 보고 FCF는 FY2025에 29.2% 마진이지만 SBC를 차감하면 FCF는 2.5억 USD로 줄어든다. 경영진이 주주 몫을 말할 때 SBC 차감 후 수치를 기준으로 삼는지는 확인되지 않았다. [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [C:dilution]
- [dilution] 희석 주식 수 증가율은 FY2025에 1.3%로 FY2023의 11.1%보다 크게 둔화했지만, 코드의 최근 신호는 연 4.8%로 기준(3%)을 넘는다. 자사주 매입으로 희석을 상쇄한 근거는 수집되지 않아, 희석이 가려졌는지 상쇄됐는지 판단할 수 없다. [C:share_change@FY2025] [C:share_change@FY2023] [C:dilution]
- [capital_allocation] 영업권이 FY2025Q1 3.6억에서 FY2025Q2 5.3억으로, FY2026Q1 5.4억에서 FY2026Q2 7.1억으로 두 번 늘었다. 인수에 자본을 쓴 정황이다. 인수 대가와 이후 수익률은 근거에 없어 가치 창출 여부는 판단할 수 없다. [F79] [F80] [F83] [F84]
- [capital_allocation] 현금은 FY2024 12.5억에서 FY2025 4.0억으로 줄었다. 같은 기간 영업현금흐름은 10.5억으로 늘었다. 감소 원인(인수, 투자 증권 매입 등)은 현금 항목만으로는 알 수 없다. 자본화 소프트웨어는 FY2024 6,078만에서 FY2025 8,584만으로 늘어 재투자는 확대되는 중이다. 설비투자와 자본화 소프트웨어를 합치면 매출의 4~5%라고 경영진이 밝혔다. [F18] [F22] [F122] [F11] [F12] [S39](https://www.benzinga.com/node/62160028)

### 회계 품질 — watch

현금흐름과 이익의 방향이 일치하고 발생액이 음수라 숫자 자체를 믿을 수 없다는 증거는 없다. 영업현금흐름이 순이익을 크게 웃돌고 DSO는 줄었으며 재무제표 정정 신호도 없다. 다만 SBC가 매출의 21.9%이고 영업현금흐름의 71.5%라, 보고 FCF는 주주 희석을 비용으로 보지 않은 숫자다. 가치평가에서는 SBC 차감 FCF(C:fcf_after_sbc@FY2025)와 희석 주식 수 증가를 반영해서 봐야 한다. GAAP 영업이익은 거의 0이고 Non-GAAP 영업이익은 그보다 훨씬 큰데, 그 차이는 대부분 SBC다. 감사의견, Non-GAAP 조정 내역, 정정 여부는 수집되지 않아 확인하지 못했다. 이 부분은 미확인이지 문제로 확인된 것은 아니다. 그래서 판정은 clean이 아니라 watch다.

- [concern] sbc_to_revenue: SBC가 매출의 21.9%로 문턱 10%의 두 배 이상이다. FY2021 이후 15.9%에서 21~23% 구간에 고정돼 있어 일회성이 아니라 구조적 비용이다. GAAP 영업이익률이 FY2025 -1.3%로 거의 0인 이유가 이것이다. Non-GAAP 마진은 경제적 수익성을 과대 표시하므로 SBC를 비용으로 넣어 봐야 한다. [C:sbc_to_revenue@FY2025] [C:operating_margin@FY2025] [F179] [F129]
- [concern] sbc_to_ocf: SBC가 영업현금흐름의 71.5%다. FCF 마진 29.2%의 상당 부분이 주식으로 지급한 비용을 되돌려 놓은 결과다. SBC를 차감하면 FCF는 크게 줄어든다. 현금 창출은 실재하지만 주주에게 귀속되는 몫은 보고 FCF보다 작다. 역DCF와 P/FCF는 SBC 차감 FCF로도 같이 봐야 한다. [C:sbc_to_ocf@FY2025] [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [F121] [F122]
- [concern] dilution: 희석 주식 수가 연 4.8% 늘어 문턱 3%를 넘는다. 그 원인은 SBC 발행이다. 현금이 4.3억 달러뿐이라 자사주 매입으로 희석을 상쇄한 흔적도 없다. 회사의 FY2026 희석 주식 수 가이던스도 증가를 전제한다. 주당 가치는 이 희석을 반영해 계산해야 하며, 시가총액 기준 FCF 수익률만 보면 희석 비용을 놓친다. [C:dilution] [C:share_change@FY2025] [F216] [F217] [F64]
- [info] 순이익은 흑자이고 영업현금흐름은 순이익보다 훨씬 크다. 발생액 비율은 모든 연도에서 음수라 이익이 현금보다 앞서 인식된 흔적이 없다. ocf_negative 신호도 없다. 이익의 질은 현금 기준으로 양호하다. [C:accruals_ratio@FY2025] [C:fcf_conversion@FY2025] [F112] [F122]
- [info] DSO는 FY2021 95.4일에서 FY2025 78.9일로 줄었다. 매출채권이 분기 말에 계절적으로 늘어도 매출채권 괴리 신호는 없다. 이연매출은 매출과 함께 증가해 선수금 축소 신호도 없다. 청구액과 RPO 증가는 매출 인식을 앞서가는 계약 기반이 있다는 쪽과 일치한다. [C:dso@FY2025] [F154] [F164] [F54] [F225] [F226]
- [info] 자본화 소프트웨어는 FY2025 8,584만 달러로 매출의 몇 % 수준이다. 경영진은 설비투자와 자본화 소프트웨어를 매출의 4~5%로 언급했다. capitalized 신호는 발동하지 않았다. 다만 FY2026 1분기에는 3,417만 달러로 올랐다가 2분기에 2,728만 달러로 내려왔으므로, 이 비율이 계속 오르는지 다음 분기부터 확인할 가치가 있다. [F12] [F14] [F239] [C:capitalized_to_revenue@FY2025] [S39](https://www.benzinga.com/node/62160028)
- [info] 영업권이 FY2026 2분기에 5.4억 달러에서 7.1억 달러로 늘었다. 인수에서 나온 것으로 보인다. 총자산 대비 문턱 40%에 한참 못 미쳐 goodwill 신호는 없다. 인수 대상과 대가 구조는 10-Q 주석에서 확인되지 않았다. [F83] [F84] [F194] [C:goodwill_to_assets@FY2025]
- [watch] 감사의견(계속기업 의문·핵심감사사항), 감사인 변경, 재무제표 정정 여부, Non-GAAP 조정 내역, 특수관계자 거래는 수집되지 않았다. 코드의 restatement·auditor_change 신호는 발동하지 않았으나 이는 공시 목록 기준이며, 10-K 본문 감사보고서는 직접 대조하지 못했다. 이 항목의 증거 부재를 문제의 부재로 읽으면 안 된다. [S10](https://www.sec.gov/Archives/edgar/data/1561550/000162828026008819/ddog-20251231.htm)
- [watch] Non-GAAP 영업이익이 GAAP 영업이익보다 훨씬 크다. 2분기 GAAP 영업이익 546만 달러에 비해 Non-GAAP은 2.6억 달러다. 차이의 대부분은 분기 SBC 2.2억 달러로 설명되며, 반복되는 비용이라 조정 항목으로 보기 어렵다. Non-GAAP 마진을 근거로 한 논거는 SBC를 비용으로 되돌려 다시 계산해야 한다. [F134] [F184] [F223] [S2](https://www.sec.gov/Archives/edgar/data/1561550/000162828026053829/ddog-20260806.htm)
- [info] 사용량 기반 과금이라 매출이 고객 사용량에 직접 연동된다. 선도 AI 고객의 갱신에서 Q3부터 사용량이 줄어든다는 점은 회계 문제가 아니라 매출 집중도와 지속성 문제다. 규모가 공개되지 않아 회계적 영향은 평가할 수 없고, 이 위험은 사업·모델 모듈에서 다룬다. [S39](https://www.benzinga.com/node/62160028) [S23](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (30%) 멀티플 붕괴. 현재 P/FCF 77.6배(C:p_fcf)는 매출이 연 20%대 중반 이상으로 10년 가까이 커진다는 가정에 기댄다(C:implied_cagr@m25). 성장률이 한 단계만 꺾여도 시장은 성장주 배수를 거둔다. 8월 6일에는 매출 성장 36%의 호실적 발표 직후 주가가 16~18% 급락했다(S26, S35). 성장이 둔화하는 것만으로 가격이 내려간다는 선례다. FCF가 그대로 늘어도 배수가 크게 줄면 주가는 52주 저점(98.01달러, S40) 부근까지 내려갈 수 있다. [C:p_fcf] [C:implied_cagr@m25] [S26](https://news.google.com/rss/articles/CBMingFBVV95cUxOQmQ3VWJCU1ZoZXg2Y0ZHNHJBalpsT1VRRHFQaHlNTWZNRmlRR3dLY2ZVQ1FJbHFrWGdoVEt0dTVMSTlFZkh5T19oWEpGNUUyOUo1ckpIbEZxWkpyRlJQcFFpeDZ3SnlaNm5LM2pQOUpMd0JXZmVlQ1FZR3lIOWVaMkR5Vk1KSTZlenpLTUNUaGRSTHV2ZWFWQzRqSG1ndw?oc=5) [S35](https://news.google.com/rss/articles/CBMilwFBVV95cUxOdVIwdUZJczN6aGpaVzl5V19FZU5WZnpCVVo3aXVCNkJnNU0zcGI3Y19zd0F3MUlXMTAtOUhTemowaGEzajZybW5jR0IwTUJGaUZqWVk4OGE5Ri04czNvSGt6STBhaXRfX1VPY19sUFJNNElZcWtxTTZPMERWbWxsRWFia00yNGY2YzJqNE1mbjQxS2sxTk1J?oc=5) [S40](https://finance.yahoo.com/quote/DDOG/)
- (20%) AI 고객 집중도 위험이 전염된다. 선도 AI 기업의 9자리 금액 갱신에서 사용량이 줄기 시작했다(S39, S23). 사용량 기반 과금이라 고객이 워크로드를 줄이거나 자체 구축·다른 도구로 옮기면 매출이 곧바로 준다. AI 고객은 약 750곳이고 연 100만 달러 이상 31곳, 1,000만 달러 이상 8곳이다(F229, S39). 상위 소수 고객이 이 구간을 지탱한다면, 같은 갱신 협상이 다른 대형 AI 고객에서 되풀이될 때 성장이 한 번에 꺾인다. 회사는 감소 규모와 고객 비중을 공개하지 않았다. [S39](https://www.benzinga.com/node/62160028) [S23](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5) [F229]
- (15%) 원가 압박과 가격 경쟁. 비GAAP 총이익률이 80.2%에서 79.6%로 내려갔고(F232), 연간 총이익률도 FY2024 80.8%에서 FY2025 80.0%로 낮아졌다(C:gross_margin@FY2024, C:gross_margin@FY2025). 클라우드 3사, Dynatrace, Cisco(Splunk)는 관측 기능을 묶음 상품이나 자체 도구로 값싸게 제공할 수 있다(S25). 대형 고객이 갱신 때 할인을 요구하면 총이익률과 NRR이 함께 내려가고, 사용량이 늘어도 매출 단가가 떨어진다. 이 경우 FCF 마진이 시장이 가정하는 25% 이상을 지키지 못한다. [F232] [C:gross_margin@FY2024] [C:gross_margin@FY2025] [S25](https://news.google.com/rss/articles/CBMilwFBVV95cUxQaktWOHBrbE1lTjlQOHI4aHYwWDE3NHJWY2tLd0NuTkJEUDFXeUhhUXU2dENqZ1NQTzJzOERqTzJnelZwZ3VwNndya0dOZ0hCSzgzVXhLUU5hbDV1ekpVVnFRMThyTGJjZDFhcGVtZFY2SF9mRXl2ZlgxRHNwWngwRmgwTFJRZ0dGNk4zRzIzUEpWbjZ3TGVF?oc=5) [C:implied_cagr@m25]
- (10%) 주주 몫의 잠식. SBC가 매출의 21.9%이고 영업현금흐름의 71.5%라(C:sbc_to_revenue@FY2025, C:sbc_to_ocf@FY2025), 보고 FCF 수익률 1.3%(C:fcf_yield)는 SBC를 차감하면 더 작다(C:fcf_after_sbc@FY2025). 성장이 느려지면 우수 인력을 붙잡으려고 SBC를 줄이기 어렵고, 주가가 내려가면 같은 보상을 채우려 더 많은 주식을 발행한다. 희석 주식 수는 가이던스(F216, F217)대로 계속 늘고, 현금은 FY2026Q2에 4.3억 달러(F24)에 그쳐 자사주 매입으로 상쇄하기 어렵다. 인수에도 현금을 써서 영업권이 7.1억 달러(F84)로 늘었고 수익률은 검증되지 않았다. 주당 가치는 보고 FCF가 늘어도 정체된다. [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [C:fcf_yield] [C:fcf_after_sbc@FY2025] [F216] [F217] [F24] [F84]
- 약한 가정 `base.exit_multiple`: 기본 시나리오의 출구 P/FCF 32배는 현재 77.6배(C:p_fcf)에서 절반 아래로 내려온 값이지만, 성장이 연 16%까지 둔화한 5년 뒤 기업에 32배를 줄 이유가 없다. 코드가 계산한 기본 시나리오 수익률 분해에서 가장 큰 항목이 멀티플 변화(-20.9%)다. 이 가정이 틀리면 가장 큰 폭으로 틀린다. 기본 시나리오가 이미 손실이라는 점에서 방향은 보수적이지만, 크기가 가장 불확실하다. [C:p_fcf] [C:expected_irr] [C:p_loss]
- 약한 가정 `base.fcf_margin`: 27%는 최근 분기 FCF 마진 25%(S39)와 FY2025 29.2%(C:fcf_margin@FY2025)의 중간이다. 그러나 SBC를 차감하면 FY2025 FCF가 2.5억 달러로 줄고(C:fcf_after_sbc@FY2025), 총이익률이 내려가는 중이다(F232). 마진이 오를 근거(규모의 이익)와 내릴 근거(AI 인프라 원가·가격 경쟁·SBC)가 함께 있는데, 모델은 이를 하나의 값으로 묶었다. [S39](https://www.benzinga.com/node/62160028) [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [F232]
- 약한 가정 `base.revenue_growth`: 기본 시나리오 FY2026 성장 30%는 가이던스(F218)에 가깝지만, 이후 24%·21%로 완만하게 내려가는 경로는 AI 고객 사용량 감소(S39, S23)가 일시적이고 비AI 성장 20%대 후반(S39)이 이어진다는 가정이다. 비AI 성장 수치는 자동 전사본 기반의 대략적인 값이고 최대 고객의 비중은 공개되지 않았다. 기저율 표가 없어(계산 경고) 이 경로가 흔한지 코드로 확인되지 않았다. [F218] [S39](https://www.benzinga.com/node/62160028) [S23](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5)

## 검증 (L6)

주장 72개 — supported 49 · unsupported 23 · contradicted 0 · leap 0 · 미검증 0

- [unsupported] 슬레이터: 앤더슨은 상방 case를 10년으로 늘려도 주가의 3.59배라서 5배 문턱에 못 미친다고 본다. 나는 이 숫자가 사업의 질이 아니라 가격의 문제라는 점에 동의한다 — 없는 근거 인용: C:upside_10y@앤더슨
- [unsupported] 회계 품질: SBC가 매출의 21.9%로 문턱 10%의 두 배 이상이다. FY2021 이후 15.9%에서 21~23% 구간에 고정돼 있어 일회성이 아니라 구조적 비용이다. G — FY2025 SBC 21.9%와 영업이익률 -1.3%는 맞지만 'FY2021 15.9%에서 21~23% 구간 고정'이라는 과거 추이는 인용 자료에 없다.
- [unsupported] 애크먼: 가격이 모든 것을 말해 준다. P/FCF는 77.56배, FCF 수익률은 1.3%, EV/매출은 23.00배다. 보수적 가정의 내재가치보다 싸게 사라는 원칙과 정 — 없는 근거 인용: C:intrinsic_value@애크먼
- [unsupported] 회계 품질: 희석 주식 수가 연 4.8% 늘어 문턱 3%를 넘는다. 그 원인은 SBC 발행이다. 현금이 4.3억 달러뿐이라 자사주 매입으로 희석을 상쇄한 흔적도 없다. 회사의 — 희석 4.8%와 가이던스상 주식 수 증가는 맞지만 희석의 원인이 SBC 발행이라는 점과 자사주 매입 흔적이 없다는 점은 인용 자료에 없다.
- [unsupported] 사업·산업: 사용량 기반 과금이라 매출이 고객의 워크로드 변화에 민감하다. 이 때문에 NRR가 낮은 120%대(S39)로 높지만, 최대 고객 하나의 사용량 감소가 가이던스에  — NRR와 최대 고객 사용량 감소의 가이던스 반영은 맞지만 가이던스 범위 44.5억~44.7억 달러와 '올렸다'는 근거가 없다(인용은 4.46억 단일 값뿐).
- [unsupported] 모델러: 우리 기본 시나리오는 5년간 성장이 30%에서 16%로 둔화하고 FCF 마진이 27%로 낮아지는 경로다. 시장 가격은 이보다 성장이 훨씬 오래 높게 유지된다는 쪽 — '이 규모에서 10년 가까이 높은 성장을 유지한 기업은 드물다는 점은 기저율로 확인된다'고 했지만 인용된 기저율 자료가 없다.
- [unsupported] 앤더슨: 질문 6·7 — 규모가 커져도 단위경제가 무너지지 않았다. 매출이 FY2022 16.8억 달러에서 FY2025 34.3억 달러로 커지는 동안 총이익률은 80% 안 — FY2022 매출 16.8억 달러와 그 사이 총이익률 80% 안팎·FCF 마진 20%대 후반~30%대 초반 유지는 FY2025 값만으로 받쳐지지 않는다.
- [unsupported] 슬레이터: 애크먼은 사용량 과금과 AI 고객 갱신 때문에 단순성과 예측 가능성 기준을 못 채운다고 반대한다. 가격이 안전마진에 크게 못 미친다는 점은 인정한다. 그러나 오늘 — 없는 근거 인용: C:intrinsic_value@애크먼
- [unsupported] 사업·산업: 매출이 FY2022 16.8억 달러에서 FY2025 34.3억 달러로 커지는 동안 총이익률 80% 안팎과 FCF 마진 20%대 중후반을 유지했다. 규모가 늘어도  — FY2022 매출 16.8억과 FY2025 34.3억은 맞고 FY2026Q2 79.6%도 맞다. 그러나 성장 기간 동안 총이익률과 FCF 마진을 유지했다는 근거는 FY2025 값뿐이고 80.2%도 인용에 없다.
- [unsupported] 슬레이터: 단위경제는 입증됐다. 매출이 두 배로 커지는 동안 총이익률은 80% 안팎, FCF 마진은 20%대 후반~30% 안팎을 유지했다. 규모가 커져도 단위 원가가 악화되 — '매출이 두 배로 커지는 동안 총이익률·FCF 마진을 유지'했다는 주장은 FY2025 값만 인용했고 FY2022 시점의 마진은 없다.
- [unsupported] 앤더슨: 질문 10 — 5배가 되는 길이 보이지 않는다. 상방 case를 10년으로 늘려도 주당 가치는 주가의 3.59배다. 이 case는 이미 낙관적이다(5년 매출 연성 — 없는 근거 인용: C:base_rate@bull, C:revenue_cagr@강세, C:fcf_margin@강세, C:exit_multiple@강세
- [unsupported] 회계 품질: 순이익은 흑자이고 영업현금흐름은 순이익보다 훨씬 크다. 발생액 비율은 모든 연도에서 음수라 이익이 현금보다 앞서 인식된 흔적이 없다. ocf_negative 신호 — FY2025 발생액 비율 음수와 OCF가 순이익보다 큰 점은 맞다. 그러나 '모든 연도에서 음수'는 FY2025 값만으로는 확인되지 않는다.
- [unsupported] 사업·산업: 관측 시장은 Dynatrace, Cisco(Splunk), 클라우드 3사의 자체 도구와 경쟁한다. 경쟁사 마진·점유율 교차 확인은 수집하지 못해 경쟁 강도와 점유 — Dynatrace·Cisco(Splunk)·클라우드 3사와 경쟁한다는 내용은 인용된 S24, S25 제목에서 확인되지 않는다.
- [unsupported] 레드팀: 기본 시나리오의 출구 P/FCF 32배는 현재 77.6배(C:p_fcf)에서 절반 아래로 내려온 값이지만, 성장이 연 16%까지 둔화한 5년 뒤 기업에 32배를  — 현재 P/FCF 77.6배와 손실확률은 맞지만 멀티플 변화 -20.9%라는 수익률 분해 값은 인용에 없다.
- [unsupported] 애크먼: 레드팀의 약한 가정 중 가장 큰 것은 기본 시나리오 출구 P/FCF 32배다. 멀티플 변화가 연 수익률의 -20.9%를 차지하므로, 32배가 틀리면 가장 크게 틀 — 출처 없는 숫자 20.9% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 앤더슨: 사전 부검 — 멀티플 압축이 성장을 상쇄한다. 기본 시나리오에서 연 수익률 분해는 매출 성장 +19.6%에 멀티플 변화 -20.9%를 더해 총 -4.1%다. 사업 — 출처 없는 숫자 19.6%, 20.9%, 4.1% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 애크먼: 앤더슨은 성장 가설이 훼손되지 않았다는 이유로 반대 대신 기권을 택했다. 그러나 그의 상방 case가 10년 뒤 주가의 3.59배에 그치고 5배 문턱에 못 미친다 — 없는 근거 인용: C:upside_10y@앤더슨
- [unsupported] 회계 품질: DSO는 FY2021 95.4일에서 FY2025 78.9일로 줄었다. 매출채권이 분기 말에 계절적으로 늘어도 매출채권 괴리 신호는 없다. 이연매출은 매출과 함께  — FY2025 DSO 78.9일은 맞다. 그러나 FY2021 95.4일, 이연매출이 매출과 함께 늘었다는 추이, 신호 없음은 인용 자료에 없다.
- [unsupported] 사업·산업: FY2025 총이익률은 80.0%로 FY2024의 80.8%보다 0.8%p 낮아졌고, FY2026Q2 비GAAP 총이익률은 79.6%로 전 분기 80.2%보다 낮 — 출처 없는 숫자 0.8% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 사업·산업: 수만 개 고객의 텔레메트리와 통합(integration) 생태계가 제품 가치를 키운다는 주장이 있다. 하지만 이를 가격 결정력이나 점유율로 확인한 공시·시장 자료 — 인용한 S25, S30은 제목뿐이라 텔레메트리와 통합 생태계가 제품 가치를 키운다는 주장이 확인되지 않는다.
- [unsupported] 레드팀: 원가 압박과 가격 경쟁. 비GAAP 총이익률이 80.2%에서 79.6%로 내려갔고(F232), 연간 총이익률도 FY2024 80.8%에서 FY2025 80.0%로 — 총이익률 하락 수치는 맞지만 80.2%는 인용에 없다. 경쟁사가 값싸게 제공할 수 있다는 내용도 S25 제목에서 확인되지 않는다.
- [unsupported] 애크먼: 사전 부검: 시장이 SBC를 비용으로 보지 않고 높은 멀티플을 계속 부여한다면 내 안전마진 기준은 너무 엄격한 것이 된다. 기본 시나리오의 연 수익률 분해에서 멀 — 없는 근거 인용: C:return_decomp@base
- [unsupported] 사업·산업: 한 플랫폼에 여러 제품을 쓰는 고객이 늘수록 전환비용이 커진다. 그 흔적은 낮은 120%대 NRR과 90%대 중후반 총매출유지율, 그리고 ARR 10만 달러 이상 — 출처 없는 숫자 90% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| 매출 (revenue) | 10.3억 USD | 16.8억 USD | 21.3억 USD | 26.8억 USD | 34.3억 USD |
| 매출 성장 (revenue_growth) | — | 62.8% | 27.1% | 26.1% | 27.7% |
| 총이익률 (gross_margin) | 77.2% | 79.3% | 80.7% | 80.8% | 80.0% |
| 영업이익률 (operating_margin) | -1.9% | -3.5% | -1.6% | 2.0% | -1.3% |
| 순이익 (net_income) | -2,074만 USD | -5,016만 USD | 4,857만 USD | 1.8억 USD | 1.1억 USD |
| 영업현금흐름 (ocf) | 2.9억 USD | 4.2억 USD | 6.6억 USD | 8.7억 USD | 10.5억 USD |
| 설비투자 (capex) | 996만 USD | 3,526만 USD | 2,759만 USD | 3,472만 USD | 4,958만 USD |
| FCF (fcf) | 2.8억 USD | 3.8억 USD | 6.3억 USD | 8.4억 USD | 10.0억 USD |
| FCF 마진 (fcf_margin) | 26.9% | 22.9% | 29.7% | 31.1% | 29.2% |
| FCF/순이익 (fcf_conversion) | — | — | 13.02x | 4.55x | 9.29x |
| SBC (sbc) | 1.6억 USD | 3.6억 USD | 4.8억 USD | 5.7억 USD | 7.5억 USD |
| SBC/매출 (sbc_to_revenue) | 15.9% | 21.7% | 22.7% | 21.2% | 21.9% |
| SBC/영업현금흐름 (sbc_to_ocf) | 57.1% | 86.8% | 73.1% | 65.5% | 71.5% |
| SBC 차감 FCF (fcf_after_sbc) | 1.1억 USD | 1,999만 USD | 1.5억 USD | 2.7억 USD | 2.5억 USD |
| ROIC (roic) | -2.5% | -5.5% | -1.6% | 3.3% | -1.1% |
| 순현금 (net_cash) | 2.7억 USD | 3.4억 USD | 3.3억 USD | 12.5억 USD | 4.0억 USD |
| 순부채/EBITDA (net_debt_to_ebitda) | — | — | -154.65x | -12.13x | -83.14x |
| 희석 주식 수 (diluted_shares) | 3.1억 | 3.2억 | 3.5억 | 3.6억 | 3.6억 |
| 주식 수 변화 (share_change) | — | 2.1% | 11.1% | 2.4% | 1.3% |
| DSO(일) (dso) | 95.4 | 87.1 | 87.3 | 81.4 | 78.9 |
| 발생액 비율 (accruals_ratio) | — | -17.4% | -17.6% | -14.1% | -15.2% |

표에 없는 키도 인용할 수 있다: capitalized_software, capitalized_to_revenue, cash, cash_total, cost_of_revenue, d_and_a, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, goodwill, goodwill_to_assets, gross_profit, income_tax, interest_expense, operating_income, pretax_income, receivables, receivables_growth, rnd, total_assets

### 시장 · TTM(FY2026Q2) 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 247.11 USD/share (2026-10-16, F215) |
| 희석 주식 수 (shares) | 3.7억 |
| 시가총액 (market_cap) | 916.8억 USD |
| 순현금 (net_cash) | 4.3억 USD |
| EV (ev) | 912.5억 USD |
| FCF 수익률 (fcf_yield) | 1.3% |
| P/FCF (p_fcf) | 77.56x |
| EV/매출 (ev_revenue) | 23.00x |
| PER (pe) | 516.28x |
| 순부채/EBITDA (net_debt_to_ebitda) | -5.55x |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 21.9% > 10%
- [watch] sbc_to_ocf (C:sbc_to_ocf): SBC/영업현금흐름 — FCF의 상당 부분이 주식 보상 71.5% > 50%
- [watch] dilution (C:dilution): 희석 주식 수 연 4.8% 증가 > 3%

### 가이던스 적중 (C:guidance_hit_rate = 100%)

- revenue FY2026Q2: 가이던스 10.8억 → 실제 11.2억 = beat [F220, F164]

### 역DCF — 현재 가격이 가정하는 것

EV 912.5억 USD를 정당화하려면 매출이 10년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 목표 마진으로 직선 수렴, 할인율 10%, 이후 영구성장 3%.
기본 시나리오 목표 마진 27% 기준: 연 26.8% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 39.6% | C:implied_cagr@m10 |
| 15% | 34.3% | C:implied_cagr@m15 |
| 20% | 30.6% | C:implied_cagr@m20 |
| 25% | 27.7% | C:implied_cagr@m25 |
| 27% | 26.8% | C:implied_cagr@m27 |
| 30% | 25.4% | C:implied_cagr@m30 |

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 30% | 66.9억 USD | 14.3% | 22% | 20x | 79.63 | 49.44 | -20.3% |
| 기본 | 50% | 91.5억 USD | 21.7% | 27% | 32x | 201.60 | 125.18 | -4.0% |
| 강세 | 20% | 110.4억 USD | 26.3% | 31% | 45x | 385.68 | 239.48 | +9.3% |

확률 가중: 주당 가치 201.82 · IV 125.32 · 기대 연 수익률 -4.0% (C:expected_irr) · 손실 확률 80% (C:p_loss) · 현재 주가 247.11

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +19.6% · 마진 변화 -1.6% · 멀티플 변화 -20.9% · 주식 수 변화 -3.4% · 현금 축적 +2.2% = -4.1%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -13.0% | -8.6% | -4.9% |
| +0%p | -8.7% | -4.0% | -0.1% |
| +5%p | -4.4% | +0.6% | +4.8% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 44.6억 USD | 28.8% | 12.8억 USD | 3.8억 | 17.2억 USD |
| FY2027 | 55.2억 USD | 28.3% | 15.6억 USD | 4.0억 | 32.8억 USD |
| FY2028 | 66.8억 USD | 27.9% | 18.6억 USD | 4.1억 | 51.4억 USD |
| FY2029 | 78.9억 USD | 27.4% | 21.6억 USD | 4.3억 | 73.1억 USD |
| FY2030 | 91.5억 USD | 27.0% | 24.7억 USD | 4.4억 | 97.8억 USD |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 26.8% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 21.7% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 26.3% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=3.59x, revenue_5y=3.22x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=4.3억 USD
- 애크먼 case={"from": "base"}: price=247.1, fcf_positive=예, net_debt_to_ebitda=-5.55x, leveraged=아니오, intrinsic_value=125.2, mos=-97.4%

### 계산 경고

- 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-08-06 | [10-Q](https://www.sec.gov/Archives/edgar/data/1561550/000162828026054458/ddog-20260630.htm) |  |
| S2 | filing | 2026-08-06 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1561550/000162828026053829/ddog-20260806.htm) |  |
| S3 | filing | 2026-06-16 | [8-K](https://www.sec.gov/Archives/edgar/data/1561550/000162828026043590/ddog-20260615.htm) |  |
| S4 | filing | 2026-05-07 | [10-Q](https://www.sec.gov/Archives/edgar/data/1561550/000162828026032328/ddog-20260331.htm) |  |
| S5 | filing | 2026-05-07 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1561550/000162828026031677/ddog-20260507.htm) |  |
| S6 | filing | 2026-04-29 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1561550/000162828026028118/ddog-20260429.htm) |  |
| S7 | filing | 2026-04-22 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1561550/000119312526168261/d81305d8k.htm) |  |
| S8 | filing | 2026-03-02 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1561550/000162828026013236/ddog-20260226.htm) |  |
| S9 | filing | 2026-02-27 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1561550/000119312526079146/d700416ddef14a.htm) |  |
| S10 | filing | 2026-02-18 | [10-K](https://www.sec.gov/Archives/edgar/data/1561550/000162828026008819/ddog-20251231.htm) |  |
| S11 | filing | 2026-02-10 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1561550/000162828026006645/ddog-20260210.htm) |  |
| S12 | filing | 2025-11-07 | [10-Q](https://www.sec.gov/Archives/edgar/data/1561550/000156155025000313/ddog-20250930.htm) |  |
| S13 | filing | 2025-11-06 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1561550/000156155025000310/ddog-20251106.htm) |  |
| S14 | filing | 2024-02-23 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1561550/000156155024000009/0001561550-24-000009-index.htm) |  |
| S15 | filing | 2025-02-20 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1561550/000156155025000025/0001561550-25-000025-index.htm) |  |
| S16 | filing | 2025-05-07 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1561550/000156155025000123/0001561550-25-000123-index.htm) |  |
| S17 | filing | 2025-08-08 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1561550/000156155025000220/0001561550-25-000220-index.htm) |  |
| S18 | filing | 2023-02-24 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1561550/000156155023000006/0001561550-23-000006-index.htm) |  |
| S19 | news | 2026-09-03 | [Datadog, Amplitude, Zscaler, DocuSign, and Salesforce Shares Skyrocket, What You Need To Know - Yahoo Finance](https://news.google.com/rss/articles/CBMirwFBVV95cUxPUmQ1QVZrVmxDWDZtT0hTeWpUU0RZNUl1UklvQW9tNXZVVVVlYWs4SE1vdXRISlBsMHJxaXR3ZXVmaW93SUJrcGdRcDFNMmJvczNVb2I2NklNODR1M1p5RlU0azYwUTV6RndsS3R6V3c4dmExWGtyM3hzSF9ad1JjRXhrdExvbDNxdHR1TlNNQ0hEZWtzaUxDYTFjS1otWi1uYlluZDdnRE9iZ3pzbVhz?oc=5) | Yahoo Finance |
| S20 | news | 2026-08-27 | [French Tech Founders Reap $3 Billion Windfall From Datadog Stock - Bloomberg.com](https://news.google.com/rss/articles/CBMitAFBVV95cUxNd1lMVWdzblhuVjJqMFZXMVUyT1kyNENFc0xFNWxaZHBla2tXdFZ5TDlWUlVtRWNYamJORk8zbXhDYmd1cVpQWTNWaTlGV21Hb01ncWlRTmROTFdoQW1sbk5FYmxOUHNaV1FUbjFwUEdXQkhvaDBaLWxtYjQ2SFdUV2dIV1phX1psdXpzanJaMlRNN1RQaHQtUzF4MEV1TGRDOTRUeEx5SjhtN0RGaWc3MVM1QlM?oc=5) | Bloomberg.com |
| S21 | news | 2026-08-21 | [Should You Buy Datadog Stock Right Now? - The Motley Fool](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOZm00ZkVhN04zRldEM1NyenJkSy00NUhZUWExZmhMZnRQZEtZUE5JTEh0TFhja0hPQWE0SV9vZUtDYmU3dDZuNlBmeDNtR0YtbUVpX0ZsMXg0b1B5WlhEejhFeTRQb0hKRnp4LTUwdXNEWUloWUROODZmbGdsYnBuMzZDZ0NWc0dH?oc=5) | The Motley Fool |
| S22 | news | 2026-08-12 | [The Top 5 Analyst Questions From Datadog’s Q2 Earnings Call - StockStory](https://news.google.com/rss/articles/CBMivwFBVV95cUxQc1VtWU9ReXVHNzlqcUpRS2NaMXNCMTRTSF94bFBjdWNQMk1yemdFQk1yZ0RXNk45RnRlb2Q4RFJ6V1lqbjBkQll2SXlvcFhzQ2pBeG9WYWpUbWhoWjFoWVo2ZkRxM3NnZzFNMDBRcFkyUS1HUVotaEZsRWxUTTFHX1d3UjVaVXhjX2Q1aW9JVk01dGsxUWQzYm9nZ0VYYm9mTV96ZGRkWmV4TnJ4UmZmTjhCaHNPb2xPMWg5T1V4dw?oc=5) | StockStory |
| S23 | news | 2026-08-06 | [Datadog Says Lower Usage From Major AI Customer Could Dent Growth - WSJ](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQmxLdzhpdWNqd0JqREtldlcyTkU5WEtRZmtqQWtGVzRPSVBubEtjYU9CaTJLWlMyNC1wR0xjRXFVMkZRQ2hlaFBsOE1DUkNkVHE2b3pRQldfUl83cjNEalVvUV9SbTY5bnJxalNuU2NNUkxXU0Mxb2JJOHI4UFpZT09NUFJPc09nektsT1FCZjFWcTZDWW14NF9kNUk1b1JLRG5xR0Jray05TERYX09vX29B?oc=5) | WSJ |
| S24 | news | 2026-08-26 | [Palo Alto Networks CEO held acquisition talks with both Okta and Datadog - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxQNUJxV3VNWlVEX2NYUk9feUpoME1oNWxTQUxJdWxuNm9fU0laS0NSeUF3YXhFUUVacU5ySEFaQUxkZXVDRWlqYU9FaHZ0MWdSNmZDM092MGJaVUliUFdaczJLZEMtZmUzZGUzaWlkLUMxWDktcFkyLWc4d1lvR1VvMEkyU1dnR2xfc0lyVVM3TjJVc1NBLVE?oc=5) | Yahoo Finance |
| S25 | news | 2026-08-22 | [Datadog (DDOG) Rides The AI And Cloud Narrative, Is The Stock Fully Valued? - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxQaktWOHBrbE1lTjlQOHI4aHYwWDE3NHJWY2tLd0NuTkJEUDFXeUhhUXU2dENqZ1NQTzJzOERqTzJnelZwZ3VwNndya0dOZ0hCSzgzVXhLUU5hbDV1ekpVVnFRMThyTGJjZDFhcGVtZFY2SF9mRXl2ZlgxRHNwWngwRmgwTFJRZ0dGNk4zRzIzUEpWbjZ3TGVF?oc=5) | Yahoo Finance |
| S26 | news | 2026-08-06 | [Datadog Stock Tumbles 16% Despite 36% Revenue Growth - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxOQmQ3VWJCU1ZoZXg2Y0ZHNHJBalpsT1VRRHFQaHlNTWZNRmlRR3dLY2ZVQ1FJbHFrWGdoVEt0dTVMSTlFZkh5T19oWEpGNUUyOUo1ckpIbEZxWkpyRlJQcFFpeDZ3SnlaNm5LM2pQOUpMd0JXZmVlQ1FZR3lIOWVaMkR5Vk1KSTZlenpLTUNUaGRSTHV2ZWFWQzRqSG1ndw?oc=5) | Yahoo Finance |
| S27 | news | 2026-08-14 | [Jim Cramer Explains Datadog, Inc. (NASDAQ:DDOG)’s Share Price Movement - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxPYVJOb0w5blJobHppUmR6enNQQ3lHWkM1Q1pvemdwUlZpcmZtMnowdHdBN3FULVJrUlpXRnF4NFplV09GM0FWUDFsNXJ2LU5xZ1k4VE9uNHhsQUdMcXdpM1JzU1llVEp5QUwxeW5KNVpkRXVTREVnZGlDUmFUWk56VndZQ1lodUxoM2xoMTdzenJQY01ZLTdlY3J5c1A?oc=5) | Yahoo Finance |
| S28 | news | 2026-08-28 | [Datadog (DDOG) Stock Could Be 25% Undervalued After Product Adoption Growth - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxNLWhWNHZCTWdUM1hZMmZYRGptUlhCMzFKMWNhZ2MxeVhGdkU2MXU4RG44WUN4UUQySnFVbl9fTUFrX0FsNjlHVG9Hb29KNFhtVTNqeUl1a2RidTBseXA0bFU3azNJb0lZd2VFbEZvTE0tb2Qta3ZaeTNjSmtjRktyYVkybDdrRmhPY2kyMlBRQkpIMkpsc05v?oc=5) | Yahoo Finance |
| S29 | news | 2026-08-19 | [Rapid7, Tenable, CrowdStrike, Twilio, and Datadog Shares Plummet, What You Need To Know - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQN2ZXYVBZYnBRM2dqdm1VeFJZUm95UmkwaVZFVTRtbV94aVlmVEZCdG1BTGhHTTFtVXIzVWFEWVNtNm04Ukp5aGFiRjRUMEpKNHZ2N3hYY2RCU254b2xGNHl1U2lsel9PTVRIMWhjVFk5VEFrbmY5Y00xdnJZN1gwajRRaHpOUTBkNHBNbUJjWFBneUVqOHlsN3B0Z0xxNmhHM29GVk01UDVvdw?oc=5) | Yahoo Finance |
| S30 | news | 2026-08-13 | [Datadog's Large Customer Base Grows: Is Revenue Momentum Building? - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxNZGNDWU50NGpTRFAtTWFGdW80eFJZQmRRT0d3QkxIODU3cWlzSEdKWVdQVmZyU3NPYnpQQWNmUUg5NGQzMGVQS3hPSnBiNUFicFk3MW1UdDhLZ3otMlpOM05Xd0VSM1k1YkpZcm16bWxhc3E3MnlFT1VvVHZteEc5OXF1X3V2a2xMTmVnMlpPdXR4MmN2VTMtOFlhM2hFRVJ1eWpYaQ?oc=5) | Yahoo Finance |
| S31 | news | 2026-08-12 | [Brokers Suggest Investing in Datadog (DDOG): Read This Before Placing a Bet - Yahoo Finance](https://news.google.com/rss/articles/CBMipgFBVV95cUxQMlBBVEJYczVHNVhrSU1wMXcwUzA3N3VvYWh6OGJmZkRuakUxMmpCdl9ydHBwblRJUjFLdjNFcFVLS281alNOYi1vcHJTTWdBVWhqcGFQWi05bGVVVURReWd3YWlFbE9sU3h2cmF3dDNwVmZqRFRyRDVyTG8tOXlpaUlNLVBYN2doSE9reXBMSXpFX0p2NmJzdjFJNUhWRjA3dU9oZWNn?oc=5) | Yahoo Finance |
| S32 | news | 2026-08-07 | [Datadog Q2 Earnings and Revenues Surpass Estimates, Rise Y/Y - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxQUjEtMHFCdklhRXdQa2hkc0dCbFYtRzFjbVhsekxIUUpGcmJSZW84ZWJJTG9PVHQ1RzNQam5SaDFKTmpqbV9FVk5Id0NOQ0VSTzJHR0V6anlRSHpKRXRISF9obUV6bEZtUGFIQ1o0Ulk5djNZczlaQkRUOE8zZW5zTy02aTIyWmZSVXpELVlZNDlSSlNLSUNSR2swbHN3YWhPNTJ3?oc=5) | Yahoo Finance |
| S33 | news | 2026-08-10 | [Evaluating Datadog’s Reincorporation Proposal and Governance Roadmap - Yahoo Finance](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQd0p5aGx4eXctXzl5SUdySlJMWkU0dXRMT0dtcWE4WTloRW9PZm5GeXhoMzFvUWNtM09GbHV3ajZvR1cwdVJRbjlvZERVOHNJWHNBbDd3OW9DWWJVNWoyb2ZvNmM4VEF1RUZSODNfd3hEOGRoMS1JZkJTWWx6aFdBODVtU0tnZW1ZQVpvNmpkaTVHRzFMNHplVzczX3JuMFlYeG1BUEV5NHdQLWRHV3dBTVhKRnRIN1ByNTE4?oc=5) | Yahoo Finance |
| S34 | news | 2026-08-13 | [Does Datadog (DDOG) Still Trade Below Fair Value After The Drop? - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxQTTdqUDk5NHBrTGQ2VElrdGNLSURYMjNUYU1xYlNqa2p4YzRoaXYyc29ZUmQ3OXVoTHJhZUtsZFB4ajhZclpzZGQwVTlvT1pCSjVGVTdmN1Z5SkpzaF9RX2MxQzl1SGJVZXd4amtFT2pVdmpZdGZQSXcyamNQRmcyaTNKa3lwclJBQk93NnBUTjdvNW9ST2xOakpR?oc=5) | Yahoo Finance |
| S35 | news | 2026-08-06 | [Datadog Stock Falls 18% After a Beat-and-Raise Quarter - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxOdVIwdUZJczN6aGpaVzl5V19FZU5WZnpCVVo3aXVCNkJnNU0zcGI3Y19zd0F3MUlXMTAtOUhTemowaGEzajZybW5jR0IwTUJGaUZqWVk4OGE5Ri04czNvSGt6STBhaXRfX1VPY19sUFJNNElZcWtxTTZPMERWbWxsRWFia00yNGY2YzJqNE1mbjQxS2sxTk1J?oc=5) | Yahoo Finance |
| S36 | news | 2026-08-06 | [Software stocks sink, led by declines from Figma, Datadog - Yahoo Finance](https://news.google.com/rss/articles/CBMisgFBVV95cUxOaDFDa19mdDVaM1UtYzYxUWROS2dkSWhBMzd4dk5rSjZoQklVc0EyOS1qaU1OSEIyck5uY1dkVGVpX0k2Sm5Va0hnR0gzRGdrTHpPTGJrZWFQQzJsS2Y5RjRWT1BGYnJCWmVHR2xOeW1FQmV5ZXJJeG5jVDdyTURYS2MwMEZydzIwMlR3REdqUERqWEVRSmlIWXN3MnZKNFZiM0hHcDZhb25LY0dqZXRpTWt3?oc=5) | Yahoo Finance |
| S37 | news | 2026-08-10 | [Datadog (DDOG) Grows Fast, Then Gets Punished For Slowing Down - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxOSWExRE44bDRYLVJRWWd0ZlM0UnJuX3hnLUdhYXNWdG1kNEdiV0xRLTdzekR1RF9rY3RucmdpTVdFVURDOTc1N2R0M0JEUGRtbXplNUhORnpfZzJYcVVSdmpnQ09BN05RdzQtcWlROHVDRE9Pa1dWMGQxQWp1eG1uZXNmaVQ5Qjl5YVkyZ0tIRVpjZjJrenFwVA?oc=5) | Yahoo Finance |
| S38 | news | 2026-09-03 | [Datadog Shares Rise Following Snowflake Quarterly Results - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxOTkpqejVWTHJzekRLMTlLSXFyRW5PSmVpYi1DeUJkX05xSnNyU0psc2JhNVBvSlRVa080eTJGRENkSWRyX2hEWW5ZVmxfQTRYMno3MGFCeEJqVW4zelRqeTg2NnhYQ29tOUlaOTBuY3E1Yk9RQzVqVlU3d3BMXzRxbHNJeWxUN3p0TFhfR1k5bW15clQ0OExJMFFXeUhOeVAtTXE0elI2bw?oc=5) | Yahoo Finance |
| S39 | call | 2026-08-06 | [Full Transcript: Datadog Q2 2026 Earnings Call](https://www.benzinga.com/node/62160028) | 자동 전사본(오류 가능, 앞 10만 자만 확인). 최근 12개월 NRR는 'low 120s'(전 분기와 비슷), 총매출유지율 'mid to high 90s'. 고객 약 33,400곳(전년 약 31,400), ARR 10만 달러 이상 고객 약 4,720곳(전년 약 3,850)이고 이들이 ARR의 약 91%. AI 고객 약 750곳, 연 100만 달러 이상 31곳, 1,000만 달러 이상 8곳. 선도 AI 기업과의 '9자리 금액 갱신'에서 사용량이 Q3부터 줄어들며 가이던스에 반영, 규모는 공개하지 않음. 비AI 고객 매출 성장은 20%대 후반으로 가속. 매출총이익률 79.6%(전 분기 80.2%). FCF 2.79억 달러(마진 25%), RPO 34.7억 달러(+43%), 청구액 11.8억 달러(+38%). 설비투자와 자본화 소프트웨어는 매출의 4~5%. 2027 언급 없음. |
| S40 | data | 2026-10-16 | [Datadog, Inc. (DDOG) Stock Price, News, Quote & History - Yahoo Finance](https://finance.yahoo.com/quote/DDOG/) | 2026-10-16 종가 247.11달러(-7.19%), 직전 종가 266.25달러. 10월 9일 종가 293.26달러로 사상 최고 종가(보도). 52주 범위 약 98.01~300.68달러(Robinhood 스냅샷). 검색 결과 요약으로 확인했고 직접 조회하지는 못함. |
| S41 | news | 2026-10-09 | [Datadog (NASDAQ:DDOG) Reaches New 12-Month High - MarketBeat](https://www.marketbeat.com/instant-alerts/price-datadog-nasdaq-ddog-reaches-new-12-month-high-heres-what-happened-2026-10-09/) | 보도. 10월 9일 52주 신고가. 10월 15일 Mizuho가 목표가를 300달러에서 330달러로 올리고 Outperform 유지(검색 요약 기준). 8월 6일 Q2 발표 후 주가는 16~18% 급락했다가(S26·S35) 10월 초 신고가까지 회복. |
| S42 | data | 2026-10-16 | [Yahoo Finance DDOG historical prices](https://finance.yahoo.com/quote/DDOG/history/) | 2026-10-16 종가 247.11 USD |
| S43 | news | 2026-08-06 | [Why is Datadog stock down 18% despite a Q2 earnings beat and guidance raise? - TradingView](https://news.google.com/rss/articles/CBMiywFBVV95cUxPQTBOWktSWmJUcVJZN3lLMEdUajl3RVlLa2F3cHdFTjZFYVdzaEhjZm51eWF0MUltT3pQdjFxS0d1RkU1b0E5aGlRMDhER3pZV0RZZ29sMG82bldLVXJIOU02T2xDOEMxdHVJMTFBaTdHNXprNlh3UmhBS3hrTS1hNUpWRW5hRG11N3ZQZE0xUFN6VUx1WjdSa2d3VlB1VHpRZDRrcEowY2FucXoyVXp0RUxhZmMyRmlWckVGLXY2RHdVclVLb1N5RkpRTQ?oc=5) | TradingView |

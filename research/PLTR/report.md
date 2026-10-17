# Palantir Technologies (PLTR) 리서치 보고서 — 기준일 2026-10-18

**반대 우세** — 찬성 0 · 반대 1 · 보류 2 · 확신 가중 점수 -0.20 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장이 반영한 것: 주가 208.67달러(F212)에서 EV/매출 85.54배(C:ev_revenue), PER 177.68배(C:pe)다. 이 가격은 지금의 초고성장이 여러 해 이어지고 마진도 유지된다는 가정을 이미 담고 있다. 시장 내재 성장은 C:implied_cagr@m20·@m30 같은 역DCF 키가 보여 주며, 기본 시나리오의 마진에 해당하는 값이 C:implied_cagr다. 컨센서스는 확보하지 못해 모델과의 직접 비교는 불가능하다.
- 우리가 다르게 보는 점: 근거로 확인되는 것은 성장 가속 자체(F149→F152, F150→F153)이고 이를 높게 반영한다. 다만 가격이 그 성장의 지속 기간까지 이미 선반영한 것으로 본다. 기본 시나리오의 주당 가치는 현재 주가와 비교해 코드가 계산하며, 매출 성장이 5년 이상 높게 유지되어야만 가격이 정당화된다. 우리 견해는 '성장은 진짜지만 가격이 요구하는 지속 기간이 불확실하다'는 것이고, 그래서 약세 확률을 0.30으로 높게 둔다.
- 왜 우리가 맞는가: 성장 지속의 핵심 근거인 NRR·계약 잔액·미국 상업 매출은 수집되지 않았다(리서처 미확인). 그런 상태에서 지금 매출 성장률을 먼 미래까지 연장하는 것은 서사 과적합이다. 반면 이연매출(F49, F51)과 영업이익률 개선(C:operating_margin@FY2025)은 수요가 실재함을 뒷받침하므로 단기 경로는 높게 잡는다. [F212] [C:ev_revenue] [C:pe] [C:implied_cagr] [F149] [F152] [F150] [F153] [F49] [F51] [C:operating_margin@FY2025]
- 촉매: 분기 실적에서 매출 성장률의 감속 속도와 이연매출·매출채권 추이(DSO)가 드러난다. 8-K 실적 발표(S2류)의 가이던스와 NRR·계약 잔액 공개도 계기가 된다.
- 시점: FY2026Q3 실적 발표(2026년 11월 초)부터 이후 4개 분기

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **99.61** vs 주가 208.67 · 기대 연 수익률 **-5.1%** · 손실 확률 75%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 30% | 39.58 | 24.58 | -28.3% | 추정: 올해 상반기의 급가속은 정부·대기업의 일회성 대형 도입이 몰린 결과이고, 그 뒤 신규 계약이 소화 국면으로 들어가 성장률이 빠르게 꺾인다. 매출채권이 매출보다 빨리 늘고 DSO가 길어진 점(C:dso@FY20 |
| 기본 | 45% | 156.42 | 97.12 | -5.6% | 올해 1·2분기 매출이 전년 동기 대비 크게 늘었다(F149→F152, F150→F153). 이연매출도 FY2025 말에서 FY2026Q2까지 늘었다(F49, F51). 그래서 FY2026은 이미 높은 성장이 확정에 |
| 강세 | 25% | 312.65 | 194.13 | +8.4% | AIP 도입이 상업 부문 전반으로 번지고, 육군 TITAN 같은 국방 조달(S31)과 PwC·Nebius 채널(S28, S26)이 신규 물량으로 이어진다. 그 결과 성장이 40% 안팎의 높은 수준으로 더 오래 간다. |

## 3. 반증 조건 (thesis break)

- [자료 없음] 앤더슨: FY2026Q3 분기 매출이 직전 분기 19.4억 달러보다 줄면 성장 가설 훼손 — `revenue < 1.94e+09` (FY2026Q3)
- [자료 없음] 앤더슨: 이연매출이 직전 분기 수준 아래로 줄면 선결제 수요 가설 훼손 — `deferred_revenue < 5.8e+08` (FY2026Q3)
- [수동 확인] 앤더슨: NRR·계약 잔액 공개 시 성장 지속을 뒷받침하는지 수동 확인
- [자료 없음] 슬레이터: 이연매출이 이 수준을 넘으면 선결제 수요가 모델 기본 경로보다 강하다는 증거이므로 비중 0 판단을 재검토한다 — `deferred_revenue > 8e+08` (FY2026Q3)
- [자료 없음] 슬레이터: 분기 매출이 모델 기본 경로를 크게 웃돌면 가격이 요구하는 지속 기간에 대한 판단을 다시 한다 — `revenue > 2.5e+09` (FY2026Q3)
- [수동 확인] 슬레이터: 10-Q나 실적 발표에서 NRR·계약 잔액이 공개되어 단위경제가 입증되면 수동 확인 후 재평가
- [미충족] 애크먼: 주가 100달러 미만 — 기본 시나리오 현재가치(97.1달러) 수준으로 내려오면 재검토 — `price < 100`
- [자료 없음] 애크먼: FY2026Q3 매출 20억 달러 미만 — 성장 감속으로 기본 시나리오 훼손 — `revenue < 2e+09` (FY2026Q3)
- [수동 확인] 애크먼: 자본 환원 정책 발표 시 수동 확인
- [충족 — 훼손] 레드팀: FY2026Q3 분기 매출이 모델러 KPI 하한 22억 미만 — 순차 성장이 꺾이는 신호 — `revenue < 2.2e+09`
- [미충족] 레드팀: FY2026Q3 매출채권이 17억 초과 — 회수 지연이 매출보다 빨리 늘어나는 신호 — `receivables > 1.7e+09`
- [충족 — 훼손] 레드팀: 이연매출이 FY2026Q2의 5.8억 아래로 감소 — 선결제 수요 둔화 — `deferred_revenue < 5.8e+08`
- [미충족] 레드팀: 분기 매출원가가 FY2026Q2의 3.0억을 넘어 계속 증가 — 총이익률 하락 위험 — `cost_of_revenue > 3e+08`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | revenue | FY2026Q3 | >= 2.2e+09 | 60% | 분기 매출이 직전 분기 19.4억(F153)에서 최근처럼 두 자릿수 순차 성장을 이어가는지 본다. 기본 시나리오의 첫해 78% 성장 가정을 시험한다. |
| K2 | revenue | FY2026 | >= 8e+09 | 70% | 연간 매출이 80억을 넘으면 기본 시나리오의 첫해 성장률 가정이 맞다. 약세 시나리오(첫해 65%)와 구분되는 지점이다. |
| K3 | operating_income | FY2026Q3 | >= 1e+09 | 65% | 영업이익이 직전 분기 9.1억(F123)보다 늘어 고정비 레버리지가 이어지는지 본다. FCF 마진 50% 가정의 전제다. |
| K4 | deferred_revenue | FY2026Q3 | >= 6e+08 | 60% | 이연매출이 FY2026Q2의 5.8억(F51)에서 계속 늘면 선결제 수요와 전환비용 가설이 유지된다. 줄면 약세 시나리오 쪽 신호다. |
| K5 | receivables | FY2026Q3 | <= 1.7e+09 | 55% | 매출채권이 FY2026Q2의 14.9억(F143)에서 매출 증가보다 빠르게 늘지 않는지 본다. 회수 지연 우려(C:receivables_gap)를 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.20 · 비중 참고값 0.0% (반대 우세 — 신규 비중 없음) · 슬레이터 시작 비중 0.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 보류 → 보류 | 3/5 | ✗ 10년 주당가치 5배 미만 또는 계산 불가 (LTGG Q10) | 2/5 실패 | founder_led=예, upside_10y=4.55x, revenue_5y=6.73x |
| 슬레이터 | 반대 → 반대 | 3/5 | ✓ | 0/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=0.0%, cash_survives=예, cash_min=94.1억 USD |
| 애크먼 | 반대 → 보류 (검증 실패 → 보류) | 4/5 | ✗ 단순·예측 가능한 사업이 아님; 잉여현금흐름을 만들지 못함 (코드 계산); 안전마진 20% 미만 또는 계산 불가 | 3/5 실패 | simple_predictable=아니오, capital_markets_dependent=아니오, catalyst=없음, intrinsic_value=97.1, mos=-114.9% |

- ⚠ 앤더슨: rebuttals[0] unsupported: 없는 근거 인용: C:mos@애크먼
- ⚠ 앤더슨: arguments[3] unsupported: 상방 10년 가치가 5배 문턱에 못 미친다는 핵심 주장의 계산값은 인용되지 않았다. EV/매출 85.5배와 주가만 인용값과 일치한다.
- ⚠ 앤더슨: arguments[4] unsupported: 없는 근거 인용: C:implied_cagr
- ⚠ 애크먼: risks[1] unsupported: 출처 없는 숫자 36.7% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: arguments[2] unsupported: 출처 없는 숫자 30.4%, 36.7%, 3.1% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: arguments[0] unsupported: 없는 근거 인용: C:mos@애크먼
- ⚠ 애크먼: rebuttals[2] unsupported: 없는 근거 인용: C:mos@애크먼
- ⚠ 애크먼: arguments[4] unsupported: 출처 없는 숫자 3% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: risks[1]: 인용하지 않은 근거의 숫자 50(C:exit_multiple@bull) — cites에 추가
- ⚠ 애크먼: arguments[2]: 인용하지 않은 근거의 숫자 35.6%(C:revenue_cagr@base), 40(C:exit_multiple@base·C:value@bear) — cites에 추가
- ⚠ 애크먼: risks[0]: 인용하지 않은 근거의 숫자 50(C:exit_multiple@bull) — cites에 추가
- ⚠ 애크먼: rebuttals[1]: 인용하지 않은 근거의 숫자 10%(C:discount_rate·C:fcf_margin@FY2022) — cites에 추가
- ⚠ 애크먼: rebuttals[0]: 인용하지 않은 근거의 숫자 4.55(C:upside_10y@anderson), 35.6%(C:revenue_cagr@base) — cites에 추가
- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 사업·산업 findings[6]: 인용하지 않은 근거의 숫자 1.92e+09(C:diluted_shares@FY2021·F52) — cites에 추가
- ⚠ 사업·산업 moat[0]: 인용하지 않은 근거의 숫자 26.7%(C:operating_margin@FY2021) — cites에 추가
- ⚠ 사업·산업 findings[1]: 인용하지 않은 근거의 숫자 10%(C:discount_rate·C:fcf_margin@FY2022) — cites에 추가
- ⚠ 레드팀 premortem[0] 검증 실패(unsupported): 출처 없는 숫자 36.7% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[0]: 인용하지 않은 근거의 숫자 78.6%(C:gross_margin@FY2022), 80.6%(C:gross_margin@FY2023·C:gross_margin@FY2024), 80.2%(C:gross_margin@FY2024) — cites에 추가
- ⚠ 레드팀 premortem[2] 검증 실패(unsupported): 출처 없는 숫자 1.4% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 회계 품질 findings[1] 검증 실패(unsupported): 출처 없는 숫자 1.4% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 레드팀 weakest[0] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base
- ⚠ 회계 품질 flags[0]: 인용하지 않은 근거의 숫자 29.6%(C:sbc_to_revenue@FY2022), 21.4%(C:sbc_to_revenue@FY2023), 24.1%(C:sbc_to_revenue@FY2024), 233.1%(C:sbc_to_ocf@FY2021), 46.9%(C:fcf_margin@FY2025) — cites에 추가
- ⚠ 회계 품질 flags[2]: 인용하지 않은 근거의 숫자 11.3%(C:share_change@FY2023), 6.7%(C:accruals_ratio@FY2025·C:share_change@FY2024) — cites에 추가
- ⚠ 모델러 variant 검증 실패(unsupported): 없는 근거 인용: C:implied_cagr
- ⚠ 경영진·자본배분 findings[4]: 인용하지 않은 근거의 숫자 10%(C:discount_rate·C:fcf_margin@FY2022) — cites에 추가
- ⚠ 경영진·자본배분 findings[3] 검증 실패(unsupported): 출처 없는 숫자 3% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[2] 검증 실패(unsupported): 출처 없는 숫자 3.32, 1.29 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base

## 앤더슨 — 보류 (3/5)

> 성장은 진짜다. 매출 성장이 가속하고 영업 레버리지와 FCF가 함께 확인되어, 5년 안에 매출이 두 배가 되는지(1번 질문)는 상방 시나리오에서 여유 있게 통과한다. 문제는 10번 질문이다. 상방 시나리오를 10년으로 늘려도 코드가 계산한 10년 뒤 주당 가치는 현재 주가의 5배에 못 미친다. 가격이 이미 상방의 상당 부분을 선반영했다는 뜻이다. 기저율 표와 컨센서스가 없어 시장이 무엇을 과소평가하는지(9번 질문)도 답하지 못한다. NRR, 계약 잔액, 미국 상업 매출 같은 확장 근거도 비어 있다. 아웃라이어일 가능성은 인정하지만 5배 길이 보이지 않는 가격에서는 찬성할 수 없다. 반대할 만큼 성장 가설이 훼손된 것도 아니므로 보류한다.

**논거**
- 매출 성장률이 FY2024 28.8%에서 FY2025 56.2%로 가속했다. 규모가 커지는데 성장이 빨라지는 것은 멱법칙 기업의 전형적 신호이며, 1번 질문(5년 내 매출 2배)의 근거다. [C:revenue_growth@FY2024] [C:revenue_growth@FY2025]
- 영업이익률이 FY2021 -26.7%에서 FY2025 31.6%로 올랐고 FCF 마진은 46.9%다. 이익률 상승 여지(6번)와 이익의 현금화(7번)가 이미 숫자로 확인된다. [C:operating_margin@FY2021] [C:operating_margin@FY2025] [C:fcf_margin@FY2025]
- FY2026Q2 분기 매출 19.4억 달러는 전년 같은 분기 10.0억 달러의 두 배에 가깝고, 이연매출도 늘고 있다. 단기 수요는 실재한다. [F153] [F150] [F51]
- EV/매출이 85.54배다. 이 가격은 상방 시나리오가 10년 동안 이어져도 5배 수익을 허락하지 않는다. 코드 계산상 상방 10년 가치가 5배 문턱에 못 미치므로 10번 질문에 '그렇다'고 답할 수 없다. [C:ev_revenue] [F212]
- 컨센서스와 기저율 표가 모두 없다. 시장이 이 기회를 왜 과소평가하는지(9번 질문)를 코드로 확인할 수 없다. 드문 일에 거는 것은 내 철학이지만, 검증 없이 크게 담을 이유는 되지 못한다. [C:implied_cagr] [S33](https://news.google.com/rss/articles/CBMingJBVV95cUxOZGo5YTdTM011UXg0UGxfR3N1VGtjQl9TTFdTYTZnb1dhVFY0RVhBVGxoeW1ZVXpGTkdpM25FYXcwSTZ6aDFqZXQxRm5rdVNkeHBMTmtxLXZGN3hEbGFyenR2Z1NEekQxR2NWSEpvUjdjb0JtckZldHd5UjdNTnJoQUtCV2dTSTZ0aUROSFVsWUJqLUdGdnNwWGxzb3hBSTJuREswZFFwM2t2dkJQdkRNZW9GNldVQzIxYXhWT0d6ZDNiTE1WVnFTY1BsaFNQVXQ0WkpRMmtjRmxXeWhMUVZNRjFKWms3VjE3aUUzVk5iajBEQ3lLVnpPTFFxNzF2M2xuTXREOHR2ajYtQTFsSFVOS1RVWXliT05UckJ0clFn?oc=5)

**사전 부검**
- 사전 부검: 성장이 둔화되면서 지금의 높은 배수가 무너진다. 확률 가중 기대 연 수익률이 음수로 계산되므로 이 경로가 주된 실패 방식이다. 이는 성장 가설이 아니라 가격의 문제다. [C:expected_irr] [C:ev_revenue]
- 사전 부검: 매출채권이 매출보다 빨리 늘어 DSO가 45.2일에서 85.0일로 길어졌다. 회수 지연이거나 계약 조건 악화라면 현금화(7번)가 약해지고 FCF 마진 가정이 깨진다. [C:dso@FY2021] [C:dso@FY2025] [C:receivables_gap]
- 사전 부검: SBC가 매출의 15.3%이고 희석 주식 수가 연 4.7% 늘었다. 자사주 매입이 이를 상쇄하지 못해 주당 가치가 매출 성장만큼 오르지 않는다. [C:sbc_to_revenue@FY2025] [C:share_change@FY2025] [F5]

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 기본 시나리오 수익률 분해에서 매출 성장 +30.4%를 멀티플 축소 -36.7%가 삼킨다는 점이다. 그러나 그 분해는 기본 시나리오(5년, 출구 40배)에 묶여 있다. 내가 묻는 것은 10년 뒤 크기이고, 상방 10년 경로의 코드 계산값은 5배에 가까이 간다(upside_10y 4.55). DCF가 현재를 정밀하게 재는 도구라는 점은 변하지 않는다. 다만 그의 안전마진 -114.9%는 기본 시나리오만 본 값이어서, 성장이 가속하는 기업의 우측 꼬리를 재지 못한다. 그래도 강세 시나리오의 5년 연 수익률이 +8.4%에 그치는 것은 내게도 불편한 숫자다. [C:irr@bull] [C:mos@애크먼] [C:expected_irr]
- → 슬레이터: 슬레이터의 가장 강한 논거는 NRR·계약 잔액·고객 수가 입증되지 않았다는 것이다. 그러나 이연매출이 FY2025 4.1억에서 FY2026Q2 5.8억으로 늘고 분기 매출이 전년 동기의 두 배에 가까운 것은 수요의 증거다. 증거를 기다리다 가장 가치 있는 구간을 놓치는 것이 내가 경계하는 실수다. 그래서 시작 비중 0이라는 결론에는 동의하지 않지만, 가격이 요구하는 지속 기간을 입증할 KPI가 비어 있어 찬성까지 가지 못한다는 점은 인정한다. [F51] [F49] [F153] [F150]
- → 레드팀: 레드팀의 첫 사전 부검은 성장 감속과 멀티플 붕괴가 겹치는 경로이고 이것이 가장 강하다. 이 경로는 성장 가설 자체를 깨는 것이 아니다. 실적이 나쁘지 않아도 배수만 내려오는 가격의 문제다. 반면 매출채권과 DSO 경로는 현금화(7번 질문)를 건드리지만, 이연매출 증가가 이를 일부 상쇄하므로 경로의 소음일 가능성이 더 크다. 정부 의존과 규제 경로도 성장 가설을 건드릴 수 있어 NRR과 계약 잔액이 공개되기 전에는 과소평가하지 않는다. [C:ev_revenue] [C:revenue_growth@FY2025] [C:dso@FY2025] [F51] [S27](https://news.google.com/rss/articles/CBMingFBVV95cUxOSXRiUnZMQ0xiTjE0dktzakxGYVpJeWtNMC1ZQ2pXd1JRU0Q0c0JtNzZqS3RoOUFYQ21LVzlUY3dyUS13cjJXTGpiOTZ1YmRHWm52XzdxLUdsMXVTSUlobzYybGkwVzBhWk55TjZoLUlkTFB2TEFSbDYwd1Z1OVJZVDBJRmlPTlh4U0hsZ0VVWWtBaDJidW1PX3dOYUl5UQ?oc=5)

**인정한 점**
- 애크먼과 레드팀이 옳은 점: 성장이 진짜여도 이 가격에서는 상방 10년 경로조차 5배 문턱에 못 미치므로(upside_10y 4.55) 10번 질문에 '그렇다'고 답하지 못한다. 찬성하지 않는 이유는 성장 가설이 아니라 가격이다.
- 슬레이터가 옳은 점: 컨센서스·기저율·NRR·계약 잔액이 비어 있어 9번 질문(시장이 왜 과소평가하는가)에 답할 수 없다. 검증되지 않은 상태에서 크게 담지 않는다.
- 성장 가설이 훼손되지 않았으므로 반대로 돌아서지는 않는다. 입장은 보류, 확신은 3을 유지한다.


## 슬레이터 — 반대 (3/5)

> 사업의 증거는 강하다. 성장은 가속했고 영업이익률은 올랐으며 현금은 쌓이고 있다. 자체 현금으로 계획을 실행할 수 있어 생존과 외부 조달 문제는 없다. 그런데 이 하네스의 기본 시나리오에서도 주가 208.67달러는 연 수익률이 마이너스이고, 확률 가중 기대 연 수익률도 마이너스이며 손실 확률이 높다. 고객 단위의 단위경제(NRR, 계약 잔액, 고객 수)는 아직 입증되지 않았다. 나는 증거가 쌓이는 만큼 비중을 키우는 사람이다. 지금은 증거가 가격이 요구하는 지속 기간을 따라가지 못한다. 그래서 담지 않고, 가설이 입증되는 신호를 기다린다. 사업이 나쁘다는 판단이 아니라, 지금 가격에서는 증거 수준에 맞는 시작 비중이 사실상 0에 가깝다는 판단이다.

**논거**
- 크기와 현금 창출은 증거로 확인된다. 매출 성장률은 FY2025에 가속했고, FCF 마진도 올랐다. 외부 자본에 기대지 않고 성장을 자체 현금으로 감당한다. 2022년의 교훈인 자본집약·외부 조달 위험은 여기에 해당하지 않는다. [C:revenue_growth@FY2025] [C:fcf_margin@FY2025] [C:net_cash]
- 가격이 이미 지속성을 요구한다. 현재 EV/매출과 PER가 매우 높고, 코드가 계산한 확률 가중 기대 연 수익률은 마이너스이며 손실 확률이 높다. 이것은 가설이 틀렸다는 뜻이 아니라, 이 가격에서는 맞아도 수익이 남지 않는다는 뜻이다. [F212] [C:ev_revenue] [C:pe] [C:expected_irr] [C:p_loss]
- 아직 계획인 것과 이미 실적인 것을 가르면, 지속성의 핵심 증거가 빠져 있다. NRR, 계약 잔액, 고객 수, 미국 상업 매출이 수집되지 않았고 해자는 회사 발표와 보도에 의존한다. 입증되지 않은 상태에서 첫 비중을 크게 줄 이유가 없다. [S1](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000041/pltr-20260630.htm) [S31](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNT1RTaFhpaURiVTJZVXZYSVpLWUg3c0ZoblZlRms3S2Y0YWpocW1zYjdsRy1ZYVZSNDZLNGpycFRqVFBJLW0zd0JoV1RxN0JGZmtUcjhmT2w4WHdfREFrTjVlQUgtakU4MG5sSXV5X1dfMElDci1IXzJvdUUtVFVscW9Hc0FDa2V6X0pxNGZ4bkdOWV9Fam5TM3FNTnBjR29UamVRSVhlVEdsZw?oc=5) [S28](https://news.google.com/rss/articles/CBMizwFBVV95cUxPdkZyTUlfQkZLY2NaVlBHMXFLbWZMTVpWUEJKY1BkT0xpemFzYkZoZnIzZF9FMUJNSkZyQUNibUJSSERqbmpGSERHQy1jWGZxUjc5ekJZLXB1R05PeHBDRml0RjUzYVBDUm1Sa3MyM3RBLUt5YmtHZzNhVl82UnBOb0h3bGUzSDJvWjI0dWRFYnRHVjRpUmV0WDk1LThxQ21BR0dHci1GZUtJeGk5b0U1NkNubjFMc0d6SzYwNlVEbmdBaEg1Zy03Tm5RQ3JoNUE?oc=5) [S26](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOdmFld2JjZEoxbldQVGZGUE9ZZVRvd2I1LWhXcV93YXAtNlo1R1IwNGVVU0dCQ1dtMVk0WmpxTGdSTVNjYXBtc1ZDQVJzVFpMM1FocTN2clQ4NlN1N1pqVTNITmV6Rnl6Sk1RUzdQdzA0OFhCTmxZdHJBOEc4YnJjdS1VbEdEUWRlV1FrNjdTRWtZZDdCdDlPTGFUOUVlMExFa0d2cC1GSUdyTzdhcmttVVFiRFdLVFRvRERFUVNKYmR0dFJYUWhqWEFxS0tIdUN6dlJkY0dUUQ?oc=5)
- 매출채권이 매출보다 빠르게 늘고 DSO가 길어졌다. 이연매출과 OCF가 이 해석에 유리하긴 하지만, 수요가 진짜인지 청구가 앞선 것인지는 아직 가려지지 않았다. 단위경제가 건강하다는 입증으로 쓰기에는 이르다. [C:receivables_gap] [C:dso@FY2025] [F51] [F143]
- SBC가 여전히 크고 자사주 매입이 이를 상쇄하지 못해 희석이 이어진다. 주당 가치로 옮기면 사업 성장의 일부가 주주에게 오지 않는다. [C:sbc_to_revenue@FY2025] [C:dilution] [F5] [F168]

**사전 부검**
- 사전 부검 — 내가 틀렸다면, 성장이 모델의 기본 경로보다 훨씬 오래 높게 이어지고 멀티플이 유지되어 기다리는 사이 가격이 더 올랐기 때문이다. 정의되지 않은 시장이 정말로 열렸다면 모델링 가능한 숫자만 보는 내 접근이 기회를 놓친다. [F150] [F153] [F51]
- 사전 부검 — 정부·국방 채널과 파트너 제휴가 실제 계약으로 확인되면 단위경제가 지금 보이는 것보다 훨씬 좋을 수 있다. 내가 NRR과 계약 잔액이 없다는 이유로 보류한 것이 단지 수집 실패일 수 있다. [S31](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNT1RTaFhpaURiVTJZVXZYSVpLWUg3c0ZoblZlRms3S2Y0YWpocW1zYjdsRy1ZYVZSNDZLNGpycFRqVFBJLW0zd0JoV1RxN0JGZmtUcjhmT2w4WHdfREFrTjVlQUgtakU4MG5sSXV5X1dfMElDci1IXzJvdUUtVFVscW9Hc0FDa2V6X0pxNGZ4bkdOWV9Fam5TM3FNTnBjR29UamVRSVhlVEdsZw?oc=5) [S28](https://news.google.com/rss/articles/CBMizwFBVV95cUxPdkZyTUlfQkZLY2NaVlBHMXFLbWZMTVpWUEJKY1BkT0xpemFzYkZoZnIzZF9FMUJNSkZyQUNibUJSSERqbmpGSERHQy1jWGZxUjc5ekJZLXB1R05PeHBDRml0RjUzYVBDUm1Sa3MyM3RBLUt5YmtHZzNhVl82UnBOb0h3bGUzSDJvWjI0dWRFYnRHVjRpUmV0WDk1LThxQ21BR0dHci1GZUtJeGk5b0U1NkNubjFMc0d6SzYwNlVEbmdBaEg1Zy03Tm5RQ3JoNUE?oc=5) [S26](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOdmFld2JjZEoxbldQVGZGUE9ZZVRvd2I1LWhXcV93YXAtNlo1R1IwNGVVU0dCQ1dtMVk0WmpxTGdSTVNjYXBtc1ZDQVJzVFpMM1FocTN2clQ4NlN1N1pqVTNITmV6Rnl6Sk1RUzdQdzA0OFhCTmxZdHJBOEc4YnJjdS1VbEdEUWRlV1FrNjdTRWtZZDdCdDlPTGFUOUVlMExFa0d2cC1GSUdyTzdhcmttVVFiRFdLVFRvRERFUVNKYmR0dFJYUWhqWEFxS0tIdUN6dlJkY0dUUQ?oc=5)
- 사전 부검 — 낮은 법인세 부담이 순이익을 키워 보이게 하므로 PER를 근거로 한 내 비싸다는 판단이 과장일 수 있다. 반대로 이 효과가 사라지면 이익 기반 가치는 더 낮아진다. 어느 쪽이든 1차 자료 확인이 필요하다. [F88] [F128] [S20](https://news.google.com/rss/articles/CBMipAFBVV95cUxOcmtBTFEwT09QS0hTa0diSmNLN1NXNTlvUFlyYjVDb28yWk1rWkdpaE9LNjhYbTRWckY4TVlJcnVkMXpUMFc1LTEtajBGMmdZQkNPcDVfVktBZl81eFBfc3hYVkpIQ183ZU9GZVhBd2dmdWg1dEE0cjlpaUtOcGJmTkFYZTZiLUFETHZPSG80elFtSFdiZHktNjNPdzRCVlFaZlZOTtIBqgFBVV95cUxPZ1pGV01wRGFZNXBVZHZLUWRmX0Z5a0ZFU2d3NElxZmNtUkRRcngzZFBzWnc2TFVURTY1dmpPSktVdV9qSFM4TUZxOXl0dF9FVUY1YnVaUFBEeHJlb2I1cVUyTW8tdVZKMThsS0dJOGtDQTVUVlI2bkh6WmE4SWxmZktCQUQ3Ull3QW0wMWlZYmZEMzlTTnJGVGVSejJTZTJiX1B6WXlWRHhSdw?oc=5)

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 성장이 가속했고 영업 레버리지와 현금 창출이 이미 숫자로 확인된다는 점이다. 이 부분은 동의한다. 다만 그가 세운 반증 조건은 FY2026Q3 매출이 직전 분기 19.4억보다 줄면 가설이 깨진다는 것인데, 이 가격이 요구하는 것은 감소하지 않는 것이 아니라 가속이 이어지는 것이다. 순차 성장이 멈춰도 그 조건은 깨지지 않는다. 아직 계획인 것과 이미 실적인 것을 가르면, 지속 기간은 NRR과 계약 잔액이 비어 있어 계획 쪽이다. 그가 가격 때문에 보류한다면 나는 같은 이유로 한 걸음 더 간다. 증거가 가격을 따라오기 전에는 시작 비중을 줄 수 없다. [F153] [F150] [F51] [C:revenue_growth@FY2025]
- → 애크먼: 애크먼의 가장 강한 논거는 기본 시나리오의 주당 현재가치가 주가의 절반에 못 미치고, 확률 가중 기대 수익률이 마이너스라는 점이다. 가격 결론에는 동의한다. 그러나 그가 단순성과 예측 가능성 때문에 담을 수 없다고 하는 데는 동의하지 않는다. 시장이 정의되지 않은 기업을 오늘 모델링하기 어렵다는 이유만으로 버리지 않는다. 내가 반대하는 이유는 예측 불가능성이 아니라 가격이 요구하는 지속 기간을 증명하는 운영 지표가 비어 있다는 것이다. 이 차이는 증거가 쌓이면 해소될 수 있다. 그래서 내 판단은 영구적인 거부가 아니라 보류 후 재평가다. [C:expected_irr] [C:p_loss] [F212] [C:ev_revenue]
- → 레드팀: 레드팀의 가장 강한 논거는 성장 감속과 멀티플 붕괴가 동시에 오는 경로다. 기본 시나리오 수익률 분해에서 멀티플 변화가 가장 큰 음의 기여를 하므로, 이 경로가 내 반대의 핵심 근거가 된다. 매출채권 17억 초과 신호는 이미 내 must_be_true에 들어 있어 선행 신호로 유지한다. 매출원가가 한 분기에 크게 늘었다는 지적도 새로 받아들인다. 다만 이 증가가 AI 추론 비용 때문인지 매출 믹스 때문인지는 확인되지 않았다. 총이익률 하락이 확인될 때까지는 경고로만 두고, 판단 변경의 근거로 쓰지 않는다. [F32] [F33] [F143] [C:gross_margin@FY2025] [C:expected_irr]

**참이어야 하는 것**
- [on_track] 분기 매출 성장이 이어져 FY2026 연간 매출이 기본 시나리오 경로에 도달한다
- [on_track] 이연매출이 계속 늘어 선결제 수요와 전환비용 가설이 유지된다
- [at_risk] 매출채권이 매출보다 빠르게 늘지 않아 회수 지연 우려가 해소된다
- [on_track] 영업이익이 직전 분기보다 늘어 고정비 레버리지가 이어진다

**인정한 점**
- 앤더슨: 성장 가설 자체는 훼손되지 않았다. 내 반대는 사업이 아니라 가격과 증거 수준 때문이며, 이연매출과 영업이익이 계속 늘면 비중 0 판단을 재검토한다.
- 애크먼: 낙관적인 강세 시나리오조차 요구수익률에 못 미친다는 점을 인정한다. 이 가격에서는 가설이 맞아도 수익이 남지 않을 수 있어, 시작 비중을 0으로 둔 판단을 유지한다.
- 레드팀: 매출원가 급증은 마진 가정(FCF 마진 50%)에 대한 새 경고다. 모델러의 첫해 성장 가정이 기저율 표 없이 검증되지 않았다는 지적도 맞다. must_be_true에서 이연매출과 영업이익 외에 총이익률 유지 여부를 추적한다.


## 애크먼 — 보류 (4/5)

> 사업의 질은 훌륭하다. 총이익률 82.4%, FCF 마진 46.9%, 무차입 순현금이라는 숫자는 내가 좋아하는 모양이다. 그러나 좋은 회사도 비싸게 사면 나쁜 투자다. 주가 208.67달러에서 PER 177.68배, EV/매출 85.54배다. 보수적 기본 시나리오의 주당 현재가치는 97.1달러로 안전마진이 -114.9%이고, 강세 시나리오의 연 수익률도 +8.4%에 그친다. 확률 가중 기대 연 수익률은 -5.1%, 손실 확률은 75%다. 10년 뒤 FCF를 합리적 범위로 좁히기도 어렵다. NRR·계약 잔액·미국 상업 매출·컨센서스를 확보하지 못했고, 성장이 몇 해 더 이어질지가 가치의 대부분을 정한다. 기본 시나리오 수익률 분해에서 매출 성장 +30.4%를 멀티플 축소 -36.7%가 삼킨다. 안전마진 20% 레드라인을 크게 밑돌므로 담지 않는다.

**논거**
- 가격이 문제다. 기본 시나리오 주당 현재가치 97.1달러는 주가 208.67달러의 절반 미만이고 안전마진은 -114.9%다. 낙관적인 강세 시나리오조차 연 수익률 +8.4%로 요구수익률 10%에 못 미친다. 확률 가중 기대 연 수익률은 -5.1%, 손실 확률은 75%다. [C:mos@애크먼] [C:expected_irr] [C:p_loss] [C:irr@bull] [F212]
- 사업의 질은 인정한다. 총이익률이 82.4%, FCF 마진이 46.9%이고 SBC를 차감한 FCF도 14.2억 달러 흑자다. 차입금이 없고 순현금이 71.8억 달러(FY2025)에서 TTM 94.1억 달러로 늘어 자본시장 의존이 없다. 이 때문에 밸리언트식 위험은 없다. 문제는 사업이 아니라 가격이다. [C:gross_margin@FY2025] [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [C:net_cash@FY2025] [C:net_cash]
- 기본 시나리오의 연 수익률 분해를 보면 매출 성장이 +30.4% 기여하는데 멀티플 변화가 -36.7%로 이를 상쇄한다. 매출이 5년간 연 35.6% 성장해도 출구 배수가 40배로 내려오면 주주는 손실을 본다. 현재 가격은 성장과 높은 배수가 모두 유지될 때만 정당화된다. 민감도 표에서 가장 좋은 칸(성장 +5%p, 멀티플 ×1.25)도 연 +3.1%다. [C:ev_revenue] [C:pe] [C:expected_irr]
- 10년 뒤 현금흐름을 합리적 범위로 추정하기 어렵다. 해자와 단위경제의 증거 등급이 'claimed'이거나 'unclear'이고, NRR·계약 잔액·고객 수·미국 상업 매출은 수집되지 않았다. 컨센서스도 없어 시장 기대와의 차이를 검증할 수 없다. 단순성과 예측 가능성 기준을 충족했다고 말할 근거가 부족하다. [F51] [S1](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000041/pltr-20260630.htm)
- 이익의 질에는 확인할 것이 남아 있다. DSO가 45.2일에서 85.0일로 길어졌고 매출채권이 FY2025 10.4억에서 FY2026Q2 14.9억 달러로 늘었다. 희석 주식 수는 연 7.5% 증가해 3% 문턱을 넘고, 자사주 매입 7,498만 달러는 SBC 6.8억 달러의 일부다. 회계 등급은 watch이며 red_flag는 아니다. 그러나 안전마진이 없는 가격에서는 작은 흠도 크게 작용한다. [C:dso@FY2025] [F141] [F143] [C:dilution] [F5] [F168]

**사전 부검**
- 사전 부검: 내가 틀렸다면 성장이 시나리오 예상보다 훨씬 오래, 높게 유지된 경우다. 이연매출이 5.8억 달러로 늘고 매출 성장이 FY2025 56.2%로 가속했다. 강세 시나리오(25%)가 현실이 되고 출구 배수 50배가 유지되면 주당 가치는 312.65달러다. 그 경우 담지 않은 비용을 치른다. [C:revenue_growth@FY2025] [F51] [C:value@bull]
- 사전 부검: 모델러가 약세·기본·강세 모두에 높은 출구 배수(20~50배)를 가정했는데 이것이 보수적이라면 내 안전마진 계산이 과하게 부정적일 수 있다. 소프트웨어 플랫폼에 대한 시장의 프리미엄이 구조적으로 유지되면 멀티플 축소 -36.7%는 일어나지 않는다. 기저율 표가 없어 성장 가정의 희소성도 검증하지 못했다. [C:ev_revenue] [C:pe]
- 사전 부검: 순현금이 TTM 기준 94.1억 달러이고 무차입이므로 경영진이 대규모 자사주 매입이나 배당 등 자본 환원을 시작하면 주당 가치 계산이 바뀔 수 있다. 현재는 사용처 방침이 근거에서 확인되지 않는다. [C:net_cash] [F5]

**반론**
- → 앤더슨: 앤더슨은 성장 가속을 멱법칙의 신호로 보고 보류에 머물렀다. 그러나 스스로 인정했듯 상방 시나리오를 10년으로 늘려도 5배 문턱(4.55배)에 못 미친다. 가장 좋은 경우에도 길이 없는 가격이면 보류가 아니라 담지 않는 것이 맞다. 생존자 편향도 걸린다. 기저율 표가 없어 연 35.6% 성장이 얼마나 드문지 검증하지 못했고, 성장 가속은 이미 EV/매출 85.54배에 반영돼 있다. [C:ev_revenue] [C:revenue_growth@FY2025] [C:expected_irr] [F212]
- → 슬레이터: 슬레이터의 가장 강한 논거는 자체 현금으로 계획을 실행하므로 생존과 외부 조달 문제가 없다는 점이다. 인정한다. 그러나 생존 경로와 단위경제는 필요조건이지 가격의 정당화가 아니다. 이 가격에서는 기본 시나리오가 맞아도 연 수익률이 -5.6%이고 강세 시나리오도 +8.4%로 요구수익률 10%에 못 미친다. 슬레이터가 2022년에 인정했듯 좋은 회사도 비싸게 사면 나쁜 투자다. 비중 0이라는 그의 결론에는 동의하고, 사유는 증거 부족보다 가격이 먼저다. [C:net_cash] [C:irr@base] [C:irr@bull] [F212]
- → 레드팀: 레드팀의 첫 사전 부검(감속과 멀티플 붕괴 동시 발생)이 가장 강하다. 멀티플 변화가 기본 시나리오 분해에서 -36.7%로 가장 큰 항목이다. 이 위험은 FCF 범위를 넓히고 출구 배수 20~40배 구간의 하방을 키운다. 매출채권과 DSO 부검까지 겹치면 안전마진은 20%가 아니라 훨씬 더 필요하다. 이미 -114.9%이므로 부검을 더하면 결론은 더 확고해진다. [C:expected_irr] [C:p_loss] [C:mos@애크먼] [C:dso@FY2025]

**인정한 점**
- 슬레이터의 지적대로 사업은 자체 현금으로 성장을 감당하며 자본시장 의존이 없다. capital_markets_dependent는 false이고 밸리언트식 위험은 없다. 문제는 가격이다.
- 앤더슨의 지적대로 성장 가속과 영업 레버리지, FCF는 숫자로 확인된다. 강세 시나리오가 현실이 되면 담지 않은 비용을 치른다. 그래도 25% 확률에 기대어 -114.9% 안전마진을 감수할 이유는 되지 못한다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Palantir은 정부·국방과 대기업에 데이터 통합·분석 소프트웨어 플랫폼을 판매하고 AI 플랫폼(AIP)을 얹어 확장하는 소프트웨어 기업이다. 비용 구조로 보면 총이익률이 80%대(FY2025 82.4%, C:gross_margin@FY2025)인 고마진 소프트웨어 모델이다. 영업이익률은 FY2021 -26.7%에서 FY2025 31.6%로 개선됐고(C:operating_margin@FY2025), 매출 성장률은 FY2025 56.2%로 가속했다(C:revenue_growth@FY2025). 다만 고객 단위의 CAC, 순매출유지율(NRR), 이탈률, 계약 잔액, 미국 상업 부문 매출 같은 KPI는 수집하지 못했다. 그래서 단위경제는 '악화'라고 볼 근거는 없지만 '입증'도 되지 않아 unclear로 판단한다. 해자는 정황(마진, 이연매출 증가, 파트너십)만 있고 점유율이나 가격 인상 후 잔존 기록은 없다. 매출채권 회수기간(DSO)이 길어지고 있어 현금화 속도는 확인이 필요하다.

- [unit_economics] 총이익률이 FY2021 78.0%, FY2022 78.6%, FY2023 80.6%, FY2024 80.2%, FY2025 82.4%로 5년간 대체로 상승했다. 이 수준은 고객 1단위를 추가할 때 한계 이익이 높다는 뜻이지만, CAC, 회수기간, 코호트 데이터는 없다. [C:gross_margin@FY2021] [C:gross_margin@FY2025] [S7](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm)
- [unit_economics] 매출 성장률은 FY2023 16.7%, FY2024 28.8%, FY2025 56.2%로 가속했다. 같은 기간 SBC/매출은 FY2021 50.5%에서 FY2025 15.3%로 내려와 규모가 커지며 보상 부담이 희석되고 있다. 다만 15.3%는 여전히 회계 신호 기준(10%)을 넘는다. [C:revenue_growth@FY2023] [C:revenue_growth@FY2024] [C:revenue_growth@FY2025] [C:sbc_to_revenue@FY2021] [C:sbc_to_revenue@FY2025]
- [unit_economics] FCF 마진은 FY2023 31.3%, FY2024 39.8%, FY2025 46.9%로 올랐고 SBC를 차감한 FCF도 FY2025 14.2억으로 흑자다. 현금 창출력은 SBC를 비용으로 보더라도 확인된다. 다만 FCF/순이익 배율이 FY2023 3.32x에서 FY2025 1.29x로 내려와 현금이 이익보다 훨씬 많던 구간은 지나갔다. [C:fcf_margin@FY2023] [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [C:fcf_conversion@FY2023] [C:fcf_conversion@FY2025]
- [customers] 매출채권이 FY2024 5.8억에서 FY2025 10.4억, FY2026Q2 14.9억으로 늘었다. DSO도 FY2021 45.2일에서 FY2025 85.0일로 길어졌다. 대형 정부·기업 계약의 결제 조건 변화나 고객 집중을 시사할 수 있으나, 고객별 매출 비중은 수집하지 못해 원인을 확정할 수 없다. [F137] [F141] [F143] [C:dso@FY2021] [C:dso@FY2025] [C:receivables_gap]
- [industry] 정부·국방 부문은 육군 TITAN 시스템 납품과 같은 대형 조달이 보도된다. 상업 부문은 PwC, Nebius 등 대형 파트너와의 제휴로 채널을 넓히는 중이다. 경쟁사별 점유율이나 경쟁 입찰 결과는 자료에 없어서 산업 내 위치를 숫자로 입증하지 못한다. 또한 'sovereign AI에 외부 가드레일이 생겼다'는 보도는 규제 위험의 단서이나 내용은 확인하지 않았다. [S31](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNT1RTaFhpaURiVTJZVXZYSVpLWUg3c0ZoblZlRms3S2Y0YWpocW1zYjdsRy1ZYVZSNDZLNGpycFRqVFBJLW0zd0JoV1RxN0JGZmtUcjhmT2w4WHdfREFrTjVlQUgtakU4MG5sSXV5X1dfMElDci1IXzJvdUUtVFVscW9Hc0FDa2V6X0pxNGZ4bkdOWV9Fam5TM3FNTnBjR29UamVRSVhlVEdsZw?oc=5) [S28](https://news.google.com/rss/articles/CBMizwFBVV95cUxPdkZyTUlfQkZLY2NaVlBHMXFLbWZMTVpWUEJKY1BkT0xpemFzYkZoZnIzZF9FMUJNSkZyQUNibUJSSERqbmpGSERHQy1jWGZxUjc5ekJZLXB1R05PeHBDRml0RjUzYVBDUm1Sa3MyM3RBLUt5YmtHZzNhVl82UnBOb0h3bGUzSDJvWjI0dWRFYnRHVjRpUmV0WDk1LThxQ21BR0dHci1GZUtJeGk5b0U1NkNubjFMc0d6SzYwNlVEbmdBaEg1Zy03Tm5RQ3JoNUE?oc=5) [S26](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOdmFld2JjZEoxbldQVGZGUE9ZZVRvd2I1LWhXcV93YXAtNlo1R1IwNGVVU0dCQ1dtMVk0WmpxTGdSTVNjYXBtc1ZDQVJzVFpMM1FocTN2clQ4NlN1N1pqVTNITmV6Rnl6Sk1RUzdQdzA0OFhCTmxZdHJBOEc4YnJjdS1VbEdEUWRlV1FrNjdTRWtZZDdCdDlPTGFUOUVlMExFa0d2cC1GSUdyTzdhcmttVVFiRFdLVFRvRERFUVNKYmR0dFJYUWhqWEFxS0tIdUN6dlJkY0dUUQ?oc=5) [S27](https://news.google.com/rss/articles/CBMingFBVV95cUxOSXRiUnZMQ0xiTjE0dktzakxGYVpJeWtNMC1ZQ2pXd1JRU0Q0c0JtNzZqS3RoOUFYQ21LVzlUY3dyUS13cjJXTGpiOTZ1YmRHWm52XzdxLUdsMXVTSUlobzYybGkwVzBhWk55TjZoLUlkTFB2TEFSbDYwd1Z1OVJZVDBJRmlPTlh4U0hsZ0VVWWtBaDJidW1PX3dOYUl5UQ?oc=5)
- [runway] 재투자 활주로를 보면 R&D는 FY2025 5.6억으로 매출 대비 비중이 작고 capex도 FY2025 3,388만에 그친다. 자본집약도가 낮아 성장에 필요한 투자 부담은 가볍다. 반면 현금과 단기투자는 FY2026Q2 기준 20.3억과 73.8억이고 부채는 없는 것으로 보여, 벌어들인 현금을 넣을 사업 내 투자처보다 쌓이는 속도가 더 빠르다. 자사주 매입도 FY2025 7,498만으로 적다. [F158] [F11] [F23] [F183] [F5] [S1](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000041/pltr-20260630.htm) [S7](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm)
- [runway] 희석 주식 수는 FY2021 19.2억에서 FY2025 25.7억으로 늘었으나 증가율은 FY2023 11.3%, FY2024 6.7%, FY2025 4.7%로 둔화했다. 최근 두 분기(FY2026Q1, FY2026Q2)는 25.7억으로 같다. 성장 투자의 비용이 주주 희석으로 지불돼 왔고, 그 속도는 줄고 있다. [C:share_change@FY2023] [C:share_change@FY2024] [C:share_change@FY2025] [F60] [F61]
- [unit_economics] 계약 잔액(RPO/TCV), NRR, 고객 수, 미국 상업 매출은 수집되지 않았다. 이연매출 증가(FY2026Q2 5.8억)와 매출 성장 가속은 수요 증거이나, 해자와 단위경제를 '입증'하려면 이들 KPI가 필요하다. 추정: 현재 확인된 숫자는 상위 레벨 흔적이어서 고객 단위 경제성은 판단 보류가 맞다. [F51] [S1](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000041/pltr-20260630.htm)
- [proven] 매출이 늘면서 영업이익률이 -26.7%(FY2021)에서 31.6%(FY2025)로 개선됐고 총이익률은 78.0%에서 82.4%로 올랐다. 고정비 레버리지와 소프트웨어 규모의 경제가 공시 숫자로 확인된다. 다만 이것은 마진 흔적이지 경쟁 우위의 인과를 보여주는 증거는 아니며, 시장 점유율 데이터는 없다. [C:operating_margin@FY2025] [C:gross_margin@FY2021] [C:gross_margin@FY2025] [S7](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm)
- [claimed] 이연매출이 FY2025 4.1억에서 FY2026Q2 5.8억으로 늘었다. 선수금과 계약 선결제가 쌓이고 있다는 점에서 고객이 장기 계약으로 묶인다는 추정과 부합한다. 그러나 NRR, 이탈률, 계약 기간과 갱신율은 확인되지 않았고 전환비용은 회사 설명과 보도에 의존한다. [F49] [F51] [S1](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000041/pltr-20260630.htm) [S7](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm)
- [claimed] 미 육군 TITAN 시스템 8대 납품 보도와 Nebius, PwC와의 제휴 발표는 정부·국방과 파트너 채널에서 입지를 보여준다. 그러나 모두 회사 발표와 보도뿐이고 계약 금액과 경쟁 입찰 결과는 공시에서 확인되지 않았다. [S31](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNT1RTaFhpaURiVTJZVXZYSVpLWUg3c0ZoblZlRms3S2Y0YWpocW1zYjdsRy1ZYVZSNDZLNGpycFRqVFBJLW0zd0JoV1RxN0JGZmtUcjhmT2w4WHdfREFrTjVlQUgtakU4MG5sSXV5X1dfMElDci1IXzJvdUUtVFVscW9Hc0FDa2V6X0pxNGZ4bkdOWV9Fam5TM3FNTnBjR29UamVRSVhlVEdsZw?oc=5) [S26](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOdmFld2JjZEoxbldQVGZGUE9ZZVRvd2I1LWhXcV93YXAtNlo1R1IwNGVVU0dCQ1dtMVk0WmpxTGdSTVNjYXBtc1ZDQVJzVFpMM1FocTN2clQ4NlN1N1pqVTNITmV6Rnl6Sk1RUzdQdzA0OFhCTmxZdHJBOEc4YnJjdS1VbEdEUWRlV1FrNjdTRWtZZDdCdDlPTGFUOUVlMExFa0d2cC1GSUdyTzdhcmttVVFiRFdLVFRvRERFUVNKYmR0dFJYUWhqWEFxS0tIdUN6dlJkY0dUUQ?oc=5) [S28](https://news.google.com/rss/articles/CBMizwFBVV95cUxPdkZyTUlfQkZLY2NaVlBHMXFLbWZMTVpWUEJKY1BkT0xpemFzYkZoZnIzZF9FMUJNSkZyQUNibUJSSERqbmpGSERHQy1jWGZxUjc5ekJZLXB1R05PeHBDRml0RjUzYVBDUm1Sa3MyM3RBLUt5YmtHZzNhVl82UnBOb0h3bGUzSDJvWjI0dWRFYnRHVjRpUmV0WDk1LThxQ21BR0dHci1GZUtJeGk5b0U1NkNubjFMc0d6SzYwNlVEbmdBaEg1Zy03Tm5RQ3JoNUE?oc=5)

### 경영진·자본배분 — mixed

보상 지표, 내부자 매매, 과거 가이던스 적중률은 근거가 없어 정렬 여부를 직접 판단할 수 없다. 확인되는 것은 세 가지다. 첫째, SBC 부담은 매출 대비 50.5%(FY2021)에서 15.3%(FY2025)로 내려왔다. 둘째, 희석 주식 수는 19.2억(FY2021)에서 25.7억(FY2025)으로 늘었고 FY2025 증가율은 4.7%다. 셋째, 자사주 매입은 SBC 규모에 비해 미미해서 희석을 상쇄하지 못한다. 차입금 없이 순현금 94.1억 USD를 쌓고 있고 대형 M&A 흔적은 데이터에 없다. 그래서 정렬은 mixed로 두며, 이는 근거가 부족하다는 뜻이다.

- [compensation] 근거 없음. DEF 14A(S6)가 근거 목록에 있으나 보상 연동 지표(장기 지표인지 단기 EPS·조정 EBITDA인지)와 베스팅 기간은 사실로 정리되지 않았다. 보상 정렬은 판단할 수 없다. [S6](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000019/pltr-20260423.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도는 리서처가 사실로 확보하지 못했다. [S6](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000019/pltr-20260423.htm)
- [guidance] 근거 없음. 과거 가이던스 사실이 저장되지 않아 가이던스 적중률(C:guidance_hit_rate)을 계산할 수 없다. 8-K 실적 발표(S2·S5·S8·S10)에서 가이던스를 추출하기 전에는 경영진 신뢰도를 평가하지 않는다. [S2](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000039/pltr-20260803.htm) [S5](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000026/pltr-20260504.htm) [S8](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000004/pltr-20260202.htm) [S10](https://www.sec.gov/Archives/edgar/data/1321655/000132165525000130/pltr-20251103.htm)
- [dilution] 희석 주식 수는 FY2021 19.2억에서 FY2025 25.7억으로 늘었다. 연간 증가율은 FY2022 7.3%, FY2023 11.3%, FY2024 6.7%, FY2025 4.7%로 둔화 중이다. 다만 코드 신호는 연 7.5% 증가가 3% 기준을 넘는다고 표시한다. 이후 분기의 희석 주식 수는 25.7억에서 거의 변하지 않았다. [F52] [F56] [C:share_change@FY2022] [C:share_change@FY2023] [C:share_change@FY2024] [C:share_change@FY2025] [C:dilution]
- [dilution] SBC는 FY2021 7.8억 USD에서 FY2025 6.8억 USD로 절대액이 줄었고, 매출 대비 비중은 50.5%에서 15.3%로 내려왔다. 그래도 코드 기준 10%는 넘는다. SBC를 차감한 FCF는 FY2025 14.2억 USD다. [F164] [F168] [C:sbc_to_revenue@FY2021] [C:sbc_to_revenue@FY2025] [C:fcf_after_sbc@FY2025]
- [capital_allocation] 자사주 매입은 FY2023까지 0이었고 FY2024 6,420만 USD, FY2025 7,498만 USD다. 같은 해 SBC가 6.9억, 6.8억 USD이므로 매입 규모가 희석을 상쇄하는 수준이 아니다. 지금 단계에서 매입은 희석을 줄이는 수단으로 쓰이지 않고 있다. [F4] [F5] [F167] [F168]
- [capital_allocation] 차입금은 FY2021 이후 XBRL에 없어 사실상 무차입으로 보이나 직접 확인하지는 못했다. 순현금은 FY2025 71.8억 USD에서 TTM 기준 94.1억 USD로 늘었다. 현금은 FY2026Q2 현금 20.3억 USD와 단기투자 73.8억 USD로 구성된다. 이 현금의 사용처(재투자·M&A·환원)에 대한 경영진 방침은 근거에서 확인되지 않는다. [F41] [F23] [F183] [C:net_cash@FY2025] [C:net_cash]
- [capital_allocation] 설비투자는 FY2025 3,388만 USD로 FCF 21.0억 USD에 비해 작고, 영업현금흐름은 FY2025 21.3억 USD다. M&A 이력은 영업권이 FY2021 187만 USD, FY2022 3,794만 USD로만 나타나 큰 인수 흔적은 없다. 그 이후 기간은 영업권 사실이 없어 인수 이력은 확정할 수 없다. [F11] [F72] [F73] [C:fcf@FY2025] [F111]

### 회계 품질 — watch

현금흐름이 이익을 뒷받침하므로 숫자를 대체로 믿을 수 있다. FY2025 영업현금흐름 21.3억(F111)은 순이익 16.3억(F101)보다 크고, 발생액 비율은 5개 연도 모두 음수다(C:accruals_ratio@FY2025 -6.7%). 이연매출도 FY2025 4.1억(F49)에서 FY2026Q2 5.8억(F51)으로 늘었다. 다만 조정해서 볼 숫자가 세 가지 있다. (1) 매출채권이 매출보다 빠르게 늘어 DSO가 45.2일에서 85.0일로 길어졌다(C:dso@FY2021, C:dso@FY2025). 청구가 현금 회수보다 앞서 있을 수 있다. (2) SBC가 FY2025에 6.8억(F168)이라, 이익과 FCF는 SBC 차감 기준인 C:fcf_after_sbc@FY2025 14.2억으로 봐야 한다. (3) 자사주 매입이 7,498만(F5)에 그쳐 SBC를 상쇄하지 못해 희석이 계속된다. 법인세 부담이 매우 낮아 세전이익 대비 순이익이 높게 나온다(F88, F128). 감사의견, Non-GAAP 조정 내역, 정정 여부는 10-K 원문을 확인하지 못했다. 재무제표 정정이나 감사인 변경 신호는 코드에 잡히지 않았다. 따라서 red_flag 근거는 없고 watch로 판정한다.

- [benign] sbc_to_revenue: SBC/매출은 문턱 10%를 넘지만 FY2021 50.5%, FY2022 29.6%, FY2023 21.4%, FY2024 24.1%, FY2025 15.3%로 꾸준히 내려왔다. 매출이 SBC보다 빠르게 커진 결과다. 다만 절대액은 FY2025 6.8억으로 여전히 크다. SBC/영업현금흐름도 FY2021 233.1%에서 FY2025 32.0%로 낮아져 문턱 50%를 밑돈다. 이익과 FCF는 SBC를 비용으로 보고 C:fcf_after_sbc@FY2025 14.2억을 기준으로 삼아야 한다. FCF 46.9%(C:fcf_margin@FY2025)는 SBC를 빼지 않은 값이다. [C:sbc_to_revenue@FY2021] [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [C:fcf_after_sbc@FY2025] [F168]
- [concern] receivables_gap: 코드 신호는 FY2024에 매출채권 증가율이 매출 증가율을 15%p 넘게 앞섰다고 알린다. 이후에도 이어졌다. 매출채권은 FY2024 5.8억(F137)에서 FY2025 10.4억(F141), FY2026Q2 14.9억(F143)으로 늘었다. 같은 기간 FY2025 매출 증가율은 56.2%(C:revenue_growth@FY2025)다. DSO는 FY2021 45.2일에서 FY2025 85.0일로 길어졌다. 대형 정부·기업 계약의 청구 시점이나 분기 말 매출 집중이 원인일 수 있다. 이연매출 증가(F49, F51)와 OCF가 순이익보다 큰 점은 이 해석에 유리하다. 그래도 계약 조건 변화인지 회수 지연인지는 확인하지 못했으므로 문제로 남긴다. 대손충당금과 고객 집중도를 10-K에서 확인해야 한다. [C:receivables_gap] [C:dso@FY2021] [C:dso@FY2025] [C:revenue_growth@FY2025] [F137] [F141] [F143] [F49] [F51]
- [concern] dilution: 희석 주식 수는 FY2021 19.2억에서 FY2025 25.7억으로 늘었고, 연 증가율 7.5%는 문턱 3%를 크게 넘는다. 연도별로는 FY2023 11.3%, FY2024 6.7%, FY2025 4.7%로 둔화 중이다. FY2025 25.7억(F56)과 FY2026Q2 25.7억(F61)이 같아 최근에는 증가가 멈춘 듯 보인다. 그러나 이 기간 중 SBC는 분기 2.7억(F173)까지 커졌고, 자사주 매입은 FY2025 7,498만(F5)으로 SBC 6.8억(F168)의 일부에 그친다. 이 정도 매입으로는 희석을 막지 못한다. 주당 가치를 계산할 때는 SBC에 따른 주식 수 증가를 반영해야 한다. [C:dilution] [C:share_change@FY2025] [F52] [F56] [F61] [F5] [F168] [F173]
- [watch] DSO가 5년 동안 두 배 가까이 길어졌다(C:dso@FY2021, C:dso@FY2025). 매출채권 증가가 매출 증가를 앞선다. 반면 FY2025 영업현금흐름/순이익은 1.0을 넘고, 발생액 비율은 음수이며 이연매출도 늘고 있다. 이익의 질을 직접 해치는 근거는 없지만 계속 지켜봐야 한다. [C:dso@FY2025] [C:accruals_ratio@FY2025] [C:fcf_conversion@FY2025] [F141] [F49]
- [watch] 세전이익 16.6억(F128) 대비 FY2025 법인세는 2,272만(F88)으로 부담이 매우 낮다. 뉴스 S20은 실효세율 1.4%를 보도했지만 1차 자료로 확인하지 못했다. 이익 증가의 상당 부분이 주식보상 공제나 이월결손금 같은 세제 효과일 수 있다. 이런 효과는 반복되지 않을 수 있으므로, 순이익이나 PER로 가치를 볼 때는 정상 세율을 적용한 이익으로 조정해서 봐야 한다. [F88] [F128] [S20](https://news.google.com/rss/articles/CBMipAFBVV95cUxOcmtBTFEwT09QS0hTa0diSmNLN1NXNTlvUFlyYjVDb28yWk1rWkdpaE9LNjhYbTRWckY4TVlJcnVkMXpUMFc1LTEtajBGMmdZQkNPcDVfVktBZl81eFBfc3hYVkpIQ183ZU9GZVhBd2dmdWg1dEE0cjlpaUtOcGJmTkFYZTZiLUFETHZPSG80elFtSFdiZHktNjNPdzRCVlFaZlZOTtIBqgFBVV95cUxPZ1pGV01wRGFZNXBVZHZLUWRmX0Z5a0ZFU2d3NElxZmNtUkRRcngzZFBzWnc2TFVURTY1dmpPSktVdV9qSFM4TUZxOXl0dF9FVUY1YnVaUFBEeHJlb2I1cVUyTW8tdVZKMThsS0dJOGtDQTVUVlI2bkh6WmE4SWxmZktCQUQ3Ull3QW0wMWlZYmZEMzlTTnJGVGVSejJTZTJiX1B6WXlWRHhSdw?oc=5)
- [info] 코드의 Non-GAAP 비교 신호(non_gaap:*)는 이번 입력에서 계산되지 않았다. 8-K 실적 발표(S2, S5, S8, S10)의 조정 내역을 사실로 추출하지 못했다. 회사의 조정 영업이익과 조정 FCF는 SBC와 관련 급여세를 제외한다고 알려져 있으나, 이번 근거에서는 크기와 반복성을 확인하지 못했다. 평가는 보류하고, GAAP 기준(C:operating_margin@FY2025 31.6%)을 쓴다. [S2](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000039/pltr-20260803.htm) [S7](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm) [C:operating_margin@FY2025]
- [info] 감사의견, 핵심감사사항, 계속기업 의문 여부, 특수관계자 거래는 10-K(S7) 원문에서 확인하지 못했다. 코드 신호에도 재무제표 정정(restatement)이나 감사인 변경(auditor_change)은 없다. 이 부분은 미확인으로 두며, '문제 없음'을 입증한 것은 아니다. [S7](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm)
- [info] 이연매출은 FY2025 4.1억(F49), FY2026Q1 5.2억(F50), FY2026Q2 5.8억(F51)으로 늘고 있다. 매출 성장 중에 이연매출이 줄어드는 신호(deferred_revenue)는 없다. 선수금이 쌓인다는 점은 매출 인식 측면에서 긍정적이다. 그러나 계약별 인식 시점과 총액·순액 정책은 확인하지 못했다. [F49] [F50] [F51]

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 성장 감속과 멀티플 붕괴가 동시에 온다. 주가 208.67달러(F212)는 EV/매출 85.54배, PER 177.68배(C:ev_revenue, C:pe)로, 매출 성장이 계속 가속한다는 가정을 이미 담고 있다. 매출 성장이 FY2025의 56.2%(C:revenue_growth@FY2025)에서 꺾이면, 실적이 나빠지지 않아도 배수만 약세 출구 배수 20배(bear)나 그 아래로 내려간다. 기본 시나리오 수익률 분해에서도 멀티플 변화가 -36.7%로 가장 크다. 성장주가 감속 국면에 들어가면 이익이 늘어도 주가가 내려가는 전형적 경로다. 약세 확률이 이미 30%인데도 기대 연 수익률이 -5.1%(C:expected_irr)라는 것은 상승 여지가 거의 없다는 뜻이다. [F212] [C:ev_revenue] [C:pe] [C:revenue_growth@FY2025] [C:expected_irr]
- (12%) 청구는 앞서가고 현금 회수는 뒤처지는 구조가 드러난다. 매출채권이 FY2024 5.8억(F137)에서 FY2026Q2 14.9억(F143)으로 늘었고 DSO는 85.0일(C:dso@FY2025)까지 길어졌다. 대형 정부·기업 계약에서 결제 조건이 느슨해졌거나 일부 고객에 매출이 몰려 있다면, 계약 조정이나 회수 지연이 한 번만 나와도 FCF 마진 46.9%(C:fcf_margin@FY2025)와 이익의 질에 대한 믿음이 흔들린다. 고객 집중도와 대손충당금은 확인되지 않았다(forensic 미확인). 시장이 '현금이 이익보다 크다'는 전제를 거두면 고배수를 지탱할 근거가 없어진다. [F137] [F143] [C:dso@FY2025] [C:receivables_gap] [C:fcf_margin@FY2025]
- (10%) 정부·국방 의존과 규제가 겹쳐 신규 계약과 갱신이 느려진다. 'sovereign AI에 외부 가드레일이 생겼다'는 보도(S27)와 AI 업체 집중 위험을 경고하는 보도(S35), 1.4% 실효세율에 대한 정치적 반발 가능성(S20)이 있다. 이연매출은 FY2026Q2 5.8억(F51)으로 늘었지만, 육군 TITAN 납품(S31) 같은 대형 조달은 예산·정권·입찰 일정에 따라 한꺼번에 움직인다. 계약 잔액과 NRR은 확인되지 않아 이 위험을 숫자로 방어할 수 없다. 선결제가 줄기 시작하면 매출보다 먼저 이연매출에서 보인다. [S27](https://news.google.com/rss/articles/CBMingFBVV95cUxOSXRiUnZMQ0xiTjE0dktzakxGYVpJeWtNMC1ZQ2pXd1JRU0Q0c0JtNzZqS3RoOUFYQ21LVzlUY3dyUS13cjJXTGpiOTZ1YmRHWm52XzdxLUdsMXVTSUlobzYybGkwVzBhWk55TjZoLUlkTFB2TEFSbDYwd1Z1OVJZVDBJRmlPTlh4U0hsZ0VVWWtBaDJidW1PX3dOYUl5UQ?oc=5) [S35](https://news.google.com/rss/articles/CBMipAFBVV95cUxONzd2MEZiSjhkQ0FEbEtSWVMxNEtHWnpJU21LUzFYcHdDN3M1TnkyWXJhdVBrU0NpTTlnX0gzNF9waVBIejhnSFltOXpNU0hzZkNJZVdzdnNfdnlUNmhfWjQ5MHJMMmNWdzZkcGNDelFlNDREdUpkbDNNTldCNjdCZGQyR0lUWFlZNUx4X21Ec3RON0E1d0dNc2VyZjlkRWNVYU9wUg?oc=5) [S20](https://news.google.com/rss/articles/CBMipAFBVV95cUxOcmtBTFEwT09QS0hTa0diSmNLN1NXNTlvUFlyYjVDb28yWk1rWkdpaE9LNjhYbTRWckY4TVlJcnVkMXpUMFc1LTEtajBGMmdZQkNPcDVfVktBZl81eFBfc3hYVkpIQ183ZU9GZVhBd2dmdWg1dEE0cjlpaUtOcGJmTkFYZTZiLUFETHZPSG80elFtSFdiZHktNjNPdzRCVlFaZlZOTtIBqgFBVV95cUxPZ1pGV01wRGFZNXBVZHZLUWRmX0Z5a0ZFU2d3NElxZmNtUkRRcngzZFBzWnc2TFVURTY1dmpPSktVdV9qSFM4TUZxOXl0dF9FVUY1YnVaUFBEeHJlb2I1cVUyTW8tdVZKMThsS0dJOGtDQTVUVlI2bkh6WmE4SWxmZktCQUQ3Ull3QW0wMWlZYmZEMzlTTnJGVGVSejJTZTJiX1B6WXlWRHhSdw?oc=5) [S31](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNT1RTaFhpaURiVTJZVXZYSVpLWUg3c0ZoblZlRms3S2Y0YWpocW1zYjdsRy1ZYVZSNDZLNGpycFRqVFBJLW0zd0JoV1RxN0JGZmtUcjhmT2w4WHdfREFrTjVlQUgtakU4MG5sSXV5X1dfMElDci1IXzJvdUUtVFVscW9Hc0FDa2V6X0pxNGZ4bkdOWV9Fam5TM3FNTnBjR29UamVRSVhlVEdsZw?oc=5) [F51]
- (10%) AI 경쟁과 컴퓨팅 비용으로 마진이 꺾이고 SBC 희석이 남는다. 매출원가가 FY2026Q1 2.2억(F32)에서 FY2026Q2 3.0억(F33)으로 한 분기에 크게 늘었다. 가격 경쟁이나 AI 추론 비용 증가가 시작되면 총이익률 82.4%(C:gross_margin@FY2025)와 FCF 마진 50% 가정이 약해진다. SBC는 분기 2.7억(F173)으로 커졌고 자사주 매입은 7,498만(F5)에 그쳐 희석이 계속된다(C:dilution). 마진 압박과 희석이 겹치면 주당 FCF는 매출만큼 늘지 않는다. [F32] [F33] [C:gross_margin@FY2025] [F173] [F5] [C:dilution]
- 약한 가정 `base.exit_multiple`: 기본 시나리오가 5년 뒤 출구 P/FCF를 40배로 둔다. 이는 매출 성장이 21%·17%로 내려온 시점에도 고배수가 유지된다는 가정이다. 현재 EV/매출 85.54배(C:ev_revenue)에서 40배로 내려가도 기본 시나리오 연 수익률은 -5.6%이고, 약세 20배에서는 더 나빠진다. 기저율 표가 없어 40배를 뒷받침하는 외부 근거가 없다. [C:ev_revenue] [C:expected_irr] [C:base_rate@base]
- 약한 가정 `base.revenue_growth`: 첫해 성장 78%, 5년 CAGR 35.6%는 기저율 표가 없어 검증되지 않았다. 컨센서스와 과거 가이던스도 확보하지 못해 이 경로가 시장과 다른지, 이미 반영됐는지 비교할 수 없다. 매출 성장이 5%p만 낮아도 기본 시나리오 수익률이 달라진다(민감도 표). [C:base_rate@base] [C:revenue_growth@FY2025]
- 약한 가정 `base.fcf_margin`: FCF 마진 50%는 FY2025의 46.9%(C:fcf_margin@FY2025)보다 높다. 그런데 이 값은 SBC를 차감하지 않은 수치이고, SBC 차감 FCF는 14.2억(C:fcf_after_sbc@FY2025)이다. DSO 상승(C:dso@FY2025)과 낮은 법인세(F88)도 지속 가능성이 불확실하다. [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [C:dso@FY2025] [F88]

## 검증 (L6)

주장 71개 — supported 55 · unsupported 16 · contradicted 0 · leap 0 · 미검증 0

- [unsupported] 애크먼: 사전 부검: 모델러가 약세·기본·강세 모두에 높은 출구 배수(20~50배)를 가정했는데 이것이 보수적이라면 내 안전마진 계산이 과하게 부정적일 수 있다. 소프트웨 — 출처 없는 숫자 36.7% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 애크먼: 기본 시나리오의 연 수익률 분해를 보면 매출 성장이 +30.4% 기여하는데 멀티플 변화가 -36.7%로 이를 상쇄한다. 매출이 5년간 연 35.6% 성장해도 출구 — 출처 없는 숫자 30.4%, 36.7%, 3.1% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 성장 감속과 멀티플 붕괴가 동시에 온다. 주가 208.67달러(F212)는 EV/매출 85.54배, PER 177.68배(C:ev_revenue, C:pe)로,  — 출처 없는 숫자 36.7% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 정부·국방 의존과 규제가 겹쳐 신규 계약과 갱신이 느려진다. 'sovereign AI에 외부 가드레일이 생겼다'는 보도(S27)와 AI 업체 집중 위험을 경고하는 — 출처 없는 숫자 1.4% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 회계 품질: 세전이익 16.6억(F128) 대비 FY2025 법인세는 2,272만(F88)으로 부담이 매우 낮다. 뉴스 S20은 실효세율 1.4%를 보도했지만 1차 자료로 확 — 출처 없는 숫자 1.4% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 기본 시나리오가 5년 뒤 출구 P/FCF를 40배로 둔다. 이는 매출 성장이 21%·17%로 내려온 시점에도 고배수가 유지된다는 가정이다. 현재 EV/매출 85. — 없는 근거 인용: C:base_rate@base
- [unsupported] 애크먼: 가격이 문제다. 기본 시나리오 주당 현재가치 97.1달러는 주가 208.67달러의 절반 미만이고 안전마진은 -114.9%다. 낙관적인 강세 시나리오조차 연 수익률 — 없는 근거 인용: C:mos@애크먼
- [unsupported] 애크먼: 레드팀의 첫 사전 부검(감속과 멀티플 붕괴 동시 발생)이 가장 강하다. 멀티플 변화가 기본 시나리오 분해에서 -36.7%로 가장 큰 항목이다. 이 위험은 FCF  — 없는 근거 인용: C:mos@애크먼
- [unsupported] 앤더슨: 애크먼의 가장 강한 논거는 기본 시나리오 수익률 분해에서 매출 성장 +30.4%를 멀티플 축소 -36.7%가 삼킨다는 점이다. 그러나 그 분해는 기본 시나리오(5 — 없는 근거 인용: C:mos@애크먼
- [unsupported] 모델러: 근거로 확인되는 것은 성장 가속 자체(F149→F152, F150→F153)이고 이를 높게 반영한다. 다만 가격이 그 성장의 지속 기간까지 이미 선반영한 것으로  — 없는 근거 인용: C:implied_cagr
- [unsupported] 앤더슨: EV/매출이 85.54배다. 이 가격은 상방 시나리오가 10년 동안 이어져도 5배 수익을 허락하지 않는다. 코드 계산상 상방 10년 가치가 5배 문턱에 못 미치므 — 상방 10년 가치가 5배 문턱에 못 미친다는 핵심 주장의 계산값은 인용되지 않았다. EV/매출 85.5배와 주가만 인용값과 일치한다.
- [unsupported] 애크먼: 이익의 질에는 확인할 것이 남아 있다. DSO가 45.2일에서 85.0일로 길어졌고 매출채권이 FY2025 10.4억에서 FY2026Q2 14.9억 달러로 늘었다 — 출처 없는 숫자 3% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 경영진·자본배분: 희석 주식 수는 FY2021 19.2억에서 FY2025 25.7억으로 늘었다. 연간 증가율은 FY2022 7.3%, FY2023 11.3%, FY2024 6.7% — 출처 없는 숫자 3% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 사업·산업: FCF 마진은 FY2023 31.3%, FY2024 39.8%, FY2025 46.9%로 올랐고 SBC를 차감한 FCF도 FY2025 14.2억으로 흑자다. 현금 — 출처 없는 숫자 3.32, 1.29 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 첫해 성장 78%, 5년 CAGR 35.6%는 기저율 표가 없어 검증되지 않았다. 컨센서스와 과거 가이던스도 확보하지 못해 이 경로가 시장과 다른지, 이미 반영됐 — 없는 근거 인용: C:base_rate@base
- [unsupported] 앤더슨: 컨센서스와 기저율 표가 모두 없다. 시장이 이 기회를 왜 과소평가하는지(9번 질문)를 코드로 확인할 수 없다. 드문 일에 거는 것은 내 철학이지만, 검증 없이 크 — 없는 근거 인용: C:implied_cagr

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| 매출 (revenue) | 15.4억 USD | 19.1억 USD | 22.3억 USD | 28.7억 USD | 44.8억 USD |
| 매출 성장 (revenue_growth) | — | 23.6% | 16.7% | 28.8% | 56.2% |
| 총이익률 (gross_margin) | 78.0% | 78.6% | 80.6% | 80.2% | 82.4% |
| 영업이익률 (operating_margin) | -26.7% | -8.5% | 5.4% | 10.8% | 31.6% |
| 순이익 (net_income) | -5.2억 USD | -3.7억 USD | 2.1억 USD | 4.6억 USD | 16.3억 USD |
| 영업현금흐름 (ocf) | 3.3억 USD | 2.2억 USD | 7.1억 USD | 11.5억 USD | 21.3억 USD |
| 설비투자 (capex) | 1,263만 USD | 4,003만 USD | 1,511만 USD | 1,263만 USD | 3,388만 USD |
| FCF (fcf) | 3.2억 USD | 1.8억 USD | 7.0억 USD | 11.4억 USD | 21.0억 USD |
| FCF 마진 (fcf_margin) | 20.8% | 9.6% | 31.3% | 39.8% | 46.9% |
| FCF/순이익 (fcf_conversion) | — | — | 3.32x | 2.47x | 1.29x |
| SBC (sbc) | 7.8억 USD | 5.6억 USD | 4.8억 USD | 6.9억 USD | 6.8억 USD |
| SBC/매출 (sbc_to_revenue) | 50.5% | 29.6% | 21.4% | 24.1% | 15.3% |
| SBC/영업현금흐름 (sbc_to_ocf) | 233.1% | 252.4% | 66.8% | 59.9% | 32.0% |
| SBC 차감 FCF (fcf_after_sbc) | -4.6억 USD | -3.8억 USD | 2.2억 USD | 4.5억 USD | 14.2억 USD |
| ROIC (roic) | — | — | — | — | 663.4% |
| 순현금 (net_cash) | 25.2억 USD | 26.3억 USD | 36.7억 USD | 52.3억 USD | 71.8억 USD |
| 순부채/EBITDA (net_debt_to_ebitda) | — | — | -23.96x | -15.29x | -4.98x |
| 희석 주식 수 (diluted_shares) | 19.2억 | 20.6억 | 23.0억 | 24.5억 | 25.7억 |
| 주식 수 변화 (share_change) | — | 7.3% | 11.3% | 6.7% | 4.7% |
| DSO(일) (dso) | 45.2 | 49.5 | 59.8 | 73.2 | 85.0 |
| 발생액 비율 (accruals_ratio) | — | -17.8% | -12.6% | -12.7% | -6.7% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, cost_of_revenue, d_and_a, debt, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, goodwill, goodwill_to_assets, gross_profit, income_tax, interest_expense, operating_income, pretax_income, receivables, receivables_growth, rnd, short_term_investments, total_assets

### 시장 · TTM(FY2026Q2) 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 208.67 USD/share (2026-10-13, F212) |
| 희석 주식 수 (shares) | 25.7억 |
| 시가총액 (market_cap) | 5,360.1억 USD |
| 순현금 (net_cash) | 94.1억 USD |
| EV (ev) | 5,266.0억 USD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 85.54x |
| PER (pe) | 177.68x |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 15.3% > 10%
- [watch] receivables_gap (C:receivables_gap): FY2024 매출채권 증가율 - 매출 증가율 28.9% > 15%
- [watch] dilution (C:dilution): 희석 주식 수 연 7.5% 증가 > 3%

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 30% | 126.1억 USD | 23.0% | 35% | 20x | 39.58 | 24.58 | -28.3% |
| 기본 | 45% | 205.0억 USD | 35.6% | 50% | 40x | 156.42 | 97.12 | -5.6% |
| 강세 | 25% | 301.2억 USD | 46.4% | 55% | 50x | 312.65 | 194.13 | +8.4% |

확률 가중: 주당 가치 160.42 · IV 99.61 · 기대 연 수익률 -5.1% (C:expected_irr) · 손실 확률 75% (C:p_loss) · 현재 주가 208.67

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +30.4% · 마진 변화 +1.3% · 멀티플 변화 -36.7% · 주식 수 변화 -2.5% · 현금 축적 +1.7% = -5.8%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -14.5% | -10.1% | -6.4% |
| +0%p | -10.3% | -5.6% | -1.7% |
| +5%p | -6.1% | -1.1% | +3.1% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 79.7억 USD | 47.5% | 37.9억 USD | 26.3억 | 132.0억 USD |
| FY2027 | 113.1억 USD | 48.2% | 54.5억 USD | 27.0억 | 186.5억 USD |
| FY2028 | 144.8억 USD | 48.8% | 70.6억 USD | 27.7억 | 257.1억 USD |
| FY2029 | 175.2억 USD | 49.4% | 86.5억 USD | 28.4억 | 343.6억 USD |
| FY2030 | 205.0억 USD | 50.0% | 102.5억 USD | 29.1억 | 446.1억 USD |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- base 시나리오 매출 성장: 연 35.6% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 46.4% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=4.55x, revenue_5y=6.73x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=94.1억 USD
- 애크먼 case={"from": "base"}: price=208.7, leveraged=아니오, intrinsic_value=97.1, mos=-114.9%

### 계산 경고

- 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-08-04 | [10-Q](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000041/pltr-20260630.htm) |  |
| S2 | filing | 2026-08-03 | [8-K 실적 발표 IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000039/pltr-20260803.htm) |  |
| S3 | filing | 2026-06-09 | [8-K](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000033/pltr-20260603.htm) |  |
| S4 | filing | 2026-05-05 | [10-Q](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000028/pltr-20260331.htm) |  |
| S5 | filing | 2026-05-04 | [8-K 실적 발표 IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000026/pltr-20260504.htm) |  |
| S6 | filing | 2026-04-24 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000019/pltr-20260423.htm) |  |
| S7 | filing | 2026-02-17 | [10-K](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm) |  |
| S8 | filing | 2026-02-02 | [8-K 실적 발표 IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000004/pltr-20260202.htm) |  |
| S9 | filing | 2025-11-04 | [10-Q](https://www.sec.gov/Archives/edgar/data/1321655/000132165525000131/pltr-20250930.htm) |  |
| S10 | filing | 2025-11-03 | [8-K 실적 발표 IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1321655/000132165525000130/pltr-20251103.htm) |  |
| S11 | filing | 2022-02-24 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1321655/000119312522050913/0001193125-22-050913-index.htm) |  |
| S12 | filing | 2025-02-18 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1321655/000132165525000022/0001321655-25-000022-index.htm) |  |
| S13 | filing | 2025-05-06 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1321655/000132165525000066/0001321655-25-000066-index.htm) |  |
| S14 | filing | 2024-02-20 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1321655/000132165524000022/0001321655-24-000022-index.htm) |  |
| S15 | filing | 2023-02-21 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1321655/000132165523000011/0001321655-23-000011-index.htm) |  |
| S16 | filing | 2025-08-05 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1321655/000132165525000106/0001321655-25-000106-index.htm) |  |
| S17 | filing | 2023-05-09 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1321655/000132165523000044/0001321655-23-000044-index.htm) |  |
| S18 | news | 2026-09-28 | [Bull of the Day: Palantir Technologies (PLTR) - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxOWjl0VWFOaU5ENWpKMEpwV18xcXVWUWpJOFZMcGpxX05QdWQtTHFjdW4yOU1LX3VHSkpiM0xQejNOcTFVLWR5TmNlM2ZabU0xY3FjUjUtWVBJWUtDNTFNazBaaE1hUW5NVVdpSWhHY0dQdXBpczVnUTBheFNWd3pwYzk2eHVjQ01DUzMxbjNpcm1wbHp1VUhLWFZDQ0dTVkh1V1E?oc=5) | Yahoo Finance |
| S19 | news | 2026-09-02 | [Peter Zaffino to Join Palantir Technologies as Global Head of Financial Services - Palantir](https://news.google.com/rss/articles/CBMiygFBVV95cUxQUjlKNlNGby0ybjlHdENGekpvYnVjOGRqUGJ5Xzl0Sm9SWU5GOFRKTVhVN05JZ1Ezd2E3YWNMNGJ5d2pObHdnTS1wZld1NTVLN0k4SElBSFladk1HdThaZ0ItVTltWHVSSnU0T1lIbjQyeWhORDFVVEt3cGNPVnlvUG5UWmUwVWRPUm5OcnIwVzg0NGt1cUEyV0JKQ3hjZHRDRm14UVM3Wm1QXzhJV3RIMGV0NXpCYVZ4LWJMMWZPazV1cFlpSXNGZ3FB?oc=5) | Palantir |
| S20 | news | 2026-08-06 | [Why $370bn tech group Palantir pays 1.4 percent tax rate: Report - Al Jazeera](https://news.google.com/rss/articles/CBMipAFBVV95cUxOcmtBTFEwT09QS0hTa0diSmNLN1NXNTlvUFlyYjVDb28yWk1rWkdpaE9LNjhYbTRWckY4TVlJcnVkMXpUMFc1LTEtajBGMmdZQkNPcDVfVktBZl81eFBfc3hYVkpIQ183ZU9GZVhBd2dmdWg1dEE0cjlpaUtOcGJmTkFYZTZiLUFETHZPSG80elFtSFdiZHktNjNPdzRCVlFaZlZOTtIBqgFBVV95cUxPZ1pGV01wRGFZNXBVZHZLUWRmX0Z5a0ZFU2d3NElxZmNtUkRRcngzZFBzWnc2TFVURTY1dmpPSktVdV9qSFM4TUZxOXl0dF9FVUY1YnVaUFBEeHJlb2I1cVUyTW8tdVZKMThsS0dJOGtDQTVUVlI2bkh6WmE4SWxmZktCQUQ3Ull3QW0wMWlZYmZEMzlTTnJGVGVSejJTZTJiX1B6WXlWRHhSdw?oc=5) | Al Jazeera |
| S21 | news | 2026-09-07 | [Palantir Stock Could Make a Dramatic Move Over the Next Year (Hint: It Implies a Big Move) - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPRVB2Q0lnekllaG9jd0NDWWp4YlFPZXBjSUhDLUp6MFV2NGhRX2FPdVNwZU5vXzNRc3NoWjE3YjdVX1VJRnJLQ3NYUVIzdmwzdnVkVW8xYzljTldrWEFCbzhNRUlkSDRKaHZBZmh6eWEwSk1aWDNwU09MVVhRZ3JhN04yUHZqWU5LeWFPcVFwLWg5QVEtR1FkNw?oc=5) | The Motley Fool |
| S22 | news | 2026-09-17 | [Palantir Technologies (PLTR) AI Deal Rush Meets A Fair Value Debate - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQdVRaQ05mTG1zNU9FYmFOLXJ3RkMxX1daRnMwaFNZdGFQeWc0OFpQaWJZWU41am54NmxwVTZFMk5OenMzc1J3U0lwa1BSbUN2TGEwVkRveHpNZER3LTdJQ3BkTjdWSHlSNVJSZVhaWlFTV2h6T3dpbUp3ajZyc1gwWjY5cU9hSURRUC0tZmRldy1VenJNeDhrTjBYVkdSSTdp?oc=5) | Yahoo Finance |
| S23 | news | 2026-09-10 | [News Summary: - Palantir](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQMHNoT2FCYmZ4VEtQNHhiM1hrMGktZjQ3YlZjdjJoYWhqV2NrQlVkYlcxME9sd2RfRWNUemhxSzE0YWp3T3o2bjRZdThjMWFjVDFiOV9LWU03YlE1dUxwSlM5cE4tSWlaR3RnLUdHVEpnWGRNLVdWMnpoWFBuRGJaQmhvMnhNblBKRHVzNEFhNGtWNlFpQVpYbXFFVVZKTjliQi1mRlNyM3ozVHlMQm5ZbDkxRnRBamZTUzc0T0l2UmFiZw?oc=5) | Palantir |
| S24 | news | 2026-08-16 | [Where Will Palantir Stock Be in 2030? - The Motley Fool](https://news.google.com/rss/articles/CBMihgFBVV95cUxQdlpqdV83STg2SFNiS2pDT1dYeEh3NmFQRWt5MFRhQTFTSHBkeWZFXzB2UVBkMGsySXliYXVJZnByU1pxZFF0SmlKcC1HRWlEcE9WOHFkcWNZLXF6ZHc2S2dRN0J2NWZyczQxTnN4ck5kVUhjdDF6RmVrS3NCTHp4cl9Ob2ZPdw?oc=5) | The Motley Fool |
| S25 | news | 2026-09-02 | [Palantir Technologies (PLTR) Could Be 5% Overvalued On Peter Zaffino Hire - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQckNnM2lqbFJxeHRMX2FSZmdrOWZoaEUycV83c21ka0VXNDVnX0ZHYnNPTkJsVzJ5UlJUZEtGcmVFZ3paNmc2TWxKemFRdXJkRGJoSzEySEpCYXcwZjJOODI1QmRFdTk5UG1zVnozN25qcm5QZWFUNjF6TmhhajBjZjhlbi1EcWlucXFLYXdCODlpWEk4RUotdHBTUGN2TFh3?oc=5) | Yahoo Finance |
| S26 | news | 2026-09-08 | [Palantir and Nebius Partner to Deliver a Complete Sovereign AI Stack to Palantir Customers - Palantir](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOdmFld2JjZEoxbldQVGZGUE9ZZVRvd2I1LWhXcV93YXAtNlo1R1IwNGVVU0dCQ1dtMVk0WmpxTGdSTVNjYXBtc1ZDQVJzVFpMM1FocTN2clQ4NlN1N1pqVTNITmV6Rnl6Sk1RUzdQdzA0OFhCTmxZdHJBOEc4YnJjdS1VbEdEUWRlV1FrNjdTRWtZZDdCdDlPTGFUOUVlMExFa0d2cC1GSUdyTzdhcmttVVFiRFdLVFRvRERFUVNKYmR0dFJYUWhqWEFxS0tIdUN6dlJkY0dUUQ?oc=5) | Palantir |
| S27 | news | 2026-09-28 | [Palantir Stock Falls as Sovereign AI Gains an External Guardrail - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxOSXRiUnZMQ0xiTjE0dktzakxGYVpJeWtNMC1ZQ2pXd1JRU0Q0c0JtNzZqS3RoOUFYQ21LVzlUY3dyUS13cjJXTGpiOTZ1YmRHWm52XzdxLUdsMXVTSUlobzYybGkwVzBhWk55TjZoLUlkTFB2TEFSbDYwd1Z1OVJZVDBJRmlPTlh4U0hsZ0VVWWtBaDJidW1PX3dOYUl5UQ?oc=5) | Yahoo Finance |
| S28 | news | 2026-09-03 | [PwC and Palantir Expand Strategic Alliance to Help Organizations Scale Enterprise AI - Palantir](https://news.google.com/rss/articles/CBMizwFBVV95cUxPdkZyTUlfQkZLY2NaVlBHMXFLbWZMTVpWUEJKY1BkT0xpemFzYkZoZnIzZF9FMUJNSkZyQUNibUJSSERqbmpGSERHQy1jWGZxUjc5ekJZLXB1R05PeHBDRml0RjUzYVBDUm1Sa3MyM3RBLUt5YmtHZzNhVl82UnBOb0h3bGUzSDJvWjI0dWRFYnRHVjRpUmV0WDk1LThxQ21BR0dHci1GZUtJeGk5b0U1NkNubjFMc0d6SzYwNlVEbmdBaEg1Zy03Tm5RQ3JoNUE?oc=5) | Palantir |
| S29 | news | 2026-08-19 | [Is Palantir Technologies (PLTR) Overvalued As Revenue Growth And 2026 Outlook Jump? - Yahoo Finance](https://news.google.com/rss/articles/CBMirwFBVV95cUxPeHR1OVhsdmN6N0h5ZDctNG1zUVBDOWIwY3pSTWl2ZWpMR0xuSWJaODB2SEhwNjlTS25lbkxkaGxybUdCSUhYMFJ6NkptVXlSU0VIeV9sQk1XSXQ3RndIczJkeFdQOUp1c1FPQ3JxQVVPSG5GSTVQR2drZmdfVU1WcWlxdDVOS2lTd202eFZuaWY0NTZrMVNiaGx6M2w0Snlad3J4ZC0xd3BCZFNMdUxn?oc=5) | Yahoo Finance |
| S30 | news | 2026-09-10 | [Palantir Customers Set New Standard for AI at AIPCon 11 - Palantir](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPSXdYeG95dS11cVFwOW8tUFROdHFiTktEOFg2TGRIZ0h0SkE4dTdENjE3YVhZbFhUY0IwRVZqNks0Z1hYUkVmRmNPZEdyaFVlam5zUGQ0Q09vLWduUEhpZmZ5aGN6ZXNSMUU2a0cxZXdNdVFOTVNBazlyQkdMeEM0TGp5TVdaeFEwc0NJMEp5eVR3eGgwMjBGSkpyTlBoa2NMWUtiM2J5Uk0?oc=5) | Palantir |
| S31 | news | 2026-09-01 | [Palantir to Deliver Eight TITAN Systems to the U.S. Army - Palantir](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNT1RTaFhpaURiVTJZVXZYSVpLWUg3c0ZoblZlRms3S2Y0YWpocW1zYjdsRy1ZYVZSNDZLNGpycFRqVFBJLW0zd0JoV1RxN0JGZmtUcjhmT2w4WHdfREFrTjVlQUgtakU4MG5sSXV5X1dfMElDci1IXzJvdUUtVFVscW9Hc0FDa2V6X0pxNGZ4bkdOWV9Fam5TM3FNTnBjR29UamVRSVhlVEdsZw?oc=5) | Palantir |
| S32 | news | 2026-09-03 | [What Does Palantir Technologies (PLTR) Winning Army Work Mean For Its AI Growth? - Yahoo Finance](https://news.google.com/rss/articles/CBMipgFBVV95cUxNeHBUelh3bGFrMlFacU9PVE0zXzBQSTVQR2pfQkNoa19BN1ZSQ1J4OTJtNGZSaTY4SmZNX2U3THZMRmRvLVpxMDR1LWwzeHkteXJOaERpVFl0UGp2dUdSYXJnOW9EdFJNck51OTlUbTdMWUt3T0h6R2YwRTgxcXdMc1ZkbHpNRzgtX2czZ195bFpXZUFxUjBOZ0ZyU2NhUDVGRG01aE13?oc=5) | Yahoo Finance |
| S33 | news | 2026-09-10 | [Palantir IR - Palantir](https://news.google.com/rss/articles/CBMingJBVV95cUxOZGo5YTdTM011UXg0UGxfR3N1VGtjQl9TTFdTYTZnb1dhVFY0RVhBVGxoeW1ZVXpGTkdpM25FYXcwSTZ6aDFqZXQxRm5rdVNkeHBMTmtxLXZGN3hEbGFyenR2Z1NEekQxR2NWSEpvUjdjb0JtckZldHd5UjdNTnJoQUtCV2dTSTZ0aUROSFVsWUJqLUdGdnNwWGxzb3hBSTJuREswZFFwM2t2dkJQdkRNZW9GNldVQzIxYXhWT0d6ZDNiTE1WVnFTY1BsaFNQVXQ0WkpRMmtjRmxXeWhMUVZNRjFKWms3VjE3aUUzVk5iajBEQ3lLVnpPTFFxNzF2M2xuTXREOHR2ajYtQTFsSFVOS1RVWXliT05UckJ0clFn?oc=5) | Palantir |
| S34 | news | 2026-09-18 | [Jim Cramer Says His Palantir Technologies Inc. (NASDAQ:PLTR) Price Target Is $250 - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxQbVNCVVA2WnA0ZlF2cGdPSkNaLXpHSHdWNWMwSzNjRDNRSXlhRkJEejZrMlFSWlFSdzVkR3dMRkF4cmhhUS0ybXBUVmt4QWkxcC1yYks5Q0o0Ulpna0ctLVNUR3lkOFB3VE1LSGs4djlya0c3THg5MDhrM0NPa3ZVcEdFMHM1Rzh3Q29KbVJ0dVhpbE5RRFFBNnY1cUhuekxjdWo2SA?oc=5) | Yahoo Finance |
| S35 | news | 2026-08-28 | [NVIDIA (NVDA), Palantir Technologies (PLTR), and the AI Achilles’ Heel: Steve Eisman’s Concentration Warning Explained - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxONzd2MEZiSjhkQ0FEbEtSWVMxNEtHWnpJU21LUzFYcHdDN3M1TnkyWXJhdVBrU0NpTTlnX0gzNF9waVBIejhnSFltOXpNU0hzZkNJZVdzdnNfdnlUNmhfWjQ5MHJMMmNWdzZkcGNDelFlNDREdUpkbDNNTldCNjdCZGQyR0lUWFlZNUx4X21Ec3RON0E1d0dNc2VyZjlkRWNVYU9wUg?oc=5) | Yahoo Finance |
| S36 | news | 2026-09-20 | [Palantir Technologies (PLTR) Unveils Alliance Push Across AI Supply Chains And Cyber Defense - Yahoo Finance](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNRWZiTU9pNjl4WUNQR2NsRDVfWFA2QWpVX0dILTZvMndEeWw3MVBfcmJOWC16QlFqellGVmhSbmF3aTBkSmRZZFBqeXVQUS1hOTZBVEtlZWFqbl9TTDdCdzZYU1B4U0EwQXJrOGhKM0dXS2cyRGNtc2tNUndXN3ZtaGpRWEo3RWNkb2ttVVBLdnd6YU96Z241amYwRWRIdGxQdTVabmREUENfdnc?oc=5) | Yahoo Finance |
| S37 | news | 2026-10-14 | [Palantir Technologies Inc. (PLTR) Registers a Bigger Fall Than the Market: Important Facts to Note - Yahoo Finance](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNbkRGM3E0bTFSM1R2TkZtZG1fRXdvLW5KbUtiOUxNbDlWWnNZaWhrcEtaRFFqbThocGJidklodTF6cDRBYWRWRGhLU1B6SlVvd0hJQVVaOG8zZlNDcGxzLUw0N0N3VHBwdnVTTno2ejhHZ3pYX2hXZ3JxRnNPLVZaeTFCSUdUZmJvOFRBUnBXRU9BVldLbDRTRHhxejhWODZEbUNjYTN2djQ?oc=5) | Yahoo Finance |
| S38 | data | 2026-10-13 | [Palantir Stock News (Oct 14, 2026): PLTR Falls 0.2% to $208.67](https://www.heygotrade.com/en/news/palantir-pltr-stock-news-october-14-2026/) | 2차 자료(HeyGoTrade). 2026-10-13 나스닥 종가 $208.67, 전일 대비 -0.16%로 보도. 52주 범위 $106.37~$212.94. 같은 검색에서 10-09 종가 209.05, 10-07 종가 194.12로 나온 자료도 있다. 기준일 10-18의 직전 거래일 종가는 확인하지 못했다. |

# Palantir Technologies (PLTR) 리서치 보고서 — 기준일 2026-10-18

**반대 우세** — 찬성 1 · 반대 2 · 보류 0 · 확신 가중 점수 -0.27 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장 내재: 매출 10년 연 34.5% (FCF 마진 52% 수렴 가정) · 기본 시나리오: 5년 연 41.0%
- 시장이 반영한 것: 현재 가격은 EV 대비 FCF 수익률이 0.7%(C:fcf_yield)이고, 역DCF로 보면 FCF 마진 30%에 수렴하더라도 10년간 매출이 연 42.0% 늘어야 한다(C:implied_cagr@m30).
- 우리가 다르게 보는 점: 단기 펀더멘털(가이던스 상향, 미국 상업 가속)은 실제이고 기본 시나리오도 이를 따른다. 다만 5년 성장 경로가 시장 내재 성장에 못 미치고 출구 배수가 압축되므로, 기본 시나리오 가치는 주가와 비슷하거나 낮다. 즉 사업은 강하지만 가격이 이를 이미 반영했다고 본다. 컨센서스를 확보하지 못해 시장 전망과 어디서 다른지는 검증하지 못했다.
- 왜 우리가 맞는가: 역DCF가 요구하는 10년 40%대 성장은 기저율상 거의 달성된 적이 없다(기저율 표 참조). 반면 가격에는 이 가정이 들어 있다. 올해 성장이 계속 가속하더라도, 성장 감속과 배수 압축이 시작되면 이익이 늘어도 주가는 정체할 수 있다. [C:fcf_yield] [C:implied_cagr@m30] [F233] [F213]
- 촉매: 분기 매출 성장률 감속이 처음 확인되는 실적 발표(미국 상업 전분기 대비 성장률 둔화), 또는 다음 분기 가이던스 상향 폭 축소.
- 시점: FY2026Q3 실적(2026년 11월 초)부터 FY2027 가이던스 제시(2027년 2월)까지.

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **111.93** vs 주가 186.03 · 기대 연 수익률 **-0.6%** · 손실 확률 80%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 30% | 62.17 | 38.60 | -19.7% | 올해는 가이던스대로 가지만 이후 미국 상업의 계약 확대가 한 번에 꺼진다. 대형 AI 플랫폼과의 경쟁, 소버린 AI 규제, 정부 예산 지연이 겹치고 성장이 급격히 둔화한다. SBC 부담과 매출채권 증가로 FCF 마진 |
| 기본 | 50% | 178.06 | 110.56 | -0.9% | 올해 성장률은 상향된 가이던스(FY2026 매출 81.5억 달러 이상, F233)에 맞춘다. 이후는 미국 상업 잔여 계약가치(F240)와 100만 달러 이상 계약 수(F242)가 받쳐 주는 만큼 감속하되 높은 수준을 |
| 강세 | 20% | 362.93 | 225.35 | +14.3% | AIP 도입이 미국 상업 밖으로 퍼져 CEO가 말한 18개월 이상 현재 미국 상업 성장률을 유지한다(S43, 2차 요약). 미국 상업 매출이 전년 대비 +149%(F239)로 가속하는 흐름이 정부와 해외 대형 계약( |

## 3. 반증 조건 (thesis break)

- [자료 없음] 앤더슨: 미국 상업 매출이 직전 분기보다 줄면 성장 가설 훼손 — `us_commercial_revenue < 7.64e+08` (FY2026Q3)
- [자료 없음] 앤더슨: 이연매출이 직전 분기 아래로 줄면 선결제 수요 가설 훼손 — `deferred_revenue < 5.8e+08` (FY2026Q3)
- [수동 확인] 앤더슨: NRR·계약 잔액이 공개되면 성장 지속을 뒷받침하는지 수동 확인
- [자료 없음] 슬레이터: 이연매출이 이 수준을 넘으면 선결제 수요가 모델 기본 경로보다 강하다는 증거이므로 비중 0 판단을 재검토한다 — `deferred_revenue > 8e+08` (FY2026Q3)
- [자료 없음] 슬레이터: 분기 매출이 모델 기본 경로를 크게 웃돌면 가격이 요구하는 지속 기간에 대한 판단을 다시 한다 — `revenue > 2.5e+09` (FY2026Q3)
- [수동 확인] 슬레이터: 10-Q나 실적 발표에서 NRR·계약 잔액이 공개되어 단위경제가 입증되면 수동 확인 후 재평가
- [미충족] 애크먼: 주가 110달러 미만 — 기본 시나리오 현재가치(110.56달러) 수준으로 내려오면 재검토 — `price < 110`
- [수동 확인] 애크먼: 자본 환원 정책 발표 시 수동 확인
- [자료 없음] 레드팀: 미국 상업 매출 전분기 대비 성장률이 2분기 +28%에서 15% 미만으로 둔화 — 감속과 배수 압축 시작 — `us_commercial_revenue_qoq_growth < 0.15`
- [미충족] 레드팀: 미국 상업 TCV가 2분기 21.3억 달러 아래로 감소 — 신규 계약 모멘텀 꺾임 — `us_commercial_total_contract_value < 2e+09`
- [미충족] 레드팀: 매출채권이 FY2026Q2 14.9억 달러에서 18억 달러를 넘음 — 매출 성장 대비 수금 지연이 심화 — `receivables > 1.8e+09`
- [미충족] 레드팀: 분기 조정 FCF가 2분기 12.2억 달러 아래로 내려감 — 성장 약속 이행 실패와 마진 압박의 동시 신호 — `adjusted_free_cash_flow < 1e+09`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | revenue | FY2026Q3 | >= 2.16e+09 | 85% | 3분기 가이던스 하단(F237)을 넘기는지 본다. 못 넘기면 가이던스 신뢰와 기본 시나리오의 첫해 성장 가정이 함께 훼손된다. |
| K2 | revenue | FY2026 | >= 8.15e+09 | 80% | 연간 가이던스 하단(F233)이다. 기본 시나리오 첫해 82% 성장을 가정한 값으로, 약세 시나리오의 첫해 가정(78%)과 구분되는 지점이다. |
| K3 | us_commercial_revenue | FY2026Q3 | >= 9e+08 | 65% | 2분기 7.6억(F239)에서 전분기 대비 약 18% 늘어야 한다. 미국 상업 성장이 이어지는지, 감속 시점이 앞당겨지는지를 시험한다. |
| K4 | operating_income | FY2026Q3 | >= 1e+09 | 60% | GAAP 영업이익이 2분기 9.1억(F123)보다 늘어 고정비 레버리지가 이어지는지 본다. FCF 마진 52% 가정의 전제다. |
| K5 | deferred_revenue | FY2026Q3 | >= 6e+08 | 60% | 이연매출이 2분기 5.8억(F51)에서 계속 늘면 선결제 수요와 전환비용 가설이 유지된다. 줄면 약세 시나리오 쪽 신호다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.27 · 비중 참고값 0.0% (반대 우세 — 신규 비중 없음) · 슬레이터 시작 비중 0.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 2/5 실패 | founder_led=예, upside_10y=7.36x, revenue_5y=8.46x |
| 슬레이터 | 반대 → 반대 | 3/5 | ✓ | 1/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=0.0%, cash_survives=예, cash_min=94.1억 USD |
| 애크먼 | 반대 → 반대 | 4/5 | ✗ 단순·예측 가능한 사업이 아님; 안전마진 20% 미만 또는 계산 불가 | 2/5 실패 | simple_predictable=아니오, capital_markets_dependent=아니오, catalyst=없음, fcf_positive=예, net_debt_to_ebitda=-3.53x, intrinsic_value=110.6, mos=-68.3% |

- ⚠ 앤더슨: arguments[2] unsupported: FY2022 영업이익률 −8.5%는 인용에 없다. 10년을 버틸 수 있다는 결론도 자료에서 따라 나오지 않는다.
- ⚠ 앤더슨: arguments[4] unsupported: 최근 3년이 가속이었다는 근거로 FY2025 성장률 하나만 인용돼 있다.
- ⚠ 앤더슨: risks[1] unsupported: 출처 없는 숫자 37% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 앤더슨: arguments[1] leap: 미국 상업 매출은 +149%인데 RDV는 +124%다. 계약이 매출보다 더 빨리 늘었다는 결론은 TCV에만 해당한다.
- ⚠ 앤더슨: rebuttals[1] leap: 미국 상업 매출은 +149%이고 RDV는 +124%다. 계약이 매출보다 빨리 늘고 있어 고객이 떠나는 모양이 아니라는 결론은 TCV에만 맞다.
- ⚠ 앤더슨: arguments[2]: 인용하지 않은 근거의 숫자 8.5%(C:operating_margin@FY2022) — cites에 추가
- ⚠ 앤더슨: risks[1]: 인용하지 않은 근거의 숫자 41%(C:receivables_growth@FY2023·C:revenue_cagr@base) — cites에 추가
- ⚠ 슬레이터: risks[1] leap: 인용된 값은 매출 7.64억과 3분기 가이던스뿐이라, 이것만으로 미국 상업 성장이 가속 중이라고 단정할 수 없다.
- ⚠ 슬레이터: arguments[0] unsupported: FY2023 성장률 16.7%는 인용에 없다. FY2025 56.2%와 Q2 +93%는 일치한다.
- ⚠ 슬레이터: arguments[3] leap: −0.6%와 손실 확률 80%는 맞다. 하지만 성장 기여와 멀티플 압축의 상쇄, 2022년 구간과의 유사성은 인용에서 따라 나오지 않는다.
- ⚠ 슬레이터: rebuttals[1] unsupported: 출처 없는 숫자 37% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 슬레이터: risks[1]: 인용하지 않은 근거의 숫자 149%(S42) — cites에 추가
- ⚠ 슬레이터: arguments[0]: 인용하지 않은 근거의 숫자 16.7%(C:revenue_growth@FY2023) — cites에 추가
- ⚠ 슬레이터: rebuttals[1]: 인용하지 않은 근거의 숫자 34.4%(C:implied_cagr·C:implied_cagr@m52) — cites에 추가
- ⚠ 애크먼: arguments[3] unsupported: 없는 근거 인용: C:base_rate@implied
- ⚠ 애크먼: rebuttals[2] unsupported: 현재 마진 −68.3%와 약세 마진 40%는 인용한 자료로 확인되지 않는다. 주가와 기본 가치가 인용에 없다.
- ⚠ 애크먼: arguments[2] unsupported: 출처 없는 숫자 37% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: rebuttals[2]: 인용하지 않은 근거의 숫자 31.7%(C:operating_margin@FY2025), 52%(C:fcf_margin@base·C:implied_cagr@m15), 68.3%(C:mos@ackman) — cites에 추가
- ⚠ 애크먼: risks[0]: 인용하지 않은 근거의 숫자 149%(S42) — cites에 추가
- ⚠ 애크먼: arguments[2]: 인용하지 않은 근거의 숫자 34.4%(C:implied_cagr·C:implied_cagr@m52) — cites에 추가
- ⚠ 애크먼: risks[1]: 인용하지 않은 근거의 숫자 52%(C:fcf_margin@base·C:implied_cagr@m15) — cites에 추가
- ⚠ 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 레드팀 weakest[0] 검증 실패(unsupported): 출처 없는 숫자 37% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 레드팀 premortem[2] 검증 실패(unsupported): 출처 없는 숫자 69%, 1.4%, 9.2e+09 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 회계 품질 findings[3] 검증 실패(unsupported): 출처 없는 숫자 1.4% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[1] 검증 실패(unsupported): FY2021 SBC/매출 50.5%는 인용에 없다. 나머지 수치는 일치한다.
- ⚠ 사업·산업 findings[0] 검증 실패(unsupported): FY2022 영업이익률 −8.5%는 인용에 없다. FY2025 31.6%, 분기 영업이익, 47%는 일치한다.
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): 10년 34~42% 성장이 역사적으로 거의 달성된 적 없다는 진술은 근거가 없다. 기저율 표가 없다고 스스로 밝히고 있다.
- ⚠ 경영진·자본배분 findings[4] 검증 실패(unsupported): FY2021 SBC 7.8억과 희석 주식 수 19.2억·25.7억은 인용에 없다.
- ⚠ 회계 품질 flags[0] 검증 실패(unsupported): FY2021 SBC/매출 50.5%와 임계값은 인용에 없다. 15.3%, 32.0%, 14.2억은 일치한다.
- ⚠ 회계 품질 findings[4] 검증 실패(unsupported): 출처 없는 숫자 9.2e+09 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 경영진·자본배분 findings[5] 검증 실패(unsupported): FY2023까지 자사주 매입이 0이었다는 내용은 인용에 없다. 나머지 수치는 일치한다.
- ⚠ 사업·산업 findings[5] 검증 실패(unsupported): FY2022 DSO 49.5일은 인용에 없고, 연초 이후 계속 늘었다는 것도 FY2026Q2 값 하나로는 알 수 없다.
- ⚠ 회계 품질 findings[0] 검증 실패(unsupported): 출처 없는 숫자 1.29 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 레드팀 premortem[1]: 인용하지 않은 근거의 숫자 153%(S42), 5e+06(S42) — cites에 추가
- ⚠ 사업·산업 moat[1] 검증 실패(unsupported): FY2021 총이익률 78.0%는 인용에 없다. FY2025 82.4%와 매출 15.4억→44.8억은 일치한다.
- ⚠ 레드팀 weakest[2] 검증 실패(unsupported): 전년 SBC 1.6억은 인용에 없다. FCF 마진 46.9%와 SBC 차감 31.7%는 인용값으로 계산된다.
- ⚠ 사업·산업 findings[6]: 인용하지 않은 근거의 숫자 40%(C:fcf_margin@FY2024·C:fcf_margin@bear) — cites에 추가
- ⚠ 회계 품질 findings[5] 검증 실패(unsupported): 영업권이 총자산 대비 미미하다는 진술에 영업권 수치가 인용되지 않았다. 부채 0과 총자산 116.8억만 있다.
- ⚠ 모델러 variant 검증 실패(unsupported): 기저율 표를 참조하라고 했지만 인용 자료에 기저율 표가 없고, 10년 40%대 성장이 거의 달성된 적 없다는 근거도 없다.
- ⚠ 레드팀 premortem[0] 검증 실패(unsupported): 출처 없는 숫자 37%, 5.6 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 회계 품질 flags[1] 검증 실패(unsupported): DSO 73.2일, 문턱 15%p, 순이익 대비 영업현금흐름 비교는 인용에 없다. 28.9%p, 85.0일, 매출채권, 이연매출은 일치한다.
- ⚠ 사업·산업 moat[2]: 인용하지 않은 근거의 숫자 1e+06(S42), 5e+06(S42) — cites에 추가

## 앤더슨 — 찬성 (3/5)

> Palantir는 멱법칙 후보의 모양을 갖췄다. 매출 성장이 FY2023 16.7%에서 FY2025 56.2%로 가속했고(C:revenue_growth@FY2025), 2026년 2분기 미국 상업 매출은 전년 대비 +149%였다(F239, S42). 총이익률은 80%대를 유지하고 FCF 마진은 46.9%다. 성장하면서 자본이 거의 들지 않고 부채가 없다는 뜻이다. 현재 가격은 매출이 연 40% 이상 성장하는 10년을 요구하며(C:implied_cagr@m30) 기본 시나리오 기대수익률은 -0.9%다. 그러나 나는 평균이 아니라 오른쪽 꼬리를 산다. 강세 시나리오의 10년 주당 가치는 현재 주가의 7.36배, 5년 매출은 8.46배로 5배 문턱을 넘는다(C:upside_10y@anderson, C:revenue_5y@anderson). 이런 꼬리는 기저율상 드물고 확률도 낮다는 사실을 숨기지 않는다. 그래서 확신은 3으로 둔다. 비싸다는 반론은 현재를 재는 잣대다. 성장 가설이 훼손될 때만 판단을 바꾼다.

*이전 판단 대비: 직전 판단은 abstain(확신 3)이었다. 이번에는 같은 근거 위에서 10번 질문의 계산값(C:upside_10y@anderson, C:revenue_5y@anderson)이 5배 문턱을 넘고 성장 가속(C:revenue_growth@FY2025)과 미국 상업 계약 확대(F240, F241)가 확인되어 꼬리에 거는 쪽으로 판단했다. 주가도 10-13 종가 208.67(F212)에서 10-16 종가 186.03(F213)으로 내려 진입 가격이 나아졌다. 다만 기본 시나리오 수익률이 음수(C:expected_irr)라 확신은 3에 머문다.*

**논거**
- 성장이 감속이 아니라 가속 중이다. 연 매출 성장률이 FY2023 16.7%, FY2024 28.8%, FY2025 56.2%로 올랐고 2026년 2분기 매출은 전년 대비 +93%다. 큰 기업이 이 속도로 가속하는 것은 수확체증의 전형적 흔적이다. [C:revenue_growth@FY2023] [C:revenue_growth@FY2024] [C:revenue_growth@FY2025] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- 미국 상업 부문이 선행 지표다. 2분기 매출이 전년 대비 +149%, 잔여 계약가치가 +124%, TCV가 +153%로 매출보다 계약이 더 빨리 늘었다. 매출이 계약을 쫓아가는 구조라 성장 지속의 가시성이 높다. 다만 근거는 보도자료 요약이다. [F239] [F240] [F241] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- 재투자 여력이 구조적으로 크다. 영업이익률이 FY2022 -8.5%에서 FY2025 31.6%로 올랐고 FCF 마진은 46.9%다. 설비투자는 미미하고 부채는 없다. 성장에 외부 자본이 필요 없으니 희석과 재무 위험 없이 10년을 버틸 수 있다. [C:operating_margin@FY2025] [C:fcf_margin@FY2025] [C:capex@FY2025] [F245]
- 10번 질문, 5배가 되는 길이 보이는가. 내 강세 case(매출 성장 5년 평균 53.3%, FCF 마진 55%, 출구 P/FCF 45)는 10년 뒤 주당 가치를 현재 주가의 7.36배로 만든다. 이 경로의 핵심 전제는 AIP가 미국 상업을 넘어 정부와 해외로 퍼지는 것이다. Army TITAN 납품과 소버린 AI 파트너십이 그 초기 흔적이다. [C:upside_10y@anderson] [C:revenue_cagr@bull] [C:fcf_margin@bull] [S31](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNT1RTaFhpaURiVTJZVXZYSVpLWUg3c0ZoblZlRms3S2Y0YWpocW1zYjdsRy1ZYVZSNDZLNGpycFRqVFBJLW0zd0JoV1RxN0JGZmtUcjhmT2w4WHdfREFrTjVlQUgtakU4MG5sSXV5X1dfMElDci1IXzJvdUUtVFVscW9Hc0FDa2V6X0pxNGZ4bkdOWV9Fam5TM3FNTnBjR29UamVRSVhlVEdsZw?oc=5) [S26](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOdmFld2JjZEoxbldQVGZGUE9ZZVRvd2I1LWhXcV93YXAtNlo1R1IwNGVVU0dCQ1dtMVk0WmpxTGdSTVNjYXBtc1ZDQVJzVFpMM1FocTN2clQ4NlN1N1pqVTNITmV6Rnl6Sk1RUzdQdzA0OFhCTmxZdHJBOEc4YnJjdS1VbEdEUWRlV1FrNjdTRWtZZDdCdDlPTGFUOUVlMExFa0d2cC1GSUdyTzdhcmttVVFiRFdLVFRvRERFUVNKYmR0dFJYUWhqWEFxS0tIdUN6dlJkY0dUUQ?oc=5)
- 시장이 과소평가하는 지점은 꼬리의 크기다. 역DCF는 마진이 30%로만 수렴해도 매출이 연 42.0% 성장해야 한다고 말한다. 이것을 '불가능'이 아니라 '이미 반영'으로 읽는 것이 시장의 평균적 시각이다. 그런데 이 회사의 최근 3년 성장 궤적은 가속이었고, 가속하는 기업의 10년 경로는 선형 외삽보다 넓게 퍼진다. [C:implied_cagr@m30] [C:revenue_growth@FY2025]

**사전 부검**
- 사전 부검 1: 미국 상업 계약 확대가 한 번에 꺼지고 성장이 급감속하면 출구 배수가 성숙 소프트웨어 수준으로 압축된다. 약세 시나리오 연 수익률은 -19.7%이고 현재 P/FCF가 142배라 배수 압축의 낙폭이 크다. 이는 성장 가설 자체를 깨는 시나리오다. [C:irr@bear] [C:p_fcf] [S27](https://news.google.com/rss/articles/CBMingFBVV95cUxOSXRiUnZMQ0xiTjE0dktzakxGYVpJeWtNMC1ZQ2pXd1JRU0Q0c0JtNzZqS3RoOUFYQ21LVzlUY3dyUS13cjJXTGpiOTZ1YmRHWm52XzdxLUdsMXVTSUlobzYybGkwVzBhWk55TjZoLUlkTFB2TEFSbDYwd1Z1OVJZVDBJRmlPTlh4U0hsZ0VVWWtBaDJidW1PX3dOYUl5UQ?oc=5)
- 사전 부검 2: 기본 시나리오조차 5년 수익률이 -0.9%다. 매출이 연 41%로 성장해도 멀티플 변화가 수익률을 -37.0% 깎는다. 성장이 사실이어도 가격이 이미 반영했다면 이익이 늘어도 주가는 제자리일 수 있다. 내 철학과 달리 이 위험은 '경로의 소음'이 아니라 구조적이다. [C:irr@base] [C:expected_irr] [C:p_loss]
- 사전 부검 3: 매출채권이 매출보다 빨리 늘어 DSO가 85.0일까지 길어졌고 SBC 부담과 연간 희석도 높다. 대형 계약의 청구 구조 때문이라면 무해하지만, 수요의 질이 나빠진 신호라면 FCF 마진 가정이 무너진다. 1차 원문 대조는 아직 하지 못했다. [C:dso@FY2025] [C:sbc_to_revenue@FY2025] [C:dilution]

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 현재 가격이 기본 시나리오 현재가치를 넘고 손실 확률이 80%라는 점이다. 이것은 맞는 계산이다. 그러나 이 계산은 세 시나리오를 확률 가중 평균으로 합친 값이다. 나는 평균을 사지 않고 꼬리를 산다. 내 강세 case의 10년 주당 가치는 현재 주가의 7.36배이고 5배 문턱을 넘는다. 강세 시나리오 연 수익률도 양수다. 현금흐름 범위가 넓어 단순하지 않다는 지적은 멱법칙 기업의 속성을 결함으로 읽은 것이다. 범위가 넓다는 것은 오른쪽 꼬리가 두껍다는 뜻이기도 하다. 다만 5배 문턱 통과가 승률이 높다는 뜻은 아니라는 점을 인정한다. [C:p_loss] [C:upside_10y@anderson] [C:irr@bull]
- → 슬레이터: 슬레이터의 가장 강한 논거는 NRR·CAC·이탈률이 없어 단위경제가 입증되지 않았다는 점이다. 고객 단위 지표가 비어 있는 것은 사실이다. 그러나 증거가 없는 것과 반대 증거가 있는 것은 다르다. 같은 분기에 미국 상업 매출은 전년 대비 +149%, 잔여 계약가치는 +124%, TCV는 +153%였다. 계약이 매출보다 빨리 늘고 있어 고객이 떠나는 모양은 아니다. 증거가 쌓일 때까지 시작 비중 0으로 기다리면 가장 가치 있는 구간을 놓칠 수 있다. 근거가 보도자료 요약이라는 한계는 인정한다. [F239] [F240] [F241] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- → 레드팀: 레드팀의 첫째 부검인 멀티플 붕괴는 성장 가설이 맞아도 올 수 있다. 기본 시나리오에서 멀티플 변화가 수익률을 크게 깎고, 현재 P/FCF가 높아 압축 시 낙폭이 크다. 이것은 경로의 소음이 아니라 구조적 가격 위험이다. 반면 둘째 부검인 미국 상업 수요의 일시성은 성장 가설 자체를 깬다. 이 둘을 구분해서 감시한다. 첫째는 내가 감수할 위험이고, 둘째는 내가 매도할 이유다. 둘째의 선행 신호는 미국 상업 TCV와 이연매출 감소이며, 둘 다 내 반증 조건에 넣어 두었다. [C:irr@base] [C:p_fcf] [F241] [S27](https://news.google.com/rss/articles/CBMingFBVV95cUxOSXRiUnZMQ0xiTjE0dktzakxGYVpJeWtNMC1ZQ2pXd1JRU0Q0c0JtNzZqS3RoOUFYQ21LVzlUY3dyUS13cjJXTGpiOTZ1YmRHWm52XzdxLUdsMXVTSUlobzYybGkwVzBhWk55TjZoLUlkTFB2TEFSbDYwd1Z1OVJZVDBJRmlPTlh4U0hsZ0VVWWtBaDJidW1PX3dOYUl5UQ?oc=5)

**인정한 점**
- 애크먼: 기대 연 수익률이 음수이고 손실 확률이 80%라는 계산은 반박하지 않는다. 그래서 확신을 4나 5로 올리지 않고 3에 둔다.
- 슬레이터: 고객 단위 증거가 없고 근거가 2차 요약이라는 점을 인정한다. 이 한계 때문에 큰 비중의 근거로 삼지 않는다.
- 레드팀: 기본 시나리오에서도 멀티플 압축이 성장의 대가를 상쇄한다는 점을 인정한다. 사업이 맞아도 주가가 제자리일 수 있는 가격 위험이다.


## 슬레이터 — 반대 (3/5)

> 사업의 증거는 실제로 쌓이고 있다. 매출 성장이 FY2025에 56.2%로 올랐고, 2026년 2분기 매출은 전년 대비 +93%, 미국 상업 잔여 계약가치는 62.4억 달러다. 생존은 문제가 아니다. 부채가 없고 현금이 충분하다. 반대하는 이유는 가설이 아니라 가격이다. 현재 가격은 FCF 마진이 30%로 수렴해도 매출이 10년간 연 42.0% 늘어야 성립한다. 기본 시나리오의 5년 매출 연성장은 41.0%인데도 기대 연 수익률은 -0.6%다. 고객 단위 증거(NRR·CAC·이탈률)가 없어 단위경제는 아직 입증되지 않았다. 입증되지 않은 가설에 1%를 넘게 걸 수 없고, 입증된 가설이어도 기대수익률이 음수인 구간에서는 키울 근거가 없다. 증거가 쌓이면 다시 본다. 지금은 시작 비중 0이다.

*이전 판단 대비: 직전 판단과 같은 입장·확신이다. 10월 중순 주가 변동(208.67 → 186.03)은 가설이 아니라 가격의 변화이므로 판단을 바꾸지 않는다.*

**논거**
- 실적은 진짜다. 매출 성장이 FY2023 16.7%에서 FY2025 56.2%로 가속했고, 2026년 2분기 매출은 전년 대비 +93%였다. 이 점은 반대 논거가 아니라 인정할 사실이다. [C:revenue_growth@FY2025] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- 고객 단위 증거가 비어 있다. 미국 상업 잔여 계약가치 62.4억 달러와 TCV 21.3억 달러는 계약 확대를 시사하지만, NRR·CAC·이탈률은 확인되지 않았고 근거도 보도자료 요약이다. 계획이 아니라 실적이어야 키운다. [F240] [F241] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- 지속성의 요구가 크다. 역DCF는 FCF 마진 30% 수렴에도 10년 연 42.0% 성장을 요구한다. 기본 시나리오 자체가 5년 연 41.0% 성장이라는 드문 가정이며, 기저율 표가 없어 이 지속성을 검증하지 못했다. [C:implied_cagr@m30] [C:revenue_cagr@base]
- 높은 성장을 그대로 반영해도 수익이 나오지 않는다. 기대 연 수익률은 -0.6%이고 손실 확률은 80%다. 기본 시나리오 수익률 분해에서 매출 성장 기여를 멀티플 압축이 상쇄한다. 좋은 회사를 너무 비싸게 산 2022년의 구간과 같은 구조다. [C:expected_irr] [C:p_loss] [C:irr@base]
- 생존은 쟁점이 아니다. 부채가 없고 현금이 충분해 외부 조달 없이 계획을 실행한다. 그래서 반대 사유는 자본 의존이 아니라 가격이 요구하는 지속 기간이다. [F245] [C:net_cash]

**사전 부검**
- 내가 틀렸다면 성장 가속이 모델의 기본 경로보다 오래 간다는 뜻이다. CEO는 18개월 동안 현재 미국 상업 성장률 이상을 유지하겠다고 말했다(2차 요약). 강세 시나리오 가치가 현재가를 크게 웃돈다. [S43](https://www.nasdaq.com/articles/palantir-technologies-q2-earnings-call-highlights) [C:value@bull]
- 모델이 첫해 이후 감속을 너무 일찍 가정했을 수 있다. 미국 상업 매출이 전년 대비 +149%로 가속하고 있어, 3분기에 감속 대신 가속이 확인되면 기본 경로가 낮아 보인다. [F239] [F237]
- 컨센서스와 NRR을 확보하지 못해 시장 기대와의 차이를 검증하지 못했다. 단위경제가 이미 입증된 상태인데 내가 이를 보지 못하고 있을 수 있다. [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm) [S43](https://www.nasdaq.com/articles/palantir-technologies-q2-earnings-call-highlights)

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 강세 case가 10년 뒤 주당 가치를 현재가의 7.36배로 만든다는 것이다. 그러나 그 case는 5년 매출 연 53.3% 성장을 전제하는데, 이는 아직 계획이지 실적이 아니다. 강세 시나리오의 확률은 20%이고 기본 시나리오 기대 수익률은 -0.9%다. 꼬리가 크다는 것과 지금 담아야 한다는 것은 다른 문제다. 이 꼬리를 사려면 고객 단위 증거(NRR·이탈률)가 입증되어야 하는데 아직 없다. 증거가 쌓이면 키운다는 것이 내 순서이고, 증거 없이 꼬리에 먼저 거는 것은 내 순서가 아니다. [C:upside_10y@anderson] [C:revenue_cagr@bull] [C:expected_irr] [C:irr@base]
- → 애크먼: 애크먼의 가장 강한 논거는 기본 시나리오에서 매출 성장 기여(+34.4%)를 멀티플 압축(-37.0%)이 전부 상쇄한다는 것이다. 이 점은 전적으로 동의한다. 다만 나는 예측 불가능하다는 이유로 이 시장을 버리지 않는다. 시장이 아직 정의되지 않은 기업은 오히려 내가 찾는 대상이다. 내가 반대하는 이유는 예측 가능성이 아니라 두 가지다. 하나는 단위경제가 입증되지 않았다는 것이고, 다른 하나는 가격이 요구하는 지속 기간이다. 역DCF는 FCF 마진이 30%로 수렴해도 10년 연 42.0% 성장을 요구한다. 가격이 내려와 요구 지속 기간이 짧아지거나 NRR이 공개되면 결론은 바뀔 수 있다. [C:irr@base] [C:implied_cagr@m30]
- → 레드팀: 레드팀의 사전 부검 중 가장 무거운 것은 미국 상업 수요의 일시성이다. 고객 단위 지표가 없는 상태에서 +149% 매출과 +153% TCV는 소수 대형 계약에 기댄 숫자일 수 있다. 이는 내 반대 논거를 더 강하게 한다. 선행 신호는 TCV와 전분기 대비 성장률이 가장 낫다. 미국 상업 TCV는 2분기에 21.3억 달러이고, 매출은 전분기 대비 +28%였다. 두 값이 꺾이는지는 매출보다 먼저 보인다. 이 신호를 재평가 조건에 반영한다. 다만 기본 경로를 깨뜨리는 쪽의 신호와 모델보다 강하다는 쪽의 신호를 함께 지켜봐야 대칭이 된다. [F239] [F241] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)

**참이어야 하는 것**
- [on_track] FY2026 연간 매출이 가이던스 하단 이상
- [on_track] 3분기 미국 상업 매출이 전분기 대비 계속 증가
- [on_track] 이연매출이 계속 늘어 선결제 수요가 유지됨
- [on_track] GAAP 영업이익이 늘어 고정비 레버리지가 이어짐
- [at_risk] 희석 주식 수가 분기 정체 수준을 유지함

**인정한 점**
- 앤더슨의 성장 가속 논거는 사실로 인정한다. 2026년 2분기 매출이 전년 대비 +93%이고, 가이던스가 상향됐다. 이것이 입장을 바꾸지 못하는 이유는 가설의 진위가 아니라 입증 수준과 기대수익률이다.
- 애크먼이 지적한 보도자료 수치와 주가 근거의 불확실성(S42·S43 원문 미대조, 종가 불일치)은 맞다. 이 때문에 시작 비중 0을 유지하고, 근거가 보강되기 전에는 올리지 않는다.
- 레드팀의 TCV와 전분기 성장률 신호는 모니터링 지표로 채택한다. 분기 결과가 기본 경로를 웃돌면 반대 입장을 다시 검토한다.


## 애크먼 — 반대 (4/5)

> 사업의 질은 내가 좋아하는 쪽에 가깝다. 총이익률이 80%대이고 FCF 마진이 46.9%이며 부채가 없다. 그러나 사고 싶은 가격이 아니다. 현재 FCF 수익률은 0.7%이고 P/FCF는 142.29배다. 기본 시나리오의 현재가치는 110.56달러인데 주가는 186.03달러이므로 안전마진이 아니라 프리미엄을 내고 사는 셈이다. 확률 가중 기대 연 수익률은 -0.6%이고 손실 확률은 80%다. 게다가 이 가격이 정당화되려면 FCF 마진 30%로 수렴하더라도 매출이 10년간 연 42.0% 커져야 한다. 단순성과 예측 가능성도 부족하다. 매출 성장률이 56.2%에서 이번 분기 +93%로 가속하는 회사의 10년 뒤 FCF를 합리적 범위로 좁힐 수 없다. 좋은 회사를 비싸게 사면 나쁜 투자다. 담지 않는다.

*이전 판단 대비: 직전 판단은 주가 208.67달러(F212) 기준이었고, 이번에는 186.03달러(F213) 기준이다. 주가가 내렸지만 기본 시나리오 현재가치 110.56달러에는 아직 못 미쳐 반대 입장은 그대로다. 재검토 기준 가격만 현재가치에 맞춰 올렸다.*

**논거**
- 가격이 모든 것을 말한다. FCF 수익률 0.7%, P/FCF 142.29배는 보수적 가정의 내재가치와 거리가 멀다. 기본 시나리오의 현재가치 110.56달러 대비 주가 186.03달러이므로 안전마진이 음수다. [C:fcf_yield] [C:p_fcf] [C:iv@base] [F213]
- 확률 가중 기대 연 수익률이 -0.6%이고 손실 확률이 80%다. 강세 시나리오(연 +14.3%)에 가까워야만 수익이 나는 비대칭이다. 우리는 하방이 보호되고 상방이 열린 구조에만 크게 건다. [C:expected_irr] [C:p_loss] [C:irr@bull]
- 기본 시나리오 수익률 분해에서 매출 성장 기여(+34.4%)를 멀티플 압축(-37.0%)이 전부 상쇄한다. 사업이 모델러의 기본 가정대로 성장해도 주주는 그 성장의 대가를 받지 못한다. [C:irr@base] [C:expected_irr]
- 단순성과 예측 가능성에서 탈락한다. 시장 내재 성장은 FCF 마진 30%에서도 연 42.0%이고, 기본 시나리오 목표 마진 52%에서도 연 34.5%다. 이 범위의 10년 뒤 FCF를 합리적 범위로 좁힐 수 없고, 같은 성장을 해낸 기업의 기저율 표도 없다. 한 문단으로 설명되는 사업이라도 현금흐름 범위가 이렇게 넓으면 단순하지 않다. [C:implied_cagr@m30] [C:implied_cagr@m52] [C:base_rate@implied]
- 재무 건전성은 흠이 없다. 순부채/EBITDA는 -3.53배로 순현금이고 부채는 0이다. 밸리언트 같은 자본시장 의존 위험은 없다. 반대 논거는 재무가 아니라 가격과 예측 가능성이다. [C:net_debt_to_ebitda] [F245] [C:net_cash]

**사전 부검**
- 사전 부검: 내가 틀렸다면 성장이 모델러의 강세 시나리오처럼 이어지고 시장이 프리미엄 배수를 계속 준 경우다. 미국 상업 매출이 전년 대비 +149%이고 가이던스가 상향되는 등 펀더멘털 모멘텀은 실제다. 그 경우 기다리는 동안 상승 폭을 놓친다. [F239] [F233] [C:irr@bull]
- 사전 부검: 현금 창출력이 기본 시나리오보다 훨씬 빠르게 커질 수 있다. 2분기 조정 FCF가 12.2억 달러이고 FY2025 FCF 마진이 46.9%이므로, 마진이 52%를 넘으면 내재가치가 올라갈 수 있다. 다만 SBC 차감 FCF로 봐야 하고 희석이 계속된다는 점은 그대로다. [F244] [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [C:dilution]
- 사전 부검: 분석 입력에 구멍이 있다. 컨센서스와 과거 가이던스 이력이 없고, 보도자료 수치는 원문 대조를 하지 못했으며, 주가도 직전 종가가 갈린다. 이 불확실성은 내가 안전마진을 더 요구하는 이유이지, 덜 요구할 이유가 아니다. [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm) [S43](https://www.nasdaq.com/articles/palantir-technologies-q2-earnings-call-highlights) [S38](https://www.heygotrade.com/en/news/palantir-pltr-stock-news-october-14-2026/) [S39](https://finance.yahoo.com/quote/PLTR/history/)

**반론**
- → 앤더슨: 앤더슨은 강세 case의 7.36배를 근거로 삼지만 강세 확률은 20%에 불과하고 기본 시나리오 수익률은 -0.9%다. 역DCF는 FCF 마진이 30%로 수렴해도 10년 연 42.0% 성장을 요구하는데 기저율 표가 없어 그 꼬리가 얼마나 드문지조차 검증되지 않았다. 최근 3년의 가속은 선형 외삽의 근거가 못 된다. 생존자 편향이다. 확률 가중 기대 수익률은 음수이고 손실 확률은 80%다. 좋은 꼬리 하나에 거는 것은 집중이 아니라 가격을 무시한 도박이다. [C:upside_10y@anderson] [C:implied_cagr@m30] [C:irr@base] [C:expected_irr] [C:p_loss]
- → 슬레이터: 슬레이터의 반대 결론에는 동의하지만 논거가 약하다. 생존 경로와 단위경제는 필요조건일 뿐이다. 슬레이터는 NRR 부재를 반대 이유로 들었지만, 설령 NRR이 입증되어도 기본 시나리오 현재가치 110.56달러 대비 주가 186.03달러이면 결론은 같다. 내 반대의 중심은 증거 부족이 아니라 가격이다. 증거가 쌓이면 다시 보겠다는 입장은 가격 조건이 빠져 있어 증거가 확인되는 순간 비싼 가격에 사게 될 위험이 있다. [C:iv@base] [F213] [C:expected_irr] [C:irr@base]
- → 레드팀: 레드팀의 사전 부검은 FCF 범위를 넓힌다. 특히 SBC 차감 FCF 마진이 FY2025 기준 31.7%로 보고 마진 46.9%보다 훨씬 낮다면, 주주 몫 FCF는 가정보다 작다. 기본 시나리오 마진 52%는 낙관적이고, 약세 마진 40%에 가까운 결과도 배제할 수 없다. 이만큼 현금흐름 범위가 넓어지면 안전마진은 20%가 아니라 훨씬 커야 한다. 현재 마진은 음수 68.3%이므로 필요한 수준과 거리가 더 멀어진다. 레드팀의 멀티플 붕괴 시나리오는 이 가격에서 가장 현실적인 하방이다. [C:fcf_after_sbc@FY2025] [C:fcf_margin@FY2025] [C:p_fcf] [C:expected_irr]

**인정한 점**
- 앤더슨이 지적한 성장 가속은 실제다. 매출 성장률이 FY2025 56.2%이고 2026년 2분기 미국 상업 매출이 전년 대비 +149%라는 점을 인정한다. 이는 기다리는 동안 상승분을 놓칠 위험이 있음을 뜻하며, 그래서 재검토 가격 조건(110달러)을 유지한다.
- 슬레이터가 말한 것처럼 재무 건전성은 쟁점이 아니다. 부채 0, 순현금이라 자본시장 의존 레드라인은 문제가 되지 않는다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Palantir는 정부(국방·정보기관)와 대기업에 데이터 통합·분석 소프트웨어 플랫폼(Foundry·Gotham·AIP)을 판매하고, 소프트웨어 구독·계약과 배포 인력 투입으로 수익을 낸다. 총이익률이 80%대(C:gross_margin@FY2025 82.4%)로 높고 영업이익률이 FY2023 5.4%에서 FY2025 31.6%로 빠르게 올랐다(C:operating_margin@FY2025). 성장도 가속 중이다. 매출 성장률은 FY2023 16.7%에서 FY2025 56.2%로 올랐고(C:revenue_growth@FY2025), 2026년 2분기 매출은 전년 대비 +93%, 미국 상업 매출은 +149%였다(S42). 단위경제는 개선 중으로 보인다. 다만 고객 단위 지표(NRR·CAC·이탈률·총 고객 수)는 확보하지 못해 고객 1명 수준의 경제성은 직접 확인되지 않았고, 해자의 증거도 대부분 간접 지표(마진·계약가치·대형 계약 수)에 의존한다.

- [unit_economics] 영업이익률이 FY2022 -8.5%에서 FY2025 31.6%로 올랐고(C:operating_margin@FY2025), 2026년 1분기 영업이익 7.5억(F122), 2분기 9.1억 달러(F123)로 분기 이익이 계속 늘고 있다. 2분기 GAAP 영업이익률은 47%로 보도됐다(S42). 매출이 늘수록 비용 레버리지가 나타나 단위경제는 개선 방향이다. 다만 고객 단위 CAC·NRR·이탈률은 확인하지 못해 `unclear`로 둔다. [C:operating_margin@FY2025] [F122] [F123] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- [unit_economics] 현금 창출이 이익을 앞선다. FY2025 FCF 마진은 46.9%(C:fcf_margin@FY2025)이고 FCF는 21.0억 달러(C:fcf@FY2025)다. SBC를 차감해도 14.2억 달러가 남는다(C:fcf_after_sbc@FY2025). SBC/매출은 FY2021 50.5%에서 FY2025 15.3%로 내려왔다(C:sbc_to_revenue@FY2025). 다만 FY2026 2분기 SBC는 2.7억 달러로 전년 같은 분기(1.6억)보다 늘었다(F173, F170). [C:fcf_margin@FY2025] [C:fcf@FY2025] [C:fcf_after_sbc@FY2025] [C:sbc_to_revenue@FY2025] [F173] [F170]
- [customers] 미국 상업 부문이 성장을 이끈다. 2026년 2분기 미국 상업 매출은 7.6억 달러로 전년 대비 +149%, 전분기 대비 +28%다(F239, S42). FY2026 미국 상업 매출 가이던스는 34.24억 달러 초과다(F236). 18개월 동안 현재 미국 상업 성장률 이상을 유지하겠다는 CEO 발언은 2차 요약으로만 확인됐다(S43). 정부 부문 비중과 고객 집중도는 확인하지 못했다. [F239] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm) [F236] [S43](https://www.nasdaq.com/articles/palantir-technologies-q2-earnings-call-highlights)
- [runway] 2026년 2분기 매출 19.4억 달러(F153)에서 FY2026 가이던스 매출은 81.5억 달러 이상으로 상향됐다(F233). 3분기 매출 가이던스는 21.6억 달러다(F237). 가이던스가 연초보다 올랐다는 점은 수요가 공급 가능 속도보다 빠르다는 신호이나, 이전 분기 가이던스와 달성 이력은 확보하지 못해 가이던스 신뢰도는 검증하지 못했다. [F153] [F233] [F237]
- [industry] 산업 구조는 AI 플랫폼 경쟁이다. 파트너(Nebius 소버린 AI 스택, PwC, 금융 서비스 책임자 영입)로 판매 채널을 넓히는 중이다(S26, S28, S19). 이는 확장의 흔적이지만, 대형 클라우드·AI 업체와의 경쟁 강도, 점유율, 가격 결정력은 근거에서 확인되지 않았다. 소버린 AI 규제가 외부 제약이 될 수 있다는 보도도 있다(S27). [S26](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOdmFld2JjZEoxbldQVGZGUE9ZZVRvd2I1LWhXcV93YXAtNlo1R1IwNGVVU0dCQ1dtMVk0WmpxTGdSTVNjYXBtc1ZDQVJzVFpMM1FocTN2clQ4NlN1N1pqVTNITmV6Rnl6Sk1RUzdQdzA0OFhCTmxZdHJBOEc4YnJjdS1VbEdEUWRlV1FrNjdTRWtZZDdCdDlPTGFUOUVlMExFa0d2cC1GSUdyTzdhcmttVVFiRFdLVFRvRERFUVNKYmR0dFJYUWhqWEFxS0tIdUN6dlJkY0dUUQ?oc=5) [S28](https://news.google.com/rss/articles/CBMizwFBVV95cUxPdkZyTUlfQkZLY2NaVlBHMXFLbWZMTVpWUEJKY1BkT0xpemFzYkZoZnIzZF9FMUJNSkZyQUNibUJSSERqbmpGSERHQy1jWGZxUjc5ekJZLXB1R05PeHBDRml0RjUzYVBDUm1Sa3MyM3RBLUt5YmtHZzNhVl82UnBOb0h3bGUzSDJvWjI0dWRFYnRHVjRpUmV0WDk1LThxQ21BR0dHci1GZUtJeGk5b0U1NkNubjFMc0d6SzYwNlVEbmdBaEg1Zy03Tm5RQ3JoNUE?oc=5) [S19](https://news.google.com/rss/articles/CBMiygFBVV95cUxQUjlKNlNGby0ybjlHdENGekpvYnVjOGRqUGJ5Xzl0Sm9SWU5GOFRKTVhVN05JZ1Ezd2E3YWNMNGJ5d2pObHdnTS1wZld1NTVLN0k4SElBSFladk1HdThaZ0ItVTltWHVSSnU0T1lIbjQyeWhORDFVVEt3cGNPVnlvUG5UWmUwVWRPUm5OcnIwVzg0NGt1cUEyV0JKQ3hjZHRDRm14UVM3Wm1QXzhJV3RIMGV0NXpCYVZ4LWJMMWZPazV1cFlpSXNGZ3FB?oc=5) [S27](https://news.google.com/rss/articles/CBMingFBVV95cUxOSXRiUnZMQ0xiTjE0dktzakxGYVpJeWtNMC1ZQ2pXd1JRU0Q0c0JtNzZqS3RoOUFYQ21LVzlUY3dyUS13cjJXTGpiOTZ1YmRHWm52XzdxLUdsMXVTSUlobzYybGkwVzBhWk55TjZoLUlkTFB2TEFSbDYwd1Z1OVJZVDBJRmlPTlh4U0hsZ0VVWWtBaDJidW1PX3dOYUl5UQ?oc=5)
- [unit_economics] 매출채권이 매출보다 빠르게 늘었다. DSO가 FY2022 49.5일에서 FY2025 85.0일로 길어졌고(C:dso@FY2025), 매출채권은 2026년 2분기 14.9억 달러로 연초 이후 계속 늘었다(F143). 대형 계약 비중이 커지며 결제 조건이 길어진 것일 수 있으나, 단위경제 악화인지 계약 구조 변화인지는 근거로 구별하지 못한다. [C:dso@FY2025] [F143]
- [runway] 재투자 활주로는 현금 측면에서 충분하다. 2026년 2분기 현금과 단기투자는 합 94.1억 달러로 계산되고(C:net_cash), 부채는 0이다(F245). 설비투자는 매출 대비 미미해(FY2025 3,388만 달러, F11) 성장에 자본이 거의 들지 않는다. 다만 현재 가격은 매출 연 40% 이상 성장을 10년 지속해야 정당화된다(C:implied_cagr@m30 42.0%). 시장이 활주로를 매우 길게 반영하고 있다는 뜻이다. [C:net_cash] [F245] [F11] [C:implied_cagr@m30]
- [claimed] 전환비용 해자는 간접 흔적만 있다. 미국 상업 잔여 계약가치 62.4억 달러(+124%)와 TCV 21.3억 달러(+153%)는 고객이 계약을 늘리고 있음을 시사하지만(F240, F241), NRR·이탈률·가격 인상 후 잔존 기록이 없어 전환비용을 직접 입증하지 못한다. 근거도 보도자료 요약(S42)이며 원문 대조를 하지 못했다. [F240] [F241] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- [proven] 총이익률이 FY2021 78.0%에서 FY2025 82.4%로 유지·개선됐다(C:gross_margin@FY2025). 같은 기간 매출이 15.4억에서 44.8억 달러로 늘었다(F144, F148). 규모 확대에도 원가율이 악화되지 않았다. 이는 소프트웨어 중심 원가 구조의 흔적이지만, 경쟁사 대비 마진 비교는 없어 해자 자체의 증거로는 약하다. [C:gross_margin@FY2025] [F144] [F148]
- [claimed] 대형 계약 기반이 두꺼워졌다. 2026년 2분기에 100만 달러 이상 계약이 220건, 500만 달러 이상이 98건이다(F242, F243). 정부·대기업 레퍼런스와 파트너 확장(PwC 제휴, Army TITAN 납품)은 규모·신뢰 효과를 시사하나(S28, S31), 점유율 추이 같은 경쟁 대비 수치는 없고 회사 발표와 보도 위주다. [F242] [F243] [S28](https://news.google.com/rss/articles/CBMizwFBVV95cUxPdkZyTUlfQkZLY2NaVlBHMXFLbWZMTVpWUEJKY1BkT0xpemFzYkZoZnIzZF9FMUJNSkZyQUNibUJSSERqbmpGSERHQy1jWGZxUjc5ekJZLXB1R05PeHBDRml0RjUzYVBDUm1Sa3MyM3RBLUt5YmtHZzNhVl82UnBOb0h3bGUzSDJvWjI0dWRFYnRHVjRpUmV0WDk1LThxQ21BR0dHci1GZUtJeGk5b0U1NkNubjFMc0d6SzYwNlVEbmdBaEg1Zy03Tm5RQ3JoNUE?oc=5) [S31](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNT1RTaFhpaURiVTJZVXZYSVpLWUg3c0ZoblZlRms3S2Y0YWpocW1zYjdsRy1ZYVZSNDZLNGpycFRqVFBJLW0zd0JoV1RxN0JGZmtUcjhmT2w4WHdfREFrTjVlQUgtakU4MG5sSXV5X1dfMElDci1IXzJvdUUtVFVscW9Hc0FDa2V6X0pxNGZ4bkdOWV9Fam5TM3FNTnBjR29UamVRSVhlVEdsZw?oc=5)

### 경영진·자본배분 — mixed

경영진의 보상 구조, 내부자 매매, 과거 가이던스 적중률은 1차 원문을 확인하지 못해 정렬 여부를 직접 판단할 근거가 없다. 확인되는 것은 세 가지다. 첫째, SBC 비중은 FY2021 50.5%에서 FY2025 15.3%로 낮아졌지만 희석은 계속된다. 둘째, 자사주 매입은 규모가 작아 희석을 상쇄하지 못한다. 셋째, 자본배분은 부채 없이 현금을 쌓는 보수적 형태이고 대형 인수 흔적은 없다. 2026년 가이던스는 상향됐으나 이전 가이던스 이력이 없어 신뢰도는 검증 불가다. 따라서 중립인 mixed로 둔다.

- [compensation] 근거 없음. DEF 14A(S6)는 수집됐지만 보상 연동 지표(장기 매출·FCF·ROIC 대 단기 EPS·조정 EBITDA)와 베스팅 기간은 원문을 확인하지 못했다. 리서처도 보상 지표를 1차 원문 확인 필요로 분류했다. [S6](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000019/pltr-20260423.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도 자료가 evidence에 없다. 9월 금융 서비스 총괄 영입 보도(S19)는 외부 인사 영입이라 내부자 정렬의 근거가 되지 않는다. [S19](https://news.google.com/rss/articles/CBMiygFBVV95cUxQUjlKNlNGby0ybjlHdENGekpvYnVjOGRqUGJ5Xzl0Sm9SWU5GOFRKTVhVN05JZ1Ezd2E3YWNMNGJ5d2pObHdnTS1wZld1NTVLN0k4SElBSFladk1HdThaZ0ItVTltWHVSSnU0T1lIbjQyeWhORDFVVEt3cGNPVnlvUG5UWmUwVWRPUm5OcnIwVzg0NGt1cUEyV0JKQ3hjZHRDRm14UVM3Wm1QXzhJV3RIMGV0NXpCYVZ4LWJMMWZPazV1cFlpSXNGZ3FB?oc=5)
- [guidance] 가이던스 적중률은 계산할 수 없다. 과거 가이던스 사실이 없어 C:guidance_hit_rate가 비어 있다. 확보한 것은 FY2026 가이던스 상향뿐이다. 연간 매출은 81.50~81.58억 달러(기존 76.50~76.62억)이고 조정 FCF는 45~47억 달러(기존 42~44억)이며 3분기 매출은 21.60~21.64억 달러다. 상향은 방향성 신호일 뿐 과거에 지켰는지는 보여주지 못한다. [F233] [F234] [F237] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- [guidance] CEO가 향후 18개월 동안 현재 미국 상업 성장률과 같거나 그 이상으로 성장시키겠다고 말했다고 보도됐다. 이는 2차 요약(S43)이고 원문은 없다. 미국 상업 매출은 FY2026Q2에 7.6억 달러로 전년 대비 +149%였다. 이 약속은 과도하게 공격적이어서 이행 여부를 추적할 가치가 있다. [S43](https://www.nasdaq.com/articles/palantir-technologies-q2-earnings-call-highlights) [F239] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- [dilution] SBC는 FY2021 7.8억에서 FY2025 6.8억으로 줄었다. 매출 대비로는 FY2021 50.5%에서 FY2025 15.3%로 크게 낮아져 개선 방향이다. 다만 희석 주식 수는 FY2021 19.2억에서 FY2025 25.7억으로 늘었고 FY2025 증가율은 4.7%다. 코드는 희석 신호를 watch로 표시한다. [C:sbc@FY2025] [C:sbc_to_revenue@FY2021] [C:sbc_to_revenue@FY2025] [C:share_change@FY2025] [C:dilution]
- [dilution] 자사주 매입은 FY2023까지 0이었고 FY2024 6,420만, FY2025 7,498만으로 시작됐다. 같은 해 SBC는 FY2024 6.9억, FY2025 6.8억이어서 매입은 SBC 규모에 비해 작다. 희석을 상쇄하는 수준이 아니고 FY2026Q2 희석 주식 수도 25.7억으로 정체돼 있다. 이 매입은 주주환원이라기보다 희석 완화 시늉에 가깝다. [C:buybacks@FY2024] [C:buybacks@FY2025] [C:sbc@FY2024] [C:sbc@FY2025] [F61]
- [capital_allocation] 부채는 0이고 순현금은 FY2025 71.8억, TTM(FY2026Q2) 기준 94.1억이다. 현금 20.3억과 단기투자 73.8억을 쌓아 두는 보수적 배분이다. 단기투자 비중이 커서 현금 보유 목적이 불분명하고 자본배분 수익률은 검증하지 못한다. [F245] [C:net_cash@FY2025] [C:net_cash] [F23] [F183]
- [capital_allocation] 대형 인수나 고점 매입의 흔적은 보이지 않는다. 영업권은 FY2022에 3,794만에 그쳤고 capex도 FY2025에 3,388만으로 작다. 재투자는 R&D 중심이고 R&D는 FY2025에 5.6억이었다. 1차 원문에 인수 이력이 없는지는 확인하지 못했다. [F73] [C:capex@FY2025] [C:rnd@FY2025]

### 회계 품질 — watch

현금 전환은 정직하다. 순이익이 흑자인 해에 영업현금흐름이 음수인 적이 없고, 영업현금흐름이 순이익을 웃돌아 발생액 비율은 -6.7%로 음수다. 재작성이나 감사인 변경 신호도 코드에는 없다. 조정해서 봐야 할 숫자는 세 가지다. 첫째, SBC가 매출의 15.3%이고 희석이 연 7.5%여서 주주 몫 FCF는 보고 FCF보다 작다. SBC 차감 FCF(14.2억 USD)를 기준으로 봐야 한다. 둘째, 매출채권이 매출보다 빨리 늘어 DSO가 73.2일에서 85.0일로 길어졌다. 이연매출도 같이 늘어 수익 선인식 신호는 아니지만, 1차 문서에서 청구 시점과 대형 계약 집중도를 확인해야 한다. 셋째, 1차 원문을 확인하지 못한 항목이 있다. 감사의견, Non-GAAP 조정 내역, 특수관계자 거래, 실효세율 1.4% 보도, 보도자료의 현금 92억 USD와 XBRL 합계의 불일치다. 이는 입증된 문제가 아니라 미확인이므로 red_flag의 근거가 되지 않는다. 판정은 watch다.

- [concern] sbc_to_revenue: SBC/매출 15.3%는 문턱 10%를 넘는다. 방향은 개선 중이다(FY2021 50.5%에서 하락). 그러나 SBC는 현금비용이 아니어도 실제 비용이다. 보고 FCF를 그대로 쓰지 말고 SBC 차감 FCF(14.2억 USD)로 봐야 한다. SBC/영업현금흐름은 32.0%로 문턱 50% 아래다. 이 신호는 회계 왜곡이 아니라 보고 이익의 질을 조정해서 봐야 한다는 뜻이다. [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [C:fcf_after_sbc@FY2025] [F168] [F148]
- [concern] receivables_gap: FY2024 매출채권 증가율이 매출 증가율을 28.9%p 웃돈다. 문턱은 15%p다. DSO는 73.2일에서 85.0일(FY2025)로 길어졌고 매출채권은 FY2026Q2에 14.9억 USD다. 완화 요인이 있다. 이연매출이 같이 늘었고(FY2025 4.1억, FY2026Q2 5.8억 USD), 영업현금흐름이 순이익을 넘는다. 따라서 채널 밀어내기나 조기 인식의 증거는 없다. 다만 정부와 대형 계약의 청구 시점으로 설명되는지는 10-Q의 계약자산과 매출채권 주석으로 확인해야 한다. 현재는 관찰 대상이다. [C:receivables_gap] [C:dso@FY2025] [F141] [F143] [F49] [F51] [F111]
- [concern] dilution: 희석 주식 수가 연 7.5% 늘어 문턱 3%를 넘는다. FY2025 단독으로는 4.7% 증가다. 최근 분기(FY2025Q3~FY2026Q2)에는 25.7억 주 수준에서 거의 늘지 않았다. 자사주 매입(FY2025 7,498만 USD)은 SBC 6.8억 USD의 일부만 상쇄한다. 매입이 희석을 막는다고 볼 수 없다. 주당 가치는 희석을 반영해 봐야 한다. [C:dilution] [C:share_change@FY2025] [F56] [F59] [F61] [F5] [F168]
- [info] 발생액 비율이 모든 연도에서 음수다(FY2025 -6.7%). 영업현금흐름이 순이익을 웃돈다(FY2025 FCF/순이익 1.29x). 이익이 현금으로 뒷받침된다. [C:accruals_ratio@FY2025] [C:fcf_conversion@FY2025] [F111] [F101]
- [watch] 이연매출이 매출 성장 이상으로 늘어(FY2026Q2 5.8억 USD) 수익 선인식의 반대 신호다. 그러나 매출채권도 같이 늘어(FY2026Q2 14.9억 USD) 청구와 수금 구조 확인이 필요하다. 매출 인식 정책의 상세(총액·순액, 다중 요소 계약)는 이번 입력에 없고 10-K 원문 확인이 필요하다. [F51] [F143] [S7](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm)
- [watch] 회사 가이던스는 조정 영업이익(FY2026 48.89억 USD)과 조정 FCF 기준이다. GAAP 대비 조정 내역은 보도자료 요약에서 확인하지 못했다. SBC가 조정 항목의 핵심일 가능성이 높아 조정 FCF는 SBC 차감 FCF와 구분해서 봐야 한다. Non-GAAP 신호는 코드에 잡히지 않았다. 다만 조정 내역은 1차 원문 확인이 필요하다. [F235] [F234] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- [watch] 법인세가 세전이익 대비 매우 작다(FY2026Q2 1,538만 USD, 세전 10.8억 USD). 낮은 실효세율이 이익의 지속가능성에 영향을 줄 수 있다. 1.4% 보도는 2차 자료이고 1차 자료로 확인하지 못했다. 이연법인세자산과 세금 공제의 지속성은 10-K 세무 주석에서 확인해야 한다. [F93] [F133] [S20](https://news.google.com/rss/articles/CBMipAFBVV95cUxOcmtBTFEwT09QS0hTa0diSmNLN1NXNTlvUFlyYjVDb28yWk1rWkdpaE9LNjhYbTRWckY4TVlJcnVkMXpUMFc1LTEtajBGMmdZQkNPcDVfVktBZl81eFBfc3hYVkpIQ183ZU9GZVhBd2dmdWg1dEE0cjlpaUtOcGJmTkFYZTZiLUFETHZPSG80elFtSFdiZHktNjNPdzRCVlFaZlZOTtIBqgFBVV95cUxPZ1pGV01wRGFZNXBVZHZLUWRmX0Z5a0ZFU2d3NElxZmNtUkRRcngzZFBzWnc2TFVURTY1dmpPSktVdV9qSFM4TUZxOXl0dF9FVUY1YnVaUFBEeHJlb2I1cVUyTW8tdVZKMThsS0dJOGtDQTVUVlI2bkh6WmE4SWxmZktCQUQ3Ull3QW0wMWlZYmZEMzlTTnJGVGVSejJTZTJiX1B6WXlWRHhSdw?oc=5)
- [watch] 보도자료의 현금·단기 미국채 합계 92억 USD가 XBRL의 현금 20.3억 USD와 단기투자 73.8억 USD 합계와 정확히 맞지 않는다. 구성 차이일 가능성이 크지만 원문 대조 전까지 순현금을 단정하지 않는다. 조정해서 볼 항목이다. [F23] [F183] [S42](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- [info] 코드 신호에 재무제표 정정이나 감사인 변경이 없다. 감사의견(계속기업 의문, 핵심감사사항)과 특수관계자 거래는 이번 입력에 없어 10-K·DEF 14A에서 확인해야 한다. 영업권은 총자산 대비 미미하고 부채는 없다. 이 둘은 회계 위험을 높이지 않는다. [S7](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm) [S6](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000019/pltr-20260423.htm) [F245] [F193]

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (30%) 멀티플 붕괴: 사업은 계획대로 성장했는데 주가만 −60%. 현재 P/FCF 142배(C:p_fcf)는 성장이 20%대로 내려오는 순간 성숙 소프트웨어 배수로 압축된다. 기본 시나리오 수익률 분해에서 멀티플 변화가 연 −37.0%로 매출 성장 +34.4%를 거의 전부 상쇄한다(C:base_rate@base 분해). 매출이 5년간 5.6배(44.8억→249.4억) 커져도 출구 P/FCF 35배면 주가는 제자리다. 성장 감속이 처음 확인되는 분기에 가이던스 상향 폭이 줄면, 이익이 늘어도 배수가 먼저 무너진다. [C:p_fcf] [C:ev_revenue] [C:expected_irr] [S27](https://news.google.com/rss/articles/CBMingFBVV95cUxOSXRiUnZMQ0xiTjE0dktzakxGYVpJeWtNMC1ZQ2pXd1JRU0Q0c0JtNzZqS3RoOUFYQ21LVzlUY3dyUS13cjJXTGpiOTZ1YmRHWm52XzdxLUdsMXVTSUlobzYybGkwVzBhWk55TjZoLUlkTFB2TEFSbDYwd1Z1OVJZVDBJRmlPTlh4U0hsZ0VVWWtBaDJidW1PX3dOYUl5UQ?oc=5)
- (20%) 미국 상업 수요의 일시성: 성장 대부분이 AI 도입 초기의 파일럿·확장 계약 쏠림이라 계약이 한 번에 꺼진다. 미국 상업 매출 +149%, TCV +153%는 소수 대형 계약(500만 달러 이상 98건)에 의존한 숫자다. 고객 단위 NRR·이탈률·총 고객 수를 아무도 확인하지 못했다(전환비용 해자는 claimed 수준). 도입 열기가 식거나 대형 AI 업체·소버린 AI 규제(S27)가 경쟁 압력이 되면 신규 TCV가 꺾이고, 매출보다 먼저 계약 지표가 움직인다. [F239] [F241] [F243] [S27](https://news.google.com/rss/articles/CBMingFBVV95cUxOSXRiUnZMQ0xiTjE0dktzakxGYVpJeWtNMC1ZQ2pXd1JRU0Q0c0JtNzZqS3RoOUFYQ21LVzlUY3dyUS13cjJXTGpiOTZ1YmRHWm52XzdxLUdsMXVTSUlobzYybGkwVzBhWk55TjZoLUlkTFB2TEFSbDYwd1Z1OVJZVDBJRmlPTlh4U0hsZ0VVWWtBaDJidW1PX3dOYUl5UQ?oc=5) [S35](https://news.google.com/rss/articles/CBMipAFBVV95cUxONzd2MEZiSjhkQ0FEbEtSWVMxNEtHWnpJU21LUzFYcHdDN3M1TnkyWXJhdVBrU0NpTTlnX0gzNF9waVBIejhnSFltOXpNU0hzZkNJZVdzdnNfdnlUNmhfWjQ5MHJMMmNWdzZkcGNDelFlNDREdUpkbDNNTldCNjdCZGQyR0lUWFlZNUx4X21Ec3RON0E1d0dNc2VyZjlkRWNVYU9wUg?oc=5)
- (15%) 수익의 질과 희석: 보고 FCF는 SBC를 제외한 숫자인데 SBC는 FY2026Q2에 2.7억 달러로 전년 동기(1.6억)보다 69% 늘었다. 희석 주식 수는 5년간 연 7.5% 늘었고 자사주 매입(7,498만 달러)은 SBC 6.8억의 일부만 상쇄한다. DSO는 85일로 길어지고(C:dso@FY2025) 매출채권이 매출보다 빨리 늘어 대형 정부·기업 계약의 수금이 지연되면 FCF 마진이 52% 가정에서 40% 이하로 내려간다. 실효세율 1.4% 보도(S20)가 사실이면 세율 정상화만으로 순이익의 지속가능성도 훼손된다. 1차 원문 미확인 항목(Non-GAAP 조정, 현금 92억 대 94.1억 불일치)이 악재로 확인될 위험도 있다. [F173] [F170] [C:dso@FY2025] [C:dilution] [C:receivables_gap] [S20](https://news.google.com/rss/articles/CBMipAFBVV95cUxOcmtBTFEwT09QS0hTa0diSmNLN1NXNTlvUFlyYjVDb28yWk1rWkdpaE9LNjhYbTRWckY4TVlJcnVkMXpUMFc1LTEtajBGMmdZQkNPcDVfVktBZl81eFBfc3hYVkpIQ183ZU9GZVhBd2dmdWg1dEE0cjlpaUtOcGJmTkFYZTZiLUFETHZPSG80elFtSFdiZHktNjNPdzRCVlFaZlZOTtIBqgFBVV95cUxPZ1pGV01wRGFZNXBVZHZLUWRmX0Z5a0ZFU2d3NElxZmNtUkRRcngzZFBzWnc2TFVURTY1dmpPSktVdV9qSFM4TUZxOXl0dF9FVUY1YnVaUFBEeHJlb2I1cVUyTW8tdVZKMThsS0dJOGtDQTVUVlI2bkh6WmE4SWxmZktCQUQ3Ull3QW0wMWlZYmZEMzlTTnJGVGVSejJTZTJiX1B6WXlWRHhSdw?oc=5)
- (15%) 정부·정책 집중과 매크로 노출: 정부 부문 비중을 확인하지 못했지만 국방·정보기관 의존이 크다면 예산 지연·정책 변화·정치적 평판 리스크가 한꺼번에 온다. 여기에 AI 인프라 투자 사이클 전반이 식으면(S35의 집중 경고) 고배수 AI 종목 전체가 동반 하락한다. 기업 쪽 파트너 확장(Nebius·PwC)이 매출로 번지지 않은 채 CEO가 약속한 '18개월간 미국 상업 성장률 이상 유지'(S43)가 깨지면 신뢰 훼손이 배수 압축을 가속한다. [S35](https://news.google.com/rss/articles/CBMipAFBVV95cUxONzd2MEZiSjhkQ0FEbEtSWVMxNEtHWnpJU21LUzFYcHdDN3M1TnkyWXJhdVBrU0NpTTlnX0gzNF9waVBIejhnSFltOXpNU0hzZkNJZVdzdnNfdnlUNmhfWjQ5MHJMMmNWdzZkcGNDelFlNDREdUpkbDNNTldCNjdCZGQyR0lUWFlZNUx4X21Ec3RON0E1d0dNc2VyZjlkRWNVYU9wUg?oc=5) [S43](https://www.nasdaq.com/articles/palantir-technologies-q2-earnings-call-highlights) [S27](https://news.google.com/rss/articles/CBMingFBVV95cUxOSXRiUnZMQ0xiTjE0dktzakxGYVpJeWtNMC1ZQ2pXd1JRU0Q0c0JtNzZqS3RoOUFYQ21LVzlUY3dyUS13cjJXTGpiOTZ1YmRHWm52XzdxLUdsMXVTSUlobzYybGkwVzBhWk55TjZoLUlkTFB2TEFSbDYwd1Z1OVJZVDBJRmlPTlh4U0hsZ0VVWWtBaDJidW1PX3dOYUl5UQ?oc=5) [S31](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNT1RTaFhpaURiVTJZVXZYSVpLWUg3c0ZoblZlRms3S2Y0YWpocW1zYjdsRy1ZYVZSNDZLNGpycFRqVFBJLW0zd0JoV1RxN0JGZmtUcjhmT2w4WHdfREFrTjVlQUgtakU4MG5sSXV5X1dfMElDci1IXzJvdUUtVFVscW9Hc0FDa2V6X0pxNGZ4bkdOWV9Fam5TM3FNTnBjR29UamVRSVhlVEdsZw?oc=5)
- 약한 가정 `base.exit_multiple`: 출구 P/FCF 35배는 5년 뒤 매출 성장이 20%대로 내려온 시점의 값인데, 이미 이 가정에서도 멀티플 변화가 연 −37.0%의 손실 요인이다. 성장이 한 자릿수 후반으로 더 빨리 떨어지면 35배가 아니라 22배(약세) 이하가 적용된다. 반대로 이 가정이 맞아도 기본 시나리오 수익률이 −0.9%라, 가격이 완벽한 성장 경로를 이미 반영한다는 점이 가장 약한 고리다. [C:expected_irr] [C:p_fcf] [C:implied_cagr@m52]
- 약한 가정 `base.revenue_growth`: 5년 매출 연 41%는 기저율 표가 없어 검증되지 않았다. 역DCF가 요구하는 10년 34~42% 성장은 역사적으로 거의 달성된 적이 없다. 첫해 82%(가이던스 반영)에서 시작해 2~5년차 50%·35%·26%·20%로 감속하는 경로는 미국 상업 18개월 약속(S43, 2차 요약)과 소수 대형 계약에 기댄다. [C:implied_cagr@m30] [S43](https://www.nasdaq.com/articles/palantir-technologies-q2-earnings-call-highlights) [F233]
- 약한 가정 `base.fcf_margin`: FCF 마진 52%는 FY2025 값 46.9%를 넘어서는 가정인데, 같은 기간 SBC 증가(2.7억, 전년 1.6억)·DSO 85일·세율 정상화 위험이 모두 마진을 깎는 방향이다. SBC 차감 FCF 마진은 이미 31.7%(14.2억/44.8억, C:fcf_after_sbc@FY2025)로 훨씬 낮고, 주주 몫 기준으로는 52%가 과대평가일 수 있다. [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [C:dso@FY2025] [F173]

## 검증 (L6)

주장 71개 — supported 40 · unsupported 26 · contradicted 0 · leap 5 · 미검증 0

- [unsupported] 애크먼: 단순성과 예측 가능성에서 탈락한다. 시장 내재 성장은 FCF 마진 30%에서도 연 42.0%이고, 기본 시나리오 목표 마진 52%에서도 연 34.5%다. 이 범위 — 없는 근거 인용: C:base_rate@implied
- [unsupported] 레드팀: 출구 P/FCF 35배는 5년 뒤 매출 성장이 20%대로 내려온 시점의 값인데, 이미 이 가정에서도 멀티플 변화가 연 −37.0%의 손실 요인이다. 성장이 한 자 — 출처 없는 숫자 37% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 수익의 질과 희석: 보고 FCF는 SBC를 제외한 숫자인데 SBC는 FY2026Q2에 2.7억 달러로 전년 동기(1.6억)보다 69% 늘었다. 희석 주식 수는 5 — 출처 없는 숫자 69%, 1.4%, 9.2e+09 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 회계 품질: 법인세가 세전이익 대비 매우 작다(FY2026Q2 1,538만 USD, 세전 10.8억 USD). 낮은 실효세율이 이익의 지속가능성에 영향을 줄 수 있다. 1.4 — 출처 없는 숫자 1.4% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 사업·산업: 현금 창출이 이익을 앞선다. FY2025 FCF 마진은 46.9%(C:fcf_margin@FY2025)이고 FCF는 21.0억 달러(C:fcf@FY2025)다.  — FY2021 SBC/매출 50.5%는 인용에 없다. 나머지 수치는 일치한다.
- [unsupported] 사업·산업: 영업이익률이 FY2022 -8.5%에서 FY2025 31.6%로 올랐고(C:operating_margin@FY2025), 2026년 1분기 영업이익 7.5억(F1 — FY2022 영업이익률 −8.5%는 인용에 없다. FY2025 31.6%, 분기 영업이익, 47%는 일치한다.
- [leap] 슬레이터: 모델이 첫해 이후 감속을 너무 일찍 가정했을 수 있다. 미국 상업 매출이 전년 대비 +149%로 가속하고 있어, 3분기에 감속 대신 가속이 확인되면 기본 경로가  — 인용된 값은 매출 7.64억과 3분기 가이던스뿐이라, 이것만으로 미국 상업 성장이 가속 중이라고 단정할 수 없다.
- [unsupported] 애크먼: 레드팀의 사전 부검은 FCF 범위를 넓힌다. 특히 SBC 차감 FCF 마진이 FY2025 기준 31.7%로 보고 마진 46.9%보다 훨씬 낮다면, 주주 몫 FCF — 현재 마진 −68.3%와 약세 마진 40%는 인용한 자료로 확인되지 않는다. 주가와 기본 가치가 인용에 없다.
- [unsupported] 레드팀: 5년 매출 연 41%는 기저율 표가 없어 검증되지 않았다. 역DCF가 요구하는 10년 34~42% 성장은 역사적으로 거의 달성된 적이 없다. 첫해 82%(가이던스 — 10년 34~42% 성장이 역사적으로 거의 달성된 적 없다는 진술은 근거가 없다. 기저율 표가 없다고 스스로 밝히고 있다.
- [unsupported] 경영진·자본배분: SBC는 FY2021 7.8억에서 FY2025 6.8억으로 줄었다. 매출 대비로는 FY2021 50.5%에서 FY2025 15.3%로 크게 낮아져 개선 방향이다. — FY2021 SBC 7.8억과 희석 주식 수 19.2억·25.7억은 인용에 없다.
- [unsupported] 슬레이터: 실적은 진짜다. 매출 성장이 FY2023 16.7%에서 FY2025 56.2%로 가속했고, 2026년 2분기 매출은 전년 대비 +93%였다. 이 점은 반대 논거가 — FY2023 성장률 16.7%는 인용에 없다. FY2025 56.2%와 Q2 +93%는 일치한다.
- [unsupported] 회계 품질: SBC/매출 15.3%는 문턱 10%를 넘는다. 방향은 개선 중이다(FY2021 50.5%에서 하락). 그러나 SBC는 현금비용이 아니어도 실제 비용이다. 보고  — FY2021 SBC/매출 50.5%와 임계값은 인용에 없다. 15.3%, 32.0%, 14.2억은 일치한다.
- [leap] 슬레이터: 높은 성장을 그대로 반영해도 수익이 나오지 않는다. 기대 연 수익률은 -0.6%이고 손실 확률은 80%다. 기본 시나리오 수익률 분해에서 매출 성장 기여를 멀티플 — −0.6%와 손실 확률 80%는 맞다. 하지만 성장 기여와 멀티플 압축의 상쇄, 2022년 구간과의 유사성은 인용에서 따라 나오지 않는다.
- [unsupported] 회계 품질: 보도자료의 현금·단기 미국채 합계 92억 USD가 XBRL의 현금 20.3억 USD와 단기투자 73.8억 USD 합계와 정확히 맞지 않는다. 구성 차이일 가능성이 — 출처 없는 숫자 9.2e+09 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 경영진·자본배분: 자사주 매입은 FY2023까지 0이었고 FY2024 6,420만, FY2025 7,498만으로 시작됐다. 같은 해 SBC는 FY2024 6.9억, FY2025 6 — FY2023까지 자사주 매입이 0이었다는 내용은 인용에 없다. 나머지 수치는 일치한다.
- [unsupported] 사업·산업: 매출채권이 매출보다 빠르게 늘었다. DSO가 FY2022 49.5일에서 FY2025 85.0일로 길어졌고(C:dso@FY2025), 매출채권은 2026년 2분기  — FY2022 DSO 49.5일은 인용에 없고, 연초 이후 계속 늘었다는 것도 FY2026Q2 값 하나로는 알 수 없다.
- [unsupported] 회계 품질: 발생액 비율이 모든 연도에서 음수다(FY2025 -6.7%). 영업현금흐름이 순이익을 웃돈다(FY2025 FCF/순이익 1.29x). 이익이 현금으로 뒷받침된다. — 출처 없는 숫자 1.29 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 앤더슨: 재투자 여력이 구조적으로 크다. 영업이익률이 FY2022 -8.5%에서 FY2025 31.6%로 올랐고 FCF 마진은 46.9%다. 설비투자는 미미하고 부채는 없 — FY2022 영업이익률 −8.5%는 인용에 없다. 10년을 버틸 수 있다는 결론도 자료에서 따라 나오지 않는다.
- [unsupported] 앤더슨: 시장이 과소평가하는 지점은 꼬리의 크기다. 역DCF는 마진이 30%로만 수렴해도 매출이 연 42.0% 성장해야 한다고 말한다. 이것을 '불가능'이 아니라 '이미  — 최근 3년이 가속이었다는 근거로 FY2025 성장률 하나만 인용돼 있다.
- [unsupported] 사업·산업: 총이익률이 FY2021 78.0%에서 FY2025 82.4%로 유지·개선됐다(C:gross_margin@FY2025). 같은 기간 매출이 15.4억에서 44.8억 — FY2021 총이익률 78.0%는 인용에 없다. FY2025 82.4%와 매출 15.4억→44.8억은 일치한다.
- [unsupported] 애크먼: 기본 시나리오 수익률 분해에서 매출 성장 기여(+34.4%)를 멀티플 압축(-37.0%)이 전부 상쇄한다. 사업이 모델러의 기본 가정대로 성장해도 주주는 그 성장 — 출처 없는 숫자 37% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: FCF 마진 52%는 FY2025 값 46.9%를 넘어서는 가정인데, 같은 기간 SBC 증가(2.7억, 전년 1.6억)·DSO 85일·세율 정상화 위험이 모두 마 — 전년 SBC 1.6억은 인용에 없다. FCF 마진 46.9%와 SBC 차감 31.7%는 인용값으로 계산된다.
- [unsupported] 앤더슨: 사전 부검 2: 기본 시나리오조차 5년 수익률이 -0.9%다. 매출이 연 41%로 성장해도 멀티플 변화가 수익률을 -37.0% 깎는다. 성장이 사실이어도 가격이  — 출처 없는 숫자 37% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 앤더슨: 미국 상업 부문이 선행 지표다. 2분기 매출이 전년 대비 +149%, 잔여 계약가치가 +124%, TCV가 +153%로 매출보다 계약이 더 빨리 늘었다. 매출이  — 미국 상업 매출은 +149%인데 RDV는 +124%다. 계약이 매출보다 더 빨리 늘었다는 결론은 TCV에만 해당한다.
- [unsupported] 슬레이터: 애크먼의 가장 강한 논거는 기본 시나리오에서 매출 성장 기여(+34.4%)를 멀티플 압축(-37.0%)이 전부 상쇄한다는 것이다. 이 점은 전적으로 동의한다. 다 — 출처 없는 숫자 37% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 회계 품질: 코드 신호에 재무제표 정정이나 감사인 변경이 없다. 감사의견(계속기업 의문, 핵심감사사항)과 특수관계자 거래는 이번 입력에 없어 10-K·DEF 14A에서 확인해 — 영업권이 총자산 대비 미미하다는 진술에 영업권 수치가 인용되지 않았다. 부채 0과 총자산 116.8억만 있다.
- [unsupported] 모델러: 단기 펀더멘털(가이던스 상향, 미국 상업 가속)은 실제이고 기본 시나리오도 이를 따른다. 다만 5년 성장 경로가 시장 내재 성장에 못 미치고 출구 배수가 압축되므 — 기저율 표를 참조하라고 했지만 인용 자료에 기저율 표가 없고, 10년 40%대 성장이 거의 달성된 적 없다는 근거도 없다.
- [leap] 회계 품질: 이연매출이 매출 성장 이상으로 늘어(FY2026Q2 5.8억 USD) 수익 선인식의 반대 신호다. 그러나 매출채권도 같이 늘어(FY2026Q2 14.9억 USD) — 이연매출 5.8억과 매출채권 14.9억은 맞다. 하지만 매출 성장 이상으로 늘었다는 결론은 매출 성장률 없이는 따라 나오지 않는다.
- [unsupported] 레드팀: 멀티플 붕괴: 사업은 계획대로 성장했는데 주가만 −60%. 현재 P/FCF 142배(C:p_fcf)는 성장이 20%대로 내려오는 순간 성숙 소프트웨어 배수로 압축 — 출처 없는 숫자 37%, 5.6 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 앤더슨: 슬레이터의 가장 강한 논거는 NRR·CAC·이탈률이 없어 단위경제가 입증되지 않았다는 점이다. 고객 단위 지표가 비어 있는 것은 사실이다. 그러나 증거가 없는 것 — 미국 상업 매출은 +149%이고 RDV는 +124%다. 계약이 매출보다 빨리 늘고 있어 고객이 떠나는 모양이 아니라는 결론은 TCV에만 맞다.
- [unsupported] 회계 품질: FY2024 매출채권 증가율이 매출 증가율을 28.9%p 웃돈다. 문턱은 15%p다. DSO는 73.2일에서 85.0일(FY2025)로 길어졌고 매출채권은 FY2 — DSO 73.2일, 문턱 15%p, 순이익 대비 영업현금흐름 비교는 인용에 없다. 28.9%p, 85.0일, 매출채권, 이연매출은 일치한다.

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
| 주가 (price) | 186.03 USD/share (2026-10-16, F213) |
| 희석 주식 수 (shares) | 25.7억 |
| 시가총액 (market_cap) | 4,778.5억 USD |
| 순현금 (net_cash) | 94.1억 USD |
| EV (ev) | 4,684.5억 USD |
| FCF 수익률 (fcf_yield) | 0.7% |
| P/FCF (p_fcf) | 142.29x |
| EV/매출 (ev_revenue) | 76.10x |
| PER (pe) | 158.40x |
| 순부채/EBITDA (net_debt_to_ebitda) | -3.53x |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 15.3% > 10%
- [watch] receivables_gap (C:receivables_gap): FY2024 매출채권 증가율 - 매출 증가율 28.9% > 15%
- [watch] dilution (C:dilution): 희석 주식 수 연 7.5% 증가 > 3%

### 역DCF — 현재 가격이 가정하는 것

EV 4,684.5억 USD를 정당화하려면 매출이 10년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 목표 마진으로 직선 수렴, 할인율 10%, 이후 영구성장 3%.
기본 시나리오 목표 마진 52% 기준: 연 34.5% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 57.6% | C:implied_cagr@m10 |
| 15% | 51.8% | C:implied_cagr@m15 |
| 20% | 47.7% | C:implied_cagr@m20 |
| 25% | 44.6% | C:implied_cagr@m25 |
| 30% | 42.0% | C:implied_cagr@m30 |
| 52% | 34.5% | C:implied_cagr@m52 |

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 30% | 169.0억 USD | 30.4% | 40% | 22x | 62.17 | 38.60 | -19.7% |
| 기본 | 50% | 249.4억 USD | 41.0% | 52% | 35x | 178.06 | 110.56 | -0.9% |
| 강세 | 20% | 378.7억 USD | 53.3% | 55% | 45x | 362.93 | 225.35 | +14.3% |

확률 가중: 주당 가치 180.27 · IV 111.93 · 기대 연 수익률 -0.6% (C:expected_irr) · 손실 확률 80% (C:p_loss) · 현재 주가 186.03

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +34.4% · 마진 변화 +2.0% · 멀티플 변화 -37.0% · 주식 수 변화 -2.0% · 현금 축적 +1.7% = -0.9%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -10.2% | -5.6% | -1.7% |
| +0%p | -5.8% | -0.9% | +3.2% |
| +5%p | -1.3% | +3.9% | +8.2% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 81.5억 USD | 47.9% | 39.1억 USD | 26.2억 | 133.1억 USD |
| FY2027 | 122.2억 USD | 49.0% | 59.8억 USD | 26.7억 | 193.0억 USD |
| FY2028 | 164.9억 USD | 50.0% | 82.4억 USD | 27.3억 | 275.4억 USD |
| FY2029 | 207.8억 USD | 51.0% | 106.0억 USD | 27.8억 | 381.4억 USD |
| FY2030 | 249.4억 USD | 52.0% | 129.7억 USD | 28.4억 | 511.0억 USD |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 34.5% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 41.0% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 53.3% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=7.36x, revenue_5y=8.46x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=94.1억 USD
- 애크먼 case={"from": "base"}: price=186.0, fcf_positive=예, net_debt_to_ebitda=-3.53x, leveraged=아니오, intrinsic_value=110.6, mos=-68.3%

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
| S39 | data | 2026-10-16 | [Yahoo Finance PLTR historical prices](https://finance.yahoo.com/quote/PLTR/history/) | 2026-10-16 종가 186.03 USD |
| S40 | news | 2026-09-10 | [Palantir IR - Palantir](https://news.google.com/rss/articles/CBMijAJBVV95cUxQOEZaam1RNXZMbXduNGhDMFp1Ny0wLVVSSEhxZzBNVjZNTUNoS1EtZi12eThhRVB5YmxWdVVHNW9paU9PX050a1N2TlNfWV9peDI3VXdWOXNtU0FBX1NHa0pxU29MRl8yRm4xOFBxVjU2Z0pORzdFMVpFcVJPdEVLQTJxUU94b21Uakpvb1h3T2gyVGpuSVlETGpJdjM4b0Fsam0xbzlhM0prYmhUdGFVWDdlZVJIeHA1al9KZnVOdEx4WmJ1Rmd6a2dTWTZCclZQeWhfVXY3ZGFpaWtBcXdEOGd1VFdQQXc1Vm0tcURkSUlBUzdubEdFVjBZNGxGWjlDSGZXM2NoMXJydmFU?oc=5) | Palantir |
| S41 | news | 2026-10-16 | [Palantir Stock Is Near Its Record. Here's the Price at Which I'd Buy It. - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxOTTk4U0pIY1hvbm10MWk0R1dXRklid21vVWRrcmM4akVSM3g2c2J3SWd0Q1NUdjUwVWs3M3JCSEhrNV8wcFhTWmFRRC14Ym9JVEdyM2tLa1BkTWlOQms4YUdvRlV3Ml9JOVAyT2pCaVdOTFRORXNFYVZtWXJxeVctRGNJcG85MkItZGc0dncxUzJmMDUwS3VIVmY4NmxTQQ?oc=5) | Yahoo Finance |
| S42 | filing | 2026-08-03 | [Palantir Technologies Inc. - Form 8-K - FY2026 (Exhibit 99.1, Q2 2026 press release)](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm) | 2026 Q2 실적 보도자료(S2의 첨부). FY2026 가이던스 상향: 매출 81.50~81.58억 달러(기존 76.50~76.62억), 조정 FCF 45~47억 달러(기존 42~44억), 미국 상업 매출 34.24억 달러 초과, 조정 영업이익 48.89~48.97억 달러. 3분기 가이던스: 매출 21.60~21.64억 달러, 조정 영업이익 12.92~12.96억 달러. 2분기: 매출 약 19.4억 달러(전년 대비 +93%), GAAP 영업이익 9.12억 달러(마진 47%), 조정 FCF 12.20억 달러(마진 63%), 부채 없음, 100만 달러 이상 계약 220건(500만 달러 이상 98건). 미국 상업 매출 7.64억 달러(전년 대비 +149%, 전분기 대비 +28%), 미국 상업 잔여 계약가치(RDV) 62.38억 달러(+124%), 미국 상업 TCV 21.3억 달러(+153%). 수치는 검색 요약으로 확인했고 원문 대조는 하지 못함. |
| S43 | call | 2026-08-03 | [Palantir Technologies Q2 Earnings Call Highlights (Nasdaq)](https://www.nasdaq.com/articles/palantir-technologies-q2-earnings-call-highlights) | 2차 요약 자료. 어닝콜 원문은 확보하지 못했다. 보도된 발언: 카르프 CEO가 향후 18개월 동안 현재 미국 상업 성장률과 같거나 그 이상으로 회사를 성장시키겠다고 말함. 회사는 2026년 각 분기에 GAAP 영업이익·순이익이 흑자일 것으로 전망. 고객 수 +35%는 한 보도(pulse2)에서만 나왔고 잘려 있어 총 고객 수는 확인 못함. |

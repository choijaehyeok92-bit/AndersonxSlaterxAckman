# Pony AI (PONY) 리서치 보고서 — 기준일 2026-10-18

**팽팽** — 찬성 1 · 반대 1 · 보류 2 · 확신 가중 점수 -0.10 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓
- 조건부 판정: 주가 ≤ 2.35 (-52%) → 찬성 우세 (찬2·반1·보1)

## 1. Variant perception

- 시장 내재: 매출 10년 연 51.7% (FCF 마진 12% 수렴 가정) · 기본 시나리오: 6년 연 46.5%
- 시장이 반영한 것: 주가 US$4.93에서 EV는 C:ev 6.6억 USD로 낮고, 역DCF는 FCF 마진 20% 도달 시 연 38.1%(C:implied_cagr@m20), 10%라면 57.4%(C:implied_cagr@m10)의 10년 매출 성장을 요구한다. 시장은 로보택시 성공을 이미 크게 할인했고, 순현금을 거의 그대로 인정한다.
- 우리가 다르게 보는 점: 순현금은 보이는 값(C:net_cash)보다 질이 낮고, 성장이 현실화돼도 설비투자와 영업손실 때문에 주주 몫의 가치는 현금 소진 속도에 좌우된다. 우리 기본 시나리오의 매출 성장은 시장 내재 성장과 비슷해 방향성 알파는 없다. 차이는 현금 소진과 매출 질에 있다.
- 왜 우리가 맞는가: 유동성 US$1,390.5M(F123)에는 보호예수 중인 GPU 투자사 지분 US$138.8M(F175)이 2025년 말 기준으로 들어 있었고, 2분기 FCF는 −US$76.2M(F120), 설비투자는 US$32.2M(F119)으로 전년의 약 3.4배다. 매출채권도 상반기 US$23.6M(F52)에서 US$43.3M(F129)으로 늘었고 인도 매출 선인식 발언(S77)이 있어 로보택시 서비스 매출의 질이 불분명하다. [F123] [F175] [F120] [F119] [F52] [F129] [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [C:implied_cagr@m20] [C:implied_cagr@m10] [C:net_cash]
- 촉매: 2026년 3분기 실적(로보택시 매출·차량 수·설비투자·매출채권), 두바이 상용 출시, 연말 3,500대 달성 여부, 2026-12 무렵 보호예수 해제.
- 시점: 2026-11 ~ 2027-01
- 컨센서스 대비 revenue FY2026: +2.4% (1.5억 USD vs 1.4억 USD)
- 컨센서스 대비 revenue FY2027: -19.2% (2.4억 USD vs 2.9억 USD)
- 컨센서스 대비 revenue FY2028: -49.2% (3.6억 USD vs 7.0억 USD)

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **4.80** vs 주가 4.93 · 기대 연 수익률 **+9.5%** · 손실 확률 30%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 30% | 1.04 | 0.59 | -22.9% | 중국 1선 도시의 차량 단위 손익분기가 회사 주장에 그쳐 실제 가동률이 Waymo에 못 미치고(S87), 연말 3,500대 목표(F79)가 늦어진다. 해외 파트너 배치는 수익 배분이 작아 매출이 작게 남고, 로보트럭 |
| 기본 | 50% | 5.94 | 3.35 | +3.2% | 2026년은 상반기 흐름(F86, F76)과 CITIC 추정(F188)에 가깝게 간다. 이후 중국 1선 도시 차량 증가와 Uber 유럽 2,000대 배치(S75)가 로보택시 매출을 키우지만, 해외는 자산경량이라 매출 |
| 강세 | 20% | 26.12 | 14.75 | +32.0% | Gen-7 원가 절감과 완전 무인 허가 확대(S92, S93)로 중국 4개 1선 도시와 두바이·유럽에서 차량당 주문이 늘어 차량 단위경제가 회사 수준 흑자로 이어진다. Uber 외 Bolt 등 플랫폼 채널(S77)이 |

## 3. 반증 조건 (thesis break)

- [대기 — FY2026 미발표] 앤더슨: 연말 로보택시 3,500대 목표 미달 — `robotaxi_fleet < 3500` (FY2026)
- [대기 — FY2026Q3 미발표] 앤더슨: 3분기 로보택시 매출이 2분기보다 줄면 성장 가설 훼손 — `robotaxi_revenue < 1.21e+07` (FY2026Q3)
- [수동 확인] 앤더슨: 차량당 단위경제가 흑자로 돌아선다는 공시 없이 추가 증자가 반복됨 — 수동 확인
- [대기 — FY2026 미발표] 슬레이터: 연말 로보택시 3,500대 목표 미달 — `robotaxi_fleet < 3500` (FY2026)
- [대기 — FY2026Q3 미발표] 슬레이터: 3분기 로보택시 매출이 2분기 수준 밑으로 후퇴 — `robotaxi_revenue < 1.2e+07` (FY2026Q3)
- [수동 확인] 슬레이터: 차량 확장을 위해 대규모 외부 조달이 필요해졌다는 공시 — 수동 확인
- [대기 — FY2026Q3 미발표] 애크먼: FY2026Q3 매출이 6,000만 USD 이상이면 성장 경로가 내 가정보다 훨씬 강하다 — `revenue >= 6e+07` (FY2026Q3)
- [미충족] 애크먼: 주가가 기본 시나리오 현재가치 대비 안전마진 20%를 확보하는 수준까지 내려오면 가격 반론이 사라진다 (FCF 음수 반론은 남는다) — `price <= 2.7`
- [수동 확인] 애크먼: TTM FCF가 흑자로 돌아서고 해외 차량 자금을 파트너가 전액 부담하는 구조가 공시로 확인되면 재검토 — 수동 확인
- [대기 — FY2026Q3 미발표] 클라만: 3분기 말 회사 유동성이 12억 달러 아래로 내려가면 순현금이 바닥 가치로 기능하지 못한다 — `total_liquidity < 1.2e+09` (FY2026Q3)
- [대기 — FY2026Q3 미발표] 클라만: 3분기 FCF 유출이 1억 달러를 넘으면 현금 소진 속도가 가정보다 빠르다 — `fcf < -1e+08` (FY2026Q3)
- [수동 확인] 클라만: 후속 공모·전환사채 등 외부 조달 공시 — 수동 확인
- [미충족] 레드팀: 분기 설비투자 US$40M 초과 — 차량 직접 소유 부담이 하반기 증차로 가속 중 — `capex > 4e+07`
- [미충족] 레드팀: 총이익률이 15% 밑으로 후퇴 — 구성 효과가 사라지고 가격 경쟁이 시작됨 — `gross_margin < 0.15`
- [미충족] 레드팀: 매출채권 US$60M 초과 — 매출 증가보다 채권 증가가 빨라 매출 질 악화 — `receivables > 6e+07`
- [대기 — FY2026 미발표] 레드팀: 차량 수가 3,000대 밑에서 정체 — 연말 3,500대 목표 실패, 확장 속도 문제 — `robotaxi_fleet < 3000`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | revenue | FY2026Q3 | >= 4e+07 | 60% | 2분기 3,620만 USD(F76)에서 분기 매출이 더 늘어 기본 시나리오의 2026년 성장 경로가 유지되는지 시험한다. |
| K2 | robotaxi_revenue | FY2026Q3 | >= 1.6e+07 | 55% | 2분기 1,210만 USD(F77)에서 차량 증가가 매출로 이어지는지, 가동 효율을 시험한다. |
| K3 | gross_margin | FY2026Q3 | >= 0.17 | 55% | 2분기 총이익률 17.5%(F102)가 구성 효과인지 구조적 개선인지, 즉 원가 우위 가설을 시험한다. |
| K4 | revenue | FY2026 | >= 1.45e+08 | 55% | 연간 매출이 CITIC 추정(F188)과 상반기 흐름대로 가는지로 기본 시나리오 첫 해를 시험한다. |
| K5 | robotaxi_fleet | FY2026 | >= 3500 | 50% | 연말 3,500대 가이던스(F79)로 경영진 가이던스 신뢰도와 인허가·공급 속도를 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.10 · 비중 참고값 0.0% (팽팽 — 신규 비중 없음) · 슬레이터 시작 비중 0.5%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 6. 조건부 판정 — 이 가격 이하라면

가치(내재가치·10년 가치·단단한 가치)는 그대로 두고 가격에 걸린 지표만 다시 계산해, 주가가 각 페르소나의 조건 가격까지 내려왔을 때의 표결을 본다. 주가를 예측하는 것이 아니다.

| 주가 | 현재가 대비 | 표 | 판정 | 이 가격이 조건인 페르소나 |
|---|---|---|---|---|
| 4.93 | 현재가 | 찬1·반1·보2 | 팽팽 |  |
| 2.35 | -52% | 찬2·반1·보1 | 찬성 우세 | 클라만 |

클라만의 세 질문 (코드 계산):

- 성장 전망이 틀리면 어디까지? 단단한 가치 주당 3.42 (순현금) — 현재가에서 -30.6% · 내재가치 범위(약세~기본) 0.59~3.35 · 순현금 3.42 · 성장 없는 현금흐름 가치 3.42
- 현재 가격에 성장이 얼마나 들어 있나? 주가의 31%가 성장 없는 가치(3.42) 위의 몫 · 시장 내재 매출 성장 연 51.7%
- 기다리면 더 싼 가격이 오나? 조건 가격 2.35 · 지난 52주 범위 4.90~22.46 — 그 기간에 조건 가격 이하로 내려간 적이 없다 — 가격은 예측하지 않는다, 기록만 본다

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 0/5 실패 | founder_led=예, upside_10y=20.49x, revenue_5y=13.60x, value_10y=101.0, buy_below=20.2 |
| 슬레이터 | 보류 → 보류 | 2/5 | ✗ 기본 시나리오에서 현금 고갈 (코드 계산) | 0/5 실패 | unit_economics=unclear, starter_weight=0.5%, cash_survives=아니오, cash_min=-9,134만 USD, runway_years=7.1 |
| 애크먼 | 반대 → 반대 | 5/5 | ✗ 단순·예측 가능한 사업이 아님; 잉여현금흐름을 만들지 못함 (코드 계산); 레버리지·자본시장 의존; 안전마진 20% 미만 또는 계산 불가 | 1/5 실패 | simple_predictable=아니오, capital_markets_dependent=예, catalyst=없음 — 창업자 의결권 70.0%라 이사회 교체·분사 등 외부 촉매를 만들 수 없다, fcf_positive=아니오, leveraged=아니오, intrinsic_value=3.4, mos=-46.9%, buy_below=2.7 |
| 클라만 | 조건부 찬성 → 보류 (조건 가격 2.3 위) | 3/5 | ✗ 보수적 내재가치 대비 안전마진 30% 미만 또는 계산 불가 | 0/5 실패 | inefficiency=neglect, intrinsic_value=3.4, iv_low=0.6, iv_high=3.4, hard_value=3.4, no_growth_ps=3.4, downside=30.6%, growth_premium=30.6%, mos=-46.9%, buy_below=2.3, low_52w=4.9, traded_below_52w=아니오, leveraged=아니오, fcf_positive=아니오, net_cash_ps=3.4, owner_fcf=-2.4억 USD, hard_basis=net_cash_ps, high_52w=22.5 |

- ⚠ 앤더슨: arguments[1]: 인용하지 않은 근거의 숫자 3000(F140·S63·S64) — cites에 추가
- ⚠ 앤더슨: rebuttals[1]: 인용하지 않은 근거의 숫자 10%(C:discount_rate·C:expected_irr·C:fcf_yield) — cites에 추가
- ⚠ 앤더슨: arguments[3]: 인용하지 않은 근거의 숫자 52(S52·S89) — cites에 추가
- ⚠ 애크먼: arguments[1] unsupported: FCF 마진 −232%, 2분기 FCF −76.2M, 설비투자 3.4배는 맞지만, 차량 목표를 채우려면 국내 차량을 직접 소유해야 한다는 내용은 인용 자료에 없다.
- ⚠ 애크먼: rebuttals[2]: 인용하지 않은 근거의 숫자 30.6%(C:downside@klarman·C:growth_premium@klarman), 2.3(C:buy_below@klarman) — cites에 추가
- ⚠ 애크먼: arguments[0]: 인용하지 않은 근거의 숫자 10%(C:discount_rate·C:expected_irr·C:fcf_yield) — cites에 추가
- ⚠ 애크먼: risks[1]: 인용하지 않은 근거의 숫자 52(S52·S89) — cites에 추가
- ⚠ 애크먼: rebuttals[3]: 인용하지 않은 근거의 숫자 12%(C:fcf_margin@base·S70) — cites에 추가
- ⚠ 클라만: rebuttals[2]: 인용하지 않은 근거의 숫자 4.93(C:price·C:price@ackman·C:price@anderson), 70%(F158·S64·S66) — cites에 추가
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 회계 품질 findings[4]: 인용하지 않은 근거의 숫자 9e+06(C:fcf@bear·C:sbc@FY2026Q2·F108) — cites에 추가
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): 출처 없는 숫자 7500, 1.6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[5] 검증 실패(unsupported): 차량 1,975대, 3,500대 목표, 3.4배 설비투자는 맞지만, 인용 자료 어디에도 국내 차량이 회사 소유라는 내용은 없다.
- ⚠ 경영진·자본배분 findings[1] 검증 실패(contradicted): 지분율·의결권은 맞지만 S90의 3개월 내부자 매도는 41,700주로 VP·CFO 두 건 합계(약 29,275주)보다 커서 '그 두 건뿐'이라는 말과 어긋난다.
- ⚠ 경영진·자본배분 findings[4] 검증 실패(unsupported): 출처 없는 숫자 3.8 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 레드팀 weakest[2] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base
- ⚠ 경영진·자본배분 findings[7]: 인용하지 않은 근거의 숫자 52(S52·S89) — cites에 추가

## 앤더슨 — 찬성 (3/5)

> Pony AI는 창업자가 의결권 과반을 쥐고 경제적 지분도 상당한 로보택시 플랫폼이다. 2분기 매출은 +68.8%, 로보택시 서비스는 +691.2%로 가속하고 있다. 멱법칙의 관점에서 질문은 '지금 흑자인가'가 아니라 '5년 안에 매출이 두 배 이상이 되고 10년 뒤 5배가 될 길이 있는가'다. 강세 시나리오를 10년으로 늘린 코드 계산값은 현재가 대비 20.49배로 레드라인 5배를 크게 넘고, 5년 매출은 13.6배다. 주가는 52주 고점에서 크게 내려 4.93달러이고, 현금과 투자자산이 시가총액의 상당 부분을 받친다. 반면 이 판단은 성장 가설 하나에 걸려 있다. 강세 시나리오 확률은 20%이고 약세 시나리오의 손실 확률은 30%이며, 차량 단위경제와 매출의 질은 아직 입증되지 않았다. 그래서 확신은 3으로 제한하고, 매도 논거는 주가 하락이 아니라 성장 가설의 훼손(차량·로보택시 매출 미달)으로만 둔다.

*이전 판단 대비: 입장(찬성)과 확신(3)은 직전 판단과 같다. 주가가 F74의 7.29달러에서 F80의 4.93달러로 내렸지만 이는 논거가 아니며, 성장 가설을 바꾸는 새 근거는 없다.*

**논거**
- 창업자 시간 지평: CEO 펑쥔이 경제적 지분 13.8%, 의결권 51.6%를 쥐고 있고 CTO까지 합치면 의결권이 크다. 분기 압박에 포획된 전문경영인이 아니라 장기 재투자를 결정할 수 있는 구조이며, 경제적 지분이 커서 이해관계도 주주와 맞닿아 있다. [S66](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#major-shareholders) [F150] [F151] [F152] [F153]
- 수확체증의 초기 흔적: 2분기 총매출은 +68.8%, 로보택시 서비스 매출은 +691.2%, 요금 징수 매출은 +849.3%다. 로보택시는 아직 매출의 약 1/3이지만 성장의 중심이 되고 있다. 연말 로보택시 3,500대 목표는 3월의 3,000대에서 상향됐고, 2분기 말 차량은 1,975대다. [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [F99] [F78] [F79]
- 5배의 길: 모델러의 강세 시나리오(연 63.4% 성장, FCF 마진 25%)를 10년으로 늘린 코드 계산값은 현재가 대비 20.49배, 5년 매출은 13.6배다. 5배 레드라인과 2배 기준을 넉넉히 넘는다. 강세의 전제는 차량 단위경제의 흑자가 회사 수준으로 이어지는 것이다. [C:upside_10y@anderson] [C:revenue_5y@anderson] [C:revenue_cagr@bull] [C:fcf_margin@bull]
- 시장이 과소평가하는 이유(질문 9): 기본 시나리오의 연 수익률은 +3.2%에 그치지만 강세는 +32.0%이고 확률 가중 기대 연 수익률은 +9.5%다. 분포는 오른쪽으로 길다. 주가가 52주 고점 대비 크게 내려 EV가 낮아졌고, 단기 가동률·매출 질에 대한 우려가 길게 보는 성장 가치를 눌러 놓았다. 이 우려가 맞는지는 3분기 실적에서 일부 확인된다. [C:irr@base] [C:irr@bull] [C:expected_irr] [C:ev] [F80] [F92]
- 존립 위험이 낮아 시간을 살 수 있다: 회사 유동성은 US$1,390.5M이고 차입금이 없다. 코드 계산 현금 소진 연수는 7.1년이다. 아웃라이어를 되기 전에 들고 있으려면 중간에 증자로 꺾이지 않아야 하는데, 지금은 그 여유가 있다. [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [C:runway_years]

**사전 부검**
- 사전 부검 1 — 성장 가설 자체가 깨진 경우: 차량 단위 손익분기는 회사 주장일 뿐 일일 주문·가동률·회수기간이 공시되지 않았다. Bloomberg Intelligence는 중국 로보택시 가동률이 Waymo에 못 미쳐 손실을 본다고 지적했다. 차량이 늘어도 매출이 따라오지 않으면 강세 시나리오는 성립하지 않는다. [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) [S76](https://www.benzinga.com/news/26/08/61272470) [S87](https://www.bloomberg.com/news/articles/2026-10-02/china-robotaxis-face-losses-as-utilization-trails-waymo-bi-says)
- 사전 부검 2 — 매출의 질: 로보트럭 매출은 특수관계자 Sinotrans에 크게 기대고 있고(FY2025 매출의 약 33%), 해외 공동 배치는 차량 인도 매출을 선인식한다는 CFO 발언이 있다. 로보택시 '서비스' 매출 +691.2%가 순수 요금 성장이 아닐 수 있다. 이 경우 성장률이 과대 평가된 것이다. [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins)
- 사전 부검 3 — 원가 우위 부재와 자본 소진: 총이익률 17.5%는 경쟁사 WeRide의 37.5%보다 낮아 원가 우위의 흔적이 없다. 국내 차량은 직접 소유라 2분기 설비투자 US$32.2M, FCF −US$76.2M으로 소진이 빨라지고 있다. 주가가 홍콩 공모가보다 크게 낮은 상태에서 증자하면 희석이 커진다. [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S84](https://www.sec.gov/Archives/edgar/data/0001867729/000110465926094571/tm2622690d2_ex99-1.htm) [F119] [F120] [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s)

**반론**
- → 슬레이터: 슬레이터의 가장 강한 논거는 차량 단위경제가 회사 주장뿐이라 매출의 질을 입증할 수 없다는 점이다. 이 지적은 옳다. 그러나 3분기 실적으로 증거가 확인된 뒤 작게 시작하면, 이 회사의 가장 가치 있는 구간이 이미 주가에 반영된 뒤일 수 있다. 로보택시 서비스 매출은 +691.2%로 가속하고 있고 연말 차량 목표는 3월보다 올라갔다. 증거는 아직 완성되지 않았지만 방향은 나오기 시작했다. 증거를 기다리는 비용은 놓친 상방이다. 슬레이터가 요구한 3분기 로보택시 매출과 차량 수는 내 반증 조건과 겹치므로, 같은 시험을 보되 나는 시험 전에 비중을 작게 시작해도 된다고 본다. [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) [S63](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#guidance-operations) [F79]
- → 애크먼: 애크먼의 가장 강한 논거는 FCF가 음수이고 마진이 10%인지 30%인지조차 증거가 없어 예측이 불가능하다는 점이다. 그러나 이 범위의 넓이가 곧 기회의 크기다. 역DCF로 보면 시장은 FCF 마진 20%에서 연 38.1%의 성장만 요구하는데, 내 강세 case는 연 63.4% 성장을 둔다. 예측하기 어렵다는 이유로 분포의 오른쪽 꼬리를 버리면 아웃라이어를 영영 사지 못한다. 가격이 기본 시나리오 내재가치보다 비싸다는 지적은 인정한다. 다만 안전마진은 내 레드라인이 아니고, 내 질문은 10년 뒤 5배의 길이 보이는가다. [C:implied_cagr@m20] [C:implied_cagr@m10] [C:implied_cagr@m30] [C:revenue_cagr@bull] [C:upside_10y@anderson]
- → 클라만: 클라만의 가장 강한 논거는 하방 30.6%가 정적 값이라 순현금이 줄면 바닥이 내려간다는 점이다. 이 지적은 옳고, 나도 순현금의 질이 겉보기보다 낮다고 본다. 그러나 성장 없는 가치로 이 회사를 재면 주가 중 성장 몫이 30.6%로 보이는 반면, 확률 가중 기대 연 수익률은 +9.5%이고 강세 case는 +32.0%다. 안전마진 음수는 성장 옵션의 값을 치르는 것이지 영구 손실의 증거가 아니다. 손실은 100%로 막혀 있고 상승은 열려 있다는 비대칭에서, 놓친 상방도 손실이다. [C:growth_premium@klarman] [C:downside@klarman] [C:expected_irr] [C:irr@bull] [C:mos@klarman]
- → 레드팀: 레드팀의 사전 부검 네 개를 성장 가설을 깨는 것과 경로의 소음으로 가른다. 차량 3,000대 밑 정체는 확장 속도 자체가 깨지는 것이라 내 반증 조건에 이미 들어 있다. 설비투자 증가와 희석은 규모를 키우는 비용이라 가설을 깨지 않는다. 다만 이 비용이 증자로 이어지는 경로는 소음이 아니다. 보호예수 해제와 홍콩 주가 약세가 겹치면 시간을 살 수 있다는 내 논거가 약해진다. Sinotrans 의존과 인도 매출 선인식은 성장률 자체를 과대평가했을 가능성을 만들므로 가설을 직접 겨냥한다. 이 둘이 3분기 이후 공시로 확인되면 입장을 바꾼다. [S63](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#guidance-operations) [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity)

**인정한 점**
- 슬레이터: 단위경제는 회사 주장뿐이고 매출의 질이 입증되지 않았다. 인정한다. 그래서 확신은 5가 아니라 3에 묶고, 3분기 로보택시 매출과 차량 수를 반증 조건으로 단다.
- 애크먼: 기본 시나리오 연 수익률은 +3.2%에 그치고 안전마진이 없다. 기대 수익의 대부분은 강세 case에서 나온다. 이는 복권 같은 분포이므로 비중은 작게 시작해야 한다는 데 동의한다. 비중은 사람이 정한다.
- 클라만: 순현금은 보호예수 지분과 장기투자까지 들어간 넓은 정의라 질이 낮고, 바닥은 움직인다. 현금 소진이 빨라지면 내 존립 여유 논거가 약해진다.
- 레드팀: 기저율 표가 없어 강세 case의 연 63.4% 성장은 검증되지 않았다. 드문 일에 거는 것은 내 철학이지만 드물다는 사실을 숨기지 않는다. 입장은 유지하되 확신을 올리지 않는다.


## 슬레이터 — 보류 (2/5)

> 시장의 천장은 높고 성장 증거도 나오기 시작했지만, 아직 계획인 것과 실적인 것을 가르면 실적이 부족하다. 로보택시 매출은 빠르게 늘지만 전체 매출의 약 1/3이다. 차량 단위 손익분기는 회사 주장뿐이고 일일 주문·가동률·회수기간이 공시되지 않았다. 코드가 계산한 기본 시나리오 현금 경로는 외부 조달 없이는 뒤쪽 연도에 0 아래로 내려간다. 국내 차량을 직접 소유해 설비투자가 늘고 있는데, 이 부담이 매출 성장보다 빨리 커지는지는 3분기에 처음 확인된다. 생존 경로를 참/거짓으로 단정할 근거도, 단위경제가 입증됐다고 말할 근거도 없다. 그래서 찬성하지 않고 보류한다. 3분기 실적에서 차량 증가가 로보택시 매출과 총이익률로 이어지면 작은 시작 비중으로 다시 볼 수 있다. 가설이 틀렸다고 보는 것은 아니다. 증거가 아직 부족할 뿐이다.

*이전 판단 대비: 직전 판단과 같은 입장(보류, 확신 2). 새로 확인된 근거가 없어 변경 사유는 없다.*

**논거**
- 크기: 중국 1선 도시에 더해 Uber와 유럽 2,000대 이상 배치가 계약됐고 연말 도시 20개 이상이 목표다. 시장이 정의되지 않았다는 점은 슬레이터의 관심사에 맞는다. 다만 Uber 계약은 수익 배분·독점·기간이 비공개라 아직 계획 단계다. [S75](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926096218/tm2623123d1_ex99-1.htm) [F141] [F79]
- 지속성: 로보택시 서비스 매출은 2분기 US$12.07M으로 +691.2%이고 총매출은 +68.8%다. 성장은 실제다. 그러나 로보택시는 2분기 매출의 약 1/3이다. 나머지 intelligent solutions는 약 +4%에 그치고 로보트럭은 특수관계자 Sinotrans에 크게 기댄다. 성장의 지속성은 로보택시 한 갈래가 지고 있다. [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [F77] [F94]
- 단위경제 역산: 선전 Gen-7의 차량당 하루 순매출 RMB338은 회사 자체 수치다. 노트 추정으로 3,500대가 이 수준이면 요금 매출은 연 약 US$60M으로, Non-GAAP 영업비용 연 약 US$250M에 크게 못 미친다. 차량 단위 손익분기가 회사 손익분기로 이어지려면 가동률과 요금이 훨씬 올라야 한다. 지금 공시로는 이 조건이 입증되지 않았다. [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S76](https://www.benzinga.com/news/26/08/61272470)
- 생존: 유동성은 US$1,390.5M이고 차입금이 없어 당장의 위험은 낮다. 그러나 2분기 FCF는 −US$76.2M이고 설비투자는 전년의 약 3.4배다. 코드의 기본 시나리오 현금 경로는 외부 자본 없이는 뒤쪽 연도에 0 아래로 내려간다. 해외 자산경량 모델이 이 간극을 메울지는 파트너 배분 조건에 달려 있고 비공개다. 그래서 생존 경로를 단정하지 않는다. [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [F123] [F120] [F119] [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model)
- 매출의 질: 매출채권이 상반기에 약 83% 늘었다. CFO는 해외 공동 배치에서 차량 인도 매출을 선인식한다고 밝혔다. 로보택시 서비스 매출이 순수 요금 매출인지 확인되지 않는다. 증거로 키운다는 원칙에서, 질이 불분명한 증거로는 비중을 늘릴 수 없다. [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [F52] [F129]

**사전 부검**
- 사전 부검: 차량은 늘었는데 가동률이 Waymo에 못 미쳐 차량당 매출이 오르지 않는다. 설비투자만 늘고 로보택시 매출이 제자리면 현금이 예상보다 빨리 줄고, 이미 낮은 주가에서 증자하면 희석이 크다. [S87](https://www.bloomberg.com/news/articles/2026-10-02/china-robotaxis-face-losses-as-utilization-trails-waymo-bi-says) [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity)
- 사전 부검: 로보트럭 성장이 독립 수요가 아니라 특수관계자 Sinotrans 거래 한도 상향에 따른 것이었고, 한도 밖에서 정체한다. 총매출 성장률이 급락하고 총이익률 개선도 구성 효과였음이 드러난다. [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm) [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins)
- 사전 부검: 현금성 자산에 포함된 보호예수 지분의 평가가 꺼지거나 유동성이 회사 정의보다 좁게 드러나, 믿던 런웨이가 짧아진다. [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [F175]

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 강세 시나리오의 10년 가치가 현재가의 20.49배라는 계산값이다. 나도 시장의 천장이 높다는 데는 동의한다. 하지만 그 5배는 차량 단위경제가 회사 수준 흑자로 이어진다는 가정에 통째로 걸려 있고, 아직 계획이지 실적이 아니다. 단위경제 개선은 회사 자체 주장이고 가동률은 공시되지 않았다. 강세 시나리오는 차량 확대 때문에 현금을 오히려 더 많이 쓰는 경로이기도 하다. 기본 시나리오에서는 코드가 계산한 현금 경로가 뒤쪽 연도에 0 아래로 내려간다. 그래서 '런웨이 7.1년이라 시간을 살 수 있다'는 말에 기대지 않는다. 그 런웨이는 순현금 정의가 넓고 소진 속도가 오르는 중이라 과대평가일 수 있다. 증거가 쌓이기 전에는 앤더슨처럼 찬성으로 가지 않는다. [C:upside_10y@anderson] [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) [S76](https://www.benzinga.com/news/26/08/61272470) [C:runway_years] [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [F119]
- → 애크먼: 애크먼의 가장 강한 논거는 FCF가 음수이고 설비투자가 늘고 있으며 기본 시나리오 가치가 주가에 못 미친다는 것이다. 이 사실에는 동의한다. 다만 오늘 10년 FCF를 모델링할 수 없다는 이유로 정의되지 않은 시장을 영구히 버리는 데는 동의하지 않는다. 그래서 against가 아니라 abstain이다. 차이는 이것이다. 나는 가격이 아무리 내려가도 사지 않는다고 하지 않고, 3분기에 차량 증가가 로보택시 매출과 총이익률로 이어지는지 증거를 본 뒤 작게 시작할 수 있다고 본다. 지금은 그 증거가 없어서 시작 비중이 거의 0이다. [C:fcf_margin@FY2025] [F120] [C:iv@base] [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S63](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#guidance-operations)
- → 클라만: 클라만의 가장 강한 논거는 하방 30.6%가 정적인 값이라 낙관적이고, 순현금에는 보호예수 지분과 장기투자가 섞여 있다는 것이다. 동의한다. 이 지점에서 나는 클라만과 같은 쪽에 선다. 다만 조건 가격 2.3달러까지 기다렸다 한 번에 사는 방식에는 동의하지 않는다. 하방이 넓다는 문제는 사지 않는 것이 아니라 작게 시작해 증거로 키우는 것으로 푼다. 지금 시작하지 않는 이유는 가격이 아니라 매출의 질이 불분명하다는 점이다. 매출채권 증가와 차량 인도 매출 선인식 발언이 그 근거다. [C:downside@klarman] [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [F175] [C:buy_below@klarman] [F129] [F52] [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model)
- → 레드팀: 레드팀의 가장 강한 논거는 매출의 질 붕괴다. 로보트럭 매출이 특수관계자 Sinotrans에 크게 기대고, 해외 로보택시 서비스 매출에 차량 인도 선인식이 섞였을 수 있으며, 매출채권이 상반기에 크게 늘었다는 점이다. 이 중 어느 것도 반박할 수 없다. 오히려 내 1라운드 must_be_true에 이 선행 신호가 없었다. 레드팀의 매출채권 문턱과 분기 설비투자 문턱은 가설이 깨지는 사건이 아니라 의심이 커지는 신호이므로, 3분기 6-K에서 매출채권과 설비투자를 가장 먼저 확인한다. 매출채권이 매출보다 빨리 늘면 시작 비중을 올리지 않는다. [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [F129] [F52] [F119]

**참이어야 하는 것**
- [at_risk] 연말 로보택시 3,500대 달성
- [at_risk] 3분기 로보택시 매출이 2분기 수준을 넘어 1,600만 달러 이상
- [on_track] 3분기 총이익률이 17% 이상 유지
- [at_risk] 3분기 FCF 적자가 2분기보다 커지지 않음

**인정한 점**
- 애크먼과 클라만이 짚은 현금 소진과 순현금의 질 문제를 인정한다. 이는 survival_path를 true로 단정하지 못하는 이유를 강화하며, 코드의 기본 시나리오 현금 경로가 0 아래로 내려가므로 찬성으로 갈 수 없다.
- 레드팀이 지적한 매출의 질 위험(Sinotrans 의존, 인도 매출 선인식, 매출채권 급증)을 인정한다. 3분기 확인 항목에 매출채권과 설비투자를 추가한다.
- 앤더슨의 오른쪽으로 긴 분포는 인정하지만, 그 상방이 입증되지 않은 가정에 달려 있어 확신을 올리지는 않는다. 입장과 확신 2는 1라운드와 같다.


## 애크먼 — 반대 (5/5)

> 사업은 한 문단으로 설명되지만 10년 뒤 FCF를 합리적 범위로 추정할 수 없다. 로보택시가 확산되는지, 매출 상당 부분이 특수관계자에서 나오는 로보트럭이 독립 수요를 얻는지에 따라 결과가 갈린다. 지금은 FCF가 음수이고 설비투자가 늘고 있어 성장 자금을 보유 현금 소진에 기댄다. 가격도 보수적 case의 내재가치보다 비싸서 안전마진이 없다. 현금이 많고 차입이 없어 파산 위험은 낮지만, 그것이 '단순하고 예측 가능하며 현금을 뿜는 지배적 사업'이라는 기준을 채우지는 않는다. 지배적 해자는 아직 증거 없이 회사 주장에 그친다. 창업자가 의결권을 쥐고 있어 내가 촉매를 만들 수도 없다. 가격이 아무리 내려가도 FCF 음수와 예측 불가능성은 그대로이므로 조건부가 아니라 반대다.

**논거**
- 10년 FCF 범위를 좁힐 수 없다. 역DCF가 요구하는 매출 성장이 목표 FCF 마진에 따라 마진 10%면 연 57.4%, 30%면 연 29.1%로 크게 갈린다. 마진이 얼마가 될지조차 증거가 없다는 뜻이고, 이것이 단순성·예측 가능성 기준의 실패다. [C:implied_cagr@m10] [C:implied_cagr@m30]
- FCF가 음수이고 악화 중이다. FY2025 FCF 마진은 -232.0%이고, 2026년 2분기 Non-GAAP FCF는 -US$76.2M이다. 설비투자는 전년의 약 3.4배로 늘었다. 연말 차량 목표를 채우려면 국내 차량을 직접 소유해야 하므로 현금 소진은 더 빨라질 가능성이 크다. [C:fcf_margin@FY2025] [F120] [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S63](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#guidance-operations)
- 안전마진이 없다. 기본 시나리오의 현재가치는 3.35인데 주가는 4.93이다. 기본 시나리오 연 수익률은 +3.2%이고, 손실 확률은 30%다. 기대 수익이 할인율을 넘기는 하지만 그 대부분이 20% 확률의 강세 시나리오에서 나온다. 그건 안전마진이 아니라 복권이다. [C:iv@base] [F80] [C:irr@base] [C:p_loss] [C:expected_irr]
- 매출의 질과 지배구조가 불투명하다. 로보트럭 자회사의 비지배주주인 특수관계자 Sinotrans가 FY2025 매출의 약 33%이고 2026-08-25에 거래 한도가 상향됐다. 창업자 두 명의 의결권이 합쳐서 크고 이사·임원 전체 의결권은 70.0%다. 소액주주는 자본배분을 바꿀 수 없으니 행동주의 촉매가 없다. [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm) [F158] [S66](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#major-shareholders)
- 지배적 해자의 증거가 없다. 총이익률은 17.5%로, 매출 규모가 비슷한 WeRide의 37.5%보다 낮다. Uber는 경쟁사들과도 일하며 수익 배분·독점·기간이 비공개라 전환비용도 입증되지 않았다. 무인 허가는 경쟁사도 받고 있어 가격결정력의 흔적이 없다. [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S84](https://www.sec.gov/Archives/edgar/data/0001867729/000110465926094571/tm2622690d2_ex99-1.htm) [S75](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926096218/tm2623123d1_ex99-1.htm) [S92](https://www.benzinga.com/markets/tech/25/07/46656199/pony-ai-gets-green-light-for-driverless-robotaxis-in-shanghais-pudong)

**사전 부검**
- 사전 부검: 내가 틀렸다면 Uber·Bolt 등 플랫폼 채널과 자산경량 해외 배치가 예상보다 빨리 매출로 이어지고 차량 단위경제가 규모에서 재현돼, 마진이 강세 시나리오 쪽으로 가는 경우다. 그때는 현재 주가가 너무 싼 값이 된다. [S75](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926096218/tm2623123d1_ex99-1.htm) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/)
- 사전 부검: 시장이 이미 사업 가치를 크게 할인했을 수 있다. EV가 매출 대비 낮고 52주 신저가 부근이라 과매도일 수 있다. 내가 FCF 음수라는 원칙에 묶여 가격이 충분히 싼 구간을 놓칠 위험이 있다. [C:ev] [F91] [F80]
- 사전 부검: 현금이 두껍고 차입이 없어 자본시장 의존도를 과대평가했을 수 있다. 회사 유동성이 크므로 한동안 증자 없이 버틸 수 있다. 다만 그 현금에는 보호예수 중인 GPU 투자사 지분이 일부 섞여 있어 질이 낮다. [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [F175]

**반론**
- → 앤더슨: 20.49배는 강세 시나리오 하나(확률 20%)를 10년으로 늘린 값이다. 기본 시나리오 연 수익률은 +3.2%이고 손실 확률은 30%다. 역DCF가 요구하는 성장도 마진 가정에 따라 크게 갈리므로 어떤 마진이 맞는지 증거가 없다. 생존자 편향에 기댄 복권이지 안전마진이 아니다. [C:upside_10y@anderson] [C:irr@base] [C:p_loss] [C:implied_cagr@m10] [C:implied_cagr@m30]
- → 슬레이터: 보류는 증거가 쌓이면 사겠다는 뜻인데, 필요조건인 생존 경로와 단위경제를 통과해도 가격과 FCF 문제가 남는다. 기본 시나리오 현재가치는 주가보다 낮고 FCF는 음수다. 슬레이터가 직접 든 must_be_true 4개 중 3개가 at_risk라면 보류보다 반대가 일관적이다. [C:iv@base] [F80] [F120] [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity)
- → 클라만: 하방 30.6%는 지금 시점의 정적 순현금 기준이다. 기본 시나리오에서 순현금이 FY2030에 음수가 되는 동적 경로에서는 바닥이 계속 내려간다. 조건 가격 2.3달러가 현실적으로 올 때까지 기다리는 것은 맞지만, FCF 음수는 가격과 무관한 내 레드라인이므로 조건부가 아니라 반대로 둔다. [C:fcf_after_sbc@FY2025] [F119] [F120] [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity)
- → 레드팀: 사전 부검이 지적한 기본 시나리오 FCF 마진 12%의 근거 부족과 차량당 연 약 US$17k 단위경제는 10년 FCF 범위를 더 넓힌다. 이 범위에서는 안전마진이 20%보다 훨씬 커야 하는데 현재는 음수다. 레드팀의 현금 소진·희석 경로는 내 capital_markets_dependent=true를 뒷받침한다. [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) [S87](https://www.bloomberg.com/news/articles/2026-10-02/china-robotaxis-face-losses-as-utilization-trails-waymo-bi-says) [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) [C:runway_years]

**인정한 점**
- 앤더슨의 지적대로 현금 US$1,390.5M, 차입금 없음이라 당장의 파산 위험은 낮다. 자본시장 의존도의 시한이 몇 년 뒤라는 뜻이지만, FCF 음수와 예측 불가능성 레드라인은 바뀌지 않는다.
- 클라만의 하방 계산이 내 기준보다 정확하게 순현금의 질 한계를 짚었다. 주가가 더 내려와도 FCF가 양수가 되지 않는 한 찬성 근거는 되지 않는다.


## 클라만 — 보류 (3/5)

> 하방은 생각보다 얕다. 주가 4.93달러는 주당 순현금 약 3.4달러 위에 있고, 성장이 틀릴 때 단단한 가치까지 내려가는 폭은 30.6%로 50% 한도 안이다. 차입금이 없고 사업·회계 때문에 어떤 가격에도 못 사는 회사도 아니므로 against는 아니다. 그러나 지금 가격에서는 안전마진이 없다. 기본 시나리오 내재가치가 주가보다 낮아 mos가 -46.9%다. 단단한 가치도 정적인 값이 아니다. 매년 2.4억 달러 안팎의 SBC 차감 FCF를 태우고 있고, 순현금에는 보호예수 지분과 장기투자까지 들어 있다. 그래서 가격만 맞으면 살 회사라고 보고 조건부 찬성으로 쓴다. 조건 가격은 코드의 buy_below 2.3달러이고 현재가보다 한참 아래다. 지금은 보류다.

**논거**
- 하방부터 본다. 단단한 가치는 주당 순현금이고, 성장이 틀려도 여기까지만 내려간다는 계산이다. 그 하락 폭은 30.6%로 영구적 손실 한도 50% 안이다. 차입금이 없어 레버리지 레드라인도 지킨다. [C:hard_value@klarman] [C:downside@klarman] [C:price] [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity)
- 그러나 이 바닥은 움직이는 바닥이다. 주주 몫 FCF는 FY2025에 SBC 차감 기준으로 크게 마이너스였고, 2026년 2분기 FCF도 -7,620만 달러다. 설비투자는 전년의 약 3.4배로 늘었다. 기본 시나리오에서도 순현금이 FY2030에 마이너스로 내려간다. 성장이 현실화돼도 순현금은 줄어든다. 하방 30.6%는 지금 시점의 정적 값이라 낙관적이다. [C:fcf_after_sbc@FY2025] [F120] [F119] [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [C:fcf@FY2025]
- 현재가에는 안전마진이 없다. 기본 시나리오 내재가치는 3.35달러이고 주가는 4.93달러다. 약세·기본 범위의 위쪽 끝(iv_high)도 현재가에 못 미친다. 시장은 순현금에 더해 성장 옵션에 값을 치르고 있다. 그 몫이 성장 프리미엄 30.6%다. 50% 경고선 아래지만 안전마진은 0보다 작다. [C:mos@klarman] [C:iv_high@klarman] [C:growth_premium@klarman] [C:price]
- 순현금의 질이 겉보기보다 낮다. 하네스 순현금은 현금·단기투자·장기투자를 모두 더해 회사 유동성 정의보다 넓다. 단기투자에는 2025년 말 기준 보호예수 Level 3 GPU 투자사 지분 US$138.8M가 들어 있었다. 6월 30일에도 보유하는지 확인되지 않았다. 매출채권도 상반기에 크게 늘었다. 그래서 단단한 가치 3.4달러는 상한에 가깝다. [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [F175] [F129] [F52]
- 조건 가격은 코드의 buy_below 2.3달러다. 안전마진 30%와 하방 50%를 둘 다 지키는 가장 높은 가격이다. 52주 최저가 4.9달러 아래로 거래된 적은 없어서 아직 싸게 팔린 증거는 없다. 가격을 예측하지는 않는다. 다만 보호예수 해제 시기(2026-12 무렵), 홍콩 주가의 공모가 대비 큰 하락, 3분기 실적 같은 사건이 가격을 비효율적으로 만들 수 있다. 그때 다시 본다. [C:buy_below@klarman] [C:traded_below_52w@klarman] [F91] [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments)

**사전 부검**
- 사전 부검 1: 순현금을 믿고 샀는데 현금 소진이 예상보다 빨랐다면, 단단한 가치가 계속 줄어드는 바닥 없는 하락이 된다. 설비투자가 늘고 해외 파트너 자금 분담이 기대에 못 미치면 소진이 빨라진다. [F119] [F120] [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [C:runway_years]
- 사전 부검 2: 보호예수 지분 평가액이 빠지고 증자 압력이 생기면 순현금이 줄어든다. 홍콩 주가가 공모가보다 크게 낮은 상태라 증자는 희석이 크다. 이 경우 성장 프리미엄만이 아니라 단단한 가치도 깎인다. [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) [F175] [S91](https://data.sec.gov/submissions/CIK0001969302.json)
- 사전 부검 3: 로보트럭 매출이 특수관계자 Sinotrans에 크게 기대고 있다. 이 매출이 독립 수요가 아니면 성장 가정만이 아니라 현재 현금흐름의 질도 틀린 것이다. 미·중 규제로 미국 보유자가 강제 매도할 가능성도 남는다. [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm) [S71](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#risk-factors-us-china) [F161]

**반론**
- → 앤더슨: 20.49배 상방은 강세 시나리오(확률 20%)를 10년으로 늘린 값이고, 그 길 위에서 순현금이 먼저 줄어든다. 기본 시나리오에서도 순현금은 FY2030에 마이너스로 내려간다. 상방이 열려 있어도 하방의 바닥이 움직이면 영구적 손실 가능성은 닫히지 않는다. 약세 시나리오 손실 확률은 30%이고 약세 현재가치 0.59는 주가 4.93의 일부에 불과하다. 이 분포는 현재가에서 안전마진을 주지 않는다. [C:upside_10y@anderson] [C:p_loss] [C:iv@bear] [C:irr@base]
- → 슬레이터: 보류의 근거인 생존 경로 불확실성에는 동의한다. 다만 시작 비중을 작게 해도 현재가는 내 조건 가격 2.3달러보다 한참 위다. 작은 비중도 순현금 위 성장 프리미엄에 값을 치르는 것이고, 3분기 증거는 가격이 아니라 가치의 근거만 보강한다. [C:buy_below@klarman] [C:growth_premium@klarman] [F120] [F119]
- → 애크먼: FCF 음수와 예측 불가능성 때문에 어떤 가격에도 반대라는 논리는 가장 강한 부분이다. 그러나 이 회사는 차입금이 없고 단단한 가치 3.4달러가 주가 4.93달러의 약 70%를 받쳐 하방이 30.6%다. 영구적 손실 한도 50% 안이어서 가격 문제로만 풀린다. 사업을 이해하기 어렵다는 것과 어떤 가격에도 사지 않는다는 것은 다른 결론이다. 다만 내 buy_below 2.3달러가 네 안전마진 가격 2.7달러보다 낮다는 점에서 두 사람의 가격 눈높이는 비슷하다. [C:downside@klarman] [C:hard_value@klarman] [C:buy_below@ackman] [C:fcf_margin@FY2025]
- → 레드팀: 사전 부검의 현금 소진·희석 시나리오는 성장 프리미엄만이 아니라 단단한 가치도 깎을 수 있다는 점에서 가장 중요하다. 설비투자 급증과 홍콩 주가가 공모가를 크게 밑도는 상태의 증자가 겹치면 순현금 바닥이 낮아진다. 반면 매출 질 붕괴와 규제 시나리오는 주로 성장 프리미엄을 지우고 현금에는 직접 영향이 작다. 그래서 하방 30.6%는 정적 값으로 낙관적이라는 내 1라운드 판단을 유지하되, 영구적 손실 한도를 넘는다는 증거는 아직 없다. [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [C:runway_years] [F175]

**인정한 점**
- 애크먼의 지적대로 순현금은 회사 유동성 정의보다 넓고 보호예수 지분이 섞여 있어 단단한 가치 3.4달러는 상한에 가깝다. 하방 30.6%는 실제로는 더 클 수 있다.
- 레드팀이 지적한 대로 기본 시나리오 FCF 마진 12%와 출구 배수 28배는 후한 가정이다. 이 때문에 내재가치 3.35달러도 낙관적일 수 있고 조건 가격 2.3달러가 과하게 보수적이지는 않다.
- 슬레이터의 지적대로 3분기 실적 전에는 차량 증가가 매출과 총이익률로 이어지는지 확인되지 않았다. 지금 가격에서 매수하지 않는다는 결론에 변함이 없다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Pony AI는 세 갈래로 돈을 번다. 로보택시 서비스(2026년 2분기 US$12.07M, +691.2%), 로보트럭 서비스(US$13.33M, +40.0%), 도메인 컨트롤러 등을 파는 intelligent solutions(US$10.82M, 약 +4%)다. 2분기 총매출은 US$36.22M(+68.8%), 총이익률은 17.5%다. 성장 동력인 로보택시는 매출의 약 1/3이다. 중국 1선 도시의 차량 단위 손익분기는 회사 주장뿐이고 일일 주문·가동률·회수기간 같은 수치는 공시되지 않았다. 영업손실은 US$65.7M이고 설비투자는 US$32.2M으로 약 3.4배 늘었다. 회사 유동성 US$1,390.5M, 차입금 없음이라 당장의 존속 위험은 낮다. 그러나 해자는 아직 흔적으로 입증되지 않았고, 로보트럭 매출은 특수관계자인 Sinotrans에 크게 기대고 있다. 단위경제는 개선 주장과 반대 신호가 섞여 있어 판단을 보류한다.

- [unit_economics] 광저우·선전의 Gen-7 차량 단위 손익분기는 회사 자체 주장이고 감사받지 않았다. 선전 2026-02 기준 차량당 하루 평균 주문 23건, 순매출 RMB338이다. 어닝콜에서는 일일 주문·가동률·회수기간 수치가 없었다. 6-K 부문 수치로는 재현할 수 없다. [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) [S76](https://www.benzinga.com/news/26/08/61272470) [S78](https://cnevpost.com/2026/03/02/pony-ai-hits-unit-profitability-in-2nd-chinese-city/)
- [unit_economics] 추정: 차량당 순매출 RMB338/일은 약 US$47~49/일, 연 약 US$17k다. 3,500대가 이 수준이면 요금 매출은 연 약 US$60M으로, Non-GAAP 영업비용(연 약 US$250M)에 크게 못 미친다. 차량 단위 손익분기와 회사 손익분기 사이의 거리가 멀다. 2분기 영업손실은 US$65.7M, Non-GAAP 영업손실은 US$56.7M이다. [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins)
- [unit_economics] 총이익률은 17.5%로 전년 16.1%, 2025년 4분기 12.7%보다 올랐다. 구성 개선으로 BofA 추정도 넘었다. 하지만 FY2025 연간은 C:gross_margin@FY2025의 15.7%이고, FY2022의 46.9%에서 크게 내려앉은 상태다. 매출 규모가 2배가 되기 전까지는 개선이 구조적인지 확인하기 어렵다. [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S64](https://www.sec.gov/Archives/edgar/data/1969302/000110465926034888/tm269906d1_ex99-1.htm) [S88](https://www.investing.com/news/analyst-ratings/bofa-cuts-pony-ai-stock-price-target-on-valuation-to-17-93CH-4865783) [C:gross_margin@FY2025] [C:gross_margin@FY2022]
- [customers] 로보트럭 매출의 상당 부분이 특수관계자인 Sinotrans(로보트럭 자회사 Cyantron의 비지배주주)에서 나온다. Sinotrans 매출은 FY2025 US$29.6M(F161)로 FY2025 매출 US$90.0M의 약 33%다. 추정: 전부 로보트럭 매출이라면 로보트럭 매출의 약 73%다. 2026-08-25 이사회는 상반기 거래량이 기존 한도를 넘어 연간 한도를 올렸다. 고객 집중과 거래 조건의 독립성이 문제다. [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm) [F161] [F56]
- [customers] intelligent solutions(구 licensing & applications)는 2분기 US$10.82M으로 전년 US$10.41M에서 약 +4%에 그쳤다. 2025년 4분기에도 US$9.4M(−53.2%)이었다. CFO는 도메인 컨트롤러 납품 변동 탓이라고 설명했다. 부문 이름을 바꿔 공시했으므로 비교 연속성을 확인해야 한다. 이 부문이 정체된 탓에 총매출 성장은 로보택시에 크게 의존한다. [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S64](https://www.sec.gov/Archives/edgar/data/1969302/000110465926034888/tm269906d1_ex99-1.htm) [S76](https://www.benzinga.com/news/26/08/61272470)
- [runway] 차량은 2026-06-30에 1,975대이고 연말 3,500대 초과가 목표다. 3월 목표 3,000대 초과에서 상향했다. 추정: 하반기에 약 1,525대(월 약 250대)를 추가해야 한다. 국내 차량은 회사 소유라 설비투자가 늘고 있다. 2분기 설비투자 US$32.2M은 전년 US$9.6M의 약 3.4배다. 2분기 Non-GAAP FCF는 −US$76.2M이다. [S63](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#guidance-operations) [S64](https://www.sec.gov/Archives/edgar/data/1969302/000110465926034888/tm269906d1_ex99-1.htm) [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- [runway] 해외는 자산경량 모델이다. Uber와 유럽 2,000대 이상을 공동 배치하며 차량 자금·소유는 시장에 따라 파트너가 맡는다(자그레브는 Verne). 해외 설비투자 부담은 줄지만 경제성을 차량 소유자·플랫폼과 나누게 된다. CFO는 차량 인도 매출을 선인식한다고 밝혀 '로보택시 서비스' 매출이 순수 요금 매출이 아닐 수 있다. 수익 배분율은 비공개다. 두바이 상용 출시는 2026년 하반기 계획이지만 2026-10-18 현재 확인된 바 없다. [S75](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926096218/tm2623123d1_ex99-1.htm) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [S80](https://autonews.gasgoo.com/articles/news/ponyai-advances-dubai-rollout-with-driverless-robotaxi-testing-milestone-2046173614297051136)
- [industry] WeRide의 2026년 2분기 매출은 약 US$34.2M(+82.2%)으로 Pony와 규모가 비슷하다. 총이익률은 37.5%로 Pony의 약 2배다. 현금·정기예금은 약 US$792.2M으로 Pony 유동성 US$1,390.5M보다 적다. Bloomberg Intelligence(헤드라인만)는 중국 로보택시의 가동률이 Waymo에 못 미쳐 손실을 본다고 지적했다. WeRide L4 매출에는 로보버스가 섞여 있어 사업 구성 차이를 감안해야 한다. [S84](https://www.sec.gov/Archives/edgar/data/0001867729/000110465926094571/tm2622690d2_ex99-1.htm) [S87](https://www.bloomberg.com/news/articles/2026-10-02/china-robotaxis-face-losses-as-utilization-trails-waymo-bi-says) [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity)
- [runway] 재무 완충은 두껍다. 차입금이 없고 총부채는 US$93.0M이다. 다만 유동성에는 2025년 말 기준 보호예수 중인 Level 3 GPU 투자사 지분(US$138.8M)이 들어 있었고, 평가이익이 GAAP 순손실을 작아 보이게 했다. 2분기 순손실 US$45.35M에는 평가이익 US$33.4M이 들어 있고, 일회성 선급금 손상 US$25.0M이 반대로 작용했다. 사업 상태는 영업손실과 Non-GAAP 수치로 봐야 한다. 매출채권은 US$43.3M으로 2025년 말 US$23.6M에서 상반기에 약 83% 늘어 DSO 개선 판단과 반대 방향이다. [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [S61](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#net-loss-nci) [F52]
- [claimed] 회사는 Gen-7 BOM이 Gen-6 대비 70% 절감되고 부품이 전부 차량용 등급이라고 주장한다. 그러나 절대 원가와 감가상각 내용연수는 공시하지 않았다. 70% 절감은 로보트럭 Gen-4 ADK에 대한 수치이기도 해서 로보택시 원가 우위의 증거로 쓰기 어렵다. 총이익률 17.5%는 경쟁사 WeRide의 37.5%보다 낮아 총이익 단계의 원가 우위 흔적도 없다. [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) [S64](https://www.sec.gov/Archives/edgar/data/1969302/000110465926034888/tm269906d1_ex99-1.htm) [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S84](https://www.sec.gov/Archives/edgar/data/0001867729/000110465926094571/tm2622690d2_ex99-1.htm)
- [claimed] 회사는 4개 1선 도시 모두에서 완전 무인 상용 로보택시 허가를 가진 유일한 회사라고 주장한다. 상하이 푸둥(2025-07)과 선전 시 전역(2025-10) 허가는 6개월을 넘은 2차 보도다. 베이징 허가 세부와 차량 수는 확인되지 않았다. 규제 허가가 진입장벽이 될 수는 있지만, 경쟁사도 비슷한 허가를 받고 있어 아직 독점적 해자로 입증되지 않았다. [S92](https://www.benzinga.com/markets/tech/25/07/46656199/pony-ai-gets-green-light-for-driverless-robotaxis-in-shanghais-pudong) [S93](https://www.itiger.com/news/1161555691) [S84](https://www.sec.gov/Archives/edgar/data/0001867729/000110465926094571/tm2622690d2_ex99-1.htm)
- [claimed] Uber와 유럽에 2,000대 이상을 배치하는 계약은 수요 채널이지만 전환비용 해자는 아니다. 수익 배분·독점·계약 기간은 공시되지 않았고, Pony는 Bolt와도 일하며 Uber도 WeRide·Baidu 등 경쟁사와 일한다. 이탈률이나 가격 인상 후 고객 유지 기록은 없다. [S75](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926096218/tm2623123d1_ex99-1.htm) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model)
- [claimed] 네트워크·브랜드·규모 해자를 입증하는 점유율 추이, 이탈률, 경쟁사 대비 마진 자료가 없다. 중국 사업자별 이동 건수·점유율 자료도 찾지 못했다. 규모에서는 WeRide(2026-07-31 L4 차량 약 3,400대)와 Waymo가 비교 대상이다. [S84](https://www.sec.gov/Archives/edgar/data/0001867729/000110465926094571/tm2622690d2_ex99-1.htm) [S85](https://electrek.co/2026/07/08/waymo-driverless-las-vegas-four-new-cities/)

### 경영진·자본배분 — mixed

창업자 두 명이 의결권 약 69.7%를 쥔 차등의결권 구조이고, CEO는 경제적 지분 13.8%를 가져 주주와 이해관계가 일부 일치한다. 다만 보상 지표(KPI 연동 여부)와 CEO 개인 보상액은 확인되지 않았고, 최근 내부자 거래는 소규모 매도뿐이다. 가이던스는 수치 목표가 거의 없어 적중률로 신뢰도를 재기 어렵다. 로보트럭 매출의 상당 부분이 특수관계자 Sinotrans에 의존하고, 해외 모델은 차량 인도 매출을 선인식해 매출 질이 불투명하다. 희석은 회계상 착시가 크고 실제 증가는 작지만, 홍콩 공모가(HK$139)보다 주가가 크게 낮아 향후 증자는 희석이 클 것이다. 자본배분은 투자 확대와 파트너 공동투자 중심이며 자사주 매입은 없다. 종합하면 정렬은 '혼재'로 본다.

- [compensation] FY2025 이사·임원 보상 총액(SBC 제외)은 US$7.3M이다. 개인별 CEO 보상액과 KPI 연동 보너스 지표는 찾지 못했다(근거 없음). SBC는 FY2025 US$30.8M, 2026년 2분기 US$9.05M으로 분기 매출의 약 25%다. 2026-10-09 직원 124명에게 RSU 1,638,591주를 성과 조건 없이 4년 분할로 부여했다. 2024 SBC US$127.0M 중 US$120.7M은 상장 때 일시 인식분이다. [S68](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#compensation-sbc) [S73](https://www.sec.gov/Archives/edgar/data/1969302/000110465926115030/tm2627277d1_ex99-1.htm) [F165] [F64] [F108] [C:sbc_to_revenue@FY2025]
- [insider] CEO 펑쥔은 경제적 지분 13.8%, 의결권 51.6%이고 CTO 러우톈청은 4.9%, 18.1%다. 이사·임원 전체로 19.5%, 70.0%다. 경제적 지분이 커서 이해관계는 일치하지만 소액주주는 자본배분에 영향을 줄 수 없다. 최근 3개월 내부자 거래는 VP와 CFO의 소규모 매도(2026-09-28, US$7.10)뿐이고 매수 기록은 없다. 매도는 RSU 가득 시기와 겹쳐 보인다(노트 추론). [S66](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#major-shareholders) [S90](https://www.marketbeat.com/instant-alerts/price-pony-ai-nasdaq-pony-reaches-new-12-month-low-heres-why-2026-10-13/) [F150] [F151] [F152] [F153] [F157] [F158]
- [guidance] 가이던스는 대부분 수치 목표가 없는 문구다. 연말 로보택시 3,500대 초과(3월 3,000대 초과에서 상향)와 로보택시 매출 작년의 3.5배 초과가 주된 목표다. 2분기 말 1,975대라 하반기에 약 1,525대(월 약 250대) 추가가 필요하다. 2분기 매출 US$36.2M은 컨센서스 US$35.2M을 넘었고 EPS는 컨센서스와 같았다. 과거 가이던스 사실과 실제의 대조 표본이 없어 적중률(C:guidance_hit_rate)로 신뢰도를 판단할 수 없다. 차량 목표 상향은 달성 여부가 연말에야 확인된다. [S63](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#guidance-operations) [S76](https://www.benzinga.com/news/26/08/61272470) [S88](https://www.investing.com/news/analyst-ratings/bofa-cuts-pony-ai-stock-price-target-on-valuation-to-17-93CH-4865783) [F78] [F79] [F140] [F142] [F193] [F194]
- [dilution] 하네스의 희석 주식 수 연 64.5%·FY2025 +232.3% 신호는 대부분 2024-11 우선주 전환(225.4M주)이 가중평균에서 빠진 회계상 착시다. FY2025 실제 신주는 홍콩 상장 48.249M주(약 12.5%)였다. 2026-03-31에서 2026-09-30 사이 발행주식은 433.54M주에서 435.18M주로 약 0.38% 늘었다. 2026년에 후속 공모·선반등록·전환사채는 없다. 홍콩 주가가 공모가 HK$139 대비 약 67% 낮아, 앞으로 증자하면 희석이 클 것이다(노트 추론). [S70](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#share-capital-history) [S72](https://www.sec.gov/Archives/edgar/data/1969302/000110465926114347/tm2627105d1_ex99-1.htm) [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) [S91](https://data.sec.gov/submissions/CIK0001969302.json) [F183] [F184] [F143] [F65] [C:share_change@FY2025]
- [capital_allocation] FY2025 설비투자는 US$43.9M으로 전년 US$11.4M의 약 3.8배이고 2026년 2분기는 US$32.2M(전년 US$9.6M)이다. 2분기 Non-GAAP FCF는 −US$76.2M이며 국내 차량은 직접 소유한다. 해외는 파트너가 차량 자본을 대는 자산경량 모델을 목표로 한다. 홍콩 상장으로 US$829.4M을 조달해 2026-06-30 유동성은 US$1,390.5M이며 차입금은 없다. 자사주 매입은 FY2023 US$0.99M 외에 없고 2분기 콜에서도 언급이 없었다. 2분기에는 '장기투자 선급금' US$25.0M을 전액 손상했는데 대상은 공시되지 않았다. 투자자본수익률은 FY2025 ROIC −42.3%다. [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S63](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#guidance-operations) [S70](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#share-capital-history) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [S61](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#net-loss-nci) [F81] [F119] [F120] [F123] [F117] [C:roic@FY2025] [C:fcf@FY2025]
- [capital_allocation] 로보트럭 자회사 Cyantron의 비지배주주 Sinotrans에 대한 매출이 FY2025 US$29.6M으로 총매출의 약 33%이고, 전부 로보트럭 매출이라면 로보트럭 매출의 약 73%다(노트 계산). 2026-08-25 이사회가 상반기 거래량이 기존 한도를 넘는다며 연간 한도를 상향했다. 한도 금액과 가격 조건은 공시에서 확인하지 못했다. 거래 조건의 독립성과 성장의 질이 의문이다. 같은 20-F에서 Toyota 매출 US$0.1M, 지분법 피투자사 Zhuifeng 매출 US$1.1M도 보고됐다. [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm) [F161] [F162] [F163] [F164]
- [capital_allocation] GAAP 순손익은 단기매매증권 공정가치 평가이익 때문에 좋게 보인다. FY2025 평가이익이 US$128.0M(GPU R&D 피투자사 상장주식, 12개월 보호예수 Level 3)이고 2026년 2분기 US$33.4M이다. 2025년 말 장부가를 뺀 조정 유동성은 약 US$1.25B다(노트 계산). 해외 파트너 공동배치에서는 차량 인도 매출을 선인식한다고 CFO가 밝혀, 로보택시 '서비스' 매출이 순수 요금 매출이 아닐 수 있다(공시로 확인 필요). 자동 전사본이라 문구는 확인이 필요하다. [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [S61](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#net-loss-nci) [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [F171] [F116] [F175]
- [insider] 2025-10 Bloomberg 보도는 Uber가 홍콩 IPO에 약 US$100M을 넣을 수 있다고 했으나, 확정 코너스톤 명단에 Uber는 없어 실제 투자는 확인되지 않는다. 2026-10-08 ADS 종가 US$5.76에서 RSU를 부여했고 2026-10-16 종가는 US$4.93으로 52주 신저가다. 주가 하락 원인을 경영진의 행동과 연결한 자료는 없다. [S83](https://www.automotiveworld.com/articles/bloomberg-uber-plans-to-invest-in-pony-ai-weride-hk-ipos/) [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) [S73](https://www.sec.gov/Archives/edgar/data/1969302/000110465926115030/tm2627277d1_ex99-1.htm) [S55](https://finance.yahoo.com/quote/PONY/history/) [F80] [F91]

### 회계 품질 — watch

회계 처리 자체를 의심할 증거는 없어서 red_flag는 아니다. 감사의견과 ICFR은 모두 적정이고(S65), 재무제표 정정(8-K 4.02)과 감사인 변경 신호는 없다. 다만 보고 숫자를 그대로 믿으면 안 되고 조정해서 봐야 한다. (1) GAAP 순손익은 단기매매증권 공정가치 이익으로 좋아 보인다. FY2025 +US$128.0M(F171), 2026년 2분기 +US$33.4M(F116)이고, 원천은 보호예수 중인 Level 3 GPU 투자사 지분이다(S69). 영업손실과 Non-GAAP 수치가 사업 실체에 가깝다. (2) 로보트럭 매출의 상당 부분이 로보트럭 자회사 비지배주주인 특수관계자 Sinotrans에서 나온다. FY2025 US$29.6M(F161)으로 매출의 약 1/3이고, 2026년 한도도 상향됐다(S74). (3) 2분기 매출채권이 US$43.3M(F129)으로 2025년 말 US$23.6M(F52)보다 크게 늘었고, 해외 공동 배치에서는 차량 인도 매출을 선인식한다는 CFO 발언이 있다(S77). 이 때문에 로보택시 '서비스' 매출의 질은 공시로 확인할 때까지 보수적으로 봐야 한다. (4) 순현금은 보호예수 지분과 장기투자까지 포함해 회사 유동성 정의보다 넓다(S62, S69). 코드의 3개 신호는 모두 해명되거나 회계상 착시로 풀리지만, 매출의 질과 현금성 자산의 질 문제가 남아 watch로 판정한다.

- [concern] sbc_to_revenue: SBC/매출 34.2%(C:sbc_to_revenue@FY2025)는 문턱 10%를 크게 넘는다. 매출이 작고 R&D 중심 비용 구조라 SBC가 실질 보상 비용이다. FY2024 SBC US$127.0M 중 US$120.7M은 2024-11 상장 때 누적 가득분을 일시 인식한 것이라(F167·S68) FY2024 비율의 대부분은 일회성이다. 그래도 FY2025 SBC는 US$30.8M(F64)이고, 2026년 2분기 SBC US$9.05M(F108)은 2분기 매출의 약 25%이며, 미인식 SBC도 US$67.9M(F166) 남아 있다. FCF를 볼 때는 SBC 차감 FCF(C:fcf_after_sbc@FY2025)를 써야 한다. [C:sbc_to_revenue@FY2025] [C:fcf_after_sbc@FY2025] [F64] [F108] [F166] [F167] [S68](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#compensation-sbc)
- [benign] deferred_revenue: 이연매출은 FY2024 US$3.23M(F16)에서 FY2025 US$1.92M(F17)으로 줄었다. 하지만 절대 규모가 매출 US$90.0M(F56)에 비해 극히 작아서 매출 당겨쓰기의 근거로 보기 어렵다. 매출 성장 20.0%(C:revenue_growth@FY2025)는 로보택시 서비스(F137)와 로보트럭(F138) 성장이 이끌었고, 이연매출 감소로 설명되지 않는다. 다만 이 신호보다 더 큰 매출 질 위험이 따로 있다. 해외 공동 배치에서 차량 인도 매출을 선인식한다는 발언(S77)과 2분기 매출채권 급증(F129 대 F52)이다. 이는 findings에서 별도로 짚는다. [F16] [F17] [F56] [F137] [F138] [F129] [F52] [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [C:deferred_revenue@FY2025] [C:revenue_growth@FY2025]
- [benign] dilution: 희석 주식 수 연 64.5%(C:dilution)와 FY2025 +232.3%(C:share_change@FY2025)는 대부분 가중평균의 회계상 착시다. FY2024 가중평균 희석 주식 수(F20)에는 2024-11 상장 때 우선주 전환으로 생긴 Class A 약 2.3억 주(F183)가 일부만 반영돼 있었다. FY2025의 실제 신주 발행은 홍콩 IPO 48,249,000주(F184)뿐이고, 홍콩 상장 전 주식 수 대비 약 12.5%다(S70 노트 계산). 이후 발행주식은 2026-03-31 4.33542억 주(S66)에서 2026-09-30 4.35184억 주(F143)로 약 0.38% 늘어 정상 범위다. 2026년에는 후속 공모, 선반등록, 전환사채가 없다(S91). 다만 2026-10-09 RSU 1,638,591주 부여(F146)처럼 SBC로 인한 희석은 계속되고, 홍콩 주가가 공모가보다 크게 낮아진 상태(S82)라 앞으로 증자하면 희석이 커질 수 있다. [C:dilution] [C:share_change@FY2025] [F20] [F183] [F184] [F143] [F146] [S66](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#major-shareholders) [S70](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#share-capital-history) [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) [S91](https://data.sec.gov/submissions/CIK0001969302.json)
- [watch] GAAP 순손익이 공정가치 이익으로 좋아 보인다. FY2025 단기매매증권 공정가치 변동은 +US$128.0M(F171)이다. 영업손실 US$260.86M(F44)에서 세전손실 US$76.76M(F48)까지 줄인 가장 큰 항목이며, 원천은 12개월 보호예수 대상인 Level 3 GPU 투자사 지분이다. 2025-12-31 장부가는 US$138.8M(F175)이고 시장성 할인 11%(F176)를 적용했다. 2026년 2분기에도 +US$33.4M(F116)이 순손실을 줄였다. 이 이익은 반복되지 않는 시장 평가 이익이므로 영업이익과 Non-GAAP 수치를 기준으로 봐야 한다. 같은 지분이 순현금과 유동성에도 들어 있어 현금성 자산의 질도 따로 따져야 한다. [F44] [F48] [F171] [F175] [F176] [F116] [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [S61](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#net-loss-nci)
- [watch] 로보트럭 자회사 Cyantron의 비지배주주 Sinotrans가 큰 고객이다. 매출은 FY2023 US$22.5M(F159), FY2024 US$30.7M(F160), FY2025 US$29.6M(F161)이고, 2025-12-31 미수금은 US$10.15M(F162)이다. 노트 계산으로 FY2025 매출의 약 33%이고, 전부 로보트럭 매출이라면 로보트럭 매출의 약 73%다. 거래 조건이 독립적인지 확인할 수 없고, 2026-08-25에는 이 거래의 연간 한도가 상향됐다(S74). 한도 금액과 가격 조건은 확인하지 못했다. 로보트럭 매출 성장을 독립된 시장 수요로 읽으면 안 된다. [F159] [F160] [F161] [F162] [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm)
- [watch] 해외 공동 배치 모델에서는 '차량 인도 매출을 선인식'하며, 수익 배분이나 라이선스 수수료를 받을 수 있다고 CFO가 말했다(S77, 자동 전사본이라 공시 확인이 필요하다). 로보택시 '서비스' 매출에 차량 판매 성격의 매출이 섞일 수 있고 분기별로 들쭉날쭉할 수 있다. 로보택시 서비스 매출은 2026년 2분기 US$12.07M(F77)이고, 요금 징수 매출 증가율은 +849.3%(F99)다. 순수 요금 매출과 차량 인도 매출의 구분은 공개되지 않았다. 매출 성장의 질을 판단하려면 이 구분이 필요하다. [F77] [F99] [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model)
- [watch] 매출채권이 2026년 2분기 US$43.3M(F129)으로 2025-12-31의 US$23.6M(F52)보다 상반기에 약 83% 늘었다(S62). 같은 기간 2분기 매출은 US$36.2M(F76)이다. 코드의 DSO 개선(C:dso@FY2025 95.9일)은 FY2025 연말 기준이고 2026년 상반기에는 반대로 움직였다. 2분기 영업현금유출은 US$44.0M(F118)으로 전년 US$25.4M(F121)보다 커졌고, CFO는 운전자본, 매입채무 결제, 재고 확충 탓이라고 설명했다. 채권 증가가 Sinotrans나 인도 매출에서 나왔는지 공시로 확인되지 않았다. [F129] [F52] [F76] [F118] [F121] [C:dso@FY2025] [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity)
- [info] 코드의 non_gaap 신호는 없다. 2026년 2분기 영업손실 US$65.7M(F106) 대비 Non-GAAP 영업손실 US$56.7M(F107)로 조정폭은 SBC 등 US$9M 수준이며 정상 범위다. 반면 US$25.0M 일회성 '장기투자 선급금' 손상(F117)은 대상이 공시되지 않았다. 순손실에는 연결 순손실 US$45.35M(F113)과 Pony AI 귀속 순손실 US$59.84M(F112)이 함께 쓰이고, 비지배지분 몫 US$14.5M(F114)이 차이를 만든다. FY2025의 '세전 손실 대 귀속 순손실 불일치'도 비지배지분 몫 US$57.21M(F170)으로 풀린다. 어느 기준의 수치인지 확인하고 써야 한다. [F106] [F107] [F112] [F113] [F114] [F117] [F170] [S61](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#net-loss-nci) [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments)
- [info] 감사인은 Deloitte 베이징으로 2022년부터 같은 감사인이다. FY2025 재무제표와 ICFR 모두 적정의견이다. 핵심감사사항은 R&D 비용(US$217.4M) 분류 1건이고 계속기업 의문은 없다. 감사 보수는 US$1.53M(F148)에서 US$1.96M(F147)로 늘었다. 재무제표 정정과 감사인 변경 신호는 없다. 다만 중국 소재 감사인이라 PCAOB 검사 접근성이 규제 위험으로 남지만, 홍콩 이중 상장 덕에 존립 위험은 아니다. [F147] [F148] [S65](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#audit-report) [S71](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#risk-factors-us-china)
- [watch] 순현금은 회사 유동성 정의보다 넓다. 하네스 순현금(C:net_cash@FY2025)은 현금, 단기투자, 장기투자를 합한 값이다. 회사 유동성은 2026-06-30 US$1,390.5M(F123)이다. 단기투자에는 보호예수 중인 Level 3 GPU 투자사 지분 US$138.8M(F175)이 2025년 말 기준으로 들어 있었고, 이를 뺀 조정 유동성은 약 US$1.25B다(S69 노트 계산). 6/30 보유 여부는 확인되지 않았다. 런웨이(C:runway_years 7.1년) 계산은 현금 소진 속도를 과소평가할 수 있다. 2분기 FCF는 −US$76.2M(F120)이고 설비투자는 US$32.2M(F119)으로 전년 US$9.6M(F122)의 약 3.4배다. [C:net_cash@FY2025] [C:runway_years] [F119] [F120] [F122] [F123] [F175] [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 현금 소진과 희석 경로: 로보택시를 키우려면 국내 차량을 직접 소유해야 해서 설비투자가 계속 늘고(2분기 설비투자 US$32.2M, 전년의 약 3.4배), 영업손실과 FCF 적자가 매출 성장보다 빨리 불어난다. 기본 시나리오 자체가 FY2030에 순현금이 음수가 되는 경로다(C:fcf_margin 적자 지속). 해외 파트너 자산경량 모델이 수익 배분을 나누는 탓에 매출이 기대만큼 마진으로 안 남고, 흑자 전환 시점이 밀린다. 홍콩 주가가 공모가 HK$139 대비 약 67% 낮은 상태에서 증자하면 희석이 매우 크고, 보호예수 해제(2026-12 무렵)가 겹쳐 주가가 한 번 더 무너진다. [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S82](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) [S69](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) [C:runway_years]
- (25%) 차량 단위경제의 허상: 광저우·선전의 차량 단위 손익분기는 감사받지 않은 회사 주장이고, 차량당 하루 순매출 RMB338(연 약 US$17k)로는 3,500대가 돌아도 요금 매출이 연 약 US$60M에 그쳐 Non-GAAP 영업비용(연 약 US$250M)을 못 덮는다. 가동률이 Waymo에 못 미친다는 지적(S87)처럼 실제 주문·가동률이 오르지 않으면 차량을 늘릴수록 손실이 커진다. 경쟁사 WeRide의 총이익률 37.5%(Pony 17.5%)는 Pony의 원가 우위 주장과 맞지 않는다. 가격 경쟁(Apollo Go, WeRide, 플랫폼 보조금)이 시작되면 차량당 매출이 더 내려간다. [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) [S87](https://www.bloomberg.com/news/articles/2026-10-02/china-robotaxis-face-losses-as-utilization-trails-waymo-bi-says) [S84](https://www.sec.gov/Archives/edgar/data/0001867729/000110465926094571/tm2622690d2_ex99-1.htm) [S60](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins)
- (20%) 매출의 질 붕괴: 로보트럭 매출의 약 73%는 비지배주주이자 특수관계자인 Sinotrans에서 나오고(FY2025 US$29.6M), 2026-08 한도 상향이 있었다. 해외 로보택시 '서비스' 매출에는 차량 인도 선인식이 섞여 있고 매출채권도 상반기에 약 83% 늘었다. 한도가 다시 못 늘거나 인도 매출이 분기마다 들쭉날쭉해지면 매출 성장이 둔화되고, 회계상 매출채권 회수나 평가에서 문제가 드러나면 신뢰가 무너진다. GAAP 순손실을 줄이던 공정가치 이익(2분기 US$33.4M)도 사라지면 실적이 갑자기 나빠 보인다. [S67](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm) [S77](https://www.benzinga.com/news/26/08/61272470#asset-light-model) [S62](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) [S61](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#net-loss-nci)
- (15%) 규제·지정학과 성장 서사 붕괴: 미국 해외투자 프로그램(OIP)에서 '대상 외국인'으로 간주되거나 커넥티드카·수출통제 강화, 미·EU 중국 AV 업체 제한이 오면 Uber 유럽 2,000대와 해외 4,000대 파이프라인이 늦어지거나 무산된다. 계약은 수익 배분·독점·기간이 비공개라서 쉽게 깨질 수 있고, 연말 3,500대 달성 실패(하반기에 월 약 250대 필요)와 두바이 상용 출시 지연이 겹치면 성장 서사가 무너진다. 미국 보유자의 강제 매도가 가세한다. 현재 주가 하락(US$7.29에서 US$4.93)은 이미 시장이 이 위험을 일부 반영하기 시작했다는 신호일 수 있다. [S71](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#risk-factors-us-china) [S75](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926096218/tm2623123d1_ex99-1.htm) [S63](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#guidance-operations) [S80](https://autonews.gasgoo.com/articles/news/ponyai-advances-dubai-rollout-with-driverless-robotaxi-testing-milestone-2046173614297051136) [S87](https://www.bloomberg.com/news/articles/2026-10-02/china-robotaxis-face-losses-as-utilization-trails-waymo-bi-says)
- 약한 가정 `base.fcf_margin`: 기본 시나리오 FCF 마진 12%는 6년 뒤 현재 −232%(FY2025)에서 흑자로 돌아서야 하는 가정인데, 기저율 표가 없어 근거가 약하다. 모델 연도별 경로에서도 FY2030까지 FCF가 적자이고 순현금이 음수로 내려가며, 이는 마진 급반전을 마지막 해 한 번에 끼워 넣은 것이다. 차량당 매출 연 약 US$17k로는 마진 전환이 어렵다는 점과 WeRide 대비 낮은 총이익률도 이 가정을 약하게 한다. [C:fcf_margin@FY2025] [C:implied_cagr@m12] [S79](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) [S84](https://www.sec.gov/Archives/edgar/data/0001867729/000110465926094571/tm2622690d2_ex99-1.htm)
- 약한 가정 `base.exit_multiple`: 출구 P/FCF 28배는 FCF 마진 12%에서 막 흑자가 된 해의 배수라 높다. 비교 가능한 성숙 기업의 배수에 비해 후하고, 매출이 6년간 연 46.5%로 커져야 한다는 가정과 겹친다. 민감도에서 배수 ×0.75만 되어도 기본 시나리오 연 수익률이 −1.6%로 떨어진다. [C:expected_irr] [C:p_loss]
- 약한 가정 `base.revenue_growth`: 기본 시나리오 매출 성장 6년 연 46.5%는 기저율 표가 없어 검증되지 않았고, 컨센서스 FY2028(US$702M) 대비 모델은 −49.2%이지만 성장 전제 자체가 지속적인 차량 증가와 해외 파트너 배치에 의존한다. 하반기 월 약 250대를 추가해야 하는 증차 속도와 Sinotrans 의존 로보트럭, 정체한 intelligent solutions를 고려하면 낙관적이다. [C:base_rate@base] [C:consensus_diff@revenue@FY2028] [S63](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#guidance-operations) [S74](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm)

## 검증 (L6)

주장 90개 — supported 84 · unsupported 5 · contradicted 1 · leap 0 · 미검증 0

- [unsupported] 레드팀: 출구 P/FCF 28배는 FCF 마진 12%에서 막 흑자가 된 해의 배수라 높다. 비교 가능한 성숙 기업의 배수에 비해 후하고, 매출이 6년간 연 46.5%로 커 — 출처 없는 숫자 7500, 1.6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 사업·산업: 차량은 2026-06-30에 1,975대이고 연말 3,500대 초과가 목표다. 3월 목표 3,000대 초과에서 상향했다. 추정: 하반기에 약 1,525대(월 약  — 차량 1,975대, 3,500대 목표, 3.4배 설비투자는 맞지만, 인용 자료 어디에도 국내 차량이 회사 소유라는 내용은 없다.
- [contradicted] 경영진·자본배분: CEO 펑쥔은 경제적 지분 13.8%, 의결권 51.6%이고 CTO 러우톈청은 4.9%, 18.1%다. 이사·임원 전체로 19.5%, 70.0%다. 경제적 지분이 — 지분율·의결권은 맞지만 S90의 3개월 내부자 매도는 41,700주로 VP·CFO 두 건 합계(약 29,275주)보다 커서 '그 두 건뿐'이라는 말과 어긋난다.
- [unsupported] 애크먼: FCF가 음수이고 악화 중이다. FY2025 FCF 마진은 -232.0%이고, 2026년 2분기 Non-GAAP FCF는 -US$76.2M이다. 설비투자는 전년의 — FCF 마진 −232%, 2분기 FCF −76.2M, 설비투자 3.4배는 맞지만, 차량 목표를 채우려면 국내 차량을 직접 소유해야 한다는 내용은 인용 자료에 없다.
- [unsupported] 경영진·자본배분: FY2025 설비투자는 US$43.9M으로 전년 US$11.4M의 약 3.8배이고 2026년 2분기는 US$32.2M(전년 US$9.6M)이다. 2분기 Non-G — 출처 없는 숫자 3.8 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 기본 시나리오 매출 성장 6년 연 46.5%는 기저율 표가 없어 검증되지 않았고, 컨센서스 FY2028(US$702M) 대비 모델은 −49.2%이지만 성장 전제  — 없는 근거 인용: C:base_rate@base

## 사용자 견해 대조 (분석이 끝난 뒤에만 비교한다)

- 사용자 보류 vs 하네스 팽팽 — 일치
- 사용자 주장 (하네스가 검증하지 않음): 상방은 매력적이다
- 사용자 주장 (하네스가 검증하지 않음): AV 분야의 경쟁이 치열할 것이라는 논리를 생각하면 확신을 갖고 담을 만큼은 아니다

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| 매출 (revenue) | 6,839만 USD | 7,190만 USD | 7,502만 USD | 9,000만 USD |
| 매출 성장 (revenue_growth) | — | 5.1% | 4.3% | 20.0% |
| 총이익률 (gross_margin) | 46.9% | 23.5% | 15.2% | 15.7% |
| 영업이익률 (operating_margin) | -249.6% | -199.2% | -380.6% | -289.8% |
| 순이익 (net_income) | -1.5억 USD | -1.2억 USD | -2.7억 USD | -1.3억 USD |
| 영업현금흐름 (ocf) | -1.5억 USD | -1.2억 USD | -1.1억 USD | -1.6억 USD |
| 설비투자 (capex) | 1,203만 USD | 509만 USD | 1,140만 USD | 4,388만 USD |
| FCF (fcf) | -1.7억 USD | -1.2억 USD | -1.2억 USD | -2.1억 USD |
| FCF 마진 (fcf_margin) | -243.9% | -167.6% | -162.8% | -232.0% |
| SBC (sbc) | 1,318만 USD | 325만 USD | 1.3억 USD | 3,080만 USD |
| SBC/매출 (sbc_to_revenue) | 19.3% | 4.5% | 169.3% | 34.2% |
| SBC 차감 FCF (fcf_after_sbc) | -1.8억 USD | -1.2억 USD | -2.5억 USD | -2.4억 USD |
| ROIC (roic) | — | — | -138.5% | -42.3% |
| 순현금 (net_cash) | 5.8억 USD | 5.9억 USD | 7.5억 USD | 11.7억 USD |
| 희석 주식 수 (diluted_shares) | 8,532만 | 8,910만 | 1.1억 | 3.8억 |
| 주식 수 변화 (share_change) | — | 4.4% | 28.3% | 232.3% |
| DSO(일) (dso) | 138.2 | 160.3 | 138.9 | 95.9 |
| 발생액 비율 (accruals_ratio) | — | -1.2% | -18.2% | 2.2% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, cost_of_revenue, d_and_a, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, gross_profit, income_tax, operating_income, pretax_income, receivables, receivables_growth, rnd, short_term_investments, total_assets

### 시장 · FY2025 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 4.93 USD/share (2026-10-16, F80) |
| 희석 주식 수 (shares) | 4.4억 |
| 시가총액 (market_cap) | 21.5억 USD |
| 순현금 (net_cash) | 14.9억 USD |
| EV (ev) | 6.6억 USD |
| FCF 수익률 (fcf_yield) | -9.7% |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 7.29x |
| PER (pe) | — |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | 7.1 |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 34.2% > 10%
- [watch] deferred_revenue (C:deferred_revenue): 매출은 늘었는데 이연매출이 10% 넘게 줄었다 — 매출 당겨쓰기 의심
- [watch] dilution (C:dilution): 희석 주식 수 연 64.5% 증가 > 3%

### 역DCF — 현재 가격이 가정하는 것

EV 6.6억 USD를 정당화하려면 매출이 10년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 목표 마진으로 직선 수렴, 할인율 10%, 이후 영구성장 3%.
기본 시나리오 목표 마진 12% 기준: 연 51.7% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 57.4% | C:implied_cagr@m10 |
| 12% | 51.7% | C:implied_cagr@m12 |
| 15% | 45.4% | C:implied_cagr@m15 |
| 20% | 38.1% | C:implied_cagr@m20 |
| 25% | 33.0% | C:implied_cagr@m25 |
| 30% | 29.1% | C:implied_cagr@m30 |

### 시나리오 가치 — 6년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 6년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 30% | 3.1억 USD | 23.2% | 3% | 15x | 1.04 | 0.59 | -22.9% |
| 기본 | 50% | 8.9억 USD | 46.5% | 12% | 28x | 5.94 | 3.35 | +3.2% |
| 강세 | 20% | 17.1억 USD | 63.4% | 25% | 30x | 26.12 | 14.75 | +32.0% |

확률 가중: 주당 가치 8.51 · IV 4.80 · 기대 연 수익률 +9.5% (C:expected_irr) · 손실 확률 30% (C:p_loss) · 현재 주가 4.93

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +38.2% · 마진·멀티플(P/S) -12.9% · 주식 수 변화 -2.5% · 현금 축적 -19.7% = +3.1%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -4.8% | -0.6% | +2.8% |
| +0%p | -1.6% | +3.2% | +7.1% |
| +5%p | +2.0% | +7.4% | +11.6% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 1.5억 USD | -191.4% | -2.8억 USD | 4.5억 | 12.1억 USD |
| FY2027 | 2.4억 USD | -150.7% | -3.6억 USD | 4.6억 | 8.5억 USD |
| FY2028 | 3.6억 USD | -110.0% | -3.9억 USD | 4.7억 | 4.6억 USD |
| FY2029 | 5.1억 USD | -69.3% | -3.5억 USD | 4.8억 | 1.0억 USD |
| FY2030 | 6.8억 USD | -28.7% | -2.0억 USD | 4.9억 | -9,134만 USD |
| FY2031 | 8.9억 USD | 12.0% | 1.1억 USD | 5.0억 | 1,524만 USD |

### 컨센서스 대비 (C:consensus_diff@지표@기간)

| 지표 | 기간 | 컨센서스 | 기본 시나리오 | 차이 |
|---|---|---|---|---|
| revenue | FY2026 | 1.4억 USD | 1.5억 USD | +2.4% |
| revenue | FY2027 | 2.9억 USD | 2.4억 USD | -19.2% |
| revenue | FY2028 | 7.0억 USD | 3.6억 USD | -49.2% |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 51.7% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 46.5% × 6년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 63.4% × 6년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: value_10y=101.0, revenue_5y=13.60x, price=4.9, upside_10y=20.49x, buy_below=20.2
- 슬레이터 case={"from": "base"}: cash_survives=아니오, cash_min=-9,134만 USD, runway_years=7.1, price=4.9
- 애크먼 case={"from": "base"}: fcf_positive=아니오, leveraged=아니오, intrinsic_value=3.4, price=4.9, mos=-46.9%, buy_below=2.7
- 클라만 case={"from": "base"}: fcf_positive=아니오, leveraged=아니오, net_cash_ps=3.4, no_growth_ps=3.4, owner_fcf=-2.4억 USD, hard_value=3.4, hard_basis=net_cash_ps, low_52w=4.9, high_52w=22.5, intrinsic_value=3.4, iv_low=0.6, iv_high=3.4, price=4.9, mos=-46.9%, downside=30.6%, growth_premium=30.6%, buy_below=2.3, traded_below_52w=아니오

### 계산 경고

- 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-10-09 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926115030/tm2627277d1_6k.htm) |  |
| S2 | filing | 2026-10-07 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926114347/tm2627105d1_6k.htm) |  |
| S3 | filing | 2026-10-02 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926112948/tm2626664d1_6k.htm) |  |
| S4 | filing | 2026-09-23 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926109772/tm2625374d1_6k.htm) |  |
| S5 | filing | 2026-09-04 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926105488/tm2624542d1_6k.htm) |  |
| S6 | filing | 2026-08-25 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_6k.htm) |  |
| S7 | filing | 2026-08-18 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926098113/tm2623382d1_6k.htm) |  |
| S8 | filing | 2026-08-14 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926096218/tm2623123d1_6k.htm) |  |
| S9 | filing | 2026-08-06 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926091620/tm2622408d1_6k.htm) |  |
| S10 | filing | 2026-07-17 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926084382/tm2620742d1_6k.htm) |  |
| S11 | filing | 2026-07-09 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926082064/tm2620042d1_6k.htm) |  |
| S12 | filing | 2026-07-07 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926080970/tm2619928d1_6k.htm) |  |
| S13 | filing | 2026-06-10 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926072318/tm2617438d1_6k.htm) |  |
| S14 | filing | 2026-06-08 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926071135/tm2617119d1_6k.htm) |  |
| S15 | filing | 2026-06-04 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926070495/tm2616910d1_6k.htm) |  |
| S16 | filing | 2026-06-03 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926069822/tm2616773d1_6k.htm) |  |
| S17 | filing | 2026-05-26 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926066016/tm2615604d1_6k.htm) |  |
| S18 | filing | 2026-05-07 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926056672/tm2613910d1_6k.htm) |  |
| S19 | filing | 2026-05-06 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926055882/tm2613708d1_6k.htm) |  |
| S20 | filing | 2026-04-22 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046441/tm261211d3_6k.htm) |  |
| S21 | filing | 2026-04-22 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046437/tm261211d2_6k.htm) |  |
| S22 | filing | 2026-04-22 | [20-F](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm) |  |
| S23 | filing | 2026-04-16 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926044041/tm2611986d1_6k.htm) |  |
| S24 | filing | 2026-04-02 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926038919/tm2610570d2_6k.htm) |  |
| S25 | filing | 2026-03-26 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926034888/tm269906d1_6k.htm) |  |
| S26 | filing | 2026-03-05 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926023721/tm268097d1_6k.htm) |  |
| S27 | filing | 2026-03-03 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926022480/tm267706d1_6k.htm) |  |
| S28 | filing | 2026-02-05 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926010640/tm265312d1_6k.htm) |  |
| S29 | filing | 2026-02-04 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926009891/tm264968d1_6k.htm) |  |
| S30 | filing | 2026-01-23 | [6-K](https://www.sec.gov/Archives/edgar/data/1969302/000110465926006018/tm263846d1_6k.htm) |  |
| S31 | filing | 2025-04-25 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/1969302/000141057825000895/0001410578-25-000895-index.htm) |  |
| S32 | news | 2026-08-18 | [China's Pony.ai plans to deploy more than 4,000 robotaxis abroad - Reuters](https://news.google.com/rss/articles/CBMizwFBVV95cUxQaUZLRVdHWnB1NFFOenZ4SHRKYmljRV9HWE9OTFMzSlBmaXNlNnFaQVNpclJjRXFCQ3V4LWxuTThwaHROd0NmeU5yc1l1QTQtOEVUNGYyX1lTM0dueHZkVGE0Y3lqbUk5QzR4d3NQZzhkcjdvWlhmMEpGd3BsRFJwd2EwMXhtWUV2a0RCMkFKei1hRUwzOGlndnlDcjBJOVlNQ19fTXJLMTBVLVVMMml4UjA2VHdQUWx5d3dtLVFxc1drc3VSVG14cGJQLXRXa2s?oc=5) | Reuters |
| S33 | news | 2026-08-19 | [Pony AI Is Scaling Robotaxis Fast—Can the Stock Reach BofA’s $17 Target? - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxQb2pwaTIwdkxXMWVCZUNuVmxGaUZjVUZKOWJDcU52cUc2YWtFSHo0ZEphQWs2NkwxLXRTUnBXa3pHaWFoWVVSZmVoLU1YNmVxNThiSV9lRUFacWRnOG5FcmVEaTZsN1Z3SDRRa0dFenFJQUtXQW8xZ2lLSHFGUjJZR1BCUG1SS2M1eHdXR2RVQXN4dkpkZUFzWXowWQ?oc=5) | Yahoo Finance |
| S34 | news | 2026-08-13 | [Uber partners with China's Pony.ai for 2,000 robotaxis in Europe - CNBC](https://news.google.com/rss/articles/CBMinwFBVV95cUxQQkpUaUFJdDNySDFnenkzQmFVRVV5cTktN0ZSakp5enc0UFp2T3VWc0lHU2taWHFCTV9uRmMwSUpKTU1vYTc1Q2YwbzZsYk5FcVE1bWtCVmZnRmRwbUFObmJoRHlzRnBqajRBQ1RzZHBwSTRrSlBpSkJUT3dFemQ5dkRzbzJqdWczWHo2S0wwaUpIX194cU44RGFTeWtLZjTSAaQBQVVfeXFMTm1FdkFRcy1fQzRXNlVUdHJmTDZaYVZiYjJ1MElheWpXejI0bnBpZ2JNcS0wNC0ySkczMVFJcHBRMFVvZHF5TWVVSnEyN0F0N2thbmRYbVhtaE1NTXg0Q29MUFNvVGtEblVvLUViQ2xXb1VIdEFfMzBPNF91WkF1eTNYdUZyWXpBS296X09HVTFidlNOVDAtcWpZTm52bG9PeXgzZ2E?oc=5) | CNBC |
| S35 | news | 2026-09-08 | [Pony.ai CEO James Peng thinks robotaxis will be widespread within five years - Fortune](https://news.google.com/rss/articles/CBMickFVX3lxTE1FRUNEbHowbnZjM01oSS1MeEJhSzVkcEhCYzE1OHdzbXpkeGxTOGhGMm0yUVFyS2o1Ym5LLXpiT0lPU2dBbGxYR0F6bWg5TW9ZN2FhS3pseVo0ei1EYUFub1lNSlh2ODNHRmt3VTRvRTAzUQ?oc=5) | Fortune |
| S36 | news | 2026-08-18 | [PONY AI Inc. Reports Second Quarter 2026 Financial Results: - GlobeNewswire](https://news.google.com/rss/articles/CBMixwJBVV95cUxQVGlWRUFvQjJieHphYVI1NlBIRlVxaGg5V1o0RXFId3VzS2pBVHkycTBZUzlXYzNveDZMX1JPZGhuZlFhN3RtMkwxdU9EWWU4emNQeEpYV2VNUmlVV21mTVlUN0R3UkVRaFdfdzJYelhFbGgtNllSWV94RnBmWUFhZWhPbnZpeHlJTmZacDgwZGV4bVRHSXZLYThGX0FhNVM4eHB6VVl0Q19vMWtwX2tNMjhhMy1wRkpXV2szWEV5SWNBRkpUYk80WnQtQUlfeS1MeGVNVFBIamlmLXFwdm9GaTh4ZG1DaUlyZjRxdllvQVJrM1l6SUVSaDN5dXRMbzROR0FwUXhHakV6U3NQN3JPTmVmNnpIM0ZfR0o1dTVpN2hYYUphNFlrbW1aR0JnX2h1ZFBfMXhHNWdJVEtVb0hRM01wY1piMVk?oc=5) | GlobeNewswire |
| S37 | news | 2026-10-08 | [Uber and China’s Pony.ai plan to launch robotaxis in London - TechCrunch](https://news.google.com/rss/articles/CBMimAFBVV95cUxPRWphNWlOMkMwRUJyX1RPVGJOeTRaOHJBQi1YcUZtcXNnZUMtNDVDb3FBV3JkV01zWjZvN1czbUxlaDk0bVFoTV80cUg5UGE3OTRaLTZ3SkhBNjZkbXZPZnZxQ3Z2LWxrcG5IdUNSRVk5MGJUVlpQdGZQUjNfbmFlMFBuMllqcHF4MHBaZ0ZYZ2hSRGtEeDRfNA?oc=5) | TechCrunch |
| S38 | news | 2026-08-18 | [Pony AI’s Robotaxi Revenue Reaches Record as Sales Jump 69% - Bloomberg.com](https://news.google.com/rss/articles/CBMirgFBVV95cUxNdW84MlY3VVNtaG1QYjdubXR4VnZaVHJqQW9wd2UyWDUtYUc5OGYyU1N5WklRdEpWQlE3dzhMUlJJMkVoblltdjdmOG9uNHF3RUNnd21hZHNuYTZwQTFNWVh5VlU2eUJSRmk1UmFUQUdNaV8zcGRBdmswRUh3Zm03ODJGMVRxN09ZWlNaWlpfUW8tRTBqcGJNbTlkQXRJVnRlY19Famhxa2s2My13MXc?oc=5) | Bloomberg.com |
| S39 | news | 2026-09-14 | [China's Pony.ai unveils latest robotruck model as it targets European sales - Reuters](https://news.google.com/rss/articles/CBMi0gFBVV95cUxQR2VTZTJjcl9FYW90RGw2alJpUEhuS0R6QkNyYXJIdnZnZHNWS0haWmpEel9iUi1TSUlfbkdhbU83NTBqemd3aVZiX0ZmUUFUR09faUNpRzdBQ0M5ZV9ISmpSTGZqX29kTVJwb3RDVFdvRVY3dVo5OHdqSm9YQUJFQXh0UWxwbWF6UGVZRmtRYkRCdGRxSW1MRnBqeUNaSHVjVWowcGlaYVJfLXBUSFY2WnpHWi1uWk5SRng0eUpSRmdrRUJFci16UFdGbWwxNkpkLXc?oc=5) | Reuters |
| S40 | news | 2026-08-15 | [Pony AI (PONY) Stock May Sit Above Fair Value After A 49% Fall - Yahoo Finance](https://news.google.com/rss/articles/CBMikAFBVV95cUxOaGRzRHgyR2FIeWdQelRWX3diX2dxWEFnWDB0VDVRdUFHWXNiemJmaXVoeTUzUFpVTWRTay11bG00N2NfWlo0SmRfdFRrYjNjMEhEcWdIbS1XZE1DWkdQRUx6Q192REhlQVZMQkRTaElfVVhWcEtQQjY2Qmc4UWNKMFBvVThYWFd5dzR1bTN4Q00?oc=5) | Yahoo Finance |
| S41 | news | 2026-08-13 | [Uber and China’s Pony AI to Deploy 2,000 Robotaxis in Europe - Bloomberg.com](https://news.google.com/rss/articles/CBMisAFBVV95cUxQNGxSVjE2azc0QTRBUC1yQXQtSzA5RExGOEVDVUUxWGlRYkN6czBSRFczcmJzTDRMQU05RXZKUHpabHNSQjcxc095QTdEOF9PWWwwelNTamRKNGZkemNMSl85NVlRWGxIblVuT2Y4eVUwVU1JR0JIREV5MTZUMFRoYy1QZkJBZVRPMzI1OFBLRFFwU1haRHY2MlFpV2lqcTc5MW8wT25HcVNoNXNsTHBaWg?oc=5) | Bloomberg.com |
| S42 | news | 2026-08-18 | [Pony AI Inc (PONY) (Q2 2026) Earnings Call Highlights: Robotaxi Revenue Soars 691% as Operating ... - Yahoo Finance](https://news.google.com/rss/articles/CBMijAFBVV95cUxPVDczS3QxRll4OGxmSzFHMmZPel9TUExfOXhwb2hrMlFzOFNzb1laT2hFS3VFNTc2ZEZDd3AwTUdDMzQwdXR0dkZacHhaM1V6TUxxMk1vVjFnbkdqOXdPdWRIY0xXRmtsNHBLa1RJNVVpU1hva0RjQjYtaVk4U1QwdDU2OXhCWkg4MkVMdg?oc=5) | Yahoo Finance |
| S43 | news | 2026-08-13 | [China's Pony.ai, Uber to jointly deploy over 2,000 robotaxis in Europe - Reuters](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5) | Reuters |
| S44 | news | 2026-08-21 | [What Does Pony AI (PONY) Launching Its First European Robotaxi Service Mean? - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxOQURhUUozVWpFbm9DTno3LXV4d2pvNGxVeGlUSlFHaGV1MWEzbE1IZ0RyYnh3eDR4ck1BQlVGWmdLYllYOXVDbFFRdTk0S0dsaFpZT3JCMkNPMjQ2amZWeVlubzU3bDlQbFpmdGxRMnV4T3ZDaGFoZkxvLVhudVBXeG5aYUlpTHRSN0pnUkNTRWxROHY0TXc?oc=5) | Yahoo Finance |
| S45 | news | 2026-08-19 | [Pony AI Stock Gains Traction as Robotaxi Fleet Expands Globally - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxQUEU2M05qQ0RoZmNRb2tCSDJPNWhZQ1F6LTJJT1NvSkpRWm1reDNic0J1X0U0clRYZGN5WXBqU21yc3Y0Qk0xaHNidjJNTDFHTjBHX3JSbXdSRU1qcUhXSkQwM0R3R2pDTlNZWEdubVgwWXNTR3dEZlZweXM4bm9HUUt0alZJT2xiUWRiTU5ZNGFHckxHRlJScw?oc=5) | Yahoo Finance |
| S46 | news | 2026-08-15 | [Is Pony AI (PONY) Undervalued Following Its Uber Robotaxi Expansion Plan? - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxONzM5TENxN1VUdUFwbmU3eG5mQXNDeXJkR25mVGYzbm1FWVc4QzNKOUpROFk3ODBwdVpiU21qZXV6WE03Ym1PRm5KaVQ4azFIV3NBSmRWMjJ4NlpxSTlwLWlyLXhlaVcyWm8zZGcyQnhfbDBoTUV4Unk3TEpXNWo0SVpoNmM3NktYQWN0T1NscDZLTzZRV0FSOFM4Q1lHYkxm?oc=5) | Yahoo Finance |
| S47 | news | 2026-08-27 | [Pony AI (PONY) Sees Robotaxi Fares Soar as Global Fleet Expands - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxOWUx3dmJURUlPLW9xSEpqNHoyVVB6V1M1WXV5VjhGYmhTX2hGR3UtTmlGQTdzOHlCR2FiS1ZIMjZzSnF0M2RyR0k4a09LTmxBU3ZPVVRLSGNwcUpJWHJydUlaR2RPWllBY25VdGYzbWZNWmZTRC1QR3FWOW95WFlGblZaUnlJSHlHN25MOVRxYmRBUjI4TXc?oc=5) | Yahoo Finance |
| S48 | news | 2026-08-16 | [Pony.ai (PONY) and Uber (UBER) Team Up For A Bigger Bet - Yahoo Finance](https://news.google.com/rss/articles/CBMikAFBVV95cUxNaDhmbTlUcGpNOGg1b3ZYX3lqNWJla2l4dHFWbkRZdVlMdEVXUk80QkJHRmNRMV83YmNVRjNXbTlMZm94dHRVVGg0UjlOOWxLblZFSElkVmdnWkJkVHJKMm9renMyNHl5TVFocm9VSWpUa0p6a0hBTWJBV0RELTJIbVJ5R1ZPTFBwNkJiQnRwcWo?oc=5) | Yahoo Finance |
| S49 | news | 2026-08-17 | [2,000 Robotaxis, Four New Cities: Pony AI, Uber Accelerate Europe’s Driverless Push - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxOS1oxVU5wY2VrWm9QUGF5a1oySExrQ0NySXRPa1BPdnlRQXRCR1FrVWVSeVVSWE5jQThlSzEyMEtNRC1PdnFrOVVlMGtCTHp4UVJxWElMRV9GS3RiVmdvWjVJTDc3LWJKamNLQTRKNjBXMk5reEpJOERfVENtM0k5Rk1yLTBIUmZZWkxYZUdPbWRoTW9NTlE?oc=5) | Yahoo Finance |
| S50 | news | 2026-08-18 | [Pony.ai Expands Overseas Robotaxi Pipeline Beyond 4,000 Vehicles - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxPWm94c24xeGcyMlA5MGZnNE8zWmJqX0JaU1YyV3Jqb1Q2VGJwaGJ1Q2NjNG5QZnBweHpGdkRWUjFxUWFqMG1HYWtzNEtkQzdSZVpzUDlqTm5uZk1EZmpXV3BuUHRIaXg0Z3JRZjJHWlVHSWl0d2EzTm00QWhKODVoeDhqTG5DSnBraEpCMG5MZjVFcmpRdEJiWlh3?oc=5) | Yahoo Finance |
| S51 | news | 2026-08-18 | [What's Going On With Pony AI Stock Tuesday? - Pony AI (NASDAQ:PONY) - Benzinga](https://news.google.com/rss/articles/CBMivwFBVV95cUxOenVaYTNEV19wVW4wY0NSY3NhbWRWNWd2MmV0NFVKQnVCRm1KLUhqUnRPTGJ1NGRfc0dzTVZ3dktzZURpLWN4bDlCTnpaRjV2UEZuXzBZVnJZbjh6bWVnakpIS1BRYlVnQXhGY1dTU19YeV9CenR6RDViUTFRNWR0SGsxdGhZcTl1dEdpdXdjd19BVzlyZFVtQkRwMG5KRVd2RjRERTcxXzBMMWh2M2ZSc1JSTE9OVVo0LThaQzhpdw?oc=5) | Benzinga |
| S52 | data | 2026-09-22 | [Pony AI Inc (PONY) Stock Price, Quote, News & History - Benzinga](https://www.benzinga.com/stock/PONY) | PONY 나스닥 종가 $7.29 (2026-09-22, 일중 범위 $6.88~$7.42). 10월 종가는 찾지 못했다. 이 가격은 기준일(2026-10-18)보다 약 4주 전이다. 참고: 2026-08-18 종가 $7.75, 52주 범위 $6.58~$24.06 (Walnut Invest). |
| S53 | news | 2026-08-18 | [PONY 2Q26 AI Summary - platformaeronaut](https://transcripts.platformaeronaut.com/summaries/PONY-2Q26-AI-Summary) | 제3자 요약. 2분기 순손실 약 $45.4M, 6/30 현금성 자산 약 $1.39B, 2분기 영업현금유출 약 $44M. 6-K 본문으로 확인하지 못한 수치이므로 사실로 넣지 않았다. |
| S54 | call | 2026-08-18 | [Pony AI Inc. Reports Second Quarter 2026 Financial Results (6-K Ex.99.1)](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) | 2026년 2분기 총매출 약 $36.2M, 전년 대비 +68.8%. 로보택시 서비스 매출 $12.1M, 전년 대비 +691.2%. 요금 징수 매출은 +849.3%. 로보택시 1,975대, 연말 3,500대 이상 목표. Uber와 유럽에 2,000대 이상 공동 배치 계획. |
| S55 | data | 2026-10-16 | [Yahoo Finance PONY historical prices](https://finance.yahoo.com/quote/PONY/history/) | 2026-10-16 종가 4.93 USD |
| S56 | filing | 2026-04-22 | [PONY 20-F (FY2025) — XBRL us-gaap:PaymentsToAcquireProductiveAssets](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/) | 20-F 현금흐름표 us-gaap:PaymentsToAcquireProductiveAssets FY2025 = 43,875,000 USD |
| S57 | filing | 2025-11-25 | [Pony AI Inc. Reports Third Quarter 2025 Financial Results (6-K Ex.99.1)](https://www.sec.gov/Archives/edgar/data/0001969302/000110465925115594/tm2532036d1_ex99-1.htm) | 2025년 3분기 총매출 US$25.4M(전년 대비 +72%), 총이익 US$4.7M(총이익률 18.4%), 순손실 US$61.6M. 로보택시 매출 US$6.7M. 현금 잔액은 검색 요약에 없어 확인하지 못했다. |
| S58 | news | 2026-08-14 | [Pony.ai and Uber Plan Deployment of More Than 2,000 Robotaxis Across Europe - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxPT205NDc5ZXViTEpDVFM3ZjlldGtYdXZSaWloLW1NSTU2WGtORS0xdEo1RWN1bzBNbWwzTHJlMTZXUGhuWGVUVTNYa05LaVZha3Q3UmQwbEZWV3R0dXJ4LVdzMXlUZWl0ZjB3amtFSFFFWHRLQ3JicmZCdlRXU0pmMi1TeVNjaEpPUGFLaVIybUZ2SGNpSkpV?oc=5) | Yahoo Finance |
| S59 | news | 2026-08-19 | [Pony.AI Has Plans For 4,000 Robotaxis Outside China - AI Business](https://news.google.com/rss/articles/CBMihwFBVV95cUxNUEMxUTZFUmxtTXB4VGxNQ0dxX3NQTldLT0xabGRWZmR0UEJYdHA4TjhCYXNLQUFXVF9xeF9yTVplSGkzVXVTUUw2dzJhSEw0NEE0MVM2ZGFyU01lei1fSnE3RF9PWFN0emZNNlc3cXM5d1Q5c25rVGJ3YVdvVWNmNjhBRWtCT28?oc=5) | AI Business |
| S60 | filing | 2026-08-18 | [Pony AI Inc. Reports Second Quarter 2026 Financial Results (6-K Ex.99.1) — 사업부별 매출·이익률·영업손실](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#segments-margins) | 2026년 2분기(2026-06-30 종료) 1차 공시. 총매출 US$36.22M, 전년 US$21.46M 대비 +68.8%. 로보택시 서비스 US$12.07M(+691.2%, 전년 US$1.53M), 요금 징수 매출 +849.3%. 로보트럭 서비스 US$13.33M(+40.0%, 전년 US$9.52M). 기존 'Licensing and applications' 부문을 'Intelligent solutions'로 이름을 바꿔 공시: US$10.82M(전년 US$10.41M, 약 +4%) — CFO는 도메인 컨트롤러 납품 변동 탓으로 설명(어닝콜). 상반기 누계 매출 US$70.47M(로보택시 US$20.64M, 로보트럭 US$23.52M, intelligent solutions US$26.30M). 매출원가 US$29.87M, 총이익 US$6.35M, 총이익률 17.5%(전년 16.1%, 2025년 4분기 12.7%). R&D US$56.2M(+14.7%), SG&A US$15.9M(전년 수준), 영업손실 US$65.7M, Non-GAAP 영업손실 US$56.7M. SBC US$9.05M(R&D US$6.36M, SG&A US$2.69M). 가중평균 주식 수(기본=희석) 433,551,136주(전년 366,831,015주), 주당순손실 US$0.14. 로보택시는 2분기 매출의 약 1/3이다. |
| S61 | filing | 2026-08-18 | [Pony AI Inc. Reports Second Quarter 2026 Financial Results (6-K Ex.99.1) — 순손실·비지배지분·공정가치 이익·손상](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#net-loss-nci) | 2분기 연결 순손실 US$45.35M(전년 대비 −14.9%). 비지배지분에 순이익 US$14.5M이 배분되어 Pony AI Inc. 귀속 순손실은 US$59.84M으로 연결 순손실보다 크다(사실 net_income은 귀속 기준, net_income_consolidated는 연결 기준, net_income_nci는 비지배지분 몫 순이익이며 양수가 이익). Non-GAAP 순손실 US$44.7M. GAAP 순손실을 줄인 항목: 단기매매증권 공정가치 평가이익 US$33.4M(상반기 누계 US$25.7M). 반대로 일회성 '장기투자 선급금' 손상 US$25.0M — 회사는 '관련 사업의 선제적 전략 조정과 새 전략적 파트너 참여에 따라' 회수할 수 없다고 판단했고, 선급금 잔액은 US$25.0M에서 0이 됐다. 무엇에 대한 선급금인지는 공시하지 않았다. 기존 S53(제3자 요약)의 순손실 약 US$45.4M은 연결 기준 수치로 이 1차 자료와 맞는다. 평가이익이 2025년 4분기·FY2025·2026년 2분기 연속으로 GAAP 순손익을 좋게 보이게 했으므로 영업손실과 Non-GAAP 수치가 사업을 더 잘 보여 준다(노트 추론). |
| S62 | filing | 2026-08-18 | [Pony AI Inc. Reports Second Quarter 2026 Financial Results (6-K Ex.99.1) — 현금흐름·유동성·재무상태표](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#cash-flow-liquidity) | 2분기 영업현금흐름 −US$44.0M(전년 −US$25.4M), 설비투자 US$32.2M(전년 US$9.6M, 약 3.4배), Non-GAAP FCF −US$76.2M. 상반기 누계: 영업 −US$118.2M, 투자 +US$160.9M(투자자산 회수), 재무 −US$0.4M, 설비투자 US$44.6M, FCF −US$162.8M. 상반기에서 2분기를 빼면 1분기 영업현금유출은 약 US$74.2M, 1분기 설비투자는 약 US$12.5M이다(노트 계산) — 어닝콜 요약의 'US$774.2M'은 오기로 보인다. CFO는 영업유출 증가를 운전자본·매입채무 결제·하반기 차량 증설 대비 재고 확충으로 설명(어닝콜). 2026-06-30 유동성(현금·현금성자산·단기투자·제한현금·자산관리용 장기 채무상품 합계) US$1,390.5M, 2026-03-31 US$1,435.5M(2025-12-31 US$1,514.8M은 4분기 보도자료). 보도자료에 '총유동성' 별도 행은 없다. 재무상태표 구성: 현금 US$327.1M, 제한현금 US$4.8M, 단기투자 US$787.0M, 장기투자 US$375.7M. 장기투자 가운데 회사 유동성에 들어가는 것은 장기 채무상품 부분뿐이고(노트 추정 약 US$271.6M) 나머지는 다른 투자다 — 하네스 순현금(현금+단기투자+장기투자)은 회사 유동성 정의보다 넓다. 단기투자에는 2025년 말 기준 보호예수 중인 Level 3 GPU 투자사 지분(US$138.8M)이 들어 있었고 6/30 보유 여부는 확인하지 못했다. 차입금 없음, 총부채 US$93.0M, 비지배지분 US$70.1M(2025-12-31 US$56.7M), 순유형자산 US$98.5M(2025-12-31 US$60.5M). 매출채권 US$43.3M(2025-12-31 US$23.6M, F52) — 상반기에 약 83% 증가. 하네스 forensic의 'DSO 개선' 판단과 반대 방향이다. |
| S63 | filing | 2026-08-18 | [Pony AI Inc. Reports Second Quarter 2026 Financial Results (6-K Ex.99.1) — 가이던스·차량·해외](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm#guidance-operations) | 수치 매출·이익률 가이던스는 없다. 문구: '연간 로보택시 서비스 매출 목표를 넘어설 자신이 있다'(목표 배수는 어닝콜에서 CEO가 '작년의 3.5배 초과'로 제시). 연말 로보택시 3,500대 초과 목표(2026년 3월에는 3,000대 초과에서 상향) — 2026-06-30 차량 1,975대(F78), 연말까지 하반기에 약 1,525대(월 약 250대) 추가가 필요하다(노트 계산). 중국 1선 도시에서 '양(+)의 단위경제'라고만 적었다. 'Uber가 유럽에서 2,000대 이상을 계약(contracted)' — 해외 4,000대 이상 규모로 협상 중인 계약 안에 포함. 싱가포르는 ComfortDelGro의 Zig 앱에서 공공 서비스 운영 중. 중동은 상투적 문구로만 언급. PonyPilot 중국 등록 이용자 150만 명 초과. 2026년 3분기 실적 발표일은 2026-10-18 현재 공지되지 않았다(2분기는 2026-07-17 이사회 일정 공지 후 2026-08-18 발표). |
| S64 | filing | 2026-03-26 | [Pony AI Inc. Reports Fourth Quarter and Fiscal Year 2025 Financial Results (6-K Ex.99.1)](https://www.sec.gov/Archives/edgar/data/1969302/000110465926034888/tm269906d1_ex99-1.htm) | [6개월 초과] FY2025 매출 US$90.0M(+20.0%): 로보택시 US$16.6M(+128.6%), 로보트럭 US$40.6M, licensing & applications(현 intelligent solutions) US$32.8M. 2025년 4분기: 매출 US$29.1M(−18.0%), 로보택시 US$6.7M, 로보트럭 US$13.1M, licensing & applications US$9.4M(−53.2%), 총이익률 12.7%, GAAP 순이익 +US$75.5M(단기매매증권 공정가치 이익 때문), Non-GAAP 순손실 US$49.0M, 영업현금흐름 −US$28.6M, 설비투자 US$6.6M. 유동성 US$1,514.8M(2025-12-31, 홍콩 상장 대금 반영), US$587.7M(2025-09-30). 차량은 1,400대를 넘었고 2026년 목표는 3,000대 초과, 2026년 말 전 세계 20개 넘는 도시(절반 가까이 해외). Toyota bZ4X 1,000대를 2026년 공동 배치용으로 확보. 70% BOM 절감은 Gen-4 로보트럭 ADK에 대한 것이다(로보택시 아님). 도하 파트너 Mowasalat(Karwa). |
| S65 | filing | 2026-04-22 | [Pony AI Inc. Annual Report (20-F, FY2025) — 감사보고서·핵심감사사항](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#audit-report) | 감사인 Deloitte Touche Tohmatsu Certified Public Accountants LLP(베이징, PCAOB ID 1113), 2022년부터 같은 감사인. FY2025 재무제표 적정의견, 2025-12-31 내부회계관리(ICFR) 적정의견 — 두 보고서 모두 2026-04-22. 신흥성장기업(EGC) 지위를 잃어 ICFR 감사인 증명이 요구됐다. 핵심감사사항(CAM) 1건: R&D 비용(US$217.4M, F60)의 분류 — 급여 분류, SBC, 감가상각 검증. 감사·감사관련 보수 FY2025 US$1.96M(FY2024 US$1.53M). PCAOB의 Deloitte 중국 법인 현재 검사 상태는 확인하지 못했다. |
| S66 | filing | 2026-04-22 | [Pony AI Inc. Annual Report (20-F, FY2025) — 의결권 구조·주요 주주(2026-03-31)](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#major-shareholders) | Class A는 1주 1표, Class B는 1주 10표(홍콩 상장규칙상 '유보 사항'은 1주 1표). Class B는 Class A로 1:1 전환된다. 2026-03-31 발행주식 433,541,553주(Class A 352,452,783주, Class B 81,088,770주) — 기존 F65(end 2025-12-31로 기록)는 이 2026-03-31 수치다. 2026-03-31 실질 소유: CEO 펑쥔(Jun 'James' Peng) Class B 60,000,000주, 경제적 지분 13.8%·의결권 51.6%. CTO 러우톈청(Tiancheng Lou) Class B 21,088,770주 + Class A 191,025주, 4.9%·18.1%. Toyota Class A 42,453,831주, 9.8%·3.6%, 이사회 1석(Takeo Hamada). HongShan 계열 5.2%·1.9%. 이사·임원 전체 19.5%·70.0%. 창업자 두 사람이 의결권 약 69.7%를 쥐고 있어 소액주주는 자본배분을 바꿀 수 없다. 반면 창업자의 경제적 지분이 커서(펑 약 13.8%) 이해관계는 일치한다. |
| S67 | filing | 2026-04-22 | [Pony AI Inc. Annual Report (20-F, FY2025) — 특수관계자 거래(Sinotrans·Toyota·Zhuifeng)](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#related-party-transactions) | 로보트럭 자회사 Cyantron의 비지배주주인 Sinotrans에 '가상 운전자 운영 및 관련 서비스' 매출: FY2023 US$22.5M, FY2024 US$30.7M, FY2025 US$29.6M. 2025-12-31 Sinotrans 미수금 US$10.15M. 노트 계산으로 Sinotrans는 FY2025 매출의 약 33%이고, 전부 로보트럭 매출이라면 로보트럭 매출의 약 73%다. 로보트럭 성장의 상당 부분이 특수관계자이자 소수지분 파트너와의 거래라서 고객 집중과 거래 조건의 독립성 문제가 있다. 기타 특수관계자 매출(FY2025): Toyota US$0.1M, 지분법 피투자사 Zhuifeng Intelligent(광저우) US$1.1M. |
| S68 | filing | 2026-04-22 | [Pony AI Inc. Annual Report (20-F, FY2025) — 임원 보상·SBC·주식보상 제도](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#compensation-sbc) | FY2025 이사·임원 보상 총액(SBC 제외) US$7.3M, 연금 적립 없음. 개인별 CEO 보상액과 KPI 연동 보너스 지표는 찾지 못했다. SBC: FY2024 US$127.0M 중 US$120.7M은 2024-11 나스닥 상장 때 누적 가득분을 일시 인식한 것이다. FY2025 SBC는 US$30.8M. 2025-12-31 미인식 SBC US$67.9M. 2016 계획 한도 58,427,257주, 2025-12-31 미행사 옵션·RSU 9,780,610주, 상장 후 2016 계획으로는 신규 부여 없음. 2026-04-02 새 2026 Share Scheme 채택(한도는 확인하지 못했다). 2026년 2분기 SBC US$9.05M은 2분기 매출의 약 25%다(노트 계산). |
| S69 | filing | 2026-04-22 | [Pony AI Inc. Annual Report (20-F, FY2025) — FY2025 순손실 조정·GPU 투자사 지분(Level 3)](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#fair-value-investments) | FY2025 연결 순손실 US$76.76M(세금 0이라 세전손실 F48과 같다), Pony AI 귀속 순손실 US$133.97M(F36). 차이 US$57.21M은 비지배지분 몫 순이익이다. 따라서 하네스가 본 '세전 −US$76.8M vs 순손실 −US$134.0M 불일치'는 귀속 기준 차이로 풀린다. 영업손실 US$260.86M(F44)에서 세전손실까지: 투자수익 US$43.0M, 단기매매증권 공정가치 변동 +US$128.0M, 기타수익 US$13.1M. 공정가치 이익의 원천은 2025-12 상장한 이름 미공개 GPU R&D 피투자사다. FY2025 공정가치 이익 US$136.9M(그중 US$16.9M은 기타포괄손익에서 재분류), 2025-12-31 장부가 US$138.8M(단기투자에 포함). 12개월 보호예수 대상이며 시장가에 시장성 할인 11%를 적용한 Level 3 평가다. 2025-01에 이 지분 일부를 US$16.7M에 팔았다. 2024-07 상장한 차량호출 피투자사 지분은 2024-12-31 US$19.7M. 즉 '현금·투자자산' 일부는 변동성 큰 보호예수 상장주식이고(보호예수는 2026-12 무렵 풀린다, 노트 추정), GAAP 순손실은 평가이익 때문에 작아 보인다. 2025년 말 장부가를 빼면 조정 유동성은 약 US$1.25B다(노트 계산). |
| S70 | filing | 2026-04-22 | [Pony AI Inc. Annual Report (20-F, FY2025) — 나스닥 상장·우선주 전환·홍콩 상장(희석 설명)](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#share-capital-history) | 2024-11 나스닥 상장: ADS 21,461,410주를 US$13.00에 발행(순 약 US$256.7M), 동시 사모로 Class A 11,672,186주(순 약 US$151.7M). 상장 때 우선주 202,699,487주 전부가 Class A 보통주 225,409,798주로 전환됐다. 2025-11-06 거래를 시작한 홍콩 이중 1차 상장: Class A 48,249,000주를 HK$139.0에 발행, 순 HK$6,509.7M(US$829.4M). 같은 20-F의 다른 부분은 순 HK$6,454.4M로 적어 내부 수치가 조금 어긋난다. FY2025 재무활동 순유입 US$814.8M은 대부분 상장 대금이다. [희석 설명] 하네스의 '희석 주식 수 연 64.5%·FY2025 +232.3%' 신호는 대부분 가중평균의 회계상 착시다. FY2024 가중평균 희석 주식 수(114.3M, F20)에는 2024-11 상장 때 우선주 전환으로 생긴 225.4M주가 빠져 있었다. FY2025의 실제 신주 발행은 홍콩 48.249M주뿐이고 홍콩 상장 전 주식 수 대비 약 12.5%다(노트 계산). 2026-03-31→2026-09-30 발행주식은 433.54M주→435.18M주로 약 0.38% 늘었다(노트 계산). 2026년에는 후속 공모·선반등록·전환사채가 없다(EDGAR 제출 목록). 1 ADS = Class A 1주이고, 홍콩 주식과 ADS는 서로 전환할 수 있다. 예탁기관은 Deutsche Bank Trust Company Americas. |
| S71 | filing | 2026-04-22 | [Pony AI Inc. Annual Report (20-F, FY2025) — 미·중 규제 위험 요인](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm#risk-factors-us-china) | HFCAA: PCAOB가 중국 소재 감사인을 검사하지 못하면 거래가 금지될 수 있다(PCAOB는 '과거에' 검사할 수 없었다). 상무부 커넥티드카 최종규칙(2025-01-14): Pony는 미국에서 차량을 운영하지 않고 미국 사업은 R&D뿐이며, 필요하면 미국 R&D를 바꾸거나 철수할 수 있다. 수출통제: 제품 분류는 EAR99 또는 5A992.c이고 BIS가 강화할 수 있다. 미국 해외투자 프로그램(OIP): Pony는 '대상 외국인(Covered Foreign Person)으로 간주될 가능성이 높다'(로봇 제어용 AI). 중국 외환·자본금 규정이 해외 상장 대금의 역내 투입을 제한할 수 있다. 홍콩 이중 1차 상장과 ADS·홍콩 주식 상호 전환 덕분에 미국 상장폐지는 존립 위험이 아니라 거래소 전환 위험에 가깝다(노트 추론). 다만 OIP·제재로 인한 미국 보유자의 강제 매도 가능성은 남는다. |
| S72 | filing | 2026-10-07 | [Pony AI 6-K Ex.99.1 (2026-10-07) — 2026년 9월 홍콩거래소 월간 주식 변동 보고](https://www.sec.gov/Archives/edgar/data/1969302/000110465926114347/tm2627105d1_ex99-1.htm) | 2026-09-30 발행주식 Class A 354,095,390주 + Class B 81,088,770주 = 435,184,160주, 자사주 없음. 9월 한 달간 Class A 770,545주 증가. 시가총액·EV 계산의 현재 주식 수로 쓴다 — FY2025 가중평균 희석 주식 수 379.9M주(F21)보다 크다. |
| S73 | filing | 2026-10-09 | [Pony AI 6-K Ex.99.1 (2026-10-09) — 2026 Share Scheme RSU 부여](https://www.sec.gov/Archives/edgar/data/1969302/000110465926115030/tm2627277d1_ex99-1.htm) | 2026-10-09 직원 124명에게 RSU 1,638,591주(발행주식의 0.38%)를 매입가 0에 부여했다. 4년 분할 가득(그중 12,500주는 2년)이며 성과 조건은 없다. 공시에 적힌 2026-10-08 ADS 종가는 US$5.76. |
| S74 | filing | 2026-08-25 | [Pony AI 6-K Ex.99.1 (2026-08-25) — Sinotrans 계속적 연결거래 연간 한도 수정](https://www.sec.gov/Archives/edgar/data/1969302/000110465926100791/tm2623870d1_ex99-1.htm) | 2026-08-25 이사회가 Sinotrans 운송 서비스 기본계약의 연간 한도를 상향했다 — 2026년 상반기 거래량으로 보아 기존 한도로는 '충분하지 않다'. Sinotrans 계열사와 화물 포워딩·물류 기본계약도 새로 맺었고, 모두 홍콩 상장규칙상 계속적 연결거래다. 한도 금액과 가격 조건은 노트에서 추출하지 못했다. 특수관계자(로보트럭 자회사 비지배주주) 매출 의존이 2026년에도 이어진다는 뜻이다. |
| S75 | filing | 2026-08-14 | [Pony AI 6-K Ex.99.1 (2026-08-14) — Uber와 유럽 로보택시 2,000대 이상 배치](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926096218/tm2623123d1_ex99-1.htm) | Uber와 유럽 전역에 로보택시 2,000대 이상을 배치한다. 대상은 자그레브(상용 서비스 운영 중, Uber 앱 '곧 제공')와 이름을 밝히지 않은 4개 도시를 합한 5개 도시이고, 중동 계획은 구체적이지 않다. '차량 자금과 소유는 시장에 따라 다른 파트너가 맡을 수 있다' — 자그레브는 Verne이 차량을 소유·운영한다. 수익 배분·독점·계약 기간·Uber 지분 투자는 공시하지 않았다. 2분기 보도자료는 이를 'Uber가 유럽에서 2,000대 이상을 계약'으로 적었다. Pony는 Bolt와도 일하고 Uber도 WeRide·Baidu 등 경쟁사와 일하므로 독점이나 전환비용 해자의 근거는 없다(노트 추론). Uber·Pony 런던 출시 계획은 S37(2026-10-08 헤드라인) 참조. |
| S76 | call | 2026-08-18 | [Pony AI Q2 2026 Earnings Call Transcript (Benzinga, 자동 전사)](https://www.benzinga.com/news/26/08/61272470) | [자동 전사본 — 문구는 공시로 확인 필요] CEO 펑쥔: 2026년 로보택시 매출 목표는 '작년 수준의 3.5배 초과'(FY2025 로보택시 매출 US$16.6M 기준). 콜 시점 차량 약 2,000대, '연말 3,500대 인도 궤도에 있다'. 하반기 로보트럭 성장은 '지속·강화'. 광저우·선전에서 단위경제가 흑자로 돌아섰고 UE 마진이 '지속 개선' 중이라고 했지만 일일 주문·가동률·회수기간 수치는 없었다. Gen-7 원가는 '매우 낮다'고만 했고 BOM 수치와 Gen-8 언급은 없다. 도시는 20개를 '넘을' 것으로 예상하며 창사·항저우·대만구(Greater Bay Area) 신규 도시를 계획한다. 광저우 서비스는 도심(하이주·톈허·황푸·판위)으로 300km² 이상, 700만 명 이상 규모로 넓혔고, 선전은 바오안 공항·선전만 항구·서커우 크루즈항을 잇는다. Gen-7 운행 차종은 GAC Aion V, BAIC ARCFOX Alpha T5, Toyota bZ4X. CFO: intelligent solutions 부진은 도메인 컨트롤러 납품 변동 탓이고, 영업현금유출 증가는 운전자본·매입채무 결제·재고 확충 탓이다. 로보트럭: Gen-4 양산, 장거리 운송 JV(전사본에서 이름 불명), China Merchants Port와 마완항 배치, CATL과 L4 경트럭 공동 개발(SF Express·China Post 파트너). 홍콩 Stock Connect 편입을 언급했고 자사주 매입 언급은 없다. |
| S77 | call | 2026-08-18 | [Pony AI Q2 2026 Earnings Call — 해외 자산경량(asset-light) 모델에 대한 CFO 발언 (Benzinga 전사)](https://www.benzinga.com/news/26/08/61272470#asset-light-model) | [회사 주장, 자동 전사본] CFO(전사본 표기 Liu Wang): 해외에서는 파트너가 '차량 자본과 현지 운영 능력'을 내고, Pony는 핵심 기술에 투자하며 국내 핵심 시장에서는 차량을 직접 소유한다. 역할 분담: Pony는 Gen-7 차량과 가상 운전자, 플랫폼(Uber·Bolt)은 수요, 운영사(크로아티아 Verne, 싱가포르 ComfortDelGro)는 차량 운영을 맡는다. Pony는 수익 배분이나 라이선스 수수료를 받을 수 있고 '현재 공동 배치 모델에서 차량 인도 매출을 선인식한다' — 즉 로보택시 '서비스' 매출이 순수 요금 매출이 아닐 수 있다(공시로 확인 필요). 파트너 공동투자로 '자본 규율을 유지'하는 것이 목표. 룩셈부르크에서 Bolt·Stellantis와의 배치가 '진행 중'. 수익 배분율과 차량 판매·서비스 매출의 구분은 공개하지 않았다. 해외 차량의 설비투자 부담은 줄지만 경제성을 차량 소유자·플랫폼과 나누고, 차량 인도를 선인식해 매출이 들쭉날쭉할 수 있다(노트 추론). 국내 차량은 계속 회사 소유라 설비투자는 늘고 있다. |
| S78 | news | 2026-03-02 | [Pony.ai hits unit profitability in 2nd Chinese city - CnEVPost](https://cnevpost.com/2026/03/02/pony-ai-hits-unit-profitability-in-2nd-chinese-city/) | [6개월 초과, 2차 — 회사 주장 전달] 광저우 Gen-7 로보택시가 2025-11 차량 단위 손익분기(UE breakeven)에 도달했고 선전은 2026-02에 도달했다. 감사받지 않은 회사 자체 수치이며, 6-K의 부문 수치로는 재현할 수 없다. |
| S79 | news | 2026-03-02 | [Pony.ai Achieves Gen-7 Robotaxi Unit Economics Breakeven in Shenzhen, Strengthening Path to Scalable Commercialization (Pony.ai 회사 블로그)](https://blog.pony.ai/pony-ai-achieves-gen-7-robotaxi-unit-economics-breakeven-in-shenzhen-strengthening-path-to-scalable-commercialization/) | [6개월 초과, 회사 주장] 선전 Gen-7(2026-02): 차량당 하루 평균 주문 23건(춘절 기간 유료 주문 하루 26건), 차량당 하루 평균 순매출 RMB338. 비용 기준은 차량·ADK 감가상각, 충전, 정비, 원격 운영, 보험, 인건비, 주차, 네트워크 인프라이고 손익분기는 월 단위로 잰다. Gen-7 BOM은 Gen-6 대비 70% 절감, 부품은 100% 차량용 등급이라고 했지만 절대 원가와 감가상각 내용연수는 공개하지 않았다. 노트 계산으로 RMB338/일은 약 US$47~49/일, 연 약 US$17k이다. 3,500대라도 요금 매출은 연 약 US$60M에 그쳐 Non-GAAP 영업비용(연 약 US$250M)에 크게 못 미친다 — 차량 단위 손익분기와 회사 손익분기 사이의 거리가 멀다(노트 추론). |
| S80 | news | 2026-04-20 | [Pony.ai advances Dubai rollout with driverless robotaxi testing milestone - Gasgoo](https://autonews.gasgoo.com/articles/news/ponyai-advances-dubai-rollout-with-driverless-robotaxi-testing-milestone-2046173614297051136) | [2차] 두바이 완전 무인 테스트는 2025-09 승인됐고, 상용 공공 서비스는 2026년 하반기 계획이며 차량을 '수백 대'로 늘릴 예정이다. 도하도 테스트를 진행 중이다(2026-04-20). 2026-10-18 현재 두바이 상용 출시를 확인한 자료는 없다 — 3·4분기 보고에서 확인할 마일스톤이다. |
| S81 | news | 2026-09-22 | [中信证券 小马智行 研报 요약 (10jqka 同花顺, 2026-09-22)](https://stock.10jqka.com.cn/20260922/c680164646.shtml) | [2차, 단일 증권사 추정 — 시장 컨센서스 아님] CITIC증권(中信证券) 매수 유지, 목표가 HK$132 / US$17. 매출 추정 유지: 2026E US$145M, 2027E US$294M, 2028E US$702M(사실은 basis consensus로 넣었지만 CITIC 한 곳의 추정이다). 자그레브에서 2026-09-10 완전 무인 공공도로 승객 테스트를 시작했다. 2분기 전(2026-05-29) Trendlyne 컨센서스의 FY2026 매출 성장 +60.4%를 FY2025 매출에 적용하면 약 US$144M으로 CITIC 추정과 비슷하다(노트 계산, 낡은 자료). |
| S82 | news | 2026-10-09 | [新浪财经/中国经济网 — 小马智行 港股 상장 후 최저가 보도 (2026-10-09)](https://cj.sina.com.cn/articles/view/1663612603/6328b6bb02002422s) | [2차] 홍콩 주가는 2026-10-09 종가 HK$45.38(장중 HK$44.14, 상장 후 최저)로 공모가 HK$139보다 67.4% 낮고, 코너스톤 투자자는 약 67% 손실이다. 홍콩 공모 총액 HK$6.707B, 순 HK$6.454B. 확정된 코너스톤은 Eastspring, Ghisallo, Athos, Hel Ved, Ocean Arete이며 Uber는 명단에 없다. 공모가보다 크게 낮은 가격이라 앞으로 증자하면 희석이 클 것이다(노트 추론). |
| S83 | news | 2025-10-28 | [Bloomberg: Uber plans to invest in Pony.ai, WeRide HK IPOs - Automotive World](https://www.automotiveworld.com/articles/bloomberg-uber-plans-to-invest-in-pony-ai-weride-hk-ipos/) | [6개월 초과, 보도] 2025-10 Bloomberg 보도: Uber가 Pony 홍콩 IPO에 약 US$100M을 넣을 수 있다(협상 내용은 '바뀔 수 있다'). Uber가 두 회사의 미국 상장에도 투자했다고 적었으나 금액은 없다. 확정 코너스톤 명단에 Uber가 없어서 실제 투자 여부는 확인되지 않는다. |
| S84 | filing | 2026-08-12 | [WeRide Inc. Second Quarter 2026 Financial Results (6-K Ex.99.1)](https://www.sec.gov/Archives/edgar/data/0001867729/000110465926094571/tm2622690d2_ex99-1.htm) | [경쟁사 1차 공시] WeRide 2026년 2분기(2026-08-12 발표): 매출 RMB231.7M(약 US$34.2M, +82.2%), 총이익률 37.5%(Pony 17.5%), 순손실 RMB400.7M(약 US$59.1M), 현금·정기예금 RMB5,374.8M(약 US$792.2M, Pony 유동성 US$1,390.5M보다 적다). 2026-07-31 L4 차량 약 3,400대, 그중 로보택시 1,800대 이상, 중동 약 400대, 13개국 60개 넘는 도시. 2분기 중국 차량당 하루 평균 이동 21건 이상(최고 28건). 아부다비·두바이에서 완전 무인 운영, Uber와 마드리드·취리히에서 시범 운영. 매출 규모는 Pony와 비슷하지만 총이익률이 약 20%p 높아 Pony의 총이익 단계 원가 우위 주장과 맞지 않는다. 다만 WeRide L4 매출에는 로보버스가 섞여 있어 사업 구성 차이를 감안해야 한다(노트 추론). |
| S85 | news | 2026-07-08 | [Waymo goes driverless in Las Vegas and four new cities - Electrek](https://electrek.co/2026/07/08/waymo-driverless-las-vegas-four-new-cities/) | [2차] Waymo: 2026년 초 주당 유료 이동 약 50만 건, 2026년 말 주 100만 건 목표. 차량 약 3,000~3,500대(기사 안에서 수치가 다르다), 누적 이동 2,000만 회 이상, 라스베이거스 포함 미국 11개 도시, 런던에 이어 도쿄 계획. 2026년 US$16B를 기업가치 US$126B에 조달. Tesla: 오스틴 무인 차량 약 20대(제3자 추적), 댈러스·휴스턴·마이애미로 확장, 대규모 증설은 FSD v15(2026년 말~2027년 초 목표)에 달려 있다. Pony를 포함한 중국 사업자별 이동 건수·점유율 비교 자료는 찾지 못했다. |
| S86 | news | 2026-10-02 | [Baidu's Apollo Go hits 1 million driverless robotaxi rides in Q2 2026, plans global expansion to 100 cities - AF.net](https://af.net/realtime/baidus-apollo-go-hits-1-million-driverless-robotaxi-rides-in-q2-2026-plans-global-expansion-to-100-cities/) | [2차, 신뢰도 낮음] AI 뉴스 집계 사이트의 주장: Apollo Go 2026년 2분기 완전 무인 이동 '100만 건', 누적 2,000만 건 이상, 차량 두 배 확대 계획, 2027년까지 100개 도시 목표. 1차 출처를 인용하지 않았고 관련 헤드라인(주 30만 건, 주 15만 건 목표)끼리도 서로 모순된다. Baidu 2분기 실적 원문은 확인하지 못했다. |
| S87 | news | 2026-10-02 | [China Robotaxis Face Losses as Utilization Trails Waymo, BI Says - Bloomberg](https://www.bloomberg.com/news/articles/2026-10-02/china-robotaxis-face-losses-as-utilization-trails-waymo-bi-says) | [보도, 헤드라인만 — 본문 접근 차단] Bloomberg Intelligence(2026-10-02): 중국 로보택시는 가동률이 Waymo에 못 미쳐 손실을 본다. 약세 신호다. 주가 하락기(2026-09-22 US$7.29, F74 → 2026-10-16 US$4.93, F80)와 겹치지만, 하락을 이 보고서나 다른 특정 사건과 연결한 자료는 없다. |
| S88 | news | 2026-08-18 | [BofA cuts Pony AI stock price target on valuation to $17 - Investing.com](https://www.investing.com/news/analyst-ratings/bofa-cuts-pony-ai-stock-price-target-on-valuation-to-17-93CH-4865783) | [2차, 증권사 의견] BofA가 목표가를 US$19에서 US$17로 내렸고('밸류에이션' 이유) 매수 의견은 유지했다(2026-08-18). 2분기 매출 US$36.2M은 컨센서스 US$35.2M을 넘었고, 총이익률 17.5%는 제품 구성 개선으로 BofA 추정을 넘었으며, Non-GAAP 순손실도 컨센서스보다 나았다. 2분기 EPS 컨센서스는 −US$0.14. |
| S89 | news | 2026-10-16 | [Pony AI stock hits 52-week low at 4.93 USD - Investing.com](https://www.investing.com/news/company-news/pony-ai-stock-hits-52week-low-at-493-usd-93CH-4954739) | [2차] 2026-10-16 종가 US$4.93으로 52주 신저가(F80 확인). 1년 −74.34%, 최근 1주 −14.4%, 52주 최고 US$22.46. Jefferies 목표가 US$32.80을 인용하지만 오래된 값으로 보인다. 다른 자료의 52주 최고는 US$24.61(Digrin)·US$24.06(S52, Walnut Invest)로 서로 다르다. |
| S90 | data | 2026-10-13 | [Pony AI (NASDAQ:PONY) Reaches New 12-Month Low - Here's Why - MarketBeat](https://www.marketbeat.com/instant-alerts/price-pony-ai-nasdaq-pony-reaches-new-12-month-low-heres-why-2026-10-13/) | [2차, 컨센서스] 2026-10-13 기준 MarketBeat 컨센서스 'Moderate Buy'(매수 7·보유 2·매도 1), 평균 목표가 US$19.57. 2026-10-13 주가 US$5.61, 50일 이동평균 US$7.16, 200일 US$8.15, 베타 3.89. 증권사 동향: Jefferies 매수 재확인(2026-08-18), BNP Paribas Exane 'Outperform' 상향(2026-08-20), Weiss 'sell (e+)'(2026-09-08). 목표가 대부분은 주가가 US$7~20이던 때 정해졌다. 내부자 매도: VP Ning Zhang 15,524주와 CFO Haojun Wang 13,751주를 2026-09-28 US$7.10에 매도했고, 3개월간 내부자 매도는 41,700주(약 US$296k)다. 내부자 매수 기록은 없다. 매도 규모가 작고 RSU 가득 시기와 겹친다(노트 추론). |
| S91 | filing | 2026-10-09 | [SEC EDGAR submissions — Pony AI Inc. (CIK 0001969302)](https://data.sec.gov/submissions/CIK0001969302.json) | 2026-04부터 2026-10-09까지 SEC 제출 목록에는 6-K·Form 4·Form 144만 있고 F-3·424B·전환사채 6-K는 없다. 즉 2026년에는 후속 공모·선반등록·전환사채가 없다. 2026년 9~10월 6-K는 홍콩거래소 월간 보고, RSU 부여, Sinotrans 연결거래 공지다. 2026-09-28/29/30과 2026-10-02에 Form 144·Form 4(내부자 매도)가 제출됐다. 3분기 실적 발표일 공지는 없다(2025년 3분기 실적은 2025-11-25 발표). |
| S92 | news | 2025-07-28 | [Pony AI Gets Green Light For Driverless Robotaxis In Shanghai's Pudong - Benzinga](https://www.benzinga.com/markets/tech/25/07/46656199/pony-ai-gets-green-light-for-driverless-robotaxis-in-shanghais-pudong) | [6개월 초과, 2차 — 회사 주장 포함] 2025-07 상하이 푸둥(진차오·화무)에서 완전 무인 상용 허가를 받았다. Pony는 자사가 4개 1선 도시 모두에서 완전 무인 상용 로보택시 허가를 가진 '유일한 회사'라고 주장한다. 베이징 허가 세부와 현재 베이징 차량 수는 확인하지 못했다. |
| S93 | news | 2025-10-31 | [Pony.ai 선전 시 전역 무인 상용 택시 허가 보도 - iTiger (2025-10-31)](https://www.itiger.com/news/1161555691) | [6개월 초과, 2차] 선전 최초의 시 전역 완전 무인 상용 택시 허가를 West Lake Group과 공동으로 받았고, 난산·첸하이·바오안에서 시작한다. |

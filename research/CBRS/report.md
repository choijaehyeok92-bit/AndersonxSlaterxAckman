# Cerebras Systems (CBRS) 리서치 보고서 — 기준일 2026-10-18

**팽팽** — 찬성 1 · 반대 1 · 보류 2 · 확신 가중 점수 -0.05 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓
- 조건부 판정: 주가 ≤ 25.65 (-80%) → 찬성 우세 (찬2·반1·보1)

## 1. Variant perception

- 시장 내재: 매출 10년 연 47.2% (FCF 마진 18% 수렴 가정) · 기본 시나리오: 5년 연 54.0%
- 시장이 반영한 것: 주가 $127.21(F61) 기준 EV 232.2억 달러(C:ev)는 10년간 매출 연 45.4%(FCF 마진 20% 수렴, C:implied_cagr@m20)에서 57.9%(마진 10%, C:implied_cagr@m10)의 성장을 가정한다. 매출 컨센서스는 없고 목표가 평균만 $291.64(F179)다. 애널리스트가 RPO 25.4B(F52)를 거의 그대로 매출로 환산한다고 읽는다.
- 우리가 다르게 보는 점: RPO가 인도되더라도 FCF는 2029년까지 음수라고 본다. 데이터센터 capex가 영업현금흐름을 크게 웃돌기 때문이다(F154, F153). 그래서 확률 가중 가치가 주가보다 낮다. 가치의 핵심 변수는 매출 성장이 아니라 OpenAI 한 곳의 인도·SLA 이행, 그리고 워런트·대출 조항이다. 시장은 RPO의 규모만 보고 인식 시기(24개월 내 22%, F113)와 집중도(S45)를 덜 반영한다.
- 왜 우리가 맞는가: FY2025 FCF 마진은 -77%(C:fcf_margin@FY2025)이고 H1 capex는 영업현금흐름의 10배가 넘는다(F154, F153). GAAP 매출총이익률은 14%(F51)로 core 41%(F50)와 큰 차이가 있다. 워런트 자산은 약 $1.13B(F97, F98)가 남아 매출 차감이 이어진다. 앞의 10년 성장 가정을 맞추려면 이 격차가 좁혀져야 하는데, 3Q 가이던스 GM은 38~40%(F57)로 아직 방향이 반대다. [F61] [C:ev] [C:implied_cagr@m20] [C:implied_cagr@m10] [F179] [F52] [F113] [F154] [F153] [F51] [F50] [F97] [F98] [F57] [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [F116] [F117]
- 촉매: Q3 실적 발표와 주 락업 해제가 겹친다(S38). core GM 저점 여부(S36), GAAP과 core의 격차, 고객 집중도 변화(F116, F117)가 확인된다.
- 시점: 2026년 11월 초중순

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **65.66** vs 주가 127.21 · 기대 연 수익률 **-3.6%** · 손실 확률 80%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 35% | 28.00 | 17.38 | -26.1% | RPO는 사실상 전부 OpenAI 계약이다(S45). 이 시나리오에서는 OpenAI가 Cerebras에서 Nvidia로 워크로드를 옮기거나(S40, S46) 인도·SLA를 맞추지 못한다. 그러면 운전자본 대출 회수와 |
| 기본 | 45% | 109.21 | 67.81 | -3.0% | FY2026은 Q3 core 가이던스(F56)와 연간 core 가이던스 상향(F54)에 GAAP 기준 워런트 차감을 반영한 값이다. FY2027은 CFO의 '3배 넘게' 발언(F174)을 core/GAAP 구분도 범 |
| 강세 | 20% | 234.00 | 145.30 | +13.0% | OpenAI 용량이 계획대로 인도되고, AWS Bedrock 분리형 추론이 2027년 중반부터 하이퍼스케일러 매출로 더해진다(S36). AMD 분리형 추론도 2026년 4분기에 양산된다(S34, S18). 이 경우  |

## 3. 반증 조건 (thesis break)

- [대기 — FY2026Q3 미발표] 앤더슨: 3분기 core 매출이 가이던스 하단 미달 — `core_revenue < 2.14e+08` (FY2026Q3)
- [미충족] 앤더슨: 잔여 이행의무가 200억 USD 아래로 감소 — 계약 잔고 훼손 — `remaining_performance_obligations < 2e+10`
- [수동 확인] 앤더슨: OpenAI 등 상위 고객의 계약 축소·해지 또는 핵심 워크로드의 타사 이전 확인 — 수동 확인
- [대기 — FY2026Q3 미발표] 슬레이터: 3분기 core 매출총이익률이 가이던스 하단 미만이면 마진 저점 가설이 깨진다. 보류가 반대로 바뀐다 — `core_gross_margin < 0.38` (FY2026Q3)
- [대기 — FY2026Q3 미발표] 슬레이터: 최대 고객 비중이 다시 40%를 넘으면 분산 가설이 깨진다 — `customer_a_revenue_share > 0.4` (FY2026Q3)
- [수동 확인] 슬레이터: OpenAI 핵심 워크로드가 Cerebras에서 이탈했다는 확인이 나오면 수동 판단으로 반대 전환
- [자료 없음] 애크먼: TTM 잉여현금흐름이 양수로 전환되면 FCF 레드라인 재검토 — `fcf > 0`
- [미충족] 애크먼: GAAP 매출총이익률이 35% 이상으로 수렴하면 core와의 격차 가설 약화 — `gaap_gross_margin >= 0.35`
- [미충족] 애크먼: 주가가 50달러 미만이면 안전마진 재평가 — `price < 50`
- [대기 — FY2026Q3 미발표] 클라만: Q3 core 매출총이익률이 가이던스 하단 미달 — 3분기가 저점이라는 설명 훼손 — `core_gross_margin < 0.38` (FY2026Q3)
- [미충족] 클라만: 고객 B(추정 OpenAI) 매출 비중 45% 초과 — 집중도 심화 — `customer_b_revenue_share > 0.45`
- [수동 확인] 클라만: OpenAI 대출 가속 상환 또는 인도·SLA 미달 공시 — 수동 확인
- [대기 — FY2026Q3 미발표] 레드팀: FY2026Q3 core 매출이 가이던스 하단(F56) 아래 — 상향 가이던스 이력이 깨지고 OpenAI 인도 차질이 시작됨 — `core_revenue < 2.14e+08`
- [대기 — FY2026Q3 미발표] 레드팀: FY2026Q3 core 매출총이익률이 가이던스 하단(F57) 아래 — '3분기 저점' 설명이 틀렸고 개선 경로 불확실 — `core_gross_margin < 0.38`
- [충족 — 훼손] 레드팀: 분기 capex가 Q2 수준(F62)을 넘는데 영업현금흐름은 개선되지 않음 — 투자 회수 전에 현금이 소진되는 경로 — `capex > 4.2e+08`
- [대기 — FY2026Q3 미발표] 레드팀: FY2026Q3 core 클라우드 매출이 Q2(S34)보다 줄어듦 — 성장 엔진 정체와 경쟁 압력 시작 — `core_revenue_cloud < 1.277e+08`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | core_revenue | FY2026Q3 | >= 2.14e+08 | 85% | 가이던스 하단(F56)이다. 첫 가이던스 상회 이력(C:guidance_hit_rate)이 반복되는지, 기본 시나리오의 첫 관문을 본다. |
| K2 | core_gross_margin | FY2026Q3 | >= 0.38 | 75% | 가이던스 하단(F57)이다. 재임차로 눌린 마진이 3분기에 저점이라는 설명(S36)을 시험한다. |
| K3 | revenue | FY2026Q3 | >= 1.7e+08 | 70% | GAAP 매출(2분기 F33)에서 워런트 차감이 core와의 격차를 얼마나 만드는지 본다. 약세 시나리오의 GAAP 단위경제 악화를 가른다. |
| K4 | core_operating_margin | FY2026Q3 | >= -0.25 | 70% | 3분기 core 영업이익률 가이던스 하단(F171)이다. 마진 개선 없이 비용만 늘어나는지 확인한다. |
| K5 | core_revenue | FY2026 | >= 8.8e+08 | 75% | 상향된 연간 가이던스 하단(F54)이다. 4분기 기여가 필요하므로 경영진 가이던스 신뢰도를 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.05 · 비중 참고값 0.0% (팽팽 — 신규 비중 없음) · 슬레이터 시작 비중 1.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 6. 조건부 판정 — 이 가격 이하라면

가치(내재가치·10년 가치·단단한 가치)는 그대로 두고 가격에 걸린 지표만 다시 계산해, 주가가 각 페르소나의 조건 가격까지 내려왔을 때의 표결을 본다. 주가를 예측하는 것이 아니다.

| 주가 | 현재가 대비 | 표 | 판정 | 이 가격이 조건인 페르소나 |
|---|---|---|---|---|
| 127.21 | 현재가 | 찬1·반1·보2 | 팽팽 |  |
| 25.65 | -80% | 찬2·반1·보1 | 찬성 우세 | 클라만 |

클라만의 세 질문 (코드 계산):

- 성장 전망이 틀리면 어디까지? 단단한 가치 주당 38.54 (유형 순자산) — 현재가에서 -69.7% · 내재가치 범위(약세~기본) 17.38~67.81 · 순현금 29.48 · 유형 순자산 38.54 · 성장 없는 현금흐름 가치 29.48
- 현재 가격에 성장이 얼마나 들어 있나? 주가의 77%가 성장 없는 가치(29.48) 위의 몫 · 시장 내재 매출 성장 연 47.2%
- 기다리면 더 싼 가격이 오나? 조건 가격 25.65 · 지난 52주 범위 126.05~386.34 — 그 기간에 조건 가격 이하로 내려간 적이 없다 — 가격은 예측하지 않는다, 기록만 본다

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 1/5 실패 | founder_led=예, upside_10y=6.44x, revenue_5y=14.25x, value_10y=818.8, buy_below=163.8 |
| 슬레이터 | 보류 → 보류 | 3/5 | ✓ | 0/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=1.0%, cash_survives=예, cash_min=63.3억 USD, runway_years=20.2 |
| 애크먼 | 반대 → 반대 | 4/5 | ✗ 단순·예측 가능한 사업이 아님; 잉여현금흐름을 만들지 못함 (코드 계산); 레버리지·자본시장 의존; 안전마진 20% 미만 또는 계산 불가 | 1/5 실패 | simple_predictable=아니오, capital_markets_dependent=예, catalyst=없음, fcf_positive=아니오, leveraged=아니오, intrinsic_value=67.8, mos=-87.6%, buy_below=54.2 |
| 클라만 | 조건부 찬성 → 보류 (조건 가격 25.6 위) | 3/5 | ✗ 보수적 내재가치 대비 안전마진 30% 미만 또는 계산 불가; 성장이 틀리면 단단한 가치까지 50% 넘게 하락 — 영구적 손실 위험 | 2/5 실패 | inefficiency=forced_selling, fcf_positive=아니오, leveraged=아니오, net_cash_ps=29.5, no_growth_ps=29.5, tangible_book_ps=38.5, owner_fcf=-4.4억 USD, hard_value=38.5, hard_basis=tangible_book_ps, low_52w=126.0, high_52w=386.3, intrinsic_value=36.6, iv_low=17.4, iv_high=67.8, mos=-247.2%, downside=69.7%, growth_premium=76.8%, buy_below=25.6, traded_below_52w=아니오 |

- ⚠ 앤더슨: arguments[3] unsupported: 역DCF 47.2%, 가격 127.21, 52주 저점 126.05와 소음 요인은 맞지만 '현재 성장률이 이 수준을 웃돈다'는 근거가 인용에 없다.
- ⚠ 앤더슨: risks[2] unsupported: 출처 없는 숫자 1.13e+09 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 앤더슨: arguments[3]: 인용하지 않은 근거의 숫자 18%(C:customer_d_revenue_share@FY2025Q2·C:fcf_margin@base·F123), 52(S27) — cites에 추가
- ⚠ 앤더슨: rebuttals[0]: 인용하지 않은 근거의 숫자 87.6%(C:mos@ackman) — cites에 추가
- ⚠ 슬레이터: arguments[0]: 인용하지 않은 근거의 숫자 48(S34) — cites에 추가
- ⚠ 애크먼: arguments[3] leap: S50은 벤더 공개표이나 S49에 Artificial Analysis 벤치마크(Cerebras 882 tok/s)가 인용돼 '독립 실측이 없다'는 단정은 과장이다(가격 열세·Groq 확보·SRAM 정체는 맞다).
- ⚠ 애크먼: arguments[2] unsupported: 기대 IRR −3.6%, 손실 확률 80%, 가격 127.21, 역DCF 47.2%는 맞지만 확률 가중 현재가치 65.66과 기본 시나리오 내재가치 67.8은 인용에 없다.
- ⚠ 애크먼: rebuttals[3] unsupported: 없는 근거 인용: C:base_rate@base
- ⚠ 애크먼: rebuttals[0] unsupported: 없는 근거 인용: C:base_rate@base
- ⚠ 애크먼: rebuttals[1] unsupported: 유동성, capex 대 OCF, 기대 IRR 음수, 가격 127.21은 맞지만 '기본 시나리오 내재가치 67.8'은 인용에 없다.
- ⚠ 애크먼: risks[2]: 인용하지 않은 근거의 숫자 18%(C:customer_d_revenue_share@FY2025Q2·C:fcf_margin@base·F123) — cites에 추가
- ⚠ 애크먼: rebuttals[1]: 인용하지 않은 근거의 숫자 67.8(C:intrinsic_value@ackman·C:iv@base·C:iv_high@klarman) — cites에 추가
- ⚠ 클라만: 주가의 77%가 성장에 대한 값 — 성장 없는 가치는 주당 29.48
- ⚠ 클라만: arguments[4] unsupported: 출처 없는 숫자 7000 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 클라만: arguments[2] unsupported: 기대 IRR 음수와 손실 확률 80%는 맞지만 약세 가치가 단단한 가치보다 낮다는 점과 가중 가치가 주가보다 낮다는 점은 인용에 단단한 가치·주가가 없어 확인되지 않는다.
- ⚠ 낡은 컨센서스 — F59: core_revenue FY2026Q3 컨센서스 2.119e+08가 회사 가이던스 하단 2.14e+08(F56)보다 낮다 — 갱신 전 값으로 보고 제외
- ⚠ 낡은 컨센서스 — F60: core_revenue FY2026 컨센서스 8.634e+08가 회사 가이던스 하단 8.8e+08(F54)보다 낮다 — 갱신 전 값으로 보고 제외
- ⚠ 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 레드팀 weakest[0] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base
- ⚠ 회계 품질 findings[1]: 인용하지 않은 근거의 숫자 24(S12·S42·S45) — cites에 추가
- ⚠ 사업·산업 findings[0] 검증 실패(unsupported): 출처 없는 숫자 1.13e+09 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[7] 검증 실패(unsupported): 출처 없는 숫자 2.7e+08, 1.03e+08 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[6]: 인용하지 않은 근거의 숫자 2.099e+08(C:core_revenue@FY2026Q2·F49·S29), 30(C:exit_multiple@base·S34·S38), 48(S34) — cites에 추가
- ⚠ 사업·산업 findings[2] 검증 실패(unsupported): Q2 A 34%·B 32%·C 10%, 상위 3개 76%, 고객 B 매출채권 57%는 맞지만 2026H1 고객 A 49%·B 20%·D 10%(F119–121)는 인용에 없다.
- ⚠ 레드팀 premortem[3] 검증 실패(unsupported): SRAM·I/O·Groq 확보·가격은 자료에 있으나 S18에 AMD 협업이 '비독점'이라는 내용이 없고 하드웨어 매출 감소는 F73의 금액만으로 확인되지 않는다.
- ⚠ 레드팀 premortem[0] 검증 실패(unsupported): RPO 사실상 전부 OpenAI, SemiAnalysis 주장, 대출 가속 조항은 맞지만 고객 B 매출채권 '1.2억 달러대'는 인용(F124는 57% 비중)에 없다.

## 앤더슨 — 찬성 (3/5)

> 이 종목은 5배가 될 수 있는 길이 보이는 몇 안 되는 후보다. 상방 시나리오를 10년으로 늘리면 주당 가치가 현재 주가의 6.44배로 계산되어 5배 기준을 넘는다. 이 계산은 강세 시나리오가 실현된다는 전제다. 강세 확률은 20%이고 기본 시나리오의 연 수익률은 음수여서, 맞으면 크고 틀리면 큰 손실이 나는 전형적인 멱법칙 베팅이다. 창업자 CEO가 99.2%의 의결권을 가진 이중 의결권 구조 아래서 600MW 규모 데이터센터 용량과 25.4B달러 RPO라는 수십 년 단위의 투자가 진행 중이다. 주가는 첫날 고점에서 크게 내려와 52주 저점(126.05달러) 부근이다. 역DCF가 요구하는 성장이 높은 것은 사실이지만 이 회사의 매출은 이미 연 100% 안팎으로 자라고 있다. 약점은 OpenAI 한 곳에 대한 집중, SRAM 확장 정체와 Nvidia·Groq의 추격, 음수 FCF가 길게 이어지는 경로다. 그래서 확신은 높지 않은 3으로 두고 크게 담지 않는다. 매도 논거는 가격이 아니라 성장 가설 훼손(RPO 훼손, 핵심 고객의 이탈)뿐이다.

*이전 판단 대비: 입장(찬성)과 확신(3)은 직전 판단과 같다. 주가가 52주 저점 부근으로 내려와(F61, F183) 10년 상방 계산이 5배 기준을 여전히 통과하고, 새로 나온 Nvidia 이전 보도(S40)는 아직 확인되지 않아 반증 조건으로만 추적한다.*

**논거**
- 10번 질문: 강세 시나리오를 10년으로 늘린 주당 가치는 현재 주가의 6.44배라 5배 기준을 통과한다. 5년 뒤 매출은 기준 연도의 14.25배다. 강세의 확률은 20%이므로 이 숫자는 예측이 아니라 비대칭의 크기를 보여 주는 것이다. [C:upside_10y@anderson] [C:revenue_5y@anderson]
- 1번 질문: 매출이 두 배가 되는 것은 이미 진행 중이다. 2026Q2 core 매출은 전년 대비 103% 늘었고, core 클라우드 매출은 287% 늘었다. 사업의 무게중심이 하드웨어 판매에서 반복 매출형 클라우드로 옮겨 가고 있다. 첫 가이던스는 첫 분기에 상회했고 연간 가이던스도 상향됐다. [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F49] [F76] [F54] [C:guidance_hit_rate]
- 수요 활주로는 길다. 잔여 이행의무는 25.4B달러이고 계약된 데이터센터 용량은 600MW다. 회사는 2027년 매출을 3배 넘게 늘릴 계획이다. 다만 2027년 계획은 core/GAAP 구분과 범위가 없는 회사 발언이고, RPO 인식은 뒤쪽에 쏠려 있다. 이 점은 숨기지 않는다. [F52] [F53] [F174] [F113] [F114]
- 9번 질문: 시장은 왜 과소평가하는가. 역DCF상 현재 가격은 마진 18% 수렴 기준으로 10년간 매출 연 47.2% 성장을 요구한다. 이는 높지만, 현재 성장률이 이 수준을 웃돈다. 시장은 경로의 소음(락업 해제, 내부자 매도, Nvidia 보도)에 주가를 떨어뜨리고 있다. 이것이 성장 가설 자체를 깨는지는 분기마다 코드가 시험한다. 52주 저점이 126.05달러이고 현재가는 127.21달러다. [C:implied_cagr@m18] [F183] [F61] [S39](https://www.benzinga.com/markets/tech/26/10/62330736/cerebras-stock-braces-for-19-4-million-share-unlock) [S40](https://www.ghanamma.com/?p=71787)
- 창업자 경영진의 시간 지평과 통제 구조가 장기 베팅에 맞는다. Class B가 의결권의 99.2%를 가지며 내부자 지분은 38.1%다. 자본은 분기 마진이 아니라 용량 확보(유럽 200MW 계획 포함)에 쓰이고 있다. 반면 소수주주의 통제력이 약하다는 단점이 있다. [F146] [F148] [F53] [S54](https://www.datacenterdynamics.com/en/news/cerebras-to-deploy-200mw-of-compute-in-europe-by-end-of-2027/)

**사전 부검**
- 사전 부검 1: RPO가 사실상 전부 OpenAI 계약이다. 핵심 워크로드가 Nvidia로 옮겨 가거나 인도·SLA를 못 맞추면 운전자본 대출 회수와 가속 상환 조항이 발동한다. 이는 경로의 소음이 아니라 성장 가설 자체를 깨는 시나리오다. 9월 말 SemiAnalysis의 주장은 양사 모두 확인하지 않은 상태다. [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [F137] [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/)
- 사전 부검 2: 기술 해자가 좁아질 수 있다. SRAM 용량 확장이 정체되었고 웨이퍼 밖 I/O가 NVLink5보다 훨씬 낮다. 프런티어 모델이 커질수록 불리하며 Nvidia는 Groq 기술을 확보했다. 속도 우위가 가격 결정력으로 이어진 증거는 없다. [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S51](https://finance.yahoo.com/news/nvidia-buy-ai-chip-startup-210634730.html) [S49](https://the-decoder.com/nvidia-says-its-groq-3-lpx-is-four-times-faster-than-cerebras-but-the-math-is-more-complicated/) [S50](https://benchlm.ai/blog/posts/cerebras-won-speed-not-the-shortlist)
- 사전 부검 3: 현금 창출이 기본 시나리오에서도 2029년까지 음수다. GAAP 매출총이익률은 14%이고 워런트 자산 약 1.13B달러의 상각이 이어진다. 가중 기대 연 수익률은 음수이며 손실 확률이 80%다. 성장이 맞아도 희석과 멀티플 압축이 수익을 깎을 수 있고, 11월 락업 해제와 Q3 실적이 겹친다. [F51] [F97] [F98] [C:expected_irr] [C:p_loss] [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d)

**반론**
- → 애크먼: 가장 강한 논거는 FCF 레드라인과 단순성 탈락이다. FCF가 음수라는 사실은 맞다. 그러나 FCF는 현재를 재는 잣대이고, 이 회사는 용량을 먼저 깔고 매출이 따라오는 구간에 있다. 지금 봐야 할 것은 10년 뒤 크기다. 강세 시나리오를 10년으로 늘린 주당 가치는 현재가의 6.44배이고, 매출은 이미 전년 대비 두 배로 자라고 있다. 안전마진 -87.6%는 기본 시나리오의 5년 값에 대한 것이고 10년 멱법칙 베팅의 크기를 재지 못한다. 반면 사업이 한 문단으로 안 읽힌다는 지적은 인정한다. 그래서 확신을 높이지 않고 작게 담는다. [C:upside_10y@anderson] [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F49] [C:fcf_margin@FY2025]
- → 슬레이터: 가장 강한 논거는 마진 저점과 고객 분산이 아직 실적으로 확인되지 않았다는 점이다. 이 시험은 3분기 실적에서 열리고, 가이던스 하단이 이미 기준으로 나와 있다. 증거를 기다리다 가장 가치 있는 구간을 놓치는 것이 내가 경계하는 실수다. 슬레이터의 반증 조건(core 마진 하단 미달)은 내 반증 조건과 겹치므로, 같은 숫자가 틀리면 나도 입장을 바꾼다. 다만 core 마진이 47%에서 41%로 내려온 방향은 단위경제가 아직 입증되지 않았다는 그의 판단을 뒷받침한다. [F57] [F56] [F110] [F50]
- → 클라만: 가장 강한 논거는 성장이 틀릴 때 단단한 가치까지의 하락 폭이 한도를 넘는다는 점이다. 하방을 묻는 것은 정당하고 코드 계산 하락 폭도 크다. 그러나 성장 없는 가치로 아웃라이어를 재면 모든 아웃라이어가 비싸 보인다. 성장 프리미엄이 주가의 대부분이라는 것은 이 베팅이 무엇인지를 설명할 뿐 틀렸다는 증거가 아니다. 그의 조건 가격은 현재가보다 한참 낮고 내 조건 가격은 현재가 위에 있다. 놓친 상방도 손실이라는 점이 우리 차이의 핵심이다. 대출 가속 조항이 단단한 가치를 깎을 수 있다는 지적은 인정하며, 그래서 이를 반증 조건으로 추적한다. [C:downside@klarman] [C:growth_premium@klarman] [C:upside_10y@anderson] [F137]
- → 레드팀: 첫 사전 부검(OpenAI 이탈과 대출 가속 상환)이 가장 강하다. 이것은 경로의 소음이 아니라 성장 가설 자체를 깬다. 다만 Nvidia 이전 주장은 양사 모두 확인하지 않은 상태이고 신호는 3분기 core 매출이 가이던스 하단을 밑도는 것으로 분기마다 검증된다. 나머지 둘(마진, 데이터센터 회수 지연)은 가설을 깨기보다 경로를 거칠게 만든다. 락업 해제와 내부자 매도는 수급이지 사업 가치가 아니다. 약한 가정으로 지목된 2027년 3배 성장은 core/GAAP 구분이 없는 회사 발언이라는 점을 인정한다. [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/) [F137] [F56] [F174]

**인정한 점**
- 애크먼: FCF가 기본 시나리오에서 2029년까지 음수이고 단순성 기준을 통과하지 못한다는 점을 인정한다. 그래서 확신은 3에 묶고 비중을 키울 근거로 쓰지 않는다.
- 슬레이터: 마진과 고객 집중이 아직 위험 구간이라는 점을 인정한다. 3분기 실적이 가이던스 하단을 밑돌면 입장을 바꾼다.
- 클라만: 성장이 틀리면 하락 폭이 크다는 점을 인정한다. 손실 확률이 높고 기대 수익률이 음수인 베팅이라는 사실을 숨기지 않는다.
- 레드팀: 매출이 사실상 한 고객에 걸려 있다는 점은 가설을 직접 깨는 위험이다. 이탈 확인이 나오면 매도 논거가 된다.


## 슬레이터 — 보류 (3/5)

> 기회의 크기는 크다. 계약 용량은 600MW이고, 저지연 추론은 아직 시장이 정의되는 중이다. 그러나 이 성장이 지속되는지는 지금 증거로 입증되지 않았다. 단위경제가 core 기준으로만 흑자다. core 매출총이익률은 1분기 47%에서 2분기 41%로 내려왔고 3분기 가이던스는 38~40%다. GAAP 매출총이익률은 14%다. 매출은 소수 고객에게 쏠려 있고, 계약 잔액 대부분은 OpenAI 한 곳이다. 생존 문제는 없다. 유동성이 충분해 현금이 바닥날 경로가 아니므로 원칙상 반대할 이유는 없다. 하지만 '무엇이 참이어야 하는가'의 핵심 항목(마진 저점 통과, 고객 분산, OpenAI 워크로드 유지)이 아직 모두 위험 구간에 있다. 증거가 쌓이기 전에는 키울 근거가 없어 보류하고, 3분기 실적으로 가설을 시험한다. 시작 비중을 정한다면 1% 이하다. 주가가 크게 내렸다는 사실은 가설이 틀렸다는 증거도, 맞다는 증거도 아니다.

*이전 판단 대비: 직전 반대에서 보류로 낮춘다. 슬레이터의 레드라인(유동성 F152, 생존 경로, must_be_true)은 모두 통과하고, 반대는 가격이나 원칙이 아니라 증거 부족 때문이다. 증거 부족은 보류가 맞다. 새 사실은 주가가 F61 기준 127.21로 내려온 것이지만, 이것이 가설을 바꾸지는 않는다. 반대 근거였던 마진과 고객 집중은 3분기 실적(F57)으로 시험된다.*

**논거**
- 크기와 활주로는 인정한다. 다만 계약 잔액의 인식 시기가 뒤로 쏠려 있다. 24개월 안에 인식될 몫은 22%, 25~48개월 구간은 43%다. 성장의 대부분이 아직 계획이고 실적이 아니다. 2027년 매출 3배 이상이라는 CFO 발언도 범위와 core/GAAP 구분이 없다. [F52] [F113] [F114] [F174]
- 단위경제는 개선이 아니라 악화 방향의 미입증 상태다. core 매출총이익률이 47%에서 41%로 내려왔고, 3분기 가이던스는 38~40%다. GAAP은 14%다. 차이는 고객 워런트 상각인데, 사실상 가격 할인이라 반복될 수 있다. 경영진이 말하는 '3분기가 저점'은 아직 검증 전이다. 그래서 `deteriorating`으로 단정하지 않고 `unclear`로 둔다. [F110] [F50] [F57] [F51] [F93] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/)
- 고객 집중은 완화 중이지만 여전히 크다. 2분기 고객 A 34%, 고객 B 32%, 고객 C 10%다. 상위 세 곳이 매출 대부분을 차지한다. 다변화 신호(6건의 계약, AWS 경로)는 있으나 AWS의 첫 매출은 2027년 중반 이후이고 규모가 계약 잔액에 없다. 지금 증거로는 키울 근거가 못 된다. [F116] [F117] [F118] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [S16](https://news.google.com/rss/articles/CBMirgFBVV95cUxOMDgtbmhLenNVQVdOQXJDbmJmck52THdJR3BYWV8zeXdjRFdieFdIdUNlTTNreWNWSy1obHdabzhtakNsQldBeGF6Y0RwLTQ0ZVRzZy11UkFycEx6azI0dWM1enN5NkdHTEg3N1VhajVFZEFqMmlKblo3Y2Zmam1wUTNLS3ZNYTd2b2MxdWNVQzJtdklpVV92WS1wZllQVGVBak9mUEdkeldoWFZRWFE?oc=5)
- 생존은 문제가 되지 않는다. 총 유동성이 86.0억 달러이고, 상반기 설비투자 5.5억 달러가 영업현금흐름 -4,750만 달러를 크게 웃돌지만 코드 계산상 기본 시나리오에서 현금은 0 아래로 내려가지 않는다. 노스볼트식 외부 조달 의존 위험은 지금 낮다. 그래서 레드라인으로 반대하지 않는다. 다만 이 현금은 데이터센터에 투입되고, 투하자본 수익률은 확인된 바 없다. [F152] [F154] [F153] [C:runway_years]
- 경영진 신뢰도의 긍정 증거는 있으나 표본이 한 번이다. 첫 가이던스를 core 매출과 core 매출총이익률 모두 상회했고 연간 가이던스도 상향했다. 하지만 GAAP 매출은 컨센서스를 밑돌았고, 가이던스와 적중이 core에서만 성립한다. 한 분기로 지속성을 입증했다고 볼 수 없다. [C:guidance_hit_rate] [F172] [F49] [F58] [F33]

**사전 부검**
- 사전 부검: OpenAI 핵심 워크로드가 Cerebras에서 Nvidia로 옮겨가고 있었다면, 계약 잔액의 사실상 전부가 한 고객에 걸려 있으므로 성장 경로와 인도 약정이 함께 무너진다. 9월 말 SemiAnalysis 주장은 양사 모두 확인하지 않았지만, 틀렸다고 단정할 근거도 없다. [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- 사전 부검: OpenAI 운전자본 대출은 인도·SLA 미달 시 회수와 가속 상환 조항이 있다. 인도 지연이 매출 둔화에서 끝나지 않고 9.2억 달러 상환 요구로 이어지면, 생존 판정의 전제(자체 현금 창출 없이도 버틴다)가 흔들린다. [F137] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- 사전 부검: 마진 저점이 3분기가 아니라면 재임차 설명이 틀린 것이다. 이 경우 워런트 상각이 계속 쌓이는 구조(자산이 남아 있다)와 맞물려 GAAP 단위경제가 구조적으로 낮다는 뜻이다. [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [F97] [F98] [F57]

**반론**
- → 앤더슨: 6.44배는 강세 시나리오를 10년으로 늘린 값이다. 그 시나리오가 성립하려면 OpenAI 인도가 계획대로 가고 AWS 매출이 2027년 중반부터 더해지고 마진이 장기 목표로 올라가야 한다. 이 셋은 지금 모두 계획이지 실적이 아니다. 확률 가중 기대 수익률은 음수이고 손실 확률이 높다. 멱법칙 베팅은 하방이 작을 때 성립한다. 이 종목은 핵심 고객 한 곳이 흔들리면 성장 가설과 대출 상환이 함께 무너진다. 그래서 상방 크기는 인정하되, 증거가 쌓이기 전에는 키울 근거가 없다고 본다. [C:upside_10y@anderson] [C:expected_irr] [C:p_loss] [F113] [F137] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/)
- → 애크먼: 자본시장 의존을 true로 둔 데 동의하지 않는다. 총 유동성이 충분하고 코드 계산상 기본 시나리오에서 현금이 0 아래로 내려가지 않으며 소진 연수도 길다. 지금은 외부 조달에 기대는 구조가 아니다. 다만 FCF가 음수라는 점, 예측 가능성이 낮다는 점은 인정한다. 나는 예측 불가능하다는 이유만으로 정의되지 않은 시장을 버리지 않는다. 그 대신 작은 비중과 증거 조건으로 시험하자는 쪽이다. 반대와 보류의 차이는 거기서 갈린다. [F152] [C:runway_years] [C:fcf_margin@FY2025] [F154] [F153]
- → 클라만: 하방이 넓으면 사지 않는다는 점은 맞다. 다만 단단한 가치로 쓴 유형 순자산이 정말 단단한지 네 사전 부검이 이미 의심했다. 고객 워런트 자산과 데이터센터 투자가 섞여 있고 대출 가속 상환이 발동하면 현금이 줄어든다. 그렇다면 조건 가격에서도 안전마진이 얇을 수 있다. 가격만 기다리는 것보다 마진 저점과 고객 분산이 실적으로 확인되는지를 기다리는 편이 가설에 더 직접 맞는다. 락업 물량이 가격을 눌렀다는 점은 사업 가치와 무관하니 가설이 틀렸다는 증거로 쓰지 않는다. [C:hard_value@klarman] [F97] [F98] [F137] [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) [S39](https://www.benzinga.com/markets/tech/26/10/62330736/cerebras-stock-braces-for-19-4-million-share-unlock)
- → 레드팀: 가장 강한 부검은 OpenAI 의존 붕괴다. 계약 잔액이 사실상 한 고객에 걸려 있고 대출에는 가속 조항이 있다. 이 선행 신호를 기계 판정 가능한 조건으로 넣을 가치가 있다고 판단한다. 3분기 core 클라우드 매출이 2분기보다 줄면 성장 엔진 정체이므로 must_be_true에 추가한다. 이탈 보도는 양사가 확인하지 않았지만 틀렸다고 단정할 근거도 없다. 그래서 반대로 돌리지 않고 이 조건이 깨지면 반대로 전환한다. [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/) [F137] [F76] [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)

**참이어야 하는 것**
- [at_risk] 3분기 core 매출총이익률이 가이던스 하단 이상으로 저점을 확인한다
- [at_risk] 3분기 GAAP 매출총이익률이 상반기 수준으로 회복된다
- [at_risk] 최대 고객 비중이 30% 아래로 내려가 분산이 실적으로 확인된다
- [at_risk] 3분기 core 클라우드 매출이 2분기 수준 아래로 줄지 않는다
- [on_track] FY2026 core 매출이 상향된 가이던스 하단을 달성한다

**인정한 점**
- 애크먼: 사업이 단순하지 않고 FCF가 음수라는 점은 맞다. GAAP 매출총이익률과 core의 격차가 아직 좁혀지지 않았으므로 보류를 찬성으로 올릴 근거가 없다.
- 클라만: 주가의 대부분이 성장 서사에 대한 값이고, 기본 시나리오의 현재가치도 현재가 아래라는 점을 인정한다. 지금 가격에서 시작 비중을 정당화하기 어렵다.
- 레드팀: 클라우드 매출 정체 신호가 must_be_true에서 빠져 있었다. 이를 추가하되 입장은 보류로 유지한다. 3분기 실적이 마진 저점 가설과 고객 분산을 시험한다.


## 애크먼 — 반대 (4/5)

> Cerebras는 한 문단으로 설명되지 않는다. 칩 회사에서 데이터센터 운영 회사로 바뀌는 중이고, 매출은 사실상 OpenAI 한 곳의 인도 이행에 달려 있다. FCF는 2029년까지 음수이고(모델 기본 시나리오), 지금도 마이너스다. 가치 대비 안전마진이 없다. 기본 시나리오 내재가치는 주당 67.8로 현재가 127.21보다 낮고, 코드 계산 안전마진은 -87.6%다. 가격이 문제이기 전에 사업이 예측 가능성과 FCF 양수라는 조건을 통과하지 못한다. 54.2 이하로 내려와도 FCF 레드라인은 그대로여서 '가격만 맞으면 산다'가 성립하지 않는다.

*이전 판단 대비: 입장 변화 없음. 직전 판단과 같은 against이며, 새 근거(F61 주가 127.21, F183 52주 저점 126.05)는 가격이 더 내려왔음을 보여 주나 안전마진은 여전히 -87.6%이고 FCF 레드라인은 그대로다.*

**논거**
- 단순성 탈락: 하드웨어 판매에서 클라우드 운영으로 사업이 바뀌고 있고, 매출에서 차감되는 고객 워런트와 대출 가속 조항이 얽혀 있다. 10년 뒤 FCF를 합리적 범위로 추정할 수 없다. 기본 시나리오조차 FCF 마진이 2029년까지 음수다. [F53] [F137] [F97] [F98] [C:fcf_margin@FY2025]
- FCF 레드라인: FY2025 FCF 마진은 -77%이고 2026년 상반기도 영업현금흐름 대비 capex가 10배 넘게 크다. 현금 창출 사업이 아니라 현금 소모 사업이다. [C:fcf_margin@FY2025] [F153] [F154]
- 가격: 확률 가중 현재가치는 65.66, 기대 연 수익률 -3.6%, 손실 확률 80%다. 현재가 127.21은 기본 시나리오 내재가치 67.8의 약 2배다. 역DCF는 10년 매출 연 47.2% 성장을 요구한다. [C:expected_irr] [C:p_loss] [C:implied_cagr@m18] [F61]
- 해자 증거 부족: 속도 우위는 벤더 공개 수치뿐이고 독립 실측이 없다. Nvidia의 Groq 기술 확보와 SRAM 확장 정체로 경쟁이 악화되고 있다. 가격은 Groq보다 비싸 가격결정력의 흔적도 없다. [S50](https://benchlm.ai/blog/posts/cerebras-won-speed-not-the-shortlist) [S51](https://finance.yahoo.com/news/nvidia-buy-ai-chip-startup-210634730.html) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S49](https://the-decoder.com/nvidia-says-its-groq-3-lpx-is-four-times-faster-than-cerebras-but-the-math-is-more-complicated/)
- 경영진 정렬 의문: CEO와 CTO가 락업 해제 구간에 $240M 넘게 팔았고, 회사는 SBC와 워런트 상각을 뺀 core 지표를 앞세운다. GAAP 매출총이익률은 14%다. 의결권은 Class B가 99.2%를 쥔다. 행동주의로 바꿀 수 있는 구조도 아니다. [S40](https://www.ghanamma.com/?p=71787) [F51] [F50] [F146]

**사전 부검**
- 사전 부검: 내가 틀렸다면 OpenAI 인도가 순조롭고 AWS Bedrock이 2027년 중반부터 매출을 더해 RPO가 빠르게 전환되는 경우다. 강세 시나리오 연 수익률은 +13.0%로 나온다. 그래도 확률 20%라 기대값을 뒤집지 못한다. [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [S18](https://news.google.com/rss/articles/CBMiywFBVV95cUxQSGxfRjlGZUZfR1hack0zbEdZcVJXY1JCaWw4dl9fMFZnQnJHVnVfU3NsZkpVd2hPbjh5Q0dHTVcxYTByelU2b3lMUzVDNk54ZFN4OG1VSko2MXEzV0d3bDdHSTJiRHlrMFZtallYSllLUzdSQ2lVdDVra2ZqY0xPaEV2cmxRaXRIWnhRd19obk82eFBGQXQ1YnpYc2hLY0poOGVsdS1yZ19mVGs0RlFVZ1diV0luRktiNV9Uc05vSHpEbmViQ1NjX1h1UQ?oc=5) [F52] [C:irr@bull]
- 사전 부검: 락업 해제 물량 때문에 주가가 이미 과하게 눌렸을 수 있다. 사상 최저 부근이다. 다만 해제가 끝나도 FCF와 단순성 문제는 남는다. 가격 하락은 안전마진을 만들 뿐 사업의 질을 바꾸지 않는다. [S39](https://www.benzinga.com/markets/tech/26/10/62330736/cerebras-stock-braces-for-19-4-million-share-unlock) [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) [F183]
- 사전 부검: core 마진이 40%대에서 60% 초과로 올라가고 GAAP과의 격차가 좁혀지면 FCF 18% 이상도 가능하다. 그러나 3분기 가이던스 GM은 38~40%로 방향이 아직 반대다. [F57] [F50] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/)

**반론**
- → 앤더슨: 10년 6.44배는 강세 시나리오(확률 20%)를 10년으로 늘린 값이다. 기본 시나리오 연 수익률은 -3.0%이고 확률 가중 기대 연 수익률은 -3.6%, 손실 확률은 80%다. 역DCF는 연 47.2% 성장을 10년간 요구한다. 현재 성장률이 높다는 이유로 이를 지속 가능하다고 보는 것은 생존자 편향이다. 기저율 표도 없어 이 성장이 드문지 검증조차 되지 않았다. 앤더슨 자신의 사전 부검이 RPO 전부가 OpenAI라는 점을 성장 가설 자체를 깨는 시나리오로 인정했다. [C:upside_10y@anderson] [C:expected_irr] [C:p_loss] [C:implied_cagr@m18] [C:base_rate@base] [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- → 슬레이터: 생존 경로와 단위경제는 필요조건이지 가격의 정당화가 아니다. 슬레이터가 생존을 통과시킨 근거인 유동성 86.0억 달러는 데이터센터 capex로 소진되는 현금이고, 상반기 capex는 영업현금흐름의 10배가 넘는다. 단위경제를 unclear로 둔 상태에서 보류로 낮추는 것은 이해하지만, 기본 시나리오 내재가치 67.8 대비 주가 127.21이면 3분기가 가설을 확인해 주어도 가격이 맞지 않는다. 증거가 쌓이는 것과 사도 되는 것은 별개다. [F152] [F154] [F153] [C:expected_irr] [F61]
- → 클라만: 하방 규율은 같고 조건부로 둔 이유(락업 강제 매도)도 이해한다. 그러나 조건 가격이 내 레드라인으로는 닿지 않는다. 내 buy_below 54.2는 가격 조건만 본 값이고 FCF 양수와 단순성은 가격이 내려와도 그대로다. 클라만의 단단한 가치는 유형 순자산인데 워런트 자산과 데이터센터 투자가 섞여 있고 OpenAI 대출 가속 상환이 발동하면 깎인다. 락업은 수급 문제일 뿐 사업의 질을 바꾸지 않는다. [F97] [F98] [F137] [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) [F61]
- → 레드팀: 사전 부검이 FCF 범위를 넓힌다. 4개 시나리오 모두 이미 현금이 마이너스인 상태에서 시작하므로, 가정이 맞아도 2029년까지 FCF가 음수이고 마진·멀티플 요인이 수익률을 깎는다. 가장 약한 가정인 2027년 3배 성장과 마진 18%에 더해 기저율 검증이 없어 필요한 안전마진은 20%보다 훨씬 커야 한다. 현재 -87.6%는 그 근처에도 못 간다. [F174] [C:base_rate@base] [C:expected_irr] [F153] [F154]

**인정한 점**
- 앤더슨: 매출이 이미 연 100% 안팎으로 자라고 있고 첫 가이던스를 상회했다는 점은 인정한다. 다만 이는 단순성·FCF 레드라인을 바꾸지 못하므로 입장은 그대로다.
- 슬레이터: 증거 부족이면 반대보다 보류가 정직하다는 논리를 인정한다. 나는 가격과 FCF 레드라인 때문에 반대를 유지한다.
- 클라만: 락업과 내부자 매도가 가격 비효율을 만들 수 있다는 점은 인정한다. 그래도 조건 가격에서도 FCF 레드라인은 남는다.


## 클라만 — 보류 (3/5)

> 하방부터 본다. 성장 전망이 틀리면 코드가 계산한 단단한 가치(유형 순자산 기준)까지 하락 폭이 70% 안팎이고, 보수적 내재가치 대비 안전마진은 음수다. 주가의 대부분(성장 프리미엄)이 성장 서사에 대한 값이므로 지금 가격에서는 원칙 두 개(안전마진, 하방 한도)를 어긴다. 반면 이 회사는 어떤 가격에도 사지 않을 회사는 아니다. 유동성이 충분해 레버리지 위험이 없고, 순현금과 유형 순자산이 두껍다. 주 락업 해제가 Q3 실적 발표와 겹치는 강제 매도성 수급이 있어 비효율이 생길 수 있다. 그래서 반대가 아니라 조건부로 본다. 조건 가격은 코드의 buy_below다. 현재가보다 한참 낮고 지난 52주에 그 가격이 있었던 적도 없다. 기다리면 더 싼 가격이 올 가능성은 락업 물량과 실적 충격이라는 구체적 사건으로 설명되지만, 그 가격까지 온다고 예측하지는 않는다. 현금에서 기다린다.

**논거**
- 성장 전망이 틀릴 때의 하방이 한도를 넘는다. 단단한 가치는 유형 순자산이고, 그 기준 하락 폭이 현재가 대비 크다. 순현금만으로는 주가를 받치지 못한다. [C:downside@klarman] [C:hard_value@klarman] [C:net_cash_ps@klarman]
- 주가의 대부분이 성장에 대한 값이다. 성장 없는 가치 위의 몫이 매우 크고, 역DCF는 마진이 개선되더라도 10년간 높은 매출 성장이 지속돼야 현재 EV가 정당화된다고 말한다. 그런데 FCF는 모델 기간 내내 음수로 시작하고 SBC를 뺀 FCF도 음수다. [C:growth_premium@klarman] [C:implied_cagr@m20] [C:owner_fcf@klarman] [C:fcf_after_sbc@FY2025]
- 확률 가중 가치가 주가보다 낮고 손실 확률이 높다. 약세 시나리오의 현재가치는 단단한 가치보다도 낮아, 시나리오 범위 전체에서 안전마진이 없다. [C:expected_irr] [C:p_loss] [C:iv_low@klarman] [C:iv_high@klarman]
- 영구적 손실 위험의 핵심은 단일 고객 의존이다. RPO는 사실상 전부 OpenAI 계약이고, 운전자본 대출에는 인도·SLA 미달 시 회수·가속 상환 조항이 있다. 단단한 가치는 이 대출을 갚고도 남는지에 달려 있으므로, 인도 실패는 성장 프리미엄만 지우는 데서 그치지 않고 유형 순자산도 깎을 수 있다. [F52] [F137] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- 가격을 비효율적으로 만드는 사건이 있다. 약 1억 7천만 주 규모의 주 락업 해제가 Q3 실적 발표와 겹치고, 분할 해제와 내부자 매도가 이어지고 있다. 사업 가치와 무관한 강제 매도성 수급이므로 기다릴 이유가 되지만, 가격이 어디까지 갈지는 예측하지 않는다. [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) [S39](https://www.benzinga.com/markets/tech/26/10/62330736/cerebras-stock-braces-for-19-4-million-share-unlock) [S40](https://www.ghanamma.com/?p=71787) [S42](https://techjacksolutions.com/?p=92070)

**사전 부검**
- 사전 부검 1: 기다리다 놓친다. 가이던스를 두 지표 모두 웃돈 이력과 큰 RPO가 실제 매출로 전환되면 주가가 조건 가격에 닿지 않고 올라갈 수 있다. 놓친 기회는 회복할 수 있는 손실이므로 감수한다. [C:guidance_hit_rate] [F52] [F113]
- 사전 부검 2: 단단한 가치가 생각보다 단단하지 않다. 유형 순자산에는 고객 워런트 자산과 데이터센터 투자가 섞여 있고, 대출 가속 상환이 발동하면 현금이 줄어든다. 이때 조건 가격에서 사도 안전마진이 얇을 수 있다. [F97] [F98] [F137] [F154]
- 사전 부검 3: 회계가 core 지표 뒤에 숨는다. GAAP과 core의 괴리가 크고 워런트 상각은 반복될 수 있는 가격 할인이다. core 마진을 근거로 내재가치를 높게 잡으면 안전마진을 과대평가한다. [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F50] [F51] [F93]

**반론**
- → 앤더슨: 강세 시나리오를 10년으로 늘리면 주가의 6.44배가 된다는 계산은 상방이 열려 있다는 증명일 뿐, 하방이 닫혀 있다는 증명이 아니다. 같은 코드가 성장이 틀릴 때 단단한 가치까지의 하락을 69.7%로 계산한다. 시나리오 전체의 손실 확률도 높다. 멱법칙 베팅은 하방이 한도 안에 있을 때 성립하는데, 지금 가격에서는 한도를 넘는다. 그래서 나는 가격이 내려온 뒤에 사겠다는 것이다. 앤더슨의 반증 조건인 핵심 고객 이탈은 내가 가장 두려워하는 영구적 손실의 경로와 같다. [C:upside_10y@anderson] [C:downside@klarman] [C:p_loss] [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- → 슬레이터: 슬레이터의 생존 경로는 하방의 바닥이 아니다. 현금이 바닥나지 않는다는 말은 주주가 돈을 되찾는다는 말과 다르다. OpenAI 운전자본 대출에는 인도·SLA 미달 시 회수·가속 상환 조항이 있다. 보류한 채 3분기 실적으로 시험하자는 방식은 존중하지만, 실적이 좋게 나오면 가격이 먼저 오를 수 있다. 시험의 결과로 가격이 달라지기 전에, 어느 가격이면 틀려도 감당할 수 있는지부터 정해 두는 쪽이 낫다. [F137] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [F152] [C:hard_value@klarman]
- → 애크먼: 애크먼은 FCF 음수와 단순성 탈락 때문에 어떤 가격에서도 사지 않겠다고 한다. 사업 질의 문제 제기는 인정한다. 다만 레버리지가 없고 유동성이 두꺼운 회사가 락업 해제와 내부자 매도 같은 사업 가치와 무관한 수급으로 눌릴 때 가격이 비효율적이 될 수 있다. 이런 곳은 가격에 단서를 붙여 기다리는 편이 맞다. 같은 안전마진이라도 애크먼의 내재가치는 성장 시나리오에 기대고 있어 성장이 어긋나면 함께 무너진다. 그래서 나는 단단한 가치에서 하방 한도를 따로 건다. 두 사람의 조건 가격은 가깝다. [C:buy_below@ackman] [C:buy_below@klarman] [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) [S39](https://www.benzinga.com/markets/tech/26/10/62330736/cerebras-stock-braces-for-19-4-million-share-unlock) [C:growth_premium@klarman]
- → 레드팀: 레드팀의 첫 사전 부검(OpenAI 이탈)이 가장 강하다. 이것이 성장 프리미엄만 지우는지 단단한 가치까지 깎는지를 가르겠다. 대출은 이미 부채로 잡혀 있어 가속 상환은 현금과 부채를 함께 줄인다. 추정: 순현금에 미치는 영향은 제한적이지만, 매출 공백과 고객 B 매출채권 회수 문제가 겹치면 유형 순자산도 훼손될 수 있다. 그래서 단단한 가치는 보수적으로 봐야 하고, 조건 가격이 현재가보다 훨씬 아래에 있는 것이 맞다. [F137] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [F124] [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [C:hard_value@klarman] [C:buy_below@klarman]

**인정한 점**
- 슬레이터의 지적대로 3분기 core 매출총이익률과 고객 분산이 시험대이고, 나의 반증 조건과 겹친다. 다만 입장은 바꾸지 않는다.
- 레드팀과 애크먼의 지적 중 고객 워런트 자산과 데이터센터 투자가 유형 순자산에 섞여 있다는 점은 인정한다. 단단한 가치가 생각보다 덜 단단할 수 있으므로 확신은 3 이상으로 올리지 않는다.
- 앤더슨의 말대로 기다리다 놓칠 수 있다. 이는 회복 가능한 손실이므로 감수한다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Cerebras는 웨이퍼 스케일 칩(WSE)과 이를 담은 시스템을 만들어 (1) 고객에게 하드웨어로 팔고 (2) 자체 데이터센터에서 초고속 추론을 클라우드 서비스로 판매한다. 매출 무게중심이 하드웨어에서 클라우드로 빠르게 이동 중이다. 2026Q2 core 매출 $209.9M 중 클라우드 $127.7M(+287%), 하드웨어 $82.1M(+17%)이다(S34, F76, F75). 고객은 극단적으로 집중돼 있다. FY2025 MBZUAI 62%, G42 24%(F127, F128)였고, 2026Q2에는 고객 A 34%, 고객 B 32%, 고객 C 10%다(F116, F117, F118). 고객 B는 OpenAI로 추정된다(노트 추론). 2026Q2에는 GAAP 매출총이익률이 14%(core 41%)까지 내려갔다(F51, F50). 고객 워런트 상각 $44.3M과 클라우드 고객에게서 시스템을 재임차하는 비용이 원인이다(F93, S36). 단위경제는 core 기준으로는 흑자 구간이지만 GAAP 기준으로는 아직 입증되지 않았다. RPO $25.4B는 사실상 전부 OpenAI 계약이며(F52, S45), 이 가운데 24개월 안에 인식될 몫은 22%뿐이다(F113). 사업의 핵심 위험은 기술 해자의 지속성(SRAM 확장 정체, Nvidia·Groq 경쟁)과 데이터센터 운영 능력이다.

- [unit_economics] 2026Q2 core 매출총이익률은 41%(하드웨어 38.8%, 클라우드 41.8%)지만 GAAP 매출총이익률은 14%다(F50, F80, F81, F51). 차이는 고객 워런트 상각 $44.3M(하드웨어 매출에서 $28.0M 차감)와 매출원가 내 SBC $15.4M, 패스스루 항목이다(F93, F94, S34). 워런트는 가격 할인에 해당하므로 core만으로 보면 단위경제를 과대평가할 수 있다. 워런트 자산이 약 $1.13B 남아 있어 상각 부담이 이어진다(F97, F98). 방향은 core 매출총이익률 47%(1Q)에서 41%(2Q)로 하락했고 3Q 가이던스는 38~40%다(F110, F50, F57). [F50] [F51] [F93] [F97] [F98] [F110] [F57]
- [unit_economics] 경영진은 2Q 매출총이익률 압박 약 500bp를 수요 대응용 시스템 재임차 때문이라고 설명하고, 3Q를 저점으로 4Q부터 개선되며 장기적으로 60% 초과를 말한다. 2027년 마진 수치는 제시하지 않았다(S36). 2차 요약이며 아직 확인된 개선은 없다. 2026 core 매출총이익률 가이던스는 41~43%로 상향됐다(F167). [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [F167]
- [customers] 매출 집중이 FY2025 상위 2개 고객 86%(F48)에서 완화되고는 있으나 여전히 높다. 2026H1 고객 A 49%, 고객 B 20%, 고객 D 10%이고(F119, F120, F121), 2026Q2 고객 A 34%, B 32%, C 10%다(F116, F117, F118). 상위 3개 고객이 Q2 매출의 76%를 차지한다(추정: 34+32+10). 고객 A·D는 UAE 관련(MBZUAI·G42)으로 추정되며 수출통제와 특수관계 위험이 있다(S44). 2026Q2 고객 B 매출채권 비중은 57%다(F124). [F116] [F117] [F118] [F124] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
- [customers] 고객 다변화 신호는 있으나 규모는 작다. 2Q에 OpenAI·하이퍼스케일러 외 $30M 초과 계약 6건이 있었고 고객으로 Figma, Cognition, Lovable, Block, AlphaSense, GSK, CrowdStrike가 거론됐다(S36). AWS Bedrock 분리형 추론은 2027Q1 GA, 첫 하이퍼스케일러 매출은 2027년 중반으로 예상된다. RPO에는 AWS 백로그가 포함돼 있지 않다(S36). 9월 Gimlet Labs 공급 계약도 발표됐다(S16). [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [S16](https://news.google.com/rss/articles/CBMirgFBVV95cUxOMDgtbmhLenNVQVdOQXJDbmJmck52THdJR3BYWV8zeXdjRFdieFdIdUNlTTNreWNWSy1obHdabzhtakNsQldBeGF6Y0RwLTQ0ZVRzZy11UkFycEx6azI0dWM1enN5NkdHTEg3N1VhajVFZEFqMmlKblo3Y2Zmam1wUTNLS3ZNYTd2b2MxdWNVQzJtdklpVV92WS1wZllQVGVBak9mUEdkeldoWFZRWFE?oc=5)
- [industry] 경쟁 구도는 악화 방향이다. Nvidia는 Groq 기술을 확보했고 Groq 3 LPX를 Nebius 등에서 가동할 예정이다(S51, S49). AMD와는 분리형 추론을 협업한다(S18). 독립 분석은 DeepSeek V4 서빙에 CS-3 약 24대가 GB300 NVL72 5랙에 해당한다고 추정하며, 1T~5T 프런티어 모델은 1,000 tok/s 미만일 수 있다고 본다(S45). 프런티어 모델 대형화는 SRAM 기반 설계에 불리하다. 반면 TSMC N5 웨이퍼를 쓰고 HBM·CoWoS에 의존하지 않아 메모리·패키징 공급 제약에서는 자유롭다(S34). [S51](https://finance.yahoo.com/news/nvidia-buy-ai-chip-startup-210634730.html) [S49](https://the-decoder.com/nvidia-says-its-groq-3-lpx-is-four-times-faster-than-cerebras-but-the-math-is-more-complicated/) [S18](https://news.google.com/rss/articles/CBMiywFBVV95cUxQSGxfRjlGZUZfR1hack0zbEdZcVJXY1JCaWw4dl9fMFZnQnJHVnVfU3NsZkpVd2hPbjh5Q0dHTVcxYTByelU2b3lMUzVDNk54ZFN4OG1VSko2MXEzV0d3bDdHSTJiRHlrMFZtallYSllLUzdSQ2lVdDVra2ZqY0xPaEV2cmxRaXRIWnhRd19obk82eFBGQXQ1YnpYc2hLY0poOGVsdS1yZ19mVGs0RlFVZ1diV0luRktiNV9Uc05vSHpEbmViQ1NjX1h1UQ?oc=5) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
- [industry] 사업은 칩 회사에서 데이터센터 운영 회사로 바뀌고 있다. 계약된 용량은 600MW 이상이고 2027년 말까지 인도한다(F53, S34). 유럽 200MW 계획이 있고 부지 확보는 '개싸움'이라고 CEO가 표현했다(S54). S-1은 하이퍼스케일 데이터센터 운영 이력이 없다는 점과 단일 파운드리(TSMC 5nm) 의존을 위험으로 적었다(S44). 2026H1 capex는 $548.9M이고(F154) 유동성은 $8.6B다(F152). 자본집약도가 높아지면서 하드웨어 판매 모델보다 투하자본 수익률이 핵심 변수가 되는데, 데이터센터 MW당 capex와 수익률은 확인되지 않았다. [F53] [S54](https://www.datacenterdynamics.com/en/news/cerebras-to-deploy-200mw-of-compute-in-europe-by-end-of-2027/) [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [F154] [F152]
- [runway] 재투자 활주로는 수요 쪽에서는 길다. RPO $25.4B는 FY2026Q2 core 매출 연환산(추정: $209.9M×4)의 약 30배다(F52, F49). 그러나 인식 시기는 24개월 내 22%, 25~48개월 43%로 뒤쪽에 쏠려 있다(F113, F114). 회사는 2027년 매출 3배 이상을 계획한다고 했으나 core/GAAP 구분과 범위가 없다(F174, S34). 가이던스 적중은 2분기 모두 상회였다(C:guidance_hit_rate). 다만 RPO는 사실상 전부 OpenAI 계약이어서 단일 고객의 인도·SLA 이행에 의존하고, OpenAI 대출 가속 조항과 워런트 확정 조건(시총 $40B 초과·2GW 전량 인도)이 얽혀 있다(S44, S45). [F52] [F113] [F114] [F174] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- [unit_economics] 현금 창출은 아직 입증되지 않았다. FY2025 영업현금흐름은 -$10.05M, capex $382.7M로 FCF 마진 -77%다(C:fcf_margin@FY2025). 2026Q2 core 영업이익률은 -16%, GAAP은 -265%다(F85, S34). GAAP 손실에는 IPO 관련 RSU 일회성 SBC 약 $270M가 포함돼 있고(F101), 반복 SBC는 약 $103M으로 추정된다(노트 계산). FY2025 순이익 $237.8M은 G42 선도계약 소멸 이익 $363.3M 일회성에 의존한다(F165, S33). 회계 신호에서 순이익 흑자인데 OCF가 음수인 점이 적색으로 잡혔다. [C:fcf_margin@FY2025] [F85] [F101] [F165]
- [claimed] 웨이퍼 전체를 하나의 칩으로 쓰는 설계로 저지연 추론 속도를 확보했다는 주장이다. 회사가 내놓은 수치는 GPT-OSS 120B 약 3,000 tok/s, GPT-5.6 Sol 750 tok/s 서비스 등이다. 모두 벤더 공개 수치이거나 회사 발언이며 독립 실측은 아니다. 독립 분석(SemiAnalysis)은 SRAM이 18GB에서 40GB, 44GB로 늘다 정체했고 웨이퍼 밖 I/O가 NVLink5의 약 1/6 수준이라고 구조적 한계를 지적한다. [S50](https://benchlm.ai/blog/posts/cerebras-won-speed-not-the-shortlist) [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- [claimed] OpenAI와 선지급·용량 약정 구조로 묶여 있다. OpenAI 750MW 약정과 운전자본 대출이 있고(F136, F137), 대출은 인도·SLA 미달 시 회수·상환 요구가 가능하다(S44). 이는 고객 전환비용이라기보다 상호 의존이며, 고객이 떠나는지 남는지에 대한 갱신·가격 인상 기록은 없다. 8월 OpenAI가 Cerebras 기반 서비스를 확인했다는 보도가 있었으나 저품질 2차 자료다(S47). 9월 말에는 GPT-6.1 Ultrafast가 Nvidia에서 돈다는 SemiAnalysis의 주장이 있었고 양사 모두 확인하지 않았다(S40, S46). [F136] [F137] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S47](https://www.kucoin.com/blog/bd-cerebras-cbrs-stock-drop-openai-nvidia) [S40](https://www.ghanamma.com/?p=71787)
- [claimed] 비용·가격 우위의 흔적은 없다. GPT-OSS 120B 가격은 Cerebras가 Groq보다 높다(입력/출력 1M 토큰당 $0.35/$0.75 대 $0.15/$0.60). Nvidia는 Groq 기술 라이선스를 확보해 같은 저지연 틈새로 들어왔다(S51). Nvidia는 Groq 3 LPX가 Cerebras보다 4배 빠르다고 주장하나 구성 조건이 달라 논쟁 중이다(S49). 속도 우위가 가격 결정력으로 이어졌다는 증거는 아직 없다. [S50](https://benchlm.ai/blog/posts/cerebras-won-speed-not-the-shortlist) [S51](https://finance.yahoo.com/news/nvidia-buy-ai-chip-startup-210634730.html) [S49](https://the-decoder.com/nvidia-says-its-groq-3-lpx-is-four-times-faster-than-cerebras-but-the-math-is-more-complicated/)

### 경영진·자본배분 — mixed

경영진은 낮게 잡은 첫 가이던스를 첫 분기에 웃돌았고(C:guidance_hit_rate 100%), 이는 신뢰도에 긍정적이다. 다만 표본은 한 분기, 두 지표뿐이다. 반면 정렬에는 의문이 남는다. CEO와 CTO는 IPO 직후 매매계획으로 $240M 넘게 팔았고, 회사는 SBC와 고객 워런트 상각을 뺀 'core' 지표를 앞세운다. GAAP 기준으로는 Q2 매출총이익률 14%, 영업손실 $(477.2)M이다. 의결권은 Class B가 99.2%를 쥐고 있어 내부자 통제가 강하다. 보상 연동 지표(DEF 14A)는 근거에 없어 확인하지 못했다. IPO 순수입 대부분은 아직 현금으로 있고, 자본배분 실적은 상장 후 5개월이라 검증할 이력이 없다.

- [compensation] DEF 14A 등 보상 설계 근거가 없어 보상이 매출·FCF·ROIC·주당가치 같은 장기 지표에 연동되는지, 베스팅 기간이 얼마인지 확인하지 못했다(근거 없음). 확인되는 것은 규모뿐이다. Q2 SBC 합계는 $377.0M으로 Q2 GAAP 매출 $180.1M의 두 배를 넘고, IPO 시점 RSU 일시 인식분이 크다. IPO 관련 SBC 급여세 $22.8M도 따로 잡혔다. 회사는 core 영업손실 산출에서 SBC를 제외하므로, 경영진이 강조하는 core 지표는 보상 비용을 가린다. [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F37] [F101] [F100] [C:sbc_to_revenue@FY2025]
- [insider] 상장 직후 대규모 매도가 있었다. CEO 앤드루 펠드먼과 CTO 션 리는 2026-08-20~09-25에 IPO 직후 채택한 매매계획으로 Class A 주식 $240M 넘게 팔았다. 2026-10-01 무렵에는 약 $84M 규모 Form 144 매도 예정 통지도 제출됐다. 매매계획에 따른 매도라 재량 매도는 아니지만, 락업 해제 구간과 주가 하락기(사상 최저 부근)에 겹친다. 내부자 매수 근거는 없다. 한편 내부자 지분은 38.1%, 의결권은 50.8%이고 Class B가 의결권 99.2%를 가져 지분 정렬은 있으나 소수주주의 통제력은 약하다. 2차 자료(S40, S42) 기반이므로 Form 4 원문 확인이 필요하다. [S40](https://www.ghanamma.com/?p=71787) [S42](https://techjacksolutions.com/?p=92070) [F148] [F149] [F146] [F147]
- [guidance] 가이던스 적중률은 100%다. Q2 core 매출은 가이던스 약 $194.0M을 웃돌아 $209.9M이었고, core 매출총이익률은 36–38% 가이던스에 41%로 나왔다. 이후 FY2026 core 매출 가이던스를 $855–865M에서 $880–890M으로, core 영업이익률을 (28)~(32)%에서 (19)~(17)%로 상향했다. 다만 표본이 첫 가이던스 한 번뿐이다. 가이던스가 낮게 설정됐을 가능성이 있고 상향 폭의 지속성은 검증되지 않았다. GAAP 매출 $180.1M은 컨센서스 $194M을 밑돌았다. 즉 가이던스와 보고 기준이 core에 맞춰져 있어 적중은 core에서만 성립한다. [C:guidance_hit_rate] [F172] [F49] [F173] [F50] [F54] [F55] [F169] [F170] [F58] [S30](https://www.newsquawk.com/headlines/cerebras-cbrs-q2-2026-usd-revenue-1801mln-exp-194mln) [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
- [guidance] 정량화되지 않은 장기 발언이 있고 일부는 출처마다 강도가 다르다. CFO는 2027년 매출을 '3배 넘게' 늘린다고 했지만 core/GAAP 구분과 범위가 없다. 2027 core 매출총이익률은 S29에서 60%대 이상을 향한다고 요약됐으나, S36에서는 '시간이 지나며' 60% 초과로 더 약하고 2027년 마진 수치는 제시되지 않았다. Q2 GM 압박 약 500bp를 클라우드 고객에게서 시스템을 재임차(rent-back)한 탓으로 돌린 설명과 'Q3가 저점'이라는 말은 아직 검증되지 않았다. Q3 core GM 가이던스는 38~40%이고 Q3 실적은 11월 초중순 예상이다. [F174] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F57]
- [dilution] 희석은 IPO로 급격히 진행됐다. 가중 희석 주식 수는 FY2026Q1 6,281만 주에서 Q2 1.5억 주로 늘었고, 10-Q 표지 기준 발행주식은 2026-08-05 기준 2.37564억 주다(Class A 1.12247억·B 1.11601억·N 1,371.55만). 미행사·미베스팅 잠재 주식으로 옵션 2,380만, RSU 1,650만, PRSU 900만이 있고, OpenAI 워런트는 명목 행사가 기준 3,344.5만 주가 있다. 완전희석 수는 근거에 없다. 자사주 매입은 없다. 오히려 IPO 때 RSU 세금 원천징수로 $416.1M(F145)을 현금으로 썼다. 즉 SBC 희석을 상쇄한 것이 아니라 IPO 수입으로 세금을 대납했다. 시장 데이터의 주식 수(F41 2.196억)는 10-Q 표지보다 작아 코드의 희석 주식 수가 낮게 잡혔을 수 있다. [F13] [F14] [F69] [F70] [F71] [F72] [F104] [F105] [F106] [F134] [F145] [F41] [C:sbc_to_revenue@FY2025]
- [capital_allocation] 상장 전 이력은 짧고 현금흐름은 약하다. FY2025 영업현금흐름은 -1,005만, capex 3.8억으로 FCF는 -3.9억이다. FY2025 순이익은 흑자지만 G42 관련 선도계약 소멸이익 $363.3M 일회성 항목이 들어 있고, non-GAAP 순손실은 $75.7M이다. 2026년 H1 capex는 5.5억으로 영업현금흐름 -4,750만을 크게 웃돈다. 자금은 IPO 순수입 62.3억, Series H 10.1억, 운전자본 대출 10.0억으로 조달했다. 2026-06-30 총 유동성은 86.0억이다. 투자 수익률을 판단할 이력(M&A·자사주)은 없고, 데이터센터 확장(계약 600MW, 유럽 200MW)이 핵심 배분처다. 2026·2027 capex 가이던스와 MW당 capex는 근거에 없다. [C:fcf@FY2025] [F65] [F67] [F154] [F153] [F156] [F157] [F138] [F152] [F53] [S54](https://www.datacenterdynamics.com/en/news/cerebras-to-deploy-200mw-of-compute-in-europe-by-end-of-2027/) [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
- [capital_allocation] 자금 조달과 고객 구조에는 이해상충 소지가 있다. 고객 인센티브로 워런트를 발행해 매출에서 차감하며(Q2 상각 $44.3M, 워런트 자산 유동 1.7억·비유동 9.6억), OpenAI에는 운전자본 대출 9.2억이 있어 용량 인도 조건에 묶여 있다. 이 대출은 인도·SLA 미달 시 회수될 수 있고 이자율 6%다. FY2025 매출의 MBZUAI 62%와 G42 24%는 UAE 특수관계 고객이다. 경영진은 재무를 매출 성장 쪽으로 쓰고 있어 자본을 고객에게 되돌려 주는 구조다. 이 구조가 주주 수익률로 이어지는지는 아직 입증되지 않았다. [F93] [F97] [F98] [F137] [F139] [F127] [F128] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)

### 회계 품질 — watch

코드가 잡은 red 신호는 `ocf_negative` 하나다. FY2025 GAAP 순이익 흑자는 G42 선도계약 소멸에 따른 일회성 비현금 이익 $363.3M 덕분이다. 이를 빼면 실질은 적자이고, 영업현금흐름이 음수인 것과 모순되지 않는다. 즉 흑자인데 현금이 안 들어오는 이익 부풀리기가 아니라, 비현금 이익이 순이익을 키운 경우다. 재무제표 정정(8-K 4.02)이나 감사인 변경 신호는 근거에 없고, 숫자를 못 믿을 증거는 없다. 다만 조정해서 봐야 할 숫자가 많아 `watch`로 판정한다. (1) GAAP과 core의 괴리가 크다. Q2 GAAP 영업손실은 $477.2M이고 core는 $33.6M이다. 차이는 대부분 SBC $377.0M(IPO 직후 RSU 일괄 인식분 포함)과 고객 워런트 상각 $44.3M이다. 워런트 상각은 매출 차감이라 GAAP 매출이 core보다 낮다. (2) 매출과 매출채권이 UAE 특수관계 고객 두 곳(MBZUAI 62.0%, G42 24.0%)에 쏠려 있었다. (3) 영업현금흐름이 FY2024 +$450M에서 FY2025 −$10M으로 급변했고, FY2026 H1도 −$47.5M이다. 이익의 질은 GAAP 순이익이 아니라 FCF와 core 지표로 봐야 한다. 일회성 이익(FY2025)과 일회성 SBC(Q2 2026)는 반복 이익으로 보면 안 된다.

- [benign] ocf_negative: FY2025 순이익이 흑자(2.4억 USD)인데 영업현금흐름은 −1,005만 USD다. 흑자의 원인은 G42 관련 선도계약 소멸에 따른 일회성 비현금 이익 $363.3M이다. 이를 제외한 non-GAAP 순손실은 $75.7M이며, 영업손실(−1.5억 USD)과 영업현금흐름 음수는 방향이 일치한다. 발생액을 이용해 이익을 키운 것이 아니라 비현금·비반복 이익이 순이익에 섞인 것이다. 일회성이므로 FY2025 순이익과 PER(127.07x)은 의미 있는 밸류에이션 입력이 아니다. 이익이 아니라 FCF(−3.9억 USD)와 non-GAAP 손익으로 봐야 한다. [F162] [F65] [F163] [F45] [F44] [C:ocf@FY2025] [C:fcf@FY2025] [C:net_income@FY2025] [C:pe] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
- [watch] Q2 core 지표는 GAAP과 크게 다르다. GAAP 영업손실 $477.2M에 대해 core는 $33.6M이고, GAAP 매출총이익률 14%에 대해 core는 41%다. 조정 항목은 SBC $377.0M, 고객 워런트 상각 $44.3M, 패스스루, IPO SBC 급여세다. 이 가운데 IPO 일회성 RSU 인식분은 반복되지 않는다. 그러나 워런트 상각은 고객 인센티브이므로 반복될 수 있고 사실상 가격 할인이다. core 매출에는 이 상각을 되돌려 더한 것이므로 core 마진을 GAAP 대용으로 쓰면 안 된다. 경영진이 말하는 장기 마진 목표(2027년)는 입증된 수치가 아니다. [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F84] [F27] [F37] [F93] [F50] [F51] [F100]
- [watch] 고객 워런트(OpenAI 포함)는 매출 차감으로 상각된다. 워런트 자산은 유동 1.7억 USD, 비유동 9.6억 USD이고 상각 일정과 대상 고객은 불완전하게만 공개돼 있다. 향후 워런트 확정과 인도 진행에 따라 GAAP 매출이 core보다 계속 낮아질 수 있다. 패스스루 매출·비용은 총액·순액 구분에 따라 매출 규모가 달라진다. RPO 254.0억 USD는 전환 시기가 길다(24개월 내 22%, 25~48개월 43%). [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F97] [F98] [F93] [F91] [F92] [F52] [F113] [F114]
- [watch] FY2025 매출의 62.0%가 MBZUAI, 24.0%가 G42(둘 다 UAE, 특수관계)였고 상위 2개 고객 비중은 0.86이다. MBZUAI는 연말 매출채권의 77.9%를 차지했다. FY2026 Q2에는 고객 A 34%, B 32%, C 10%로 분산되기 시작했으나 고객 B(OpenAI로 추정)에 대한 의존이 새로 생겼다. UAE 매출은 수출통제(BIS) 위험이 있다. 특수관계 거래라 가격과 조건이 독립 거래와 같은지 확인할 수 없다. [F127] [F128] [F129] [F48] [F116] [F117] [F118] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
- [watch] 고객 B는 Q2 매출채권의 57%, 고객 D는 19%를 차지한다. OpenAI 운전자본 대출($920M 잔액)은 용량 인도로 상환하는 구조이고 인도·SLA 미달 시 회수·가속 상환 조항이 있다. 인도 실패는 부채 부담으로 직결되고, 대출 상환이 매출 인식과 얽혀 있어 수익의 질을 해석하기 어렵다. 영업현금흐름은 FY2024 4.5억 USD에서 FY2025 −1,005만 USD로 급변했는데, 선수금 등 일회성 성격 가능성이 있어 FY2024 현금흐름을 기준 삼으면 안 된다. [F124] [F125] [F137] [F66] [F65] [F153] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- [info] 공개 자료 간 수치 충돌이 있다. 일부 보도는 FY2025 순이익을 $87.9M으로 적었으나 424B4 기준은 2.4억 USD다. 공시 수치를 따르고 2차 자료의 수치는 쓰지 않는다. 재무제표 정정이나 감사인 변경, 계속기업 의문 같은 감사 이슈는 근거에 없다. 단 10-Q 원문과 감사의견 본문은 확인하지 못했다. [S54](https://www.datacenterdynamics.com/en/news/cerebras-to-deploy-200mw-of-compute-in-europe-by-end-of-2027/) [F162] [S33](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) OpenAI 의존이 깨졌다. RPO 25.4B달러(F52)는 사실상 전부 OpenAI 계약이다(S45). SemiAnalysis가 GPT-6.1 Sol Ultrafast가 Nvidia에서 돈다고 주장했고(S40, S46), 핵심 저지연 워크로드가 이탈하기 시작했다. 인도·SLA 미달이나 계약 종료가 생기면 운전자본 대출 9.2억 달러의 가속 상환 조항이 발동한다(F137, S44). 대출 상환 부담과 매출 공백이 동시에 오고, 1.2억 달러대로 불어난 고객 B 매출채권(F124)도 회수 문제가 된다. 주가는 RPO 규모에 대한 믿음으로 버티고 있어서 이 믿음이 깨지면 −60%로 이어진다. [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/) [F52] [F137] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [F124]
- (25%) GAAP 단위경제가 회복되지 않았다. Q2 core 매출총이익률은 41%지만 GAAP은 14%다(F50, F51). 차이는 고객 워런트 상각이며 워런트 자산이 약 1.13B달러 남아 있어 상각이 이어진다(F97, F98). 경영진은 3분기를 저점이라고 했지만(S36), 가이던스가 이미 38~40%로 후퇴해 있다(F57). 3분기 마진이 하단 아래로 나오면 '60% 초과' 장기 목표(S36)는 신뢰를 잃는다. 이렇게 되면 시장은 core 지표를 버리고 GAAP 기준으로 재평가한다. 워런트 상각은 사실상 가격 할인이라 고객 확보 비용이 구조적으로 높다는 뜻이 되고, 멀티플이 압축된다. [F50] [F51] [F97] [F98] [F57] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/)
- (20%) 데이터센터 투자 회수가 지연됐다. 사업이 칩 회사에서 데이터센터 운영 회사로 바뀌었는데(F53, S54), 하이퍼스케일 운영 이력이 없다(S44). H1 capex 5.5억 달러는 영업현금흐름 −4,750만 달러(F154, F153)를 크게 웃돈다. 600MW 계약 용량과 유럽 200MW를 채우려면 현금이 계속 나가고, 부지 확보는 '개싸움'이다(S54). 계약이 장기 선지급 구조라 FCF는 2029년까지 음수에 머문다. 지금 8.6B달러 유동성(F152)이 실제 MW당 capex에 비해 부족해지면 추가 자본 조달과 희석이 불가피하다. 여기에 락업 해제 물량(S38)과 CEO·CTO의 매도(S40)가 겹쳐 수급이 무너진다. [F53] [S54](https://www.datacenterdynamics.com/en/news/cerebras-to-deploy-200mw-of-compute-in-europe-by-end-of-2027/) [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [F154] [F153] [F152] [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) [S40](https://www.ghanamma.com/?p=71787)
- (15%) 기술적 우위가 사라졌다. SRAM 용량 확장이 정체했고 웨이퍼 밖 I/O가 NVLink5보다 훨씬 좁다(S45). 프런티어 모델이 커질수록 SRAM 기반 설계가 불리하다. Nvidia는 Groq 기술을 확보해 같은 저지연 틈새에 들어왔고(S51, S49), AMD와의 분리형 추론 협업(S18)도 비독점이다. GPT-OSS 120B 가격은 이미 Groq보다 높아(S50) 속도 프리미엄이 가격 결정력으로 이어지지 않는다. 클라우드 매출이 신규 고객 없이 정체하면 성장의 축이던 클라우드(F76)가 꺾이고, 하드웨어도 감소 중이라(F73) 둘 다 막힌다. [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S51](https://finance.yahoo.com/news/nvidia-buy-ai-chip-startup-210634730.html) [S49](https://the-decoder.com/nvidia-says-its-groq-3-lpx-is-four-times-faster-than-cerebras-but-the-math-is-more-complicated/) [S18](https://news.google.com/rss/articles/CBMiywFBVV95cUxQSGxfRjlGZUZfR1hack0zbEdZcVJXY1JCaWw4dl9fMFZnQnJHVnVfU3NsZkpVd2hPbjh5Q0dHTVcxYTByelU2b3lMUzVDNk54ZFN4OG1VSko2MXEzV0d3bDdHSTJiRHlrMFZtallYSllLUzdSQ2lVdDVra2ZqY0xPaEV2cmxRaXRIWnhRd19obk82eFBGQXQ1YnpYc2hLY0poOGVsdS1yZ19mVGs0RlFVZ1diV0luRktiNV9Uc05vSHpEbmViQ1NjX1h1UQ?oc=5) [S50](https://benchlm.ai/blog/posts/cerebras-won-speed-not-the-shortlist) [F76] [F73]
- 약한 가정 `base.revenue_growth`: 2027년 성장률은 CFO의 '3배 넘게' 발언(F174)에 기댄 것이다. 이 발언은 core와 GAAP 구분도 범위도 없다(S34). RPO는 24개월 안에 인식될 몫이 22%뿐이고 25~48개월에 43%가 쏠려 있다(F113, F114). 역DCF가 요구하는 성장도 이미 높다(C:implied_cagr@m20). 기저율 표가 없어(C:base_rate@base) 이 성장이 드문지 검증조차 되지 않았다. 실행 위험이 가장 큰 가정이다. [F174] [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F113] [F114] [C:implied_cagr@m20] [C:base_rate@base]
- 약한 가정 `base.fcf_margin`: 2030년 FCF 마진 18% 가정은 core 매출총이익률이 41%대에서 60% 초과 목표로 올라간다는 전제다(F50, S36). 그 목표는 '시간이 지나며'라는 약한 표현이고 2027년 마진 수치는 없다(S36). 3분기 가이던스는 오히려 후퇴했고(F57), GAAP 마진은 14%다(F51). 워런트 상각이 이어지는 한 core 마진과 현금 마진의 격차가 닫힌다는 근거가 없다. [F50] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [F57] [F51]
- 약한 가정 `base.exit_multiple`: 출구 P/FCF 30배는 5년 뒤 성장이 둔화한 시점의 값이다. 현재 EV/매출은 45.52배(C:ev_revenue)이고 기본 시나리오의 연 수익률은 이미 음수다(C:expected_irr). 멀티플이 낮아지면 기대 수익률이 더 나빠진다. 손실 확률도 이미 높다(C:p_loss). 반대로 가정이 맞아도 마진·멀티플 요인이 수익률을 깎는다. [C:ev_revenue] [C:expected_irr] [C:p_loss]

## 검증 (L6)

주장 83개 — supported 65 · unsupported 14 · contradicted 0 · leap 4 · 미검증 0

- [unsupported] 레드팀: 2027년 성장률은 CFO의 '3배 넘게' 발언(F174)에 기댄 것이다. 이 발언은 core와 GAAP 구분도 범위도 없다(S34). RPO는 24개월 안에 인 — 없는 근거 인용: C:base_rate@base
- [leap] 애크먼: 해자 증거 부족: 속도 우위는 벤더 공개 수치뿐이고 독립 실측이 없다. Nvidia의 Groq 기술 확보와 SRAM 확장 정체로 경쟁이 악화되고 있다. 가격은 G — S50은 벤더 공개표이나 S49에 Artificial Analysis 벤치마크(Cerebras 882 tok/s)가 인용돼 '독립 실측이 없다'는 단정은 과장이다(가격 열세·Groq 확보·SRAM 정체는 맞다).
- [unsupported] 클라만: 가격을 비효율적으로 만드는 사건이 있다. 약 1억 7천만 주 규모의 주 락업 해제가 Q3 실적 발표와 겹치고, 분할 해제와 내부자 매도가 이어지고 있다. 사업 가 — 출처 없는 숫자 7000 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 애크먼: 가격: 확률 가중 현재가치는 65.66, 기대 연 수익률 -3.6%, 손실 확률 80%다. 현재가 127.21은 기본 시나리오 내재가치 67.8의 약 2배다. 역 — 기대 IRR −3.6%, 손실 확률 80%, 가격 127.21, 역DCF 47.2%는 맞지만 확률 가중 현재가치 65.66과 기본 시나리오 내재가치 67.8은 인용에 없다.
- [unsupported] 사업·산업: 2026Q2 core 매출총이익률은 41%(하드웨어 38.8%, 클라우드 41.8%)지만 GAAP 매출총이익률은 14%다(F50, F80, F81, F51). 차 — 출처 없는 숫자 1.13e+09 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 모델러: FY2026은 Q3 core 가이던스(F56)와 연간 core 가이던스 상향(F54)에 GAAP 기준 워런트 차감을 반영한 값이다. FY2027은 CFO의 '3배 — RPO 24개월 내 22%·25–48개월 43%는 매출이 2027~2028년에 몰린다는 근거가 아니라 오히려 그 이후로 쏠림을 뜻해 이 성장 경로를 뒷받침한다는 연결이 따라 나오지 않는다.
- [unsupported] 사업·산업: 현금 창출은 아직 입증되지 않았다. FY2025 영업현금흐름은 -$10.05M, capex $382.7M로 FCF 마진 -77%다(C:fcf_margin@FY20 — 출처 없는 숫자 2.7e+08, 1.03e+08 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 앤더슨: 9번 질문: 시장은 왜 과소평가하는가. 역DCF상 현재 가격은 마진 18% 수렴 기준으로 10년간 매출 연 47.2% 성장을 요구한다. 이는 높지만, 현재 성장률 — 역DCF 47.2%, 가격 127.21, 52주 저점 126.05와 소음 요인은 맞지만 '현재 성장률이 이 수준을 웃돈다'는 근거가 인용에 없다.
- [unsupported] 애크먼: 사전 부검이 FCF 범위를 넓힌다. 4개 시나리오 모두 이미 현금이 마이너스인 상태에서 시작하므로, 가정이 맞아도 2029년까지 FCF가 음수이고 마진·멀티플 요 — 없는 근거 인용: C:base_rate@base
- [leap] 사업·산업: 재투자 활주로는 수요 쪽에서는 길다. RPO $25.4B는 FY2026Q2 core 매출 연환산(추정: $209.9M×4)의 약 30배다(F52, F49). 그러 — RPO 약 30배, 22%/43%, 3배 발언의 한계, OpenAI 집중은 맞지만 적중률 1만으로 '2분기 모두 상회'가 따라 나오지 않는다(인용된 가이던스 대조는 Q2 한 번뿐).
- [unsupported] 사업·산업: 매출 집중이 FY2025 상위 2개 고객 86%(F48)에서 완화되고는 있으나 여전히 높다. 2026H1 고객 A 49%, 고객 B 20%, 고객 D 10%이고( — Q2 A 34%·B 32%·C 10%, 상위 3개 76%, 고객 B 매출채권 57%는 맞지만 2026H1 고객 A 49%·B 20%·D 10%(F119–121)는 인용에 없다.
- [unsupported] 애크먼: 10년 6.44배는 강세 시나리오(확률 20%)를 10년으로 늘린 값이다. 기본 시나리오 연 수익률은 -3.0%이고 확률 가중 기대 연 수익률은 -3.6%, 손실 — 없는 근거 인용: C:base_rate@base
- [unsupported] 앤더슨: 사전 부검 3: 현금 창출이 기본 시나리오에서도 2029년까지 음수다. GAAP 매출총이익률은 14%이고 워런트 자산 약 1.13B달러의 상각이 이어진다. 가중  — 출처 없는 숫자 1.13e+09 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 기술적 우위가 사라졌다. SRAM 용량 확장이 정체했고 웨이퍼 밖 I/O가 NVLink5보다 훨씬 좁다(S45). 프런티어 모델이 커질수록 SRAM 기반 설계가  — SRAM·I/O·Groq 확보·가격은 자료에 있으나 S18에 AMD 협업이 '비독점'이라는 내용이 없고 하드웨어 매출 감소는 F73의 금액만으로 확인되지 않는다.
- [leap] 레드팀: 출구 P/FCF 30배는 5년 뒤 성장이 둔화한 시점의 값이다. 현재 EV/매출은 45.52배(C:ev_revenue)이고 기본 시나리오의 연 수익률은 이미 음수 — EV/매출 45.52배와 기대 IRR·손실 확률은 맞지만 C:expected_irr은 확률 가중값이지 '기본 시나리오의 연 수익률'이 아니다.
- [unsupported] 클라만: 확률 가중 가치가 주가보다 낮고 손실 확률이 높다. 약세 시나리오의 현재가치는 단단한 가치보다도 낮아, 시나리오 범위 전체에서 안전마진이 없다. — 기대 IRR 음수와 손실 확률 80%는 맞지만 약세 가치가 단단한 가치보다 낮다는 점과 가중 가치가 주가보다 낮다는 점은 인용에 단단한 가치·주가가 없어 확인되지 않는다.
- [unsupported] 레드팀: OpenAI 의존이 깨졌다. RPO 25.4B달러(F52)는 사실상 전부 OpenAI 계약이다(S45). SemiAnalysis가 GPT-6.1 Sol Ultra — RPO 사실상 전부 OpenAI, SemiAnalysis 주장, 대출 가속 조항은 맞지만 고객 B 매출채권 '1.2억 달러대'는 인용(F124는 57% 비중)에 없다.
- [unsupported] 애크먼: 생존 경로와 단위경제는 필요조건이지 가격의 정당화가 아니다. 슬레이터가 생존을 통과시킨 근거인 유동성 86.0억 달러는 데이터센터 capex로 소진되는 현금이고, — 유동성, capex 대 OCF, 기대 IRR 음수, 가격 127.21은 맞지만 '기본 시나리오 내재가치 67.8'은 인용에 없다.

## 사용자 견해 대조 (분석이 끝난 뒤에만 비교한다)

- 사용자 찬성 vs 하네스 팽팽 — 불일치: 하네스 근거를 먼저 읽는다
- 사용자 주장 (하네스가 검증하지 않음): 앤더슨의 의견에 동의한다
- 사용자 주장 (하네스가 검증하지 않음): 추론이 중요해지는 AI 국면에서 상방이 무궁무진하다

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2024 | FY2025 |
|---|---|---|
| 매출 (revenue) | 2.9억 USD | 5.1억 USD |
| 매출 성장 (revenue_growth) | — | 75.7% |
| 영업이익률 (operating_margin) | — | -28.6% |
| 순이익 (net_income) | — | 2.4억 USD |
| 영업현금흐름 (ocf) | 4.5억 USD | -1,005만 USD |
| 설비투자 (capex) | 2,344만 USD | 3.8억 USD |
| FCF (fcf) | 4.3억 USD | -3.9억 USD |
| FCF 마진 (fcf_margin) | 147.6% | -77.0% |
| FCF/순이익 (fcf_conversion) | — | -1.65x |
| SBC (sbc) | — | 4,980만 USD |
| SBC/매출 (sbc_to_revenue) | — | 9.8% |
| SBC 차감 FCF (fcf_after_sbc) | — | -4.4억 USD |

표에 없는 키도 인용할 수 있다: debt_total, non_gaap_net_income, operating_income

### 시장 · FY2025 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 127.21 USD/share (2026-10-16, F61) |
| 희석 주식 수 (shares) | 2.4억 |
| 시가총액 (market_cap) | 302.2억 USD |
| 순현금 (net_cash) | 70.0억 USD |
| EV (ev) | 232.2억 USD |
| FCF 수익률 (fcf_yield) | -1.3% |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 45.52x |
| PER (pe) | 127.07x |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | 20.2 |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [red] ocf_negative: 순이익은 흑자인데 영업현금흐름이 음수인 해가 있다

### 가이던스 적중 (C:guidance_hit_rate = 100%)

- core_revenue FY2026Q2: 가이던스 1.9억 → 실제 2.1억 = beat [F172, F49]
- core_gross_margin FY2026Q2: 가이던스 37.0% → 실제 41.0% = beat [F173, F50]

### 역DCF — 현재 가격이 가정하는 것

EV 232.2억 USD를 정당화하려면 매출이 10년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 목표 마진으로 직선 수렴, 할인율 10%, 이후 영구성장 3%.
기본 시나리오 목표 마진 18% 기준: 연 47.2% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 57.9% | C:implied_cagr@m10 |
| 15% | 50.4% | C:implied_cagr@m15 |
| 18% | 47.2% | C:implied_cagr@m18 |
| 20% | 45.4% | C:implied_cagr@m20 |
| 25% | 41.7% | C:implied_cagr@m25 |
| 30% | 38.8% | C:implied_cagr@m30 |

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 35% | 16.4억 USD | 26.3% | 6% | 15x | 28.00 | 17.38 | -26.1% |
| 기본 | 45% | 44.2억 USD | 54.0% | 18% | 30x | 109.21 | 67.81 | -3.0% |
| 강세 | 20% | 72.7억 USD | 70.1% | 25% | 35x | 234.00 | 145.30 | +13.0% |

확률 가중: 주당 가치 105.74 · IV 65.66 · 기대 연 수익률 -3.6% (C:expected_irr) · 손실 확률 80% (C:p_loss) · 현재 주가 127.21

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +43.2% · 마진·멀티플(P/S) -42.6% · 주식 수 변화 -3.0% · 현금 축적 -0.6% = -3.1%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -10.6% | -6.8% | -3.5% |
| +0%p | -7.2% | -3.0% | +0.6% |
| +5%p | -3.6% | +0.9% | +4.8% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 7.9억 USD | -58.0% | -4.6억 USD | 2.4억 | 65.4억 USD |
| FY2027 | 15.4억 USD | -39.0% | -6.0억 USD | 2.5억 | 59.4억 USD |
| FY2028 | 24.7억 USD | -20.0% | -4.9억 USD | 2.6억 | 54.5억 USD |
| FY2029 | 34.5억 USD | -1.0% | -3,465만 USD | 2.7억 | 54.2억 USD |
| FY2030 | 44.2억 USD | 18.0% | 8.0억 USD | 2.8억 | 62.1억 USD |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 47.2% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 54.0% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 70.1% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: value_10y=818.8, revenue_5y=14.25x, price=127.2, upside_10y=6.44x, buy_below=163.8
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=63.3억 USD, runway_years=20.2, price=127.2
- 애크먼 case={"from": "base"}: fcf_positive=아니오, leveraged=아니오, intrinsic_value=67.8, price=127.2, mos=-87.6%, buy_below=54.2
- 클라만 case={"from": "base", "exit_multiple": 20, "fcf_margin": 0.12}: fcf_positive=아니오, leveraged=아니오, net_cash_ps=29.5, no_growth_ps=29.5, tangible_book_ps=38.5, owner_fcf=-4.4억 USD, hard_value=38.5, hard_basis=tangible_book_ps, low_52w=126.0, high_52w=386.3, intrinsic_value=36.6, iv_low=17.4, iv_high=67.8, price=127.2, mos=-247.2%, downside=69.7%, growth_premium=76.8%, buy_below=25.6, traded_below_52w=아니오

### 계산 경고

- 낡은 컨센서스 — F59: core_revenue FY2026Q3 컨센서스 2.119e+08가 회사 가이던스 하단 2.14e+08(F56)보다 낮다 — 갱신 전 값으로 보고 제외
- 낡은 컨센서스 — F60: core_revenue FY2026 컨센서스 8.634e+08가 회사 가이던스 하단 8.8e+08(F54)보다 낮다 — 갱신 전 값으로 보고 제외
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
| S34 | filing | 2026-08-12 | [Cerebras Announces Financial Results for Second Quarter 2026 (8-K Ex.99.1)](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) | Q2 FY2026(2026-06-30 종료) 실적 보도자료. GAAP 매출 $180.1M(+74% YoY): 하드웨어 $54.1M(−23%), 클라우드·기타 서비스 $126.0M(+281%). Core 매출 $209.9M(+103%): core 하드웨어 $82.1M(+17%), core 클라우드 $127.7M(+287%). H1 GAAP 매출 $373.5M, core $401.2M. GAAP 매출총이익 $25.6M(14.2%) vs core $85.2M(40.6%); core 하드웨어 GM 38.8%, core 클라우드 GM 41.8%; H1 GAAP GM 29.9%, core 43.4%. GAAP 영업손실 $(477.2)M(−265%) vs core $(33.6)M(−16%); 조정 EBITDA $(53.1)M; GAAP 순손실 $(450.5)M(EPS −$2.98) vs core 순손실 $(6.9)M. Core는 '고객 워런트의 비현금 상각과 주식보상'과 패스스루 항목 등을 제외. 매출 브리지: GAAP $180.1M − 패스스루 매출 $14.5M + 워런트 상각 $44.3M(하드웨어 $28.0M, 클라우드 $16.2M) = core $209.9M. 매출총이익 조정: 패스스루 비용 $14.1M, 워런트 상각 $44.3M, 매출원가 내 SBC $15.4M, IPO 관련 SBC 급여세 $0.5M. 영업 조정: SBC 합계 $377.0M, 워런트 상각 $44.3M, 패스스루 비용 $14.1M, IPO SBC 급여세 $22.8M, 패스스루 매출 차감 $14.5M; GAAP 영업비용 $502.8M vs core $118.8M. Q2 2025 GAAP 순이익 $309.5M에는 선도계약 소멸 이익 $363.3M 포함. 2026-06-30 현금성자산 $6,742.2M, 제한현금 $684.7M, 투자자산(유동) $1,179.4M, 총 유동성 $8.6B. H1 현금흐름: 영업 $(47.5)M, capex $(548.9)M, 재무 +$7,853.2M(IPO 순수입 $6,232.5M, Series H $1,014.2M, 운전자본 대출 $1,004.6M). 가이던스: Q3 core 매출 $214–216M, core GM 38–40%, core 영업이익률 (25)%~(23)%. FY2026 상향: core 매출 $880–890M(종전 $855–865M), core GM 41–43%(종전 38–41%), core 영업이익률 (19)%~(17)%(종전 (28)~(32)%). CFO: 2027년 매출을 '3배 넘게(more than triple)' 늘릴 계획 — 정량 범위·core/GAAP 구분 없음. >600 MW 가동·계약(2027년 말까지 인도), Flex·Sanmina·Rocket EMS 위탁생산으로 2026년 생산능력 10배 이상. TSMC 웨이퍼 확보, HBM·CoWoS·3nm 미사용. 회사 주장: GPT-5.6 Sol 750 tok/s 서비스, AMD 분리형 추론 최대 5배 처리량(2026Q4 양산), AWS Bedrock 분리형 추론(2027Q1). |
| S35 | filing | 2026-06-23 | [Cerebras Announces Financial Results for First Quarter 2026 (8-K Ex.99.1)](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm) | Q1 FY2026(2026-03-31 종료) 실적 보도자료. GAAP 매출 $193.4M(+94% YoY): 하드웨어 $110.6M, 클라우드·기타 $82.8M. Core 매출 $191.3M(+92%). GAAP GM 45%, core 47%. GAAP 영업손실 $15.0M, core $3.5M. GAAP 순손실 $14.0M. Q1과 함께 낸 첫 가이던스: Q2 core 매출 약 $194.0M, core GM 36–38%; FY2026 core 매출 $855–865M, core GM 38–41%, core 영업이익률 (28)%~(32)%. 최대 $850M 리볼빙 신용한도('데이터센터 인수 자금용') — 미인출(MarketBeat 2026-08-12 기준). 실적 이력: Q2 core 매출 $209.9M과 core GM 40.6%는 이 가이던스(약 $194M, 36–38%)를 웃돌았다(S900). |
| S36 | call | 2026-08-12 | [Cerebras Systems Q2 Earnings Call Highlights (MarketBeat)](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) | 2차(콜 요약, 원문 아님). 경영진: Q2 매출총이익률 압박 약 500bp는 수요 대응을 위해 클라우드 고객에게서 시스템을 일시 재임차(rent-back)한 탓; Q3가 GM 저점이고 자체 시스템 데이터센터 가동으로 Q4 개선 예상. 장기 GM 목표는 '시간이 지나며' 60% 초과 — 2027년 마진 수치는 제시하지 않음(S29의 '2027 core GM 60%+'보다 약함). CS-5는 2027년 하반기 예정, 속도 매년 2배·향후 18개월 처리량 20배 이상 주장. RPO $25.4B에는 AWS 등 하이퍼스케일러 백로그 미포함. AWS Bedrock GA 2027Q1 예상, 첫 하이퍼스케일러 매출 2027년 중반, 2028년까지 증가. Q2에 OpenAI·하이퍼스케일러 외 $30M 초과 계약 6건; 고객 Figma·Cognition·Lovable·Block·AlphaSense·GSK·CrowdStrike. 계약 시설로 2027년 추가 3–4배 능력. $850M 리볼버 미인출. |
| S37 | news | 2026-05-13 | [Cerebras stock almost doubles initial offering price in biggest tech IPO in years (SiliconANGLE)](https://siliconangle.com/2026/05/13/cerebras-stock-almost-doubles-initial-offering-price-biggest-tech-ipo-years-raised-55b/) | IPO 2026-05-13 가격 결정, 05-14 거래 시작. 범위 $115–125(2,800만 주) → $150–160(3,000만 주)로 상향 후 $185에 결정. 시초가 $350, 장중 고점 약 $386, 첫날 종가 $311.07(+68%). IPO가 기준 완전희석 가치 약 $56.4B. FY2025 MBZUAI 62%·G42 24% 매출 비중(S-1 기준 보도). |
| S38 | news | 2026-05-17 | [Cerebras Faces Fast IPO Lockup Release (LetsDataScience)](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) | 2차(Seeking Alpha의 S-1 요약 인용). 주 락업은 (a) 2026-09-30 종료 분기 실적 발표 후 2거래일 또는 (b) 투자설명서 날짜 후 180일 중 이른 날 종료. 약 1억 7,100만 주(IPO 규모의 약 5배)가 대상. 180일은 약 2026-11-09(노트 계산). 즉 Q3 실적(2026년 11월 초중순 예상)과 주 락업 해제가 겹친다. |
| S39 | news | 2026-10-13 | [Cerebras stock braces for 19.4 million share unlock (Benzinga)](https://www.benzinga.com/markets/tech/26/10/62330736/cerebras-stock-braces-for-19-4-million-share-unlock) | 2026-10-12 종가 $146.62 — 당시 사상 최저. 10-13 장중 $147.34(이후 위젯 $132.30, −6.94%). 분할 락업 해제: 2026-08-19부터 2주마다 최대 1,460만 주, 2026-09-30 최대 1,940만 주(발행주식 약 8%), 2026-10-14 추가 최대 1,940만 주. Citi는 2026–2028 매출 전망 '변경 없음', GPT-6.1 롤아웃에 대해 '많이 읽기엔 이르다'. 주의: 10-12 종가 $146.62는 기존 F40($175.44를 2026-10-13 값으로 기록, S27 Weiss)이 10-13 종가일 수 없음을 보여준다 — F40은 9/30~10/1 무렵 값으로 보인다(노트 추론). |
| S40 | news | 2026-10-02 | [Cerebras stock hits post-IPO low on Nvidia pressure, lockup expiration (CNBC via Ghanamma)](https://www.ghanamma.com/?p=71787) | CNBC 기사 전재(2차). CEO 앤드루 펠드먼과 CTO 션 리가 2026-08-20~09-25에 IPO 직후 채택한 매매계획으로 Class A 주식 $240M 넘게 매도. 2026-10-02 종가 $166.43, 시총 약 $39B. Axios: IPO 시점에 추가 해제 회차가 '10월 말까지' 이어진다고 보도. 2026-09-30 SemiAnalysis가 X에 OpenAI GPT-6.1 Sol 'Ultrafast' 모드가 Cerebras가 아닌 Nvidia GPU에서 돈다고 게시 — 양사 모두 확인·부인하지 않음. |
| S41 | news | 2026-10-02 | [Cerebras stock hits post-IPO low on Nvidia pressure, lockup expiration (CNBC)](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html) | CNBC 원문. Q2 실적 후 주가 약 14% 하락. OpenAI 계약을 '2028년까지 $10B 넘는' 규모로 기술 — 424B4의 '$20B 넘는'과 충돌(공시 수치 우선). |
| S42 | news | 2026-10-01 | [Cerebras insiders file Form 144 (Tech Jacks citing 24/7 Wall St.)](https://techjacksolutions.com/?p=92070) | 2차. 2026-10-01 무렵 약 $84M 규모 Form 144 매도 예정 통지 제출. 2026-09-30 종가 $194.95, 10-01 장중 약 $177.65(−8.9%). |
| S43 | news | 2026-07-02 | [Cerebras IPO (Curved Trading)](https://curvedtrading.com/articles/en/investing/cerebras-ipo/) | 2차. 2026-06-23 Q1 실적 후 약 2,800만 주 조기 해제, 주 180일 락업은 '2026년 11월 중순 무렵'이라고 기술 — 다른 2차 자료(S904·S905)와 일정이 일부 다르다. Q1 실적 후 주가 약 20% 하락, 매출총이익률 가이던스가 계기, CEO는 '오해'라고 언급. |
| S44 | news | 2026-04-22 | [Cerebras S-1 Teardown: Is the $23B Wafer-Scale IPO the End of GPU Homogeneity? (Futurum)](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) | 2차(S-1 분석). FY2025 매출 비중 MBZUAI 62.0%, G42 24.0%(둘 다 UAE, 특수관계); MBZUAI는 연말 매출채권의 77.9%. FY2025 GAAP 순이익에는 G42 관련 선도계약 소멸에 따른 일회성 비현금 이익 $363.3M 포함; FY2025 non-GAAP 순손실 $75.7M, SBC $49.8M. OpenAI 운전자본 대출: 이자율 6%, 용량 인도로 상환하면 이자 면제; 인도·SLA 미달 시 OpenAI가 대출 자금을 회수하고 상환을 요구할 수 있음. OpenAI 워런트 확정 조건에 시총 $40B 초과·2GW 전량 인도 등 포함, 전량 확정 시 OpenAI 지분 약 10%. AWS와 구속력 있는 텀시트: Bedrock에 CS-3, Trainium3가 prefill·Cerebras가 decode. S-1 위험: UAE 매출 집중, BIS 수출통제, OpenAI 대출 회수, 하이퍼스케일 데이터센터 운영 이력 없음, 단일 파운드리(TSMC 5nm) 의존, TSMC의 5nm→3nm 전환. Series H $1B(Tiger Global 주도) 2026년 2월 종결. 주관사 Morgan Stanley·Citigroup·Barclays·UBS. S-1 시점 가치 약 $23B(후행 매출 약 45배). |
| S45 | news | 2026-05-13 | [Cerebras: Faster Tokens Please (SemiAnalysis)](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) | 2차(독립 분석, 일부 유료). 구조적 비판: SRAM 확장 정체 — 18GB(16nm)·40GB(7nm)·44GB(5nm), N3E는 '축소 0', CS-4도 WSE-3 SRAM 유지. 웨이퍼 밖 I/O 약 150GB/s vs NVLink5 900GB/s. DeepSeek V4에 CS-3 약 24대 vs GB300 NVL72 5랙. 프로덕션 최대 모델 120B(355B 프리뷰), 1T–5T 프런티어 모델은 1,000 tok/s 미만 가능성. WSE-3: TSMC N5 웨이퍼 1장 약 $20k, 44GB SRAM, 약 21PB/s; 마케팅 125 PFLOPS(희소 FP16) vs SemiAnalysis 추정 밀집 약 15.6 PFLOPS(B300 13.5·GB300 15·Rubin 35 PFLOPS 밀집 FP4). 랙당 BOM 약 $450k(메모리 비용으로 $350k에서 상향). 오클라호마 시설은 5°C 입수 6,000톤 냉각 플랜트(NVL72 사양 45°C). RPO는 2025-12-31 $24.6B, '사실상 전부' OpenAI. OpenAI 워런트 완전희석 최대 약 12%; 주당 $82.02 기준 OpenAI 워런트 매출 차감 이론상 최대 약 $2.74B(예상 OpenAI 매출의 약 10%). OpenAI 대출: OpenAI 자신의 미치유 위반이 아닌 사유로 계약이 끝나면 잔액 전액 즉시 상환 요구 가능(가속 조항). |
| S46 | news | 2026-10-01 | [Cerebras (CBRS) stock plummets 9% on Nvidia partnership concerns (Parameter)](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/) | 2차. 2026-09-30 SemiAnalysis 주장: OpenAI GPT-6.1 Sol Ultrafast가 Nvidia에서 돈다 — 핵심은 '낮은 배치 크기' 서비스. 약세 근거: RPO 전환의 가장 중요한 단일 반대 신호(노트 추론). 주의: 이 기사는 IPO가를 $350로 잘못 적음($350은 시초가, IPO가 $185). |
| S47 | news | 2026-10-05 | [Cerebras CBRS stock drop: OpenAI and Nvidia (KuCoin blog)](https://www.kucoin.com/blog/bd-cerebras-cbrs-stock-drop-openai-nvidia) | 저품질 2차. 강세 반론: 2026년 8월 OpenAI가 GPT-5.6 Sol Ultrafast는 Cerebras 기반(최대 약 750 tok/s)이라고 확인; OpenAI는 750MW 계약을 취소하지 않았다. 2026-09-25 주가 $206.75. |
| S48 | news | 2026-10-12 | [Cerebras stock record low, down 62 percent (Crypto Briefing)](https://cryptobriefing.com/cerebras-stock-record-low-down-62-percent/) | 2차, 모호함. '여름에 나온' SemiAnalysis 보고서가 핵심 워크로드의 Cerebras→Nvidia 이동을 시사했다고 보도. 첫날 장중 고점 약 $386 대비 사상 최저. |
| S49 | news | 2026-08-25 | [Nvidia says its Groq 3 LPX is four times faster than Cerebras, but the math is more complicated (The Decoder)](https://the-decoder.com/nvidia-says-its-groq-3-lpx-is-four-times-faster-than-cerebras-but-the-math-is-more-complicated/) | 2차, 날짜는 Hot Chips 발표일(2026-08-25) 기준. Nvidia 주장: Groq 3 LPX가 Gemma 4 31B·100K 컨텍스트에서 3,400 tok/s(Artificial Analysis 벤치마크)로 Cerebras 882 tok/s의 4배. 강세 반론(단서): Nvidia 구성은 가속기 최소 64개 vs Cerebras 1–2대, 밀집 모델이 한 랙에 들어가는 경우이고 MoE 확장은 미검증, CS-4는 비교에서 빠짐. LPX는 2026년 하반기 Nebius부터 가동. |
| S50 | news | 2026-08-18 | [Cerebras won speed, not the shortlist (BenchLM)](https://benchlm.ai/blog/posts/cerebras-won-speed-not-the-shortlist) | 벤더 공개표(독립 실측 아님). 속도: GPT-OSS 120B Cerebras 약 3,000 tok/s vs Groq 약 500; Gemma 4 31B Cerebras 약 1,850 tok/s. 가격: GPT-OSS 120B Cerebras 입력/출력 1M 토큰당 $0.35/$0.75 vs Groq $0.15/$0.60 — 더 빠르지만 더 비쌈. Cerebras 공개 카탈로그는 엔드포인트 2개뿐; 필자는 속도가 에이전트 지연을 좌우하는 일은 드물다고 주장. |
| S51 | news |  | [Nvidia to buy AI chip startup Groq assets (Yahoo Finance / Reuters)](https://finance.yahoo.com/news/nvidia-buy-ai-chip-startup-210634730.html) | 2025년 12월(정확한 날짜 미확인). Nvidia가 Groq 기술 라이선스와 경영진 영입에 합의, 거래 가치 약 $20B — Cerebras의 저지연 추론 틈새에 직접 경쟁. |
| S52 | data | 2026-10-13 | [Cerebras Systems cratered by 20% this year; it's going to double according to this analyst (24/7 Wall St.)](https://247wallst.com/investing/2026/10/13/cerebras-systems-cratered-by-20-this-year-its-going-to-double-in-price-according-to-this-respected-wall-street-analyst/) | 2026-10-13 기준 컨센서스 목표가 $291.64(애널리스트 11명: Strong Buy 3·Buy 7·Hold 1). 최고 목표가 UBS(Timothy Arcuri) Buy $330. 2027년 EPS 컨센서스 $1.27(60일 전 $0.96). 매출 컨센서스는 없음. |
| S53 | news | 2026-06-09 | [Cerebras stock soars 18% as multiple Wall Street firms launch coverage with buy ratings (TIKR)](https://www.tikr.com/blog/cerebras-nasdaq-crbs-stock-soars-18-as-multiple-wall-street-firms-launch-coverage-with-buy-ratings) | 2차. 2026-06-09 9개사 커버리지 개시, 전원 매수 등급, 목표가 $250–300(Barclays·Citi·Mizuho·Morgan Stanley·Needham·Rosenblatt·TD Cowen·UBS·Wedbush). 06-08 종가 $234, 06-09 +18%. UBS: Cerebras는 현재 선지급 계약으로 OpenAI에 출하하는 유일한 공급사. |
| S54 | news | 2026-07-09 | [Cerebras to deploy 200MW of compute in Europe by end of 2027 (DCD)](https://www.datacenterdynamics.com/en/news/cerebras-to-deploy-200mw-of-compute-in-europe-by-end-of-2027/) | 2027년 말까지 유럽 200MW(프랑스·북유럽·노르웨이·핀란드). 기존 미국: Santa Clara·Stockton(Nautilus 부유 바지선)·Dallas·Columbiana AL, Minneapolis 구축 중; Montreal(Bit Digital), Saskatchewan·Manitoba(Bell), Guyana(계획), India(G42와). 2026년 5월 Digi Power X(앨라배마) 40MW 임차. CEO: 부지 확보는 '개싸움(dog fight)'. 주의: 이 기사의 'FY2025 순이익 $87.9M'은 424B4($237.8M)와 충돌 — 공시 수치 사용. |
| S55 | news | 2025-04-01 | [UAE-backed Cerebras passes US security check before IPO (AGBI)](https://www.agbi.com/ai/2025/04/uae-backed-cerebras-passes-us-security-check-before-ipo) | 6개월 넘은 자료. 2025년 3–4월 CFIUS가 G42 관계 심사 통과 — G42는 무의결권 주식 매입($335M, 약 5% 예정). 2024년 상반기 G42가 매출의 87%. 2026년 UAE·인도 출하 수출 허가 현황은 미확인. |

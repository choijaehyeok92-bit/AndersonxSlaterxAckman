# Cerebras Systems (CBRS) 리서치 보고서 — 기준일 2026-10-18

**반대 우세** — 찬성 1 · 반대 2 · 보류 0 · 확신 가중 점수 -0.27 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장 내재: 매출 10년 연 50.4% (FCF 마진 15% 수렴 가정) · 기본 시나리오: 5년 연 44.8%
- 시장이 반영한 것: 현재가 기준 EV는 역DCF상 FCF 마진 20% 수렴 시 연 45% 안팎의 매출 성장을 10년간 요구한다. 컨센서스 목표가는 평균 약 $292이고 FY2027 EPS 컨센서스는 $1.27이다. 시장은 RPO $25.4B와 경영진의 2027년 '3배' 발언을 core 기준으로 받아들이는 쪽이다.
- 우리가 다르게 보는 점: 수주잔고는 크지만 매출 인식은 늦고(24개월 내 22%) 워런트 상각·패스스루 때문에 GAAP 매출과 총이익률이 core보다 훨씬 낮다. 2027년 GAAP 매출은 '3배'가 아니라 약 2배 안팎으로 본다. 즉 컨센서스가 core 기준 낙관에 기대고 있다고 본다. 반면 주가는 락업 해제와 Nvidia 우려로 이미 크게 내려, 약세 시나리오의 상당 부분이 가격에 반영돼 있을 수 있다.
- 왜 우리가 맞는가: GAAP 총이익률이 1분기 45%에서 2분기 14%로 내려갔고 core와의 격차가 워런트 상각 4,430만에서 비롯된다. 고객 워런트 자산이 약 11.3억 쌓여 있어 이 차감은 앞으로도 이어진다. 그리고 RPO 인식 시기가 뒤로 쏠려 있어 단기 성장은 용량 확보 속도에 묶인다. [C:implied_cagr@m20] [F179] [F182] [F52] [F113] [F111] [F51] [F93] [F97] [F98] [F174] [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d)
- 촉매: FY2026 Q3 실적(core·GAAP 총이익률, GAAP 매출 대 core 매출 격차)과 주 락업 해제, 이어서 FY2026 Q4 가이던스와 2027년 매출 정량 범위 제시.
- 시점: 2026년 11월 초중순(Q3 실적), 이후 2027년 2월 전후(Q4 실적)

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **42.84** vs 주가 127.21 · 기대 연 수익률 **-11.5%** · 손실 확률 85%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 35% | 22.57 | 14.01 | -29.2% | 추론 수요가 Nvidia(Groq 계열 저지연 제품)로 이동하고, 모델이 커지면서 SRAM 구조의 한계가 드러난다. OpenAI 핵심 워크로드가 Nvidia GPU에서 돈다는 보도가 사실로 굳는다. 용량은 계속 늘리 |
| 기본 | 50% | 60.33 | 37.46 | -13.9% | FY2026은 core 가이던스 상향분과 H1 GAAP 매출을 반영한다. 2027년은 경영진의 '3배 넘게'(core·GAAP 구분 없음)를 그대로 믿지 않고 GAAP 기준으로 낮춰 본다. RPO 중 24개월 안에  |
| 강세 | 15% | 206.18 | 128.02 | +10.1% | AWS Bedrock 분리형 추론이 2027년 중반부터 하이퍼스케일러 매출을 만들고, 계약 시설로 늘어나는 용량이 빠르게 채워진다. 생산능력 확대와 자체 데이터센터 가동으로 core 총이익률이 장기 목표(60% 초과 |

## 3. 반증 조건 (thesis break)

- [대기 — FY2026Q3 미발표] 앤더슨: 3분기 core 매출이 가이던스 하단 미달 — `core_revenue < 2.14e+08` (FY2026Q3)
- [미충족] 앤더슨: 잔여 이행의무가 200억 USD 아래로 감소 — 계약 잔고 훼손 — `remaining_performance_obligations < 2e+10`
- [수동 확인] 앤더슨: OpenAI 등 상위 고객의 계약 축소·해지 또는 핵심 워크로드의 타사 이전 확인 — 수동 확인
- [대기 — FY2026Q3 미발표] 슬레이터: 3분기 GAAP 총이익률이 상반기 수준으로 회복되면 마진 저점 가설이 입증되어 반대 논지가 약해진다 — `gaap_gross_margin >= 0.3` (FY2026Q3)
- [대기 — FY2026Q3 미발표] 슬레이터: 최대 고객 비중이 30% 아래로 내려가 분산이 실적으로 확인되면 반대 근거가 해소된다 — `customer_a_revenue_share < 0.3` (FY2026Q3)
- [수동 확인] 슬레이터: 2027년 매출의 정량 범위와 계약 잔액 인식 시기가 공시되고 OpenAI 핵심 워크로드가 Cerebras에서 유지된다는 확인이 나오면 수동 판단
- [자료 없음] 애크먼: TTM 잉여현금흐름이 양수로 전환되면 FCF 레드라인 재검토 — `fcf > 0`
- [미충족] 애크먼: GAAP 매출총이익률이 35% 이상으로 수렴하면 core와의 격차 가설 약화 — `gaap_gross_margin >= 0.35`
- [미충족] 애크먼: 주가가 50달러 미만이면 안전마진 재평가 — `price < 50`
- [미충족] 레드팀: OpenAI 분기 매출이 Q2(F130)보다 줄면 RPO 전환이 멈췄다는 뜻 — 이전 병목 신호 — `openai_revenue < 5.68e+07`
- [대기 — FY2026Q3 미발표] 레드팀: core 총이익률이 3분기 가이던스 하단 아래로 내려가면 3분기 저점 설명이 깨졌고 용량 확장 수익률도 의심된다 — `core_gross_margin < 0.38`
- [미충족] 레드팀: GAAP 총이익률이 Q2(14%)보다 더 낮아지면 워런트·재임차 부담이 일시적이 아니라 구조라는 뜻 — `gaap_gross_margin < 0.14`
- [미충족] 레드팀: 주가가 $90 아래로 내려가면 −60%(IPO 후 고점 대비가 아니라 현재가 대비 약 −30%) 경로의 초입으로 본다. 락업 소화 실패 신호 — `price < 90`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | core_revenue | FY2026Q3 | >= 2.14e+08 | 80% | 가이던스 하단(F56)을 지키는지 본다. 기본 시나리오 성장의 첫 관문이다. |
| K2 | core_gross_margin | FY2026Q3 | >= 0.38 | 75% | 가이던스 하단(F57)이다. 2분기 재임차로 눌린 마진이 3분기에 저점을 찍는다는 경영진 설명(S36)을 시험한다. |
| K3 | revenue | FY2026Q3 | >= 1.85e+08 | 60% | GAAP 매출이 2분기(F33)보다 늘어 core와의 격차가 줄어드는지 본다. 기본 시나리오는 GAAP 기준이다. |
| K4 | gaap_gross_margin | FY2026Q3 | >= 0.14 | 60% | GAAP 총이익률(F51)이 2분기보다 나빠지지 않는지 본다. 워런트 상각이 마진을 계속 누르는지 확인한다. |
| K5 | core_revenue | FY2026 | >= 8.8e+08 | 75% | 상향된 연간 가이던스 하단(F54)이다. 경영진 가이던스의 신뢰도를 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.27 · 비중 참고값 0.0% (반대 우세 — 신규 비중 없음) · 슬레이터 시작 비중 0.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 0/5 실패 | founder_led=예, upside_10y=5.40x, revenue_5y=10.90x |
| 슬레이터 | 반대 → 반대 | 3/5 | ✓ | 0/6 실패 | unit_economics=unclear, survival_path=예, starter_weight=0.0%, cash_survives=예, runway_years=20.2, cash_min=63.5억 USD |
| 애크먼 | 반대 → 반대 | 4/5 | ✗ 단순·예측 가능한 사업이 아님; 잉여현금흐름을 만들지 못함 (코드 계산); 레버리지·자본시장 의존; 안전마진 20% 미만 또는 계산 불가 | 0/5 실패 | simple_predictable=아니오, capital_markets_dependent=예, catalyst=없음 — 락업 해제와 Q3 실적은 가치와 가격의 격차를 좁히는 행동이 아니라 시험일 뿐이다, fcf_positive=아니오, intrinsic_value=37.5, mos=-239.6% |

- ⚠ 앤더슨: rebuttals[0] leap: iv 37.46 대 주가 127.21은 맞지만, 인용에 없는 강세 가치 5배 이상을 전제로 삼았다. 역DCF 내재 성장 50%를 회사가 이미 보이는 성장과 같은 범위라고 한 것도 자료에서 따라 나오지 않는다.
- ⚠ 앤더슨: arguments[4] leap: 유동성 8.6B와 runway 20년은 맞지만, '시나리오 어디에서도' 자본시장에 기대지 않는다는 결론은 기본 시나리오 계산값만으로 따라 나오지 않는다.
- ⚠ 앤더슨: arguments[3] leap: 가격 하락과 IPO가 하회는 맞지만, 역DCF 내재 성장 50%가 이미 달성 중인 성장과 같은 규모라는 비교는 인용 자료에 없고 약세 요인이 수급·소음뿐이라는 결론도 따라 나오지 않는다.
- ⚠ 슬레이터: arguments[4]: 인용하지 않은 근거의 숫자 48(S34) — cites에 추가
- ⚠ 애크먼: rebuttals[0] unsupported: 기대 IRR -11.5%, 손실 확률 85%, iv 37.46은 맞지만, 강세 확률 15%와 5.4배는 인용에 없다.
- ⚠ 애크먼: rebuttals[0]: 인용하지 않은 근거의 숫자 5.4(C:upside_10y@anderson) — cites에 추가
- ⚠ 낡은 컨센서스 — F59: core_revenue FY2026Q3 컨센서스 2.119e+08가 회사 가이던스 하단 2.14e+08(F56)보다 낮다 — 갱신 전 값으로 보고 제외
- ⚠ 낡은 컨센서스 — F60: core_revenue FY2026 컨센서스 8.634e+08가 회사 가이던스 하단 8.8e+08(F54)보다 낮다 — 갱신 전 값으로 보고 제외
- ⚠ 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 회계 품질 findings[3] 검증 실패(unsupported): CNBC $10B 대 424B4 $20B 충돌, 순이익 $87.9M 대 $237.8M, 현재가 127.21은 맞지만 F40(175.44)의 날짜가 틀렸다는 주장은 인용 자료에 없다.
- ⚠ 회계 품질 flags[9] 검증 실패(unsupported): capex 5.5억과 워런트 자산 1.7억·9.6억은 맞지만, 상각이 매출 차감으로 처리된다는 내용은 인용한 사실에 없다.
- ⚠ 경영진·자본배분 findings[4] 검증 실패(unsupported): 희석 주식 수 증가, 2.376억 주, SBC 비율, 워런트 10~12%는 맞지만, 자사주 매입이 없다는 내용은 인용 자료에 없다.
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base
- ⚠ 회계 품질 flags[11]: 인용하지 않은 근거의 숫자 100%(C:guidance_hit_rate) — cites에 추가
- ⚠ 회계 품질 flags[13] 검증 실패(unsupported): 인용된 S1과 S5는 내용이 비어 있어 Item 4.02 정정 공시가 없다는 주장을 받치지 못한다.
- ⚠ 사업·산업 findings[2] 검증 실패(unsupported): 출처 없는 숫자 1.7e+08 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 레드팀 premortem[3]: 인용하지 않은 근거의 숫자 311(F178·S37) — cites에 추가
- ⚠ 경영진·자본배분 findings[5] 검증 실패(unsupported): 출처 없는 숫자 1.03e+08 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 회계 품질 flags[12]: 인용하지 않은 근거의 숫자 3.77e+08(C:sbc@FY2026Q2·F37·S34) — cites에 추가
- ⚠ 회계 품질 findings[0] 검증 실패(unsupported): 출처 없는 숫자 1.13e+09 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 회계 품질 flags[14] 검증 실패(unsupported): 인용된 S6은 내용이 비어 있고 S33 발췌에도 감사인 변경 공시 유무가 없어 이 주장을 받치지 못한다.
- ⚠ 사업·산업 findings[8]: 인용하지 않은 근거의 숫자 24(S12·S42·S45), 48(S34), 48(S34) — cites에 추가
- ⚠ 레드팀 premortem[1] 검증 실패(unsupported): 출처 없는 숫자 52.5% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[0]: 인용하지 않은 근거의 숫자 103%(S29·S34) — cites에 추가
- ⚠ 회계 품질 flags[0]: 인용하지 않은 근거의 숫자 127(C:pe·C:price·C:price@ackman) — cites에 추가
- ⚠ 회계 품질 flags[5] 검증 실패(unsupported): 이연매출 1.5억에서 1.7억으로의 증가와 RPO 22%·43%는 맞지만, 대부분 OpenAI 계약이라는 내용은 인용한 사실에 없다.

## 앤더슨 — 찬성 (3/5)

> Cerebras는 추론 시장에서 속도라는 한 축을 극단까지 민 회사이고, 매출이 두 배 이상 불어나는 구간에 들어와 있다. 시장은 지금 락업 해제 물량, 내부자 매도, Nvidia 이전 보도라는 경로의 소음을 가격에 반영하고 있다. 주가는 상장가 아래로 내려왔다. 성장 가설 자체는 아직 훼손되지 않았다. 2분기 core 매출은 가이던스를 넘겼고 연간 가이던스도 올랐다. 수주잔고는 크고, 상장으로 조달한 현금이 용량 확장을 뒷받침한다. 창업자가 의결권을 쥐고 있어 10년 단위로 재투자할 수 있다. 다만 확신은 중간이다. 매출 집중, GAAP과 core의 괴리, 희석, 핵심 워크로드 이탈 가능성은 실재하는 위험이다. 확률 가중 기대수익률은 음수다. 이 투자는 강세 시나리오 한 갈래의 멱법칙에 거는 것이므로 작게 시작해 증거로 키우는 크기가 맞다.

*이전 판단 대비: 입장(찬성)과 확신(3)은 직전과 같다. 달라진 것은 가격이 더 내려간 것(F61)뿐이며 성장 가설을 바꾸는 새 근거는 없다.*

**논거**
- 성장은 이미 숫자로 나오고 있다. 2분기 core 매출은 +103%였고, 첫 가이던스를 두 지표 모두 웃돌았으며 연간 core 매출 가이던스를 올렸다. 1번 질문(5년간 매출 두 배)은 가이던스 기준으로도 통과하고, 강세 시나리오는 그 위에서 5년 매출을 한 자릿수 배수 이상으로 본다. [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F49] [F54] [C:guidance_hit_rate] [C:revenue_cagr@bull]
- 수요 가시성이 크다. RPO가 $25.4B이고 하이퍼스케일러 백로그는 그 안에 들어 있지도 않다. 계약 데이터센터 용량 600MW, OpenAI 750MW 계약, AWS Bedrock 분리형 추론 경로는 용량이 채워지는 속도가 성장을 결정한다는 뜻이다. 수요 쪽 위험보다 공급 쪽 실행이 변수다. [F52] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [F53] [F136] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
- 창업자형 경영진이 지배한다. Class B가 의결권 99.2%를 가지고 내부자 지분이 38.1%이다. 분기 압력에서 자유로운 구조라 대규모 용량 선투자를 10년 지평으로 밀어붙일 수 있다. 3번 질문의 해자는 아직 주장 단계이지만, 재투자 의지는 확인된다. [F146] [F148] [F149] [S33](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)
- 9번 질문: 시장은 무엇을 과소평가하는가. 주가는 상장 첫날 종가 $311.07에서 $127.21로 내려와 상장가 $185 아래다. 역DCF가 요구하는 성장은 높지만 이미 달성 중인 성장률과 같은 규모다. 약세 요인 대부분은 락업 해제와 내부자 매도, 제3자 보도 같은 수급·소음이고 매출 인식에 닿은 훼손이 아니다. 나는 소음 때문에 낮아진 가격에서 시작할 기회로 읽는다. [F178] [F61] [F140] [C:implied_cagr@m15] [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) [S39](https://www.benzinga.com/markets/tech/26/10/62330736/cerebras-stock-braces-for-19-4-million-share-unlock)
- 재무 생존 위험은 낮다. 총 유동성이 $8.6B이고 리볼버는 미인출이다. 시나리오 어디에서도 자본시장에 기대지 않고 용량 확장을 이어갈 수 있다. 앤더슨의 비대칭 논리(손실은 100%가 한계, 상승은 열려 있음)에서 파산 경로가 막혀 있는 것이 중요하다. [F152] [F161] [C:runway_years]

**사전 부검**
- 사전 부검 1: 핵심 워크로드가 Nvidia로 이동한다. SemiAnalysis는 OpenAI의 Ultrafast 모드가 Nvidia GPU에서 돈다고 게시했고, 양사 모두 확인도 부인도 하지 않았다. SRAM 확장 정체와 웨이퍼 밖 I/O 한계는 모델이 커질수록 구조적 약점이 된다. 이것이 사실이면 일시적 소음이 아니라 성장 가설이 깨진 것이다. [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S49](https://the-decoder.com/nvidia-says-its-groq-3-lpx-is-four-times-faster-than-cerebras-but-the-math-is-more-complicated/)
- 사전 부검 2: 매출이 소수 고객과 얽힌 계약에 몰려 있다. 2분기 고객 A 34%·B 32%·C 10%이고, 운전자본 대출은 인도·SLA 미달 시 회수를 요구할 수 있다. 용량 인도가 늦어지면 대출 회수와 워런트 차감이 동시에 오는 경로가 있다. [F116] [F117] [F118] [F137] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- 사전 부검 3: 보고 이익의 질과 희석이다. GAAP 총이익률은 14%로 core 41%와 크게 벌어져 있고 고객 워런트 자산이 쌓여 있다. 발행주식은 늘었고 락업 해제와 RSU가 남아 있어, 주당 가치가 매출 성장만큼 늘지 않을 수 있다. 기본 시나리오 기대수익률이 음수인 이유도 이 마진·멀티플 압축이다. [F51] [F50] [F97] [F98] [F69] [F105] [C:expected_irr]

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 안전마진이다. 기본 시나리오의 현재가치가 주가보다 한참 낮다는 계산은 맞고 부정하지 않는다. 다만 그 계산은 5년 창을 기본 시나리오에 놓고 현재를 정밀하게 재는 도구다. 내가 거는 것은 기본 시나리오가 아니라 강세 시나리오 한 갈래이고, 강세의 10년 주당 가치는 코드가 주가의 5배 이상으로 계산한다. 시장 내재 성장은 높지만 회사가 이미 보이는 성장 규모와 같은 범위다. 그래서 이 투자는 안전마진으로 평가하지 않고 작은 비중의 비대칭 옵션으로 평가한다. [C:iv@base] [C:price] [C:implied_cagr@m15] [C:revenue_cagr@bull]
- → 슬레이터: 슬레이터의 가장 강한 논거는 단위경제가 아직 증명되지 않았다는 점이고 이것도 사실이다. 그러나 마진 하락의 원인으로 경영진이 제시한 설명은 일시적 재임차다. 3분기 core 총이익률 가이던스가 이미 나와 있어 다음 실적이 곧 시험이 된다. 회사는 지금까지 가이던스를 모두 웃돌았다. 증거를 기다리라는 요구는 존중하지만, 실적이 확인된 뒤에는 가장 가치 있는 구간의 일부가 이미 가격에 들어가 있을 수 있다. 그래서 크게 사지 않고 작게 시작한다. [F57] [F50] [F110] [C:guidance_hit_rate] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/)
- → 레드팀: 레드팀의 첫 부검, 즉 핵심 워크로드의 Nvidia 이동은 경로의 소음이 아니라 성장 가설 자체를 깨는 시나리오이므로 가장 진지하게 본다. 다만 현재 근거는 한 건의 제3자 게시이고 양사 모두 확인도 부인도 하지 않았다. 반대로 회사는 OpenAI와 750MW 용량 계약을 맺고 있으며 그 계약은 취소되었다는 공시가 없다. 이동이 사실이면 OpenAI 분기 매출이 줄거나 RPO가 감소하는 형태로 숫자에 나타난다. 내 반증 조건에 RPO를 넣은 이유다. 확인 전까지는 가설 훼손이 아니라 미확인 위험으로 분류한다. [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/) [F136] [F52] [F130]

**인정한 점**
- 애크먼의 지적대로 기본 시나리오 기준 안전마진이 없고 확률 가중 기대수익률이 음수라는 점을 인정한다. 그래서 확신을 올리지 않고 비중은 작게 둔다.
- 슬레이터의 지적대로 GAAP과 core의 격차는 고객 획득 비용 일부가 core에서 빠진다는 뜻이다. 강세 시나리오의 마진 가정은 core가 아니라 GAAP이 수렴해야 성립한다는 점을 인정한다.
- 레드팀이 약한 고리로 꼽은 강세 시나리오의 출구 멀티플과 FCF 마진은 입증된 것이 아니라 내 가정이다. 이 가정이 틀리면 찬성은 성립하지 않는다.


## 슬레이터 — 반대 (3/5)

> 시장의 천장이 정의되지 않은 추론 인프라라는 점과, 상장 자금으로 외부 조달 없이 계획을 실행할 수 있다는 점은 슬레이터의 기준에 맞는다. 그러나 단위경제는 아직 증명되지 않았다. 증거가 가설을 따라오지 못한다. core 총이익률은 1분기 47%에서 2분기 41%로, GAAP 총이익률은 45%에서 14%로 내려갔다. 경영진의 '3분기가 저점' 설명은 2차 요약이다. 매출은 소수 고객에 몰려 있고, 핵심 고객 OpenAI의 최신 워크로드가 Nvidia에서 돈다는 보도가 나왔다. 계약 잔액은 크지만 인식이 뒤로 쏠려 있다. 시작 비중은 1% 내외라는 원칙에 비추어도 지금은 증거를 더 기다릴 단계다. 코드 계산상 기본 시나리오 연 수익률이 음수이고 손실 확률이 높아 안전판도 없다. 3분기 실적에서 마진 저점 가설과 고객 분산이 확인되면 입장을 다시 본다.

**논거**
- 생존은 문제가 아니다. 상장과 Series H로 총 유동성이 충분하고 코드가 계산한 기본 시나리오 현금 경로도 바닥이 0 위에 있다. 이 점이 '반대'를 파산 위험 때문이 아니라 증거 부족 때문으로 한정한다. [F152] [F3] [C:runway_years] [C:net_cash]
- 단위경제 개선의 증거가 없다. core 총이익률은 1분기 47%에서 2분기 41%로, GAAP 총이익률은 45%에서 14%로 내려갔다. '3분기가 저점'이라는 설명은 어닝콜 원문이 아닌 2차 요약이어서 3분기 실적이 나오기 전에는 입증된 것이 아니다. [F110] [F50] [F111] [F51] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/)
- core 마진은 고객 획득 비용의 일부를 제외한 숫자다. GAAP 매출에 고객 워런트 상각을 되가산해 core 매출이 되고, 워런트 자산이 유동과 비유동에 걸쳐 쌓여 있다. 이 차감은 앞으로도 이어지므로 core 기준 빠른 성장이 곧 단위경제의 개선은 아니다. [F93] [F97] [F98] [F33] [F49]
- 고객 집중이 높다. 2분기 고객 A 34%, B 32%, C 10%이고 FY2025에는 상위 2개 고객이 86%였다. 분산은 진행 중이지만 단일 고객 이탈의 충격이 크다. 아직 계획인 분산과 이미 실적인 분산을 가르면 실적은 한 분기뿐이다. [F116] [F117] [F118] [F48]
- 계약 잔액의 인식 시기가 늦다. 24개월 안에 인식될 몫은 22%, 25~48개월은 43%다. 지속성은 크지만 증거가 쌓이는 속도는 느리다. 인도·SLA를 못 맞추면 OpenAI 운전자본 대출 회수 요구가 가능한 구조라, 용량 인도가 곧 생존 조건이다. [F52] [F113] [F114] [F137] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
- 코드 계산상 기본 시나리오 연 수익률은 음수이고 확률 가중 기대 연 수익률도 음수이며 손실 확률이 높다. 가격이 이미 많이 내렸어도 기본 시나리오를 넘어서려면 강세 쪽 가정이 필요하다. 락업 해제가 Q3 실적과 겹치는 구간이라 증거를 보고 키우는 순서가 맞다. [C:expected_irr] [C:p_loss] [C:irr@base] [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d)

**사전 부검**
- 사전 부검 1: 마진이 저점이 아니었다. 3분기에도 core 총이익률이 가이던스 하단을 밑돌고 GAAP과 core의 격차가 좁혀지지 않으면 용량이 늘수록 경제성이 나빠지는 구조라는 뜻이다. [F57] [F51] [F93]
- 사전 부검 2: 핵심 고객의 워크로드가 이동한다. OpenAI 최신 모델의 Ultrafast 모드가 Nvidia GPU에서 돈다는 보도가 사실로 굳으면 계약 잔액의 인식 속도와 대출 상환 구조가 함께 흔들린다. 양사 모두 확인도 부인도 하지 않았다. [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/) [F137]
- 사전 부검 3: 반대가 틀릴 수 있다. 3분기에 마진이 회복되고 하이퍼스케일러 매출이 예정대로 시작되면 이미 하락한 가격에서 기회를 놓친 것이 된다. 가이던스를 두 지표 모두 웃돈 이력이 있다. [C:guidance_hit_rate] [F172] [F173] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/)

**반론**
- → 앤더슨: 앤더슨은 성장이 이미 숫자로 나온다고 하지만 그 성장은 core 기준이다. core 매출은 GAAP 매출에 고객 워런트 상각을 되가산해 만든 값이고, GAAP 총이익률은 1분기 45%에서 2분기 14%로 내려갔다. 가이던스 상회도 한 분기 이력이다. 5배가 성립하려면 마진 저점 가설과 고객 분산이 실적으로 확인되어야 하는데 지금은 둘 다 계획 단계다. 가격이 내려온 것과 가설이 입증된 것은 다른 문제다. [F49] [F33] [F93] [F111] [F51] [C:guidance_hit_rate]
- → 애크먼: 애크먼은 자본시장 의존을 반대 근거로 들지만 총 유동성이 86.0억 USD이고 리볼버가 미인출이라 자금 때문에 계획이 막히지는 않는다. 내 반대는 생존 위험이 아니라 증거 부족이다. 예측 불가능하다는 이유만으로 정의되지 않은 시장을 버리지 않는다. 다만 안전마진 부재와 기대수익률 음수라는 결론에는 동의한다. [F152] [F161] [C:runway_years] [C:expected_irr]
- → 레드팀: 레드팀의 첫 사전 부검에서 가장 강한 것은 OpenAI 매출과 RPO 전환의 정체다. 선행 신호인 OpenAI 분기 매출이 2분기 수준 아래로 내려가는지를 must_be_true에 이미 넣었다. 다만 Nvidia 이동 보도는 양사가 확인도 부인도 하지 않았고, 회사의 GPT-5.6 Sol 750 tok/s 주장과 부딪힌다. 확정 전에는 소음일 수 있어, 보도 하나가 아니라 매출 숫자로 판정한다. [F130] [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/) [S47](https://www.kucoin.com/blog/bd-cerebras-cbrs-stock-drop-openai-nvidia) [F52] [F113]

**참이어야 하는 것**
- [at_risk] 3분기 core 총이익률이 가이던스 하단 이상으로 유지되어 2분기 재임차에 따른 저점이라는 설명이 입증된다
- [at_risk] GAAP 총이익률이 2분기보다 나빠지지 않아 워런트 상각이 마진을 계속 누르지 않는다
- [on_track] 연간 core 매출이 상향된 가이던스 하단 이상으로 마무리된다
- [at_risk] OpenAI 매출이 2분기 수준 이상으로 유지되어 대형 계약이 실제 매출로 전환되고 있음을 보인다

**인정한 점**
- 앤더슨의 지적대로 가이던스를 두 지표 모두 웃돈 이력이 있고, 약세 요인 상당수는 수급 성격이어서 3분기에 마진이 저점을 확인하면 내 반대가 틀린 것이 된다. 그래서 확신은 3으로 유지하고 반증 조건을 3분기 실적에 걸어 둔다.
- 애크먼의 안전마진 지적을 인정한다. 코드 계산상 기본 시나리오 연 수익률이 음수이고 손실 확률이 높아, 증거가 쌓이기 전에 비중을 줄 이유가 없다.


## 애크먼 — 반대 (4/5)

> 단순하고 예측 가능한 현금 창출 사업이라는 내 첫 조건을 통과하지 못한다. 매출은 하드웨어에서 자체 데이터센터 기반 추론 클라우드로 옮겨가는 중이다. 소수 고객과 워런트·선지급·대출이 얽힌 계약에 기대고 있고, GAAP과 core의 격차도 크다. 10년 뒤 FCF를 합리적 범위로 추정하기 어렵다. 잉여현금흐름은 음수이고 대규모 capex가 계속되므로 성장 자금을 자본시장에 의존한다. 기본 시나리오의 현재가치는 주가보다 훨씬 낮아 안전마진이 없다. 주가가 이미 크게 내렸지만, 가치 대비 싸졌다는 증거는 아니다. 락업 해제와 내부자 매도가 겹쳐 격차를 좁힐 촉매도 없다. 좋은 기술일 수는 있어도 내 기준의 투자 대상은 아니다.

**논거**
- 한 문단으로 설명하기 어렵고 10년 FCF를 추정할 수 없다. 클라우드 매출이 하드웨어를 대체하는 중이고, 마진은 core 41%와 GAAP 14%로 크게 갈린다. 이 차이는 고객 워런트 상각과 패스스루 항목에서 나온다. 사업의 경제성을 어느 기준으로 봐야 하는지부터 불분명하다. [F50] [F51] [F73] [F74] [F93]
- FCF 레드라인에 걸린다. FY2025 FCF 마진은 -77.0%였고, FY2026 상반기에도 영업현금흐름은 음수이며 capex는 5.5억 USD다. 현금 소진은 당장의 문제가 아니지만, 이 사업은 성장 자금을 IPO 수입과 대출에 의존한다. [C:fcf_margin@FY2025] [F153] [F154] [F156]
- 가격에 안전마진이 없다. 기본 시나리오 현재가치(IV)는 37.46 USD인데 주가는 127.21 USD다. 기대 연 수익률은 -11.5%이고 손실 확률은 85%로 계산된다. 20% 안전마진 기준에 한참 못 미친다. [C:iv@base] [C:price] [C:expected_irr] [C:p_loss]
- 해자와 고객 구조가 검증되지 않았다. FY2025 상위 2개 고객이 86%였고 둘 다 UAE 특수관계다. 속도 우위는 벤더 공개 수치일 뿐이고 가격 결정력의 증거는 없다. 핵심 워크로드가 Nvidia로 옮겨갔다는 보도가 나왔고 양사 모두 확인하지도 부인하지도 않았다. [F48] [F127] [F128] [S50](https://benchlm.ai/blog/posts/cerebras-won-speed-not-the-shortlist) [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/)
- 경영진 정렬은 혼재되어 있다. 가이던스 적중은 한 분기뿐이라 이력이 짧다. CEO와 CTO는 IPO 직후 매매계획으로 대규모 매도를 이어갔고, 보상 설계 근거(DEF 14A)가 없다. 내가 바꿀 수 있는 경영진도 아니다. Class B가 의결권의 99.2%를 쥐고 있기 때문이다. [C:guidance_hit_rate] [S40](https://www.ghanamma.com/?p=71787) [S42](https://techjacksolutions.com/?p=92070) [F146]

**사전 부검**
- 내 판단이 틀렸다면, 이유는 AWS Bedrock 분리형 추론과 OpenAI 용량 인도가 예상보다 빨라 용량이 채워지고 GAAP 총이익률이 core 쪽으로 수렴하는 경우일 것이다. 가이던스는 지금까지 모두 상회했다. 그 경우 강세 시나리오 쪽 가치가 열리고 FCF 흑자 전환이 앞당겨진다. [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [C:guidance_hit_rate] [F172] [F173]
- 자본시장 의존이라는 판정이 과할 수 있다. 총 유동성이 86.0억 USD이고 리볼버는 미인출이며 순부채는 없다. 자금줄이 끊겨 망할 위험은 �밀리 크지 않다. 이 경우 반대 근거는 안전마진과 사업 예측 불가능성으로 좁혀진다. [F152] [F161] [F8]
- 주가가 이미 첫날 종가에서 크게 내려왔다. 락업 해제 물량이 소화된 뒤 Q3 실적에서 총이익률이 저점을 확인하면 반등할 수 있다. 그러나 이는 가치 대비 가격의 문제가 아니라 수급의 문제이고, 내 기준의 매수 이유가 되지 못한다. [F178] [F61] [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/)

**반론**
- → 앤더슨: 앤더슨은 역DCF가 요구하는 성장이 이미 달성 중인 성장률과 같은 규모라고 하지만, 달성한 것은 한 분기의 core 매출 성장이다. 역DCF는 이 성장이 10년 동안 이어지고 FCF 마진이 직선으로 수렴한다고 가정한다. 기본 시나리오의 기대 연 수익률은 음수이고 손실 확률은 85%다. 상장가 아래로 내려왔다는 것은 가치 대비 싸졌다는 증거가 아니다. 강세 시나리오에 15%의 확률을 걸고 5.4배를 기대하는 것은 생존자 편향에 기댄 논리다. 가격은 기본 시나리오의 현재가치보다 훨씬 높다. [C:implied_cagr@m15] [C:expected_irr] [C:p_loss] [C:iv@base] [F61] [F140]
- → 슬레이터: 슬레이터가 '반대'를 증거 부족으로 한정한 것에 동의한다. 다만 생존 경로와 단위경제는 필요조건이지 가격의 정당화가 아니다. 3분기에 마진 저점이 확인되어 슬레이터의 조건이 풀린다 해도, 기본 시나리오 현재가치는 주가에 한참 못 미치고 FCF는 2029년까지 음수다. 증거가 나와도 좋은 회사를 비싸게 사는 문제는 남는다. 나는 가격 문제에서 한 걸음 더 나아가 반대한다. [C:iv@base] [C:expected_irr] [F57] [F51]
- → 레드팀: 레드팀의 약한 가정 중 기본 시나리오 FCF 마진 15%가 가장 아프다. 사전 부검은 FCF 범위를 위로 넓히기보다 아래로 늘린다. 기본 시나리오조차 2029년까지 FCF가 음수이고, FY2025 FCF 마진은 -77.0%였다. 이 범위에서는 10년 FCF를 합리적 범위로 추정할 수 없으므로 요구하는 안전마진은 20%보다 훨씬 커야 한다. 현재 안전마진은 음수다. [C:fcf_margin@FY2025] [F85] [F154] [C:iv@base] [C:implied_cagr@m15]

**인정한 점**
- 앤더슨의 지적대로 총 유동성이 86.0억 USD이고 리볼버는 미인출이어서 파산 위험은 낮다. 이로써 반대 근거는 자금줄 단절이 아니라 단순성 부재, FCF 음수, 안전마진 부재로 좁혀진다. 자본시장 의존이라는 판정은 코드가 정하며 입장은 그대로다.
- 슬레이터와 앤더슨이 짚은 대로 가이던스를 두 지표 모두 웃돈 이력과 주가 하락(IPO 후 첫날 종가 대비)은 사실이다. 그러나 이력은 한 분기이고 하락은 가치가 아닌 수급 현상이어서 결론을 바꾸지 못한다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Cerebras는 웨이퍼 크기 AI 가속기(WSE)를 하드웨어로 팔고, 자체 데이터센터에서 추론 클라우드로도 판다. 2026년 2분기 GAAP 하드웨어 매출은 $54.1M(−23%), 클라우드·기타는 $126.0M(+281%)이다. 매출 무게가 '시스템 판매'에서 '토큰 추론 서비스'로 옮겨가고 있고, 이는 데이터센터 선투자와 MW 단위 용량 확보에 달린 자본집약 사업이다. 매출은 소수 고객(고객 A 34%·B 32%·C 10%)과 선지급·워런트가 얽힌 대형 계약에 기대고 있다. 2분기 core 총이익률은 41%로 1분기 47%에서 떨어졌다. 단위경제가 개선인지 악화인지는 CAC·이탈률·코호트 공시가 없어 판단할 수 없다. RPO $25.4B는 크지만 대부분 아직 인식되지 않았다.

- [unit_economics] 2분기 core 매출은 $209.9M(+103%)로 가이던스 약 $194M를 웃돌았다. 그러나 core 총이익률은 1분기 47%에서 2분기 41%로, GAAP 총이익률은 45%에서 14%로 내려갔다. 경영진은 수요 대응을 위해 클라우드 고객에게서 시스템을 재임차한 탓이라고 설명하며 3분기가 저점이라고 했다. 이는 회사 설명(2차 요약)이므로 3분기 실적으로 확인해야 한다. [F49] [F172] [F110] [F50] [F111] [F51] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/)
- [unit_economics] core 총이익률은 하드웨어 38.8%, 클라우드 41.8%로 두 사업이 비슷하다. 회사는 3분기 core 총이익률 38~40%를 가이던스로 냈고, 2027년 이후 60% 초과는 '시간이 지나며'라는 장기 목표로만 언급했다. 60%대 전망은 입증된 수치가 아니라 경영진 발언이다. [F80] [F81] [F57] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- [unit_economics] GAAP과 core의 차이가 크다. GAAP 매출 $180.1M은 패스스루 매출 $14.5M을 빼고 고객 워런트 상각 $44.3M을 더해 core $209.9M이 된다. 워런트 상각이 매출 차감으로 잡힌다는 것은 대형 고객 확보에 지분성 보상이 들어간다는 뜻이다. 즉 core 마진은 고객 획득 비용 일부를 제외한 수치다. 워런트 자산도 유동 $170M, 비유동 $960M이 쌓여 있다. [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F91] [F93] [F97] [F98]
- [customers] 고객 집중이 매우 높다. FY2025에는 MBZUAI 62%·G42 24%였고(UAE 특수관계), MBZUAI가 연말 매출채권의 77.9%를 차지했다. 2026년 2분기에는 고객 A 34%·B 32%·C 10%이고 상반기 기준 A 49%·B 20%·D 10%다. 분산은 진행 중이지만 단일 고객 이탈이 매출에 미치는 충격은 여전히 크다. 고객 정체는 노트의 추론(B=OpenAI, A=MBZUAI)이다. [F127] [F128] [F129] [F116] [F117] [F118] [F119] [F120] [F121]
- [customers] OpenAI와의 관계는 매출 기여가 아직 작다. 2분기 OpenAI 매출은 $56.8M으로 GAAP 매출의 일부이며, 750MW 용량이 계약돼 있다. OpenAI 운전자본 대출은 약 $920M이고 이자율 6%다. 용량 인도로 상환하면 이자가 면제되며, 인도·SLA를 못 맞추면 OpenAI가 회수를 요구할 수 있다. 공급자가 고객에게서 자금을 받고 그 용량을 인도해야 하는 구조다. [F130] [F136] [F137] [F139] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- [industry] 경쟁은 Nvidia와 다른 저지연 전문 업체에서 온다. Nvidia는 Groq 3 LPX가 Gemma 4 31B에서 3,400 tok/s로 Cerebras 882 tok/s의 4배라고 주장한다. 이에 대한 반론은 Nvidia 구성이 가속기 최소 64개이고 MoE 확장은 미검증이며 CS-4가 비교에서 빠졌다는 점이다. 또한 Nvidia는 2025년 12월 Groq 기술 라이선스와 경영진 영입(약 $20B)에 합의해 Cerebras의 틈새를 직접 겨냥한다. 두 쪽 모두 벤더 수치다. [S49](https://the-decoder.com/nvidia-says-its-groq-3-lpx-is-four-times-faster-than-cerebras-but-the-math-is-more-complicated/) [S51](https://finance.yahoo.com/news/nvidia-buy-ai-chip-startup-210634730.html) [S50](https://benchlm.ai/blog/posts/cerebras-won-speed-not-the-shortlist)
- [industry] 구조적 약점으로 지적되는 것은 SRAM 확장 정체다. WSE 세대별 SRAM이 18GB(16nm)·40GB(7nm)·44GB(5nm)로 늘다 말았고, CS-4도 WSE-3 SRAM을 유지한다. 웨이퍼 밖 I/O는 약 150GB/s로 NVLink5 900GB/s에 못 미친다. 이 분석에 따르면 1T~5T 규모 프런티어 모델은 1,000 tok/s 미만일 수 있다. 독립 분석(2차)이라 반박 가능하지만 해자가 모델 크기 증가에 약하다는 근거다. [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S8](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBmMUQxb0dVSUo2UzM1MVE2dExHRlRYUlg2QW1GSktqeTd0WmVldXpKaVFIVUxaWVpwQ0RpQlpnYjBUZWJ4ZmZBWHowMzlRQkdPV0E3VzE3VkxfdjJtUmNBNFE1dFI?oc=5)
- [runway] 재투자 수요는 크지만 수익률은 입증 전이다. 상반기 영업현금흐름은 −$47.5M, capex는 $548.9M이고, IPO 순수입 $6,232.5M으로 2분기 말 현금성자산은 $6,742.2M, 총 유동성 $8.6B다. 유럽 200MW 등 용량 확장 계획이 있고, 회사는 부지 확보를 '개싸움'이라 표현했다. 새 MW가 core 약 40% 총이익률을 유지하며 채워지는지가 재투자 수익률을 가른다. 2026~2027년 capex 가이던스와 MW당 capex는 찾지 못했다. [F153] [F154] [F156] [F3] [F152] [S54](https://www.datacenterdynamics.com/en/news/cerebras-to-deploy-200mw-of-compute-in-europe-by-end-of-2027/) [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
- [runway] 수요 가시성은 RPO $25.4B가 보여주지만 인식 시기가 늦다. 24개월 안에 인식될 몫이 22%이고 25~48개월이 43%다. 나머지는 48개월 이후이며 노트 계산이다. RPO에는 AWS 등 하이퍼스케일러 백로그가 빠져 있고, 2027년 매출 '3배 넘게'는 정량 범위가 없는 CFO 계획이다. 가이던스는 지금까지 두 항목 모두 상회해 신뢰 흔적이 있으나 이력이 한 분기뿐이다. [F52] [F113] [F114] [F174] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [F172] [F173]
- [claimed] 웨이퍼 규모 칩으로 낮은 지연 추론이라는 틈새를 차지하고 있다. 벤더 공개표에서 GPT-OSS 120B는 약 3,000 tok/s로 Groq 약 500을 앞선다. 다만 독립 실측이 아니며, 가격은 입력/출력 1M 토큰당 $0.35/$0.75로 Groq $0.15/$0.60보다 비싸다. 속도 우위는 주장일 뿐 가격 결정력의 흔적은 아니다. [S50](https://benchlm.ai/blog/posts/cerebras-won-speed-not-the-shortlist) [S15](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNjNfbnRoZFloVUFkdDZxWUppbzg1ejVBcTIxVGVxQXZOS0hNZFdPVi02UFVGdU1oR0NPWjBrelZnUnY2bHFDSm1hdDl2a0JDNnBWNV9YQ2ZyT21nOWt6TTdFZjZNMm4tMVUzX3lYQy1QMzMwbmNuSmFZalQycjNZQlhFSTRfa2RYeHVFUnFXSGs0aGRMNGVSOGRR?oc=5)
- [claimed] 규모의 해자는 아직 공시 숫자로 입증되지 않았다. 계약 데이터센터 용량 600MW와 위탁생산(Flex·Sanmina·Rocket EMS)으로 2026년 생산능력 10배 이상을 계획한다고 하나 모두 회사 발언이다. 하이퍼스케일 데이터센터 운영 이력이 없다는 점이 S-1 위험으로 꼽힌다. 매출총이익률도 규모 효과를 보이지 않고 core 47%에서 41%로 내려갔다. [F53] [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [F110] [F50]
- [claimed] 전환비용의 흔적은 약하다. OpenAI·AWS 등 대형 계약이 있지만 선지급·워런트·대출이 얽힌 구조라 고객이 가격을 올려도 남았다는 기록은 아니다. 2026-09-30 SemiAnalysis는 OpenAI GPT-6.1 Sol Ultrafast가 Nvidia GPU에서 돈다고 게시했고, 양사 모두 확인하지도 부인하지도 않았다. 핵심 워크로드가 이동할 수 있다는 신호다. [S40](https://www.ghanamma.com/?p=71787) [S46](https://parameter.io/cerebras-cbrs-stock-plummets-9-on-nvidia-partnership-concerns/) [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
- [proven] 공시에서 확인되는 사실은 해자보다 고객 의존이다. FY2025 top2 고객 비중은 86%(MBZUAI 62%·G42 24%)였다. 2026년 2분기에도 고객 A 34%·B 32%·C 10%로 세 고객이 합쳐 대부분을 차지한다. 지배적 점유율이나 낮은 이탈률을 보여주는 공시 지표는 없다. [F48] [F127] [F128] [F116] [F117] [F118]

### 경영진·자본배분 — mixed

경영진은 지분과 의결권을 대부분 쥐고 있고, 상장 후 첫 두 번의 분기 가이던스를 모두 웃돌았다. 한편 CEO와 CTO는 상장 직후 채택한 매매계획으로 대규모 매도를 이어가고 있다. 회사가 내세우는 core 지표는 SBC와 고객 워런트 상각을 제외해 GAAP과 격차가 크다. 보상 설계(DEF 14A)는 근거가 없어 장기 지표 연동 여부를 판단할 수 없다. 자본배분은 상장으로 조달한 자금을 데이터센터와 생산능력에 쏟는 단계다. 아직 수익률이 검증되지 않았고, 매출은 특수관계 성격의 UAE 고객과 OpenAI에 집중돼 있다. 정렬은 '혼재'로 본다.

- [compensation] 보상 연동 지표(장기 FCF·ROIC·주당가치 대 단기 EPS·조정 EBITDA)와 베스팅 기간은 DEF 14A가 수집되지 않아 근거 없음. 확인되는 것은 규모뿐이다. 2분기 SBC가 3.8억 USD이고 그중 상장 시점 RSU 일시 인식분이 2.7억 USD다. 2분기에 IPO 관련 SBC 급여세 2,280만 USD도 따로 나왔다. 미베스팅 RSU 1,650만 주, 옵션 2,380만 주, 조건부 PRSU 900만 주가 남아 있다. 설계가 주주 정렬적인지는 판단할 수 없다. [F37] [F101] [F100] [F105] [F104] [F106] [S1](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm) [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
- [insider] 내부자 지분 38.1%, 의결권 50.8%로 지분 정렬의 토대는 있다. Class B가 의결권의 99.2%를 가져 소수 주주의 영향력은 제한적이다. 그러나 CEO와 CTO가 IPO 직후 채택한 매매계획으로 2026-08-20~09-25에 Class A 주식 2.4억 달러 넘게 팔았다. 10월 초에는 약 8,400만 달러 규모의 Form 144 매도 통지도 제출됐다. 락업 분할 해제 기간에 내부자가 계속 파는 셈이다. 이 중 상당 부분은 2차 자료(CNBC 전재)에 근거한다. [F148] [F149] [F146] [S33](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm) [S40](https://www.ghanamma.com/?p=71787) [S42](https://techjacksolutions.com/?p=92070)
- [guidance] 코드 대조상 가이던스 적중률은 100%(C:guidance_hit_rate)이다. 2분기 core 매출은 가이던스 약 1.9억 USD를 넘겼고 core 매출총이익률 41%는 가이던스 37%를 웃돌았다. 연간 core 매출 가이던스는 855~865백만 USD에서 880~890백만 USD로 올렸다. 다만 표본은 한 분기, 두 지표뿐이라 신뢰도를 입증하기에는 부족하다. 첫 가이던스는 Q1과 함께 나왔고 과거 이력이 없다. 3분기 core 매출총이익률 가이던스(38~40%)는 2분기 실적(41%)보다 낮다. 2027년 매출 '3배 넘게'는 정량 범위도, core와 GAAP 구분도 없는 발언이다. [C:guidance_hit_rate] [F172] [F49] [F173] [F50] [F54] [F55] [F57] [F174] [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [S35](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm)
- [guidance] 공시와 보도가 어긋나는 사례가 있다. CNBC는 OpenAI 계약을 '2028년까지 100억 달러 넘는' 규모로 적었지만 424B4는 '200억 달러 넘는'으로 기술했다. 공시 수치가 우선이므로 보도 오류일 가능성이 크다. 어닝콜 원문이 없어 경영진 발언의 정확성은 2차 요약으로만 확인된다. 2027년 core 매출총이익률 60%대 목표(S29)는 MarketBeat 요약(S36)에서 '시간이 지나며 60% 초과'로 약해져 있다. 두 요약이 서로 다르다. [S41](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html) [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [S33](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)
- [dilution] 상장 전후로 주식 수가 급증했다. 희석 가중평균 주식 수는 1분기 6,281만 주에서 2분기 1.5억 주로 늘었고, 10-Q 표지 기준 발행주식은 약 2.376억 주(2026-08-05)다. 시가총액 계산에 쓰이는 희석 주식 수는 2.4억 주다. FY2025 SBC/매출은 9.8%(C:sbc_to_revenue@FY2025)였다. 2분기 SBC는 매출 대비 2배가 넘는다. OpenAI 워런트는 확정되면 지분을 약 10~12% 차지할 수 있다(SemiAnalysis·Futurum 추정). 완전희석 수는 확정할 수 없다. 자사주 매입은 없어 희석을 상쇄하는 장치도 없다. [F13] [F14] [F69] [C:shares] [C:sbc_to_revenue@FY2025] [F37] [F105] [F104] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- [dilution] 회사가 강조하는 core 지표는 비용을 크게 제외한다. 2분기 GAAP 영업비용 5.0억 USD가 core로는 약 1.2억 USD가 된다. core는 SBC 합계 3.77억 USD와 고객 워런트 상각 4,430만 USD 등을 뺀다. 2분기 GAAP 영업손실은 4.8억 USD, core 영업손실은 3,360만 USD로 격차가 크다. 워런트 상각은 고객에게 지분을 주고 받은 대가라 경제적 비용이다. core 가이던스만 보면 경영 성과를 실제보다 좋게 읽게 된다. 2분기 이후 반복 SBC는 일회성을 뺀 약 1.03억 USD로 추정되나 3분기 확인이 필요하다. [F89] [F90] [F27] [F84] [F93] [F37] [F101] [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)
- [capital_allocation] 상장 순수입 62.3억 USD와 Series H 10.1억 USD로 총 유동성이 86.0억 USD가 됐고, 상반기 설비투자는 5.5억 USD, 영업현금흐름은 -4,750만 USD였다. 신규 자본은 데이터센터·생산능력 확장에 쓰인다. 계약 용량은 600MW이고 유럽 200MW 계획이 있으며 위탁생산사 3곳으로 생산능력을 늘린다. 이 투자의 수익률 이력은 아직 없다. FY2025 FCF는 -3.9억 USD(C:fcf@FY2025)였다. 하이퍼스케일 데이터센터 운영 이력이 없다는 점은 S-1 위험요인에도 명시돼 있다. 유럽 건은 2027년 말까지 200MW 구축을 계획하는 단계다. 자사주·배당·M&A 이력은 근거 없음. [F156] [F157] [F152] [F154] [F153] [C:fcf@FY2025] [F53] [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S54](https://www.datacenterdynamics.com/en/news/cerebras-to-deploy-200mw-of-compute-in-europe-by-end-of-2027/)
- [capital_allocation] 재무구조와 이해관계에 주의할 점이 있다. FY2025 순이익 2.4억 USD는 G42 관련 선도계약 소멸 이익 3.6억 USD(비현금·일회성)가 만든 것이다. non-GAAP 순손실은 -7,570만 USD였다. FY2025 매출의 62%가 MBZUAI, 24%가 G42로 UAE 특수관계 집중이 높았다. OpenAI 운전자본 대출 9.2억 USD는 인도·SLA 미달 시 회수·상환 요구가 가능하고 가속 조항도 있다. 8.5억 USD 리볼버는 미인출이다. 경영진이 일회성 이익과 고객 의존 구조를 얼마나 투명하게 다루는지는 이 점들에서 갈린다. [F162] [F163] [F45] [F127] [F128] [F137] [F161] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)

### 회계 품질 — watch

회계 신호 하나가 코드에서 red(ocf_negative)로 잡혔지만, 원인은 FY2025 순이익 2.4억에 들어 있는 선도계약 소멸이익 $363.3M(일회성·비현금)이다. 이 이익을 빼면 적자이고, 영업현금흐름은 -1,005만이다. 정정공시나 감사인 변경 근거는 없고, 이익 부풀리기보다 이익의 질과 보고 지표(core)의 괴리가 문제라고 본다. 따라서 red_flag가 아니라 watch로 판정한다. 조정해서 봐야 할 숫자는 다섯 가지다. (1) GAAP 순이익 2.4억은 쓰지 않고 non-GAAP 순손실 -7,570만을 본다. (2) core 매출·core 이익률은 고객 워런트 상각(Q2 4,430만)과 SBC를 빼므로 GAAP 매출총이익률 14%를 같이 본다. (3) Q2 SBC 3.8억 중 IPO 일회성 RSU 따라잡기(2.7억)를 제외한 반복 SBC도 크다. (4) 상위 고객 집중(MBZUAI·G42 등 UAE 특수관계)과 매출채권 집중이 있다. (5) OpenAI 운전자본 대출 9.2억은 인도 미달 시 회수·가속 조항이 있어 이익의 질이 계약 이행에 연동된다. 1차 공시(10-Q·424B4·8-K)로 확인된 숫자는 비교적 믿을 만하다. 2차 자료의 수치는 공시와 충돌하는 경우가 있어(OpenAI 계약 규모 $10B vs $20B 이상, FY2025 순이익 $87.9M vs $237.8M) 공시를 우선한다.

- [benign] ocf_negative: FY2025 순이익은 흑자(2.4억)이고 영업현금흐름은 -1,005만이라 코드가 red로 잡았다. 순이익에는 G42 관련 선도계약 소멸에 따른 일회성 비현금 이익 $363.3M(3.6억)이 들어 있다. 이를 빼면 순손실이고, 회사의 non-GAAP 순손실도 -7,570만이다. 즉 현금과 이익의 괴리는 이익 조작이 아니라 일회성 비현금 이익이 원인이다. 다만 FY2025 GAAP 순이익·PER(127x)은 의미가 없는 값이므로 쓰지 않는다. FY2025 FCF는 -3.9억이다. [F162] [F65] [F163] [F45] [C:ocf@FY2025] [C:net_income@FY2025] [C:fcf@FY2025]
- [benign] ocf_to_ni: FY2025 영업현금흐름/순이익이 음수로 나오지만 분모가 일회성 이익으로 부풀려져 있어 비율 자체가 무의미하다. 이익의 질은 non-GAAP 손실과 FCF로 판단한다. FY2024에는 영업현금흐름이 4.5억 흑자였으나 선수금 성격으로 보여 추세 근거로 쓰기 어렵다. FY2026 H1 영업현금흐름은 -4,750만이다. [F162] [F65] [F66] [F153] [C:fcf_conversion@FY2025]
- [concern] accruals: FY2025 말 총자산이 사실 저장소에 없어 코드 계산이 안 된다. 다만 발생액 성격의 일회성 이익 3.6억이 순이익을 키웠으므로 FY2025 발생액은 문턱을 넘었을 가능성이 크다고 본다. 일회성 이익 때문이라 반복 신호로 보지 않는다. FY2026 총자산은 Q1 49.5억에서 Q2 116.3억으로 IPO 현금 유입 때문에 급증했다. [F163] [F162] [F38] [F39]
- [concern] receivables_gap: 매출채권은 Q1 6,263만에서 Q2 1.2억으로 늘었는데 GAAP 매출은 Q1 1.9억에서 Q2 1.8억으로 줄었다. 즉 매출보다 채권이 훨씬 빨리 늘었다. 채권은 특정 고객에 몰려 있다. Q2 고객 B(OpenAI로 추정) 57%·고객 D 19%이고, FY2025 말에는 MBZUAI가 77.9%였다. 회수 위험보다 집중이 문제이며, 특수관계 UAE 고객이라 대금 조건이 시장 조건인지 확인이 필요하다. [F30] [F31] [F32] [F33] [F124] [F125] [F129]
- [benign] inventory_gap: 재고는 Q1 8,904만에서 Q2 3,267만으로 줄었다. 재고 쌓기 신호는 없다. 하드웨어 매출 감소와 클라우드 전환(재임차)에 따른 자산 이동으로 보이며, 쌓인 재고를 이익으로 이월하는 패턴은 없다. [F21] [F22] [F73]
- [benign] deferred_revenue: 이연매출은 Q1 1.5억에서 Q2 1.7억으로 늘었다. 매출이 늘 때 이연매출이 줄어드는 선행 악화 신호(매출 +10% 초과·이연매출 -10% 초과)에 해당하지 않는다. RPO는 $25.4B이지만 인식 시기가 길다. 24개월 안에 22%, 25~48개월에 43%만 인식되며, 대부분 OpenAI 계약이다. [F11] [F12] [F52] [F113] [F114]
- [concern] sbc_to_revenue: FY2025 SBC/매출은 9.8%로 문턱 직전이다. FY2026 Q2는 SBC 3.8억이 GAAP 매출 1.8억의 두 배를 넘는다. 이 중 IPO RSU 일회성 따라잡기 2.7억을 빼도 반복 SBC가 매출에 비해 크다. Q2 GAAP 영업손실 -4.8억은 대부분 이 일회성 SBC 때문이므로 GAAP 영업이익률만으로 사업 부진을 판단하면 안 된다. 반대로 core 영업이익률이 SBC를 빼므로 SBC를 비용으로 봐야 한다. [F36] [F37] [F101] [F166] [C:sbc_to_revenue@FY2025] [F33] [F27]
- [concern] sbc_to_ocf: 영업현금흐름이 FY2025 -1,005만, FY2026 H1 -4,750만으로 음수라 SBC/영업현금흐름 비율은 의미가 없고, SBC가 현금 비용을 대체하고 있는 구조다. SBC 차감 FCF는 FY2025 -4.4억이다. IPO 후 반복 SBC는 Q3로 확인이 필요하다. [F65] [F153] [C:fcf_after_sbc@FY2025] [F102]
- [concern] dilution: 희석 주식 수 가중평균은 Q1 6,281만에서 Q2 1.5억으로 늘었고, 10-Q 표지 발행주식은 2.376억(Class A·B·N 합)이다. IPO, RSU 정산, OpenAI 워런트(확정 시 지분 약 10%)로 희석이 크고, 옵션 2,380만·RSU 1,650만·PRSU 900만이 남아 있다. 완전희석 주식 수를 알 수 없고 S28의 2.196억은 10-Q 표지보다 작다. 주당 수치는 보수적으로 큰 쪽(2.376억)을 써야 한다. [F13] [F14] [F69] [F104] [F105] [F106] [F41] [F134]
- [benign] capitalized: 자본화 소프트웨어 사실이 저장소에 없어 코드 신호를 계산할 수 없다. 회계 이슈는 비용 자본화보다 데이터센터·시스템 capex(FY2026 H1 5.5억)와 고객 워런트 자산에 있다. 워런트 자산은 유동 1.7억·비유동 9.6억이고, 상각이 매출 차감으로 처리된다. 자본화 항목은 10-Q에서 확인이 필요하다. [F154] [F97] [F98]
- [benign] goodwill: 영업권 사실이 없고 인수합병 이력도 근거에 없어 이 신호는 해당하지 않는다고 본다. 자산의 대부분은 IPO 현금이다. [F39] [F3]
- [concern] non_gaap:core_revenue: 회사의 core 지표는 GAAP보다 좋아 보이게 만든다. Q2 core 매출 2.1억 대 GAAP 매출 1.8억은 고객 워런트 상각 4,430만을 되가산하고 패스스루 매출 1,450만을 뺀 결과다. 워런트 상각은 고객에게 지분을 주고 매출을 사는 구조라 경제적 비용인데 core에서는 빠진다. core 매출총이익률 41% 대 GAAP 14%도 같은 이유다. 가이던스는 core 기준이라 beat 기록(100%)도 core에 한정된 것이다. 투자 판단에는 GAAP 기준과 core 기준을 함께 놓고 봐야 한다. [F49] [F33] [F93] [F91] [F50] [F51] [F79]
- [concern] non_gaap:operating_income: Q2 core 영업손실 -3,360만 대 GAAP 영업손실 -4.8억의 차이는 대부분 SBC 합계 3.77억과 IPO SBC 급여세 2,280만이다. SBC는 반복 비용이다. 일회성 IPO 따라잡기 몫은 조정이 타당하나 나머지 반복 SBC까지 빼는 core 영업이익은 실제 수익성을 과대 표시한다. 회사의 FY2026 core 영업이익률 가이던스(-19%~-17%)도 같은 정의다. [F84] [F27] [F100] [F101] [F169] [F90] [F89]
- [benign] restatement: 제공된 8-K 목록(실적 발표·기타 중요 사항)에 Item 4.02 재무제표 정정은 없다. 확인된 근거 범위에서 정정 신호는 없으나, IPO 후 1~2개 분기밖에 안 된 상장 이력이라 감사·내부통제의 검증 이력이 짧다. [S1](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm) [S5](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035605/closing8-k.htm)
- [benign] auditor_change: 근거 목록에 Item 4.01 감사인 변경 공시는 없다. 감사의견(계속기업·핵심감사사항) 원문은 수집하지 못해 확인하지 못했다. [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm) [S33](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)
- [watch] 고객 워런트 상각은 매출 차감으로 처리되고 하드웨어 매출에서 2,800만, 클라우드에서 1,620만이 차감됐다. 워런트 자산 합계는 약 11.3억이다. 상각 일정(2031년 10월까지)과 OpenAI 외 워런트 보유 고객은 확인되지 않았다. OpenAI 워런트 확정 조건(시총 $40B 초과·2GW 인도 등)이 충족되면 매출 차감이 커진다. 이 구조는 매출의 일부를 지분으로 사는 것과 같아 core 매출을 그대로 믿으면 안 된다. [F93] [F94] [F95] [F97] [F98] [F132] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- [watch] FY2025 매출의 MBZUAI 62%·G42 24%로 상위 2개 고객이 86%였고 둘 다 UAE 특수관계다. MBZUAI는 연말 매출채권의 77.9%였다. FY2026 H1에는 고객 A 49%·B 20%·D 10%로 분산되고 있으나 A는 여전히 크다. G42 관련 선도계약 소멸 이익 $363.3M이 순이익에 들어 있어 특수관계 거래가 보고 이익에 직접 영향을 줬다. 계약 구조(MBZUAI·G42)는 확인되지 않았다. 수출통제(BIS) 위험도 S-1에 있다. [F48] [F127] [F128] [F129] [F119] [F120] [F121] [F163] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
- [watch] OpenAI 운전자본 대출 9.2억(이자 6%)은 용량 인도로 상환하면 이자가 면제되고, 인도·SLA 미달 시 회수·상환 요구가 가능하며 계약 종료 시 잔액 전액 즉시 상환 요구 조항이 있다. 부채가 사실상 선지급 성격이라 매출과 부채의 경계가 흐리다. 현금 8.6B에 제한현금 6.8억이 포함되어 있어 가용 유동성은 그보다 작다. [F137] [F139] [F152] [F150] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please)
- [info] 공시와 2차 자료의 충돌이 있다. OpenAI 계약 규모는 CNBC가 $10B 넘는다고 썼지만 424B4는 $20B 넘는다고 썼다. FY2025 순이익도 2차 자료는 $87.9M으로 쓰고 공시는 $237.8M이다. 공시 수치를 우선한다. 또 IPO 후 첫 주가 F40(175.44)은 날짜가 실제와 맞지 않아 현재가 F61(127.21)을 쓴다. [S41](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html) [S54](https://www.datacenterdynamics.com/en/news/cerebras-to-deploy-200mw-of-compute-in-europe-by-end-of-2027/) [S33](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm) [F61]
- [info] 이연 위험이 아닌 지배구조 사실: Class B가 의결권 99.2%를 가지고 내부자 의결권이 50.8%다. 경영진(CEO·CTO)은 IPO 직후 채택한 매매계획으로 $240M 넘게 매도했다. 락업 해제는 Q3 실적 발표 전후와 겹친다. 회계 신호는 아니지만 보고 숫자를 감시할 외부 견제가 약하다는 뜻이다. [F146] [F149] [S40](https://www.ghanamma.com/?p=71787) [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 핵심 워크로드가 Nvidia로 이동하고 OpenAI 매출이 기대만큼 늘지 않는다. RPO $25.4B는 사실상 OpenAI 한 고객에 몰려 있고 24개월 안에 인식될 몫은 22%뿐이다. SemiAnalysis는 GPT-6.1 Sol Ultrafast가 Nvidia GPU에서 돈다고 주장했고 양사 모두 부인하지 않았다. SRAM이 44GB에서 정체돼 1T 이상 프런티어 모델에서는 지연 우위가 사라진다. Nvidia는 Groq 기술을 흡수해 같은 저지연 틈새를 겨냥한다. OpenAI가 인도·SLA 미달을 이유로 용량 배정을 줄이고 $920M 대출의 회수·즉시 상환 조항(가속 조항)을 행사하면, 현금이 풍부해 보이던 재무가 약해진다. 수주잔고가 매출로 바뀌지 않고, 시장은 45배 매출 배수를 거둔다. [S40](https://www.ghanamma.com/?p=71787) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S49](https://the-decoder.com/nvidia-says-its-groq-3-lpx-is-four-times-faster-than-cerebras-but-the-math-is-more-complicated/) [S51](https://finance.yahoo.com/news/nvidia-buy-ai-chip-startup-210634730.html) [F52] [F113] [F137] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
- (20%) 데이터센터 확장 투자가 수익률 없이 자본만 먹는다. 상반기 capex는 $548.9M이었고 2027년 말까지 600MW에 유럽 200MW를 더 짓는다. 하이퍼스케일 데이터센터 운영 이력이 없고, 5°C 입수 냉각 같은 특수 설비를 쓰며 부지 확보는 '개싸움'이다. 새 MW가 채워지지 않거나 core 총이익률이 약 40%에 머물면(60% 목표 미달) FCF는 2029년까지도 음수이고, 회사는 추가 증자를 한다. 락업 해제로 이미 늘어난 주식 수(발행 2.376억)에 옵션·RSU·PRSU·OpenAI 워런트(최대 약 10~12%)가 더해져 주당 가치가 희석된다. 기본 시나리오 연 수익률 분해에서 마진·멀티플이 −52.5%로 가장 크다. [F154] [F53] [S54](https://www.datacenterdynamics.com/en/news/cerebras-to-deploy-200mw-of-compute-in-europe-by-end-of-2027/) [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/) [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [F69] [F104] [F105] [F106] [C:expected_irr]
- (15%) 보고 지표(core)와 경제적 현실의 격차가 드러나며 신뢰가 무너진다. GAAP 총이익률은 Q1 45%에서 Q2 14%로 내려갔고, core는 고객 워런트 상각 $44.3M과 SBC를 뺀다. 워런트 자산이 약 $1.13B 쌓여 있어 상각은 계속 매출을 깎는다. OpenAI 워런트 확정 조건(시총 $40B 초과·2GW 인도)이 충족되면 차감이 더 커질 수 있다. 가이던스 beat 이력은 core 기준이고 한 분기뿐이다. 2027년 '3배 넘게'는 정량 범위도 core/GAAP 구분도 없는 CFO 발언이어서, 실제 GAAP 매출이 2배 안팎에 그치면 컨센서스 EPS $1.27이 무너진다. 경영진은 이미 CEO·CTO 합계 $240M 넘게 매도했다. 동시에 UAE 특수관계 고객(FY2025 매출의 86%)의 수출통제(BIS) 문제가 겹칠 수 있다. [F111] [F51] [F93] [F97] [F98] [F174] [F182] [S40](https://www.ghanamma.com/?p=71787) [S34](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) [F48] [S44](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
- (15%) 락업 해제와 Q3 실적이 겹쳐 수급이 무너지고 가격이 가치로 수렴하지 않는다. 약 1억 7,100만 주가 락업 대상이고 주 락업 해제가 2026년 11월 초중순 Q3 실적과 겹친다. 10월 14일에도 최대 1,940만 주가 풀렸고 주가는 이미 IPO 후 첫날 종가 $311에서 $127로 내려갔다. 시장이 가격을 낮춰도 시나리오 분석상 약세 35%·기본 50%가 모두 현재가(127.21)보다 낮은 현재가치를 주어 확률 가중 손실 확률이 85%다. 인덱스 편입이나 내부자 매도 같은 수급 호재가 없으면 '이미 많이 빠졌다'는 논리가 반복해 깨진다. 컨센서스 목표가 $292는 이미 한 번 어긋난 UBS·Barclays 등 초기 매수 일색 등급에 기대 있다. [S38](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d) [S39](https://www.benzinga.com/markets/tech/26/10/62330736/cerebras-stock-braces-for-19-4-million-share-unlock) [S40](https://www.ghanamma.com/?p=71787) [S53](https://www.tikr.com/blog/cerebras-nasdaq-crbs-stock-soars-18-as-multiple-wall-street-firms-launch-coverage-with-buy-ratings) [F61] [F179] [C:p_loss]
- 약한 가정 `base.fcf_margin`: 기본 시나리오는 5년 뒤 FCF 마진 15%를 가정하지만 FY2025 FCF 마진은 −77%였고 기본 시나리오 연도별 표에서도 2029년까지 FCF가 음수다. 데이터센터 중심 사업은 자본집약적이고 core 총이익률 약 40%에서 영업이익률은 −16%이다. 15%로 가려면 총이익률이 크게 오르고 capex가 매출 대비 급감해야 하는데, MW당 capex와 2026~2027 capex 가이던스가 없어 근거가 부족하다. [C:fcf_margin@FY2025] [F85] [F154] [C:implied_cagr@m15]
- 약한 가정 `base.revenue_growth`: 기본 시나리오는 2027년 매출 성장 +75%(2026 약 $8.1억에서 2027 약 $14.1억)를 가정한다. 이는 CFO의 '3배'보다는 보수적이지만, RPO 24개월 인식 몫이 22%뿐이고 고객 집중이 높으며 하이퍼스케일러 매출은 2027년 중반에야 시작한다. 용량 확보 속도에 묶인 성장인데 용량 가동 일정 자료가 회사 발언뿐이다. 5년 매출 CAGR 44.8%는 기저율 표가 없어 검증되지 않았다. [F174] [F113] [F114] [S36](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/) [C:base_rate@base]
- 약한 가정 `bull.exit_multiple`: 강세 시나리오의 출구 P/FCF 30배는 높은 마진(28%)과 곱해져 주당 가치 $206의 대부분을 만든다. 강세 확률 15%가 기대 수익률을 좌우하는데, 경쟁(Nvidia Groq 3 LPX, SRAM 정체)이 구조적으로 해자를 깎는 상황에서 30배를 유지하려면 성장과 마진이 동시에 입증돼야 한다. 이 가정은 한 변수의 오류가 가치를 크게 흔드는 가장 취약한 지점이다. [S45](https://newsletter.semianalysis.com/p/cerebras-faster-tokens-please) [S49](https://the-decoder.com/nvidia-says-its-groq-3-lpx-is-four-times-faster-than-cerebras-but-the-math-is-more-complicated/) [C:value@bull] [C:irr@bull]

## 검증 (L6)

주장 86개 — supported 70 · unsupported 12 · contradicted 0 · leap 4 · 미검증 0

- [unsupported] 회계 품질: 공시와 2차 자료의 충돌이 있다. OpenAI 계약 규모는 CNBC가 $10B 넘는다고 썼지만 424B4는 $20B 넘는다고 썼다. FY2025 순이익도 2차 자 — CNBC $10B 대 424B4 $20B 충돌, 순이익 $87.9M 대 $237.8M, 현재가 127.21은 맞지만 F40(175.44)의 날짜가 틀렸다는 주장은 인용 자료에 없다.
- [unsupported] 회계 품질: 자본화 소프트웨어 사실이 저장소에 없어 코드 신호를 계산할 수 없다. 회계 이슈는 비용 자본화보다 데이터센터·시스템 capex(FY2026 H1 5.5억)와 고객 — capex 5.5억과 워런트 자산 1.7억·9.6억은 맞지만, 상각이 매출 차감으로 처리된다는 내용은 인용한 사실에 없다.
- [leap] 앤더슨: 애크먼의 가장 강한 논거는 안전마진이다. 기본 시나리오의 현재가치가 주가보다 한참 낮다는 계산은 맞고 부정하지 않는다. 다만 그 계산은 5년 창을 기본 시나리오에 — iv 37.46 대 주가 127.21은 맞지만, 인용에 없는 강세 가치 5배 이상을 전제로 삼았다. 역DCF 내재 성장 50%를 회사가 이미 보이는 성장과 같은 범위라고 한 것도 자료에서 따라 나오지 않는다.
- [unsupported] 경영진·자본배분: 상장 전후로 주식 수가 급증했다. 희석 가중평균 주식 수는 1분기 6,281만 주에서 2분기 1.5억 주로 늘었고, 10-Q 표지 기준 발행주식은 약 2.376억 — 희석 주식 수 증가, 2.376억 주, SBC 비율, 워런트 10~12%는 맞지만, 자사주 매입이 없다는 내용은 인용 자료에 없다.
- [unsupported] 애크먼: 앤더슨은 역DCF가 요구하는 성장이 이미 달성 중인 성장률과 같은 규모라고 하지만, 달성한 것은 한 분기의 core 매출 성장이다. 역DCF는 이 성장이 10년  — 기대 IRR -11.5%, 손실 확률 85%, iv 37.46은 맞지만, 강세 확률 15%와 5.4배는 인용에 없다.
- [unsupported] 레드팀: 기본 시나리오는 2027년 매출 성장 +75%(2026 약 $8.1억에서 2027 약 $14.1억)를 가정한다. 이는 CFO의 '3배'보다는 보수적이지만, RPO — 없는 근거 인용: C:base_rate@base
- [unsupported] 회계 품질: 제공된 8-K 목록(실적 발표·기타 중요 사항)에 Item 4.02 재무제표 정정은 없다. 확인된 근거 범위에서 정정 신호는 없으나, IPO 후 1~2개 분기밖에 — 인용된 S1과 S5는 내용이 비어 있어 Item 4.02 정정 공시가 없다는 주장을 받치지 못한다.
- [unsupported] 사업·산업: GAAP과 core의 차이가 크다. GAAP 매출 $180.1M은 패스스루 매출 $14.5M을 빼고 고객 워런트 상각 $44.3M을 더해 core $209.9M이 — 출처 없는 숫자 1.7e+08 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 경영진·자본배분: 회사가 강조하는 core 지표는 비용을 크게 제외한다. 2분기 GAAP 영업비용 5.0억 USD가 core로는 약 1.2억 USD가 된다. core는 SBC 합계 — 출처 없는 숫자 1.03e+08 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 앤더슨: 재무 생존 위험은 낮다. 총 유동성이 $8.6B이고 리볼버는 미인출이다. 시나리오 어디에서도 자본시장에 기대지 않고 용량 확장을 이어갈 수 있다. 앤더슨의 비대칭 — 유동성 8.6B와 runway 20년은 맞지만, '시나리오 어디에서도' 자본시장에 기대지 않는다는 결론은 기본 시나리오 계산값만으로 따라 나오지 않는다.
- [unsupported] 회계 품질: 고객 워런트 상각은 매출 차감으로 처리되고 하드웨어 매출에서 2,800만, 클라우드에서 1,620만이 차감됐다. 워런트 자산 합계는 약 11.3억이다. 상각 일정 — 출처 없는 숫자 1.13e+09 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 회계 품질: 근거 목록에 Item 4.01 감사인 변경 공시는 없다. 감사의견(계속기업·핵심감사사항) 원문은 수집하지 못해 확인하지 못했다. — 인용된 S6은 내용이 비어 있고 S33 발췌에도 감사인 변경 공시 유무가 없어 이 주장을 받치지 못한다.
- [leap] 사업·산업: OpenAI와의 관계는 매출 기여가 아직 작다. 2분기 OpenAI 매출은 $56.8M으로 GAAP 매출의 일부이며, 750MW 용량이 계약돼 있다. OpenAI — OpenAI 매출 $56.8M은 맞지만, 인용 자료에 GAAP 매출 대비 비중이 없고 RPO가 사실상 OpenAI에 몰려 있다는 점과도 어긋나 '매출 기여가 작다'는 결론이 따라 나오지 않는다.
- [unsupported] 레드팀: 데이터센터 확장 투자가 수익률 없이 자본만 먹는다. 상반기 capex는 $548.9M이었고 2027년 말까지 600MW에 유럽 200MW를 더 짓는다. 하이퍼스케 — 출처 없는 숫자 52.5% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 앤더슨: 9번 질문: 시장은 무엇을 과소평가하는가. 주가는 상장 첫날 종가 $311.07에서 $127.21로 내려와 상장가 $185 아래다. 역DCF가 요구하는 성장은 높 — 가격 하락과 IPO가 하회는 맞지만, 역DCF 내재 성장 50%가 이미 달성 중인 성장과 같은 규모라는 비교는 인용 자료에 없고 약세 요인이 수급·소음뿐이라는 결론도 따라 나오지 않는다.
- [unsupported] 회계 품질: 이연매출은 Q1 1.5억에서 Q2 1.7억으로 늘었다. 매출이 늘 때 이연매출이 줄어드는 선행 악화 신호(매출 +10% 초과·이연매출 -10% 초과)에 해당하지  — 이연매출 1.5억에서 1.7억으로의 증가와 RPO 22%·43%는 맞지만, 대부분 OpenAI 계약이라는 내용은 인용한 사실에 없다.

## 사용자 견해 대조 (분석이 끝난 뒤에만 비교한다)

- 사용자 찬성 vs 하네스 반대 우세 — 불일치: 하네스 근거를 먼저 읽는다
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
기본 시나리오 목표 마진 15% 기준: 연 50.4% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 57.9% | C:implied_cagr@m10 |
| 15% | 50.4% | C:implied_cagr@m15 |
| 20% | 45.4% | C:implied_cagr@m20 |
| 25% | 41.7% | C:implied_cagr@m25 |
| 30% | 38.8% | C:implied_cagr@m30 |

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 35% | 13.1억 USD | 20.7% | 5% | 12x | 22.57 | 14.01 | -29.2% |
| 기본 | 50% | 32.4억 USD | 44.8% | 15% | 22x | 60.33 | 37.46 | -13.9% |
| 강세 | 15% | 55.6억 USD | 61.2% | 28% | 30x | 206.18 | 128.02 | +10.1% |

확률 가중: 주당 가치 68.99 · IV 42.84 · 기대 연 수익률 -11.5% (C:expected_irr) · 손실 확률 85% (C:p_loss) · 현재 주가 127.21

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +37.0% · 마진·멀티플(P/S) -52.5% · 주식 수 변화 -3.0% · 현금 축적 +3.5% = -14.9%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -19.1% | -16.5% | -14.2% |
| +0%p | -16.8% | -13.9% | -11.2% |
| +5%p | -14.4% | -11.0% | -8.1% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 8.1억 USD | -58.6% | -4.7억 USD | 2.4억 | 65.3억 USD |
| FY2027 | 14.1억 USD | -40.2% | -5.7억 USD | 2.5억 | 59.6억 USD |
| FY2028 | 20.4억 USD | -21.8% | -4.5억 USD | 2.6억 | 55.2억 USD |
| FY2029 | 26.6억 USD | -3.4% | -9,047만 USD | 2.7억 | 54.3억 USD |
| FY2030 | 32.4억 USD | 15.0% | 4.9억 USD | 2.8억 | 59.1억 USD |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 50.4% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 44.8% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 61.2% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=5.40x, revenue_5y=10.90x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=63.5억 USD, runway_years=20.2
- 애크먼 case={"from": "base"}: price=127.2, fcf_positive=아니오, leveraged=아니오, intrinsic_value=37.5, mos=-239.6%

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

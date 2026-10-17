# Samsara (IOT) 리서치 보고서 — 기준일 2026-10-18

**팽팽** — 찬성 1 · 반대 1 · 보류 1 · 확신 가중 점수 -0.07 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장 내재: 매출 10년 연 19.7% (FCF 마진 25% 수렴 가정) · 기본 시나리오: 5년 연 19.8%
- 시장이 반영한 것: 현재 가격(F218)은 FCF 마진이 20~25%로 올라가는 경우 10년간 연 약 20% 안팎의 매출 성장을 요구한다(C:implied_cagr@m20, C:implied_cagr@m25). 시장은 ARR 성장이 지금 속도로 오래 이어진다고 보고 있다.
- 우리가 다르게 보는 점: 우리 기본 시나리오는 시장이 요구하는 성장과 거의 같거나 약간 낮다. 가이던스가 이미 ARR 성장보다 낮은 매출 성장으로 감속을 예고했고(S53), 올해 FCF 마진은 오히려 낮아지며(F257), 주당 가치는 SBC 희석이 깎는다(C:dilution). 그래서 가격에는 성장 가속에 대한 여유가 없고, 컨센서스와 크게 다른 매출 모델도 아니다.
- 왜 우리가 맞는가: FY27 매출 컨센서스(F216, F217)는 상향 전 값이라 낡았고 가이던스 상향 후 신뢰할 만한 컨센서스를 찾지 못했다. 따라서 매출 쪽의 차별화된 시각은 주장하지 않는다. 우리가 보는 차이는 하나다. 보고 FCF 마진이 SBC를 비용으로 치면 아직 음수라는 점(C:fcf_after_sbc@FY2026)이 가격에 충분히 반영되지 않았을 수 있다. [F218] [F216] [F217] [F257] [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf) [C:implied_cagr@m20] [C:implied_cagr@m25] [C:dilution] [C:fcf_after_sbc@FY2026]
- 촉매: Q3 FY27 실적에서 순신규 ARR 가속 여부와 FCF 마진 전망 수정, SBC 추이가 확인된다.
- 시점: FY27 Q3 실적 발표(12월 초로 추정)

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **31.09** vs 주가 39.57 · 기대 연 수익률 **+4.8%** · 손실 확률 25%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 25% | 15.52 | 9.64 | -17.1% | Motive는 IPO를 철회하고 $1.3B를 조달해 하드웨어 보조와 가격 공세 여력이 생겼다(S64). 같은 시기에 경영진의 FCF 마진 전망은 한 분기 만에 개선에서 하락으로 뒤집혔다(S56, S57). 신규 AR |
| 기본 | 55% | 50.34 | 31.26 | +4.9% | 1년차는 FY27 매출 가이던스 중앙값(F213)과 거의 같다. 이후 성장은 가이던스가 보여 주는 완만한 감속(Q3 가이던스 F214, 연간 성장률 C:revenue_growth@FY2026)을 따라 매년 2~4%p |
| 강세 | 20% | 92.49 | 57.43 | +18.5% | 신규 제품이 순신규 ACV의 20% 넘게를 계속 차지하고(S56) 비미국 비중과 AI 기능 채택이 확대되어 성장이 20%대 중반을 오래 유지한다. $1M 이상 고객의 확장이 이어지고(F252) 기기 원가 부담이 일시 |

## 3. 반증 조건 (thesis break)

- [대기 — FY2027Q3 미발표] 앤더슨: FY2027Q3 순신규 ARR이 1억 달러 미만이면 성장 가설이 훼손된다 — `net_new_arr < 1e+08` (FY2027Q3)
- [대기 — FY2027Q3 미발표] 앤더슨: ARR $100K 이상 고객 수가 줄면 대형 고객 확장 가설이 깨진다 — `customers_over_100k_arr < 3605` (FY2027Q3)
- [수동 확인] 앤더슨: FY28 가이던스가 매출 성장 감속을 한 자릿수 후반으로 반영하면 수동 확인
- [대기 — FY2027Q3 미발표] 슬레이터: 다음 분기 ARR이 22억 달러 미만이면 순신규 ARR 둔화가 가속된 것 — `arr < 2.2e+09` (FY2027Q3)
- [대기 — FY2027Q3 미발표] 슬레이터: GAAP 영업이익이 다시 적자로 돌아서면 SBC가 영업 레버리지를 지운 것 — `operating_income < 0` (FY2027Q3)
- [수동 확인] 슬레이터: 외부 조달(증자·차입)이 필요해지는 징후 — 수동 확인
- [미충족] 애크먼: 주가가 기본 시나리오 현재가치에 20% 안전마진을 둔 수준 아래로 내려오면 가격 근거가 바뀐다 — `price < 25`
- [대기 — FY2027Q3 미발표] 애크먼: FY2027 Q3 매출이 가이던스를 크게 웃돌아 성장 감속 가정이 흔들린다 — `revenue >= 5.3e+08` (FY2027Q3)
- [수동 확인] 애크먼: SBC 차감 FCF가 양수로 전환되면 현금 창출 전제를 다시 평가 — 수동 확인
- [미충족] 레드팀: 분기 순신규 ARR이 $110M 아래로 — Q2 $134.1M, Q4 FY26 $144.8M 대비 감속이 가시화, 성장 지속 서사 훼손 — `net_new_arr < 1.1e+08`
- [미충족] 레드팀: 비GAAP 총이익률이 76% 아래로 — 기기 원가·가격 경쟁이 구독 마진을 누르기 시작 — `non_gaap_gross_margin < 0.76`
- [미충족] 레드팀: 분기 SBC가 $100M 초과 — Q2 $96.4M에서 추가 급증, 영업 레버리지가 SBC로 상쇄되고 희석 가속 — `sbc > 1e+08`
- [미충족] 레드팀: ARR $100K 이상 고객 분기 순증이 170곳 미만으로 — Q2 242곳(최대)에서 확장 엔진 둔화 — `customers_over_100k_arr_net_adds < 170`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | revenue | FY2027Q3 | >= 5.15e+08 | 85% | 가이던스(F214) 중앙값 이상을 달성하는지로 기본 시나리오 1년차 매출 경로를 시험한다. |
| K2 | revenue | FY2027 | >= 2.05e+09 | 65% | FY27 가이던스 상단(F213) 위로 나오는지로 기본 시나리오의 첫 해 성장을 시험한다. |
| K3 | arr | FY2027Q3 | >= 2.24e+09 | 60% | ARR(F209)에 순신규 ARR 약 1.15억을 더한 값으로 감속 속도를 시험한다. 못 미치면 약세 시나리오 쪽이다. |
| K4 | operating_income | FY2027Q3 | > 0 | 60% | GAAP 영업이익 흑자 유지(F127)로 SBC 증가가 영업 레버리지를 지우지 않는지 시험한다. |
| K5 | sbc | FY2027Q3 | <= 1e+08 | 55% | 분기 SBC가 Q2(F177)보다 더 뛰지 않는지로 희석과 FCF 질 문제의 방향을 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.07 · 비중 참고값 0.0% (팽팽 — 신규 비중 없음) · 슬레이터 시작 비중 1.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 1/5 실패 | founder_led=예, upside_10y=5.29x, revenue_5y=2.90x |
| 슬레이터 | 보류 → 보류 | 2/5 | ✓ | 0/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=1.0%, cash_survives=예, cash_min=13.3억 USD |
| 애크먼 | 반대 → 반대 | 4/5 | ✗ 안전마진 20% 미만 또는 계산 불가 | 0/5 실패 | simple_predictable=예, capital_markets_dependent=아니오, catalyst=없음 — 자사주 매입 프로그램이 없고 창업자가 Class B로 지배해 외부 주주가 만들 촉매가 없다. 다음 확인 시점은 Q3 실적(순신규 ARR, FCF 마진 전망)뿐이다., fcf_positive=예, net_debt_to_ebitda=-26.94x, intrinsic_value=31.3, mos=-26.6% |

- ⚠ 앤더슨: arguments[0] contradicted: ARR +30%와 FY2026 성장 29.6%는 맞지만, 가이던스 상향은 3월 최초 가이던스 이후 6월·9월 두 번이다(자료: '이후 두 번 상향'). '세 차례'는 틀리다.
- ⚠ 앤더슨: rebuttals[2] unsupported: 출처 없는 숫자 18.1% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 앤더슨: risks[2]: 인용하지 않은 근거의 숫자 3%(C:operating_margin@FY2026·C:share_change@FY2026·S58) — cites에 추가
- ⚠ 앤더슨: rebuttals[2]: 인용하지 않은 근거의 숫자 25.3%(C:sbc_to_revenue@FY2024) — cites에 추가
- ⚠ 애크먼: risks[2] contradicted: 인용한 가이던스 값 세 개(1.97B→2.009B→2.045B)는 최초 가이던스에 두 번 상향한 것이어서 '세 번 올린'은 맞지 않다. 컨센서스가 낡았다는 부분은 자료와 맞는다.
- ⚠ 애크먼: rebuttals[0]: 인용하지 않은 근거의 숫자 55%(C:p@base) — cites에 추가
- ⚠ 애크먼: arguments[3]: 인용하지 않은 근거의 숫자 100(S50·S56·S57), 100(S50·S56·S57), 3%(C:operating_margin@FY2026·C:share_change@FY2026·S58) — cites에 추가
- ⚠ 애크먼: rebuttals[1]: 인용하지 않은 근거의 숫자 2.2e+09(C:total_assets@FY2026Q2·F183) — cites에 추가
- ⚠ 낡은 컨센서스 — F216: 같은 revenue FY2027 컨센서스 F217가 더 최근 — 제외
- ⚠ 낡은 컨센서스 — F217: revenue FY2027 컨센서스 2.01e+09가 회사 가이던스 하단 2.043e+09(F238)보다 낮다 — 갱신 전 값으로 보고 제외
- ⚠ 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 회계 품질 findings[0] 검증 실패(unsupported): 출처 없는 숫자 1.4e+07 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 회계 품질 flags[0]: 인용하지 않은 근거의 숫자 27.2%(C:sbc_to_revenue@FY2023), 25.3%(C:sbc_to_revenue@FY2024) — cites에 추가
- ⚠ 레드팀 weakest[2] 검증 실패(unsupported): 출처 없는 숫자 61% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): 출처 없는 숫자 7500, 0.1% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 회계 품질 findings[2]: 인용하지 않은 근거의 숫자 2.3e+08(C:cash@FY2025·C:cash_total@FY2025·C:net_cash@FY2025) — cites에 추가
- ⚠ 레드팀 weakest[0]: 인용하지 않은 근거의 숫자 15.3%(C:accruals_ratio@FY2025) — cites에 추가
- ⚠ 경영진·자본배분 findings[2] 검증 실패(contradicted): 나열한 가이던스는 3월 최초값에서 6월·9월 두 번 올린 것이어서(자료: '이후 두 번 상향') '세 번 올렸다'는 틀리다. 추정 대비 매출 초과는 맞다.
- ⚠ 회계 품질 flags[2]: 인용하지 않은 근거의 숫자 24%(C:inventory_growth@FY2026·C:revenue_cagr@bull·S53), 29.6%(C:revenue_growth@FY2026) — cites에 추가
- ⚠ 레드팀 premortem[0] 검증 실패(unsupported): 없는 근거 인용: C:bear
- ⚠ 회계 품질 findings[6] 검증 실패(unsupported): 출처 없는 숫자 1.8% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 회계 품질 flags[1]: 인용하지 않은 근거의 숫자 4.2e+08(C:fcf_after_sbc@FY2022·C:revenue@FY2026Q3·F155) — cites에 추가

## 앤더슨 — 찬성 (3/5)

> Samsara는 물리 세계의 운영 데이터를 클라우드 구독으로 바꾸는 플랫폼이고, 아직 초기 확장 구간에 있다. ARR 성장이 30%로 유지되는 가운데 ARR $1M 이상 대형 고객과 멀티프로덕트 채택이 함께 깊어지고 있다. 코드가 계산한 강세 시나리오 10년 가치는 현재 주가의 5배를 간신히 넘는다(upside_10y 5.29배). 마진 여지가 크고(FCF 마진이 FY2022 대비 크게 개선) 창업자가 고의결권으로 지배하므로 긴 시간 지평에 맞는다. 다만 5배는 여유가 큰 숫자가 아니라서 확신은 중간(3)으로 둔다. 시장 내재 성장(역DCF)이 이미 높은 편이라 기본 시나리오만으로는 모자라고, 대형 고객 확장이 계속되어 강세 경로로 가야 의미 있는 수익이 난다. 이 종목은 멱법칙 후보로서 작게라도 담을 가치가 있다고 판단한다.

*이전 판단 대비: 직전 판단과 같은 입장이며, 새 근거로 바뀐 점은 없다.*

**논거**
- 성장이 크기에 비해 꺾이지 않는다. 종료 ARR 성장은 +30%를 유지하고 있고, FY2026 연간 매출 성장률도 29.6%였다. 가이던스는 세 차례 올랐다. 1번 질문(5년 내 매출 2배)의 답은 코드 계산상 충족이다. [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [C:revenue_growth@FY2026] [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- 대형 고객 확장이 복리의 엔진이다. ARR $1M 이상 고객은 210곳이고 이들의 ARR은 $500 million을 넘었으며 3분기 연속 50% 넘게 성장했다. 성장의 대부분은 신규 로고가 아니라 기존 고객 확장이다. 이는 랜드앤익스팬드가 작동한다는 신호로, 수확체증 구조에 가깝다. [F252] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [F211]
- 멀티프로덕트 채택이 깊어지고 있다. ARR $100K 이상 고객의 96%가 2개 이상, 72%가 3개 이상 제품을 쓰며 3개 이상 비중은 전년 66%에서 올랐다. 제품이 늘수록 이탈하기 어려워지고 고객당 가치가 커진다. 신규 제품이 3분기 연속 순신규 ACV의 20% 넘게를 차지한다. [F253] [F254] [F271] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- 이익률은 오를 여지가 있고 실제로 오르고 있다. FCF 마진은 FY2022 -44.6%에서 FY2026 12.8%로 올라왔고 GAAP 영업이익은 4분기 연속 흑자다. 총이익률은 소프트웨어에 가까운 수준이다. 6번 질문(이익률 상승 여지)과 7번 질문(수익의 FCF 전환)에 모두 긍정적이다. [C:fcf_margin@FY2022] [C:fcf_margin@FY2026] [C:gross_margin@FY2026] [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- 시장은 이 기회를 이미 상당 부분 가격에 넣었지만 10년 뒤 크기까지는 아니다. 역DCF는 FCF 마진 25% 도달 가정에서 연 19.7%의 매출 성장을 요구한다. 가시성(RPO)이 높고 확장 활주로가 길어 이 성장이 불가능한 일은 아니다. 5배 경로는 이 성장이 지속되고 마진이 오르는 강세 쪽에서만 보인다. [C:implied_cagr@m25] [F234] [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm)

**사전 부검**
- 사전 부검: 5배 여유가 얇다. 강세 시나리오에서도 10년 가치는 주가의 5.29배라, 성장률이나 출구 배수가 조금만 낮아져도 레드라인 아래로 내려간다. 기본 시나리오의 연 수익률은 낮고 멀티플 압축이 수익을 깎는다. 이 판단이 틀렸다면 성장이 평범한 소프트웨어 수준으로 식으면서 높은 배수가 정상화된 경우다. [C:implied_cagr@m25] [C:expected_irr] [C:p_loss]
- 사전 부검: 경쟁 심화. Motive가 IPO를 철회하고 $1.3B를 조달해 성장이 가속했다고 주장한다. 하드웨어 보조나 가격 공세 여력이 생기면 신규 확장이 둔화될 수 있다. 다만 승률·가격에 대한 1차 자료가 없고 Samsara의 콜에서도 경쟁 언급이 없었다. [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/) [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- 사전 부검: 기기 원가와 현금 전환이 구조적이라면 마진 상승 가설이 약해진다. FY27 FCF 마진 전망이 한 분기 만에 개선에서 하락으로 뒤집혔고, SBC는 영업현금흐름의 133.3%다. 희석이 연 3%대로 이어지면 주당 가치가 깎인다. 경영진은 일시적이라고 하나 아직 검증되지 않았다. [F257] [F258] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [C:sbc_to_ocf@FY2026] [C:dilution]

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 기본 시나리오 내재가치가 주가보다 낮아 안전마진이 음수라는 것이다. 이 계산은 맞지만, 기본 시나리오 한 점으로 멱법칙 종목을 재는 방식이다. 이 종목의 수익은 분포의 오른쪽 꼬리에서 나오고, 강세 시나리오의 연 수익률은 18.5%다. 손실은 100%로 막혀 있고 상승은 열려 있으므로 확률 가중 기대수익이 낮다는 사실만으로 담지 않을 이유가 되지 않는다. 촉매가 없다는 지적도 내게는 반대다. 창업자가 고의결권으로 지배하기 때문에 분기 압박 없이 10년을 재투자할 수 있다. 성장의 근거는 대형 고객 확장이고, 성장 대부분이 신규 로고가 아닌 기존 고객 확장에서 나온다. [C:irr@bull] [C:mos@ackman] [F237] [F252] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- → 슬레이터: 슬레이터의 가장 강한 논거는 CAC·이탈률·NRR 실적치가 없어 단위경제가 증명되지 않았다는 것이다. 이 공백은 인정한다. 다만 증거를 기다리면 가장 가치 있는 구간을 놓친다. 공개된 가시성은 이미 상당하다. RPO의 약 43%가 12개월 안에 인식되고, ARR $100K 이상 고객은 5분기 연속 늘었으며, 분기 순증 242곳은 최대다. 순현금이 충분해 생존 위험이 없다는 점은 슬레이터 본인도 인정했다. 파산 위험이 없는 곳에서 비중을 작게라도 시작하는 비용은 작고, 기다리는 비용은 비대칭이다. [F234] [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) [F229] [F275] [C:net_cash]
- → 레드팀: 레드팀의 첫 사전 부검은 멀티플 붕괴이고 가장 강하다. 그러나 이는 성장 가설이 아니라 수익률의 경로 소음이다. 성장이 유지되는 동안 높은 배수가 내려오는 것과 성장 자체가 꺾이는 것은 다른 일이다. 기본 시나리오 수익률 분해에서 매출 성장 기여는 +18.1%, 멀티플은 -25.3%로, 압축은 성장 가설이 맞아도 이미 가격에 반영된 부분이다. 성장 가설을 실제로 깨는 신호는 순신규 ARR 감속과 ARR $100K 이상 고객 순증 둔화이며, 내 반증 조건이 바로 이 둘이다. 반면 Motive 조달과 FCF 마진 전망 반전은 경로를 흔드는 것이지 아직 성장 가설을 깨는 증거가 아니다. 승률·가격에 대한 1차 자료가 없고 Q2 콜에도 경쟁 언급이 없었다. [C:implied_cagr@m25] [F210] [F229] [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/) [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)

**인정한 점**
- 애크먼의 지적대로 기본 시나리오 연 수익률이 낮고 안전마진이 음수라 이 판단은 강세 경로에 대한 베팅이다. 5배는 레드라인을 간신히 넘는 값이라 확신을 4로 올리지 않고 3에 둔다.
- 슬레이터와 레드팀이 짚은 FCF 마진 전망 반전과 SBC 차감 FCF 음수는 마진 상승 가설(6번·7번 질문)의 확실성을 낮춘다. 시작 비중은 작아야 하고 Q3 실적에서 순신규 ARR과 FCF 전망을 확인하며 늘려 간다.
- NRR '약 115%'는 목표이지 실적이 아니므로 해자 논거에서 입증된 근거로 쓰지 않는다.


## 슬레이터 — 보류 (2/5)

> 기회의 크기와 지속성은 좋다. ARR $100K 이상 고객이 3,605곳으로 분기 최대인 242곳 순증을 기록했고, 성장 대부분은 기존 고객 확장에서 나온다. 순현금이 13.3억 USD이고 FCF가 흑자라 외부 자본 없이 계획을 실행할 수 있다. 하지만 증거가 아직 가설을 입증하는 수준은 아니다. CAC·이탈률·코호트·NRR 실적치가 없어 단위경제는 '불명'이다. 경영진의 '약 115%'는 목표이지 실적이 아니다. FCF 마진 전망은 한 분기 만에 개선에서 하락으로 뒤집혔다. 경쟁사 Motive는 자본 제약이 풀렸다. 가격 쪽에서는 기본 시나리오 기대 연 수익률이 +4.8%에 그치고, 출구 멀티플 축소(-25.3%)가 매출 성장 기여(+18.1%)를 상당 부분 지운다. 담을 만한 회사이고 파산 위험은 없다. 하지만 이 가격에서는 증거가 쌓일 때까지 기다리는 쪽이 맞다고 본다. 시작 비중을 둔다면 1% 이하이고, 그것도 Q3 실적의 ARR·FCF 전망 확인 뒤다.

*이전 판단 대비: 직전 판단과 같은 입장(보류)이며 확신도도 같다. 새 근거는 없고 같은 근거로 다시 판단했다. 위 must_be_true를 일부 보강했을 뿐이다.*

**논거**
- 규모 있는 고객의 확장이 가속한다. ARR $100K 이상 고객이 5분기 연속 늘어 3,605곳이 됐고, 이번 분기 순증 242곳은 분기 최대다. 평균 ARR도 오르고 있어 시장 천장보다 침투 속도가 문제인 사업으로 보인다. [F211] [F229] [F275] [F281] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- 생존 경로는 확실하다. 차입금이 없고 현금과 투자자산이 있으며, 코드가 계산한 기본 시나리오 현금 경로는 0 아래로 내려가지 않는다. FCF도 흑자라 외부 조달 의존이라는 2022년의 교훈에 해당하지 않는다. [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) [C:net_cash] [C:fcf_margin@FY2026] [F20]
- 다만 단위경제는 증명되지 않았다. CAC 회수기간과 이탈률이 공개되지 않았고, NRR '약 115%'는 핵심 고객 대상 목표이지 실적치가 아니다. 과거 실적치가 없어 추세도 만들 수 없다. 아직 계획인 것과 이미 실적인 것을 구분해야 한다. [S55](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#nrr) [F231] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- 성장은 가시적이지만 완만히 감속한다. 연간 매출 성장률은 FY25 33.3%에서 FY26 29.6%로 내렸다. RPO는 42.9억 USD라 앞으로의 매출 가시성은 높고, FY27 매출 가이던스는 두 번 상향됐다. [C:revenue_growth@FY2025] [C:revenue_growth@FY2026] [F234] [F238] [F259] [F284]
- 가격이 증거 수준을 앞선다. 확률 가중 기대 연 수익률은 +4.8%이고, 현재 가격은 목표 FCF 마진 25% 기준으로 10년간 연 19.7%의 매출 성장을 요구한다. 증거가 가설을 입증하지 못한 상태에서 이 기대를 선반영하는 가격에 크게 담을 이유가 없다. [C:expected_irr] [C:implied_cagr] [C:implied_cagr@m25] [F218]

**사전 부검**
- 사전 부검: 기기·공급망 원가 상승이 일시적이지 않고 구독 마진을 계속 누르면, FCF 마진 25% 도달 가정이 무너진다. 이미 FCF 마진 전망이 한 분기 만에 뒤집혔고 비GAAP 총이익률도 79%에서 76%로 내려간 적이 있다. [F257] [F258] [F282] [F283] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- 사전 부검: Motive가 $1.3B를 조달해 하드웨어 보조와 가격 공세 여력이 생겼다. 승률·가격에 대한 1차 자료가 없어 경쟁 악화는 늦게 확인되며, 그때는 순신규 ARR 둔화로 이미 나타난 뒤일 수 있다. [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/) [S62](https://fintool.com/news/motive-ipo-fleet-management) [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- 사전 부검: SBC가 FCF의 상당 부분을 차지하고 SBC 차감 FCF는 음수다. 희석이 연 3%대로 이어지면 매출이 계획대로 커져도 주당 가치 성장이 그만큼 깎인다. [C:fcf_after_sbc@FY2026] [C:sbc_to_ocf@FY2026] [C:dilution] [C:share_change@FY2026]

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 대형 고객 확장이 복리 엔진이라는 점이고, 이 부분에는 동의한다. 하지만 이 논거는 아직 실적이 아니라 회사 KPI다. 확장이 계속된다는 증명은 NRR 실적치와 이탈률인데 둘 다 공개되지 않았고, CFO가 말한 '약 115%'는 핵심 고객 대상 목표다. 또 앤더슨의 5배 경로는 강세 시나리오 한 가지에만 서 있다. 확률 가중 기대 연 수익률은 +4.8%에 그친다. 이 경로가 성립하려면 FCF 마진이 개선되고 배수가 높게 유지되어야 하는데, FCF 마진 전망은 한 분기 만에 뒤집혔다. 그래서 '담을 가치가 있다'는 결론에는 동의하지만 '지금'이라는 시점에는 동의하지 않는다. 먼저 증거가 쌓여야 한다. [S55](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#nrr) [F231] [C:expected_irr] [F257] [F258]
- → 애크먼: 애크먼은 촉매가 없다는 점을 반대 사유로 든다. 나는 촉매 유무를 기준으로 쓰지 않는다. 창업자가 Class B로 지배하는 구조는 외부 주주가 만들 촉매가 없다는 뜻이지만, 장기 보유에는 오히려 맞는 구조일 수 있다. 내가 보류하는 이유는 촉매가 없어서가 아니라 단위경제 증거가 없어서다. 애크먼이 든 안전마진 음수와 SBC 차감 FCF가 음수라는 점은 인정한다. 다만 이것이 곧 '담지 않는다'는 결론은 아니다. 가격이 증거 수준을 앞선 것이므로, 증거가 쌓이거나 가격이 내려오면 입장이 바뀔 수 있어야 한다. 애크먼의 반증은 가격 조건이라 이 점은 비슷하다. [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) [F237] [C:mos@ackman] [C:fcf_after_sbc@FY2026]
- → 레드팀: 레드팀의 가장 강한 논거는 Motive가 자본을 얻어 가격과 하드웨어 보조 공세를 펼칠 수 있고, 외부에서 초기 징후를 볼 수 없다는 것이다. 이 선행 신호는 비GAAP 총이익률과 ARR $100K 이상 고객 순증으로 잡을 수 있어 모니터링 가치가 있다. 다만 약세 확률이 낮다는 지적에는 부분적으로만 동의한다. 약세 시나리오에서도 Samsara는 차입금이 없고 현금 경로가 0 아래로 내려가지 않아, 이 위험은 생존 문제가 아니라 수익률 문제다. 그래서 내 레드라인(생존 경로)은 건드리지 않고 비중만 줄이는 쪽으로 반영한다. [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/) [F282] [F283] [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) [C:p_loss]

**참이어야 하는 것**
- [on_track] FY27 매출이 가이던스 하단 이상으로 마감한다
- [on_track] FY27 Q3 GAAP 영업이익이 흑자를 유지한다
- [on_track] ARR $100K 이상 고객이 다음 분기에도 계속 늘어 3,800곳을 넘는다
- [at_risk] 다음 분기 ARR이 22억 달러 이상으로 순신규 ARR 둔화가 가속되지 않는다
- [at_risk] ARR $100K 이상 고객 중 3개 이상 제품 사용 비중이 계속 올라 75%에 닿는다

**인정한 점**
- 앤더슨의 지적대로 성장·멀티프로덕트·대형 고객 지표는 모두 개선 방향이고 경쟁사 대비 규모 우위도 보인다. 다만 이는 기회의 크기와 지속성에 대한 증거이고 단위경제의 증거는 아니므로, 결론은 보류에서 바뀌지 않는다.
- 애크먼이 지적한 안전마진 음수와 SBC 차감 FCF 음수는 인정한다. 이 가격에서는 첫 비중을 키울 근거가 없으므로 시작 비중은 이미 낮게 잡은 1% 이하를 유지하고 Q3 실적 확인 뒤로 미룬다.
- 레드팀이 제시한 순신규 ARR 감속과 비GAAP 총이익률 하락은 내 반증 조건과 같은 방향의 선행 신호로 받아들인다. 이 신호가 나오면 보류를 반대로 바꾼다.


## 애크먼 — 반대 (4/5)

> Samsara는 기기를 깔고 구독 소프트웨어를 얹는 사업이라 한 문단으로 설명되고, 고객 확장과 RPO 덕에 매출 가시성도 높다. 하지만 지금 가격에는 안전마진이 없다. 기본 시나리오 내재가치가 주가보다 낮아 안전마진이 음수이고, 기대 수익률은 요구수익률에 한참 못 미친다. 보고 FCF 마진은 올해 오히려 낮아질 전망이며, SBC를 비용으로 치면 FCF는 아직 음수다. 자사주 매입도 없고 창업자가 고의결권 주식으로 지배하므로 내가 격차를 좁힐 촉매도 없다. 좋은 사업이지만 이 가격에서는 담지 않는다.

*이전 판단 대비: 직전 판단과 같은 입장이다. 새 근거로 바뀐 것은 없고, 가격(F218)과 코드 계산 안전마진이 여전히 레드라인에 못 미친다.*

**논거**
- 사업의 질은 좋다. 규모 있는 고객(ARR $100K 이상)이 5분기 연속 늘고 그중 96%가 2개 이상 제품을 쓰며, 순신규 ARR 성장은 기존 고객 확장이 이끈다. 단순하고 가시성 높은 구독 사업이라는 점은 인정한다. 다만 NRR 실적치와 이탈률이 없어 해자는 아직 입증된 것이 아니라 회사 KPI다. [F211] [F253] [F275] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [S55](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#nrr)
- 가격이 문제다. 코드가 계산한 기본 시나리오 내재가치는 현재 주가보다 낮고 안전마진은 음수다. 내 기준(20% 이상)에서 한참 모자란다. [C:intrinsic_value@ackman] [C:mos@ackman] [F218]
- 확률 가중 기대 연 수익률은 약 5%로 할인율에 못 미치고, 손실 확률은 25%다. 기본 시나리오의 수익률 분해에서 매출 성장과 마진 확대가 만든 수익을 출구 멀티플 하락이 거의 다 지운다. 시장이 이미 높은 배수를 지불하고 있다는 뜻이다. [C:expected_irr] [C:p_loss] [C:p_fcf] [C:ev_revenue]
- 현금 창출의 질이 보고 숫자보다 낮다. FY27 FCF 마진은 한 분기 만에 '+100bp 개선'에서 '약 100bp 하락'으로 뒤집혔고(기기·재고·공급망 비용), SBC를 비용으로 치면 FCF는 FY2026에도 음수다. FCF 수익률은 1%대에 그치고 희석은 연 3%를 넘는다. [F257] [F258] [C:fcf_margin@FY2026] [C:fcf_after_sbc@FY2026] [C:fcf_yield] [C:dilution]
- 촉매가 없다. 자사주 매입이 없고 순주식결제는 직원 세금 대납일 뿐이며, 창업자가 고의결권 Class B로 지배해 행동주의가 통할 구조가 아니다. 최근 3개월은 내부자 순매도에 매수 0이다. 격차를 좁힐 행동이 보이지 않으면 싸게 사야 한다는 원칙만 남는다. [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) [F237] [S60](https://www.marketbeat.com/instant-alerts/samsara-nyseiot-hits-new-52-week-low-should-you-sell-2026-02-02/) [F251]

**사전 부검**
- 사전 부검: 내가 틀렸다면 강세 시나리오가 실현된 경우다. 신규 제품과 해외·대형 고객 확장으로 성장이 20%대 중반을 오래 유지하고, 기기 원가 부담이 경영진 말대로 일시적이어서 FCF 마진이 30%까지 오르면 연 수익률이 두 자릿수 후반이 된다. 이 경우 지금 안 사는 비용이 크다. [C:irr@bull] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [F252] [F257]
- 사전 부검: 약세 쪽 꼬리도 두껍다. Motive가 $1.3B를 조달해 하드웨어 보조와 가격 공세 여력이 생겼고, 경쟁 승률·가격에 대한 1차 자료가 없다. 성장이 한 자릿수로 식으면 FCF 범위가 크게 넓어져 안전마진이 훨씬 더 필요하다. [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/) [C:irr@bear] [C:p_loss]
- 사전 부검: 컨센서스가 낡아 시장이 이미 무엇을 기대하는지 정확히 알 수 없다. 가이던스를 세 번 올린 보수적 패턴이 이어지면 매출은 모델보다 빨리 오를 수 있고, 그러면 기본 시나리오의 안전마진 계산이 너무 박할 수 있다. [F238] [F259] [F284] [F217]

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 대형 고객 확장이 복리를 만든다는 것이다. 그 사업의 질은 인정한다. 하지만 그의 찬성은 강세 시나리오 하나에 기대고 있다. 강세 시나리오 10년 가치도 레드라인인 5배를 간신히 넘을 뿐이다(C:upside_10y@anderson). 확률 가중 기대 연 수익률은 +4.8%이고(C:expected_irr), 손실 확률은 25%다(C:p_loss). 주가 아래로 내려가는 기본 시나리오가 55% 확률의 중심이다. 생존자 편향을 피하려면 중심 시나리오로 사야 하는데, 중심 시나리오에서 안전마진이 음수다(C:mos@ackman). 강세 경로에서만 보이는 5배를 근거로 사는 것은 가격 규율이 아니다. 역DCF가 요구하는 성장(C:implied_cagr@m25)에 대한 기저율 표도 없다(계산 경고). 그러니 이 5배는 검증되지 않은 가정이다. [C:upside_10y@anderson] [C:expected_irr] [C:p_loss] [C:mos@ackman] [C:implied_cagr@m25]
- → 슬레이터: 슬레이터는 담을 만한 회사이지만 이 가격에서는 증거가 쌓일 때까지 기다리자고 했다. 가격이 증거를 앞선다는 결론은 나와 같다. 다만 내 결론은 기다리는 것이 아니라 안 사는 것이다. 생존 경로와 순현금은 필요조건일 뿐 가격의 정당화가 아니다. Q3에서 ARR과 FCF 전망이 확인돼도 가격이 그대로면 기본 시나리오 수익률은 그대로다. 기본 시나리오의 연 수익률 분해에서 멀티플 변화가 매출 성장 기여를 상당 부분 지운다(C:expected_irr). 그리고 그가 must_be_true에 올린 것 중 ARR 22억 달러는 스스로 위험(at_risk)이라 표시했다. 그 가정 위에서 시작 비중을 말하는 것은 아직 일러 보인다. [C:expected_irr] [C:mos@ackman] [F209] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- → 레드팀: 레드팀의 FCF 마진 정체 시나리오가 내 판단에서 가장 중요하다. 보고 FCF 마진은 12.8%이고(C:fcf_margin@FY2026), CFO는 올해 마진이 약 100bp 낮아질 것이라고 했다(S56). 한 분기 전 전망은 반대 방향이었다(S57). 기본 시나리오의 마진 상승은 이 가시성 낮은 전망 위에 서 있다. 사전 부검이 말하는 약세 경로(마진 정체, 멀티플 붕괴)가 현실이 되면, 내가 보는 10년 FCF 범위의 하단이 훨씬 낮아진다. 그렇다면 필요한 안전마진은 20%보다 더 커야 한다. 지금은 20%가 아니라 음수다. 즉 레드팀의 부검은 내 판단을 약하게 만들지 않고 더 강하게 만든다. [C:fcf_margin@FY2026] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [S57](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf) [C:mos@ackman] [C:fcf_after_sbc@FY2026]

**인정한 점**
- 앤더슨 인정: 대형 고객 확장과 멀티프로덕트 채택이 실재하고, 성장 가시성(RPO)이 높다. 사업의 질에 대한 반론이 아니라 가격에 대한 반론이다.
- 슬레이터 인정: 순현금과 흑자 FCF로 생존 위험은 없다. 이 사업은 '외부 자본에 의존한다'는 레드라인에 걸리지 않는다. 그래서 나의 반대는 가격과 촉매 부재에서만 나온다.
- 내 1라운드 사전 부검 인정: 가이던스를 세 번 올린 패턴이 이어지면 기본 시나리오가 박할 수 있다. 하지만 FCF 전망이 한 분기 만에 뒤집힌 것과 SBC 차감 FCF가 음수인 점을 감안하면, 상향 여지가 안전마진 음수를 20%까지 메운다고 볼 근거는 없다.
- 입장은 유지한다. 새 근거가 없고, 상대의 논거는 모두 가격이 아니라 사업의 질에 대한 것이었다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Samsara는 차량·장비·현장 운영에 센서, 카메라, 게이트웨이 같은 IoT 기기를 깔고, 그 위의 클라우드 소프트웨어를 구독(ARR)으로 파는 연결 운영 플랫폼이다. 하드웨어를 설치하고 제품을 추가 판매하는 구조다. 최근 FY27 Q2 종료 ARR은 $2,124.7M(+30%)이고, 연간 매출 성장률은 29.6%(C:revenue_growth@FY2026)였다. 총이익률은 76.7%(C:gross_margin@FY2026)로 소프트웨어에 가깝고, 4분기 연속 GAAP 영업흑자다. 규모 있는 고객(ARR $100K 이상 3,605곳)이 빠르게 늘고 멀티프로덕트 채택도 높다. 다만 CAC, 이탈률, 코호트, NRR 실적치가 공개되지 않아 단위경제는 증거로 확정하지 못한다. 경영진의 FY27 FCF 마진 전망이 한 분기 만에 '+100bp 개선'에서 '약 100bp 하락'으로 바뀐 점은 하드웨어와 공급망 비용 부담을 보여 준다. 비상장 경쟁사 Motive는 IPO를 철회하고 $1.3B를 조달했다.

- [unit_economics] 총이익률은 GAAP 77%, 비GAAP 78%로 전년 대비 보합이다(S53). 다만 비GAAP 총이익률은 Q1 FY26 79%에서 Q1 FY27 76%로 내려갔다가 Q2에 78%로 돌아왔다. Q1 서한은 AI 관련 투자로 매출원가 비중이 2%p 올랐다고 밝혔다. CAC, 회수기간, 총·순 이탈률, 코호트는 공개되지 않아 단위경제의 개선·악화를 판정할 근거가 없다. [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf) [F282] [F283] [F247] [S57](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf) [C:gross_margin@FY2026]
- [unit_economics] 경영진은 FY27 FCF 마진이 FY26보다 약 100bp 낮을 것으로 전망했다. 이유는 성장에 따른 IoT 기기 증가, 완충 재고 선구매, 하반기 공급망 비용 상승이며 '일시적'이라고 했다. 한 분기 전 Q1 서한은 100bp 개선을 전망했으므로 방향이 뒤집혔다. 기기 원가가 구독 마진을 누르는 구조적 노출이고, FY26 FCF 마진은 12.8%(C:fcf_margin@FY2026)다. 원가는 매출원가로 서서히 상각되며 반영된다고 한다. [F257] [F258] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [S57](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf) [C:fcf_margin@FY2026]
- [customers] ARR $100K 이상 고객은 Q1 FY26 2,638곳에서 Q2 FY27 3,605곳으로 늘었고 Q2 순증 242곳은 분기 최대다. 해당 고객 ARR은 $1.3B(+38%)다. 이 고객군 평균 ARR은 Q1 FY26 $338K에서 Q1 FY27 $365K로 올랐다. ARR $1M 이상 고객은 210곳(순증 20)이고, 이들의 ARR은 $500M을 넘었으며 3분기 연속 50% 넘게 성장했다. 성장 대부분은 신규 로고가 아니라 기존 고객 확장이어서 랜드앤익스팬드 모델이 작동한다는 신호다. [F275] [F211] [F229] [F212] [F280] [F281] [F252] [S58](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf) [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- [customers] NRR: CFO가 말한 '약 115%'는 핵심 고객(ARR $25,000 이상) 대상 목표치이고 보고된 실적치가 아니다. 과거 분기·연도의 NRR 실적도 어디에도 없어 추세를 만들 수 없다. F231(nrr 1.15, reported)은 목표로 읽어야 한다. 반면 Motive는 NRR이 110% 초과(S-1)이고 ARR $100K 이상 고객은 120% 초과라고 주장하는데, 이는 검증되지 않은 자체 주장이다. 단일 고객 집중은 낮아 10% 이상 매출 고객이 없다. [S55](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#nrr) [F231] [S63](https://www.freightwaves.com/?p=569009) [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/) [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm)
- [industry] 경쟁은 강해지는 중이다. Motive는 2026-09-10 S-1을 철회하고 General Catalyst 주도로 $1.3B 넘게 조달했으며 ARR이 $600M을 넘고 성장률이 30%로 가속했다고 주장한다. 자본 제약이라는 약세 요인이 사라져 하드웨어 보조나 가격 공세 여력이 생긴 셈이다. Geotab은 커넥티드 차량 구독 500만 건과 고객 100,000곳 이상을 밝혔다. Samsara는 Motive 상대 ITC 비침해 판단(2025-09-08)을 받았지만 중재에서는 $30.3M 판정 이익을 얻었다. 승률·가격·할인에 대한 1차 자료는 없고 FY27 Q2 콜에서도 경쟁이나 Motive 언급이 없었다. [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/) [S65](https://www.geotab.com/ie/press-release/5-million-subscriptions/) [S62](https://fintool.com/news/motive-ipo-fleet-management) [F274] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- [runway] 가시성은 높다. RPO는 $4,285.2M이고 이 중 약 43%($1,838.9M)가 12개월 안에 인식된다. 신규 제품은 3분기 연속 순신규 ACV의 20% 넘게 차지했고, 비미국 비중은 순신규 ACV의 18%로 분기 기록 타이다. 유럽 순신규 ACV는 4분기 연속 50% 넘게 성장했다. AI 기능 채택은 두 달 새 4배 넘게 늘었으나 CEO는 에이전트 도입이 아직 초기라고 했다. 재투자 활주로는 넓어 보이지만 신규 제품별 ARR이 공개되지 않아 경영진 설명에 의존한다. [F234] [F235] [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [F255]
- [runway] 성장은 완만하게 둔화하고 있다. 연간 매출 성장률은 FY25 33.3%에서 FY26 29.6%로 내렸고(C:revenue_growth@FY2025, C:revenue_growth@FY2026), 가이던스는 FY27 +26%, Q3 +24%다. ARR 성장은 +30%로 유지되지만 순신규 ARR은 Q4 FY26 $144.8M(+33%)에서 Q2 FY27 $134.1M(+28%)으로 분기 변동이 있다. FY27 매출 가이던스는 3월 $1.965~1.975B에서 9월 $2.043~2.047B까지 두 번 상향됐다. [C:revenue_growth@FY2025] [C:revenue_growth@FY2026] [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf) [F288] [F210] [S59](https://s29.q4cdn.com/853855404/files/doc_financials/2026/q4/Q4-2026-Earnings-Press-Release-FINAL.pdf)
- [unit_economics] 하드웨어 재고와 수익성 질도 사업 구조의 일부다. FY26 DIO는 46.7일(C:dio@FY2026)이고, FY25 재고 증가율이 매출 증가율을 41.7%p 웃돌아 회계 신호(C:inventory_gap)로 잡혔다. 경영진은 하반기 완충 재고 선구매를 인정했고 재고를 '경쟁우위'라고도 표현했다. 한편 SBC는 매출의 19.5%(C:sbc_to_revenue@FY2026)이고 SBC 차감 FCF는 아직 음수(C:fcf_after_sbc@FY2026)여서, 비GAAP 영업이익률 21%만으로 소프트웨어 수준의 경제성을 단정하기 어렵다. [C:dio@FY2026] [C:inventory_gap] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [C:sbc_to_revenue@FY2026] [C:fcf_after_sbc@FY2026] [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- [claimed] ARR $100K 이상 고객의 96%가 2개 이상, 72%가 3개 이상 제품을 쓰고, 이 고객군 수는 5분기 연속 증가했다(2,638 → 3,605). 하드웨어가 현장에 설치되고 여러 제품에 걸쳐 쓰이므로 전환비용이 높을 것으로 추정되지만, 이탈률·가격 인상 후 잔존 기록·실적 NRR이 없어 아직 흔적이 아니라 회사 KPI다. 경영진의 NRR '약 115%'는 핵심 고객 대상 목표치이고 과거 실적치가 없다. [F253] [F254] [F275] [F211] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [S55](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#nrr)
- [claimed] 분기 매출 $508.4M, GAAP 총이익률 77%(전년 보합), GAAP 영업이익 $4.9M으로 흑자를 유지한다. 경쟁사 Motive는 2025년 9개월 매출 $327.3M에 순손실 $138.5M으로 보도됐다(2차 요약). 규모의 이점은 보이나 경쟁사 수치가 2차 자료와 비상장사의 자체 주장이라 점유율·마진 격차로 입증되지는 않는다. [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf) [S62](https://fintool.com/news/motive-ipo-fleet-management) [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/)

### 경영진·자본배분 — mixed

경영진은 가이던스를 세 차례 올렸고 실제 매출도 상향된 가이던스를 넘겨 왔다. 다만 FY27 FCF 마진 전망은 한 분기 만에 +100bp 개선에서 −100bp 악화로 뒤집혔다. 자사주 매입은 없고 SBC에 따른 희석이 계속된다. 창업자는 고의결권 Class B로 지배권을 가지며, 최근 3개월 내부자 매도 $107.38M에 매수는 0이다. DEF 14A는 있지만 보상 지표를 읽지 못해 보상 정렬은 판단할 수 없다. 이 때문에 정렬 등급은 '혼재'(mixed)로 둔다.

- [compensation] DEF 14A(2026-06-01 제출)가 근거 목록에 있지만 보상 연동 지표(매출·FCF·ROIC·주당가치 vs 단기 EPS·조정 EBITDA)와 베스팅 기간을 확인하지 못했다. 근거 없음. [S6](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039492/iot-20260601.htm)
- [insider] 집계 사이트(2차) 기준 최근 3개월 내부자 매도는 약 $107.38M이고 매수는 0이다. CAO 등의 매도 기록이 있다. 내부자 지분은 35.13%다. 고의결권 Class B는 205,332,173주로 창업자가 지배한다. 보유 지분이 크지만 순매도 흐름이어서 정렬 신호가 엇갈린다. [S60](https://www.marketbeat.com/instant-alerts/samsara-nyseiot-hits-new-52-week-low-should-you-sell-2026-02-02/) [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm)
- [guidance] FY27 매출 가이던스를 세 번 올렸다. 2026-03-05 $1.965~1.975B에서 2026-06-04 $2.005~2.013B로, 2026-09-03 $2.043~2.047B(+26%)로 올렸다. Q2 실제 매출 $508.4M은 추정 $483.26M을 웃돌았다. 매출 가이던스는 보수적으로 제시하고 초과 달성하는 패턴이다. 코드의 가이던스 적중률(C:guidance_hit_rate)은 입력에 없다. [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf) [S59](https://s29.q4cdn.com/853855404/files/doc_financials/2026/q4/Q4-2026-Earnings-Press-Release-FINAL.pdf) [S39](https://www.itiger.com/news/2664435814) [F284] [F259] [F238]
- [guidance] FCF 마진 전망은 신뢰를 깎는다. Q1 주주서한은 FY27 조정 FCF 마진이 전년 대비 100bp 개선된다고 했다. Q2 콜에서 CFO는 FY26보다 약 100bp 낮을 것이라고 바꿨다. 이유는 IoT 기기 증가, 완충 재고 선구매, 하반기 공급망 비용이다. 경영진은 이를 일시적이라고 했다. 한 분기 만에 방향이 뒤집혔고 경영진이 말한 대로 일시적인지는 아직 검증되지 않았다. [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [S57](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf) [F257] [F258]
- [dilution] 희석 주식 수는 FY2026에 3.1% 늘었고 연 3.7% 증가로 회계 신호(dilution)에 걸린다. SBC/매출은 FY2026 19.5%로 내려왔지만 SBC/영업현금흐름은 133.3%다. Q2 SBC는 현금흐름표 기준 $96.4M로 전년 $81.1M보다 늘었다. 자사주 매입 프로그램은 없다. [C:share_change@FY2026] [C:dilution] [C:sbc_to_revenue@FY2026] [C:sbc_to_ocf@FY2026] [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf) [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm)
- [dilution] 상반기 주식 발행 6.69M주 중 2.12M주를 세금 $70.4M에 원천징수(순주식결제)했다. Q2 납부액은 $36.0M다. 이는 직원 세금 대납용 현금 유출일 뿐 자사주 매입이 아니어서 희석을 상쇄하지 못한다. [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf) [F251]
- [capital_allocation] 차입금이 없고 현금 및 투자자산이 약 $1,325.7M이다. 순현금은 13.3억 USD다. 자본은 주로 제품 개발과 현금 보유에 쓰였고 눈에 띄는 대형 인수 이력은 근거에 없다. 설비투자는 FY2026 2,877만 USD로 작다. 투자자산 수익률과 M&A 이력은 근거 없음. [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) [C:net_cash] [C:capex@FY2026]
- [capital_allocation] 경쟁사 Motive에 대한 소송에서 중재 판정 이익 $30.3M을 Q1에 인식했다. 이 일회성 이익이 Q1 GAAP 순이익을 부풀렸다. 비GAAP에서는 제외된다. 경영진은 소송을 공격적으로 수행하지만, 상대 Motive가 $1.3B를 조달해 향후 경쟁 대응 비용이 늘 수 있다. [S57](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf) [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf) [S62](https://fintool.com/news/motive-ipo-fleet-management) [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/)

### 회계 품질 — watch

현금흐름과 발생액은 이익보다 오히려 좋아서 숫자 자체를 못 믿을 근거는 없다(영업현금흐름 흑자 전환, 발생액 비율 음수). 다만 GAAP 이익은 SBC가 지배하고, 올해 1분기 순이익은 Motive 중재 일회성 이익으로 부풀려졌다. 그래서 `watch`로 판정한다. 이익은 SBC 차감 FCF(FY2026 약 -1.1억 USD)와 중재 이익 제외 기준으로 봐야 하고, 희석은 연 3.7%라 주당 가치에서 차감해야 한다. 감사의견·감사인 변경·재무제표 정정·특수관계자 거래는 확인하지 못했다. 이 항목들은 '문제 없음'이 아니라 '미확인'이다.

- [concern] sbc_to_revenue: SBC가 매출의 19.5%로 문턱 10%의 약 2배다. 다만 53.4%(FY2022)에서 27.2%, 25.3%, 22.2%, 19.5%로 매년 내려왔고, 투자자 자료의 조정표 기준(FY26 약 21%)과도 방향이 같다. 감소 추세는 긍정적이나 절대 수준이 높아 GAAP 영업이익률이 -3.2%에 머문다. 이익은 SBC를 비용으로 보고 판단해야 한다. [C:sbc_to_revenue@FY2026] [C:sbc_to_revenue@FY2022] [C:sbc_to_revenue@FY2025] [C:operating_margin@FY2026] [F172] [S58](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf)
- [concern] sbc_to_ocf: SBC가 영업현금흐름의 133.3%(FY2025는 211.1%)다. 즉 FCF 흑자는 주식 보상을 현금 비용으로 치지 않은 결과다. SBC 차감 FCF는 FY2026에도 약 -1.1억 USD로 음수다(FY2022 -4.2억에서 개선). 분기 SBC는 FY2027Q1 7,747만에서 Q2 9,638만으로 늘었는데 설명을 찾지 못했다. 주주 몫 현금창출력은 보고 FCF마진 12.8%보다 훨씬 낮게 봐야 한다. [C:sbc_to_ocf@FY2026] [C:sbc_to_ocf@FY2025] [C:fcf_after_sbc@FY2026] [C:fcf_margin@FY2026] [F176] [F177]
- [benign] inventory_gap: FY2025의 41.7%p 격차는 기저효과가 크다. 재고가 FY2023 4,057만에서 FY2024 2,224만으로 줄었다가 FY2025 3,891만으로 원래 수준에 돌아온 것이다. FY2026은 재고 4,819만(약 +24%)이 매출 증가율 29.6%보다 느리다. DIO도 FY2024 32.9일에서 47.6일, 46.7일로 안정됐다. 적체나 매출 부풀리기의 증거는 없다. 다만 경영진이 완충 재고를 선구매했다고 밝혔고 FY2027Q2 재고는 5,703만으로 계속 늘고 있다. 재고 평가손실 여부는 모니터링한다. [C:inventory_gap] [C:dio@FY2024] [C:dio@FY2025] [C:dio@FY2026] [F92] [F93] [F94] [F98] [F100] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi)
- [concern] dilution: 희석 주식 수가 연 3.7% 늘어 문턱 3%를 넘는다. FY2026은 3.1%, FY2027Q1은 전년 동기 대비 +3.5%다. 자사주 매입 프로그램은 없고 순주식결제 세금 납부(Q2 3,600만)가 있을 뿐이다. 이는 희석을 줄이는 매입이 아니라 SBC의 현금 비용이다. 주당 가치는 매년 3~4%씩 깎이는 것으로 모델에 반영해야 한다. [C:dilution] [C:share_change@FY2026] [F251] [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) [S58](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf)
- [watch] Motive 중재 판정 이익 3,030만 USD가 FY2027Q1에 인식됐고 비GAAP에서는 제외됐다. Q1 GAAP 순이익 4,451만 중 큰 부분이 일회성이다. 정상화하면 Q1은 약 1,400만 수준이다. Q2 순이익은 1,624만이다. 일회성이므로 FY2027 순이익이나 PER에 반복되는 것으로 쓰면 안 된다. 10-Q 법률 주석 원문은 확인하지 못했다. [F274] [F109] [F110] [S57](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf) [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- [watch] FY2027Q2 비GAAP 영업이익은 약 1.1억(21%)인데 GAAP 영업이익은 488만이다. 차이의 대부분은 SBC 관련 비용(약 1.0억)이다. 조정은 SBC에 집중되어 있어 성격은 단순하고 반복적이다. 이 조정 때문에 가이던스의 '비GAAP 영업이익률 21%'를 수익성으로 읽으면 과대평가한다. 코드의 non_gaap 신호(GAAP 대비 30% 초과)는 발동하지 않았으나, 흑자 전환 직후라 비율 자체의 의미는 작다. [F243] [F127] [F249] [F245] [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- [info] 매출채권은 FY2026 3.2억(FY2025 2.3억 대비 큰 증가)이고 DSO는 68.4일에서 72.5일로 늘었다. 코드의 receivables_gap(15%p) 문턱은 넘지 않았다. 이연매출은 FY2027Q2 7.3억으로 꾸준히 늘고 RPO도 42.9억이다. 선수금 증가는 매출 품질에 우호적이다. 매출채권 증가율이 매출을 앞서는 추세만 추적한다. 10% 이상 고객은 없어 집중 위험은 낮다. [C:dso@FY2025] [C:dso@FY2026] [F145] [F50] [F234] [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm)
- [watch] FCF 전망이 한 분기 사이에 뒤집혔다. Q1 서한은 FY27 FCF 마진이 전년 대비 100bp 개선이라 했고 Q2 콜은 100bp 낮다고 했다(IoT 기기, 완충 재고, 공급망 비용). 회계 문제는 아니지만 현금흐름 가시성이 낮다는 뜻이다. 비용이 매출원가로 천천히 상각되면 총이익률이 압박받을 수 있다. 비GAAP 총이익률은 79%(Q1 FY26)에서 76%(Q1 FY27)로 이미 내려갔다. [F257] [F258] [F282] [F283] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [S57](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf)
- [info] NRR '약 115%'는 핵심 고객(ARR 25,000 USD 이상) 대상의 경영진 목표이고 보고된 실적치가 아니다. 과거 NRR 실적도 없다. 사실 F231이 'reported'로 저장돼 있어도 실적으로 인용하면 안 된다. 회계 오류는 아니나 KPI 해석에서 오독 위험이 있다. [F231] [S55](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#nrr)
- [watch] 감사의견(계속기업·핵심감사사항), 감사인 변경, 재무제표 정정, 특수관계자 거래를 확인하지 못했다. 코드의 restatement·auditor_change 신호는 발동하지 않았으나 8-K 항목 4.02·4.01이 수집 목록에서 확인되지 않은 것이다. 이 점은 불확실성으로 남기며, `red_flag` 근거로는 쓰지 않는다. 이중 의결권 구조(Class B 2.05억주, 창업자 지배)는 지배구조 위험이다. [S9](https://www.sec.gov/Archives/edgar/data/1642896/000162828026018167/iot-20260131.htm) [S54](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) [F237]
- [info] 코드의 capitalized(자본화 소프트웨어) 신호는 발동하지 않았다. 연구개발비(FY2026 약 3.4억)는 비용으로 처리되고 있다. 설비투자는 FY2026 2,877만으로 매출의 약 1.8%라 비용 자본화로 이익을 키운 흔적은 없다. 영업현금흐름과 순이익의 방향도 일치한다(영업현금흐름이 이익보다 크다). [F162] [F8] [F115] [F105]

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 멀티플 붕괴: 주가 $39.57은 EV/매출 11.9x, P/FCF 91x(C:ev_revenue, C:p_fcf)로 이미 성장이 오래 지속된다는 가정을 담고 있다. 5년 뒤 매출 성장이 한 자릿수~10%대로 식고 FCF 마진이 15% 안팎에 머물면 시장은 이 회사를 성숙 IoT·소프트웨어 배수(출구 P/FCF 15~18x)로 평가한다. 기본 시나리오 수익률 분해에서 멀티플 변화가 이미 연 −25.3%를 차지하는데(C:base_rate@base 표가 없어 성장 지속 확률도 검증되지 않았다), 성장이 약세 시나리오(연 13.8%, C:revenue_cagr@bear)보다 더 나쁘면 −60%는 산술적으로 가능하다. 2026-07-22 회사 뉴스 없이 7.6% 하락하고 최대 낙폭 46.37%를 기록한 이력이 고배수 소프트웨어의 민감도를 보여 준다(S61). [S61](https://www.tikr.com/blog/samsara-stock-fell-nearly-8-in-a-day-its-customers-just-put-dollar-figures-on-why-they-stay) [C:ev_revenue] [C:p_fcf] [C:bear] [S43](https://www.investing.com/equities/samsara)
- (15%) 자본을 얻은 Motive의 가격·하드웨어 보조 공세: Motive는 S-1을 철회하고 $1.3B를 조달했으며 ARR $600M·성장률 30%·$100K 이상 고객 NRR 120% 초과를 주장한다(S64). 자본 제약이 사라져 기기 무상 제공·할인으로 신규 로고와 갱신을 빼앗기 시작하면 Samsara의 순신규 ARR이 줄고, 대응하려면 기기 보조와 영업비용이 늘어 FCF 마진이 목표 25%에 못 간다. Samsara의 단위경제(CAC·이탈률·승률)는 공개되지 않아(S56 콜에도 경쟁 언급 없음) 외부에서 초기 징후를 볼 수 없고, 비GAAP 총이익률은 이미 79%에서 76%로 내려간 적이 있다(F282, F283). 해자는 회사 KPI로만 주장될 뿐 실적 NRR 이력이 없다(S55). [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/) [S62](https://fintool.com/news/motive-ipo-fleet-management) [S55](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#nrr) [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [F282] [F283]
- (15%) FCF 마진 정체와 SBC 희석: 보고 FCF 마진 12.8%(C:fcf_margin@FY2026)는 SBC를 현금 비용으로 치지 않은 수치이며 SBC 차감 FCF는 여전히 음수다(C:fcf_after_sbc@FY2026). 경영진은 한 분기 만에 FY27 FCF 마진 전망을 +100bp 개선에서 약 100bp 하락으로 뒤집었다(S57, S56). 기기 비중과 공급망 비용이 '일시적'이 아니라 구조적이면 마진은 모델의 25%가 아니라 15% 안팎에 머문다. 여기에 희석이 연 3.7%(C:dilution) 이어지고 자사주 매입은 없으며(S54) 내부자는 3개월간 약 $107M을 순매도했다(S60). 주당 FCF는 매출이 성장해도 제자리이고, 투자자는 '조정 이익'의 질을 재평가한다. [C:fcf_margin@FY2026] [C:fcf_after_sbc@FY2026] [S57](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf) [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [C:dilution] [S60](https://www.marketbeat.com/instant-alerts/samsara-nyseiot-hits-new-52-week-low-should-you-sell-2026-02-02/)
- (10%) AI·자율주행·OEM 내장 텔레매틱스에 따른 기능 대체와 고객 확장 한계: 성장의 대부분이 신규 로고가 아니라 기존 고객 확장(S56)이므로, 핵심 고객이 이미 2개 이상 제품을 96% 쓰는 상태(F253)에서 확장 여지가 포화되면 성장은 급격히 둔화한다. 신규 AI 기능 채택은 초기이고 CEO도 에이전트 도입이 초기라고 했다(S56). OEM이 차량에 기본 텔레매틱스·카메라를 내장하거나 Geotab(500만 구독, S65) 같은 대형 경쟁자와 Motive가 번들 가격을 내리면 신규 제품이 순신규 ACV의 20%를 계속 채우지 못한다. 이 경우 ARR $100K 이상 고객 순증이 둔화하는 것이 먼저 보인다. 가이던스는 이미 매출 성장 26%→Q3 24%로 감속을 예고한다(S53). [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [F253] [S65](https://www.geotab.com/ie/press-release/5-million-subscriptions/) [S53](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- 약한 가정 `base.fcf_margin`: 기본 시나리오는 FCF 마진이 FY27 15.3%에서 5년 뒤 25%로 직선 상승한다고 가정하지만, 현재 12.8%(C:fcf_margin@FY2026)이고 경영진은 올해 약 100bp 하락을 전망했다(S56). 한 분기 전 전망이 반대 방향이었다는 점은 가시성이 낮다는 뜻이다. 기기 비용은 매출원가로 서서히 상각되며 반영된다고 했으므로 하방 압력은 후행할 수 있다. 25% 도달은 기기 원가 압박이 일시적이고 Motive 가격 경쟁이 없다는 이중 가정에 의존한다. 이 가정이 15%로 바뀌면 기본 시나리오 수익률은 크게 낮아진다. [C:fcf_margin@FY2026] [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [S57](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf) [C:implied_cagr@m25]
- 약한 가정 `base.exit_multiple`: 출구 P/FCF 30x는 현재 91x(C:p_fcf)에서 크게 내려온 값이지만, 5년 뒤 성장이 연 15%로 식은 기업에 30x를 주는 것이 합리적인지 근거가 없다. 수익률 분해에서 멀티플 변화가 이미 −25.3%이고 민감도 표에서 배수 ×0.75만으로 수익률이 −0.1%가 된다(C:expected_irr 기준 기대 연 수익률 +4.8%). 기저율 표가 없어(계산 경고) 성장 지속 확률도 검증되지 않았다. 약세 시나리오의 18x가 더 현실적인 중심일 수 있다. [C:p_fcf] [C:expected_irr] [C:implied_cagr@m25]
- 약한 가정 `bear.p`: 약세 확률 25%는 Motive의 $1.3B 조달(S64), 컨센서스 부재, 기저율 표 부재, FCF 전망 반전이 겹친 상태에 비해 낮을 수 있다. 약세 시나리오 자체도 성장이 13.8%로 유지되고 FCF 마진 14%, 출구 18x를 가정해 −60%보다 훨씬 덜 나쁜 결과(연 −17.1%, 5년 누적 약 −61% 수준이 아니라 가치 15.52)를 그린다. 약세의 꼬리가 더 두꺼울 수 있다. [S64](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/) [S57](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf) [S56](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) [C:p_loss]

## 검증 (L6)

주장 73개 — supported 64 · unsupported 6 · contradicted 3 · leap 0 · 미검증 0

- [unsupported] 회계 품질: Motive 중재 판정 이익 3,030만 USD가 FY2027Q1에 인식됐고 비GAAP에서는 제외됐다. Q1 GAAP 순이익 4,451만 중 큰 부분이 일회성이다 — 출처 없는 숫자 1.4e+07 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 약세 확률 25%는 Motive의 $1.3B 조달(S64), 컨센서스 부재, 기저율 표 부재, FCF 전망 반전이 겹친 상태에 비해 낮을 수 있다. 약세 시나리오 — 출처 없는 숫자 61% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 출구 P/FCF 30x는 현재 91x(C:p_fcf)에서 크게 내려온 값이지만, 5년 뒤 성장이 연 15%로 식은 기업에 30x를 주는 것이 합리적인지 근거가 없 — 출처 없는 숫자 7500, 0.1% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [contradicted] 앤더슨: 성장이 크기에 비해 꺾이지 않는다. 종료 ARR 성장은 +30%를 유지하고 있고, FY2026 연간 매출 성장률도 29.6%였다. 가이던스는 세 차례 올랐다. 1 — ARR +30%와 FY2026 성장 29.6%는 맞지만, 가이던스 상향은 3월 최초 가이던스 이후 6월·9월 두 번이다(자료: '이후 두 번 상향'). '세 차례'는 틀리다.
- [contradicted] 애크먼: 사전 부검: 컨센서스가 낡아 시장이 이미 무엇을 기대하는지 정확히 알 수 없다. 가이던스를 세 번 올린 보수적 패턴이 이어지면 매출은 모델보다 빨리 오를 수 있고 — 인용한 가이던스 값 세 개(1.97B→2.009B→2.045B)는 최초 가이던스에 두 번 상향한 것이어서 '세 번 올린'은 맞지 않다. 컨센서스가 낡았다는 부분은 자료와 맞는다.
- [contradicted] 경영진·자본배분: FY27 매출 가이던스를 세 번 올렸다. 2026-03-05 $1.965~1.975B에서 2026-06-04 $2.005~2.013B로, 2026-09-03 $2 — 나열한 가이던스는 3월 최초값에서 6월·9월 두 번 올린 것이어서(자료: '이후 두 번 상향') '세 번 올렸다'는 틀리다. 추정 대비 매출 초과는 맞다.
- [unsupported] 레드팀: 멀티플 붕괴: 주가 $39.57은 EV/매출 11.9x, P/FCF 91x(C:ev_revenue, C:p_fcf)로 이미 성장이 오래 지속된다는 가정을 담고 있 — 없는 근거 인용: C:bear
- [unsupported] 회계 품질: 코드의 capitalized(자본화 소프트웨어) 신호는 발동하지 않았다. 연구개발비(FY2026 약 3.4억)는 비용으로 처리되고 있다. 설비투자는 FY2026  — 출처 없는 숫자 1.8% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 앤더슨: 레드팀의 첫 사전 부검은 멀티플 붕괴이고 가장 강하다. 그러나 이는 성장 가설이 아니라 수익률의 경로 소음이다. 성장이 유지되는 동안 높은 배수가 내려오는 것과  — 출처 없는 숫자 18.1% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)

## 사용자 견해 대조 (분석이 끝난 뒤에만 비교한다)

- 사용자 찬성 vs 하네스 팽팽 — 불일치: 하네스 근거를 먼저 읽는다
- 사용자 주장 (하네스가 검증하지 않음): NRR 115% 이상이라는 자료를 찾았다 — 찬성으로 의견을 변경한다

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2026)

| 지표 (키) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| 매출 (revenue) | 4.3억 USD | 6.5억 USD | 9.4억 USD | 12.5억 USD | 16.2억 USD |
| 매출 성장 (revenue_growth) | — | 52.3% | 43.7% | 33.3% | 29.6% |
| 총이익률 (gross_margin) | 70.9% | 72.0% | 73.6% | 76.1% | 76.7% |
| 영업이익률 (operating_margin) | -82.6% | -39.8% | -34.5% | -15.2% | -3.2% |
| 순이익 (net_income) | -3.6억 USD | -2.5억 USD | -2.9억 USD | -1.5억 USD | -912만 USD |
| 영업현금흐름 (ocf) | -1.7억 USD | -1.0억 USD | -1,182만 USD | 1.3억 USD | 2.4억 USD |
| 설비투자 (capex) | 1,935만 USD | 3,324만 USD | 1,095만 USD | 2,018만 USD | 2,877만 USD |
| FCF (fcf) | -1.9억 USD | -1.4억 USD | -2,277만 USD | 1.1억 USD | 2.1억 USD |
| FCF 마진 (fcf_margin) | -44.6% | -20.9% | -2.4% | 8.9% | 12.8% |
| SBC (sbc) | 2.3억 USD | 1.8억 USD | 2.4억 USD | 2.8억 USD | 3.1억 USD |
| SBC/매출 (sbc_to_revenue) | 53.4% | 27.2% | 25.3% | 22.2% | 19.5% |
| SBC/영업현금흐름 (sbc_to_ocf) | — | — | — | 211.1% | 133.3% |
| SBC 차감 FCF (fcf_after_sbc) | -4.2억 USD | -3.1억 USD | -2.6억 USD | -1.7억 USD | -1.1억 USD |
| ROIC (roic) | -522.4% | -35.2% | -41.5% | -22.6% | -2.4% |
| 순현금 (net_cash) | 9.2억 USD | 2.0억 USD | 1.4억 USD | 2.3억 USD | 3.2억 USD |
| 희석 주식 수 (diluted_shares) | 2.8억 | 5.1억 | 5.3억 | 5.6억 | 5.7억 |
| 주식 수 변화 (share_change) | — | 85.3% | 4.0% | 4.0% | 3.1% |
| DSO(일) (dso) | 69.9 | 68.7 | 63.0 | 68.4 | 72.5 |
| DIO(일) (dio) | 97.0 | 81.1 | 32.9 | 47.6 | 46.7 |
| 발생액 비율 (accruals_ratio) | — | -9.1% | -16.4% | -15.2% | -10.7% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, cost_of_revenue, d_and_a, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, gross_profit, income_tax, inventory, inventory_growth, operating_income, pretax_income, receivables, receivables_growth, rnd, total_assets

### 시장 · TTM(FY2027Q2) 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 39.57 USD/share (2026-10-16, F218) |
| 희석 주식 수 (shares) | 5.9억 |
| 시가총액 (market_cap) | 233.6억 USD |
| 순현금 (net_cash) | 13.3억 USD |
| EV (ev) | 220.4억 USD |
| FCF 수익률 (fcf_yield) | 1.1% |
| P/FCF (p_fcf) | 91.45x |
| EV/매출 (ev_revenue) | 11.93x |
| PER (pe) | 258.02x |
| 순부채/EBITDA (net_debt_to_ebitda) | -26.94x |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 19.5% > 10%
- [watch] sbc_to_ocf (C:sbc_to_ocf): SBC/영업현금흐름 — FCF의 상당 부분이 주식 보상 133.3% > 50%
- [watch] inventory_gap (C:inventory_gap): FY2025 재고 증가율 - 매출 증가율 41.7% > 15%
- [watch] dilution (C:dilution): 희석 주식 수 연 3.7% 증가 > 3%

### 역DCF — 현재 가격이 가정하는 것

EV 220.4억 USD를 정당화하려면 매출이 10년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 목표 마진으로 직선 수렴, 할인율 10%, 이후 영구성장 3%.
기본 시나리오 목표 마진 25% 기준: 연 19.7% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 31.2% | C:implied_cagr@m10 |
| 15% | 26.0% | C:implied_cagr@m15 |
| 20% | 22.4% | C:implied_cagr@m20 |
| 25% | 19.7% | C:implied_cagr@m25 |
| 30% | 17.4% | C:implied_cagr@m30 |

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 25% | 30.9억 USD | 13.8% | 14% | 18x | 15.52 | 9.64 | -17.1% |
| 기본 | 55% | 40.0억 USD | 19.8% | 25% | 30x | 50.34 | 31.26 | +4.9% |
| 강세 | 20% | 47.0억 USD | 23.8% | 30% | 40x | 92.49 | 57.43 | +18.5% |

확률 가중: 주당 가치 50.07 · IV 31.09 · 기대 연 수익률 +4.8% (C:expected_irr) · 손실 확률 25% (C:p_loss) · 현재 주가 39.57

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +18.1% · 마진 변화 +13.4% · 멀티플 변화 -25.3% · 주식 수 변화 -3.0% · 현금 축적 +1.6% = +4.8%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -4.6% | +0.1% | +4.0% |
| +0%p | -0.1% | +4.9% | +9.1% |
| +5%p | +4.5% | +9.9% | +14.3% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2027 | 20.5억 USD | 15.3% | 3.1억 USD | 6.1억 | 16.4억 USD |
| FY2028 | 25.0억 USD | 17.7% | 4.4억 USD | 6.3억 | 20.8억 USD |
| FY2029 | 29.7억 USD | 20.1% | 6.0억 USD | 6.5억 | 26.8억 USD |
| FY2030 | 34.8억 USD | 22.6% | 7.8억 USD | 6.6억 | 34.6억 USD |
| FY2031 | 40.0억 USD | 25.0% | 10.0억 USD | 6.8억 | 44.6억 USD |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 19.7% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 19.8% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 23.8% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=5.29x, revenue_5y=2.90x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=13.3억 USD
- 애크먼 case={"from": "base"}: price=39.6, fcf_positive=예, net_debt_to_ebitda=-26.94x, leveraged=아니오, intrinsic_value=31.3, mos=-26.6%

### 계산 경고

- 낡은 컨센서스 — F216: 같은 revenue FY2027 컨센서스 F217가 더 최근 — 제외
- 낡은 컨센서스 — F217: revenue FY2027 컨센서스 2.01e+09가 회사 가이던스 하단 2.043e+09(F238)보다 낮다 — 갱신 전 값으로 보고 제외
- 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-09-08 | [10-Q](https://www.sec.gov/Archives/edgar/data/1642896/000162828026060909/iot-20260801.htm) |  |
| S2 | filing | 2026-09-03 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1642896/000162828026060438/iot-20260903.htm) |  |
| S3 | filing | 2026-07-23 | [8-K](https://www.sec.gov/Archives/edgar/data/1642896/000162828026049446/iot-20260722.htm) |  |
| S4 | filing | 2026-06-09 | [10-Q](https://www.sec.gov/Archives/edgar/data/1642896/000162828026041893/iot-20260502.htm) |  |
| S5 | filing | 2026-06-04 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1642896/000162828026040788/iot-20260604.htm) |  |
| S6 | filing | 2026-06-01 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039492/iot-20260601.htm) |  |
| S7 | filing | 2026-06-01 | [8-K](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039465/iot-20260601.htm) |  |
| S8 | filing | 2026-05-01 | [8-K](https://www.sec.gov/Archives/edgar/data/1642896/000119312526201457/d69859d8k.htm) |  |
| S9 | filing | 2026-03-16 | [10-K](https://www.sec.gov/Archives/edgar/data/1642896/000162828026018167/iot-20260131.htm) |  |
| S10 | filing | 2026-03-05 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1642896/000162828026015170/iot-20260305.htm) |  |
| S11 | filing | 2026-01-06 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1642896/000162828026000886/iot-20260106.htm) |  |
| S12 | filing | 2025-12-09 | [10-Q](https://www.sec.gov/Archives/edgar/data/1642896/000162828025056069/iot-20251101.htm) |  |
| S13 | filing | 2025-12-04 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1642896/000162828025055355/iot-20251204.htm) |  |
| S14 | filing | 2024-03-26 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1642896/000164289624000016/0001642896-24-000016-index.htm) |  |
| S15 | filing | 2025-03-25 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1642896/000164289625000022/0001642896-25-000022-index.htm) |  |
| S16 | filing | 2023-03-21 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1642896/000164289623000016/0001642896-23-000016-index.htm) |  |
| S17 | filing | 2025-06-10 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1642896/000164289625000058/0001642896-25-000058-index.htm) |  |
| S18 | filing | 2025-09-09 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1642896/000164289625000074/0001642896-25-000074-index.htm) |  |
| S20 | news | 2026-07-30 | [Samsara Inc. (IOT) Stock Falls Amid Market Uptick: What Investors Need to Know - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxONVJ5VEJ6TnJ4Y2dvSTJSTmIwT1MydlFuVmFkOXUyR05WbHJtZlYtSFpVQ0xMQXB2U0MtZm5wd0VvbkdTZjdqbzhsWERqT3U5TUNxNXV3RXFtaGV2VnVHUFJLblpzN1d6RnlkaFd1UHJMelJnZXpKVWJWQXhrbjNOWUJYaVpVbmZydTZWb3VlZldEZVh4QW1B?oc=5) | Yahoo Finance |
| S23 | news | 2026-08-19 | [Samsara Launches Fuel Command Center to Help Fleets Control Costs Amid Price Volatility - Business Wire](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNU1QyWk9pdjBfLXZIaXRCVGlwY1kwSFB2ZTBXUHkwczlnWUZpWGpBT3A5bUJBb251dkxTZERBX3ZrdEs5dDBXeXYwYjJ4WGVoRXF1V1BieV9fTExDZVJKbnFMYU9Zd18xUmoyb0ZJdV9KT2hNYUpzbTFPUndnaHBvN2dNWUFqRG5rRWo4OEJpM1VDVmRKeFJhUnp4bXBlZERIUVBBS2VIbjhFemlYT1ZKSXotMmpmejcwQlhxVF8tUC1IRnhCMTZ6bWt2RVBhcTZtS0lPMHhRdUZXMFRL?oc=5) | Business Wire |
| S25 | news | 2026-08-18 | [Samsara Inc. (IOT) Increases Despite Market Slip: Here's What You Need to Know - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxNVzB0bUNFUnRpN1EyR2U4aWJRQ3pMa2FSNDhwRm1iYmJyZGtNRHpxczlCeTBxTzdXNDRCQzFwc1NfMUU3SHRvOUtmV21RVlVPRFJEcEkwM1pIbE9oYjdtS1Rsby1PNlBVZnJVUFVBXzNBQ2ozZHozM1AwaTVnX01NcS14c2JoTG1UZjN0OGt6TnhQd1dFT1haOGNsNk5oUVE?oc=5) | Yahoo Finance |
| S26 | news | 2026-08-13 | [3 Reasons Investors Love Samsara (IOT) - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxQVVdiTU9tcE9KdVkxM1RjZmU2aGYta0lIdUJnajR3aEk2ZXJIbmNaNDRGNzltM1R4Qmg4RHhfTEVHT2lPeU0xUHg3d0RKcjU2cEZSaUd3STFRcnlURGtRUUNYNWVYbXk5R18yU2t0SDhqRVRzekF4YVlJMlVqVjdSai1WZEg5UHNNNGl5dmRnUzB6cjZhbEpDMkdsazFYQQ?oc=5) | Yahoo Finance |
| S27 | news | 2026-08-10 | [Samsara (IOT) Maintains 30% Growth as Margins Improve and AI Risks Stay Low - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxOR1U1Z2xJQTJONFkzVFp4Zm5NSjB1N3BzaVozbjg0RkkyYjhVZ2o2UHh3Q3RTUlJKRmhsWGt1UE1mWTR3NkMycm5lQmlzMFV5VHcyV0ZUcVBWRk1wS1NuSG92aF9UN1VYSUxPSnI3dWRudG1kZ1htRG9lc0lwT1hRMXNXVUtSaGlpOWJmck9fd2pBeGdNdUI5bjM0V1k?oc=5) | Yahoo Finance |
| S28 | news | 2026-08-12 | [Samsara Inc. (IOT) Stock Falls Amid Market Uptick: What Investors Need to Know - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxOSTFzR0ZGc1QxSXlLd1VMT01oQUhqYkx3RnNpd0h3all2NzNLd1Q0LTlkOTVHdGFQZFlDT0NhRFQxUURvTzRIOG8xWGJKdHJaVUdpSXJReGw2M19NZ1c5a3RZbUZaQTd5UkRFMUZtNktRYUNuX1lMQ0FOYUNHeWlWR3RFcWxQQ1hYWnItYmVBZ2ZKaUg5V19F?oc=5) | Yahoo Finance |
| S29 | news | 2026-10-10 | [Samsara Inc. (IOT) stock price, news, quote and history - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9fcllwVmY5NUw5NFpycmFHQ3NkSzlmZTRhYUhEaFdSYlQ5SVBFYTAwQnZXOF9fV1J4TDJrQ1VQX0tJVHU2dVJzX0FmNVRpNGtV?oc=5) | Yahoo Finance Singapore |
| S30 | news | 2026-07-21 | [Samsara (IOT) Beat Q1 Expectations, Is The Stock Still Overvalued? - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxQR0c2bmROLXlZM2tvT0JpaFYyNnBud2dGcnd4OVRpdHlMUFhmUWFOSVJRRTZNRUlxS3E0UnlsVXFYdHJZclEzcXk5VmswMEhmUGhTeElzdUowYUhwejBvdFQyN09FZUtNWVFZTlo3NnRqeWNVVWpKUG5hR2NudFlZVE1idGZ0UXVQWS1NbDNhQjA2RHQzY0lFdjE1Yk16dw?oc=5) | Yahoo Finance |
| S31 | news | 2026-07-23 | [Why Samsara Inc. (IOT) Dipped More Than Broader Market Today - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxPQUpWajJYRmtVSTRzRVJOR1hsaGtzZHB1Uy1ISWFlVFhtS1pleHp1aTVJaDFneHFhWkRubDVUbVBOZ0RFS29rc3pNY1hTdkhCa0l1bTdrUFpaZGR2eFlvWkpQREJ0T3MyTzJaYkZhT3hxNW9aWkJnNmhnQTh4eTVpUUdpN0pYNXYwb2lpU256U0NjaHZJcVE?oc=5) | Yahoo Finance |
| S32 | news | 2026-09-04 | [Samsara Q2 Earnings Surpass Estimates, Revenues Rise Y/Y - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxOZ0F3dmIydG4ySEpZN0p1elFuTGY3c09acGRkYnlacUtvZlNPRXI3YVRLSW5oSktzaDZhc2ktMlFKeTk1Q0xlblAzanhCZ19aWmRSU2lTcEpDcjJueDFTd0I2ZDk4b2tiRXhOTVhNM0t2VXp3ODNsXzVsQ0gzTVB4TEtMNmZVRkdXU29yZWg5U0RyQ25KWXVwSlVkRFFBY3FOVFB2VQ?oc=5) | Yahoo Finance |
| S33 | news | 2026-08-25 | [Samsara Inc. (IOT) Stock Falls Amid Market Uptick: What Investors Need to Know - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxPM1I3ZDZNZ1RwVjFncHNiT2prMHcwMEMyVlBBZmJmYjh0LUdtWTNncFduQTBPRU56QUpFUkh4a1hZRVlINU5JUElQQ3lRNE4zZlZ6VVUzSGU2ZDNSUHpVQ3Y0eFlwTDJldlJiN0tJZlktenZFWG5nVGg0aEJselRIRTJnSVNmaVlqTFlkWFljRy1MN1hlMFV3?oc=5) | Yahoo Finance |
| S34 | news | 2026-08-06 | [Samsara Inc. (IOT) Registers a Bigger Fall Than the Market: Important Facts to Note - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPUWF3amIzVFlLbkxCZE5aSHVOdmZnTkdpZDF0WmRWTkFLWXNrWkM0dzRzOG91eWliY01UR2R2NzlnUG1jS18xX2s3MlZVODhDU2hKNTg4bDNGMjltWFZsMDB1Rm5uUXZpMTN5a3FQNjZmYzMzQWNBZ2tvY3BKci1ZMzBTQjZfdVVCZS1qZ1dwVUg4QTlCRkhhQW5oWEpudw?oc=5) | Yahoo Finance |
| S35 | news | 2026-08-26 | [Is Samsara (IOT) Undervalued On Its Fuel Command Center Launch? - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxONGJldFA4MHJOWWhNLW9jM003RlNEclozcFhWNXJ2N191QTgyRURDdlAwdWlwUFgtZnlPWlk1c0RENFlpTHFNZGd3OEhXRXRwdHowMWRJR09tUEN4V0pRMkdmSkk5T2RpWGNINS1mQXBzOWNNdjVVZFU1UHJzNHN2RWNPMmY4REY0VjNwcHZ1NGxrTnlJQmJtWURnanMxWVZ6QXlN?oc=5) | Yahoo Finance |
| S36 | news | 2026-07-29 | [Atlassian, ServiceNow, and Samsara Shares Are Soaring, What You Need To Know - Yahoo Finance](https://news.google.com/rss/articles/CBMirAFBVV95cUxPWVNYdFotZmZKSWRIV05oM01XdG82cjctTlZFWUZpSUZ0N21GM2MtZ3BqNDJBMkx5SXZOc0FFa05faTNoSldYZWFTX3FEbU5rYjE0TVNwakxfME00a3hQSFNXaWlEcGxuMUdoa1pXbkRyVzhyenQ4elhOWTBRTWtsNWNkQ09RbWFqUTQ0WnZjcGo2cVB4UGRkeEEyeUpEcllzc056ZjBiUzVwRkRB?oc=5) | Yahoo Finance |
| S37 | news | 2026-07-21 | [Can Samsara (IOT) Justify Its Price After A 46% Gain? - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNNVNuN3JibFZMRWxsMjVMeVlVcU9kM3I2YWVrUnBoNGRaczZIaE5OV2VKWHRlakhNOXRSYmx5bTJLZDRqcURrSWVLTi00TTBmWG0zQnZiUi0xdHRBQjVSYm5PbDFyNUNWU3I1ejFSZEdtcktrVHRDRXlRUUl2dFgyU0pBcGRXZGJRN2p4bGcwQXJCT2NPUEowRg?oc=5) | Yahoo Finance |
| S38 | news | 2026-08-04 | [Samsara (IOT) Following Its Connected Operations Story With Fair Value In Focus - Yahoo Finance](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQeVdGTFZZdlRYVU9QTk1RTE8wSzZCaTh0NGE4bnFKd3N5QW9ScW5xb2d3a1pOazVoejNNOUV5RS1rRjVfNWdiY2RySERiT3dsRkM5VGh6ZU5ob1BCSG9sTnhkQm0zWkZPWWhUbUY3ZWZpbTItYWZrbWFKdGdUWUNNMG94UjdONDlRMlJ4b2V1dmwyQS1lZTJacml1a2VEWXh0UzczZlRUTDRTSzA?oc=5) | Yahoo Finance |
| S39 | data | 2026-09-04 | [Samsara Analysts Boost Their Forecasts After Strong Q2 Earnings](https://www.itiger.com/news/2664435814) | 보도. IOT 주가 2026-09-04(금) 장중 $40.29, +4%. FY27 Q2 매출 $508.44M(추정 $483.26M), EPS $0.20(추정 $0.16). 목표가 상향: BTIG 54, Guggenheim 51, KeyBanc 55, TD Cowen 53, RBC 55, Wells Fargo 58, BMO 54, BofA 55 (모두 매수 의견). 공식 종가가 아니라 기사 속 장중가. |
| S40 | news | 2026-09-03 | [Samsara Reports Second Quarter Fiscal Year 2027 Financial Results (Quartr·Zacks·Benzinga 등 2차 요약)](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) | 보도(2차 요약, 원문은 403으로 열지 못함). 종료 ARR 약 $2.125B(+30% YoY), 순신규 ARR $134.1M(+28%), ARR $100K 이상 고객 3,605곳(해당 고객 ARR $1.3B, +38%). 가이던스: FY27 Q3 매출 $514~516M, FY27 매출 $2.043~2.047B, 비GAAP 영업이익률 Q3·FY 모두 21%. 직전 FY27 가이던스는 매출 $2.005~2.013B, 비GAAP EPS $0.70~0.72. |
| S41 | data | 2026-08-01 | [Samsara Inc. (IOT) Stock Forecast — TickFlow 컨센서스 (2026-08-01 기준)](https://tickflow.io/stock/IOT/forecast) | FY27(2027-01-31 종료) 매출 컨센서스 평균 $1.97B(저 $1.95B~고 $1.98B). Q2 실적·가이던스 상향 이전 값이라 낡았다. FY28은 분기 합계 약 $2.7B로 읽히나 명확한 연간 컨센서스는 못 찾았다. |
| S42 | data | 2026-09-03 | [Earnings Whispers — IOT FY2027 가이던스·컨센서스](https://earningswhispers.com/epsdetails/IOT/202607) | 보도성 집계. Q2 발표 전 FY27(2027-01 종료) 매출 컨센서스 약 $2.01B. 상향 후 가이던스 $2.043~2.047B. |
| S43 | data | 2026-08-10 | [Investing.com — Samsara Inc (IOT) 시세 스냅샷](https://www.investing.com/equities/samsara) | 종가 39.34(-2.43%). 52주 범위 약 $23.38~47.47. 12개월 평균 목표가 44.31, 컨센서스 '매수'. Piper Sandler 하향(2026-08-10)이 표에 있음. 2차 집계 페이지라 시차가 있을 수 있다. |
| S44 | data | 2026-10-16 | [Yahoo Finance IOT historical prices](https://finance.yahoo.com/quote/IOT/history/) | 2026-10-16 종가 39.57 USD |
| S45 | news | 2026-10-15 | [Samsara Tracking Label: The Best Inventions of 2026 - Time Magazine](https://news.google.com/rss/articles/CBMifEFVX3lxTE1pdFBsQ2V5MWM4Z2k1MkcxbG81SFBMSUlFWUhId1lMZ0tRWi1EdFYwbElDT0dRbExjVUw2UlU5U0x5SVBsRE5odTdyc29fakhiTkJYRDNEeTZkOEdtclJYbTJGUW9VazRHaTRDMlBXb20yUmhNTU1ZaG1KUFo?oc=5) | Time Magazine |
| S46 | news | 2026-09-07 | [Samsara Fleet Management: Features, Fees, Support 2026 - Tech.co](https://news.google.com/rss/articles/CBMickFVX3lxTFBJdFdIVm0xTHE3dzFwTHMxSmtndkUzVmkyeFk4YVk0N0FWSTFZVDNwb1VpZHdkZVVEaHY1VS1ieGpXd1pybjl5emNaWm9tbjhOVUxoMDEyRVJiZk5zUTFua1E2c2M5T2djcnd6MzdtSzhCQQ?oc=5) | Tech.co |
| S47 | news | 2026-10-07 | [Samsara Fleet Management Review and Pricing - Business.com](https://news.google.com/rss/articles/CBMiU0FVX3lxTE13NlVyUDVSYk9GWTkwMU04T3k2VG5HNnVkUXhpMVRSa0ViWElfTEdyYTAtckRPWTRfY2VVMGZjS2psWXhHWm1zS2pOMFZndFh5eTZz?oc=5) | Business.com |
| S48 | news | 2026-08-27 | [Why this company ditched tech blue for construction yellow in its new logo - Fast Company](https://news.google.com/rss/articles/CBMickFVX3lxTE1IMmZBNU45dy1QUEwxLTZJWndoYmw0ZFo4dXJaZFFXdUstZ2lTb3BaQlp2VTNhUGJZVmJpZ3ctS3doUjFidWZzWDVvM1RLejBlMFhRQWo1TzJORTJRUlJqWVlIdFB5TlVMc2QzTTBOQzl6dw?oc=5) | Fast Company |
| S49 | news | 2026-08-10 | [Samsara’s Tiny Tracker Offers 45-Day Visibility for Any Shipment - FreightWaves](https://news.google.com/rss/articles/CBMingFBVV95cUxOQ3FXeDYxTXQweTN3X0xpZ2kwakR3b0pTdjVndFNTODFxYXlnU2plVlZWa3VKeEZWcDg4eUpfX3plU1hhc3B6QS1UTzRLdXpjenFWX2NESnpVa3BuLUxTdVRlNlBpbXpqMTRDSDAwUVNwUUJ3dG5Zb1hYcWRETHN5bWl2QkZUb2s4ZVRnbUNOZnFPREpnbGhhalpXcEFDZw?oc=5) | FreightWaves |
| S50 | call | 2026-09-03 | [Samsara (IOT) Q2 2027 earnings summary — Quartr 이벤트 페이지](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw) | FY27 Q2(2026-08-01 종료) 어닝콜의 2차 요약 페이지. 트랜스크립트 원문은 열지 못했다. 보도(2차): 종료 ARR 약 $2.125B(+30% YoY), 분기 매출 $508.4M, GAAP EPS $0.03(4분기 연속 GAAP 흑자). ARR $100K 이상 고객 순증 242곳, ARR $1M 이상 고객 순증 20곳(둘 다 분기 최대로 소개). 경영진은 FY27 FCF 마진이 FY26보다 약 100bp 낮을 것이라 했고 이유로 IoT 기기 투자 확대와 공급망 비용을 들었다. 가이던스: FY27 매출 $2.043~2.047B, FY27 Q3 매출 $514~516M. |
| S51 | call | 2026-09-03 | [Stock Taper — IOT 어닝콜 요약 (Q2 FY2027 콜 트랜스크립트 기반이라고 표기)](https://www.stocktaper.com/earningsCallSummary/IOT) | 보도(2차 요약). 콜 트랜스크립트를 요약했다고 표기한 사이트이고 본문은 열지 못했다. 단독 근거로 쓰지 말고 S50·S40과 함께 교차 확인용으로만 쓴다. |
| S52 | call | 2026-09-03 | [Samsara Q2 FY2027 earnings call transcript (2026-09-03)](https://www.tradingkey.com/news/transcripts/262150876-tradingkey) | CFO Dominic Phillips: 멀티프로덕트 도입이 핵심 고객 대상 목표 달러 기준 순매출유지율(NRR) 약 115% 달성에 기여 (준비 발언). Q&A에서 'target net retention rate of 115%' 유지 언급. '이상'이 아니라 '약 115%', 핵심 고객 기준 |
| S53 | filing | 2026-09-03 | [Samsara Reports Second Quarter Fiscal Year 2027 Financial Results (press release PDF)](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf) | Q2 FY27(2026-08-01 종료) 실적 보도자료 원문(8-K 첨부). 매출 $508.4M(+30% YoY, 고정환율 +29%), 상반기 매출 $987.3M(+30%). 총이익률 GAAP 77%·비GAAP 78%, 둘 다 전년 대비 보합. GAAP 영업이익 $4.9M(1%) vs 전년 −$26.6M(−7%), 비GAAP 영업이익 $106.0M(21%) vs $59.7M(15%) — GAAP 흑자 4분기 연속. 순이익 $16.2M, GAAP EPS $0.03, 비GAAP EPS $0.20. 영업현금흐름 $73.5M(14%), FCF $64.7M(13%), 상반기 FCF $137.9M(14%). SBC(현금흐름표) $96.4M vs 전년 $81.1M, SBC 관련 비용 합계 $101.1M vs $86.3M, 상반기 $184.9M vs $170.6M. 상반기 실적에는 Motive Technologies 상대 중재 판정 이익 $30.3M(Q1 FY27 인식)이 들어 있고 비GAAP에서는 제외. 순주식결제 세금 납부 Q2 $36.0M — 자사주 매입이 아니다(자사주 매입 프로그램 언급 없음). 가이던스(2026-09-03): FY27 매출 $2.043~2.047B(+26%), 비GAAP 영업이익률 21%, 비GAAP EPS $0.76~0.78; Q3 FY27 매출 $514~516M(+24%, 고정환율 +23~24%), 비GAAP 영업이익률 21%, 비GAAP EPS $0.18~0.19, GAAP 흑자 예상. FY27 매출 가이던스 상향 이력: 2026-03-05 $1.965~1.975B(21~22%) → 2026-06-04 $2.005~2.013B(24%) → 2026-09-03 $2.043~2.047B(26%). 가이던스 사실은 같은 값의 2차 요약(S40)보다 1차 자료를 우선하도록 이 문서를 출처로 다시 넣었다. |
| S54 | filing | 2026-09-08 | [Samsara Inc. Form 10-Q for the quarter ended August 1, 2026 — 재무상태표·RPO·주식 수 상세](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm) | S1과 같은 10-Q. 2026-08-01 재무상태표: 현금및현금성자산 $291.4M, 단기 투자자산 $537.5M, 장기 투자자산 $496.8M, 합계 약 $1,325.7M. 차입금 항목 없음. 기존 순현금 2.9억 USD는 현금및현금성자산만 센 값이었다. 잔여이행의무(RPO) $4,285.2M, 그중 약 43%($1,838.9M)가 12개월 안에 인식. 매출·매출채권의 10% 이상을 차지하는 고객 없음. 표지 기준 2026-09-01 발행주식 Class A 380,273,036주, Class B(고의결권, 창업자 지배) 205,332,173주. 상반기 주식 발행 6.69M주, 그중 2.12M주를 세금 $70.4M에 원천징수(순주식결제). 자사주 매입 프로그램 없음. Motive 중재 판정의 법률 주석 원문은 확인하지 못했다. |
| S55 | call | 2026-09-03 | [Samsara Q2 FY2027 earnings call transcript — CFO NRR 발언 원문](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#nrr) | S52와 같은 전사본(2차 전사 사이트)의 NRR 발언 부분. CFO Dominic Phillips의 원문: "our target dollar-based net retention rate of approximately 115% for core customers" — 멀티프로덕트 도입이 이 목표 달성을 "helped us achieve"했다고 말했다. 즉 보고된 실적치가 아니라 '약 115%'라는 경영진 목표이고, '115% 이상'도 아니다. 핵심 고객(core customers)은 ARR $25,000 이상 고객(Q1 FY27 주주서한 정의). Q1 FY27 주주서한도 "our FY27 target dollar-based net retention rate of approximately 115% for core customers"로 같은 틀. Q2 콜·Q1 서한·Q1 투자자 자료 어디에도 과거 분기·연도의 NRR 실적치가 없어 추세를 만들 수 없다. 기존 사실 F231(nrr 1.15, basis reported)은 실적이 아니라 목표치로 읽어야 한다. |
| S56 | call | 2026-09-03 | [Samsara Q2 FY2027 earnings call transcript — 성장 KPI·FCF 전망 발언](https://www.tradingkey.com/news/transcripts/262150876-tradingkey#kpi) | S52와 같은 전사본(2차 전사 사이트)의 KPI·전망 부분. ARR $2,124.7M(+30%), 순신규 ARR $134.1M(+28%), 최근 12개월 순신규 ARR $485M(고정환율 +27%). ARR $100K 이상 고객 3,605곳(분기 순증 242, 최대), 해당 ARR $1.3B(+38%). ARR $1M 이상 고객 210곳(순증 20, 최대). $1M 이상 고객 ARR이 "surpassed $500 million", 3분기 연속 50% 넘게 성장, 성장 대부분이 신규 로고가 아닌 기존 고객 확장. $100K 이상 고객의 96%가 2개 이상, 72%가 3개 이상 제품 사용. 신규 제품(emerging products)이 3분기 연속 "more than 20% of net new ACV". "18% of net new ACV came from non-U.S. geographies, tied for a quarterly record", 유럽 순신규 ACV 4분기 연속 50% 넘게 성장, 멕시코 가속. 공공부문 순신규 ACV 비중 역대 두 번째. 일부 신규 AI 기능 채택 두 달 새 4배 넘게 증가(1,000곳 이상), CEO는 에이전트 실제 도입이 아직 초기라고 말함. CFO의 FCF 전망: "We now expect free cash flow margin to be approximately 100 basis points lower than FY '26." 이유는 성장에 따른 IoT 기기 증가, 완충 재고 선구매, 하반기 공급망 비용 상승. "we expect this to be temporary." 한 분기 전 Q1 주주서한(S904)의 '전년 대비 100bp 개선'에서 방향이 뒤집혔다(약 200bp 변화). 원가 상승은 "come gradually as costs amortize into COGS". 연료비가 일부 달에 전년 대비 거의 40% 올라 연료 분석 수요 증가. 콜에서 경쟁·승률·가격·Motive 언급 없음(재고가 "a competitive advantage"라는 말만). |
| S57 | conference | 2026-06-04 | [Samsara Q1 FY27 Shareholder Letter](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf) | Q1 FY27(2026-05-02 종료) 주주서한. ARR 약 $2.0B(+30%), 순신규 ARR $101M(+30%, 고정환율 +27%). ARR $100K 이상 고객 3,363곳(분기 +169), $1M 이상 190곳(+15). 멀티프로덕트: $100K 이상 고객 96%·핵심 고객 92%가 2개 이상(전년 95%·91%), 70%·54%가 3개 이상(전년 66%·51%). 핵심 고객 = ARR $25,000 이상. NRR 문구: "our FY27 target dollar-based net retention rate of approximately 115% for core customers"(목표, 실적치 아님). FCF 전망: "We expect adjusted free cash flow margin for full-year FY27 to improve 100 bps year-over-year." 매출원가 비중이 "to support AI-related investments" 2%p 상승. Motive Technologies 상대 중재 판정 $30.3M(계약 위반·사기·불공정 경쟁·허위 광고)을 Q1에 인식 — Q1 GAAP 순이익 $44.5M(F109)이 이 일회성 이익으로 부풀려졌다. 가이던스(2026-06-04): FY27 매출 $2.005~2.013B(+24%), 비GAAP 영업이익률 20%, 비GAAP EPS $0.70~0.72. FY27 희석 가중평균 주식 수 약 5.94억주 예상(Q2 보도자료와 함께 인용됨). |
| S58 | conference | 2026-06-04 | [Samsara Q1 FY27 Investor Presentation](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf) | Q1 FY27 투자자 자료. ARR $100K 이상 고객 수 5분기: 2,638(Q1 FY26) → 2,771 → 2,990 → 3,194 → 3,363(Q1 FY27). $100K 이상 고객 평균 ARR $338K(Q1 FY26) → $365K(Q1 FY27). 비GAAP 총이익률 79%(Q1 FY26) → 76%(Q1 FY27). 희석 가중평균 주식 수 534.9M(FY24)·556.3M(FY25)·573.5M(FY26), 567.7M(Q1 FY26)·587.7M(Q1 FY27, +3.5%). 조정 내역표 기준 SBC/매출은 약 27%(FY24)·24%(FY25)·21%(FY26), 약 23%(Q1 FY26)·17%(Q1 FY27) — 하네스의 현금흐름표 SBC 기준(FY26 19.5%)과 측정 기준이 다르다. NRR은 정의만 있고 과거 수치는 없다. |
| S59 | filing | 2026-03-05 | [Samsara Reports Fourth Quarter and Fiscal Year 2026 Financial Results (press release PDF)](https://s29.q4cdn.com/853855404/files/doc_financials/2026/q4/Q4-2026-Earnings-Press-Release-FINAL.pdf) | Q4 FY26(2026-01-31 종료) 보도자료. Q4 매출 $444.3M(+28%), ARR $1,889.9M(+30%), 순신규 ARR $144.8M(+33%). FY26 매출 $1,618.6M(+30%), FCF $207.4M(13%), GAAP 영업이익률 −3%. 최초 FY27 가이던스(2026-03-05): 매출 $1.965~1.975B(+21~22%), 비GAAP 영업이익률 19%, 비GAAP EPS $0.65~0.69. 이후 두 번 상향(6월·9월). |
| S60 | data | 2026-10-16 | [Samsara (NYSE:IOT) Hits New 52-Week Low - Should You Sell? — MarketBeat (페이지 데이터 2026-10-16 기준)](https://www.marketbeat.com/instant-alerts/samsara-nyseiot-hits-new-52-week-low-should-you-sell-2026-02-02/) | 2차(집계 사이트). 기사 제목·URL은 2026-02-02 것이지만 페이지 데이터는 2026-10-16 기준. 내부자 매매: 최근 3개월(~2026-10-16) 매도 약 $107.38M, 매수 0. 9월 하순·10월 중순 CAO 등 매도 기록. 내부자 지분 35.13%, 기관 96.02%(집계치). 애널리스트: Moderate Buy(강력매수 2·매수 14·보유 6·매도 0), 평균 목표가 $51.68(최고 $58·최저 $45, 22명). 주가 $39.54, 시가총액 $23.15B, 52주 범위 $23.38~$47.47, 2026년 시초 $35.43. 자사주 매입 없음. |
| S61 | news | 2026-07-23 | [Samsara Stock Fell Nearly 8% in a Day. Its Customers Just Put Dollar Figures on Why They Stay — TIKR](https://www.tikr.com/blog/samsara-stock-fell-nearly-8-in-a-day-its-customers-just-put-dollar-figures-on-why-they-stay) | 2차. 게시일은 2026년 7월 하순(정확한 날짜 미확인, 7-22 하락 직후). 2026-07-22 회사 뉴스 없이 7.6% 하락해 $33.33(고배수 소프트웨어 매도), 당시 NTM EV/EBITDA 38.8x·선행 PER 43.7x(2025년 8월 선행 EV/EBITDA 81.0x). 최대 낙폭 46.37%(2026-02-05). 동종 선행 EBITDA 배수: Trimble 약 10.8x, Karooooo 약 11.4x(날짜 미표기). 2026년 6월 투자자의 날 고객 ROI: Primoris(카메라 약 8,000대) 사고 42% 감소·연 약 $5M 절감, Performance Food Group은 예산 잡은 $20M 보험료 인상의 절반만 필요. Morgan Stanley Equal Weight(2026-07-21), Guggenheim 매수로 커버 개시(2026-07-23). Q2 실적 전 자료. |
| S62 | news | 2025-12-23 | [Motive IPO: fleet management S-1 summary — Fintool](https://fintool.com/news/motive-ipo-fleet-management) | 2차(S-1 요약, S-1 원문 https://www.sec.gov/Archives/edgar/data/1646681/000162828025058773/motive-sx1.htm 은 직접 확인하지 못함). 경쟁사 Motive가 약 2025-12-23 S-1 공개 제출: 2025년 9개월 매출 $327.3M(+22%), 2025년 3분기 매출 $115.8M(+23%), 9개월 순손실 $138.5M(전년 $113.9M), 고객 약 100,000곳, 직원 4,508명. 소송: Samsara가 2024년 1월 Motive를 영업비밀·특허·가짜 계정으로 제소하고 ITC에 제소, 2025-09-08 ITC 판사가 비침해 판단·주장 청구항 9개 중 8개 무효. 델라웨어 사기·허위광고 소송은 진행 중. Samsara IPO 공모가 $23(2021년 12월). |
| S63 | news | 2025-12-26 | [Motive S-1 coverage — FreightWaves](https://www.freightwaves.com/?p=569009) | 2차(보도). Motive S-1 기준: 순달러유지율 "exceeds 110%", 핵심 고객 약 89%가 2개 이상 제품 사용, ARR 약 30%가 트럭·물류, 건설·현장 서비스·대중교통에서 더 빠르게 성장. |
| S64 | news | 2026-09-10 | [Motive lands $1.3B from General Catalyst, pulls its IPO filing — Dealroom](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/) | 2차(보도, 회사 주장). 2026-09-10 발표: Motive가 S-1을 철회하고 General Catalyst 주도 성장 지분 투자로 $1.3B 넘게 조달, 기업가치 비공개. Motive 주장: ARR $600M 돌파, 성장률 30%로 "accelerated", ARR $100K 이상 고객 ARR 약 60% 성장, 해당 고객 NRR 120% 초과. 자본 제약이라는 약세 시나리오가 사라지고 하드웨어 보조·가격 공세 여력이 생겼다는 의미. 비상장사 자체 발표라 검증되지 않은 수치. |
| S65 | news | 2025-09-04 | [Geotab surpasses 5 million connected vehicle subscriptions — Geotab press release](https://www.geotab.com/ie/press-release/5-million-subscriptions/) | 경쟁사 자체 발표(6개월 넘은 자료). Geotab 커넥티드 차량 구독 500만 돌파, 고객 100,000곳 이상, 연 R&D $150M 이상, 2년마다 약 100만 구독 추가. Lytx·Netradyne·Verizon Connect의 최신 수치는 찾지 못함. |

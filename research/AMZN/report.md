# Amazon (AMZN) 리서치 보고서 — 기준일 2026-10-18

**찬성 우세** — 찬성 2 · 반대 1 · 보류 0 · 확신 가중 점수 +0.13 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장 내재: 매출 10년 연 13.8% (FCF 마진 13% 수렴 가정) · 기본 시나리오: 5년 연 12.3%
- 시장이 반영한 것: 현재 주가는 FCF 마진이 15%까지 올라간다면 10년간 연 12.1% 매출 성장을 가정한다(C:implied_cagr@m15). 컨센서스 매출(FY2026 약 8,289억 달러)은 우리 매출 경로와 거의 같고, 8월 시점 capex 컨센서스(약 2,061억 달러)는 2,200억 달러 가이던스 상향 전의 값이다.
- 우리가 다르게 보는 점: 매출에서는 컨센서스와 다르지 않다. 다른 점은 현금 전환이다. 우리는 2030년 FCF 마진을 13%로 보고, 시장이 요구하는 15%보다 낮다. 2026년 capex가 약 2,200억 달러로 올랐고 메모리 가격 상승이 주된 이유라서, 같은 매출 성장에서 필요한 자본이 컨센서스 추정보다 크다. 회사 정의 TTM FCF는 이미 -76.0억 달러다.
- 왜 우리가 맞는가: 경영진이 FCF는 데이터센터 가동·수익화 전까지 역풍이라고 밝혔고, 차입금은 FY2025 656.5억에서 FY2026Q2 1,288.9억 달러로 두 배가 됐다. capex가 가이던스 상향으로 계속 올라가고 있으므로 FCF 추정은 매출 추정보다 아래쪽으로 수정될 가능성이 크다. 단, 이 판단은 서버 회수 기간과 AWS 마진에 따라 달라진다. [C:implied_cagr@m15] [F135] [F141] [F140] [F348] [F26] [F194] [S62](https://www.webull.com/news/15364638750483456) [S45](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/amazon-postq-aws-reaccelerates-as-ai-investment-pushes-capex-higher)
- 촉매: FY2026Q3 실적에서 capex 분기 금액, AWS 영업이익, 매출채권, 2027 capex 가이던스. 차입 조달 규모도 확인된다.
- 시점: 2026-10-29 전후 3분기 실적, 2027-02 4분기 실적과 2027 capex 가이던스
- 컨센서스 대비 revenue FY2026: -0.1% (8,280.5억 USD vs 8,289.0억 USD)

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **232.43** vs 주가 250.00 · 기대 연 수익률 **+8.4%** · 손실 확률 30%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 30% | 103.58 | 64.31 | -16.2% | AI 증설이 수요보다 앞서가는 경우다. 2026년 capex는 약 2,200억 달러까지 올랐는데, 서버 회수 기간이 3년을 조금 넘는 수준에서 더 길어지고 수주잔고 4,960억 달러의 상당 부분이 Anthropic· |
| 기본 | 50% | 406.20 | 252.22 | +10.2% | FY2026은 상반기 실적이 이미 나왔고 3분기 가이던스가 있어 매출 성장이 컨센서스(약 8,289억 달러)와 거의 같다. 이후 AWS 성장 가속(+36.7%)과 광고(+26%)가 소매 성장을 끌어올려 성장률이 서서 |
| 강세 | 20% | 700.81 | 435.15 | +22.9% | AWS 수주잔고가 매출로 빠르게 바뀌고 자체 칩(Trainium+Graviton)이 AWS 밖으로도 팔리는 경우다. 칩 연 환산 매출이 250억 달러를 넘고 세 자릿수로 성장하고 있어, 엔비디아 대비 원가 우위가 A |

## 3. 반증 조건 (thesis break)

- [대기 — FY2026Q3 미발표] 앤더슨: AWS 매출이 2분기 수준 아래로 후퇴 — 수요가 증설을 따라오지 못한다는 신호 — `aws_revenue < 4.2e+10` (FY2026Q3)
- [대기 — FY2026Q3 미발표] 앤더슨: AWS 영업이익이 2분기보다 줄어듦 — 규모의 이익 가설 훼손 — `aws_operating_income < 1.6e+10` (FY2026Q3)
- [수동 확인] 앤더슨: 연간 설비투자를 올리는데 AWS 성장률이 오히려 둔화하는 분기가 이어지면 수동 확인
- [대기 — FY2026Q3 미발표] 슬레이터: AWS 영업이익이 FY2026Q2 수준 아래로 후퇴 — 증설이 이익으로 돌아온다는 가설 훼손 — `aws_operating_income < 1.66e+10` (FY2026Q3)
- [대기 — FY2026Q3 미발표] 슬레이터: 분기 설비투자가 정점을 지나지 못하고 계속 증가 — `capex > 6.2e+10` (FY2026Q3)
- [수동 확인] 슬레이터: 증설 자금을 위해 대규모 외부 조달이 필요해지는 경우 — 수동 확인
- [대기 — FY2026Q3 미발표] 애크먼: 회사 정의 TTM FCF가 다시 양수로 전환 — `fcf_company_ttm > 0` (FY2026Q3)
- [대기 — FY2026Q3 미발표] 애크먼: 3분기 설비투자 620억 달러 이하로 정점 신호 — `capex <= 6.2e+10` (FY2026Q3)
- [미충족] 애크먼: 주가가 205달러 아래로 내려가 기본 시나리오 대비 안전마진 20% 확보 — `price < 205`
- [미충족] 레드팀: 회사 정의 TTM FCF가 -200억 달러 아래로 악화 — 증설 비용이 수익화를 앞지르는 중 — `fcf_company_ttm < -2e+10`
- [미충족] 레드팀: AWS 성장률이 30% 아래로 둔화 — 5분기 연속 가속 서사가 끊김 — `aws_revenue_growth < 0.3`
- [대기 — FY2026Q3 미발표] 레드팀: 총부채가 1,500억 달러 초과 — 3분기 이후에도 차입이 가속 중 — `debt > 1.5e+11`
- [미충족] 레드팀: AWS 영업이익이 FY2026Q2 166.2억 아래로 후퇴 — 마진 개선 가설이 훼손 — `aws_operating_income < 1.6e+10`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | revenue | FY2026Q3 | >= 2.02e+11 | 60% | 가이던스 상단 이상 상회 패턴(최근 두 분기 모두 상단 초과)이 이어지는지 시험한다. 기본 시나리오의 FY2026 성장 경로를 지탱한다. |
| K2 | operating_income | FY2026Q3 | >= 2.65e+10 | 55% | 감가상각이 늘어도 영업이익이 가이던스 상단을 넘으면 마진 개선 가설이 유지된다. 단, 3분기 가이던스에는 에너지 파생 재평가가 빠져 있다. |
| K3 | aws_revenue | FY2026Q3 | >= 4.5e+10 | 60% | AWS 재가속이 이어지는지가 기본·강세 시나리오 매출 경로의 핵심 전제다. 약세 시나리오는 이 성장이 둔화되는 경우다. |
| K4 | aws_operating_income | FY2026Q3 | >= 1.75e+10 | 50% | 증설 비용이 늘어도 AWS 영업이익이 늘어야 FCF 마진 회복 가정이 유지된다. |
| K5 | capex | FY2026Q3 | <= 6.2e+10 | 55% | 연간 가이던스 약 2,200억 달러가 지켜지는지, 분기 지출이 정점에 가까워지는지 시험한다. 초과하면 FCF 마진 13% 가정이 위험해진다. |

## 5. 확신도와 비중

- 확신 가중 점수 +0.13 · 비중 참고값 0.0% (확률 가중 기대 연 수익률 +8.4%가 요구수익률 10% 이하 — 찬성이어도 가격이 보상하지 않는다) · 슬레이터 시작 비중 1.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 0/5 실패 | founder_led=아니오, upside_10y=5.47x, revenue_5y=1.99x |
| 슬레이터 | 찬성 → 찬성 | 3/5 | ✓ | 0/5 실패 | unit_economics=proven, survival_path=예, starter_weight=1.0%, cash_survives=예, cash_min=1,229.9억 USD, runway_years=10.6 |
| 애크먼 | 반대 → 반대 | 4/5 | ✗ 단순·예측 가능한 사업이 아님; 잉여현금흐름을 만들지 못함 (코드 계산); 레버리지·자본시장 의존; 안전마진 20% 미만 또는 계산 불가 | 0/5 실패 | simple_predictable=아니오, capital_markets_dependent=예, catalyst=없음 — 3분기 실적에서 capex 정점 신호와 FCF 흑자 전환이 확인되기 전까지 가치와 가격의 격차를 좁힐 구체적 행동이 없다, intrinsic_value=252.2, mos=0.9%, fcf_positive=아니오, net_debt_to_ebitda=0.05x |

- ⚠ 앤더슨: 5년 매출 1.99배 < 2배 (LTGG Q1)
- ⚠ 앤더슨: rebuttals[1] leap: 수주잔고·capex·AWS 영업이익은 맞지만, 병목이 '수요가 아니라 전력과 칩'이라는 결론은 자료에 명시되어 있지 않다.
- ⚠ 앤더슨: arguments[1] leap: 수주잔고와 용량 부족 발언은 맞지만, 매출 두 배에 필요한 것이 전력과 칩 공급이라는 결론은 자료에서 따라 나오지 않는다.
- ⚠ 앤더슨: arguments[4] leap: 코드 값(12.1%, 5.47배, 컨센서스 차이 -0.1%)은 바르지만, 컨센서스 매출이 기본 시나리오와 같다는 것만으로 강세 상방이 가격에 반영되지 않았다는 결론은 따라 나오지 않는다.
- ⚠ 앤더슨: rebuttals[0] unsupported: 없는 근거 인용: C:fcf_company_ttm
- ⚠ 앤더슨: arguments[4]: 인용하지 않은 근거의 숫자 15%(C:deferred_revenue_growth@FY2023·C:revenue_cagr@bull·S64), 14.8%(C:revenue_cagr@bull), 18%(C:fcf_margin@bull·C:roic@FY2025) — cites에 추가
- ⚠ 슬레이터: rebuttals[2] unsupported: 없는 근거 인용: C:p_fcf
- ⚠ 슬레이터: arguments[2]: 인용하지 않은 근거의 숫자 520(S62) — cites에 추가
- ⚠ 슬레이터: rebuttals[0]: 인용하지 않은 근거의 숫자 5.2e+09(S64) — cites에 추가
- ⚠ 애크먼: arguments[4] leap: AWS 지표, 순이익 626.5억과 OCF 453.9억은 맞지만, 영업외수익 534.1억이 '주로 Anthropic 평가이익'이라는 귀속은 인용 자료에 없다.
- ⚠ 애크먼: rebuttals[2] unsupported: 없는 근거 인용: C:p_fcf
- ⚠ 애크먼: rebuttals[0]: 인용하지 않은 근거의 숫자 10%(C:accruals_ratio@FY2024·C:discount_rate·C:fcf_conversion@FY2025) — cites에 추가
- ⚠ 애크먼: risks[1]: 인용하지 않은 근거의 숫자 13%(C:fcf_margin@base·S75), 10%(C:accruals_ratio@FY2024·C:discount_rate·C:fcf_conversion@FY2025) — cites에 추가
- ⚠ 낡은 컨센서스 — F141: capex FY2026 컨센서스 2.061e+11가 회사 가이던스 하단 2.2e+11(F140)보다 낮다 — 갱신 전 값으로 보고 제외
- ⚠ 모델이 컨센서스와 사실상 같다 — variant perception이 없다면 알파도 없다
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 모델러 scenarios.bear 검증 실패(contradicted): 자료의 서버 손익분기는 '3년 조금 못 미침'인데 주장은 '3년을 조금 넘는 수준'이라고 써서 방향이 다르다. 나머지 사실(capex 2,200억, TTM FCF -76억, 수주잔고, 차입금)은 맞다.
- ⚠ 회계 품질 findings[6]: 인용하지 않은 근거의 숫자 7.7e+09(C:fcf@FY2025) — cites에 추가
- ⚠ 회계 품질 findings[2]: 인용하지 않은 근거의 숫자 650(S62), 520(S62), 100%(C:guidance_hit_rate) — cites에 추가
- ⚠ 경영진·자본배분 findings[3]: 인용하지 않은 근거의 숫자 1.947e+10(C:d_and_a@FY2025Q4·C:sbc@FY2025·F111) — cites에 추가
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): 없는 근거 인용: C:p_fcf
- ⚠ 레드팀 premortem[3]: 인용하지 않은 근거의 숫자 53.1%(S73) — cites에 추가

## 앤더슨 — 찬성 (3/5)

> 아마존은 AI 인프라라는 새 기술혁명의 수확체증 구간에 가장 큰 자본을 쏟아붓는 회사다. AWS는 5분기 연속 가속해 매출 422.3억 달러(+36.7%)에 이르렀고, 수주잔고는 4,960억 달러다. 자체 칩 사업은 연 환산 250억 달러를 넘었다. 광고는 +26%로 두 번째 고마진 엔진이 됐다. 코드가 계산한 강세 case의 10년 뒤 주당 가치는 현재가의 5.47배로, 5배 문턱을 겨우 넘긴다. 5년 매출 배수는 1.99배로 2배에 약간 모자란다. 즉 마진 상방과 높은 재투자 활주로가 모두 맞아떨어져야 하는 베팅이다. 현재 가격은 FCF 마진이 15%로 오를 때 연 12.1% 성장을 가정하는데, 이는 대담한 기대가 아니다. FCF가 음수로 돌아서고 차입이 늘어난 것은 성장 가설을 깨는 신호가 아니라 증설 구간의 비용이다. 단, 수주잔고가 소수 고객에 쏠려 있을 가능성과 경쟁사의 더 빠른 성장 때문에 확신은 중간(3)으로 둔다.

*이전 판단 대비: 직전 판단과 같은 입장(찬성)이다. 새 근거는 없고 모델 가정과 강세 case도 같다. 직전 최종 결론은 반대였으나 내 표는 같다.*

**논거**
- AWS가 가속하면서 마진도 오르고 있다. AWS 매출 성장률은 FY2026Q1 28%에서 FY2026Q2 36.7%로 높아졌고, 영업이익은 166.2억 달러다. 경영진은 마진이 전년보다 650bp 올랐다고 했고, 파생상품 회계 이익을 빼도 520bp다. 규모가 커지는 중에 마진이 오르는 것은 수확체증의 전형이다. [F311] [F310] [F152] [F153] [F315] [F316] [S62](https://www.webull.com/news/15364638750483456)
- 수요가 공급을 앞선다. AWS 수주잔고는 4,960억 달러이고, 경영진은 2026년과 2027년 모두 수요를 다 맞출 용량이 없으며 2027년 용량 대부분이 이미 예약됐다고 밝혔다. 5년 안에 매출을 두 배로 만드는 데 필요한 것은 수요가 아니라 전력과 칩 공급이다. 이 병목을 푸는 데 자본을 쓰는 것이 지금의 capex다. [F317] [F140] [S62](https://www.webull.com/news/15364638750483456)
- 자체 칩이 원가 곡선을 바꿀 선택지다. Trainium과 Graviton의 연 환산 매출은 분기 사이 200억 달러에서 250억 달러로 늘었고 세 자릿수 성장 중이다. 경영진은 AWS 밖 판매도 실제 가능성이 있다고 했다. 이것이 현실이 되면 AWS 마진과 새 매출원이 동시에 열린다. 다만 이 단계는 경영진 발언이고 칩 사업의 별도 손익은 없다. [F369] [F368] [F370] [S62](https://www.webull.com/news/15364638750483456)
- 두 번째 고마진 엔진인 광고가 소매 위에 얹혀 있다. 광고 매출은 FY2026Q1 172.0억 달러(+24%)에서 FY2026Q2 198.1억 달러(+26%)로 커졌다. 판매자 서비스와 구독을 합치면 소매의 이익 구조가 바뀐다. 이는 영업이익률 상방(질문 6번)의 근거다. [F333] [F334] [F331] [F332] [F330] [F335]
- 시장이 요구하는 것은 대담하지 않다. 역DCF는 목표 FCF 마진 15%일 때 10년간 연 12.1% 매출 성장만을 요구한다. 강세 case(5년 연 14.8% 성장, FCF 마진 18%)가 이를 넘어서는 부분의 가치가 비대칭 상방이다. 코드가 계산한 강세 case 10년 업사이드는 문턱 5배 위에 있다. 컨센서스 매출은 기본 시나리오와 사실상 같아 이 상방은 가격에 반영되어 있지 않다. [C:implied_cagr@m15] [C:upside_10y@anderson] [C:consensus_diff@revenue@FY2026]

**사전 부검**
- 사전 부검 1: 증설이 수요를 앞질렀다. 2026년 capex 가이던스는 약 2,200억 달러이고 회사 정의 TTM FCF는 이미 -76.0억 달러다. 수주잔고의 상당 부분이 Anthropic과 OpenAI 같은 소수 고객에서 나왔다면, 그들의 자금 조달이 막히는 순간 가동률과 마진이 동시에 꺾인다. 이것은 소음이 아니라 성장 가설을 직접 깨는 시나리오다. [F140] [F348] [F317] [S62](https://www.webull.com/news/15364638750483456) [S71](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic)
- 사전 부검 2: 순환 구조가 AWS 성장의 독립성을 가린다. 아마존은 Anthropic에 최대 330억 달러를 투자하고 Anthropic은 AWS에 1,000억 달러 이상을 쓰기로 약정했다. 이익 일부는 평가이익이다. AWS 성장과 수주잔고 중 외부 수요가 얼마인지 알 수 없다. [F366] [F367] [F339] [F338] [S71](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic)
- 사전 부검 3: 점유율을 잃으며 커진다. 구글 클라우드는 같은 분기 매출 248억 달러로 +82%, 마이크로소프트 Azure는 +43% 성장했다고 보도됐다. 용량 제약이 풀리면 AWS의 성장률 격차가 드러날 수 있다. 차입금이 FY2025 656.5억 달러에서 FY2026Q2 1,288.9억 달러로 늘어, 조달 비용 상승이 겹치면 재투자 속도가 막힌다. [S70](https://www.fierce-network.com/cloud/google-cloud-surges-alphabets-ai-capex-problem-grows) [S69](https://tech-insider.org/azure-678-billion-backlog-earnings-2026/) [F26] [F194] [S67](https://fortune.com/2026/07/08/amazons-25-billion-surprise-bond-sale-dangled-extra-yield-to-lure-in-buyers/)

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 기본 시나리오 기준 안전마진이 거의 없다는 것이다. 그 계산은 맞다. 하지만 그것은 5년 뒤 출구 배수로 현재를 재는 도구다. 내가 묻는 것은 10년 뒤 크기다. 기본 시나리오의 연 수익률 분해에서 마진 변화는 +49.9%를 만들고 멀티플은 -53.1%를 깎는다. 가치는 멀티플이 아니라 현금 전환이 얼마나 커지느냐에 달려 있다. 강세 case는 그 상방을 코드가 5배 이상으로 계산한 것이다. FCF가 음수라는 사실도 성장 가설을 깨는 신호가 아니다. 증설 구간의 비용이고, 경영진도 데이터센터 가동·수익화 전까지의 역풍이라고 밝혔다. '현금을 뿜는 사업'이라는 기준은 이 단계의 기업에는 너무 늦게 충족된다. [C:iv@base] [F156] [C:fcf_company_ttm] [F348] [S62](https://www.webull.com/news/15364638750483456)
- → 슬레이터: 슬레이터의 가장 강한 논거는 입증된 회수가 아니라 입증되고 있는 회수이므로 작게 시작하고 증거로 키우자는 것이다. 방향에는 동의한다. 다만 그가 기다리는 증거는 분기 capex의 정점과 AWS 영업이익 유지다. 반면 가장 가치 있는 구간은 그 증거가 확정되기 전에 지나간다. AWS 수주잔고는 4,960억 달러이고 2027년 용량은 대부분 예약됐다. 병목은 수요가 아니라 전력과 칩이다. 증거를 기다리다 크기를 못 채우는 것이 내가 경계하는 실수다. 그래서 시작 비중은 작아도 좋지만 가설을 훼손하는 조건에서만 팔겠다는 원칙은 유지한다. [F317] [F140] [F153] [S62](https://www.webull.com/news/15364638750483456)
- → 레드팀: 레드팀의 가장 강한 시나리오는 수주잔고와 성장이 소수 AI 연구소에 쏠린 순환 수요라는 것이다. 이 시나리오는 소음이 아니라 성장 가설을 직접 깨므로 위험으로 인정한다. 다만 신호로 둔 AWS 성장률 30% 미만은 FY2026Q1 28%에서 FY2026Q2 36.7%로 가속한 직후의 값과 거리가 있다. 그 신호가 먼저 작동하면 내 철회 조건도 함께 발동한다. 또 Anthropic은 AWS만 쓰지 않고 Azure와 구글 클라우드도 병행하므로, 수요가 한 고객의 자금 조달에만 달린 구조는 아니다. 고객 구성은 공시되지 않았으니, 이는 입증이 아니라 반증이 아직 없다는 뜻이다. [F311] [F310] [F366] [F367] [S71](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic) [S69](https://tech-insider.org/azure-678-billion-backlog-earnings-2026/)

**인정한 점**
- 강세 case의 10년 뒤 주당 가치는 코드 계산으로 문턱을 간신히 넘는 수준이고 5년 매출 배수는 2배에 못 미친다. 이 베팅은 마진 상방과 재투자 활주로가 둘 다 맞아야 성립하므로, 확신을 4로 올리지 않고 3에 둔다.
- 애크먼이 지적한 순이익의 질 문제는 인정한다. 영업외수익 534.1억 달러가 대부분 평가이익이라 PER 20.15배가 낮아 보이는 착시를 만든다. 나는 PER로 판단하지 않으므로 결론은 같지만 논거에서 이익 수치를 쓰지 않는다.
- 레드팀이 짚은 대로 기본 시나리오의 FCF 마진 13%는 가장 약한 가정이다. 이 가정이 틀리면 내 상방도 줄어든다.


## 슬레이터 — 찬성 (3/5)

> 시장의 천장은 보이지 않고, 증거는 쌓이는 중이다. AWS는 5분기 연속 가속해 매출이 +36.7%, 영업이익이 166.2억 달러가 됐고, 수주잔고는 4,960억 달러이며 2027년 용량 대부분이 이미 예약됐다. 광고도 +26%로 커진다. 코드가 계산한 기본 시나리오의 현금 경로는 0 아래로 내려가지 않는다. 다만 이것은 '입증된 회수'가 아니라 '입증되고 있는 회수'다. TTM FCF는 -76.0억 달러로 돌아섰고 차입금은 두 배가 됐다. 그래서 크게 시작하지 않고 작게 시작해 증거로 키운다. 다음 시험은 3분기 실적에서 AWS 영업이익이 166.2억 달러 아래로 후퇴하는지, 분기 capex가 정점을 지나는지다. 둘 중 하나라도 깨지면 가설이 훼손된 것으로 보고 정리한다.

**논거**
- 크기와 지속성의 증거가 숫자로 나온다. AWS 성장률은 5분기 연속 가속해 FY2026Q2에 36.7%, 영업이익은 166.2억 달러다. 경영진은 2026년에도 2027년에도 수요를 다 맞출 용량이 없다고 말한다. 시장이 아직 공급에 막혀 있다는 뜻이다. [F310] [F153] [S75](https://www.trefis.com/stock/amzn/articles2/617445/the-dates-that-matter-most-for-amazon-stock/2026-10-02) [S62](https://www.webull.com/news/15364638750483456)
- 수요는 계획이 아니라 약정으로 확인된다. AWS 수주잔고는 4,960억 달러이고 2027년 용량 대부분이 예약됐다. 다만 고객별 구성은 공시되지 않았고 2차 트랜스크립트 기준이라, '입증'이 아니라 '유력한 흔적'으로만 읽는다. [F317] [S62](https://www.webull.com/news/15364638750483456)
- 단위경제는 AWS와 광고 두 곳에서 개선되고 있다. 광고는 FY2026Q2 198.1억 달러로 +26%, 연결 총이익률은 FY2025에 50.3%까지 올랐다. 일회성을 빼도 AWS 마진 개선은 520bp로 남는다. [F331] [F332] [C:gross_margin@FY2025] [F316]
- 생존은 외부 충격 없이 가능하다. 코드가 계산한 기본 시나리오 현금 경로는 0 아래로 내려가지 않고, 현금 소진 연수 계산값도 길다. 신용등급은 A1/AA/AA-다. 2022년의 교훈이던 '외부 자본 의존 기업'과는 출발점이 다르다. [C:cash_survives@slater] [C:runway_years] [S66](https://www.investing.com/news/stock-market-news/amazon-launches-eightpart-us-investment-grade-bond-offering-4779013)
- 아직 계획인 것과 이미 실적인 것을 가른다. 실적은 AWS 성장·마진과 가이던스 4개 항목의 상회다. 계획은 FCF 회복이다. 회사 정의 TTM FCF는 -76.0억 달러이고 경영진도 데이터센터 가동·수익화 전까지 FCF가 역풍이라고 했다. 그래서 확신은 3에 머문다. [C:guidance_hit_rate] [F348] [S62](https://www.webull.com/news/15364638750483456)

**사전 부검**
- 사전 부검 1 — 증설이 수요보다 앞섰다면. capex 가이던스는 약 2,200억 달러로 올랐고 주된 이유는 메모리 가격이다. 비용이 오른 만큼 매출이 따라오지 않으면 FCF 마진이 회복되지 않는다. 서버 손익분기가 3년 조금 못 미친다는 설명은 건물을 제외한 값이다. [F140] [S62](https://www.webull.com/news/15364638750483456) [S65](https://letsdatascience.com/news/aws-revenue-growth-outruns-available-ai-capacity-b0361d90)
- 사전 부검 2 — Anthropic 의존과 순환 구조. 아마존 투자, Anthropic의 AWS 지출 약정, 평가이익이 서로 연결돼 있어 AWS 성장과 수주잔고의 독립성을 확인할 수 없다. 고객 한두 곳이 흔들리면 수주잔고 해석이 바뀐다. [F366] [F367] [F317] [S71](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic)
- 사전 부검 3 — 조달 비용이 오르는 경우. 차입금이 두 배가 됐고, 7월 회사채는 신규 발행 프리미엄이 필요했으며 주문이 3월보다 적었다. 증설을 자체 현금흐름이 아니라 자본시장에 기대는 비중이 커진다. [F26] [F194] [S67](https://fortune.com/2026/07/08/amazons-25-billion-surprise-bond-sale-dangled-extra-yield-to-lure-in-buyers/) [F363]

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 TTM FCF -76.0억 달러, 차입금 두 배, 안전마진 0.9%다. 그러나 FCF 음수는 증설 구간의 결과이지 사업 단위경제 악화의 증거가 아니다. 연 환산 순이자 부담은 약 52억 수준으로 AWS 분기 영업이익 166.2억 달러에 견주면 감당 범위이고, 신용등급은 A1/AA/AA-다. 나는 예측 가능성 때문에 정의되지 않은 시장을 버리지 않는다. 대신 비중을 작게 잡고 증거로 키운다. 그래서 가격 여유가 없다는 지적은 전체 비중이 아니라 시작 비중으로 반영한다. [F348] [F26] [F194] [F361] [F153] [S66](https://www.investing.com/news/stock-market-news/amazon-launches-eightpart-us-investment-grade-bond-offering-4779013) [C:mos@ackman]
- → 앤더슨: 앤더슨의 5배 상방은 강세 case에서 5.47배로 문턱을 겨우 넘고 5년 매출 배수는 1.99배로 모자란다. 마진 상방과 재투자 활주로가 동시에 맞아야 하는 베팅이다. '5배'에 기대지 않고, 성립하려면 AWS 영업이익이 166.2억 달러 아래로 후퇴하지 않고 분기 capex가 정점을 지나야 한다는 운영 지표로 역산한다. 수주잔고 4,960억 달러는 아직 계획이지 실적이 아니므로 확신을 3 이상으로 올리지 않는다. [C:upside_10y@anderson] [C:revenue_5y@anderson] [F317] [F153] [F140]
- → 레드팀: 레드팀의 가장 강한 논거는 기본 시나리오 FCF 마진 13%와 출구 배수 25배에 현재 앵커가 없다는 점이다. 인정한다. 그래서 FCF 마진 가정에 기대지 않고 AWS 영업이익과 분기 capex를 must_be_true로 잡았다. 사전 부검의 선행 신호 중 AWS 성장률 30% 미만과 총부채 1,500억 달러 초과를 반증 조건에 넣어 코드가 분기마다 대조하게 한다. 소수 고객 집중은 공시가 없어 수동 확인으로 남긴다. [C:fcf_margin@FY2025] [C:p_fcf] [F317] [F194] [S71](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic)

**참이어야 하는 것**
- [on_track] AWS 매출 성장이 30% 이상을 유지해 재가속이 일시적 현상이 아님을 보인다
- [on_track] AWS 영업이익이 FY2026Q2의 166.2억 달러 이상을 유지해 증설이 이익으로 돌아옴을 보인다
- [at_risk] 분기 capex가 620억 달러 이하로 관리되어 정점에 가까워진다
- [on_track] 광고 매출 성장이 FY2026Q1의 24%보다 낮아지지 않아 소매 쪽 고마진 엔진이 유지된다

**인정한 점**
- 애크먼: 기본 시나리오 안전마진이 0.9%라 가격 여유가 없고 TTM FCF가 음수라는 점을 인정한다. 결과적으로 시작 비중을 0.02에서 0.01로 낮추고 capex 조건을 at_risk로 유지한다.
- 레드팀: 수주잔고 고객 집중과 Anthropic 순환 구조는 공시로 검증할 수 없다. 결과적으로 수주잔고를 입증이 아니라 흔적으로만 읽고 AWS 성장률 30% 미만을 반증 조건에 추가한다.
- 앤더슨: 상방은 인정하지만 5배 문턱이 아슬아슬해 확신을 올리는 근거가 되지 못한다.


## 애크먼 — 반대 (4/5)

> 아마존은 질 좋은 사업이다. 그러나 지금 가격에서는 담지 않는다. 기본 시나리오 내재가치는 252.22달러인데 주가가 250달러라 안전마진이 거의 없다. 회사 정의 TTM FCF는 이미 -76.0억 달러로 돌아섰고, 2026년 설비투자 가이던스는 약 2,200억 달러다. 차입금은 2배로 늘었고 회사채 시장에는 신규 발행 프리미엄까지 얹었다. FCF 마진 가정이 6%에서 18%까지 벌어지는 사업은 10년 뒤 FCF 범위를 좁게 추정할 수 없다. 단순·예측 가능·현금 창출·자본시장 비의존이라는 네 조건 중 지금 충족하는 것이 없다. 좋은 회사지만 이 가격에서는 기다린다.

**논거**
- 가격: 기본 시나리오 현재가치 252.22달러 대비 주가 250달러라 안전마진이 0.9%에 그친다. 20% 기준에 크게 못 미치고, 기본 시나리오를 그대로 믿어도 여유가 없다. [C:iv@base] [C:mos@ackman] [F156]
- 현금: 회사 정의 TTM FCF가 -76.0억 달러다. 2026년 설비투자 가이던스는 약 2,200억 달러로 2월 계획에서 올랐고, FY2025에도 FCF 마진은 1.1%에 불과했다. 경영진도 FCF는 데이터센터 수익화 전까지 역풍이라고 말했다. '현금을 뿜는' 사업이라는 첫 조건이 현재는 성립하지 않는다. [F348] [F140] [C:fcf_margin@FY2025] [S62](https://www.webull.com/news/15364638750483456)
- 자본시장 의존: 총부채가 FY2025 656.5억 달러에서 FY2026Q2 1,288.9억 달러로 늘었고, 7월에 250억 달러 회사채를 발행했다. 이 발행은 신규 발행 프리미엄을 제시했고 최대 주문이 620억 달러로 3월보다 적었다. 순부채/EBITDA는 낮지만 FCF가 음수라 성장 자금을 외부 조달에 기대는 구조가 됐다. 밸리언트의 교훈상 싸도 사지 않는 영역이다. [F26] [F194] [F362] [F363] [S67](https://fortune.com/2026/07/08/amazons-25-billion-surprise-bond-sale-dangled-extra-yield-to-lure-in-buyers/) [C:net_debt_to_ebitda]
- 단순성: 소매·광고·AWS에 더해 Leo 위성과 116억 달러 규모의 Globalstar 인수까지 얹혔다. Leo의 총 비용은 공시되지 않았다. 모델러의 FCF 마진 가정이 약세 6%에서 강세 18%까지 벌어진다는 사실 자체가 10년 FCF를 합리적 범위로 추정하기 어렵다는 증거다. [F374] [S72](https://www.constellationr.com/insights/news/amazon-doubles-down-leo-acquires-globalstar-116-billion) [C:fcf_margin@bear] [C:fcf_margin@bull]
- 사업의 질은 인정한다. AWS 매출이 36.7% 성장했고 영업이익이 166.2억 달러다. 그러나 순이익 626.5억 달러는 영업현금흐름 453.9억 달러보다 크고, 영업외수익 534.1억 달러(주로 Anthropic 평가이익)가 키웠다. 질 좋은 사업과 질 좋은 이익은 다르며, PER 20.15배도 이 평가이익으로 낮아 보인다. [F310] [F153] [F80] [F90] [F338] [C:pe]

**사전 부검**
- 사전 부검: 내가 틀렸다면 AWS 수주잔고 4,960억 달러가 예상보다 빠르게 매출로 바뀌고 마진이 계속 오른 경우다. 그러면 2027~2028년에 capex 증가가 꺾이면서 FCF가 급반등하고, 강세 시나리오 쪽으로 가치가 올라간다. 지금 사지 않아 상승분을 놓친다. [F317] [F315] [C:iv@bull]
- 사전 부검: 안전마진 계산은 모델러의 기본 시나리오 FCF 마진 13%에 기댄다. 이 가정이 보수적이라면 내재가치가 252.22달러보다 높을 수 있다. 반대로 기대 연 수익률이 +8.4%로 요구수익률 10%에 못 미치므로, 확률 가중으로도 싸지 않다는 결론은 유지된다. [C:iv@base] [C:expected_irr]
- 사전 부검: Anthropic·OpenAI 같은 소수 고객 의존과 순환 구조가 사실이면 가치가 더 낮아진다. 이 경우 안전마진은 음수로 바뀌고 반대 판단이 더 강해질 뿐이므로 방향은 같다. [F366] [F367] [S71](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic)

**반론**
- → 앤더슨: 앤더슨의 강세 case는 10년 업사이드 5.47배로 문턱 5배를 겨우 넘고 5년 매출 배수는 1.99배로 2배에 못 미친다. 마진 상방과 재투자 활주로가 동시에 맞아야 하는 베팅이다. 강세 확률은 20%이고 약세 확률은 30%이며, 확률 가중 기대 연 수익률은 +8.4%로 요구수익률 10%에 못 미친다. 가장 좋은 시나리오를 기준으로 삼는 것은 생존자 편향이다. 역DCF의 12.1%는 FCF 마진 15% 도달을 전제하는데, 현재 회사 정의 TTM FCF는 마이너스다. [C:upside_10y@anderson] [C:revenue_5y@anderson] [C:expected_irr] [C:implied_cagr@m15] [F348]
- → 슬레이터: 슬레이터가 말한 생존 경로와 단위경제는 필요조건이지 가격의 정당화가 아니다. 기본 시나리오 내재가치는 252.22달러이고 주가는 250달러라 안전마진은 0.9%다. 슬레이터 스스로 capex 조건을 '위험'으로 표시했고, 차입금은 두 배가 됐으며 7월 회사채는 신규 발행 프리미엄이 필요했다. 좋은 회사도 비싸게 사면 나쁜 투자다. [C:iv@base] [C:mos@ackman] [F26] [F194] [S67](https://fortune.com/2026/07/08/amazons-25-billion-surprise-bond-sale-dangled-extra-yield-to-lure-in-buyers/)
- → 레드팀: 레드팀의 약한 고리인 기본 시나리오 FCF 마진 13%와 출구 배수 25배를 받아들인다. 출구 배수를 0.75배로 낮추면 기본 시나리오 연 수익률이 +10.2%에서 +4.7%로 내려간다. 그렇다면 안전마진이 20%보다 훨씬 커야 하는데 현재 0.9%뿐이다. 내 반대는 이 사전 부검으로 더 강해진다. [C:p_fcf] [C:fcf_yield] [C:iv@base] [C:mos@ackman]

**인정한 점**
- 앤더슨의 지적대로 AWS 성장이 5분기 연속 가속되고 영업이익이 166.2억 달러인 것은 사업의 질을 입증하는 증거다. 다만 사업의 질은 인정해도 가격과 현금 전환의 조건이 충족되지 않으므로 결론은 바뀌지 않는다.
- 슬레이터의 말처럼 신용등급이 높고 순부채/EBITDA가 낮아 단기 생존 위험은 작다. 그러나 이는 자본시장 의존도 판정을 약화시킬 뿐 안전마진 부족을 해소하지 못한다.


## 분석 모듈 (L4)

### 사업·산업 — proven

아마존은 세 개의 현금 엔진을 가진 복합 플랫폼이다. 하나는 온라인·3P 마켓플레이스·물류 소매다. 둘째는 광고와 구독이다. 셋째는 AWS 클라우드·AI 인프라다. 연결 총이익률은 FY2021 42.0%에서 FY2025 50.3%로 올랐다(C:gross_margin@FY2021, C:gross_margin@FY2025). 고마진 사업인 AWS, 광고, 3P 서비스의 비중이 커진 결과다. FY2026Q2에는 AWS 매출이 422.3억 달러(+36.7%)로 가속했고 영업이익은 166.2억 달러였다. 반면 FY2026 capex 가이던스는 약 2,200억 달러로, TTM FCF는 회사 정의로 -76.0억 달러가 됐다. 단위경제는 AWS와 광고에서 개선되고 있다. 다만 AI 자본집약도가 높아져 재투자 수익률은 아직 입증되지 않았다.

- [unit_economics] 연결 수익성은 구조적으로 개선됐다. 총이익률은 42.0%에서 50.3%로, 영업이익률은 FY2021 5.3%에서 FY2025 11.2%로 올랐다. FY2026Q2 영업이익은 274.6억이다. 이 중 관세 환급 약 6억과 에너지 계약 공정가치 이익 약 6억이 일회성 비용 감소로 포함돼 있다(2차 요약). 이를 빼면 질이 낮아진다. 경영진도 마진 개선이 선형적이지 않을 수 있다고 말했다. [C:gross_margin@FY2021] [C:gross_margin@FY2025] [C:operating_margin@FY2021] [C:operating_margin@FY2025] [F96] [F342] [F343] [S63](https://transcripts.platformaeronaut.com/summaries/AMZN-2Q26-AI-Summary)
- [unit_economics] 소매 물류 단위경제는 개선이 불확실하다. 전 세계 유료 판매 단위는 +17%인데, 2차 블로그는 배송비가 +19%로 더 빨리 늘었다고 적었다(원문 대조 필요). 4월 FBA 유류할증, 중동발 연료비, 운전기사 부족이 언급됐다. 당일·익일 배송은 40% 이상 증가했고, 로봇 팔은 2026년에 '두 배 이상' 늘어난다. 이 투자가 단위당 비용을 낮추는지는 아직 공시 숫자로 확인되지 않는다. 그래서 소매 쪽은 개선 중이라 단정하지 않는다. [F337] [S62](https://www.webull.com/news/15364638750483456) [S64](https://www.levelheadedinvesting.com/p/amazon-com-inc-amzn-q2-2026-results-same-strategy-opposite-reaction)
- [industry] 클라우드·AI 인프라는 소수 하이퍼스케일러가 용량을 두고 경쟁하는 구조다. 구글 클라우드 2분기 매출은 248억(+82%), 마진 35.6%였다. 마이크로소프트 Azure는 +43%, 상업용 RPO는 6,780억이다. AWS 성장 36.7%는 5분기 연속 가속이지만, 경쟁사 성장률이 더 높다는 점은 점유율 방어가 입증되지 않았음을 뜻한다. 경쟁사 수치는 모두 2차 기사다. [F310] [S70](https://www.fierce-network.com/cloud/google-cloud-surges-alphabets-ai-capex-problem-grows) [S69](https://tech-insider.org/azure-678-billion-backlog-earnings-2026/) [S75](https://www.trefis.com/stock/amzn/articles2/617445/the-dates-that-matter-most-for-amazon-stock/2026-10-02)
- [customers] AWS AI 수요가 특정 고객에 집중됐고 순환 구조의 위험이 있다. 아마존은 Anthropic에 최대 330억 달러를 투자하기로 했고, Anthropic은 10년간 AWS에 1,000억 달러 이상을 쓰기로 약정했다. 아마존 FY2026Q1에는 Anthropic 평가이익 168억이 반영됐고, FY2026Q2 기타영업외수익도 534.1억이었다. 이는 순이익 626.5억의 상당 부분을 설명한다. 순이익이 영업 현금으로 환원된 것이 아니다. Anthropic은 Azure와 구글 클라우드도 병행해 쓴다. [F366] [F367] [F339] [F338] [F80] [S71](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic)
- [runway] 재투자 활주로는 크지만 수익률은 미입증이다. FY2025 capex는 1,318.2억, 2026 가이던스는 약 2,200억으로 올랐다. 주된 이유는 메모리 가격 상승이고, 로보틱스·반도체·위성(Leo) 등 비AWS 항목이 포함된다. AI·비AI 구분은 공시되지 않았다. TTM FCF는 -76.0억, 순현금은 -92.4억이다(C:net_cash). 차입금은 FY2025 656.5억에서 FY2026Q2 1,288.9억으로 늘었다. 서버 손익분기가 3년 조금 못 미친다는 경영진 설명은 회수 기간의 단서이나, 건물과 기타 자산은 제외된 값이다. [F165] [F140] [F348] [C:net_cash] [F26] [F194] [S62](https://www.webull.com/news/15364638750483456) [S65](https://letsdatascience.com/news/aws-revenue-growth-outruns-available-ai-capacity-b0361d90) [S64](https://www.levelheadedinvesting.com/p/amazon-com-inc-amzn-q2-2026-results-same-strategy-opposite-reaction)
- [runway] AWS 외 신사업 투자의 규모가 크고 손익은 공시되지 않는다. Leo 위성은 FY2026Q1 250기에서 FY2026Q2 400기로 늘었고, Globalstar 인수는 약 116억 달러(2027년 종결 예상)다. Leo의 총 프로그램 비용·capex·매출은 공시되지 않았다. 그래서 이 투자의 단위경제는 판단할 수 없다. [F373] [F372] [F374] [S72](https://www.constellationr.com/insights/news/amazon-doubles-down-leo-acquires-globalstar-116-billion)
- [industry] AI 인프라 증설 자금이 자본시장으로 이동하고 있다. 7월에 250억 달러 8개 트랜치 회사채를 발행했다(최대 주문 620억으로 3월보다 적었다). 신규 발행 프리미엄이 제시됐고, 9월에는 첫 파운드화 채권 준비가 보도됐다. 신용등급은 A1/AA/AA-다. 경영진도 FCF는 데이터센터 가동·수익화 전까지 '역풍'이라고 했다. 이는 사업 모델이 외부 조달에 더 의존하게 됐다는 뜻이다. [F362] [F363] [S66](https://www.investing.com/news/stock-market-news/amazon-launches-eightpart-us-investment-grade-bond-offering-4779013) [S67](https://fortune.com/2026/07/08/amazons-25-billion-surprise-bond-sale-dangled-extra-yield-to-lure-in-buyers/) [S68](https://techeconomy.ng/amazon-sterling-bond-sale-ai-spending-220-billion) [S62](https://www.webull.com/news/15364638750483456)
- [proven] AWS 규모의 흔적: FY2025Q2 AWS 매출 308.7억에서 FY2026Q2 422.3억으로 성장했고, 같은 기간 영업이익은 101.6억에서 166.2억으로 늘었다. 경영진은 성장 가속과 함께 마진이 전년 대비 650bp 올랐다고 밝혔다(일회성 제외 520bp). 2026~2027년 수요를 다 맞출 용량이 없다는 점도 규모 우위를 뒷받침한다. 단 경쟁사도 용량 제약 속에서 성장하고 있어 점유율 증거는 아니다. [F308] [F152] [F309] [F153] [F315] [F316] [S62](https://www.webull.com/news/15364638750483456)
- [claimed] AWS 수주잔고 4,960억 달러(세 자릿수 증가)는 다년 약정이라는 전환비용의 흔적이다. 그러나 1차 공시(10-Q)에는 고객별 구성이 없다. 구글 클라우드 수주잔고(5,140억)와 마이크로소프트 상업용 RPO(6,780억)가 더 크다는 2차 보도가 있어, AWS 단독 우위의 증거는 아니다. 집중도(Anthropic·OpenAI 비중)도 미공개다. [F317] [S62](https://www.webull.com/news/15364638750483456) [S70](https://www.fierce-network.com/cloud/google-cloud-surges-alphabets-ai-capex-problem-grows) [S69](https://tech-insider.org/azure-678-billion-backlog-earnings-2026/) [S64](https://www.levelheadedinvesting.com/p/amazon-com-inc-amzn-q2-2026-results-same-strategy-opposite-reaction)
- [claimed] 자체 칩(Trainium+Graviton) 연 환산 매출이 250.0억 달러로 늘고 있어 AI 인프라 원가 우위의 단초가 된다. 다만 이는 경영진 발언이고 AWS 밖 판매는 '가능성' 단계다. 칩 사업의 별도 마진과 손익은 공시되지 않았다. [F368] [F370] [S62](https://www.webull.com/news/15364638750483456) [S48](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm)
- [proven] 마켓플레이스·광고 네트워크 효과의 흔적: 3P 판매자 서비스 매출 467.8억, 광고 매출 198.1억(+26%), 구독 137.3억이다. 광고는 FY2026Q1 172.0억(+24%)에서 FY2026Q2 198.1억(+26%)으로 커졌다. 판매자 트래픽을 수익화하는 구조가 공시 숫자로 확인된다. FTC가 스폰서드 광고 소송을 제기해 이 수익원에는 규제 리스크가 있다. [F330] [F331] [F332] [F333] [F334] [F335] [S32](https://news.google.com/rss/articles/CBMiigFBVV95cUxNN1RnMWxFWmtqTEJZNmtTNmVHdGZhUXhVbEVTenNKam8xZmtIVGNfQlYwRlY2anZ1ZXZWc1RDUW9DUFc2endnM1pOdU13c2I0RExUUGNrVFlvajZFWk8wNHZDQVdLR0JNc0wxeG1Lb05mektkVnVhejRsd1oxSG1jNGxBVWhoY2xkSHc?oc=5)

### 경영진·자본배분 — mixed

가이던스 신뢰도는 높게 나타났지만 표본이 두 분기뿐이다. 보상, 내부자 매매, 자사주 승인 현황은 근거를 찾지 못해 정렬 여부를 판단할 수 없다. 자본배분은 AI 설비투자와 차입을 크게 늘리는 쪽으로 움직였다. FCF는 TTM 기준으로 음수로 돌아섰다. 지분 희석은 SBC 대비 작은 편이고 FY2023~FY2024 자사주 매입은 0이었다. 관계사 Anthropic 투자와 평가이익이 이익과 지출 약정에 순환 구조로 얽혀 있다. 이 점은 해석에 주의가 필요하다. 종합하면 정렬은 '혼재'로 본다.

- [compensation] 근거 없음. DEF 14A(2026-04-09)는 근거 목록에 있지만 보상 연동 지표(장기 FCF·ROIC·주당가치 vs 단기 EPS·조정 EBITDA)와 베스팅 기간은 수집되지 않았다. 보상 구조가 주주와 같은 방향인지 판단할 수 없다. [S13](https://www.sec.gov/Archives/edgar/data/1018724/000110465926041026/tm261382-1_def14a.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도 자료는 수집되지 않았다. 이사회에는 2026-09-09 보도 기준 Kevin Mandia(사이버보안 전문가)가 합류했다. 같은 날 경영진 변동 8-K도 제출됐지만 내용은 수집되지 않았다. [S41](https://news.google.com/rss/articles/CBMijAFBVV95cUxNdHVLaG9jX1A0Qk81YV92YzFwVDBlTnRTamtSaS1DUnFnQ0hRdWRzcktUeXIwc1h6dW9MY1ZaeDdNNkRSY0Q2UDRfUnlPY0VULUxyMGNfOXBDbVJlRTFQcDd0N1BjMWZJSHFGRW13NHRMeU0wQjloaGY1d3dzWFRtSHIyajZuMUJJTlZseg?oc=5) [S2](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000036/amzn-20260908.htm)
- [guidance] 코드 대조 결과 가이던스 적중률은 100%다. FY2026Q1 매출은 가이던스 1,755.0억 달러 대비 실제 1,815.2억 달러, 영업이익은 190.0억 달러 대비 238.5억 달러였다. FY2026Q2 매출은 1,965.0억 달러 대비 2,006.1억 달러, 영업이익은 220.0억 달러 대비 274.6억 달러였다. 네 항목 모두 beat이고 영업이익은 가이던스 중간값을 크게 웃돌았다. 표본이 두 분기뿐이라 보수적 가이던스 관행이라고 단정하기는 어렵다. 2분기 영업이익에는 관세 환급 약 6억 달러와 에너지 계약 공정가치 이익 6.0억 달러가 일회성으로 섞여 있다(2차 자료). [C:guidance_hit_rate] [F154] [F107] [F155] [F95] [F357] [F108] [F358] [F96] [S63](https://transcripts.platformaeronaut.com/summaries/AMZN-2Q26-AI-Summary)
- [dilution] 희석 주식 수는 FY2024 107.2억 주, FY2025 108.3억 주, FY2026Q2 109.0억 주로 늘었다. FY2025 주식 수 변화는 1.0%다. SBC는 FY2025 194.7억 달러로 매출 대비 2.7%이고 FY2023 4.2%에서 낮아졌다. 다만 FY2025 SBC 차감 FCF는 -117.7억 달러다. 자사주 매입은 FY2023·FY2024에 0, FY2022에 60.0억 달러였다. 매입으로 희석을 상쇄하지 않고 희석 규모 자체를 작게 유지하는 구조다. [C:share_change@FY2025] [C:sbc_to_revenue@FY2025] [C:sbc_to_revenue@FY2023] [C:fcf_after_sbc@FY2025] [F214] [F41] [F46] [F157] [F158] [F159] [F160]
- [capital_allocation] 설비투자는 FY2023 527.3억 달러, FY2024 830.0억 달러, FY2025 1,318.2억 달러로 늘었다. 2026년 가이던스는 약 2,200억 달러로, 2월의 약 2,000억 달러에서 상향됐고 주된 이유는 메모리 가격 상승이다. FCF는 FY2024 328.8억 달러, FY2025 77.0억 달러로 줄었다. 회사 정의 TTM FCF는 FY2026Q2에 -76.0억 달러다. 경영진은 데이터센터 가동·수익화 전까지 FCF가 역풍이라고 밝혔다. 이 투자의 수익률은 아직 확인되지 않았다. 다만 AWS 영업이익이 FY2025Q2 101.6억 달러에서 FY2026Q2 166.2억 달러로 늘었고 수주잔고는 4,960.0억 달러다. 수주잔고는 2차 트랜스크립트 기준이다. [C:capex@FY2023] [C:capex@FY2024] [C:capex@FY2025] [C:fcf@FY2024] [C:fcf@FY2025] [F140] [F348] [F309] [F153] [F317] [S62](https://www.webull.com/news/15364638750483456) [S65](https://letsdatascience.com/news/aws-revenue-growth-outruns-available-ai-capacity-b0361d90)
- [capital_allocation] 재무 레버리지가 빠르게 올라갔다. 총부채는 FY2025 656.5억 달러에서 FY2026Q2 1,288.9억 달러로 늘었다. 2026년 상반기 차입은 약 670억 달러(2차)이고, 7월에는 250억 달러 8개 트랜치 회사채를 발행했다. 이 발행은 주문 규모가 3월보다 작았고, 신규 발행 프리미엄을 제시했다는 보도가 있다. 9월에는 첫 파운드화 채권을 준비했다. 경영진은 '다른 조달 방안'도 검토 중이라고 밝혔다. 코드 기준 순현금은 -92.4억 달러이고 순부채/EBITDA는 0.05배로 아직 낮다. 조달 의존도는 높아지는 중이다. [F26] [F194] [F360] [F362] [F363] [S66](https://www.investing.com/news/stock-market-news/amazon-launches-eightpart-us-investment-grade-bond-offering-4779013) [S67](https://fortune.com/2026/07/08/amazons-25-billion-surprise-bond-sale-dangled-extra-yield-to-lure-in-buyers/) [S68](https://techeconomy.ng/amazon-sterling-bond-sale-ai-spending-220-billion) [S62](https://www.webull.com/news/15364638750483456) [C:net_cash] [C:net_debt_to_ebitda]
- [capital_allocation] Anthropic 투자는 2023~2025년 80억 달러 단계 투자에 이어 2026년 4월 최대 330억 달러(신규 지분 50억 달러와 마일스톤 연동 최대 200억 달러)로 확대됐다. Anthropic은 10년간 AWS에 1,000억 달러 이상 지출하기로 약정했다. FY2026Q1에는 Anthropic 투자 이익 168.0억 달러가 인식됐고 FY2026Q2 기타수익은 534.1억 달러다. 이 중 Anthropic 몫은 별도 공시가 없고 '주로' Anthropic이라는 서술뿐이다. 지분 투자, 지출 약정, 평가이익이 서로 연결된 순환 구조여서 순이익 626.5억 달러의 질을 따로 해석해야 한다. 이 지적은 경영진의 의도가 아니라 구조에 대한 것이다. 이 구조의 판단은 회계 분석가의 몫이다. [F366] [F367] [F339] [F338] [F80] [S71](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic) [S48](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm)
- [capital_allocation] M&A 이력은 아직 쌓이는 중이다. 2026-04-14에 Globalstar를 약 116억 달러에 인수하기로 합의했다. 종결은 2027년 예상이고 Leo(위성) 직접-단말 서비스 확대와 연결된다. Leo의 총 프로그램 비용, capex, 매출은 공시되지 않았다. 따라서 이 인수의 수익률은 평가할 수 없다. 어닝콜에서도 Leo 비용 언급은 없었다. [F374] [S72](https://www.constellationr.com/insights/news/amazon-doubles-down-leo-acquires-globalstar-116-billion) [S62](https://www.webull.com/news/15364638750483456)

### 회계 품질 — watch

코드가 계산한 회계 품질 신호는 없고, 연간 기준 발생액 비율(C:accruals_ratio@FY2025 -8.6%)과 영업현금흐름 대비 순이익도 양호하다. 다만 숫자를 그대로 믿기 어려운 곳이 세 군데 있다. (1) FY2026Q2 순이익 626.5억은 영업외 이익 534.1억(주로 Anthropic 지분 평가이익)이 부풀렸고, 이는 현금이 아니며 Anthropic이 AWS 지출을 약정한 순환 구조와 연결된다. (2) FY2026Q2 영업이익 274.6억에는 관세 환급 6.0억과 에너지 계약 공정가치 이익 6.0억의 일회성이 들어 있다. (3) 최근 분기 매출채권이 전년 동기보다 훨씬 빠르게 늘었고, 부채와 부외 약정이 급증하며 FCF가 마이너스(-76.0억)로 돌아섰다. 회계 부정의 증거는 없어 red_flag는 아니다. 순이익은 평가이익을 빼고, 영업이익은 일회성을 빼고, FCF는 총 설비투자와 SBC 기준으로 조정해서 봐야 하므로 watch로 판정한다.

- [watch] FY2026Q2 순이익 626.5억의 상당 부분은 영업외수익 534.1억에서 나왔다. 이 항목은 '주로' Anthropic 지분 평가이익이지만 금액 분리는 공시되지 않았다. FY2026Q1에도 Anthropic 세전 이익 168억이 있었다. 같은 분기 영업현금흐름 453.9억은 순이익보다 작다. 이익의 질을 볼 때는 평가이익을 빼야 하며, PER 20.15배(C:pe)도 이 이익 때문에 낮게 나온다. 자본(F222)도 이 평가이익으로 부풀어 ROIC 등 장부 기준 수익률이 왜곡된다. [F80] [F338] [F339] [F90] [F222] [C:pe]
- [watch] Anthropic 순환 구조: 아마존이 지분을 투자하면(최대 330억) Anthropic이 AWS에 지출하겠다고 약정(1,000억 이상)하고, 아마존은 그 지분에서 평가이익을 인식한다. AWS 수주잔고와 매출 중 Anthropic 몫은 미공개라 AWS 성장과 수주잔고 4,960억의 독립성을 확인할 수 없다. 2차 자료 기반이므로 10-Q 원문 대조가 필요하다. [F366] [F367] [F317] [S71](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic)
- [watch] FY2026Q2 영업이익 274.6억에는 관세 환급 약 6억과 에너지 계약 공정가치 이익 약 6억의 일회성이 포함된다(2차 요약 기준). 경영진은 AWS 마진 개선분 650bp 중 파생상품 회계 이익을 빼면 520bp라고 밝혔다. 가이던스 상회(beat) 기록이 100%이지만 이 일회성을 빼고 해석해야 하며, 마진은 선형으로 개선되지 않을 수 있다고 경영진이 말했다. [F96] [F342] [F343] [F315] [F316] [S63](https://transcripts.platformaeronaut.com/summaries/AMZN-2Q26-AI-Summary)
- [watch] 매출채권이 FY2026Q2 880.9억으로 전년 동기 574.1억보다 크게 늘어, 같은 기간 매출 증가(2,006.1억 대비 1,677.0억)를 웃돈다. 코드 신호(receivables_gap)는 연간 기준이라 걸리지 않았지만, 분기 전년 동기 비교로는 격차가 크다. AWS 대형 계약 고객이나 Anthropic 관련 채권 증가일 가능성이 있으나 근거는 없다. 3분기 실적(10월 말)에서 DSO 추세를 확인해야 한다. [F265] [F262] [F108] [F105] [C:dso@FY2025]
- [watch] 재무 레버리지와 부외 약정이 빠르게 커지고 있다. 차입금은 FY2025Q2 507.2억에서 FY2026Q2 1,288.9억이 됐고, 상반기 차입이 670억이다. 7월 회사채 발행에서는 신규 발행 프리미엄이 필요했다. 부외 약정 약 2,860억과 총 약정 약 6,500억은 블로그 2차 수치라 10-Q Note 4 원문 대조 전까지는 확정하지 않는다. 회사 정의 TTM FCF는 -76.0억으로 돌아섰고, 코드의 FCF 수익률도 음수다. [F194] [F191] [F360] [F365] [F364] [F348] [F363] [S67](https://fortune.com/2026/07/08/amazons-25-billion-surprise-bond-sale-dangled-extra-yield-to-lure-in-buyers/) [C:fcf_yield]
- [info] 설비투자 정의가 여러 개라 FCF를 비교할 때 혼동하기 쉽다. 회사 정의는 영업현금흐름에서 인센티브를 차감한 순 설비투자를 빼고, 코드는 총 설비투자를 쓴다. 콜에서 말한 현금 capex 531억과 현금흐름표 총 매입 542.1억도 정의가 다르다. 비교는 총 설비투자 기준(코드 FCF)으로 통일해 읽어야 한다. 일부 서버 내용연수를 6년에서 5년으로 줄인 것은 이익을 보수적으로 만드는 방향이다(2차 자료). [F149] [F347] [F345] [F346] [F344] [S62](https://www.webull.com/news/15364638750483456) [S64](https://www.levelheadedinvesting.com/p/amazon-com-inc-amzn-q2-2026-results-same-strategy-opposite-reaction)
- [info] SBC는 FY2025 194.7억으로 매출의 2.7%(C:sbc_to_revenue@FY2025), 영업현금흐름의 14.0%(C:sbc_to_ocf@FY2025)이며 문턱을 한참 밑돈다. 다만 총 설비투자 기준 FCF 77.0억에서 SBC를 빼면 -117.7억(C:fcf_after_sbc@FY2025)이므로 SBC 차감 FCF로 봐야 한다. 희석 주식 수 증가는 연 1.0%(C:share_change@FY2025)로 낮다. [F111] [F83] [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [C:fcf_after_sbc@FY2025] [C:share_change@FY2025]
- [info] 감사의견, 감사인 변경, 재무제표 정정, 특수관계자 거래는 별도 근거로 확인하지 못했다. 코드의 restatement·auditor_change 신호도 없다. 근거 부재이지 문제의 증거는 아니며, 영업권/총자산은 낮아(C:goodwill_to_assets@FY2025) 인수 회계 위험은 작다. 지속된 확인 대상은 Globalstar 인수(2027년 종결 예상)다. [F56] [F374] [C:goodwill_to_assets@FY2025] [C:accruals_ratio@FY2025]

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) AI 설비투자가 수요보다 앞서간 과잉 증설이었다. 2026년 capex 가이던스는 약 2,200억 달러로 올랐고 회사 정의 TTM FCF는 -76.0억 달러로 돌아섰다. 경영진도 데이터센터가 가동·수익화되기 전까지 FCF는 역풍이라고 했다. 용량 제약이 풀리자 경쟁사가 더 빨리 성장했다(구글 클라우드 +82%). 그 결과 감가상각이 매출보다 빨리 늘었고 FCF 마진이 회복되지 않았다. 시장은 FCF 배수를 낮췄다. 현재 가격은 이미 기본 시나리오의 FCF 마진 13% 달성을 가정한다. [F140] [F348] [F317] [S62](https://www.webull.com/news/15364638750483456) [S70](https://www.fierce-network.com/cloud/google-cloud-surges-alphabets-ai-capex-problem-grows) [C:implied_cagr@m13]
- (15%) AWS 수주잔고와 성장이 Anthropic·OpenAI 같은 소수 AI 연구소에 쏠려 있었고, 일부는 아마존의 지분 투자로 만들어진 순환 수요였다. Anthropic은 마이크로소프트 Azure와 구글 클라우드도 병행해 쓴다. 이들이 지출을 줄이거나 자금 조달이 막히면 AWS 가속(+36.7%)이 꺾인다. 증설한 용량이 비고, 4,960억 달러 수주잔고의 실제 전환율이 낮았음이 드러난다. 수주잔고 고객 구성이 공시되지 않아 시장이 뒤늦게 알아챘다. [F317] [F310] [F366] [F367] [S71](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic) [S69](https://tech-insider.org/azure-678-billion-backlog-earnings-2026/) [S70](https://www.fierce-network.com/cloud/google-cloud-surges-alphabets-ai-capex-problem-grows)
- (15%) 자금 조달이 병목이 되었다. 차입금은 FY2025 656.5억에서 FY2026Q2 1,288.9억 달러로 두 배가 됐다. 7월 250억 달러 회사채는 주문이 3월보다 적었고 신규 발행 프리미엄이 필요했다. 9월에는 통화를 넓혀 파운드채까지 준비했다. 증설을 계속하려면 외부 자금이 필요한데 FCF는 음수다. 금리가 오르거나 신용 스프레드가 벌어지면 이자 부담이 늘고, 증설을 줄이면 수주잔고를 못 채운다. 어느 쪽이든 주주 몫이 줄어든다. [F26] [F194] [F360] [F362] [F363] [S66](https://www.investing.com/news/stock-market-news/amazon-launches-eightpart-us-investment-grade-bond-offering-4779013) [S67](https://fortune.com/2026/07/08/amazons-25-billion-surprise-bond-sale-dangled-extra-yield-to-lure-in-buyers/) [S68](https://techeconomy.ng/amazon-sterling-bond-sale-ai-spending-220-billion)
- (15%) 이익의 질이 무너졌다. 낮아 보이는 PER 20.15배는 Anthropic 평가이익이 부풀린 순이익 위에 있다. FY2026Q2 영업이익에도 관세 환급과 에너지 파생이익이라는 일회성이 섞여 있다. 평가이익과 일회성을 빼면 영업이익 개선이 선형이 아니라고 경영진이 말한 대로 AWS 마진이 정체했다. 시장이 이익을 다시 계산하자 '저평가'가 사라지고 배수가 내려왔다. 기본 시나리오 수익률 분해에서도 마진 확대가 +49.9%를 떠받치는 반면 멀티플은 -53.1%를 깎는다. [F338] [F80] [F342] [F343] [F315] [F316] [S63](https://transcripts.platformaeronaut.com/summaries/AMZN-2Q26-AI-Summary) [C:pe]
- 약한 가정 `base.fcf_margin`: 기본 시나리오는 FCF 마진이 FY2025의 1.1%에서 2030년 13%로 오른다고 본다. 이는 FY2024의 5.2%보다도 훨씬 높다. 회사 정의 TTM FCF는 이미 -76.0억 달러이고 2026년 capex는 약 2,200억 달러로 올랐다. 기본 시나리오 연도별 FCF 마진 경로에는 감가상각이 매출보다 빨리 늘어나는 효과와 메모리 가격 상승이 들어 있지 않다. 이 한 가정이 틀리면 기본 시나리오 가치 전체가 무너진다. [C:fcf_margin@FY2025] [C:fcf_margin@FY2024] [F348] [F140] [C:implied_cagr@m13]
- 약한 가정 `base.exit_multiple`: 기본·강세 시나리오는 5년 뒤 출구 P/FCF를 각각 25배·28배로 둔다. 현재 TTM FCF가 음수여서 P/FCF 자체가 산출되지 않으므로 이 배수에는 현재 시장 값의 앵커가 없다. 약세 시나리오는 16배다. 출구 배수 하나가 기본 시나리오 수익률을 가장 크게 움직이고, 민감도 표에서 배수 ×0.75만으로도 기본 시나리오 연 수익률이 +10.2%에서 +4.7%로 내려간다. [C:p_fcf] [C:fcf_yield]

## 검증 (L6)

주장 70개 — supported 61 · unsupported 4 · contradicted 1 · leap 4 · 미검증 0

- [contradicted] 모델러: AI 증설이 수요보다 앞서가는 경우다. 2026년 capex는 약 2,200억 달러까지 올랐는데, 서버 회수 기간이 3년을 조금 넘는 수준에서 더 길어지고 수주잔 — 자료의 서버 손익분기는 '3년 조금 못 미침'인데 주장은 '3년을 조금 넘는 수준'이라고 써서 방향이 다르다. 나머지 사실(capex 2,200억, TTM FCF -76억, 수주잔고, 차입금)은 맞다.
- [unsupported] 슬레이터: 레드팀의 가장 강한 논거는 기본 시나리오 FCF 마진 13%와 출구 배수 25배에 현재 앵커가 없다는 점이다. 인정한다. 그래서 FCF 마진 가정에 기대지 않고  — 없는 근거 인용: C:p_fcf
- [leap] 앤더슨: 슬레이터의 가장 강한 논거는 입증된 회수가 아니라 입증되고 있는 회수이므로 작게 시작하고 증거로 키우자는 것이다. 방향에는 동의한다. 다만 그가 기다리는 증거는  — 수주잔고·capex·AWS 영업이익은 맞지만, 병목이 '수요가 아니라 전력과 칩'이라는 결론은 자료에 명시되어 있지 않다.
- [leap] 앤더슨: 수요가 공급을 앞선다. AWS 수주잔고는 4,960억 달러이고, 경영진은 2026년과 2027년 모두 수요를 다 맞출 용량이 없으며 2027년 용량 대부분이 이미 — 수주잔고와 용량 부족 발언은 맞지만, 매출 두 배에 필요한 것이 전력과 칩 공급이라는 결론은 자료에서 따라 나오지 않는다.
- [leap] 애크먼: 사업의 질은 인정한다. AWS 매출이 36.7% 성장했고 영업이익이 166.2억 달러다. 그러나 순이익 626.5억 달러는 영업현금흐름 453.9억 달러보다 크고 — AWS 지표, 순이익 626.5억과 OCF 453.9억은 맞지만, 영업외수익 534.1억이 '주로 Anthropic 평가이익'이라는 귀속은 인용 자료에 없다.
- [unsupported] 레드팀: 기본·강세 시나리오는 5년 뒤 출구 P/FCF를 각각 25배·28배로 둔다. 현재 TTM FCF가 음수여서 P/FCF 자체가 산출되지 않으므로 이 배수에는 현재  — 없는 근거 인용: C:p_fcf
- [leap] 앤더슨: 시장이 요구하는 것은 대담하지 않다. 역DCF는 목표 FCF 마진 15%일 때 10년간 연 12.1% 매출 성장만을 요구한다. 강세 case(5년 연 14.8%  — 코드 값(12.1%, 5.47배, 컨센서스 차이 -0.1%)은 바르지만, 컨센서스 매출이 기본 시나리오와 같다는 것만으로 강세 상방이 가격에 반영되지 않았다는 결론은 따라 나오지 않는다.
- [unsupported] 앤더슨: 애크먼의 가장 강한 논거는 기본 시나리오 기준 안전마진이 거의 없다는 것이다. 그 계산은 맞다. 하지만 그것은 5년 뒤 출구 배수로 현재를 재는 도구다. 내가 묻 — 없는 근거 인용: C:fcf_company_ttm
- [unsupported] 애크먼: 레드팀의 약한 고리인 기본 시나리오 FCF 마진 13%와 출구 배수 25배를 받아들인다. 출구 배수를 0.75배로 낮추면 기본 시나리오 연 수익률이 +10.2%에 — 없는 근거 인용: C:p_fcf

## 사용자 견해 대조 (분석이 끝난 뒤에만 비교한다)

- 사용자 찬성 vs 하네스 찬성 우세 — 일치
- 사용자 주장 (하네스가 검증하지 않음): 그 자체로 좋은 사업이다
- 사용자 주장 (하네스가 검증하지 않음): 피지컬 AI로 로보틱스 물류가 실현되면 마진이 전폭적으로 개선될 옵션이 있다
- 사용자 주장 (하네스가 검증하지 않음): 아웃라이어 상방 옵션이 있는 기업을 놓치는 것보다 값을 지불하는 것이 낫다

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| 매출 (revenue) | 4,698.2억 USD | 5,139.8억 USD | 5,747.9억 USD | 6,379.6억 USD | 7,169.2억 USD |
| 매출 성장 (revenue_growth) | — | 9.4% | 11.8% | 11.0% | 12.4% |
| 총이익률 (gross_margin) | 42.0% | 43.8% | 47.0% | 48.9% | 50.3% |
| 영업이익률 (operating_margin) | 5.3% | 2.4% | 6.4% | 10.8% | 11.2% |
| 순이익 (net_income) | 333.6억 USD | -27.2억 USD | 304.2억 USD | 592.5억 USD | 776.7억 USD |
| 영업현금흐름 (ocf) | 463.3억 USD | 467.5억 USD | 849.5억 USD | 1,158.8억 USD | 1,395.1억 USD |
| 설비투자 (capex) | 610.5억 USD | 636.5억 USD | 527.3억 USD | 830.0억 USD | 1,318.2억 USD |
| FCF (fcf) | -147.3억 USD | -168.9억 USD | 322.2억 USD | 328.8억 USD | 77.0억 USD |
| FCF 마진 (fcf_margin) | -3.1% | -3.3% | 5.6% | 5.2% | 1.1% |
| FCF/순이익 (fcf_conversion) | -0.44x | — | 1.06x | 0.55x | 0.10x |
| SBC (sbc) | 127.6억 USD | 196.2억 USD | 240.2억 USD | 220.1억 USD | 194.7억 USD |
| SBC/매출 (sbc_to_revenue) | 2.7% | 3.8% | 4.2% | 3.5% | 2.7% |
| SBC/영업현금흐름 (sbc_to_ocf) | 27.5% | 42.0% | 28.3% | 19.0% | 14.0% |
| SBC 차감 FCF (fcf_after_sbc) | -274.8억 USD | -365.1억 USD | 81.9억 USD | 108.7억 USD | -117.7억 USD |
| ROIC (roic) | 21.3% | 6.6% | 16.0% | 22.4% | 17.7% |
| 순현금 (net_cash) | 458.1억 USD | -1.2억 USD | 199.7억 USD | 435.6억 USD | 546.3억 USD |
| 순부채/EBITDA (net_debt_to_ebitda) | -0.77x | 0.00x | -0.23x | -0.36x | -0.37x |
| 희석 주식 수 (diluted_shares) | 103.0억 | 101.9억 | 104.9억 | 107.2억 | 108.3억 |
| 주식 수 변화 (share_change) | — | -1.0% | 3.0% | 2.2% | 1.0% |
| DSO(일) (dso) | 25.6 | 30.1 | 33.2 | 31.7 | 34.5 |
| DIO(일) (dio) | 43.7 | 43.5 | 39.9 | 38.3 | 39.2 |
| 발생액 비율 (accruals_ratio) | — | -11.2% | -11.0% | -9.8% | -8.6% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, cost_of_revenue, d_and_a, debt, debt_current, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, goodwill, goodwill_to_assets, gross_profit, income_tax, interest_expense, inventory, inventory_growth, operating_income, receivables, receivables_growth, short_term_investments, total_assets

### 시장 · TTM(FY2026Q2) 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 250 USD/share (2026-10-16, F156) |
| 희석 주식 수 (shares) | 109.0억 |
| 시가총액 (market_cap) | 2.73조 USD |
| 순현금 (net_cash) | -92.4억 USD |
| EV (ev) | 2.73조 USD |
| FCF 수익률 (fcf_yield) | -0.4% |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 3.53x |
| PER (pe) | 20.15x |
| 순부채/EBITDA (net_debt_to_ebitda) | 0.05x |
| 현금 소진 연수 (runway_years) | 10.6 |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 가이던스 적중 (C:guidance_hit_rate = 100%)

- revenue FY2026Q1: 가이던스 1,755.0억 → 실제 1,815.2억 = beat [F154, F107]
- operating_income FY2026Q1: 가이던스 190.0억 → 실제 238.5억 = beat [F155, F95]
- revenue FY2026Q2: 가이던스 1,965.0억 → 실제 2,006.1억 = beat [F357, F108]
- operating_income FY2026Q2: 가이던스 220.0억 → 실제 274.6억 = beat [F358, F96]

### 역DCF — 현재 가격이 가정하는 것

EV 2.73조 USD를 정당화하려면 매출이 10년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 목표 마진으로 직선 수렴, 할인율 10%, 이후 영구성장 3%.
기본 시나리오 목표 마진 13% 기준: 연 13.8% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 17.1% | C:implied_cagr@m10 |
| 13% | 13.8% | C:implied_cagr@m13 |
| 15% | 12.1% | C:implied_cagr@m15 |
| 20% | 8.6% | C:implied_cagr@m20 |
| 25% | 5.9% | C:implied_cagr@m25 |
| 30% | 3.8% | C:implied_cagr@m30 |

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 30% | 1.07조 USD | 8.3% | 6% | 16x | 103.58 | 64.31 | -16.2% |
| 기본 | 50% | 1.28조 USD | 12.3% | 13% | 25x | 406.20 | 252.22 | +10.2% |
| 강세 | 20% | 1.43조 USD | 14.8% | 18% | 28x | 700.81 | 435.15 | +22.9% |

확률 가중: 주당 가치 374.33 · IV 232.43 · 기대 연 수익률 +8.4% (C:expected_irr) · 손실 확률 30% (C:p_loss) · 현재 주가 250.00

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +11.6% · 마진 변화 +49.9% · 멀티플 변화 -53.1% · 주식 수 변화 -0.8% · 현금 축적 +2.1% = +9.7%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -0.4% | +4.8% | +9.1% |
| +0%p | +4.7% | +10.2% | +14.8% |
| +5%p | +9.8% | +15.6% | +20.4% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 8,280.5억 USD | 3.5% | 286.4억 USD | 109.9억 | 194.0억 USD |
| FY2027 | 9,356.9억 USD | 5.8% | 546.8억 USD | 110.8억 | 740.9억 USD |
| FY2028 | 1.05조 USD | 8.2% | 862.4억 USD | 111.7억 | 1,603.3억 USD |
| FY2029 | 1.16조 USD | 10.6% | 1,234.8억 USD | 112.6억 | 2,838.0억 USD |
| FY2030 | 1.28조 USD | 13.0% | 1,663.5억 USD | 113.5억 | 4,501.5억 USD |

### 컨센서스 대비 (C:consensus_diff@지표@기간)

| 지표 | 기간 | 컨센서스 | 기본 시나리오 | 차이 |
|---|---|---|---|---|
| revenue | FY2026 | 8,289.0억 USD | 8,280.5억 USD | -0.1% |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 13.8% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 12.3% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 14.8% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=5.47x, revenue_5y=1.99x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=1,229.9억 USD, runway_years=10.6
- 애크먼 case={"from": "base"}: price=250.0, fcf_positive=아니오, net_debt_to_ebitda=0.05x, leveraged=아니오, intrinsic_value=252.2, mos=0.9%

### 계산 경고

- 낡은 컨센서스 — F141: capex FY2026 컨센서스 2.061e+11가 회사 가이던스 하단 2.2e+11(F140)보다 낮다 — 갱신 전 값으로 보고 제외
- 모델이 컨센서스와 사실상 같다 — variant perception이 없다면 알파도 없다
- 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-09-14 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1018724/000110465926107526/tm2624614d5_8k.htm) |  |
| S2 | filing | 2026-09-09 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000036/amzn-20260908.htm) |  |
| S3 | filing | 2026-07-31 | [10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm) |  |
| S4 | filing | 2026-07-30 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260730.htm) |  |
| S5 | filing | 2026-07-09 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1018724/000110465926082293/tm2619352d4_8k.htm) |  |
| S6 | filing | 2026-06-12 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1018724/000110465926073562/tm2613616d5_8k.htm) |  |
| S7 | filing | 2026-06-10 | [8-K 중요 계약](https://www.sec.gov/Archives/edgar/data/1018724/000110465926072140/tm2613616d4_8k.htm) |  |
| S8 | filing | 2026-05-22 | [8-K](https://www.sec.gov/Archives/edgar/data/1018724/000110465926065717/tm2614288d1_8k.htm) |  |
| S9 | filing | 2026-04-30 | [10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm) |  |
| S10 | filing | 2026-04-29 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000012/amzn-20260429.htm) |  |
| S11 | filing | 2026-04-14 | [8-K IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1018724/000110465926042880/tm2611746d1_8k.htm) |  |
| S12 | filing | 2026-04-09 | [8-K IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1018724/000110465926041034/tm263815d2_8k.htm) |  |
| S13 | filing | 2026-04-09 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1018724/000110465926041026/tm261382-1_def14a.htm) |  |
| S14 | filing | 2026-03-16 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1018724/000110465926028556/tm266670d9_8k.htm) |  |
| S15 | filing | 2026-03-13 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1018724/000110465926027729/tm266670d8_8k.htm) |  |
| S16 | filing | 2026-02-27 | [8-K 중요 계약 IR·컨퍼런스 자료 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1018724/000110465926021050/tm267374d1_8k.htm) |  |
| S17 | filing | 2026-02-06 | [10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm) |  |
| S18 | filing | 2026-02-05 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20260205.htm) |  |
| S19 | filing | 2025-11-20 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1018724/000110465925114647/tm2530638d3_8k.htm) |  |
| S20 | filing | 2025-10-31 | [10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000123/amzn-20250930.htm) |  |
| S21 | filing | 2025-10-30 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000121/amzn-20251030.htm) |  |
| S22 | filing | 2025-05-02 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000036/0001018724-25-000036-index.htm) |  |
| S23 | filing | 2025-08-01 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000086/0001018724-25-000086-index.htm) |  |
| S25 | news | 2026-07-30 | [Amazon hikes 2026 capex to $220 billion due to higher memory costs - CNBC](https://news.google.com/rss/articles/CBMifEFVX3lxTE5YU3ZKX2xoamdmZWNkOE52VGdqb3VtQTFUTXl1S0hwdWFZNGlNTE1SMGNjZlR1MXpVN2lINkVwd1VoWEdkTGFmcFItRTlxVFIyUkhwYlJCM3l5T29aYjhUM0tRSjdYNGVZY3c5eHBqVTNpVmR4aEdSTXJtd1HSAYIBQVVfeXFMTVhaMjBSNjI0eXFRb3NsNUxJNzNlalZvUjRUQkpmSFNkMGJtUVVGS19PN1JLdWpmMEdJaVVvR1B4S1dDN0NUM3dpcWRqdmxiZjdDakUzblV0TmU2QVI0UzRWNldDS3F0MC1DWGU2MUEydXV5c0lYYWI5bFA3WlJoSFhSZw?oc=5) | CNBC |
| S26 | news | 2026-07-30 | [Amazon to boost spending on AI and other technology by $20 billion after strong Q2 results - AP News](https://news.google.com/rss/articles/CBMinAFBVV95cUxPYWNwWXZRNEt4SjNsc2hzSThoZ2ZSYktrQ0JZdUdLN3owZnVXRkpXVm5DSXhMTVZYTHdTWk1FWWVhUEtpWE0zWGRMaHlHdi01YXh1Sm9KNXJDUWcxVmNIT3YwWlJaM2U0dDJDQWtQWmVkeTBCWWZWMzczdy14My1NMWUzbFo0S0tDc0V3Ulg4dlVrWjNoNTFOSkpoRmc?oc=5) | AP News |
| S28 | news | 2026-08-19 | [Amazon Prime Air drone delivery is expanding to nearly 500 US cities and towns this year - About Amazon](https://news.google.com/rss/articles/CBMikwFBVV95cUxQR1FIZVdwZWpWd2FwTHliRUprMC1IVl9DWnpzVmNTeTFvUHh0NEZGNFVvNGk0aHh0NFUtV0pNNjQyZFp5ZG1BZkVnYVlMQlk2ZWJOSWhvSHdPTk92SHdNN0tGWnVEV1dNcEplYzBvNVpoWl91Y2hHdnVpWF9zWDE1UUpNU2dWREVsQkxsSXRNbXhUUXc?oc=5) | About Amazon |
| S30 | news | 2026-10-02 | [The race our nation can’t afford to lose, plus a new commitment from us and a fresh set of community investments - About Amazon](https://news.google.com/rss/articles/CBMihwFBVV95cUxQSmVvOXNHN3ROUU96WTF0R3hKSnhDcFNXclNzUzBNMEM1bngzV044M3VNdUFNWkJVYjhlcTc3enNfbkV3MTRBNE9CVzUwUURTYThWazJnX2x6MmtWNjZnWXB2bGFZNjhxMjVzZU9Id0lqWnA5SHR5NDl0OVFlS1hROURLOU1qRlE?oc=5) | About Amazon |
| S31 | news | 2026-10-15 | [Amazon introduces 2 new AI products from Bee: Bee Frontier and Bee Eclipse - About Amazon](https://news.google.com/rss/articles/CBMijAFBVV95cUxPS056WlBEQzdVTUZLVy1hUDU3cF80SVEyU0xQNDFlYmU4cG5kY0lUQnpFYlhrMEpQRWNiV1dCeTJxZmRoc2NQd3hjSkdtNGhaVWpQMlM5amdXNlNvdDY2SjdiZHc3ZVN3emNXZmlJUW9NLTJ2WVczVE01cXRwVElrR0gtSkJueWZKQzhfRw?oc=5) | About Amazon |
| S32 | news | 2026-08-31 | [Amazon’s response to the FTC’s lawsuit regarding Sponsored Ads - About Amazon](https://news.google.com/rss/articles/CBMiigFBVV95cUxNN1RnMWxFWmtqTEJZNmtTNmVHdGZhUXhVbEVTenNKam8xZmtIVGNfQlYwRlY2anZ1ZXZWc1RDUW9DUFc2endnM1pOdU13c2I0RExUUGNrVFlvajZFWk8wNHZDQVdLR0JNc0wxeG1Lb05mektkVnVhejRsd1oxSG1jNGxBVWhoY2xkSHc?oc=5) | About Amazon |
| S33 | news | 2026-07-27 | [How Amazon Leo plans to connect mobile devices from space - About Amazon](https://news.google.com/rss/articles/CBMioAFBVV95cUxNajdxUy1zYmtPMHN6ZU5UQVlIc0VZckkwdU4ySVVFakY0QUItTmdCeFRESmxXejVCdzJwbGpKSEtLRGpTQmtmUVNkN19vOVkzcXg2eUY5emNweVg3SWpOZVVIOWo5TDFRcmxTdUZJVWhPSzUycTdOTFdNMjlyRnRGRlVqYzVwd09LRUt1ZWpVZzEzRFJxMENOWVdfNEVRckl6?oc=5) | About Amazon |
| S36 | news | 2026-09-23 | [Amazon gives sellers an even smarter Seller Assistant and a new plugin for Amazon Quick and Anthropic’s Claude - About Amazon](https://news.google.com/rss/articles/CBMingFBVV95cUxQaUJEMEhNVjVhWlBoRXNvX0FlWEtZMUxyRGZXekdwR2NVcjhTSWZYd0phakF5N3N3Q3FuN2F3UV91SW9McFY3c1REZmhpTmE0NVR0RkFVT1FJSFNBWFNEX0FJV2czQ0VvOWkxY2J3U0RVUjBSV3NzQzA5eUxXTTJ3SjdBQWNwQ2dJbklNWlkwV2N6SUJfSzhwTWdaU2p3Zw?oc=5) | About Amazon |
| S37 | news | 2026-08-26 | [AWS to acquire DuckLabs, the Amsterdam-based company behind DuckDB - About Amazon](https://news.google.com/rss/articles/CBMiakFVX3lxTE40S2JJbEVhVWJaQUs0eUFDdTFvbjNGTFppdDRGUlVxaEhGU1BxdkZLdlU5bkp5Nk5yZWlQQlEzMUhWMDFSLU9GR21uRW8tcVFhNlltWU1rOXVQVW1qdVB4YmNFNHk5WDQzVEE?oc=5) | About Amazon |
| S39 | news | 2026-09-10 | [Amazon Leo adds 6 new Arianespace launches, expanding its launch partnership - About Amazon](https://news.google.com/rss/articles/CBMihgFBVV95cUxQZktuX0V0R0x5UzdGVWJBU3dhaWxoUHBYUmtEQUxhRDBwMHdQem9MVzk0RXZlMXRCd19ZMFByMWxfZG9qd3ZGX1k4ZUNZNXhnZV9nU04tRWVFbnFSOU1QN0w3dGpmU3Zjd1FWMnFycUp6Rlp0M0pnOXRPV0VNSWtXTjlnbTVfQQ?oc=5) | About Amazon |
| S40 | news | 2026-09-24 | [Sellers can now manage sales across Amazon, eBay, Shopify, TikTok, and Walmart from Seller Central - About Amazon](https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ3lUWUszZ0lhaXRhM0FRb2hvTjA2QlBINWhKbEcydkpSRW5uak1jeUZfVGYxUzcyRE55SDNfZHQ0UHF3OW1ab0h4TExxTG5zMmF3YTQyZlA4NWZOVXJmNnhUZC1hb1cySzdyY0NMcURIc0JoQnRKU1puYnhULXRpbkdQLUd3R1h4WDdiSlp6THBWX2doTmFQRUgxX3U?oc=5) | About Amazon |
| S41 | news | 2026-09-09 | [Cybersecurity expert Kevin Mandia joins Amazon's Board of Directors - About Amazon](https://news.google.com/rss/articles/CBMijAFBVV95cUxNdHVLaG9jX1A0Qk81YV92YzFwVDBlTnRTamtSaS1DUnFnQ0hRdWRzcktUeXIwc1h6dW9MY1ZaeDdNNkRSY0Q2UDRfUnlPY0VULUxyMGNfOXBDbVJlRTFQcDd0N1BjMWZJSHFGRW13NHRMeU0wQjloaGY1d3dzWFRtSHIyajZuMUJJTlZseg?oc=5) | About Amazon |
| S44 | data | 2026-10-13 | [Amazon Stock News (Oct 14, 2026): AMZN Falls 0.4% to $258.58](https://www.heygotrade.com/en/news/amazon-amzn-stock-news-october-14-2026/) | AMZN 2026-10-13 종가 $258.58 (전일 대비 -$0.95, -0.37%). 2차 자료(시세 요약). 10-14~10-16 종가는 찾지 못함 |
| S45 | data | 2026-08-01 | [Amazon post-Q2: AWS reaccelerates as AI investment pushes capex higher - S&P Global Market Intelligence](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/amazon-postq-aws-reaccelerates-as-ai-investment-pushes-capex-higher) | FY2026 매출 컨센서스 약 $828.9B (실적 후 +0.5% 상향), 3분기 매출 컨센서스 약 $202B. Visible Alpha 실적 전 컨센서스: 3분기 매출 $203.9B, 영업이익 $25.4B, 2026 capex $206.1B. 날짜는 8월 기사로 추정. 단일 출처, 2027 컨센서스 없음 |
| S46 | filing | 2026-02-05 | [Amazon 8-K Exhibit 99.1 — Q4 및 FY2025 실적 발표문](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm) | FY2025Q4 매출 213,386백만, 영업이익 24,977백만, 영업현금흐름 54,459백만, 설비투자(purchases of property and equipment) 39,522백만. FY2025 연간 영업현금흐름 139,514백만, 설비투자 131,819백만. AWS Q4 매출 35,579백만, 영업이익 12,465백만. 2026년 1분기 가이던스: 매출 173,500~178,500백만, 영업이익 16,500~21,500백만 |
| S47 | filing | 2026-04-29 | [Amazon 8-K Exhibit 99.1 — 2026년 1분기 실적 발표문](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000012/amzn-20260331xex991.htm) | FY2026Q1 매출 181,519백만, 영업현금흐름 26,032백만, 설비투자 44,203백만 |
| S48 | filing | 2026-07-30 | [Amazon 8-K Exhibit 99.1 — 2026년 2분기 실적 발표문](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm) | FY2026Q2 매출 200,606백만, 영업현금흐름 45,387백만(TTM 161,403백만), 설비투자 54,208백만(상반기 98,411백만, TTM 173,028백만). AWS Q2 매출 42,232백만, 영업이익 16,621백만. 3분기 가이던스 매출 197,000~202,000백만, 영업이익 22,500~26,500백만. 수주잔고(backlog) 수치는 발표문에 없음. Graviton 매출 약정이 전 분기 대비 약 3배 증가했다고 서술 |
| S49 | filing | 2025-10-30 | [Amazon 8-K Exhibit 99.1 — 2025년 3분기 실적 발표문](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000121/amzn-20250930xex991.htm) | FY2025Q3 매출 180,169백만, 영업현금흐름 35,525백만, 설비투자 35,095백만(3분기 누적 92,297백만) |
| S50 | data | 2026-10-16 | [Yahoo Finance AMZN historical prices](https://finance.yahoo.com/quote/AMZN/history/) | 2026-10-16 종가 250.0 USD |
| S51 | filing | 2024-02-02 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/0001018724-24-000008-index.htm) |  |
| S52 | filing | 2025-02-07 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/0001018724-25-000004-index.htm) |  |
| S53 | filing | 2023-02-03 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1018724/000101872423000004/0001018724-23-000004-index.htm) |  |
| S54 | news | 2026-10-08 | [Introducing all-new Amazon Alexa Tablets—powerful tablets with Alexa+ built in - About Amazon](https://news.google.com/rss/articles/CBMiggFBVV95cUxNUkRnQVVzRnhxTms2bEEwZ1BKVGt3NzRSS0hGVmZ3R0Qzd3E5VjB4MjdpN1V5Vkp2b3lQb3pZNk1IRk10ZmpXMzVOYVNQRlM3ZE1qVmRjWHh5Y2t0bDZEZ09FclZkOEJuV1pFc2FqdnI0MUFtMzhPV3hCY3JGOTJSWDJR?oc=5) | About Amazon |
| S55 | news | 2026-07-31 | [Amazon sued by consumers over seafood sustainability claims - Reuters](https://news.google.com/rss/articles/CBMiugFBVV95cUxOWmp1amEwUVhDdUFSOEhuZV9fZDl1eHRFbXEzY3d6NUlrbnNyNEN6VG16eUZ4VWVHNGhsQjUtbHZIVjM0bEN6bEREVnlqZE12YUpOcGQ3QTRTcXdfNWt4SzRDWGNxOUJuV29uTXp3cUZpSUg4QzBzMXpheEx1bmNmdk9RWlo0MlJsNWk3M185SWFfZU9aV3pqbmJxWEc0SjNyck9VUWVseUtpcVpNZVl0bGhZWWZ1a3NpYnc?oc=5) | Reuters |
| S56 | news | 2026-10-01 | [Amazon introduces a completely redesigned Kindle family - About Amazon](https://news.google.com/rss/articles/CBMicEFVX3lxTFBLV0JvcFVJYWJhamRudmVSbVR2cTdKMVBkUVd5NXlRUkdiSUo5MFJjZUhmbUM5NldQMGNicHZNQ3dDM0ZicUxnSDlMWlNGaDFRb0ZTOEU5LURaTEJIbDE4bnh2Wk43QkRyNHVvX3ZrYzE?oc=5) | About Amazon |
| S57 | news | 2026-09-29 | [Fire TV launches all-new, faster 4K stick and new remote design - About Amazon](https://news.google.com/rss/articles/CBMid0FVX3lxTE5hNHBsRzI2RXdpR2FUbkpiYzFxQ3ctaXAyRHdtdldVMEJZdnFSMy03dS1oR0lUQVZoaU1GOWUxQmwyVWJMeC1oS1pXVXN2dzhZM2kyY245ZUtEYXExMkplbkZVdEFJa2VvNUpkS2ItSUFsRV96cE40?oc=5) | About Amazon |
| S58 | news | 2026-09-01 | [Is that message really from Amazon? Just ask Alexa for Shopping. - About Amazon](https://news.google.com/rss/articles/CBMikgFBVV95cUxQb090UVQyOFZlQnJqSS1RSUl3Z01RNmN6YXdMM1hyRG9rOFFDcE5uXzE3UF90YjBtOHhvLWhXYUFtZXhQSlFMZDhoUHprMVg4aUJXaHZ4ZUNJSHU0d2pWam9Nb3pQUV9sLTRRbmxrcmZYanlVNWNBQmVFUjR4bEFTd0dzZVVpeHF1R1JydVBxaFRFZw?oc=5) | About Amazon |
| S59 | news | 2026-10-07 | [Ring ends smart lock anxiety with a lock you can recharge by hand - About Amazon](https://news.google.com/rss/articles/CBMifkFVX3lxTE9BUmRhMl83ZVgtaHVuZnM2OGxGSW85UUJvd1hqMmhnS0NpT1g3UTFlWGZRck43UjBKX1gyNzQtdHl4ek12RjE0NTJOYUxwMVVJRTFtVEtZN0JUOWhlYlI3ZE9Hckc2RE5IbmZxWXFNOXl2YmFHNGFaQ1d5dXk0UQ?oc=5) | About Amazon |
| S60 | news | 2026-09-10 | [The Prime Video Shop the Show Experience Introduces New Features and Expands Across Thousands of Titles - About Amazon](https://news.google.com/rss/articles/CBMi5wFBVV95cUxNS2ZTbDJXN2pPck1tWkh2SkNzSGNpR0tEaWVMN3BmOUplS01VUW9TODZxbEZlRUsxTWVzTXoxOFpMY0RUQUJPOWh0SThBUWdobDZzb2E4X2RLRnVIZzRzeHB3NjlIM29yYmRjN3VvbndPcnc2UmZjT2JIaU9EZEpjOE9WYk5tTmtlYnZRdkRUOF9wWUlsVUFQQzk0YnZsLWdnWUNZVDJYQ1YwYmNRRUE4ZDB6MUotSVJySlpfYXplRXg5U2s4MHJwbWM5ajk3Uk5WRWM5d3VSX2NnWDFRVWpxZ1dUaXgyQ1E?oc=5) | About Amazon |
| S61 | news | 2026-10-08 | [Amazon announces an all-new family of tablets designed just for kids - About Amazon](https://news.google.com/rss/articles/CBMickFVX3lxTE5feUQ3UGgxM0dJUWZWZ3FfWGRFRUFXX3ppSkZOR2dNRzRFN2VROFdYLWVRNnBabkVsS2ZXNDg0UGxYS3RfWmczUko1YTMtTXpYQVdBNnp2VkhRSm5hMGh2Wl9rYkZ6eWFKZThwbmRxWnprZw?oc=5) | About Amazon |
| S62 | call | 2026-07-30 | [Amazon Q2 2026 earnings call transcript (Webull)](https://www.webull.com/news/15364638750483456) | 2차(제3자 트랜스크립트, IR 원문 아님). 2026-07-30 2분기 어닝콜. Jassy: AWS 수주잔고(backlog) 4,960억 달러, 전년 대비 '세 자릿수' 증가. AWS 성장 36.7%. 2026년 현금 설비투자 가이던스 '약 2,200억 달러'(2월 약 2,000억에서 상향), 주된 이유는 메모리 가격 상승, 로보틱스·반도체·위성 등 비AWS 포함. 2분기 현금 capex 531억(Olsavsky, 현금흐름표 총 매입 542억과 다름), '대부분' AWS·생성형 AI(비율 미공개). Olsavsky: AWS 영업이익률 전년 대비 650bp 상승, 에너지 계약 파생상품 회계 이익 제외 시 520bp. 서버 손익분기 '3년 조금 못 미침', 내용연수 5~6년, 데이터센터 30년 이상. 2026년에도 수요를 다 맞출 용량이 없고 2027년도 같다고 예상, 2027 용량 '대부분 예약', 2025년 대비 2027년 말 전력 용량 2배 목표, 2027 capex 수치는 없음. FCF는 데이터센터 가동·수익화 전까지 '역풍', 올해 채권 발행했고 '다른 조달 방안 검토 중'. 칩 사업(Trainium+Graviton) 연 환산 250억 달러 돌파·세 자릿수 성장, Anthropic·OpenAI 다년·수 GW Trainium 약정, Uber·Pinterest 채택, AWS 밖 Trainium 판매 '실제 가능성'. 광고 198억(+26%, 스폰서드 프로덕트·프라임비디오 광고·스포츠 중계). 로봇 팔(Cardinal·Sparrow) 2026년 '두 배 이상'. 당일·익일 배송 40% 이상 증가, 중동발 연료비·운전기사 부족, 4월 FBA 유류할증. Leo 비용은 콜에서 언급 없음. Q3 가이던스(발표문): 매출 1,970~2,020억(+9~12%), 프라임데이가 대부분 대국에서 2분기로 옮겨 이를 빼면 성장률 약 400bp 높음, 환율 역풍 약 80bp, 영업이익 225~265억(에너지 파생 재평가 영향 미가정). |
| S63 | call | 2026-07-30 | [AMZN 2Q26 AI Summary (Platform Aeronaut)](https://transcripts.platformaeronaut.com/summaries/AMZN-2Q26-AI-Summary) | 2차(AI 요약, 2026-07-30 2분기 콜 대상). 2분기 영업이익 안에 관세 환급 약 6억 달러와 에너지 계약 공정가치 이익 약 6억 달러, 합계 약 12억 달러의 비용 감소 일회성. 전 세계 유료 판매 단위 +17%. 경영진: 영업이익률은 '변동할 수 있고' 개선이 '선형적이지 않을 수 있다'. |
| S64 | news |  | [Amazon.com Inc (AMZN) Q2 2026 Results: Same Strategy, Opposite Reaction (Levelheaded Investing)](https://www.levelheadedinvesting.com/p/amazon-com-inc-amzn-q2-2026-results-same-strategy-opposite-reaction) | 2차(개인 블로그, 게시일 미확인, 2026-07-31 이후). 10-Q Note 4 기준 총 계약 약정 약 6,500억 달러, 그중 약 2,860억 달러 부외(2차 — 10-Q 원문 대조 필요). AWS 수주잔고 가중평균 잔여기간 6.4년, 공시상 수주잔고 고객명 없음. 2026년 상반기 차입 약 670억 달러, 2분기 이자비용 13억(연 환산 약 52억). 2분기 종가 2026-07-31 271.58달러(당일 +15.3%). 일회성 제외 AWS 마진 약 38.2%, 북미 마진 약 7.3%(블로거 추정, 1분기보다 낮음). 북미 영업이익 전년 대비 +21%. 배송비 +19% vs 유료 단위 +17%(스프레드 -2pt, 2024년 4분기 +7pt가 고점). 일부 서버 내용연수 2025년 1월 6년→5년 단축, 공개된 회수기간은 건물 제외 서버만. 연 희석 약 1.18% 가정. 주가 259달러에서 TTM 영업현금흐름 17.6배, 10년 중앙값 25배, 적정가 약 428달러(의견). |
| S65 | news | 2026-07-31 | [AWS revenue growth outruns available AI capacity (Let's Data Science)](https://letsdatascience.com/news/aws-revenue-growth-outruns-available-ai-capacity-b0361d90) | 2차. 2026년 현금 설비투자 가이던스 '약 2,200억 달러'로 2월 약 2,000억에서 상향, Jassy는 메모리 비용 상승을 주된 이유로 듦. 총액에 로보틱스·반도체·위성(Leo) 등 비AWS 항목 포함. |
| S66 | news | 2026-07-07 | [Amazon launches eight-part US investment-grade bond offering (Investing.com)](https://www.investing.com/news/stock-market-news/amazon-launches-eightpart-us-investment-grade-bond-offering-4779013) | 보도. 2026-07-07 아마존 250억 달러 8개 트랜치 미국 달러 투자등급 회사채, 만기 3~40년. 스프레드 3년 고정 국채+40bp, 10년 +80bp, 40년 +125bp. 최대 주문 620억 달러로 3월 발행 때보다 '훨씬 적음'. 등급 A1/AA/AA-. 3월에는 370억 달러 '초대형' 회사채 발행. 아마존이 주관사에 2026년 달러 채권은 이것으로 끝이라고 전한 것으로 보도. |
| S67 | news | 2026-07-08 | [Amazon's $25 billion surprise bond sale dangled extra yield to lure in buyers (Fortune)](https://fortune.com/2026/07/08/amazons-25-billion-surprise-bond-sale-dangled-extra-yield-to-lure-in-buyers/) | 보도. 2026년 7월 250억 달러 깜짝 회사채 발행에서 투자자 유치를 위해 추가 금리(신규 발행 프리미엄)를 제시. 3월 발행보다 수요가 약해 조달 비용 상승 신호로 읽힘. |
| S68 | news | 2026-09-08 | [Amazon sterling bond sale as AI spending hits $220 billion (TechEconomy)](https://techeconomy.ng/amazon-sterling-bond-sale-ai-spending-220-billion) | 2차 보도. 2026년 9월 아마존 첫 파운드화 회사채 준비(만기 3~19년, 주관 JPMorgan·Barclays·HSBC·NatWest), 금액 미공개. 2026년 앞서 유로·캐나다달러·스위스프랑 채권도 발행했다고 언급, 금액 없음. 이 기사는 250억 달러 달러채를 8월·약 120bp로 적었으나 Investing.com·Fortune은 7월 7~8일로 보도 — 7월이 맞는 것으로 본다. |
| S69 | news |  | [Azure $678 billion backlog: Microsoft earnings 2026 (Tech Insider)](https://tech-insider.org/azure-678-billion-backlog-earnings-2026/) | 2차(경쟁사, 게시일 미확인). 마이크로소프트 FY2026 4분기(2026-07-29 발표): Azure 전년 대비 +43%, Microsoft Cloud 593억 달러(+27%), 상업용 RPO 6,780억 달러, 약 45%가 OpenAI 관련. RPO 증가율이 본문 +43%와 표 +84%로 충돌. 4분기에 용량 제약이 완화됐다고 보도. 마이크로소프트 발표문으로 대조하지 않았다. |
| S70 | news |  | [Google Cloud surges, Alphabet's AI capex problem grows (Fierce Network)](https://www.fierce-network.com/cloud/google-cloud-surges-alphabets-ai-capex-problem-grows) | 2차(경쟁사, 게시일 미확인, 약 2026-07-22 실적 대상). 구글 클라우드 2026년 2분기 매출 248억 달러(+82%), 영업이익 88억(마진 35.6%, 전년 20.7%), 수주잔고 5,140억 달러(2026년 1분기 4,600억, 2025년 2분기 1,060억). 알파벳 2026 capex 가이던스 1,800~1,900억, 2027년 '더 높음'. 알파벳 2분기 FCF -59억. TPU 시스템 판매 첫 매출 인식. 같은 분기 AWS 수주잔고 4,960억은 구글 클라우드(5,140억)와 마이크로소프트 상업용 RPO(6,780억)보다 작다. |
| S71 | news | 2026-04-27 | [Amazon commits up to $33B to Anthropic (Global Data Center Hub)](https://www.globaldatacenterhub.com/p/amazon-commits-up-to-33b-to-anthropic) | 2차. 2023~2025년 80억 달러 단계 투자에 이어 2026년 4월(04-20/21 발표) 프리머니 3,500억 달러 가치로 신규 지분 50억 + 상업적 마일스톤 연동 최대 200억, 합계 최대 330억 달러. Anthropic은 10년간 AWS에 1,000억 달러 이상 지출, 2036년까지 최대 5GW 컴퓨팅, 2026년 말까지 Trainium2/3 약 1GW 가동 예상. Project Rainier: 2025년 중반 Trainium2 약 50만 개로 완전 가동, 인디애나 1,200에이커·7개 건물, 2.2GW 증설 계획, 100만 개 이상으로 확장 계획. 멀티클라우드: 2025년 말 마이크로소프트·엔비디아가 Anthropic에 150억 투자, Anthropic은 Azure 컴퓨팅 300억 약정, 구글 클라우드도 사용. Anthropic의 AWS 매출 기여는 미공개. 순환 구조(아마존 지분 투자 → Anthropic의 AWS 지출 약정 → 지분 평가이익) 주의. |
| S72 | news | 2026-04-14 | [Amazon doubles down on Leo, acquires Globalstar for $11.6 billion (Constellation Research)](https://www.constellationr.com/insights/news/amazon-doubles-down-leo-acquires-globalstar-116-billion) | 2차. 2026-04-14 아마존이 Globalstar를 약 116억 달러에 인수 합의. 주주는 주당 현금 90달러 또는 AMZN 0.3210주(상한 있음) 선택, 2027년 종결 예상. 애플과 합의해 Globalstar 기반 아이폰·워치 위성 서비스를 아마존 Leo 직접-단말(D2D)로 유지. Leo 총 프로그램 비용·capex·매출은 공시되지 않음. |
| S73 | news | 2026-03-10 | [Amazon trades at premium P/E: time to hold or fold the stock? (Zacks via Nasdaq)](https://www.nasdaq.com/articles/amazon-trades-premium-p-e-time-hold-or-fold-stock) | 2차, 6개월 이상 지난 자료(오래됨). 2026년 1분기 가이던스에 '아마존 Leo 관련 전년 대비 약 10억 달러 추가 비용' 포함. 2월 2026 capex 가이던스 '약 2,000억 달러'는 2025년 1,318억 대비 약 +53%. AWS 성장 2025년 3분기 +20%, 4분기 약 +24%. 당시 2026 EPS 컨센서스 7.78달러, 선행 PER 26.5배(업종 21.8배) — Anthropic 평가이익으로 이미 낡은 값. |
| S74 | data | 2026-09-07 | [Amazon share price forecast (Capital.com)](https://capital.com/en-gb/market-updates/amazon-share-price-forecast-05-08-2026) | 2차(집계 기사, 2026년 9월 게시, 정확한 게시일 미확인·기사 내 최신 주가 2026-09-07 258.84달러). 12개월 목표가: Rosenblatt 335달러 매수(2026-08-19), Morgan Stanley 335달러 비중확대·330에서 상향(2026-08-17), TD Cowen 350달러 유지(2026-08-24), Wells Fargo 338달러 매수(2026-09-03), 24/7 Wall St. 353.44달러(2026-08-13). 검색에 뜨는 Evercore 280→335 등 TipRanks/The Fly 상향 기사는 2025년 10월 것이라 현재 목표가로 쓰지 않는다. 평균·중앙 목표가와 등급 분포는 찾지 못했다. |
| S75 | news | 2026-10-02 | [The dates that matter most for Amazon stock (Trefis)](https://www.trefis.com/stock/amzn/articles2/617445/the-dates-that-matter-most-for-amazon-stock/2026-10-02) | 2차. 3분기 실적은 '2026-10-29 전후' 예정, 알파벳·마이크로소프트는 약 10-27. AWS 성장 2026년 1분기 +28%, 2분기 +36.7%로 5분기 연속 가속. 2분기 실적 후 2일간 +19.8%, 2025년 4분기 실적·2,000억 capex 계획(2026-02-05) 후 2일간 -9.7%. 연초 대비 +8.3%, 12개월 +13.1%(S&P500 +16.0%). 2025년 11월 고점→2026년 2월 저점 하락폭 21.7%. 따라서 2026-10-18 기준 FY2026Q3 실적은 아직 발표되지 않았다. |

# Pony AI (PONY) 리서치 보고서 — 기준일 2026-10-18

**팽팽** — 찬성 1 · 반대 1 · 보류 1 · 확신 가중 점수 -0.13 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장 내재: 매출 10년 연 45.7% (FCF 마진 15% 수렴 가정) · 기본 시나리오: 5년 연 38.2%
- 시장이 반영한 것: 현재 EV 7.1억 USD(C:ev)는 FCF 마진 20% 도달을 가정하면 연 38.5% 매출 성장을 요구한다(C:implied_cagr@m20). 시장은 이를 가격에 반영한 상태이고, 주가는 4주 사이 7.29 USD(F74)에서 4.93 USD(F80)로 내려 2분기의 성장 호재를 이미 반영하지 않는다.
- 우리가 다르게 보는 점: 단기 매출 성장(F76, F77)은 시장 가정과 비슷하다. 우리가 다르게 보는 점은 마진 도달 시점이다. 차량당 단위경제가 공시로 입증되지 않았고(C:gross_margin@FY2025), 희석이 계속된다(C:dilution). 그래서 base 시나리오의 주당 가치는 시장 가격에 대한 우위를 보이지 않는다.
- 왜 우리가 맞는가: 총이익률이 FY2022 이후 내려와 15%대에서 멈춰 있고(C:gross_margin@FY2025), 로보택시 매출이 늘어도 영업이익률은 크게 음수다(C:operating_margin@FY2025). 회사가 규모의 경제를 숫자로 보인 적이 없다. 이 판단은 컨센서스 데이터가 없는 상태에서 하는 것이어서 확신이 낮다. [F74] [F76] [F77] [F79] [F80] [C:ev] [C:implied_cagr@m20] [C:gross_margin@FY2025] [C:operating_margin@FY2025] [C:dilution]
- 촉매: 분기 6-K에서 로보택시 부문 총이익 또는 대당 단위경제 공시, 연말 차량 3,500대 달성 여부(F79).
- 시점: FY2026Q3(2026-11 중순 예상) 실적과 FY2026 연간 실적

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **2.84** vs 주가 4.93 · 기대 연 수익률 **+0.3%** · 손실 확률 80%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 35% | 0.92 | 0.52 | -28.6% | 추정: 로보택시 매출은 차량 증가로 올해 계속 늘지만(F77, F78) 차량당 매출이 낮은 채 정체한다. 유럽 인허가와 Uber 공동 배치가 지연되고 연말 3,500대 목표(F79)를 못 채운다. 총이익률이 15%대 |
| 기본 | 45% | 4.34 | 2.46 | -2.5% | 추정: 2026년 2분기 매출은 3,620만 USD(F76)이고 로보택시 매출은 1,210만 USD(F77)다. 차량이 1,975대에서 연말 3,500대(F78, F79)로 늘고 Uber 유럽 배치가 단계적으로 가동 |
| 강세 | 20% | 13.68 | 7.76 | +22.7% | 추정: 유럽·중동 확장이 일정대로 진행되고(S54, S43) 해외 4,000대 이상 파이프라인(S50)이 가동된다. 대당 매출이 늘고 로보택시가 총이익률을 끌어올린다. 규모의 경제로 FCF 마진이 25%까지 간다.  |

## 3. 반증 조건 (thesis break)

- [자료 없음] 앤더슨: 연말 로보택시 3,500대 목표 미달 — `robotaxi_fleet < 3500` (FY2026)
- [자료 없음] 앤더슨: 3분기 로보택시 매출이 2분기보다 줄면 성장 가설 훼손 — `robotaxi_revenue < 1.21e+07` (FY2026Q3)
- [수동 확인] 앤더슨: 차량당 단위경제가 흑자로 돌아선다는 공시 없이 추가 증자가 반복됨 — 수동 확인
- [자료 없음] 슬레이터: 연말 로보택시 3,500대 목표 미달 — `robotaxi_fleet < 3500` (FY2026)
- [자료 없음] 슬레이터: 3분기 로보택시 매출이 2분기 수준 밑으로 후퇴 — `robotaxi_revenue < 1.2e+07` (FY2026Q3)
- [수동 확인] 슬레이터: 차량 확장을 위해 대규모 외부 조달이 필요해졌다는 공시 — 수동 확인
- [자료 없음] 애크먼: FY2026Q3 매출이 6,000만 USD 이상이면 성장 경로가 내 가정보다 훨씬 강하다 — `revenue >= 6e+07` (FY2026Q3)
- [미충족] 애크먼: 주가가 base 현재가치 대비 안전마진 20%를 확보하는 수준까지 내려오면 가격 반론이 사라진다 — `price <= 1.9`
- [자료 없음] 레드팀: 분기 총이익률이 15% 아래로 내려가면 대수 확대가 마진을 개선하지 않고 있다는 뜻 — `gross_margin < 0.15`
- [미충족] 레드팀: 연간 설비투자가 1억 USD를 넘으면 차량 확대 자금 수요가 모델보다 빠르게 늘고 있다는 뜻 — `capex > 1e+08`
- [충족 — 훼손] 레드팀: FY2026 말 차량이 3,500대 미만이면 인허가·배치 속도가 가이던스에 못 미친다 — `robotaxi_fleet < 3500`
- [충족 — 훼손] 레드팀: FY2026Q3 로보택시 매출이 1,600만 USD 미만이면 차량 증가가 매출로 이어지지 않는다 — `robotaxi_revenue < 1.6e+07`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | revenue | FY2026Q3 | >= 4e+07 | 60% | 분기 매출이 2분기 3,620만 USD(F76)에서 더 늘어 성장 경로(base 연 65%)가 유지되는지 시험한다. |
| K2 | robotaxi_revenue | FY2026Q3 | >= 1.6e+07 | 60% | 2분기 1,210만 USD(F77)에서 차량 증가가 매출로 이어지는지, 즉 가동 효율을 시험한다. |
| K3 | robotaxi_fleet | FY2026 | >= 3500 | 50% | 연말 3,500대 가이던스(F79)를 지키는지로 경영진 가이던스의 신뢰도와 인허가 속도를 시험한다. |
| K4 | revenue | FY2026 | >= 1.5e+08 | 55% | 연간 매출이 2026년 1·2분기 흐름(F86, F76)대로 FY2025 대비 약 65% 성장하는지 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.13 · 비중 참고값 0.0% (팽팽 — 신규 비중 없음) · 슬레이터 시작 비중 0.5%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 1/5 실패 | founder_led=예, upside_10y=13.87x, revenue_5y=10.29x |
| 슬레이터 | 보류 → 보류 | 2/5 | ✓ | 1/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=0.5%, cash_survives=예, cash_min=2.4억 USD, runway_years=5.6 |
| 애크먼 | 반대 → 반대 | 5/5 | ✗ 단순·예측 가능한 사업이 아님; 잉여현금흐름을 만들지 못함 (코드 계산); 레버리지·자본시장 의존; 안전마진 20% 미만 또는 계산 불가 | 0/5 실패 | simple_predictable=아니오, capital_markets_dependent=예, catalyst=없음 — 자사주나 분사 같은 가치 실현 수단이 없고, 로보택시 단위경제 공시가 유일한 변수다, fcf_positive=아니오, intrinsic_value=2.5, mos=-100.2% |

- ⚠ 앤더슨: rebuttals[0] unsupported: 13.87배는 이 주장의 인용에 없다. 나머지(38.5%, 20%, +691%, 11.7억, 5.6년)는 맞다.
- ⚠ 앤더슨: arguments[3] unsupported: 순현금과 런웨이는 맞다. 기본 시나리오 현금 경로가 바닥에서 버틴다는 내용은 인용에 없다.
- ⚠ 앤더슨: rebuttals[2]: 인용하지 않은 근거의 숫자 1.17e+09(C:cash_total@FY2025·C:net_cash·C:net_cash@FY2025) — cites에 추가
- ⚠ 슬레이터: rebuttals[2] unsupported: 출처 없는 숫자 6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 슬레이터: arguments[4] unsupported: 희석 상당 부분이 상장에 따른 기계적 증가라는 내용은 인용 자료에 없다. 희석 64.5%는 맞다.
- ⚠ 애크먼: arguments[4] leap: 희석 64.5%와 SBC 34.2%는 맞다. 하지만 인용 자료만으로는 성장 자금을 주식 발행으로 조달했기 때문에 희석이 생겼다고 볼 수 없다.
- ⚠ 애크먼: risks[0] unsupported: 없는 근거 인용: C:revenue_5y
- ⚠ 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 경영진·자본배분 findings[3]: 인용하지 않은 근거의 숫자 10%(C:receivables_growth@FY2024), 1.1e+08(C:diluted_shares@FY2024·C:ocf@FY2024·F20), 3.8e+08(C:diluted_shares@FY2025·C:shares·F21), 3%(C:fcf_margin@bear·C:irr@base) — cites에 추가
- ⚠ 레드팀 premortem[1] 검증 실패(unsupported): 출처 없는 숫자 8.9e+08, 3.6e+08 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[6]: 인용하지 않은 근거의 숫자 1.1e+08(C:diluted_shares@FY2024·C:ocf@FY2024·F20), 3500(F79·S54) — cites에 추가
- ⚠ 회계 품질 flags[2] 검증 실패(unsupported): 상장과 우선주 전환이 주식 수 증가의 원인이라는 내용은 인용 자료에 없다. 주식 수와 자기자본 값은 맞다.
- ⚠ 경영진·자본배분 findings[6] 검증 실패(unsupported): FY2022 현금 3.2억은 인용에 없다. FY2025 현금, 단기투자, 순현금, 런웨이는 맞다.
- ⚠ 사업·산업 findings[4]: 인용하지 않은 근거의 숫자 1.92e+06(F17) — cites에 추가
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): 출처 없는 숫자 7500, 7.1% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[7] 검증 실패(unsupported): 출처 없는 숫자 32% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 레드팀 weakest[0] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base
- ⚠ 레드팀 premortem[3]: 인용하지 않은 근거의 숫자 691%(S42·S54), 1.92e+06(F17), 30%(C:implied_cagr@m30) — cites에 추가
- ⚠ 경영진·자본배분 findings[4] 검증 실패(unsupported): 없는 근거 인용: C:buybacks

## 앤더슨 — 찬성 (3/5)

> Pony AI는 아직 아무것도 증명하지 못한 적자 기업이다. 그러나 멱법칙 투자에서는 그 점이 오히려 가격이 싸게 매겨지는 이유가 된다. 2분기 로보택시 매출은 전년 대비 +691%로 늘었고 차량은 1,975대, 연말 목표는 3,500대다. 순현금 11.7억 USD로 런웨이 5.6년이 확보되어 있어 성장 가설을 시험할 시간이 있다. 주가는 4주 사이 크게 내렸고 현재 EV는 7.1억 USD다. 강세 시나리오가 실현되면 코드가 계산한 10년 뒤 주당 가치는 현재 주가의 13.87배이고 5년 매출은 10.29배다. 확률은 20%에 불과하고 손실 확률은 80%다. 이것은 네 번 틀려도 한 번의 큰 승리가 포트폴리오를 결정하는 전형적인 비대칭 베팅이다. 다만 단위경제와 총이익률이 입증되지 않았고 희석이 크기 때문에 확신은 중간(3)으로 제한하고, 작게 담는 것을 전제로 찬성한다.

**논거**
- 10번 질문(5배 가능성): 강세 시나리오로 계산한 10년 뒤 주당 가치가 현재 주가의 13.87배, 5년 뒤 매출이 기준 연도의 10.29배다. 5배 경로는 가정이 아니라 코드 계산상 열려 있으며, 레드라인(5배)을 크게 웃돈다. [C:upside_10y@anderson] [C:revenue_5y@anderson]
- 1번 질문(매출 두 배): 로보택시 매출이 2분기에 1,210만 USD로 전년 대비 +691.2% 늘었고 요금 징수 매출은 +849.3%다. 낮은 기저 효과를 감안해도, 수요가 있고 차량을 늘리면 매출이 따라온다는 첫 번째 증거다. 차량은 1,975대에서 연말 3,500대가 목표다. [F77] [F78] [F79] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- 9번 질문(시장은 왜 과소평가하는가): 4주 사이 주가가 7.29 USD에서 4.93 USD로 내려, EV가 7.1억 USD가 되었다. 역DCF는 이 가격이 FCF 마진 20%에서 연 38.5% 성장만 요구한다고 말한다. 강세 시나리오의 연 59.4% 성장은 그보다 높은 수준이고, 시장은 하방만 가격에 넣고 있다. [F74] [F80] [C:ev] [C:implied_cagr@m20] [C:revenue_cagr@bull]
- 생존 가능성: 순현금 11.7억 USD와 현금 소진 연수 5.6년은 성장 가설이 시험될 시간을 준다. 기본 시나리오에서도 현금 경로가 바닥에서 버틴다. 극단적 손실은 100%로 막혀 있고 상방은 열려 있다. [C:net_cash@FY2025] [C:runway_years]
- 확장 채널: Uber와 유럽에 2,000대 이상을 공동 배치하는 계획과 해외 4,000대 이상 파이프라인은 자체 운영만으로 도달하기 어려운 규모를 열어 줄 수 있다. 계획 수준이라는 한계는 인정하지만, 확장 방향이 맞다는 신호다. [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5) [S50](https://news.google.com/rss/articles/CBMimgFBVV95cUxPWm94c24xeGcyMlA5MGZnNE8zWmJqX0JaU1YyV3Jqb1Q2VGJwaGJ1Q2NjNG5QZnBweHpGdkRWUjFxUWFqMG1HYWtzNEtkQzdSZVpzUDlqTm5uZk1EZmpXV3BuUHRIaXg0Z3JRZjJHWlVHSWl0d2EzTm00QWhKODVoeDhqTG5DSnBraEpCMG5MZjVFcmpRdEJiWlh3?oc=5)

**사전 부검**
- 사전 부검 — 단위경제가 끝내 흑자가 되지 않았다. 총이익률은 FY2022 이후 15.7%에서 정체하고 영업이익률은 -289.8%다. 차량이 늘어도 대당 손익이 음수라면 규모는 손실만 키우고, 강세 시나리오의 FCF 마진 25%는 성립하지 않는다. 이것은 경로의 소음이 아니라 성장 가설 자체를 깨는 위험이다. [C:gross_margin@FY2025] [C:operating_margin@FY2025]
- 사전 부검 — 희석이 수익을 갉아먹었다. 희석은 연 64.5%로 컸고 차량 3,500대 확대에 필요한 자본은 확인되지 않았다. 추가 증자가 반복되면 매출이 커져도 주당 가치는 늘지 않는다. [C:dilution] [C:share_change@FY2025]
- 사전 부검 — 확률 가중으로는 이 베팅이 이기지 못한다. 기대 연 수익률은 +0.3%에 그치고 손실 확률은 80%다. 강세 20%가 실현되지 않으면 원금 대부분이 사라지는 구조라, 비중을 키우면 이 비대칭은 소멸한다. [C:expected_irr] [C:p_loss]

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 FCF가 구조적으로 음수이고 안전마진이 음수라는 점이다. 이는 현재 가치를 재는 도구로는 옳다. 그러나 이 회사의 가치는 현재 FCF가 아니라 10년 뒤 크기에 있다. 강세 시나리오 코드 계산은 10년 뒤 주당 가치가 현재 주가의 13.87배다. 역DCF는 목표 FCF 마진 20%에서 연 38.5% 성장만 요구하는데, 2분기 로보택시 매출은 전년 대비 +691%였다. 현금 11.7억 USD와 런웨이 5.6년이 있어 이 가설을 시험할 시간이 있다. 자본시장 의존은 인정하되, 그것이 상방을 막지는 않는다. [C:implied_cagr@m20] [C:runway_years] [C:net_cash@FY2025] [F77] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- → 슬레이터: 슬레이터의 가장 강한 논거는 증거 앞에서 사지 말고 단위경제가 공시될 때까지 기다리자는 것이다. 그러나 이 기업의 가장 가치 있는 구간은 단위경제가 증명되기 전에 지나간다. 증명 후에는 역DCF가 요구하는 성장이 이미 가격에 들어간다. 슬레이터가 정한 관찰 지표(차량 대수, 로보택시 매출)는 내 반증 조건과 같으므로 틀리면 같은 신호로 바로 알 수 있다. 작은 비중으로 시작하는 것에는 동의한다. 기다림의 비용이 더 크다. [F78] [F79] [F77] [C:upside_10y@anderson]
- → 레드팀: 레드팀의 가장 강한 시나리오는 차량당 단위경제가 흑자가 되지 못하는 것이다. 이것은 성장 가설 자체를 깨므로 경로의 소음이 아니고, 내 반증 조건에 연말 3,500대와 3분기 로보택시 매출을 넣어 확인한다. 반면 희석과 증자 시나리오는 주당가치를 깎지만 가설을 깨지는 않는다. 현금 소진이 모델보다 빨라져도 순현금 11.7억 USD와 런웨이 5.6년이 완충한다. 유럽 인허가 지연은 경로의 문제이지만 연말 차량이 3,500대에 못 미치면 가설 위반으로 취급한다. [C:gross_margin@FY2025] [C:dilution] [C:runway_years] [F79] [F78]

**인정한 점**
- 애크먼: 확률 가중 기대 연 수익률은 +0.3%이고 손실 확률은 80%여서 이 베팅은 비중을 키우면 비대칭이 사라진다. 따라서 작은 비중을 전제로만 찬성한다.
- 슬레이터: 단위경제와 총이익률이 입증되지 않았으므로 확신을 3 이하로 제한한다.
- 레드팀: 기본 시나리오의 희석 가정 4%는 FY2025의 연 64.5% 증가와 비교하면 낙관적이어서, 주당 가치의 하방이 모델보다 클 수 있다.


## 슬레이터 — 보류 (2/5)

> 시장의 크기와 지속성은 슬레이터가 좋아하는 유형이다. 로보택시 시장은 아직 정의되지 않았고, 2분기 로보택시 매출은 1,210만 USD로 전년 대비 +691%였다. 생존도 당장은 문제가 아니다. 순현금 11.7억 USD로 런웨이가 5.6년이고, 기본 시나리오의 현금 경로도 0 아래로 내려가지 않는다. 그러나 확신은 회사가 증명해야 하는데, 지금 증명된 것은 매출 성장뿐이다. 총이익률은 15.7%에서 정체했고, 차량당 단위경제는 공시되지 않았다. 확률 가중 기대 연 수익률은 +0.3%, 손실 확률은 80%다. 이 상태에서 비중을 싣는 것은 가설을 증거 앞에서 사는 일이다. 가설이 깨진 것은 아니므로 매도 사유도 없다. 찬성도 반대도 아닌 관찰 상태로 두고, 4분기 안에 확인할 운영 지표(차량 대수, 로보택시 매출, 총이익)를 정해 두며, 증거가 쌓이면 1% 내외로 시작한다.

**논거**
- 로보택시 서비스 매출 1,210만 USD가 총매출 3,620만 USD의 약 1/3까지 올라왔고 전년 대비 +691%다. 정의되지 않은 시장에서 수요 증거가 숫자로 나오기 시작했다는 점은 슬레이터가 보는 긍정 신호다. [F77] [F76] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- 생존은 문제가 아니다. 순현금 11.7억 USD와 런웨이 5.6년이라 외부 자본 없이 계획을 실행할 수 있다. 2022년 교훈(외부 조달 의존 기업의 실패)에 비추어 이 지점은 통과한다. [C:net_cash@FY2025] [C:runway_years]
- 확률 가중 기대 연 수익률이 +0.3%이고 손실 확률이 80%다. 기본 시나리오에서도 연 수익률이 마이너스여서, 지금 가격은 증명이 끝나기 전부터 상당 부분 반영되어 있다. 증거 앞서 사야 할 이유가 없다. [C:expected_irr] [C:p_loss]
- 단위경제는 확인되지 않았다. 총이익률이 15.7%로 정체한 가운데 영업이익률은 -289.8%다. 로보택시 매출이 커져도 차량당 이익이 나는지는 6-K에 없다. `unit_economics`를 `proven`이 아니라 `unclear`로 둔다. [C:gross_margin@FY2025] [C:operating_margin@FY2025]
- 자금 조달이 희석으로 이뤄졌다. 희석 주식 수가 연 64.5% 증가했고, 이 중 상당 부분은 상장에 따른 기계적 증가로 보인다. 그러나 차량 3,500대 확장에 필요한 자본 규모가 공개되지 않아 추가 조달 가능성이 열려 있다. [C:dilution] [F79]

**사전 부검**
- 연말 3,500대 목표를 못 채우면 인허가와 파트너 배치 속도가 계획보다 느리다는 뜻이다. 2분기 말 차량은 1,975대였다. [F78] [F79] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- Uber 유럽 공동 배치 2,000대 이상은 계획 단계로 보도된 것이고 6-K 숫자로 확인된 배치가 아니다. 이를 실적처럼 다루면 계획과 실적을 혼동하게 된다. [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5)
- 차량이 늘수록 감가상각과 운영비가 먼저 늘어 총이익률이 개선되기 전에 영업손실이 커질 수 있다. 설비투자가 4,388만 USD로 이미 늘었다. [F81] [C:gross_margin@FY2025]

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 '역DCF는 FCF 마진 20%에서 연 38.5% 성장만 요구하니 시장이 하방만 가격에 넣고 있다'는 것이다. 그러나 이 성장률은 마진이 -232.0%에서 20%로 올라간다는 전제 위에서 나온 숫자다. 마진 도달을 뒷받침할 단위경제는 공시된 적이 없고, 총이익률은 15.7%에 머문다. 성장은 증명되고 있지만 마진은 증명되지 않았으므로, 역DCF가 낮아 보인다는 이유로 상방이 열려 있다고 말할 수 없다. 강세 시나리오 확률은 20%이고 손실 확률은 80%여서, 코드가 계산한 기대 연 수익률(+0.3%)은 비대칭 베팅이라는 주장을 받쳐 주지 않는다. [C:implied_cagr@m20] [C:fcf_margin@FY2025] [C:gross_margin@FY2025] [C:expected_irr] [C:p_loss]
- → 애크먼: 애크먼은 FCF가 음수라서 자본시장 의존이 확인된다고 본다. 이 점은 반만 맞다. 2022년 이후 내가 경계하는 것은 외부 조달 없이는 계획을 실행하지 못하는 기업인데, 이 회사는 순현금 11.7억 USD에 런웨이 5.6년이라 지금은 그 상태가 아니다. 다만 이 런웨이는 FY2025 말 기준이라 분기 소진 속도로는 확인되지 않았다. 또 오늘 모델링할 수 없다는 이유로 정의되지 않은 시장을 버리는 것은 단순성 기준이 만드는 맹점이다. 내가 기다리는 이유는 예측 불가능성이 아니라 증거 부족이다. 그래서 반대가 아니라 관찰로 둔다. [C:net_cash@FY2025] [C:runway_years] [C:fcf_margin@FY2025]
- → 레드팀: 레드팀의 두 번째 사전 부검은 자본 부담이 모델보다 빠르게 늘면 런웨이가 3년 안팎으로 줄 수 있다고 한다. 방향은 맞지만 3년이라는 값은 근거가 없고, 차량 조달 비용과 파트너 분담 구조가 확인되지 않았다는 사실에서 나온 추측이다. 반면 희석 가정이 연 3~6%로 낙관적이라는 지적과, 기본 시나리오에서 마진이 마지막 해에 한꺼번에 뛴다는 지적은 타당하다. 이 두 가지는 내 관찰 상태를 유지할 이유가 된다. 총이익률 15% 미만과 설비투자 1억 USD 초과는 선행 신호로 모니터링에 넣을 가치가 있다. [C:runway_years] [C:dilution] [C:fcf_margin@FY2025] [C:gross_margin@FY2025] [F81]

**참이어야 하는 것**
- [at_risk] 연말 로보택시 3,500대 목표를 달성한다
- [on_track] 3분기 로보택시 매출이 2분기 1,210만 USD보다 늘어 1,600만 USD 이상이 된다. 차량 증가가 매출로 이어진다는 뜻이다
- [at_risk] 2026년 연간 매출이 1.5억 USD 이상이다. 상반기 추세가 하반기에도 이어진다는 뜻이다
- [at_risk] 로보택시 부문 총이익 또는 대당 단위경제가 공시되고, 총이익률이 15%대에서 벗어나 개선된다

**인정한 점**
- 애크먼: 지금 이 회사는 단순하고 예측 가능한 현금 창출 사업이 아니다. 이 차이는 인정하지만 내 질문은 예측 가능성이 아니라 증명 여부이고, 그 답이 아직 '아니오'라서 찬성하지 않는다.
- 레드팀: 연 3~6% 희석 가정은 FY2025의 희석 이력과 SBC 부담에 비추어 낙관적일 수 있다. 확신을 올릴 이유가 아니므로 conviction을 2로 유지하고 비중 참고값도 늘리지 않는다.
- 앤더슨: 로보택시 매출이 낮은 기저에서 빠르게 늘고 있다는 수요 증거는 유효하다. 다만 이것은 매출이 증명된 것이지 단위경제가 증명된 것이 아니므로 입장은 바꾸지 않는다.


## 애크먼 — 반대 (5/5)

> Pony AI는 한 문단으로 설명할 수는 있다. 로보택시를 운영하고 플랫폼 제휴로 확장하는 자율주행 회사다. 그러나 10년 뒤 FCF를 합리적인 범위로 추정할 수는 없다. 차량당 단위경제가 공시로 확인된 적이 없고, 총이익률은 15%대에서 정체해 있으며, FCF는 구조적으로 크게 음수다. 현재 이익이 아니라 미래 성장 서사에 대한 베팅이라서 내가 찾는 단순하고 예측 가능한 현금 창출 사업이 아니다. 성장 자금은 자본시장에서 조달한 주식이었고 희석은 연 64.5%였다. 현금이 많아 당장 망할 회사는 아니지만, FCF가 음수인 한 자본시장 의존은 면하지 못한다. 가격도 싸지 않다. 코드가 계산한 base 시나리오 현재가치는 주가보다 낮아 안전마진이 음수이고, 확률 가중 기대 수익률은 거의 0이며 손실 확률이 높다. 좋은 서사와 좋은 가격은 별개다. 레드라인 네 개 중 세 개를 넘지 못하므로 담지 않는다.

**논거**
- FCF가 구조적으로 음수다. FY2025 FCF 마진은 -232.0%이고 설비투자는 늘고 있다. 현금을 뿜는 사업이 아니라 현금을 태우는 사업이라서 첫 번째 기준을 통과하지 못한다. [C:fcf@FY2025] [C:fcf_margin@FY2025] [C:capex@FY2025]
- 10년 뒤 FCF를 추정할 수 없어 단순성 기준에 실패한다. 총이익률이 15.7%에 머물러 규모의 경제가 숫자로 나타난 적이 없다. 시장 가격은 목표 FCF 마진 20%를 가정하면 연 38.5%의 매출 성장을 10년간 요구한다. 이 범위는 너무 넓어서 보수적 내재가치를 잡을 수 없다. [C:gross_margin@FY2025] [C:implied_cagr@m20] [C:operating_margin@FY2025]
- 가격이 싸지 않다. 코드 계산상 확률 가중 기대 연 수익률은 +0.3%에 그치고 손실 확률은 80%다. 안전마진은 음수라서 20% 기준에 크게 못 미친다. 좋은 시나리오가 실현되어야만 수익이 나는 비대칭 구조다. [C:expected_irr] [C:p_loss] [C:ev_revenue]
- 해자는 아직 주장 수준이다. 사업 모듈 기준으로 규모, 전환비용, 기술 모두 입증 등급이 낮다. Uber 제휴의 계약 기간·독점 여부·수익 배분이 확인되지 않아 가격결정력도 입증되지 않았다. [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5) [C:gross_margin@FY2023]
- 자본시장 의존이 확인된다. 성장 자금을 주식 발행으로 조달해 희석이 연 64.5%였고, SBC도 매출의 34.2%다. 순현금이 많아 당장의 위험은 작지만 FCF가 양수로 돌아서기 전에는 추가 조달 가능성이 열려 있다. [C:dilution] [C:sbc_to_revenue@FY2025] [C:net_cash@FY2025] [C:runway_years]

**사전 부검**
- 사전 부검 — 내가 틀렸다면, 로보택시 단위경제가 예상보다 빨리 흑자로 전환되고 유럽 확장이 일정대로 진행되어 강세 시나리오가 실현된 경우다. 그러면 주가가 낮은 지금 놓친 기회가 된다. 다만 이 시나리오의 확률은 20%이고 기저율상 드문 경로다. [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [S50](https://news.google.com/rss/articles/CBMimgFBVV95cUxPWm94c24xeGcyMlA5MGZnNE8zWmJqX0JaU1YyV3Jqb1Q2VGJwaGJ1Q2NjNG5QZnBweHpGdkRWUjFxUWFqMG1HYWtzNEtkQzdSZVpzUDlqTm5uZk1EZmpXV3BuUHRIaXg0Z3JRZjJHWlVHSWl0d2EzTm00QWhKODVoeDhqTG5DSnBraEpCMG5MZjVFcmpRdEJiWlh3?oc=5) [C:revenue_5y]
- 사전 부검 — 주가가 최근 4주 사이 크게 내려 이미 비관이 많이 반영됐을 수 있다. 다만 EV/매출 7.86x는 여전히 높은 성장을 가정한다. [F74] [F80] [C:ev_revenue]
- 사전 부검 — 순현금이 풍부해 자본시장 의존이 과장됐을 수 있다. 그러나 런웨이는 FY2025 말 기준이고 분기 현금 소진 속도는 6-K로 확인되지 않았다. [C:runway_years] [C:net_cash@FY2025]

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 강세 시나리오의 10년 뒤 주당 가치가 현재 주가의 13.87배라는 것이다. 이것은 확률 가중 결과가 아니라 강세 한 갈래의 결과다. 확률 가중 기대 연 수익률은 +0.3%이고 손실 확률은 80%다. 기저율 표가 없어 강세 경로가 얼마나 드문지 확인할 수도 없다. 이것은 생존자 편향에 기댄 베팅이다. 역DCF가 요구하는 성장도 가볍지 않다. 목표 FCF 마진 20% 기준으로 연 38.5%다. 시장이 하방만 가격에 넣고 있다는 주장은 이 요구 성장을 설명하지 못한다. 단위경제가 공시되지 않은 상태에서 상방 배수를 근거로 담는 것은 가격 규율이 아니다. [C:upside_10y@anderson] [C:expected_irr] [C:p_loss] [C:implied_cagr@m20]
- → 슬레이터: 슬레이터는 생존 경로가 확보됐다고 보고 증거 앞에서 사지 않겠다며 기권했다. 증거 앞에서 사지 않겠다는 결론에는 동의한다. 그러나 생존 경로는 필요조건일 뿐 가격의 정당화가 아니다. 런웨이 5.6년은 FY2025 말 기준이고 분기 현금 소진 속도는 6-K로 확인되지 않았다. 기본 시나리오의 연 수익률은 -2.5%다. 좋은 서사와 좋은 가격은 별개다. 기권은 이 가격에서 보유할 이유가 있다는 뜻으로 읽히면 안 된다. FCF가 음수인 동안은 자본시장 의존이 해소되지 않는다. 내 레드라인에서는 기권이 아니라 반대다. [C:runway_years] [C:irr@base] [C:fcf_margin@FY2025]
- → 레드팀: 레드팀의 사전 부검은 FCF 범위를 넓힌다. 단위경제 실패, 현금 소진 가속, 인허가 차단, 질 낮은 성장 모두 근거가 있다. 기본 시나리오의 FCF 마진 도달 가정이 가장 약하다는 지적에 동의한다. FY2025 FCF 마진이 -232.0%이고 총이익률은 15.7%에 머무는데, 규모의 경제를 보인 숫자가 없다. FCF 범위가 이렇게 넓어지면 보수적 가정의 내재가치는 더 낮아진다. 기본 시나리오 현재가치조차 주가에 못 미치므로 안전마진 20%를 요구하면 더 큰 가격 하락이 필요하다. 증자로 인한 희석은 주당가치를 추가로 깎는다. [C:fcf_margin@FY2025] [C:gross_margin@FY2025] [C:dilution] [C:sbc_to_revenue@FY2025]

**인정한 점**
- 앤더슨: 순현금과 런웨이 덕분에 가설을 시험할 시간이 있고 극단적 손실이 당장 닥치지는 않는다. 이 점은 인정한다. 그러나 이것은 담지 않는 이유를 약하게 할 뿐 레드라인 위반을 해소하지 않는다.
- 슬레이터: 가설이 깨진 것은 아니므로 매도 사유가 없다는 점에 동의한다. 나는 보유자가 아니므로 진입 사유가 없다는 결론이 달라지지 않는다.
- 레드팀: 주가가 최근 4주 사이 크게 내려 비관이 일부 반영됐을 가능성은 인정한다. 다만 가격이 내려도 단순성과 FCF 양수 요건은 충족되지 않는다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Pony AI는 자율주행 소프트웨어·하드웨어 스택을 로보택시(직접 운영 및 Uber 등 플랫폼 제휴), 로보트럭, 라이선싱·서비스로 수익화하려는 적자 기업이다. FY2025 매출은 9,000만 USD(C:revenue_growth@FY2025 20.0%)이고 총이익률은 15.7%(C:gross_margin@FY2025)에 불과하며 영업이익률은 -289.8%(C:operating_margin@FY2025)이다. 2026년 2분기 로보택시 매출은 1,210만 USD(전년 대비 +691%)로 총매출 3,620만 USD의 약 1/3까지 올라왔고 차량은 1,975대(연말 3,500대 목표)다. 다만 차량당 단위경제(차량 원가, 운영 인력, 가동률, 요금 대비 비용)는 공시로 확인되지 않았고 총이익률 추이도 FY2022 46.9%에서 15%대로 내려앉은 뒤 정체 상태다. 현금·투자 중심 순현금은 11.7억 USD로 런웨이는 5.6년(C:runway_years)이라 생존 위험은 당장 크지 않지만, 희석이 연 64.5%로 컸고 EV 7.1억 USD가 가정하는 성장(목표 FCF 마진 20% 기준 연 38.5%)은 단위경제 입증에 달려 있다.

- [unit_economics] 총이익률이 FY2022 46.9%에서 FY2023 23.5%, FY2024 15.2%, FY2025 15.7%로 내려와 정체 중이다. 로보택시 비중이 커지면 마진 구조가 바뀌므로 믹스 변화가 핵심 변수인데, 로보택시 부문 단독 총이익은 공시되지 않았다. [C:gross_margin@FY2022] [C:gross_margin@FY2023] [C:gross_margin@FY2024] [C:gross_margin@FY2025]
- [unit_economics] 2026년 2분기 로보택시 매출 1,210만 USD는 전년 대비 +691%, 요금 징수 매출은 +849%로 급증했다. 낮은 기저에서의 증가이고, 대당 매출로 환산하면 분기 1,975대 기준 대략 월 2천 USD 수준이라는 추정이므로 차량 원가와 운영비를 상회하는지는 알 수 없다. 추정: 12.1M ÷ 1,975대 ÷ 3개월 ≈ 월 2,000 USD. [F77] [F78] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- [unit_economics] 운영 손실 규모가 매출을 크게 웃돈다. FY2025 영업손실 2.6억 USD, FCF -2.1억 USD(마진 -232%)이고 SBC 차감 FCF는 -2.4억 USD다. FY2025 설비투자가 FY2024 1,140만 USD에서 4,388만 USD로 늘어 차량 투자가 시작된 흔적이 있다. [C:operating_income@FY2025] [C:fcf@FY2025] [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [C:capex@FY2024] [C:capex@FY2025]
- [industry] 유럽 공동 배치(Uber 2,000대 이상)와 해외 4,000대 이상 파이프라인은 지리적 확장 의지를 보여주나, 대부분 계획·보도 수준이며 인허가와 실제 배치 완료 여부는 6-K 숫자로 확인되지 않았다. 규제와 현지 인허가가 확장 속도의 병목이다. [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [S32](https://news.google.com/rss/articles/CBMizwFBVV95cUxQaUZLRVdHWnB1NFFOenZ4SHRKYmljRV9HWE9OTFMzSlBmaXNlNnFaQVNpclJjRXFCQ3V4LWxuTThwaHROd0NmeU5yc1l1QTQtOEVUNGYyX1lTM0dueHZkVGE0Y3lqbUk5QzR4d3NQZzhkcjdvWlhmMEpGd3BsRFJwd2EwMXhtWUV2a0RCMkFKei1hRUwzOGlndnlDcjBJOVlNQ19fTXJLMTBVLVVMMml4UjA2VHdQUWx5d3dtLVFxc1drc3VSVG14cGJQLXRXa2s?oc=5) [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5) [S50](https://news.google.com/rss/articles/CBMimgFBVV95cUxPWm94c24xeGcyMlA5MGZnNE8zWmJqX0JaU1YyV3Jqb1Q2VGJwaGJ1Q2NjNG5QZnBweHpGdkRWUjFxUWFqMG1HYWtzNEtkQzdSZVpzUDlqTm5uZk1EZmpXV3BuUHRIaXg0Z3JRZjJHWlVHSWl0d2EzTm00QWhKODVoeDhqTG5DSnBraEpCMG5MZjVFcmpRdEJiWlh3?oc=5)
- [customers] 매출 구성에서 로보택시 외 부문(로보트럭, 라이선싱·서비스)의 고객 집중도와 계약 구조는 확인되지 않았다. 매출채권 DSO는 FY2023 160일에서 FY2025 96일로 줄었으나 이연매출은 192만 USD로 감소해 선수금형 수요 증거는 약하다. [C:dso@FY2023] [C:dso@FY2025] [C:deferred_revenue@FY2025]
- [runway] 순현금 11.7억 USD와 런웨이 5.6년은 재투자 활주로를 제공하지만, 활주로의 질은 투하자본수익률로 판단해야 한다. ROIC는 FY2025 -42.3%로 음수이고 FY2024 -138.5%에서 개선됐다. 고수익 재투자처가 입증된 것이 아니라 투자 진행 중이다. [C:net_cash@FY2025] [C:runway_years] [C:roic@FY2024] [C:roic@FY2025]
- [runway] 자금 조달은 주식 희석으로 이뤄졌다. 희석 주식 수가 FY2024 1.1억에서 FY2025 3.8억으로 늘었고(연 64.5%), 이는 확장을 위해 자본시장에 의존했다는 의미다. 향후 차량 3,500대 확대에 필요한 자본 규모는 확인되지 않아 추가 조달 가능성이 열려 있다. [C:share_change@FY2025] [C:dilution] [F21]
- [industry] 주가는 4주 사이 7.29 USD에서 4.93 USD로 약 32% 하락했고 하락 사유는 확인되지 않았다. 현재 EV/매출 7.86x는 매출 성장이 FY2025 20% 수준일 때 높고 2Q 69% 성장이 지속될 때 정당화된다. 역DCF는 목표 FCF 마진 20%에서 연 38.5% 성장을 요구한다. [F74] [F80] [C:ev_revenue] [C:implied_cagr@m20]
- [claimed] 차량 대수 확대(1,975대→3,500대 목표)와 Uber 등 제휴 채널을 통한 유럽·중동 확장으로 데이터·운영 규모의 이점을 주장하지만, 규모가 단위당 원가 하락이나 점유율로 이어진 숫자는 없다. 총이익률은 FY2023 23.5%에서 FY2025 15.7%로 오히려 낮아졌다. [F78] [F79] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [C:gross_margin@FY2023] [C:gross_margin@FY2025]
- [claimed] Uber와의 2,000대 유럽 공동 배치 등 플랫폼 제휴는 유통 접근권이지만 계약 기간·독점 여부·수익 배분은 확인되지 않았다. 제휴 상대가 다른 AV 업체와도 병행할 수 있어 전환비용 해자로 보기 어렵다. [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5) [S34](https://news.google.com/rss/articles/CBMinwFBVV95cUxQQkpUaUFJdDNySDFnenkzQmFVRVV5cTktN0ZSakp5enc0UFp2T3VWc0lHU2taWHFCTV9uRmMwSUpKTU1vYTc1Q2YwbzZsYk5FcVE1bWtCVmZnRmRwbUFObmJoRHlzRnBqajRBQ1RzZHBwSTRrSlBpSkJUT3dFemQ5dkRzbzJqdWczWHo2S0wwaUpIX194cU44RGFTeWtLZjTSAaQBQVVfeXFMTm1FdkFRcy1fQzRXNlVUdHJmTDZaYVZiYjJ1MElheWpXejI0bnBpZ2JNcS0wNC0ySkczMVFJcHBRMFVvZHF5TWVVSnEyN0F0N2thbmRYbVhtaE1NTXg0Q29MUFNvVGtEblVvLUViQ2xXb1VIdEFfMzBPNF91WkF1eTNYdUZyWXpBS296X09HVTFidlNOVDAtcWpZTm52bG9PeXgzZ2E?oc=5)
- [claimed] 자율주행 알고리즘과 하드웨어 통합 기술은 연 R&D 2.2억 USD(FY2025)로 뒷받침되나, 안전 지표(개입 빈도 등)나 경쟁사 대비 우위를 보인 시장 데이터는 없다. 해자라기보다 진입 비용에 가깝다. [C:rnd@FY2025] [S35](https://news.google.com/rss/articles/CBMickFVX3lxTE1FRUNEbHowbnZjM01oSS1MeEJhSzVkcEhCYzE1OHdzbXpkeGxTOGhGMm0yUVFyS2o1Ym5LLXpiT0lPU2dBbGxYR0F6bWg5TW9ZN2FhS3pseVo0ei1EYUFub1lNSlh2ODNHRmt3VTRvRTAzUQ?oc=5)

### 경영진·자본배분 — mixed

경영진과 주주가 같은 방향을 보는지는 근거가 부족해 판단하기 어렵다. 보상 구조(DEF 14A 대신 20-F 기준), 내부자 매매, 과거 가이던스 적중률은 모두 수집되지 않았다. 확인되는 것은 세 가지다. 첫째, SBC가 매출 대비 크다(FY2024 169.3%, FY2025 34.2%). 둘째, 희석 주식 수가 FY2025에 크게 늘었다(232.3%). 셋째, 설비투자가 FY2025에 4,388만 USD로 늘었고 현금 소진이 계속된다. 반면 순현금 11.7억 USD(소진 5.6년)와 Uber 등 파트너십을 통한 해외 확장 계획은 자본을 사업 확장에 쓰고 있음을 보여준다. 다만 이 투자의 수익률은 아직 입증되지 않았다. 판단은 mixed로 두며, 근거가 없는 영역은 정렬의 증거가 아니다.

- [compensation] 근거 없음. 임원 보상이 어떤 지표(장기 매출·FCF·ROIC·주당가치 vs 단기 지표)에 연동되는지, 베스팅 기간이 어떤지 알 수 있는 자료가 수집되지 않았다. 20-F는 목록에 있으나 보상 항목은 확인하지 못했다. 보상 정렬은 판단하지 않는다. [S22](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm)
- [insider] 근거 없음. 창업자·경영진 지분율과 최근 내부자 매수·매도 자료가 없다. 확인되는 것은 발행 주식 수 4.33542e+08주(2025-12-31)뿐이며, 경영진의 보유 비중은 알 수 없다. [F65]
- [guidance] 과거 매출·비용 가이던스를 찾지 못해 적중률(C:guidance_hit_rate)을 계산할 수 없다. 확인되는 가이던스는 연말 로보택시 3500대 목표 하나다. 2026년 2분기 실제는 1975대로 목표의 일부이며, 달성 여부는 연말에야 확인된다. 신뢰도는 검증된 바 없다. [F79] [F78] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- [dilution] SBC는 FY2024 1.3억 USD(매출 대비 169.3%)에서 FY2025 3,080만 USD(34.2%)로 줄었으나 여전히 10%를 크게 웃돌아 회계 품질 신호(watch)가 켜져 있다. 희석 주식 수는 FY2024 1.1억에서 FY2025 3.8억으로 늘어 주식 수 변화가 232.3%다. 코드는 연 64.5% 증가로 보고 3% 기준을 초과한 것으로 표시했다. 증가 원인(상장 전환·신주 발행 등)은 자료로 확인하지 못했다. [C:sbc@FY2024] [C:sbc@FY2025] [C:sbc_to_revenue@FY2024] [C:sbc_to_revenue@FY2025] [C:share_change@FY2025] [C:dilution]
- [dilution] 자사주 매입은 FY2023의 99만 USD가 유일하게 확인되며, 이후 기간에는 기록이 없다. 규모가 작아 희석을 상쇄하지 못하고 가리지도 못한다. 희석은 매입이 아니라 실질적으로 방치된 상태에 가깝다. [F1] [C:buybacks]
- [capital_allocation] 설비투자는 FY2024 1,140만 USD에서 FY2025 4,388만 USD로 늘었다. 같은 기간 FCF는 -2.1억 USD이고 마진은 -232.0%다. 재투자 규모는 커졌지만 ROIC는 -42.3%로 아직 자본 수익을 내지 못한다. 투자 대비 수익률을 판단할 근거는 부족하다. [F84] [F81] [C:fcf@FY2025] [C:fcf_margin@FY2025] [C:roic@FY2025]
- [capital_allocation] 현금 3.2억 USD(FY2022) 수준에서 FY2025에는 현금 2.9억 USD, 단기투자 8.7억 USD로 보유 구조가 바뀌었고 순현금은 11.7억 USD, 소진 연수는 5.6년이다. 자본이 쌓여 있어 당장 자금 조달 압박은 크지 않다. 이 자본을 M&A나 인수에 쓴 이력은 자료에 없으며, 고점 매입·비싼 인수 여부는 판단할 수 없다. [F5] [F69] [C:net_cash@FY2025] [C:runway_years]
- [capital_allocation] 2026년 2분기 기준 로보택시는 1975대이고, Uber와 유럽에 2,000대 이상을 공동 배치하는 계획이 공표됐다. 확장 방향은 자본을 사업에 쓰는 쪽이다. 다만 파트너 자금 분담 구조나 차량 조달 비용은 확인되지 않아, 자본 배분 규율을 평가하기에는 정보가 부족하다. 주가는 7.29 USD(2026-09-22)에서 4.93 USD(2026-10-16)로 내려 시장의 평가도 호의적이지 않다. [F78] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [F74] [F80]

### 회계 품질 — watch

회계 신뢰성을 해칠 증거는 없지만 조정해서 봐야 할 숫자가 있어 watch로 판정한다. 이 회사는 FCF 적자가 구조적이고 SBC 부담이 크다. 따라서 이익이 아니라 SBC 차감 FCF와 현금 소진 속도로 봐야 한다. 코드 신호 3개(SBC/매출, 이연매출, 희석)는 모두 해명했다. 이연매출은 금액이 작아 문제가 아니고, 희석은 상당 부분 IPO에 따른 기계적 증가다. SBC는 실제 비용이다. 순이익 흑자·OCF 음수, 재무제표 정정, 감사인 변경 같은 red 신호는 없다. 매출채권은 줄고 DSO는 개선되어 매출 당겨쓰기 증거는 없다. 다만 FY2025 세전손실과 순손실이 맞지 않는 점, 분기 현금흐름이 확인되지 않은 점, 감사의견이 확인되지 않은 점은 열린 항목이다.

- [concern] sbc_to_revenue: FY2025 SBC가 매출의 34.2%로 문턱 10%를 크게 넘는다. 순이익은 영업적자를 SBC로 부풀린 것이 아니라 SBC가 비용에 포함된 상태다. 그러나 FCF에는 SBC가 들어가지 않아 SBC 차감 FCF가 더 적자다. FY2024 SBC 1.3억은 상장 시 일회성 성격이 커 보이고, FY2025 3,080만으로 내려왔다. 그래도 매출 대비 비율이 높아 가치평가에서는 FCF가 아니라 SBC 차감 FCF를 기준으로 삼아야 한다. [F61] [F62] [F63] [F64] [F56] [C:sbc_to_revenue@FY2025] [C:fcf_after_sbc@FY2025]
- [benign] deferred_revenue: FY2025 매출은 늘었고 이연매출은 FY2024 323만에서 FY2025 192만으로 줄었다. 절대액이 작아 매출 9,000만 대비 의미 있는 당겨쓰기로 보기 어렵다. 같은 기간 매출채권이 줄고 DSO도 개선되어, 채권 증가로 매출을 부풀린 흔적이 없다. 이연매출 감소는 선수금 계약 비중이 작은 사업 구조에서 나온 변동으로 본다. 로보택시 요금 징수 매출이 늘면서 선수금 비중은 더 작아질 수 있다. [F16] [F17] [F55] [F56] [F51] [F52] [C:deferred_revenue@FY2025] [C:dso@FY2025]
- [benign] dilution: 희석 주식 수가 FY2024 1.1억에서 FY2025 3.8억으로 크게 늘었다. 자기자본이 FY2023 음수에서 FY2024 양수로 바뀐 것은 상장과 우선주 전환 때문이다. 가중평균 주식 수가 전환 시점부터 반영되면서 뛰었으므로 상당 부분은 자본구조 정리에 따른 기계적 증가다. 보통주 기준 발행주식은 FY2025 말 4.33542억 주다. 다만 상장 후에도 SBC와 추가 자금조달로 주식 수는 계속 늘 수 있다. 신규 주식 수를 가정하고 주당가치를 계산해야 한다. [F19] [F20] [F21] [F23] [F24] [F65] [C:dilution] [C:share_change@FY2025]
- [watch] FY2025 세전손실(-7,676만)과 순손실(-1.3억)의 관계가 정합하지 않다. 영업손실은 -2.6억인데 세전손실이 훨씬 작은 것은 영업외 이익(이자수익·공정가치 변동 등)이 컸다는 뜻이다. 세전손실보다 순손실이 더 큰 것은 FY2025 법인세 사실이 없어 설명되지 않는다. 사실 추출 오류이거나 비지배지분·기타 항목 때문일 수 있다. 20-F 손익계산서로 대조하기 전에는 FY2025 순이익 -1.3억을 보수적으로만 쓴다. 영업손실과 OCF가 더 믿을 만하다. [F36] [F44] [F48] [S22](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm)
- [info] 발생액 비율이 작고 순이익과 OCF가 모두 크게 음수다. 이익을 현금보다 크게 보이게 만든 구조가 아니며, 적자는 현금 유출로 실제 확인된다. 현금 소진 연수 5.6년은 FY2025 말 현금·단기투자 기준이다. 분기 현금 유출 속도와 최근 현금 잔액은 6-K로 확인되지 않았다. [F40] [F36] [F5] [F69] [C:accruals_ratio@FY2025] [C:runway_years]
- [watch] FY2025 설비투자가 4,388만으로 전년 1,140만에서 크게 늘었다. 로보택시 차량 확대(1,975대, 연말 3,500대 이상 목표)와 맞는 방향이다. 감가상각은 FY2025 710만으로 계속 줄었고, 차량이 가동되면 비용이 따라 늘 것이다. 이 시차가 향후 영업이익률을 눌러 현재 손실 폭보다 나빠질 수 있다. 감가상각 정책과 차량 내용연수는 20-F 주석으로 확인되지 않았다. 자본화 소프트웨어 신호는 코드에 없다. [F84] [F85] [F81] [F13] [F78] [F79] [C:capex@FY2025]
- [info] 코드의 non_gaap 신호는 없다. 그러나 리서처가 Non-GAAP 조정 내역을 확인하지 못했다. 회사 발표 숫자는 GAAP 6-K 본문과 대조되기 전에는 쓰지 않는 편이 안전하다. 제3자 요약의 분기 순손실·현금 수치는 사실로 채택되지 않았다. [S53](https://transcripts.platformaeronaut.com/summaries/PONY-2Q26-AI-Summary) [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- [watch] 감사의견, 핵심감사사항, 감사인 변경, 특수관계자 거래는 찾지 못했다. 코드의 restatement·auditor_change 신호는 없지만, 근거가 없다는 사실이 문제가 없다는 증거는 아니다. 이 영역은 미확인으로 남는다. 20-F 감사보고서 확인 전까지 clean을 줄 수 없다. [S22](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm)
- [watch] 로보택시 서비스 매출이 빠르게 늘고 있고 요금 징수 매출이 그보다 더 빠르게 늘었다. 총액·순액 표시 여부, Uber 등 파트너 거래의 수익 인식 방식, 차량 판매와 서비스 매출의 구분이 공시로 확인되지 않았다. 파트너 배치가 커지면 이 정책이 매출 규모와 총이익률에 직접 영향을 준다. 매출 성장률은 정책 확인 전까지 가정으로만 써야 한다. [F77] [F76] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (25%) 차량당 단위경제가 끝내 흑자로 돌아서지 못한다. 로보택시 매출 1,210만 USD를 1,975대로 나누면 대당 월 약 2천 USD 수준이라는 추정인데, 차량 원가·원격 안전요원·보험·충전·정비를 덮지 못한다. 규모를 키울수록 손실이 커지는 구조가 되어 총이익률은 15%대에서 정체하거나 악화하고, 3,500대 이상으로 늘린 차량이 감가상각 부담만 키운다(FY2025 감가상각 710만 USD는 차량이 가동되면 급증한다). FCF 마진 15% 도달 가정이 무너지면 출구 멀티플 25배도 성립하지 않는다. [F77] [F78] [F13] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [C:gross_margin@FY2025] [C:operating_margin@FY2025]
- (30%) 현금 소진이 모델보다 빠르고 추가 증자가 반복된다. 기본 시나리오조차 FY2027까지 FCF가 -2.9억 USD이고 순현금이 8.9억에서 3.6억 USD(FY2028)로 줄어든다. 차량 3,500대 이상과 유럽 2,000대 배치의 자본 부담(차량 조달, 파트너 분담 구조 미확인)이 예상보다 크면 런웨이 5.6년은 3년 안팎으로 줄어든다. 주가가 이미 4.93 USD로 떨어진 상태에서 증자하면 희석이 크고 주당가치는 시나리오 계산보다 낮아진다. 이미 FY2025 희석 주식 수가 연 64.5% 늘었고, 모델의 연 3~6% 증가 가정은 낙관적이다. [C:runway_years] [C:net_cash@FY2025] [C:dilution] [C:share_change@FY2025] [F80] [F81]
- (20%) 유럽·중동 확장이 인허가와 지정학 때문에 막힌다. 회사의 성장 서사는 Uber와의 유럽 2,000대 배치와 해외 4,000대 파이프라인에 크게 의존하는데, 대부분 계획·보도 수준이고 6-K 숫자로 확인되지 않았다. 중국 기업이라는 점이 서구 규제(커넥티드카 제한, 데이터 안보, 상장 폐지 압박)와 충돌하거나, Uber가 다른 자율주행 업체로 배치를 돌리면 해외 성장 경로가 닫힌다. 제휴는 계약 기간·독점·수익 배분이 확인되지 않아 전환비용이 낮다. 연말 차량 3,500대 가이던스 미달이 첫 신호가 된다. [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5) [S50](https://news.google.com/rss/articles/CBMimgFBVV95cUxPWm94c24xeGcyMlA5MGZnNE8zWmJqX0JaU1YyV3Jqb1Q2VGJwaGJ1Q2NjNG5QZnBweHpGdkRWUjFxUWFqMG1HYWtzNEtkQzdSZVpzUDlqTm5uZk1EZmpXV3BuUHRIaXg0Z3JRZjJHWlVHSWl0d2EzTm00QWhKODVoeDhqTG5DSnBraEpCMG5MZjVFcmpRdEJiWlh3?oc=5) [S34](https://news.google.com/rss/articles/CBMinwFBVV95cUxQQkpUaUFJdDNySDFnenkzQmFVRVV5cTktN0ZSakp5enc0UFp2T3VWc0lHU2taWHFCTV9uRmMwSUpKTU1vYTc1Q2YwbzZsYk5FcVE1bWtCVmZnRmRwbUFObmJoRHlzRnBqajRBQ1RzZHBwSTRrSlBpSkJUT3dFemQ5dkRzbzJqdWczWHo2S0wwaUpIX194cU44RGFTeWtLZjTSAaQBQVVfeXFMTm1FdkFRcy1fQzRXNlVUdHJmTDZaYVZiYjJ1MElheWpXejI0bnBpZ2JNcS0wNC0ySkczMVFJcHBRMFVvZHF5TWVVSnEyN0F0N2thbmRYbVhtaE1NTXg0Q29MUFNvVGtEblVvLUViQ2xXb1VIdEFfMzBPNF91WkF1eTNYdUZyWXpBS296X09HVTFidlNOVDAtcWpZTm52bG9PeXgzZ2E?oc=5) [F79] [F78]
- (20%) 로보택시 매출 급증이 질 낮은 성장으로 드러난다. 2분기 매출 +691%는 낮은 기저 효과이고 요금 징수 매출은 보조금·프로모션 요금에 의존했을 수 있다. 파트너 거래의 총액·순액 표시가 확인되지 않았고, 이연매출은 192만 USD로 감소해 선수금형 수요 증거가 약하다. 경쟁사(Waymo, Baidu Apollo Go 등)와 가격 경쟁이 시작되면 대당 매출이 오르지 않고 매출 성장이 둔화한다. 성장이 25~30%대로 꺾이면 EV/매출 7.86배를 지탱할 근거가 없어 멀티플이 압축된다. [F76] [F77] [C:deferred_revenue@FY2025] [C:ev_revenue] [C:revenue_growth@FY2025]
- 약한 가정 `base.fcf_margin`: FCF 마진이 FY2025 -232%에서 5년 만에 +15%로 올라야 하는데, 총이익률은 FY2022 46.9%에서 FY2025 15.7%로 내려와 정체해 있고 규모의 경제를 보인 숫자가 없다. 모델 경로상 FY2029에도 -34.4%다. 마지막 해에 -34%에서 +15%로 약 50%p가 한 번에 점프한다. 기저율 표가 없어 비교 근거도 없다. [C:fcf_margin@FY2025] [C:gross_margin@FY2025] [C:gross_margin@FY2022] [C:base_rate@base]
- 약한 가정 `base.exit_multiple`: 출구 P/FCF 25배는 5년차에 FCF 마진이 막 흑자로 전환한 시점에 적용된다. 성장이 22%로 둔화하는 해에 이 멀티플을 받을 수 있는지 근거가 없다. 민감도에서 멀티플 ×0.75만 되어도 기본 시나리오 연 수익률은 -7.1%이다. [C:exit_multiple@base] [C:irr@base]
- 약한 가정 `base.share_change`: 연 4% 희석 가정은 FY2025 희석 주식 수 증가(연 64.5%)와 FY2027~FY2028 기본 경로의 순현금 감소, SBC(34.2%)와 맞지 않는다. 증자 없이 흑자 전환까지 버티지 못하면 주당가치가 줄어든다. [C:dilution] [C:sbc_to_revenue@FY2025] [C:net_cash@FY2025]

## 검증 (L6)

주장 72개 — supported 58 · unsupported 12 · contradicted 0 · leap 2 · 미검증 0

- [unsupported] 앤더슨: 애크먼의 가장 강한 논거는 FCF가 구조적으로 음수이고 안전마진이 음수라는 점이다. 이는 현재 가치를 재는 도구로는 옳다. 그러나 이 회사의 가치는 현재 FCF가 — 13.87배는 이 주장의 인용에 없다. 나머지(38.5%, 20%, +691%, 11.7억, 5.6년)는 맞다.
- [unsupported] 레드팀: 현금 소진이 모델보다 빠르고 추가 증자가 반복된다. 기본 시나리오조차 FY2027까지 FCF가 -2.9억 USD이고 순현금이 8.9억에서 3.6억 USD(FY20 — 출처 없는 숫자 8.9e+08, 3.6e+08 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 애크먼: 자본시장 의존이 확인된다. 성장 자금을 주식 발행으로 조달해 희석이 연 64.5%였고, SBC도 매출의 34.2%다. 순현금이 많아 당장의 위험은 작지만 FCF가 — 희석 64.5%와 SBC 34.2%는 맞다. 하지만 인용 자료만으로는 성장 자금을 주식 발행으로 조달했기 때문에 희석이 생겼다고 볼 수 없다.
- [leap] 사업·산업: 자금 조달은 주식 희석으로 이뤄졌다. 희석 주식 수가 FY2024 1.1억에서 FY2025 3.8억으로 늘었고(연 64.5%), 이는 확장을 위해 자본시장에 의존 — 희석 주식 수 증가는 맞다. 하지만 이것이 확장을 위한 자본시장 의존이라는 결론은 인용 자료에서 따라 나오지 않는다.
- [unsupported] 회계 품질: 희석 주식 수가 FY2024 1.1억에서 FY2025 3.8억으로 크게 늘었다. 자기자본이 FY2023 음수에서 FY2024 양수로 바뀐 것은 상장과 우선주 전환 — 상장과 우선주 전환이 주식 수 증가의 원인이라는 내용은 인용 자료에 없다. 주식 수와 자기자본 값은 맞다.
- [unsupported] 경영진·자본배분: 현금 3.2억 USD(FY2022) 수준에서 FY2025에는 현금 2.9억 USD, 단기투자 8.7억 USD로 보유 구조가 바뀌었고 순현금은 11.7억 USD,  — FY2022 현금 3.2억은 인용에 없다. FY2025 현금, 단기투자, 순현금, 런웨이는 맞다.
- [unsupported] 슬레이터: 레드팀의 두 번째 사전 부검은 자본 부담이 모델보다 빠르게 늘면 런웨이가 3년 안팎으로 줄 수 있다고 한다. 방향은 맞지만 3년이라는 값은 근거가 없고, 차량 조 — 출처 없는 숫자 6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 출구 P/FCF 25배는 5년차에 FCF 마진이 막 흑자로 전환한 시점에 적용된다. 성장이 22%로 둔화하는 해에 이 멀티플을 받을 수 있는지 근거가 없다. 민감 — 출처 없는 숫자 7500, 7.1% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 슬레이터: 자금 조달이 희석으로 이뤄졌다. 희석 주식 수가 연 64.5% 증가했고, 이 중 상당 부분은 상장에 따른 기계적 증가로 보인다. 그러나 차량 3,500대 확장에  — 희석 상당 부분이 상장에 따른 기계적 증가라는 내용은 인용 자료에 없다. 희석 64.5%는 맞다.
- [unsupported] 사업·산업: 주가는 4주 사이 7.29 USD에서 4.93 USD로 약 32% 하락했고 하락 사유는 확인되지 않았다. 현재 EV/매출 7.86x는 매출 성장이 FY2025 2 — 출처 없는 숫자 32% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 앤더슨: 생존 가능성: 순현금 11.7억 USD와 현금 소진 연수 5.6년은 성장 가설이 시험될 시간을 준다. 기본 시나리오에서도 현금 경로가 바닥에서 버틴다. 극단적 손 — 순현금과 런웨이는 맞다. 기본 시나리오 현금 경로가 바닥에서 버틴다는 내용은 인용에 없다.
- [unsupported] 레드팀: FCF 마진이 FY2025 -232%에서 5년 만에 +15%로 올라야 하는데, 총이익률은 FY2022 46.9%에서 FY2025 15.7%로 내려와 정체해 있고  — 없는 근거 인용: C:base_rate@base
- [unsupported] 애크먼: 사전 부검 — 내가 틀렸다면, 로보택시 단위경제가 예상보다 빨리 흑자로 전환되고 유럽 확장이 일정대로 진행되어 강세 시나리오가 실현된 경우다. 그러면 주가가 낮은 — 없는 근거 인용: C:revenue_5y
- [unsupported] 경영진·자본배분: 자사주 매입은 FY2023의 99만 USD가 유일하게 확인되며, 이후 기간에는 기록이 없다. 규모가 작아 희석을 상쇄하지 못하고 가리지도 못한다. 희석은 매입이  — 없는 근거 인용: C:buybacks

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
| 희석 주식 수 (shares) | 3.8억 |
| 시가총액 (market_cap) | 18.7억 USD |
| 순현금 (net_cash) | 11.7억 USD |
| EV (ev) | 7.1억 USD |
| FCF 수익률 (fcf_yield) | -11.1% |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 7.86x |
| PER (pe) | — |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | 5.6 |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 34.2% > 10%
- [watch] deferred_revenue (C:deferred_revenue): 매출은 늘었는데 이연매출이 10% 넘게 줄었다 — 매출 당겨쓰기 의심
- [watch] dilution (C:dilution): 희석 주식 수 연 64.5% 증가 > 3%

### 역DCF — 현재 가격이 가정하는 것

EV 7.1억 USD를 정당화하려면 매출이 10년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 목표 마진으로 직선 수렴, 할인율 10%, 이후 영구성장 3%.
기본 시나리오 목표 마진 15% 기준: 연 45.7% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 57.7% | C:implied_cagr@m10 |
| 15% | 45.7% | C:implied_cagr@m15 |
| 20% | 38.5% | C:implied_cagr@m20 |
| 25% | 33.4% | C:implied_cagr@m25 |
| 30% | 29.6% | C:implied_cagr@m30 |

### 시나리오 가치 — 5년, 할인율 12% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 35% | 2.4억 USD | 21.5% | 3% | 10x | 0.92 | 0.52 | -28.6% |
| 기본 | 45% | 4.5억 USD | 38.2% | 15% | 25x | 4.34 | 2.46 | -2.5% |
| 강세 | 20% | 9.3억 USD | 59.4% | 25% | 25x | 13.68 | 7.76 | +22.7% |

확률 가중: 주당 가치 5.01 · IV 2.84 · 기대 연 수익률 +0.3% (C:expected_irr) · 손실 확률 80% (C:p_loss) · 현재 주가 4.93

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +32.4% · 마진·멀티플(P/S) -14.8% · 주식 수 변화 -3.9% · 현금 축적 -16.2% = -2.5%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -9.6% | -5.6% | -2.2% |
| +0%p | -7.1% | -2.5% | +1.3% |
| +5%p | -4.2% | +0.9% | +5.2% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 1.5억 USD | -182.6% | -2.7억 USD | 4.0억 | 8.9억 USD |
| FY2027 | 2.2억 USD | -133.2% | -2.9억 USD | 4.1억 | 6.1억 USD |
| FY2028 | 2.9억 USD | -83.8% | -2.4억 USD | 4.3억 | 3.6억 USD |
| FY2029 | 3.7억 USD | -34.4% | -1.3억 USD | 4.4억 | 2.4억 USD |
| FY2030 | 4.5억 USD | 15.0% | 6,809만 USD | 4.6억 | 3.0억 USD |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 45.7% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 38.2% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 59.4% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=13.87x, revenue_5y=10.29x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=2.4억 USD, runway_years=5.6
- 애크먼 case={"from": "base"}: price=4.9, fcf_positive=아니오, leveraged=아니오, intrinsic_value=2.5, mos=-100.2%

### 계산 경고

- 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
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

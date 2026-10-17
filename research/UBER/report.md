# Uber Technologies (UBER) 리서치 보고서 — 기준일 2026-10-18

**찬성 우세** — 찬성 2 · 반대 1 · 보류 0 · 확신 가중 점수 +0.20 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장 내재: 매출 10년 연 2.2% (FCF 마진 20% 수렴 가정) · 기본 시나리오: 5년 연 10.1%
- 시장이 반영한 것: 현재 EV는 FCF 마진이 20%까지 오르면 10년간 연 매출 성장 2.2%만 있어도 정당화된다. 시장은 사실상 성장 없는 FCF 유지 값만 가격에 넣었고, 자율주행의 공급 측 교란을 할인 요인으로 반영하고 있다. 3분기 가이던스가 컨센서스를 소폭 밑돈 점도 약세 요인이다.
- 우리가 다르게 보는 점: 총예약액이 가이던스대로 18~22% 성장하고 FCF 마진이 18~20%대를 지키면, 시장 내재 성장(C:implied_cagr@m20)보다 훨씬 높은 성장이 이어진다. 가이던스 하회는 폭이 작고 보수적 가이던스의 성격이 강해 구조적 둔화로 보기 어렵다.
- 왜 우리가 맞는가: TTM FCF가 이미 100억 달러를 넘었고(S43) FCF 마진은 FY2023 9.0%에서 FY2025 18.8%로 올랐다. 자사주 매입이 SBC 희석을 상쇄하고도 남아 주당 FCF가 더 빠르게 늘어난다. 시장이 가정하는 마진 후퇴가 일어나려면 자율주행으로 수수료율이 꺾여야 하는데, 지금까지 확인된 파트너 구조는 Uber가 수요 집합자로 남는 쪽에 가깝다. [C:implied_cagr@m20] [C:fcf_yield] [F202] [F205] [F201] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow) [C:fcf_margin@FY2023] [C:fcf_margin@FY2025]
- 촉매: 3분기 실적에서 총예약액과 조정 EBITDA가 가이던스 범위 안에 들어오고, 구조조정 후 FCF 마진이 유지되는 것이 확인되는 시점. 자율주행 파트너 확장의 수수료 구조 공개도 계기가 된다.
- 시점: FY2026Q3 실적(2026년 11월 초)부터 FY2027 상반기
- 컨센서스 대비 revenue FY2026: +0.4% (585.2억 USD vs 582.8억 USD)

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **110.12** vs 주가 70.35 · 기대 연 수익률 **+20.3%** · 손실 확률 25%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 25% | 69.46 | 43.13 | -0.3% | 자율주행 사업자가 차량 공급을 직접 쥐면서 Uber의 수수료율이 눌리고, 승차·배달이 다중 앱으로 쓰이는 탓에 경쟁 보조금도 늘어난다. 규제와 소송 비용이 겹쳐 총예약액 성장이 3분기 가이던스 하단(환율 불변 18% |
| 기본 | 50% | 175.49 | 108.97 | +20.1% | FY2026은 컨센서스 매출(F207)과 같은 선에서 시작하고, 이후 성장이 점차 둔화한다. 조직 개편과 규모의 운영 레버리지로 FCF 마진은 FY2025 18.8%에서 20%까지 완만히 오른다. 자사주 매입이 SB |
| 강세 | 25% | 288.97 | 179.43 | +32.7% | Costco 배달 확대와 Zipline·Baidu·Wayve 같은 다자 자율주행 네트워크가 수요를 더하고, 광고와 교차 이용이 마진을 끌어올린다. 총예약액 성장이 3분기 가이던스 상단(환율 불변 22%)에 가깝게 유 |

## 3. 반증 조건 (thesis break)

- [자료 없음] 앤더슨: 3분기 총예약액이 가이던스 하단(582.5억 달러)에 못 미치면 성장 가설 훼손 — `gross_bookings < 5.825e+10` (FY2026Q3)
- [자료 없음] 앤더슨: 3분기 조정 EBITDA가 가이던스 하단 미만이면 마진 상방 가정 훼손 — `adjusted_ebitda < 2.86e+09` (FY2026Q3)
- [수동 확인] 앤더슨: 주요 AV 파트너가 Uber를 거치지 않는 직접 수요 채널을 가동하면 집합자 가설 훼손 — 수동 확인
- [미충족] 슬레이터: 조정 EBITDA 마진이 총예약액 대비 4% 아래로 내려가면 마진 개선 가설이 깨진다 — `adjusted_ebitda_margin_gross_bookings < 0.04`
- [미충족] 슬레이터: 희석 주식 수가 다시 늘면 자본 환원이 희석을 상쇄한다는 전제가 깨진다 — `diluted_shares > 2.15e+09`
- [수동 확인] 슬레이터: 자율주행 파트너가 수수료율 인하를 요구하거나 직접 판매로 전환하는 사례가 공시·보도로 확인되면 수동 점검
- [자료 없음] 애크먼: 3분기 총예약액이 가이던스 하단(582.5억 달러) 미만 — `gross_bookings < 5.825e+10` (FY2026Q3)
- [자료 없음] 애크먼: 3분기 조정 EBITDA가 가이던스 하단(28.6억 달러) 미만 — `adjusted_ebitda < 2.86e+09` (FY2026Q3)
- [수동 확인] 애크먼: 자율주행 파트너가 수수료 인하를 요구하거나 직접 수요를 확보하는 계약이 확인됨 — 수동 확인
- [미충족] 레드팀: 총예약액 대비 조정 EBITDA 마진이 현재 4.9%에서 4.5% 아래로 내려가면 수수료율 압박이 진행 중 — `adjusted_ebitda_margin_gross_bookings < 0.045`
- [충족 — 훼손] 레드팀: FY2026Q3 총예약액이 자체 가이던스 하단 582.5억 달러에도 못 미치면 성장 둔화가 가이던스 안에서도 막히지 않은 것 — `gross_bookings < 5.825e+10`
- [미충족] 레드팀: 분기 FCF가 현재 28억 달러에서 20억 달러 아래로 내려가면 비용 누수가 현금에 나타난 것 — `free_cash_flow < 2e+09`
- [미충족] 레드팀: 현금이 FY2026Q2의 48.7억 달러에서 40억 달러 아래로 내려가면 매입·인수가 현금 완충을 소진한 것 — `cash < 4e+09`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | gross_bookings | FY2026Q3 | >= 5.925e+10 | 60% | 가이던스 중간값 달성 여부로 성장 둔화가 일시적인지 시험한다. 약세 시나리오는 이 선을 밑돈다. |
| K2 | adjusted_ebitda | FY2026Q3 | >= 2.86e+09 | 85% | 가이던스 하단 이상이면 마진 개선 가설이 유지된다. |
| K3 | revenue | FY2026Q3 | >= 1.5e+10 | 65% | 상반기 매출 성장률이 3분기에도 이어지는지 본다. 기본 시나리오의 연간 성장 경로를 분기 단위로 시험한다. |
| K4 | revenue | FY2026 | >= 5.828e+10 | 60% | 연간 매출이 컨센서스 평균에 도달하는지로 기본 시나리오의 첫 해 성장률을 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 +0.20 · 비중 참고값 10.0% (0.25 켈리 — 5년 초과수익 +91%(요구수익률 10% 차감), 분산 1.22, 상한 10%) · 슬레이터 시작 비중 2.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 0/5 실패 | founder_led=아니오, upside_10y=8.53x, revenue_5y=1.83x |
| 슬레이터 | 찬성 → 찬성 | 3/5 | ✓ | 0/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=2.0%, cash_survives=예, cash_min=53.9억 USD |
| 애크먼 | 찬성 → 반대 (레드라인 → 반대) | 3/5 | ✗ 안전마진 20% 미만 또는 계산 불가 | 1/5 실패 | simple_predictable=예, capital_markets_dependent=아니오, catalyst=구조조정으로 비용 구조를 단순화하고, FCF의 상당 부분으로 자사주를 매입해 주식 수를 줄이는 중. 3분기 실적에서 가이던스 범위 안의 총예약액과 조정 EBITDA가 확인되면 가격과 가치의 격차가 좁혀진다., fcf_positive=예, net_debt_to_ebitda=0.72x, intrinsic_value=84.2, mos=16.5% |

- ⚠ 앤더슨: 5년 매출 1.83배 < 2배 (LTGG Q1)
- ⚠ 앤더슨: rebuttals[2] unsupported: 출처 없는 숫자 4.5% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 슬레이터: rebuttals[2] unsupported: '매입 기간에 현금은 줄고 부채는 늘었다'는 말은 FY2026Q2 한 시점의 현금·부채만 인용해서는 확인되지 않는다. 매입액과 주식 수 감소율은 맞다.
- ⚠ 애크먼: rebuttals[1] unsupported: 출처 없는 숫자 35.4% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: arguments[2] unsupported: 출처 없는 숫자 35.4% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: rebuttals[0]: 인용하지 않은 근거의 숫자 1.83(C:revenue_5y@anderson) — cites에 추가
- ⚠ 애크먼: rebuttals[2]: 인용하지 않은 근거의 숫자 16(C:exit_multiple@base·S42) — cites에 추가
- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 모델이 컨센서스와 사실상 같다 — variant perception이 없다면 알파도 없다
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): 인용한 값은 FY2023 9.0%와 FY2025 18.8% 두 시점뿐이다. 20%에 한 번도 도달한 적이 없다는 말과 최근 분기 OCF·capex가 역산 근사치라는 말은 인용 자료에 없다.
- ⚠ 경영진·자본배분 findings[3] 검증 실패(unsupported): 희석 주식 수 증감과 SBC 비율, 분기 SBC는 일치한다. 그러나 매입이 희석을 상쇄하고도 남는다는 결론은 매입액을 인용하지 않아 받쳐지지 않고, 비율이 '꾸준히' 낮아졌다는 것도 양 끝값만으로는 알 수 없다.
- ⚠ 사업·산업 findings[6]: 인용하지 않은 근거의 숫자 20%(C:expected_irr·C:fcf_margin@base·C:irr@base), 15%(C:receivables_growth@FY2025·C:roic@FY2025) — cites에 추가
- ⚠ 레드팀 weakest[2] 검증 실패(unsupported): 현금이 줄고 부채가 늘었다고 하지만 인용한 것은 FY2026Q2 한 시점의 현금·부채뿐이라 비교할 수 없다. 현금 축적 +5.0%p 가정도 인용 자료에 없다.
- ⚠ 사업·산업 moat[1] 검증 실패(unsupported): 출처 없는 숫자 6.5% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[1]: 인용하지 않은 근거의 숫자 3.36e+09(C:fcf@FY2023), 6.7%(C:sbc_to_revenue@FY2021) — cites에 추가
- ⚠ 회계 품질 findings[4] 검증 실패(unsupported): FY2025 발생액 비율, DSO, OCF와 영업이익은 맞다. 그러나 FY2024 6.0%와 '매출 성장과 큰 격차 없이' 움직였다는 말은 이전 분기 매출채권 등 비교 자료가 없어 인용 자료로 확인되지 않는다.
- ⚠ 회계 품질 findings[6] 검증 실패(unsupported): 인용한 S11·S3에는 내용이 없고 공시 목록에 4.02·4.01 항목이 없다는 것을 확인할 자료도 제시되지 않았다.
- ⚠ 레드팀 weakest[0] 검증 실패(unsupported): 출처 없는 숫자 0.9% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 사업·산업 findings[5] 검증 실패(unsupported): 출처 없는 숫자 0.7% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)

## 앤더슨 — 찬성 (3/5)

> Uber는 승차·배달·화물을 한 앱으로 묶은 양면 플랫폼이고, 자율주행 시대에도 수요를 모으는 집합자로 남을 수 있다면 10년 뒤 가치는 지금 가격과 비대칭이다. 시장은 FCF 마진이 20%까지 오르는 경우 연 2.2% 성장만 가격에 넣었다. 상방 시나리오에서는 희석을 반영한 10년 뒤 주당 가치가 현재 주가의 5배를 넘는다. 약점도 분명하다. 창업자가 경영하지 않고, 5년 매출 2배는 상방 시나리오에서도 모자라며, 자율주행이 수수료율을 압박할 수 있다. 그래도 하방은 약세 시나리오에서 본전 근처이고 상방은 열려 있어, 소액이라도 담을 만한 비대칭이라고 본다. 확신은 중간이다.

*이전 판단 대비: 직전 판단과 같은 입장(찬성, 확신 3)이다. 새 근거는 없고 직전 반증 조건을 그대로 유지한다.*

**논거**
- 시장은 성장을 거의 가격에 넣지 않았다. 역DCF상 FCF 마진 20%에 도달하면 연 2.2% 성장만으로 현재 EV가 정당화된다. 5배가 되는 길은 이 낮은 기대와 상방 시나리오 사이의 간격에서 나온다. [C:implied_cagr@m20] [C:implied_cagr@m15]
- 규모가 커지면서 수익성이 구조적으로 올랐다. 영업이익률은 FY2022 -5.7%에서 FY2025 10.7%로, FCF 마진은 1.2%에서 18.8%로 올랐다. 매출은 FY2025에도 18.3% 늘었다. 성장과 마진이 함께 오르는 구간이라 6번과 7번 질문에 답이 된다. [C:operating_margin@FY2022] [C:operating_margin@FY2025] [C:fcf_margin@FY2022] [C:fcf_margin@FY2025] [C:revenue_growth@FY2025]
- 자율주행 파트너 네트워크가 다자로 넓어지고 있다. Baidu(두바이), Wayve(영국), 스페인 로보택시 허가, Zipline 드론 배달이 모두 Uber를 수요 채널로 쓴다. 공급이 여러 사업자에게 분산되면 수요 집합자의 협상력이 유지된다. 이것이 10년 뒤 모습(2번 질문)의 핵심 가설이다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5) [S22](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQclNPVTE0M0xWUGpKVlMwT2VXLU9SaVBKbjdDOWRtTjhBelVBYnBwSzUzemlXVHBuQ3IybU1aQWZuZUZBZ2FJZEV4bFFkSGN0c0o0cE1tZ2MteUMxRU91RW03LVFKaE9faTBQaW54TWFtdFJ4WEcxQlcxaDFiSl8taWRwWEJyX1B2X25DakI1SmRFU1ZSdjh1NVBHOTMtckJzX183R181bUtQdDI1VkZSQmc2OWctMVZCcnJkWDNsaHFiMlVLX3JEZVVfX3VXenVia3FZZ1ZaV2RoVWQ2dl9uZGxhcjhZcjlFcUozSQ?oc=5)
- 자금 창출과 자본배분이 장기 복리를 받쳐 준다. 설비투자는 매출의 1%가 안 되고, FY2025 자사주 매입 65.2억 달러가 SBC 희석을 넘어 희석 주식 수가 FY2025에 1.4% 줄었다. SBC 차감 FCF도 79.4억 달러로 남아 7번과 8번 질문에 부합한다. [F11] [F4] [C:share_change@FY2025] [C:fcf_after_sbc@FY2025]
- 3분기 가이던스가 컨센서스를 소폭 밑돈 것은 성장 가설을 깨는 신호가 아니라 경로의 소음이다. 환율 불변 18~22% 성장은 여전히 높고, 총예약액은 2분기에 24% 늘었다. 단기 가이던스 오차에 반응하는 것은 이 시간 지평에서 방향이 틀렸다고 본다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F202] [F205] [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow)

**사전 부검**
- 사전 부검 — 자율주행 사업자가 차량과 고객 접점을 직접 쥐고 Uber를 우회한다면 수수료율이 꺾이고 집합자 가설이 무너진다. 이 경우 FCF 마진이 FY2025 수준에서 후퇴하고 5배는 불가능하다. 지금 근거로는 어느 쪽인지 판별되지 않는다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S37](https://news.google.com/rss/articles/CBMiogFBVV95cUxNWXdxWlBSU0tMMnp3LWgzTkFUZHJIWC0xcVpVSFVHSnZCcnlNenlQS0pib2RBZXVaUDVBZzZCZ2FpVm8zOEVpeENEeHdoOGxFLWlULURSU0QyWVJtUDhwbnBfWW5QZy13TGJjOGpSTjBpazVPX3FrNkU1NEZuVmxtOWdDU2ZJUmhyWWVtMFA3empfX0t5Rno0TWE5NWNmV0JoeVE?oc=5)
- 사전 부검 — 상방 시나리오에서도 5년 뒤 매출은 기준 연도의 2배에 못 미친다. 5배는 성장 가속이 아니라 마진 확대와 출구 배수에 크게 기댄다. 이 가정이 틀리면 멱법칙형 아웃라이어가 아니라 잘 운영되는 성숙 플랫폼에 그친다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [C:fcf_margin@FY2025]
- 사전 부검 — 감원 3,300명과 소송 합의, 나이지리아 철수 같은 비용이 조정 EBITDA 밖에 계속 쌓이면 보고 이익이 현금 창출력을 과대평가한 것이 된다. 이 경우 FCF 마진 상방 가정이 훼손된다. [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) [S25](https://news.google.com/rss/articles/CBMirgFBVV95cUxQelprYTZqU1R2cFNKc2lqX0NZdGFxR0tyVjI0OGRUNFJHSHJJSkkzWmlfNGY0cXc2ZmpZaUc2X3RHZ3h5eEx1U2xZdkRBOHJQZnpRMVJYckhhUUVqZVd0Q3FWczl0dVNycmxiUGxuT3lqcWZVdkpLeW1jaG5rV0lNeTU0RzVYNVZKQTNRLWxXbE9CMkplR2xQaTlzZEJOaUU0MVMyanZZaUIwY0o3OHc?oc=5) [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5) [S29](https://news.google.com/rss/articles/CBMilwFBVV95cUxPS2hNV0dUbTNrV3hwMU9FVDNxSF9vaWE5dHlWeW9PeldOb2R4RkRMTXc3NENOTXhHc19FZ1JxOE1sZXh0MVp0Q1FKdUY5Nm5qa245THJrSjhIQ1YtcXNyRURhRHRjbzNOaVNfQ3lBU291NkpJdmlLb0ZmdDZMOURHajZVNDZqMFRvWjhGbDR5YXNuSW14aWIw?oc=5)

**반론**
- → 애크먼: 애크먼의 안전마진은 기본 시나리오 DCF에 기댄다. 그는 약세 시나리오에서 마진이 사라진다고 스스로 인정했다. 하지만 약세 시나리오의 연 수익률은 -0.3%로 원금 근처이고, 상방은 열려 있다. 나는 안전마진이 아니라 이 비대칭에 건다. 역DCF가 보여 주듯 시장은 FCF 마진 유지만 가격에 넣었고, 5배는 그 낮은 기대와 상방 사이의 간격에서 나온다. [C:irr@bear] [C:p_loss] [C:implied_cagr@m20]
- → 슬레이터: 슬레이터의 가장 강한 논거는 CAC·코호트 같은 단위경제 직접 자료가 없다는 점이다. 나는 이 점을 받아들인다. 그래도 단위경제가 규모 속에서 개선돼 온 흔적은 FCF 마진이 1.2%에서 18.8%로 오른 데 있다. 코호트 자료가 공시될 때까지 기다리면 가장 가치 있는 구간을 놓칠 수 있다. 그래서 크게 사지 않고 작게 시작하는 그의 접근에는 동의한다. [C:fcf_margin@FY2022] [C:fcf_margin@FY2025] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- → 레드팀: 레드팀의 첫 부검인 자율주행 사업자가 수요 접점을 직접 쥐는 경우는 경로의 소음이 아니라 성장 가설 자체를 깬다. 이것이 이 판단에서 가장 무거운 위험이다. 반면 3분기 가이던스가 컨센서스를 소폭 밑돈 것은 같은 가설을 깨지 못한다. 환율 불변 18~22% 성장은 가이던스 안에 있기 때문이다. 그래서 가이던스 하단 미만의 총예약액과 조정 EBITDA 마진 하락을 반증 조건에 둔다. 마진 신호는 4.5%로 잡은 레드팀 기준을 받아들여 추적한다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F202] [F205] [F200]

**인정한 점**
- 창업자가 경영하지 않고, 상방 시나리오에서도 5년 매출이 기준 연도의 2배에 못 미친다는 점은 인정한다. 이 종목은 멱법칙형 성장 아웃라이어라기보다 현금 창출형 플랫폼에 가깝다. 확신을 3에서 더 올리지 않는 이유다.
- 레드팀의 출구 배수 지적은 타당하다. 내 상방 case는 현재 P/FCF보다 높은 출구 배수에 기댄다. 5배 시나리오가 성장 가속이 아니라 마진과 배수에 의존한다는 점을 숨기지 않는다.
- 최근 분기 OCF·capex가 보도자료 기반 역산값이라는 점은 원문 대조 전까지 가정으로 취급한다.


## 슬레이터 — 찬성 (3/5)

> Uber는 시장이 아직 정의되지 않은 기업이 아니라, 이미 증명된 현금 창출 기계에 자율주행이라는 선택권이 붙은 종목이다. 크기와 지속성 면에서는 모빌리티·배달 위에 Zipline·Baidu·Wayve 같은 다자 AV 네트워크가 얹히는 구조라 천장이 보이지 않는다. 생존은 의문이 없다. FCF 마진이 FY2023 9.0%에서 FY2025 18.8%로 올랐고, 2분기 FCF는 28억 달러다. 약점은 단위경제를 직접 입증할 CAC·코호트 자료가 없다는 점이어서 `unit_economics`는 'unclear'로 두고, 확신은 3에 그친다. 기본 시나리오의 연 수익률은 +20.1%이고 손실 확률은 25%이므로, 가설이 틀렸을 때 잃는 폭이 제한적이다. 첫 비중은 작게 시작하고, 3분기 가이던스 달성과 구조조정 뒤 마진 유지가 확인되면 키운다. 가이던스가 컨센서스를 소폭 하회한 것은 가격 신호일 뿐 가설이 깨졌다는 증거는 아니다.

**논거**
- 생존과 자체 현금 창출은 증명됐다. FY2025 FCF 마진은 18.8%이고 FY2023의 9.0%에서 두 배로 올랐다. 외부 자본에 기댈 일이 없고, 순부채/EBITDA는 0.46배로 낮다. [C:fcf_margin@FY2025] [C:fcf_margin@FY2023] [C:net_debt_to_ebitda@FY2025]
- 역산하면 현재 가격이 요구하는 것이 낮다. FCF 마진이 20%에 닿으면 연 매출 성장 2.2%만으로 EV가 정당화된다. 기본 시나리오가 참이 되려면 성장이 둔화되더라도 한 자릿수 후반~두 자릿수 초반을 유지하고 마진이 18~20%대를 지키면 된다. 2분기 총예약액은 전년비 24%였고 3분기 가이던스도 환율 불변 18~22%다. [C:implied_cagr@m20] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F202]
- 기대 수익 구조가 비대칭이다. 확률 가중 기대 연 수익률은 +20.3%이고 손실 확률은 25%이다. 약세 시나리오도 연 수익률이 -0.3% 수준이라 가설이 깨져도 원금 훼손폭이 작다. P/FCF는 14.27배, FCF 수익률은 7.0%이다. [C:expected_irr] [C:p_loss] [C:irr@bear] [C:p_fcf] [C:fcf_yield]
- 지속성의 선택권은 AV 파트너 확장에 있다. Baidu Apollo Go의 두바이 운행, Wayve의 영국 첫 승차, 스페인 로보택시 허가가 모두 Uber를 수요 집합자로 두는 구조다. 다만 이는 회사 발표와 보도 수준이어서 아직 계획이지 실적이 아니다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5)
- 자본배분이 증거로 확인된다. FY2025 자사주 매입 65.2억 달러가 SBC 18.3억 달러를 넘어 희석 주식 수가 FY2024 21.5억에서 FY2026Q2 20.5억으로 줄었다. 분기 SBC가 FY2026Q2 5.6억 달러로 늘고 있는 점은 지켜볼 대상이다. [F4] [F156] [F55] [F61] [F161]

**사전 부검**
- 사전 부검 1: 자율주행 사업자가 차량 공급을 직접 쥐고 수수료율을 낮추라고 요구하면, 마진 개선 가설이 깨진다. 지금 근거는 파트너십 발표뿐이라 수수료 구조는 확인되지 않았다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5)
- 사전 부검 2: 3분기 가이던스가 컨센서스를 소폭 하회한 것이 성장 둔화의 시작일 수 있다. 총예약액 가이던스 중간값과 Non-GAAP EPS 가이던스가 모두 추정치 아래였다. 보수적 가이던스가 아니라 구조적 둔화라면 기본 시나리오의 성장 경로가 낮아진다. [F202] [F205] [F204] [F206] [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow)
- 사전 부검 3: 3,300명 구조조정과 성폭행 소송 합의 비용이 조정 EBITDA 밖에 반복적으로 쌓이면 조정 이익이 현금 창출력을 과대표시한다. 최근 분기 OCF·capex도 보도자료 기반 역산값이라 원문 대조가 남아 있다. [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5) [F216] [F214]

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 AV 파트너가 다자로 늘수록 수요 집합자의 협상력이 유지된다는 것이다. 그런데 Baidu 두바이, Wayve 영국, 스페인 허가는 모두 출범 발표 수준이다. 수수료 구조나 이용 규모는 공개된 적이 없어서 아직 계획이지 실적이 아니다. 파트너가 여럿이라는 사실은 Uber의 지위를 보여 주기도 하지만 AV 사업자에게 대안이 많다는 뜻이기도 하다. 그래서 나는 이 가설을 5배의 근거로 쓰지 않고, 총예약액 대비 조정 EBITDA 마진이 유지되는지로만 검증한다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5) [F200]
- → 애크먼: 애크먼의 가장 강한 논거는 기본 시나리오 안전마진이 문턱을 넘는다는 것이다. 이 안전마진은 출구 배수와 FCF 마진 20%라는 두 가정 위에 서 있다. 둘 다 현재 수준보다 높은 값이다. 약세 시나리오의 현재가치는 주가 아래이므로 안전마진은 하방을 막아 주지 못한다. 나는 가격 대비 할인이 아니라 가설이 분기마다 입증되는지를 보고, 그래서 비중을 작게 시작한다. [C:mos@ackman] [C:exit_multiple@base] [C:fcf_margin@FY2025] [C:iv@bear]
- → 레드팀: 레드팀의 가장 강한 지적은 기본 시나리오의 주식 수 감소와 현금 축적이 동시에 성립하는지 모델이 보여 주지 않는다는 것이다. 매입 기간에 현금은 줄고 부채는 늘었다. 생존 판정은 코드가 계산한 현금 경로로 하므로 이 지적은 생존 여부보다 매입 지속성에 관한 것이다. 그래서 `must_be_true`의 희석 주식 수 조건을 유지하고, 현금 완충이 얇아지는 신호는 반증 조건으로 추적한다. 출구 배수는 레드팀 말대로 현재 배수보다 높게 둘 근거가 약해서 case에서 낮춘다. [F4] [F6] [F23] [F43] [C:share_change@FY2025] [C:p_fcf] [C:exit_multiple@base]

**참이어야 하는 것**
- [on_track] 조정 EBITDA 마진이 총예약액 대비 4% 이상으로 유지된다
- [on_track] 희석 주식 수가 21.5억 주를 넘지 않는다 (매입이 SBC 희석을 상쇄)
- [on_track] 분기 FCF가 20억 달러 이상을 유지한다
- [on_track] 3분기 총예약액이 가이던스 하단 이상으로 나온다

**인정한 점**
- 기본 시나리오의 출구 배수가 현재 배수보다 높다는 레드팀 지적을 인정한다. 이 가정은 성장이 둔화한다는 시나리오와도 맞지 않는다. case의 출구 배수를 현재 배수 근처로 낮추고, 수익률이 줄어도 입장은 바꾸지 않는다.
- 단위경제를 직접 입증하지 못하고, 최근 분기 OCF와 capex는 보도자료에서 역산한 값이다. 이 불확실성을 반영해 시작 비중을 낮춘다.
- 애크먼의 안전마진과 앤더슨의 상방 모두 약세 시나리오 앞에서 사라진다는 점을 인정한다. 내 찬성은 가격이 싸다는 판단이 아니라 현금 창출 증거와 작은 비중의 비대칭에 기댄다.


## 애크먼 — 반대 (3/5)

> Uber는 승차·배달 수요를 모아 수수료와 광고로 매출화하는 플랫폼이라 한 문단으로 설명된다. 규모가 커지며 FCF 마진이 두 배가 됐고, 순부채/EBITDA가 낮아 자본시장에 기대지 않는다. 기본 시나리오로 계산한 안전마진은 하네스 문턱을 넘는다. 시장 가격은 FCF 마진 유지만 반영하고 성장은 거의 반영하지 않는다. 다만 해자는 아직 회사 주장 수준이고 자율주행이 수수료율을 누를 수 있다. 약세 시나리오의 가치는 현재 주가 아래다. 그래서 크게 담을 확신은 아니고 찬성 쪽 중간 확신으로 둔다. 촉매는 행동주의가 아니라 구조조정과 자사주 매입이다.

**논거**
- 사업은 승차·배달 수요를 모아 수수료를 받는 플랫폼으로 한 문단에 설명된다. 매출은 18% 안팎으로 성장했고, 가장 중요한 변화는 FCF 마진이 9.0%에서 18.8%로 오른 점이다. 10년 뒤 FCF는 범위로 추정할 수 있다. 다만 그 하단이 자율주행 시나리오에 달려 있다. [C:revenue_growth@FY2025] [C:fcf_margin@FY2023] [C:fcf_margin@FY2025] [F136]
- 재무가 단단하다. 순부채/EBITDA는 낮고 TTM FCF 수익률은 7.0%다. 2분기 FCF는 28억 달러이고 TTM FCF는 100억 달러를 넘었다. 부채 상환이 자본시장 접근에 달려 있지 않다. 밸리언트형 위험은 보이지 않는다. [C:net_debt_to_ebitda] [C:fcf_yield] [F201] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- 가격이 싸다. 기본 case의 주당 내재가치는 109.0, 주가는 70.3, 안전마진은 35.4%로 20% 문턱을 넘는다. 역DCF를 보면 FCF 마진 20%에서 시장이 가정하는 매출 성장은 연 2.2%뿐이다. 성장 없는 마진 유지만 가격에 들어 있다. [C:mos@ackman] [C:intrinsic_value@ackman] [C:price@ackman] [C:implied_cagr@m20]
- 자본배분이 일관된다. FY2025 자사주 매입 65.2억 달러가 SBC 18.3억 달러를 크게 넘어, 희석 주식 수가 FY2024 21.5억에서 FY2026Q2 20.5억으로 줄었다. 낮은 멀티플에서 주당 가치를 쌓는 구조다. SBC 차감 후에도 FCF가 남는다. [F4] [F156] [F55] [F61] [C:fcf_after_sbc@FY2025]
- 해자는 주장 수준이다. 규모가 커지며 영업이익률이 3.0%에서 10.7%로 오른 것은 입증됐지만, 네트워크·전환비용 해자는 회사 발표와 간접 추정에 그친다. 승차와 배달은 다중 앱 이용이 가능해 가격결정력이 확인되지 않았다. 그래서 확신을 4~5가 아니라 3에 둔다. [C:operating_margin@FY2023] [C:operating_margin@FY2025] [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S38](https://news.google.com/rss/articles/CBMingFBVV95cUxQamNCcUc3Tzg5Tk1NUXZmRW4zc0RsVTZxZ1VIbV94Ykh5STItcjVYVFFTUUdxMGJfOGxab0d6bVpZMUlCRV9GdTRBOHRPSUFHVnNiWW1fOXdzWmphd3dqZXdycC0zcG4wcV9qQk15ZTgyYjhjN09aeXFDMEFFQzkyc0VyVk4yUHhjdFVYOEp5X2ZUMzFBMXVCY0xlb3RMZw?oc=5)

**사전 부검**
- 사전 부검: 자율주행 사업자가 차량 공급을 쥐고 수수료율을 낮추면 FCF 마진이 꺾인다. 약세 시나리오의 현재가치는 43.13으로 주가보다 낮고 손실 확률은 25%다. 안전마진은 이 시나리오 앞에서 사라진다. [C:iv@bear] [C:p_loss] [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5)
- 사전 부검: 이익의 질이 보이는 것보다 약하다. 순이익에는 지분 재평가 이익과 세금 이익이 섞여 있고, 최근 분기 OCF·capex는 보도자료에서 역산한 값이다. 구조조정과 소송 정산이 조정 EBITDA 밖으로 반복해서 빠지면 실제 FCF는 낮아진다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F86] [F104] [F216] [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5)
- 사전 부검: 3분기 총예약액·EPS 가이던스 중간값이 컨센서스를 밑돌았다. 성장 둔화가 일시적이 아니라 구조적이면 기본 시나리오의 성장 경로와 출구 멀티플이 모두 낮아진다. [F202] [F205] [F204] [F206] [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow)

**반론**
- → 앤더슨: 앤더슨의 '10년 뒤 5배'는 상방 시나리오의 5년 매출이 기준의 2배에도 못 미치고(C:revenue_5y 1.83배), 마진 확대와 출구 배수에 기대는 계산이다. 이는 생존자 편향에 취약하다. 나는 상방이 아니라 기본 시나리오로 안전마진을 본다. 역DCF가 보여 주듯 시장이 넣은 성장은 FCF 마진 20%에서 연 2.2%뿐이므로, 5배가 아니라 마진 유지만으로도 가격이 정당화되는지가 내 판단 기준이다. [C:implied_cagr@m20] [C:implied_cagr@m15] [C:mos@ackman]
- → 슬레이터: 슬레이터의 생존 경로와 현금 창출은 필요조건이다. 그러나 약세 시나리오 연 수익률 -0.3%는 '원금 훼손폭이 작다'는 뜻이지 가격이 싸다는 증명이 아니다. 단위경제는 'unclear'로 직접 입증되지 않았고, 좋은 회사도 비싸게 사면 나쁜 투자다. 내가 찬성하는 이유는 생존이 아니라 기본 case 안전마진 35.4%가 20% 문턱을 넘기 때문이다. [C:irr@bear] [C:mos@ackman] [C:p_fcf]
- → 레드팀: 레드팀이 지적한 출구 P/FCF 16배는 현재 14.27배보다 높아 약한 가정이다. 이를 12배로 낮추고 FCF 마진을 15%로 보수화한 가치를 case로 다시 보면 안전마진이 얼마나 남는지가 관건이며, 약세 현재가치 43.13은 주가보다 낮아 그 구간에서는 안전마진이 사라진다. 그래서 확신을 3에서 올리지 않고, 사전 부검이 FCF 범위의 하단을 넓힌다는 점을 반영해 보수 case로 판정한다. 최근 분기 OCF·capex가 역산 근사치라는 지적도 받아들인다. [C:p_fcf] [C:iv@bear] [C:p_loss] [F214] [F216]

**인정한 점**
- 앤더슨: 상방 5배는 마진·배수 의존이며 성장 가속이 아니라는 점을 인정한다. 그래서 상방이 아닌 기본·보수 case로 판단한다.
- 슬레이터: 생존과 자본 환원이 증명됐다는 점은 인정하나 가격의 정당화는 안전마진이 따로 해야 한다.
- 레드팀: 출구 배수 16배와 FCF 마진 20%는 약한 가정이며 base 안전마진 35.4%는 낙관 쪽으로 기울어 있다. 이를 반영해 보수 case로 전환하고 확신은 3에 둔다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Uber는 승차 공유(모빌리티)·음식 배달(Eats)·화물 중개 플랫폼으로, 운전자·가맹점과 소비자를 연결하고 총예약액의 일부를 수수료·광고로 매출화한다. 2분기 총예약액은 580억 달러(전년비 24%)로 성장했고 조정 EBITDA는 28.2억 달러(총예약액 대비 4.9%), 잉여현금흐름은 28억 달러로 TTM 100억 달러를 넘었다(S43). 영업이익률은 FY2022 -5.7%에서 FY2025 10.7%로, FCF 마진은 1.2%에서 18.8%로 개선되어(C:operating_margin@FY2025, C:fcf_margin@FY2025) 규모의 단위경제는 개선 중이다. 다만 CAC·이탈률·코호트·부문별 수익성 공시는 이번 근거에 없어 단위경제를 직접 입증하지는 못한다. 자율주행(Waymo 외 Baidu·Wayve 등)은 수요 플랫폼으로서의 기회이자 공급 측 교란 위험이다.

- [unit_economics] 2026년 2분기 총예약액 대비 조정 EBITDA는 4.9%, 잉여현금흐름은 28억 달러다. 수익성은 총예약액 기준으로 개선 중이나 부문별(모빌리티·배달·화물) 마진, CAC, 이탈률은 공시 근거에서 찾지 못해 고객 단위 경제성은 직접 확인되지 않는다. [F199] [F200] [F201] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- [unit_economics] 자금 창출력은 크게 개선되었다. FCF는 FY2023 33.6억에서 FY2025 97.6억 달러로 늘었고, TTM FCF 수익률은 7.0%다. SBC는 매출의 3.5%로 FY2021 6.7%에서 낮아졌고, SBC 차감 FCF도 79.4억 달러로 남는다. 이익의 질은 양호하다. [C:fcf@FY2025] [C:fcf_yield] [C:sbc_to_revenue@FY2025] [C:fcf_after_sbc@FY2025]
- [industry] 경쟁 강도와 점유율은 이번 근거로 확인되지 않는다. 산업 구조상 승차·배달은 다중 앱 이용이 가능해 전환비용이 낮을 수 있고, 규제(Nigeria 철수와 반독점 조사, 소송 정산)가 지역별 리스크로 나타난다. 이는 추정:이며 보도 수준 근거다. [S26](https://news.google.com/rss/articles/CBMirgFBVV95cUxNZjJweERweGlzcGVEZV9nRWNmaGdXSFpwXzhsZ2luOV9XMThzTFFqWEgxRXZXLXFUekhkMjJZbTB5R3J0enBNQnBtMGRoRDZHTnozQ2dIVFFEUUZmdktwMHlvenNZbXJBSWZfOXpteG1EeWNGUEhYaXZMSGNIZW4wZk1iR1c1clhpdUlHWFNzZlA4aVp4VnJNZklpYWhiU0Z3c3pGcWdFT2JSd09Yb3c?oc=5) [S29](https://news.google.com/rss/articles/CBMilwFBVV95cUxPS2hNV0dUbTNrV3hwMU9FVDNxSF9vaWE5dHlWeW9PeldOb2R4RkRMTXc3NENOTXhHc19FZ1JxOE1sZXh0MVp0Q1FKdUY5Nm5qa245THJrSjhIQ1YtcXNyRURhRHRjbzNOaVNfQ3lBU291NkpJdmlLb0ZmdDZMOURHajZVNDZqMFRvWjhGbDR5YXNuSW14aWIw?oc=5) [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5)
- [industry] 자율주행은 공급 측 구조를 바꿀 수 있다. Uber는 Baidu(두바이), Wayve(영국), 스페인 로보택시 허가 등 다자 파트너 네트워크를 구축 중이다. 수요 집합자로서 지위를 지키면 기회이고, 차량 보유 주체가 AV 사업자로 이동하면 수수료율이 압박받을 수 있다. 어느 쪽인지 근거로는 판단이 안 된다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5) [S37](https://news.google.com/rss/articles/CBMiogFBVV95cUxNWXdxWlBSU0tMMnp3LWgzTkFUZHJIWC0xcVpVSFVHSnZCcnlNenlQS0pib2RBZXVaUDVBZzZCZ2FpVm8zOEVpeENEeHdoOGxFLWlULURSU0QyWVJtUDhwbnBfWW5QZy13TGJjOGpSTjBpazVPX3FrNkU1NEZuVmxtOWdDU2ZJUmhyWWVtMFA3empfX0t5Rno0TWE5NWNmV0JoeVE?oc=5)
- [customers] 성장 둔화 신호가 있다. 2분기 총예약액은 전년비 24%(환율 불변 22%)이나 3분기 가이던스는 환율 불변 18~22%로 낮아지고 중간값이 컨센서스를 소폭 하회했다. Non-GAAP EPS 가이던스 0.84~0.88도 컨센서스 0.89 아래다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F202] [F205] [F204] [F206]
- [runway] 재투자 활주로는 넓지만 효율은 미확인이다. 설비투자는 매출의 약 0.7%(FY2025 3.4억)로 자본 집약도가 낮고, 현금의 대부분은 자사주 매입(FY2025 65.2억, FY2026Q1 30.1억 달러)으로 쓰인다. 이는 경영진이 내부 재투자 수익률보다 매입을 선호함을 시사하며, 희석 주식 수는 FY2024 21.5억에서 FY2026Q2 20.5억으로 줄었다. [F11] [F4] [F6] [F55] [F61] [C:share_change@FY2025]
- [runway] 역DCF상 현재 EV로 FCF 마진 20%에 도달하면 매출 연 2.2% 성장만으로 정당화된다. 마진이 15%로 머물면 5.1% 성장이 필요하다. 시장은 높은 성장보다 현 FCF 마진의 지속성을 가격에 반영하고 있어, 사업 질의 핵심은 마진 유지 여부(AV 위협, 규제, 소송 비용)다. [C:implied_cagr@m20] [C:implied_cagr@m15] [C:ev]
- [unit_economics] 회계 신호는 없고 DSO는 51.0일(FY2021)에서 26.9일(FY2025)로 낮아졌으나 FY2026Q2 매출채권은 43.0억 달러로 증가세다. 순이익 24억 달러에는 지분 재평가 이익 세전 16억이 포함되어 있어(S43) 사업 수익력은 영업이익 18.9억 달러 기준으로 봐야 한다. [C:dso@FY2025] [F131] [F121] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- [claimed] 운전자·소비자·가맹점 양면 네트워크와 Eats·모빌리티 교차 이용이 해자의 핵심이라는 주장. 이용자 수·점유율·이탈률 같은 직접 지표가 이번 근거에 없어 매출 성장과 마진 개선으로 간접 추정만 가능하다. 매출은 FY2022 318.8억에서 FY2025 520.2억 달러로 성장했다. [F136] [F133] [C:revenue_growth@FY2025]
- [proven] 규모가 커지면서 마진이 올랐다. 연 매출 성장률 17~18%를 유지하며 영업이익률은 3.0%(FY2023)에서 10.7%(FY2025)로, FCF 마진은 9.0%에서 18.8%로 올랐다. R&D는 매출 대비 약 6.5%(FY2025 34.0억/520.2억)로 매출보다 느리게 늘었다는 점이 운영 레버리지 흔적이다. 다만 경쟁사 대비 마진 비교는 없다. [C:operating_margin@FY2025] [C:operating_margin@FY2023] [C:fcf_margin@FY2025] [C:fcf_margin@FY2023] [F146] [F136]
- [claimed] Costco 배달 확대 등 제휴와 Zipline·Baidu·Wayve 같은 자율주행 파트너 확장은 플랫폼 지위를 보여주나, 이는 회사 발표와 보도(S22, S30, S32, S38)이며 가격 인상 후 이용자 유지 기록은 없다. [S22](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQclNPVTE0M0xWUGpKVlMwT2VXLU9SaVBKbjdDOWRtTjhBelVBYnBwSzUzemlXVHBuQ3IybU1aQWZuZUZBZ2FJZEV4bFFkSGN0c0o0cE1tZ2MteUMxRU91RW03LVFKaE9faTBQaW54TWFtdFJ4WEcxQlcxaDFiSl8taWRwWEJyX1B2X25DakI1SmRFU1ZSdjh1NVBHOTMtckJzX183R181bUtQdDI1VkZSQmc2OWctMVZCcnJkWDNsaHFiMlVLX3JEZVVfX3VXenVia3FZZ1ZaV2RoVWQ2dl9uZGxhcjhZcjlFcUozSQ?oc=5) [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S38](https://news.google.com/rss/articles/CBMingFBVV95cUxQamNCcUc3Tzg5Tk1NUXZmRW4zc0RsVTZxZ1VIbV94Ykh5STItcjVYVFFTUUdxMGJfOGxab0d6bVpZMUlCRV9GdTRBOHRPSUFHVnNiWW1fOXdzWmphd3dqZXdycC0zcG4wcV9qQk15ZTgyYjhjN09aeXFDMEFFQzkyc0VyVk4yUHhjdFVYOEp5X2ZUMzFBMXVCY0xlb3RMZw?oc=5)

### 경영진·자본배분 — mixed

자본배분 쪽 증거는 주주 친화적이다. FY2025 자사주 매입 65.2억 달러가 SBC 18.3억 달러를 크게 넘어서 희석 주식 수가 줄었고(FY2025 -1.4%), FY2026Q2에는 20.5억 주까지 내려왔다. 반면 보상 지표(DEF 14A), 내부자 매매, 과거 가이던스 적중률은 수집되지 않아 정렬의 핵심인 '무엇에 보상받는가'를 판단할 수 없다. 최근 3분기 가이던스가 컨센서스를 소폭 밑돈 점과 대규모 조직 개편(S25, S27)은 중립적 관찰로만 남긴다. 따라서 'mixed'로 둔다.

- [compensation] 근거 없음. DEF 14A(S10)는 목록에 있으나 보상 연동 지표(장기 FCF·ROIC 대 단기 EPS·조정 EBITDA)와 베스팅 기간이 수집되지 않았다. 회사가 조정 EBITDA와 Non-GAAP EPS를 핵심 지표로 공표하는 것(S43)은 사실이지만, 이것이 보상 지표인지는 확인되지 않는다. [S10](https://www.sec.gov/Archives/edgar/data/1543151/000130817926000125/uber014597-def14a.htm) [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도는 수집되지 않았다. 경영진 변동 8-K(S6, S13)가 있으나 내용은 확인되지 않아 평가하지 않는다. [S6](https://www.sec.gov/Archives/edgar/data/1543151/000155278126000320/e26247_uber-8k.htm) [S13](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000011/uber-20260130.htm)
- [guidance] 과거 가이던스와 실제의 대조 자료가 없어 적중률(C:guidance_hit_rate)을 계산할 수 없다. 확인된 것은 최근 1건뿐이다. 3분기 총예약액 가이던스 중간값 592.5억 달러는 컨센서스 593.3억 달러를 소폭 밑돌고, Non-GAAP EPS 가이던스 중간값 0.86달러는 컨센서스 0.89달러를 밑돈다. 신뢰도 판단에는 표본이 부족하다. [F202] [F205] [F204] [F206] [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow)
- [dilution] 희석 주식 수는 FY2023 20.9억, FY2024 21.5억(+2.8%)에서 FY2025 21.2억(-1.4%), FY2026Q2 20.5억으로 줄었다. SBC는 FY2025 18.3억 달러로 매출의 3.5%이고, 이 비율은 FY2021 6.7%에서 꾸준히 낮아졌다. 다만 분기 SBC는 FY2025Q2 4.8억 달러에서 FY2026Q2 5.6억 달러로 늘었다. 매입이 희석을 가리는 수준이 아니라 상쇄하고도 남는 규모라는 점이 확인된다. [C:share_change@FY2025] [C:share_change@FY2024] [C:sbc_to_revenue@FY2025] [C:sbc_to_revenue@FY2021] [F61] [F158] [F161]
- [capital_allocation] 자사주 매입은 FY2022~FY2023 0, FY2024 12.5억 달러, FY2025 65.2억 달러, FY2026Q1 30.1억 달러로 급증했다. FY2025 FCF 97.6억 달러의 약 3분의 2에 해당한다. 매입 평균 가격은 확인되지 않아 고점 매입 여부는 판단할 수 없다. 현재 P/FCF는 14.27배다. [F3] [F4] [F6] [C:fcf@FY2025] [C:p_fcf]
- [capital_allocation] 재투자와 M&A 쪽에서는 영업권이 FY2026Q1 89.2억 달러에서 FY2026Q2 94.7억 달러로 늘어 새로운 인수가 있었음을 시사하지만, 대상과 가격, 수익률 자료는 없다. 총부채는 FY2024 83.5억 달러에서 FY2026Q2 107.3억 달러로 늘었고 현금은 FY2025 71.0억 달러에서 FY2026Q2 48.7억 달러로 줄었다. 순부채/EBITDA는 FY2025 기준 0.46배로 낮다. [F80] [F81] [F37] [F43] [F21] [F23] [C:net_debt_to_ebitda@FY2025]
- [capital_allocation] 2026년 9월 기업 직원 감축과 관리 구조 개편(S24, S25, S27) 및 나이지리아 철수(S29)가 보도됐다. 구조조정 비용과 절감 효과는 수집되지 않았다. 사업 정리 의지의 신호일 수는 있으나 자본배분 수익률로 환산할 근거는 없다. [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) [S25](https://news.google.com/rss/articles/CBMirgFBVV95cUxQelprYTZqU1R2cFNKc2lqX0NZdGFxR0tyVjI0OGRUNFJHSHJJSkkzWmlfNGY0cXc2ZmpZaUc2X3RHZ3h5eEx1U2xZdkRBOHJQZnpRMVJYckhhUUVqZVd0Q3FWczl0dVNycmxiUGxuT3lqcWZVdkpLeW1jaG5rV0lNeTU0RzVYNVZKQTNRLWxXbE9CMkplR2xQaTlzZEJOaUU0MVMyanZZaUIwY0o3OHc?oc=5) [S27](https://news.google.com/rss/articles/CBMiZEFVX3lxTE85bEp6SC12Ukx6bDZRb2hQU2FsbmhreFpnSVBIcHNjb0JIQ2YteWdLdkVndUYwRi1vc01waS1GRDJwUHlGTENQVG1Ec2FLUlplRWM0SF93V29GYXZ6TmFoWGlZRFI?oc=5) [S29](https://news.google.com/rss/articles/CBMilwFBVV95cUxPS2hNV0dUbTNrV3hwMU9FVDNxSF9vaWE5dHlWeW9PeldOb2R4RkRMTXc3NENOTXhHc19FZ1JxOE1sZXh0MVp0Q1FKdUY5Nm5qa245THJrSjhIQ1YtcXNyRURhRHRjbzNOaVNfQ3lBU291NkpJdmlLb0ZmdDZMOURHajZVNDZqMFRvWjhGbDR5YXNuSW14aWIw?oc=5)

### 회계 품질 — watch

코드가 계산한 회계 품질 신호는 하나도 없다. 영업현금흐름이 순이익을 뒷받침하고, 발생액 비율과 매출채권 증가도 정상 범위다. 다만 GAAP 순이익은 일회성 항목으로 부풀어 있어 영업이익과 영업현금흐름·FCF 기준으로 봐야 한다. FY2024 순이익 98.6억 달러에는 세금 이익 -57.6억 달러가, FY2025 순이익 100.5억 달러에는 세금 이익 -43.5억 달러(FY2025Q3 -40.5억 달러)가 들어 있다. 둘 다 이연법인세 자산 인식으로 보이며, 이 비용 항목은 영업과 무관하다. 그래서 TTM PER 15.06배는 낙관적으로 낮게 나오고, 이 이익이 빠지면 PER은 올라간다. FY2026Q2 순이익 24억 달러에는 지분 재평가 이익 세전 16억 달러도 포함되어 있다(S43). 이 이익은 영업과 무관하고 반복되지 않는다. Non-GAAP인 조정 EBITDA(F199)는 SBC와 기타 조정이 영업이익에 더해진 값이어서, 실제 현금 창출력은 SBC 차감 FCF(C:fcf_after_sbc@FY2025)로 보는 것이 맞다. 최근 분기 OCF·capex는 보도자료와 2차 요약에서 가져와 역산한 값이라 원문 확인이 남아 있다. 구조조정(3,300명 감원)과 소송 충당금은 아직 숫자로 확인되지 않았다. 숫자 자체를 믿을 수 없는 근거는 없으므로 red_flag는 아니다. 순이익 대신 영업이익·OCF·SBC 차감 FCF를 기준으로 조정해서 보는 조건으로 watch로 판정한다.

- [watch] GAAP 순이익이 세금 이익으로 부풀어 있다. FY2024 법인세 -57.6억 달러, FY2025 -43.5억 달러(FY2025Q3 -40.5억 달러)가 이익을 키웠다. 이 영향으로 FY2025 순이익 100.5억 달러가 영업이익 55.6억 달러보다 크다. 순이익 기반 지표(PER, FCF/순이익)는 왜곡되므로 영업이익과 FCF 기준으로 평가해야 한다. 현금 지표는 이 영향을 받지 않는다. [F85] [F86] [F89] [F99] [F116] [C:fcf_conversion@FY2025] [C:pe]
- [watch] FY2026Q2 순이익 24억 달러에는 지분 재평가 이익 세전 16억 달러가 들어 있다. 영업 외 평가이익이어서 반복성이 없고, FY2026Q1 순이익 2.6억 달러와의 변동도 이 평가손익 때문으로 보인다. 분기 순이익 추이로 이익 체력을 판단하면 안 된다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F103] [F104]
- [watch] 조정 EBITDA 28.2억 달러(총예약액 대비 4.9%)는 영업이익 18.9억 달러에 D&A 1.9억 달러와 SBC 5.6억 달러를 더하고도 남는 기타 조정이 더해진 값이다. 기타 조정은 세부 내역(법적·구조조정·기타)을 확인하지 못했다. 반복적 법적 비용이나 구조조정이 일회성으로 분류되는지 확인해야 한다. 가이던스(F203)도 같은 Non-GAAP 기준이다. [F199] [F200] [F121] [F33] [F161] [F203]
- [info] SBC는 매출 대비 3.5%이고 영업현금흐름 대비 18.1%로 과도하지 않다(FY2025). 문턱값 이하이며 추세도 개선되고 있다. 희석 주식 수는 FY2024 21.5억에서 FY2026Q2 20.5억으로 줄었다. 다만 감소는 자사주 매입(FY2025 65.2억 달러, FY2026Q1 30.1억 달러)이 SBC 희석을 상쇄한 결과이므로, FCF 일부는 사실상 SBC 상쇄에 쓰인다. SBC 차감 FCF가 실제 주주 몫에 가깝다. [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [C:fcf_after_sbc@FY2025] [F55] [F61] [F4] [F6]
- [info] 발생액 비율이 FY2025 -0.1%이고 FY2024 6.0%로 문턱을 넘지 않으며 DSO도 26.9일로 개선되었다. 영업현금흐름 101.0억 달러가 FY2025 영업이익 55.6억 달러를 웃돌아 이익의 현금 뒷받침이 충분하다. 매출채권은 FY2026Q2 43.0억 달러로 증가했지만 매출 성장과 큰 격차 없이 움직여 채권 부풀리기 신호는 없다. [C:accruals_ratio@FY2025] [C:dso@FY2025] [F109] [F116] [F131] [F141]
- [info] 영업권이 FY2026Q2 94.7억 달러로 FY2026Q1 89.2억 달러보다 늘었다. 인수에 따른 증가로 보이며 총자산 대비 비중은 낮아 영업권 문턱과 거리가 멀다. 영업권 증가가 인수 대금과 일치하는지는 10-Q 주석으로 확인해야 한다. [F80] [F81] [F182] [S3](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000032/uber-20260630.htm)
- [info] 공시 목록에서 8-K 4.02 재무제표 정정과 4.01 감사인 변경을 시사하는 항목은 없다(코드 신호도 없음). 감사의견·핵심감사사항·계속기업 의문 여부는 10-K 원문을 확인하지 못했다. [S11](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm) [S3](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000032/uber-20260630.htm)
- [watch] FY2025Q3·FY2025Q4·FY2026Q2의 영업현금흐름과 capex는 현금흐름표 원문이 아니라 보도자료와 2차 요약에서 가져왔고, capex는 OCF에서 FCF를 뺀 역산 근사치다. TTM FCF 100억 달러 초과(S43)는 회사 발표 수치로, 10-Q·10-K 현금흐름표의 설비투자 항목으로 대조하지 못했다. 반올림 오차 범위는 작지만 확인 전까지는 가정으로 취급한다. [F212] [F214] [F216] [F201] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- [watch] 3,300명 규모 구조조정(전체 인력의 약 10%)이 발표되어 이후 분기에 퇴직 비용이 발생한다. 이 비용이 조정 EBITDA에서 제외되는지가 조정 이익의 질을 가른다. 성폭행 소송 합의(세 번째 bellwether)도 충당금과 합의금 규모가 아직 공시 사실로 확보되지 않았다. 둘 다 정량이 없어 red로 올릴 근거는 없다. [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) [S25](https://news.google.com/rss/articles/CBMirgFBVV95cUxQelprYTZqU1R2cFNKc2lqX0NZdGFxR0tyVjI0OGRUNFJHSHJJSkkzWmlfNGY0cXc2ZmpZaUc2X3RHZ3h5eEx1U2xZdkRBOHJQZnpRMVJYckhhUUVqZVd0Q3FWczl0dVNycmxiUGxuT3lqcWZVdkpLeW1jaG5rV0lNeTU0RzVYNVZKQTNRLWxXbE9CMkplR2xQaTlzZEJOaUU0MVMyanZZaUIwY0o3OHc?oc=5) [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (15%) 자율주행이 수수료 구조를 바꿔 Uber가 수요 집합자 자리를 잃었다. Baidu, Wayve, 스페인 허가처럼 파트너가 여럿이라는 점은 Uber의 지위를 보여 주는 동시에 AV 사업자의 대안이 많다는 뜻이다. 차량을 보유한 AV 사업자가 자체 앱이나 다른 플랫폼으로 수요를 직접 받기 시작하면, 승차·배달이 이미 다중 앱으로 쓰이는 탓에 이용자는 쉽게 옮겨 간다. Uber는 총예약액을 지키려고 수수료를 내리거나 보조금을 쓰게 되고, 마진 개선 서사가 꺾이면서 시장이 FCF 배수를 낮췄다. 지금의 FCF 마진 18.8%는 이 구조 변화를 반영하지 않은 값이다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5) [S37](https://news.google.com/rss/articles/CBMiogFBVV95cUxNWXdxWlBSU0tMMnp3LWgzTkFUZHJIWC0xcVpVSFVHSnZCcnlNenlQS0pib2RBZXVaUDVBZzZCZ2FpVm8zOEVpeENEeHdoOGxFLWlULURSU0QyWVJtUDhwbnBfWW5QZy13TGJjOGpSTjBpazVPX3FrNkU1NEZuVmxtOWdDU2ZJUmhyWWVtMFA3empfX0t5Rno0TWE5NWNmV0JoeVE?oc=5) [F200] [C:fcf_margin@FY2025]
- (12%) 총예약액 성장이 일시적 둔화가 아니라 구조적 둔화로 굳었다. 2분기 환율 불변 22%에서 3분기 가이던스는 18~22%로 낮아졌고, 가이던스 중간값이 컨센서스를 밑돌았다. 이것이 한 번이 아니라 연속되면 시장은 성장주 배수를 거두고, 모델이 가정한 출구 P/FCF 16배는 약세 시나리오의 12배로 내려간다. 높은 FCF 마진이 성장이 멈춘 뒤에도 유지된다는 보장은 없다. 성장이 한 자릿수로 내려가면 보조금과 광고 확대 같은 방어 지출이 늘고 마진도 같이 눌린다. [F202] [F205] [F204] [F206] [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow) [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- (8%) 소송·규제·구조조정 비용이 조정 항목 밖에서 반복적으로 쌓여 현금이 실제로 줄었다. 성폭행 소송은 세 번째 bellwether 사건까지 합의로 끝났지만 충당금과 합의금 규모가 공시로 확인되지 않는다. 앞으로의 사건도 같은 방식으로 이어질 수 있다. 나이지리아 반독점 조사처럼 지역 규제 이슈가 늘고, 3,300명 감원의 퇴직 비용도 일회성으로 분류돼 조정 EBITDA에서 빠진다. 조정 EBITDA는 건강해 보이는데 FCF가 이를 따라가지 못하면서 시장이 조정 지표를 불신하게 되었다. [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5) [S26](https://news.google.com/rss/articles/CBMirgFBVV95cUxNZjJweERweGlzcGVEZV9nRWNmaGdXSFpwXzhsZ2luOV9XMThzTFFqWEgxRXZXLXFUekhkMjJZbTB5R3J0enBNQnBtMGRoRDZHTnozQ2dIVFFEUUZmdktwMHlvenNZbXJBSWZfOXpteG1EeWNGUEhYaXZMSGNIZW4wZk1iR1c1clhpdUlHWFNzZlA4aVp4VnJNZklpYWhiU0Z3c3pGcWdFT2JSd09Yb3c?oc=5) [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) [S25](https://news.google.com/rss/articles/CBMirgFBVV95cUxQelprYTZqU1R2cFNKc2lqX0NZdGFxR0tyVjI0OGRUNFJHSHJJSkkzWmlfNGY0cXc2ZmpZaUc2X3RHZ3h5eEx1U2xZdkRBOHJQZnpRMVJYckhhUUVqZVd0Q3FWczl0dVNycmxiUGxuT3lqcWZVdkpLeW1jaG5rV0lNeTU0RzVYNVZKQTNRLWxXbE9CMkplR2xQaTlzZEJOaUU0MVMyanZZaUIwY0o3OHc?oc=5) [F199] [F201]
- (5%) 자본배분 실패. FCF를 자사주 매입에 쓰는 동안 현금은 줄고 부채는 늘었다. 인수로 영업권이 한 분기에 늘었는데 대상과 수익률이 공개되지 않았다. 매입이 고점에서 이뤄졌고 인수 수익률이 낮았다면, 주식 수 감소로 얻은 주당 가치 성장이 사라진다. 성장 투자와 AV 파트너십에 자금이 필요한 시점에 현금이 얇으면 부채나 주식으로 조달해야 하고, 모델의 연 주식 수 감소 가정이 반대로 움직인다. [F21] [F23] [F41] [F43] [F80] [F81] [F4] [F6]
- 약한 가정 `base.exit_multiple`: 기본 시나리오는 출구 P/FCF 16배를 쓰는데 현재 배수는 14.27배다. 수익률 분해에서 멀티플 변화가 +0.9%p를 차지한다. 성장이 둔화하는 5년 뒤에 지금보다 높은 배수를 받는다는 가정은 논리가 약하고, 약세 시나리오의 12배가 오히려 성장 둔화와 더 일관된다. 이 가정은 근거 인용 없이 모델러가 고른 값이다. [C:p_fcf] [C:exit_multiple@base] [C:exit_multiple@bear]
- 약한 가정 `base.fcf_margin`: FCF 마진 20%는 FY2025 18.8%보다 높고 한 번도 도달한 적이 없다. 마진은 9.0%에서 18.8%로 빠르게 올랐지만 개선이 계속된다는 근거는 감원 효과뿐이고, AV 파트너 확대에 따른 수수료율 변화와 소송 비용은 반대 방향이다. 최근 3개 분기의 OCF와 capex는 원문이 아니라 역산 근사치여서 마진 기준선 자체도 확인이 끝나지 않았다. 역DCF가 말하듯 기본 시나리오 가치는 이 마진에 크게 의존한다. [C:fcf_margin@FY2025] [C:fcf_margin@FY2023] [C:implied_cagr@m20] [F214] [F216]
- 약한 가정 `base.share_change`: 연 -1.5% 주식 수 감소는 FY2025 65.2억 달러, FY2026Q1 30.1억 달러 규모의 매입이 계속된다는 전제다. 같은 기간 현금은 줄고 부채는 늘었으므로 매입은 외부 조달이나 현금 소진 없이는 이어지기 어렵고, 현금 축적이 연 수익률 +5.0%p로 잡혀 있는 점도 매입 가정과 충돌한다. 둘이 동시에 성립하는지 모델은 보여 주지 않는다. [F4] [F6] [F23] [F43] [C:share_change@FY2025]

## 검증 (L6)

주장 71개 — supported 56 · unsupported 12 · contradicted 0 · leap 3 · 미검증 0

- [unsupported] 레드팀: FCF 마진 20%는 FY2025 18.8%보다 높고 한 번도 도달한 적이 없다. 마진은 9.0%에서 18.8%로 빠르게 올랐지만 개선이 계속된다는 근거는 감원  — 인용한 값은 FY2023 9.0%와 FY2025 18.8% 두 시점뿐이다. 20%에 한 번도 도달한 적이 없다는 말과 최근 분기 OCF·capex가 역산 근사치라는 말은 인용 자료에 없다.
- [unsupported] 경영진·자본배분: 희석 주식 수는 FY2023 20.9억, FY2024 21.5억(+2.8%)에서 FY2025 21.2억(-1.4%), FY2026Q2 20.5억으로 줄었다. SB — 희석 주식 수 증감과 SBC 비율, 분기 SBC는 일치한다. 그러나 매입이 희석을 상쇄하고도 남는다는 결론은 매입액을 인용하지 않아 받쳐지지 않고, 비율이 '꾸준히' 낮아졌다는 것도 양 끝값만으로는 알 수 없다.
- [unsupported] 애크먼: 슬레이터의 생존 경로와 현금 창출은 필요조건이다. 그러나 약세 시나리오 연 수익률 -0.3%는 '원금 훼손폭이 작다'는 뜻이지 가격이 싸다는 증명이 아니다. 단위 — 출처 없는 숫자 35.4% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 연 -1.5% 주식 수 감소는 FY2025 65.2억 달러, FY2026Q1 30.1억 달러 규모의 매입이 계속된다는 전제다. 같은 기간 현금은 줄고 부채는 늘었 — 현금이 줄고 부채가 늘었다고 하지만 인용한 것은 FY2026Q2 한 시점의 현금·부채뿐이라 비교할 수 없다. 현금 축적 +5.0%p 가정도 인용 자료에 없다.
- [unsupported] 앤더슨: 레드팀의 첫 부검인 자율주행 사업자가 수요 접점을 직접 쥐는 경우는 경로의 소음이 아니라 성장 가설 자체를 깬다. 이것이 이 판단에서 가장 무거운 위험이다. 반면 — 출처 없는 숫자 4.5% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 애크먼: 가격이 싸다. 기본 case의 주당 내재가치는 109.0, 주가는 70.3, 안전마진은 35.4%로 20% 문턱을 넘는다. 역DCF를 보면 FCF 마진 20%에서 — 출처 없는 숫자 35.4% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 회계 품질: 영업권이 FY2026Q2 94.7억 달러로 FY2026Q1 89.2억 달러보다 늘었다. 인수에 따른 증가로 보이며 총자산 대비 비중은 낮아 영업권 문턱과 거리가  — 영업권 89.2억에서 94.7억으로의 증가는 맞다. 그러나 총자산 대비 약 14%가 '낮고 문턱과 거리가 멀다'는 결론은 인용 자료에 문턱이 없어 따라 나오지 않는다.
- [unsupported] 사업·산업: 규모가 커지면서 마진이 올랐다. 연 매출 성장률 17~18%를 유지하며 영업이익률은 3.0%(FY2023)에서 10.7%(FY2025)로, FCF 마진은 9.0% — 출처 없는 숫자 6.5% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 모델러: 총예약액이 가이던스대로 18~22% 성장하고 FCF 마진이 18~20%대를 지키면, 시장 내재 성장(C:implied_cagr@m20)보다 훨씬 높은 성장이 이어 — TTM FCF 100억과 마진 상승은 맞다. 그러나 보수적 가이던스의 성격, 매입이 SBC 희석을 넘는다는 것, 파트너 구조가 수요 집합자 쪽이라는 결론은 인용 자료에서 따라 나오지 않는다.
- [unsupported] 회계 품질: 발생액 비율이 FY2025 -0.1%이고 FY2024 6.0%로 문턱을 넘지 않으며 DSO도 26.9일로 개선되었다. 영업현금흐름 101.0억 달러가 FY2025 — FY2025 발생액 비율, DSO, OCF와 영업이익은 맞다. 그러나 FY2024 6.0%와 '매출 성장과 큰 격차 없이' 움직였다는 말은 이전 분기 매출채권 등 비교 자료가 없어 인용 자료로 확인되지 않는다.
- [unsupported] 회계 품질: 공시 목록에서 8-K 4.02 재무제표 정정과 4.01 감사인 변경을 시사하는 항목은 없다(코드 신호도 없음). 감사의견·핵심감사사항·계속기업 의문 여부는 10- — 인용한 S11·S3에는 내용이 없고 공시 목록에 4.02·4.01 항목이 없다는 것을 확인할 자료도 제시되지 않았다.
- [leap] 사업·산업: 2026년 2분기 총예약액 대비 조정 EBITDA는 4.9%, 잉여현금흐름은 28억 달러다. 수익성은 총예약액 기준으로 개선 중이나 부문별(모빌리티·배달·화물)  — Q2 마진 4.9%와 FCF 28억은 맞다. 그러나 수익성이 '개선 중'이라는 결론은 인용한 분기 하나로 알 수 없다.
- [unsupported] 레드팀: 기본 시나리오는 출구 P/FCF 16배를 쓰는데 현재 배수는 14.27배다. 수익률 분해에서 멀티플 변화가 +0.9%p를 차지한다. 성장이 둔화하는 5년 뒤에 지 — 출처 없는 숫자 0.9% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 슬레이터: 레드팀의 가장 강한 지적은 기본 시나리오의 주식 수 감소와 현금 축적이 동시에 성립하는지 모델이 보여 주지 않는다는 것이다. 매입 기간에 현금은 줄고 부채는 늘었 — '매입 기간에 현금은 줄고 부채는 늘었다'는 말은 FY2026Q2 한 시점의 현금·부채만 인용해서는 확인되지 않는다. 매입액과 주식 수 감소율은 맞다.
- [unsupported] 사업·산업: 재투자 활주로는 넓지만 효율은 미확인이다. 설비투자는 매출의 약 0.7%(FY2025 3.4억)로 자본 집약도가 낮고, 현금의 대부분은 자사주 매입(FY2025  — 출처 없는 숫자 0.7% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| 매출 (revenue) | 174.6억 USD | 318.8억 USD | 372.8억 USD | 439.8억 USD | 520.2억 USD |
| 매출 성장 (revenue_growth) | — | 82.6% | 17.0% | 18.0% | 18.3% |
| 영업이익률 (operating_margin) | -22.0% | -5.7% | 3.0% | 6.4% | 10.7% |
| 순이익 (net_income) | -5.0억 USD | -91.4억 USD | 18.9억 USD | 98.6억 USD | 100.5억 USD |
| 영업현금흐름 (ocf) | -4.5억 USD | 6.4억 USD | 35.9억 USD | 71.4억 USD | 101.0억 USD |
| 설비투자 (capex) | 3.0억 USD | 2.5억 USD | 2.2억 USD | 2.4억 USD | 3.4억 USD |
| FCF (fcf) | -7.4억 USD | 3.9억 USD | 33.6억 USD | 69.0억 USD | 97.6억 USD |
| FCF 마진 (fcf_margin) | -4.3% | 1.2% | 9.0% | 15.7% | 18.8% |
| FCF/순이익 (fcf_conversion) | — | — | 1.78x | 0.70x | 0.97x |
| SBC (sbc) | 11.7억 USD | 17.9억 USD | 19.4억 USD | 18.0억 USD | 18.3억 USD |
| SBC/매출 (sbc_to_revenue) | 6.7% | 5.6% | 5.2% | 4.1% | 3.5% |
| SBC/영업현금흐름 (sbc_to_ocf) | — | 279.3% | 54.0% | 25.2% | 18.1% |
| SBC 차감 FCF (fcf_after_sbc) | -19.1억 USD | -14.0억 USD | 14.3억 USD | 51.0억 USD | 79.4억 USD |
| ROIC (roic) | -15.6% | -11.7% | 5.7% | 9.2% | 14.7% |
| 순현금 (net_cash) | -50.1억 USD | -49.8억 USD | -40.8억 USD | -25.2억 USD | -28.9억 USD |
| 순부채/EBITDA (net_debt_to_ebitda) | — | — | 2.11x | 0.72x | 0.46x |
| 희석 주식 수 (diluted_shares) | 19.0억 | 19.7억 | 20.9억 | 21.5억 | 21.2억 |
| 주식 수 변화 (share_change) | — | 4.2% | 5.9% | 2.8% | -1.4% |
| DSO(일) (dso) | 51.0 | 31.8 | 33.3 | 27.7 | 26.9 |
| 발생액 비율 (accruals_ratio) | — | -27.6% | -4.8% | 6.0% | -0.1% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, d_and_a, debt, debt_current, debt_total, ebitda, equity, goodwill, goodwill_to_assets, income_tax, interest_expense, operating_income, receivables, receivables_growth, rnd, short_term_investments, total_assets

### 시장 · TTM(FY2026Q2) 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 70.35 USD/share (2026-10-16, F197) |
| 희석 주식 수 (shares) | 20.5억 |
| 시가총액 (market_cap) | 1,442.3억 USD |
| 순현금 (net_cash) | -53.4억 USD |
| EV (ev) | 1,495.7억 USD |
| FCF 수익률 (fcf_yield) | 7.0% |
| P/FCF (p_fcf) | 14.27x |
| EV/매출 (ev_revenue) | 2.71x |
| PER (pe) | 15.06x |
| 순부채/EBITDA (net_debt_to_ebitda) | 0.72x |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 역DCF — 현재 가격이 가정하는 것

EV 1,495.7억 USD를 정당화하려면 매출이 10년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 목표 마진으로 직선 수렴, 할인율 10%, 이후 영구성장 3%.
기본 시나리오 목표 마진 20% 기준: 연 2.2% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 9.3% | C:implied_cagr@m10 |
| 15% | 5.1% | C:implied_cagr@m15 |
| 20% | 2.2% | C:implied_cagr@m20 |
| 25% | -0.1% | C:implied_cagr@m25 |
| 30% | -2.0% | C:implied_cagr@m30 |

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 25% | 663.1억 USD | 5.0% | 12% | 12x | 69.46 | 43.13 | -0.3% |
| 기본 | 50% | 841.1억 USD | 10.1% | 20% | 16x | 175.49 | 108.97 | +20.1% |
| 강세 | 25% | 949.7억 USD | 12.8% | 24% | 20x | 288.97 | 179.43 | +32.7% |

확률 가중: 주당 가치 177.35 · IV 110.12 · 기대 연 수익률 +20.3% (C:expected_irr) · 손실 확률 25% (C:p_loss) · 현재 주가 70.35

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +9.6% · 마진 변화 +1.3% · 멀티플 변화 +0.9% · 주식 수 변화 +1.5% · 현금 축적 +5.0% = +18.3%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | +9.5% | +14.4% | +18.6% |
| +0%p | +14.8% | +20.1% | +24.6% |
| +5%p | +20.1% | +25.7% | +30.5% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 585.2억 USD | 19.0% | 111.3억 USD | 20.2억 | 57.9억 USD |
| FY2027 | 649.6억 USD | 19.3% | 125.1억 USD | 19.9억 | 183.0억 USD |
| FY2028 | 714.5억 USD | 19.5% | 139.4억 USD | 19.6억 | 322.4억 USD |
| FY2029 | 778.8억 USD | 19.8% | 153.8억 USD | 19.3억 | 476.3억 USD |
| FY2030 | 841.1억 USD | 20.0% | 168.2억 USD | 19.0억 | 644.5억 USD |

### 컨센서스 대비 (C:consensus_diff@지표@기간)

| 지표 | 기간 | 컨센서스 | 기본 시나리오 | 차이 |
|---|---|---|---|---|
| revenue | FY2026 | 582.8억 USD | 585.2억 USD | +0.4% |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 2.2% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 10.1% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 12.8% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=8.53x, revenue_5y=1.83x
- 슬레이터 case={"from": "base", "exit_multiple": 14}: cash_survives=예, cash_min=53.9억 USD
- 애크먼 case={"from": "base", "fcf_margin": 0.17, "exit_multiple": 14}: price=70.3, fcf_positive=예, net_debt_to_ebitda=0.72x, leveraged=아니오, intrinsic_value=84.2, mos=16.5%

### 계산 경고

- 모델이 컨센서스와 사실상 같다 — variant perception이 없다면 알파도 없다
- 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-09-15 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1543151/000155278126000486/e26383_uber-8k.htm) |  |
| S2 | filing | 2026-08-07 | [8-K 중요 계약](https://www.sec.gov/Archives/edgar/data/1543151/000155278126000414/e26328_uber-8k.htm) |  |
| S3 | filing | 2026-08-05 | [10-Q](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000032/uber-20260630.htm) |  |
| S4 | filing | 2026-08-05 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000027/uber-20260805.htm) |  |
| S5 | filing | 2026-07-16 | [8-K 중요 계약 IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1543151/000155278126000382/e26302_uber-8k.htm) |  |
| S6 | filing | 2026-05-11 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1543151/000155278126000320/e26247_uber-8k.htm) |  |
| S7 | filing | 2026-05-08 | [8-K](https://www.sec.gov/Archives/edgar/data/1543151/000155278126000314/e26243_uber-8k.htm) |  |
| S8 | filing | 2026-05-06 | [10-Q](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000022/uber-20260331.htm) |  |
| S9 | filing | 2026-05-06 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000019/uber-20260506.htm) |  |
| S10 | filing | 2026-03-23 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1543151/000130817926000125/uber014597-def14a.htm) |  |
| S11 | filing | 2026-02-13 | [10-K](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm) |  |
| S12 | filing | 2026-02-09 | [8-K IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1543151/000155278126000043/e26049_uber-8k.htm) |  |
| S13 | filing | 2026-02-04 | [8-K 실적 발표 경영진 변동](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000011/uber-20260130.htm) |  |
| S14 | filing | 2026-01-12 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000005/uber-20260112.htm) |  |
| S15 | filing | 2025-11-04 | [10-Q](https://www.sec.gov/Archives/edgar/data/1543151/000154315125000033/uber-20250930.htm) |  |
| S16 | filing | 2025-11-04 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1543151/000154315125000030/uber-20251104.htm) |  |
| S17 | filing | 2025-02-14 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/0001543151-25-000008-index.htm) |  |
| S18 | filing | 2024-02-15 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1543151/000154315124000012/0001543151-24-000012-index.htm) |  |
| S19 | filing | 2023-02-21 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1543151/000154315123000010/0001543151-23-000010-index.htm) |  |
| S20 | filing | 2025-05-07 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1543151/000154315125000015/0001543151-25-000015-index.htm) |  |
| S21 | filing | 2025-08-06 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1543151/000154315125000023/0001543151-25-000023-index.htm) |  |
| S22 | news | 2026-08-17 | [Uber Technologies, Inc. - Uber and Zipline Partner to Bring Drone Delivery to Millions of Americans - Uber Investor Relations](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQclNPVTE0M0xWUGpKVlMwT2VXLU9SaVBKbjdDOWRtTjhBelVBYnBwSzUzemlXVHBuQ3IybU1aQWZuZUZBZ2FJZEV4bFFkSGN0c0o0cE1tZ2MteUMxRU91RW03LVFKaE9faTBQaW54TWFtdFJ4WEcxQlcxaDFiSl8taWRwWEJyX1B2X25DakI1SmRFU1ZSdjh1NVBHOTMtckJzX183R181bUtQdDI1VkZSQmc2OWctMVZCcnJkWDNsaHFiMlVLX3JEZVVfX3VXenVia3FZZ1ZaV2RoVWQ2dl9uZGxhcjhZcjlFcUozSQ?oc=5) | Uber Investor Relations |
| S23 | news | 2026-09-21 | [Why Is Uber Technologies (UBER) Back In Focus After Its $15 Billion Deal Progress? - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxQbHdacFdoNE4zSjFiWDgwYTY0QWFaS2FnWkNOSFJDN3VocWxZcmV1STIzVmRTR2RteE9QRVl0LTFpeFd5OGQ0MGhpSzhBWWQwZE0zUmZFbUVXQ0x5MFItcHlPWjdDNzBaaVl5SGFtczF3UW5nbWZ5dlRpQWxEZDFzRzNlR3hqRm1DNGh2b2JrRXZGTW9wOTVjODhGNmg?oc=5) | Yahoo Finance |
| S24 | news | 2026-09-02 | [Uber to cut 3,300 corporate jobs in management overhaul - The Guardian](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) | The Guardian |
| S25 | news | 2026-09-03 | [Uber to lay off 10% of staff in biggest cuts since COVID - Reuters](https://news.google.com/rss/articles/CBMirgFBVV95cUxQelprYTZqU1R2cFNKc2lqX0NZdGFxR0tyVjI0OGRUNFJHSHJJSkkzWmlfNGY0cXc2ZmpZaUc2X3RHZ3h5eEx1U2xZdkRBOHJQZnpRMVJYckhhUUVqZVd0Q3FWczl0dVNycmxiUGxuT3lqcWZVdkpLeW1jaG5rV0lNeTU0RzVYNVZKQTNRLWxXbE9CMkplR2xQaTlzZEJOaUU0MVMyanZZaUIwY0o3OHc?oc=5) | Reuters |
| S26 | news | 2026-09-06 | [Nigeria’s Antitrust Agency Probes Uber’s Exit From Country - Bloomberg.com](https://news.google.com/rss/articles/CBMirgFBVV95cUxNZjJweERweGlzcGVEZV9nRWNmaGdXSFpwXzhsZ2luOV9XMThzTFFqWEgxRXZXLXFUekhkMjJZbTB5R3J0enBNQnBtMGRoRDZHTnozQ2dIVFFEUUZmdktwMHlvenNZbXJBSWZfOXpteG1EeWNGUEhYaXZMSGNIZW4wZk1iR1c1clhpdUlHWFNzZlA4aVp4VnJNZklpYWhiU0Z3c3pGcWdFT2JSd09Yb3c?oc=5) | Bloomberg.com |
| S27 | news | 2026-09-02 | [Building a simpler, faster Uber - Uber](https://news.google.com/rss/articles/CBMiZEFVX3lxTE85bEp6SC12Ukx6bDZRb2hQU2FsbmhreFpnSVBIcHNjb0JIQ2YteWdLdkVndUYwRi1vc01waS1GRDJwUHlGTENQVG1Ec2FLUlplRWM0SF93V29GYXZ6TmFoWGlZRFI?oc=5) | Uber |
| S28 | news | 2026-10-10 | [Uber Technologies (UBER): Strong Operational Growth Offset by Soft Guidance - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOaHFhOVU5ZFA0dE1IV3FFOXhhaHRJOVRYeWRORnpqcFc0XzVXZTVrZE5CNlFoR2xxVW1XcWR5dW8wVUUza3lYYS13S0o1emlFTjlQU3BoYm0tX3V2eklrOHRaY3UxZDg3cUxuRURzOEgtb05XSkgzUWRtQkNxMzVZTGlJd3lhYVl4THk4SGxFMkxHRUlTcENlUWhsVldibzcySldqNFlvd25odw?oc=5) | Yahoo Finance |
| S29 | news | 2026-09-03 | [Uber to exit Nigeria after 12 years of operations - Reuters](https://news.google.com/rss/articles/CBMilwFBVV95cUxPS2hNV0dUbTNrV3hwMU9FVDNxSF9vaWE5dHlWeW9PeldOb2R4RkRMTXc3NENOTXhHc19FZ1JxOE1sZXh0MVp0Q1FKdUY5Nm5qa245THJrSjhIQ1YtcXNyRURhRHRjbzNOaVNfQ3lBU291NkpJdmlLb0ZmdDZMOURHajZVNDZqMFRvWjhGbDR5YXNuSW14aWIw?oc=5) | Reuters |
| S30 | news | 2026-08-20 | [Uber Launches Baidu’s Fully Driverless Apollo Go in Dubai, Establishing the First Multi-Partner Autonomous Network Globally - Uber Investor Relations](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) | Uber Investor Relations |
| S32 | news | 2026-09-03 | [Uber Technologies, Inc. - Wayve and Uber Launch First-Ever Autonomous Rides in the UK - Uber Investor Relations](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) | Uber Investor Relations |
| S33 | news | 2026-09-01 | [Uber Technologies Stock: Is UBER Underperforming the Technology Sector? - Yahoo Finance](https://news.google.com/rss/articles/CBMirgFBVV95cUxOWDZCczhSY0JESzVrVTFCc2hpM1dCM0hwR0pLZi03TVAxa0FJNXl2SDZ2NHh4Q29ZeFhVY1Frd2dvNUhTYlRxeGtCbHI5aDFWaW5ZQlpzdEhtV2pQNzRkNVF1SE5jMlpYLWNwUmhhODcwcTBuV3pJN1dfakhzZUplOXFKMnRwZEN0VDJUR3hGVV9ibzRLYmJQQzA5ZkF1UUdBTjFuOW9TbmxFdUhRTUE?oc=5) | Yahoo Finance |
| S34 | news | 2026-09-18 | [Uber Technologies (UBER), Why Is It Back In The Spotlight? - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxOVWo4SE53b09wX1ZENWNfd1NKd2dsLVF6ZVBSdGxnTmFZeHlDTUd3Z2FVOWF0VHhIeG8yWmtwdllnWE84bnk2aUFua2tKSFJYcW96SmdQcDlkeHRrUHRsRmF2d0RScEkwZkZndTJrMzBIdE4yemhlUjB4MGdaX25WSnkwNVRaaEM0YlpXMk5EZ2NQRE5OSFo4dmdwUGk?oc=5) | Yahoo Finance |
| S35 | news | 2026-10-09 | [Uber Technologies (UBER) Climbed, What Is Behind The Latest Attention? - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxPeXlJeWR6UG9mV3FYRkdvX09mMkx0WlRkbEFTVE5DMkhmUk9aaUtFTV9PMTkzQWxBUmk5OWNSVDIzSVl0cFlaWm9PejlITDdwaWpEVWlZZE80YlJseWQtWklMX1ItTUlwaUUtTTFLOFdLZ1d5QXBQVWx6S1FPb01ITk9SOFZab2pTVmg1RzM0NWdpaF9POGhnanYweFRUSDZZRk9WWg?oc=5) | Yahoo Finance |
| S36 | news | 2026-09-14 | [Is Most-Watched Stock Uber Technologies, Inc. (UBER) Worth Betting on Now? - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxPbk9LMGg1U1VzNTdpRmtTdDRjVThzU3kwZHcwN1JfbjdXcXdza3gwdlgzVFZRczg4VjJZNFUzWW9UY1lpTW9lNmp2bzhna1dCdU9Fcjd6RmhVZ1ZJVlVORjRRa0U1Y3NVSTlzVnRfejNmQ2ZINHJpNmhsMXg5QmxGNGd1N25TcDVpU0xrcUNzR3FJS0NsaEZrSlRiekpucmFySzlj?oc=5) | Yahoo Finance |
| S37 | news | 2026-09-24 | [Beyond Rides: How Uber Technologies (UBER) Is Building a Global Delivery and AV Powerhouse? - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxNWXdxWlBSU0tMMnp3LWgzTkFUZHJIWC0xcVpVSFVHSnZCcnlNenlQS0pib2RBZXVaUDVBZzZCZ2FpVm8zOEVpeENEeHdoOGxFLWlULURSU0QyWVJtUDhwbnBfWW5QZy13TGJjOGpSTjBpazVPX3FrNkU1NEZuVmxtOWdDU2ZJUmhyWWVtMFA3empfX0t5Rno0TWE5NWNmV0JoeVE?oc=5) | Yahoo Finance |
| S38 | news | 2026-09-30 | [The Bull Case For Uber Technologies (UBER) Could Change Following Nationwide Costco Delivery Expansion Via Uber Eats - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxQamNCcUc3Tzg5Tk1NUXZmRW4zc0RsVTZxZ1VIbV94Ykh5STItcjVYVFFTUUdxMGJfOGxab0d6bVpZMUlCRV9GdTRBOHRPSUFHVnNiWW1fOXdzWmphd3dqZXdycC0zcG4wcV9qQk15ZTgyYjhjN09aeXFDMEFFQzkyc0VyVk4yUHhjdFVYOEp5X2ZUMzFBMXVCY0xlb3RMZw?oc=5) | Yahoo Finance |
| S39 | news | 2026-09-24 | [What Does Uber Technologies (UBER) Winning Spain's First Robotaxi Permit Mean? - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5) | Yahoo Finance |
| S40 | news | 2026-10-07 | [Uber Technologies (UBER) Settles Third Bellwether Sexual Assault Lawsuit - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5) | Yahoo Finance |
| S41 | news | 2026-09-09 | [Why Uber Technologies (UBER) Dipped More Than Broader Market Today - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxPWGtya2c3anp5REFPSXZ3LU1YaG5oWjFWM1NMSngzZ2MwQVIyZjM4VmREWnFMM1Z5UUZiQ3VKcjZsUHZkYjlZWl95dWpKUWU4Q3hQNlZ0cUVfVEpUaGVLNXNTZHVZMEdmdE94c3ltbEZ5R2xtMnd6aHAxbDJwakNaMlVGeXdnaTJBc0VvaU12b3F2XzVYVnBMd0NSbjZMMDA?oc=5) | Yahoo Finance |
| S42 | data | 2026-10-16 | [Uber Technologies (UBER) 일별 주가 이력 - StockAnalysis](https://stockanalysis.com/stocks/uber/history/) | 2026-10-16 종가 70.35달러. 직전 거래일 10-15 71.27, 10-14 69.29, 10-13 71.32. |
| S43 | filing | 2026-08-05 | [Uber Announces Results for Second Quarter 2026 (8-K 보도자료)](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) | 2분기 총예약액 580억 달러(전년비 24%, 환율 불변 22%), 조정 EBITDA 28.2억 달러(총예약액 대비 4.9%), 잉여현금흐름 28억 달러로 TTM 100억 달러 초과. 순이익 24억 달러에는 지분 재평가 이익 세전 16억 달러가 포함. 3분기 가이던스: 총예약액 582.5억~602.5억 달러(환율 불변 18~22% 성장, 환율 역풍 약 1%p), 조정 EBITDA 28.6억~29.6억 달러, Non-GAAP EPS 0.84~0.88달러. 2차 요약(Seeking Alpha·BusinessWire 등)으로 교차 확인. |
| S44 | data | 2026-10-18 | [Uber Technologies (UBER) Stock Forecast - TickFlow (애널리스트 컨센서스)](https://tickflow.io/stock/UBER/forecast) | 2026년 매출 평균 추정 582.8억 달러(39명, 범위 568.4억~608.4억). 2027년 분기별 평균 152.5억·162.6억·169.7억·180.3억 달러. 날짜가 불분명한 집계 사이트이고 Simply Wall St는 2026년 약 601억 달러(51명)로 더 높다. 컨센서스는 출처 간 편차가 있어 참고용. |
| S45 | news | 2026-08-05 | [Uber Q3 guidance misses estimates despite $58B Q2 bookings and record $10B free cash flow](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow) | 보도. 3분기 총예약액 가이던스 중간값(592.5억)이 컨센서스 593.3억 달러를 소폭 하회, Non-GAAP EPS 가이던스 0.84~0.88이 추정치 0.89 하회. |

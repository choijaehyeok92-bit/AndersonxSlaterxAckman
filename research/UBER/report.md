# Uber Technologies (UBER) 리서치 보고서 — 기준일 2026-10-18

**찬성 우세** — 찬성 2 · 반대 1 · 보류 0 · 확신 가중 점수 +0.27 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장이 반영한 것: 시장은 3분기 가이던스가 컨센서스를 소폭 밑돈 점과 자율주행의 수요 탈취 가능성을 반영해, 이익 대비 낮은 배수에 거래한다. 현재 가격이 요구하는 성장은 역DCF 값(C:implied_cagr)으로 확인한다. 컨센서스는 2026년 매출 평균을 보여주고 출처 간 편차가 있다.
- 우리가 다르게 보는 점: 우리 기본 시나리오의 매출 성장은 컨센서스와 크게 다르지 않아 성장 전망에서는 알파를 주장하지 않는다. 차이는 두 가지다. 첫째, 이익의 질이다. 순이익은 세금 환입과 지분 재평가 이익으로 부풀려져 PER이 왜곡되지만, 현금(FCF)은 이익을 뒷받침한다. 시장이 이를 PER로만 보면 현금창출력을 낮게 본다. 둘째, 가이던스가 보수적이었는지는 과거 이력이 없어 확정하지 못하지만, 이번 가이던스 미달 폭은 작다.
- 왜 우리가 맞는가: FY2025 FCF와 SBC 차감 FCF가 순이익과 비슷한 수준이고, 자본집약도가 낮으며 순부채 부담이 작다. 따라서 가치 평가는 PER이 아니라 FCF 기준이어야 한다. 반대로 AV 위협은 계약 조건과 투자 규모가 미확인이므로 약세 시나리오 확률 30%로 반영했다. [F198] [F199] [F201] [F202] [F205] [F207] [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [C:pe] [C:implied_cagr] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow) [S44](https://tickflow.io/stock/UBER/forecast)
- 촉매: 3분기 실적 발표에서 총예약액과 조정 EBITDA의 가이던스 대비 결과, FCF 지속성, AV 파트너 단위경제 공개.
- 시점: 2026년 11월 3분기 실적 발표 이후 4개 분기.
- 컨센서스 대비 revenue FY2026: +0.4% (585.2억 USD vs 582.8억 USD)

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **86.55** vs 주가 70.35 · 기대 연 수익률 **+14.7%** · 손실 확률 30%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 30% | 55.50 | 34.46 | -4.6% | 자율주행 업체가 수요를 직접 가져가거나 Uber에 수수료 인하를 요구해 플랫폼 수수료율이 내려간다. 규제·소송 비용(성범죄 소송, 나이지리아 같은 지역 철수)과 AV 투자 부담이 마진 개선을 되돌린다. 성장은 3분기 |
| 기본 | 50% | 146.75 | 91.12 | +15.8% | FY2026은 상반기 매출 흐름과 컨센서스 부근(연 환산 두 자릿수 초반 성장)에서 출발하고, 이후 성장은 총예약액 규모가 커지면서 완만하게 둔화한다. FCF 마진은 FY2025의 18.8%에서 소폭 올라 정착한다. |
| 강세 | 20% | 246.82 | 153.25 | +28.5% | Uber가 Baidu, Wayve, Zipline 등 여러 AV 파트너를 묶는 수요 집합자로 자리 잡는다. 이용 빈도와 구독·배달 교차 판매가 늘어 총예약액 성장이 최근 분기(전년비 24%)를 따라 유지된다. 이 경 |

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
- [충족 — 훼손] 레드팀: 3분기 총예약액이 가이던스 하단(582.5억 달러) 미달 — 성장이 가이던스 밖으로 꺾이기 시작 — `gross_bookings < 5.825e+10`
- [미충족] 레드팀: 분기 영업이익이 FY2026Q2 수준(18.9억 달러) 아래로 후퇴 — 일회성 비용이 경상 이익을 잠식 — `operating_income < 1.89e+09`
- [미충족] 레드팀: 현금이 FY2026Q2의 48.7억 달러 아래로 계속 감소 — 환원·투자가 현금창출을 앞지르는 중 — `cash < 4.87e+09`
- [충족 — 훼손] 레드팀: 3분기 조정 EBITDA가 가이던스 하단(28.6억 달러) 미달 — 마진 개선 가설 훼손 — `adjusted_ebitda < 2.86e+09`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | gross_bookings | FY2026Q3 | >= 5.925e+10 | 65% | 가이던스 중간값 달성 여부로 성장 둔화가 일시적인지 시험한다. |
| K2 | adjusted_ebitda | FY2026Q3 | >= 2.86e+09 | 85% | 가이던스 하단 이상이면 마진 개선 가설이 유지된다. 약세 시나리오는 이 선을 밑돈다. |
| K3 | revenue | FY2026Q3 | >= 1.5e+10 | 60% | 상반기 매출 성장률(전년비 12~15%)이 3분기에도 이어지는지 본다. |
| K4 | revenue | FY2026 | >= 5.828e+10 | 55% | 연간 매출이 컨센서스 평균에 도달하는지로 기본 시나리오의 첫 해 성장률을 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 +0.27 · 비중 참고값 10.0% (0.25 켈리 — 5년 초과수익 +37%(요구수익률 10% 차감), 분산 0.90, 상한 10%) · 슬레이터 시작 비중 2.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 0/5 실패 | founder_led=아니오, upside_10y=6.61x, revenue_5y=1.96x |
| 슬레이터 | 찬성 → 찬성 | 3/5 | ✓ | 0/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=2.0%, cash_survives=예, cash_min=53.9억 USD |
| 애크먼 | 찬성 → 반대 (레드라인 → 반대) | 2/5 | ✗ 잉여현금흐름을 만들지 못함 (코드 계산) | 0/5 실패 | simple_predictable=예, capital_markets_dependent=아니오, catalyst=FCF 재원의 자사주 매입 지속과 약 3,300명 감원을 통한 비용 구조 단순화. 3분기 실적(2026-11-04)에서 가이던스 하단 이상 달성 여부가 첫 시험, net_debt_to_ebitda=0.72x, intrinsic_value=91.1, mos=22.8% |

- ⚠ 앤더슨: 5년 매출 1.96배 < 2배 (LTGG Q1)
- ⚠ 앤더슨: risks[2] unsupported: 소송과 철수·조사는 뉴스 제목이 받치지만, '전문경영인 체제라 창업자의 장기 지평에 기대기 어렵다'는 사실은 인용에 없다.
- ⚠ 앤더슨: rebuttals[2]: 인용하지 않은 근거의 숫자 15%(C:expected_irr·C:receivables_growth@FY2025·C:roic@FY2025) — cites에 추가
- ⚠ 애크먼: rebuttals[2]: 인용하지 않은 근거의 숫자 19%(C:fcf_margin@FY2025·C:fcf_margin@base), 15(C:exit_multiple@base·C:pe·S23), 18.8%(C:fcf_margin@FY2025), 12%(C:fcf_margin@bear·C:roic@FY2022) — cites에 추가
- ⚠ 애크먼: rebuttals[0]: 인용하지 않은 근거의 숫자 22.8%(C:mos@ackman) — cites에 추가
- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 모델이 컨센서스와 사실상 같다 — variant perception이 없다면 알파도 없다
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 모델러 variant 검증 실패(unsupported): 없는 근거 인용: C:implied_cagr
- ⚠ 회계 품질 findings[3] 검증 실패(unsupported): 발생액 비율과 DSO 26.9일은 맞지만 '51.0일'이라는 이전 DSO는 인용에 없다.
- ⚠ 사업·산업 findings[0]: 인용하지 않은 근거의 숫자 12(S29) — cites에 추가
- ⚠ 레드팀 weakest[2] 검증 실패(unsupported): 출처 없는 숫자 5.3% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 회계 품질 findings[5] 검증 실패(unsupported): 없는 근거 인용: C:goodwill_to_assets
- ⚠ 경영진·자본배분 findings[3]: 인용하지 않은 근거의 숫자 1.83e+09(C:operating_income@FY2022·C:sbc@FY2025·F113) — cites에 추가
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base

## 앤더슨 — 찬성 (3/5)

> Uber는 승객·운전자, 소비자·가맹점, 화주·운송사를 잇는 거대한 양면 네트워크다. 이 네트워크가 자율주행 파트너를 묶는 수요 집합자가 되면 10년 뒤 크기는 지금의 DCF로 잴 수 없을 만큼 커질 수 있다. 상방 시나리오(case: bull)를 10년으로 늘리면 코드 계산 기준 주당 가치가 현재 주가의 6.61배다. 5배 기준(10번 질문)을 넘는 길이 보인다. 다만 이 길이 열릴 확률은 모델러 기준 20%에 그치고, 5년 뒤 매출 배수는 2배에 아주 조금 못 미쳐 1번 질문의 기준선에 걸쳐 있다. 창업자형 경영진도 아니다. 그래서 확신은 중간(3)으로 둔다. 손실은 막혀 있고 상승은 열려 있다. FCF가 자사주 매입까지 감당하므로 기다리는 동안의 비용도 낮다. 이 비대칭이 찬성의 이유다.

**논거**
- 수익 구조가 증명되었다. FCF 마진이 FY2021 -4.3%에서 FY2025 18.8%로 올랐다. 네트워크 규모가 커질수록 고정비 레버리지가 현금으로 이어진다는 뜻이다(7번 질문). 설비투자가 가벼워 성장에 자본이 크게 들지 않는다. [C:fcf_margin@FY2021] [C:fcf_margin@FY2025] [F11]
- 성장 모멘텀이 아직 살아 있다. 2분기 총예약액은 580.0억 달러로 전년비 24% 늘었다. 이 규모에서 이 속도라면 매출이 5년 안에 두 배에 가까워지는 길이 열려 있다(1번 질문). 3분기 가이던스는 소폭 낮지만 소음 수준이다. [F198] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F202]
- 자율주행은 위협이자 이 회사가 커질 가장 큰 기회다. Baidu(두바이), Wayve(영국), Zipline(드론 배달)과 제휴하고 스페인 로보택시 허가를 받았다. 공급자가 여럿으로 갈라질수록 수요를 쥔 집합자의 가치가 커진다. 이 가설은 아직 입증되지 않았다. 그러나 열 번 중 한 번의 대성공이 결과를 결정하는 비대칭 구조에서는 옵션 가치가 있다(5번 질문). [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S22](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQclNPVTE0M0xWUGpKVlMwT2VXLU9SaVBKbjdDOWRtTjhBelVBYnBwSzUzemlXVHBuQ3IybU1aQWZuZUZBZ2FJZEV4bFFkSGN0c0o0cE1tZ2MteUMxRU91RW03LVFKaE9faTBQaW54TWFtdFJ4WEcxQlcxaDFiSl8taWRwWEJyX1B2X25DakI1SmRFU1ZSdjh1NVBHOTMtckJzX183R181bUtQdDI1VkZSQmc2OWctMVZCcnJkWDNsaHFiMlVLX3JEZVVfX3VXenVia3FZZ1ZaV2RoVWQ2dl9uZGxhcjhZcjlFcUozSQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5)
- 상방 시나리오의 크기가 5배 기준을 넘는다. 코드가 계산한 앤더슨 case의 10년 뒤 주당 가치는 현재 주가 대비 6.61배다. 확률 가중 기대 연 수익률도 14.7%로, 시장이 이 기회를 과소평가한다는 가설(9번 질문)과 맞는다. [C:upside_10y@anderson] [C:expected_irr] [C:revenue_5y@anderson]
- 자본배분이 주주 편이다. FY2025 자사주 매입 65.2억 달러가 SBC를 넘어 희석 주식 수를 줄였다. 번 현금을 증식시키는 데 쓰고 있다(8번 질문). [F4] [F156] [C:share_change@FY2025]

**사전 부검**
- 사전 부검: AV 업체가 Uber를 건너뛰고 수요를 직접 가져가면 성장 가설 자체가 깨진다. 이는 경로의 소음이 아니라 가설의 훼손이다. 파트너십의 계약 조건과 투자 약정은 근거에 없어 이 위험을 지금 가를 수 없다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S37](https://news.google.com/rss/articles/CBMiogFBVV95cUxNWXdxWlBSU0tMMnp3LWgzTkFUZHJIWC0xcVpVSFVHSnZCcnlNenlQS0pib2RBZXVaUDVBZzZCZ2FpVm8zOEVpeENEeHdoOGxFLWlULURSU0QyWVJtUDhwbnBfWW5QZy13TGJjOGpSTjBpazVPX3FrNkU1NEZuVmxtOWdDU2ZJUmhyWWVtMFA3empfX0t5Rno0TWE5NWNmV0JoeVE?oc=5)
- 사전 부검: 상방 시나리오는 5년 매출이 기준 연도의 2배에 못 미치는 경로다(1번 질문의 기준선 미달). 최근 분기 성장률을 5년 동안 유지해야 하고, 3분기 가이던스는 성장이 둔화되는 방향이다. 상방이 아니라 기본 시나리오에 머물면 5배는 오지 않는다. [C:revenue_5y@anderson] [F202] [F205]
- 사전 부검: 성범죄 소송과 지역 철수·규제 조사는 이 사업의 구조적 비용이다. 충당금 규모가 미확보라 마진 상방 가정이 흔들릴 수 있다. 전문경영인 체제라 창업자의 장기 지평에 기대기도 어렵다. [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5) [S26](https://news.google.com/rss/articles/CBMirgFBVV95cUxNZjJweERweGlzcGVEZV9nRWNmaGdXSFpwXzhsZ2luOV9XMThzTFFqWEgxRXZXLXFUekhkMjJZbTB5R3J0enBNQnBtMGRoRDZHTnozQ2dIVFFEUUZmdktwMHlvenNZbXJBSWZfOXpteG1EeWNGUEhYaXZMSGNIZW4wZk1iR1c1clhpdUlHWFNzZlA4aVp4VnJNZklpYWhiU0Z3c3pGcWdFT2JSd09Yb3c?oc=5) [S29](https://news.google.com/rss/articles/CBMilwFBVV95cUxPS2hNV0dUbTNrV3hwMU9FVDNxSF9vaWE5dHlWeW9PeldOb2R4RkRMTXc3NENOTXhHc19FZ1JxOE1sZXh0MVp0Q1FKdUY5Nm5qa245THJrSjhIQ1YtcXNyRURhRHRjbzNOaVNfQ3lBU291NkpJdmlLb0ZmdDZMOURHajZVNDZqMFRvWjhGbDR5YXNuSW14aWIw?oc=5)

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 안전마진 22.8%가 기준 20%를 간신히 넘는다는 점과, 컨센서스와 같은 모델이라 초과 수익의 근거가 없다는 점이다. 그러나 기본 시나리오는 5년짜리 DCF라서 10년 뒤 크기를 재지 못한다. 안전마진이 얇다고 말하는 것은 현재를 정밀하게 재는 것이다. 내 판단은 상방 경로에서 10년 뒤 주당 가치가 주가의 5배를 넘느냐에 달려 있고, 코드가 계산한 값은 6.61배다. 기본 시나리오의 기대 연 수익률도 확률 가중으로 14.7%이므로, 얇은 안전마진은 반대 근거가 아니라 크게 담지 말라는 근거로 받아들인다. [C:mos@ackman] [C:upside_10y@anderson] [C:expected_irr]
- → 슬레이터: 슬레이터의 가장 강한 논거는 고객 단위 경제성(CAC, 이탈률, 순매출유지율)에 증거가 없어 '입증'이 아니라 '계획'이라는 점이다. 맞다. 다만 악화의 증거도 없다. 영업이익률이 FY2023 3.0%에서 FY2025 10.7%로, ROIC가 5.7%에서 14.7%로 오른 것은 단위경제가 나빠지는 회사에서는 나타나지 않는다. 증거가 쌓이길 기다리다 가장 가치 있는 구간을 놓치는 것이 더 큰 실수다. 작게 시작하자는 슬레이터의 제안은 받아들이되, 그 이유는 불명확성이 아니라 20%뿐인 상방 확률이다. [C:operating_margin@FY2023] [C:operating_margin@FY2025] [C:roic@FY2023] [C:roic@FY2025] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- → 레드팀: 레드팀의 가장 강한 부검은 자율주행 업체가 수요를 직접 가져가 Uber가 수수료를 깎아 주는 하위 채널이 되는 경로다. 이것은 경로의 소음이 아니라 성장 가설 자체를 깨는 시나리오라는 점을 인정한다. 그래도 레드팀이 매긴 확률은 15%다. 현재 Baidu, Wayve와의 제휴와 스페인 로보택시 허가는 Uber가 공급자를 여럿 묶는 집합자 위치에 있음을 보여 준다. 공급자가 여럿으로 갈라질수록 수요를 쥔 쪽의 가치가 커진다. 계약 조건을 모르는 만큼 반증 조건에 총예약액 가이던스 하단과 수동 점검을 넣었고, 첫 신호는 3분기 총예약액에서 확인된다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5) [F202]

**인정한 점**
- 애크먼이 짚은 대로 안전마진 22.8%는 기준을 겨우 넘고 모델이 컨센서스와 같아 성장 전망에서 알파를 주장할 수 없다. 내 찬성은 시장이 틀렸다는 확신이 아니라 상방 비대칭에 기댄 것이므로 확신을 3 이상으로 올리지 않는다.
- 슬레이터의 지적대로 고객 단위 경제성은 근거가 없다. 비중은 작게 시작하는 것이 맞다.
- 레드팀이 지적한 대로 기본 시나리오의 FCF 마진 19%와 출구 배수 15배는 소송 충당금과 AV 투자를 거의 반영하지 않은 낙관적 가정이다. 상방 가치 6.61배도 이 가정이 흔들리면 줄어든다.
- 상방 시나리오의 5년 뒤 매출이 기준 연도의 2배에 조금 못 미쳐 1번 질문의 기준선에 걸쳐 있다. 이를 숨기지 않는다.


## 슬레이터 — 찬성 (3/5)

> Uber는 외부 자본 없이 계획을 실행할 수 있는 회사다. 사업 규모도 이미 증명돼 있다. 연매출은 FY2023 372.8억 달러에서 FY2025 520.2억 달러로 늘었고, FCF 마진은 18.8%다. 코드가 계산한 기본 시나리오의 현금 경로도 0 아래로 내려가지 않는다. 다만 이 판단은 회사 전체 합계에 기대고 있다. 고객·부문 단위경제(CAC, 이탈률, 순매출유지율, 부문별 마진)와 자율주행 제휴의 계약 조건은 근거에 없다. 그래서 단위경제는 '악화'가 아니라 '불명'으로 두고, 시작 비중을 작게 제안한다. 기본 시나리오가 성립하려면 총예약액 성장이 가이던스 범위를 지키고, 조정 EBITDA 마진이 유지되며, 주식 수가 늘지 않아야 한다. 이 셋은 모두 다음 분기부터 사실로 대조할 수 있다. 증거가 쌓이면 비중을 키우고, 깨지면 손익과 무관하게 정리한다.

**논거**
- 시장의 크기와 지속성은 이미 실적으로 보인다. 매출이 FY2023 372.8억 달러에서 FY2025 520.2억 달러로 늘었고, 2분기 총예약액은 580.0억 달러로 전년비 24% 늘었다. 천장이 보이는 성장이라는 증거는 없다. [F134] [F136] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- 생존은 자체 현금으로 해결된다. FY2025 FCF는 97.6억 달러, FCF 마진은 18.8%다. 2022년의 교훈이었던 외부 조달 의존이 없고, 코드가 계산한 기본 시나리오 현금 경로도 0 아래로 내려가지 않는다. [C:fcf@FY2025] [C:fcf_margin@FY2025] [F201]
- 확률 가중 기대 연 수익률은 +14.7%지만 손실 확률이 30%다. 높은 확신으로 키울 구간이 아니라 증거가 쌓일 때마다 늘릴 구간이다. 시작 비중을 작게 잡는 근거다. [C:expected_irr] [C:p_loss]
- 고객 단위 경제성은 증거가 없다. CAC, 이탈률, 순매출유지율, 부문별 마진을 확보하지 못했다. 악화의 증거도 없으므로 레드라인에 걸리지는 않지만, '입증'이라고 쓸 수도 없다. 아직 계획인 것과 실적인 것을 가르면 이 부분은 계획이다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- 자율주행 제휴(Baidu, Wayve, Zipline)와 스페인 로보택시 허가는 선택지를 넓히지만 계약 조건과 투자 약정 규모를 알 수 없다. 이 선택지는 상방으로 계산하지 않고, 약세 시나리오의 위협으로만 반영한다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S22](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQclNPVTE0M0xWUGpKVlMwT2VXLU9SaVBKbjdDOWRtTjhBelVBYnBwSzUzemlXVHBuQ3IybU1aQWZuZUZBZ2FJZEV4bFFkSGN0c0o0cE1tZ2MteUMxRU91RW03LVFKaE9faTBQaW54TWFtdFJ4WEcxQlcxaDFiSl8taWRwWEJyX1B2X25DakI1SmRFU1ZSdjh1NVBHOTMtckJzX183R181bUtQdDI1VkZSQmc2OWctMVZCcnJkWDNsaHFiMlVLX3JEZVVfX3VXenVia3FZZ1ZaV2RoVWQ2dl9uZGxhcjhZcjlFcUozSQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5)

**사전 부검**
- 사전 부검: 자율주행 업체가 수요를 직접 가져가거나 수수료 인하를 요구하면, 플랫폼 수수료율이 내려가 마진 개선이 되돌려진다. 선행 신호는 조정 EBITDA 마진 하락이다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [F200]
- 사전 부검: 3분기 가이던스의 환율 불변 성장률 하단이 2분기보다 낮고 중간값이 컨센서스를 소폭 밑돈다. 성장 둔화가 일시적이 아니라 구조적이었다면, 기본 시나리오의 성장 경로가 틀린 것이다. [F202] [F205] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow)
- 사전 부검: 2분기 순이익에는 세전 16억 달러의 지분 재평가 이익이 들어 있다. 소송 충당금과 구조조정 비용 규모도 미확보다. 이를 본업 수익력으로 오해하면 현금 창출력을 과대평가한다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F104] [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5) [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5)

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 상방 시나리오의 10년 뒤 주당 가치가 현재 주가의 몇 배라는 계산이다. 상방에 동의한다. 하지만 그 길이 성립하려면 총예약액 성장이 최근 분기 수준으로 오래 유지되어야 한다. 그런데 3분기 가이던스의 환율 불변 성장률은 2분기보다 낮다. 그 길은 아직 계획이고 실적이 아니다. 나는 그 상방을 비중 확대의 근거로 쓰지 않는다. 가이던스 하단 이상의 총예약액과 조정 EBITDA 같은 분기 실적이 쌓일 때만 비중을 키운다. 그 전까지 시작 비중은 작게 둔다. [C:upside_10y@anderson] [C:revenue_5y@anderson] [F202] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- → 애크먼: 애크먼의 가장 강한 논거는 현금 창출과 낮은 레버리지 덕에 자본시장에 기대지 않는다는 점이다. 생존 측면에서는 나도 동의하고, 기본 시나리오의 현금 경로가 0 아래로 내려가지 않는다는 코드 계산도 같은 결론이다. 다만 안전마진이 기준을 간신히 넘는 수준이라 가격만으로는 확신을 키울 수 없다. 그 마진은 기본 시나리오의 마진과 출구 배수 가정에 달려 있다. 내가 의존하는 것은 가격 여유가 아니라 분기마다 대조되는 운영 지표다. 그래서 확신은 3에 머문다. [C:mos@ackman] [C:cash_min@slater] [F201]
- → 레드팀: 레드팀의 가장 강한 논거는 부채가 늘어난 상태에서 자사주를 사면서 현금이 줄었다는 점이다. 현금은 이전 연말보다 줄었고 부채는 늘었다. 이 지적은 옳아서 내 필수 조건에 반영한다. 모델은 FCF를 전부 순현금에 쌓는다고 가정하므로 실제 환원 정책과 다르다. 다만 분기 FCF가 환원과 감원 비용을 감당하는지는 분기 사실로 확인할 수 있다. 그래서 희석 주식 수 조건을 유지하고, 영업이익이 최근 분기 아래로 후퇴하지 않는다는 조건을 더한다. 현금 감소가 이어지는데 영업이익까지 후퇴하면 가설이 깨진 것으로 보고 정리한다. [F21] [F23] [F37] [F43] [F6] [F201] [F121]

**참이어야 하는 것**
- [on_track] 조정 EBITDA 마진(총예약액 대비)이 4.5% 이상으로 유지된다
- [on_track] 3분기 총예약액이 가이던스 하단 이상이다
- [on_track] 3분기 조정 EBITDA가 가이던스 하단 이상이다
- [on_track] 희석 주식 수가 늘지 않는다(자사주 매입이 SBC 희석을 넘는다)
- [on_track] 3분기 영업이익이 FY2026Q2 수준 아래로 후퇴하지 않는다

**인정한 점**
- 레드팀이 짚은 대로 모델의 현금 축적 경로는 실제 환원과 다르다. 현금 창출이 조금만 흔들려도 완충이 얇아질 수 있으므로, 영업이익 하한 조건을 필수 조건에 추가한다.
- 앤더슨의 상방은 크지만 입증되지 않았다. 이 상방을 시작 비중 산정에는 넣지 않는다. 또 애크먼의 안전마진 22.8%는 여유가 작아 확신을 올릴 근거가 못 된다.


## 애크먼 — 반대 (2/5)

> Uber는 이용자와 공급자를 잇고 거래액에서 수수료를 떼는 마켓플레이스라서 한 문단으로 설명된다. 현금도 실제로 번다. FY2025 FCF 마진은 18.8%이고 순부채/EBITDA는 낮아 자본시장에 기대지 않아도 된다. 기본 시나리오 기준 안전마진은 22.8%로 하네스 기준(20%)을 간신히 넘는다. 여유가 크지 않아 확신은 3에 그친다. 해자는 아직 '주장' 수준이다. 점유율과 이탈률 근거가 없고, 자율주행이 수요를 직접 가져갈 가능성은 10년 FCF 범위를 넓힌다. 그래서 크게 담을 종목은 아니고 가격이 허락하는 만큼만 담는다. 촉매는 FCF를 재원으로 한 자사주 매입과 감원을 통한 비용 구조 단순화다.

**논거**
- 현금 창출력이 이익으로 뒷받침된다. FY2025 FCF 마진은 18.8%이고 SBC를 차감한 FCF도 79.4억 달러다. 설비투자가 작은 자산 경량 구조라서 FCF를 평가의 기준으로 삼을 수 있다. [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [F11]
- 재무가 단단해 자금줄이 끊겨도 버틴다. 순부채/EBITDA는 TTM 기준 0.72x이고 레버리지 판정도 '아니오'다. 밸리언트식 자본시장 의존과는 거리가 멀다. [C:net_debt_to_ebitda] [C:net_debt_to_ebitda@FY2025]
- 가격이 기본 시나리오 내재가치 아래에 있다. 기본 시나리오 현재가치는 주당 91.1달러, 주가는 70.3달러이고 안전마진은 22.8%다. 기준(20%)을 넘지만 여유는 작다. [F197] [C:iv@base] [C:mos@ackman]
- 자본배분이 주주 친화적이다. FY2025 자사주 매입은 65.2억 달러로 SBC를 크게 넘어 희석 주식 수를 -1.4% 줄였다. 격차를 좁힐 촉매가 이미 작동 중이다. [F4] [F156] [C:share_change@FY2025]
- 운영 레버리지가 숫자로 확인된다. 영업이익률은 FY2023 3.0%에서 FY2025 10.7%로, ROIC는 5.7%에서 14.7%로 올랐다. 규모의 경제는 입증됐지만 경쟁사 대비 해자까지는 입증되지 않았다. [C:operating_margin@FY2023] [C:operating_margin@FY2025] [C:roic@FY2023] [C:roic@FY2025]

**사전 부검**
- 사전 부검: 자율주행 파트너가 수요를 직접 가져가거나 수수료 인하를 요구하면 플랫폼 수수료율이 무너진다. 약세 시나리오 연 수익률은 -4.6%이고 손실 확률은 30%다. 이 경우 현재가는 안전마진이 아니라 고평가가 된다. 파트너십 계약 조건은 확인되지 않았다. [C:irr@bear] [C:p_loss] [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5)
- 사전 부검: 이익 품질이 PER에 나타난 것보다 나쁘다. 2분기 순이익에는 세전 16억 달러의 지분 재평가 이익이 포함돼 있다. 법인세 환입도 순이익을 키웠다. FCF 기준으로 보더라도 소송 충당금과 구조조정 비용이 확인되지 않은 상태다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F85] [F86] [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5)
- 사전 부검: 성장 둔화가 일시적이지 않을 수 있다. 3분기 총예약액 가이던스 중간값이 컨센서스를 소폭 하회했다. 컨센서스와 사실상 같은 모델이므로 가격이 이미 이 성장을 반영하고 있다면 초과 수익의 근거가 없다. [F202] [F205] [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow)

**반론**
- → 앤더슨: 앤더슨의 6.61배는 강세 시나리오(확률 20%)를 10년으로 늘린 값이다. 생존자 편향에 기댄 숫자다. 이 길은 5년 매출이 2배에 못 미치는 경로이기도 하다. 확률 가중 기대 연 수익률은 14.7%이고 손실 확률은 30%다. 내 판단은 기본 시나리오의 안전마진 22.8%에서 나온 것이지 꼬리 상방에서 나온 것이 아니다. [C:upside_10y@anderson] [C:revenue_5y@anderson] [C:expected_irr] [C:p_loss]
- → 슬레이터: 슬레이터의 생존 경로와 현금 경로는 필요조건이다. 현금이 0 아래로 내려가지 않는다는 사실이 현재 가격의 정당화는 아니다. 단위경제가 '불명'인 상태에서 기본 시나리오가 요구하는 19% FCF 마진이 사상 최고 구간이라는 점이 가격 판단의 핵심 약점이다. 시작 비중을 작게 잡는다는 결론에는 동의한다. [C:fcf_margin@FY2025] [C:cash_min@slater] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- → 레드팀: 레드팀이 지적한 약점은 base FCF 마진 19%와 출구 배수 15배다. 마진을 FY2025 수준 18.8%에서 12%(약세)쪽으로 흔들면 안전마진이 20% 기준 아래로 내려간다. 기본 시나리오의 안전마진 22.8%는 이 가정들에 거의 여유가 없다. 따라서 이 종목은 크게 담을 이유가 없고, 3분기 총예약액과 조정 EBITDA가 가이던스 하단을 지키는지 확인하는 증거가 쌓일 때까지 확신을 낮춘다. [C:mos@ackman] [C:iv@base] [F202] [F203]

**인정한 점**
- 레드팀의 지적을 인정한다. 기본 시나리오의 FCF 마진 19%와 출구 배수 15배에는 소송 충당금, 감원 비용, AV 수수료 압박이 반영돼 있지 않다. 안전마진 22.8%는 기준 20%를 넘지만 여유가 작아 확신을 3에서 2로 낮춘다.
- 슬레이터가 옳은 부분: 해자는 '주장' 수준이고 단위경제는 불명이다. 그래서 비중은 작아야 하고, 찬성은 가격이 허락하는 최소한이다.
- 레드팀이 인용한 모델의 순현금 경로는 실제 환원 정책(부채로 자사주 매입)과 다르다. 현금 축적 기여(+5.3%)가 과대 평가됐을 수 있어 내재가치 91.1달러를 그대로 믿지 않는다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Uber은 승객과 운전자(모빌리티), 소비자와 가맹점·배달원(배달), 화주와 운송사(화물)를 연결하는 양면 마켓플레이스다. 거래액(총예약액)에서 수수료를 떼어 수익을 낸다. 2026년 2분기 총예약액은 580.0억 달러(전년비 24%)이고 조정 EBITDA는 28.2억 달러(총예약액 대비 4.9%)다(S43). FY2021 영업이익률 -22.0%에서 FY2025 10.7%로 올랐고, FCF 마진은 18.8%다(C:operating_margin@FY2025, C:fcf_margin@FY2025). 규모의 레버리지는 숫자로 보이지만, 고객 1명 단위의 경제성(CAC·이탈률·순매출유지율)과 부문별 마진은 이번 근거에 없다. 그래서 단위경제는 '확인 불가'로 둔다. 자율주행(AV) 파트너십은 선택지를 넓혀 주는 동시에 장기 위협이다. 지금은 계약 조건과 투자 규모를 알 수 없다.

- [unit_economics] 수익성이 빠르게 개선됐다. FY2025 FCF는 97.6억 달러, FCF 마진은 18.8%다. SBC를 차감한 FCF도 79.4억 달러다. 2분기 FCF는 28억 달러였고, 최근 12개월 FCF는 100억 달러를 넘었다고 회사가 밝혔다. 자본집약도는 낮아서 FY2025 설비투자는 3.4억 달러에 그쳤다. 다만 이 수치는 회사 전체 합계이고 고객·건당 경제성은 아니다. [C:fcf@FY2025] [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [F201] [F11] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- [unit_economics] 고객 1명 단위의 지표가 없다. CAC·회수기간·순매출유지율·이탈률·월간 활성 이용자·구독 회원 수·부문별 총예약액과 조정 EBITDA를 리서처가 확보하지 못했다. 따라서 단위경제가 개선 중인지 악화 중인지 이번 근거만으로는 판정할 수 없다. 악화의 증거(CAC 상승과 이탈률 악화)는 보이지 않는다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- [unit_economics] 2026년 2분기 순이익 24억 달러에는 지분 재평가 이익이 세전 16억 달러 포함돼 있다. 영업이익은 18.9억 달러다. 본업 수익력은 영업이익과 조정 EBITDA로 봐야 한다. 이익 품질은 회계 모듈의 몫이다. 사업 관점에서는 보고 순이익이 영업 성과를 과대 반영한다는 점만 짚는다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F121] [F104]
- [industry] 성장 모멘텀은 유지되지만 단기 가이던스는 약하다. 3분기 총예약액 가이던스는 582.5억~602.5억 달러(환율 불변 기준 18~22% 성장, 환율 역풍 약 1%p)로 2분기 성장률 24%(환율 불변 22%)보다 낮다. 중간값 592.5억 달러는 컨센서스 593.3억 달러를 소폭 하회했고, 가이던스 EPS 0.86달러도 컨센서스 0.89달러보다 낮다. [F202] [F205] [F204] [F206] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow)
- [industry] 경쟁·규제 구도에서는 지역 단위 리스크가 드러난다. 나이지리아에서 12년 만에 철수했고, 현지 반독점 당국이 철수 경위를 조사 중이다. 성범죄 소송은 벨웨더 재판 3건을 합의로 마쳤다. 충당금과 잔여 소송 규모는 확보하지 못했다. 이는 사업 모델의 비용 항목이지만 크기는 불명이다. [S29](https://news.google.com/rss/articles/CBMilwFBVV95cUxPS2hNV0dUbTNrV3hwMU9FVDNxSF9vaWE5dHlWeW9PeldOb2R4RkRMTXc3NENOTXhHc19FZ1JxOE1sZXh0MVp0Q1FKdUY5Nm5qa245THJrSjhIQ1YtcXNyRURhRHRjbzNOaVNfQ3lBU291NkpJdmlLb0ZmdDZMOURHajZVNDZqMFRvWjhGbDR5YXNuSW14aWIw?oc=5) [S26](https://news.google.com/rss/articles/CBMirgFBVV95cUxNZjJweERweGlzcGVEZV9nRWNmaGdXSFpwXzhsZ2luOV9XMThzTFFqWEgxRXZXLXFUekhkMjJZbTB5R3J0enBNQnBtMGRoRDZHTnozQ2dIVFFEUUZmdktwMHlvenNZbXJBSWZfOXpteG1EeWNGUEhYaXZMSGNIZW4wZk1iR1c1clhpdUlHWFNzZlA4aVp4VnJNZklpYWhiU0Z3c3pGcWdFT2JSd09Yb3c?oc=5) [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5)
- [industry] 자율주행이 플랫폼의 위협이자 기회다. Baidu Apollo Go(두바이), Wayve(영국), Zipline(드론 배달)과의 제휴와 스페인 로보택시 허가 확보는 Uber이 공급 측 '집합자'로 남으려는 시도다. 계약 조건·단위경제·투자 약정 규모는 확인되지 않았다. 차량 소유자(AV 업체)가 직접 수요를 가져가면 수수료 구조가 흔들릴 수 있다. 이 점은 입증되지 않은 가설이다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S22](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQclNPVTE0M0xWUGpKVlMwT2VXLU9SaVBKbjdDOWRtTjhBelVBYnBwSzUzemlXVHBuQ3IybU1aQWZuZUZBZ2FJZEV4bFFkSGN0c0o0cE1tZ2MteUMxRU91RW03LVFKaE9faTBQaW54TWFtdFJ4WEcxQlcxaDFiSl8taWRwWEJyX1B2X25DakI1SmRFU1ZSdjh1NVBHOTMtckJzX183R181bUtQdDI1VkZSQmc2OWctMVZCcnJkWDNsaHFiMlVLX3JEZVVfX3VXenVia3FZZ1ZaV2RoVWQ2dl9uZGxhcjhZcjlFcUozSQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5) [S37](https://news.google.com/rss/articles/CBMiogFBVV95cUxNWXdxWlBSU0tMMnp3LWgzTkFUZHJIWC0xcVpVSFVHSnZCcnlNenlQS0pib2RBZXVaUDVBZzZCZ2FpVm8zOEVpeENEeHdoOGxFLWlULURSU0QyWVJtUDhwbnBfWW5QZy13TGJjOGpSTjBpazVPX3FrNkU1NEZuVmxtOWdDU2ZJUmhyWWVtMFA3empfX0t5Rno0TWE5NWNmV0JoeVE?oc=5)
- [customers] 배달·구독 측면에서 이용자 접점을 넓히는 움직임이 있다. Costco 배달을 Uber Eats로 전국 확대했다. 이용자 규모나 재구매율 같은 수치는 없다. 보도 기반이라 '확장 시도'로만 보고 해자의 증거로 쓰지 않는다. [S38](https://news.google.com/rss/articles/CBMingFBVV95cUxQamNCcUc3Tzg5Tk1NUXZmRW4zc0RsVTZxZ1VIbV94Ykh5STItcjVYVFFTUUdxMGJfOGxab0d6bVpZMUlCRV9GdTRBOHRPSUFHVnNiWW1fOXdzWmphd3dqZXdycC0zcG4wcV9qQk15ZTgyYjhjN09aeXFDMEFFQzkyc0VyVk4yUHhjdFVYOEp5X2ZUMzFBMXVCY0xlb3RMZw?oc=5)
- [runway] 재투자와 자본 환원 여력은 크다. FY2025 영업현금흐름은 101.0억 달러이고 자사주 매입은 65.2억 달러였다. 희석 주식 수는 FY2025에 -1.4% 줄었다. 부채는 107.3억 달러, 현금은 48.7억 달러다. 순부채/EBITDA는 0.46배(FY2025)로 레버리지 부담은 낮다. 한편 2026년 9월 약 3,300명(10%) 감원은 조직 단순화를 위한 비용 구조 조정이다. 구조조정 비용 규모는 미확보다. [F109] [F4] [C:share_change@FY2025] [F43] [F23] [C:net_debt_to_ebitda@FY2025] [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) [S25](https://news.google.com/rss/articles/CBMirgFBVV95cUxQelprYTZqU1R2cFNKc2lqX0NZdGFxR0tyVjI0OGRUNFJHSHJJSkkzWmlfNGY0cXc2ZmpZaUc2X3RHZ3h5eEx1U2xZdkRBOHJQZnpRMVJYckhhUUVqZVd0Q3FWczl0dVNycmxiUGxuT3lqcWZVdkpLeW1jaG5rV0lNeTU0RzVYNVZKQTNRLWxXbE9CMkplR2xQaTlzZEJOaUU0MVMyanZZaUIwY0o3OHc?oc=5) [S27](https://news.google.com/rss/articles/CBMiZEFVX3lxTE85bEp6SC12Ukx6bDZRb2hQU2FsbmhreFpnSVBIcHNjb0JIQ2YteWdLdkVndUYwRi1vc01waS1GRDJwUHlGTENQVG1Ec2FLUlplRWM0SF93V29GYXZ6TmFoWGlZRFI?oc=5)
- [claimed] 이용자와 공급자가 서로를 끌어들이는 양면 네트워크가 핵심 해자로 주장되지만, 점유율 추이·이탈률·가격 인상 후 잔존 기록은 근거에 없다. 매출이 FY2023 372.8억에서 FY2025 520.2억 달러로 컸고 2분기 총예약액 성장률이 24%인 점은 규모 확장의 흔적이다. 다만 경쟁사 대비 점유율을 입증하지는 못한다. [F134] [F136] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [S37](https://news.google.com/rss/articles/CBMiogFBVV95cUxNWXdxWlBSU0tMMnp3LWgzTkFUZHJIWC0xcVpVSFVHSnZCcnlNenlQS0pib2RBZXVaUDVBZzZCZ2FpVm8zOEVpeENEeHdoOGxFLWlULURSU0QyWVJtUDhwbnBfWW5QZy13TGJjOGpSTjBpazVPX3FrNkU1NEZuVmxtOWdDU2ZJUmhyWWVtMFA3empfX0t5Rno0TWE5NWNmV0JoeVE?oc=5)
- [proven] 고정비 레버리지가 재무제표에 나타난다. 영업이익률이 FY2023 3.0%에서 FY2025 10.7%로 올랐고, R&D는 매출 증가보다 느리게 늘었다(FY2023 31.6억, FY2025 34.0억 달러). ROIC도 5.7%에서 14.7%로 올랐다. 규모의 경제는 확인되지만, 경쟁사 대비 마진 비교는 없어 '해자'가 아니라 '운영 레버리지'까지만 입증된다. [C:operating_margin@FY2023] [C:operating_margin@FY2025] [C:roic@FY2023] [C:roic@FY2025] [F144] [F146]

### 경영진·자본배분 — mixed

자본배분 실적은 주주 친화적이다. FY2025 자사주 매입은 65.2억 달러로, SBC 18.3억 달러를 크게 넘어 희석을 상쇄하고도 주식 수를 줄였다(희석 주식 수 변화 FY2025 -1.4%). 이는 FY2024 +2.8%, FY2023 +5.9% 증가세가 뒤집힌 것이다. 반면 이 판단의 핵심인 보상 지표(DEF 14A), 내부자 매매, 과거 가이던스 적중률은 수집되지 않아 정렬도를 확정할 근거가 없다. 지분 평가이익과 인수(영업권 증가)처럼 질을 따져야 할 항목도 남아 있다. 그래서 정렬도는 'mixed'로 두며, 이는 근거 부족을 반영한 값이다.

- [compensation] 근거 없음. 2026-03-23 DEF 14A(S10)는 목록에 있으나 보상 연동 지표(장기 FCF·ROIC·주당가치 vs 단기 EPS·조정 EBITDA)와 베스팅 기간은 수집되지 않았다. 보상 정렬은 판단하지 않는다. [S10](https://www.sec.gov/Archives/edgar/data/1543151/000130817926000125/uber014597-def14a.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도는 수집되지 않았다. 2026-05-11 및 2026-02-04 8-K에 경영진 변동 항목이 있으나 내용은 확인되지 않았다. [S6](https://www.sec.gov/Archives/edgar/data/1543151/000155278126000320/e26247_uber-8k.htm) [S13](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000011/uber-20260130.htm)
- [guidance] 과거 가이던스 이력을 찾지 못해 적중률(C:guidance_hit_rate)을 계산할 수 없다. 신뢰도는 판단 불가다. 참고로 3분기 가이던스 총예약액 중간값 592.5억 달러는 컨센서스 593.3억 달러를 소폭 하회하고, Non-GAAP EPS 가이던스 0.86달러(범위 0.84~0.88)도 추정치 0.89달러보다 낮다. 이는 보수적 가이던스 관행일 수도 있으나, 이력이 없어 구분할 수 없다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow) [F202] [F205] [F204] [F206]
- [dilution] SBC는 FY2025 18.3억 달러로 매출 대비 3.5%이며 FY2021 6.7%에서 꾸준히 낮아졌다. 희석 주식 수는 FY2024 21.5억에서 FY2026Q2 20.5억으로 줄었다. 다만 분기 SBC는 FY2026Q1 4.7억에서 FY2026Q2 5.6억 달러로 늘었고, 이 증가가 일시적인지는 근거가 없다. [C:sbc_to_revenue@FY2025] [C:sbc_to_revenue@FY2021] [C:share_change@FY2025] [F55] [F61] [F160] [F161]
- [capital_allocation] 자사주 매입은 FY2023 0, FY2024 12.5억, FY2025 65.2억, FY2026Q1 한 분기에만 30.1억 달러로 급증했다. FY2025 FCF 97.6억 달러의 상당 부분이 환원에 쓰였고, 매입은 SBC(FY2025 18.3억)보다 훨씬 커서 희석을 가리는 수준을 넘어 실제 주식 수를 줄였다. 다만 매입 단가와 잔여 승인 한도는 수집되지 않아 고점 매입 여부는 판단할 수 없다. [F2] [F3] [F4] [F6] [C:fcf@FY2025] [F156]
- [capital_allocation] 부채는 FY2024 83.5억에서 FY2025 105.2억, FY2026Q2 107.3억 달러로 늘었고 매입이 확대된 시기와 겹친다. 그래도 순부채/EBITDA는 FY2025 0.46x(TTM 기준 0.72x)로 낮아 레버리지 부담은 제한적이다. 환원이 부채 증가를 동반했다는 점은 사실이다. [F37] [F41] [F43] [C:net_debt_to_ebitda@FY2025] [C:net_debt_to_ebitda]
- [capital_allocation] 영업권은 FY2025Q1 80.7억에서 FY2026Q2 94.7억 달러로 늘어, 이 기간에 인수나 이에 준하는 투자가 있었음을 시사한다. 대상·가격·수익률은 수집되지 않았다. 또 2분기 순이익 24억 달러에는 지분 재평가 이익 세전 16억 달러가 포함돼, 이익 일부는 영업이 아닌 투자 평가에서 나왔다. 내역은 미확보다. [F76] [F81] [F104] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- [capital_allocation] 경영진은 2026년 9월 기업 인력 약 3,300명(10%) 감축을 발표했다. 구조조정 비용 규모는 미확보다. 비용 통제 의지를 보여주는 신호일 수 있으나, 보상·지분 근거가 없어 주주 정렬의 증거로 쓰기는 이르다. [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) [S25](https://news.google.com/rss/articles/CBMirgFBVV95cUxQelprYTZqU1R2cFNKc2lqX0NZdGFxR0tyVjI0OGRUNFJHSHJJSkkzWmlfNGY0cXc2ZmpZaUc2X3RHZ3h5eEx1U2xZdkRBOHJQZnpRMVJYckhhUUVqZVd0Q3FWczl0dVNycmxiUGxuT3lqcWZVdkpLeW1jaG5rV0lNeTU0RzVYNVZKQTNRLWxXbE9CMkplR2xQaTlzZEJOaUU0MVMyanZZaUIwY0o3OHc?oc=5)

### 회계 품질 — watch

코드 신호는 하나도 걸리지 않았고, 영업현금흐름·FCF가 이익을 뒷받침한다. FY2025 영업현금흐름 101.0억 달러와 FCF 97.6억 달러는 순이익 100.5억 달러와 비슷한 수준이다. 현금이 이익보다 뒤처지는 구조는 아니다. 다만 보고 순이익은 그대로 믿으면 안 된다. FY2024(-57.6억)와 FY2025(-43.5억)의 법인세는 큰 음수라서 순이익을 크게 부풀렸다. 평가충당금 환입 같은 비현금 세금 이익으로 보이지만 내역은 확인하지 못했다. 2026년 2분기 순이익 23.9억 달러에도 세전 16억 달러의 지분 재평가 이익이 들어 있다. 이 이익은 반복되지 않고 현금도 아니다. 그래서 이익 배수(PER)보다 FCF와 SBC 차감 FCF(FY2025 79.4억 달러)를 기준으로 봐야 한다. 이연 세금·재평가 이익을 제외한 영업이익(FY2025 55.6억)이 경상 이익에 더 가깝다. 매출채권 증가, 영업권, SBC, 희석은 모두 문턱 안이다. 소송 충당금과 구조조정 비용, 2분기 OCF·capex 분기값은 확인하지 못해 watch로 둔다. 숫자를 믿을 수 없는 수준(red_flag)의 증거는 없다.

- [watch] FY2024·FY2025 법인세가 각각 -57.6억, -43.5억 달러의 큰 음수로, 순이익(98.6억, 100.5억 달러)을 크게 키웠다. 영업이익은 FY2024 28.0억, FY2025 55.6억 달러에 그쳐 순이익과 차이가 크다. 이는 이연법인세자산(평가충당금) 환입 성격의 비현금 이익으로 보이나 내역은 미확인이다. 경상 이익은 영업이익·FCF로 판단해야 하고 PER은 과소평가될 수 있다. [F85] [F86] [F98] [F99] [F115] [F116] [C:operating_margin@FY2025]
- [watch] FY2026 2분기 순이익 24.0억 달러 수준에는 세전 16억 달러의 지분(AV 등) 재평가 이익이 포함된다. 비현금·비반복 이익이므로 TTM 이익과 PER(15.06배)에서 제외하고 봐야 한다. 같은 분기 영업이익은 18.9억 달러다. [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F104] [F121] [C:pe]
- [info] 조정 EBITDA 28.2억 달러(총예약액 대비 4.9%)와 Non-GAAP EPS 가이던스는 SBC 같은 비용을 뺀 지표다. 코드의 non_gaap 신호는 걸리지 않았지만 조정 항목의 상세 내역은 미확보다. 가치는 GAAP 영업이익과 SBC 차감 FCF 기준으로 본다. [F199] [F200] [F204] [C:fcf_after_sbc@FY2025]
- [info] 발생액 비율은 FY2025 -0.1%로 문턱(10%) 안이고 DSO는 51.0일에서 26.9일로 개선됐다. 2026년 2분기 매출채권은 전년 같은 분기 대비 늘었지만 매출 증가와 비슷한 속도여서 채권 부풀리기 징후는 없다. [C:accruals_ratio@FY2025] [C:dso@FY2025] [F127] [F131] [F138] [F141]
- [info] SBC는 매출의 3.5%, 영업현금흐름의 18.1%로 문턱 아래다. 희석 주식 수는 FY2025 -1.4%로 줄었고 자사주 매입(FY2025 65.2억 달러)이 SBC 희석을 상쇄한다. 다만 매입 재원이 FCF이므로 SBC는 실질 비용으로 차감해서 봐야 한다. [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [C:share_change@FY2025] [F4]
- [info] 영업권은 총자산 대비 약 14%(94.7억/658.0억 달러)로 문턱(40%)보다 훨씬 낮다. 2026년 2분기에 영업권이 늘었으므로 M&A 인수가 반영됐을 가능성이 있다. 순부채/EBITDA는 0.46배로 낮다. [F81] [F182] [C:goodwill_to_assets] [C:net_debt_to_ebitda@FY2025]
- [watch] 성범죄 소송(벨웨더 3건 합의)의 충당금과 잔여 소송 규모, 2026년 9월 감원(약 3,300명)의 구조조정 비용, 나이지리아 철수 영향은 미확보다. 향후 일회성 비용으로 이익이 흔들릴 수 있어 10-Q 우발부채 주석을 확인해야 한다. 감사의견·계속기업 의문과 관련해 확인된 문제는 없다. [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5) [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) [S26](https://news.google.com/rss/articles/CBMirgFBVV95cUxNZjJweERweGlzcGVEZV9nRWNmaGdXSFpwXzhsZ2luOV9XMThzTFFqWEgxRXZXLXFUekhkMjJZbTB5R3J0enBNQnBtMGRoRDZHTnozQ2dIVFFEUUZmdktwMHlvenNZbXJBSWZfOXpteG1EeWNGUEhYaXZMSGNIZW4wZk1iR1c1clhpdUlHWFNzZlA4aVp4VnJNZklpYWhiU0Z3c3pGcWdFT2JSd09Yb3c?oc=5) [S3](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000032/uber-20260630.htm)
- [info] FY2026 2분기 OCF·capex 분기값이 XBRL 사실에 없고 FCF 28억 달러는 보도자료 수치다. 따라서 코드로 현금 전환을 대조하지 못했다. 그래도 TTM FCF가 100억 달러를 넘는다는 회사 발표는 FY2025 OCF 101.0억 달러와 맞는다. [F201] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [F109]

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (15%) 자율주행 업체가 수요를 직접 가져가 Uber이 수수료를 깎아 주는 하위 공급 채널로 밀렸다. Baidu, Wayve, Zipline 같은 파트너는 지금은 Uber 네트워크에 올라타지만, 차량과 기술을 가진 쪽이 자체 앱이나 다른 플랫폼으로 수요를 옮기고 Uber에는 수수료 인하를 요구한다. 총예약액 성장은 가이던스 하단에서 더 꺾이고 플랫폼 수수료율이 내려가 마진이 줄어든다. 계약 조건과 투자 약정 규모가 공개되지 않은 점이 이 위험을 가린다. [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5) [S32](https://news.google.com/rss/articles/CBMi7wFBVV95cUxPUlpoZ2p2RU0wTnB4cnBVSEo2X1hMYUNHZl8xZGRKV3ltYmFiMmxPbnZNcDBiMi1xcnBuR1RWTWU4QmhhX3RoVWRZVTM4aWcxbTZkSC1NMDBQakFNcDVaOUpmbGhlYVFnVk54NDkzb2tDckR6SktxaDh6TWQtT2cxUUxSRVpEaXVrTy1BNWZMTUNjbVBOTHRJMHJmcnVlTnV3Xy1xME51OVZyalV0R2lndzVhT2c3M2w1YnF2VUU4VklLcVRhNEhvV2d5S3dLSmc0TnVWaGhsdHItLVpxTkhTZmhxTERQYTFEWWxrTVgtWQ?oc=5) [S22](https://news.google.com/rss/articles/CBMi7AFBVV95cUxQclNPVTE0M0xWUGpKVlMwT2VXLU9SaVBKbjdDOWRtTjhBelVBYnBwSzUzemlXVHBuQ3IybU1aQWZuZUZBZ2FJZEV4bFFkSGN0c0o0cE1tZ2MteUMxRU91RW03LVFKaE9faTBQaW54TWFtdFJ4WEcxQlcxaDFiSl8taWRwWEJyX1B2X25DakI1SmRFU1ZSdjh1NVBHOTMtckJzX183R181bUtQdDI1VkZSQmc2OWctMVZCcnJkWDNsaHFiMlVLX3JEZVVfX3VXenVia3FZZ1ZaV2RoVWQ2dl9uZGxhcjhZcjlFcUozSQ?oc=5) [S39](https://news.google.com/rss/articles/CBMioAFBVV95cUxQRHFPZExzM0E1RWFGell1dENnMk1DZGRtTkNnSUQ2SDJRM1dGckxrdTNYMnZlYUpkaGtsa1ExVVhJdVRxeWllRkhYcmxWcmp1aE80ZEVqUS1xbGpnN2w4NVRTUm1nZUVpcXd0bDlXZ1lzeEd2bGZQdlJFWUd1ZmpWUjMtUXktVnR4LWpDb3FwWTVZQ1VxbG9fWGtGUF9CekNN?oc=5) [F202]
- (12%) 소송과 규제 비용이 상시 비용이 되어 이익을 갉아먹었다. 성범죄 소송은 벨웨더 재판 3건을 합의로 끝냈지만 충당금과 잔여 소송 규모는 확인되지 않았다. 합의가 쌓이면 더 많은 원고를 부르고, 나이지리아 철수 조사 같은 지역 규제 마찰이 다른 시장으로 번진다. 모델은 소송 비용을 FCF 마진에 사실상 반영하지 않았다. 영업이익이 최근 분기 수준을 지키지 못하면 이 경로가 진행 중이다. [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5) [S26](https://news.google.com/rss/articles/CBMirgFBVV95cUxNZjJweERweGlzcGVEZV9nRWNmaGdXSFpwXzhsZ2luOV9XMThzTFFqWEgxRXZXLXFUekhkMjJZbTB5R3J0enBNQnBtMGRoRDZHTnozQ2dIVFFEUUZmdktwMHlvenNZbXJBSWZfOXpteG1EeWNGUEhYaXZMSGNIZW4wZk1iR1c1clhpdUlHWFNzZlA4aVp4VnJNZklpYWhiU0Z3c3pGcWdFT2JSd09Yb3c?oc=5) [S29](https://news.google.com/rss/articles/CBMilwFBVV95cUxPS2hNV0dUbTNrV3hwMU9FVDNxSF9vaWE5dHlWeW9PeldOb2R4RkRMTXc3NENOTXhHc19FZ1JxOE1sZXh0MVp0Q1FKdUY5Nm5qa245THJrSjhIQ1YtcXNyRURhRHRjbzNOaVNfQ3lBU291NkpJdmlLb0ZmdDZMOURHajZVNDZqMFRvWjhGbDR5YXNuSW14aWIw?oc=5) [F121]
- (10%) 부채로 자사주를 사고 성장이 꺾이는 고점 환원이었다. 부채는 FY2024의 83.5억 달러에서 FY2026Q2의 107.3억 달러로 늘었고, 같은 기간 자사주 매입은 FY2025 65.2억 달러, FY2026Q1 한 분기에만 30.1억 달러로 급증했다. 현금은 FY2025의 71.0억 달러에서 FY2026Q2의 48.7억 달러로 줄었다. 매입 단가와 잔여 승인 한도는 알 수 없다. 현금창출이 둔화되면 완충이 얇아지고, 매입은 중단되며 주식 수 감소라는 가치 원천도 사라진다. AV 투자나 인수가 겹치면 자본시장에 기대야 한다. [F37] [F43] [F4] [F6] [F21] [F23]
- (15%) 이익의 질에 대한 착시가 깨지고 배수가 줄었다. 순이익은 FY2024·FY2025의 큰 음수 법인세와 2분기의 세전 16억 달러 지분 재평가 이익으로 부풀려져 있다. 시장이 PER 15.06배를 싸다고 본 것이 실제 경상 이익 기준으로는 비싼 값이었다. 3분기 가이던스가 컨센서스를 밑돈 것은 성장 둔화의 첫 신호였을 수 있다. 조정 EBITDA마저 가이던스 하단에 못 미치면 성장과 마진이 함께 꺾인 것이어서 출구 배수가 10배 수준까지 눌린다. [F85] [F86] [F104] [F121] [S43](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) [S45](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow) [F203] [C:pe]
- 약한 가정 `base.fcf_margin`: 기본 시나리오는 FCF 마진을 FY2025의 18.8%보다 높은 19%에 고정한다. 그런데 이 마진에는 소송 충당금, 감원 구조조정 비용, AV 투자 부담이 사실상 들어 있지 않다. 현재 마진이 이미 사상 최고 구간이어서 평균 회귀와 AV 수수료 압박에 가장 취약하다. 이 가정이 1%p만 흔들려도 5년 FCF 경로 전체가 움직인다. [C:fcf_margin@FY2025] [S40](https://news.google.com/rss/articles/CBMiowFBVV95cUxQTWE5TExfdXhPdE1Ua2pJWGNzbXJOak44RjRzTDM3SmFjVXVrcDFldGtWRG1neHJpeFFmVGhOczQ2ZWJBMjJYSC02V0g5YkNCSk83bDBaWmE5NmdrMmtLQnByeFdya1dVckpJamhJNktfSTVMeW9lUVM5Z0RVeVlxVmo4cnhIeVptNVR0aTNzTzBSVmx2bWJGLXZIdFJ2a2RZYmNN?oc=5) [S24](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQY3ZtbUlneW5fUEJTZWtoUXE0TmVfOExkdEw4N3BHYlZTWTVweHN3TmNxbHppTmprNld5T0ZGQTAtZEphQks4ejRRWXZxVkc3dFh6WVhxRFpINm15QUlCZEtaSWJWVkxjWWdGX3FWT080U01KdER1SEhBaEFTeHhvdFZaQXRRNDRJUWRRbU11akJib2hiOTU1dGw4bXk3RXJ6aUpkWm1SSTc?oc=5) [S30](https://news.google.com/rss/articles/CBMirAJBVV95cUxPTU5GZnpnbXlteTNKV250bFZfaWpnZ0lrX2RZQ2laRVpOdjV4eEpxQnFzWHUwWHJNbGZ2SjB4MGFsZ25WYnItTF9GaDZfYVJMQjlPb19kbzl5a2VXanN3REkyUG0yaDdDNUQ0Q1JwVGx5Y2N2ajZ0dE04NndWSzZPdXZwMmJBTVA0b3NXSzE0aXl5TTAwSERaeGJEQlU2U0puSVE2X1hZNlFsaDdQSkNUMDN0Mm9melpPMTJtYkwzMTIxLURxNzRqTTVBRkszN3pKVDAtVTVTV1dvakZMUHZqYVhiUHBKNUtMUS13emVpZHFld0pxMkloUHgxN1dpVVY0YmJ6MEM2THVDWU9iYTRKU0pQS0tpWlhaUGVkSko3cVBJbGpMMkxHVVBibHA?oc=5)
- 약한 가정 `base.exit_multiple`: 출구 P/FCF 15배는 현재 시장 수준보다 높은 값으로, 성장률이 두 자릿수 초반으로 둔화한 뒤에도 같은 배수를 받는다고 가정한다. 기저율 표가 없어 이 성장과 배수를 함께 해낸 기업 비율을 확인하지 못했다. 민감도에서 멀티플 ×0.75만 적용해도 기본 시나리오 수익률은 10.8%로 내려간다. [C:ev_revenue] [C:pe] [C:base_rate@base]
- 약한 가정 `base.share_change`: 모델은 FCF를 전부 순현금에 쌓고 SBC 희석만 반영한다. 실제로는 부채를 늘려 자사주를 사고 있다. 순현금 경로가 현실의 환원 정책과 다르므로 현금 축적 기여(+5.3%)가 과대 평가됐을 수 있고, 환원이 멈추면 이 기여도 흔들린다. [F4] [F6] [F43] [F23] [C:share_change@FY2025]

## 검증 (L6)

주장 70개 — supported 63 · unsupported 6 · contradicted 0 · leap 1 · 미검증 0

- [unsupported] 앤더슨: 사전 부검: 성범죄 소송과 지역 철수·규제 조사는 이 사업의 구조적 비용이다. 충당금 규모가 미확보라 마진 상방 가정이 흔들릴 수 있다. 전문경영인 체제라 창업자 — 소송과 철수·조사는 뉴스 제목이 받치지만, '전문경영인 체제라 창업자의 장기 지평에 기대기 어렵다'는 사실은 인용에 없다.
- [unsupported] 모델러: 우리 기본 시나리오의 매출 성장은 컨센서스와 크게 다르지 않아 성장 전망에서는 알파를 주장하지 않는다. 차이는 두 가지다. 첫째, 이익의 질이다. 순이익은 세금  — 없는 근거 인용: C:implied_cagr
- [unsupported] 회계 품질: 발생액 비율은 FY2025 -0.1%로 문턱(10%) 안이고 DSO는 51.0일에서 26.9일로 개선됐다. 2026년 2분기 매출채권은 전년 같은 분기 대비 늘었 — 발생액 비율과 DSO 26.9일은 맞지만 '51.0일'이라는 이전 DSO는 인용에 없다.
- [unsupported] 레드팀: 모델은 FCF를 전부 순현금에 쌓고 SBC 희석만 반영한다. 실제로는 부채를 늘려 자사주를 사고 있다. 순현금 경로가 현실의 환원 정책과 다르므로 현금 축적 기여 — 출처 없는 숫자 5.3% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 회계 품질: FY2026 2분기 순이익 24.0억 달러 수준에는 세전 16억 달러의 지분(AV 등) 재평가 이익이 포함된다. 비현금·비반복 이익이므로 TTM 이익과 PER(1 — 24억 순이익과 16억 재평가 이익, 영업이익 18.9억은 맞다. 그러나 '비현금·비반복'과 'AV 등'은 자료에 없는 추론이다.
- [unsupported] 회계 품질: 영업권은 총자산 대비 약 14%(94.7억/658.0억 달러)로 문턱(40%)보다 훨씬 낮다. 2026년 2분기에 영업권이 늘었으므로 M&A 인수가 반영됐을 가능 — 없는 근거 인용: C:goodwill_to_assets
- [unsupported] 레드팀: 출구 P/FCF 15배는 현재 시장 수준보다 높은 값으로, 성장률이 두 자릿수 초반으로 둔화한 뒤에도 같은 배수를 받는다고 가정한다. 기저율 표가 없어 이 성장과 — 없는 근거 인용: C:base_rate@base

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
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 2.71x |
| PER (pe) | 15.06x |
| 순부채/EBITDA (net_debt_to_ebitda) | 0.72x |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 30% | 682.4억 USD | 5.6% | 12% | 10x | 55.50 | 34.46 | -4.6% |
| 기본 | 50% | 884.0억 USD | 11.2% | 19% | 15x | 146.75 | 91.12 | +15.8% |
| 강세 | 20% | 1,018.6억 USD | 14.4% | 23% | 19x | 246.82 | 153.25 | +28.5% |

확률 가중: 주당 가치 139.38 · IV 86.55 · 기대 연 수익률 +14.7% (C:expected_irr) · 손실 확률 30% (C:p_loss) · 현재 주가 70.35

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +10.6% · 마진 변화 +0.2% · 멀티플 변화 -0.4% · 주식 수 변화 -1.0% · 현금 축적 +5.3% = +14.7%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | +5.7% | +10.4% | +14.4% |
| +0%p | +10.8% | +15.8% | +20.1% |
| +5%p | +15.9% | +21.3% | +25.8% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 585.2억 USD | 18.8% | 110.1억 USD | 20.7억 | 56.8억 USD |
| FY2027 | 661.3억 USD | 18.9% | 124.7억 USD | 20.9억 | 181.5억 USD |
| FY2028 | 737.3억 USD | 18.9% | 139.4억 USD | 21.1억 | 320.9억 USD |
| FY2029 | 811.0억 USD | 19.0% | 153.7억 USD | 21.3억 | 474.6억 USD |
| FY2030 | 884.0억 USD | 19.0% | 168.0억 USD | 21.5억 | 642.6억 USD |

### 컨센서스 대비 (C:consensus_diff@지표@기간)

| 지표 | 기간 | 컨센서스 | 기본 시나리오 | 차이 |
|---|---|---|---|---|
| revenue | FY2026 | 582.8억 USD | 585.2억 USD | +0.4% |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- base 시나리오 매출 성장: 연 11.2% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 14.4% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=6.61x, revenue_5y=1.96x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=53.9억 USD
- 애크먼 case={"from": "base"}: price=70.3, net_debt_to_ebitda=0.72x, leveraged=아니오, intrinsic_value=91.1, mos=22.8%

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

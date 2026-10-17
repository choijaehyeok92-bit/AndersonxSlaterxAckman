# Pony AI (PONY) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 모델** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✗ model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

## 1. Variant perception

- 시장이 반영한 것: 주가 7.29달러(F74)는 52주 저점 부근이고 EV/매출 17.82x(C:ev_revenue)다. 시장은 높은 성장을 이미 반영하면서도 흑자 전환을 확신하지 않는다. 역DCF(C:implied_cagr)가 시장이 요구하는 매출 성장을 보여 주며, 우리 기본 시나리오의 성장(C:implied_cagr 대비)과 비교한다.
- 우리가 다르게 보는 점: 2분기 서비스 매출 가속은 실재하지만, 이를 단위경제 개선의 증거로 읽는 것은 이르다. 총이익률은 FY2022 이후 하락해 낮은 수준에서 정체한다(C:gross_margin@FY2025). 기본 시나리오는 성장은 인정하되 FCF 마진을 낮게 잡아 시장의 낙관 서사와 다르다. 시장이 성장을 과소평가하는지, 마진을 과대평가하는지는 코드의 시나리오 가치와 역DCF 대비로 판단한다.
- 왜 우리가 맞는가: 차량당 매출·원가가 공시되지 않아(S54) 마진 개선은 아직 입증되지 않았다. 반대로 2분기 서비스 매출이 +691.2%(F77)로 늘고 차량이 늘어나는 추세는 연간 수치에 아직 충분히 반영되지 않았다. 따라서 성장은 컨센서스보다 높게 볼 여지가 있으나 컨센서스는 찾지 못했다. [F74] [F77] [F79] [C:ev_revenue] [C:gross_margin@FY2025] [C:implied_cagr] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- 촉매: 3분기·4분기 실적에서 서비스 총이익률과 차량당 매출 공개, 연말 3,500대 달성 여부, 유럽 첫 상업 서비스 개시.
- 시점: 2026년 11월 3분기 실적부터 2027년 2분기까지

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ 주가 기준일 2026-09-22이 as_of(2026-10-18)보다 26일 오래됨
- ⚠ 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 분석 모듈 (L4)

### 사업·산업 — unclear

Pony AI는 자율주행 기술 스택을 보유하고 로보택시 서비스(요금 징수), 로보트럭, 기술 라이선스·차량 판매로 매출을 낸다. FY2025 매출은 9,000만 달러(C:revenue@FY2025, 전년 +20.0%)였으나 총이익률은 15.7%(C:gross_margin@FY2025), 영업이익률은 -289.8%(C:operating_margin@FY2025)로 구조적 적자다. 2026년 2분기 총매출은 약 3,620만 달러(+68.8%)이고 로보택시 서비스 매출은 1,210만 달러(+691.2%)로 매출 믹스가 서비스로 이동 중이다(F76, F77, S54). 차량 1,975대, 연말 3,500대 목표, Uber와 유럽 2,000대 공동 배치 계획이 있다(F78, F79, S54, S43). 다만 차량당 매출·비용 등 단위경제 공시가 없어 개선 여부를 숫자로 확인할 수 없고, 현금은 FY2025 말 기준 순현금 11.7억 달러(C:net_cash@FY2025)로 영업현금유출 1.6억 달러(F40)를 수년 버틸 수준이나 주식 수가 급증해 왔다.

- [unit_economics] 총이익률이 FY2022 46.9%에서 FY2023 23.5%, FY2024 15.2%, FY2025 15.7%로 내려와 낮은 수준에서 정체한다. 규모가 커지면 개선된다는 증거는 아직 연간 수치에 없다. [C:gross_margin@FY2022] [C:gross_margin@FY2023] [C:gross_margin@FY2024] [C:gross_margin@FY2025]
- [unit_economics] 2분기 로보택시 서비스 매출은 1,210만 달러로 전년 대비 +691.2%, 요금 징수 매출은 +849.3% 늘었다. 성장은 매우 빠르지만 기저가 작고, 차량당 일 매출·주문 수·차량 원가·운전자 없는 차량 비중은 공시되지 않아 CAC·이탈률 대신 볼 단위경제 지표가 없다. [F77] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- [unit_economics] 연간 매출 성장은 FY2023 5.1%, FY2024 4.3%, FY2025 20.0%로 완만했다가 2026년 2분기에 +68.8%로 가속했다. 이 가속이 지속되는지는 다음 분기 이후로 확인이 필요하다. [C:revenue_growth@FY2023] [C:revenue_growth@FY2024] [C:revenue_growth@FY2025] [F76] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- [industry] 유럽 진출은 Uber 등 플랫폼과의 협력 구조로 진행되며 런던 등 신규 도시 계획이 보도된다. 규제 승인, 현지 경쟁사, 차량 공급 원가 같은 산업 구조 변수는 근거에 없다. 가치사슬상 Pony는 기술·운영 공급자이고 수요 접점은 Uber 같은 플랫폼에 있을 가능성이 크다. [S34](https://news.google.com/rss/articles/CBMinwFBVV95cUxQQkpUaUFJdDNySDFnenkzQmFVRVV5cTktN0ZSakp5enc0UFp2T3VWc0lHU2taWHFCTV9uRmMwSUpKTU1vYTc1Q2YwbzZsYk5FcVE1bWtCVmZnRmRwbUFObmJoRHlzRnBqajRBQ1RzZHBwSTRrSlBpSkJUT3dFemQ5dkRzbzJqdWczWHo2S0wwaUpIX194cU44RGFTeWtLZjTSAaQBQVVfeXFMTm1FdkFRcy1fQzRXNlVUdHJmTDZaYVZiYjJ1MElheWpXejI0bnBpZ2JNcS0wNC0ySkczMVFJcHBRMFVvZHF5TWVVSnEyN0F0N2thbmRYbVhtaE1NTXg0Q29MUFNvVGtEblVvLUViQ2xXb1VIdEFfMzBPNF91WkF1eTNYdUZyWXpBS296X09HVTFidlNOVDAtcWpZTm52bG9PeXgzZ2E?oc=5) [S37](https://news.google.com/rss/articles/CBMimAFBVV95cUxPRWphNWlOMkMwRUJyX1RPVGJOeTRaOHJBQi1YcUZtcXNnZUMtNDVDb3FBV3JkV01zWjZvN1czbUxlaDk0bVFoTV80cUg5UGE3OTRaLTZ3SkhBNjZkbXZPZnZxQ3Z2LWxrcG5IdUNSRVk5MGJUVlpQdGZQUjNfbmFlMFBuMllqcHF4MHBaZ0ZYZ2hSRGtEeDRfNA?oc=5) [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5)
- [customers] FY2025 매출이 늘 때 이연매출은 감소했고 코드 신호가 매출 당겨쓰기 가능성을 표시한다. 고객·파트너 집중도와 차량 판매 대 서비스 매출 구성이 공시되지 않아 매출 질을 평가하기 어렵다. [F16] [F17] [C:deferred_revenue]
- [runway] FY2025 말 현금 2.9억 달러와 단기투자 8.7억 달러로 순현금은 11.7억 달러이며 영업현금흐름은 -1.6억 달러다. 단순 비교로 수년의 활주로가 있다. 다만 희석주식 수는 FY2025 3.8억으로 연 64.5% 증가 신호가 떴고 SBC는 매출의 34.2%여서, 성장 자금이 주주 희석으로 조달돼 왔다. [F5] [F69] [F40] [C:net_cash@FY2025] [C:sbc_to_revenue@FY2025] [C:dilution]
- [runway] 시가총액 27.7억 달러에 EV/매출 17.82x로 시장은 높은 성장을 이미 가격에 넣고 있다. 주가는 52주 범위 6.58~24.06달러의 하단 부근이고 기준일보다 26일 오래된 가격이다. 재투자 수익률(ROIC)은 FY2025 -42.3%여서 재투자 활주로의 질은 아직 입증되지 않았다. [C:market_cap] [C:ev_revenue] [C:roic@FY2025] [F74] [S52](https://www.benzinga.com/stock/PONY)
- [claimed] 자율주행 소프트웨어·데이터 기술 우위는 회사 발표와 보도로만 서술된다. R&D는 FY2025 2.2억 달러(F60)로 매출의 큰 비중이지만 경쟁사 대비 성능·점유율 자료는 근거에 없다. [F60] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [S35](https://news.google.com/rss/articles/CBMickFVX3lxTE1FRUNEbHowbnZjM01oSS1MeEJhSzVkcEhCYzE1OHdzbXpkeGxTOGhGMm0yUVFyS2o1Ym5LLXpiT0lPU2dBbGxYR0F6bWg5TW9ZN2FhS3pseVo0ei1EYUFub1lNSlh2ODNHRmt3VTRvRTAzUQ?oc=5)
- [claimed] Uber 같은 플랫폼 파트너십은 수요 확보 채널이지만, 파트너가 다른 자율주행 업체로 바꾸는 비용이나 독점 계약 여부는 확인되지 않는다. 오히려 고객·플랫폼 의존 위험일 수 있다. [S34](https://news.google.com/rss/articles/CBMinwFBVV95cUxQQkpUaUFJdDNySDFnenkzQmFVRVV5cTktN0ZSakp5enc0UFp2T3VWc0lHU2taWHFCTV9uRmMwSUpKTU1vYTc1Q2YwbzZsYk5FcVE1bWtCVmZnRmRwbUFObmJoRHlzRnBqajRBQ1RzZHBwSTRrSlBpSkJUT3dFemQ5dkRzbzJqdWczWHo2S0wwaUpIX194cU44RGFTeWtLZjTSAaQBQVVfeXFMTm1FdkFRcy1fQzRXNlVUdHJmTDZaYVZiYjJ1MElheWpXejI0bnBpZ2JNcS0wNC0ySkczMVFJcHBRMFVvZHF5TWVVSnEyN0F0N2thbmRYbVhtaE1NTXg0Q29MUFNvVGtEblVvLUViQ2xXb1VIdEFfMzBPNF91WkF1eTNYdUZyWXpBS296X09HVTFidlNOVDAtcWpZTm52bG9PeXgzZ2E?oc=5) [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5) [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- [claimed] 로보택시 1,975대에서 연말 3,500대, 해외 4,000대 이상 파이프라인 목표는 규모 확대 계획이지만 목표(guidance)일 뿐 실제 규모의 원가 우위는 입증되지 않았다. 총이익률은 FY2022 46.9%에서 FY2025 15.7%로 낮아졌다. [F78] [F79] [C:gross_margin@FY2022] [C:gross_margin@FY2025] [S50](https://news.google.com/rss/articles/CBMimgFBVV95cUxPWm94c24xeGcyMlA5MGZnNE8zWmJqX0JaU1YyV3Jqb1Q2VGJwaGJ1Q2NjNG5QZnBweHpGdkRWUjFxUWFqMG1HYWtzNEtkQzdSZVpzUDlqTm5uZk1EZmpXV3BuUHRIaXg0Z3JRZjJHWlVHSWl0d2EzTm00QWhKODVoeDhqTG5DSnBraEpCMG5MZjVFcmpRdEJiWlh3?oc=5)

### 경영진·자본배분 — mixed

경영진 보상 구조, 내부자 매매, 이중의결권 구조는 모두 근거가 없어 정렬 여부를 직접 판단할 수 없다. 확인되는 것은 희석과 가이던스 두 가지다. 주식 수는 FY2025에 232.3% 늘었고(C:share_change@FY2025), SBC는 매출 대비 34.2%였다(C:sbc_to_revenue@FY2025). 이는 기존 주주 몫이 크게 줄었다는 뜻이다. 가이던스는 연말 로보택시 3,500대 이상 목표(F79) 하나뿐이다. 2분기 말 1,975대(F78)와 비교할 수 있을 뿐, 과거 가이던스 적중률(C:guidance_hit_rate)은 계산되지 않았다. 이 때문에 정렬은 '혼재(mixed)'로 두며, 이는 근거 부족의 표시이지 긍정 평가가 아니다.

- [compensation] 근거 없음. 외국 민간발행인이라 DEF 14A가 없고, 보상 연동 지표와 베스팅 기간은 20-F(S22) 본문으로 확인되지 않았다. 보상이 장기 가치 지표와 연동되는지 판단할 수 없다. [S22](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm)
- [insider] 근거 없음. 창업자·경영진 지분, 이중의결권 구조, 최근 내부자 매수·매도에 대한 사실이 수집되지 않았다. 보도에는 CEO가 5년 내 로보택시가 보편화될 것으로 본다는 발언이 있으나(S35), 이는 지분이나 매매 정보가 아니다. [S35](https://news.google.com/rss/articles/CBMickFVX3lxTE1FRUNEbHowbnZjM01oSS1MeEJhSzVkcEhCYzE1OHdzbXpkeGxTOGhGMm0yUVFyS2o1Ym5LLXpiT0lPU2dBbGxYR0F6bWg5TW9ZN2FhS3pseVo0ei1EYUFub1lNSlh2ODNHRmt3VTRvRTAzUQ?oc=5)
- [dilution] 희석 주식 수는 FY2024에 28.3%, FY2025에 232.3% 증가했다. 증가율이 크게 뛴 것은 FY2024 이후 주식 수 기준이 바뀐 영향일 수 있다. 원인은 수집된 자료로 확인되지 않는다. 코드 신호도 연 64.5% 증가를 경고했다. 기존 주주 몫이 크게 줄었다는 사실은 분명하다. [C:share_change@FY2024] [C:share_change@FY2025] [C:dilution] [F20] [F21]
- [dilution] SBC/매출은 FY2024에 169.3%, FY2025에 34.2%였다. FY2025 SBC 규모는 FY2024보다 크게 줄었지만 매출 대비로는 여전히 높다. 코드 신호 기준 10%를 넘는다. 자사주 매입은 FY2023에 99만 USD가 기록된 것이 전부다. 이후 매입은 확인되지 않았고, 이 규모로는 희석을 상쇄하지 못한다. [C:sbc_to_revenue@FY2024] [C:sbc_to_revenue@FY2025] [C:sbc_to_revenue] [F1] [F63] [F64]
- [guidance] 확인된 가이던스는 연말 로보택시 3,500대 이상 목표 하나뿐이다. 2분기 말 보유는 1,975대로, 하반기에 크게 늘려야 달성된다. 이 목표의 적중 여부는 아직 알 수 없다. 매출·비용 가이던스와 과거 가이던스 이력은 수집되지 않아 적중률은 계산되지 않았다. 신뢰도는 판단 불가다. [F78] [F79] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [C:guidance_hit_rate]
- [capital_allocation] FY2025 연구개발비는 2.2억 USD로 영업현금흐름 적자(-1.6억 USD)와 같은 규모다. 사실상 모든 자본을 기술·차량 확장에 재투자하는 구조다. 연구개발비의 수익률은 아직 측정되지 않는다. 같은 해 영업이익률은 -289.8%였다. [F60] [F40] [C:operating_margin@FY2025]
- [capital_allocation] FY2025 말 현금 2.9억 USD와 단기투자 8.7억 USD를 합치면 현금성 자산이 크게 늘었다. 같은 해 영업현금흐름은 적자였으므로 이 증가는 외부 조달로 이뤄졌다고 추정한다(조달 내역은 수집되지 않았다). 6월 말 잔액은 제3자 요약(S53)에만 있고 6-K로 확인되지 않았다. 인수나 고점 자사주 매입 이력도 확인되지 않았다. [F5] [F69] [F40] [S53](https://transcripts.platformaeronaut.com/summaries/PONY-2Q26-AI-Summary) [C:net_cash@FY2025]
- [capital_allocation] Uber와 유럽 공동 배치 2,000대 이상 계획(S43, S54)은 자본을 파트너와 나눠 쓰는 방식이 될 수 있다. 다만 차량 소유, 비용 분담, 계약 조건은 근거에 없다. 자본효율 개선으로 볼 수 있는지는 판단할 수 없다. [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5) [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [S34](https://news.google.com/rss/articles/CBMinwFBVV95cUxQQkpUaUFJdDNySDFnenkzQmFVRVV5cTktN0ZSakp5enc0UFp2T3VWc0lHU2taWHFCTV9uRmMwSUpKTU1vYTc1Q2YwbzZsYk5FcVE1bWtCVmZnRmRwbUFObmJoRHlzRnBqajRBQ1RzZHBwSTRrSlBpSkJUT3dFemQ5dkRzbzJqdWczWHo2S0wwaUpIX194cU44RGFTeWtLZjTSAaQBQVVfeXFMTm1FdkFRcy1fQzRXNlVUdHJmTDZaYVZiYjJ1MElheWpXejI0bnBpZ2JNcS0wNC0ySkczMVFJcHBRMFVvZHF5TWVVSnEyN0F0N2thbmRYbVhtaE1NTXg0Q29MUFNvVGtEblVvLUViQ2xXb1VIdEFfMzBPNF91WkF1eTNYdUZyWXpBS296X09HVTFidlNOVDAtcWpZTm52bG9PeXgzZ2E?oc=5)

### 회계 품질 — watch

현재 근거로는 숫자 자체를 믿지 못할 증거가 없어 red_flag는 아니다. 순손실과 영업현금유출이 같은 방향이고(순이익 FY2025 -1.3억, OCF -1.6억 USD), 발생액 비율은 2.2%, DSO는 138일에서 96일로 줄었다. 그래도 조정해서 봐야 할 숫자가 있어 watch로 둔다. 첫째, SBC가 매출의 34.2%로 크다. 비용 구조를 볼 때 SBC를 현금 비용으로 간주해야 한다. 둘째, FY2025 세전손실(-7,676만 USD)이 영업손실(-2.6억 USD)보다 훨씬 작다. 영업외 이익이 크다는 뜻인데 근거에 내역이 없다. 셋째, 순손실(-1.3억 USD)이 세전손실보다 크다. 이 차이는 근거만으로는 설명되지 않아 20-F의 손익계산서와 대조해야 한다. 넷째, 감사의견, 감사인, 특수관계자 거래, 매출 인식 정책, 고객 집중도 정보가 없어 감사 관련 결론은 내릴 수 없다. 2026년 2분기의 순손실, 현금, OCF는 제3자 요약(S53)에만 있어 판단에 쓰지 않았다. 매출 성장은 FY2025 +20.0%이고 2분기 로보택시 서비스 매출이 급증했다(S54). 다만 총이익률이 15.7%로 낮아 매출 성장이 이익 개선으로 이어지는지는 아직 확인되지 않았다.

- [concern] sbc_to_revenue: SBC가 FY2025 매출의 34.2%(3,080만 USD)로 문턱 10%를 크게 넘는다. FY2024의 169.3%(1.3억 USD)는 상장 전후 일회성 성격이 강해 보이지만 이 근거만으로는 단정할 수 없다. FY2025에도 일회성이 아닌 수준이 남아 있다. SBC는 실제 경제적 비용이므로 영업현금흐름과 FCF를 볼 때 SBC를 현금 지출로 간주한 값을 함께 봐야 한다. 매출 대비 비중이 크지만 영업현금흐름 대비로는 문턱 50%를 넘지 않는다. sbc_to_ocf 신호가 켜지지 않은 것도 이를 뒷받침한다. 영업현금유출이 SBC로 가려진 구조는 아니다. [F61] [F62] [F63] [F64] [F56] [F40] [C:sbc_to_revenue@FY2025] [C:sbc_to_revenue@FY2024]
- [benign] deferred_revenue: FY2025 매출은 늘었는데(9,000만 USD) 이연매출이 323만에서 192만 USD로 줄어 코드 신호가 켜졌다. 그러나 이연매출의 절대 규모가 매출에 비해 매우 작아 매출 당겨쓰기를 숨길 수 있는 크기가 아니다. 같은 기간 매출채권도 2,856만에서 2,364만 USD로 줄고 DSO도 138.9일에서 95.9일로 줄어, 선수금이 줄고 외상 매출이 늘어나는 식의 매출 부풀리기 패턴은 아니다. 다만 매출 인식 정책(총액·순액, 기간 인식)을 확인하지 못했으므로 benign 판정은 규모에 근거한 것이다. [F16] [F17] [F51] [F52] [F56] [C:deferred_revenue@FY2025] [C:dso@FY2025]
- [benign] dilution: 희석 주식 수가 FY2024 1.1억에서 FY2025 3.8억으로 늘어 연 64.5% 증가로 잡혔다. 같은 기간 자기자본이 FY2023 -6.8억에서 FY2024 +9.5억 USD로 뒤집힌 것을 보면, 상환 의무가 있는 우선주가 보통주로 전환되면서 가중평균 주식 수가 한꺼번에 늘어난 것으로 보인다. 이는 근거에서 추정한 것이며 20-F로 확인하지 않았다. 반복되는 증발적 희석이라고 보기는 어렵다. 다만 FY2025 말 발행주식 4.335억(F65)과 가중평균 3.8억(F21)의 차이, 그리고 SBC 34.2%가 앞으로도 주식 수를 늘릴 수 있다는 점은 남는다. 주당 가치 계산에는 최신 희석 주식 수가 필요한데 리서처가 찾지 못했다. [F20] [F21] [F65] [F23] [F24] [C:dilution] [C:share_change@FY2025]
- [watch] FY2025 영업손실은 -2.6억 USD인데 세전손실은 -7,676만 USD로 영업외 이익이 크게 잡힌다. 내역이 근거에 없다. 이자수익이나 공정가치 평가이익일 가능성이 있으나 확인하지 못했다. 영업외 이익은 반복성이 낮으므로 사업의 수익성은 영업손실로 판단해야 한다. [F44] [F48]
- [watch] FY2025 순손실(-1.3억 USD)이 세전손실(-7,676만 USD)보다 크고, 법인세 사실은 FY2025가 비어 있다. 세금 비용만으로 설명되는 차이인지, 사실 태그가 다른 이익 항목(지배주주 귀속 이익 등)인지 근거에서 알 수 없다. 20-F 손익계산서와 대조해야 하며, 대조 전에는 순이익과 세전이익을 섞어 쓰지 않는다. [F36] [F48] [F44]
- [info] 코드가 Non-GAAP 대비 GAAP 신호를 만들지 않았고 근거에 Non-GAAP 조정 내역이 없다. 조정의 크기와 반복성은 확인하지 못했다. 이 회사의 조정 항목은 SBC가 가장 클 가능성이 높으므로 보고서의 조정 이익은 SBC를 되돌려 읽는다. [F64] [S22](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm)
- [info] 매출채권이 FY2023 3,158만에서 FY2025 2,364만 USD로 줄었고 매출은 늘었다. 매출채권과 매출 증가율 차이 신호(receivables_gap)는 켜지지 않았고 발생액 비율은 FY2025 2.2%다. 운전자본에서 이익을 부풀린 징후는 보이지 않는다. 재고는 근거에 없다. [F50] [F52] [F56] [C:dso@FY2025] [C:accruals_ratio@FY2025]
- [watch] 총이익률이 FY2022 46.9%에서 FY2025 15.7%로 낮아졌고 매출원가가 매출 증가보다 빠르게 늘었다. 로보택시 매출이 늘면 마진 구성이 바뀌는데 요금 징수 매출의 총액·순액 처리와 파트너 정산 구조를 확인하지 못했다. 2026년 2분기 로보택시 서비스 매출 1,210만 USD(전년 대비 +691.2%)가 이 정책에 따라 크게 달라질 수 있다. [F26] [F29] [F6] [F9] [F77] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [C:gross_margin@FY2025]
- [watch] 감사의견, 계속기업 의문 문단, 핵심감사사항, 감사인 변경 여부를 근거에서 확인하지 못했다. 코드의 restatement·auditor_change 신호는 켜지지 않았지만 외국 민간발행인이 제출하는 6-K에는 8-K 항목 4.01·4.02가 없어 이 신호가 작동했는지 확신할 수 없다. 20-F(S22)에서 직접 확인해야 한다. 순현금이 11.7억 USD이고 FY2025 OCF 유출이 1.6억 USD여서 계속기업 위험은 낮아 보이지만 감사의견으로 확인한 것은 아니다. [S22](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm) [F40] [C:net_cash@FY2025]
- [info] 특수관계자 거래, 고객·파트너 집중도, 연결·별도 차이, 이중의결권 구조는 근거에 없다. 중국 기반 사업이므로 변동지분실체 구조와 현지 파트너 거래는 20-F에서 별도로 확인해야 한다. 지금은 문제를 발견한 것이 아니라 확인하지 못한 항목으로 둔다. [S22](https://www.sec.gov/Archives/edgar/data/1969302/000110465926046406/pony-20251231x20f.htm)
- [info] 2026년 2분기 순손실 약 $45.4M, 현금 약 $1.39B, OCF 약 $44M 유출은 제3자 요약(S53)에만 있어 6-K 본문으로 확인되지 않았다. 이 숫자는 판단 근거로 쓰지 않았다. 주가는 기준일보다 오래된 2026-09-22 값이라 시가총액 기반 지표는 낡았다. [S53](https://transcripts.platformaeronaut.com/summaries/PONY-2Q26-AI-Summary) [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [F74]

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 유럽·해외 확장이 규제 승인 지연과 현지 경쟁으로 막히고, 2분기 +68.8% 가속이 차량 판매·라이선스 같은 일회성 매출에 의존한 것으로 드러난다. 연말 3,500대 목표를 놓치고 성장률이 한 자릿수~십대로 꺾이면 EV/매출 17.82x를 정당화할 근거가 사라지고 멀티플이 8배 안팎으로 압축된다. 주가는 성장이 아니라 배수 붕괴로 −60%가 된다. [C:ev_revenue] [F76] [F79] [F78] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm) [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5)
- (25%) 규모가 커져도 단위경제가 개선되지 않는다. 차량 원가, 안전요원·원격운영 인력, 충전·정비, 파트너 수수료를 빼면 서비스 매출 총이익률이 낮은 수준에서 정체하거나 음수가 된다. 총이익률은 FY2022 46.9%에서 FY2025 15.7%로 내려왔고 차량당 매출·원가 공시가 없다. 차량이 늘수록 영업현금 유출이 커지고 흑자 전환 서사가 무너져 시장이 성장에 대한 지불 의사를 거둔다. [C:gross_margin@FY2022] [C:gross_margin@FY2025] [C:operating_margin@FY2025] [F40] [S54](https://www.sec.gov/Archives/edgar/data/0001969302/000110465926098113/tm2623382d1_ex99-1.htm)
- (20%) 자본 조달과 희석이다. 영업현금 유출(FY2025 −1.6억 달러)에 차량·해외 확장 투자가 더해져 현금 소진이 빨라지고, 주가가 낮을 때 증자나 전환사채로 조달한다. 주식 수는 FY2025 말 4.335억에서 이미 늘었고 SBC는 매출의 34.2%다. 시총 27.7억 달러에서 신주 발행이 반복되면 주당 가치가 시총 변화보다 더 빠르게 줄어 −60%가 된다. [F40] [F65] [C:sbc_to_revenue@FY2025] [C:dilution] [C:net_cash@FY2025] [C:market_cap]
- (15%) 플랫폼 파트너 의존과 지정학이다. 수요 접점이 Uber 같은 플랫폼에 있어 Pony는 기술·운영 공급자로 마진을 나눠야 하고, 파트너가 다른 자율주행 업체를 병행하면 협상력이 약하다. 여기에 중국 기반 사업에 대한 미국·유럽의 데이터·보안 규제나 상장 지위 압박이 겹치면 해외 배치가 멈추고 파이프라인 4,000대가 계획으로만 남는다. 해외 비중이 성장 서사의 핵심이라 한 번의 규제로 서사가 꺾인다. [S34](https://news.google.com/rss/articles/CBMinwFBVV95cUxQQkpUaUFJdDNySDFnenkzQmFVRVV5cTktN0ZSakp5enc0UFp2T3VWc0lHU2taWHFCTV9uRmMwSUpKTU1vYTc1Q2YwbzZsYk5FcVE1bWtCVmZnRmRwbUFObmJoRHlzRnBqajRBQ1RzZHBwSTRrSlBpSkJUT3dFemQ5dkRzbzJqdWczWHo2S0wwaUpIX194cU44RGFTeWtLZjTSAaQBQVVfeXFMTm1FdkFRcy1fQzRXNlVUdHJmTDZaYVZiYjJ1MElheWpXejI0bnBpZ2JNcS0wNC0ySkczMVFJcHBRMFVvZHF5TWVVSnEyN0F0N2thbmRYbVhtaE1NTXg0Q29MUFNvVGtEblVvLUViQ2xXb1VIdEFfMzBPNF91WkF1eTNYdUZyWXpBS296X09HVTFidlNOVDAtcWpZTm52bG9PeXgzZ2E?oc=5) [S43](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPOTFjbGtTXzEyN0FWNms5M1Z5ZnlDZXA1Qlktd3ZFOWk3N01FQXNPdFlNaFBRNGotM295YkhCWkh5WDh5WjByaUc3MlN4N3hnYTlVVlB6SW81elB0M0dFeldIcFMyQ2ZkQTFvVjFpMlNVd3otMVJFWlpjTGlOMW5LWVNtOUJreDNhNjBvRXY3cV9sMDAzMGE0djRCWUJwTnp2Y3pXVkVYemdaS00?oc=5) [S50](https://news.google.com/rss/articles/CBMimgFBVV95cUxPWm94c24xeGcyMlA5MGZnNE8zWmJqX0JaU1YyV3Jqb1Q2VGJwaGJ1Q2NjNG5QZnBweHpGdkRWUjFxUWFqMG1HYWtzNEtkQzdSZVpzUDlqTm5uZk1EZmpXV3BuUHRIaXg0Z3JRZjJHWlVHSWl0d2EzTm00QWhKODVoeDhqTG5DSnBraEpCMG5MZjVFcmpRdEJiWlh3?oc=5) [S37](https://news.google.com/rss/articles/CBMimAFBVV95cUxPRWphNWlOMkMwRUJyX1RPVGJOeTRaOHJBQi1YcUZtcXNnZUMtNDVDb3FBV3JkV01zWjZvN1czbUxlaDk0bVFoTV80cUg5UGE3OTRaLTZ3SkhBNjZkbXZPZnZxQ3Z2LWxrcG5IdUNSRVk5MGJUVlpQdGZQUjNfbmFlMFBuMllqcHF4MHBaZ0ZYZ2hSRGtEeDRfNA?oc=5) [C:ev_revenue]
- 약한 가정 `base.exit_multiple`: 기본 시나리오 출구 배수 22는 5년 뒤에도 EV/매출 17.82x에 가까운 배수가 유지된다고 가정한다. 이 배수는 성장률이 여전히 25%인 시점에서 흑자 전환이 끝난 기업에 주는 값인데, 현재 총이익률 15.7%에서 FCF 마진 8%로 가는 경로는 공시된 단위경제 없이 추정일 뿐이다. 성장이 둔화하고 마진이 확인되지 않으면 배수가 먼저 줄어든다. [C:ev_revenue] [C:gross_margin@FY2025] [C:base_rate@base]
- 약한 가정 `base.fcf_margin`: FCF 마진이 현재 영업이익률 −289.8%에서 5년 안에 +8%로 가는 가정이다. 총이익률이 15.7%에서 정체한 이력(FY2023~FY2025)과 FY2025 영업현금흐름 −1.6억 달러, R&D 2.2억 달러 규모를 고려하면 매출이 수십 배로 늘어야 겨우 닿는 값이다. 기저율상 이 정도의 마진 전환은 드물다. [C:operating_margin@FY2025] [C:gross_margin@FY2025] [F40] [F60] [C:base_rate@base]
- 약한 가정 `base.revenue_growth`: 5년 평균 매출 성장 약 40%대의 경로는 FY2023~FY2024 성장률 4~5%에서 한 분기의 +68.8% 가속으로 외삽한 것이다. 소규모 기저와 일회성 차량·라이선스 매출 비중이 확인되지 않았고, 연간 성장은 FY2025에 20.0%였다. 한 분기 데이터로 5년 고성장을 가정하면 기저율에 비해 과도하다. [F76] [C:revenue_growth@FY2023] [C:revenue_growth@FY2024] [C:revenue_growth@FY2025] [C:base_rate@base]

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
| SBC (sbc) | 1,318만 USD | 325만 USD | 1.3억 USD | 3,080만 USD |
| SBC/매출 (sbc_to_revenue) | 19.3% | 4.5% | 169.3% | 34.2% |
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
| 주가 (price) | 7.29 USD/ADR (2026-09-22, F74) → 주당 7.29 USD |
| 희석 주식 수 (shares) | 3.8억 |
| 시가총액 (market_cap) | 27.7억 USD |
| 순현금 (net_cash) | 11.7억 USD |
| EV (ev) | 16.0억 USD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 17.82x |
| PER (pe) | — |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 34.2% > 10%
- [watch] deferred_revenue (C:deferred_revenue): 매출은 늘었는데 이연매출이 10% 넘게 줄었다 — 매출 당겨쓰기 의심
- [watch] dilution (C:dilution): 희석 주식 수 연 64.5% 증가 > 3%

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull", "years": 10, "revenue_growth": [0.8, 1.0, 0.8, 0.6, 0.5, 0.4, 0.3, 0.25, 0.2, 0.15], "fcf_margin": 0.22, "exit_multiple": 25, "share_change": 0.03}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "base"}: price=7.3, leveraged=아니오

### 계산 경고

- 주가 기준일 2026-09-22이 as_of(2026-10-18)보다 26일 오래됨
- 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

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

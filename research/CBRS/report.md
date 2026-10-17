# Cerebras Systems (CBRS) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 모델** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✗ model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

## 1. Variant perception

- 시장이 반영한 것: 시장은 RPO 254억 USD(F52)와 600MW 용량(F53)을 대부분 매출로 바뀔 것으로 보고, 주가를 EV/매출 26배 수준(C:ev_revenue)에 두고 있다. 주가는 출처마다 달라(F40, F61) 이 해석은 확인이 필요하다.
- 우리가 다르게 보는 점: RPO는 수요 신호이지만 인식 시기와 고객 구성, 해지 조건이 확인되지 않았다. 따라서 매출 가시성의 증거로 쓰지 않고, 본 모델은 5년 성장이 기저율상 드문 구간에 있다고 본다. core와 GAAP의 총이익률 격차(F50, F51)가 설명되지 않은 채 가이던스와 2027 목표가 모두 core 기준이어서, 마진 개선 경로가 가격에 과대 반영됐을 가능성이 있다.
- 왜 우리가 맞는가: 3분기 core 총이익률 가이던스(F57)가 2분기 실적(F50)보다 낮고, 2분기 GAAP 매출은 컨센서스를 밑돌았다(F58, F33). 2027년 목표(S29)로 가는 경로가 근거에 없다. 반대로 core 매출 가이던스가 상향됐고(F54, F55) 클라우드는 기대를 웃돌았다(S30). 그래서 확률을 약세 쪽에 조금 더 두면서도 상방을 닫지 않았다. [F52] [F53] [F50] [F51] [F57] [F58] [F33] [F54] [F55] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [S30](https://www.newsquawk.com/headlines/cerebras-cbrs-q2-2026-usd-revenue-1801mln-exp-194mln) [F40] [F61]
- 촉매: 3분기 실적에서 GAAP 대 core 총이익률 격차의 구성이 공개되고, RPO의 연도별 인식 비중과 고객 구성이 10-Q에서 확인될 때.
- 시점: FY2026Q3 실적 발표(2026년 11월 전후)부터 FY2026 10-K까지.

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 분석 모듈 (L4)

### 사업·산업 — unclear

Cerebras sells AI inference and training systems built on its own wafer-scale chip. Revenue comes from hardware sales (CS-4 systems, S8) and from a cloud service that rents the capacity back out. FY2025 revenue was $510M, up 75.7% from $290M (C:revenue_growth@FY2025), and the top two customers made up 86% of FY2025 revenue (F48). In Q2 2026, GAAP revenue was $180.1M and core revenue was $209.9M, up 103% (S29). Gross margin is split: core is 41% and GAAP is 14% (F50, F51), and the cause of the gap is not documented. The remaining performance obligations of $25.4B (F52) and the 600MW of contracted data center capacity (F53) show large future demand. They also show a shift toward a capital-heavy cloud model, with a $420M quarterly capex figure (F62). Unit economics cannot be assessed because CAC, churn and cohort data are missing. Customer concentration is the main weakness in the business.

- [customers] The top two customers accounted for 86% of FY2025 revenue (F48), and the S-1 reporting links them to G42 and MBZUAI. Revenue depends on very few counterparties. The concentration may have eased in 2026, but the evidence does not show this. [F48] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- [unit_economics] Core gross margin was 41% (F50) against GAAP gross margin of 14% (F51) in Q2 2026. FY2025 gross margin was 39% (F47). The gap between core and GAAP margin has not been explained. Core excludes items that GAAP includes, and the filing needs to be read to see which ones. Core margin of 41% is not clearly higher than the FY2025 level of 39%. [F47] [F50] [F51] [S2](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrs-20260812.htm)
- [unit_economics] Q3 guidance calls for core revenue of $214~216M and core gross margin of 38~40% (F56, F57). The consensus of $211.9M before guidance (F59) is slightly below that. Core margin is guided below the 41% reported in Q2, so there is no sign yet of margin expansion. [F56] [F57] [F59] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- [industry] Q2 GAAP revenue of $180.1M missed the consensus of $194M (F58). Hardware was weak and cloud beat estimates (S30). The stock fell 14~16% after the report (S9, S20). This suggests the market is giving less weight to the hardware business and more to cloud, but the cloud and hardware split is not in the facts. [F58] [S9](https://news.google.com/rss/articles/CBMingFBVV95cUxPS3RxTUJxMTh2Mk9XSmgxdm1MZDh6MlRtcVl5aFM1bmF1ajVmWlFnUF9nNU0yYjloQ0pON2VSWFZBYTVldmJ0TGI5N2psYlcwZVRuSURZaUM1NkYzVkh4NGVNRUtjd0F0M3RMTno2X0RSNG9VbF91V2lDOUh0OG5nSDJiY2M4cDdrM1lGRnNicldnNXBBQTBDRFVzNHdJQQ?oc=5) [S20](https://news.google.com/rss/articles/CBMif0FVX3lxTFBJcHVySkhhUXc0UTFTUU44MC1zazJYSFpyMVRkdy1MUG5QSDBOX1dkVmstdi1VWVBZTm91U2ZXYzhXZmlzUlAzT2NNdExXMVZ6eWdyQkQ0eFA0UzU3amczTzYxQkthMTRWOXJGRjZ0bzQyT2F6b1pGbFMwN1hHcTDSAYQBQVVfeXFMTlk2ekExUzkydDVRQ1E3elduc0F5c08tUklVMFJBazUyS1lEZml4alVXSTdxYWpSdVdiVEFuVnMtVnFSTnNOWjZsaldlUlFyMnBEU0pWbkFJektITkdWSnItZS05aFBfRm94X1ZOV1J0Y3FIdXBUdklRLWZJSktrekxYRG8x?oc=5) [S30](https://www.newsquawk.com/headlines/cerebras-cbrs-q2-2026-usd-revenue-1801mln-exp-194mln)
- [runway] RPO is $25.4B (F52), and deferred revenue is only $170M (F12, 1.7억). The backlog is recognized over a long period, and the timing, customer mix and termination terms are not known. OpenAI and AWS contract sizes are also not found. The backlog is therefore a signal of demand and cannot be used as a forecast of revenue. [F12] [F52] [S24](https://news.google.com/rss/articles/CBMikgFBVV95cUxOalM0ejc1WHVWb29zVVZRdEFSVm5aeWhSUDVLVjlUZDAyc1Y2LWhfa1RTTVNXYVM2ZzRSY0Q3cW1pdDN2Q21FeWYybUNwLWRtMl9reTVyb1RDSDdCTmxBRXlselNHTUtfdTY4eG15WDVWQzJxRWxOVlNQdFo1WkRwMkZwQmRKQkotR0xaYlRZc1l1Zw?oc=5)
- [runway] Cash was $6.74B at the end of Q2 (F3, 67.4억) and equity was $9.15B (F16, 91.5억), both well above the Q1 levels of $1.72B (F2) and -$190M (F15). The increase follows the May IPO. Q2 capex was $420M (F62) and operating cash flow was -$59.82M (F64). Building out the cloud capacity is funded by IPO money for now. [F2] [F3] [F15] [F16] [F62] [F64] [S1](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm)
- [industry] The competitors are NVIDIA and AMD, but no share data or competitor margin comparison was collected. Management says 2026 core revenue will be $880~890M, raised from $855~865M (S29). The market position cannot be judged from the evidence, which holds only company guidance and press coverage. [F54] [F55] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- [claimed] The wafer-scale chip architecture and the CS-4 launch are positioned as the fastest AI inference (S8, S15). The sources are Cerebras's own announcements and press coverage. No third-party benchmarks, share data or price-retention records are in the evidence. [S8](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBmMUQxb0dVSUo2UzM1MVE2dExHRlRYUlg2QW1GSktqeTd0WmVldXpKaVFIVUxaWVpwQ0RpQlpnYjBUZWJ4ZmZBWHowMzlRQkdPV0E3VzE3VkxfdjJtUmNBNFE1dFI?oc=5) [S15](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNjNfbnRoZFloVUFkdDZxWUppbzg1ejVBcTIxVGVxQXZOS0hNZFdPVi02UFVGdU1oR0NPWjBrelZnUnY2bHFDSm1hdDl2a0JDNnBWNV9YQ2ZyT21nOWt6TTdFZjZNMm4tMVUzX3lYQy1QMzMwbmNuSmFZalQycjNZQlhFSTRfa2RYeHVFUnFXSGs0aGRMNGVSOGRR?oc=5) [S32](https://news.google.com/rss/articles/CBMijAFBVV95cUxOcUpZSVhkNDcyU0lXNWx4WHF0ZTRweFE2N3pvbU5URlU4SjQtQVRXekhGV0t4TFVWa1A1YTY1U2pwRGExR3EydjI4U3E4ZTRDZzZaX2VMVjhWUXVNUWJBNnBYcmRrYmhmRm5pc3lxcUlVaGp4OG1qUVl1Ym1aa3BDVHlyYWdWRzF1RkpUaA?oc=5)
- [claimed] Contracted data center capacity of 600MW (F53) and a $25.4B backlog (S24) suggest scale, and management says core gross margin is moving toward the 60% range in 2027 (S29). That target is a company statement and has not been shown in results. Core gross margin of 41% in Q2 is above the Q3 guidance of 38~40% (F57), so the near-term trend is flat to slightly down. [F53] [F57] [S24](https://news.google.com/rss/articles/CBMikgFBVV95cUxOalM0ejc1WHVWb29zVVZRdEFSVm5aeWhSUDVLVjlUZDAyc1Y2LWhfa1RTTVNXYVM2ZzRSY0Q3cW1pdDN2Q21FeWYybUNwLWRtMl9reTVyb1RDSDdCTmxBRXlselNHTUtfdTY4eG15WDVWQzJxRWxOVlNQdFo1WkRwMkZwQmRKQkotR0xaYlRZc1l1Zw?oc=5) [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- [claimed] The partnerships with AMD (disaggregated inference) and Gimlet Labs show ecosystem expansion (S18, S16). No record of retention, repurchase or price increases at the customer level was found, so switching costs are unproven. [S16](https://news.google.com/rss/articles/CBMirgFBVV95cUxOMDgtbmhLenNVQVdOQXJDbmJmck52THdJR3BYWV8zeXdjRFdieFdIdUNlTTNreWNWSy1obHdabzhtakNsQldBeGF6Y0RwLTQ0ZVRzZy11UkFycEx6azI0dWM1enN5NkdHTEg3N1VhajVFZEFqMmlKblo3Y2Zmam1wUTNLS3ZNYTd2b2MxdWNVQzJtdklpVV92WS1wZllQVGVBak9mUEdkeldoWFZRWFE?oc=5) [S18](https://news.google.com/rss/articles/CBMiywFBVV95cUxQSGxfRjlGZUZfR1hack0zbEdZcVJXY1JCaWw4dl9fMFZnQnJHVnVfU3NsZkpVd2hPbjh5Q0dHTVcxYTByelU2b3lMUzVDNk54ZFN4OG1VSko2MXEzV0d3bDdHSTJiRHlrMFZtallYSllLUzdSQ2lVdDVra2ZqY0xPaEV2cmxRaXRIWnhRd19obk82eFBGQXQ1YnpYc2hLY0poOGVsdS1yZ19mVGs0RlFVZ1diV0luRktiNV9Uc05vSHpEbmViQ1NjX1h1UQ?oc=5)

### 경영진·자본배분 — mixed

경영진이 주주와 같은 방향을 보는지 판단할 근거가 부족하다. 보상 지표(DEF 14A), 내부자 매매, 락업 해제 일정, 가이던스 적중 이력은 수집되지 않았다. 확인되는 것은 세 가지다. 2분기 SBC가 3.8억 USD로 직전 분기 959만 USD에서 급증했다. IPO 이후 가중 희석주식수가 6,281만에서 1.5억으로 늘었다. 경영진이 core 기준(조정) 지표를 앞세워 설명한다. 2026 core 매출 가이던스는 상향됐지만 2분기 GAAP 매출은 컨센서스를 밑돌았다. 상장 후 콜이 두 번뿐이라 신뢰도는 입증되지 않았다. 공개된 2027 목표(매출 3배 이상, core 총이익률 60%대)는 정량 범위가 없는 회사 발언이다. 이 때문에 '혼재'로 두되, 정렬 여부는 판정을 유보한다.

- [compensation] 근거 없음. DEF 14A 보상 지표(장기 지표 대 단기 EPS·조정 EBITDA), 베스팅 기간, 창업자 보상 구조를 찾지 못했다. 경영진이 core 매출총이익률 41%와 GAAP 14%를 병기해 설명하므로 보상이 어느 쪽 지표에 연동되는지가 핵심 미확인 사항이다. [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [F50] [F51]
- [insider] 근거 없음. 창업자·경영진 지분율, 최근 내부자 매수·매도, IPO 락업 해제 일정은 수집되지 않았다. 시장 수치만 있고 지분 구조 정보는 없다. 주식수 자체도 출처마다 달라(1.51억 대 2.196억) 지분율 계산의 분모조차 확정되지 않았다. [S28](https://www.fool.com/quote/NASDAQ/CBRS) [F41]
- [guidance] 2026 core 매출 가이던스는 6월 23일 발표분 8.55억~8.65억 USD에서 8월 12일 8.8억~8.9억 USD로 상향됐다. 상향 이후 3분기 core 매출 가이던스는 2.14억~2.16억 USD이다. 상향 전 컨센서스는 3분기 2.119억 USD, 2026 연간 8.634억 USD였다. 다만 2분기 GAAP 매출 1.8억 USD는 컨센서스 1.94억 USD를 하회했고 보도에서 하드웨어 부진이 지적됐다. 가이던스가 core 기준이라 GAAP 부진과 직접 비교되지 않는다. 가이던스 대비 실적 이력은 상장 후 콜 2회뿐이어서 적중률(C:guidance_hit_rate)을 신뢰할 수 없다. [S4](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044941/cbrs-20260623.htm) [S2](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056186/cbrs-20260812.htm) [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [S30](https://www.newsquawk.com/headlines/cerebras-cbrs-q2-2026-usd-revenue-1801mln-exp-194mln) [F54] [F55] [F56] [F59] [F60] [F58] [F33]
- [guidance] 경영진의 2027년 목표(매출 3배 이상, core 총이익률 60%대 이상)는 2차 요약 기반의 정성 발언으로, 정량 범위와 조건이 없다. 3분기 core 총이익률 가이던스는 38~40%로, 2분기 core 41%보다 낮다. 60%대 목표와의 간극을 메울 경로는 근거에 없다. [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [F57] [F50]
- [dilution] SBC가 1분기 959만 USD에서 2분기 3.8억 USD로 늘었고, 같은 기간 매출 대비 비중이 급격히 커졌다(2분기 매출 1.8억 USD). IPO 연계 일회성 인식일 가능성이 있으나 성격은 확인되지 않았다. 가중 희석주식수는 6,281만에서 1.5억으로 늘었고, 일부는 IPO 시점 효과이다. 기말 주식수는 2.196억으로 추정되나 10-Q 표지로 확인이 필요하다. 자사주 매입 근거는 없어 희석을 상쇄하는 장치가 보이지 않는다. [F36] [F37] [F13] [F14] [F33] [F41] [S28](https://www.fool.com/quote/NASDAQ/CBRS)
- [capital_allocation] IPO 후 현금이 1분기 17.2억 USD에서 2분기 67.4억 USD로 늘었고 자기자본은 -1.9억 USD에서 91.5억 USD로 전환됐다. 부채는 3.6억 USD에서 1.8억 USD로 줄었다. 반면 단기 부채(debt_current)는 6.2억 USD에서 7.4억 USD로 늘어 구성이 엇갈린다. 조달 자금의 사용처가 핵심이다. 2분기 capex는 4.2억 USD로 1분기 1.3억 USD의 몇 배이고, 영업현금흐름은 1,234만 USD에서 -5,982만 USD로 악화됐다. 재투자 수익률은 아직 입증되지 않았다. [F2] [F3] [F15] [F16] [F7] [F8] [F9] [F10] [F1] [F62] [F25] [F64]
- [capital_allocation] 계약된 데이터센터 용량 600MW와 RPO 254.0억 USD는 대규모 선투자 의지를 뜻하지만, RPO의 인식 시기·고객 구성·해지 조건은 확인되지 않았다. 상위 2개 고객이 FY2025 매출의 86%를 차지하는 집중도는 경영진의 고객·계약 선택의 위험을 보여준다. G42·MBZUAI 특수관계 여부는 미확인이다. [F53] [F52] [F48] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- [capital_allocation] M&A, 배당, 자사주 매입 이력은 근거에 없다. 비싼 인수나 고점 자사주 매입 여부는 판단할 수 없다. 주가 출처가 서로 달라(10월 13일 175.44 USD, 10월 16일 127.21 USD) 상장 후 주가 흐름에 대한 경영진 행동의 평가도 보류한다. [F40] [F61] [S27](https://weissratings.com/en/instant-news-alerts/cerebras-systems-inc-cbrs-down-4-8-time-to-cash-out) [S31](https://finance.yahoo.com/quote/CBRS/history/)

### 회계 품질 — watch

코드가 계산한 회계 신호는 없다. 다만 신호가 없는 것은 입력이 부족해서일 수도 있다. FY2025 ocf·capex와 TTM 분기 값이 비어 있어 ocf/순이익, 발생액, 매출채권·재고 격차 같은 신호는 계산되지 않았다. 직접 확인한 결과 조정해서 봐야 할 숫자가 여럿 있어 'watch'로 판정한다. (1) 2분기 SBC 3.8억은 순손실 -4.5억의 대부분이고 IPO 연계 일회성 성격이 강해, GAAP 손익은 SBC를 분리해서 봐야 한다. (2) core 매출총이익률 0.41과 GAAP 0.14의 차이가 매우 크고, core 매출(2.1억)이 GAAP 매출(1.8억)보다 크다. 조정 내역은 아직 확인되지 않았으며, 이것이 이번 판정의 가장 큰 불확실성이다. (3) 상위 2개 고객이 FY2025 매출의 0.86이고 G42·MBZUAI 특수관계 가능성이 있다. (4) 매출은 1분기 대비 줄었는데 매출채권은 2배 가까이 늘었다. 지금 증거로는 '숫자를 믿을 수 없다'는 red_flag 근거(정정·감사의견 한정·ocf 음수 흑자)가 없으나, 감사의견·감사인·정정 이력은 아직 확인되지 않았다. core 조정 내역과 특수관계 거래가 확인되면 등급을 다시 봐야 한다.

- [watch] 2분기 core 매출총이익률 0.41, GAAP 0.14로 차이가 매우 크다. core 매출(2.1억)이 GAAP 매출(1.8억)보다 크다. 조정 항목(고객 대상 워런트·계약 자산 상각, 일회성 매출 차감 등)의 구성과 반복성이 아직 확인되지 않았다. 가이던스와 2027년 '60%대' 목표가 모두 core 기준이라, GAAP이 아닌 core를 근거로 한 밸류에이션은 이 차이를 해명한 뒤에만 신뢰할 수 있다. [F50] [F51] [F49] [F33] [F57]
- [watch] 2분기 SBC 3.8억은 1분기 959만에서 급증했고, 순손실 -4.5억과 영업손실 -4.8억의 대부분을 설명한다. IPO 시점에 충족된 RSU 조건에 따른 일회성 인식으로 보이나 확인되지 않았다. 2분기 R&D 3.2억도 같은 이유로 급증했을 가능성이 크다. 반복되는 영업 성과로 보지 말고 SBC를 뺀 영업이익·현금흐름으로 봐야 한다. 2분기 ocf -5,982만은 분기 값을 누적에서 차감해 만든 값이므로 10-Q 원문과 대조해야 한다. [F37] [F36] [F24] [F27] [F35] [F34] [F64]
- [watch] 상위 2개 고객이 FY2025 매출의 0.86를 차지한다. G42·MBZUAI와의 특수관계 여부, 계약 조건, 회수 가능성이 확인되지 않았다. 특수관계 거래라면 매출 인식과 가격의 독립성을 별도로 검증해야 한다. [F48] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- [watch] 2분기 매출은 1분기보다 줄었는데 매출채권은 1분기보다 크게 늘었다. 재고는 줄었고 이연매출은 소폭 늘었다. 이 매출채권 증가가 대형 고객 청구 시점 때문인지 회수 지연인지 확인되지 않았다. 코드 신호(receivables_gap)는 연간 기준 매출 성장률이 없어 계산되지 않았으므로 이 관찰이 신호를 대신한다. [F30] [F31] [F32] [F33] [F21] [F22] [F11] [F12]
- [watch] RPO 254.0억은 연 매출(FY2025 5.1억)에 비해 매우 크다. 인식 시기, 고객 구성, 해지 조건이 확인되지 않아 이를 매출 가시성의 증거로 쓰면 안 된다. 기간별 인식 비중이 확인될 때까지 '입증되지 않은 수치'로 취급한다. [F52] [F42]
- [info] FY2025 Non-GAAP 순손실(-7,570만)과 보도된 GAAP 순이익(S-1 2차 보도에서 일회성 비현금 이익 언급)의 부호가 반대다. 비현금 일회성 이익 때문으로 보이나, 보도마다 수치가 달라 사실에 넣지 않았다. S-1 원문의 이익 구성을 확인해야 한다. FY2025 GAAP 이익은 영업 성과로 읽으면 안 된다. FY2025 영업이익은 -1.5억이다. [F45] [F44] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- [info] 2분기 희석 주식 수(1.5억)는 5월 IPO 이전 구간이 섞인 가중평균이라 기말 주식 수보다 작다. 시장 자료의 발행주식수(2.1961e+08)와 주당 지표를 섞어 쓰면 오류가 난다. 주가도 출처마다 달라(175.44 대 127.21), 가격 의존 지표는 확인 전까지 신뢰하기 어렵다. 이는 회계 문제는 아니나 per-share 계산의 신뢰도 문제다. 또 장기 부채(F8)와 단기 부채(F10) 분류가 1분기와 2분기에 크게 달라, 차입 구조를 10-Q 주석으로 확인해야 한다. [F14] [F41] [F40] [F61] [F8] [F10]
- [watch] 감사인, 감사의견(계속기업 의문·핵심감사사항), IPO 전후 재무제표 정정, 내부통제 약점 공시가 모두 확인되지 않았다. 8-K에 재무제표 정정(4.02)이 있다는 정보는 없으나 이는 부재의 증거가 아니라 미확인이다. 이 항목이 확인되기 전에는 'clean'을 줄 수 없다. [S1](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm) [S5](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035605/closing8-k.htm) [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 고객 집중이 현실화됐다. 상위 2개 고객이 FY2025 매출의 86%였고 G42·MBZUAI 연계로 보도됐다(F48, S6). 이 중 한 곳이 발주를 미루거나 줄이면 매출이 바로 꺾인다. 600MW 용량과 선투자 capex는 이미 확정되어 가동률이 비고, 고정비가 남는다. 2분기 GAAP 매출은 1분기보다 줄었고 컨센서스를 밑돌았다(F33, F32, F58). 5년 뒤 매출 성장이 기대에 못 미치면 26배 수준의 EV/매출이 크게 낮아진다. [F48] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm) [F33] [F32] [F58]
- (20%) core와 GAAP의 총이익률 격차가 구조적이었다. core 41%와 GAAP 14%의 차이(F50, F51)는 고객 대상 워런트·계약 자산 상각 같은 반복 비용일 수 있다. 2027년 '60%대' 목표는 core 기준 회사 발언일 뿐이고(S29), 3분기 core 가이던스는 38~40%로 2분기보다 낮다(F57). 하드웨어 가격 경쟁과 클라우드 믹스 확대로 core 마진이 오르지 않고 GAAP 마진도 회복되지 않는다. 시장이 core 기준 마진 개선을 가격에 넣었다가 GAAP 기준으로 재평가하면서 배수가 무너진다. [F50] [F51] [F57] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- (20%) 클라우드 전환의 자본 부담이 현금을 소진했다. 2분기 capex는 4.2억 USD로 1분기의 몇 배였고, 영업현금흐름은 양수에서 음수로 바뀌었다(F62, F1, F64, F25). 600MW 용량 확충(F53)은 선투자를 계속 요구한다. 가동률과 단가가 따라오지 않으면 IPO로 들어온 현금 67.4억 USD(F3)가 줄고 추가 차입이나 증자가 필요해진다. 단기 부채도 이미 늘었다(F10, F9). 증자와 SBC 희석이 겹쳐 주당 가치가 크게 줄어든다(F37, F14). [F62] [F1] [F64] [F25] [F53] [F3] [F10] [F9] [F37] [F14]
- (15%) RPO 254억 USD가 매출로 전환되지 않았다. 5년 매출(FY2025 5.1억 USD, F42)에 비해 RPO는 지나치게 크고(F52), 인식 시기·고객 구성·해지 조건이 확인되지 않았다(리서처 공백). 이연매출은 1.7억 USD에 그친다(F12). 일부 계약이 변경·해지·연기되면 backlog가 줄고, 시장이 backlog를 근거로 준 프리미엄이 사라진다. 상장 후 주가가 이미 52주 고점에서 절반 넘게 빠졌다는 보도(S19, S27)는 신뢰 약화가 시작됐다는 신호일 수 있다. [F52] [F42] [F12] [S19](https://news.google.com/rss/articles/CBMinwFBVV95cUxOT2FhTUFkZVhBM1RBdm1vS2VXdlpudndaVVNvcTIzSnhXNVRGRHRNYjROZlV5OXNXUmFTZDVsTDQ0Sm93QWhnZ2RQemlDcURXS090a0xOVWJKSlBXMFdlUkg0aERSQWY4UXo4WlBQbFdmOURsdmU1Y3luUnh2eXJSU2VkUFZQd1JnT19zUlB3R08wQ0tqcVZtc1JvdG9venc?oc=5) [S27](https://weissratings.com/en/instant-news-alerts/cerebras-systems-inc-cbrs-down-4-8-time-to-cash-out)
- 약한 가정 `base.fcf_margin`: base의 FCF 마진 가정은 분기 capex 4.2억 USD(F62)와 영업현금흐름 -5,982만 USD(F64)의 현재 흐름과 거리가 멀다. 클라우드 모델은 가동률이 확인되기 전까지 FCF가 흑자로 돌아선다는 증거가 없다. FY2025 영업이익률도 -28.6%(C:operating_margin@FY2025)였다. [F62] [F64] [C:operating_margin@FY2025]
- 약한 가정 `base.exit_multiple`: 출구 배수 가정은 core 마진 개선이 실현된다는 전제에 기대는데, core 총이익률의 3분기 가이던스(F57)는 2분기(F50)보다 낮고 GAAP 총이익률은 14%(F51)에 머문다. 현재 EV/매출도 26.24배(C:ev_revenue)로 이미 높다. 그 위에 높은 출구 배수를 얹는 것은 마진 개선과 매출 성장이 모두 맞아야 성립한다. [F57] [F50] [F51] [C:ev_revenue]
- 약한 가정 `base.revenue_growth`: 2027년 65% 성장은 경영진의 '3배 이상' 목표(S29)를 할인해 반영한 것이지만, 상위 2개 고객 집중(F48)과 미확인 RPO(F52)가 풀리지 않은 상태에서 이 성장의 근거는 회사 발언뿐이다. 2분기 GAAP 매출은 컨센서스를 밑돌았다(F58). [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [F48] [F52] [F58]

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2024 | FY2025 |
|---|---|---|
| 매출 (revenue) | 2.9억 USD | 5.1억 USD |
| 매출 성장 (revenue_growth) | — | 75.7% |
| 영업이익률 (operating_margin) | — | -28.6% |

표에 없는 키도 인용할 수 있다: debt_total, non_gaap_net_income, operating_income

### 시장 · FY2025 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 127.21 USD/share (2026-10-16, F61) |
| 희석 주식 수 (shares) | 1.5억 |
| 시가총액 (market_cap) | 192.0억 USD |
| 순현금 (net_cash) | 58.2억 USD |
| EV (ev) | 133.8억 USD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 26.24x |
| PER (pe) | — |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "bear"}: price=127.2, leveraged=아니오

### 계산 경고

- 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

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

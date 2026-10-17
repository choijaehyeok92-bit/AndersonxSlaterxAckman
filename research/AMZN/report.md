# Amazon (AMZN) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 모델** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✗ model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

## 1. Variant perception

- 시장이 반영한 것: 주가 258.58 USD(2026-10-13)는 시가총액 약 2.82조 USD로, 시장은 매출이 컨센서스 FY2026 8,289억 수준에서 이어 늘고 capex 2,200억 이후 FCF가 회복된다는 가정을 이미 가격에 담았다. 역DCF의 시장 내재 성장(C:implied_cagr)과 우리 기본 시나리오의 대조는 calc 결과로 확인해야 한다. 3분기 컨센서스(매출 2,039억, 영업이익 254억)는 회사 가이던스 중간값(1,995억, 245억)보다 높다.
- 우리가 다르게 보는 점: 성장은 컨센서스와 크게 다르지 않다. 차이는 FCF 경로다. 시장은 영업이익 증가에 주목하지만, 우리는 capex 2,200억이 감가상각으로 손익에 번지면서 FCF 마진이 회복되는 시점과 폭이 불확실하다고 본다. 기본 시나리오의 12% 마진 도달은 가정이지 확인된 사실이 아니다. 따라서 variant는 성장이 아니라 투자 회수 속도에 있고, 시나리오 분포가 한쪽으로 쏠리지 않고 양쪽으로 넓다는 점이다.
- 왜 우리가 맞는가: 분기 감가상각이 FY2025Q1 142.6억에서 FY2026Q2 199.9억으로 늘어 투자 부담이 손익에 들어오기 시작했다. 반면 같은 기간 영업이익은 늘어 지금은 매출 성장이 상각을 앞선다. 컨센서스 capex(2,061억)보다 회사 가이던스(2,200억)가 높아 시장이 투자 규모를 아직 따라가는 중이다. 부문별 매출·AWS 수주잔고 사실이 없어 이 판단의 근거는 약하다. 이 한계를 확신도에 반영해야 한다. [F18] [F22] [F92] [F96] [F136] [F137] [F138] [F139] [F140] [F141] [F135] [F132] [S25](https://news.google.com/rss/articles/CBMifEFVX3lxTE5YU3ZKX2xoamdmZWNkOE52VGdqb3VtQTFUTXl1S0hwdWFZNGlNTE1SMGNjZlR1MXpVN2lINkVwd1VoWEdkTGFmcFItRTlxVFIyUkhwYlJCM3l5T29aYjhUM0tRSjdYNGVZY3c5eHBqVTNpVmR4aEdSTXJtd1HSAYIBQVVfeXFMTVhaMjBSNjI0eXFRb3NsNUxJNzNlalZvUjRUQkpmSFNkMGJtUVVGS19PN1JLdWpmMEdJaVVvR1B4S1dDN0NUM3dpcWRqdmxiZjdDakUzblV0TmU2QVI0UzRWNldDS3F0MC1DWGU2MUEydXV5c0lYYWI5bFA3WlJoSFhSZw?oc=5) [S45](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/amazon-postq-aws-reaccelerates-as-ai-investment-pushes-capex-higher)
- 촉매: 3분기 실적과 2027년 capex·마진 가이던스, 감가상각과 영업이익의 증가율 비교.
- 시점: 2026년 4분기 ~ 2027년 상반기

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 사실 충돌 cash FY2025: F2=5.7741e+10, F3=6.6922e+10, F4=8.681e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 cash FY2026: F5=1.01816e+11, F6=7.8213e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 d_and_a FY2025: F13=5.8562e+10, F14=6.1916e+10, F15=6.5756e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 d_and_a FY2026: F16=7.0439e+10, F17=7.52e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 debt FY2025: F24=5.0718e+10, F25=5.0742e+10, F26=6.5648e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 debt FY2026: F27=1.19074e+11, F28=1.28894e+11 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 debt_current FY2025: F30=5.005e+09, F31=3.997e+09, F32=2.748e+09 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 debt_current FY2026: F33=2.832e+09, F34=3.33e+09 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 deferred_revenue FY2025: F36=2.1662e+10, F37=2.1113e+10, F38=2.0576e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 deferred_revenue FY2026: F39=2.0887e+10, F40=2.0428e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 equity FY2025: F48=3.33775e+11, F49=3.69631e+11, F50=4.11065e+11 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 equity FY2026: F51=4.41914e+11, F52=5.5162e+11 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 inventory FY2025: F66=4.0825e+10, F67=4.1494e+10, F68=3.8325e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 inventory FY2026: F69=3.6534e+10, F70=3.8184e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 net_income FY2025: F71=7.0623e+10, F72=7.6482e+10, F73=7.767e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 net_income FY2026: F74=9.0798e+10, F75=1.35281e+11 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 ocf FY2025: F81=1.21137e+11, F82=1.30691e+11, F83=1.39514e+11 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 ocf FY2026: F84=1.48531e+11, F85=1.61403e+11 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 receivables FY2025: F98=5.7415e+10, F99=6.1175e+10, F100=6.7729e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 receivables FY2026: F101=7.5532e+10, F102=8.8092e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 sbc FY2025: F109=2.0551e+10, F110=2.0065e+10, F111=1.9467e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 sbc FY2026: F112=1.981e+10, F113=1.9314e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 short_term_investments FY2025: F121=3.5439e+10, F122=2.7275e+10, F123=3.6219e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 short_term_investments FY2026: F124=4.1273e+10, F125=4.4775e+10 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 total_assets FY2025: F127=6.8217e+11, F128=7.27921e+11, F129=8.18042e+11 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 사실 충돌 total_assets FY2026: F130=9.1663e+11, F131=1.09569e+12 — 1차 자료 우선으로 하나만 쓴다
- ⚠ 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 분석 모듈 (L4)

### 사업·산업 — unclear

Amazon은 온라인·오프라인 리테일과 3자 판매자 서비스(수수료·물류·광고), 구독(Prime), 클라우드(AWS)로 돈을 버는 복합 플랫폼이다. 부문별 매출·영업이익 사실이 이번 근거에 없어 믹스는 확인하지 못했다. FY2025 매출은 7,169.2억 USD로 전년 대비 12.4% 성장했고, 총이익률 50.3%, 영업이익률 11.2%, ROIC 22.6%를 냈다. 2026년 1~2분기에는 매출과 영업이익이 모두 늘었다. 다만 capex 가이던스가 2,200억 USD로 올라 회사는 AI·인프라 투자 확대기에 있고, 부채도 크게 늘었다. 고객 단위 코호트·이탈률·CAC 데이터가 없어 단위경제는 규모 마진으로만 간접 확인되며 '불명확'으로 둔다.

- [unit_economics] FY2025 총이익률은 50.3%, 영업이익률은 11.2%였다. 매출총이익 대비 영업이익 비중이 낮아 판관·기술·물류 비용이 큰 구조다. 고객당 경제성(CAC, 순매출유지율, 코호트)은 근거에 없어 개선·악화 판단은 보류한다. [C:gross_margin@FY2025] [C:operating_margin@FY2025] [S17](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm)
- [unit_economics] 분기 영업이익은 FY2025Q1 184.1억, Q2 191.7억, Q3 174.2억 USD였고 FY2026Q1 238.5억, Q2 274.6억 USD로 올랐다. 추정: FY2026Q2 영업이익은 전년 동기 대비 약 43% 늘었고 매출 증가율(약 20%)을 웃돈다. 영업 레버리지가 나타난 것으로 보인다. 단 부문 구성과 일회성 요인은 확인하지 못했다. [F92] [F93] [F94] [F95] [F96] [F105] [F108]
- [unit_economics] 3분기 가이던스는 매출 1,995억 USD(범위 1,970억~2,020억), 영업이익 245억 USD(범위 225억~265억)다. 컨센서스는 매출 2,039억, 영업이익 254억으로 가이던스 중간값보다 높다. 시장은 가이던스 상단 이상을 기대하고 있다. [F138] [F139] [F136] [F137] [S4](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260730.htm) [S45](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/amazon-postq-aws-reaccelerates-as-ai-investment-pushes-capex-higher)
- [runway] 2026년 capex 가이던스는 2,200억 USD이며, 메모리 비용 상승이 이유로 보도됐다. 컨센서스(2,061억)보다 높다. 재투자 활주로는 크지만(AI·클라우드 수요), 수익률은 아직 공시로 입증되지 않았다. 감가상각은 FY2026Q2 199.9억으로 FY2025Q1의 142.6억에서 늘어 투자 부담이 손익에 반영되기 시작했다. [F140] [F141] [F18] [F22] [S25](https://news.google.com/rss/articles/CBMifEFVX3lxTE5YU3ZKX2xoamdmZWNkOE52VGdqb3VtQTFUTXl1S0hwdWFZNGlNTE1SMGNjZlR1MXpVN2lINkVwd1VoWEdkTGFmcFItRTlxVFIyUkhwYlJCM3l5T29aYjhUM0tRSjdYNGVZY3c5eHBqVTNpVmR4aEdSTXJtd1HSAYIBQVVfeXFMTVhaMjBSNjI0eXFRb3NsNUxJNzNlalZvUjRUQkpmSFNkMGJtUVVGS19PN1JLdWpmMEdJaVVvR1B4S1dDN0NUM3dpcWRqdmxiZjdDakUzblV0TmU2QVI0UzRWNldDS3F0MC1DWGU2MUEydXV5c0lYYWI5bFA3WlJoSFhSZw?oc=5) [S26](https://news.google.com/rss/articles/CBMinAFBVV95cUxPYWNwWXZRNEt4SjNsc2hzSThoZ2ZSYktrQ0JZdUdLN3owZnVXRkpXVm5DSXhMTVZYTHdTWk1FWWVhUEtpWE0zWGRMaHlHdi01YXh1Sm9KNXJDUWcxVmNIT3YwWlJaM2U0dDJDQWtQWmVkeTBCWWZWMzczdy14My1NMWUzbFo0S0tDc0V3Ulg4dlVrWjNoNTFOSkpoRmc?oc=5) [S45](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/amazon-postq-aws-reaccelerates-as-ai-investment-pushes-capex-higher)
- [runway] 투자 재원은 영업현금흐름만으로는 부족해 보인다. 영업현금흐름은 FY2025 1,211.4억 USD(코드 계산값), 부채는 FY2025 656.5억에서 FY2026 1,288.9억으로 늘었다. 현금은 782.1억 수준이다. 기간 라벨이 섞여 있어 정확한 비교는 어렵지만 외부 조달 의존이 커진 방향은 분명하다. [C:ocf@FY2025] [F26] [F28] [F6] [S3](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm)
- [industry] 산업 구조와 경쟁 강도, 규제 리스크의 일부만 확인된다. FTC가 스폰서 광고 관련 소송을 제기했고 회사는 이에 대응했다. 금액 영향은 수집되지 않았다. 광고 사업이 수익성의 핵심 축일 가능성이 있지만 광고 매출 수치는 없다. [S32](https://news.google.com/rss/articles/CBMiigFBVV95cUxNN1RnMWxFWmtqTEJZNmtTNmVHdGZhUXhVbEVTenNKam8xZmtIVGNfQlYwRlY2anZ1ZXZWc1RDUW9DUFc2endnM1pOdU13c2I0RExUUGNrVFlvajZFWk8wNHZDQVdLR0JNc0wxeG1Lb05mektkVnVhejRsd1oxSG1jNGxBVWhoY2xkSHc?oc=5)
- [industry] 신규 사업 확장이 나타난다. 드론 배송 확대, 위성 인터넷(Leo) 발사 계약 추가, AWS의 DuckLabs 인수, Bee AI 제품 출시 등이다. 활주로는 넓지만 사업 범위가 넓어 자본 배분의 집중도는 낮아질 수 있다. 각 사업의 단위경제 수치는 없다. [S28](https://news.google.com/rss/articles/CBMikwFBVV95cUxQR1FIZVdwZWpWd2FwTHliRUprMC1IVl9DWnpzVmNTeTFvUHh0NEZGNFVvNGk0aHh0NFUtV0pNNjQyZFp5ZG1BZkVnYVlMQlk2ZWJOSWhvSHdPTk92SHdNN0tGWnVEV1dNcEplYzBvNVpoWl91Y2hHdnVpWF9zWDE1UUpNU2dWREVsQkxsSXRNbXhUUXc?oc=5) [S39](https://news.google.com/rss/articles/CBMihgFBVV95cUxQZktuX0V0R0x5UzdGVWJBU3dhaWxoUHBYUmtEQUxhRDBwMHdQem9MVzk0RXZlMXRCd19ZMFByMWxfZG9qd3ZGX1k4ZUNZNXhnZV9nU04tRWVFbnFSOU1QN0w3dGpmU3Zjd1FWMnFycUp6Rlp0M0pnOXRPV0VNSWtXTjlnbTVfQQ?oc=5) [S37](https://news.google.com/rss/articles/CBMiakFVX3lxTE40S2JJbEVhVWJaQUs0eUFDdTFvbjNGTFppdDRGUlVxaEhGU1BxdkZLdlU5bkp5Nk5yZWlQQlEzMUhWMDFSLU9GR21uRW8tcVFhNlltWU1rOXVQVW1qdVB4YmNFNHk5WDQzVEE?oc=5) [S31](https://news.google.com/rss/articles/CBMijAFBVV95cUxPS056WlBEQzdVTUZLVy1hUDU3cF80SVEyU0xQNDFlYmU4cG5kY0lUQnpFYlhrMEpQRWNiV1dCeTJxZmRoc2NQd3hjSkdtNGhaVWpQMlM5amdXNlNvdDY2SjdiZHc3ZVN3emNXZmlJUW9NLTJ2WVczVE01cXRwVElrR0gtSkJueWZKQzhfRw?oc=5)
- [customers] 운전자본은 고객 측 단서를 준다. FY2025 DSO는 34.5일, DIO는 39.2일이다. 수취채권은 FY2025Q1 542.2억에서 FY2026Q2 880.9억으로 늘어 매출 증가(AWS 등 기업 고객 비중 확대)를 시사하지만, 부문별 근거가 없어 추정에 그친다. [C:dso@FY2025] [C:dio@FY2025] [F97] [F102]
- [proven] 공시 재무에 규모의 흔적이 있다. FY2025 매출 7,169.2억 USD를 총이익률 50.3%, ROIC 22.6%로 운영한다. 매출은 FY2023 5,747.9억, FY2024 6,379.6억, FY2025 7,169.2억으로 커졌고 FY2025 성장률은 11.0%에서 12.4%로 높아졌다. 다만 경쟁사 대비 마진이나 점유율은 근거에 없어 해자의 깊이는 확인되지 않는다. [F103] [F133] [F134] [C:gross_margin@FY2025] [C:roic@FY2025] [C:revenue_growth@FY2025] [S17](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm)
- [claimed] Prime·셀러 도구·AWS 생태계에 의한 전환비용은 회사 보도와 제품 발표(멀티채널 관리, Seller Assistant, AI 제품 출시)로만 나타난다. 이탈률·가격 인상 후 잔존율 기록은 없다. [S36](https://news.google.com/rss/articles/CBMingFBVV95cUxQaUJEMEhNVjVhWlBoRXNvX0FlWEtZMUxyRGZXekdwR2NVcjhTSWZYd0phakF5N3N3Q3FuN2F3UV91SW9McFY3c1REZmhpTmE0NVR0RkFVT1FJSFNBWFNEX0FJV2czQ0VvOWkxY2J3U0RVUjBSV3NzQzA5eUxXTTJ3SjdBQWNwQ2dJbklNWlkwV2N6SUJfSzhwTWdaU2p3Zw?oc=5) [S40](https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ3lUWUszZ0lhaXRhM0FRb2hvTjA2QlBINWhKbEcydkpSRW5uak1jeUZfVGYxUzcyRE55SDNfZHQ0UHF3OW1ab0h4TExxTG5zMmF3YTQyZlA4NWZOVXJmNnhUZC1hb1cySzdyY0NMcURIc0JoQnRKU1puYnhULXRpbkdQLUd3R1h4WDdiSlp6THBWX2doTmFQRUgxX3U?oc=5) [S31](https://news.google.com/rss/articles/CBMijAFBVV95cUxPS056WlBEQzdVTUZLVy1hUDU3cF80SVEyU0xQNDFlYmU4cG5kY0lUQnpFYlhrMEpQRWNiV1dCeTJxZmRoc2NQd3hjSkdtNGhaVWpQMlM5amdXNlNvdDY2SjdiZHc3ZVN3emNXZmlJUW9NLTJ2WVczVE01cXRwVElrR0gtSkJueWZKQzhfRw?oc=5)
- [claimed] 판매자·구매자 양면 네트워크 효과는 구조상 합리적이지만 점유율·판매자 수 추이 같은 수치 증거가 수집되지 않았다. 판매자가 eBay·Shopify·TikTok·Walmart 판매를 Seller Central에서 함께 관리하는 기능은 멀티호밍을 전제하므로 락인이 약할 수 있다는 단서이기도 하다. [S40](https://news.google.com/rss/articles/CBMinAFBVV95cUxOQ3lUWUszZ0lhaXRhM0FRb2hvTjA2QlBINWhKbEcydkpSRW5uak1jeUZfVGYxUzcyRE55SDNfZHQ0UHF3OW1ab0h4TExxTG5zMmF3YTQyZlA4NWZOVXJmNnhUZC1hb1cySzdyY0NMcURIc0JoQnRKU1puYnhULXRpbkdQLUd3R1h4WDdiSlp6THBWX2doTmFQRUgxX3U?oc=5) [S32](https://news.google.com/rss/articles/CBMiigFBVV95cUxNN1RnMWxFWmtqTEJZNmtTNmVHdGZhUXhVbEVTenNKam8xZmtIVGNfQlYwRlY2anZ1ZXZWc1RDUW9DUFc2endnM1pOdU13c2I0RExUUGNrVFlvajZFWk8wNHZDQVdLR0JNc0wxeG1Lb05mektkVnVhejRsd1oxSG1jNGxBVWhoY2xkSHc?oc=5)

### 경영진·자본배분 — mixed

수집된 근거만으로는 경영진 정렬을 'mixed'로 둘 수밖에 없다. 보상 지표(DEF 14A, S13), 내부자 매매, 과거 가이던스 적중률, 자사주 이력은 수치로 채우지 못했다. 확인되는 사실은 세 가지다. 첫째, 희석은 크지 않다. SBC/매출은 2.9%이고 희석 주식 수는 완만하게 늘었다. 둘째, 자본배분은 AI 투자 쪽으로 크게 기울었다. 2026 capex 가이던스가 $220 billion으로 올랐고 부채도 급증했다. 셋째, 이사회에 사이버보안 전문가가 합류했다. 경영진의 약속 이행은 가이던스 이력이 없어 검증할 수 없다.

- [compensation] 근거 없음. 보상 연동 지표와 베스팅 기간이 있는 DEF 14A(S13)는 공시 목록에만 있고 수치로 채워지지 않았다. 장기 지표 연동인지 단기 EPS 연동인지 판단할 수 없다. [S13](https://www.sec.gov/Archives/edgar/data/1018724/000110465926041026/tm261382-1_def14a.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도 사실이 수집되지 않았다. 8-K 경영진 변동(S2)과 이사회 신규 선임(S41)은 확인되나 지분 정보는 없다. [S2](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000036/amzn-20260908.htm) [S41](https://news.google.com/rss/articles/CBMijAFBVV95cUxNdHVLaG9jX1A0Qk81YV92YzFwVDBlTnRTamtSaS1DUnFnQ0hRdWRzcktUeXIwc1h6dW9MY1ZaeDdNNkRSY0Q2UDRfUnlPY0VULUxyMGNfOXBDbVJlRTFQcDd0N1BjMWZJSHFGRW13NHRMeU0wQjloaGY1d3dzWFRtSHIyajZuMUJJTlZseg?oc=5)
- [guidance] 과거 가이던스(2025년 2분기~2026년 2분기)를 찾지 못해 적중률(C:guidance_hit_rate)을 낼 수 없다. 현재 3분기 가이던스 매출은 1,995억 USD이고 컨센서스는 2,039억 USD다. 가이던스가 컨센서스보다 낮은 보수적 구조로 보이나, 실제 적중 이력이 없어 신뢰도 평가는 보류한다. [F138] [F136] [S4](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260730.htm) [S45](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/amazon-postq-aws-reaccelerates-as-ai-investment-pushes-capex-higher)
- [dilution] SBC는 FY2025 기준 매출의 2.9%(C:sbc_to_revenue@FY2025), 영업현금흐름의 17.0%(C:sbc_to_ocf@FY2025)다. 희석 주식 수는 FY2025Q1 107.9억 주에서 FY2026Q2 109.0억 주로 늘었다. 증가폭이 작아 희석 부담은 낮다. 같은 기간 자사주 매입 근거는 없다. [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [F42] [F46]
- [capital_allocation] 2026 capex 가이던스는 $220 billion으로 상향됐다(메모리 비용 상승이 이유). 실적 발표 전 컨센서스 capex는 2,061억 USD여서 시장 예상보다 높다. 재투자 수익률(ROIC)은 FY2025 22.6%(C:roic@FY2025)이나, 대규모 AI 투자가 이 수익률을 유지할지는 근거가 없다. [S25](https://news.google.com/rss/articles/CBMifEFVX3lxTE5YU3ZKX2xoamdmZWNkOE52VGdqb3VtQTFUTXl1S0hwdWFZNGlNTE1SMGNjZlR1MXpVN2lINkVwd1VoWEdkTGFmcFItRTlxVFIyUkhwYlJCM3l5T29aYjhUM0tRSjdYNGVZY3c5eHBqVTNpVmR4aEdSTXJtd1HSAYIBQVVfeXFMTVhaMjBSNjI0eXFRb3NsNUxJNzNlalZvUjRUQkpmSFNkMGJtUVVGS19PN1JLdWpmMEdJaVVvR1B4S1dDN0NUM3dpcWRqdmxiZjdDakUzblV0TmU2QVI0UzRWNldDS3F0MC1DWGU2MUEydXV5c0lYYWI5bFA3WlJoSFhSZw?oc=5) [S26](https://news.google.com/rss/articles/CBMinAFBVV95cUxPYWNwWXZRNEt4SjNsc2hzSThoZ2ZSYktrQ0JZdUdLN3owZnVXRkpXVm5DSXhMTVZYTHdTWk1FWWVhUEtpWE0zWGRMaHlHdi01YXh1Sm9KNXJDUWcxVmNIT3YwWlJaM2U0dDJDQWtQWmVkeTBCWWZWMzczdy14My1NMWUzbFo0S0tDc0V3Ulg4dlVrWjNoNTFOSkpoRmc?oc=5) [F140] [F141] [C:roic@FY2025]
- [capital_allocation] 부채는 FY2025Q1 533.7억 USD에서 FY2026 1,288.9억 USD로 늘었다. 보고 라벨이 겹쳐 기간 해석에는 주의가 필요하다. 투자 재원을 외부 조달로 확대했다는 방향은 확인된다. 다만 계산된 순부채/EBITDA는 0.07x로 아직 낮다. [F23] [F28] [C:net_debt_to_ebitda@FY2025]
- [capital_allocation] AWS의 DuckLabs(DuckDB 개발사) 인수가 발표됐다. 인수 금액과 가격 적정성은 근거에 없어 고점 인수 여부를 판단할 수 없다. 자사주 매입·배당 이력도 수집되지 않았다. [S37](https://news.google.com/rss/articles/CBMiakFVX3lxTE40S2JJbEVhVWJaQUs0eUFDdTFvbjNGTFppdDRGUlVxaEhGU1BxdkZLdlU5bkp5Nk5yZWlQQlEzMUhWMDFSLU9GR21uRW8tcVFhNlltWU1rOXVQVW1qdVB4YmNFNHk5WDQzVEE?oc=5)
- [capital_allocation] 사실 충돌이 현금·부채·SBC 등 여러 항목에 있다. 같은 연도 라벨에 분기말 값이 섞인 것이 원인이다. 위 관찰은 방향성 수준으로만 쓰고, 정확한 시점 비교는 기간 라벨 교정 뒤에 해야 한다. [F24] [F26] [F109] [F110]

### 회계 품질 — watch

코드가 계산한 회계 품질 신호는 없고, 재무제표 정정·감사인 변경·계속기업 의문 같은 red 단서도 이 근거에서는 찾지 못했다(찾지 못했다는 것이지 없다는 확인은 아니다). 그러나 이 '신호 없음'은 입력 오염 때문에 신뢰도가 낮다. 같은 FY2025·FY2026 라벨에 분기말 값이 섞여 충돌했고, 그 때문에 연간 기준 발생액·채권 갭·OCF/순이익 신호가 제대로 계산되지 않았을 가능성이 크다. 분기 값을 직접 보면 조정해서 볼 숫자가 있다. (1) FY2026Q2 순이익 626.5억(F80)이 영업이익 274.6억(F96)의 두 배를 넘는다. 이익 상당 부분이 영업 밖에서 왔고(투자 평가이익 등으로 추정, 원인 확인 필요), 반복되지 않는다고 봐야 한다. 이익의 질은 순이익이 아니라 영업이익과 영업현금흐름으로 판단한다. (2) 매출채권이 FY2025 2분기 말 574.1억(F98)에서 FY2026 2분기 말 880.9억(F102)으로 늘었다. 같은 기간 분기 매출은 1,677.0억(F105)에서 2,006.1억(F108)으로 늘어, 채권이 매출보다 훨씬 빠르게 증가했다. AWS 대형 계약의 결제 조건 변화일 수 있으나 근거에 없어 미해명이다. (3) 부채가 656.5억(F26)에서 1,288.9억(F28)으로 늘었고 연간 capex 가이던스가 2,200억(F140)이라 자본집약도가 크게 높아졌다. 이는 회계 조작이 아니라 감가상각 증가로 이어질 이익 지속성 문제다. 따라서 `red_flag`는 아니고 `watch`로 판정한다. 영업이익 기준으로 보고, 비영업 이익을 제외하고, 채권 증가의 원인이 풀릴 때까지 조정해서 봐야 한다.

- [watch] 코드 신호가 '없음'으로 나왔지만 입력 사실에 기간 라벨 충돌이 있다. cash·debt·ocf·net_income·receivables·sbc·total_assets 등이 같은 FY 라벨 아래 서로 다른 분기말 값으로 섞여 있어, 연간 기준 발생액·OCF/순이익·채권/재고 갭 신호가 정상 계산되지 않았을 가능성이 크다. 기간 라벨을 바로잡아 코드 신호를 다시 계산하기 전에는 '신호 없음'을 깨끗하다는 증거로 읽으면 안 된다. [F81] [F82] [F83] [F100] [F102]
- [watch] FY2026Q2 순이익 626.5억은 영업이익 274.6억의 두 배를 넘는다. 차이는 비영업 항목(투자 평가이익 등으로 추정)이고 반복 가능성이 낮다. 이 근거에는 구성 내역이 없어 10-Q 손익계산서의 기타 수익(비용)을 직접 확인해야 한다. 이익 배수나 EPS 추세는 순이익이 아니라 영업이익 기준으로 본다. [F80] [F96] [S3](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm)
- [watch] 매출채권이 FY2025 2분기 말 574.1억에서 FY2026 2분기 말 880.9억으로 늘었다. 같은 기간 분기 매출은 1,677.0억에서 2,006.1억으로 늘었다. 채권이 매출보다 빠르게 증가하는 것이 계약 결제 조건 변화, 큰 고객의 청구 시점, 매출 인식 방식 중 무엇 때문인지 근거로 확인되지 않았다. 재고는 같은 기간 감소해 상품 쪽 부담은 아니다. [F98] [F102] [F105] [F108] [F70]
- [watch] 부채가 656.5억에서 1,288.9억으로 늘었고 FY2026 capex 가이던스는 2,200억이다(컨센서스는 2,061억). 자본화된 설비의 감가상각이 앞으로 이익을 압박하고, 내용연수 가정을 바꾸면 이익이 달라질 수 있다. 감가상각비는 분기 기준 142.6억에서 199.9억으로 늘었다. 내용연수 변경과 건설 중 자산 규모는 10-K·10-Q 주석에서 확인해야 한다. [F26] [F28] [F140] [F141] [F18] [F22]
- [info] SBC는 FY2025 연간 기준 매출의 2.9%, 영업현금흐름의 17.0%로 문턱(10%·50%) 아래다. 희석 주식 수는 FY2025 1분기 107.9억에서 FY2026 2분기 109.0억으로 완만하게 늘었다. 주식보상이 이익을 부풀리는 구조는 아니다. [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [F42] [F46]
- [info] 이연매출은 약 205억~217억 범위에서 거의 변하지 않는 반면 매출은 두 자릿수로 늘었다. 선수금을 앞당겨 인식한 흔적은 보이지 않는다. 영영권은 총자산 대비 비중이 작아 인수 회계 리스크는 낮다. [F38] [F40] [F58] [C:goodwill_to_assets@FY2025]
- [info] 감사의견, 감사인 변경, 재무제표 정정, 특수관계자 거래에 대한 별도 근거를 찾지 못했다. 코드의 restatement·auditor_change 신호도 없다. 다만 직접 확인한 것이 아니므로 10-K와 DEF 14A를 읽을 때까지 미확인으로 둔다. FTC 광고 소송은 금액 영향을 알 수 없다. [S17](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm) [S13](https://www.sec.gov/Archives/edgar/data/1018724/000110465926041026/tm261382-1_def14a.htm) [S32](https://news.google.com/rss/articles/CBMiigFBVV95cUxNN1RnMWxFWmtqTEJZNmtTNmVHdGZhUXhVbEVTenNKam8xZmtIVGNfQlYwRlY2anZ1ZXZWc1RDUW9DUFc2endnM1pOdU13c2I0RExUUGNrVFlvajZFWk8wNHZDQVdLR0JNc0wxeG1Lb05mektkVnVhejRsd1oxSG1jNGxBVWhoY2xkSHc?oc=5)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) AI 인프라 과잉투자와 수익 미회수. 2026 capex가 2,200억 USD까지 올랐는데 AI·클라우드 수요가 투자 속도를 따라오지 못한다. 설비가 가동률 부족에 걸리면 감가상각만 쌓인다. 분기 감가상각은 이미 142.6억에서 199.9억으로 늘었다. 영업이익이 상각을 따라가지 못하면 FCF 마진은 한 자릿수에 머문다. 시장은 PER 약 40배(C:pe)를 FCF 회복을 전제로 지불하고 있어 배수 압축과 이익 정체가 동시에 온다. 메커니즘은 '투자 선행 → 가동률 부족 → 상각 부담 → 배수 하락'이다. [F140] [F141] [F18] [F22] [F96] [C:pe] [S25](https://news.google.com/rss/articles/CBMifEFVX3lxTE5YU3ZKX2xoamdmZWNkOE52VGdqb3VtQTFUTXl1S0hwdWFZNGlNTE1SMGNjZlR1MXpVN2lINkVwd1VoWEdkTGFmcFItRTlxVFIyUkhwYlJCM3l5T29aYjhUM0tRSjdYNGVZY3c5eHBqVTNpVmR4aEdSTXJtd1HSAYIBQVVfeXFMTVhaMjBSNjI0eXFRb3NsNUxJNzNlalZvUjRUQkpmSFNkMGJtUVVGS19PN1JLdWpmMEdJaVVvR1B4S1dDN0NUM3dpcWRqdmxiZjdDakUzblV0TmU2QVI0UzRWNldDS3F0MC1DWGU2MUEydXV5c0lYYWI5bFA3WlJoSFhSZw?oc=5)
- (12%) 외부 조달 의존과 금리·신용 충격. 투자 재원이 영업현금흐름으로 부족해 부채가 656.5억에서 1,288.9억으로 늘었다. capex가 2,200억 수준으로 이어지면 부채는 더 늘고, 신용시장이 닫히거나 금리가 높게 유지되면 이자 부담이 FCF를 잠식한다. 현재 순부채/EBITDA는 0.07x로 낮아 출발점은 건전하다. 그러나 시장이 AI 투자 회수를 의심하는 순간 조달 비용이 오르고 투자 축소·배당 불가능 구도로 몰릴 수 있다. 부채가 완충을 먹는 속도가 위험이다. [F26] [F28] [F140] [C:net_debt_to_ebitda@FY2025]
- (10%) 규제·소송으로 고수익 광고·마켓플레이스 수익 훼손. FTC가 스폰서 광고 관련 소송을 제기했다. 광고가 수익성의 핵심 축일 가능성이 높은데 부문 수치가 없어 노출 규모를 알 수 없다. 패소 또는 합의로 광고 노출 방식·수수료 구조가 바뀌면 소매 부문의 영업이익률이 훼손된다. 영업이익률 11.2%(C:operating_margin@FY2025)는 얇아 광고 수익이 줄면 영업이익이 크게 줄어든다. 영업 레버리지가 반대로 작동한다. [S32](https://news.google.com/rss/articles/CBMiigFBVV95cUxNN1RnMWxFWmtqTEJZNmtTNmVHdGZhUXhVbEVTenNKam8xZmtIVGNfQlYwRlY2anZ1ZXZWc1RDUW9DUFc2endnM1pOdU13c2I0RExUUGNrVFlvajZFWk8wNHZDQVdLR0JNc0wxeG1Lb05mektkVnVhejRsd1oxSG1jNGxBVWhoY2xkSHc?oc=5) [C:operating_margin@FY2025]
- (12%) 이익의 질 저하와 매출채권 팽창. 채권이 574.1억에서 880.9억으로 늘어 매출 증가율보다 빠르다. 대형 고객의 결제 조건 완화나 신용 위험이라면 매출 인식이 현금으로 이어지지 않고, 순이익 626.5억이 영업이익 274.6억의 두 배 이상인 것은 비영업 평가이익에 의존했다는 뜻이다. 투자자가 영업이익과 현금흐름으로 가치를 재평가하면 PER 약 40배는 정당화되지 않는다. 이익의 질에 대한 의문이 커지는 과정이다. [F98] [F102] [F105] [F108] [F80] [F96] [C:pe]
- 약한 가정 `base.fcf_margin`: 기본 시나리오가 FCF 마진 12%로 직선 상승한다고 가정하지만 이것이 시나리오의 핵심이고 확인된 사실이 아니다. capex가 가이던스 2,200억이면 매출 대비 투자 비중이 매우 커서(FY2026 컨센서스 매출 8,289억 대비 약 27%) 마진 회복은 capex 정점과 상각 흡수 시점에 달려 있다. 모델러도 가정이라고 인정했다. 기저율 표와 대조해도 근거가 약하다. [F140] [F135] [F141]
- 약한 가정 `base.exit_multiple`: 종료 배수 26배는 현재 PER 약 40배(C:pe)에서의 압축을 반영한 것이나, 투자 회수가 불확실한 환경에서 시장이 26배를 유지할지는 별도 근거가 없다. 성장이 한 자릿수로 둔화하는 5년 차에 26배를 주는 것은 낙관적일 수 있다. [C:pe] [F135]

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| 매출 (revenue) | 5,747.9억 USD | 6,379.6억 USD | 7,169.2억 USD |
| 매출 성장 (revenue_growth) | — | 11.0% | 12.4% |
| 총이익률 (gross_margin) | — | — | 50.3% |
| 영업이익률 (operating_margin) | — | — | 11.2% |
| 순이익 (net_income) | — | — | 706.2억 USD |
| 영업현금흐름 (ocf) | — | — | 1,211.4억 USD |
| SBC (sbc) | — | — | 205.5억 USD |
| SBC/매출 (sbc_to_revenue) | — | — | 2.9% |
| SBC/영업현금흐름 (sbc_to_ocf) | — | — | 17.0% |
| ROIC (roic) | — | — | 22.6% |
| 순현금 (net_cash) | — | — | 546.3억 USD |
| 순부채/EBITDA (net_debt_to_ebitda) | — | — | -0.39x |
| 희석 주식 수 (diluted_shares) | — | — | 108.3억 |
| DSO(일) (dso) | — | — | 34.5 |
| DIO(일) (dio) | — | — | 39.2 |

표에 없는 키도 인용할 수 있다: cash, cash_total, cost_of_revenue, d_and_a, debt, debt_current, debt_total, deferred_revenue, ebitda, equity, goodwill, goodwill_to_assets, gross_profit, income_tax, inventory, operating_income, receivables, short_term_investments, total_assets

### 시장 · FY2025 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 258.58 USD/share (2026-10-13, F132) |
| 희석 주식 수 (shares) | 109.0억 |
| 시가총액 (market_cap) | 2.82조 USD |
| 순현금 (net_cash) | -92.4억 USD |
| EV (ev) | 2.83조 USD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 3.95x |
| PER (pe) | 39.92x |
| 순부채/EBITDA (net_debt_to_ebitda) | 0.07x |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull", "revenue_growth": [0.17, 0.16, 0.14, 0.13, 0.12, 0.11, 0.1, 0.1, 0.09, 0.09], "fcf_margin": 0.18, "exit_multiple": 30, "share_change": 0.003, "years": 10}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "bear"}: price=258.6, net_debt_to_ebitda=0.07x, leveraged=아니오

### 계산 경고

- 사실 충돌 cash FY2025: F2=5.7741e+10, F3=6.6922e+10, F4=8.681e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 cash FY2026: F5=1.01816e+11, F6=7.8213e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 d_and_a FY2025: F13=5.8562e+10, F14=6.1916e+10, F15=6.5756e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 d_and_a FY2026: F16=7.0439e+10, F17=7.52e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 debt FY2025: F24=5.0718e+10, F25=5.0742e+10, F26=6.5648e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 debt FY2026: F27=1.19074e+11, F28=1.28894e+11 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 debt_current FY2025: F30=5.005e+09, F31=3.997e+09, F32=2.748e+09 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 debt_current FY2026: F33=2.832e+09, F34=3.33e+09 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 deferred_revenue FY2025: F36=2.1662e+10, F37=2.1113e+10, F38=2.0576e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 deferred_revenue FY2026: F39=2.0887e+10, F40=2.0428e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 equity FY2025: F48=3.33775e+11, F49=3.69631e+11, F50=4.11065e+11 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 equity FY2026: F51=4.41914e+11, F52=5.5162e+11 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 inventory FY2025: F66=4.0825e+10, F67=4.1494e+10, F68=3.8325e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 inventory FY2026: F69=3.6534e+10, F70=3.8184e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 net_income FY2025: F71=7.0623e+10, F72=7.6482e+10, F73=7.767e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 net_income FY2026: F74=9.0798e+10, F75=1.35281e+11 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 ocf FY2025: F81=1.21137e+11, F82=1.30691e+11, F83=1.39514e+11 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 ocf FY2026: F84=1.48531e+11, F85=1.61403e+11 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 receivables FY2025: F98=5.7415e+10, F99=6.1175e+10, F100=6.7729e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 receivables FY2026: F101=7.5532e+10, F102=8.8092e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 sbc FY2025: F109=2.0551e+10, F110=2.0065e+10, F111=1.9467e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 sbc FY2026: F112=1.981e+10, F113=1.9314e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 short_term_investments FY2025: F121=3.5439e+10, F122=2.7275e+10, F123=3.6219e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 short_term_investments FY2026: F124=4.1273e+10, F125=4.4775e+10 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 total_assets FY2025: F127=6.8217e+11, F128=7.27921e+11, F129=8.18042e+11 — 1차 자료 우선으로 하나만 쓴다
- 사실 충돌 total_assets FY2026: F130=9.1663e+11, F131=1.09569e+12 — 1차 자료 우선으로 하나만 쓴다
- 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

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

# ASML Holding (ASML) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 근거 충분성** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✗ 주가·주식 수 없음 — 시장 가격과 비교할 수 없다

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: 주가·주식 수 없음 — 시장 가격과 비교할 수 없다

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 주가 통화 USD ≠ 재무 통화 EUR — fx 사실 필요 (단위 EUR/USD)
## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| 매출 (revenue) | 186.1억 EUR | 211.7억 EUR | 275.6억 EUR | 282.6억 EUR | 326.7억 EUR |
| 매출 성장 (revenue_growth) | — | 13.8% | 30.2% | 2.6% | 15.6% |
| 총이익률 (gross_margin) | 52.7% | 50.5% | 51.3% | 51.3% | 52.8% |
| 영업이익률 (operating_margin) | 36.3% | 30.7% | 32.8% | 31.9% | 34.6% |
| 순이익 (net_income) | 58.8억 EUR | 56.2억 EUR | 78.4억 EUR | 75.7억 EUR | 96.1억 EUR |
| 영업현금흐름 (ocf) | 108.5억 EUR | 84.9억 EUR | 54.4억 EUR | 111.7억 EUR | 126.6억 EUR |
| 설비투자 (capex) | 9.0억 EUR | 12.8억 EUR | 21.6억 EUR | 20.7억 EUR | 15.7억 EUR |
| FCF (fcf) | 99.5억 EUR | 72.0억 EUR | 32.9억 EUR | 91.0억 EUR | 110.8억 EUR |
| FCF 마진 (fcf_margin) | 53.4% | 34.0% | 11.9% | 32.2% | 33.9% |
| FCF/순이익 (fcf_conversion) | 1.69x | 1.28x | 0.42x | 1.20x | 1.15x |
| SBC (sbc) | 1.2억 EUR | 6,890만 EUR | 1.3억 EUR | 1.7억 EUR | 2.0억 EUR |
| SBC/매출 (sbc_to_revenue) | 0.6% | 0.3% | 0.5% | 0.6% | 0.6% |
| SBC/영업현금흐름 (sbc_to_ocf) | 1.1% | 0.8% | 2.5% | 1.5% | 1.6% |
| SBC 차감 FCF (fcf_after_sbc) | 98.3억 EUR | 71.4억 EUR | 31.5억 EUR | 89.3억 EUR | 108.8억 EUR |
| ROIC (roic) | 68.6% | 88.5% | 64.5% | 68.3% | 80.5% |
| 순현금 (net_cash) | 23.7억 EUR | 30.1억 EUR | 23.7억 EUR | 80.5억 EUR | 85.3억 EUR |
| 순부채/EBITDA (net_debt_to_ebitda) | -0.33x | -0.42x | -0.24x | -0.81x | -0.69x |
| 희석 주식 수 (diluted_shares) | 4.1억 | 4.0억 | 3.9억 | 3.9억 | 3.9억 |
| 주식 수 변화 (share_change) | — | -3.0% | -1.0% | -0.1% | -1.2% |
| DSO(일) (dso) | 59.4 | 91.8 | 57.4 | 57.8 | 33.8 |
| DIO(일) (dio) | 214.8 | 250.9 | 240.7 | 288.7 | 270.7 |
| 발생액 비율 (accruals_ratio) | — | -8.6% | 6.3% | -8.1% | -6.2% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, cost_of_revenue, d_and_a, debt, debt_current, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, goodwill, goodwill_to_assets, gross_profit, income_tax, interest_expense, inventory, inventory_growth, operating_income, receivables, receivables_growth, rnd, total_assets

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] inventory_gap (C:inventory_gap): FY2024 재고 증가율 - 매출 증가율 20.5% > 15%

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "base"}: leveraged=아니오

### 계산 경고

- 주가 통화 USD ≠ 재무 통화 EUR — fx 사실 필요 (단위 EUR/USD)

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-10-14 | [6-K](https://www.sec.gov/Archives/edgar/data/937966/000162828026065813/form6-kquarterlyfilings.htm) |  |
| S2 | filing | 2026-07-15 | [6-K](https://www.sec.gov/Archives/edgar/data/937966/000162828026048235/form6-kquarterlyfilings.htm) |  |
| S3 | filing | 2026-04-23 | [6-K](https://www.sec.gov/Archives/edgar/data/937966/000162828026026703/form6-kagmdisclosureofagmr.htm) |  |
| S4 | filing | 2026-04-15 | [6-K](https://www.sec.gov/Archives/edgar/data/937966/000162828026025147/form6-kquarterlyfilings.htm) |  |
| S5 | filing | 2026-03-11 | [6-K](https://www.sec.gov/Archives/edgar/data/937966/000162828026016671/form6-kagm.htm) |  |
| S6 | filing | 2026-02-25 | [20-F](https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/asml-20251231.htm) |  |
| S7 | filing | 2026-02-25 | [6-K](https://www.sec.gov/Archives/edgar/data/937966/000162828026011377/form6-kannualreportbasedon.htm) |  |
| S8 | filing | 2026-01-28 | [6-K](https://www.sec.gov/Archives/edgar/data/937966/000162828026003701/form6-kquarterlyfilings.htm) |  |
| S9 | filing | 2025-10-15 | [6-K](https://www.sec.gov/Archives/edgar/data/937966/000162828025045043/form6-kquarterlyfilings.htm) |  |
| S10 | filing | 2024-02-14 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/937966/000093796624000008/0000937966-24-000008-index.htm) |  |
| S11 | filing | 2025-03-05 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/937966/000093796625000009/0000937966-25-000009-index.htm) |  |
| S12 | filing | 2023-02-15 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/937966/000093796623000014/0000937966-23-000014-index.htm) |  |
| S14 | news | 2026-09-24 | [ASML says it sold 'absolutely nothing' in Europe in 2026 — lithography giant calls on EU to help create demand - Tom's Hardware](https://news.google.com/rss/articles/CBMi1wFBVV95cUxNVXNTOGdaT1dackdKN0RxQjZPek8yamd0RFdnU3BlMlBTSmFqWFBfUFYtbXp1blNTcWFGak4zTTRhQlZ4TU5MLVZZZjRuVFU0VDJFYVo4S0lmalVWVkZzbXhaTEpRZWhpcU1mRkJGSFh0Q2k5TG5JVEhhUHZFY2wzOFdQR0cwN0dPNFB1OGUxbWFaTG1kU1JMTkNka1FiX1NuQ013am1FbE9iVS0zOXdVcW91YzBqV05RMUpMdGhHSFg3ZDBwSkR0QmM2ZU1DUHVoNUkxZkstaw?oc=5) | Tom's Hardware |
| S15 | news | 2026-08-12 | [ASML Holding N.V. (ASML) vs. Taiwan Semiconductor Manufacturing Company Limited (TSM): A Key Supplier Says it Can Keep Up With the AI Boom - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxNa1B4Y0RCbFZtZDJkdGhjeUFISWlIbllMRjZrblNGREdvSGlDNE1BQU1aQWprOUY0NmhfRUVYRG5wc09HVXNOYl8weUx3ZzRHVVY0a1U1X0xEbElfRDIyZENNdnUxZklCOEJXNUZRZkpJdjJpSjdyTDdaYWJaOVRvaXNlaE9uUEFpQTBVTFNYUQ?oc=5) | Yahoo Finance |
| S16 | news | 2026-10-14 | [EU to Lift Sanction on Chinese Firm to Save an ASML Supplier - Bloomberg.com](https://news.google.com/rss/articles/CBMisgFBVV95cUxNM2lUQllVYjVsZFEtVnBjdHNGYXZxUzhwOTVtNnk5OENHUktsbUFaLVhXMUswYVNKa0dDYmF4a1gyM05MWEgyb3BTLTdJeS1pMXJnZlFIUmozelVVS2ROQTkyNWtCdTQxVXp5bGFKWmVpZU1EN0VyMXZ3TU1aN3puSTc1bTFLdGY2TmxIR0hOY3dCSHRFbVlLVWQ0YnhLbDE2YTdCWHpLamJyeHVUTWpybk5n?oc=5) | Bloomberg.com |
| S17 | news | 2026-10-10 | [Dear ASML Stock Fans, Mark Your Calendars for October 14 - Barchart.com](https://news.google.com/rss/articles/CBMioAFBVV95cUxObWZ3TFZHUWxOVzEwWEVsRnp1QXVrS1FjMlJlRUhqVXdSS3BoeG1QZ01wSWJVOERBWlVuYlBNdWhDMWdqdTlURXNodElzVGRsODFIcU4xRzM5QnA3UlZUNmVBOU4zMXdORFZHcmFCeEdkZ0M3V2NQYnBFcndMQ1VPNklNaHJkZXFIYlhUZ3hZSWJNbVVpOFNpUDZaVmt0N240?oc=5) | Barchart.com |
| S18 | news | 2026-09-27 | [ASML chief: ‘There is only one company making those machines’ - Financial Times](https://news.google.com/rss/articles/CBMihAFBVV95cUxOZjB5dTFZdHdwdktnU25XdWE2aDRCM05tNUpIbjdCWVlvUnIzWXBqdkZzaG9SUnJrMnUyd3NYV3Y2eWV4SHFtSjdScHEtanEzbHBrdTJTaUpCNzlTRVk4dm5ISGVVNGRsdi1aX25ZbGI4MEl2anhpNXY3cExpNUVEbG9IZVk?oc=5) | Financial Times |
| S21 | news | 2026-09-24 | [Dutch Premier Hopes to Prevent More US Export Curbs on ASML - Bloomberg.com](https://news.google.com/rss/articles/CBMirwFBVV95cUxNUUNaNGRPR1BseDBJX0FoSU9zeDllZmhqVE5KTDJqbVEzY3k1WU5idFhRWm9SWEJyRUJwZk5LNGhWZU1adVRDTVJKSjZXQXdxaGFoaG1pQlg2YVVWOVdUZ2VYbDFDNGsyVXpYV1A4c0NXd3R1dkxKU2ZSWHZlc01nZTY0RzlOTmYwaVY2Qm1POW9xQWs1ZXY2WlRFeUd2aUw3NmpCbUQzcVlCRktvcUdV?oc=5) | Bloomberg.com |
| S22 | news | 2026-09-17 | [ASML Holding N.V. (ASML) is Attracting Investor Attention: Here is What You Should Know - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxOUWM5UVdBYUlpZ3luMFJ5UGNsakpOUXg4dmV1M3QyamRZV1YyekxIS3NTUUh2Z1l5YkhJa3hSR3gtNFpYOG8tUnpHNnY5dXhmNGJGNjBEelpfVzZWXzFpdTl1T2dHQnMzanl6UWF1dXZMZEJQcTZUR3Jjbk1nSlhZUklGVjJGanBUbGlxMmJxVQ?oc=5) | Yahoo Finance |
| S23 | news | 2026-09-22 | [ASML Executive Says Europe’s Biggest Firm Has No Sales in Europe - Bloomberg.com](https://news.google.com/rss/articles/CBMitgFBVV95cUxNQTZrVTMtc1h4MjNLb0dYNGZoQzhxeU1uRnZPMDhyckpQUVdZNDdrSm5VNmlWWGxSQzdRanBIZWpnMXNQc1g5dDJ2bnZibW1OemZ5aWI2Mm1UeXFwallMTGdUUzJwNGRCNm5nV1I3cV96dGduTEVkRExrcXlVX1dEZHJ5TUphbnVwZzl1NEJmOE92ZHhhUmFtY2Rkd0pDVS1ucmM4ZV80ZDR4Rk1LcGpFQW5nVDAzdw?oc=5) | Bloomberg.com |
| S24 | news | 2026-09-21 | [ASML Holding (ENXTAM:ASML) Alliances Put Valuation Back In Focus - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQOVJneDdNSGZfODhjMjdXTkdaWldDcUdUOWtWUnE4c2JXbDEtVkFMTWRGMDZKTEgwOUlCN204Y1JFQkpmb0xTaXBDejdHbTZ4RUhQajFnTEVtbjhEU3BmbVBHV2E0bkYydFVQS0JuYkh2c2E3amFqN25lckRPNHA4ZmJQMDM1bDlOdTQtVzgxTXJoN1dacHBBTEhxQm5uRHZX?oc=5) | Yahoo Finance |
| S25 | news | 2026-09-30 | [Here is What to Know Beyond Why ASML Holding N.V. (ASML) is a Trending Stock - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxOU3Q2Qkx4WkNTTWxCanB5dC1wU3pYaDdmajhGYnAyTEQ4alRva2FacmdGdEtTclp0VlBkSHdNb0wteUtHYlJNUHJ3d010MUh0cUlERG9TdzA1NWlmZHNjU2JyWWV2TGpScGlseG9PRXJ4MnVRbWFGUnRKM0hodm0yei1paHBhMklyOGluRnNDalR1SnVlbnBMWA?oc=5) | Yahoo Finance |
| S26 | news | 2026-10-12 | [Broader Industry-Wide Volatility Weighs on ASML Holding NV (ASML) - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxPcVNJbHMwc3pUSnphUzE1WWtjV0dndDVnR0dCekJBOGl4REFqaGlwYmItemN4QVItTTRtbjVpZHVPYWMweTBFbkM2T1Y1MzJhanV2WXpkLWpkSXctaUZtWnZVcUtjVEFfd0hTTGxWUE9KRlpGVU5IVzdOcHNmZzZHcTNuWTVfQnIwRkx2S0hUX2RvLUxuOEdxRkFYLTBPS3MyR21CNXY4cw?oc=5) | Yahoo Finance |
| S27 | news | 2026-09-16 | [ASML Holding (ASML) Faces Fresh Questions Over Future AI Demand - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNSW1QWmNqVmhNMUI3Y1UtRnNCX1A4dXA2ZXRTeG96UXBJVHZIeW5DUno1QVhXa29tU2lyMkNyZlU1a2lZOTBDYmU2U2QySWN4cm1QWnlIY3V1U21WQUJCbkpIbEFMYWtZVGEyVVZ3cDdUbVhfVm5abkZmXzlNYUp0OWJoMUc1WnAwNkdqZk4yWHU2Ymc5TG5MMg?oc=5) | Yahoo Finance |
| S28 | news | 2026-10-08 | [ASML Holding (ASML) Tests Its Valuation As The Mistral Deal Reshapes The Story - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxNSXlDZzZ1TFI0QmdtTDJZemcyeHR4NlE5WWJIY2U2OFh6NWVpZGRpRmpFRXAzaE5VRUJDZFZqZHhiaDJWWTYzLWVOX21qbFRyNlpsbUtkRUREdXMtQ3FzbDEyTFRkcXI1aVNoVXdYbFZwdXF6N1FIdmdkVi1XVTNNTEkyZS1ha3l1X2l2aGI4dy1oOVFVZkwwWTFKa0JNcm8?oc=5) | Yahoo Finance |
| S29 | news | 2026-10-09 | [ASML Holding (ENXTAM:ASML) Faces An AI Pullback, Is The Stock Too Expensive? - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxNazkycXdEc3ZocGFYUWlOMnQ3WjRPdXBNQXZhdkt3cExGX1hlMFZiMTdjOWNmZ2tUbDlCaEFadkVoaVpCZU9yZm83dU1WdWZBWFZzRGJCVE9mUmFoOTFJX3RqcXY1S21PSTNaTnBPenNIOG5xSlRjV3NBVnlGREQ0YXNobURsdkFIaHdRVldkR3NMQXRpMUwwaHA2dw?oc=5) | Yahoo Finance |
| S30 | news | 2026-10-12 | [Is ASML Holding NV's Stock a Buy Ahead of Its Q3 Earnings Report Wednesday? - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxQY2ttWjhZZ0RoLVZmRXloYUV3bFRlRTJzNnZNOGxsVkFuT2pRTWNwdTVNUU1vS2lFUjlpUW51WVBZeGxzYW0yQWxJWE10T3RiUUFCZG8wTUttZW9UTXctc1E0SHVoOTVGTm1VdWViZzV3dW83ZEthR0R1RnRCYjk2WEU3NEpjMzdWbVp6YUwyWlJobmpzZlE?oc=5) | Yahoo Finance |
| S31 | news | 2026-10-14 | [ASML Holding N.V. (ASML) Gains 9.4% as AI-Driven Demand Boosts Confidence in Lithography Equipment - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxPc18td1o4VFVSVEdxSmlnOTRieENfbVFLVFFaaWNGbTU5bmRGN0ZST1gwT0pUQ1ZDLVh4eEFaakNxa2JwNGtTX1oxandZYWFzUUIyZGRQSFVYb2prVjVYN3NhOGE1dlhZRXpva1pYWTZLN2RSOE1NeGpIM1NISUF5anl0U3Awc3M0d3cyeF91NA?oc=5) | Yahoo Finance |
| S32 | news | 2026-10-12 | [ASML Holding's Next Earnings Report on Oct. 14 Could Send the Stock Soaring. Here's Why. - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQVkJLMkg4M0JIOVdrSk14VGNsYVgwRlJrSF91UGY3WlRzVnpHZnFwa0ZEUnZ3TlViLWljNnBJeVp4TjFzTDBFaTBnTkVfZnhlWTlfN1paa0VuN2dkUzJiTEtYMDdtSXdZdHJJQk96bWZIWXQxVDh5eko3WFNpMWdzYlZtRVp4ZXhWelYyNzZjVHVZdWpXUEpHZkRoS0RPdEVZ?oc=5) | Yahoo Finance |
| S33 | filing | 2026-10-14 | [ASML reports €11.7 billion total net sales and €5.0 billion net income in Q3 2026 (6-K press release)](https://www.sec.gov/Archives/edgar/data/0000937966/000162828026065813/pressreleasefinancialresul.htm) | 2026년 3분기 총순매출 €11,662M, 매출총이익 €6,700M(57.5%), 순이익 €4,960M, 설치기반관리(IBM) 매출 €3,289M, 신규 리소그래피 장비 113대(2분기 86대), 중고 8대. 현금·단기투자 €12,735M(2분기 €7,582M). 3분기 자사주 매입 약 €4.1B(2026–2028 프로그램). 2026 중간배당 주당 €1.88(11월 4일 지급). 가이던스: 4분기 순매출 €14.2~15.2B·매출총이익률 약 57%, R&D 약 €1.2B, SG&A 약 €0.4B; 2026 연간 순매출 €44~45B·매출총이익률 약 56%. 2분기 비교치: 순매출 €9,326M, 매출총이익 €5,035M(54.0%), 순이익 €2,918M, IBM €2,762M. |
| S34 | data | 2026-10-09 | [ASML (Nasdaq) share price history – InvestSmart](https://www.investsmart.com.au/security/nasdaq/asml/asml-holding-nv/share-price) | 나스닥 ASML(뉴욕 등록 보통주) 2026-10-09 종가 USD 1,770.29. 같은 페이지의 실시간 표시가 약 1,780.34는 시점 불명이라 쓰지 않음. 10월 14일 실적 발표 후 주가 반응(S31 보도 제목은 +9.4%)은 반영되지 않은 값 — 최신 종가 아님. |
| S35 | news | 2026-10-14 | [ASML Q3 2026: Record €11.7 billion in sales and higher margins (Vested Finance)](https://vestedfinance.com/blog/us-stocks/asml-q3-earnings-2026/) | 2차 요약(보도). 3분기 순이익에 지분투자 평가이익 약 €509.7M 포함 → 이를 제외한 기초 순이익 약 €4.5B라는 분석. 경영진 발언: 현재 계획된 2027·2028년 공급은 고객 수요를 다 채우지 못하며, 일부 고객이 2029·2030년 주문에도 관심을 표명(주문 확정이 아니라 관심 표명). 3분기 신규 수주(bookings)는 확인되지 않음. |

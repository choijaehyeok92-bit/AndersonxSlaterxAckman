# Credo Technology (CRDO) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 근거 충분성** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✗ 주가·주식 수 없음 — 시장 가격과 비교할 수 없다

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: 주가·주식 수 없음 — 시장 가격과 비교할 수 없다

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 주가 사실 없음 (metric=price, basis=market, 단위 USD/share 또는 USD/ADR)
## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2026)

| 지표 (키) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| 매출 (revenue) | 1.1억 USD | 1.8억 USD | 1.9억 USD | 4.4억 USD | 13.4억 USD |
| 매출 성장 (revenue_growth) | — | 73.0% | 4.8% | 126.3% | 205.7% |
| 총이익률 (gross_margin) | 60.1% | 57.7% | 61.9% | 64.8% | 68.0% |
| 영업이익률 (operating_margin) | -20.6% | -11.5% | -19.2% | 8.5% | 33.3% |
| 순이익 (net_income) | -2,218만 USD | -1,655만 USD | -2,837만 USD | 5,218만 USD | 4.7억 USD |
| 영업현금흐름 (ocf) | -3,083만 USD | -2,462만 USD | 3,274만 USD | 6,508만 USD | 4.6억 USD |
| 설비투자 (capex) | 1,758만 USD | 2,171만 USD | 1,565만 USD | 3,606만 USD | 5,730만 USD |
| FCF (fcf) | -4,841만 USD | -4,633만 USD | 1,708만 USD | 2,902만 USD | 4.1억 USD |
| FCF 마진 (fcf_margin) | -45.5% | -25.2% | 8.9% | 6.6% | 30.5% |
| FCF/순이익 (fcf_conversion) | — | — | — | 0.56x | 0.86x |
| SBC (sbc) | 919만 USD | 2,352만 USD | 3,902만 USD | 7,736만 USD | 1.8억 USD |
| SBC/매출 (sbc_to_revenue) | 8.6% | 12.8% | 20.2% | 17.7% | 13.7% |
| SBC/영업현금흐름 (sbc_to_ocf) | — | — | 119.2% | 118.9% | 39.3% |
| SBC 차감 FCF (fcf_after_sbc) | -5,760만 USD | -6,984만 USD | -2,194만 USD | -4,833만 USD | 2.2억 USD |
| ROIC (roic) | -29.3% | -15.1% | -28.5% | 14.1% | 71.3% |
| 순현금 (net_cash) | 2.6억 USD | 2.2억 USD | 4.1억 USD | 4.3억 USD | 14.4억 USD |
| 순부채/EBITDA (net_debt_to_ebitda) | — | — | — | -7.30x | -3.01x |
| 희석 주식 수 (diluted_shares) | 8,840만 | 1.5억 | 1.6억 | 1.8억 | 1.9억 |
| 주식 수 변화 (share_change) | — | 65.8% | 5.8% | 16.8% | 3.9% |
| DSO(일) (dso) | 101.2 | 98.2 | 112.8 | 135.5 | 63.8 |
| DIO(일) (dio) | 235.0 | 215.4 | 128.6 | 213.6 | 214.5 |
| 발생액 비율 (accruals_ratio) | — | 2.1% | -12.2% | -1.8% | 0.5% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, cost_of_revenue, d_and_a, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, goodwill, goodwill_to_assets, gross_profit, income_tax, inventory, inventory_growth, operating_income, pretax_income, receivables, receivables_growth, rnd, short_term_investments, total_assets

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 13.7% > 10%
- [watch] receivables_gap (C:receivables_gap): FY2025 매출채권 증가율 - 매출 증가율 45.4% > 15%
- [watch] inventory_gap (C:inventory_gap): FY2025 재고 증가율 - 매출 증가율 121.2% > 15%
- [watch] dilution (C:dilution): 희석 주식 수 연 8.7% 증가 > 3%

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "base"}: leveraged=아니오

### 계산 경고

- 주가 사실 없음 (metric=price, basis=market, 단위 USD/share 또는 USD/ADR)

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-10-16 | [8-K](https://www.sec.gov/Archives/edgar/data/1807794/000162828026066139/crdo-20261016.htm) |  |
| S2 | filing | 2026-09-02 | [10-Q](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/crdo-20260801.htm) |  |
| S3 | filing | 2026-09-01 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1807794/000162828026059795/crdo-20260901.htm) |  |
| S4 | filing | 2026-08-25 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1807794/000162828026058936/crdo-20260825.htm) |  |
| S5 | filing | 2026-06-15 | [10-K](https://www.sec.gov/Archives/edgar/data/1807794/000162828026043303/crdo-20260502.htm) |  |
| S6 | filing | 2026-06-01 | [8-K 실적 발표 경영진 변동](https://www.sec.gov/Archives/edgar/data/1807794/000162828026039474/crdo-20260528.htm) |  |
| S7 | filing | 2026-04-13 | [8-K IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1807794/000162828026024892/crdo-20260413.htm) |  |
| S8 | filing | 2026-03-03 | [10-Q](https://www.sec.gov/Archives/edgar/data/1807794/000162828026014017/crdo-20260131.htm) |  |
| S9 | filing | 2026-03-02 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1807794/000162828026013205/crdo-20260302.htm) |  |
| S10 | filing | 2026-02-09 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1807794/000162828026006370/crdo-20260209.htm) |  |
| S11 | filing | 2025-12-02 | [10-Q](https://www.sec.gov/Archives/edgar/data/1807794/000162828025054549/crdo-20251101.htm) |  |
| S12 | filing | 2025-12-01 | [8-K](https://www.sec.gov/Archives/edgar/data/1807794/000162828025054428/crdo-20251201.htm) |  |
| S13 | filing | 2025-10-29 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1807794/000162828025046890/crdo-20251023.htm) |  |
| S14 | filing | 2025-10-16 | [8-K](https://www.sec.gov/Archives/edgar/data/1807794/000162828025045208/crdo-20251013.htm) |  |
| S15 | filing | 2025-10-07 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1807794/000162828025044360/crdo-20251006.htm) |  |
| S16 | filing | 2023-06-23 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1807794/000162828023023187/0001628280-23-023187-index.htm) |  |
| S17 | filing | 2024-06-24 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1807794/000162828024029629/0001628280-24-029629-index.htm) |  |
| S18 | filing | 2025-07-02 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1807794/000162828025033813/0001628280-25-033813-index.htm) |  |
| S19 | filing | 2025-03-10 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1807794/000162828025011738/0001628280-25-011738-index.htm) |  |
| S20 | filing | 2025-09-04 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1807794/000180779425000021/0001807794-25-000021-index.htm) |  |
| S21 | news | 2026-10-12 | [Credo Unveils 1.6T ZeroFlap Active Light Cable, Industry’s First Row-Scale, Wide-Parallel Optical Interconnect for AI Data Centers - Credo Technology Group Holding Ltd - Investor Relations](https://news.google.com/rss/articles/CBMisAJBVV95cUxQbjBhWjd4UFR3UjhFT3pEX1g1a181RFlWbFZhSi1naENRdlc2ZlFvV3JqWUZRUDItVnR3Ym5hdVFpM2g0QXBEUThib3Z1NUdROVhNVUZJdlgxNHQ2MmdnSlVRNElRcmpobjdJaDZOLXFrZVhLUEhURWNNay1VWlhBQkZDZUV5TnVJaFd4alFLTS0tVmNNMnd1MkxtcnVhRU91dEJnczNxUGhlSHlIelU3dUVfaDBhV1YxTndKcHliNVpJZTY0dXVtcXd0cF9BX0txUjhoUFZHSUozcVJTcUt2eTZkYkZ5U1c4RnBnUVVDZFF1RXRqNGpGQWl6a2hsOHdBbkZkcnh5TUtWZUxyZzhza1ZtWlZTcmJxN1VEZ0ZaWFYzR0ZYd1VGV2VRdDFTQjJD?oc=5) | Credo Technology Group Holding Ltd - Investor Relations |
| S22 | news | 2026-09-05 | [Credo Technology stock draws rave reviews on Q1 (CRDO:NASDAQ) - Seeking Alpha](https://news.google.com/rss/articles/CBMiigFBVV95cUxQX1RpVXlSZlRyWFVNVFpSMlpjYnZTRm1QYWpXeUszaTg3UU1fbzZmdGZMRm1WUDlkTVdmMTVOdHRrd0tPS3BIU1dGTUR5RHJLVTJYRzBuWTc0UHNNTTZVVDRELXM3eGdzT0ktWkpwNWttUUZCWnRTWk5sdzBOUE1PbkxLcUZxSDhIM0E?oc=5) | Seeking Alpha |
| S23 | news | 2026-10-01 | [Credo Technology Group (CRDO) Up 17.9% Since Last Earnings Report: Can It Continue? - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxOdzQycm9WanFPa043Q3ZDZXh5RWFMM1I0OVE5bkI1VWYtV0I3SGk5djhiU2VkQl9VdzZoem9TR2F2YTZqb0lKaFBUMGgzbFNwbUlmSzdoNjFVcERXSVhhQUpXWDJURHNteUNnYTlsSjY1N1FwT2FaS0lJLXM2NEZaYU12T1MxdHRhNUJRa1NZZGQ0d01yOTE1WGtjMA?oc=5) | Yahoo Finance |
| S24 | news | 2026-09-03 | [Why Credo Technology Sank This Week - The Motley Fool](https://news.google.com/rss/articles/CBMihAFBVV95cUxPZzZJT3NLcmFEeEY5YWRBYW5LMDVrTHEtS2ZWc2NNWk1CSVhya2E1UVhHaGdiQ05YMG9mMEtEeS1EMEVlWkRWQ21NbXZfbGQ5SlUtUU5SbUhHSTZDZ1JOMXVVMkQ4T3QxZ0U0NnU0SU10a1llemhyc3dyNGhyd1F4QWY2bWc?oc=5) | The Motley Fool |
| S25 | news | 2026-09-15 | [Credo Technology Group Holding Ltd - Credo Expands ZeroFlap Portfolio with 224G-Based 1.6T Optical Transceivers, Addressing the Growing Demand for AI Network Infrastructure - Credo Technology Group Holding Ltd - Investor Relations](https://news.google.com/rss/articles/CBMiugJBVV95cUxNNHowSFkyQXVZYlcwVDR1LVBkNzZ0QWd3eXFzZlFYb0VlQUZqQ0dERktuT1RTOGpvN1JleW1qck8wV1ZUdHVoNUxHTi1XSmtHa3VyaFB1dUl3MTg5M3EwLTVVZ3VRM1VSNUJPYlVjR2xFRWJOU0huVjhnMk1ET3Zrd2o2UzByNjhXeFNoTFVEb1FXdkp5b2RPeDZndmp3c0s5d0V1NzVZa1drWDRUMThTT09tTG9yRmIwd05EOVFXVEdRMENOSzV0X3BvanhTMjBHNkFTMzduNEEzWUlobTcxQ0N3cVk4V2ZueThudVAySHpITFNUV2Y2ODVyOTBydW1YMVBuV3Q2LTRvRkpyNXNBSlFROFFJaWpldFNVOVgyUHAtNXc2QWNudjUyYy1FU0YzZVU1SGY2eE43dw?oc=5) | Credo Technology Group Holding Ltd - Investor Relations |
| S26 | news | 2026-10-15 | [Arm vs. Credo Technology Group: Which Semiconductor Stock Is a Better Buy in 2026? - The Motley Fool](https://news.google.com/rss/articles/CBMizAFBVV95cUxQd3BTalE4ZHg1Yk9CMU5JUzVwQ3ZhanV0UHVNSmFDZE9WWHhvQmFxMGVGVTl6bjd2M2M0LWxMNVRoSVd4c2psYmE2ZjdIZVM5ZjhyZy03UVdIZVNBTlZaRnNkWEY4SEdmMWJkWUI3c0o3SnlCVElleDE2aUdsRGwtWVUtWVUtNkR2QTgteVJQWEhoNWM5aWtyN1FFaEdOTmNudzdYakhvU1pjVFhkTEZOMDZpalFzdWhkaVNZeGdBQVB3ZXk2ekFqMTk5VHk?oc=5) | The Motley Fool |
| S27 | news | 2026-10-12 | [Credo Launches Short-Reach Micro-Emitter Optics (SRMO) Standardization for AI Data Center Scale-Up and Scale-Out Applications - Credo Technology Group Holding Ltd - Investor Relations](https://news.google.com/rss/articles/CBMiqwJBVV95cUxNUkJRMTZKdGpvcWFtNkR3V3lsRVd5WXJLTFUwTThaMzdmaC1tYmtEQzM0NFFQdE9NbHo5YldGTi0yR00yYUxoWlo0X3czcld2b0hxYm9Ec0d1UENFMmlYRWFVd2NkNFdGMUVHV0ZZX3JVSVNPYVNuQ1VxanJEalRveXVOaVFETFJDSktya1FjZG1VN2dPUDJ3WW5WVmR1TmUyRFNYQmN6N3Z1N3d2QUFlWHMxZ3Fsd3ZlcFBmeXhZcmpqNVNMMHV4cmRkZWtBMVY1VjdHVmJrQnZHTEJQQm9QT1RzdzNwWEhKaDZla25ydV9RdFVnUDZOV0h0anpRVmhNbk5UM2l5OExXcUVrdnJCZkVBb2psV1RaUk5iZ0hTVjR1SFVpWDFMX2xtcw?oc=5) | Credo Technology Group Holding Ltd - Investor Relations |
| S28 | news | 2026-09-17 | [What's Going On With Credo Technology Stock on Thursday? - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxOTEFrdzZ6c3JXaHRGS2Rzd2F0VVNEU1B0VVNVRTVDanA4b0tETktOTE10bkpmbDR5bVZMOWxKQ2FmQXNwdE8yZmN1N2NzeGhsYWdmTnJfQk5rNE1xNWpwOHY1aXVfNDdQQTR5SzJVTF9ObEZPVWk1T3NiWGlyc1BJeEMySE5XYUJSVlhQQ1ZIUTRjTl9JR29pTXFnaWtsQUx0?oc=5) | Yahoo Finance |
| S29 | news | 2026-10-13 | [Credo Breaks the Memory Wall Using AMD Programmable Logic-Based AI Accelerators - Credo Technology Group Holding Ltd - Investor Relations](https://news.google.com/rss/articles/CBMi8AFBVV95cUxNbVdnajdwOWl4M1dKOEF0X25NR3Z0Mkh0eU1HOHZOMG05VWUwbFBRQXpfbW13cHhpN0NhT21CZGJ3cnZlRFJzc2ZiZmkzZ3VTWlFWTkkwMTVSQ2RrQnlleU93Smxpc0U2RTJyWm9kM01mai1iY3VNWHNILUtTNlE5MlNNRDJpSmdVckpQSlMwZm5fb0w4ckwwU2M0R1djTWFJdndveU4tbVVJelQyRG55Zk8zZHBnOTdkM3A4bFNzT3VVVFJuT055ZTFtZGczWnEtX0RwX0xzVENLVVMzNDRsQnN0RUdmSjJ1a0hWcUZqZVg?oc=5) | Credo Technology Group Holding Ltd - Investor Relations |
| S30 | news | 2026-09-21 | [AI build-out Strengthens Credo Technology Group Holding Ltd (CRDO) - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxQcUNPdGprZTRFVjFTbjdqOFJNbDdxTnB2d1Zma3JtekpvdjVCTlUtUVlfSEItUXZ0OEFaQjZ3TWI4cTRqUVlBdUowd2oxSUdmTGNDMWtDMVd0NlctYW9nSXphdm5jWWNDUFFRMEV0UnVsNUJtN3prSHFqcXZVY2hKa1RkMzI1NF81d2h4RXlKM3F1eUttbDMycUpWeWpDMmVRTjdv?oc=5) | Yahoo Finance |
| S31 | news | 2026-09-16 | [ZeroFlap Optics Expands to 1.6T - Credo \\| We Connect](https://news.google.com/rss/articles/CBMi3AFBVV95cUxOZUhGSXpoTXcxQm40TlZoYVZFLVRIcUV6aV81OE1pRXVQTTRGUjFmOVdrTzZPdlNIOURLVnNTSjFfUkdHcTRBY3J3RklPYnRhN2VSYWwyQVFONFRGdlc0OW5lc0ZDd0t6RGtGOUNwRW9ySlFVQS1WVjBtWGMyazJmNXNkWlg5X0RoUDV5dktma1VhRkh2dDA2OG01OWNueWtWbUpKYUFDR1NJRHhRWU9Dd3R5UXJyTTdBY0VQV3gwRkJjQjYzbDVMcm5fVkhrV1ZoNlFrVFg4ZC1KMHJP?oc=5) | Credo \| We Connect |
| S32 | news | 2026-10-10 | [Where Will Credo Technology Be in 3 Years? - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxNY3oxelhBak9DSjlneEhFbVJHaVBqQmV5MV9oSmp4bjhEUlp1WFMyclNCOWJ4VHNEd3RWZzE5YVNSdFVJaDdzX1czNmY5eGFheGwxMVEtSm1mM3dVdHk4OVRpTDZVaTd6OWs0dm5faGxuTjdRYUpGd1pKcC1oWVVhSERYcXVHN0lpeTgzT3dOenRvSHI0U09rY1d3Yw?oc=5) | Yahoo Finance |
| S33 | news | 2026-10-08 | [Credo Technology (CRDO) Joins the Co-Packaged Optics Race: Could It Unlock a New AI Growth Opportunity? - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxPOTBTdlNVSE1RWkFWbWotblZCSkNUY2E1bDlrbVpvY0RydzJnVWFFRzQzZ0UxNUlkS3ZFNW94Zy05UklBczV0WFltX20yYU40SUZUTkF2ZXhVNVdWSUF3dXpvenh6Qjk2dFlzNVE5b1JVZ0tadXVQQ1dBQ2tSZ0JRb1ZRMV9Ebmw0OU5vTHpxckRmTHdvU1RheDlR?oc=5) | Yahoo Finance |
| S34 | news | 2026-09-25 | [What Makes Credo Technology Stock A Buy Today? - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPMHVxdU9GUHdmR1RDNWFZb2RNa24xZEI4U00wV2NvVnV3ZGlCRGVyaENBaHNZWjRTRHFkWVlGYXBrbXRuem0xZ2Ywa3VHUzBhSTBxR081U0pEbEFNVnlGU3N0VjFDblJUTEc5RXJPNmlsak9rYjBzUXNoZVJlNllySmtELURNTm50RzBUZ0RrNTdoZUpWcThGWHB4eDl5UQ?oc=5) | Yahoo Finance |
| S35 | news | 2026-10-02 | [Up 30%, Should You Buy Credo Technology Right Now? - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxPUm9tcUtrMk9CMk5hOWVUU2N0Nm1aamdFZWVXWmFaamVueEN1VmdrMUEtTXgxZnBkWXhmS25LbDJpc0JVd281WlQ3YmdSaUN0a0dsU2R4WFNtVWNRSHhYZ2h1NzR4dllBR2FqUmFqQl9ScDRPRVhPakFnNlV5My1RWERNN3JXZV8wblVxcERhTlN4aER3bzU0?oc=5) | Yahoo Finance |
| S36 | news | 2026-09-25 | [Accelerating AI Data Center Infrastructure Demand Drives Credo Technology (CRDO) - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNeVJyUmZ1QkZHYkdObmJCN0Focm4xRlNKdlRTb2h1c05VVi1QWVRmRnc1b0tMRzFKQk1vb04wYkZHd3NOcHU3bkJ2WVhhaVFxdjZsbkgwUk9KUUQzME5EXzhKYWY0WHEyNkRzbTNHOThaZmZZeWVoNC1rUGN3ZzZwUEtyMXlRMlhaYnA4SlNxUTVyY213WGt3cVBrVmdxVU1UeFItSXlYUWc1UQ?oc=5) | Yahoo Finance |
| S37 | news | 2026-09-02 | [Credo Technology Group Holding Ltd Q1 2027 Earnings Call Summary - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxNaEFEREdsczV0ei05SmFvbmtXOEZrc2ZyZG1NdEx6V1lGWjlHTFduNk1oNDFfLWljdzF0d1JwblVxSjhMWjRsOF85WUJfWTROREhCNmJFbmpwTEFJUU5UVzRBalcyb3I4VjRMb0NYU1NTRDFzSktlQmdRRHVQODA2Yk1zODlGbW02QndkaEVvUUhmTElZaFRRaHhZN3YtRFE3?oc=5) | Yahoo Finance |
| S38 | news | 2026-10-15 | [Credo Technology Group Holding (CRDO) Starts New Optical Connectivity Standards Group - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxQRDZrcktpQ1BCbkVSMnRzQXpiT1JKSFhFUEwyamloUXc0WllEUHVqN0UtSHpGRUcxMjVWT1ZQWnRTalZ3NS10bFg4dXJWLXpNQ1RiRkJNOTJ6aVlYb3d6WHBKVWFjQXdYWm9UdEprSTlIYUJEYk5BdkdmV2xJTS1BbHozX3NLM0UtT21RUU15VW1ybmh1ZGloeFI0cVA?oc=5) | Yahoo Finance |
| S39 | news | 2026-09-27 | [Can Credo Technology (CRDO) Turn 1.6T Optical Transceivers Into Its Next AI Growth Driver? - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxPTjdrNEp3THhvSU1acF9wVjNxWFlQVEJEeUxxUmtyRE53aXJuSjhsSFY5M1BLb1hySTRQX2JBdW9HcENUT0JhRDhQMlpIaW04bW0wRWVjamVZSUxsU0RmN3VMR3VERUxDMFJHdElTZFRuVTBqa2tXeUZMLXRTUXNFM2hIMGZSSkl1TEJhckx3VTlJYjhZd0M0?oc=5) | Yahoo Finance |
| S40 | news | 2026-09-21 | [The Zacks Analyst Blog Highlights Credo Technology and NVIDIA - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxNeklZdGdWTnEtZGRMbUoxbnlmQzVibUg1STdkTVRSMmhxbGRyek0wcmpyem96MXZ5eV90SE1Lb01GWTFtTmZxN1dzTl9rejNOaUFEV25XaW1UMjFOZldaR2NldzdKVUJta2haNFlTNUp6bFlrVFppdk1tR3V5RGV6RHpmRUF3aWF2bDFPbkttVVN1YlIwUFg3Z1pYb000Q1FOQVE?oc=5) | Yahoo Finance |
| S41 | news | 2026-09-01 | [Credo Reports Q1 Fiscal 2027 Revenue Of $479 Million, Up 115% Year Over Year](https://pulse2.com/credo-reports-q1-fiscal-2027-revenue-of-479-million-up-115-year-over-year/) | 보도(2차 요약, 회사 8-K S3로 재확인 필요). Q1 FY27 매출 4.79억 달러(전년비 +114.7%, 전분기비 +9.6%), 비GAAP EPS 1.20달러, 비GAAP 매출총이익률 68.0%. 컨센서스 매출 약 4.718억 달러, EPS 1.17달러. Q2 FY27 가이던스: 매출 5.25~5.35억 달러, 비GAAP 매출총이익률 67~69%, 비GAAP 영업비용 1.00~1.05억 달러. FY27 전체 매출 성장률 전망은 출처마다 80% 초과·85% 초과로 엇갈림. 실적 발표 후 마진 우려로 주가 약 8~9% 하락. |

# Taiwan Semiconductor Manufacturing (TSM) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 근거 충분성** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✗ 주가·주식 수 없음 — 시장 가격과 비교할 수 없다

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: 주가·주식 수 없음 — 시장 가격과 비교할 수 없다

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ 주가 통화 USD ≠ 재무 통화 TWD — fx 사실 필요 (단위 TWD/USD)
## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| 매출 (revenue) | 1.34조 TWD | 1.59조 TWD | 2.26조 TWD | 2.16조 TWD | 2.89조 TWD | 3.81조 TWD |
| 매출 성장 (revenue_growth) | — | 18.5% | 42.6% | -4.5% | 33.9% | 31.6% |
| 총이익률 (gross_margin) | 53.1% | 51.6% | 59.6% | 54.4% | 56.1% | — |
| 영업이익률 (operating_margin) | 42.3% | 40.9% | 49.5% | 42.6% | 45.7% | — |
| 순이익 (net_income) | 5,107.4억 TWD | 5,923.6억 TWD | 9,929.2억 TWD | 8,517.4억 TWD | 1.16조 TWD | 1.72조 TWD |
| 영업현금흐름 (ocf) | 8,226.7억 TWD | 1.11조 TWD | 1.61조 TWD | 1.24조 TWD | 1.83조 TWD | — |
| 설비투자 (capex) | 5,072.4억 TWD | 8,392.0억 TWD | 1.08조 TWD | 9,498.2억 TWD | 9,560.1억 TWD | — |
| FCF (fcf) | 3,154.3억 TWD | 2,729.7억 TWD | 5,279.3억 TWD | 2,921.5억 TWD | 8,701.7억 TWD | — |
| FCF 마진 (fcf_margin) | 23.6% | 17.2% | 23.3% | 13.5% | 30.1% | — |
| FCF/순이익 (fcf_conversion) | 0.62x | 0.46x | 0.53x | 0.34x | 0.75x | — |
| ROIC (roic) | 42.2% | 53.6% | 62.4% | 40.8% | 51.4% | — |
| 순현금 (net_cash) | 6,601.7억 TWD | 1.06조 TWD | 1.34조 TWD | 1.47조 TWD | 2.13조 TWD | — |
| 희석 주식 수 (diluted_shares) | 259.3억 | 259.3억 | 259.3억 | 259.3억 | 259.3억 | — |
| 주식 수 변화 (share_change) | — | 0.0% | -0.0% | 0.0% | -0.0% | — |
| DIO(일) (dio) | 79.8 | 91.8 | 88.2 | 92.9 | 82.7 | — |
| 발생액 비율 (accruals_ratio) | — | -16.0% | -14.2% | -7.4% | -10.9% | — |

표에 없는 키도 인용할 수 있다: cash, cash_total, cost_of_revenue, debt_total, equity, gross_profit, income_tax, inventory, inventory_growth, operating_income, pretax_income, rnd, total_assets

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "base"}: leveraged=아니오

### 계산 경고

- 주가 통화 USD ≠ 재무 통화 TWD — fx 사실 필요 (단위 TWD/USD)

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-10-15 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000726/tsm-20261015x6k.htm) |  |
| S2 | filing | 2026-10-08 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000680/tsm-revenue20261008.htm) |  |
| S3 | filing | 2026-09-24 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000660/tsm-monthend6kx20260924.htm) |  |
| S4 | filing | 2026-09-10 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000658/tsm-revenue20260910.htm) |  |
| S5 | filing | 2026-09-01 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000552/tsm-dividendadjustmentx202.htm) |  |
| S6 | filing | 2026-08-25 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000545/tsm-monthend6kx20260825.htm) |  |
| S7 | filing | 2026-08-14 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000541/tsm-fsx20260814x6k.htm) |  |
| S8 | filing | 2026-08-11 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000539/sonysemiconductorsolutions.htm) |  |
| S9 | filing | 2026-08-11 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000536/tsm-boardx20260811.htm) |  |
| S10 | filing | 2026-08-10 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000471/tsm-revenue20260810.htm) |  |
| S11 | filing | 2026-07-24 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000459/tsm-monthend6kx20260724.htm) |  |
| S12 | filing | 2026-07-16 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000451/tsm-20260716x6k.htm) |  |
| S13 | filing | 2026-07-13 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000447/tsm-revenue20260713.htm) |  |
| S14 | filing | 2026-07-02 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000381/a20260702changeofaztreasur.htm) |  |
| S15 | filing | 2026-06-25 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000377/tsm-monthend6kx20260625.htm) |  |
| S16 | filing | 2026-06-10 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000367/tsm-revenue20260610.htm) |  |
| S17 | filing | 2026-06-04 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000302/tsm-agmx20260604x6k.htm) |  |
| S18 | filing | 2026-05-27 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000294/tsm-dividendadjustmentx202.htm) |  |
| S19 | filing | 2026-05-26 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000292/tsm-monthend6kx20260526.htm) |  |
| S20 | filing | 2026-05-15 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000280/tsmctosell81ofvanguardinte.htm) |  |
| S21 | filing | 2026-05-15 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000278/tsm-fsx20260515x6k.htm) |  |
| S22 | filing | 2026-05-12 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000275/a20260512boardofdirectorsr.htm) |  |
| S23 | filing | 2026-05-12 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000274/tsm-boardx20260512.htm) |  |
| S24 | filing | 2026-05-08 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000215/sonysemiconductorsolutions.htm) |  |
| S25 | filing | 2026-05-08 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000213/tsm-revenue20260508.htm) |  |
| S26 | filing | 2026-04-24 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000205/tsm-monthend6kx20260424.htm) |  |
| S27 | filing | 2026-04-17 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000203/tsm-boardx20260417x6k.htm) |  |
| S28 | filing | 2026-04-16 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000201/tsm_20260416.htm) |  |
| S29 | filing | 2026-04-16 | [6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000199/tsm-20260416x6k.htm) |  |
| S30 | filing | 2026-04-16 | [20-F](https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm) |  |
| S31 | filing | 2023-04-20 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/1046179/000119312523107214/0001193125-23-107214-index.htm) |  |
| S32 | filing | 2024-04-18 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/1046179/000119312524099840/0001193125-24-099840-index.htm) |  |
| S33 | filing | 2025-04-17 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/1046179/000119312525083423/0001193125-25-083423-index.htm) |  |
| S34 | filing | 2022-04-14 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/1046179/000119312522104891/0001193125-22-104891-index.htm) |  |
| S35 | news | 2026-10-01 | [Prediction: Taiwan Semiconductor Manufacturing Stock Will Skyrocket After Oct. 15 - Yahoo Finance](https://news.google.com/rss/articles/CBMitwFBVV95cUxPUUJwbWhobGxQZlR1emo1ejVPenVvXzdxejlhZFpjc2x5cXhSUWpNUmY2cS1ubE9LZ0ZHTnBzNEpDZGtmVzdvMFNtUEdpVy1ZdVRZNk5OdGdLSXV2YXF6X3BXamkwOEU2eWgtY2V6SDVCOWVxdWRHTVFBeElSemVoN1hzd2ljWUlwb3pQX3AzQ0JyNTVhTEFVTXRiTzVsa0dOR3o4cmhpTjlwNVRaTXpzbjV2VjF2Yzg?oc=5) | Yahoo Finance |
| S36 | news | 2026-10-15 | [Taiwan chipmaker TSMC explores Texas investment to expand production in the US - AP News](https://news.google.com/rss/articles/CBMipwFBVV95cUxPdWxqdEVyUzNvcUNVQVVJUnpWd1hWeHRLcVBfWWNSS1FpTWtpOXdKYk54REhBZGFxcVVZUVJ2NXdnZTQ2NktEbnRtREpOVUpMdEtMTmRnb3Iwb3g4VGRzUXV2T1QzVmFCZUZOdUpsSEY3STdDc1VRVjFuTlNPdmdlQ2F4enh1cWxEUzJtRFY5ZHJHcWVmNEtra0cyTnFna0FEWi0tSnV3bw?oc=5) | AP News |
| S37 | news | 2026-07-22 | [TSMC Arizona Megaproject Grows to $265 Billion - Engineering News-Record](https://news.google.com/rss/articles/CBMihwFBVV95cUxQWmVVY2pVa3FRRHNQY2JNVVRmR1ZZZTc2V1NCcXRKcm41OHZnYS1kS2hTaTJHZGJURmdJaHJWQUFNSy1GV3BuT2VUR2hlblVMdXpxeVZodnM3SE9mblBjM2xmb0NZeEFNSlQzdE5SQnhPODNiZUl3MElydlNxVjFFd0lMdXJtNXM?oc=5) | Engineering News-Record |
| S38 | news | 2026-10-14 | [TSMC 'prudent' going into 2027 after posting sixth straight quarter of record profit - Reuters](https://news.google.com/rss/articles/CBMixgFBVV95cUxOWE9HY3JEZl96LXVuQmdXM1I4VVBoUUI4d09uNk9qYUdDSXpBTE8zYnJsNUwxUEljLXJ2aTYxYW5rcnFza0duNVNVRnFCWVAzd19MSXVzUTc2cnhnZkxfaVNXS3I2b25JNlJHZnlpMmpiTkQ1NXF5cWNVTG5sRTk3TE9fZExqRExHcjRUa3EybXEzZ1JRNjJPYlZUTWVaMk5hdWJta0g0UWtHZ251dE5BLTk5bk9nYm5vTDh5alo5c05QT054QVE?oc=5) | Reuters |
| S39 | news | 2026-10-01 | [Prediction: Taiwan Semiconductor Manufacturing Stock Will Skyrocket After Oct. 15 - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOdEtDT1RRcWw1NFpRT0FlZ29UNnFOTl9td3BGRHFWZjlwNmVVdEpKT0FkNDVlYnk5U0c4cWUyX1YxTUFRZTFNY3VFVkhzVWFqWTlsU2tuNlpka21XQ01tU3drak9YQ29sbXBlVUlMMzVxYkMxVHhNMEkwVWhuaVVNTmpmLVFfcG5SYUo2RWNiX3lNZ2xHX0ZCRQ?oc=5) | The Motley Fool |
| S40 | news | 2026-10-15 | [TSMC Reports Third Quarter EPS of NT$29.43\\|Taiwan Semiconductor Manufacturing Company Limited - TSMC](https://news.google.com/rss/articles/CBMiTkFVX3lxTE53WTNKZC1rRTNpMk5IYXZOU2J1REhGZXdqNkduVDg2YVJvSHRVdHAxWlJGSldYTmJDVlZEeXhFaU9EU1V0T21fSzJYQ3NsUQ?oc=5) | TSMC |
| S41 | news | 2026-10-15 | [Taiwan Semiconductor Manufacturing Q3 Earnings Call Highlights - MarketBeat](https://news.google.com/rss/articles/CBMixgFBVV95cUxNYjd5WnY4cUZJRFZ1Y056dmJXZzZkeS1MU2VjUFUtN1diSkNMTmd0VTJDQlNHYWZkdEM1bGpwR0RRN01DRWl1bDJocHNZN09HUjZkN2xzaC1sMDVlcUxCNHl2ZHQ5QjM3Ql9DVm1DUzhweVdTcTE5Q3ZodmxGN2pZY1h1S1pwY1BBVUR0Y2NmelBUUW5uUlZpcEpwTl8yYUNabkhVa0FONWltYWJjb3A4QloyX0hHYnp1c2FuMk5NWndpNGR2LVE?oc=5) | MarketBeat |
| S42 | news | 2026-10-12 | [Taiwan Semiconductor Manufacturing Just Dropped a Major Bombshell Investors Must Be Aware Of - Yahoo Finance](https://news.google.com/rss/articles/CBMisgFBVV95cUxQZ1ZMNlp0SGtFN1hyQVBHS1lnZExnR3RQdVItWFoxZkJKSzExLXNoQ3hCNHNTcFJ3TXZpMWdVZnV6LU9jc0VIYnJQNTJZcV9zczVxLXBWdnl5OUFnekZrZVllcnZFSG9FeFlpeXhfUF9YaG93emt5ZkhMNEtJa2M0Mkk2U0t1aERCaTdxM01vQUQxMnFzZE1KTjU5U0dLdTB0aldRTHZ5QWN4WXBKczU2U193?oc=5) | Yahoo Finance |
| S43 | news | 2026-10-08 | [Taiwan Semiconductor Manufacturing Could Have Big News on Oct. 15 - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOSjItVVBFWjlSck0xNWp5b1lrR2VwMTJyUm1ZZkRScEpvMGdFS2k3UThoSU1sbnJiWUtBRHI3b2I2Uk1QekVqd1ZxaUwtVUM1Y2ZzcHdhTnFVUnB4Q05VZzJLLXdUSzhPLVhsaTlLUTIyaEhBeElUUENNdUJwaG1adEJKLWlmN2s2VmlwVElQWk9IMHkzbmFORQ?oc=5) | The Motley Fool |
| S44 | news | 2026-10-02 | [Taiwan Semiconductor Manufacturing (TSM), Why Is Fresh Attention Building Now? - Yahoo Finance](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOdVVleTZuaURydjNZdjd1aGtENVVwZmNnZm5FTUVBbTI0bVdXVzVQaTRteGpCSkJtM3R6Um55WGpzdFZiRlBPcElEcExueG1uUUE1YVpwMjVyOXRyRkF3S2NHVXZTQXdxekkwSTVyaElGcnFubXVrdmlGN2xhSWRJblFtY3RXekFWZk51R2RyeU9RMU5odGtyX2pkcXQzaXV2emdFWHVuWDR5TnM?oc=5) | Yahoo Finance |
| S45 | news | 2026-10-17 | [Taiwan Semiconductor Manufacturing (TSM) Is In Talks On A US Chipmaking Tie Up - Yahoo Finance](https://news.google.com/rss/articles/CBMirgFBVV95cUxQUnljT3Nub0lWUWl1VG1xTnV1MVdoTmZaR1F0X1FScUZtWG50Z25LUnFaWjd5SG5qMlI5dV9zd3hiejFTTmpqU3VhSHpKSnhZNWtrN1Z4OVY5Z1VNSU5odGducm5nSEEyekxkRTNOck9LTkJFbXgzNjJmMDc2R01HME92c2VUMDZLeS1yRmNUeE1zdlVyVmRlRk9TY3VyVnhnRUFudHhXeHprUkpBWXc?oc=5) | Yahoo Finance |
| S46 | news | 2026-09-02 | [Taiwan Semiconductor Manufacturing Company Limited (TSM): The Powerhouse of Advanced Semiconductor Manufacturing - Yahoo Finance](https://news.google.com/rss/articles/CBMitgFBVV95cUxNU09qeUg0QUZ0aVNnUkZTVjdFQmZ2SGtuaVktTndPbzBITzlmeXd3dzN4emZYM2lteE1JRkxoQjdreEtidEJva0N6Z1V1Y0lqYnloZG9oaUVYX2ZyaHlEQy1zaHdjdk9CbTNuZEw4TkhqQXgzQTVOenVVblNqdllvMGh4UEpWd2R0dGF4VWN1SWVyRnZIcDhNNUFfVkxROGsyOVJqVW5GVUVRbVVFQUpFR29vUjlLZw?oc=5) | Yahoo Finance |
| S47 | news | 2026-10-06 | [Taiwan Semiconductor Manufacturing Company Ltd. (TSM) Hits Fresh High: Is There Still Room to Run? - Yahoo Finance](https://news.google.com/rss/articles/CBMisAFBVV95cUxOM2RrM1prTy0wRUR1QlluWC1feTNXZWladnBxN1FJa3JIRnRUM1h2dmZ3YlVNamJVMW05V2w2UTE5NzBfcTBGYUV1UXZrMXJNU1BaQjdtM2RSSTZ5dXN1c1NNUjFVN2YxU2JhVHN2X2NxcW1nS3VROGp5UUtXQi1tdWhGR3RUaXBNeXpWTGxFSHVIVG1Wd2s5OXVjb2xUNkU2dEZVYzFhSm9ZYjNvZm9VTw?oc=5) | Yahoo Finance |
| S48 | news | 2026-10-16 | [Taiwan Semiconductor Manufacturing: 3 Key Takeaways for Long-Term Investors - Yahoo Finance](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPS05aQlpvQzJndHF6OTh6UmhEcnhWdzh0X050MGQ3Sm1JcVNMcW9yX3JUQzF2ZzFjbnJtTTRYcXBNLThZUHlLMVgtUkpzNXVERzdlSjllaXhScFFxdEpXd29FdVgxcnpSNnQ2eElCSGV6Q0c1YWhYeGVCeDlIMDRTME51bzZZamNPcE1DTVVBM2hDNkhGNUxNMFhSdzhldHFXai02UGZFTWw?oc=5) | Yahoo Finance |
| S49 | news | 2026-10-10 | [Taiwan Semiconductor Manufacturing (TSM) Posted Record Q3 2026 Revenue - Yahoo Finance](https://news.google.com/rss/articles/CBMirwFBVV95cUxPcElfVlVvc1NhWjVLY1piLWdNcUJvQWhnLUUtTS1Ud0pXbDU3RHJXaldRWEdqdzc4blo3eWFCVGF3Ul9OelNESVlWbTBuTXhEdHBVRmlKdUdTTXNVY2xMQjZWRzU0TGUyWUstXzgzaGV5dHZGaTZkTGtkNmJaQTZOWTh4WWgwYXdWQktqTkh2SlBzSFZvb0JucUo3WkN4VmpoQU5NajBwQzI5bkFOa3dr?oc=5) | Yahoo Finance |
| S50 | news | 2026-10-06 | [Investors Heavily Search Taiwan Semiconductor Manufacturing Company Ltd. (TSM): Here is What You Need to Know - Yahoo Finance](https://news.google.com/rss/articles/CBMirwFBVV95cUxOR1VXYU9OeDJiRXZlSzdMLTJWYUlOblVpbmR3UkhDZEdhVjM1RXNxRXBWOS1lSzc5UUNXYW9vQjV1cHQ4SHVwTDFfV0lrRnNzT05PRGJLUEZESXVkQkNWZV9iTDhDNlJpX2VCWU9zWGVZZlpXajZsTktZbnJiMHlNckRiQWcwb1RjY2JZb0xjOHJqT3hwWDVlSkZ1dTlxVllKQ1FZSFZkX3Exa0F1akN3?oc=5) | Yahoo Finance |
| S51 | news | 2026-10-16 | [Taiwan Semiconductor Manufacturing Co Ltd (TSM) (Q3 2026) Earnings Call Highlights: Record ... - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQbHR5ODFTMGdGa0x4aGdkeFo3V293ajhVQmJFNXR1azBMYTY5Q0RZeHlYYnBBUUE0dzFSdlJVcXJSb25na1lMdFNETXdKMGxYZ19RMm1FaEpxZ0NyTk52NDM1eDFXLUlQNDNFcUJYVDRFNmktcVJubkl5MW5BVjNwVHczQUd1Uk0wVmlaU3VlQTAzTmlGQkw0ZHhZbXZHLWZYRHRyTVM5UE9HZw?oc=5) | Yahoo Finance |
| S52 | news | 2026-10-14 | [Taiwan Semiconductor Manufacturing And 2 AI Chip Stocks To Watch - Yahoo Finance](https://news.google.com/rss/articles/CBMipgFBVV95cUxNY2VieU9KcFNRcTRmbWowY0pOd2dvZ2hDSzRDNDBhM0RoVWo4Y05vWTByUXk2a0hpSU1HVks1SXYtdFhZbi1OVXFtVnpFTHZNVU5RelJoM2EzYmdCQURqQkkwd1RDNHlSUW9fbmZnZ1ZvZ2wwOFZFaXNnQk1Pd1lJYUpxblp6cEJtZUNzaXo5U0N3TWNJUzYzdnZUanBOeGt3M2lOMHBR?oc=5) | Yahoo Finance |
| S53 | news | 2026-10-12 | [Can Taiwan Semiconductor Manufacturing (NYSE:TSM) Justify Its Price On Cash Flow? - Yahoo Finance](https://news.google.com/rss/articles/CBMirAFBVV95cUxPcFhudVBYZGM4RGFoUWhHSFo4UUdRRlhCY2ExMDNVUDNoUUlUMEpXREFVUXdVS1JlWTZPUWRMUkpWalMtNWtBRUVhbzJPbFVOcy1ld1lGM3hlRVk4UDhUdW1ZdXhyNWFfaVpmX0l5TzU5SFBfRUM2M0hzYWx5cWllMjIzaXFDZl9zRnhSemdHNGt0ZWQ2NXpUcm5VZnV5cVo1UlhUd3NXTDNpQ0Ru?oc=5) | Yahoo Finance |
| S54 | news | 2026-10-08 | [GlobalFoundries Signs $2 Billion Silicon Supply Deal With Taiwan Semiconductor Manufacturing - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxNY2ZPUml0X2VTR08xUTkta283RkNQck9QVlVoWTZkRVRmOGVMNHRaUGl1NnJqeW5PNHJmN3FUYVZWVTlfTElUalBld3FYdDJBdXNnamptUkNTMnZDcGNvMzA1SXhpWWJNYnJodERrckFXYm5HTjh1WkZfN0I4LWs0YXp6SzlzVXpjdEFSbGRRVWp6bkVoZDhrSEJ5alBxcDUyNmc?oc=5) | Yahoo Finance |
| S55 | data | 2026-10-16 | [TSM (NYSE) 일별 종가 이력 — StockAnalysis](https://stockanalysis.com/stocks/tsm/history/) | TSM ADR 종가 2026-10-16 USD 412.61, 10-15 422.25, 10-14 430.00, 10-13 445.12, 10-12 444.35, 10-09 453.31, 10-08 457.99, 10-07 472.20. 어닝 발표(10-15) 전후 약 12.6% 하락(10-07 대비 10-16). |
| S56 | filing | 2026-10-15 | [6-K — 3Q26 실적 발표 및 4Q26 가이던스 (a3q26e_withguidancexfinal)](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm) | 3Q26 매출 NT$1,494.24bn(전년比 +50.9%), 매출총이익 NT$992,379백만(총이익률 66.4%), 영업이익 NT$876,445백만(영업이익률 58.7%), 순이익 NT$763.06bn(전년比 +68.7%), 희석 EPS NT$29.43(ADR 단위 US$4.60). 4Q26 가이던스: 매출 US$52.3~54.3bn, 총이익률 65~67%, 영업이익률 56.5~58.5%, 환율 가정 US$1=NT$31.8. 보도에 따르면 2nm 초기 비용으로 총이익률·영업이익률은 2Q 대비 하락. 이 문서에는 3Q 영업현금흐름·설비투자·현금과 연간 설비투자 가이던스가 없음. |
| S57 | call | 2026-10-15 | [TSMC (TSM) Q3 2026 Earnings Call Transcript — Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/10/15/tsmc-tsm-q3-2026-earnings-call-transcript/) | 3Q26 어닝콜 원문(이번 조사에서 본문은 읽지 못함 — 요약·헤드라인만 확인). 보도 요약: 매출이 자체 가이던스를 상회, 2nm 생산 확대, 2027 전망에 신중(Reuters 'prudent'). 설비투자·AI 수요·2027 성장 발언은 원문 확인 필요. |
| S58 | news | 2026-01-15 | [TSMC Delivers Record 2025 Revenue and Profit as AI Chip Demand Fuels Growth, US Expansion Accelerates - Telecom Lead](https://telecomlead.com/semiconductor/tsmc-delivers-record-2025-revenue-and-profit-as-ai-chip-demand-fuels-growth-us-expansion-accelerates-124150) | 보도(2차 자료). 날짜는 4Q25 실적 발표일 기준으로 둠. FY2025 매출 NT$3,809.05bn(+31.6%), US$122.42bn(+35.9%), 매출총이익률 59.9%, 영업이익률 50.8%. 순이익 NT$1.7178조·EPS NT$66.25는 이 검색에서 단일 출처 보도로만 확인됨. |
| S59 | news | 2026-01-15 | [TSMC 2025 Q4 earnings — VectorShift](https://vectorshift.ai/research/companies/taiwan-semiconductor-manufacturing-co/earnings/2025-q4) | 보도(2차 자료). 날짜는 4Q25 실적 발표일 기준으로 둠. 4Q25 영업활동현금흐름 약 NT$726bn, 설비투자 NT$357bn. 4Q25 설비투자 US$11.51bn, FY2025 설비투자 US$40.90bn. 연간 NT$ 설비투자와 연간 영업현금흐름은 확인하지 못함. |
| S60 | news | 2026-10-15 | [TSMC Q3 Revenue Rises to $46.7B With a 66.4% Gross Margin - FourWeekMBA](https://fourweekmba.com/ai-tsmc-q3-revenue-rises-to-46-7b-with-a-66-4-gross-margin/) | 보도(2차 자료). 3Q26 매출 US$46.72bn, 매출총이익률 66.4%, 매출이 자체 가이던스 상단 상회. |
| S61 | news | 2026-07-21 | [TSMC post-Q2: AI drives beat, outlook raised; higher capex weighs on sentiment - S&P Global Market Intelligence](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/tsmc-postq-ai-drives-beat-outlook-raised-higher-capex-weighs-on-sentiment) | 보도(2차 자료). 2Q26 콜에서 2026 설비투자 가이던스를 US$52~56bn에서 US$60~64bn으로 상향. CFO는 향후 3년 설비투자가 직전 3년보다 크게 늘 것이라고 발언(보도). 3Q26 콜에서의 변경 여부는 XTB 요약이 US$64bn 언급(미확인). |

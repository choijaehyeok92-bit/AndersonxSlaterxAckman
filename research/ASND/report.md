# Ascendis Pharma A/S (ASND) 리서치 보고서 — 기준일 2026-10-18

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
| 매출 (revenue) | 778만 EUR | 5,117만 EUR | 2.7억 EUR | 3.6억 EUR | 7.2억 EUR |
| 매출 성장 (revenue_growth) | — | 557.9% | 421.2% | 36.3% | 98.0% |
| 총이익률 (gross_margin) | 54.7% | 76.3% | 83.4% | 87.8% | 86.8% |
| 영업이익률 (operating_margin) | -5808.6% | -1097.9% | -170.8% | -76.7% | -18.9% |
| 순이익 (net_income) | -3.8억 EUR | -5.8억 EUR | -4.8억 EUR | -3.8억 EUR | -2.3억 EUR |
| 영업현금흐름 (ocf) | -4.2억 EUR | -5.0억 EUR | -4.7억 EUR | -3.1억 EUR | 5,390만 EUR |
| 설비투자 (capex) | 2,370만 EUR | 1,449만 EUR | 244만 EUR | — | — |
| FCF (fcf) | -4.4억 EUR | -5.1억 EUR | -4.7억 EUR | — | — |
| FCF 마진 (fcf_margin) | -5674.4% | -997.0% | -176.1% | — | — |
| 순현금 (net_cash) | 4.5억 EUR | 4.4억 EUR | 3.9억 EUR | 5.6억 EUR | 6.2억 EUR |
| 희석 주식 수 (diluted_shares) | 5,477만 | 5,607만 | 5,629만 | 5,789만 | 6,061만 |
| 주식 수 변화 (share_change) | — | 2.4% | 0.4% | 2.9% | 4.7% |
| DIO(일) (dio) | 7,812.3 | 3,929.8 | 1,717.8 | 2,437.9 | 1,159.6 |
| 발생액 비율 (accruals_ratio) | — | -8.0% | -1.5% | -7.2% | -22.7% |

표에 없는 키도 인용할 수 있다: cash, cash_total, cost_of_revenue, debt_total, gross_profit, income_tax, inventory, inventory_growth, operating_income, pretax_income, rnd, total_assets

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "base"}: leveraged=아니오
- 클라만 case={"from": "base"}: leveraged=아니오

### 계산 경고

- 주가 통화 USD ≠ 재무 통화 EUR — fx 사실 필요 (단위 EUR/USD)

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-10-16 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526423938/d167361d6k.htm) |  |
| S2 | filing | 2026-10-14 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526421789/d743945d6k.htm) |  |
| S3 | filing | 2026-09-29 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526407293/d153773d6k.htm) |  |
| S4 | filing | 2026-09-15 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526390877/d183438d6k.htm) |  |
| S5 | filing | 2026-09-15 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526390874/d52763d6k.htm) |  |
| S6 | filing | 2026-09-09 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526386630/d152057d6k.htm) |  |
| S7 | filing | 2026-09-09 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526386434/d32116d6k.htm) |  |
| S8 | filing | 2026-08-31 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526376733/d139239d6k.htm) |  |
| S9 | filing | 2026-08-13 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526348046/d31437d6k.htm) |  |
| S10 | filing | 2026-08-13 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000161204226000016/asnd-20260630.htm) |  |
| S11 | filing | 2026-08-12 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526347172/d135787d6k.htm) |  |
| S12 | filing | 2026-08-06 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526337270/d169607d6k.htm) |  |
| S13 | filing | 2026-07-15 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526304903/d109910d6k.htm) |  |
| S14 | filing | 2026-06-30 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526290485/d93159d6k.htm) |  |
| S15 | filing | 2026-06-29 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526288414/d22299d6k.htm) |  |
| S16 | filing | 2026-06-17 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526274306/d78361d6k.htm) |  |
| S17 | filing | 2026-06-15 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526270227/d48156d6k.htm) |  |
| S18 | filing | 2026-06-12 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526268415/d136465d6k.htm) |  |
| S19 | filing | 2026-06-10 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526265829/d85296d6k.htm) |  |
| S20 | filing | 2026-05-13 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526221597/d865415d6k.htm) |  |
| S21 | filing | 2026-05-07 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526210386/d121855d6k.htm) |  |
| S22 | filing | 2026-05-07 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000161204226000005/asnd-20260331.htm) |  |
| S23 | filing | 2026-04-21 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526167208/d91071d6k.htm) |  |
| S24 | filing | 2026-04-21 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526165330/d139196d6k.htm) |  |
| S25 | filing | 2026-04-20 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526162766/d620541d6k.htm) |  |
| S26 | filing | 2026-04-16 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526157347/d134243d6k.htm) |  |
| S27 | filing | 2026-04-08 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526147597/d118310d6k.htm) |  |
| S28 | filing | 2026-04-08 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526147577/d132436d6k.htm) |  |
| S29 | filing | 2026-04-07 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526144463/d121667d6k.htm) |  |
| S30 | filing | 2026-03-30 | [6-K](https://www.sec.gov/Archives/edgar/data/1612042/000119312526131753/d127945d6k.htm) |  |
| S31 | filing | 2024-02-07 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/1612042/000095017024012212/0000950170-24-012212-index.htm) |  |
| S32 | filing | 2025-02-12 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/1612042/000095017025018852/0000950170-25-018852-index.htm) |  |
| S33 | filing | 2026-02-11 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/1612042/000119312526046590/0001193125-26-046590-index.htm) |  |
| S34 | filing | 2023-02-16 | [20-F (XBRL)](https://www.sec.gov/Archives/edgar/data/1612042/000095017023003068/0000950170-23-003068-index.htm) |  |
| S35 | news | 2026-10-16 | [Ascendis Pharma A/S (ASND) Stock Price, News, Quote & History - Yahoo! Finance Canada](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9EOVJNcG5FM21pY0NPNEJDVzVLbUhTT05JUkhKb2FxbzNUZEZ4dGJEWnNaR1h6QUkyZXoxU0tDZ0ZtdVBEY3dXOXNmTDRlcV9iZ3c?oc=5) | Yahoo! Finance Canada |
| S36 | news | 2026-08-13 | [Ascendis Pharma A/S Q2 Earnings Call Highlights - TradingView](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOdUJFVXhFNDdmaGU5NEJqWDgycEdZZFdkMV9iM3hQZWJIWDhqLXp2ZVVoWmFxR0JIQnMtMlNqV0RzNmEwSDdfaENpOGhJbXNLc2w0cGYzMVJkc1ZweVgtV25DaVlfZVhkZWFEZGlMY0FnZi1xWWtCcVVrNkVaY1paUXdUVTJUcm96eEZ2aVh6N0Y1bkxIZV9uT3hSVHBHeUlBZTFJSlZHTmwtZ00?oc=5) | TradingView |
| S37 | news | 2026-10-03 | [Ascendis Pharma (NasdaqGS:ASND) Stock Price - Simply Wall Street](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5MZnBMYU94VVhYYWcwd05DVWNXTDBkNEw1MFU1M2toTVpKUUZ6N3FFN1dfNUYzdm9ZNlVrbGxpM1NKU3BPTDc1YmF1WFh0YUFlSHFV?oc=5) | Simply Wall Street |
| S38 | news | 2026-09-08 | [Ascendis Pharma to Participate in the Morgan Stanley 24th Annual Global Healthcare Conference - GlobeNewswire](https://news.google.com/rss/articles/CBMi-AFBVV95cUxQMndMeTdpclVMNm5XZTVwcG5IQ0hFZTNkdWwxUk5sSHdObWNIOEJ4MkVjMEdPdk1mbzNsN1NHc0NTMEk4YUVEV3hTblYwdnZUbDdGTlFyRVI1UGw0MXlsMEMwN19hXzhPbzJSVzhyQUU5SkU5VGU1SlpzNDZaWG5tckRWX2ZjZGQ3ak9tQVFHcm5pWXUtdl8xbWszbjlRbEFYSUstaXRjU2RWR1NwUEMyWGE0cnp6ZENSaEZhWFV4OE1fTG9fbUd6NnZSaHZhU0lTY0dkRk9JYUwyNFJqei00VVlOUGtqWlNwQWU0SW9ZU3VPcl9uWk1xUA?oc=5) | GlobeNewswire |
| S39 | news | 2026-08-13 | [Ascendis Pharma Reports More Than 220 U.S. YUVIWEL Enrollments - Stock Titan](https://news.google.com/rss/articles/CBMirAFBVV95cUxONHVXM2EtWkc1M1padi16bnF0YW52elAyM25UMHp4RnlqMzctdTdMMV9UNDZVTWN1NThwTUN6Q25YZ2NWLUdxeUFndFBaWE5leUZCb28yRE9Fdi1nNGdmZzFRMmhBd0VnTlBFOFBQZW10MU1jNVZhYVpVcDNReHh5WFB4TXREenh3ZnVmXy03bmpLbWcxRzFGVXJyNUV4ZnRsUnBsV3ZSUE9TTUJD?oc=5) | Stock Titan |
| S40 | news | 2026-09-16 | [Ascendis Pharma: Back To Full Independence (NASDAQ:ASND) - Seeking Alpha](https://news.google.com/rss/articles/CBMiigFBVV95cUxQam9fZWc1Q2hyWEhxNllSQ1dGdGJKdU1mWUM0SE5qUmxKa21DUlRmU1gxQjBtOFpGeklNWVNvZ2VBQUE2b0J4Q2dpT2w0Zm9IWnFzSGZCZDhYOXhLdXFfRHZBOGp2bzNRSDZobzlSQk5jVDNBVU5mcnRkWVIwdWRabm9oelJlN1JWbHc?oc=5) | Seeking Alpha |
| S41 | news | 2026-10-12 | [Morgan Stanley Initiates Ascendis Pharma A/S(ASND.US) With Buy Rating, Announces Target Price $273 - Moomoo](https://news.google.com/rss/articles/CBMipwFBVV95cUxQdTdmbVJFYTdjX25mbGxMaEhsZFBUR0pxZUppbVJ0TV9leERyR3JNbW5RR3JfRTZ2QzdNdVRaaGhJU2h1N1JkT25mY1RJMmlncV9Ed2tpWjRIVmFCMUVHT1JqcDJkRXhTdUdUaFV4RGZSQjdueFlqTHRkYVp6bVhOU2JuVUNTeHRyeGw1UmkzTndSdGU0Zl9jU2owS3JxTFNadXVYUURSWQ?oc=5) | Moomoo |
| S42 | news | 2026-09-15 | [Ascendis Pharma A/S Stock (ASND) Moved Down by 12.08% on Sep 15: What Signal Does It Send? - TradingKey](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQNnRHZTVhRTFWTmUwVkx3Y0hjeWU4cFZSeEVLemtmZ2lhZ1JOQkR2UjJkOFFscXRBNEtISFJWNkp3RlcwcHdZWFFDMEJ6WTRZN3NmRFdkaUk0aVZ1WmV5b0MtNnpTMy1acUp2dW9VWnNzUFFmX3RMaDZoNUtuaEJFUUc0VHdtREtiNUJR?oc=5) | TradingKey |
| S43 | news | 2026-10-14 | [Employees receive 35,890 warrants from Ascendis Pharma (ASND) at a $223.21 exercise price. - Stock Titan](https://news.google.com/rss/articles/CBMitgFBVV95cUxNdU1tSTlnWlJ5R0Z4Mm9UNUkzbjc2dVMwUHhwd3JiUlR5N1JIeTNoSGpXVlNOcndKWlVKQ0RzUzhPNmtqWW56TFQxYzY3RTZkSElZOXJVMk81RnZVbE5hcVkwVGRlRmgtRkpOdGFDODRlTlRfcHRXWFU3UDZPQkxxUERjUERaMXE0R2l3a1NwS0p4SmlYWEtyVFVhZnJvUXNYTnNVZzFEaDNTcHQtWmVsTFEtdW9PUQ?oc=5) | Stock Titan |
| S44 | news | 2026-08-27 | [HC Wainwright Initiates Coverage on Ascendis Pharma A/S With Buy Rating, $345 Price Target - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOaVd3eHJkZzViUE1KOVZfcWNudnBPX3MzazdGeDhiRllCS1F1YmlWdm5VVk0zaVZZVEZMc1lsTThFVUdoUDNFbnUxSEFrV2dNWkdGNjJvMy1tTzRNdmtTWkpjRGJ4VlFEcDJqdVNhMlVRWWhNLXB0N2F0VmRzbHBBeXhnVlJsNE41dk9OcDBOVWU2RTUzS2ZCM1FsMlFwYjdDR0E3MEpnT3I2dw?oc=5) | Yahoo Finance |
| S45 | news | 2026-10-16 | [EU advisers weigh in on once-weekly TransCon CNP for children at Ascendis Pharma (ASND) - Stock Titan](https://news.google.com/rss/articles/CBMitgFBVV95cUxOOUV5eUdjYWplbmNVc0hRaWFuT0RteWVjRUZXV3E1c18xakI4Xzc5Mk94T3N3RUF5S3Z0ZWJxa0czdm1xZXJLLWtSemVQMjZTRmphTnFIaF9XaUFsRmFyeVo5c2s0dWRJTGhfTkl5U0hZQlY0RjhoWEh1UDRkNVFlbjh2MU5QTDJtVy1UOVZLX0dMR2JlUWZybEMtbzd6OXZmMUlhZmJxNGFWUXAwRXd4VWZLUFRPQQ?oc=5) | Stock Titan |
| S46 | news | 2026-08-21 | [Ascendis Pharma (ASND): Three New Drugs Are Turning This Biotech Into A Growth Machine - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxObVB2N29uMk1WYmhhcXNFSjE0N00zOFhQTjYyYy12VmxqN0RyazYxZUlhMmdrM2RhRE96dTBjWF82UUduTmZaX08xNDFMRDdDN3JNeVpZTFVYbmV3RnpoeUVRb0VQSjFSYTBwaXV1SWdnTXZ5X2hkdjdUN0VuNUk1cjdqZEVEVTBBenZ3TUlCdEtMbHE1ZzljXw?oc=5) | Yahoo Finance |
| S47 | news | 2026-09-29 | [At about $123.36 per share, warrant exercises add 210,812 shares at Ascendis Pharma (ASND). - Stock Titan](https://news.google.com/rss/articles/CBMitgFBVV95cUxNTV94WmdkVWFYTGEtUUpvNWxVZlhuajNPZ0cyWUNYRFJkMmVMZnpaT0QzbW9ORVV2Mnl0ZUZSNFdQUlBvVUxKQVU5MHI4cmcxSGVoRlVGYXVEZ1lYdk9hengxdmJzQ1dhWXNvLXZIdk1Rbm52TlBycjZSblByZHhDYWo3cXFtYzhOTW4zSTBBRnlWTE5OVFF0dGJNTFZMT3RKSjZxOHBJLV95RUtxRGNQalFReXdqQQ?oc=5) | Stock Titan |
| S48 | news | 2026-09-17 | [Ascendis Pharma (ASND) Will Regain Metabolic Drug Rights. Is Greater Ownership Worth the Cost? - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxQLU9FT0RRb3FhY1VNcW9qc1pLdVJncjljS2hFNHlXcmp5Tm15S3ZXOXdKRUZRN3hkM1J1UjJHNUNES1htTUQxZnRLXzhCVFJlNDl4QWVBVG40SUc1YVktVlFJYV91NS1vWTlPOWpFSy1XQVhPb1prcWdVbWUzcXE5aEh5M3NMTmxDWXNBVUNjX1RjT3FVemlXV0RsbFB1ZFk?oc=5) | Yahoo Finance |
| S49 | news | 2026-09-15 | [Novo Nordisk deal ends as Ascendis (NASDAQ: ASND) takes back obesity drug rights, with more programs shifting over - Stock Titan](https://news.google.com/rss/articles/CBMitgFBVV95cUxObEV1c05rMXI1T3VwalBRR1R5amdCeXlXcVM4VVpYa1lMc0hPYnNsZHNrZDVQZl9yRVNnMF9FRFVMRDBycXVUVEgyalg2U084aElBTG5GOUN5dkJVd2tiODVMZXl6b1dGM01CNnFGc3VkcFFubDlNVlduaVA4RDdQU1o2LVFXVVgyMzlRT2VzSG1PTGotTlF0d0RPSG9zMVFZenpQNVN5M05hRkxILUZrdVpFWl9VUQ?oc=5) | Stock Titan |
| S50 | news | 2026-09-20 | [Ascendis Pharma (ASND) Authorizes $400M Share Buyback - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxOX3BRdUlYU2g1NmVJLTM1VXRPSGxlamR3T1BCRDVVTTB3Z213VnFjdDQ5VVVlODJtNEhnQTZpcDMxaUdSZ25TRTBzZEFuUUJzdXllNTBEcC00ZkJiMkFnWWdwbWt2dkN6bjE1TlE0MnF6TlRXbTVzbGVPUER3MHg3R0tWQ2ZDSEpJNUhkSF9YdTQ5R3VvV2YxZkExY0VpTm9ZWlZv?oc=5) | Yahoo Finance |
| S51 | news | 2026-09-15 | [Ascendis Pharma (NASDAQ: ASND) board okays discretionary $400M share buyback - Stock Titan](https://news.google.com/rss/articles/CBMitgFBVV95cUxOTTFnQmFrN1lxeENBcVppV1F2Z19MQVhuMThjcHV6bHhOX0tYak9YN3V2MzdyQ0loeHFsekdFZnQ2Umowazl4aVJVU0Q1NVI5d1hVU0RNUWU3VzJ5d0FIVXhjUHdRUTEtTVZNa0RYbzhUMWEtVWVyNVRmSHk4TV9qdDY4SUhQeTUzNEt3Ty1zTS1DOEJkZVZBT0djSWJvWjZkZ05SMW84Q2F5R0kwZEwzR3JqbUhZdw?oc=5) | Stock Titan |
| S52 | news | 2026-10-16 | [UBS Adjusts Ascendis Pharma A/S Price Target to $269 From $307, Maintains Buy Rating - Moomoo](https://news.google.com/rss/articles/CBMimwFBVV95cUxOQTVsanpVelJISlR6TGZLV0pjbTg4d1ltSk9kZWhqMGNMazkxWEZ5YUhjaENuVmtnRXFXdy10bmZtaUxVMnRjcXdMbGtHRWZoMEJUTmYwX3BmWEpGQjh6WmFhYkRXQ2stR2NNbkNGWU03d2I2alllVjZWcjE4MW1xMUg0cXJEZzZZUnNIbWVaQ0Jyc3l1eng5ZXZBdw?oc=5) | Moomoo |
| S53 | news | 2026-09-14 | [Ascendis Pharma Regains Rights to TransCon Metabolic and Cardiovascular Programs, Including Once-Monthly TransCon Semaglutide - Quiver Quantitative](https://news.google.com/rss/articles/CBMi8gFBVV95cUxPOS1MdzFyanNaNzMwZDB1N1F1OGVPR2xjUnZYX3V5LVdNU0NQR2JtR1VoOEdkRkxjY0FRVzIxTDZWcm93VHBhZ2NHSnZhTm92dXNvWmpWTHFIMlVPY21mN0tLVFZJTmo1YTQ2dGpOU082X1U5eXhFNHUyd3BzWUNSTUZfQmVzS19tUnJPMm1DQWdINThRaUxEampoYUY3ZkEzaF9LWUgxaTNPbUdqLVVUNW93MnpKMlFzb00tZUhxRHE3cUp5LUt6dUVZQjhfWFA4QkljTUdoYURmV29oTkgxWDRlMGRXc3pjTlFqUFNqdXNtQQ?oc=5) | Quiver Quantitative |
| S54 | news | 2026-08-06 | [Ascendis Announces COACH Week 78 Results and Provides - GlobeNewswire](https://news.google.com/rss/articles/CBMimAJBVV95cUxOSjB6b05ObkY5QmNxeXFRU25vdzNJVjNoUVh2M1UxaUh0X09aT25iSkxfSGozdFctTFFFaE81U3pRSDZLcGplZU5kX2M4SzBuaXdyODljV1VTN2taSmw1VVdHcldSYnltWGRCZkwyYm5mTVgzeG5sd0gwVEZoR3R1NC1NZVNGQWtzbzdDZG9yUjdyVG9zSGJxS2VtNkN2cDkzdzlKVHlNWktxak9jblBPdHhWVWtkQWFabDlzbDd0R1RBTV9SN1pPY2F6RHNTS3FrcWtEd242U3JPdUgyblJjOVc3RU1ESVkwNm1MZmlmTjMzQUpJbm5DSVIwSF9CekhxcnBvVW9XejNueVZYMllZSEM3S3lQVVBN?oc=5) | GlobeNewswire |
| S55 | data | 2026-10-12 | [Why Ascendis Pharma A/S's (ASND) Stock Is Down 12.50% - AAII](https://www.aaii.com/investingideas/article/543156-why-ascendis-pharma-as8217s-asnd-stock-is-down-1250) | 2026-10-12 오후 4시(CST) 기준 ASND 주가 $227.00, 직전 종가 $229.230 대비 -0.97%. 10월 16일 종가는 찾지 못했다. 다른 날짜의 참고치: 10월 2일 종가 $227.87(chartrow). 같은 시기 증권사 목표가는 모건스탠리 $273(10/12 신규 매수), UBS $269(10/16, $307에서 하향), HC Wainwright $345(8/27 신규 매수) — 모두 언론 보도 기준. |

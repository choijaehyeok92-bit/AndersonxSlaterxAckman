# Taiwan Semiconductor Manufacturing (TSM) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 모델** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✗ model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

## 1. Variant perception

- 시장이 반영한 것: 주가는 10-07 대비 약 12.6% 하락했고(S55), 하락은 '신중'한 2027 전망(S38)과 설비투자 상향(F99)에 대한 반응으로 보인다. 다만 근거에 하락 원인 분석은 없어 이 해석은 추정이다. 현재 P/E는 40배(C:pe)로, 시장은 높은 성장이 오래 가는 것을 가격에 넣고 있다. 컨센서스는 확보하지 못했다.
- 우리가 다르게 보는 점: FY2026 매출은 이미 거의 확정이다(F80, F87). 시장이 값을 매기는 것은 FY2027 이후의 성장 속도와 설비투자가 FCF에 미치는 영향이다. 우리 기본 시나리오는 FY2027 성장이 둔화하되 이어지고, FCF 마진이 설비투자 정점 이후 FY2024 수준으로 회복한다고 본다. 여기서 알파는 크지 않다. 기본 시나리오의 기대수익률은 요구수익률 부근이며, 우위는 하락 시나리오의 폭과 확률에 대한 판단에서 나온다.
- 왜 우리가 맞는가: 마진이 높게 유지된 이력(C:operating_margin@FY2024, C:roic@FY2024)이 있고, 가이던스를 상회한 사례(F98, F109)도 있다. 그러나 가이던스 적중 표본은 1건뿐이고 컨센서스와 20-F 현금흐름 원문이 없어 확신은 낮다. [F80] [F87] [S55](https://stockanalysis.com/stocks/tsm/history/) [S38](https://news.google.com/rss/articles/CBMixgFBVV95cUxOWE9HY3JEZl96LXVuQmdXM1I4VVBoUUI4d09uNk9qYUdDSXpBTE8zYnJsNUwxUEljLXJ2aTYxYW5rcnFza0duNVNVRnFCWVAzd19MSXVzUTc2cnhnZkxfaVNXS3I2b25JNlJHZnlpMmpiTkQ1NXF5cWNVTG5sRTk3TE9fZExqRExHcjRUa3EybXEzZ1JRNjJPYlZUTWVaMk5hdWJta0g0UWtHZ251dE5BLTk5bk9nYm5vTDh5alo5c05QT054QVE?oc=5) [F99] [C:pe] [C:operating_margin@FY2024] [C:roic@FY2024] [F98] [F109]
- 촉매: 4Q26 실적과 2027 설비투자·매출 가이던스, 그리고 어닝콜 원문에서 확인되는 2026 설비투자의 갱신 여부.
- 시점: 2027-01 (4Q26 실적 발표)

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 분석 모듈 (L4)

### 사업·산업 — proven

TSMC는 팹리스·시스템 기업(엔비디아 등 AI·모바일·HPC 고객)의 설계를 위탁받아 최첨단 공정으로 웨이퍼를 제조하는 순수 파운드리다. 고객은 선단 공정(3nm·2nm)과 첨단 패키징에서 대안이 사실상 제한적이고, 이에 따라 매출총이익률이 FY2024 56.1%(C:gross_margin@FY2024)에서 FY2025 59.9%(F92), 3Q26 66.4%(F85)로 올라왔다. 3Q26 매출은 전년比 +50.9%이고 영업이익률은 58.7%(F86)로, 단위(웨이퍼)당 경제성은 개선 중이다. 반면 설비투자는 2026년 US$60~64bn 가이던스(F99)로 급증해 FCF 부담이 커지고, 2nm 초기 비용이 마진을 일부 깎는다(S56). 고객 집중도·공정별 비중·웨이퍼 가격 등 해자의 직접 증거는 이번 근거에 없어 해자 일부는 '주장' 수준이다.

- [unit_economics] 매출 성장이 가속·지속 중이다. FY2024 +33.9%(C:revenue_growth@FY2024), FY2025 +31.6%(C:revenue_growth@FY2025), 3Q26 전년比 +50.9%(F80, S56). 분기 매출은 1Q26 1.13조(F102) → 2Q26 1.27조(F103) → 3Q26 1.49조 TWD(F80)로 연속 증가하고, 3Q26 USD 매출 467.2억(F98)은 가이던스 452.0억(F109)을 상회했다. [C:revenue_growth@FY2024] [C:revenue_growth@FY2025] [F80] [F102] [F103] [F98] [F109]
- [unit_economics] 마진 구조가 구조적으로 높다. 3Q26 영업이익 8,764.5억 TWD(F82)로 영업이익률 58.7%(F86), 순이익 7,630.6억 TWD(F83). 4Q26 가이던스는 총이익률 65~67%(F88), 영업이익률 56.5~58.5%(F89)로 3Q 수준을 유지하는 것으로 제시됐다. 2nm 초기 비용으로 2Q26 대비 마진은 소폭 하락(S56 보도). [F82] [F86] [F83] [F88] [F89] [S56](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm)
- [industry] 가치사슬에서 TSMC는 설계(고객)와 장비(ASML 등) 사이의 제조 병목이다. 선단 공정 설비투자가 FY2020 5,072.4억(F1)에서 FY2024 9,560.1억 TWD(F5)로 늘었고, 2026년은 US$60~64bn 가이던스(F99, S61: 직전 52~56bn에서 상향)다. 이 투자 규모 자체가 신규 진입을 막는 장벽이나, 동시에 자본집약도 위험이다. [F1] [F5] [F99] [S61](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/tsmc-postq-ai-drives-beat-outlook-raised-higher-capex-weighs-on-sentiment)
- [customers] 고객 집중도·상위 고객 비중·HPC/스마트폰 매출 구성은 이번 근거에서 확인되지 않았다(리서처 미확인). AI 가속기 수요가 성장 동력이라는 서술은 보도(S41, S51, S35)에 의존하며, 고객 협상력과 수요 지속성은 평가할 수 없다. [S41](https://news.google.com/rss/articles/CBMixgFBVV95cUxNYjd5WnY4cUZJRFZ1Y056dmJXZzZkeS1MU2VjUFUtN1diSkNMTmd0VTJDQlNHYWZkdEM1bGpwR0RRN01DRWl1bDJocHNZN09HUjZkN2xzaC1sMDVlcUxCNHl2ZHQ5QjM3Ql9DVm1DUzhweVdTcTE5Q3ZodmxGN2pZY1h1S1pwY1BBVUR0Y2NmelBUUW5uUlZpcEpwTl8yYUNabkhVa0FONWltYWJjb3A4QloyX0hHYnp1c2FuMk5NWndpNGR2LVE?oc=5) [S51](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQbHR5ODFTMGdGa0x4aGdkeFo3V293ajhVQmJFNXR1azBMYTY5Q0RZeHlYYnBBUUE0dzFSdlJVcXJSb25na1lMdFNETXdKMGxYZ19RMm1FaEpxZ0NyTk52NDM1eDFXLUlQNDNFcUJYVDRFNmktcVJubkl5MW5BVjNwVHczQUd1Uk0wVmlaU3VlQTAzTmlGQkw0ZHhZbXZHLWZYRHRyTVM5UE9HZw?oc=5)
- [runway] 재투자 활주로는 넓지만 현금전환은 낮아지고 있다. FY2024 FCF 8,701.7억 TWD, FCF 마진 30.1%(C:fcf_margin@FY2024)였으나 FCF/순이익은 0.34~0.75x로 변동(C:fcf_conversion@FY2023, FY2024). 2026 capex 상향(F99)과 미국 애리조나 프로젝트 확대 보도(S37: 총 $265bn)는 FCF를 압박할 수 있다. 2Q26 OCF 7,830억 vs capex 4,960억 TWD(F106, F107)로 분기 FCF는 양(+)이다. [C:fcf_margin@FY2024] [C:fcf_conversion@FY2023] [C:fcf_conversion@FY2024] [F99] [S37](https://news.google.com/rss/articles/CBMihwFBVV95cUxQWmVVY2pVa3FRRHNQY2JNVVRmR1ZZZTc2V1NCcXRKcm41OHZnYS1kS2hTaTJHZGJURmdJaHJWQUFNSy1GV3BuT2VUR2hlblVMdXpxeVZodnM3SE9mblBjM2xmb0NZeEFNSlQzdE5SQnhPODNiZUl3MElydlNxVjFFd0lMdXJtNXM?oc=5) [F106] [F107]
- [runway] 재무 완충은 두껍다. 현금 FY2024 2.13조 TWD(F10), 자기자본 4.24조(F25), 희석 주식 수는 5년간 259.3억으로 불변(C:share_change@FY2024)이라 희석 위험은 없다. 부채 최신값은 확인하지 못했다. [F10] [F25] [C:share_change@FY2024]
- [industry] 수요 사이클·재고 신호: FY2023 매출이 -4.5%(C:revenue_growth@FY2023)로 역성장했고 그해 영업이익률은 42.6%로 하락했다. 반도체 수요 둔화에 노출되는 사이클성이 있다. 경영진은 2027 전망에 '신중'(S38 보도)이라 했으나 구체적 내용은 어닝콜 원문 미확인(S57). [C:revenue_growth@FY2023] [C:operating_margin@FY2023] [S38](https://news.google.com/rss/articles/CBMixgFBVV95cUxOWE9HY3JEZl96LXVuQmdXM1I4VVBoUUI4d09uNk9qYUdDSXpBTE8zYnJsNUwxUEljLXJ2aTYxYW5rcnFza0duNVNVRnFCWVAzd19MSXVzUTc2cnhnZkxfaVNXS3I2b25JNlJHZnlpMmpiTkQ1NXF5cWNVTG5sRTk3TE9fZExqRExHcjRUa3EybXEzZ1JRNjJPYlZUTWVaMk5hdWJta0g0UWtHZ251dE5BLTk5bk9nYm5vTDh5alo5c05QT054QVE?oc=5) [S57](https://www.fool.com/earnings/call-transcripts/2026/10/15/tsmc-tsm-q3-2026-earnings-call-transcript/)
- [industry] 지정학·관세 리스크(대만 집중, 미국 현지 생산 확대와 텍사스 투자 검토 보도)는 근거에 정량 자료가 없다. 미국 생산 확대가 마진을 희석하는지는 확인되지 않았다. [S36](https://news.google.com/rss/articles/CBMipwFBVV95cUxPdWxqdEVyUzNvcUNVQVVJUnpWd1hWeHRLcVBfWWNSS1FpTWtpOXdKYk54REhBZGFxcVVZUVJ2NXdnZTQ2NktEbnRtREpOVUpMdEtMTmRnb3Iwb3g4VGRzUXV2T1QzVmFCZUZOdUpsSEY3STdDc1VRVjFuTlNPdmdlQ2F4enh1cWxEUzJtRFY5ZHJHcWVmNEtra0cyTnFna0FEWi0tSnV3bw?oc=5) [S45](https://news.google.com/rss/articles/CBMirgFBVV95cUxQUnljT3Nub0lWUWl1VG1xTnV1MVdoTmZaR1F0X1FScUZtWG50Z25LUnFaWjd5SG5qMlI5dV9zd3hiejFTTmpqU3VhSHpKSnhZNWtrN1Z4OVY5Z1VNSU5odGducm5nSEEyekxkRTNOck9LTkJFbXgzNjJmMDc2R01HME92c2VUMDZLeS1yRmNUeE1zdlVyVmRlRk9TY3VyVnhnRUFudHhXeHprUkpBWXc?oc=5) [S37](https://news.google.com/rss/articles/CBMihwFBVV95cUxQWmVVY2pVa3FRRHNQY2JNVVRmR1ZZZTc2V1NCcXRKcm41OHZnYS1kS2hTaTJHZGJURmdJaHJWQUFNSy1GV3BuT2VUR2hlblVMdXpxeVZodnM3SE9mblBjM2xmb0NZeEFNSlQzdE5SQnhPODNiZUl3MElydlNxVjFFd0lMdXJtNXM?oc=5)
- [proven] FY2020~FY2024 영업이익률 40.9~49.5%, ROIC 40.8~62.4%가 5년 내내 유지됐다(경기 둔화기인 FY2023도 영업이익률 42.6%, ROIC 40.8%). 이후 FY2025 50.8%(F93), 3Q26 58.7%(F86)로 상승. 대규모 설비투자(FY2024 capex 9,560.1억 TWD, F5)를 감당하며 높은 수익률을 내는 규모 흔적이다. [C:operating_margin@FY2020] [C:operating_margin@FY2023] [C:operating_margin@FY2024] [C:roic@FY2023] [C:roic@FY2024] [F5] [F93] [F86]
- [proven] 총이익률이 FY2023 54.4%에서 FY2024 56.1%, FY2025 59.9%(F92), 2Q26 67.7%(F104), 3Q26 66.4%(F85)로 상승했다. 매출이 늘면서 마진이 함께 오른 것은 가격결정력·가동률·공정 우위가 결합된 결과로 읽히나, 가격 vs 믹스 vs 가동률의 분해는 근거에 없다. [C:gross_margin@FY2023] [C:gross_margin@FY2024] [F92] [F104] [F85]
- [claimed] 고객이 설계를 특정 공정·IP 라이브러리에 맞추기 때문에 전환비용이 높다는 것이 통상 논리이나, 이번 근거에는 고객 이탈·점유율·웨이퍼 가격 인상 후 잔존 기록이 없다. GlobalFoundries의 $2bn 공급 계약 보도(S54)는 타 파운드리가 선단 외 영역에서 TSMC에 의존하기도 함을 시사하나 보도 수준이다. [S54](https://news.google.com/rss/articles/CBMiogFBVV95cUxNY2ZPUml0X2VTR08xUTkta283RkNQck9QVlVoWTZkRVRmOGVMNHRaUGl1NnJqeW5PNHJmN3FUYVZWVTlfTElUalBld3FYdDJBdXNnamptUkNTMnZDcGNvMzA1SXhpWWJNYnJodERrckFXYm5HTjh1WkZfN0I4LWs0YXp6SzlzVXpjdEFSbGRRVWp6bkVoZDhrSEJ5alBxcDUyNmc?oc=5) [S45](https://news.google.com/rss/articles/CBMirgFBVV95cUxQUnljT3Nub0lWUWl1VG1xTnV1MVdoTmZaR1F0X1FScUZtWG50Z25LUnFaWjd5SG5qMlI5dV9zd3hiejFTTmpqU3VhSHpKSnhZNWtrN1Z4OVY5Z1VNSU5odGducm5nSEEyekxkRTNOck9LTkJFbXgzNjJmMDc2R01HME92c2VUMDZLeS1yRmNUeE1zdlVyVmRlRk9TY3VyVnhnRUFudHhXeHprUkpBWXc?oc=5)
- [claimed] 2nm 양산 확대와 선단 공정 선도는 어닝콜·보도 요약에서만 확인된다. 삼성 파운드리·인텔 18A 대비 점유율·수율 데이터는 확인하지 못했다. [S57](https://www.fool.com/earnings/call-transcripts/2026/10/15/tsmc-tsm-q3-2026-earnings-call-transcript/) [S56](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm)

### 경영진·자본배분 — mixed

이번 조사에서는 경영진 보상(DEF 14A 해당 없음, 20-F 원문 미확인)과 내부자 매매 근거를 확보하지 못해 정렬 여부의 핵심 축은 비어 있다. 확인되는 것은 세 가지다. 첫째, 희석이 없다: 희석 주식 수가 FY2020~FY2024 내내 259.3억 주로 일정해 SBC·희석이 주주가치를 갉아먹은 흔적이 없다. 둘째, 가이던스 신뢰도는 긍정적이나 표본이 1건뿐이다: 3Q26 매출은 가이던스 452.0억 달러 대비 실제 467.2억 달러로 상회했다. 셋째, 자본배분은 대규모 재투자 중심이다: 설비투자가 FY2024 9,560.1억 TWD로 높고 2026년 가이던스가 US$60~64bn으로 상향됐으며, 애리조나 투자가 US$265bn 규모로 커지고 있어 FCF 전환(FY2024 0.75x)과 해외 증설 수익률이 핵심 쟁점이다. 보상·내부자·M&A 이력이 비어 있으므로 정렬은 '혼재'로 보수적으로 분류한다.

- [compensation] 경영진 보상 구조(연동 지표·베스팅 기간)는 수집된 근거에 없다. 20-F(S30) 본문과 보상 관련 공시를 읽지 못해 단기 지표 연동인지 장기 지표 연동인지 판단할 수 없다. 근거 없음. [S30](https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm)
- [insider] 창업자·경영진 지분과 최근 내부자 매수·매도 근거가 없다. 리서처 미확인 항목으로 명시되어 있다. 근거 없음. [S30](https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm)
- [guidance] 가이던스 적중률은 100%이나 표본은 3Q26 매출 1건뿐이다. 가이던스 452.0억 달러 대비 실제 467.2억 달러로 상회했다. 한 분기라 신뢰도 판단의 근거로는 약하고, 다른 분기의 과거 가이던스는 확인되지 않았다. [C:guidance_hit_rate] [F109] [F98] [S60](https://fourweekmba.com/ai-tsmc-q3-revenue-rises-to-46-7b-with-a-66-4-gross-margin/)
- [guidance] 4Q26 가이던스는 매출 US$52.3~54.3bn, 총이익률 65~67%, 영업이익률 56.5~58.5%다. 2nm 초기 비용으로 마진이 2Q 대비 하락한다는 보도가 있고, Reuters는 2027 전망에 대해 경영진이 '신중'했다고 전한다. 가이던스를 보수적으로 제시하는 경향인지는 표본 부족으로 판단할 수 없다. [S56](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm) [S38](https://news.google.com/rss/articles/CBMixgFBVV95cUxOWE9HY3JEZl96LXVuQmdXM1I4VVBoUUI4d09uNk9qYUdDSXpBTE8zYnJsNUwxUEljLXJ2aTYxYW5rcnFza0duNVNVRnFCWVAzd19MSXVzUTc2cnhnZkxfaVNXS3I2b25JNlJHZnlpMmpiTkQ1NXF5cWNVTG5sRTk3TE9fZExqRExHcjRUa3EybXEzZ1JRNjJPYlZUTWVaMk5hdWJta0g0UWtHZ251dE5BLTk5bk9nYm5vTDh5alo5c05QT054QVE?oc=5) [S57](https://www.fool.com/earnings/call-transcripts/2026/10/15/tsmc-tsm-q3-2026-earnings-call-transcript/)
- [dilution] 희석 주식 수는 FY2020~FY2024 내내 259.3억 주로 변화가 없고, 연간 주식 수 변화도 0.0% 안팎이다. 주식 수는 2025-12-31 기준 259.3억 주로 유지된다. 희석은 관찰되지 않는다. SBC 규모는 사실로 수집되지 않았다. 자사주 매입 이력은 근거에 없다. [C:share_change@FY2024] [F71] [F20]
- [capital_allocation] 설비투자는 FY2020 5,072.4억 TWD에서 FY2022 1.08조 TWD, FY2024 9,560.1억 TWD로 높은 수준이 이어졌다. 2026년 설비투자 가이던스는 직전 US$52~56bn에서 US$60~64bn으로 상향됐고, CFO는 향후 3년 설비투자가 직전 3년보다 크게 늘 것이라고 발언했다고 보도됐다. 재투자 비중이 매우 크다. [F1] [F3] [F5] [F99] [S61](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/tsmc-postq-ai-drives-beat-outlook-raised-higher-capex-weighs-on-sentiment)
- [capital_allocation] 재투자 수익률은 과거 높았다. ROIC가 FY2021 53.6%, FY2022 62.4%, FY2024 51.4%로 기록됐고, FCF 마진은 FY2023 13.5%에서 FY2024 30.1%로 변동이 컸다. FCF/순이익은 FY2023 0.34x, FY2024 0.75x로 설비투자 주기에 따라 크게 움직인다. [C:roic@FY2024] [C:fcf_margin@FY2023] [C:fcf_margin@FY2024] [C:fcf_conversion@FY2023] [C:fcf_conversion@FY2024]
- [capital_allocation] 미국 증설이 확대되고 있다. 애리조나 프로젝트가 US$265bn 규모로 커졌다는 보도와 텍사스 투자 검토 보도가 있다. 해외 팹의 수익률과 비용 구조는 근거에 없어 이 투자가 과거 ROIC를 유지할지는 판단할 수 없다. 배당·자사주·M&A 이력도 이번 근거에는 없다. [S37](https://news.google.com/rss/articles/CBMihwFBVV95cUxQWmVVY2pVa3FRRHNQY2JNVVRmR1ZZZTc2V1NCcXRKcm41OHZnYS1kS2hTaTJHZGJURmdJaHJWQUFNSy1GV3BuT2VUR2hlblVMdXpxeVZodnM3SE9mblBjM2xmb0NZeEFNSlQzdE5SQnhPODNiZUl3MElydlNxVjFFd0lMdXJtNXM?oc=5) [S36](https://news.google.com/rss/articles/CBMipwFBVV95cUxPdWxqdEVyUzNvcUNVQVVJUnpWd1hWeHRLcVBfWWNSS1FpTWtpOXdKYk54REhBZGFxcVVZUVJ2NXdnZTQ2NktEbnRtREpOVUpMdEtMTmRnb3Iwb3g4VGRzUXV2T1QzVmFCZUZOdUpsSEY3STdDc1VRVjFuTlNPdmdlQ2F4enh1cWxEUzJtRFY5ZHJHcWVmNEtra0cyTnFna0FEWi0tSnV3bw?oc=5) [S45](https://news.google.com/rss/articles/CBMirgFBVV95cUxQUnljT3Nub0lWUWl1VG1xTnV1MVdoTmZaR1F0X1FScUZtWG50Z25LUnFaWjd5SG5qMlI5dV9zd3hiejFTTmpqU3VhSHpKSnhZNWtrN1Z4OVY5Z1VNSU5odGducm5nSEEyekxkRTNOck9LTkJFbXgzNjJmMDc2R01HME92c2VUMDZLeS1yRmNUeE1zdlVyVmRlRk9TY3VyVnhnRUFudHhXeHprUkpBWXc?oc=5)

### 회계 품질 — clean

코드 회계 신호는 하나도 걸리지 않았다. FY2020~FY2024 영업현금흐름은 모든 해에 순이익을 웃돌고 발생액 비율은 전 기간 음수여서, 이익이 현금으로 뒷받침된다. 희석 주식 수는 259.3억으로 5년 내내 일정해 SBC 희석 문제도 보이지 않는다. 다만 감사의견, 핵심감사사항, 특수관계자 거래, 매출 인식 정책, 재무제표 정정·감사인 변경 여부는 20-F 원문을 읽지 못해 확인하지 못했다. FY2025 연간 영업현금흐름·설비투자와 매출채권·이연매출·SBC·영업권 데이터도 없다. FY2025 순이익과 마진은 2차 보도 단일 출처(S58)라 20-F 대조 전까지 잠정치로 본다. 확인된 범위에서는 숫자를 그대로 믿어도 된다. 이 회사의 핵심 위험은 회계가 아니라 설비투자 강도(FCF 변동)와 사이클이다. FCF는 설비투자 후 기준으로 봐야 한다.

- [benign] ocf_to_ni: 코드 신호는 없다. FY2024 영업현금흐름 1.83조 TWD가 순이익 1.16조 TWD보다 크고, FY2023도 영업현금흐름 1.24조가 순이익 8,517.4억을 웃돈다. 현금 전환은 양호하다. FCF/순이익이 0.34x~0.75x로 낮게 보이는 것은 이익의 질 문제가 아니라 설비투자가 커서다. [F50] [F45] [F49] [F44] [C:fcf_conversion@FY2024]
- [benign] accruals: 발생액 비율이 FY2021~FY2024 전 기간 음수(FY2024 -10.9%)다. 이익이 현금보다 부풀려진 흔적이 없다. [C:accruals_ratio@FY2024] [C:accruals_ratio@FY2023]
- [benign] inventory_gap: FY2024 재고는 2,878.7억 TWD로 늘었지만, 같은 기간 매출은 2.89조 TWD로 크게 늘었다. DIO는 FY2023 92.9일에서 FY2024 82.7일로 개선됐다. 재고 적체 신호가 없다. 매출채권과 이연매출은 사실에 없어 해당 신호는 평가하지 못했다. [F40] [F65] [C:dio@FY2024] [C:dio@FY2023]
- [benign] dilution: 희석 주식 수가 FY2020~FY2024 내내 259.3억으로 일정하고 변화율은 0%다. SBC 희석은 보이지 않는다. SBC 금액 자체는 사실에 없어 sbc_to_revenue와 sbc_to_ocf는 평가하지 못했다. 이 항목은 확인 공백이다. [F20] [C:share_change@FY2024]
- [watch] 감사의견, 핵심감사사항, 감사인 변경, 재무제표 정정 여부는 20-F(S30) 본문을 읽지 못해 확인하지 못했다. 코드가 restatement와 auditor_change 신호를 내지 않았으나, 확인되지 않은 것과 없는 것은 다르다. 공백으로 남긴다. [S30](https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm)
- [info] FY2024까지 영업현금흐름, 발생액, DIO가 모두 이익의 질이 양호하다는 쪽을 가리킨다. FY2023은 매출이 -4.5% 줄었지만 재고 증가는 완만했고 영업현금흐름은 순이익을 웃돌았다. 사이클 하락기에도 운전자본 왜곡은 보이지 않는다. [C:revenue_growth@FY2023] [F39] [F49] [F44]
- [watch] FY2025 순이익 1.72조 TWD와 마진(총이익률 59.9%, 영업이익률 50.8%)은 2차 보도(S58) 단일 출처이고, 연간 영업현금흐름·설비투자는 집계 사이트마다 값이 달라 사실로 넣지 못했다. 최신 해의 이익과 현금 대응을 코드가 검증하지 못한다. 20-F 현금흐름표 확인 전까지 FY2025 수치는 잠정치로 쓴다. [F94] [F92] [F93] [S58](https://telecomlead.com/semiconductor/tsmc-delivers-record-2025-revenue-and-profit-as-ai-chip-demand-fuels-growth-us-expansion-accelerates-124150) [S68](https://tickerleague.com/companies/TSM/financials/operating-cash-flow)
- [info] 3Q26 6-K의 순이익 7,630.6억 TWD는 영업이익 8,764.5억 TWD보다 작고, 그 차이는 세금과 영업외손익으로 설명 가능한 범위다. 3Q26 매출은 자체 가이던스를 넘어섰고 가이던스 적중률은 100%다. 다만 표본이 1분기뿐이라 가이던스 신뢰도를 판단하기엔 이르다. [F83] [F82] [S56](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm) [C:guidance_hit_rate]
- [info] 특수관계자 거래, 연결·별도 차이, 지배주주 귀속 이익은 사실에 없어 평가하지 못했다. 주 위험으로 판단하지는 않지만 20-F 주석에서 확인할 항목이다. [S30](https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) AI 설비 소화 조정기. 2026년 설비투자가 US$60~64bn(F99)까지 늘어난 뒤 AI 가속기 고객의 주문이 멈춘다. 감가상각과 가동률 하락이 한꺼번에 와서 총이익률이 3Q26의 66.4%(F85)에서 급락한다. FY2023에는 매출이 -4.5%(C:revenue_growth@FY2023)로 줄고 영업이익률도 내려갔다. 이번에는 고정비 기반이 훨씬 커서 이익 감소 폭이 더 크다. 경영진은 이미 2027 전망에 '신중'했다(S38). 현재 PER 40배(C:pe)는 높은 성장이 오래 간다는 가정을 담고 있어, 이익 감소와 배수 압축이 겹치면 −60%에 도달할 수 있다. [F99] [F85] [C:revenue_growth@FY2023] [S38](https://news.google.com/rss/articles/CBMixgFBVV95cUxOWE9HY3JEZl96LXVuQmdXM1I4VVBoUUI4d09uNk9qYUdDSXpBTE8zYnJsNUwxUEljLXJ2aTYxYW5rcnFza0duNVNVRnFCWVAzd19MSXVzUTc2cnhnZkxfaVNXS3I2b25JNlJHZnlpMmpiTkQ1NXF5cWNVTG5sRTk3TE9fZExqRExHcjRUa3EybXEzZ1JRNjJPYlZUTWVaMk5hdWJta0g0UWtHZ251dE5BLTk5bk9nYm5vTDh5alo5c05QT054QVE?oc=5) [C:pe] [S61](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/tsmc-postq-ai-drives-beat-outlook-raised-higher-capex-weighs-on-sentiment)
- (15%) 설비투자가 현금 창출을 계속 앞지른다. 미국 애리조나 프로젝트가 US$265bn 규모로 커졌고(S37) 텍사스 투자도 검토 중이다(S36). CFO는 향후 3년 설비투자가 직전 3년보다 크게 늘 것이라고 말했다(S61). 해외 팹의 비용 구조와 수익률은 근거에 없다. 투자 수익률이 과거 ROIC에 못 미치면 FCF는 사이클 정점에서도 약해진다. FCF/순이익은 FY2023에 0.34x(C:fcf_conversion@FY2023)까지 내려간 적이 있다. 시장이 높은 PER을 FCF 회복에 대한 믿음으로 정당화해 왔다면, 그 믿음이 깨질 때 배수가 크게 내려간다. [S37](https://news.google.com/rss/articles/CBMihwFBVV95cUxQWmVVY2pVa3FRRHNQY2JNVVRmR1ZZZTc2V1NCcXRKcm41OHZnYS1kS2hTaTJHZGJURmdJaHJWQUFNSy1GV3BuT2VUR2hlblVMdXpxeVZodnM3SE9mblBjM2xmb0NZeEFNSlQzdE5SQnhPODNiZUl3MElydlNxVjFFd0lMdXJtNXM?oc=5) [S36](https://news.google.com/rss/articles/CBMipwFBVV95cUxPdWxqdEVyUzNvcUNVQVVJUnpWd1hWeHRLcVBfWWNSS1FpTWtpOXdKYk54REhBZGFxcVVZUVJ2NXdnZTQ2NktEbnRtREpOVUpMdEtMTmRnb3Iwb3g4VGRzUXV2T1QzVmFCZUZOdUpsSEY3STdDc1VRVjFuTlNPdmdlQ2F4enh1cWxEUzJtRFY5ZHJHcWVmNEtra0cyTnFna0FEWi0tSnV3bw?oc=5) [S61](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/tsmc-postq-ai-drives-beat-outlook-raised-higher-capex-weighs-on-sentiment) [F99] [C:fcf_conversion@FY2023] [C:fcf_margin@FY2023]
- (10%) 지정학·관세와 해외 생산 비용. 생산이 대만에 집중되어 있고 미국 현지 생산 확대(S36, S45)가 비용을 높인다. 해외 증설의 마진 영향은 근거에 없다. 관세나 대만 해협 긴장으로 고객이 공급 다변화를 서두르거나 미국 생산 비중이 급격히 커지면, 높은 영업이익률(F86)이 유지되지 못한다. 시장은 이 위험을 낮은 확률로 보고 가격에 넣었다고 가정하는 편이 안전하지 않다. 사건 한 번에 배수와 이익이 동시에 내려간다. [S36](https://news.google.com/rss/articles/CBMipwFBVV95cUxPdWxqdEVyUzNvcUNVQVVJUnpWd1hWeHRLcVBfWWNSS1FpTWtpOXdKYk54REhBZGFxcVVZUVJ2NXdnZTQ2NktEbnRtREpOVUpMdEtMTmRnb3Iwb3g4VGRzUXV2T1QzVmFCZUZOdUpsSEY3STdDc1VRVjFuTlNPdmdlQ2F4enh1cWxEUzJtRFY5ZHJHcWVmNEtra0cyTnFna0FEWi0tSnV3bw?oc=5) [S45](https://news.google.com/rss/articles/CBMirgFBVV95cUxQUnljT3Nub0lWUWl1VG1xTnV1MVdoTmZaR1F0X1FScUZtWG50Z25LUnFaWjd5SG5qMlI5dV9zd3hiejFTTmpqU3VhSHpKSnhZNWtrN1Z4OVY5Z1VNSU5odGducm5nSEEyekxkRTNOck9LTkJFbXgzNjJmMDc2R01HME92c2VUMDZLeS1yRmNUeE1zdlVyVmRlRk9TY3VyVnhnRUFudHhXeHprUkpBWXc?oc=5) [S37](https://news.google.com/rss/articles/CBMihwFBVV95cUxQWmVVY2pVa3FRRHNQY2JNVVRmR1ZZZTc2V1NCcXRKcm41OHZnYS1kS2hTaTJHZGJURmdJaHJWQUFNSy1GV3BuT2VUR2hlblVMdXpxeVZodnM3SE9mblBjM2xmb0NZeEFNSlQzdE5SQnhPODNiZUl3MElydlNxVjFFd0lMdXJtNXM?oc=5) [F86]
- (10%) 선단 공정의 가격결정력 약화와 고객 협상력 상승. 총이익률이 FY2023 54.4%(C:gross_margin@FY2023)에서 3Q26 66.4%(F85)까지 올랐는데, 가격·믹스·가동률 중 무엇이 원인인지 근거에 없다. 고객 집중도도 확인되지 않았다(S41). 소수의 대형 고객이 대안 공급(삼성 파운드리·인텔 18A)을 키우거나 직접 협상력을 쓰면 마진은 평균으로 회귀한다. 이 마진은 매출이 가이던스를 넘는 동안만 확인된 상태다. 가이던스 상회 표본은 1건뿐이다(F98, F109). [C:gross_margin@FY2023] [F85] [S41](https://news.google.com/rss/articles/CBMixgFBVV95cUxNYjd5WnY4cUZJRFZ1Y056dmJXZzZkeS1MU2VjUFUtN1diSkNMTmd0VTJDQlNHYWZkdEM1bGpwR0RRN01DRWl1bDJocHNZN09HUjZkN2xzaC1sMDVlcUxCNHl2ZHQ5QjM3Ql9DVm1DUzhweVdTcTE5Q3ZodmxGN2pZY1h1S1pwY1BBVUR0Y2NmelBUUW5uUlZpcEpwTl8yYUNabkhVa0FONWltYWJjb3A4QloyX0hHYnp1c2FuMk5NWndpNGR2LVE?oc=5) [F98] [F109] [S54](https://news.google.com/rss/articles/CBMiogFBVV95cUxNY2ZPUml0X2VTR08xUTkta283RkNQck9QVlVoWTZkRVRmOGVMNHRaUGl1NnJqeW5PNHJmN3FUYVZWVTlfTElUalBld3FYdDJBdXNnamptUkNTMnZDcGNvMzA1SXhpWWJNYnJodERrckFXYm5HTjh1WkZfN0I4LWs0YXp6SzlzVXpjdEFSbGRRVWp6bkVoZDhrSEJ5alBxcDUyNmc?oc=5)
- 약한 가정 `base.fcf_margin`: 기본 시나리오는 설비투자 정점 이후 FCF 마진이 FY2024 수준으로 돌아온다고 본다. 그러나 FY2023 FCF 마진은 13.5%(C:fcf_margin@FY2023)였고 FY2024는 30.1%(C:fcf_margin@FY2024)로 해마다 크게 흔들렸다. 설비투자는 2026년 US$60~64bn(F99)이고 향후 3년도 더 크다는 발언이 있다(S61). 회복 시점과 수준을 정하는 근거가 없고, FY2025 연간 OCF·설비투자는 사실로 확보되지 않았다. [C:fcf_margin@FY2024] [C:fcf_margin@FY2023] [F99] [S61](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/tsmc-postq-ai-drives-beat-outlook-raised-higher-capex-weighs-on-sentiment)
- 약한 가정 `base.revenue_growth`: FY2026 이후 성장률은 경영진이 '신중'하다고 한 2027 전망(S38)을 기본 시나리오에서 둔화로만 반영한다. 컨센서스와 기저율이 없고 시나리오 가치 계산도 되지 않았다(계산 경고). 이 구간의 성장률은 검증 수단이 없다. FY2023 역성장(C:revenue_growth@FY2023) 같은 정체 구간이 기본 시나리오에 없다. [S38](https://news.google.com/rss/articles/CBMixgFBVV95cUxOWE9HY3JEZl96LXVuQmdXM1I4VVBoUUI4d09uNk9qYUdDSXpBTE8zYnJsNUwxUEljLXJ2aTYxYW5rcnFza0duNVNVRnFCWVAzd19MSXVzUTc2cnhnZkxfaVNXS3I2b25JNlJHZnlpMmpiTkQ1NXF5cWNVTG5sRTk3TE9fZExqRExHcjRUa3EybXEzZ1JRNjJPYlZUTWVaMk5hdWJta0g0UWtHZ251dE5BLTk5bk9nYm5vTDh5alo5c05QT054QVE?oc=5) [C:revenue_growth@FY2023] [C:revenue_growth@FY2025]
- 약한 가정 `bull.exit_multiple`: 상승 시나리오는 높은 배수가 유지된다고 가정한다. 현재 PER이 40배(C:pe)로 이미 높고, 10-07 이후 주가가 12.6% 하락한 것은 시장이 성장 지속을 의심하기 시작했다는 신호일 수 있다(S55). 그 원인은 근거에 없다. [C:pe] [S55](https://stockanalysis.com/stocks/tsm/history/) [S38](https://news.google.com/rss/articles/CBMixgFBVV95cUxOWE9HY3JEZl96LXVuQmdXM1I4VVBoUUI4d09uNk9qYUdDSXpBTE8zYnJsNUwxUEljLXJ2aTYxYW5rcnFza0duNVNVRnFCWVAzd19MSXVzUTc2cnhnZkxfaVNXS3I2b25JNlJHZnlpMmpiTkQ1NXF5cWNVTG5sRTk3TE9fZExqRExHcjRUa3EybXEzZ1JRNjJPYlZUTWVaMk5hdWJta0g0UWtHZ251dE5BLTk5bk9nYm5vTDh5alo5c05QT054QVE?oc=5)

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

### 시장 · FY2025 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 412.61 USD/ADR (2026-10-16, F77) → 주당 2,676.02 TWD |
| 희석 주식 수 (shares) | 259.3억 |
| 시가총액 (market_cap) | 69.38조 TWD |
| 순현금 (net_cash) | 2.13조 TWD |
| EV (ev) | 67.26조 TWD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 17.66x |
| PER (pe) | 40.39x |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 가이던스 적중 (C:guidance_hit_rate = 100%)

- revenue FY2026Q3: 가이던스 452.0억 → 실제 467.2억 = beat [F109, F98]

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "base", "fcf_margin": 0.25, "exit_multiple": 22}: price=2,676.0, leveraged=아니오

### 계산 경고

- 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

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
| S62 | data | 2026-10-16 | [Yahoo Finance TSM historical prices](https://finance.yahoo.com/quote/TSM/history/) | 2026-10-16 종가 412.61 USD (ADR, 1 ADR = 5 보통주) |
| S63 | data | 2026-10-16 | [Yahoo Finance USDTWD=X historical rates](https://finance.yahoo.com/quote/USDTWD=X/history/) | 2026-10-16 종가 1 USD = 32.428 TWD |
| S64 | news | 2026-10-17 | [Taiwan Semiconductor Manufacturing (TSM) Dropped, So What Is Behind The Move? - Yahoo Finance](https://news.google.com/rss/articles/CBMisAFBVV95cUxNU1lxVG1ueWNWR1Ezc3JJN3p5VDk3YU9IZi1DUVpLZDRyTWVqeUFBSnY1REVJWW1OTmRNQnQ2dV84aTBtRUlvSTBRU1VfR1Y4b2pBR19zYW85TGUtb0tVRXpVMGJtd1FfTXQ3cUF0WXRHa0tDcEFPOTF4aWotVG5zWXM1ZjlMRWJXYmQ2OEVreVRjWDBHbjlVU0tpUjUwczlSdFQ1UXNxU2FuQkN4UU4tRA?oc=5) | Yahoo Finance |
| S65 | news | 2026-10-07 | [Taiwan Semiconductor Manufacturing Heads 3 AI Chip Stocks To Watch - Yahoo Finance](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNWXRTTmNnNFdERjdmcjRiRzM1LVBlcmFkUHhHd2Q3dnUzMlZlYTFMQm8tS3dQQnJtRG1qdDNEVEw1V2VFTkZBeDREYW9RVmZsOVU0MU9rVjdJNG9DSDJKU2xMN1NiQkc2UGx2alpydGxJSHpDS3pyMEFOOTNaR18xMldpWU5IT2dneVkyNTBZTVNwWEtoMUdWMmV1MHYwVTRablhZaG1Cb3dPQQ?oc=5) | Yahoo Finance |
| S66 | filing | 2026-07-16 | [TSMC 2Q26 Management Report](https://investor.tsmc.com/english/encrypt/files/encrypt_file/qr/phase4_reports/2026-07/bf09036349a253e83f78155099133806cad0320b/2Q26%20ManagementReport.pdf) | 2Q26 매출 NT$1,270.38bn(1Q26 NT$1,134.10bn 대비 +12.0%), 매출총이익률 67.7%, 영업이익률 60.3%. 검색 요약으로 확인했고 원문은 읽지 못함. |
| S67 | call | 2026-07-16 | [Taiwan Semiconductor Reports Q2 2026 Results: Full Earnings Call Transcript (Webull)](https://www.webull.com/news/15237944504312832) | 2Q26 영업활동현금흐름 약 NT$783bn, 설비투자 NT$496bn(약 US$15.7bn). 2026 설비투자 가이던스 US$60~64bn(직전 US$52~56bn), 3Q26 매출 가이던스 US$44.6~45.8bn. 검색 요약으로 확인했고 원문은 읽지 못함. |
| S68 | news | 2026-01-15 | [TSMC FY2025 cash flow aggregators (Tickerleague, AlphaSense)](https://tickerleague.com/companies/TSM/financials/operating-cash-flow) | 보도·집계 사이트(2차 자료). FY2025 영업현금흐름 약 NT$2.3~2.38조, 설비투자 약 NT$1.29~1.3조(US$40.9bn)로 출처 간 값이 달라 사실로 넣지 않음. 20-F 원문 확인 필요. |

# MercadoLibre (MELI) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 모델** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✗ model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

## 1. Variant perception

- 시장이 반영한 것: 주가는 마진 우려(S27, S29)로 연초 대비 약 15% 내렸지만 PER 46배(C:pe)와 EV/매출 3.72배(C:ev_revenue)는 여전히 높은 성장 지속을 반영한다. 월가 평균 목표가 약 2,167달러는 현재가보다 약 28% 높아 시장이 이익 감소를 일시적 투자 비용으로 보고 있음을 보여준다(S44). 연간 매출 컨센서스는 확보하지 못해 컨센서스와의 정량 대비는 불가능하다.
- 우리가 다르게 보는 점: 성장은 시장 걱정보다 강하지만(2분기 매출이 컨센서스보다 높았다, S43), 이익 질은 겉으로 보이는 것보다 약하다. 영업현금흐름은 핀테크 자금 흐름 때문에 이익의 질 증거로 쓸 수 없고(forensic), 부채가 FY2025 91.9억에서 2분기 106.3억 달러로 계속 늘었으며(F43, F45), 신용 건전성 자료는 없다. 기본 시나리오 가치는 현재가를 웃돌지만 약세 시나리오의 하락폭이 커 확률 가중 접근이 필요하다.
- 왜 우리가 맞는가: 성장은 보고된 분기 매출(F162, F163, F165, F166)로 확인되지만, 마진 압박은 3분기 연속 이익 감소(S22, S34)와 영업이익률 하락(C:operating_margin@FY2025)으로 확인된다. 시장은 두 흐름 중 성장에만 크게 가중한다. 신용 부실이 늘 때 레버리지가 어떻게 작동할지가 핵심 위험이며, 이는 연체율 자료 없이는 판단할 수 없다. [C:pe] [C:ev_revenue] [F43] [F45] [F134] [S22](https://news.google.com/rss/articles/CBMitwFBVV95cUxQZFRkMnJTWlZLT19MaVcydlhlQ3NkUklRS1UxMjJwTzY0dWVRbkoyeFc0ejF5QmVfcmItUDNkMjJsQXJMbUlWdFRXNEppcnk4bkswTFNGd3JydDhEd0VDRlVELWI2TzJldWx6ellLbHdnNnJGT0s4TjlZLW9ZeERlMlhfX0s1dFhia0FHbEdBYzlxbmQ1X0txU1pCMGFEZUxDTXVjNVFfUFFSdlBXZ2x3azNELTFvRTg?oc=5) [S27](https://news.google.com/rss/articles/CBMipwFBVV95cUxNQ3lUYjRFWkVIdVNMM2J4a1JxaHkxS3pJS202cHdocGprVXRnaENUUlVZWFRwdXNHSDJval9fM242eXQzN3RyNEF0THRabzNLUWlYNWdWcGl0SnRLaVNMaGoycHN0OFIzY0pyMXFENjBLUWRxVHJ3V0VUaUlILWs0YzR5V0RFS3dvSzg2RHMwc0ZSS19ST2s2dWVsNXlYWDYtMFk3c2Z5UQ?oc=5) [S34](https://news.google.com/rss/articles/CBMipwFBVV95cUxObU1yMnR3bVFaeXpCcS1zN0I3YUxnQXpGZDl6VFhsSk10LXlrNzZHc2tCdWRXVmZ3RnNrNDZ4bk92Zjl0ZTNQamVHWHFIZFlHM3A3aFFSZVdJTjJkT0w4SlBycHR0Vkltd0FkTGFMZ1ZNdVpad0I5anJUVmZ5VU83aHByU0pzRFZEUjlLbEI2aWFfN18wYXNYQlc4bndOeXctMTl6WGJvdw?oc=5) [S43](https://www.chartmill.com/news/MELI/Chartmill-52866-MercadoLibre-NASDAQMELI-Beats-Q2-Estimates-but-Shares-Fall-66-After-Hours) [S44](https://www.tikr.com/blog/mercadolibre-stock-hits-a-four-year-revenue-high-while-shares-are-down-17-in-2026)
- 촉매: 2026년 3분기 실적 발표에서 영업이익이 전년 같은 분기(F134 7.2억 달러)를 회복하는지, 신용 연체율과 충당금이 공개되는지.
- 시점: 2026년 3분기 실적 발표(2026년 11월 초 예상)와 2026년 연간 실적(2027년 2월)

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 주가 기준일 2026-10-03이 as_of(2026-10-18)보다 15일 오래됨
- ⚠ 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 분석 모듈 (L4)

### 사업·산업 — unclear

MercadoLibre는 라틴아메리카에서 전자상거래 마켓플레이스와 물류, 핀테크(결제·신용)를 묶어 운영하는 플랫폼이다. 상품 판매와 서비스 수수료, 금융 수익으로 돈을 번다. 연간 매출은 FY2021 57.1억 달러에서 FY2025 203.3억 달러로 늘었고(F157, F161), FY2025 성장률은 34.3%다(C:revenue_growth@FY2025). 영업이익률은 FY2023 21.0%에서 FY2025 15.7%로 낮아졌다(C:operating_margin@FY2023, C:operating_margin@FY2025). 2026년 2분기 영업이익은 6.8억 달러로 전년 같은 분기의 8.2억 달러보다 줄었다(F136, F133). 보도는 매출 성장이 4년 만에 가장 빠르지만 이익은 3분기 연속 감소했다고 전한다(S22, S34). 회사가 성장을 위해 마진을 쓰는 국면으로 보이지만, 고객 단위경제(CAC·이탈률·연체율)를 직접 확인할 자료가 없어 단위경제는 'unclear'로 둔다. 주의: XBRL 매출(F166 70.5억 달러)이 보도된 2분기 순매출 약 102억 달러(S43)와 크게 달라 매출 기반 비율(총이익률 등)은 신뢰하기 어렵다.

- [unit_economics] XBRL 연결 매출과 보도 매출이 어긋난다. 2026년 2분기 XBRL 매출은 70.5억 달러(F166)인데 보도는 약 102억 달러에 전년 대비 약 +50%라고 한다(S43). 총이익률 같은 매출 기반 단위경제 지표는 10-K·10-Q 연결 순매출로 다시 대조하기 전에는 확정하지 않는다. [F166] [S43](https://www.chartmill.com/news/MELI/Chartmill-52866-MercadoLibre-NASDAQMELI-Beats-Q2-Estimates-but-Shares-Fall-66-After-Hours) [C:gross_margin@FY2025]
- [unit_economics] 이익 압박이 나타난다. 2026년 2분기 영업이익 6.8억 달러는 전년 같은 분기 8.2억 달러보다 낮고, 순이익도 4.7억 달러로 5.2억 달러보다 낮다. 같은 기간 R&D는 5.7억 달러에서 7.3억 달러로 늘었다. 보도는 성장 투자를 위해 마진을 희생하고 있다고 해석한다. 마진이 낮아진 원인이 신용 비용인지 물류·무료배송 투자인지는 자료에서 가려지지 않는다. [F136] [F133] [F119] [F116] [F173] [F176] [S39](https://news.google.com/rss/articles/CBMisgFBVV95cUxNSlQtMV84SlptSERqZk1NSE9WSGRzU3VTQ1p1XzM5TWNKTDh5cVBobzdkWmhpcGQ2eHA1UWhjRUEwUDVUTXlocjdaYkxLdVVDTGRhdmo4WFduTlJscS1vc0dKekF4ZEdnYkFoQ0YwRWZPelo0QThUZzZWemF5dDlzbG1icDRXLWJVVmQ0Qk9hRFB1bV9PZXZjMi05WmJPNVFwbzlXY3MzQUprMFAycDZmX2Zn?oc=5) [S27](https://news.google.com/rss/articles/CBMipwFBVV95cUxNQ3lUYjRFWkVIdVNMM2J4a1JxaHkxS3pJS202cHdocGprVXRnaENUUlVZWFRwdXNHSDJval9fM242eXQzN3RyNEF0THRabzNLUWlYNWdWcGl0SnRLaVNMaGoycHN0OFIzY0pyMXFENjBLUWRxVHJ3V0VUaUlILWs0YzR5V0RFS3dvSzg2RHMwc0ZSS19ST2s2dWVsNXlYWDYtMFk3c2Z5UQ?oc=5)
- [unit_economics] CAC, 순매출유지율, 이탈률, 신용 연체율, 대손충당금은 수집되지 않았다. 따라서 단위경제의 개선과 악화를 판정할 근거가 없고 'deteriorating' 조건(CAC 상승과 이탈률 악화의 동시 지속)도 확인할 수 없다. [S3](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000023/meli-20260630.htm) [S10](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm)
- [industry] 라틴아메리카 전자상거래·핀테크에서 방어 비용이 커지고 있다는 보도가 있다. 경쟁 강도와 점유율 변화는 숫자로 확인되지 않았다. 신규 사업인 자체 약국을 브라질에서 칠레로 확장하려는 시도(S26)는 사업 영역 확대를 보여주는 흔적이다. [S40](https://news.google.com/rss/articles/CBMioAFBVV95cUxQV3NfQ1N1MWxxTlF0V3VNNWNRVlBhV2JhOW51SXdySXpQTEVPR09zYlNONWJodk5BdXRWcElaVUptSExrbW9lZlpXUENzOGFRbnJyV0d1OUNIU3BiTktZSnBpSWo0RnFfakJvUFVKbXMyNWZBckgwdVNZaDB6TUJJT1RTd1pkcWlxN0JWX0RqS1JtZ2J4bmZNZUIyUDAyU2s0?oc=5) [S26](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOZHYxOGV0bHBpb3c5VzJGc29QdzZqemxfb2o3OGRhVlRrLVVBOFBaSXg0QWxOdTJyS2ZPdmRFdG5xZHdpOExYblFKb3J6QnBHUng2MHlRZjlSWWJpclN4SkNvSXcxX0U5RmxlQU1WSnpiUmwyQlhleVJIZW9DQ3o2MVY4eEJDeVlSRjBKNUEzek1lcmpxbUVrRjQ2a1FEaHQzWjdpR3VtMDdJdFk1MWJBdGF0Q0k5X2tELTNsOUNtMUE4WXc0ZVJpeUxQM0UxZHM4UHc?oc=5)
- [customers] 고객 지표 공백이 크다. 고유 구매자 수와 핀테크 활성 사용자 수가 없다. 매출채권 DSO는 FY2025에 6.6일로 짧아(C:dso@FY2025) 상품 판매 중심 대금 회수는 빠른 편이지만, 신용 포트폴리오 건전성은 여기서 알 수 없다. 코드는 FY2024 매출채권 증가가 매출 증가를 크게 웃돈 점을 watch 신호로 냈다(C:receivables_gap). [C:dso@FY2025] [C:receivables_gap]
- [runway] 재투자 활주로는 길어 보이지만 자금 조달 의존이 커지고 있다. 부채가 FY2024 57.1억 달러에서 FY2025 91.9억 달러, 2026년 2분기 106.3억 달러로 늘었다. 총자산은 FY2026Q2에 513.6억 달러다. 순부채/EBITDA는 FY2025에 0.72배로 아직 높지 않다. 영업현금흐름은 FY2025에 121.2억 달러다. 다만 신용 사업의 대출 확대가 영업현금흐름과 부채 양쪽에 섞여 있을 수 있어, 영업현금흐름을 주주 몫 현금으로 읽으면 안 된다. [F39] [F43] [F45] [F197] [F124] [C:net_debt_to_ebitda@FY2025]
- [runway] 재고가 빠르게 늘고 있다. 재고는 FY2025의 5.7억 달러에서 2026년 2분기 8.2억 달러로 증가했고 FY2025 재고 증가율이 매출 증가율을 크게 웃돌아 코드가 watch로 표시했다. 직접 매입·판매 비중이 커지거나 약국 같은 신규 사업을 준비하는 흔적일 수 있으나, 어느 쪽인지는 확인되지 않는다. [F107] [F109] [C:inventory_gap] [S26](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOZHYxOGV0bHBpb3c5VzJGc29QdzZqemxfb2o3OGRhVlRrLVVBOFBaSXg0QWxOdTJyS2ZPdmRFdG5xZHdpOExYblFKb3J6QnBHUng2MHlRZjlSWWJpclN4SkNvSXcxX0U5RmxlQU1WSnpiUmwyQlhleVJIZW9DQ3o2MVY4eEJDeVlSRjBKNUEzek1lcmpxbUVrRjQ2a1FEaHQzWjdpR3VtMDdJdFk1MWJBdGF0Q0k5X2tELTNsOUNtMUE4WXc0ZVJpeUxQM0UxZHM4UHc?oc=5)
- [runway] 자본 배분은 성장 재투자 쪽이다. 자사주 매입은 FY2024와 FY2025에 각각 100만 달러에 그쳤고, 희석 주식 수는 5,070만 주로 변하지 않았다(주식 수 데이터는 분기마다 같은 값이 반복돼 확인이 필요하다). 벌어들인 현금을 주주에게 돌려주기보다 사업과 부채 확대에 쓰고 있다. [F4] [F5] [F53] [F54]
- [claimed] 매출이 FY2025에 203.3억 달러로 커졌고 R&D도 22.7억 달러를 쓴다. 이 규모를 물류와 결제에 걸쳐 쓰는 구조가 해자라는 것이 보도의 논지다. 다만 점유율 추이나 경쟁사 대비 마진 같은 흔적은 수집되지 않았고, 매출 계산이 불확실하다. [F161] [F171] [S40](https://news.google.com/rss/articles/CBMioAFBVV95cUxQV3NfQ1N1MWxxTlF0V3VNNWNRVlBhV2JhOW51SXdySXpQTEVPR09zYlNONWJodk5BdXRWcElaVUptSExrbW9lZlpXUENzOGFRbnJyV0d1OUNIU3BiTktZSnBpSWo0RnFfakJvUFVKbXMyNWZBckgwdVNZaDB6TUJJT1RTd1pkcWlxN0JWX0RqS1JtZ2J4bmZNZUIyUDAyU2s0?oc=5)
- [claimed] 구매자와 판매자, 결제·신용이 서로를 강화하는 생태계라는 평가는 보도에만 있다. 고유 구매자 수, 핀테크 월간 활성 사용자, 이탈률 같은 확인 가능한 수치는 확보하지 못했다. [S40](https://news.google.com/rss/articles/CBMioAFBVV95cUxQV3NfQ1N1MWxxTlF0V3VNNWNRVlBhV2JhOW51SXdySXpQTEVPR09zYlNONWJodk5BdXRWcElaVUptSExrbW9lZlpXUENzOGFRbnJyV0d1OUNIU3BiTktZSnBpSWo0RnFfakJvUFVKbXMyNWZBckgwdVNZaDB6TUJJT1RTd1pkcWlxN0JWX0RqS1JtZ2J4bmZNZUIyUDAyU2s0?oc=5) [S31](https://news.google.com/rss/articles/CBMinwFBVV95cUxOVmtBSUY0WEhmaDZPWkJOVnlhNWdiZWd4YTNoRUI4SS1JdjBkNkJJUE14dlBNN1dGRUlNaHIwb2lycUJDU29QcWlFMUxfNGVpd1Bhd2RxaDdpMURuUHNCVFhROC04YXNEc2xMN2k5M0NXaWd4ZG5YX09CVHVOaDEyTzFHMkFnODNqaG41Y0ozbi1YNkFzdWp3bWs5azdwVTQ?oc=5)

### 경영진·자본배분 — mixed

보상 구조, 내부자 매매, 가이던스 적중률은 근거를 확보하지 못해 정렬 여부를 직접 판단할 수 없다. 확인되는 것은 자본배분과 희석이다. 희석은 통제되어 있다(C:share_change@FY2025 -0.0%). 자사주 매입은 FY2023 3.6억 달러 이후 FY2024·FY2025에 각각 100만 달러로 사실상 멈췄다. 같은 기간 부채는 FY2021 35.2억 달러에서 FY2026Q2 106.3억 달러로 늘었고, 순현금은 FY2025에 -28.9억 달러로 바뀌었다. 영업 마진은 하락 중이며(C:operating_margin@FY2025 15.7%), 경영진이 성장 투자를 위해 마진을 희생하는 전략을 택한 것으로 보도된다. 이 전략이 장기 가치에 맞는지는 보상 지표와 신용 포트폴리오 수익률 근거 없이는 판정할 수 없다. 따라서 mixed로 둔다.

- [compensation] 근거 없음. DEF 14A(S8, 2026-04-23)는 수집됐지만 보상 연동 지표(장기 매출·FCF·ROIC 대 단기 EPS·조정 EBITDA)와 베스팅 기간이 사실로 정리되지 않았다. 주주와 같은 방향인지 판단할 수 없다. [S8](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000010/meli-20260423.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도를 확보하지 못했다. 2026-04-03에 경영진 변동 8-K(S9)가 있었으나 내용이 사실로 정리되지 않아 누가 바뀌었는지, 사업에 어떤 의미인지 알 수 없다. [S9](https://www.sec.gov/Archives/edgar/data/1099590/000199937126007656/meli_8k-033126.htm)
- [guidance] 가이던스 적중률(C:guidance_hit_rate)을 계산할 수 없다. 과거 가이던스 사실이 없고, 2분기 실적 발표에도 정식 가이던스가 없는 것으로 보도됐다. 말한 것을 지키는지 검증할 근거가 없으며, 정식 가이던스를 내지 않는 관행 자체가 책임성 측면에서는 중립 이하다. [S43](https://www.chartmill.com/news/MELI/Chartmill-52866-MercadoLibre-NASDAQMELI-Beats-Q2-Estimates-but-Shares-Fall-66-After-Hours) [C:guidance_hit_rate]
- [dilution] 희석 주식 수는 FY2022에 5,134만으로 늘었다가(C:share_change@FY2022 3.1%) FY2023·FY2024에 각각 소폭 줄었고(C:share_change@FY2023 -0.6%, C:share_change@FY2024 -0.6%), FY2025는 변화가 없다(C:share_change@FY2025 -0.0%). 다만 FY2024부터 FY2026Q2까지 분기마다 5,070만으로 같은 값이 반복되어 XBRL 수집 오류일 가능성이 있다. 보통주 발행 주식 수는 5,069.68만 주(2026-08-05)로 일관된다. SBC 규모(C:sbc_to_revenue)는 수집하지 못해 희석의 실제 비용은 확인되지 않는다. [F50] [F51] [F53] [F54] [F59] [F177] [C:share_change@FY2022] [C:share_change@FY2023] [C:share_change@FY2024] [C:share_change@FY2025]
- [capital_allocation] 자사주 매입은 FY2021 4.9억, FY2022 1.5억, FY2023 3.6억 달러였다가 FY2024와 FY2025에는 각각 100만 달러로 사실상 중단됐다. 주식 수가 늘지 않으므로 매입이 희석을 가리는 구조는 아니다. 현금이 매입보다 사업 확장으로 향하고 있다는 뜻이다. [F1] [F2] [F3] [F4] [F5]
- [capital_allocation] 부채는 FY2021 35.2억 달러에서 FY2024 57.1억, FY2025 91.9억, FY2026Q2 106.3억 달러로 계속 늘었다. 순현금은 FY2023 15.4억, FY2024 14.1억 달러에서 FY2025 -28.9억 달러로 바뀌었다. 순부채/EBITDA는 아직 낮지만(C:net_debt_to_ebitda@FY2025 0.72x) 방향은 레버리지 확대다. 차입이 신용 포트폴리오 등 어디에 쓰였는지, 그 수익률이 어떤지는 근거가 없어 확인하지 못했다. [F36] [F39] [F43] [F45] [C:net_cash@FY2023] [C:net_cash@FY2024] [C:net_cash@FY2025] [C:net_debt_to_ebitda@FY2025]
- [capital_allocation] 대형 인수의 흔적은 없다. 영업권은 FY2021 1.5억 달러에서 FY2026Q2 1.7억 달러로 거의 그대로여서, 성장은 인수보다 내부 투자에 의존한다. R&D는 FY2023 18.3억, FY2025 22.7억 달러로 늘었고 FY2026Q2 분기 R&D는 7.3억 달러다. 재고는 FY2025 5.7억에서 FY2026Q2 8.2억 달러로 늘었다(C:inventory_gap 경고 참고). FY2024 이후 capex는 수집되지 않아 FCF를 계산할 수 없고, 재투자 수익률을 직접 평가할 수 없다. [F70] [F79] [F169] [F171] [F176] [F107] [F109] [C:inventory_gap]
- [capital_allocation] 자본 효율은 떨어지고 있다. ROIC는 FY2023 91.4%, FY2024 70.2%에서 FY2025 23.3%로 낮아졌고, 영업이익률도 FY2023 21.0%에서 FY2025 15.7%로 내려갔다. 2026년 2분기에는 이익이 세 분기 연속 줄었다고 보도됐고, 시장은 마진 우려로 반응했다. 경영진이 성장을 위해 마진을 희생하는 선택을 하고 있다는 해석이 가능하며, 그 선택이 보상 지표와 일치하는지는 확인되지 않는다. [S22](https://news.google.com/rss/articles/CBMitwFBVV95cUxQZFRkMnJTWlZLT19MaVcydlhlQ3NkUklRS1UxMjJwTzY0dWVRbkoyeFc0ejF5QmVfcmItUDNkMjJsQXJMbUlWdFRXNEppcnk4bkswTFNGd3JydDhEd0VDRlVELWI2TzJldWx6ellLbHdnNnJGT0s4TjlZLW9ZeERlMlhfX0s1dFhia0FHbEdBYzlxbmQ1X0txU1pCMGFEZUxDTXVjNVFfUFFSdlBXZ2x3azNELTFvRTg?oc=5) [S27](https://news.google.com/rss/articles/CBMipwFBVV95cUxNQ3lUYjRFWkVIdVNMM2J4a1JxaHkxS3pJS202cHdocGprVXRnaENUUlVZWFRwdXNHSDJval9fM242eXQzN3RyNEF0THRabzNLUWlYNWdWcGl0SnRLaVNMaGoycHN0OFIzY0pyMXFENjBLUWRxVHJ3V0VUaUlILWs0YzR5V0RFS3dvSzg2RHMwc0ZSS19ST2s2dWVsNXlYWDYtMFk3c2Z5UQ?oc=5) [S39](https://news.google.com/rss/articles/CBMisgFBVV95cUxNSlQtMV84SlptSERqZk1NSE9WSGRzU3VTQ1p1XzM5TWNKTDh5cVBobzdkWmhpcGQ2eHA1UWhjRUEwUDVUTXlocjdaYkxLdVVDTGRhdmo4WFduTlJscS1vc0dKekF4ZEdnYkFoQ0YwRWZPelo0QThUZzZWemF5dDlzbG1icDRXLWJVVmQ0Qk9hRFB1bV9PZXZjMi05WmJPNVFwbzlXY3MzQUprMFAycDZmX2Zn?oc=5) [S43](https://www.chartmill.com/news/MELI/Chartmill-52866-MercadoLibre-NASDAQMELI-Beats-Q2-Estimates-but-Shares-Fall-66-After-Hours) [C:roic@FY2023] [C:roic@FY2024] [C:roic@FY2025] [C:operating_margin@FY2023] [C:operating_margin@FY2025]

### 회계 품질 — watch

코드 red 신호는 없고 감사인 변경·재무제표 정정(8-K 4.01·4.02)도 수집된 공시 목록에서 보이지 않는다. 다만 믿고 쓰기 전에 조정하거나 확인할 숫자가 셋 있다. (1) 재고가 매출보다 빠르게 늘고 있다. 직접 판매 확대와 맞물린 것으로 보이지만 2026년 상반기에도 이어지고 있다. (2) 영업현금흐름이 순이익을 크게 웃돈다. 핀테크 고객 자금과 대출 관련 현금흐름 분류의 영향을 받았을 가능성이 높아, 영업현금흐름이나 FCF를 이익의 질 증거로 그대로 쓰면 안 된다. (3) 이 하네스의 XBRL 매출(F166, F161)은 보도된 연결 순매출과 범위가 맞지 않고, 분기 희석 주식 수는 같은 값이 반복된다. 신용 포트폴리오의 대손충당금·연체율, 감사의견, 특수관계자 거래는 사실로 확보하지 못했다. 이 부분은 확인되지 않은 영역이지 문제가 없다고 확인된 영역이 아니다. 결론은 watch다. red_flag로 볼 증거는 없지만, 매출 정의를 10-K·10-Q 연결 순매출로 대조하고 신용 건전성을 확인하기 전에는 clean도 줄 수 없다.

- [benign] receivables_gap: FY2024 매출채권 증가율이 매출 증가율을 문턱 이상 넘었다. 그러나 매출채권 절대 규모가 매출 대비 매우 작고 DSO가 한 자릿수 일수대에 머물러 매출 인식을 앞당긴 흔적으로 보기 어렵다. FY2025에는 DSO가 크게 달라지지 않았다. 단, 이 항목(F150, F149)은 대출채권(핀테크 신용)이 아닌 일반 매출채권으로 보인다. 진짜 신용 위험은 이 신호가 아니라 대손충당금과 연체율에서 확인해야 하며, 그 사실은 수집하지 못했다. [C:receivables_gap] [F150] [F149] [C:dso@FY2024] [C:dso@FY2025]
- [concern] inventory_gap: FY2025 재고(F107)가 FY2024(F103)보다 크게 늘어 매출 증가율과의 차이가 문턱을 크게 넘었고, DIO도 9.6일에서 13.0일로 길어졌다. 직접 판매(1P) 확대와 약국·물류 확장 때문일 수 있다. 그러나 2026년에도 재고가 1분기(F108), 2분기(F109)로 계속 늘고 있어 일회성이 아니다. 매출원가도 같은 방향으로 늘고 있어 재고 쌓임이 곧바로 매출 부풀리기를 뜻하지는 않는다. 다만 재고 평가손이나 재고 회전 악화가 총이익률을 압박할 수 있어 추적이 필요하다. 이 문제는 이익을 부풀리는 쪽이 아니라 마진·운전자본 쪽 위험이다. [C:inventory_gap] [F103] [F107] [F108] [F109] [C:dio@FY2024] [C:dio@FY2025] [C:gross_margin@FY2025]
- [watch] 영업현금흐름(F124)이 순이익(F114)을 몇 배 웃돌고 발생액 비율은 매년 큰 음수(-29.8%)다. 보통은 이익의 질이 좋다는 신호지만, 이 회사는 핀테크 고객 자금(예치금·지급 대기금)의 증감이 영업현금흐름에 들어가고 대출 확대는 다른 현금흐름 구간에서 잡힐 수 있다. 그러면 영업현금흐름이 부풀어 보인다. 영업현금흐름과 FCF를 순이익 대체재나 주주 몫 현금으로 그대로 쓰지 말고, 핀테크 자금 증감과 신용 자산 증가를 분리해서 봐야 한다. 이 분해는 수집된 사실에 없다. [F124] [F114] [C:accruals_ratio@FY2025] [C:ocf@FY2025]
- [watch] FY2024·FY2025 설비투자(capex)가 수집되지 않아 FCF 계산이 FY2023에서 끊긴다. 최근 FCF 마진과 FCF/순이익을 코드가 계산하지 못했으므로, FCF 기반 지표는 최근 해에 대해 쓸 수 없다. [F8] [C:fcf@FY2023] [C:fcf_margin@FY2023]
- [watch] XBRL로 수집한 분기 매출(F166)은 보도된 2분기 순매출과 크게 다르고, 연 매출(F161)도 회사가 보고한 순매출 및 금융수익 합계와 범위가 달라 보인다. 수집 태그가 순매출 일부(상품 매출 등)만 잡았을 가능성이 있다. 이 경우 매출 대비 비율(영업이익률, 매출 성장, 발생액, 채권·재고 갭)이 모두 왜곡된다. 이 신호들이 임계를 넘거나 넘지 않은 것도 분모 오류의 영향일 수 있다. 10-K·10-Q의 연결 순매출과 대조하기 전에는 마진·성장 수치를 확정 근거로 쓰지 않는다. [F166] [F161] [S22](https://news.google.com/rss/articles/CBMitwFBVV95cUxQZFRkMnJTWlZLT19MaVcydlhlQ3NkUklRS1UxMjJwTzY0dWVRbkoyeFc0ejF5QmVfcmItUDNkMjJsQXJMbUlWdFRXNEppcnk4bkswTFNGd3JydDhEd0VDRlVELWI2TzJldWx6ellLbHdnNnJGT0s4TjlZLW9ZeERlMlhfX0s1dFhia0FHbEdBYzlxbmQ1X0txU1pCMGFEZUxDTXVjNVFfUFFSdlBXZ2x3azNELTFvRTg?oc=5) [S43](https://www.chartmill.com/news/MELI/Chartmill-52866-MercadoLibre-NASDAQMELI-Beats-Q2-Estimates-but-Shares-Fall-66-After-Hours) [S3](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000023/meli-20260630.htm) [S10](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm)
- [watch] 매출 인식 정책(1P 총액 vs 마켓플레이스 수수료·광고·핀테크 이자수익 구분, 순액·총액 판단)을 10-K 주석에서 직접 확인하지 못했다. 직접 판매 비중 확대는 매출을 총액으로 키우고 총이익률을 낮추는 효과가 있어 성장률 비교 시 구성 변화를 따로 봐야 한다. [S10](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm) [C:gross_margin@FY2024] [C:gross_margin@FY2025]
- [watch] 분기 희석 주식 수(F53~F59)가 같은 값으로 반복돼 실제 분기 값이 아닐 수 있다. 연평균 희석 증가율 신호는 정상으로 계산됐지만 입력 자체가 의심스러워 희석 위험 판단은 보류한다. 발행 주식 수(F177)는 별도로 확인된다. [F53] [F59] [F177] [C:share_change@FY2025]
- [watch] 부채가 FY2025부터 2026년 2분기까지 계속 늘고 있고 순현금은 순부채로 바뀌었다. 신용 포트폴리오 자금 조달(대출 확대를 위한 차입)이 원인일 수 있으나 이 하네스에서는 판매 목적 차입과 영업용 차입을 구분하지 못한다. 순부채/EBITDA 문턱 판단은 별도 모듈에서 하되 회계 품질 관점에서는 부채 성격 확인이 필요하다. [F43] [F44] [F45] [C:net_cash@FY2025] [C:net_debt_to_ebitda@FY2025]
- [info] 코드 신호 중 재무제표 정정(restatement)과 감사인 변경(auditor_change)은 발생하지 않았다. 수집된 8-K 제목(실적, 경영진 변동, 중요 계약, 기타)에 4.01·4.02로 보이는 항목이 없다. 그러나 감사의견(계속기업 의문·핵심감사사항)과 특수관계자 거래는 사실로 정리되지 않아 확인된 것이 아니라 미확인이다. [S1](https://www.sec.gov/Archives/edgar/data/1099590/000114036126036495/ef20081942_8k.htm) [S5](https://www.sec.gov/Archives/edgar/data/1099590/000199937126012770/meli-8k_060926.htm) [S9](https://www.sec.gov/Archives/edgar/data/1099590/000199937126007656/meli_8k-033126.htm) [S10](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm)
- [info] 코드의 Non-GAAP 대비 GAAP 신호는 걸리지 않았다. 다만 보도된 비GAAP EPS는 2차 자료이며 GAAP-비GAAP 조정 내역과 SBC 규모는 사실로 확보하지 못해 이 항목은 검증할 수 없다. [S43](https://www.chartmill.com/news/MELI/Chartmill-52866-MercadoLibre-NASDAQMELI-Beats-Q2-Estimates-but-Shares-Fall-66-After-Hours)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 신용 포트폴리오 부실 사이클: 핀테크 대출이 부채 조달(F45 106.3억 달러, FY2024 57.1억 대비 급증)로 확대된 상태에서 중남미 거시 충격이나 실업 악화로 연체·대손이 급증한다. 충당금 선반영이 이익을 잠식하고, 조달 비용 상승이 순이자 마진을 압박하며, 시장은 '플랫폼'이 아니라 '레버리지 소비자 대출 기관'으로 재평가해 배수가 크게 내려간다. 연체율·충당금은 수집되지 않아 외부에서 보이지 않는다. [F45] [F39] [F43] [S40](https://news.google.com/rss/articles/CBMioAFBVV95cUxQV3NfQ1N1MWxxTlF0V3VNNWNRVlBhV2JhOW51SXdySXpQTEVPR09zYlNONWJodk5BdXRWcElaVUptSExrbW9lZlpXUENzOGFRbnJyV0d1OUNIU3BiTktZSnBpSWo0RnFfakJvUFVKbXMyNWZBckgwdVNZaDB6TUJJT1RTd1pkcWlxN0JWX0RqS1JtZ2J4bmZNZUIyUDAyU2s0?oc=5)
- (30%) 마진 희생이 구조화: 무료배송·물류·약국 등 신규 투자 경쟁(S40, S26)이 경쟁사 대응 비용으로 굳어, 영업이익 감소가 3분기 연속(S22, S34)에서 계속 이어진다. 성장은 유지되지만 이익이 줄어 PER 46배(C:pe)의 분모가 줄고, 성장이 둔화하는 순간 배수가 15배 안팎으로 압축된다. 가격(주가 1,696달러)에 높은 성장 지속이 이미 반영돼 있어 이익 정체 + 배수 압축의 이중 타격이 −60%를 만든다. [S22](https://news.google.com/rss/articles/CBMitwFBVV95cUxQZFRkMnJTWlZLT19MaVcydlhlQ3NkUklRS1UxMjJwTzY0dWVRbkoyeFc0ejF5QmVfcmItUDNkMjJsQXJMbUlWdFRXNEppcnk4bkswTFNGd3JydDhEd0VDRlVELWI2TzJldWx6ellLbHdnNnJGT0s4TjlZLW9ZeERlMlhfX0s1dFhia0FHbEdBYzlxbmQ1X0txU1pCMGFEZUxDTXVjNVFfUFFSdlBXZ2x3azNELTFvRTg?oc=5) [S34](https://news.google.com/rss/articles/CBMipwFBVV95cUxObU1yMnR3bVFaeXpCcS1zN0I3YUxnQXpGZDl6VFhsSk10LXlrNzZHc2tCdWRXVmZ3RnNrNDZ4bk92Zjl0ZTNQamVHWHFIZFlHM3A3aFFSZVdJTjJkT0w4SlBycHR0Vkltd0FkTGFMZ1ZNdVpad0I5anJUVmZ5VU83aHByU0pzRFZEUjlLbEI2aWFfN18wYXNYQlc4bndOeXctMTl6WGJvdw?oc=5) [S40](https://news.google.com/rss/articles/CBMioAFBVV95cUxQV3NfQ1N1MWxxTlF0V3VNNWNRVlBhV2JhOW51SXdySXpQTEVPR09zYlNONWJodk5BdXRWcElaVUptSExrbW9lZlpXUENzOGFRbnJyV0d1OUNIU3BiTktZSnBpSWo0RnFfakJvUFVKbXMyNWZBckgwdVNZaDB6TUJJT1RTd1pkcWlxN0JWX0RqS1JtZ2J4bmZNZUIyUDAyU2s0?oc=5) [C:pe] [C:operating_margin@FY2025]
- (15%) 재고·운전자본 함정: 직접 판매(1P)와 약국 확장으로 재고가 FY2025 5.7억에서 2026Q2 8.2억 달러로 매출보다 빠르게 쌓이고(F107, F109), 수요 둔화나 물류 병목 시 평가손과 총이익률 하락이 발생한다. 총이익률이 이미 FY2023 72.4%에서 FY2025 63.2%로 내려왔고(C:gross_margin@FY2025), 구성이 저마진 총액 매출로 이동하면 성장률은 유지돼도 이익 가치는 줄어든다. [F107] [F109] [C:inventory_gap] [C:gross_margin@FY2025]
- (15%) 자본 의존과 이익 질 오인: 영업현금흐름(F124 121.2억)이 순이익(20.0억)의 6배인 것은 핀테크 고객 자금·대출 분류 효과일 가능성이 크고(forensic), 투자자가 이를 FCF로 오인해 가치를 산정한다. 실제 주주 몫 현금은 작고 자사주 매입은 사실상 중단(F4, F5)됐으며 순현금이 순부채로 전환(C:net_cash@FY2025 −28.9억)됐다. 자금시장이 닫히거나 비용이 오르면 성장 자체를 줄여야 하고, 그때 기대와 현실 괴리가 드러나며 재평가된다. [F124] [F114] [F4] [F5] [C:net_cash@FY2025] [C:accruals_ratio@FY2025]
- 약한 가정 `base.fcf_margin`: FCF 마진 12%는 근거가 없다. FY2023 이후 capex가 수집되지 않아 FCF가 계산되지 않았고(FY2024·FY2025 공백), 영업현금흐름은 핀테크 자금 흐름에 왜곡돼 이익의 질 증거가 되지 못한다. 영업이익률이 FY2023 21.0%에서 FY2025 15.7%로 하락 추세인데 마진 회복을 전제하고 있다. 기저율 점검도 매출 기준 불일치(F166 대 S43) 때문에 신뢰하기 어렵다. [F124] [C:operating_margin@FY2023] [C:operating_margin@FY2025] [C:accruals_ratio@FY2025]
- 약한 가정 `base.revenue_growth`: 첫해 30%, 5년 연속 15% 이상 성장은 가정 기준 매출이 보도 매출과 어긋난 상태(F166 70.5억 대 S43 약 102억)에서 설정되었다. 최근 분기 성장률(45~47%)이 어떤 정의의 매출인지 불분명하고, 대규모 기저에서 5년간 높은 성장을 유지하는 것은 기저율상 드물다. [F161] [F166] [S43](https://www.chartmill.com/news/MELI/Chartmill-52866-MercadoLibre-NASDAQMELI-Beats-Q2-Estimates-but-Shares-Fall-66-After-Hours) [C:revenue_growth@FY2025]
- 약한 가정 `base.exit_multiple`: 출구 배수 22배는 성장이 15%로 둔화한 시점에 적용되지만 마진이 하락 중이고 레버리지가 높아지는 기업에는 관대할 수 있다. 현재 PER 46배에서 반토막이면 충분히 낮아 보이나, 신용 중심 구조로 재분류되면 10~15배가 될 수 있다. [C:pe] [F45] [C:operating_margin@FY2025]

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| 매출 (revenue) | 57.1억 USD | 74.5억 USD | 104.9억 USD | 151.4억 USD | 203.3억 USD |
| 매출 성장 (revenue_growth) | — | 30.5% | 40.8% | 44.3% | 34.3% |
| 총이익률 (gross_margin) | 52.6% | 69.8% | 72.4% | 63.3% | 63.2% |
| 영업이익률 (operating_margin) | 7.7% | 14.3% | 21.0% | 17.4% | 15.7% |
| 순이익 (net_income) | 8,300만 USD | 4.8억 USD | 9.9억 USD | 19.1억 USD | 20.0억 USD |
| 영업현금흐름 (ocf) | 9.7억 USD | 29.4억 USD | 51.4억 USD | 79.2억 USD | 121.2억 USD |
| 설비투자 (capex) | 5.7억 USD | 4.5억 USD | 5.1억 USD | — | — |
| FCF (fcf) | 3.9억 USD | 24.9억 USD | 46.3억 USD | — | — |
| FCF 마진 (fcf_margin) | 6.9% | 33.4% | 44.2% | — | — |
| FCF/순이익 (fcf_conversion) | 4.72x | 5.16x | 4.69x | — | — |
| ROIC (roic) | 13.3% | 28.3% | 91.4% | 70.2% | 23.3% |
| 순현금 (net_cash) | -1.2억 USD | -5.1억 USD | 15.4억 USD | 14.1억 USD | -28.9억 USD |
| 순부채/EBITDA (net_debt_to_ebitda) | 0.19x | 0.35x | -0.56x | -0.43x | 0.72x |
| 희석 주식 수 (diluted_shares) | 4,980만 | 5,134만 | 5,101만 | 5,070만 | 5,070만 |
| 주식 수 변화 (share_change) | — | 3.1% | -0.6% | -0.6% | -0.0% |
| DSO(일) (dso) | 6.3 | 6.4 | 5.4 | 6.1 | 6.6 |
| DIO(일) (dio) | 22.7 | 9.9 | 11.6 | 9.6 | 13.0 |
| 발생액 비율 (accruals_ratio) | — | -20.6% | -26.5% | -28.1% | -29.8% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, cost_of_revenue, d_and_a, debt, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, goodwill, goodwill_to_assets, gross_profit, income_tax, inventory, inventory_growth, operating_income, pretax_income, receivables, receivables_growth, rnd, short_term_investments, total_assets

### 시장 · TTM(FY2026Q2) 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 1696.24 USD/share (2026-10-03, F214) |
| 희석 주식 수 (shares) | 5,070만 |
| 시가총액 (market_cap) | 859.9억 USD |
| 순현금 (net_cash) | -49.0억 USD |
| EV (ev) | 908.9억 USD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 3.72x |
| PER (pe) | 46.16x |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] receivables_gap (C:receivables_gap): FY2024 매출채권 증가율 - 매출 증가율 19.1% > 15%
- [watch] inventory_gap (C:inventory_gap): FY2025 재고 증가율 - 매출 증가율 58.2% > 15%

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull", "revenue_growth": [0.35, 0.3, 0.25, 0.22, 0.2, 0.17, 0.15, 0.13, 0.12, 0.1], "fcf_margin": 0.1, "exit_multiple": 20, "share_change": 0.005, "years": 10}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "base"}: price=1,696.2, leveraged=아니오

### 계산 경고

- 주가 기준일 2026-10-03이 as_of(2026-10-18)보다 15일 오래됨
- 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-09-14 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1099590/000114036126036495/ef20081942_8k.htm) |  |
| S2 | filing | 2026-09-10 | [8-K 중요 계약 IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1099590/000114036126036136/ef20081842_8k.htm) |  |
| S3 | filing | 2026-08-06 | [10-Q](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000023/meli-20260630.htm) |  |
| S4 | filing | 2026-08-05 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000021/meli-20260805.htm) |  |
| S5 | filing | 2026-06-12 | [8-K](https://www.sec.gov/Archives/edgar/data/1099590/000199937126012770/meli-8k_060926.htm) |  |
| S6 | filing | 2026-05-08 | [10-Q](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000017/meli-20260331.htm) |  |
| S7 | filing | 2026-05-07 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000014/meli-20260507.htm) |  |
| S8 | filing | 2026-04-23 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000010/meli-20260423.htm) |  |
| S9 | filing | 2026-04-03 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1099590/000199937126007656/meli_8k-033126.htm) |  |
| S10 | filing | 2026-02-25 | [10-K](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm) |  |
| S11 | filing | 2026-02-24 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000003/meli-20260224.htm) |  |
| S12 | filing | 2025-12-09 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1099590/000114036125045035/ef20060926_8k.htm) |  |
| S13 | filing | 2025-12-05 | [8-K 중요 계약 IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1099590/000114036125044457/20058389x5_8k.htm) |  |
| S14 | filing | 2025-10-30 | [10-Q](https://www.sec.gov/Archives/edgar/data/1099590/000109959025000051/meli-20250930.htm) |  |
| S15 | filing | 2025-10-29 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1099590/000109959025000048/meli-20251029.htm) |  |
| S16 | filing | 2025-09-16 | [8-K 중요 계약](https://www.sec.gov/Archives/edgar/data/1099590/000109959025000046/meli-20250916.htm) |  |
| S17 | filing | 2024-02-23 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1099590/000109959024000008/0001099590-24-000008-index.htm) |  |
| S18 | filing | 2025-02-21 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1099590/000109959025000007/0001099590-25-000007-index.htm) |  |
| S19 | filing | 2023-02-24 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1099590/000109959023000007/0001099590-23-000007-index.htm) |  |
| S20 | filing | 2025-05-08 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1099590/000109959025000028/0001099590-25-000028-index.htm) |  |
| S21 | filing | 2025-08-05 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1099590/000109959025000044/0001099590-25-000044-index.htm) |  |
| S22 | news | 2026-08-05 | [MercadoLibre profit beats forecasts, but third straight decline dents shares - Reuters](https://news.google.com/rss/articles/CBMitwFBVV95cUxQZFRkMnJTWlZLT19MaVcydlhlQ3NkUklRS1UxMjJwTzY0dWVRbkoyeFc0ejF5QmVfcmItUDNkMjJsQXJMbUlWdFRXNEppcnk4bkswTFNGd3JydDhEd0VDRlVELWI2TzJldWx6ellLbHdnNnJGT0s4TjlZLW9ZeERlMlhfX0s1dFhia0FHbEdBYzlxbmQ1X0txU1pCMGFEZUxDTXVjNVFfUFFSdlBXZ2x3azNELTFvRTg?oc=5) | Reuters |
| S23 | news | 2026-08-10 | [MercadoLibre (MELI) Just Broke $10B, So Why Did Shares Sink? - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxOMjROcGx3dEFEbzVtcmhBYWIyTkR0RXRxRVRrbExTM3JlQTlubzNsVHVVeTZvMXlaLXZnRGtiQXFWRC1tRGUyTmZCX19sdEZDR3BuMkIwVXBkX0h1WEdIQmJoczVpeGlKQkUtWnR6OVVBUmtNTkRUUkNZT25kZ0l0VkVBVlRVOUFvY1hQQXRJTUhEZHB3NDRUZGpiWTVvUQ?oc=5) | Yahoo Finance |
| S24 | news | 2026-07-21 | [Prediction: MercadoLibre Stock Could Soar in the Next 5 Years if This Happens - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxPWEZ1dVZMaUlNWVEyM3FUal9rUVA1SXo2ZGZGek1mZVpwVnZFTGl3aEdhZXNIcDNmdnNIZzRLVkRvT0JLNklvNVdlSTVnZGlNS2h0VUNtZFJsWHE3c2RDa3pONEZsdjlpM18zMmU3Y1RrTXFkWXNTNWE4TWZjQ2pVN2wzOVZ4ZEROSWlTTmx3ZXVhbV8tX25xNw?oc=5) | The Motley Fool |
| S25 | news | 2026-08-19 | [Should You Buy MercadoLibre Stock at $1,779 After Its Third Straight Profit Decline? Here’s What Analysts Are Saying. - TIKR.com](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQVTRQS0ZIWUUyNXQyTGlVWWRka1VIQmE1eUhudmZrOXpoMy1ZV1drZE9JMjRDYVlyb1dGYUt1MTdtVEJTU1RhNlRIMXM5UERmX09Md2VsTlViY041bGc0RXFoV0VsZEYwUXZYaGFBdTBrRmt3eS1vZFF6MnNHd3JtZTdpUFkzSmRkblJZVkdMMzBndi1FY3lHY2hpUk83Um5hMWg4TllkWFY0NG1sSnJZTGFvTG9MQmNNYkpmOVNnQ2pqQzcxbWVxRkdQVTQwNUtZT2ZVSg?oc=5) | TIKR.com |
| S26 | news | 2026-07-23 | [MercadoLibre pitches in-house pharmacy to Chile after launch in Brazil - Reuters](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOZHYxOGV0bHBpb3c5VzJGc29QdzZqemxfb2o3OGRhVlRrLVVBOFBaSXg0QWxOdTJyS2ZPdmRFdG5xZHdpOExYblFKb3J6QnBHUng2MHlRZjlSWWJpclN4SkNvSXcxX0U5RmxlQU1WSnpiUmwyQlhleVJIZW9DQ3o2MVY4eEJDeVlSRjBKNUEzek1lcmpxbUVrRjQ2a1FEaHQzWjdpR3VtMDdJdFk1MWJBdGF0Q0k5X2tELTNsOUNtMUE4WXc0ZVJpeUxQM0UxZHM4UHc?oc=5) | Reuters |
| S27 | news | 2026-08-05 | [MercadoLibre beats estimates but shares dip on margin concerns - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxNQ3lUYjRFWkVIdVNMM2J4a1JxaHkxS3pJS202cHdocGprVXRnaENUUlVZWFRwdXNHSDJval9fM242eXQzN3RyNEF0THRabzNLUWlYNWdWcGl0SnRLaVNMaGoycHN0OFIzY0pyMXFENjBLUWRxVHJ3V0VUaUlILWs0YzR5V0RFS3dvSzg2RHMwc0ZSS19ST2s2dWVsNXlYWDYtMFk3c2Z5UQ?oc=5) | Yahoo Finance |
| S28 | news | 2026-07-31 | [Should You Buy MercadoLibre Stock Before Aug. 5? - The Motley Fool](https://news.google.com/rss/articles/CBMikwFBVV95cUxQNWlSOUpQVXRpVWg0TmkwM1VYS2EzOUdER0JtNEFFOEt3SURlNGZ4YTkxck9pOFRNT0JhYTYzYjZhbUdBYVVpejQ5SGR2SVY2dWNxOUFlcXVnT0VSUmh2MUxfT1EtYmZuSmhqUFNFaHJia0NZX3V6a3dsYkZ5UnQxQUY5MVVwZHZ0WXlPeHdzSm1GcXc?oc=5) | The Motley Fool |
| S29 | news | 2026-08-19 | [MercadoLibre (MELI) Is Down 8.3% After Q2 Revenue Rose But Profitability Weakened – Has The Bull Case Changed? - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxPQ21DUjlNNzNaRnFSY19UT3BjMnRmYjU5bENNZGVIajZIcWw3bUhTWUxpNVk3OGV1RGR3N240MzBCUXZSdHRYc250SE1yM2VzekpZLTloYlVpcmxHc0dldnhxYzJhdksyMUdDam5uRUVJY3BnOXFfTDVKMkZQMElkSEtXd2VfTGZWT0lZYjFLRlZhWXBqZHc?oc=5) | Yahoo Finance |
| S30 | news | 2026-08-13 | [Prediction: MercadoLibre Will Join Amazon, Walmart, and Costco in the $100 Billion Revenue Club by 2029 - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxNRE0tbXM0OXRYWUZibjdlX3I4bnU4Yldfd0F1aTNkUEFBamNoai03TENuVm90aFRDYWx5R2Q2UEF2a3JqWlNoMmdNSVBaaXBjcnRYZ1NOU3QtV0ZxTERsTmVYOFVpRUJuRmNTLVE4VXl1RE8xM3FTM1lhQ29ZaWpqcjRCZ0VyMnRHZXZ1OHNvMWVrSHFVckhoaA?oc=5) | The Motley Fool |
| S31 | news | 2026-08-19 | [Here’s Why MercadoLibre (MELI) Offers Long Runway for Growth? - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxOVmtBSUY0WEhmaDZPWkJOVnlhNWdiZWd4YTNoRUI4SS1JdjBkNkJJUE14dlBNN1dGRUlNaHIwb2lycUJDU29QcWlFMUxfNGVpd1Bhd2RxaDdpMURuUHNCVFhROC04YXNEc2xMN2k5M0NXaWd4ZG5YX09CVHVOaDEyTzFHMkFnODNqaG41Y0ozbi1YNkFzdWp3bWs5azdwVTQ?oc=5) | Yahoo Finance |
| S32 | news | 2026-07-31 | [Should You Buy MercadoLibre Stock Before Aug. 5? - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxPZXFRVDdIaFZseDlacU1iTXpCWEN0Y0xMblZIZmxGaEFnOWRsOG4yQWxDTFFnUWZfNjZKTDBBNlRzY2VTRmd0Y3hTSVdCdTVJc093bE1mZVdyRXozLU1zU0stTnc3SVlyWDdKNHVqaDNzLXBJLTFTWVVMSkMyVGtFUWhFSm53WGEtU2FpQUZEdWMyeTU3ZFEwRg?oc=5) | Yahoo Finance |
| S33 | news | 2026-08-13 | [MercadoLibre (MELI) Stock Trades Up, Here Is Why - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxPV1lNSUVzM0cwekx2Y0VSSURMZ01HTWc0SUVobkhsb3pNblVkNmNRVWQxbGJUcWZ2MnFzbDlGVjFFTDEzalNEYVZBLVdudVg1V25TdGZrekpFQ3lMSWpDd0tFTnFFTmVJS1M2dDhITWVTbUJoaHZkYjNVY2pwbmZ3ZGdSZXpmSFBWUFc4ZWdsTDVwMGFKanBidWZuZXJ6Tksy?oc=5) | Yahoo Finance |
| S34 | news | 2026-08-06 | [MercadoLibre Posted Its Fastest Growth in Four Years and a Third Profit Drop - Yahoo Finance](https://news.google.com/rss/articles/CBMipwFBVV95cUxObU1yMnR3bVFaeXpCcS1zN0I3YUxnQXpGZDl6VFhsSk10LXlrNzZHc2tCdWRXVmZ3RnNrNDZ4bk92Zjl0ZTNQamVHWHFIZFlHM3A3aFFSZVdJTjJkT0w4SlBycHR0Vkltd0FkTGFMZ1ZNdVpad0I5anJUVmZ5VU83aHByU0pzRFZEUjlLbEI2aWFfN18wYXNYQlc4bndOeXctMTl6WGJvdw?oc=5) | Yahoo Finance |
| S35 | news | 2026-07-31 | [Stay Ahead of the Game With MercadoLibre (MELI) Q2 Earnings: Wall Street's Insights on Key Metrics - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxNa2gtSDJrd3I5cVR4NUR4YnJJTXJoZFVDMVpvWmhQMXA0cUV5R1hGN3o4a1ZzNFE2SXlYbEJCSWtkUW1Jc3lWaGRtT1lLVW9MQnJVXzc0OWY2cTd6WlpNcGVMUFFxbHJibVVWUWpfc2ZQaGRQajk5ZWl1aVd6UWdoMmhuc2xna2o1NHpmV09uVTA5MkRncHNJSnZPLUtIb0k?oc=5) | Yahoo Finance |
| S36 | news | 2026-10-17 | [MercadoLibre, Inc. (MELI) Stock Price, News, Quote & History - Yahoo! Finance Canada](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9zN2ZGWE5MSkl2WWI1OU5BYU9TYkZQbE1ockVqVXJ3QTZadmxOVXNRczdsbjBnenpyZElVVnEybUE0ZlllTXJtWTBIYmNSUWd6THc?oc=5) | Yahoo! Finance Canada |
| S37 | news | 2026-08-09 | [MercadoLibre (MELI) Stock Looks Reasonable On Cash Flow But Rich On Earnings - Yahoo Finance](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQOGlqUXl6dUZFZ2JVa0k5YUVrZFZYbWU0V1QxeW5JaDVVWWNBNEZyNk1wSmJUTTNyaE11Mk0xX0oweFBtM1lRTlp5ZHM3ekY3SEYxTUtGeThXNmpPSXdMZzNVN2VBaTRqOWNNZlVFN2JqTWt2YmVpay02ZGdGQmtsYjZYbW8wVGxuWWtLWXJhX0FhQVBZX3oyVUo5ZGFISTZOMGJQM1QxcW0?oc=5) | Yahoo Finance |
| S38 | news | 2026-08-15 | [MercadoLibre (MELI) Bets Big On Growth. Is The Payoff Worth The Wait? - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxPT01jZFFxeWxlaTRLUWNsZ2F6bGdzWUZicEFoZ1VvUW81UHZNN3p6aUktUFdHX1ZpR2tid29UM241c3ZZMU1RY3B0MHFGNWRRQjVjRy1TWkFJUlhObGVpNHlYTHQ5QWk0am9BYW5iMUR1eUlpWXotTHhGaV9VQ2Q0Uk8zYlpDcGtMQnBDVFRRdG9tY09BMTA3QkxwVUxnYmM?oc=5) | Yahoo Finance |
| S39 | news | 2026-08-10 | [MercadoLibre Sacrifices Margins for Growth: Is the Strategy Paying Off? - Yahoo Finance](https://news.google.com/rss/articles/CBMisgFBVV95cUxNSlQtMV84SlptSERqZk1NSE9WSGRzU3VTQ1p1XzM5TWNKTDh5cVBobzdkWmhpcGQ2eHA1UWhjRUEwUDVUTXlocjdaYkxLdVVDTGRhdmo4WFduTlJscS1vc0dKekF4ZEdnYkFoQ0YwRWZPelo0QThUZzZWemF5dDlzbG1icDRXLWJVVmQ0Qk9hRFB1bV9PZXZjMi05WmJPNVFwbzlXY3MzQUprMFAycDZmX2Zn?oc=5) | Yahoo Finance |
| S40 | news | 2026-08-03 | [Why MercadoLibre (MELI) Is Spending Big to Defend Its Latin American Moat - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxQV3NfQ1N1MWxxTlF0V3VNNWNRVlBhV2JhOW51SXdySXpQTEVPR09zYlNONWJodk5BdXRWcElaVUptSExrbW9lZlpXUENzOGFRbnJyV0d1OUNIU3BiTktZSnBpSWo0RnFfakJvUFVKbXMyNWZBckgwdVNZaDB6TUJJT1RTd1pkcWlxN0JWX0RqS1JtZ2J4bmZNZUIyUDAyU2s0?oc=5) | Yahoo Finance |
| S41 | news | 2026-07-29 | [MercadoLibre, Inc. to Report Second Quarter 2026 Financial Results - Yahoo Finance](https://news.google.com/rss/articles/CBMipgFBVV95cUxNVGhBdXhwTVl1OC1INzlIb1BaMm5OMXozQm9YSTdUSHh5STVINWEwMGJhTGZwZ202WllfWjQzT244TmpSTjc1M05GN1VoaGdwVGVKdlloTXI2VGdUbFJxWnhhb2JoOVJ4QV9uQ1JwYThXUlliTC1DUW5XRWJsSW5EbzdydWhXc0hwdmVGMThaRmgzQTBVMlRVblQ4TlJiaklxRUVaWEt3?oc=5) | Yahoo Finance |
| S42 | data | 2026-10-03 | [MELI share price (investsmart.com.au)](https://www.investsmart.com.au/security/nasdaq/meli/mercadolibre/share-price) | 2026-10-03 종가 $1,696.24 (거래량 90,060주, 장중 $1,679.27~$1,709.36). 연초 대비 약 -15.7%, 2026 고가 $2,342·저가 $1,495. 2026-10-17 종가는 확인하지 못했고 집계 사이트 수치라 검증되지 않았다. |
| S43 | news | 2026-08-05 | [Chartmill: MercadoLibre Beats Q2 Estimates but Shares Fall 6.6% After Hours](https://www.chartmill.com/news/MELI/Chartmill-52866-MercadoLibre-NASDAQMELI-Beats-Q2-Estimates-but-Shares-Fall-66-After-Hours) | 보도: 2분기 순매출 약 102억 달러(전년 대비 약 +50%), 컨센서스 매출 약 98.6억 달러, 비GAAP EPS 9.19달러(컨센서스 8.69~8.83달러). 마진은 직전 분기와 비슷하나 전년 대비 하락. 시간외 주가 약 -6.6%. 공식 가이던스 없음. 2차 자료. |
| S44 | news | 2026-08-19 | [TIKR: MercadoLibre Stock Hits a Four-Year Revenue High While Shares Are Down 17% in 2026](https://www.tikr.com/blog/mercadolibre-stock-hits-a-four-year-revenue-high-while-shares-are-down-17-in-2026) | 보도: 월가 컨센서스는 매수. 목표주가 하단 약 1,750달러, 상단 약 2,600달러, 평균 약 2,167달러 (애널리스트 33명, 집계 사이트 기준). 2026년 EPS 추정은 어닝 전 기준 약 41달러. |

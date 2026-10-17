# MercadoLibre (MELI) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 모델** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✗ model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

## 1. Variant perception

- 시장이 반영한 것: 컨센서스는 매수이고 평균 목표주가가 2,167달러다(F221). 현재 주가 1,696달러(F214)는 연초 대비 하락한 수준이어서, 시장은 높은 성장은 인정하되 3분기 연속 감소한 이익과 마진 하락을 할인하고 있다. 정확히 얼마의 성장과 FCF 마진을 가정하는지는 역DCF(C:implied_cagr)로 확인해야 한다. 연도별 매출 컨센서스는 확보하지 못해 모델과 직접 대조할 수 없다.
- 우리가 다르게 보는 점: 마진 하락의 핵심은 성장 투자와 신용 확대라는 선택의 결과이고 영구적인 경쟁력 훼손이 아니라고 본다. 단, 이 판단은 신용 건전성 자료가 없어 가설 수준이다. 이익이 늘지 않는 성장이 4분기 이상 이어지면 이 견해는 틀린 것으로 본다.
- 왜 우리가 맞는가: 매출이 +50% 늘면서 영업이익이 -17%다. 이는 비용 증가가 신용 확대와 물류 투자에서 나온다는 회사의 선택과 일치하고(S39, S40), 이 투자 비용이 먼저 나가고 매출은 뒤에 따라오는 구조라면 시차가 지나며 마진이 회복된다. 그러나 연체율과 대손충당금을 확인하지 못했으므로, 이 논거는 증명되지 않았고 반증 가능한 가설로만 쓴다. [F214] [F221] [F136] [F133] [F220] [S22](https://news.google.com/rss/articles/CBMitwFBVV95cUxQZFRkMnJTWlZLT19MaVcydlhlQ3NkUklRS1UxMjJwTzY0dWVRbkoyeFc0ejF5QmVfcmItUDNkMjJsQXJMbUlWdFRXNEppcnk4bkswTFNGd3JydDhEd0VDRlVELWI2TzJldWx6ellLbHdnNnJGT0s4TjlZLW9ZeERlMlhfX0s1dFhia0FHbEdBYzlxbmQ1X0txU1pCMGFEZUxDTXVjNVFfUFFSdlBXZ2x3azNELTFvRTg?oc=5) [S34](https://news.google.com/rss/articles/CBMipwFBVV95cUxObU1yMnR3bVFaeXpCcS1zN0I3YUxnQXpGZDl6VFhsSk10LXlrNzZHc2tCdWRXVmZ3RnNrNDZ4bk92Zjl0ZTNQamVHWHFIZFlHM3A3aFFSZVdJTjJkT0w4SlBycHR0Vkltd0FkTGFMZ1ZNdVpad0I5anJUVmZ5VU83aHByU0pzRFZEUjlLbEI2aWFfN18wYXNYQlc4bndOeXctMTl6WGJvdw?oc=5) [S39](https://news.google.com/rss/articles/CBMisgFBVV95cUxNSlQtMV84SlptSERqZk1NSE9WSGRzU3VTQ1p1XzM5TWNKTDh5cVBobzdkWmhpcGQ2eHA1UWhjRUEwUDVUTXlocjdaYkxLdVVDTGRhdmo4WFduTlJscS1vc0dKekF4ZEdnYkFoQ0YwRWZPelo0QThUZzZWemF5dDlzbG1icDRXLWJVVmQ0Qk9hRFB1bV9PZXZjMi05WmJPNVFwbzlXY3MzQUprMFAycDZmX2Zn?oc=5) [S40](https://news.google.com/rss/articles/CBMioAFBVV95cUxQV3NfQ1N1MWxxTlF0V3VNNWNRVlBhV2JhOW51SXdySXpQTEVPR09zYlNONWJodk5BdXRWcElaVUptSExrbW9lZlpXUENzOGFRbnJyV0d1OUNIU3BiTktZSnBpSWo0RnFfakJvUFVKbXMyNWZBckgwdVNZaDB6TUJJT1RTd1pkcWlxN0JWX0RqS1JtZ2J4bmZNZUIyUDAyU2s0?oc=5) [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results)
- 촉매: 3분기 실적에서 영업이익과 순이익이 전년 대비 반등하는지, 신용 포트폴리오의 연체율과 충당금이 공개되는지.
- 시점: 2026년 3분기 실적 발표(2026년 11월 전후)부터 4분기까지

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ 주가 기준일 2026-10-03이 as_of(2026-10-18)보다 15일 오래됨
- ⚠ 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 분석 모듈 (L4)

### 사업·산업 — unclear

MercadoLibre는 중남미에서 이커머스 마켓플레이스와 물류, 핀테크(결제·신용)를 한 생태계로 묶어 돈을 번다. 수익원은 판매 수수료, 광고, 물류, 결제 처리, 신용 이자다. 2026년 2분기 순매출·금융수익은 101.7억 달러(F215), GMV는 219.0억 달러(F218), TPV는 1,010.0억 달러(F219)다. 신용 포트폴리오는 164.0억 달러(F220)까지 커졌다. 단위경제는 성장 쪽은 강하지만 수익성은 약해지고 있다. 2분기 영업이익은 6.8억 달러(F136)로 전년 동기 8.2억 달러(F133)보다 줄었고, 영업이익률은 6.7%다(S46). 연간 영업이익률도 FY2023 21.0%에서 FY2025 15.7%로 내려왔다(C:operating_margin@FY2023, C:operating_margin@FY2025). 회사가 성장과 신용 확대, 물류 투자를 위해 마진을 희생하는 국면으로 보인다(S39, S40). 고객 단위의 CAC, 이탈률, 코호트 자료는 근거에 없어서 단위경제를 판정할 수 없다. 해자 주장은 대부분 회사 발표와 보도에 기대고 있다.

- [unit_economics] 2026년 2분기 영업이익은 6.8억 달러로 전년 동기 8.2억 달러보다 낮다. 영업이익률은 6.7%이고, 매출은 +50% 늘었는데 영업이익은 -17%다. 성장이 이익으로 이어지지 않는다. 순이익도 3분기 연속 감소했다고 보도됐다(S22, S34). 2분기 순이익은 4.7억 달러로 전년 동기 5.2억 달러보다 낮다. [F136] [F133] [F119] [F116] [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results) [S22](https://news.google.com/rss/articles/CBMitwFBVV95cUxQZFRkMnJTWlZLT19MaVcydlhlQ3NkUklRS1UxMjJwTzY0dWVRbkoyeFc0ejF5QmVfcmItUDNkMjJsQXJMbUlWdFRXNEppcnk4bkswTFNGd3JydDhEd0VDRlVELWI2TzJldWx6ellLbHdnNnJGT0s4TjlZLW9ZeERlMlhfX0s1dFhia0FHbEdBYzlxbmQ1X0txU1pCMGFEZUxDTXVjNVFfUFFSdlBXZ2x3azNELTFvRTg?oc=5) [S34](https://news.google.com/rss/articles/CBMipwFBVV95cUxObU1yMnR3bVFaeXpCcS1zN0I3YUxnQXpGZDl6VFhsSk10LXlrNzZHc2tCdWRXVmZ3RnNrNDZ4bk92Zjl0ZTNQamVHWHFIZFlHM3A3aFFSZVdJTjJkT0w4SlBycHR0Vkltd0FkTGFMZ1ZNdVpad0I5anJUVmZ5VU83aHByU0pzRFZEUjlLbEI2aWFfN18wYXNYQlc4bndOeXctMTl6WGJvdw?oc=5)
- [unit_economics] 연간 마진은 장기적으로 내려오고 있다. 영업이익률은 FY2023 21.0%, FY2024 17.4%, FY2025 15.7%다. 같은 기간 총이익률은 72.4%에서 63.3%, 63.2%로 내려왔다. 총이익률 하락의 원인(신용 비용, 무료배송, 믹스 변화)은 근거로 분해하지 못했다. 원인을 모르므로 악화 판정은 보류하고 unclear로 둔다. [C:operating_margin@FY2023] [C:operating_margin@FY2024] [C:operating_margin@FY2025] [C:gross_margin@FY2023] [C:gross_margin@FY2024] [C:gross_margin@FY2025]
- [unit_economics] CAC 회수기간, 순매출유지율, 이탈률, 코호트, 신용 연체율(NPL), 대손충당금은 수집하지 못했다. 이 항목이 없으면 신용 확대가 수익성 있는 성장인지 판단할 수 없다. 이것이 이번 사업 분석의 가장 큰 공백이다. [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results) [S45](https://quartr.com/events/mercadolibre-inc-meli-q2-2026_3ePJ0gcZ)
- [runway] 재투자 수요가 크다. 2분기 설비투자는 4.4억 달러이고, 신용 포트폴리오 증가에 21억 달러가 들어갔다. 신용 포트폴리오는 164.0억 달러다. 2분기 조정 FCF는 2.1억 달러로 얇다. 성장 활주로는 길지만 현금으로 자체 조달하는 단계가 아니라 외부 자금과 부채에 기대고 있다. [F216] [F217] [F220] [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results)
- [runway] 재무 부담이 올라가고 있다. 부채는 FY2024 57.1억 달러에서 FY2026Q2 106.3억 달러로 늘었다. 같은 시점 현금은 36.5억 달러, 단기투자는 20.8억 달러다. 신용 자산을 부채로 조달하는 구조이므로 사업의 질은 대출 자산의 건전성에 크게 좌우된다. [F39] [F45] [F18] [F187]
- [industry] 경쟁 방어에 돈을 쓰고 있다. 보도는 라틴아메리카에서 해자를 지키려고 큰 지출을 한다고 전한다(S40). 자체 약국 사업을 브라질에 이어 칠레로 확장하려는 시도도 있다(S26). 신규 영역 진출은 TAM을 넓히지만 투자 부담도 키운다. 경쟁사 대비 마진 자료는 없어 상대 우위는 입증하지 못했다. [S40](https://news.google.com/rss/articles/CBMioAFBVV95cUxQV3NfQ1N1MWxxTlF0V3VNNWNRVlBhV2JhOW51SXdySXpQTEVPR09zYlNONWJodk5BdXRWcElaVUptSExrbW9lZlpXUENzOGFRbnJyV0d1OUNIU3BiTktZSnBpSWo0RnFfakJvUFVKbXMyNWZBckgwdVNZaDB6TUJJT1RTd1pkcWlxN0JWX0RqS1JtZ2J4bmZNZUIyUDAyU2s0?oc=5) [S26](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOZHYxOGV0bHBpb3c5VzJGc29QdzZqemxfb2o3OGRhVlRrLVVBOFBaSXg0QWxOdTJyS2ZPdmRFdG5xZHdpOExYblFKb3J6QnBHUng2MHlRZjlSWWJpclN4SkNvSXcxX0U5RmxlQU1WSnpiUmwyQlhleVJIZW9DQ3o2MVY4eEJDeVlSRjBKNUEzek1lcmpxbUVrRjQ2a1FEaHQzWjdpR3VtMDdJdFk1MWJBdGF0Q0k5X2tELTNsOUNtMUE4WXc0ZVJpeUxQM0UxZHM4UHc?oc=5)
- [customers] 재고와 매출채권이 빠르게 늘고 있다. 재고는 FY2025 5.7억 달러에서 FY2026Q2 8.2억 달러로 늘었고, 매출채권은 3.7억 달러에서 4.2억 달러로 늘었다. 직접 판매나 물류 재고 투자가 확대됐을 가능성이 있다. 이 부분의 사업적 설명은 근거에 없다. 회계 신호(inventory_gap, receivables_gap)는 forensic이 따로 다룬다. [F107] [F109] [F154] [F156] [C:inventory_gap]
- [industry] 공시 기준 매출(XBRL)과 회사가 보고하는 순매출·금융수익이 다르다. 2분기 XBRL 매출은 70.5억 달러이고 순매출·금융수익은 101.7억 달러다. 따라서 코드 계산 매출과 마진(예: 총이익률)은 합계 매출 기준과 다른 분모를 쓴다. 이 수치를 해자의 마진 증거로 쓸 때 주의가 필요하다. [F166] [F215] [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results)
- [claimed] 마켓플레이스 판매자·구매자와 결제 네트워크가 서로를 키우는 구조다. 2분기 GMV 219.0억 달러, TPV 1,010.0억 달러라는 거래 규모는 이를 뒷받침하는 흔적이다. 다만 점유율 추이, 고유 구매자 수, 핀테크 활성 사용자는 확보하지 못했다. 거래 규모만으로는 경쟁사 대비 우위를 입증하지 못한다. 방어 지출 보도(S40)도 해자가 위협받는다는 신호일 수 있다. [F218] [F219] [S40](https://news.google.com/rss/articles/CBMioAFBVV95cUxQV3NfQ1N1MWxxTlF0V3VNNWNRVlBhV2JhOW51SXdySXpQTEVPR09zYlNONWJodk5BdXRWcElaVUptSExrbW9lZlpXUENzOGFRbnJyV0d1OUNIU3BiTktZSnBpSWo0RnFfakJvUFVKbXMyNWZBckgwdVNZaDB6TUJJT1RTd1pkcWlxN0JWX0RqS1JtZ2J4bmZNZUIyUDAyU2s0?oc=5)
- [claimed] 매출은 FY2021 57.1억 달러에서 FY2025 203.3억 달러로 커졌고, 2026년 2분기 순매출·금융수익은 전년 대비 +50%다. 이 규모가 물류·결제 고정비를 분산하는 원천이다. 그러나 규모 확대에도 총이익률은 FY2023 72.4%에서 FY2025 63.2%로 내려갔다. 이 비율은 XBRL 기준 매출을 쓴 것이라 합계 매출 기준 값과 다를 수 있다. 규모의 경제가 마진으로 드러난다는 흔적은 아직 없다. [C:revenue@FY2021] [C:revenue@FY2025] [C:gross_margin@FY2023] [C:gross_margin@FY2025] [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results)
- [claimed] 결제·신용·물류를 한 계정에서 쓰게 하면 전환비용이 생긴다는 논리다. 가격 인상 후 고객이 남은 기록이나 이탈률 같은 직접 증거는 없다. 신용 포트폴리오 164.0억 달러는 고객 락인 수단이면서 동시에 위험 자산이기도 하다. [F220] [S31](https://news.google.com/rss/articles/CBMinwFBVV95cUxOVmtBSUY0WEhmaDZPWkJOVnlhNWdiZWd4YTNoRUI4SS1JdjBkNkJJUE14dlBNN1dGRUlNaHIwb2lycUJDU29QcWlFMUxfNGVpd1Bhd2RxaDdpMURuUHNCVFhROC04YXNEc2xMN2k5M0NXaWd4ZG5YX09CVHVOaDEyTzFHMkFnODNqaG41Y0ozbi1YNkFzdWp3bWs5azdwVTQ?oc=5)

### 경영진·자본배분 — mixed

경영진의 정렬을 판단할 핵심 근거가 비어 있다. DEF 14A의 보상 지표, 내부자 매매, 과거 가이던스는 사실로 정리되지 않았고, 2분기 발표에 정식 가이던스도 없었다고 보도됐다. 확인되는 것은 자본배분 행태다. 자사주 매입은 FY2023의 3.6억 달러 이후 FY2024·FY2025에 각 100만 달러로 사실상 멈췄다. 희석 주식 수는 5,070만 주로 정체했으니 희석은 통제되고 있다. 한편 부채는 FY2024 57.1억에서 FY2026Q2 106.3억 달러로 늘었고, 신용 포트폴리오는 164.0억 달러에 이른다. 마진을 줄이면서 성장과 신용 확대에 투자하는 전략이며 주주 수익률보다 재투자가 우선이다. 이 전략이 주주에게 득이 될지는 보상 구조와 ROIC로 판단해야 하는데 보상 근거가 없다. 그래서 정렬 판단은 '혼재'로 둔다.

- [compensation] 근거 없음. DEF 14A(S8, 2026-04-23)는 근거 목록에 있으나 보상 연동 지표(장기 지표인지 단기 EPS·조정 EBITDA인지)와 베스팅 기간은 사실로 정리되지 않았다. 보상이 주주 가치와 맞물리는지 판단하지 않는다. [S8](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000010/meli-20260423.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도는 정리되지 않았다. 2026-04-03에 '경영진 변동' 8-K(S9)가 있으나 내용은 확인하지 못했으므로 해석하지 않는다. [S9](https://www.sec.gov/Archives/edgar/data/1099590/000199937126007656/meli_8k-033126.htm)
- [guidance] 신뢰도를 판단할 수 없다. 2분기 발표에 정식 가이던스가 없는 것으로 보도됐고, 과거 가이던스 사실이 없어 코드의 가이던스 적중률(C:guidance_hit_rate)도 산출되지 않았다. 컨센서스 대비로는 2분기 매출과 비GAAP EPS가 컨센서스를 웃돌았으나, 이는 경영진 약속의 이행과 다른 개념이다. [S43](https://www.chartmill.com/news/MELI/Chartmill-52866-MercadoLibre-NASDAQMELI-Beats-Q2-Estimates-but-Shares-Fall-66-After-Hours) [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results)
- [dilution] 희석 주식 수는 FY2022에 5,134만으로 늘었다가(C:share_change@FY2022 3.1%) FY2023·FY2024에 소폭 줄었고(각 -0.6%), FY2025에는 사실상 변동이 없다. 최근 희석은 크지 않다. 다만 SBC 규모(C:sbc_to_revenue)는 사실로 확보되지 않았고, 분기 희석 주식 수 5,070만이 반복되는 값이라 실제 분기값 확인이 필요하다. 희석 통제는 연간 수치로만 확인된다. [C:share_change@FY2022] [C:share_change@FY2023] [C:share_change@FY2024] [C:share_change@FY2025] [F54] [F58] [F59]
- [capital_allocation] 자사주 매입은 FY2021 4.9억, FY2022 1.5억, FY2023 3.6억 달러였다가 FY2024·FY2025에는 각 100만 달러로 거의 중단됐다. 현금을 주주환원보다 사업과 신용 확대에 쓰는 방향이다. 매입 시점의 주가 대비 수익률은 판단할 근거가 없다. [F1] [F2] [F3] [F4] [F5]
- [capital_allocation] 재투자는 자체 현금흐름만으로 조달되지 않고 차입으로 이어지고 있다. 부채는 FY2024 57.1억에서 FY2025 91.9억, FY2026Q2 106.3억 달러로 늘었다. 순현금은 FY2024 14.1억에서 FY2025 -28.9억 달러로 돌아섰고, 순부채/EBITDA는 FY2025에 0.72x다. 2분기에 신용 포트폴리오 증가에 21억 달러를 투입했고 포트폴리오는 164.0억 달러다. 연체율과 대손충당금은 확보되지 않아 이 신용 확대의 수익률은 검증할 수 없다. [F39] [F43] [F45] [F220] [C:net_cash@FY2024] [C:net_cash@FY2025] [C:net_debt_to_ebitda@FY2025] [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results)
- [capital_allocation] 성장 투자의 수익성은 약해지는 중이다. ROIC는 FY2023 91.4%, FY2024 70.2%에서 FY2025 23.3%로 낮아졌다. 영업이익률은 FY2023의 21.0%에서 FY2025의 15.7%로 내렸고, 2분기 영업이익률은 6.7%로 보도됐다. 2분기 설비투자는 4.4억 달러이고 조정 FCF는 2.1억 달러다. 경영진은 마진을 희생하며 성장을 선택했고, 보도(S39)도 이를 같은 취지로 전한다. 이 선택이 주주 가치를 더하는지는 이후 ROIC 회복으로 확인해야 한다. [C:roic@FY2023] [C:roic@FY2024] [C:roic@FY2025] [C:operating_margin@FY2023] [C:operating_margin@FY2025] [F216] [F217] [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results) [S39](https://news.google.com/rss/articles/CBMisgFBVV95cUxNSlQtMV84SlptSERqZk1NSE9WSGRzU3VTQ1p1XzM5TWNKTDh5cVBobzdkWmhpcGQ2eHA1UWhjRUEwUDVUTXlocjdaYkxLdVVDTGRhdmo4WFduTlJscS1vc0dKekF4ZEdnYkFoQ0YwRWZPelo0QThUZzZWemF5dDlzbG1icDRXLWJVVmQ0Qk9hRFB1bV9PZXZjMi05WmJPNVFwbzlXY3MzQUprMFAycDZmX2Zn?oc=5)
- [capital_allocation] 대형 인수의 흔적은 작다. 영업권은 FY2021 1.5억에서 FY2026Q2 1.7억 달러로 거의 변하지 않았다. 비싼 인수로 자본을 낭비한 이력은 근거에서 보이지 않는다. 성장은 인수가 아니라 자체 투자(R&D는 FY2025 22.7억 달러)로 이루어진 것으로 읽힌다. [F70] [F79] [F171]

### 회계 품질 — watch

코드가 낸 신호는 매출채권·재고 증가율 갭 두 개이고, 둘 다 사업 구조로 설명되며 숫자를 믿을 수 없다고 볼 근거는 아니다. 재정정, 감사인 변경, 순이익 흑자인데 영업현금흐름이 음수인 해는 없다. SBC, 희석(희석 주식 수가 5,070만 근처에서 거의 변하지 않음), 영업권, 이연매출에서도 문제가 없다. 다만 이 회사는 핀테크 신용 사업을 하기 때문에 영업현금흐름(FY2025 121.2억)이 이익의 질을 보여 주는 지표로 쓸 수 없다. 코드의 발생액 비율(-29.8%)과 OCF/순이익은 고객 예수금과 신용 투입의 영향으로 과도하게 좋게 나온다. 신용 포트폴리오(FY2026Q2 164.0억)가 커지고 있어 대손충당금과 연체율이 핵심 회계 판단인데, 이번 수집에서는 확인하지 못했다. 감사의견과 핵심감사사항도 확인하지 못했다. XBRL 매출(FY2026Q2 70.5억)과 보도자료의 순매출 및 금융수익(101.7억)이 정의가 달라 일치하지 않으니, 매출 규모와 마진은 하나의 정의로 맞춰서 봐야 한다. 증거가 부족하므로 red_flag는 아니고, 신용 사업 조정 FCF(FY2026Q2 2.1억)로 보고 대손충당금을 추적하는 watch로 판정한다.

- [benign] receivables_gap: FY2024 매출채권이 1.6억에서 2.5억으로 늘어 증가율이 매출 증가율을 19.1%p 앞섰다. 절대 규모가 작다. DSO가 5~7일(FY2024 6.1일, FY2025 6.6일)로 안정적이고 매출채권이 매출에서 차지하는 비중도 미미하다. 핀테크·마켓플레이스 결제 구조라 대부분 즉시 정산돼 채권 누적으로 매출을 부풀릴 여지가 작다. 신호는 작은 기저에서 나온 비율 착시에 가깝다. 신용 포트폴리오의 대출채권은 이 항목에 들어 있지 않으므로 별도로 봐야 한다. [C:receivables_gap] [F150] [F149] [C:revenue_growth@FY2024] [C:dso@FY2024] [C:dso@FY2025]
- [benign] inventory_gap: FY2025 재고가 3.0억에서 5.7억으로 늘어 증가율이 매출 증가율을 58.2%p 앞섰고, 이후 FY2026Q1 6.8억, FY2026Q2 8.2억으로 계속 늘고 있다. 직매입(1P) 확대와 브라질 약국 사업 등 신규 카테고리 선적재가 원인으로 보이나, 이는 사업 설명이지 이번에 확인한 사실이 아니다. 재고 절대 규모는 총자산 대비 작고 DIO도 13일(FY2025)이다. 재고 평가손이나 부진 재고 신호는 확인되지 않았다. 다만 갭이 두 해 연속 확대되고 있어 평가충당금과 재고 회전을 추적해야 한다. 지금은 우려 단계가 아니라 관찰 단계다. [C:inventory_gap] [F103] [F107] [F108] [F109] [C:dio@FY2025] [S26](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOZHYxOGV0bHBpb3c5VzJGc29QdzZqemxfb2o3OGRhVlRrLVVBOFBaSXg0QWxOdTJyS2ZPdmRFdG5xZHdpOExYblFKb3J6QnBHUng2MHlRZjlSWWJpclN4SkNvSXcxX0U5RmxlQU1WSnpiUmwyQlhleVJIZW9DQ3o2MVY4eEJDeVlSRjBKNUEzek1lcmpxbUVrRjQ2a1FEaHQzWjdpR3VtMDdJdFk1MWJBdGF0Q0k5X2tELTNsOUNtMUE4WXc0ZVJpeUxQM0UxZHM4UHc?oc=5)
- [watch] 영업현금흐름이 이익의 질을 보여 주는 지표로 쓸 수 없다. FY2025 OCF 121.2억은 순이익 20.0억의 약 6배이고, 코드의 발생액 비율이 -29.8%다. 고객 예수금(자금 지급 의무)과 신용 사업의 현금 흐름이 OCF에 섞여 있다. 회사의 조정 FCF는 FY2026Q2 2.1억에 그치고, 같은 분기 설비투자는 4.4억이며 신용 포트폴리오 증가에 21억이 투입됐다. 밸류에이션에서는 보고 OCF 기반 FCF 대신 조정 FCF와 신용 투입 차감 후 현금창출력을 써야 한다. [F124] [F114] [C:accruals_ratio@FY2025] [F217] [F216] [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results)
- [watch] 신용 사업의 대손충당금과 연체율을 확인하지 못했다. 신용 포트폴리오가 164.0억으로 총자산 513.6억의 상당 부분을 차지하고 부채도 106.3억으로 늘었다. 충당금 정책과 연체 추이가 이익의 가장 큰 회계 판단이다. 최근 3개 분기 순이익이 전년 대비 감소하는 와중에 충당금이 어떻게 움직였는지 확인이 필요하다. [F220] [F197] [F45] [S22](https://news.google.com/rss/articles/CBMitwFBVV95cUxQZFRkMnJTWlZLT19MaVcydlhlQ3NkUklRS1UxMjJwTzY0dWVRbkoyeFc0ejF5QmVfcmItUDNkMjJsQXJMbUlWdFRXNEppcnk4bkswTFNGd3JydDhEd0VDRlVELWI2TzJldWx6ellLbHdnNnJGT0s4TjlZLW9ZeERlMlhfX0s1dFhia0FHbEdBYzlxbmQ1X0txU1pCMGFEZUxDTXVjNVFfUFFSdlBXZ2x3azNELTFvRTg?oc=5)
- [watch] 매출 정의가 자료마다 다르다. XBRL revenue(FY2026Q2 70.5억)는 보도자료의 순매출 및 금융수익(101.7억)보다 작다. 코드가 이 갭을 어느 쪽으로 정리하느냐에 따라 마진과 성장률이 달라진다. 총액·순액 인식 정책과 금융수익 분류를 10-K·10-Q 원문으로 확인해야 한다. 이번에는 보도자료를 요약으로만 확인했다. [F166] [F215] [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results) [S4](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000021/meli-20260805.htm)
- [info] 코드 신호에 non_gaap 항목이 없다. 2분기 비GAAP EPS가 보도됐으나(S43) 조정 항목의 크기는 수집하지 못했다. 회사는 조정 FCF를 별도 지표로 제시하므로 정의를 10-Q에서 확인하는 것이 좋다. [S43](https://www.chartmill.com/news/MELI/Chartmill-52866-MercadoLibre-NASDAQMELI-Beats-Q2-Estimates-but-Shares-Fall-66-After-Hours) [F217]
- [info] 감사의견, 계속기업 의문, 핵심감사사항, 재무제표 정정(8-K 4.02), 감사인 변경(4.01) 여부는 이번 수집에서 사실로 정리되지 않았다. 코드의 restatement·auditor_change 신호는 나오지 않았다. 확인한 공시 목록에서도 정정이나 감사인 변경으로 볼 만한 8-K는 없다. 미확인이므로 clean으로 올리지 않는다. [S10](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000006/meli-20251231.htm) [S1](https://www.sec.gov/Archives/edgar/data/1099590/000114036126036495/ef20081942_8k.htm) [S5](https://www.sec.gov/Archives/edgar/data/1099590/000199937126012770/meli-8k_060926.htm)
- [info] 영업권이 총자산의 극히 일부(1.7억/513.6억)이고, 이연매출은 0.77억에서 1.3억으로 늘어 소폭이다. 희석 주식 수는 5,070만으로 FY2024부터 변하지 않았다. 다만 분기 희석 주식 수가 5,070만으로 반복되는 값이어서 실제 분기별 수치 확인이 필요하다. 소프트웨어 자본화 지표는 수집되지 않았다. [F79] [F197] [F48] [F49] [F54] [F59]

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 신용 포트폴리오 부실화. 신용 포트폴리오가 164.0억 달러(F220)까지 빠르게 커졌고 2분기에만 21억 달러가 투입됐다(S46). 연체율과 대손충당금은 공개 근거가 없다(미확인). 브라질·멕시코·아르헨티나의 거시 충격이나 신규 차주 대출의 부실이 겹치면 대손비용이 급증한다. 충당금이 뒤늦게 쌓이면서 이익이 급감하고, 부채 106.3억(F45)으로 조달한 자산이라 손실이 자기자본(78.3억, F69)을 직접 갉는다. 시장은 이익 질에 대한 신뢰를 잃고 배수를 대폭 낮춘다. [F220] [F45] [F69] [S46](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results) [S22](https://news.google.com/rss/articles/CBMitwFBVV95cUxQZFRkMnJTWlZLT19MaVcydlhlQ3NkUklRS1UxMjJwTzY0dWVRbkoyeFc0ejF5QmVfcmItUDNkMjJsQXJMbUlWdFRXNEppcnk4bkswTFNGd3JydDhEd0VDRlVELWI2TzJldWx6ellLbHdnNnJGT0s4TjlZLW9ZeERlMlhfX0s1dFhia0FHbEdBYzlxbmQ1X0txU1pCMGFEZUxDTXVjNVFfUFFSdlBXZ2x3azNELTFvRTg?oc=5)
- (25%) 경쟁 방어 지출의 영구화. 마진 하락은 투자 시차가 아니라 가격·물류 보조금 경쟁의 결과일 수 있다. 매출이 +50%인데 영업이익이 −17%이고 영업이익률이 6.7%다(S46). 영업이익률은 FY2023 21.0%에서 FY2025 15.7%로 이미 내려왔다(C:operating_margin@FY2023, C:operating_margin@FY2025). 경쟁사가 무료배송·핀테크 수수료로 계속 맞서면 규모가 커져도 마진이 회복되지 않는다. 성장이 둔화하는 순간 성장주 배수가 사라지고 이익도 낮아 이중 타격이 된다. [F136] [F133] [S40](https://news.google.com/rss/articles/CBMioAFBVV95cUxQV3NfQ1N1MWxxTlF0V3VNNWNRVlBhV2JhOW51SXdySXpQTEVPR09zYlNONWJodk5BdXRWcElaVUptSExrbW9lZlpXUENzOGFRbnJyV0d1OUNIU3BiTktZSnBpSWo0RnFfakJvUFVKbXMyNWZBckgwdVNZaDB6TUJJT1RTd1pkcWlxN0JWX0RqS1JtZ2J4bmZNZUIyUDAyU2s0?oc=5) [S39](https://news.google.com/rss/articles/CBMisgFBVV95cUxNSlQtMV84SlptSERqZk1NSE9WSGRzU3VTQ1p1XzM5TWNKTDh5cVBobzdkWmhpcGQ2eHA1UWhjRUEwUDVUTXlocjdaYkxLdVVDTGRhdmo4WFduTlJscS1vc0dKekF4ZEdnYkFoQ0YwRWZPelo0QThUZzZWemF5dDlzbG1icDRXLWJVVmQ0Qk9hRFB1bV9PZXZjMi05WmJPNVFwbzlXY3MzQUprMFAycDZmX2Zn?oc=5) [C:operating_margin@FY2023] [C:operating_margin@FY2025]
- (15%) 외부 자금 의존과 금리·조달 충격. 이 사업은 자체 현금으로 성장을 조달하지 못한다. 2분기 조정 FCF는 2.1억(F217)인데 설비투자 4.4억(F216)에 신용 확대 21억이 들었다. 부채는 FY2024 57.1억에서 106.3억으로 거의 두 배가 됐다(F39, F45). 자본시장이 닫히거나 조달금리가 오르면 신용 확대를 줄여야 하고, 성장과 이익이 동시에 꺾인다. 현금 36.5억(F18)은 부채 규모에 비해 얇다. [F217] [F216] [F39] [F45] [F18]
- (10%) 신용 확대가 멈추거나 재고·실물 사업 확대의 손실. 재고는 FY2025 5.7억에서 FY2026Q2 8.2억으로 늘었고(F107, F109), 직매입·약국 등 신규 영역(S26)이 투자 부담을 키운다. 신규 영역이 규모에 도달하지 못하면 재고 평가손과 고정비가 쌓인다. 규제 변화(핀테크 신용 규제)가 신용 확대 자체를 제한할 가능성도 있다. 성장 서사가 약해지면 컨센서스 기대(목표가 평균 2,167달러, F221)가 한꺼번에 내려간다. [F107] [F109] [S26](https://news.google.com/rss/articles/CBMi0gFBVV95cUxOZHYxOGV0bHBpb3c5VzJGc29QdzZqemxfb2o3OGRhVlRrLVVBOFBaSXg0QWxOdTJyS2ZPdmRFdG5xZHdpOExYblFKb3J6QnBHUng2MHlRZjlSWWJpclN4SkNvSXcxX0U5RmxlQU1WSnpiUmwyQlhleVJIZW9DQ3o2MVY4eEJDeVlSRjBKNUEzek1lcmpxbUVrRjQ2a1FEaHQzWjdpR3VtMDdJdFk1MWJBdGF0Q0k5X2tELTNsOUNtMUE4WXc0ZVJpeUxQM0UxZHM4UHc?oc=5) [F221]
- 약한 가정 `base.fcf_margin`: 기본 시나리오 FCF 마진 11%는 근거가 약하다. 현재 조정 FCF는 2분기 2.1억으로 합계 매출 101.7억 대비 약 2%이고(F217, F215), 영업이익률도 6.7%다. 11%까지의 회복은 마진 하락이 일시적이라는 미검증 가설에 전적으로 기대며, 연체율 자료도 없다. 기준 매출도 XBRL 정의(FY2025 203.3억)와 합계 매출 정의가 달라 마진 분모가 어긋난다. [F217] [F215] [F136] [C:operating_margin@FY2025]
- 약한 가정 `base.exit_multiple`: 출구 배수 25는 성장이 15%대로 둔화한 기업에 대한 가정인데, 현재 PER이 46.2배(C:pe)이고 순부채가 늘고 있으며 신용 위험이 큰 금융형 사업을 포함한다. 금융 비중이 큰 기업에는 낮은 배수가 붙는 경향이 있어 bear의 14가 더 현실적일 수 있다. [C:pe] [F45] [F220]
- 약한 가정 `base.revenue_growth`: 첫해 40%와 이후 30%, 24%의 고성장 경로는 기저율상 드문 값일 가능성이 크다. 대규모 매출에서 5년 연속 두 자릿수 후반 이상 성장을 유지하는 비율은 낮다. 기준 매출 203.3억에서 시작하는 경로이므로 calc의 기저율 경고로 확인해야 한다. [C:revenue_growth@FY2025] [F166] [F215]

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

- 앤더슨 case={"from": "bull", "years": 10, "revenue_growth": [0.4, 0.33, 0.28, 0.24, 0.2, 0.17, 0.15, 0.13, 0.12, 0.1], "fcf_margin": 0.13, "exit_multiple": 25, "share_change": 0.0}: 
- 슬레이터 case={"from": "base", "fcf_margin": 0.08, "exit_multiple": 20}: 
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
| S45 | call | 2026-08-05 | [MercadoLibre (MELI) Q2 2026 earnings summary - Quartr](https://quartr.com/events/mercadolibre-inc-meli-q2-2026_3ePJ0gcZ) | 2026년 2분기 어닝콜 요약 페이지. 검색 결과에서 링크만 확인했고 본문은 읽지 못했다. 원문 트랜스크립트가 아니며 사실 근거로 쓰지 않았다. |
| S46 | news | 2026-08-05 | [MercadoLibre Inc. Reports Second Quarter 2026 Financial Results - Business Wire](https://businesswire.com/news/home/20260805925866/en/MercadoLibre-Inc.-Reports-Second-Quarter-2026-Financial-Results) | 2분기 실적 보도자료(S4 8-K 첨부와 같은 내용). 검색 요약으로 확인한 수치: 순매출 및 금융수익 101.69억 달러(전년 대비 +50%, 환율 중립 +43%), 영업이익 6.83억 달러(-17%, 영업이익률 6.7%), 순이익 4.66억 달러, 조정 FCF 2.14억 달러(1~2분기 누적 1.58억 달러), 설비투자 4.41억 달러, 신용 포트폴리오 증가에 21억 달러 투입. 요약을 통해 본 것이고 원문 대조는 하지 못했다. |

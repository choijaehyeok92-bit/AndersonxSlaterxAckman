# Cerebras Systems (CBRS) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 모델** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✗ model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

## 1. Variant perception

- 시장이 반영한 것: 주가는 40배 안팎의 EV/매출로 큰 폭의 장기 성장을 이미 반영한다. 한편 상장 후 고점에서 절반 넘게 빠져 있어, 시장이 RPO의 크기보다 GAAP 마진·SBC·고객 집중을 더 무겁게 본다는 신호도 있다. FY2027 컨센서스는 찾지 못해, 시장이 2027년에 얼마를 깔았는지는 모른다.
- 우리가 다르게 보는 점: RPO 254.0억 USD는 실제 숫자이지만 인식 시점과 마진은 공개되지 않았다. 우리는 매출 성장 경로를 경영진 목표보다 낮게 잡고, 가치의 대부분은 클라우드 전환 후 GAAP 마진이 core 마진 쪽으로 수렴하는지에 달렸다고 본다. 이 마진 수렴은 아직 데이터로 입증되지 않았으므로 약세 시나리오 확률을 낮지 않게 둔다.
- 왜 우리가 맞는가: GAAP 매출총이익은 1분기에서 2분기로 줄었고, 3분기 core 마진 가이던스(38~40%)도 2분기 core(41%)보다 낮다. 경영진의 2027년 60%대 목표는 현재 궤적과 반대 방향이다. 따라서 마진 개선이 확인되기 전에는 높은 성장 가정을 기본 시나리오에 넣지 않는다. [F40] [F50] [F51] [F57] [F52] [F60] [C:ev_revenue]
- 촉매: 3분기 실적에서 GAAP과 core 매출총이익률의 차이가 좁아지는지, RPO의 인식 비율과 신규 고객 비중이 공개되는지.
- 시점: FY2026Q3 실적 발표(2026년 11월 전후)와 FY2027 가이던스 발표

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 분석 모듈 (L4)

### 사업·산업 — unclear

Cerebras는 웨이퍼 스케일 AI 가속기 시스템(CS-4)을 판매하고, 자체 데이터센터에서 추론 클라우드 서비스를 운영한다. 지금은 하드웨어 판매 중심에서 클라우드 용량 중심으로 옮겨 가는 중이다. 매출은 FY2024 2.9억 달러에서 FY2025 5.1억 달러로 성장했고(C:revenue_growth@FY2025 75.7%), 계약 잔량(RPO)은 254.0억 달러, 계약된 데이터센터 용량은 600MW다. 단위경제는 입증되지 않았다. 고객당 CAC·이탈률·코호트 자료가 없고, GAAP 매출총이익률(14%)과 회사가 쓰는 core 기준(41%)의 차이도 설명되지 않았다. 상위 2개 고객(UAE 연계 법인)이 매출의 86%를 차지하고, 해자는 대부분 회사 발표에 근거한다.

- [unit_economics] 2분기 core 매출총이익률은 41%이고 GAAP 매출총이익률은 14%다. 두 기준의 차이 요인은 확인되지 않았다. 3분기 core 가이던스는 38~40%로 2분기보다 낮다. 경영진은 2027년에 60%대 이상을 목표로 한다고 하지만, 이는 회사 발언일 뿐 입증된 수치가 아니다. [F50] [F51] [F57] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- [unit_economics] GAAP 매출총이익은 1분기 8,618만 달러에서 2분기 2,556만 달러로 줄었다. 같은 기간 GAAP 매출은 1.9억에서 1.8억 달러로 거의 정체였다. 2분기 GAAP 매출 1.8억 달러는 컨센서스 1.94억 달러를 밑돌았고, 하드웨어 부진이 원인으로 보도됐다. [F17] [F18] [F32] [F33] [F58] [S30](https://www.newsquawk.com/headlines/cerebras-cbrs-q2-2026-usd-revenue-1801mln-exp-194mln)
- [customers] FY2025 매출의 86%가 UAE 연계 두 법인(G42·MBZUAI)에서 나왔다. 이 수치는 S-1에 대한 2차 보도에서 가져왔고 원문 대조는 되지 않았다. 신규 고객 사례로 Gimlet Labs 공급과 AMD와의 분리형 추론 협업이 있다. 이들은 규모와 조건이 공개되지 않아 집중도 완화를 입증하지 못한다. [F48] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm) [S16](https://news.google.com/rss/articles/CBMirgFBVV95cUxOMDgtbmhLenNVQVdOQXJDbmJmck52THdJR3BYWV8zeXdjRFdieFdIdUNlTTNreWNWSy1obHdabzhtakNsQldBeGF6Y0RwLTQ0ZVRzZy11UkFycEx6azI0dWM1enN5NkdHTEg3N1VhajVFZEFqMmlKblo3Y2Zmam1wUTNLS3ZNYTd2b2MxdWNVQzJtdklpVV92WS1wZllQVGVBak9mUEdkeldoWFZRWFE?oc=5) [S18](https://news.google.com/rss/articles/CBMiywFBVV95cUxQSGxfRjlGZUZfR1hack0zbEdZcVJXY1JCaWw4dl9fMFZnQnJHVnVfU3NsZkpVd2hPbjh5Q0dHTVcxYTByelU2b3lMUzVDNk54ZFN4OG1VSko2MXEzV0d3bDdHSTJiRHlrMFZtallYSllLUzdSQ2lVdDVra2ZqY0xPaEV2cmxRaXRIWnhRd19obk82eFBGQXQ1YnpYc2hLY0poOGVsdS1yZ19mVGs0RlFVZ1diV0luRktiNV9Uc05vSHpEbmViQ1NjX1h1UQ?oc=5)
- [runway] RPO는 254.0억 달러로, FY2025 매출 5.1억 달러와 비교하면 매출 대비 수십 배에 이른다. 이는 장기 계약이 크다는 신호다. 다만 인식 시기와 고객 구성이 없어 실제 매출로 바뀌는 속도를 판단할 수 없다. 이 백로그의 마진 구조도 보도에서 질문으로만 제기된다. [F52] [F42] [S24](https://news.google.com/rss/articles/CBMikgFBVV95cUxOalM0ejc1WHVWb29zVVZRdEFSVm5aeWhSUDVLVjlUZDAyc1Y2LWhfa1RTTVNXYVM2ZzRSY0Q3cW1pdDN2Q21FeWYybUNwLWRtMl9reTVyb1RDSDdCTmxBRXlselNHTUtfdTY4eG15WDVWQzJxRWxOVlNQdFo1WkRwMkZwQmRKQkotR0xaYlRZc1l1Zw?oc=5)
- [industry] 회사는 2026년 core 매출 가이던스를 8.8~8.9억 달러로 상향했다(기존 8.55~8.65억 달러). 이는 컨센서스 약 8.634억 달러 위다. 보도는 실적 직후 주가가 하락했다고 전한다. 시장이 매출보다 마진과 GAAP 품질을 더 따지고 있다는 의미일 수 있다. [F54] [F55] [F60] [S9](https://news.google.com/rss/articles/CBMingFBVV95cUxPS3RxTUJxMTh2Mk9XSmgxdm1MZDh6MlRtcVl5aFM1bmF1ajVmWlFnUF9nNU0yYjloQ0pON2VSWFZBYTVldmJ0TGI5N2psYlcwZVRuSURZaUM1NkYzVkh4NGVNRUtjd0F0M3RMTno2X0RSNG9VbF91V2lDOUh0OG5nSDJiY2M4cDdrM1lGRnNicldnNXBBQTBDRFVzNHdJQQ?oc=5) [S20](https://news.google.com/rss/articles/CBMif0FVX3lxTFBJcHVySkhhUXc0UTFTUU44MC1zazJYSFpyMVRkdy1MUG5QSDBOX1dkVmstdi1VWVBZTm91U2ZXYzhXZmlzUlAzT2NNdExXMVZ6eWdyQkQ0eFA0UzU3amczTzYxQkthMTRWOXJGRjZ0bzQyT2F6b1pGbFMwN1hHcTDSAYQBQVVfeXFMTlk2ekExUzkydDVRQ1E3elduc0F5c08tUklVMFJBazUyS1lEZml4alVXSTdxYWpSdVdiVEFuVnMtVnFSTnNOWjZsaldlUlFyMnBEU0pWbkFJektITkdWSnItZS05aFBfRm94X1ZOV1J0Y3FIdXBUdklRLWZJSktrekxYRG8x?oc=5)
- [unit_economics] 2분기 영업손실은 4.8억 달러이고 SBC는 3.8억 달러다. 영업이익률은 FY2025 -28.6%였다. 2분기 손실의 상당 부분이 IPO 연계 주식보상으로 보이지만 확인되지 않았다. 따라서 현금 기준 단위경제와 GAAP 기준을 구분해서 봐야 한다. [F27] [F37] [C:operating_margin@FY2025]
- [runway] IPO 이후 현금은 17.2억 달러에서 67.4억 달러로 늘었고 자기자본은 -1.9억 달러에서 91.5억 달러로 바뀌었다. 재투자 활주로는 자금 면에서는 충분하다. 자본이 어느 정도의 수익률로 쓰일지는 단위경제가 입증되지 않아 판단할 수 없다. 1분기 capex는 1.3억 달러였다. [F2] [F3] [F15] [F16] [F1]
- [claimed] 웨이퍼 스케일 칩과 CS-4의 추론 속도 우위는 회사의 제품 발표와 Hot Chips 발표에 근거한다. 점유율, 재계약, 경쟁사 대비 마진 같은 독립 수치는 확인되지 않았다. GAAP 매출총이익률 14%는 가격 결정력이 입증되지 않았다는 쪽에 가깝다. [S8](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBmMUQxb0dVSUo2UzM1MVE2dExHRlRYUlg2QW1GSktqeTd0WmVldXpKaVFIVUxaWVpwQ0RpQlpnYjBUZWJ4ZmZBWHowMzlRQkdPV0E3VzE3VkxfdjJtUmNBNFE1dFI?oc=5) [S15](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNjNfbnRoZFloVUFkdDZxWUppbzg1ejVBcTIxVGVxQXZOS0hNZFdPVi02UFVGdU1oR0NPWjBrelZnUnY2bHFDSm1hdDl2a0JDNnBWNV9YQ2ZyT21nOWt6TTdFZjZNMm4tMVUzX3lYQy1QMzMwbmNuSmFZalQycjNZQlhFSTRfa2RYeHVFUnFXSGs0aGRMNGVSOGRR?oc=5) [F51]
- [claimed] 600MW 용량과 RPO 254.0억 달러는 규모 우위의 후보다. 다만 RPO의 인식 시기, 고객 구성, 해지 조건은 확인되지 않았다. 규모가 원가 우위로 이어졌다는 흔적도 없다. 현금은 67.4억 달러지만 총이익은 오히려 줄었다. [F53] [F52] [F3] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- [claimed] 전환비용이나 네트워크 효과를 보여 주는 증거(이탈률, 순매출유지율, 가격 인상 후 잔존)가 수집되지 않았다. NVIDIA·AMD 대비 경쟁 위치도 교차 확인하지 못했다. [S10](https://news.google.com/rss/articles/CBMingFBVV95cUxQNk5ZWDcya0pXamNfMGIybGhZNGQ4U05LX21iUFVZeDhKd3gtUlR5dWFjXzNSd3FZc1JUQlJCX0NoSWpmNEpWdkZ5UjBQcjZ3dEFxMWF2NF85XzBibThSLXNPeE54SlpwX0FwM1FrQktNT1ZoaU10V3NWb2J1aWNyamlpbTdaTHV5bHRueWpJcFQtNFBxQWNaY01rR19qUQ?oc=5)

### 경영진·자본배분 — mixed

경영진의 보상 구조, 내부자 매매, 락업, 과거 가이던스 적중률은 근거가 없어 정렬 여부를 직접 판단할 수 없다. 확인되는 것은 세 가지다. 첫째, 2분기 SBC가 3.8억 USD로 1분기 959만 USD에서 급증했고 희석 주식 수는 6,281만에서 1.5억으로 늘었다. IPO 전후 변화로 보이지만 IPO 연계 성격은 근거로 확인하지 못했다. 둘째, 2026년 core 매출 가이던스를 8.6억 USD에서 8.85억 USD로 올렸지만, 같은 분기 GAAP 매출 1.8억 USD는 컨센서스 1.94억 USD를 밑돌았다. 셋째, 2분기 말 현금이 67.4억 USD로 늘었지만 자본배분 이력(인수, 자사주, 상환)은 확인되지 않는다. 가이던스가 신뢰할 만한지는 상장 후 콜이 두 번뿐이라 아직 검증되지 않았다. 증거로 정렬 또는 비정렬을 판정할 수 없어 mixed로 둔다.

- [compensation] 근거 없음. DEF 14A와 보상 연동 지표, 베스팅 기간은 수집되지 않았다. 보상이 장기 가치 지표에 연동되는지 단기 EPS·조정 EBITDA에 연동되는지 판단할 수 없다. 다만 2분기 SBC는 3.8억 USD로 1분기 959만 USD의 큰 배수이고, 경영진이 강조하는 core 지표와 GAAP 지표의 차이도 크다(core 매출총이익률 41%, GAAP 14%). 이 차이의 조정 내역은 확인되지 않았다. [F36] [F37] [F50] [F51]
- [insider] 근거 없음. 창업자·경영진 지분, 내부자 매수·매도, 락업 해제 일정은 찾지 못했다. 5월 IPO 이후 락업 해제가 주가에 부담이 되는지 여부는 이 근거로 판단할 수 없다. [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- [guidance] 2026년 core 매출 가이던스를 8.6억 USD(범위 8.55억~8.65억)에서 8.85억 USD(범위 8.8억~8.9억)로 상향했다. 상향 전 컨센서스 8.634억 USD보다 높다. 3분기 core 매출 가이던스는 2.15억 USD(범위 2.14억~2.16억)로, 컨센서스 2.119억 USD보다 약간 높고 core 매출총이익률은 0.39(0.38~0.4)로 제시했다. 반면 2분기 GAAP 매출 1.8억 USD는 컨센서스 1.94억 USD를 하회했고 GAAP 매출총이익률은 기대에 크게 못 미쳤다고 보도되었다. 가이던스 적중률(C:guidance_hit_rate)은 계산되지 않았다. 상장 후 콜이 1분기와 2분기 두 번뿐이라 이력이 부족하다. 2027년 목표(매출 3배 이상, core 매출총이익률 60%대 이상)는 정량 범위 없는 경영진 발언이다. [F54] [F55] [F56] [F57] [F58] [F59] [F60] [F33] [F51] [S9](https://news.google.com/rss/articles/CBMingFBVV95cUxPS3RxTUJxMTh2Mk9XSmgxdm1MZDh6MlRtcVl5aFM1bmF1ajVmWlFnUF9nNU0yYjloQ0pON2VSWFZBYTVldmJ0TGI5N2psYlcwZVRuSURZaUM1NkYzVkh4NGVNRUtjd0F0M3RMTno2X0RSNG9VbF91V2lDOUh0OG5nSDJiY2M4cDdrM1lGRnNicldnNXBBQTBDRFVzNHdJQQ?oc=5) [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [S30](https://www.newsquawk.com/headlines/cerebras-cbrs-q2-2026-usd-revenue-1801mln-exp-194mln)
- [dilution] 희석 주식 수가 FY2026Q1 6,281만에서 FY2026Q2 1.5억으로 늘었다. 2분기 가중 평균에 IPO 이전 구간이 섞여 있어 기말 수치와 다르다. 발행주식수는 약 2.196억(S28)과 1.51억(2026-09-18)으로 출처가 엇갈려 현재 희석 규모를 확정할 수 없다. 2분기 SBC는 3.8억 USD로 1분기 959만 USD에서 급증했으나 IPO 연계 일회성인지 지속적인 보상 비용인지는 확인되지 않았다. 자사주 매입 근거는 없다. 따라서 희석을 상쇄하는지 가리는지는 판단할 수 없다. [F13] [F14] [F36] [F37] [F41] [S28](https://www.fool.com/quote/NASDAQ/CBRS)
- [capital_allocation] IPO 전후로 현금이 FY2026Q1 17.2억 USD에서 FY2026Q2 67.4억 USD로, 자본총계가 -1.9억 USD에서 91.5억 USD로 바뀌었다. 같은 기간 차입금은 3.6억 USD에서 1.8억 USD로 줄었으나 유동 부채(debt_current)는 6.2억 USD에서 7.4억 USD로 늘었다. 상환에 쓴 금액과 용도는 확인되지 않는다. 1분기 capex는 1.3억 USD이고 연간 capex는 없다. 계약된 데이터센터 용량은 600MW이며 잔여 이행 의무(RPO)는 254.0억 USD다. 이 대규모 투자의 수익률과 M&A·자사주 이력은 근거가 없다. [F1] [F2] [F3] [F7] [F8] [F9] [F10] [F15] [F16] [F52] [F53]
- [capital_allocation] 고객 집중이 매우 높다. FY2025 상위 2개 고객(UAE 연계 두 법인)이 매출의 0.86을 차지한다. 이는 S-1에 대한 2차 보도에서 가져왔고 원문 대조 전이다. 특수관계 여부와 계약 조건은 확인되지 않았다. 경영진이 이 집중을 어떻게 관리하는지, 거래가 주주 이익에 맞는지 판단하려면 S-1 원문 확인이 필요하다. [F48] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)

### 회계 품질 — watch

코드 신호는 하나도 켜지지 않았다. 다만 신호가 없다는 것이 회계가 깨끗하다는 증거는 못 된다. 연간 현금흐름·희석 추이·TTM을 계산할 사실이 없어서 대부분의 신호가 계산 불가였기 때문이다. 직접 확인한 사실로는 조정해서 봐야 할 숫자가 여럿 있다. (1) 2분기 SBC가 3.8억 USD로 순손실 4.5억 USD의 대부분이다. IPO와 연계된 일회성 성격일 가능성이 높지만 10-Q 원문으로 확인하지 못했다. (2) 회사가 내세우는 'core' 매출(2.1억)이 GAAP 매출(1.8억)보다 크고, 총이익률도 core 41% 대 GAAP 14%로 벌어진다. 조정 내역을 읽지 못했으므로 core 지표는 입증된 숫자가 아니라 회사 주장으로만 취급해야 한다. (3) 2분기에 매출은 1분기보다 줄었는데 매출채권은 약 두 배가 됐다. (4) 2025년 매출의 86%가 UAE 연계 두 법인(G42·MBZUAI)에 몰려 있는데, 특수관계 여부와 거래 조건을 확인하지 못했다. (5) FY2025 GAAP 순이익이 보도마다 달라(일회성 비현금 이익 언급 포함) 어느 값도 쓸 수 없다. 감사의견, 정정, 감사인 변경을 확인할 원문이 없어 clean은 줄 수 없다. 반대로 숫자를 믿을 수 없다는 직접 증거도 없으므로 red_flag도 아니다. 판정은 watch다. GAAP 기준 숫자만 쓰고, SBC를 비용으로 차감하고, core 지표와 2027 목표는 검증 전 가정으로 다뤄야 한다.

- [watch] 2분기 core 매출(2.1억 USD)이 GAAP 매출(1.8억 USD)보다 크다. 총이익률도 core 41% 대 GAAP 14%로 차이가 크다. core는 GAAP에서 어떤 항목을 더하고 빼는지 조정 내역을 읽지 못했다. 가이던스(FY2026 core 매출, 3분기 core 총이익률)도 모두 core 기준이라, 회사가 말하는 지표와 GAAP 실적이 서로 다른 잣대일 수 있다. 판단에는 GAAP을 기준으로 삼고, core는 조정 내역이 확인되기 전까지 보조 지표로만 쓴다. [F49] [F33] [F50] [F51] [F54] [F57]
- [watch] 2분기 SBC가 3.8억 USD로, 같은 분기 순손실 4.5억 USD와 영업손실 4.8억 USD의 대부분을 차지한다. 1분기 SBC는 959만 USD였다. IPO(2026-05) 시점에 베스팅 조건이 충족되며 한꺼번에 인식된 비용일 가능성이 높지만 확인하지 못했다. 반복되는 비용인지, 일회성인지에 따라 이익 추정이 크게 달라진다. 앞으로 분기에도 이 수준이면 SBC 차감 후 현금흐름으로 봐야 한다. [F36] [F37] [F24] [F27]
- [watch] 1분기에서 2분기로 넘어가며 매출은 1.9억에서 1.8억 USD로 줄었는데 매출채권은 6,263만에서 1.2억 USD로 늘었다. 재고는 8,904만에서 3,267만 USD로 줄었고 이연매출은 1.5억에서 1.7억 USD로 늘었다. 하드웨어 납품 시점의 변화나 고객 집중에 따른 대금 회수 지연일 수 있다. 분기 두 점뿐이라 코드 신호가 계산되지 않았다. 다음 10-Q에서 매출채권 회수와 연령을 확인해야 한다. [F30] [F31] [F32] [F33] [F21] [F22] [F11] [F12]
- [watch] FY2025 매출의 86%가 UAE 연계 두 법인(G42·MBZUAI)에서 나왔다고 보도됐다. 이 둘이 회사의 주주나 이사회 관계자와 연결된 특수관계인지, 거래 조건이 시장 조건인지, 대금 회수가 정상인지는 S-1 원문을 읽지 못해 확인하지 못했다. 집중도 자체는 매출의 질 문제이고, 특수관계라면 회계 문제가 된다. 이 수치는 S-1에 대한 2차 보도 기준이다. [F48] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- [watch] FY2025 GAAP 순이익이 보도마다 다르다(흑자로 보도되었고, 3.6억 USD대 일회성 비현금 이익이 언급됨). FY2024 순손실도 보도마다 엇갈린다. 그래서 사실에는 non-GAAP 순손실 -7,570만 USD와 영업손실 -1.5억 USD만 담겼다. 영업손실과 순이익의 방향이 다르다면 영업 외 평가이익이 이익을 부풀렸다는 뜻이다. 연간 GAAP 순이익으로 영업현금흐름 대비나 발생액 비율을 계산하면 안 된다. [F44] [F45] [F46] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm)
- [info] IPO로 자본구조가 바뀌어 연속성이 끊겼다. 자기자본은 1분기 -1.9억에서 2분기 91.5억 USD로, 현금은 17.2억에서 67.4억 USD로, 총자산은 49.5억에서 116.3억 USD로 늘었다. 가중 희석주식수는 6,281만에서 1.5억 주로 늘었는데, 이는 IPO 이전 구간이 섞인 값이라 연평균 희석률 신호로 쓸 수 없다. 분기 간 재무 비율은 IPO 전후를 구분해서 읽어야 한다. [F15] [F16] [F2] [F3] [F38] [F39] [F13] [F14]
- [info] 차입금 사실이 서로 어긋나 있다. 2분기 장기 debt는 1.8억 USD인데 단기성 debt_current가 7.4억 USD다. 같은 항목의 분류 차이인지 별도 항목인지 확인하지 못했다. 순현금 계산에 영향을 주므로 10-Q 대차대조표로 재확인이 필요하다. [F8] [F10] [F7] [F9]
- [watch] 감사의견, 감사인, 핵심감사사항, 계속기업 문구, IPO 전후 정정 여부는 S-1·10-Q 원문을 읽지 못해 확인하지 못했다. 연간 현금흐름 사실(FY2025 영업현금흐름·자본적 지출)도 없어 현금 전환도 검증하지 못했다. 1분기에는 순손실 -1,401만 USD에도 영업현금흐름이 +1,234만 USD였고, 2분기 영업현금흐름 사실은 없다. 이 공백 때문에 clean이 아닌 watch로 둔다. 원문에서 정정이나 계속기업 의문이 나오면 red_flag로 올려야 한다. [S1](https://www.sec.gov/Archives/edgar/data/2021728/000162828026056357/cbrs-20260630.htm) [S3](https://www.sec.gov/Archives/edgar/data/2021728/000162828026044981/cbrs-20260331.htm) [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm) [F23] [F25]

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 고객 집중이 풀리지 않고 RPO가 매출로 전환되지 않는다. FY2025 매출의 86%를 UAE 연계 두 법인이 차지했고, 신규 고객(Gimlet Labs, AMD 협업)은 규모와 조건이 공개되지 않았다. 254.0억 달러 RPO는 인식 시기·고객 구성·해지 조건이 불명이라 소수 고객의 계약 축소나 지연, 지정학·수출 규제 변화만으로 상당 부분이 사라질 수 있다. 백로그가 줄면 40배 EV/매출을 지탱하는 성장 서사가 무너지고 배수가 한 자릿수로 압축된다. [F48] [F52] [S6](https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm) [S16](https://news.google.com/rss/articles/CBMirgFBVV95cUxOMDgtbmhLenNVQVdOQXJDbmJmck52THdJR3BYWV8zeXdjRFdieFdIdUNlTTNreWNWSy1obHdabzhtakNsQldBeGF6Y0RwLTQ0ZVRzZy11UkFycEx6azI0dWM1enN5NkdHTEg3N1VhajVFZEFqMmlKblo3Y2Zmam1wUTNLS3ZNYTd2b2MxdWNVQzJtdklpVV92WS1wZllQVGVBak9mUEdkeldoWFZRWFE?oc=5) [S18](https://news.google.com/rss/articles/CBMiywFBVV95cUxQSGxfRjlGZUZfR1hack0zbEdZcVJXY1JCaWw4dl9fMFZnQnJHVnVfU3NsZkpVd2hPbjh5Q0dHTVcxYTByelU2b3lMUzVDNk54ZFN4OG1VSko2MXEzV0d3bDdHSTJiRHlrMFZtallYSllLUzdSQ2lVdDVra2ZqY0xPaEV2cmxRaXRIWnhRd19obk82eFBGQXQ1YnpYc2hLY0poOGVsdS1yZ19mVGs0RlFVZ1diV0luRktiNV9Uc05vSHpEbmViQ1NjX1h1UQ?oc=5) [S24](https://news.google.com/rss/articles/CBMikgFBVV95cUxOalM0ejc1WHVWb29zVVZRdEFSVm5aeWhSUDVLVjlUZDAyc1Y2LWhfa1RTTVNXYVM2ZzRSY0Q3cW1pdDN2Q21FeWYybUNwLWRtMl9reTVyb1RDSDdCTmxBRXlselNHTUtfdTY4eG15WDVWQzJxRWxOVlNQdFo1WkRwMkZwQmRKQkotR0xaYlRZc1l1Zw?oc=5)
- (20%) 클라우드 전환 후에도 GAAP 마진이 core 마진으로 수렴하지 않는다. 2분기 GAAP 매출총이익률은 14%, core는 41%로 차이가 크고 두 기준의 조정 내역은 확인되지 않았다. 3분기 core 가이던스(38~40%)도 2분기보다 낮다. 600MW 데이터센터 투자는 감가상각과 전력·임대 고정비를 먼저 키우므로 가동률이 늦어지면 총이익이 줄고 현금이 소모된다. 2027년 60%대 마진 목표가 입증되지 않은 채 시장이 GAAP 기준으로 재평가하면 배수와 이익이 함께 내려간다. [F50] [F51] [F57] [F17] [F18] [F53] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX)
- (15%) 추론 시장에서 NVIDIA·AMD와의 경쟁으로 속도 우위가 가격 결정력으로 이어지지 않는다. 속도 우위는 회사 발표와 Hot Chips 발표에 근거할 뿐 점유율·재계약·이탈률 같은 독립 수치가 없다. 경쟁사가 추론 가속기와 소프트웨어를 개선하면 가격 경쟁이 시작되고, 2분기 GAAP 매출이 컨센서스를 밑돌고 매출이 정체한 하드웨어 부문이 먼저 압박받는다. 매출 성장이 둔화되면 SBC와 투자 부담이 그대로 남아 주당 가치가 희석된다. [S8](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBmMUQxb0dVSUo2UzM1MVE2dExHRlRYUlg2QW1GSktqeTd0WmVldXpKaVFIVUxaWVpwQ0RpQlpnYjBUZWJ4ZmZBWHowMzlRQkdPV0E3VzE3VkxfdjJtUmNBNFE1dFI?oc=5) [S15](https://news.google.com/rss/articles/CBMimgFBVV95cUxQNjNfbnRoZFloVUFkdDZxWUppbzg1ejVBcTIxVGVxQXZOS0hNZFdPVi02UFVGdU1oR0NPWjBrelZnUnY2bHFDSm1hdDl2a0JDNnBWNV9YQ2ZyT21nOWt6TTdFZjZNMm4tMVUzX3lYQy1QMzMwbmNuSmFZalQycjNZQlhFSTRfa2RYeHVFUnFXSGs0aGRMNGVSOGRR?oc=5) [S30](https://www.newsquawk.com/headlines/cerebras-cbrs-q2-2026-usd-revenue-1801mln-exp-194mln) [F32] [F33] [F58] [S10](https://news.google.com/rss/articles/CBMingFBVV95cUxQNk5ZWDcya0pXamNfMGIybGhZNGQ4U05LX21iUFVZeDhKd3gtUlR5dWFjXzNSd3FZc1JUQlJCX0NoSWpmNEpWdkZ5UjBQcjZ3dEFxMWF2NF85XzBibThSLXNPeE54SlpwX0FwM1FrQktNT1ZoaU10V3NWb2J1aWNyamlpbTdaTHV5bHRueWpJcFQtNFBxQWNaY01rR19qUQ?oc=5)
- (15%) 회계 품질과 희석 문제가 늦게 드러난다. core 지표 조정 내역, 특수관계 여부, SBC 3.8억 달러의 성격, 감사 관련 사항은 원문을 읽지 못해 확인되지 않았다. 2분기에 매출은 줄었는데 매출채권은 약 두 배가 됐고, 주식 수도 출처마다 1.51억~2.196억으로 엇갈린다. 락업 해제로 공급이 늘고 SBC가 반복 비용으로 판명되면, 주당 가치가 희석되고 FCF가 SBC 차감 후 음수로 남아 신뢰가 훼손된다. 매출채권 회수가 지연되면 고객 집중 문제와 겹쳐 충격이 커진다. [F31] [F30] [F37] [F36] [F14] [F41] [S28](https://www.fool.com/quote/NASDAQ/CBRS) [F48]
- 약한 가정 `base.fcf_margin`: 기본 시나리오는 모델 끝에서 FCF 마진 12%를 가정하지만 FCF 수익률·연간 현금흐름 사실이 전혀 없어 출발점이 없다. 2분기 GAAP 매출총이익률이 14%이고 3분기 core 마진 가이던스도 2분기보다 낮은데, 600MW 투자로 capex가 커지는 구간에서 마진이 오른다는 증거가 없다. 마진 수렴은 경영진의 2027년 목표에 의존한다. [F51] [F57] [F53] [S29](https://quartr.com/events/cerebras-systems-inc-cbrs-q2-2026_FTEZH3AX) [C:operating_margin@FY2025]
- 약한 가정 `base.revenue_growth`: 기본 시나리오의 FY2027 성장 80%는 RPO가 일부 인식된다는 가정에 기대지만, RPO의 인식 시기와 고객 구성이 공개되지 않았다. FY2027 컨센서스도 없어 이 가정이 시장 대비 어디에 있는지 검증할 수 없다. 2분기 GAAP 매출이 1분기 대비 정체한 점과도 맞지 않는다. [F52] [F32] [F33] [C:revenue_growth@FY2025]
- 약한 가정 `base.exit_multiple`: 기본 시나리오의 22배 배수는 5년 뒤 성장이 25%로 둔화한 시점에 적용된다. 현재 EV/매출은 40.51배이고 상장 후 고점에서 절반 넘게 빠진 상태라, 배수 압축 폭이 어느 정도인지에 따라 수익률이 크게 달라진다. 이 배수를 뒷받침하는 기저율 자료가 인용되지 않았다. [C:ev_revenue] [F40] [S27](https://weissratings.com/en/instant-news-alerts/cerebras-systems-inc-cbrs-down-4-8-time-to-cash-out)

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
| 주가 (price) | 175.44 USD/share (2026-10-13, F40) |
| 희석 주식 수 (shares) | 1.5억 |
| 시가총액 (market_cap) | 264.9억 USD |
| 순현금 (net_cash) | 58.2억 USD |
| EV (ev) | 206.6억 USD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 40.51x |
| PER (pe) | — |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull", "fcf_margin": 0.25, "exit_multiple": 30, "years": 10}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "bear"}: price=175.4, leveraged=아니오

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

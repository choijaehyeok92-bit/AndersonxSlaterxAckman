# AppLovin (APP) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 모델** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✗ model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

## 1. Variant perception

- 시장이 반영한 것: 주가는 52주 범위 상단 735.50 USD에서 크게 내려온 297.82 USD 근처다(S41). 보도는 2분기 매출 미달, 3분기 마진 가이던스 하락, 점유율 정체 우려, 소송 위험을 이유로 든다(S19, S37, S22, S23). 이는 성장 둔화가 구조적이고 규제 위험이 커졌다는 가정을 가격에 반영한 것으로 읽힌다. 다만 연간 매출 컨센서스와 현재 주가를 찾지 못해 시장 내재 성장은 코드의 역DCF(C:implied_cagr)로 확인해야 하며, 컨센서스 대비 차이는 검증하지 못했다.
- 우리가 다르게 보는 점: 둔화의 원인이 수요·경쟁 상실이 아니라 핵심 게임 광고 모델 개선의 시차라고 본다. 따라서 성장은 완만히 낮아질 뿐 붕괴하지 않고, 현금 창출력도 크게 훼손되지 않는다. 여기에 이커머스·소비자 광고는 가격에 거의 반영되지 않은 선택권이다. 다만 기본 시나리오는 이 선택권에 매출을 거의 배정하지 않는다.
- 왜 우리가 맞는가: 경영진은 개선분이 분기 종료 직후 반영됐다고 했고(S40, 보도), 3분기 가이던스 중간값은 컨센서스보다 약 0.6% 낮은 정도다. 매출 20.55억~20.85억 USD(F207)와 조정 EBITDA 17.1억~17.4억 USD(F209) 가이던스는 성장 지속을 전제한다. 재무적으로는 현금 30.5억 USD(F23)와 낮은 레버리지(C:net_debt_to_ebitda@FY2025)가 소송·규제 충격의 완충이 된다. 이 설명이 틀리면 3분기 실적에서 가이던스 하단 미달로 바로 드러난다. [S35](https://news.google.com/rss/articles/CBMiowFBVV95cUxOM2Yzd0xFZVFEZUluTC1lV3l5ZVl2UXBmZlJnbVpPakJocm40Ym90cnFtZWxWc3hTakdfWENmQ3p2Yk44YWktVWJCaGVOY19ud3ptcm84UWIyMW9vSjdJUXNaRnlGM2VPdW9JX1EwTGpQY3RhRVY3emJRaXlad0pTQnJmdUx4ZVdsNlZEcnc2SkR5LXVoQ2gtTERod0JPc0FxM19z?oc=5) [S40](https://ppc.land/applovin-revenue-growth-slows-to-53-as-q3-margin-guidance-drops-to-83/) [S41](https://www.coingecko.com/en/stocks/applovin) [F207] [F209] [F23] [C:net_debt_to_ebitda@FY2025]
- 촉매: 2026년 3분기 실적 발표(S35)에서 매출·조정 EBITDA가 가이던스 범위 안에 들어오는지와 4분기 가이던스. Unity 분쟁과 샌디에이고 소송의 전개.
- 시점: 2026년 3분기 실적 발표 직후부터 2026년 4분기 가이던스까지

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 주가 기준일 2026-09-01이 as_of(2026-10-18)보다 47일 오래됨
- ⚠ 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 분석 모듈 (L4)

### 사업·산업 — proven

AppLovin은 모바일 앱 개발자(광고 수요 측)와 광고 지면 보유자(공급 측)를 연결하는 광고 소프트웨어·플랫폼 사업자로, 광고 거래 수수료로 매출을 올린다. 매출은 FY2025 54.8억 USD(C:revenue_growth@FY2025 +70.0%)이고 2026년 2분기 19.2억 USD(전년 동기 +53%, S39)로 성장세가 둔화 중이다. 총이익률은 87.9%, 영업이익률은 75.8%(C:gross_margin@FY2025, C:operating_margin@FY2025)로 소프트웨어 중에서도 매우 높다. 다만 고마진의 원인이 해자인지 알고리즘 개선에 따른 일시적 효율인지는 공시만으로 입증되지 않는다. 3분기 가이던스 마진은 약 83%로 낮아졌고(S39), 경영진은 핵심 게임 광고의 모델 개선 지연을 이유로 들었다(S40, 보도). 이커머스·소비자 광고 확장은 아직 초기이며 지표가 없고, Unity와의 분쟁·아동 대상 광고 소송 등 규제·법적 위험이 새로 나왔다(S22, S23, 보도).

- [unit_economics] 매출총이익률이 FY2022 55.4%에서 FY2025 87.9%로, 영업이익률은 -1.7%에서 75.8%로 올랐다. 이 개선은 사업 믹스 변화(소프트웨어 플랫폼 중심으로의 전환, 2023년 매출이 18.4억 USD로 줄어든 뒤 급증)와 함께 나타났다. 분기 매출원가는 FY2025Q1 1.5억에서 FY2026Q2 2.3억 USD로 늘었지만 매출은 11.6억에서 19.2억 USD로 더 빨리 늘었다. [C:gross_margin@FY2022] [C:gross_margin@FY2025] [C:operating_margin@FY2025] [F29] [F33] [F155] [F159]
- [unit_economics] 성장과 마진 모두 둔화 신호가 있다. 2분기 매출 성장률은 +53%로 FY2025의 +70.0%보다 낮고(S39, C:revenue_growth@FY2025), 3분기 조정 EBITDA 마진 가이던스는 약 83%로 2분기 약 84%(조정 EBITDA 16.14억 ÷ 매출 19.24억)에서 소폭 낮아졌다. 3분기 가이던스 중간값은 컨센서스보다 약 0.6% 낮았다(S40, 보도). 단위경제가 악화라고 단정할 CAC·이탈률 근거는 없다. [S39](https://www.businesswire.com/news/home/20260805303503/en/AppLovin-Announces-Second-Quarter-2026-Financial-Results/) [S40](https://ppc.land/applovin-revenue-growth-slows-to-53-as-q3-margin-guidance-drops-to-83/) [C:revenue_growth@FY2025] [F207] [F209]
- [unit_economics] 이익의 현금 전환이 강하다. FY2025 영업현금흐름 39.7억 USD가 순이익 33.3억 USD를 넘고, FY2024 FCF 마진은 65.0%였다. 발생액 비율은 -9.7%로 이익이 현금으로 뒷받침된다. 다만 매출채권은 FY2024 12.8억에서 FY2026Q2 21.7억 USD로 늘어 DSO가 121일(FY2025)이고, 매출보다 채권이 더 빠르게 늘어나는지는 추가 확인이 필요하다. [F117] [F107] [C:fcf_margin@FY2024] [C:accruals_ratio@FY2025] [C:dso@FY2025] [F143] [F149]
- [industry] 모바일 앱 광고 시장은 대형 플랫폼(애플·구글의 개인정보 정책)과 경쟁 광고 네트워크·Unity에 둘러싸인 구조다. 공급자(앱 지면·OS 사업자)의 협상력이 크고 광고주는 성과 지표에 민감하다. 최근 Unity와의 데이터 수집 분쟁과 법원의 신청 기각 보도는 경쟁사와의 법적 충돌이 상시 위험임을 보여준다. 산업 구조에 관한 정량 자료(점유율)는 수집분에 없다. [S22](https://news.google.com/rss/articles/CBMisAFBVV95cUxPLWx3ZnVkdWdoaGt0a0VoT0t6MldvR2J3d0JKQnVIRjVabEQxUlRxM0FZbmxGMkxFc1lIN1BxUnZzSW9TVmd0Z25NaTd5ZHF4bHFrY1JOSGI2UmZFd2o5OVFmbXh5QUJOUTdtWTM4WFAyUXFUdFVtUlZJYk1EOTJKX0hFdGs0eGRUblZsSERYeE0ycFN3RklfY3lNX045ZldORXRjaEVaNlhHQlhPSHRjTQ?oc=5) [S28](https://news.google.com/rss/articles/CBMiugFBVV95cUxObTFNZGkzS0Y4ZzRPYnlTYjhsWnZnSGZUMV9Qc1diOEFncFdyRnRibWlHcVh0MHFfbGMwWHU2UEx6YkJ3ME53QmhDbC1qdkV5NjlqUGNsRWdHQkRYNUNrRzhBS0RDaGFmQ3l2Q3FweHNTYWl2c1VnVXRQdWtncDloaE1WQUNGZlMxWUpJY2tfdkRjNzJDMTdTbjRXSkpBM2sybjR0V2w1Q3FPU2ZheENUU05xbERDbXprblE?oc=5) [S37](https://news.google.com/rss/articles/CBMioAFBVV95cUxOM1FXVzlpXzYzZnowbmhLVWZ5UVlTanJyRjFxQ2ZUWUllei1ULVhfY1FaQ3V4NmFMVjBfYkIxSndvOW5Lelo1MXFMYk5NSkZYR0hpQ2F4MDB5NmFNb2JaSTFPOWlVU0U3b3VreTFWOEpvV3BIVWhnTEgxY080X1h2Yi13bDZOd2Yzb3VwNGNXZkJVbk53OG03Nkd4SmJwTXZC?oc=5)
- [customers] 고객·광고주 수, 이탈률, 순매출유지율, 이커머스·소비자 광고 비중은 수집분에 없다. 따라서 '고객 1명당 경제성'은 매출총이익률과 현금 전환에서 간접 추정만 가능하며, 코호트 근거가 없다. 경영진은 이커머스·소비자 광고 확장에 인내를 요청했다(S20, 보도). [S20](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdGhPUFJZM1lTb2NkRUc2TjI4UGlTYU1GWGw2WWNIdlBxaDFKLUtkVE1LUXNPcGw3TU1YZkRxMzdWSi1qRjVFWkFWME9mTnVaS2NHVDhXVk9rTXFmSFgyYjk1cnZ5RVhudExSTFVsWnN1X3pvdTdUejFCMHc1alJLNHQwSzF1Q3l0OWdQY1BLaDNJWEdQWlBxQTd5OEc5b2QtOG5ESXZ5UFVJODgya3J1endtcVBTMW0w?oc=5)
- [runway] 재투자 활주로는 이커머스·소비자 광고로의 확장에 달려 있다고 회사는 설명한다(S20, 보도). 자본 배분은 이미 자사주 매입에 크게 쓰였다(FY2025 21.9억, FY2026Q1 9.8억 USD). 희석 주식 수는 FY2022 3.7억에서 FY2025 3.4억으로 줄었다. 자사주 매입이 커진다는 것은 내부 재투자 수요가 한정적일 수 있다는 신호이기도 하나, 단정할 근거는 없다. [F5] [F7] [F64] [F67] [S20](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdGhPUFJZM1lTb2NkRUc2TjI4UGlTYU1GWGw2WWNIdlBxaDFKLUtkVE1LUXNPcGw3TU1YZkRxMzdWSi1qRjVFWkFWME9mTnVaS2NHVDhXVk9rTXFmSFgyYjk1cnZ5RVhudExSTFVsWnN1X3pvdTdUejFCMHc1alJLNHQwSzF1Q3l0OWdQY1BLaDNJWEdQWlBxQTd5OEc5b2QtOG5ESXZ5UFVJODgya3J1endtcVBTMW0w?oc=5)
- [industry] 규제·법적 위험이 새로 나왔다. 샌디에이고 시가 아동 기기에 선정적 광고가 노출됐다며 소송을 냈고(S23, 보도), Unity와는 데이터 수집 분쟁이 있다(S22, 보도). 두 건 모두 1차 공시 근거가 없어 규모와 영향은 알 수 없다. 광고 노출 통제와 데이터 수집 방식이 사업 모델의 핵심이어서 결과에 따라 지면 접근이나 타기팅 방식이 제한될 수 있다. [S22](https://news.google.com/rss/articles/CBMisAFBVV95cUxPLWx3ZnVkdWdoaGt0a0VoT0t6MldvR2J3d0JKQnVIRjVabEQxUlRxM0FZbmxGMkxFc1lIN1BxUnZzSW9TVmd0Z25NaTd5ZHF4bHFrY1JOSGI2UmZFd2o5OVFmbXh5QUJOUTdtWTM4WFAyUXFUdFVtUlZJYk1EOTJKX0hFdGs0eGRUblZsSERYeE0ycFN3RklfY3lNX045ZldORXRjaEVaNlhHQlhPSHRjTQ?oc=5) [S23](https://news.google.com/rss/articles/CBMitAFBVV95cUxNcmw3WEF0UDdzdnEtLXhlTVkySXkxVFJDUHByUzdDRUc4RTNOOTdncWg3OE5pSTQ2RXZYdVM1QldjN2E2RjJpZDhZdjFWS3pQSW4xLVlvYm1ORVpSbTZrV1VZWGhUNzJRSTFDQ2VPM2FzUDJkenFvYWR0ckVhNGVsTTdKS0JndDdjZDFmUDRBaHFndFlrRVVfMGdpb0JQWWx3Nlk3Q1Bfak9SVFBRZEpUb1pDRHQ?oc=5) [S28](https://news.google.com/rss/articles/CBMiugFBVV95cUxObTFNZGkzS0Y4ZzRPYnlTYjhsWnZnSGZUMV9Qc1diOEFncFdyRnRibWlHcVh0MHFfbGMwWHU2UEx6YkJ3ME53QmhDbC1qdkV5NjlqUGNsRWdHQkRYNUNrRzhBS0RDaGFmQ3l2Q3FweHNTYWl2c1VnVXRQdWtncDloaE1WQUNGZlMxWUpJY2tfdkRjNzJDMTdTbjRXSkpBM2sybjR0V2w1Q3FPU2ZheENUU05xbERDbXprblE?oc=5)
- [unit_economics] 재무구조는 이익에 비해 부담이 작다. 총부채는 약 35.2억 USD로 거의 일정하고 현금은 FY2026Q2 30.5억 USD까지 늘어 순부채/EBITDA는 FY2025 0.24x다. 사업이 갑자기 꺾여도 단기 생존 위험은 낮지만, 이는 단위경제의 질이 아니라 재무 여력을 보여주는 지표다. [C:net_debt_to_ebitda@FY2025] [F50] [F23]
- [claimed] 방대한 앱 지면·데이터에 기반한 광고 매칭 알고리즘의 규모 우위를 시사하는 흔적은 마진 추이(총이익률 64.6%→87.9%)다. 그러나 점유율·광고주 이탈률·가격 인상 후 잔존 기록 같은 직접 증거는 수집분에 없고, 한 애널리스트는 시장 점유율 성장이 정체됐다고 지적한다(S37, 보도). [C:gross_margin@FY2021] [C:gross_margin@FY2025] [S37](https://news.google.com/rss/articles/CBMioAFBVV95cUxOM1FXVzlpXzYzZnowbmhLVWZ5UVlTanJyRjFxQ2ZUWUllei1ULVhfY1FaQ3V4NmFMVjBfYkIxSndvOW5Lelo1MXFMYk5NSkZYR0hpQ2F4MDB5NmFNb2JaSTFPOWlVU0U3b3VreTFWOEpvV3BIVWhnTEgxY080X1h2Yi13bDZOd2Yzb3VwNGNXZkJVbk53OG03Nkd4SmJwTXZC?oc=5)
- [claimed] 광고주·개발자가 플랫폼에 연동해 쓰는 구조라 전환비용이 있을 수 있으나, 순매출유지율·고객 이탈 자료가 없어 입증되지 않는다. Unity와의 데이터 수집 분쟁은 이 지면·데이터 접근 자체가 도전받을 수 있음을 보여준다(S22, 보도). [S22](https://news.google.com/rss/articles/CBMisAFBVV95cUxPLWx3ZnVkdWdoaGt0a0VoT0t6MldvR2J3d0JKQnVIRjVabEQxUlRxM0FZbmxGMkxFc1lIN1BxUnZzSW9TVmd0Z25NaTd5ZHF4bHFrY1JOSGI2UmZFd2o5OVFmbXh5QUJOUTdtWTM4WFAyUXFUdFVtUlZJYk1EOTJKX0hFdGs0eGRUblZsSERYeE0ycFN3RklfY3lNX045ZldORXRjaEVaNlhHQlhPSHRjTQ?oc=5) [S28](https://news.google.com/rss/articles/CBMiugFBVV95cUxObTFNZGkzS0Y4ZzRPYnlTYjhsWnZnSGZUMV9Qc1diOEFncFdyRnRibWlHcVh0MHFfbGMwWHU2UEx6YkJ3ME53QmhDbC1qdkV5NjlqUGNsRWdHQkRYNUNrRzhBS0RDaGFmQ3l2Q3FweHNTYWl2c1VnVXRQdWtncDloaE1WQUNGZlMxWUpJY2tfdkRjNzJDMTdTbjRXSkpBM2sybjR0V2w1Q3FPU2ZheENUU05xbERDbXprblE?oc=5)
- [claimed] 이커머스·소비자 광고 영역은 해자 흔적이 아직 없다. 경영진이 인내를 요청한 단계다(S20, 보도). [S20](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdGhPUFJZM1lTb2NkRUc2TjI4UGlTYU1GWGw2WWNIdlBxaDFKLUtkVE1LUXNPcGw3TU1YZkRxMzdWSi1qRjVFWkFWME9mTnVaS2NHVDhXVk9rTXFmSFgyYjk1cnZ5RVhudExSTFVsWnN1X3pvdTdUejFCMHc1alJLNHQwSzF1Q3l0OWdQY1BLaDNJWEdQWlBxQTd5OEc5b2QtOG5ESXZ5UFVJODgya3J1endtcVBTMW0w?oc=5)

### 경영진·자본배분 — mixed

경영진의 정렬을 판단할 핵심 근거가 비어 있다. 보상 구조(DEF 14A 본문), 내부자 매매, 과거 가이던스 적중률은 수집분에 없다. 확인되는 것은 자본배분과 희석 관리다. 매년 대규모 자사주 매입으로 희석 주식 수를 줄여 왔고(FY2023~FY2025 연속 감소), SBC 부담도 매출 대비 3.8%까지 내려왔다. 부채는 35.1억 USD 수준에서 움직이지 않고 순부채/EBITDA는 0.24x로 낮다. 신뢰도 쪽에서는 2026년 2분기 매출이 시장 기대에 못 미쳤고 경영진이 스스로 기준에 못 미쳤다고 인정했다. 3분기 가이던스도 컨센서스를 소폭 밑돌았다. 근거가 부족해 '혼재'로 둔다.

- [compensation] 근거 없음. 2026-04-21 DEF 14A가 근거 목록에는 있으나 보상 연동 지표(장기 지표인지 단기 EPS·조정 EBITDA인지)와 베스팅 기간은 수집분에 들어 있지 않다. 정렬 여부를 판단할 수 없다. [S6](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000028/app-20260420.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도 자료가 수집분에 없다. 2026-04-07 8-K에 경영진 변동이 언급되어 있으나 내용은 확인되지 않았다. [S7](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000014/app-20260402.htm)
- [guidance] 과거 분기 가이던스(FY2025Q1~FY2026Q2)가 수집분에 없어 적중률을 계산할 수 없다. 확인되는 것은 최근 한 건이다. 2026년 2분기 실적 발표에서 3분기 가이던스(매출 20.55억~20.85억 USD, 조정 EBITDA 17.1억~17.4억 USD)가 컨센서스보다 약 0.6% 낮았다. 보도에 따르면 경영진은 핵심 게임 광고 부문의 모델 개선이 늦어진 것을 원인으로 들었다. 수요·경쟁 탓은 아니라고 했고, 개선분은 분기 종료 직후 반영됐다고 한다. 이 설명이 맞는지는 3분기 실적으로 확인할 수 있다. [F207] [F209] [S39](https://www.businesswire.com/news/home/20260805303503/en/AppLovin-Announces-Second-Quarter-2026-Financial-Results/) [S40](https://ppc.land/applovin-revenue-growth-slows-to-53-as-q3-margin-guidance-drops-to-83/)
- [guidance] 2026년 2분기 매출은 19.2억 USD(전년 동기 대비 +53%)로 성장률이 둔화했다. 언론은 매출 미달로 보도했고 WSJ은 경영진이 결과가 자신들의 기준에 못 미쳤다고 말했다고 전했다. 미달을 숨기지 않고 인정한 점은 신뢰도에 긍정적이다. 다만 미달 자체는 기대 관리의 실패이기도 하다. [F159] [S19](https://news.google.com/rss/articles/CBMie0FVX3lxTE9YYnFMSHpkWG9fcE1ZYXlSOVIzQmxoZVJFUGVhSnFYUl80eVVtU1gyTkpOZmdEM3NfbTAwME1hcWtiUWFzeEEyVkJQT3BydmJSY3hOT0tWM29pcko3TFVaV1NlZVdMd3B2QTVPdHNkb0xFSGN5czRVeVc3TdIBgAFBVV95cUxOb1hGNGZKQ0ttcUNuOTd2ODJYQ2hWNUhGNzdlUXhObUVlSmhNX3BRcXA2cWFmODNzMDJnZVBFTkRRRDNqM3BFRWRVOG50TWZ6QXNaeEdvTmRHTE5zZ0wtZTJTdnhrbWQ2dHpSMTFvSHcxVnRpNV84TnBYb1ZCenBZcg?oc=5) [S26](https://news.google.com/rss/articles/CBMitAFBVV95cUxPZFBPWW4zc3licGd0c1gxa2dqS1A2bFYyMTRvMTllczIyTWRrRVRURE1MV2l2dVhxU0tnZ1hhQ0ItRi1rcmpNSV9JWWdXaFdjY0daQ0ViS2Z5RlpGa2daS1FEMDU4TFVhMDlpcS1IQ3hVLW9RS3RUUXJCTkVTal9Wd3dEMlFEUW81RFZsNVRNSzd5a1BIOTA5SG40bjJOSXFSMHJiM1F0MnE2N283ZjJFZm80YXg?oc=5) [S39](https://www.businesswire.com/news/home/20260805303503/en/AppLovin-Announces-Second-Quarter-2026-Financial-Results/)
- [dilution] 희석 주식 수는 FY2022 이후 줄었다. 주식 수 변화는 FY2023 -2.4%, FY2024 -4.1%, FY2025 -1.7%이고 FY2026Q2 희석 주식 수는 약 3.4억 주다. SBC는 FY2025 2.1억 USD로 매출의 3.8%(FY2023 19.7%, FY2024 11.5%)까지 내려왔다. 다만 분기 SBC는 FY2025Q3 3,377만에서 FY2026Q2 8,578만 USD로 다시 늘었다. 감소 추세가 이어지는지는 지켜봐야 한다. [C:share_change@FY2023] [C:share_change@FY2024] [C:share_change@FY2025] [C:sbc_to_revenue@FY2023] [C:sbc_to_revenue@FY2024] [C:sbc_to_revenue@FY2025] [F72] [F174] [F177] [F179]
- [capital_allocation] 자사주 매입은 FY2022 3.4억, FY2023 11.5억, FY2024 9.8억, FY2025 21.9억 USD이고 FY2026Q1에만 9.8억 USD다. 같은 기간 희석 주식 수가 줄었으므로 SBC 희석을 단순히 가리는 수준을 넘어 실제 주식 수를 줄이는 쪽이다. 다만 매입 평균가를 알 수 없고, 52주 범위(297.82~735.50 USD)가 넓어 고점 매입 여부는 판단할 수 없다. FY2025 영업현금흐름은 39.7억 USD였다. [F2] [F3] [F4] [F5] [F7] [F117] [S41](https://www.coingecko.com/en/stocks/applovin)
- [capital_allocation] 차입은 FY2024 이후 35.1억 USD로 사실상 변함이 없고 FY2026Q2에 35.2억 USD다. 현금은 FY2024 7.0억에서 FY2026Q2 30.5억 USD로 늘었고, 순부채/EBITDA는 FY2023 2.08x에서 FY2025 0.24x로 내려왔다. 부채를 갚기보다 만기까지 유지하면서 현금을 쌓고 자사주를 사는 구조다. 재무 레버리지 위험은 낮아졌다. [F44] [F50] [F17] [F23] [C:net_debt_to_ebitda@FY2023] [C:net_debt_to_ebitda@FY2025]
- [capital_allocation] M&A 이력은 영업권 추이로만 간접 확인된다. 영업권이 FY2021 9.7억에서 FY2022 18.2억 USD로 크게 늘었다가 FY2023 15.0억, FY2026Q2 15.2억 USD로 줄거나 유지됐다. 개별 인수의 가격과 수익률은 근거가 없어 판단하지 않는다. 최근에는 이커머스·소비자 광고로의 확장을 말하고 있으나(회사 설명), 투자 규모와 목표 수익률을 확인하지 못했다. [F83] [F84] [F85] [F92] [S20](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdGhPUFJZM1lTb2NkRUc2TjI4UGlTYU1GWGw2WWNIdlBxaDFKLUtkVE1LUXNPcGw3TU1YZkRxMzdWSi1qRjVFWkFWME9mTnVaS2NHVDhXVk9rTXFmSFgyYjk1cnZ5RVhudExSTFVsWnN1X3pvdTdUejFCMHc1alJLNHQwSzF1Q3l0OWdQY1BLaDNJWEdQWlBxQTd5OEc5b2QtOG5ESXZ5UFVJODgya3J1endtcVBTMW0w?oc=5)

### 회계 품질 — watch

코드 신호는 하나도 걸리지 않았고, 현금흐름은 이익의 질을 뒷받침한다. FY2025 영업현금흐름 39.7억 USD가 순이익 33.3억 USD보다 크고, 발생액 비율은 -9.7%로 음수다. SBC는 매출의 3.8%에 불과하고 희석 주식 수는 줄고 있다. 다만 두 가지는 조정해서 봐야 한다. 첫째, 매출채권이 크다(DSO 121.2일). 이는 퍼블리셔 지급분을 뺀 순액으로 매출을 잡는 구조와 맞물린 것으로 보이지만, 수집분에서는 확인하지 못했다. 둘째, 수집한 이력은 사업 매각 전후의 재작성 기준이 섞여 있는 것으로 보인다. 그래서 FY2023 매출 -34.6%나 FY2024Q4 파생값(매출보다 큰 영업이익, 음수 매출원가)은 회계 문제가 아니라 비교 불가능한 숫자로 읽어야 한다. 감사의견, 정정, 감사인 변경, Non-GAAP 조정, 특수관계자 거래는 10-K 본문에서 확인하지 못했다. 이 항목들은 미확인이며 문제로 확인된 것은 아니다. red_flag 근거는 없다.

- [watch] DSO가 121.2일로 길고 매출채권이 분기 매출보다 크다(FY2026Q2 매출채권 21.7억 USD, 매출 19.2억 USD). 매출채권 증가율은 매출 증가율보다 낮아 부풀림 신호는 아니다. 매출채권이 퍼블리셔 지급 전 총액이고 매출은 순액이라는 구조 설명은 추정이며, 수집분에서 확인하지 못했다. 매출 인식 정책과 매출채권 연령 분석을 10-K에서 확인해야 한다. [C:dso@FY2025] [F149] [F159] [F147] [F143]
- [watch] FY2023 이전과 이후 수치의 기준이 달라 보인다. FY2023 매출이 FY2022보다 크게 줄어든 것(-34.6%)은 사업 구성 변화(재작성)일 가능성이 크다. FY2024Q4 파생값은 영업이익이 매출보다 크고 매출원가가 음수여서 연간(재작성)과 분기(원 기준) 값을 섞은 산물로 보인다. 추세 분석은 FY2024 이후 값 중심으로 해야 하고, 성장률 기저율 계산에 FY2023 이전을 쓰면 왜곡된다. [C:revenue_growth@FY2023] [F193] [F195] [F190]
- [info] 조정 EBITDA 16.1억 USD는 같은 분기 영업이익 14.9억 USD보다 크다. 차이는 감가상각과 SBC 등 조정 항목이다. 조정 내역은 수집분에 없으므로 조정 항목이 반복되는지는 확인하지 못했다. SBC는 매출 대비 낮은 수준이다. [F208] [F129] [F179] [C:sbc_to_revenue@FY2025]
- [info] 감사의견, 핵심감사사항, 계속기업 의문, 감사인 변경, 재무제표 정정 여부를 확인하지 못했다. 코드가 8-K 4.02/4.01 신호를 내지 않았으므로 수집된 공시 목록에는 해당 사항이 없다. 다만 10-K 본문은 읽지 못했다. [S8](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000010/app-20251231.htm)
- [watch] Unity와의 데이터 수집 분쟁과 샌디에이고 시의 아동 대상 광고 소송이 보도되었으나 1차 공시 근거가 없다. 우발채무 주석(충당 여부)을 확인하기 전에는 회계 신뢰성이 아니라 규제·소송 위험으로 분류한다. [S22](https://news.google.com/rss/articles/CBMisAFBVV95cUxPLWx3ZnVkdWdoaGt0a0VoT0t6MldvR2J3d0JKQnVIRjVabEQxUlRxM0FZbmxGMkxFc1lIN1BxUnZzSW9TVmd0Z25NaTd5ZHF4bHFrY1JOSGI2UmZFd2o5OVFmbXh5QUJOUTdtWTM4WFAyUXFUdFVtUlZJYk1EOTJKX0hFdGs0eGRUblZsSERYeE0ycFN3RklfY3lNX045ZldORXRjaEVaNlhHQlhPSHRjTQ?oc=5) [S23](https://news.google.com/rss/articles/CBMitAFBVV95cUxNcmw3WEF0UDdzdnEtLXhlTVkySXkxVFJDUHByUzdDRUc4RTNOOTdncWg3OE5pSTQ2RXZYdVM1QldjN2E2RjJpZDhZdjFWS3pQSW4xLVlvYm1ORVpSbTZrV1VZWGhUNzJRSTFDQ2VPM2FzUDJkenFvYWR0ckVhNGVsTTdKS0JndDdjZDFmUDRBaHFndFlrRVVfMGdpb0JQWWx3Nlk3Q1Bfak9SVFBRZEpUb1pDRHQ?oc=5)
- [info] 이익의 질을 뒷받침하는 신호가 여럿 있다. FY2025 영업현금흐름(39.7억 USD)이 순이익(33.3억 USD)을 웃돌고, 발생액 비율은 음수이며, SBC/영업현금흐름은 5.3%로 낮다. 희석 주식 수는 줄고 있어(-1.7%) 현금 이익이 SBC로 상쇄되지 않는다. 자사주 매입은 FY2025에 21.9억 USD였다. [F117] [F107] [C:accruals_ratio@FY2025] [C:sbc_to_ocf@FY2025] [C:share_change@FY2025] [F5]

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 핵심 게임 광고의 점유율이 구조적으로 정체된다. 모델 개선 지연을 '일시적 시차'로 설명했지만, 실제로는 경쟁 네트워크와 Unity 같은 경쟁사가 따라붙고 광고주가 예산을 분산한 결과였다. 성장률이 FY2025 +70.0%에서 2분기 +53%로 이미 꺾였고, 시장은 성장주 배수를 성숙 광고기술 배수로 재평가한다. 이익은 줄지 않아도 배수 압축만으로 주가가 크게 내려간다. 현재 가격은 둔화가 가속되지 않는다는 가정을 깔고 있다. [S37](https://news.google.com/rss/articles/CBMioAFBVV95cUxOM1FXVzlpXzYzZnowbmhLVWZ5UVlTanJyRjFxQ2ZUWUllei1ULVhfY1FaQ3V4NmFMVjBfYkIxSndvOW5Lelo1MXFMYk5NSkZYR0hpQ2F4MDB5NmFNb2JaSTFPOWlVU0U3b3VreTFWOEpvV3BIVWhnTEgxY080X1h2Yi13bDZOd2Yzb3VwNGNXZkJVbk53OG03Nkd4SmJwTXZC?oc=5) [S39](https://www.businesswire.com/news/home/20260805303503/en/AppLovin-Announces-Second-Quarter-2026-Financial-Results/) [S40](https://ppc.land/applovin-revenue-growth-slows-to-53-as-q3-margin-guidance-drops-to-83/) [C:revenue_growth@FY2025]
- (20%) 마진 압박이 구조화된다. 3분기 조정 EBITDA 마진 가이던스가 이미 낮아졌고, 지면 공급자와 광고주가 수수료 인하를 요구한다. 여기에 규제·소송 대응 비용이 더해지면 최고 수준의 마진이 평균 회귀한다. 현재 영업이익률 75.8%는 알고리즘 효율의 일시적 우위일 수 있어서, 마진이 몇 %p만 내려가도 이익은 매출 성장 둔화와 겹쳐 크게 줄어든다. 해자가 회사 발표만으로 지지되는 상태라 완충이 없다. [S39](https://www.businesswire.com/news/home/20260805303503/en/AppLovin-Announces-Second-Quarter-2026-Financial-Results/) [F209] [C:operating_margin@FY2025] [C:gross_margin@FY2025]
- (15%) 법적·규제 충격이 지면과 데이터 접근을 직접 제한한다. 아동 대상 선정 광고 소송과 Unity와의 데이터 수집 분쟁이 선례가 되어 다른 지자체·경쟁사·규제기관의 추가 제소로 번지고, 타기팅 방식과 지면 접근이 제한된다. 사업 모델의 핵심이 데이터 수집과 광고 노출 통제여서 판결 한 건이 매출 구조에 영향을 준다. 1차 공시 근거가 없어 시장도 규모를 모른다. 우발채무와 합의금, 광고주 이탈이 한꺼번에 나타나면 이익과 배수가 함께 무너진다. [S22](https://news.google.com/rss/articles/CBMisAFBVV95cUxPLWx3ZnVkdWdoaGt0a0VoT0t6MldvR2J3d0JKQnVIRjVabEQxUlRxM0FZbmxGMkxFc1lIN1BxUnZzSW9TVmd0Z25NaTd5ZHF4bHFrY1JOSGI2UmZFd2o5OVFmbXh5QUJOUTdtWTM4WFAyUXFUdFVtUlZJYk1EOTJKX0hFdGs0eGRUblZsSERYeE0ycFN3RklfY3lNX045ZldORXRjaEVaNlhHQlhPSHRjTQ?oc=5) [S23](https://news.google.com/rss/articles/CBMitAFBVV95cUxNcmw3WEF0UDdzdnEtLXhlTVkySXkxVFJDUHByUzdDRUc4RTNOOTdncWg3OE5pSTQ2RXZYdVM1QldjN2E2RjJpZDhZdjFWS3pQSW4xLVlvYm1ORVpSbTZrV1VZWGhUNzJRSTFDQ2VPM2FzUDJkenFvYWR0ckVhNGVsTTdKS0JndDdjZDFmUDRBaHFndFlrRVVfMGdpb0JQWWx3Nlk3Q1Bfak9SVFBRZEpUb1pDRHQ?oc=5) [S28](https://news.google.com/rss/articles/CBMiugFBVV95cUxObTFNZGkzS0Y4ZzRPYnlTYjhsWnZnSGZUMV9Qc1diOEFncFdyRnRibWlHcVh0MHFfbGMwWHU2UEx6YkJ3ME53QmhDbC1qdkV5NjlqUGNsRWdHQkRYNUNrRzhBS0RDaGFmQ3l2Q3FweHNTYWl2c1VnVXRQdWtncDloaE1WQUNGZlMxWUpJY2tfdkRjNzJDMTdTbjRXSkpBM2sybjR0V2w1Q3FPU2ZheENUU05xbERDbXprblE?oc=5)
- (10%) 이커머스·소비자 광고 확장이 실패하고 자본배분이 흔들린다. 경영진이 인내를 요청한 확장은 해자 흔적이 없는 영역이어서 막대한 투자가 수익을 못 낸다. 그 사이 자사주 매입은 고점에서 대규모로 이뤄져 가치를 파괴했다. 총부채가 35.2억 USD로 줄지 않은 채 성장이 꺾이면 순현금 개선이 멈추고 매입 여력도 사라진다. 시장이 믿던 성장 선택권이 사라지고, 성장도 자본환원도 없는 회사가 된다. [S20](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdGhPUFJZM1lTb2NkRUc2TjI4UGlTYU1GWGw2WWNIdlBxaDFKLUtkVE1LUXNPcGw3TU1YZkRxMzdWSi1qRjVFWkFWME9mTnVaS2NHVDhXVk9rTXFmSFgyYjk1cnZ5RVhudExSTFVsWnN1X3pvdTdUejFCMHc1alJLNHQwSzF1Q3l0OWdQY1BLaDNJWEdQWlBxQTd5OEc5b2QtOG5ESXZ5UFVJODgya3J1endtcVBTMW0w?oc=5) [F5] [F7] [F50] [F23]
- 약한 가정 `base.revenue_growth`: 기본 시나리오의 첫해 성장률은 FY2026 가이던스 경로를 이어받고 이후 완만히 둔화한다고 둔다. 그러나 기저율은 고성장이 5년 내내 유지되는 경우가 드물다는 점을 보여주고, 성장률은 이미 FY2025에서 2분기로 둔화했다. 점유율 정체 보도(S37)까지 있어 둔화 속도가 가정보다 빠를 가능성을 과소평가했다. [C:base_rate@base] [C:revenue_growth@FY2025] [S37](https://news.google.com/rss/articles/CBMioAFBVV95cUxOM1FXVzlpXzYzZnowbmhLVWZ5UVlTanJyRjFxQ2ZUWUllei1ULVhfY1FaQ3V4NmFMVjBfYkIxSndvOW5Lelo1MXFMYk5NSkZYR0hpQ2F4MDB5NmFNb2JaSTFPOWlVU0U3b3VreTFWOEpvV3BIVWhnTEgxY080X1h2Yi13bDZOd2Yzb3VwNGNXZkJVbk53OG03Nkd4SmJwTXZC?oc=5)
- 약한 가정 `base.fcf_margin`: FCF 마진 62%는 FY2024의 65.0%에서 소폭만 내린 값이다. 반면 3분기 마진 가이던스는 이미 낮아졌고, 규제·소송 비용과 수수료 압박은 반영하지 않았다. 해자가 회사 발표만으로 지지되는 상태에서 최고 수준의 마진이 유지된다는 가정은 평균 회귀에 가장 취약하다. 마진이 낮아지면 FCF 감소율이 매출 감소율보다 크다. [C:fcf_margin@FY2024] [F209] [C:operating_margin@FY2025]
- 약한 가정 `base.exit_multiple`: 종료 배수 18은 현재 PER 23.85배와 약세 시나리오 배수 사이의 값이다. 성장이 한 자릿수로 내려오는 5년 차에도 이런 배수가 유지되는지에 대한 근거가 없다. 역DCF로 시장 내재 성장을 확인하지 못했고(주가가 낡았다), 컨센서스도 없어서 배수 가정을 검증할 수단이 없다. [C:pe] [C:base_rate@base]

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| 매출 (revenue) | 27.9억 USD | 28.2억 USD | 18.4억 USD | 32.2억 USD | 54.8억 USD |
| 매출 성장 (revenue_growth) | — | 0.9% | -34.6% | 75.1% | 70.0% |
| 총이익률 (gross_margin) | 64.6% | 55.4% | 80.6% | 83.9% | 87.9% |
| 영업이익률 (operating_margin) | 5.4% | -1.7% | 41.9% | 59.3% | 75.8% |
| 순이익 (net_income) | 3,545만 USD | -1.9억 USD | 3.6억 USD | 15.8억 USD | 33.3억 USD |
| 영업현금흐름 (ocf) | 3.6억 USD | 4.1억 USD | 10.6억 USD | 21.0억 USD | 39.7억 USD |
| 설비투자 (capex) | 139만 USD | 66만 USD | 425만 USD | 478만 USD | — |
| FCF (fcf) | 3.6억 USD | 4.1억 USD | 10.6억 USD | 20.9억 USD | — |
| FCF 마진 (fcf_margin) | 12.9% | 14.6% | 57.4% | 65.0% | — |
| FCF/순이익 (fcf_conversion) | 10.17x | — | 2.96x | 1.33x | — |
| SBC (sbc) | 1.3억 USD | 1.9억 USD | 3.6억 USD | 3.7억 USD | 2.1억 USD |
| SBC/매출 (sbc_to_revenue) | 4.8% | 6.8% | 19.7% | 11.5% | 3.8% |
| SBC/영업현금흐름 (sbc_to_ocf) | 36.8% | 46.4% | 34.2% | 17.6% | 5.3% |
| SBC 차감 FCF (fcf_after_sbc) | 2.3억 USD | 2.2억 USD | 6.9억 USD | 17.2억 USD | — |
| ROIC (roic) | 3.0% | -1.1% | 18.2% | 48.3% | 114.1% |
| 순현금 (net_cash) | -17.1억 USD | -21.3억 USD | -26.2억 USD | -28.1억 USD | -10.3억 USD |
| 순부채/EBITDA (net_debt_to_ebitda) | 2.94x | 4.27x | 2.08x | 1.19x | 0.24x |
| 희석 주식 수 (diluted_shares) | 3.4억 | 3.7억 | 3.6억 | 3.5억 | 3.4억 |
| 주식 수 변화 (share_change) | — | 8.4% | -2.4% | -4.1% | -1.7% |
| DSO(일) (dso) | 67.2 | 91.1 | 189.0 | 145.3 | 121.2 |
| 발생액 비율 (accruals_ratio) | — | -10.1% | -12.6% | -9.2% | -9.7% |

표에 없는 키도 인용할 수 있다: buybacks, capitalized_software, capitalized_to_revenue, cash, cash_total, cost_of_revenue, d_and_a, debt, debt_current, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, goodwill, goodwill_to_assets, gross_profit, income_tax, operating_income, pretax_income, receivables, receivables_growth, rnd, total_assets

### 시장 · TTM(FY2026Q2) 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 312.06 USD/share (2026-09-01, F206) |
| 희석 주식 수 (shares) | 3.4억 |
| 시가총액 (market_cap) | 1,051.7억 USD |
| 순현금 (net_cash) | -4.6억 USD |
| EV (ev) | 1,056.4억 USD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 15.47x |
| PER (pe) | 23.85x |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- 신호 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull", "years": 10}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "base"}: price=312.1, leveraged=아니오

### 계산 경고

- 주가 기준일 2026-09-01이 as_of(2026-10-18)보다 47일 오래됨
- 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-08-05 | [10-Q](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000059/app-20260630.htm) |  |
| S2 | filing | 2026-08-05 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000057/app-20260805.htm) |  |
| S3 | filing | 2026-06-05 | [8-K](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000050/app-20260603.htm) |  |
| S4 | filing | 2026-05-06 | [10-Q](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000044/app-20260331.htm) |  |
| S5 | filing | 2026-05-06 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000042/app-20260506.htm) |  |
| S6 | filing | 2026-04-21 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000028/app-20260420.htm) |  |
| S7 | filing | 2026-04-07 | [8-K 경영진 변동 IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000014/app-20260402.htm) |  |
| S8 | filing | 2026-02-19 | [10-K](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000010/app-20251231.htm) |  |
| S9 | filing | 2026-02-11 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1751008/000175100826000005/app-20260211.htm) |  |
| S10 | filing | 2025-11-05 | [10-Q](https://www.sec.gov/Archives/edgar/data/1751008/000175100825000081/app-20250930.htm) |  |
| S11 | filing | 2025-11-05 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1751008/000175100825000079/app-20251105.htm) |  |
| S12 | filing | 2024-02-26 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1751008/000175100824000012/0001751008-24-000012-index.htm) |  |
| S13 | filing | 2025-02-27 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1751008/000175100825000018/0001751008-25-000018-index.htm) |  |
| S14 | filing | 2023-02-28 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1751008/000175100823000006/0001751008-23-000006-index.htm) |  |
| S15 | filing | 2025-05-07 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1751008/000175100825000053/0001751008-25-000053-index.htm) |  |
| S16 | filing | 2025-08-06 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1751008/000175100825000072/0001751008-25-000072-index.htm) |  |
| S17 | filing | 2022-03-11 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1751008/000175100822000005/0001751008-22-000005-index.htm) |  |
| S18 | news | 2026-09-30 | [AppLovin (APP) Declines More Than Market: Some Information for Investors - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxNSWtYdnpQUk4xTFRJcHB3eFBoX044LUZWS1I2Y19KZ3JfajdwalpnWmk4dGJfM0VUeTR5ZmZJZy02NlRSc3BXWkllLWs4by1tVWxWZFNyYnQxS2gzZm1wemZUWkVrZS1Ca1lJcElSRzNKRzFIams1bHpjSVRyVzZzdV80MHdxWmc1WFljS0xJRzF5LTVKUTcxNnpHbUZvRDQ?oc=5) | Yahoo Finance |
| S19 | news | 2026-08-06 | [AppLovin stock tanks on Q2 revenue miss - CNBC](https://news.google.com/rss/articles/CBMie0FVX3lxTE9YYnFMSHpkWG9fcE1ZYXlSOVIzQmxoZVJFUGVhSnFYUl80eVVtU1gyTkpOZmdEM3NfbTAwME1hcWtiUWFzeEEyVkJQT3BydmJSY3hOT0tWM29pcko3TFVaV1NlZVdMd3B2QTVPdHNkb0xFSGN5czRVeVc3TdIBgAFBVV95cUxOb1hGNGZKQ0ttcUNuOTd2ODJYQ2hWNUhGNzdlUXhObUVlSmhNX3BRcXA2cWFmODNzMDJnZVBFTkRRRDNqM3BFRWRVOG50TWZ6QXNaeEdvTmRHTE5zZ0wtZTJTdnhrbWQ2dHpSMTFvSHcxVnRpNV84TnBYb1ZCenBZcg?oc=5) | CNBC |
| S20 | news | 2026-08-05 | [AppLovin Asks For Patience As It Grows Its Ecommerce And Consumer Ads Business - AdExchanger](https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdGhPUFJZM1lTb2NkRUc2TjI4UGlTYU1GWGw2WWNIdlBxaDFKLUtkVE1LUXNPcGw3TU1YZkRxMzdWSi1qRjVFWkFWME9mTnVaS2NHVDhXVk9rTXFmSFgyYjk1cnZ5RVhudExSTFVsWnN1X3pvdTdUejFCMHc1alJLNHQwSzF1Q3l0OWdQY1BLaDNJWEdQWlBxQTd5OEc5b2QtOG5ESXZ5UFVJODgya3J1endtcVBTMW0w?oc=5) | AdExchanger |
| S21 | news | 2026-10-02 | [AppLovin: The Market Is Likely Wrong (NASDAQ:APP) - Seeking Alpha](https://news.google.com/rss/articles/CBMiggFBVV95cUxNU3ZYNGpYLVI2MWJQNTBVVmNlWU1iMGpycUUwendsNDMwaHcwM3dQb0pXZ05ZcFFENHF2N1gxWGsyTDlWejJpbmdYNGp4U2ZxemJHQ2w5RnFwZU1UcUJoYWNQdlVlaDg0eUhPb1R4eDVuYk9ONGo2dURhSXNOb3Z3X0Fn?oc=5) | Seeking Alpha |
| S22 | news | 2026-09-29 | [Mobile ad giants AppLovin and Unity locked in legal dispute over data collection - Digiday](https://news.google.com/rss/articles/CBMisAFBVV95cUxPLWx3ZnVkdWdoaGt0a0VoT0t6MldvR2J3d0JKQnVIRjVabEQxUlRxM0FZbmxGMkxFc1lIN1BxUnZzSW9TVmd0Z25NaTd5ZHF4bHFrY1JOSGI2UmZFd2o5OVFmbXh5QUJOUTdtWTM4WFAyUXFUdFVtUlZJYk1EOTJKX0hFdGs0eGRUblZsSERYeE0ycFN3RklfY3lNX045ZldORXRjaEVaNlhHQlhPSHRjTQ?oc=5) | Digiday |
| S23 | news | 2026-10-05 | [San Diego Sues AppLovin Over Explicit Ads Shown to Kids’ Devices - Bloomberg.com](https://news.google.com/rss/articles/CBMitAFBVV95cUxNcmw3WEF0UDdzdnEtLXhlTVkySXkxVFJDUHByUzdDRUc4RTNOOTdncWg3OE5pSTQ2RXZYdVM1QldjN2E2RjJpZDhZdjFWS3pQSW4xLVlvYm1ORVpSbTZrV1VZWGhUNzJRSTFDQ2VPM2FzUDJkenFvYWR0ckVhNGVsTTdKS0JndDdjZDFmUDRBaHFndFlrRVVfMGdpb0JQWWx3Nlk3Q1Bfak9SVFBRZEpUb1pDRHQ?oc=5) | Bloomberg.com |
| S24 | news | 2026-10-05 | [History's Warning For AppLovin Stock Dip-Buyers - Trefis](https://news.google.com/rss/articles/CBMitwFBVV95cUxPLV9PeXN1TWdHanY0MVAyWU9IMEw1OHlPQmVLY005R3c4WFRlUFF0bDZscmJILXFHdTZkTmVaeTd5LUNwYmtLNDF5ZllkNTZINE1zdHo2YjdZcTYxT1hPOVpQODlGRmdKQ1l6cUFLbC0waHlwMFRqampMeEJvdnFVZzlxSUtiY0JiM1lJWXk4Ui1qNTRRMG9hV1lQaDJleWYtbXhZUUhoZDBqTWhUd0RxaTllQndvM2M?oc=5) | Trefis |
| S25 | news | 2026-10-02 | [AppLovin Stock Sinks To 52-Week Low - Here's Why - Benzinga](https://news.google.com/rss/articles/CBMinwFBVV95cUxPQkFxWXk3eWNLV05OVnNQeGFJU2VuSmNhTW1hcXpRajJ6b3A3bTZTbWhzQWo5Z0tqcW04TTBtd2xwS0EyYU82RXAtNWtZM3REOHhmaVhIUGF0U2o0VUQwVEJqMHUyc2t3RjFVX1UxdE5uNWFYTEpmNUxvWjIxbU9MVF94clY3ZjEzWlFZd0h1d0U3OXBWdHJFM2RkTUU0b3M?oc=5) | Benzinga |
| S26 | news | 2026-08-05 | [AppLovin Says Second-Quarter Results Fell Short of Its Standards - WSJ](https://news.google.com/rss/articles/CBMitAFBVV95cUxPZFBPWW4zc3licGd0c1gxa2dqS1A2bFYyMTRvMTllczIyTWRrRVRURE1MV2l2dVhxU0tnZ1hhQ0ItRi1rcmpNSV9JWWdXaFdjY0daQ0ViS2Z5RlpGa2daS1FEMDU4TFVhMDlpcS1IQ3hVLW9RS3RUUXJCTkVTal9Wd3dEMlFEUW81RFZsNVRNSzd5a1BIOTA5SG40bjJOSXFSMHJiM1F0MnE2N283ZjJFZm80YXg?oc=5) | WSJ |
| S27 | news | 2026-09-26 | [Down 54%, Is AppLovin Still a Millionaire-Maker Stock? - The Motley Fool](https://news.google.com/rss/articles/CBMimAFBVV95cUxOZk53WE95WVpLa05iOE1GQ09PNmtWM3VyaW9QSnJYU2NBa1lJZDM5Y3JKNUVCVjRNaEhMUEtQZXpEaDNKNENZZVV1ak9sVThaY3REemRZd2FfaU1OOG52czBWOEkwT1NuTk5EVXpGa01wRW1pX0VZZjZaWjFjd3NQR3lQeGhEZ0prSV84NURFeTl2a0lpdW1sUw?oc=5) | The Motley Fool |
| S28 | news | 2026-10-02 | [AppLovin shares fall after court denies request against Unity - Investing.com](https://news.google.com/rss/articles/CBMiugFBVV95cUxObTFNZGkzS0Y4ZzRPYnlTYjhsWnZnSGZUMV9Qc1diOEFncFdyRnRibWlHcVh0MHFfbGMwWHU2UEx6YkJ3ME53QmhDbC1qdkV5NjlqUGNsRWdHQkRYNUNrRzhBS0RDaGFmQ3l2Q3FweHNTYWl2c1VnVXRQdWtncDloaE1WQUNGZlMxWUpJY2tfdkRjNzJDMTdTbjRXSkpBM2sybjR0V2w1Q3FPU2ZheENUU05xbERDbXprblE?oc=5) | Investing.com |
| S30 | news | 2026-10-13 | [AppLovin (APP) Grew 53% and Got Cheaper. Is the Market Missing Something? - Yahoo Finance](https://news.google.com/rss/articles/CBMikwFBVV95cUxPemZpM3lyTDdpNWNUbm5SSzRlOGtDOTVtYWRyTGRyNVJ1Ql9RVDlDU1p5Tm52aXVMMlE4dlkyRFNacDJCQ3lucEZPRFhfQV9pYkhhaWRTbUh5Z1hLMGZ1NUFLWkFqVmx2aUZRMjR3Y0FqZ1dOREFad3BWWkJZbEt3d2tWYW50UlNmWUc0bWR6cThyb0U?oc=5) | Yahoo Finance |
| S32 | news | 2026-08-17 | [AppLovin (APP) Offers Attractive Cash Flow Multiple? - Yahoo Finance](https://news.google.com/rss/articles/CBMiogFBVV95cUxQREdqckRmNHN1cWkwTDFPYkM5Tks3V25QY1NVWFNzOFpyaE9zRHFzeGFGNTNMQW5JVndhV3ZEdC1jZ1hQZ3F1bUNYUFpHNFhERXdxWEVOWmExMGxJa3FjUlVxVjFPa2FRSEhRWURwbjdJQXdYMDJrb2FDQ3FGWk9RejdHWm9Na3h5LWVNYmRCWDJfY2NEQXNhLUZORmpqVWRUaFE?oc=5) | Yahoo Finance |
| S33 | news | 2026-08-06 | [AppLovin Corp (APP) (Q2 2026) Earnings Call Highlights: Record Revenue and Strategic Expansion ... - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxQdmNwQVBGQmlJajZSaGNOckp6MDJVU2tFV01XZ2d0b3J4N2ZEZWxzUEo4bGhKQ2VWS1dOSFpQNHVEMHpHZXJ3RUxWcnotZXEtR2huUVRkMEdhV21GTGdvWVFuczRmR3NEbFFlWEtiZTF5WG9Ea3pRSmNVYWhISnZKdGF3dFV3NzFCUmp2LThldXQtYjNV?oc=5) | Yahoo Finance |
| S34 | news | 2026-09-26 | [Down 54%, Is AppLovin Still a Millionaire-Maker Stock? - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxOT3JOZG9FZGlZZHQ5TDRFTk4tSlVUbjhEcUZpMmFPcGxhbUdBanVFOXlaTnFuMGdTUjhLQkZkZ2xENE5DWFdlQzNvQ0VncUF2T2xSTFRQT2dlLV9yX2twUXJZQVlZLWZqOWJpOWhJbEdFTU55Q01kOVFrYWJLZ2ZtV1p3a2FvYkYzQW9fMkFyX2FxQk0yMjg5VnRwSDl0ZFJx?oc=5) | Yahoo Finance |
| S35 | news | 2026-10-07 | [AppLovin to Announce Third Quarter 2026 Results - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxOM2Yzd0xFZVFEZUluTC1lV3l5ZVl2UXBmZlJnbVpPakJocm40Ym90cnFtZWxWc3hTakdfWENmQ3p2Yk44YWktVWJCaGVOY19ud3ptcm84UWIyMW9vSjdJUXNaRnlGM2VPdW9JX1EwTGpQY3RhRVY3emJRaXlad0pTQnJmdUx4ZVdsNlZEcnc2SkR5LXVoQ2gtTERod0JPc0FxM19z?oc=5) | Yahoo Finance |
| S37 | news | 2026-09-23 | [AppLovin drops 3% as Edgewater analyst warns of stalled market share growth - Yahoo Finance](https://news.google.com/rss/articles/CBMioAFBVV95cUxOM1FXVzlpXzYzZnowbmhLVWZ5UVlTanJyRjFxQ2ZUWUllei1ULVhfY1FaQ3V4NmFMVjBfYkIxSndvOW5Lelo1MXFMYk5NSkZYR0hpQ2F4MDB5NmFNb2JaSTFPOWlVU0U3b3VreTFWOEpvV3BIVWhnTEgxY080X1h2Yi13bDZOd2Yzb3VwNGNXZkJVbk53OG03Nkd4SmJwTXZC?oc=5) | Yahoo Finance |
| S38 | data | 2026-09-01 | [Current share price for APP - InvestSmart](https://www.investsmart.com.au/security/nasdaq/app/applovin-corp/share-price) | 2026-09-01 종가 312.06 USD. 기준일(10-18)보다 약 6주 전 값이라 낡았다. 52주 저가는 약 297.5 USD. |
| S39 | filing | 2026-08-05 | [AppLovin Announces Second Quarter 2026 Financial Results](https://www.businesswire.com/news/home/20260805303503/en/AppLovin-Announces-Second-Quarter-2026-Financial-Results/) | 2분기 매출 19.24억 USD(전년 동기 대비 +53%), 조정 EBITDA 16.14억 USD(+58%). 3분기 가이던스: 매출 20.55억~20.85억 USD, 조정 EBITDA 17.1억~17.4억 USD(마진 약 83%). |
| S40 | news | 2026-08-06 | [AppLovin revenue growth slows to 53% as Q3 margin guidance drops to 83% - PPC Land](https://ppc.land/applovin-revenue-growth-slows-to-53-as-q3-margin-guidance-drops-to-83/) | 보도. 3분기 가이던스 중간값은 컨센서스보다 약 0.6% 낮았다. 경영진은 핵심 게임 광고 부문의 모델 개선이 늦어진 것을 원인으로 들었고, 수요·경쟁 탓은 아니라고 했다. 개선분은 분기 종료 직후에 반영됐다. |
| S41 | data | 2026-09-01 | [AppLovin (APP) market data - CoinGecko](https://www.coingecko.com/en/stocks/applovin) | 날짜 불명 스냅샷(9월 초로 추정). 시가총액 약 1,077억 USD, 52주 범위 297.82~735.50 USD. 7월에는 약 528 USD였다는 보도가 있다(Robinhood 페이지). |

# NVIDIA (NVDA) 리서치 보고서 — 기준일 2026-10-18

**판정 불가 — 모델** — 토론 전 단계에서 멈춤

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✗ model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: model.json 없음 또는 시나리오 계산 불가 — 계산 경고 참고

## 1. Variant perception

- 시장이 반영한 것: 현재 주가 214.13달러(F249)는 지속적인 고성장과 높은 마진이 FY2028 이후에도 이어진다는 가정을 상당 부분 반영한다. 컨센서스는 3분기 매출 약 1,040억 달러(F252)이고 가이던스는 1,080억 달러(F250)이다. 연간 컨센서스는 찾지 못했다.
- 우리가 다르게 보는 점: FY2027 매출은 이미 상당 부분 확정이라 이견이 없다. 이견은 지속 기간이다. 경영진의 FY2028 약 70% 성장(F253)보다 낮은 성장과 총이익률 하락(F251)을 기본 시나리오로 본다. 시장이 성장 둔화 속도와 운전자본·차입 확대의 질(F181, F44)을 충분히 가격에 넣지 않았을 가능성을 본다. 반대로 3분기 가이던스를 넘는 실적이 반복될 가능성도 열어 둔다.
- 왜 우리가 맞는가: 성장률이 높은 구간은 기저율상 드물고, 운전자본(재고·매출채권, C:inventory_gap)과 부채(F44)가 매출보다 빠르게 늘고 있다. 마진 하락 원인이 일시적 비용이 아니라 구조적 원가 상승이라면 FCF 마진 가정이 낮아진다. 다만 이 판단은 연간 컨센서스와 2차 요약(S47) 원문이 확인돼야 검증된다. [F249] [F252] [F250] [F253] [F251] [F181] [F44] [C:inventory_gap] [S47](https://fourweekmba.com/ai-nvidia-q2-fy2027-guide-margin-memory-tax/)
- 촉매: FY2027 3분기·4분기 실적 발표에서 총이익률, 매출채권 회전, 재고와 FY2028 가이던스 원문이 확인된다.
- 시점: FY2027Q3 실적(2026년 11월 하순 예상)부터 FY2027Q4 실적(2027년 2월 하순 예상)까지

## 5. 확신도와 비중

- 확신 가중 점수 +0.00 · 비중 참고값 0.0% (판정 전)
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`


- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 분석 모듈 (L4)

### 사업·산업 — unclear

NVIDIA는 AI 가속기와 네트워킹, CUDA 소프트웨어 스택을 데이터센터 고객에게 팔아 돈을 번다. 보도에 따르면 2분기(FY2027Q2) 데이터센터 매출은 890억 달러이다(S46, 원문 대조 전). 공시상 2분기 매출은 962.2억 달러(F191)이고 영업이익은 637.3억 달러(F161)이다. 총이익률은 75.0%(S47)이고 3분기 가이던스는 74.0%(F251)이다. 부품·메모리 비용 상승이 마진 하락의 원인이라고 보도되었다(S47). 단위경제의 핵심 지표(고객당 수익, 이탈률, 순매출유지율, 고객 집중도)는 공시 원문에서 확인하지 못했다. 마진과 현금창출력은 강하다. 다만 운전자본(매출채권·재고)과 부채가 빠르게 늘고 있어, 수요가 공급 제약으로 한도에 걸린 호황의 질을 확인해야 한다.

- [unit_economics] 총이익률이 FY2026에 71.1%로 내렸다가(FY2025는 75.0%) 2분기에 75.0% 수준으로 회복했다. 3분기 가이던스는 74.0%±0.5%p로 다시 소폭 하락하며, 원인은 부품·메모리 비용 상승이다. 가격 결정력은 있지만 공급 측 원가 압력이 마진을 좌우한다. (원인 설명은 2차 요약이라 원문 대조 필요) [C:gross_margin@FY2025] [C:gross_margin@FY2026] [F251] [S47](https://fourweekmba.com/ai-nvidia-q2-fy2027-guide-margin-memory-tax/)
- [unit_economics] CAC·회수기간·순매출유지율·코호트·고객 집중도는 확인하지 못했다. 이 사업은 소수의 대형 고객이 큰 비중을 차지하는 구조일 가능성이 있으나 근거가 없으므로 단위경제는 '불명확'으로 둔다. 악화의 근거(CAC 상승과 이탈 악화)는 없다. [S2](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- [industry] 성장 속도는 가이던스상 둔화된다. 2분기 매출은 전년 대비 +106%이고(S46), FY2026 연 성장률은 65.5%였다(C:revenue_growth@FY2026). 경영진은 FY2028 매출 성장을 약 70%로 전망했고 수요가 아니라 공급이 한도라고 밝혔다(S47, 2차 요약). 3분기 가이던스는 1,080억 달러, 컨센서스는 약 1,040억 달러이다. 이 가이던스에서 중국 데이터센터 컴퓨트 매출은 제외된다. 규제 근거(수출 통제 공시)는 수집되지 않았다. [F250] [F252] [F253] [C:revenue_growth@FY2026] [S46](https://www.iphoneincanada.ca/2026/08/27/nvidia-blows-past-expectations-with-96-2-billion-revenue-in-q2-2027/) [S47](https://fourweekmba.com/ai-nvidia-q2-fy2027-guide-margin-memory-tax/)
- [customers] 매출채권이 1분기 407.1억 달러에서 2분기 630.6억 달러로 급증했고(F180, F181), 같은 기간 매출은 816.1억 달러에서 962.2억 달러로 늘었다(F190, F191). 재고는 315.8억 달러로 계속 증가한다(F134). 회계 품질 신호로 발생액 비율 10.9%, 재고 증가율-매출 증가율 격차 46.9%가 경고되었다. 고객의 지급 조건 완화, 분기 말 출하 집중 여부, 재고 선매입 사유는 원문 확인이 필요하다. [F180] [F181] [F190] [F191] [F134] [C:accruals] [C:inventory_gap] [C:dso@FY2026]
- [customers] 이연수익이 1분기 17.1억 달러에서 2분기 46.2억 달러로 늘었다. 선수금·선지급형 계약이 늘고 있을 수 있으나 계약 구조는 확인하지 못했다. 같은 분기 부채가 74.7억 달러에서 323.7억 달러로, 배당 지급이 2.4억 달러에서 60.0억 달러로 급증했다. 원인은 미확인이며, 공급망·고객 선지원 목적인지 일회성 지급인지 판별하려면 10-Q 확인이 필요하다. [F61] [F62] [F43] [F44] [F80] [F81]
- [runway] 재투자 활주로는 넓은 편이다. 2분기 R&D는 70.5억 달러이고, 영업현금흐름은 FY2027Q1 503.4억 달러이다. 인수(Hugging Face 인수 발표)와 지분·보증형 투자(SB Energy 캠퍼스 보증, SK그룹 제휴, 프랑스 스타트업 투자)가 생태계 확장에 쓰이고 있다. 영업권은 FY2026Q3 62.6억 달러에서 FY2027Q2 211.2억 달러로 늘었다. 이 투자가 높은 수익률을 내는지는 아직 입증되지 않았다. [F201] [F151] [F98] [F101] [S27](https://news.google.com/rss/articles/CBMibkFVX3lxTE9id3J6aTYyX0NWdXR6emdfeEc2RTBRWjcwQ3ZDNFczYWF6dzEweEk2XzFaeDZ2TW1mb3ZsNUFHNzhGN2JGT1VjNXJrUkxtVURnZENaTXVpQld5SjBDbExHT05JZk1oNVo1QzB0VmJB?oc=5) [S40](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNYXdyMXl0ZUs3UDVBSFo1a3BCcDg4UlZUazQxSEp1allrY1B3SEVxYnQ2RjFQVFY5T3Q1YUFYM19Jc1ZQNXVobGtZNVJBc1BPQXpFWFFsTlBvWEJqV3VRM1lCU0ZzSVlHcS14UGxUZldBaEVsdUJveHN0TXJOLURfWDBxRlJYaFdXMHREU3VSNlVrcFZncENub1czY2lGV1F6eGpGSWZiU2loYlJYVVRFZTdQSU80Q0lNZmdvX3FZQ0hTU1pjZF8weHhCRWEzeURkcDk3N1Z3?oc=5) [S30](https://news.google.com/rss/articles/CBMiygFBVV95cUxQWWdmVzNHOG9UWDV2VnM0ek1kOTlMSDMydklMbjQzSDBSUWVYaGFJeFQwZk9tR09qNDVtMWlHS2pIUmVHVGxoOVFPSm1LYS1UUXdzNnNwa2U2MUVGaXFJLWVPb1NvNlN1OWhCX21OR3ROa1FjVFVsVVpuekRLMGVDYWw0SzBnMXRGMGY2ZlVXalpHVktOM2xhVlprcXpDLVV6WUVLdUFCOW43TkM2dW9lTnpBbS1TZ1hYd2pOMUMyc1lrVU1YaERxaWRR?oc=5) [S42](https://news.google.com/rss/articles/CBMic0FVX3lxTFBTRGZFbUlVZjJzY1M2ZGVVc3hubnlhYmNTTlJCWk5xdWJBeENiZzN2RGRfZ2U5d21tMjNVV0xKcFFSMm5BWDFydDhjT0o1NFBGQlc5aWlEcG5kMUlNY1pNS2J1UGhJaGlwbmhkaTFnYmtoNEE?oc=5)
- [runway] 회사는 1,500억 달러 규모로 자사주 매입 승인 한도를 늘렸다. 활주로에 대한 자신감이 있다는 신호로 읽을 수 있지만, 동시에 부채가 늘고 순현금이 마이너스(-109.2억 달러)로 돌아섰다는 점은 자본배분 분석가가 따져야 한다. 매입 승인액은 한도일 뿐 실행액이 아니다. FY2026 실제 매입은 400.9억 달러, FY2027Q1은 193.1억 달러이다. [S38](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPR0Vsb0ZuR3F0Sl9oYldFNF90azJObUVsNkJIb0VCWVJxWDRmRmdyR2swZE90ZkxwRGJERXBveVRvX040RUJMLU9Tc3lIbm44R2lzMzcxZHVYRkZmS0lGRWhHMDF4azNCakJHSk00UU1KdEhzNzVrYVd1SVpnNDZyZkV4bWVNVHY3cC1fSlpUSm1BTnZTdS1Vak5LOXB2NkF5X0VnZFhFR1A?oc=5) [F5] [F7] [C:net_cash]
- [proven] 규모의 흔적은 공시 숫자에 있다. FY2026 영업이익률 60.4%(C:operating_margin@FY2026)이고, 2분기 R&D는 70.5억 달러(F201)로 FY2022 연간 R&D 52.7억 달러(F192)를 한 분기에 넘어선다. 이 R&D 규모를 감당하며 이 마진을 유지하는 것이 규모 우위의 흔적이다. 다만 경쟁사 대비 마진·점유율 비교는 근거에 없다. [C:operating_margin@FY2026] [F201] [F192] [F161] [F191]
- [claimed] CUDA 생태계 기반 전환비용은 회사 발표·보도(CUDA-Q 확장, 오픈 에이전트 안전 플랫폼, Hugging Face 인수 발표)에서만 확인된다. 고객 이탈률, 가격 인상 후 잔존, 경쟁 플랫폼 이전 사례 같은 숫자 흔적은 수집되지 않았다. [S33](https://news.google.com/rss/articles/CBMitAFBVV95cUxPMjBPVXRfZFRUYmRtTUVFSXVfaUdHNTBFNjFONTkxWDhMMmUzRjBPcjdvRmNKbVNTLUxodExCS2RDZ1p2ZzhaaVM2ZTlFbUxmSnVfaWlaaTFnTzJHT09iMlZXTVRoTGxHNl9mS1NoZWJ1bDBPeXQyaFRUUEJyZGJJM3ZKOTZ1Nk03d3dnYk5YN3VFYm9RRnpYc0VabmUzb2lLZENBcUU2Z3B3ekd0YWtzcEtxRUg?oc=5) [S25](https://news.google.com/rss/articles/CBMibkFVX3lxTFAxdzBTN1hGTnNfZXZNWUU1MjhzQnpHUndjNkNYMGZiRGc1TDR5NExfTmtrbkFvZU5Fakp1eG1CVVFOZ0tpYzJ2aFVVY1pCSFY4Vl80Tkhqbkp3blMyejJkUXdpTVlBZWdzd2VKdVdR?oc=5) [S27](https://news.google.com/rss/articles/CBMibkFVX3lxTE9id3J6aTYyX0NWdXR6emdfeEc2RTBRWjcwQ3ZDNFczYWF6dzEweEk2XzFaeDZ2TW1mb3ZsNUFHNzhGN2JGT1VjNXJrUkxtVURnZENaTXVpQld5SjBDbExHT05JZk1oNVo1QzB0VmJB?oc=5)
- [claimed] 고객사 용량을 보증·공동 투자로 확보하는 움직임(AWS의 GPU 200만 개 추가 공급 발표, SB Energy 오하이오 캠퍼스를 NVIDIA 컴퓨트 전용으로 보증)은 수요 고정 시도로 읽힌다. 하지만 계약 조건과 경제성은 원문 미확인이다. [S35](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNZUNocGNzT2FJb01QNmVWTHpoSXkxUUNVdlRDTVZET3hZZVBDN0JGTVBTUFF5aEdERTJOcU9LeV9VMW12ZlZSck5uQ194MjFmYVlMWGt1SzdVODFjY2hkV2RFamlFdzVaWkNYNUdnbXcxbF9rTGJwY005LTlwN1BtUDdTWDVaMk1kejdPRzJKaVRTUVB4X3FWVnVlNnNPcUxUZGNHSzNTV0liVVJaNTMwdEdYcENaOFVtZVc5TXFIY0xsUlZJZUg2bkJKVnJ2OUhqSVg3bDZrQTd3eWdTVmNvMlJkcw?oc=5) [S40](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNYXdyMXl0ZUs3UDVBSFo1a3BCcDg4UlZUazQxSEp1allrY1B3SEVxYnQ2RjFQVFY5T3Q1YUFYM19Jc1ZQNXVobGtZNVJBc1BPQXpFWFFsTlBvWEJqV3VRM1lCU0ZzSVlHcS14UGxUZldBaEVsdUJveHN0TXJOLURfWDBxRlJYaFdXMHREU3VSNlVrcFZncENub1czY2lGV1F6eGpGSWZiU2loYlJYVVRFZTdQSU80Q0lNZmdvX3FZQ0hTU1pjZF8weHhCRWEzeURkcDk3N1Z3?oc=5)

### 경영진·자본배분 — mixed

경영진이 주주와 같은 방향을 보는지는 보상(DEF 14A)과 내부자 매매 근거가 없어 판단할 수 없다. 자본배분과 희석에서는 주주에게 우호적인 흔적이 있다. FY2026 자사주 매입은 400.9억 달러로 SBC 63.9억 달러를 크게 웃돌았고, 희석 주식 수는 245.1억 주에서 FY2027Q2에 242.8억 주로 줄었다. SBC/매출도 3.0%로 낮아졌다. 반면 FY2027Q2에 부채가 323.7억 달러로, 배당이 60.0억 달러로 급증했고 Hugging Face 인수 발표(S27)와 SB Energy 보증(S40) 같은 대형 결정이 이어졌다. 원문을 확인하지 못해 자본배분의 수익률과 규율은 평가할 수 없다. 가이던스 적중률도 과거 분기 가이던스가 없어 계산하지 못했다. 근거 부족을 반영해 mixed로 둔다.

- [compensation] 근거 없음. DEF 14A(S10, 2026-05-12)가 수집돼 있으나 보상 연동 지표와 베스팅 기간은 근거에 담기지 않았다. 장기 지표(FCF·ROIC·주당가치)에 연동되는지 단기 EPS에 연동되는지 판단할 수 없다. [S10](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000036/nvda-20260512.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도 자료가 수집되지 않았다. 2026년에 경영진 변동 8-K가 여러 건 있었으나(2026-01-23, 2026-03-06, 2026-04-27, 2026-05-08, 2026-07-02) 내용을 확인하지 못해 해석하지 않는다. [S16](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000003/nvda-20260120.htm) [S13](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000024/nvda-20260302.htm) [S12](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000026/nvda-20260424.htm) [S11](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000028/nvda-20260507.htm) [S5](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000060/nvda-20260628.htm)
- [guidance] 과거 분기 가이던스가 수집되지 않아 적중률(C:guidance_hit_rate)을 계산할 수 없다. 경영진 신뢰도는 검증되지 않았다. 확인된 가이던스는 FY2027Q3 매출 1,080억 달러(컨센서스 약 1,040억 달러)와 FY2028 매출 성장률 약 70%뿐이다. 후자는 2차 요약 보도(S47)라서 원문 대조가 필요하고, 두 가이던스는 중국 데이터센터 컴퓨트 매출을 제외한 수치다. [F250] [F252] [F253] [S46](https://www.iphoneincanada.ca/2026/08/27/nvidia-blows-past-expectations-with-96-2-billion-revenue-in-q2-2027/) [S47](https://fourweekmba.com/ai-nvidia-q2-fy2027-guide-margin-memory-tax/)
- [dilution] 희석은 통제되고 있다. SBC는 FY2026 63.9억 달러이고 SBC/매출은 3.0%로 FY2022 7.4%에서 낮아졌다. 희석 주식 수는 FY2026 245.1억 주(전년 대비 -1.2%)에서 FY2027Q2 242.8억 주로 줄었다. 매입이 SBC를 상쇄하고 주식 수를 실제로 줄이는 것으로 보인다. SBC는 분기마다 늘어 FY2027Q1 19.3억 달러, FY2027Q2 20.3억 달러다. [C:sbc_to_revenue@FY2026] [C:sbc_to_revenue@FY2022] [C:share_change@FY2026] [F206] [F67] [F72] [F210] [F211]
- [capital_allocation] 자사주 매입은 FY2025 337.1억 달러, FY2026 400.9억 달러, FY2027Q1 193.1억 달러로 커졌다. 이사회는 1,500억 달러 증액을 승인했다(S38). 다만 매입 평균 단가는 확인되지 않았다. 현 주가는 214.13달러이고 52주 범위는 164.27~243.37달러라서 고점 매입 여부를 판단할 수 없다. [F4] [F5] [F7] [S38](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPR0Vsb0ZuR3F0Sl9oYldFNF90azJObUVsNkJIb0VCWVJxWDRmRmdyR2swZE90ZkxwRGJERXBveVRvX040RUJMLU9Tc3lIbm44R2lzMzcxZHVYRkZmS0lGRWhHMDF4azNCakJHSk00UU1KdEhzNzVrYVd1SVpnNDZyZkV4bWVNVHY3cC1fSlpUSm1BTnZTdS1Vak5LOXB2NkF5X0VnZFhFR1A?oc=5) [F249] [S45](https://stockanalysis.com/stocks/nvda/)
- [capital_allocation] FY2027Q2에 부채가 74.7억 달러에서 323.7억 달러로, 배당이 2.4억 달러에서 60.0억 달러로 늘었다. 대규모 차입을 주주환원 확대와 같은 시기에 했다는 뜻일 수 있으나 원인은 S2·S3 원문 확인 전이라 단정하지 않는다. 같은 분기 현금은 224.4억 달러로 늘었다. [F43] [F44] [F80] [F81] [F17] [S2](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- [capital_allocation] M&A와 보증 약정이 늘고 있다. 영업권은 FY2026Q3 62.6억 달러에서 FY2026 208.3억 달러로 늘었다. 2026-09-03에는 Hugging Face 인수가 발표됐고(S27), SB Energy 캠퍼스 보증도 공시됐다(S40). 인수 대가, 보증 규모, 수익률 근거는 사실로 담기지 않았다. 영업권 증가가 어느 인수에서 비롯됐는지도 확인되지 않았다. [F98] [F99] [S27](https://news.google.com/rss/articles/CBMibkFVX3lxTE9id3J6aTYyX0NWdXR6emdfeEc2RTBRWjcwQ3ZDNFczYWF6dzEweEk2XzFaeDZ2TW1mb3ZsNUFHNzhGN2JGT1VjNXJrUkxtVURnZENaTXVpQld5SjBDbExHT05JZk1oNVo1QzB0VmJB?oc=5) [S40](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNYXdyMXl0ZUs3UDVBSFo1a3BCcDg4UlZUazQxSEp1allrY1B3SEVxYnQ2RjFQVFY5T3Q1YUFYM19Jc1ZQNXVobGtZNVJBc1BPQXpFWFFsTlBvWEJqV3VRM1lCU0ZzSVlHcS14UGxUZldBaEVsdUJveHN0TXJOLURfWDBxRlJYaFdXMHREU3VSNlVrcFZncENub1czY2lGV1F6eGpGSWZiU2loYlJYVVRFZTdQSU80Q0lNZmdvX3FZQ0hTU1pjZF8weHhCRWEzeURkcDk3N1Z3?oc=5)
- [capital_allocation] 재투자는 R&D가 FY2025 129.1억 달러에서 FY2026 185.0억 달러로 늘었고, FY2027Q2 분기 R&D는 70.5억 달러다. 영업이익률은 FY2026 60.4%로 높은 수준이다. 재투자의 수익은 높게 유지되고 있으나, 이것이 경영진의 배분 규율 덕분인지 업황 덕분인지는 이 근거만으로 가를 수 없다. [F195] [F196] [F201] [C:operating_margin@FY2026]

### 회계 품질 — watch

코드가 낸 red 신호는 없고 watch 신호 3개(발생액·매출채권 격차·재고 격차)가 있다. 셋 다 매출이 2배 안팎으로 커지는 가운데 운전자본이 쌓인 결과로 설명된다. 근거는 DSO가 안정적이고(C:dso@FY2026 65.0일), SBC 비중이 낮으며(C:sbc_to_revenue@FY2026 3.0%), 희석이 아니라 주식 수가 줄고 있다는 점이다(C:share_change@FY2026 -1.2%). 다만 재고가 매출보다 빠르게 늘어(C:inventory_gap) 평가손·충당금 위험을 따로 봐야 한다. FY2027Q2의 매출채권(630.6억 달러), 부채(323.7억 달러), 배당(60.0억 달러), 이연매출(46.2억 달러) 급증은 원문(S2) 확인 전까지 해명되지 않았다. 감사의견, 감사인 변경, 특수관계자 거래, Non-GAAP 조정 내역도 확인하지 못했다. 이 공백들은 red_flag의 증거가 아니라 미확인 항목이므로 grade는 watch로 둔다. 순이익보다 영업현금흐름 기준으로 보는 것이 안전하고, 재고와 매출채권 추이를 계속 따라가야 한다.

- [concern] accruals: 발생액 비율이 10.9%로 문턱 10%를 소폭 넘고, 직전 해도 9.9%로 문턱 근처였다. 순이익이 영업현금흐름보다 큰 상태가 두 해째 이어진다. 다만 순이익 대부분이 재고(100.8억→214.0억 달러)와 매출채권(230.7억→384.7억 달러) 증가에 묶인 운전자본 확대로 설명된다. 영업현금흐름 자체는 흑자이고(ocf_negative 신호 없음) 현금 전환이 순이익을 크게 밑돌지는 않는다. 그래도 이익의 질은 순이익보다 영업현금흐름 기준으로 보는 편이 안전하다. [C:accruals] [C:accruals_ratio@FY2026] [C:accruals_ratio@FY2025] [F139] [F149] [F132] [F128] [F179] [F175]
- [benign] receivables_gap: 초과 폭 16.5%p는 FY2025 기준이고 문턱 15%를 약간 넘는 수준이다. 당시 매출이 2배 넘게 늘던 급성장기의 채권 증가이고, DSO는 FY2024 59.9일에서 FY2025 64.5일로, FY2026 65.0일로 안정적이다. 채권 질이 나빠졌다는 신호는 약하다. 다만 FY2027Q2 매출채권이 407.1억 달러에서 630.6억 달러로 급증했다. 같은 분기 매출은 816.1억 달러에서 962.2억 달러로 늘었다. 이 급증은 매출 증가에 비해 크므로 집중도나 지급 조건 변경 여부를 S2 원문에서 확인해야 한다. [C:receivables_gap] [C:dso@FY2024] [C:dso@FY2025] [C:dso@FY2026] [F174] [F175] [F180] [F181] [F190] [F191]
- [concern] inventory_gap: FY2026 재고 증가율이 매출 증가율(65.5%)을 46.9%p 웃돈다. DIO도 FY2025 112.7일에서 FY2026 125.0일로 늘었고, 재고는 FY2027Q2 315.8억 달러까지 계속 증가했다. 공급 제약 속에서 신제품 램프업과 부품 선확보로 재고를 쌓는 것일 수 있다. 하지만 세대 교체가 빠른 제품이라 평가손·충당금 위험이 있고, 이는 이익의 질에 직접 영향을 준다. 재고 충당금과 구매 약정 규모는 확인하지 못했다. [C:inventory_gap] [C:revenue_growth@FY2026] [C:dio@FY2025] [C:dio@FY2026] [F132] [F134] [F128]
- [watch] FY2027Q2에 매출채권(630.6억 달러), 이연매출(46.2억 달러), 부채(323.7억 달러), 배당(60.0억 달러)이 한 분기에 크게 변했다. 이연매출은 17.1억 달러에서 늘었고 부채는 74.7억 달러에서 늘었다. 배당은 직전 분기 2.4억 달러였다. 선수금 구조 변화, 차입 조달, 특별배당 가능성이 있으나 원문 확인 전이다. [F181] [F62] [F44] [F81] [F61] [F43] [F80] [S2](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- [info] 영업권이 FY2026에 62.6억 달러(FY2026Q3)에서 208.3억 달러로 크게 늘었다. 인수로 인한 증가로 보이며 FY2027Q2에는 211.2억 달러다. 총자산 대비 비중은 문턱 40%에 한참 못 미쳐 영업권 신호는 없다. 다만 Hugging Face 인수(S27)가 실행되면 영업권이 더 늘 수 있다. [F98] [F99] [F101] [F229] [S27](https://news.google.com/rss/articles/CBMibkFVX3lxTE9id3J6aTYyX0NWdXR6emdfeEc2RTBRWjcwQ3ZDNFczYWF6dzEweEk2XzFaeDZ2TW1mb3ZsNUFHNzhGN2JGT1VjNXJrUkxtVURnZENaTXVpQld5SjBDbExHT05JZk1oNVo1QzB0VmJB?oc=5)
- [info] SBC는 FY2026 63.9억 달러로 매출의 3.0%, 영업현금흐름의 6.2% 수준이라 문턱(10%·50%) 아래다. 코드가 낸 non_gaap 신호도 없다. 다만 Non-GAAP 조정 내역의 반복성은 8-K 실적 발표 원문으로 확인하지 못했다. [F206] [C:sbc_to_revenue@FY2026] [C:sbc_to_ocf@FY2026] [S3](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/nvda-20260826.htm) [S15](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/nvda-20260225.htm)
- [info] 희석 주식 수는 FY2027Q2 242.8억 주로 분기마다 줄고 있다. 자사주 매입은 FY2026 400.9억 달러, FY2027Q1 193.1억 달러였고, 1,500억 달러 증액 승인이 발표됐다(S38). 희석 신호는 없다. 다만 FY2022의 희석 주식 수 25.4억 주는 주식 분할 전 값으로 보여 FY2023 추이 계산은 단위 정합성에 주의해야 한다. [F72] [F5] [F7] [S38](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPR0Vsb0ZuR3F0Sl9oYldFNF90azJObUVsNkJIb0VCWVJxWDRmRmdyR2swZE90ZkxwRGJERXBveVRvX040RUJMLU9Tc3lIbm44R2lzMzcxZHVYRkZmS0lGRWhHMDF4azNCakJHSk00UU1KdEhzNzVrYVd1SVpnNDZyZkV4bWVNVHY3cC1fSlpUSm1BTnZTdS1Vak5LOXB2NkF5X0VnZFhFR1A?oc=5) [F63] [F64] [C:share_change@FY2026]
- [watch] 감사의견(계속기업 의문·핵심감사사항), 감사인 변경, 재무제표 정정은 이번 근거에서 확인하지 못했다. 8-K 목록에 정정(4.02)이나 감사인 변경(4.01)을 나타내는 항목은 보이지 않지만 이것이 부재의 증거는 아니다. 10-K 원문 확인이 필요하다. [S14](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm) [S1](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm) [S5](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000060/nvda-20260628.htm) [S6](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000056/nvda-20260624.htm)
- [watch] SB Energy 시설 보증(S40), 투자 약정, 고객·파트너 거래 같은 순환 구조의 거래가 있다. 특수관계자·지분 투자 거래가 매출 인식에 영향을 주는지는 원문으로 확인하지 못했다. 현재 증거로 red로 올릴 근거는 없다. [S40](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNYXdyMXl0ZUs3UDVBSFo1a3BCcDg4UlZUazQxSEp1allrY1B3SEVxYnQ2RjFQVFY5T3Q1YUFYM19Jc1ZQNXVobGtZNVJBc1BPQXpFWFFsTlBvWEJqV3VRM1lCU0ZzSVlHcS14UGxUZldBaEVsdUJveHN0TXJOLURfWDBxRlJYaFdXMHREU3VSNlVrcFZncENub1czY2lGV1F6eGpGSWZiU2loYlJYVVRFZTdQSU80Q0lNZmdvX3FZQ0hTU1pjZF8weHhCRWEzeURkcDk3N1Z3?oc=5) [S35](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNZUNocGNzT2FJb01QNmVWTHpoSXkxUUNVdlRDTVZET3hZZVBDN0JGTVBTUFF5aEdERTJOcU9LeV9VMW12ZlZSck5uQ194MjFmYVlMWGt1SzdVODFjY2hkV2RFamlFdzVaWkNYNUdnbXcxbF9rTGJwY005LTlwN1BtUDdTWDVaMk1kejdPRzJKaVRTUVB4X3FWVnVlNnNPcUxUZGNHSzNTV0liVVJaNTMwdEdYcENaOFVtZVc5TXFIY0xsUlZJZUg2bkJKVnJ2OUhqSVg3bDZrQTd3eWdTVmNvMlJkcw?oc=5) [S30](https://news.google.com/rss/articles/CBMiygFBVV95cUxQWWdmVzNHOG9UWDV2VnM0ek1kOTlMSDMydklMbjQzSDBSUWVYaGFJeFQwZk9tR09qNDVtMWlHS2pIUmVHVGxoOVFPSm1LYS1UUXdzNnNwa2U2MUVGaXFJLWVPb1NvNlN1OWhCX21OR3ROa1FjVFVsVVpuekRLMGVDYWw0SzBnMXRGMGY2ZlVXalpHVktOM2xhVlprcXpDLVV6WUVLdUFCOW43TkM2dW9lTnpBbS1TZ1hYd2pOMUMyc1lrVU1YaERxaWRR?oc=5)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (15%) 고객의 AI 설비투자가 소화 국면에 들어가며 수요가 급락한다. 공급 한도로 가려져 있던 수요 둔화가 드러나는 순서는 다음과 같다. 대형 고객이 주문을 줄이고, 선확보해 둔 재고(F134)와 급증한 매출채권(F181)이 평가손과 대손으로 바뀐다. 기저율상 드문 고성장 구간이 끝나면서 이익이 매출보다 더 빠르게 줄어든다. 높은 배수는 성장 지속을 전제로 하므로(C:pe), 이익 감소와 배수 하락이 동시에 오며 주가가 크게 내려간다. 재고·채권 쏠림은 이미 회계 신호로 잡혀 있다(C:inventory_gap, C:receivables_gap). [F134] [F181] [C:inventory_gap] [C:receivables_gap] [C:pe] [S46](https://www.iphoneincanada.ca/2026/08/27/nvidia-blows-past-expectations-with-96-2-billion-revenue-in-q2-2027/)
- (15%) 원가 압력과 가격 경쟁으로 총이익률이 구조적으로 내려간다. 3분기 총이익률 가이던스가 이미 하락했고 원인은 부품·메모리 비용 상승이다(F251, S47). 공급 제약이 풀리거나 고객이 자체 칩·대체 공급처를 키우면 가격 전가력이 약해진다. 마진이 꺾이면 FCF 마진 가정이 무너지고, 시장이 가격에 넣은 마진 지속성(C:operating_margin@FY2026)이 훼손된다. 총이익률은 FY2026에 이미 한 번 내려갔다(C:gross_margin@FY2026). [F251] [S47](https://fourweekmba.com/ai-nvidia-q2-fy2027-guide-margin-memory-tax/) [C:operating_margin@FY2026] [C:gross_margin@FY2026]
- (10%) 순환 구조의 자본배분이 부실화한다. 한 분기에 부채가 크게 늘고(F44), 배당이 크게 늘고(F81), 영업권이 FY2026에 급증했다(F99). 여기에 Hugging Face 인수(S27), SB Energy 시설 보증(S40), 고객·파트너 투자가 겹친다. 고객의 자금 조달을 회사가 보증·투자로 떠받치면 수요가 실제인지 회사 자금이 만든 것인지 가려지지 않는다. 호황이 꺾이면 보증이 현실화되고, 영업권 손상이 나며, 고점에서 집행한 자사주 매입(S38)은 가치를 파괴한다. 순현금은 이미 마이너스다(C:net_cash). [F44] [F81] [F99] [S27](https://news.google.com/rss/articles/CBMibkFVX3lxTE9id3J6aTYyX0NWdXR6emdfeEc2RTBRWjcwQ3ZDNFczYWF6dzEweEk2XzFaeDZ2TW1mb3ZsNUFHNzhGN2JGT1VjNXJrUkxtVURnZENaTXVpQld5SjBDbExHT05JZk1oNVo1QzB0VmJB?oc=5) [S40](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNYXdyMXl0ZUs3UDVBSFo1a3BCcDg4UlZUazQxSEp1allrY1B3SEVxYnQ2RjFQVFY5T3Q1YUFYM19Jc1ZQNXVobGtZNVJBc1BPQXpFWFFsTlBvWEJqV3VRM1lCU0ZzSVlHcS14UGxUZldBaEVsdUJveHN0TXJOLURfWDBxRlJYaFdXMHREU3VSNlVrcFZncENub1czY2lGV1F6eGpGSWZiU2loYlJYVVRFZTdQSU80Q0lNZmdvX3FZQ0hTU1pjZF8weHhCRWEzeURkcDk3N1Z3?oc=5) [S38](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPR0Vsb0ZuR3F0Sl9oYldFNF90azJObUVsNkJIb0VCWVJxWDRmRmdyR2swZE90ZkxwRGJERXBveVRvX040RUJMLU9Tc3lIbm44R2lzMzcxZHVYRkZmS0lGRWhHMDF4azNCakJHSk00UU1KdEhzNzVrYVd1SVpnNDZyZkV4bWVNVHY3cC1fSlpUSm1BTnZTdS1Vak5LOXB2NkF5X0VnZFhFR1A?oc=5) [C:net_cash]
- (10%) 수출 통제 강화와 고객 집중이 겹친다. 가이던스가 중국 데이터센터 컴퓨트 매출을 이미 제외하고 있어(S46) 중국은 상방 완충이 아니라 추가 규제의 하방 변수다. 소수 대형 고객의 비중이 크다면(근거 미확인, F250·F252의 가이던스와 컨센서스 격차가 작지 않은 것도 기대치가 높다는 신호) 한 고객의 발주 지연이나 내재화가 매출 가이던스 미달로 이어진다. 가이던스 미달은 성장주에 가장 큰 충격이 된다. [S46](https://www.iphoneincanada.ca/2026/08/27/nvidia-blows-past-expectations-with-96-2-billion-revenue-in-q2-2027/) [F250] [F252]
- 약한 가정 `base.fcf_margin`: 기본 시나리오는 FY2026 영업현금흐름 마진과 영업이익률이 유지된다고 본다. 그러나 근거는 마진이 이미 흔들림을 보여 준다. 총이익률은 FY2026에 한 번 내려갔고(C:gross_margin@FY2026), 3분기 가이던스도 다시 낮아졌다(F251). 재고와 매출채권이 현금으로 바뀌지 않고 쌓이는 중이며(C:accruals), 영업현금흐름보다 순이익이 큰 상태가 이어지고 있다. 설비투자와 인수·보증까지 반영한 FCF 마진은 아직 검증되지 않았다. [C:gross_margin@FY2026] [F251] [C:accruals] [F149] [F186]
- 약한 가정 `base.exit_multiple`: 출구 배수는 성장이 둔화해도 높은 배수가 유지된다는 가정이다. 성장이 한 자릿수로 내려오는 구간에서도 현재와 가까운 배수를 받으려면 마진과 점유율이 그대로여야 하는데, 이는 해자의 숫자 증거가 약한 상태(business.json은 전환비용과 비용 우위를 claimed로 분류)에서 가장 낙관적인 부분이다. 현재 PER(C:pe)이 이미 성장 지속을 상당 부분 가격에 넣은 상태라서, 배수 가정이 조금만 어긋나도 5년 수익률이 크게 바뀐다. [C:pe] [C:ev_revenue] [F253]
- 약한 가정 `base.revenue_growth`: 기본 시나리오의 FY2028 성장률은 경영진 전망보다 낮추었으나, 그 전망 자체가 2차 요약이라 원문 대조가 안 됐고(S47), 연간 컨센서스도 없다. 기저율 경고조차 계산되지 않았다(시나리오 계산 불가). 이후 연도의 급격한 둔화 경로가 근거 없이 놓여 있어 하방 위험의 시점과 크기를 어느 쪽으로도 확인할 수 없다. [F253] [S47](https://fourweekmba.com/ai-nvidia-q2-fy2027-guide-margin-memory-tax/) [C:revenue_growth@FY2026]

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2026)

| 지표 (키) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| 매출 (revenue) | 269.1억 USD | 269.7억 USD | 609.2억 USD | 1,305.0억 USD | 2,159.4억 USD |
| 매출 성장 (revenue_growth) | — | 0.2% | 125.9% | 114.2% | 65.5% |
| 총이익률 (gross_margin) | 64.9% | 56.9% | 72.7% | 75.0% | 71.1% |
| 영업이익률 (operating_margin) | 37.3% | 15.7% | 54.1% | 62.4% | 60.4% |
| 순이익 (net_income) | 97.5억 USD | 43.7억 USD | 297.6억 USD | 728.8억 USD | 1,200.7억 USD |
| 영업현금흐름 (ocf) | 91.1억 USD | 56.4억 USD | 280.9억 USD | 640.9억 USD | 1,027.2억 USD |
| SBC (sbc) | 20.0억 USD | 27.1억 USD | 35.5억 USD | 47.4억 USD | 63.9억 USD |
| SBC/매출 (sbc_to_revenue) | 7.4% | 10.0% | 5.8% | 3.6% | 3.0% |
| SBC/영업현금흐름 (sbc_to_ocf) | 22.0% | 48.0% | 12.6% | 7.4% | 6.2% |
| ROIC (roic) | 60.2% | 21.4% | 108.7% | 158.5% | 71.3% |
| 순현금 (net_cash) | 102.6억 USD | 23.4억 USD | 162.8억 USD | 347.5억 USD | 21.4억 USD |
| 순부채/EBITDA (net_debt_to_ebitda) | -0.92x | -0.41x | -0.47x | -0.42x | -0.02x |
| 희석 주식 수 (diluted_shares) | 25.4억 | 250.7억 | 249.4억 | 248.0억 | 245.1억 |
| 주식 수 변화 (share_change) | — | 889.0% | -0.5% | -0.5% | -1.2% |
| DSO(일) (dso) | 63.1 | 51.8 | 59.9 | 64.5 | 65.0 |
| DIO(일) (dio) | 100.7 | 162.1 | 116.0 | 112.7 | 125.0 |
| 발생액 비율 (accruals_ratio) | — | -3.0% | 3.1% | 9.9% | 10.9% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, cost_of_revenue, d_and_a, debt, debt_current, debt_total, deferred_revenue, deferred_revenue_growth, dividends, ebitda, equity, goodwill, goodwill_to_assets, gross_profit, income_tax, interest_expense, inventory, inventory_growth, operating_income, pretax_income, receivables, receivables_growth, rnd, short_term_investments, total_assets

### 시장 · TTM(FY2027Q2) 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 214.13 USD/share (2026-10-16, F249) |
| 희석 주식 수 (shares) | 242.8억 |
| 시가총액 (market_cap) | 5.20조 USD |
| 순현금 (net_cash) | -109.2억 USD |
| EV (ev) | 5.21조 USD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 17.20x |
| PER (pe) | 26.96x |
| 순부채/EBITDA (net_debt_to_ebitda) | — |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] accruals (C:accruals): 발생액 비율(순이익-영업현금흐름)/평균 총자산 10.9% > 10%
- [watch] receivables_gap (C:receivables_gap): FY2025 매출채권 증가율 - 매출 증가율 16.5% > 15%
- [watch] inventory_gap (C:inventory_gap): FY2026 재고 증가율 - 매출 증가율 46.9% > 15%

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull", "revenue_growth": [0.88, 0.7, 0.4, 0.25, 0.15, 0.12, 0.1, 0.08, 0.07, 0.06], "fcf_margin": 0.5, "exit_multiple": 25, "share_change": -0.015}: 
- 슬레이터 case={"from": "base"}: 
- 애크먼 case={"from": "base"}: price=214.1, leveraged=아니오

### 계산 경고

- 시나리오 계산 불가 — 연간 매출·영업현금흐름·설비투자·주가·주식 수 필요

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-09-03 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm) |  |
| S2 | filing | 2026-08-26 | [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) |  |
| S3 | filing | 2026-08-26 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/nvda-20260826.htm) |  |
| S4 | filing | 2026-08-17 | [8-K 중요 계약 IR·컨퍼런스 자료](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm) |  |
| S5 | filing | 2026-07-02 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000060/nvda-20260628.htm) |  |
| S6 | filing | 2026-06-30 | [8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000056/nvda-20260624.htm) |  |
| S7 | filing | 2026-06-18 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1045810/000119312526275783/d48176d8k.htm) |  |
| S8 | filing | 2026-05-20 | [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm) |  |
| S9 | filing | 2026-05-20 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/nvda-20260520.htm) |  |
| S10 | filing | 2026-05-12 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000036/nvda-20260512.htm) |  |
| S11 | filing | 2026-05-08 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000028/nvda-20260507.htm) |  |
| S12 | filing | 2026-04-27 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000026/nvda-20260424.htm) |  |
| S13 | filing | 2026-03-06 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000024/nvda-20260302.htm) |  |
| S14 | filing | 2026-02-25 | [10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm) |  |
| S15 | filing | 2026-02-25 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/nvda-20260225.htm) |  |
| S16 | filing | 2026-01-23 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000003/nvda-20260120.htm) |  |
| S17 | filing | 2025-11-19 | [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm) |  |
| S18 | filing | 2025-11-19 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000228/nvda-20251119.htm) |  |
| S19 | filing | 2024-02-21 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/0001045810-24-000029-index.htm) |  |
| S20 | filing | 2025-02-26 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/0001045810-25-000023-index.htm) |  |
| S21 | filing | 2023-02-24 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1045810/000104581023000017/0001045810-23-000017-index.htm) |  |
| S22 | filing | 2025-05-28 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000116/0001045810-25-000116-index.htm) |  |
| S23 | filing | 2025-08-27 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000209/0001045810-25-000209-index.htm) |  |
| S24 | filing | 2022-03-18 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000036/0001045810-22-000036-index.htm) |  |
| S25 | news | 2026-09-28 | [NVIDIA Launches Open Agent Safety Platform to Secure Agents From Testing to Deployment - NVIDIA Newsroom](https://news.google.com/rss/articles/CBMibkFVX3lxTFAxdzBTN1hGTnNfZXZNWUU1MjhzQnpHUndjNkNYMGZiRGc1TDR5NExfTmtrbkFvZU5Fakp1eG1CVVFOZ0tpYzJ2aFVVY1pCSFY4Vl80Tkhqbkp3blMyejJkUXdpTVlBZWdzd2VKdVdR?oc=5) | NVIDIA Newsroom |
| S27 | news | 2026-09-03 | [NVIDIA to Acquire Hugging Face - NVIDIA Blog](https://news.google.com/rss/articles/CBMibkFVX3lxTE9id3J6aTYyX0NWdXR6emdfeEc2RTBRWjcwQ3ZDNFczYWF6dzEweEk2XzFaeDZ2TW1mb3ZsNUFHNzhGN2JGT1VjNXJrUkxtVURnZENaTXVpQld5SjBDbExHT05JZk1oNVo1QzB0VmJB?oc=5) | NVIDIA Blog |
| S29 | news | 2026-09-09 | [NVIDIA Expands AI Infrastructure Capacity in Partnership With Australia’s Data Center Ecosystem - NVIDIA Newsroom](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPd2dkbUp0Zi13THRQMU1kMXNIZVktQVN5NVR2cEszemg1RWM1cURfcDBCRGhLMGJfc3NTaW12anhJeGVDb1FfTC1SaHUzcnVUTzBnVmJseHBuUngteFBFLUZQT2FkMzBaTEEzclA0WFJGT0FmZ1htaFFSX1YwNnVTNk1yT0dnNVhzUm9Vbms0U0N0ck5UNVpyUlNZZ2JaQ3NDZ0hHUEw1VE5BMjZ0dGFIX2plWTRqRHRDeG5yQTFnY3pHZlFhcG9Ndw?oc=5) | NVIDIA Newsroom |
| S30 | news | 2026-07-24 | [SK Group and NVIDIA Expand Strategic Partnership Across AI Factories and Next-Generation Memory - NVIDIA Newsroom](https://news.google.com/rss/articles/CBMiygFBVV95cUxQWWdmVzNHOG9UWDV2VnM0ek1kOTlMSDMydklMbjQzSDBSUWVYaGFJeFQwZk9tR09qNDVtMWlHS2pIUmVHVGxoOVFPSm1LYS1UUXdzNnNwa2U2MUVGaXFJLWVPb1NvNlN1OWhCX21OR3ROa1FjVFVsVVpuekRLMGVDYWw0SzBnMXRGMGY2ZlVXalpHVktOM2xhVlprcXpDLVV6WUVLdUFCOW43TkM2dW9lTnpBbS1TZ1hYd2pOMUMyc1lrVU1YaERxaWRR?oc=5) | NVIDIA Newsroom |
| S31 | news | 2026-08-26 | [NVIDIA Announces Financial Results for Second Quarter Fiscal 2027 - NVIDIA Newsroom](https://news.google.com/rss/articles/CBMiogFBVV95cUxOcjZPeVV6eC01Z2tWOHlyVEhmMG9uZDgyaXdvVTV3MVVMWGdKVVhJdlNiRHBvejd0UnlSNFJfTFA4dXAxUk9fVi1RQ2h2VU1kd2FkSUoydEJheDVMNWRnYUdMa2RFcG8zcTROTl9ZX1lJQ0tRU1VZR2pkQjFRdEtkM0tpUUlOcXhsYTFGcGY5RHFQYWZyNkh6LXVCSmN0Y1J3WWc?oc=5) | NVIDIA Newsroom |
| S33 | news | 2026-09-14 | [NVIDIA Expands Open Source CUDA-Q Platform for Fault-Tolerant Quantum Computing - NVIDIA Newsroom](https://news.google.com/rss/articles/CBMitAFBVV95cUxPMjBPVXRfZFRUYmRtTUVFSXVfaUdHNTBFNjFONTkxWDhMMmUzRjBPcjdvRmNKbVNTLUxodExCS2RDZ1p2ZzhaaVM2ZTlFbUxmSnVfaWlaaTFnTzJHT09iMlZXTVRoTGxHNl9mS1NoZWJ1bDBPeXQyaFRUUEJyZGJJM3ZKOTZ1Nk03d3dnYk5YN3VFYm9RRnpYc0VabmUzb2lLZENBcUU2Z3B3ekd0YWtzcEtxRUg?oc=5) | NVIDIA Newsroom |
| S34 | news | 2026-10-14 | [NVIDIA Commits $250 Million to Advance UK Agentic Safety and Security Research Over the Next Five Years - NVIDIA Newsroom](https://news.google.com/rss/articles/CBMi0wFBVV95cUxObFZSeVlfYXk3T3JDamt0enRzU3UwYVpvSmlfcVlrdkJSbmtxSTg2eVR5bkRYNmlHVDdDeWtiVVBmYUdyajNSRWhwTkRxVTltaGVIVEg2VGJ2ZU5nb1RETW9jMnVFbWtNWF9OZUdSeGZnZ0FxNExYZVJzSlFtQ25tdVpSbmlYUlVYVC1LQW5DN01Lck9pNWNXdGlIOF90UVhERzBjMGtJVEVqUWJIb1Zsdm5OSkdPV0xmT1BaZ1h6M1NtNjdzYklhOUNudko0V2dxLXRn?oc=5) | NVIDIA Newsroom |
| S35 | news | 2026-08-26 | [AWS and NVIDIA to Deliver 2 Million Additional GPUs and Next-Generation Infrastructure for Agentic and Physical AI - NVIDIA Newsroom](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNZUNocGNzT2FJb01QNmVWTHpoSXkxUUNVdlRDTVZET3hZZVBDN0JGTVBTUFF5aEdERTJOcU9LeV9VMW12ZlZSck5uQ194MjFmYVlMWGt1SzdVODFjY2hkV2RFamlFdzVaWkNYNUdnbXcxbF9rTGJwY005LTlwN1BtUDdTWDVaMk1kejdPRzJKaVRTUVB4X3FWVnVlNnNPcUxUZGNHSzNTV0liVVJaNTMwdEdYcENaOFVtZVc5TXFIY0xsUlZJZUg2bkJKVnJ2OUhqSVg3bDZrQTd3eWdTVmNvMlJkcw?oc=5) | NVIDIA Newsroom |
| S36 | news | 2026-10-08 | [NVIDIA Commits $1 Billion to Advance US Science Over the Next Five Years - NVIDIA Newsroom](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOWV9LdlNrOEhZeWpWaHNwSUlhSllPWFo3Y05sckNRbXBIeVZ5NElkNDdJbHlOR0pvZHRfRk9CMEI3U0xmNlU5RndtMkx3TWFRVk5oLWxIRktoeS0wMGxZMEpkN2hEVWZQa0JuWk85RUpZRVAxVGkwdnkxa1dxR0cxdFdXVlpQQUk3dGYzM21IVDdwZjJCNjFPamRib2FfdHhsWF9Ma2VFNVZmUQ?oc=5) | NVIDIA Newsroom |
| S37 | news | 2026-07-27 | [Industry Leaders Unite in Open Secure AI Alliance for AI Safety and Security - NVIDIA Blog](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1jbERSYTYzMDlvaExvNHBYWTZrU2Zfd210S2U0NHAyMDBqWG5DS0hkenZPaUgxVDcxcEtPUUhrbVhObUpvQzV2b0VKSzRjOF9sMW9WdW03ZVhyUC1TaG5XVGdHS3Q?oc=5) | NVIDIA Blog |
| S38 | news | 2026-09-28 | [NVIDIA Announces a $150 Billion Share Repurchase Authorization Increase - NVIDIA Newsroom](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPR0Vsb0ZuR3F0Sl9oYldFNF90azJObUVsNkJIb0VCWVJxWDRmRmdyR2swZE90ZkxwRGJERXBveVRvX040RUJMLU9Tc3lIbm44R2lzMzcxZHVYRkZmS0lGRWhHMDF4azNCakJHSk00UU1KdEhzNzVrYVd1SVpnNDZyZkV4bWVNVHY3cC1fSlpUSm1BTnZTdS1Vak5LOXB2NkF5X0VnZFhFR1A?oc=5) | NVIDIA Newsroom |
| S39 | news | 2026-09-28 | [NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring \\| NVIDIA Technical Blog - NVIDIA Developer](https://news.google.com/rss/articles/CBMiwAFBVV95cUxPVFg4WTJZY1lxdDNpSXJJZnFsTFlidFZlM2VOd3NSY0VFR2Mzc3hxaFNla3V2bklFdms1U0NSM05pQzROVk1obUEtXy0xVXh6d3RCTncyaFlldjh3WmpQeHE5Q2pOQnZuaDNpbS1jMkh3eHU5dHRpbk5OYVhvaVBQVk1BWXAzNFBfUGN5TmlyMmVhTWE2SWtLQzk4Znd0S0hHQXY1MklHV2JoQWItQkg1VHFJTV9odmxCYTg4cXVsNjI?oc=5) | NVIDIA Developer |
| S40 | news | 2026-08-17 | [NVIDIA Guarantees SB Energy’s PORTS-Pike Technology Campus in Ohio to Exclusively Host NVIDIA AI Compute - NVIDIA Newsroom](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNYXdyMXl0ZUs3UDVBSFo1a3BCcDg4UlZUazQxSEp1allrY1B3SEVxYnQ2RjFQVFY5T3Q1YUFYM19Jc1ZQNXVobGtZNVJBc1BPQXpFWFFsTlBvWEJqV3VRM1lCU0ZzSVlHcS14UGxUZldBaEVsdUJveHN0TXJOLURfWDBxRlJYaFdXMHREU3VSNlVrcFZncENub1czY2lGV1F6eGpGSWZiU2loYlJYVVRFZTdQSU80Q0lNZmdvX3FZQ0hTU1pjZF8weHhCRWEzeURkcDk3N1Z3?oc=5) | NVIDIA Newsroom |
| S42 | news | 2026-10-13 | [NVIDIA Announces New Investments in France’s Startups - NVIDIA Blog](https://news.google.com/rss/articles/CBMic0FVX3lxTFBTRGZFbUlVZjJzY1M2ZGVVc3hubnlhYmNTTlJCWk5xdWJBeENiZzN2RGRfZ2U5d21tMjNVV0xKcFFSMm5BWDFydDhjT0o1NFBGQlc5aWlEcG5kMUlNY1pNS2J1UGhJaGlwbmhkaTFnYmtoNEE?oc=5) | NVIDIA Blog |
| S44 | news | 2026-08-26 | [NVIDIA NVLink Fusion Brings NVHBM to Next-Generation AI Infrastructure \\| NVIDIA Technical Blog - NVIDIA Developer](https://news.google.com/rss/articles/CBMiqAFBVV95cUxQWEEwcE9ISjdxZmlzWXJiaXFEWTNmeEVCX3R0NU1Qa2ZONThvZ21DTDAwVmIyOUVJRHBLd1ZHeE5lWmROekVqTUdMQ2ExS0JpRVhwQmxSTWpFMGFTTW5yZ3g3NFRjTEc5U1AzU1Bmc01SemFlVHRzNFhOTzlRbDBnMWNpal91ZXNNT3RHYkNkVE9oZC1qOHRZcFpqbWVmbDIyMjdjMGI5MWc?oc=5) | NVIDIA Developer |
| S45 | data | 2026-10-16 | [NVIDIA (NVDA) Stock Price & Overview](https://stockanalysis.com/stocks/nvda/) | 2026-10-16 정규장 종가 214.13달러, 전일 종가 217.23달러 대비 -1.43%. 52주 범위 164.27~243.37달러. Yahoo Finance도 같은 값. 다른 사이트는 217.09달러, 215.11달러로 달랐고 더 많은 곳이 일치한 214.13달러를 썼다. |
| S46 | news | 2026-08-27 | [Nvidia Blows Past Expectations with $96.2 Billion Revenue in Q2 2027](https://www.iphoneincanada.ca/2026/08/27/nvidia-blows-past-expectations-with-96-2-billion-revenue-in-q2-2027/) | 보도. 2분기(FY2027Q2) 매출 약 962억 달러, 전년 대비 +106%. 데이터센터 890억 달러. 3분기 매출 가이던스 1,080억 달러 ±2%, 총이익률 74.0% ±0.5%p. 컨센서스는 약 1,040억 달러(출처마다 1,039~1,046억 달러). 가이던스는 중국 데이터센터 컴퓨트 매출을 제외한다. |
| S47 | news | 2026-08-27 | [NVIDIA's Q2 FY2027: The Guide and the Margin Are the Story, Not the Beat](https://fourweekmba.com/ai-nvidia-q2-fy2027-guide-margin-memory-tax/) | 보도. 2분기 총이익률 75.0%. 3분기 총이익률 가이던스 하락 원인은 부품·메모리 비용 상승. 경영진은 FY2028 매출 성장률을 약 70%로 전망했고 수요가 아니라 공급이 한도라고 밝혔다. 2차 요약이라 원문 대조가 필요하다. |

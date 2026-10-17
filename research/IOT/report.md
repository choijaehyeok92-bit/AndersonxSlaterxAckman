# Samsara (IOT) 리서치 보고서 — 기준일 2026-10-18

**반대 우세** — 찬성 0 · 반대 2 · 보류 1 · 확신 가중 점수 -0.40 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장 내재: 매출 10년 연 24.4% (FCF 마진 18% 수렴 가정) · 기본 시나리오: 5년 연 20.3%
- 시장이 반영한 것: 현재 EV(C:ev)는 FCF 마진 20% 도달 시 10년간 연 23%의 매출 성장을 요구한다(C:implied_cagr@m20). 단기 지표는 강하다: Q2 실적 상회와 FY2027 가이던스 상향(F213)이 컨센서스(F216, F217)보다 높고 애널리스트 목표가도 올랐다(S39).
- 우리가 다르게 보는 점: 단기 매출은 컨센서스보다 강하다는 데 동의한다. 그러나 가격이 요구하는 것은 단기 상회가 아니라 10년 가까운 높은 성장 지속이며, 우리 기본 시나리오는 성장이 매년 둔화해 5년 뒤 15%까지 내려간다고 본다. 또 보고 FCF는 SBC를 비용으로 보지 않은 값이어서(C:sbc_to_ocf, C:fcf_after_sbc@FY2026) FCF 수익률(C:fcf_yield)은 주주 몫을 과대 표시한다.
- 왜 우리가 맞는가: 매출 성장은 FY2023부터 FY2026까지 매년 둔화했고(C:revenue_growth@FY2023, C:revenue_growth@FY2026), 순신규 ARR 증가율(F210)은 이미 ARR 증가율(F209)보다 낮다. 경영진도 FY2027 FCF 마진이 낮아질 것이라 밝혔다(S50). 희석은 연 3% 이상이다(C:dilution). [C:implied_cagr@m20] [C:ev] [F213] [F216] [F217] [F209] [F210] [C:sbc_to_ocf] [C:fcf_after_sbc@FY2026] [C:dilution] [S39](https://www.itiger.com/news/2664435814) [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw)
- 촉매: 분기 순신규 ARR의 전년 대비 증가율, 대형 고객 순증 지속 여부, SBC 비중 추이, FY2028 가이던스 발표.
- 시점: FY2027 Q3 실적(2026년 12월경)부터 FY2027 연간 결과와 FY2028 가이던스(2027년 3월경)까지.
- 컨센서스 대비 revenue FY2027: +3.9% (20.5억 USD vs 19.7억 USD)
- 컨센서스 대비 revenue FY2027: +1.9% (20.5억 USD vs 20.1억 USD)

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **22.96** vs 주가 39.57 · 기대 연 수익률 **-1.3%** · 손실 확률 80%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 30% | 10.15 | 6.30 | -23.8% | FY2027 가이던스(F213)까지는 달성하지만 순신규 ARR 증가율이 ARR 증가율보다 낮은 흐름(F210, F209)이 이어져 대형 고객 확장이 식는다. IoT 기기 투자와 공급망 비용으로 FCF 마진이 FY20 |
| 기본 | 50% | 38.41 | 23.85 | -0.6% | 첫해는 가이던스 상향(F213)과 컨센서스 대비 상회(F216, F217)를 반영한다. 이후는 ARR $100K 이상 고객 확장(F212, F211)이 전체 성장보다 빠르게 이어지되 매출 성장률은 FY2023~FY2 |
| 강세 | 20% | 73.63 | 45.72 | +13.2% | 대형 고객 ARR이 전체보다 빠르게 늘어나는 흐름(F212, F229, F230)이 연료·안전·정비 등 신규 제품으로 확대되어 성장 감속이 느려진다. 기기 투자가 구독 매출로 회수되면서 총이익률(C:gross_mar |

## 3. 반증 조건 (thesis break)

- [자료 없음] 앤더슨: FY2027Q3 순신규 ARR이 1억 달러 미만이면 성장 가설이 훼손된다 — `net_new_arr < 1e+08` (FY2027Q3)
- [자료 없음] 앤더슨: ARR $100K 이상 고객 수가 줄면 대형 고객 확장 가설이 깨진다 — `customers_over_100k_arr < 3605` (FY2027Q3)
- [수동 확인] 앤더슨: 다음 분기 이후 가이던스가 매출 성장 감속을 한 자릿수 후반으로 반영하면 수동 확인
- [자료 없음] 슬레이터: 다음 분기 ARR이 22억 달러 미만이면 순신규 ARR 둔화가 가속된 것 — `arr < 2.2e+09` (FY2027Q3)
- [자료 없음] 슬레이터: GAAP 영업이익이 다시 적자로 돌아서면 SBC가 영업 레버리지를 지운 것 — `operating_income < 0` (FY2027Q3)
- [수동 확인] 슬레이터: 외부 조달(증자·차입)이 필요해지는 징후 — 수동 확인
- [미충족] 애크먼: 주가가 기본 시나리오 현재가치 수준 아래로 내려오면 가격 근거가 바뀐다 — `price < 25`
- [자료 없음] 애크먼: FY2027 Q3 매출이 가이던스를 크게 웃돌아 성장 감속 가정이 흔들린다 — `revenue >= 5.3e+08` (FY2027Q3)
- [수동 확인] 애크먼: SBC 차감 FCF가 양수로 전환되면 현금 창출 전제를 다시 평가 — 수동 확인
- [미충족] 레드팀: 분기 순신규 ARR이 FY27 Q2의 $134.1M 아래로 내려감 — 신규 유입 감속이 ARR 성장보다 먼저 가시화 — `net_new_arr < 1.341e+08`
- [미충족] 레드팀: 분기 SBC가 1억 USD 초과 — 희석·비용 압력이 개선 추세를 꺾음 — `sbc > 1e+08`
- [미충족] 레드팀: 재고가 6,000만 USD를 넘음 — 기기 선투자가 매출로 회수되지 않고 쌓이는 중 — `inventory > 6e+07`
- [미충족] 레드팀: ARR $100K 이상 고객 순증이 242곳 미만 — 대형 고객 확장 둔화가 시작됨 — `customers_over_100k_arr_net_adds < 242`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | revenue | FY2027Q3 | >= 5.15e+08 | 85% | 가이던스 상단(F214) 이상인지로 회사가 가이던스를 보수적으로 내는지 시험한다. |
| K2 | revenue | FY2027 | >= 2.05e+09 | 65% | FY2027 가이던스 상단(F213)을 넘는지로 기본 시나리오 1년차 성장을 시험한다. |
| K3 | arr | FY2027Q3 | >= 2.24e+09 | 60% | ARR(F209)에 순신규 ARR 약 1.15억을 더한 값으로 성장 감속 속도를 시험한다. |
| K4 | operating_income | FY2027Q3 | > 0 | 60% | GAAP 영업이익 흑자 유지(F127)로 SBC 증가가 영업 레버리지를 지우지 않는지 시험한다. |
| K5 | sbc | FY2027Q3 | <= 1e+08 | 55% | 분기 SBC가 Q2(F177)보다 더 뛰지 않는지로 희석 우려를 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.40 · 비중 참고값 0.0% (반대 우세 — 신규 비중 없음) · 슬레이터 시작 비중 0.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 반대 → 반대 | 2/5 | ✗ 10년 주당가치 5배 미만 또는 계산 불가 (LTGG Q10) | 0/5 실패 | founder_led=예, upside_10y=3.92x, revenue_5y=2.81x |
| 슬레이터 | 보류 → 보류 | 2/5 | ✓ | 1/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=0.0%, cash_survives=예, cash_min=2.9억 USD |
| 애크먼 | 반대 → 반대 | 4/5 | ✗ 안전마진 20% 미만 또는 계산 불가 | 0/5 실패 | simple_predictable=예, capital_markets_dependent=아니오, catalyst=없음, fcf_positive=예, net_debt_to_ebitda=-5.92x, intrinsic_value=23.8, mos=-65.9% |

- ⚠ 앤더슨: rebuttals[0]: 인용하지 않은 근거의 숫자 32(C:exit_multiple@base), 18%(C:fcf_margin@base·C:implied_cagr@m30) — cites에 추가
- ⚠ 앤더슨: arguments[3]: 인용하지 않은 근거의 숫자 18%(C:fcf_margin@base·C:implied_cagr@m30) — cites에 추가
- ⚠ 앤더슨: rebuttals[2]: 인용하지 않은 근거의 숫자 28%(S40) — cites에 추가
- ⚠ 슬레이터: arguments[1] unsupported: 현금과 FCF 마진은 맞지만, '부채 없음'과 '기본 시나리오 현금 경로가 0 아래로 가지 않는다'는 인용에 없다.
- ⚠ 슬레이터: rebuttals[2] unsupported: 출처 없는 숫자 6e+07 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 슬레이터: arguments[3]: 인용하지 않은 근거의 숫자 18%(C:fcf_margin@base·C:implied_cagr@m30) — cites에 추가
- ⚠ 애크먼: rebuttals[2] unsupported: 출처 없는 숫자 7500, 5.5%, 60% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: arguments[3]: 인용하지 않은 근거의 숫자 18%(C:fcf_margin@base·C:implied_cagr@m30) — cites에 추가
- ⚠ 애크먼: rebuttals[2]: 인용하지 않은 근거의 숫자 32(C:exit_multiple@base), 18%(C:fcf_margin@base·C:implied_cagr@m30), 65.9%(C:mos@ackman) — cites에 추가
- ⚠ 모델이 컨센서스와 사실상 같다 — variant perception이 없다면 알파도 없다
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 레드팀 premortem[0] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base
- ⚠ 경영진·자본배분 findings[1] 검증 실패(unsupported): 인용 없음
- ⚠ 레드팀 weakest[0] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base
- ⚠ 레드팀 premortem[1]: 인용하지 않은 근거의 숫자 91(C:p_fcf) — cites에 추가
- ⚠ 레드팀 weakest[1] 검증 실패(unsupported): FCF 마진 12.8%, SBC 차감 FCF 음수, 경영진의 100bp 하락 발언, 분기 SBC는 맞지만, '이 마진 가정이 가치의 절반을 결정한다'는 인용에 근거가 없다.
- ⚠ 사업·산업 findings[0] 검증 실패(unsupported): 양 끝값(70.9%, 76.7%)은 맞지만, FY2023~FY2025 중간값(72.0%, 73.6%, 76.1%)과 '매년 상승'은 인용에 없고 S9는 내용이 비어 있다.
- ⚠ 회계 품질 flags[1] 검증 실패(unsupported): 출처 없는 숫자 100% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 레드팀 weakest[2] 검증 실패(contradicted): 52.3%→29.6%는 3년간 약 22.7%p, 연 약 7.6%p 하락이라 '연 10%p 이상'과 다르다.
- ⚠ 사업·산업 moat[2] 검증 실패(unsupported): 인용한 S27·S23에는 기기·데이터가 AI 기능을 개선한다는 회사 측 논리가 드러나지 않는다(제목과 출처만 있음).
- ⚠ 레드팀 premortem[3]: 인용하지 않은 근거의 숫자 38%(S40) — cites에 추가
- ⚠ 사업·산업 findings[5]: 인용하지 않은 근거의 숫자 20%(C:implied_cagr@m25·C:p@bull·C:revenue_cagr@base) — cites에 추가

## 앤더슨 — 반대 (2/5)

> Samsara는 앤더슨이 찾는 종류의 회사다. 물리 세계의 운영 데이터를 플랫폼으로 묶고, 대형 고객 중심으로 확장하며, 적자에서 현금 창출로 넘어왔다. 창업자형 경영진이 이끈다는 점도 맞다(다만 이 근거 묶음에서는 확인하지 못했다). 문제는 가격이다. 현재 EV가 요구하는 성장은 기본 시나리오 수준의 연 24.4%를 10년 지속하는 것이고, 내가 가장 낙관적으로 잡은 강세 가정으로도 10년 뒤 주당 가치가 현재 주가의 5배에 닿지 않는다. 확률 가중 기대 연 수익률은 -1.3%, 손실 확률은 80%다. 앤더슨의 질문 10번, 즉 5배가 되는 길이 보이느냐에 코드가 아니라고 답한다. 성장 가설이 훼손된 것은 아니다. 매수할 가격이 아닐 뿐이다. 이 회사를 지켜보되, 성장 가설을 더 키워 줄 증거(순신규 ARR 가속, 대형 고객 확장의 제품 다변화)가 나오기 전에는 대담함이 아니라 값을 치르는 쪽에 가깝다.

*이전 판단 대비: 직전 판단과 같은 입장(반대, 확신 2)이다. 새 근거 없이 바뀐 것이 없고, 가격(F218)과 기대 수익률(C:expected_irr)이 여전히 5배 시나리오를 뒷받침하지 못한다.*

**논거**
- 성장 둔화에도 매출 성장률이 안정적이다. FY2026 매출 성장률은 29.6%이고 종료 ARR도 30% 늘었다. 5년 매출 2배(질문 1)는 성장이 한 자릿수 후반까지 떨어지지 않는 한 현실적이다. [C:revenue_growth@FY2026] [F209] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- 확장은 대형 고객에서 일어나고 있다. ARR $100K 이상 고객의 ARR이 38% 늘어 전체 ARR 증가율 30%보다 빠르다. 고객이 플랫폼에 더 많은 업무를 얹고 있다는 신호이고, 이것이 이 회사의 멱법칙 경로다. 다만 순매출유지율 같은 직접 증거는 없다. [F211] [F212] [F229] [F230] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw)
- 마진 개선 여지(질문 6, 7)는 실제로 진행 중이다. 영업이익률이 -82.6%에서 -3.2%로 올랐고 FCF 마진은 12.8%다. 총이익률은 76.7%다. [C:operating_margin@FY2022] [C:operating_margin@FY2026] [C:fcf_margin@FY2026] [C:gross_margin@FY2026]
- 시장이 이 기회를 과소평가하지 않는다(질문 9). 역DCF상 FCF 마진 18% 도달을 가정해도 연 24.4%의 매출 성장을 10년 지속해야 현재 EV가 정당화된다. 시장은 이미 강한 성장 지속을 가격에 넣었다. [C:implied_cagr@m18] [C:implied_cagr@m20] [C:ev]
- 시나리오 분포가 비대칭을 주지 않는다(질문 10). 확률 가중 기대 연 수익률은 -1.3%이고 손실 확률은 80%다. 상방이 열려 있어도 현재 가격에서는 그 상방에 닿는 확률이 낮다. 비대칭의 이점은 사는 가격에서 나온다. [C:expected_irr] [C:p_loss]

**사전 부검**
- 사전 부검 — 내가 틀렸다면, 대형 고객 확장이 제품 다변화(연료·안전·정비)로 이어져 성장 감속이 예상보다 훨씬 느렸고 그 결과 10년 뒤 규모가 내 강세 가정을 넘어선 경우다. 이때는 가격이 비싸 보였던 것이 실수가 된다. [F212] [F229] [S23](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNU1QyWk9pdjBfLXZIaXRCVGlwY1kwSFB2ZTBXUHkwczlnWUZpWGpBT3A5bUJBb251dkxTZERBX3ZrdEs5dDBXeXYwYjJ4WGVoRXF1V1BieV9fTExDZVJKbnFMYU9Zd18xUmoyb0ZJdV9KT2hNYUpzbTFPUndnaHBvN2dNWUFqRG5rRWo4OEJpM1VDVmRKeFJhUnp4bXBlZERIUVBBS2VIbjhFemlYT1ZKSXotMmpmejcwQlhxVF8tUC1IRnhCMTZ6bWt2RVBhcTZtS0lPMHhRdUZXMFRL?oc=5)
- 사전 부검 — 순신규 ARR 증가율(28%)이 ARR 증가율(30%)보다 이미 낮다. 반대로 내가 너무 낙관적이었다면 이 감속이 가속되어 성장 가설 자체가 깨진 경우다. 경로의 소음이 아니라 신규 유입의 구조적 둔화일 수 있다. [F210] [F209] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- 사전 부검 — SBC가 매출의 19.5%이고 희석이 연 3.7%여서, 주당 가치는 매출 성장보다 느리게 늘어난다. 창업자 정렬을 확인할 DEF 14A·내부자 자료도 수집되지 않아 시간 지평의 근거가 비어 있다. [C:sbc_to_revenue] [C:dilution] [S6](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039492/iot-20260601.htm)

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 안전마진 -65.9%와 기대수익률 -1.3%다. 가격 규율 자체는 인정한다. 다만 그의 내재가치는 5년 출구 멀티플 32배와 FCF 마진 18%라는 기본 시나리오에 묶여 있어, 10년 뒤 규모를 재지 못하는 도구라는 한계가 있다. 내가 반대하는 이유는 그 계산이 아니라 내 강세 case로도 10년 뒤 주당 가치가 주가의 5배에 닿지 않기 때문이다. 성장 가설은 훼손되지 않았고, 값이 비쌀 뿐이다. [C:mos@ackman] [C:expected_irr] [C:irr@bull]
- → 슬레이터: 슬레이터의 가장 강한 논거는 순매출유지율·CAC 회수기간 같은 단위경제 증거가 없다는 점이다. 이 공백은 인정한다. 그러나 증거가 쌓이길 기다리는 것만으로는 멱법칙 구간을 놓칠 수 있다. 대형 고객 ARR이 +38%로 전체 +30%보다 빠르다는 흔적은 이미 있다. 내가 지금 담지 않는 이유는 증거 부족이 아니라 가격이 5배 시나리오를 뒷받침하지 못하기 때문이다. [F212] [F209] [F210] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- → 레드팀: 레드팀의 첫째 부검(성장 감속과 멀티플 압축 동시 발생)은 성장 가설을 깨는 시나리오가 아니라 가격에 내장된 위험이다. 순신규 ARR 증가율(28%)이 ARR 증가율(30%)보다 낮은 것은 경로의 소음일 수도, 구조적 둔화의 시작일 수도 있다. 이를 가르는 것은 다음 분기 순신규 ARR이다. 둘째 부검의 SBC는 창업자 정렬과 희석 문제로 주당 가치에 직접 영향을 주므로 가볍게 보지 않는다. [F209] [F210] [C:dilution] [C:sbc_to_ocf]

**인정한 점**
- 애크먼의 지적대로 확률 가중 기대 연 수익률이 -1.3%이고 손실 확률이 80%여서, 현재 가격은 비대칭 이점을 주지 않는다. 입장은 유지한다.
- 슬레이터의 지적대로 순매출유지율과 CAC 회수기간이 근거에 없어 해자가 '주장' 수준이다. 확신은 올리지 않는다.
- 레드팀이 지적한 SBC의 주주 몫 잠식과 희석은 10년 주당 가치를 깎는다. 성장이 이어져도 주당 가치 증가는 그보다 느리다.


## 슬레이터 — 보류 (2/5)

> 시장의 천장은 아직 보이지 않고 성장도 이어지고 있지만, 지금 가격에 담을 만큼 증거가 쌓이지는 않았다. 대형 고객 확장이 전체 성장보다 빠르고(F212, F211), 부채 없이 FCF가 흑자라서 외부 자본 없이 계획을 실행할 수 있다(C:fcf_margin@FY2026, F20). 반면 단위경제의 핵심인 순매출유지율, CAC 회수기간, 이탈률은 근거에 없다. 순신규 ARR 증가율은 이미 ARR 증가율보다 낮다(F210, F209). 코드가 계산한 기본 시나리오는 연 수익률이 마이너스이고 확률 가중 기대 수익률도 마이너스다(C:expected_irr). 가설이 깨진 것은 아니지만 입증된 것도 아니므로 지금은 시작 비중을 정당화하기 어렵다. 다음 분기 ARR, GAAP 영업이익, SBC로 확인하며 지켜본다.

**논거**
- 기회의 크기와 지속성에 대한 흔적은 좋다. ARR $100K 이상 고객은 3,605곳이고 분기 순증이 242곳이며, 이 고객군 ARR은 +38%로 전체 ARR +30%보다 빠르다. 다만 출처가 2차 요약이어서 원문 확인 전까지는 '주장' 수준이다. [F211] [F229] [F212] [F209] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw)
- 생존 경로는 막혀 있지 않다. 부채가 없고 현금이 2.9억 USD이며 FY2026 FCF 마진이 12.8%로 흑자다. 코드가 계산한 기본 시나리오 현금 경로도 0 아래로 내려가지 않는다. 2022년의 교훈인 외부 자본 의존 문제는 이 회사에는 해당하지 않는다. [F20] [C:fcf_margin@FY2026] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- 단위경제는 증명되지 않았다. 순신규 ARR 증가율(+28%)이 ARR 증가율(+30%)보다 낮아 신규 유입 모멘텀이 ARR 성장보다 느리다. 순매출유지율과 CAC 회수기간이 없어 기존 고객 확장과 신규 유입의 비중을 가를 수 없다. 개선 추세는 있어도 입증은 아직이다. [F210] [F209] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- 가격이 요구하는 것이 크다. 역DCF상 현재 EV는 FCF 마진 18% 도달 시 10년간 연 24.4%의 매출 성장을 요구한다. 코드 계산의 확률 가중 기대 연 수익률은 -1.3%이고 손실 확률은 80%다. 사업이 좋아도 증거 수준에 비해 시작 비중을 줄 만한 가격이 아니다. [C:implied_cagr] [C:expected_irr] [C:p_loss]
- 영업 레버리지가 증거로 굳지 않았다. GAAP 영업이익은 FY2027Q1 720만에서 Q2 488만으로 줄었고 같은 기간 SBC는 7,747만에서 9,638만으로 뛰었다. 이익이 늘 때 키운다는 원칙에 비춰 아직 키울 단계가 아니다. [F126] [F127] [F176] [F177]

**사전 부검**
- 사전 부검: SBC 부담이 줄지 않으면 보고 FCF는 주주 몫을 과대 표시한다. SBC가 영업현금흐름의 133.3%이고 희석이 연 3.7%여서, 사업이 성장해도 주당 가치는 기대만큼 늘지 않았을 수 있다. [C:sbc_to_ocf] [C:dilution] [C:fcf_after_sbc@FY2026]
- 사전 부검: 성장 감속이 예상보다 빨랐을 수 있다. 매출 성장률은 이미 FY2023 52.3%에서 FY2026 29.6%로 내려왔고, 순신규 ARR 증가율도 ARR 증가율보다 낮다. 감속이 이어지면 출구 멀티플 압축과 겹쳐 기본 시나리오도 손실로 끝난다. [C:revenue_growth@FY2023] [C:revenue_growth@FY2026] [F210] [F209]
- 사전 부검: 하드웨어 선투자가 구독 매출보다 먼저 현금을 쓰는 구조에서 회수가 늦어졌을 수 있다. 경영진이 FY27 FCF 마진 하락과 기기 투자·공급망 비용을 직접 언급했고 재고도 늘고 있다. 이 발언은 2차 요약이어서 원문 대조가 필요하다. [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw) [F100] [F95]

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 가격이다. 확률 가중 기대 연 수익률이 마이너스이고 손실 확률이 80%라는 점이다. 이 숫자에는 동의한다. 다만 반대 근거를 '5배가 안 된다'에 두면 약하다. 5배가 성립하려면 무엇이 참이어야 하는지를 물어야 한다. 순신규 ARR 증가율(28%)이 이미 ARR 증가율(30%)보다 낮은 지금은, 그 감속이 멈춘다는 증거가 아직 없다. 그래서 나는 반대가 아니라 보류로 두고 다음 분기 순신규 ARR로 가설을 확인한다. 상방이 큰 것과 지금 시작 비중을 줄 만한 것은 다른 문제다. [C:expected_irr] [C:p_loss] [F210] [F209] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- → 애크먼: 애크먼의 안전마진 계산은 기본 시나리오의 출구 멀티플 축소에 크게 기대고 있다. 같은 시나리오에서 사업 자체(매출 성장과 마진 개선)는 수익률에 플러스로 기여한다. 손실은 사업이 나빠져서가 아니라 멀티플이 내려와서 생긴다. 그 점에서 '비싸게 산 좋은 회사'라는 진단은 맞고, '사업이 나쁘다'로 읽으면 틀린다. 또 가격만 보고 촉매가 없다고 하지만, 생존 경로는 막혀 있지 않다. 부채가 없고 현금이 쌓이며 순부채/EBITDA가 음수라서 외부 자본에 기대지 않고 계획을 실행한다. 이런 회사는 반대로 확정하지 않고 증거가 쌓이는 동안 지켜보는 쪽이 낫다. [C:irr@base] [C:expected_irr] [C:net_debt_to_ebitda] [F20] [C:fcf_margin@FY2026]
- → 레드팀: 레드팀이 고른 가장 강한 부검은 성장 감속과 멀티플 압축이 같이 오는 경로다. 인정한다. 그 선행 신호인 분기 순신규 ARR이 직전 분기 값 아래로 내려가는 것을 must_be_true에 넣겠다. SBC가 1억을 넘는 신호는 내 목록에 이미 있다. 반면 재고가 6,000만을 넘는 신호는 아직 기기 투자와 구분되지 않는다. 재고 증가는 경영진이 밝힌 기기 투자 확대와 방향이 같으므로, 재고만으로는 훼손 신호가 아니라 관찰 항목으로 둔다. [F210] [F177] [F100] [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw)

**참이어야 하는 것**
- [on_track] ARR이 순신규 ARR 둔화 없이 다음 분기에도 이어진다
- [at_risk] 분기 순신규 ARR이 직전 분기 수준을 지킨다
- [at_risk] GAAP 영업이익이 SBC 증가에도 흑자를 유지한다
- [on_track] ARR $100K 이상 고객이 계속 늘어난다
- [at_risk] 분기 SBC가 1억 USD를 넘지 않는다

**인정한 점**
- 앤더슨과 애크먼 모두 가격이 증거 수준에 비해 높다고 본다. 이 점이 옳아서 시작 비중은 0으로 유지한다.
- 레드팀의 순신규 ARR 신호를 인정해 must_be_true에 추가했다. 이 조건이 깨지면 성장 지속성 가설이 약해진다.
- 단위경제 증거(순매출유지율·CAC 회수기간)가 비어 있다는 애크먼과 앤더슨의 지적을 받아들인다. 이 증거가 나오기 전에는 찬성으로 옮기지 않는다.


## 애크먼 — 반대 (4/5)

> 사업은 한 문단으로 설명된다. 차량·장비에 IoT 기기를 설치하고 클라우드 구독으로 반복 매출을 받는 구조이고, 부채가 없으며 현금이 쌓이고 총이익률도 올랐다. 그러나 가격이 문제다. 기본 시나리오의 현재가치는 주가에 크게 못 미쳐 안전마진이 큰 음수이고, 확률 가중 기대수익률도 마이너스다. FCF 수익률은 1%대이며 그마저 SBC를 비용으로 보지 않은 값이다. 좋은 회사를 비싸게 사면 나쁜 투자다. 격차를 좁힐 촉매(자사주, 분사, 비용 구조 개편)도 보이지 않고, 오히려 희석이 계속된다. 주가가 내재가치 수준으로 내려오기 전에는 담지 않는다.

**논거**
- 가격: 기본 시나리오 내재가치가 주가를 크게 밑돌아 안전마진이 -65.9%다. 요구하는 안전마진에 한참 못 미친다. [C:intrinsic_value@ackman] [C:price] [C:mos@ackman]
- 현금 수익률: FCF 수익률은 1.1%이고 P/FCF는 91.45배다. 게다가 SBC 차감 FCF는 FY2026에도 음수여서 주주 몫은 보고 FCF보다 작다. [C:fcf_yield] [C:p_fcf] [C:fcf_after_sbc@FY2026]
- 기대수익: 확률 가중 기대 연 수익률이 -1.3%이고 손실 확률이 80%다. 기본 시나리오조차 연 -0.6%로 멀티플 축소가 성장을 상쇄한다. 강세 시나리오에서만 연 13.2%다. [C:expected_irr] [C:p_loss] [C:irr@base] [C:irr@bull]
- 시장 내재 기대: 현재 EV는 FCF 마진 18% 도달 시 10년간 연 24.4%의 매출 성장을 요구한다. 매출 성장은 FY2023 52.3%에서 FY2026 29.6%로 매년 둔화했고, 순신규 ARR 증가율도 ARR 증가율보다 낮다. [C:implied_cagr@m18] [C:revenue_growth@FY2023] [C:revenue_growth@FY2026] [F209] [F210]
- 사업의 질은 인정한다. 총이익률 76.7%, 부채 없음, 순부채/EBITDA -5.92배로 자본시장 의존이 없다. 그러나 이것은 필요조건이다. 해자 증거는 순매출유지율 같은 직접 증거 없이 대형 고객 흔적에 머문다. [C:gross_margin@FY2026] [C:net_debt_to_ebitda] [F211] [F212] [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw)

**사전 부검**
- 사전 부검: 내 판단이 틀린다면 대형 고객 확장이 새 제품으로 이어져 성장 감속이 느려지고 SBC 비중이 계속 내려 FCF 마진이 강세 가정까지 오르는 경우다. 그때 강세 시나리오 연 수익률이 현실이 되고 높은 멀티플도 유지된다. [C:irr@bull] [C:sbc_to_revenue@FY2026] [F229] [F230]
- 사전 부검: 기본 시나리오의 수익률 손실은 출구 멀티플 축소 가정에 크게 의존한다. 시장이 성장주 프리미엄을 유지하면 내 안전마진 계산이 지나치게 보수적일 수 있다. [C:irr@base] [C:implied_cagr@m18]
- 사전 부검: 가이던스 상향과 컨센서스 상회가 이어지면 단기 매출이 모델보다 강해 주가가 더 오를 수 있다. 가격 규율 때문에 상승분을 놓치는 비용이다. [F213] [F216] [F217] [S39](https://www.itiger.com/news/2664435814)

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 대형 고객 확장이 멱법칙 경로라는 것이다. 그러나 그는 강세 가정으로도 10년 뒤 5배에 못 닿는다고 스스로 인정했다. 그렇다면 같은 결론이지만 이유가 다르다. 나는 5배를 요구하지 않는다. 내재가치 대비 안전마진이 필요하다. 기본 시나리오 안전마진은 -65.9%이고, 확률 가중 기대 연 수익률은 -1.3%, 손실 확률은 80%다. 역DCF가 요구하는 연 24.4% 성장을 10년 지속하는 기업은 기저율 표가 없어 검증되지 않았다. 앤더슨이 말한 '성장 가설은 훼손되지 않았다'는 필요조건일 뿐 가격의 정당화가 아니다. [C:mos@ackman] [C:expected_irr] [C:p_loss] [C:implied_cagr@m18]
- → 슬레이터: 슬레이터의 가장 강한 논거는 생존 경로가 열려 있다는 것이다. 부채가 없고 현금 2.9억 USD, FCF 흑자라서 외부 자본 의존이 없다는 데 동의한다. 그러나 생존 경로와 단위경제는 필요조건이지 가격의 정당화가 아니다. 슬레이터 본인도 기본 시나리오 연 수익률이 마이너스라고 쓰고 보류에 머물렀다. 내 질문은 증거가 쌓이면 담겠느냐가 아니라, 증거가 모두 확인돼도 이 가격에서 수익이 나느냐다. 모든 must_be_true가 충족돼도 기본 시나리오 연 수익률은 -0.6%다. 보류가 아니라 반대가 맞다. [F20] [C:fcf_margin@FY2026] [C:irr@base] [C:expected_irr]
- → 레드팀: 레드팀의 가장 강한 논거는 기본 시나리오 출구 배수 32배와 FCF 마진 18% 가정이 낙관적이라는 것이다. 이는 내 안전마진을 더 악화시키는 방향이다. 민감도상 배수 ×0.75만 적용해도 기본 시나리오 수익률은 -5.5%이고, FCF 마진은 SBC 차감 후 여전히 음수라 범위가 더 넓어진다. 이미 -65.9%인 안전마진에 사전 부검의 하방이 더해지면 요구 마진 20%는 현재가보다 훨씬 낮은 가격에서야 충족된다. 다만 레드팀이 제시한 약세 -60%는 확률 15~20% 수준의 개별 경로여서 시나리오 가중 기대치에는 이미 반영되어 있다. 내 반대는 이 하방 없이도 성립한다. [C:irr@base] [C:fcf_margin@FY2026] [C:fcf_after_sbc@FY2026] [C:p_fcf]

**인정한 점**
- 앤더슨 지적대로 대형 고객 확장(ARR $100K 이상 고객 ARR +38%)이 제품 다변화로 이어지면 성장 감속이 예상보다 느려질 수 있다. 이 경우 강세 시나리오 연 13.2%가 현실이 되지만, 확률 20%이고 이 경우에도 요구수익률 10%를 소폭 넘는 수준이라 안전마진 요건을 충족하지는 못한다.
- 슬레이터가 옳게 짚은 대로 부채가 없고 FCF가 흑자여서 밸리언트형 자본시장 의존 위험은 없다. 반대는 사업 질이 아니라 전적으로 가격 때문이다.
- 레드팀이 지적한 대로 출구 배수 32배는 성장 15%의 기업에 대한 가정으로 근거가 약하다. 내 기본 시나리오 내재가치는 오히려 낙관적일 수 있다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Samsara는 차량·장비·현장 운영에 IoT 기기(카메라·게이트웨이·추적기)를 설치하고, 그 데이터를 클라우드 플랫폼(Connected Operations)의 구독으로 판매해 반복 매출(ARR)을 얻는다. 종료 ARR은 약 $2.125B(+30% YoY)이며(F209), 매출 성장은 FY2023 52%에서 FY2026 30%로 둔화하면서도 안정적이다(C:revenue_growth@FY2026). 총이익률은 FY2022 70.9%에서 FY2026 76.7%로 올랐고(C:gross_margin@FY2026), 영업이익률은 -82.6%에서 -3.2%로 개선되어 GAAP 기준 흑자 전환 직전~직후다(C:operating_margin@FY2026, F126, F127). 단위경제는 대형 고객 확대와 마진 개선으로 개선 중으로 보이나, 순매출유지율·CAC 회수기간·이탈률 같은 코호트 지표는 근거에서 확인되지 않았다. 선행 투자(재고·기기)와 SBC가 FCF의 질을 낮추는 점이 변수다.

- [unit_economics] 총이익률은 FY2022 70.9%, FY2023 72.0%, FY2024 73.6%, FY2025 76.1%, FY2026 76.7%로 매년 상승했다. 하드웨어를 함께 파는 모델에서 높은 수준이며, 구독 비중이 커지는 구조와 일치한다. [C:gross_margin@FY2022] [C:gross_margin@FY2026] [S9](https://www.sec.gov/Archives/edgar/data/1642896/000162828026018167/iot-20260131.htm)
- [unit_economics] 영업이익률이 -82.6%(FY2022)에서 -3.2%(FY2026)로 개선되었고, 분기 영업이익은 FY2026Q4부터 흑자(902만)였으나 FY2027Q1 720만, Q2 488만으로 다시 줄었다. 가이던스의 비GAAP 영업이익률은 FY27 21%다. GAAP과 비GAAP의 격차는 SBC(FY2027Q2 9,638만)가 대부분이다. [C:operating_margin@FY2022] [C:operating_margin@FY2026] [F203] [F126] [F127] [F215] [F177]
- [customers] ARR $100K 이상 고객은 3,605곳이고 분기 순증이 242곳, ARR $1M 이상 고객 순증이 20곳이다(둘 다 분기 최대로 소개됨). 이 고객군 ARR은 $1.3B로 +38% 증가해 전체 ARR 증가율보다 빠르며, 대형 고객 중심으로 확장 중임을 시사한다. 출처는 2차 요약이다. [F211] [F212] [F229] [F230] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw)
- [unit_economics] 순신규 ARR은 분기 $134.1M(+28%)이다. 순신규 ARR 증가율(+28%)이 ARR 증가율(+30%)보다 낮아 신규 유입 모멘텀이 ARR 성장보다 약간 느리다. 순매출유지율과 CAC 회수기간은 찾지 못해 신규와 기존 고객 확장의 비중을 가를 수 없다. [F210] [F209] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- [industry] Q2 매출 $508.4M가 추정 $483.3M을 웃돌았고, FY27 매출 가이던스가 $2.005~2.013B에서 $2.043~2.047B로 상향되었다. 상향 전 컨센서스($1.97B, 약 $2.01B)보다도 높다. 경쟁사 점유율이나 산업 규모 근거는 없어 산업 구조는 판단 보류다. [F213] [F216] [F217] [S39](https://www.itiger.com/news/2664435814) [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) [S41](https://tickflow.io/stock/IOT/forecast) [S42](https://earningswhispers.com/epsdetails/IOT/202607)
- [runway] 재투자 활주로: 매출 성장률이 FY2023 52%에서 FY2026 30%로 둔화하는 한편 FCF 마진은 -44.6%에서 12.8%로 올랐다. 역DCF상 현재 EV는 FCF 마진 20% 도달 시 연 23% 매출 성장을 10년 지속해야 정당화된다. 성장 둔화 속도가 핵심 변수다. [C:revenue_growth@FY2023] [C:revenue_growth@FY2026] [C:fcf_margin@FY2022] [C:fcf_margin@FY2026] [C:implied_cagr@m20]
- [unit_economics] 경영진은 FY27 FCF 마진이 FY26보다 약 100bp 낮아질 것이라 했고 이유로 IoT 기기 투자 확대와 공급망 비용을 들었다. 재고는 FY2026Q1 3,788만에서 FY2027Q2 5,703만으로 늘었다. 하드웨어 선투자가 구독 매출보다 먼저 현금을 쓰는 구조여서 하드웨어 마진과 투자 회수의 증거가 필요하다. 이 발언은 2차 요약이다. [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw) [F95] [F100]
- [unit_economics] SBC가 매출의 19.5%이고 영업현금흐름의 133.3%라서 SBC 차감 FCF는 FY2026에도 음수(-1.1억)다. 희석 주식 수는 연 3.7% 늘었다. 이 사업의 현금 창출이 주주에게 얼마나 남는지는 이 비용을 어떻게 보느냐에 크게 좌우된다. [C:sbc_to_revenue] [C:sbc_to_ocf] [C:fcf_after_sbc@FY2026] [C:dilution]
- [claimed] 기기 설치와 업무 워크플로(안전·정비·연료·규정 준수)에 통합되는 플랫폼이라 전환비용이 클 가능성이 있다. 흔적으로는 ARR $100K 이상 고객이 3,605곳이고 이 고객들의 ARR이 $1.3B(+38%)로 전체 성장(+30%)보다 빠르다. 다만 순매출유지율·이탈률 같은 직접 증거가 없고 출처가 2차 요약이다. [F211] [F212] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw)
- [claimed] 총이익률이 5년간 70.9%에서 76.7%로 올랐다. 규모와 데이터 축적에 따른 효과일 수 있으나 경쟁사 대비 마진 비교가 없어 해자라기보다 단위경제 개선의 흔적이다. [C:gross_margin@FY2022] [C:gross_margin@FY2026]
- [claimed] 기기·데이터가 늘수록 AI 기능과 벤치마킹이 좋아진다는 회사 측 논리가 있으나, 점유율·가격 인상 후 잔존 기록은 근거에 없다. 보도와 회사 발표 수준이다. [S27](https://news.google.com/rss/articles/CBMinAFBVV95cUxOR1U1Z2xJQTJONFkzVFp4Zm5NSjB1N3BzaVozbjg0RkkyYjhVZ2o2UHh3Q3RTUlJKRmhsWGt1UE1mWTR3NkMycm5lQmlzMFV5VHcyV0ZUcVBWRk1wS1NuSG92aF9UN1VYSUxPSnI3dWRudG1kZ1htRG9lc0lwT1hRMXNXVUtSaGlpOWJmck9fd2pBeGdNdUI5bjM0V1k?oc=5) [S23](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNU1QyWk9pdjBfLXZIaXRCVGlwY1kwSFB2ZTBXUHkwczlnWUZpWGpBT3A5bUJBb251dkxTZERBX3ZrdEs5dDBXeXYwYjJ4WGVoRXF1V1BieV9fTExDZVJKbnFMYU9Zd18xUmoyb0ZJdV9KT2hNYUpzbTFPUndnaHBvN2dNWUFqRG5rRWo4OEJpM1VDVmRKeFJhUnp4bXBlZERIUVBBS2VIbjhFemlYT1ZKSXotMmpmejcwQlhxVF8tUC1IRnhCMTZ6bWt2RVBhcTZtS0lPMHhRdUZXMFRL?oc=5)

### 경영진·자본배분 — mixed

경영진의 정렬 여부를 판단할 핵심 증거(DEF 14A 보상 지표, 내부자 매매, 과거 가이던스 이력)가 수집되지 않아 정렬도는 확정하지 못하고 mixed로 둔다. 확인되는 것은 세 가지다. 첫째, 운영 실적은 개선 중이다: 매출 성장은 둔화했지만(C:revenue_growth@FY2026 29.6%) 영업이익률은 -34.5%(FY2024)에서 -3.2%(FY2026)로 올랐고 FCF 마진은 12.8%(C:fcf_margin@FY2026)다. 둘째, 주식 보상 의존이 크다: SBC가 FCF를 훨씬 넘어 SBC 차감 FCF는 여전히 음수(C:fcf_after_sbc@FY2026)이고, SBC/OCF는 133.3%(C:sbc_to_ocf@FY2026)다. 셋째, 희석이 지속된다: 희석 주식 수가 연 3~4% 증가하고(C:share_change@FY2026 3.1%) 자사주 매입은 FY2022 이후 기록이 없다. 경영진은 FY27 FCF 마진이 FY26보다 약 100bp 낮아질 것이라 직접 밝혔는데, 이는 2차 요약에만 있어 원문 확인이 필요하다.

- [compensation] 근거 없음. DEF 14A(S6)가 목록에는 있으나 보상 연동 지표(장기 매출·FCF·ROIC 대 단기 EPS·조정 지표)와 베스팅 기간이 수집되지 않았다. 다만 SBC 규모는 매출의 19.5%(C:sbc_to_revenue@FY2026)로, FY2022 53.4%(C:sbc_to_revenue@FY2022)에서 꾸준히 내려왔다. [S6](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039492/iot-20260601.htm) [C:sbc_to_revenue@FY2026] [C:sbc_to_revenue@FY2022]
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도 자료를 찾지 못했다. 정렬 판단에서 가장 큰 공백이다. 
- [guidance] 가이던스 적중률은 계산되지 않았다(C:guidance_hit_rate 없음). 과거 분기 가이던스 이력이 수집되지 않았기 때문이다. 확인되는 것은 FY27 매출 가이던스가 상향된 점이다: Q2 발표 전 컨센서스 약 $2.01B(F217)에 비해 새 가이던스는 $2.043~2.047B(F213)다. 같은 기간 비GAAP 영업이익률 가이던스는 21%(F215)다. 신뢰도는 판단 불가. [F213] [F215] [F217] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) [S42](https://earningswhispers.com/epsdetails/IOT/202607)
- [guidance] 경영진은 FY27 FCF 마진이 FY26보다 약 100bp 낮을 것이라 했고 이유로 IoT 기기 투자 확대와 공급망 비용을 들었다. 불리한 전망을 스스로 밝힌 점은 신뢰에 긍정적이다. 다만 어닝콜 원문을 열지 못한 2차 요약이어서 발언 원문 대조가 필요하다. [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw) [S51](https://www.stocktaper.com/earningsCallSummary/IOT)
- [dilution] 희석은 계속되고 있다. 희석 주식 수는 FY2024 이후 연 3~4% 늘었고(C:share_change@FY2026 3.1%, C:share_change@FY2025 4.0%) 코드 신호도 연 3.7% 증가로 watch 상태다(C:dilution). SBC는 FY2027Q2 분기에 9,638만 USD(F177)로 직전 분기 7,747만 USD(F176)보다 크게 늘었다. [C:share_change@FY2026] [C:share_change@FY2025] [C:dilution] [F177] [F176]
- [dilution] FCF의 질이 SBC 의존적이다. FY2026 FCF는 SBC 차감 후 음수이고(C:fcf_after_sbc@FY2026), SBC/OCF는 133.3%(C:sbc_to_ocf@FY2026)다. 주주에게 돌아오는 현금흐름은 회계상 FCF보다 작다. 다만 SBC 차감 FCF 적자는 FY2022 -4.2억에서 FY2026 -1.1억 USD로 줄어드는 추세다. [C:fcf_after_sbc@FY2026] [C:sbc_to_ocf@FY2026] [C:fcf_after_sbc@FY2022]
- [capital_allocation] 자본배분은 내부 재투자 중심이다. 매입 기록은 FY2022 5,000 USD(F1) 한 건뿐이고 FY2023·FY2024는 0이다. 부채는 없고 현금은 FY2027Q2에 2.9억 USD(F20)다. 연구개발비는 FY2026 3.4억 USD(F162)에서 FY2027Q2 분기 1.0억 USD(F167)로 늘고 있으며, 매출 대비 재투자 수익률(ROIC)은 -2.4%(C:roic@FY2026)로 아직 자본비용에 못 미치지만 -522.4%(C:roic@FY2022)에서는 크게 개선됐다. M&A 이력은 수집되지 않았다. [F1] [F20] [F162] [F167] [C:roic@FY2026] [C:roic@FY2022]
- [capital_allocation] 설비투자와 재고가 늘고 있다. 설비투자는 FY2026 2,877만 USD(F8)로 FY2025 2,018만 USD(F7)에서 증가했고, 재고는 FY2027Q2 5,703만 USD(F100)로 FY2026 말 4,819만 USD(F98)보다 늘었다. 경영진이 IoT 기기 투자 확대를 FCF 마진 하락 이유로 든 것과 맞아떨어진다. [F8] [F7] [F100] [F98] [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw)

### 회계 품질 — watch

숫자 자체는 믿을 만하다. 코드의 red 신호(순이익 흑자인데 영업현금흐름 음수, 재무제표 정정)는 없고, 영업현금흐름은 FY2025부터 흑자이며 발생액 비율은 계속 음수다(C:accruals_ratio@FY2026 -10.7%). 이연매출도 꾸준히 늘었다(F44 → F48 → F50). 조정해서 봐야 할 것은 주식 보상(SBC)이다. FY2026 SBC(F172)가 영업현금흐름(F115)보다 커서 SBC 차감 FCF는 여전히 음수다(C:fcf_after_sbc@FY2026). 보고 FCF는 SBC를 비용으로 보지 않은 값이므로 주주에게 남는 현금흐름으로 읽으면 안 된다. 희석도 연 3.7%로 문턱을 넘는다. 최근 GAAP 흑자는 영업이익보다 영업외 수익(이자 등으로 추정)의 몫이 크다. FY2027Q2 세전이익(F137)이 영업이익(F127)의 몇 배다. 감사의견·감사인 변경·재무제표 정정·특수관계자 거래는 확인하지 못했다. 그 확인 공백 때문에 `clean`이 아니라 `watch`로 판정한다.

- [concern] sbc_to_revenue: SBC/매출이 19.5%로 문턱 10%의 두 배 가까이 된다. 다만 FY2022 53.4%에서 FY2026 19.5%로 꾸준히 내려오고 있어 방향은 개선이다. 그래도 SBC는 실제 경제적 비용이므로 이익과 FCF는 SBC를 차감한 값으로 봐야 한다. 최근 분기는 FY2027Q1 7,747만(F176)에서 FY2027Q2 9,638만(F177)으로 뛰어 개선 추세가 꺾였다. [C:sbc_to_revenue@FY2026] [C:sbc_to_revenue@FY2022] [F172] [F176] [F177]
- [concern] sbc_to_ocf: SBC가 영업현금흐름의 133.3%라서 보고 FCF의 상당 부분은 주식 보상이 비용에서 빠진 데서 나온다. 이 때문에 SBC 차감 FCF가 FY2026에도 음수다. FY2025의 211.1%에서는 내려왔지만 여전히 100%를 넘는다. FCF 수익률 1.1%·P/FCF 91배도 SBC를 차감하지 않은 값이므로 밸류에이션에서는 SBC 차감 기준으로 조정해 봐야 한다. [C:sbc_to_ocf@FY2026] [C:sbc_to_ocf@FY2025] [C:fcf_after_sbc@FY2026] [F172] [F115]
- [benign] inventory_gap: 신호는 FY2025 재고(F94, 전년 F93 대비 급증)가 매출 성장을 41.7%p 앞질렀다는 것이다. 다만 FY2024 재고가 이례적으로 낮았던 기저효과가 크다(DIO 32.9일). 이후 DIO는 FY2026에 46.7일로 FY2025(47.6일)와 비슷한 수준에서 안정됐다. 재고가 매출채권이나 이연매출 같은 선행 지표와 어긋나게 쌓이는 모습도 없다. 경영진도 IoT 기기 투자와 공급망 비용을 언급했다(S50). 재고 평가손실이나 매출 부풀리기의 증거는 없다. 분기 재고는 FY2027Q2 5,703만(F100)까지 완만하게 늘고 있어 계속 추적하되 문제로 보지는 않는다. [C:inventory_gap] [C:dio@FY2024] [C:dio@FY2025] [C:dio@FY2026] [F93] [F94] [F100] [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw)
- [concern] dilution: 희석 주식 수가 연 3.7% 늘어 문턱 3%를 넘는다. FY2026 증가율은 3.1%(C:share_change@FY2026)이고 FY2026Q3~FY2027Q2 분기값은 5.9억(F58, F60)으로 높게 유지되고 있다. 자사주 매입은 FY2022 이후 기록이 없어(F2, F3) SBC 희석을 상쇄하는 장치가 없다. 주당 가치는 이 희석을 반영해 낮춰 잡아야 한다. [C:dilution] [C:share_change@FY2026] [F55] [F58] [F60] [F2] [F3]
- [watch] FY2027Q1·Q2 GAAP 순이익(F109, F110)은 영업이익(F126, F127)보다 훨씬 크다. 세전이익(F136, F137)이 영업이익을 크게 웃돌기 때문이다. 영업외 항목이 이익을 키운 것으로 추정되지만 항목별 내역은 확인하지 못했다. 'GAAP 연속 흑자'는 본업의 수익성이 아니라 영업이익률(C:operating_margin@FY2026 -3.2%)로 판단해야 한다. [F109] [F110] [F126] [F127] [F136] [F137] [C:operating_margin@FY2026]
- [info] 영업현금흐름이 순이익보다 줄곧 크고 발생액 비율은 음수다. 이연매출이 FY2025 5.6억(F44)에서 FY2027Q2 7.3억(F50)으로 늘어 선수금 기반의 현금 창출이 이익의 질을 받쳐 준다. 반면 매출채권 증가율은 매출 성장률을 문턱(15%p) 아래에서 웃도는 수준이고, DSO는 FY2024 63.0일에서 FY2026 72.5일로 올랐다. 큰 문제는 아니지만 채권 회수 속도는 계속 지켜볼 항목이다. [C:accruals_ratio@FY2026] [C:dso@FY2024] [C:dso@FY2026] [F44] [F50] [F145] [F147]
- [watch] 가이던스가 비GAAP 영업이익률 21%(F215) 기준이다. 같은 기간 GAAP 영업이익률은 한 자릿수 이하다(FY2027Q2 영업이익 F127을 매출 F157에 견주면 알 수 있다). 두 값의 차이는 대부분 SBC(F177)로 설명되며 반복되는 비용이다. 비GAAP 마진을 GAAP처럼 읽으면 안 된다. 코드의 non_gaap 신호는 비GAAP와 GAAP 비교용 사실이 없어 계산되지 않았다. [F215] [F127] [F157] [F177]
- [info] 코드의 restatement(8-K 4.02 정정)와 auditor_change(4.01 감사인 변경) 신호는 뜨지 않았다. 다만 리서처가 감사의견, 계속기업 의문, 핵심감사사항, 특수관계자 거래, DEF 14A 보상 지표를 확인하지 못했다고 밝혔다. 이 부분은 미확인이지 문제가 없다는 확인이 아니다. 10-K(S9)에서 확인이 필요하다. [S9](https://www.sec.gov/Archives/edgar/data/1642896/000162828026018167/iot-20260131.htm) [S6](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039492/iot-20260601.htm)
- [info] 경영진은 FY27 FCF 마진이 FY26(C:fcf_margin@FY2026 12.8%)보다 약 100bp 낮을 것이라 했고, 이유로 기기 투자 확대와 공급망 비용을 들었다. 2차 요약이라 원문 대조는 필요하지만, 설비투자가 FY2027Q2 878만(F221)까지 늘어난 것과 방향이 맞는다. 비용을 자본화해 FCF를 부풀리는 모습은 보이지 않는다. [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw) [C:fcf_margin@FY2026] [F221]

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 성장 감속과 멀티플 압축이 동시에 왔다. 순신규 ARR 증가율(+28%)은 이미 ARR 증가율(+30%)보다 낮다. 가이던스 상향으로 기대가 높아진 상태에서 신규 유입이 식으면 시장은 성장주 배수를 거둔다. 현재 EV/매출 12.49배, P/FCF 91.45배는 성장이 둔화되는 기업에는 유지되지 않는다. 기본 시나리오조차 멀티플 변화로 연 -24.9%를 잃는다. 매출이 약세 시나리오 속도인 연 13.8%까지 내려가고 출구 배수가 18배로 수렴하면 주가는 -60% 근처가 된다. [F209] [F210] [C:ev_revenue] [C:p_fcf] [C:base_rate@base] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- (15%) 주식 보상(SBC)이 주주 몫의 현금흐름을 잠식했다. SBC는 영업현금흐름의 133.3%이고 SBC 차감 FCF는 FY2026에도 음수다. 보고 FCF 기준 P/FCF 91배는 SBC 차감 기준으로는 의미가 없다. 주가가 정체하면 인재 유지를 위해 SBC를 더 늘려야 하고 희석은 연 3.7%를 넘는다. 자사주 매입은 없다. 분기 SBC가 이미 9,638만으로 뛰었다. 주당 가치는 희석으로 깎이고 투자자가 가정한 FCF 마진 확대는 SBC 비용 인식 앞에서 사라진다. [C:sbc_to_ocf] [C:fcf_after_sbc@FY2026] [C:dilution] [F177] [F176]
- (15%) 하드웨어 선투자가 구독 매출로 회수되지 않았다. 경영진은 IoT 기기 투자 확대와 공급망 비용으로 FY27 FCF 마진이 FY26보다 약 100bp 낮을 것이라 했다. 재고는 FY2026Q1 3,788만에서 FY2027Q2 5,703만으로 늘었다. 경쟁사가 기기 가격을 낮추거나 기기를 무상 제공하는 가격 경쟁을 시작하면 기기 마진과 신규 계약 단가가 함께 무너진다. 재고 평가손실과 공급망 비용이 겹치면 FCF 마진은 18%에 이르지 못하고 12.8%대에 머문다. 이 경우 FCF 마진 확대라는 투자 논거가 사라진다. [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw) [F95] [F100] [C:fcf_margin@FY2026] [C:inventory_gap]
- (15%) 대형 고객 확장이 성장의 거의 전부였고 그 흐름이 꺾였다. ARR $100K 이상 고객이 ARR의 대부분(약 $1.3B, +38%)이며 순증 242곳이 분기 최대로 소개됐다. 분기 최대치는 이후 분기에 쉽게 낮아진다. 순매출유지율과 이탈률은 확인되지 않았고 해자 근거는 2차 요약뿐이다. 대형 고객이 예산을 줄이거나 경쟁사로 일부 전환하면 가장 빠르게 성장하던 부분이 먼저 식고 전체 성장 둔화가 가속된다. 그동안 GAAP 영업이익은 이미 720만에서 488만으로 줄었고 SBC가 늘면 적자로 돌아선다. [F211] [F212] [F229] [F230] [F126] [F127] [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw)
- 약한 가정 `base.exit_multiple`: 기본 시나리오는 5년 뒤에도 출구 P/FCF 32배를 가정한다. 이때 성장률은 15%까지 내려가 있다. 기저율 표가 없어 이 조합이 얼마나 드문지 검증되지 않았다. 현재 91.45배에서 32배로 내려오는 것만으로 연 -24.9%가 깎이며, 민감도상 배수 ×0.75만 적용해도 기본 시나리오 수익률은 -5.5%다. 성장이 15%로 식은 기업에 32배를 주는 근거는 모델에 없다. [C:p_fcf] [C:expected_irr] [C:base_rate@base] [C:irr@base]
- 약한 가정 `base.fcf_margin`: 기본 시나리오는 FCF 마진을 FY2026 12.8%에서 18%까지 올린다. 그러나 경영진은 FY27에 마진이 약 100bp 낮아진다고 했다. 이 FCF는 SBC를 비용으로 보지 않은 값이고 SBC 차감 FCF는 FY2026에도 음수다. 영업 레버리지가 SBC 증가(분기 9,638만)에 먼저 소진되는 경로가 가능하다. 역DCF에서도 이 마진 가정이 가치의 절반을 결정한다. [C:fcf_margin@FY2026] [C:fcf_after_sbc@FY2026] [C:implied_cagr@m18] [S50](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw) [F177]
- 약한 가정 `base.revenue_growth`: 기본 시나리오 첫해 성장률 26.5%는 가이던스 상향에 맞춘 값이다. 이후 감속은 연 2.5~3%p로 매끄럽게 가정되었다. FY2023 52%에서 FY2026 30%까지 감속은 연 10%p 이상 빨랐다. 순신규 ARR 증가율이 이미 ARR 증가율보다 낮아 감속이 더 빠르게 진행될 가능성이 모델에 반영되지 않았다. [C:revenue_growth@FY2023] [C:revenue_growth@FY2026] [F209] [F210]

## 검증 (L6)

주장 72개 — supported 61 · unsupported 10 · contradicted 1 · leap 0 · 미검증 0

- [unsupported] 레드팀: 성장 감속과 멀티플 압축이 동시에 왔다. 순신규 ARR 증가율(+28%)은 이미 ARR 증가율(+30%)보다 낮다. 가이던스 상향으로 기대가 높아진 상태에서 신규 — 없는 근거 인용: C:base_rate@base
- [unsupported] 슬레이터: 생존 경로는 막혀 있지 않다. 부채가 없고 현금이 2.9억 USD이며 FY2026 FCF 마진이 12.8%로 흑자다. 코드가 계산한 기본 시나리오 현금 경로도 0 — 현금과 FCF 마진은 맞지만, '부채 없음'과 '기본 시나리오 현금 경로가 0 아래로 가지 않는다'는 인용에 없다.
- [unsupported] 경영진·자본배분: 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도 자료를 찾지 못했다. 정렬 판단에서 가장 큰 공백이다. — 인용 없음
- [unsupported] 레드팀: 기본 시나리오는 5년 뒤에도 출구 P/FCF 32배를 가정한다. 이때 성장률은 15%까지 내려가 있다. 기저율 표가 없어 이 조합이 얼마나 드문지 검증되지 않았다 — 없는 근거 인용: C:base_rate@base
- [unsupported] 레드팀: 기본 시나리오는 FCF 마진을 FY2026 12.8%에서 18%까지 올린다. 그러나 경영진은 FY27에 마진이 약 100bp 낮아진다고 했다. 이 FCF는 SBC — FCF 마진 12.8%, SBC 차감 FCF 음수, 경영진의 100bp 하락 발언, 분기 SBC는 맞지만, '이 마진 가정이 가치의 절반을 결정한다'는 인용에 근거가 없다.
- [unsupported] 사업·산업: 총이익률은 FY2022 70.9%, FY2023 72.0%, FY2024 73.6%, FY2025 76.1%, FY2026 76.7%로 매년 상승했다. 하드웨어를 — 양 끝값(70.9%, 76.7%)은 맞지만, FY2023~FY2025 중간값(72.0%, 73.6%, 76.1%)과 '매년 상승'은 인용에 없고 S9는 내용이 비어 있다.
- [unsupported] 슬레이터: 레드팀이 고른 가장 강한 부검은 성장 감속과 멀티플 압축이 같이 오는 경로다. 인정한다. 그 선행 신호인 분기 순신규 ARR이 직전 분기 값 아래로 내려가는 것을 — 출처 없는 숫자 6e+07 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 회계 품질: SBC가 영업현금흐름의 133.3%라서 보고 FCF의 상당 부분은 주식 보상이 비용에서 빠진 데서 나온다. 이 때문에 SBC 차감 FCF가 FY2026에도 음수다 — 출처 없는 숫자 100% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [contradicted] 레드팀: 기본 시나리오 첫해 성장률 26.5%는 가이던스 상향에 맞춘 값이다. 이후 감속은 연 2.5~3%p로 매끄럽게 가정되었다. FY2023 52%에서 FY2026 3 — 52.3%→29.6%는 3년간 약 22.7%p, 연 약 7.6%p 하락이라 '연 10%p 이상'과 다르다.
- [unsupported] 사업·산업: 기기·데이터가 늘수록 AI 기능과 벤치마킹이 좋아진다는 회사 측 논리가 있으나, 점유율·가격 인상 후 잔존 기록은 근거에 없다. 보도와 회사 발표 수준이다. — 인용한 S27·S23에는 기기·데이터가 AI 기능을 개선한다는 회사 측 논리가 드러나지 않는다(제목과 출처만 있음).
- [unsupported] 애크먼: 레드팀의 가장 강한 논거는 기본 시나리오 출구 배수 32배와 FCF 마진 18% 가정이 낙관적이라는 것이다. 이는 내 안전마진을 더 악화시키는 방향이다. 민감도상 — 출처 없는 숫자 7500, 5.5%, 60% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2026)

| 지표 (키) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| 매출 (revenue) | 4.3억 USD | 6.5억 USD | 9.4억 USD | 12.5억 USD | 16.2억 USD |
| 매출 성장 (revenue_growth) | — | 52.3% | 43.7% | 33.3% | 29.6% |
| 총이익률 (gross_margin) | 70.9% | 72.0% | 73.6% | 76.1% | 76.7% |
| 영업이익률 (operating_margin) | -82.6% | -39.8% | -34.5% | -15.2% | -3.2% |
| 순이익 (net_income) | -3.6억 USD | -2.5억 USD | -2.9억 USD | -1.5억 USD | -912만 USD |
| 영업현금흐름 (ocf) | -1.7억 USD | -1.0억 USD | -1,182만 USD | 1.3억 USD | 2.4억 USD |
| 설비투자 (capex) | 1,935만 USD | 3,324만 USD | 1,095만 USD | 2,018만 USD | 2,877만 USD |
| FCF (fcf) | -1.9억 USD | -1.4억 USD | -2,277만 USD | 1.1억 USD | 2.1억 USD |
| FCF 마진 (fcf_margin) | -44.6% | -20.9% | -2.4% | 8.9% | 12.8% |
| SBC (sbc) | 2.3억 USD | 1.8억 USD | 2.4억 USD | 2.8억 USD | 3.1억 USD |
| SBC/매출 (sbc_to_revenue) | 53.4% | 27.2% | 25.3% | 22.2% | 19.5% |
| SBC/영업현금흐름 (sbc_to_ocf) | — | — | — | 211.1% | 133.3% |
| SBC 차감 FCF (fcf_after_sbc) | -4.2억 USD | -3.1억 USD | -2.6억 USD | -1.7억 USD | -1.1억 USD |
| ROIC (roic) | -522.4% | -35.2% | -41.5% | -22.6% | -2.4% |
| 순현금 (net_cash) | 9.2억 USD | 2.0억 USD | 1.4억 USD | 2.3억 USD | 3.2억 USD |
| 희석 주식 수 (diluted_shares) | 2.8억 | 5.1억 | 5.3억 | 5.6억 | 5.7억 |
| 주식 수 변화 (share_change) | — | 85.3% | 4.0% | 4.0% | 3.1% |
| DSO(일) (dso) | 69.9 | 68.7 | 63.0 | 68.4 | 72.5 |
| DIO(일) (dio) | 97.0 | 81.1 | 32.9 | 47.6 | 46.7 |
| 발생액 비율 (accruals_ratio) | — | -9.1% | -16.4% | -15.2% | -10.7% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, cost_of_revenue, d_and_a, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, gross_profit, income_tax, inventory, inventory_growth, operating_income, pretax_income, receivables, receivables_growth, rnd, total_assets

### 시장 · TTM(FY2027Q2) 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 39.57 USD/share (2026-10-16, F218) |
| 희석 주식 수 (shares) | 5.9억 |
| 시가총액 (market_cap) | 233.6억 USD |
| 순현금 (net_cash) | 2.9억 USD |
| EV (ev) | 230.7억 USD |
| FCF 수익률 (fcf_yield) | 1.1% |
| P/FCF (p_fcf) | 91.45x |
| EV/매출 (ev_revenue) | 12.49x |
| PER (pe) | 258.02x |
| 순부채/EBITDA (net_debt_to_ebitda) | -5.92x |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 19.5% > 10%
- [watch] sbc_to_ocf (C:sbc_to_ocf): SBC/영업현금흐름 — FCF의 상당 부분이 주식 보상 133.3% > 50%
- [watch] inventory_gap (C:inventory_gap): FY2025 재고 증가율 - 매출 증가율 41.7% > 15%
- [watch] dilution (C:dilution): 희석 주식 수 연 3.7% 증가 > 3%

### 역DCF — 현재 가격이 가정하는 것

EV 230.7억 USD를 정당화하려면 매출이 10년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 목표 마진으로 직선 수렴, 할인율 10%, 이후 영구성장 3%.
기본 시나리오 목표 마진 18% 기준: 연 24.4% (C:implied_cagr)

| 목표 FCF 마진 | 내재 매출 성장(연) | 인용 키 |
|---|---|---|
| 10% | 31.9% | C:implied_cagr@m10 |
| 15% | 26.7% | C:implied_cagr@m15 |
| 18% | 24.4% | C:implied_cagr@m18 |
| 20% | 23.0% | C:implied_cagr@m20 |
| 25% | 20.3% | C:implied_cagr@m25 |
| 30% | 18.0% | C:implied_cagr@m30 |

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 30% | 30.9억 USD | 13.8% | 10% | 18x | 10.15 | 6.30 | -23.8% |
| 기본 | 50% | 40.8억 USD | 20.3% | 18% | 32x | 38.41 | 23.85 | -0.6% |
| 강세 | 20% | 45.5억 USD | 22.9% | 25% | 40x | 73.63 | 45.72 | +13.2% |

확률 가중: 주당 가치 36.98 · IV 22.96 · 기대 연 수익률 -1.3% (C:expected_irr) · 손실 확률 80% (C:p_loss) · 현재 주가 39.57

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +18.5% · 마진 변화 +6.8% · 멀티플 변화 -24.9% · 주식 수 변화 -3.0% · 현금 축적 +2.0% = -0.6%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -10.0% | -5.4% | -1.5% |
| +0%p | -5.5% | -0.6% | +3.5% |
| +5%p | -1.0% | +4.2% | +8.5% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2027 | 20.5억 USD | 13.9% | 2.8억 USD | 6.1억 | 5.8억 USD |
| FY2028 | 25.2억 USD | 14.9% | 3.7억 USD | 6.3억 | 9.5억 USD |
| FY2029 | 30.2억 USD | 15.9% | 4.8억 USD | 6.5억 | 14.3억 USD |
| FY2030 | 35.5억 USD | 17.0% | 6.0억 USD | 6.6억 | 20.3억 USD |
| FY2031 | 40.8억 USD | 18.0% | 7.4억 USD | 6.8억 | 27.7억 USD |

### 컨센서스 대비 (C:consensus_diff@지표@기간)

| 지표 | 기간 | 컨센서스 | 기본 시나리오 | 차이 |
|---|---|---|---|---|
| revenue | FY2027 | 19.7억 USD | 20.5억 USD | +3.9% |
| revenue | FY2027 | 20.1억 USD | 20.5억 USD | +1.9% |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- 시장 내재 성장 (역DCF): 연 24.4% × 10년 → 기저율 표 없음
- base 시나리오 매출 성장: 연 20.3% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 22.9% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=3.92x, revenue_5y=2.81x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=2.9억 USD
- 애크먼 case={"from": "base"}: price=39.6, fcf_positive=예, net_debt_to_ebitda=-5.92x, leveraged=아니오, intrinsic_value=23.8, mos=-65.9%

### 계산 경고

- 모델이 컨센서스와 사실상 같다 — variant perception이 없다면 알파도 없다
- 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-09-08 | [10-Q](https://www.sec.gov/Archives/edgar/data/1642896/000162828026060909/iot-20260801.htm) |  |
| S2 | filing | 2026-09-03 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1642896/000162828026060438/iot-20260903.htm) |  |
| S3 | filing | 2026-07-23 | [8-K](https://www.sec.gov/Archives/edgar/data/1642896/000162828026049446/iot-20260722.htm) |  |
| S4 | filing | 2026-06-09 | [10-Q](https://www.sec.gov/Archives/edgar/data/1642896/000162828026041893/iot-20260502.htm) |  |
| S5 | filing | 2026-06-04 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1642896/000162828026040788/iot-20260604.htm) |  |
| S6 | filing | 2026-06-01 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039492/iot-20260601.htm) |  |
| S7 | filing | 2026-06-01 | [8-K](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039465/iot-20260601.htm) |  |
| S8 | filing | 2026-05-01 | [8-K](https://www.sec.gov/Archives/edgar/data/1642896/000119312526201457/d69859d8k.htm) |  |
| S9 | filing | 2026-03-16 | [10-K](https://www.sec.gov/Archives/edgar/data/1642896/000162828026018167/iot-20260131.htm) |  |
| S10 | filing | 2026-03-05 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1642896/000162828026015170/iot-20260305.htm) |  |
| S11 | filing | 2026-01-06 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1642896/000162828026000886/iot-20260106.htm) |  |
| S12 | filing | 2025-12-09 | [10-Q](https://www.sec.gov/Archives/edgar/data/1642896/000162828025056069/iot-20251101.htm) |  |
| S13 | filing | 2025-12-04 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1642896/000162828025055355/iot-20251204.htm) |  |
| S14 | filing | 2024-03-26 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1642896/000164289624000016/0001642896-24-000016-index.htm) |  |
| S15 | filing | 2025-03-25 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1642896/000164289625000022/0001642896-25-000022-index.htm) |  |
| S16 | filing | 2023-03-21 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1642896/000164289623000016/0001642896-23-000016-index.htm) |  |
| S17 | filing | 2025-06-10 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1642896/000164289625000058/0001642896-25-000058-index.htm) |  |
| S18 | filing | 2025-09-09 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1642896/000164289625000074/0001642896-25-000074-index.htm) |  |
| S20 | news | 2026-07-30 | [Samsara Inc. (IOT) Stock Falls Amid Market Uptick: What Investors Need to Know - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxONVJ5VEJ6TnJ4Y2dvSTJSTmIwT1MydlFuVmFkOXUyR05WbHJtZlYtSFpVQ0xMQXB2U0MtZm5wd0VvbkdTZjdqbzhsWERqT3U5TUNxNXV3RXFtaGV2VnVHUFJLblpzN1d6RnlkaFd1UHJMelJnZXpKVWJWQXhrbjNOWUJYaVpVbmZydTZWb3VlZldEZVh4QW1B?oc=5) | Yahoo Finance |
| S23 | news | 2026-08-19 | [Samsara Launches Fuel Command Center to Help Fleets Control Costs Amid Price Volatility - Business Wire](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNU1QyWk9pdjBfLXZIaXRCVGlwY1kwSFB2ZTBXUHkwczlnWUZpWGpBT3A5bUJBb251dkxTZERBX3ZrdEs5dDBXeXYwYjJ4WGVoRXF1V1BieV9fTExDZVJKbnFMYU9Zd18xUmoyb0ZJdV9KT2hNYUpzbTFPUndnaHBvN2dNWUFqRG5rRWo4OEJpM1VDVmRKeFJhUnp4bXBlZERIUVBBS2VIbjhFemlYT1ZKSXotMmpmejcwQlhxVF8tUC1IRnhCMTZ6bWt2RVBhcTZtS0lPMHhRdUZXMFRL?oc=5) | Business Wire |
| S25 | news | 2026-08-18 | [Samsara Inc. (IOT) Increases Despite Market Slip: Here's What You Need to Know - Yahoo Finance](https://news.google.com/rss/articles/CBMinwFBVV95cUxNVzB0bUNFUnRpN1EyR2U4aWJRQ3pMa2FSNDhwRm1iYmJyZGtNRHpxczlCeTBxTzdXNDRCQzFwc1NfMUU3SHRvOUtmV21RVlVPRFJEcEkwM1pIbE9oYjdtS1Rsby1PNlBVZnJVUFVBXzNBQ2ozZHozM1AwaTVnX01NcS14c2JoTG1UZjN0OGt6TnhQd1dFT1haOGNsNk5oUVE?oc=5) | Yahoo Finance |
| S26 | news | 2026-08-13 | [3 Reasons Investors Love Samsara (IOT) - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxQVVdiTU9tcE9KdVkxM1RjZmU2aGYta0lIdUJnajR3aEk2ZXJIbmNaNDRGNzltM1R4Qmg4RHhfTEVHT2lPeU0xUHg3d0RKcjU2cEZSaUd3STFRcnlURGtRUUNYNWVYbXk5R18yU2t0SDhqRVRzekF4YVlJMlVqVjdSai1WZEg5UHNNNGl5dmRnUzB6cjZhbEpDMkdsazFYQQ?oc=5) | Yahoo Finance |
| S27 | news | 2026-08-10 | [Samsara (IOT) Maintains 30% Growth as Margins Improve and AI Risks Stay Low - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxOR1U1Z2xJQTJONFkzVFp4Zm5NSjB1N3BzaVozbjg0RkkyYjhVZ2o2UHh3Q3RTUlJKRmhsWGt1UE1mWTR3NkMycm5lQmlzMFV5VHcyV0ZUcVBWRk1wS1NuSG92aF9UN1VYSUxPSnI3dWRudG1kZ1htRG9lc0lwT1hRMXNXVUtSaGlpOWJmck9fd2pBeGdNdUI5bjM0V1k?oc=5) | Yahoo Finance |
| S28 | news | 2026-08-12 | [Samsara Inc. (IOT) Stock Falls Amid Market Uptick: What Investors Need to Know - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxOSTFzR0ZGc1QxSXlLd1VMT01oQUhqYkx3RnNpd0h3all2NzNLd1Q0LTlkOTVHdGFQZFlDT0NhRFQxUURvTzRIOG8xWGJKdHJaVUdpSXJReGw2M19NZ1c5a3RZbUZaQTd5UkRFMUZtNktRYUNuX1lMQ0FOYUNHeWlWR3RFcWxQQ1hYWnItYmVBZ2ZKaUg5V19F?oc=5) | Yahoo Finance |
| S29 | news | 2026-10-10 | [Samsara Inc. (IOT) stock price, news, quote and history - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9fcllwVmY5NUw5NFpycmFHQ3NkSzlmZTRhYUhEaFdSYlQ5SVBFYTAwQnZXOF9fV1J4TDJrQ1VQX0tJVHU2dVJzX0FmNVRpNGtV?oc=5) | Yahoo Finance Singapore |
| S30 | news | 2026-07-21 | [Samsara (IOT) Beat Q1 Expectations, Is The Stock Still Overvalued? - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxQR0c2bmROLXlZM2tvT0JpaFYyNnBud2dGcnd4OVRpdHlMUFhmUWFOSVJRRTZNRUlxS3E0UnlsVXFYdHJZclEzcXk5VmswMEhmUGhTeElzdUowYUhwejBvdFQyN09FZUtNWVFZTlo3NnRqeWNVVWpKUG5hR2NudFlZVE1idGZ0UXVQWS1NbDNhQjA2RHQzY0lFdjE1Yk16dw?oc=5) | Yahoo Finance |
| S31 | news | 2026-07-23 | [Why Samsara Inc. (IOT) Dipped More Than Broader Market Today - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxPQUpWajJYRmtVSTRzRVJOR1hsaGtzZHB1Uy1ISWFlVFhtS1pleHp1aTVJaDFneHFhWkRubDVUbVBOZ0RFS29rc3pNY1hTdkhCa0l1bTdrUFpaZGR2eFlvWkpQREJ0T3MyTzJaYkZhT3hxNW9aWkJnNmhnQTh4eTVpUUdpN0pYNXYwb2lpU256U0NjaHZJcVE?oc=5) | Yahoo Finance |
| S32 | news | 2026-09-04 | [Samsara Q2 Earnings Surpass Estimates, Revenues Rise Y/Y - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxOZ0F3dmIydG4ySEpZN0p1elFuTGY3c09acGRkYnlacUtvZlNPRXI3YVRLSW5oSktzaDZhc2ktMlFKeTk1Q0xlblAzanhCZ19aWmRSU2lTcEpDcjJueDFTd0I2ZDk4b2tiRXhOTVhNM0t2VXp3ODNsXzVsQ0gzTVB4TEtMNmZVRkdXU29yZWg5U0RyQ25KWXVwSlVkRFFBY3FOVFB2VQ?oc=5) | Yahoo Finance |
| S33 | news | 2026-08-25 | [Samsara Inc. (IOT) Stock Falls Amid Market Uptick: What Investors Need to Know - Yahoo Finance](https://news.google.com/rss/articles/CBMilwFBVV95cUxPM1I3ZDZNZ1RwVjFncHNiT2prMHcwMEMyVlBBZmJmYjh0LUdtWTNncFduQTBPRU56QUpFUkh4a1hZRVlINU5JUElQQ3lRNE4zZlZ6VVUzSGU2ZDNSUHpVQ3Y0eFlwTDJldlJiN0tJZlktenZFWG5nVGg0aEJselRIRTJnSVNmaVlqTFlkWFljRy1MN1hlMFV3?oc=5) | Yahoo Finance |
| S34 | news | 2026-08-06 | [Samsara Inc. (IOT) Registers a Bigger Fall Than the Market: Important Facts to Note - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPUWF3amIzVFlLbkxCZE5aSHVOdmZnTkdpZDF0WmRWTkFLWXNrWkM0dzRzOG91eWliY01UR2R2NzlnUG1jS18xX2s3MlZVODhDU2hKNTg4bDNGMjltWFZsMDB1Rm5uUXZpMTN5a3FQNjZmYzMzQWNBZ2tvY3BKci1ZMzBTQjZfdVVCZS1qZ1dwVUg4QTlCRkhhQW5oWEpudw?oc=5) | Yahoo Finance |
| S35 | news | 2026-08-26 | [Is Samsara (IOT) Undervalued On Its Fuel Command Center Launch? - Yahoo Finance](https://news.google.com/rss/articles/CBMiowFBVV95cUxONGJldFA4MHJOWWhNLW9jM003RlNEclozcFhWNXJ2N191QTgyRURDdlAwdWlwUFgtZnlPWlk1c0RENFlpTHFNZGd3OEhXRXRwdHowMWRJR09tUEN4V0pRMkdmSkk5T2RpWGNINS1mQXBzOWNNdjVVZFU1UHJzNHN2RWNPMmY4REY0VjNwcHZ1NGxrTnlJQmJtWURnanMxWVZ6QXlN?oc=5) | Yahoo Finance |
| S36 | news | 2026-07-29 | [Atlassian, ServiceNow, and Samsara Shares Are Soaring, What You Need To Know - Yahoo Finance](https://news.google.com/rss/articles/CBMirAFBVV95cUxPWVNYdFotZmZKSWRIV05oM01XdG82cjctTlZFWUZpSUZ0N21GM2MtZ3BqNDJBMkx5SXZOc0FFa05faTNoSldYZWFTX3FEbU5rYjE0TVNwakxfME00a3hQSFNXaWlEcGxuMUdoa1pXbkRyVzhyenQ4elhOWTBRTWtsNWNkQ09RbWFqUTQ0WnZjcGo2cVB4UGRkeEEyeUpEcllzc056ZjBiUzVwRkRB?oc=5) | Yahoo Finance |
| S37 | news | 2026-07-21 | [Can Samsara (IOT) Justify Its Price After A 46% Gain? - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNNVNuN3JibFZMRWxsMjVMeVlVcU9kM3I2YWVrUnBoNGRaczZIaE5OV2VKWHRlakhNOXRSYmx5bTJLZDRqcURrSWVLTi00TTBmWG0zQnZiUi0xdHRBQjVSYm5PbDFyNUNWU3I1ejFSZEdtcktrVHRDRXlRUUl2dFgyU0pBcGRXZGJRN2p4bGcwQXJCT2NPUEowRg?oc=5) | Yahoo Finance |
| S38 | news | 2026-08-04 | [Samsara (IOT) Following Its Connected Operations Story With Fair Value In Focus - Yahoo Finance](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQeVdGTFZZdlRYVU9QTk1RTE8wSzZCaTh0NGE4bnFKd3N5QW9ScW5xb2d3a1pOazVoejNNOUV5RS1rRjVfNWdiY2RySERiT3dsRkM5VGh6ZU5ob1BCSG9sTnhkQm0zWkZPWWhUbUY3ZWZpbTItYWZrbWFKdGdUWUNNMG94UjdONDlRMlJ4b2V1dmwyQS1lZTJacml1a2VEWXh0UzczZlRUTDRTSzA?oc=5) | Yahoo Finance |
| S39 | data | 2026-09-04 | [Samsara Analysts Boost Their Forecasts After Strong Q2 Earnings](https://www.itiger.com/news/2664435814) | 보도. IOT 주가 2026-09-04(금) 장중 $40.29, +4%. FY27 Q2 매출 $508.44M(추정 $483.26M), EPS $0.20(추정 $0.16). 목표가 상향: BTIG 54, Guggenheim 51, KeyBanc 55, TD Cowen 53, RBC 55, Wells Fargo 58, BMO 54, BofA 55 (모두 매수 의견). 공식 종가가 아니라 기사 속 장중가. |
| S40 | news | 2026-09-03 | [Samsara Reports Second Quarter Fiscal Year 2027 Financial Results (Quartr·Zacks·Benzinga 등 2차 요약)](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) | 보도(2차 요약, 원문은 403으로 열지 못함). 종료 ARR 약 $2.125B(+30% YoY), 순신규 ARR $134.1M(+28%), ARR $100K 이상 고객 3,605곳(해당 고객 ARR $1.3B, +38%). 가이던스: FY27 Q3 매출 $514~516M, FY27 매출 $2.043~2.047B, 비GAAP 영업이익률 Q3·FY 모두 21%. 직전 FY27 가이던스는 매출 $2.005~2.013B, 비GAAP EPS $0.70~0.72. |
| S41 | data | 2026-08-01 | [Samsara Inc. (IOT) Stock Forecast — TickFlow 컨센서스 (2026-08-01 기준)](https://tickflow.io/stock/IOT/forecast) | FY27(2027-01-31 종료) 매출 컨센서스 평균 $1.97B(저 $1.95B~고 $1.98B). Q2 실적·가이던스 상향 이전 값이라 낡았다. FY28은 분기 합계 약 $2.7B로 읽히나 명확한 연간 컨센서스는 못 찾았다. |
| S42 | data | 2026-09-03 | [Earnings Whispers — IOT FY2027 가이던스·컨센서스](https://earningswhispers.com/epsdetails/IOT/202607) | 보도성 집계. Q2 발표 전 FY27(2027-01 종료) 매출 컨센서스 약 $2.01B. 상향 후 가이던스 $2.043~2.047B. |
| S43 | data | 2026-08-10 | [Investing.com — Samsara Inc (IOT) 시세 스냅샷](https://www.investing.com/equities/samsara) | 종가 39.34(-2.43%). 52주 범위 약 $23.38~47.47. 12개월 평균 목표가 44.31, 컨센서스 '매수'. Piper Sandler 하향(2026-08-10)이 표에 있음. 2차 집계 페이지라 시차가 있을 수 있다. |
| S44 | data | 2026-10-16 | [Yahoo Finance IOT historical prices](https://finance.yahoo.com/quote/IOT/history/) | 2026-10-16 종가 39.57 USD |
| S45 | news | 2026-10-15 | [Samsara Tracking Label: The Best Inventions of 2026 - Time Magazine](https://news.google.com/rss/articles/CBMifEFVX3lxTE1pdFBsQ2V5MWM4Z2k1MkcxbG81SFBMSUlFWUhId1lMZ0tRWi1EdFYwbElDT0dRbExjVUw2UlU5U0x5SVBsRE5odTdyc29fakhiTkJYRDNEeTZkOEdtclJYbTJGUW9VazRHaTRDMlBXb20yUmhNTU1ZaG1KUFo?oc=5) | Time Magazine |
| S46 | news | 2026-09-07 | [Samsara Fleet Management: Features, Fees, Support 2026 - Tech.co](https://news.google.com/rss/articles/CBMickFVX3lxTFBJdFdIVm0xTHE3dzFwTHMxSmtndkUzVmkyeFk4YVk0N0FWSTFZVDNwb1VpZHdkZVVEaHY1VS1ieGpXd1pybjl5emNaWm9tbjhOVUxoMDEyRVJiZk5zUTFua1E2c2M5T2djcnd6MzdtSzhCQQ?oc=5) | Tech.co |
| S47 | news | 2026-10-07 | [Samsara Fleet Management Review and Pricing - Business.com](https://news.google.com/rss/articles/CBMiU0FVX3lxTE13NlVyUDVSYk9GWTkwMU04T3k2VG5HNnVkUXhpMVRSa0ViWElfTEdyYTAtckRPWTRfY2VVMGZjS2psWXhHWm1zS2pOMFZndFh5eTZz?oc=5) | Business.com |
| S48 | news | 2026-08-27 | [Why this company ditched tech blue for construction yellow in its new logo - Fast Company](https://news.google.com/rss/articles/CBMickFVX3lxTE1IMmZBNU45dy1QUEwxLTZJWndoYmw0ZFo4dXJaZFFXdUstZ2lTb3BaQlp2VTNhUGJZVmJpZ3ctS3doUjFidWZzWDVvM1RLejBlMFhRQWo1TzJORTJRUlJqWVlIdFB5TlVMc2QzTTBOQzl6dw?oc=5) | Fast Company |
| S49 | news | 2026-08-10 | [Samsara’s Tiny Tracker Offers 45-Day Visibility for Any Shipment - FreightWaves](https://news.google.com/rss/articles/CBMingFBVV95cUxOQ3FXeDYxTXQweTN3X0xpZ2kwakR3b0pTdjVndFNTODFxYXlnU2plVlZWa3VKeEZWcDg4eUpfX3plU1hhc3B6QS1UTzRLdXpjenFWX2NESnpVa3BuLUxTdVRlNlBpbXpqMTRDSDAwUVNwUUJ3dG5Zb1hYcWRETHN5bWl2QkZUb2s4ZVRnbUNOZnFPREpnbGhhalpXcEFDZw?oc=5) | FreightWaves |
| S50 | call | 2026-09-03 | [Samsara (IOT) Q2 2027 earnings summary — Quartr 이벤트 페이지](https://quartr.com/events/samsara-inc-iot-q2-2027_ojW4QHpw) | FY27 Q2(2026-08-01 종료) 어닝콜의 2차 요약 페이지. 트랜스크립트 원문은 열지 못했다. 보도(2차): 종료 ARR 약 $2.125B(+30% YoY), 분기 매출 $508.4M, GAAP EPS $0.03(4분기 연속 GAAP 흑자). ARR $100K 이상 고객 순증 242곳, ARR $1M 이상 고객 순증 20곳(둘 다 분기 최대로 소개). 경영진은 FY27 FCF 마진이 FY26보다 약 100bp 낮을 것이라 했고 이유로 IoT 기기 투자 확대와 공급망 비용을 들었다. 가이던스: FY27 매출 $2.043~2.047B, FY27 Q3 매출 $514~516M. |
| S51 | call | 2026-09-03 | [Stock Taper — IOT 어닝콜 요약 (Q2 FY2027 콜 트랜스크립트 기반이라고 표기)](https://www.stocktaper.com/earningsCallSummary/IOT) | 보도(2차 요약). 콜 트랜스크립트를 요약했다고 표기한 사이트이고 본문은 열지 못했다. 단독 근거로 쓰지 말고 S50·S40과 함께 교차 확인용으로만 쓴다. |

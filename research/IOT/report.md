# Samsara (IOT) 리서치 보고서 — 기준일 2026-10-18

**반대 우세** — 찬성 0 · 반대 2 · 보류 1 · 확신 가중 점수 -0.40 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장이 반영한 것: 주가 $40.29(F208)에서 EV/매출 12.72배(C:ev_revenue)로, 시장은 ARR +30% 안팎의 성장이 상당 기간 이어지는 것을 가격에 넣고 있다. 상향된 FY2027 가이던스(F213)는 Q2 발표 전 컨센서스($1.97B·$2.01B, F216·F217)보다 높고, 분석가 목표가는 $51~58로 현재가보다 높다(S39).
- 우리가 다르게 보는 점: FY2027 매출은 가이던스를 소폭 웃돌 가능성이 높아 단기 실적 서프라이즈의 방향은 시장과 같다. 다른 점은 그 이후다. 보고 FCF(C:fcf_margin@FY2026 12.8%)는 SBC 차감 후 음수(C:fcf_after_sbc@FY2026)이고 희석이 연 3% 이상이다. 그래서 장기 주당 가치는 시장이 보는 성장 지속보다 SBC 차감 후 현금창출과 성장 감속 속도에 더 좌우된다. 우리 기본 시나리오는 성장 감속을 기본값으로 둔다.
- 왜 우리가 맞는가: 매출 성장률은 FY2023부터 FY2026까지 한 번도 반등 없이 내려왔다(C:revenue_growth@FY2026). 순신규 ARR 증가율(+28%, F210)도 ARR 증가율(+30%, F209)보다 낮아 가속의 증거가 없다. 단기 서프라이즈는 이미 가격과 목표가에 반영됐고, 기본 시나리오 기준 기대수익률은 요구수익률을 크게 웃돌지 않는다. [F208] [F213] [F216] [F217] [F209] [F210] [S39](https://www.itiger.com/news/2664435814) [C:ev_revenue] [C:fcf_after_sbc@FY2026]
- 촉매: FY2027 Q3·Q4 실적에서 순신규 ARR 증가율과 FY2028 가이던스. 가이던스가 성장 감속 폭을 얼마나 반영하는지가 계기다.
- 시점: FY2027 Q3 실적(2026년 12월경) ~ FY2027 Q4 실적(2027년 3월경)
- 컨센서스 대비 revenue FY2027: +4.3% (20.6억 USD vs 19.7억 USD)
- 컨센서스 대비 revenue FY2027: +2.3% (20.6억 USD vs 20.1억 USD)

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **25.33** vs 주가 40.29 · 기대 연 수익률 **+0.3%** · 손실 확률 80%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 30% | 13.18 | 8.18 | -20.0% | 추정: 대형 고객 확장이 둔화하고 신규 ARR 성장(+28%, F210)이 FY2027 가이던스 이후 급격히 꺾인다. 성장률이 FY2023 52.3%에서 FY2026 29.6%로 매년 내려온 추세(C:revenue_ |
| 기본 | 50% | 40.24 | 24.99 | -0.0% | 추정: FY2027은 가이던스(F213, $2.043~2.047B)보다 소폭 높은 성장으로 마친다. Q2 매출이 추정을 웃돌았고(S39) 가이던스가 상향된 흐름이 근거다. 이후 성장은 ARR +30%(F209)에서  |
| 강세 | 20% | 83.62 | 51.92 | +15.7% | 추정: ARR $100K 이상 고객(F211)에서 확장이 이어진다. 해당 고객 ARR이 +38%로 전체(+30%)보다 빠르기 때문이다(F212, F209). Fuel Command Center 같은 제품 확장(S23 |

## 3. 반증 조건 (thesis break)

- [자료 없음] 앤더슨: FY2027Q3 순신규 ARR이 1억 달러 미만이면 성장 가설이 훼손된다 — `net_new_arr < 1e+08` (FY2027Q3)
- [자료 없음] 앤더슨: ARR $100K 이상 고객의 ARR이 줄면 대형 고객 확장 가설이 깨진다 — `arr_100k_customers < 1.3e+09` (FY2027Q3)
- [수동 확인] 앤더슨: 다음 분기 이후 가이던스가 매출 성장 감속을 한 자릿수 후반으로 반영하면 수동 확인
- [자료 없음] 슬레이터: 다음 분기 ARR이 22억 달러 미만이면 순신규 ARR 둔화가 가속된 것 — `arr < 2.2e+09` (FY2027Q3)
- [자료 없음] 슬레이터: GAAP 영업이익이 다시 적자로 돌아서면 SBC가 영업 레버리지를 지운 것 — `operating_income < 0` (FY2027Q3)
- [수동 확인] 슬레이터: 외부 조달(증자·차입)이 필요해지는 징후 — 수동 확인
- [미충족] 애크먼: 주가가 기본 시나리오 현재가치 수준(약 25달러) 아래로 내려오면 가격 근거가 바뀐다 — `price < 25`
- [자료 없음] 애크먼: FY2027 Q3 매출이 가이던스 하단 미만이면 성장 둔화가 가속된다는 뜻 — `revenue < 5.14e+08` (FY2027Q3)
- [수동 확인] 애크먼: SBC 차감 FCF가 양수로 전환되면 현금 창출 전제를 다시 평가 — 수동 확인
- [미충족] 레드팀: 순신규 ARR이 FY2027Q2의 $134.1M보다 작아진다 — 성장 감속이 가속 국면으로 진입 — `net_new_arr < 1.341e+08`
- [미충족] 레드팀: 분기 SBC가 1억 USD를 넘는다 — 희석과 SBC 비용이 영업 레버리지를 지운다 — `sbc > 1e+08`
- [충족 — 훼손] 레드팀: 이연매출이 FY2027Q2 수준(7.3억 USD) 아래로 줄어든다 — 선결제·계약 기간이 줄고 있음 — `deferred_revenue < 7.3e+08`
- [미충족] 레드팀: GAAP 영업이익이 다시 0 이하 — 흑자 전환 서사가 훼손 — `operating_income <= 0`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | revenue | FY2027Q3 | >= 5.15e+08 | 85% | 가이던스 상단(F214) 이상. 회사가 가이던스를 보수적으로 내는지 시험한다. |
| K2 | revenue | FY2027 | >= 2.05e+09 | 65% | FY2027 가이던스(F213) 상단을 넘는지로 기본 시나리오 1년차 성장 27%를 시험한다. |
| K3 | arr | FY2027Q3 | >= 2.24e+09 | 60% | ARR 2.125B(F209)에 순신규 ARR 약 $115M 이상을 더한 값. 성장 감속 속도를 확인한다. |
| K4 | operating_income | FY2027Q3 | > 0 | 60% | GAAP 영업이익 흑자 유지(F127 488만). SBC 증가가 영업 레버리지를 지우지 않는지 시험한다. |
| K5 | sbc | FY2027Q3 | <= 1e+08 | 55% | 분기 SBC가 Q2의 9,638만(F177)에서 더 뛰지 않는지로 희석 우려를 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.40 · 비중 참고값 0.0% (반대 우세 — 신규 비중 없음) · 슬레이터 시작 비중 1.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 반대 → 반대 | 2/5 | ✗ 10년 주당가치 5배 미만 또는 계산 불가 (LTGG Q10) | 1/5 실패 | founder_led=예, upside_10y=4.56x, revenue_5y=2.86x |
| 슬레이터 | 보류 → 보류 | 2/5 | ✓ | 1/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=1.0%, cash_survives=예, cash_min=2.9억 USD |
| 애크먼 | 반대 → 반대 | 4/5 | ✗ 단순·예측 가능한 사업이 아님; 잉여현금흐름을 만들지 못함 (코드 계산); 안전마진 20% 미만 또는 계산 불가 | 2/5 실패 | simple_predictable=아니오, capital_markets_dependent=아니오, catalyst=없음. 행동주의로 바꿀 경영 문제가 보이지 않고, 자사주 매입이나 분사 같은 가치 격차를 좁힐 행동도 근거에 없다., intrinsic_value=25.0, mos=-61.2%, net_debt_to_ebitda=-5.92x |

- ⚠ 앤더슨: rebuttals[0] unsupported: 없는 근거 인용: C:mos
- ⚠ 앤더슨: arguments[4] unsupported: 출처 없는 숫자 26.6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 앤더슨: risks[1]: 인용하지 않은 근거의 숫자 28%(C:fcf_margin@bull·S40) — cites에 추가
- ⚠ 앤더슨: risks[2]: 인용하지 않은 근거의 숫자 28%(C:fcf_margin@bull·S40) — cites에 추가
- ⚠ 앤더슨: arguments[3]: 인용하지 않은 근거의 숫자 40(C:exit_multiple@bull·C:price·C:price@ackman) — cites에 추가
- ⚠ 슬레이터: rebuttals[1] unsupported: 없는 근거 인용: C:mos
- ⚠ 슬레이터: arguments[2] unsupported: 순부채/EBITDA 음수와 현금은 맞지만 '기본 시나리오 현금 경로가 0 아래로 내려가지 않는다'는 인용 자료에 없다.
- ⚠ 슬레이터: rebuttals[0]: 인용하지 않은 근거의 숫자 40(C:exit_multiple@bull·C:price·C:price@ackman) — cites에 추가
- ⚠ 애크먼: arguments[0] unsupported: 없는 근거 인용: C:mos
- ⚠ 애크먼: risks[1] unsupported: 출처 없는 숫자 26.6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: arguments[1] unsupported: 출처 없는 숫자 16.6%, 26.6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: rebuttals[0] unsupported: 없는 근거 인용: C:mos
- ⚠ 애크먼: rebuttals[2] unsupported: 없는 근거 인용: C:mos
- ⚠ 애크먼: risks[0]: 인용하지 않은 근거의 숫자 100000(S40), 38%(S40) — cites에 추가
- ⚠ 애크먼: arguments[1]: 인용하지 않은 근거의 숫자 10.8%(C:accruals_ratio@FY2026) — cites에 추가
- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 주가 기준일 2026-09-04이 as_of(2026-10-18)보다 44일 오래됨
- ⚠ 모델이 컨센서스와 사실상 같다 — variant perception이 없다면 알파도 없다
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 레드팀 weakest[0] 검증 실패(unsupported): 출처 없는 숫자 26.6%, 4.9% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 경영진·자본배분 findings[7]: 인용하지 않은 근거의 숫자 5.258e+07(C:ocf@FY2026Q1·C:operating_income@FY2026·F116) — cites에 추가
- ⚠ 경영진·자본배분 findings[3]: 인용하지 않은 근거의 숫자 5.1e+08(C:diluted_shares@FY2023·C:revenue@FY2027Q2·F157), 5.7e+08(C:diluted_shares@FY2026·C:diluted_shares@FY2026Q1·C:diluted_shares@FY2026Q2), 5.9e+08(C:diluted_shares@FY2026Q3·C:diluted_shares@FY2027Q1·C:diluted_shares@FY2027Q2), 4%(C:share_change@FY2024·C:share_change@FY2025·S39), 10%(C:discount_rate) — cites에 추가
- ⚠ 레드팀 weakest[2]: 인용하지 않은 근거의 숫자 18.1%(C:revenue_cagr@base) — cites에 추가
- ⚠ 회계 품질 findings[0]: 인용하지 않은 근거의 숫자 262.71(C:pe) — cites에 추가
- ⚠ 레드팀 premortem[3]: 인용하지 않은 근거의 숫자 8(C:iv@bear·S10·S11) — cites에 추가
- ⚠ 사업·산업 findings[2]: 인용하지 않은 근거의 숫자 61%(C:mos@ackman) — cites에 추가
- ⚠ 경영진·자본배분 findings[4]: 인용하지 않은 근거의 숫자 211.1%(C:sbc_to_ocf@FY2025), 2.1e+08(C:fcf@FY2026·C:rnd@FY2022·F158) — cites에 추가
- ⚠ 레드팀 premortem[2]: 인용하지 않은 근거의 숫자 61%(C:mos@ackman) — cites에 추가

## 앤더슨 — 반대 (2/5)

> Samsara는 멱법칙 후보로 볼 만한 사업이다. 종료 ARR이 약 $2.125B로 +30%이고, 매출 성장은 29.6%를 지키며 영업이익률은 -82.6%에서 -3.2%로 올라왔다. 그러나 내 기준은 10년 안에 5배가 되는 길이 보이느냐이고, 그 길이 숫자로는 닫혀 있다. 강세 시나리오를 10년으로 늘려도 주당 가치는 현재 주가의 4.56배에 그친다. 5년 매출은 2.86배라 첫 질문은 통과하지만 10번 질문은 못 넘는다. 시가총액이 이미 약 238억 달러이고 EV/매출이 12.72배라서, 시장이 성장 지속을 대부분 가격에 넣어 둔 상태다. 기본 시나리오 기대수익률은 연 0%대인데, 분해하면 매출 성장과 마진 확대가 만든 수익을 멀티플 압축이 거의 전부 지운다. 이 회사가 대담한 성장주가 아니라는 말은 아니다. 지금 가격에서 비대칭이 충분하지 않다는 말이다. 성장 가설이 가속하는 증거(순신규 ARR 증가율이 ARR 증가율을 넘어서는 것)가 나오거나 가격이 내려오면 다시 본다.

**논거**
- 1번·2번 질문: 매출은 5년 뒤 2배를 넘길 수 있다. 강세 시나리오 기준 5년 매출은 기준 연도의 2.86배이고, 매출 성장은 FY2026에도 29.6%로 30% 안팎을 지켰다. 성장 질문은 통과한다. [C:revenue_growth@FY2026] [C:revenue_5y@anderson] [F209]
- 6번·7번 질문: 이익률 여지는 실제로 있다. 총이익률은 70.9%에서 76.7%로 올랐고, 영업이익률은 -82.6%에서 -3.2%로 개선됐으며, FCF 마진은 12.8%다. 규모가 커질수록 레버리지가 나오는 사업 구조와 일치한다. [C:gross_margin@FY2022] [C:gross_margin@FY2026] [C:operating_margin@FY2022] [C:operating_margin@FY2026] [C:fcf_margin@FY2026]
- 3번 질문: 전환비용이 해자일 가능성은 있다. ARR $100K 이상 고객의 ARR이 $1.3B로 +38%라 전체 ARR 성장(+30%)보다 빠르다. 다만 2차 요약에서만 확인되고, 순매출유지율·이탈률이 없어 해자 입증은 아니다. [F211] [F212] [F209] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- 10번 질문이 막힌다. 강세 시나리오(연 매출 성장 23.4%, 출구 P/FCF 40배)를 10년으로 늘려도 주당 가치가 현재가의 4.56배라 5배 문턱에 못 미친다. 내 철학은 드문 일에 거는 것이지만, 걸어서 닿는 크기가 기준 아래라면 이 자리에서 대담함을 이유로 가정을 키워 맞추지 않는다. [C:upside_10y@anderson] [C:revenue_cagr@bull]
- 9번 질문: 시장은 이 기회를 과소평가하지 않는다. EV/매출이 12.72배이고 기본 시나리오 연 수익률 분해에서 멀티플 변화가 -26.6%를 차지해, 매출 성장과 마진 확대의 기여를 거의 다 상쇄한다. 과소평가가 아니라 이미 반영된 가격이다. [C:ev_revenue] [C:expected_irr] [F208]

**사전 부검**
- 사전 부검: 내가 틀렸다면, 대형 고객 안의 확장이 10년간 이어져 매출이 모델의 강세 경로보다 훨씬 오래 가속하는 경우다. ARR $100K 이상 고객의 ARR이 전체보다 빠르게 늘고 있어 그 가능성은 열려 있다. 그러면 지금 사지 않은 것이 너무 일찍 팔거나 과소 보유하는 실수가 된다. [F212] [F209] [F211]
- 사전 부검: 반대로 내가 '반대'를 유지하다 틀리는 경로는 총이익률과 영업 레버리지가 예상보다 빨리 올라 FCF 마진이 강세 시나리오의 28%를 넘는 것이다. 매출 성장 감속이 늦어지면 같은 배수에서도 5배 문턱을 넘을 수 있다. [C:gross_margin@FY2026] [C:fcf_margin@FY2026] [F215]
- 사전 부검: 반대로 성장 가설 자체가 약해지는 경로도 있다. 매출 성장률이 FY2023 이후 한 번도 반등 없이 내려왔고, 순신규 ARR 증가율(+28%)이 ARR 증가율(+30%)보다 낮다. 가속의 증거가 없다는 점이 성장 가설의 가장 큰 약점이다. [C:revenue_growth@FY2023] [C:revenue_growth@FY2026] [F209] [F210]

**반론**
- → 애크먼: 가장 강한 논거는 보고 FCF가 SBC로 부풀려져 있고 SBC 차감 FCF가 음수라는 점이다. 이 점은 맞다. 다만 SBC 차감 FCF는 FY2026 기준 -1.1억에서 이전 해 -1.7억으로 매년 개선 중이고, 내 기준은 현재 현금이 아니라 10년 뒤 크기다. 반대 이유는 SBC 때문이 아니라 강세 시나리오로도 5배에 닿지 못하기 때문이다. 또 안전마진 -61.2%는 기본 시나리오 하나에서 나온 값이고, 확률 가중 IV가 25.33인 점은 같은 방향이다. 이 회사가 대담한 사업이라는 사실이 가격 문제를 지우지는 않는다. [C:fcf_after_sbc@FY2026] [C:fcf_after_sbc@FY2025] [C:upside_10y@anderson] [C:mos]
- → 슬레이터: 단위경제가 입증되지 않아 보류한다는 논거가 가장 강하다. 반박은 이렇다. CAC 회수기간과 NRR이 없다는 이유로 기다리면 아웃라이어의 가장 가치 있는 구간을 놓친다. 총이익률이 70.9%에서 76.7%로 오르고 ARR $100K 이상 고객의 ARR이 전체보다 빠르게 늘어난 흔적은 단위경제가 나쁘지 않다는 정황이다. 다만 나도 이 가격에서는 사지 않으므로 슬레이터의 보류와 결과는 가깝다. 차이는 이유다. 나는 증거 부족이 아니라 5배 비대칭 부족 때문에 물러선다. [C:gross_margin@FY2022] [C:gross_margin@FY2026] [F212] [F209]
- → 레드팀: 가장 강한 부검은 성장 감속이 모델보다 빨라 배수가 거두어진다는 첫 시나리오다. 성장률이 FY2023 이후 반등 없이 내려왔고 순신규 ARR 증가율이 ARR 증가율보다 낮다는 점은 인정한다. 그러나 이것은 경로의 소음이 아니라 성장 가설 자체를 겨누므로 내 반대 근거를 강화한다. 반면 SBC 시나리오는 성장 가설을 깨지 않고 이익의 질만 건드린다. 대형 고객 확장이 이어지면 SBC 비중은 규모와 함께 내려가는 경로의 소음에 가깝다고 본다. [C:revenue_growth@FY2023] [C:revenue_growth@FY2026] [F209] [F210] [C:sbc_to_revenue@FY2026]

**인정한 점**
- 애크먼의 지적대로 보고 FCF는 SBC 차감 후 음수이므로, 내 강세 시나리오의 FCF 마진 28%가 SBC 비중이 충분히 내려와야 성립한다는 점을 인정한다. 그래서 4.56배 상방이 더 낙관적으로 읽힐 위험이 있다.
- 레드팀이 지적한 대로 순신규 ARR 증가율이 ARR 증가율보다 낮아 성장 가속의 증거가 없다. 이 증거가 나오기 전에는 확신을 올리지 않는다.
- 슬레이터의 보류 논거에 일부 동의한다. 가격이 내려오거나 가속 증거가 나오기 전에는 시작 비중도 정당화하기 어렵다.


## 슬레이터 — 보류 (2/5)

> 기회의 크기와 현금 생존은 합격선이다. 종료 ARR이 약 $2.125B이고 성장이 30% 안팎을 지키며, 자체 현금으로 계획을 실행할 수 있다. 그러나 내가 증거로 요구하는 단위경제(CAC 회수기간, 순매출유지율, 이탈률)는 근거에 하나도 없어서 'proven'으로 부를 수 없다. 코드가 계산한 기본 시나리오의 확률 가중 기대 연 수익률은 거의 0%이고, 주가는 이미 성장 지속을 가격에 반영하고 있다. 가설이 틀렸다는 증거는 없지만 입증됐다는 증거도 없다. 그래서 찬성도 반대도 하지 않고 보류한다. 다음 분기들에서 ARR과 영업이익, SBC가 아래 must_be_true대로 움직이면 작은 시작 비중에서 키울 근거가 생긴다.

**논거**
- 크기와 지속성은 합격이다. 종료 ARR은 약 $2.125B이고 전년 대비 30% 늘었으며, 지금 규모에서도 성장이 급락하지 않았다. 다만 2차 요약에서 나온 수치라 원문 대조가 필요하다. [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) [F209]
- 규모가 커지는 동안 총이익률이 70.9%에서 76.7%로 올랐다. 단위경제가 나빠지지 않았다는 정황이지만, 고객 단위의 CAC·NRR·이탈률 증거가 아니므로 'proven'의 근거는 못 된다. [C:gross_margin@FY2022] [C:gross_margin@FY2026]
- 생존 경로는 열려 있다. 코드가 계산한 기본 시나리오 현금 경로는 바닥에서도 0 아래로 내려가지 않고, 순부채/EBITDA가 음수라 외부 자본 의존이 없다. 2022년 교훈(외부 조달 의존)에 걸리지 않는다. [F20] [C:net_debt_to_ebitda]
- 보고 FCF는 SBC를 차감하면 아직 음수다. 흑자 전환은 사실이지만 주주 몫의 경제성은 입증 전이고, 이것이 단위경제를 'unclear'로 두는 이유 중 하나다. [C:fcf_after_sbc@FY2026] [C:fcf_margin@FY2026]
- 가격 쪽은 증거 수준에 비해 앞서 있다. 기본 시나리오 확률 가중 기대 연 수익률은 0.3%에 그치고 손실 확률이 80%로 계산된다. 이 시나리오는 성장 감속을 전제로 하고 있어 가설이 틀렸다는 뜻은 아니지만, 지금 비중을 키울 이유도 못 된다. [C:expected_irr] [C:p_loss]

**사전 부검**
- 매출 성장률이 FY2023 52.3%에서 FY2026 29.6%로 한 번도 반등 없이 내려왔다. 감속이 가속되면 시장이 주는 배수가 먼저 무너진다. [C:revenue_growth@FY2023] [C:revenue_growth@FY2026]
- 희석이 연 3.7% 안팎으로 이어지고 SBC가 FCF를 잠식하는 구조가 지속되면, 매출이 계획대로 커도 주당 가치는 따라오지 않는다. [C:dilution] [C:sbc_to_ocf@FY2026]
- 성장의 질을 대형 고객 확장에 기대고 있다. 대형 고객 3,605곳의 ARR이 빠르게 늘지만 NRR·집중도·가격 인상 후 잔존 기록이 없어, 확장이 꺾이는 신호를 늦게 알아챌 수 있다. [F211] [F212] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 강세 시나리오를 10년으로 늘려도 주당 가치가 현재가의 4.56배라 5배 문턱에 못 닿는다는 것이다. 이 결론은 강세 case 안의 출구 P/FCF 40배와 FCF 마진 가정에 기댄다. 그런데 그 FCF는 SBC를 차감하기 전 값이다. 그래서 반대의 근거를 '5배에 못 미친다'로 세우면 오히려 낙관적인 숫자 위에 서게 된다. 내 반대 없는 보류의 근거는 달라서, 상방이 모자란 것이 아니라 단위경제가 아직 입증되지 않았다는 점이다. 이 둘을 구분해야 앤더슨이 말한 '가속의 증거가 나오면 다시 본다'는 조건이 어느 지표인지 분명해진다. 그 지표는 순신규 ARR이다. [C:upside_10y@anderson] [C:fcf_after_sbc@FY2026] [F210]
- → 애크먼: 애크먼의 가장 강한 논거는 기본 시나리오의 현재가치가 24.99달러인데 주가는 40.29달러라서 안전마진이 -61.2%라는 것이다. 가격 쪽 계산은 인정한다. 다만 그가 '단순하고 예측 가능하지 않다'를 반대 이유로 드는 데는 동의하지 않는다. 순매출유지율과 이탈률이 근거에 없다는 것은 사업이 예측 불가능하다는 증거가 아니라, 우리가 아직 측정하지 못했다는 뜻이다. 나는 정의가 끝나지 않은 시장을 오늘 모델링이 안 된다는 이유로 버리지 않는다. 그래서 반대하지 않고 보류한다. 확률 가중 기대 연 수익률이 0.3%라는 점에서 가격은 비중을 키울 이유가 되지 못한다. 이 부분은 애크먼과 같은 결론이다. [C:mos] [C:iv@base] [F208] [C:expected_irr]
- → 레드팀: 레드팀의 첫 번째 사전 부검은 성장 감속이 모델보다 빠를 수 있다고 본다. 선행 신호로 둔 순신규 ARR이 직전 분기의 1.341억 달러보다 줄어드는 것을 나는 must_be_true에 넣을 가치가 있다고 본다. 순신규 ARR은 ARR 증가율이 꺾이기 전에 먼저 움직이고, 코드가 기계적으로 대조할 수 있다. 두 번째 사전 부검의 SBC 1억 달러 초과 신호는 이미 내 must_be_true에 있다. 레드팀이 말한 SBC 차감 FCF 관점은 맞다. 보고 FCF가 SBC를 빼면 음수라는 점을 내 보류의 근거 중 하나로 두고 있다. [F210] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) [F177] [C:fcf_after_sbc@FY2026]

**참이어야 하는 것**
- [on_track] 종료 ARR이 순신규 ARR 둔화 없이 다음 분기에 22.4억 달러 이상으로 늘어난다
- [at_risk] 순신규 ARR이 직전 분기의 1.341억 달러 이상을 유지해 성장 감속이 가속되지 않는다
- [at_risk] GAAP 영업이익이 SBC 증가에도 흑자를 유지한다
- [at_risk] 분기 SBC가 1억 달러 이하로 묶여 희석이 더 빨라지지 않는다
- [on_track] FY2028 매출이 24억 달러 이상으로 성장 감속이 완만하다

**인정한 점**
- 애크먼의 안전마진 계산을 인정한다. 가격이 증거 수준보다 앞서 있어서 비중을 키울 근거가 없다. 이 결과로 시작 비중은 1% 이하로 유지하고 보류에서 찬성으로 옮기지 않는다.
- 레드팀의 순신규 ARR 신호를 받아들여 must_be_true에 추가한다. 앤더슨의 가속 증거 조건과 같은 지표라서 둘의 기준이 하나로 모인다.
- 앤더슨의 5배 문턱에는 동의하지 않는다. 다만 상방이 부족하다는 그의 결론은 인정하고, 이는 내 보류의 이유를 바꾸지는 않지만 찬성으로 갈 가능성을 더 낮춘다.


## 애크먼 — 반대 (4/5)

> Samsara는 사업의 질은 좋아지고 있지만 지금 가격으로는 담을 수 없다. 기본 시나리오의 현재가치(IV)는 주당 24.99달러인데 주가는 40.29달러라 안전마진이 -61.2%다(C:mos). 기본 시나리오 연 수익률은 0%에 가깝고(C:irr@base), 확률 가중 기대 연 수익률은 +0.3%이며 손실 확률은 80%다(C:expected_irr, C:p_loss). 보고 FCF 마진은 흑자(12.8%)이지만 SBC를 차감하면 음수다(C:fcf_after_sbc@FY2026). 주식 보상으로 지급한 비용을 빼면 주주에게 남는 현금이 아직 없으므로 '현금을 뿜는 사업'이라는 전제가 성립하지 않는다. 좋은 회사를 비싸게 사는 전형적인 경우여서 반대한다. 가격이 크게 내려오거나 SBC 차감 FCF가 양수로 돌아서면 다시 본다.

**논거**
- 가격이 가치보다 크게 높다. 기본 시나리오 현재가치(IV)는 주당 24.99달러, 주가는 40.29달러로 안전마진은 -61.2%다. 레드라인 20%에 크게 못 미친다. [C:mos] [C:iv@base] [F208]
- 기본 시나리오의 수익률 분해를 보면 매출 성장(+16.6%)과 마진 개선(+10.8%)이 멀티플 축소(-26.6%)로 모두 상쇄된다. 지금 가격에는 이미 성장 지속이 들어가 있어 여유가 없다. EV/매출은 12.72배다. [C:irr@base] [C:ev_revenue]
- 보고 FCF는 SBC 때문에 부풀려져 있다. FY2026 FCF 마진 12.8%에 대해 SBC/영업현금흐름이 133.3%이고, SBC 차감 FCF는 마이너스다. 희석도 연 3.7%여서 주당 가치가 계속 깎인다. [C:fcf_margin@FY2026] [C:sbc_to_ocf@FY2026] [C:fcf_after_sbc@FY2026] [C:dilution]
- 단순성과 예측 가능성을 입증하기 어렵다. 순매출유지율, 이탈률, CAC 회수기간이 근거에 없고 단위경제가 'unclear'다. 해자의 증거 등급도 모두 claimed여서 10년 뒤 FCF 범위를 좁게 추정할 수 없다. 이것이 첫 번째 반론이다. [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) [F209] [F211]
- 재무 건전성은 강점이다. 순현금이 있고 순부채/EBITDA가 -5.92배라 자본시장 의존은 없다. 성장 둔화(FY2023 52.3% → FY2026 29.6%) 속에서도 30% 안팎을 지키는 점은 인정한다. 그러나 이는 필요조건일 뿐 싸다는 근거가 아니다. [C:net_debt_to_ebitda] [C:revenue_growth@FY2023] [C:revenue_growth@FY2026]

**사전 부검**
- 사전 부검: 내가 틀렸다면, 성장이 둔화하지 않고 ARR $100K 이상 고객의 확장(+38%)이 계속되어 강세 시나리오(연 수익률 +15.7%)가 현실이 된 경우다. 이때는 기회를 놓친다. 그러나 강세 확률은 20%에 불과하다. [F212] [C:irr@bull]
- 사전 부검: 모델러의 기본 시나리오 출구 배수 30배가 보수적일 수 있다. 시장이 성장주 배수를 계속 유지하면 멀티플 축소(-26.6%)가 일어나지 않아 수익률이 크게 오른다. 다만 이는 가정에 의존한 낙관이다. [C:irr@base]
- 사전 부검: 주가 기준일(2026-09-04)이 44일 오래됐다. 그 사이 주가가 많이 내렸다면 안전마진 판단이 달라질 수 있다. 최신 주가 확인이 필요하다. [F208]

**반론**
- → 앤더슨: 앤더슨은 강세 시나리오로도 10년 상승이 4.56배라 5배 문턱에 못 미친다고 스스로 인정했다. 그런데 강세 확률은 20%에 불과하고 기본 시나리오의 연 수익률은 0%에 가깝다. 앤더슨의 기준으로 가장 낙관적인 경로도 통과하지 못하는 가격이면, 내 기준의 안전마진(-61.2%)은 더 말할 것도 없다. 두 기준이 같은 결론을 가리킨다. 또 앤더슨이 인정한 '대형 고객 확장' 가설은 순매출유지율과 이탈률 근거가 없어 아직 입증되지 않았다. [C:upside_10y@anderson] [C:mos] [C:irr@base] [F212]
- → 슬레이터: 슬레이터는 생존 경로와 현금 생존을 합격선으로 보고 단위경제가 입증되지 않았다는 이유로 보류했다. 그러나 생존은 필요조건이지 가격의 정당화가 아니다. 자체 현금으로 계획을 실행할 수 있다는 점은 인정하지만(순부채/EBITDA -5.92배), 슬레이터 스스로 기대수익률 0.3%와 손실 확률 80%를 인정했다. 증거가 불충분한 데다 가격이 증거보다 앞서 있다면 보류가 아니라 담지 않는 것이 맞다. 보류는 사실상 반대와 같은 결론이다. [C:net_debt_to_ebitda] [C:expected_irr] [C:p_loss]
- → 레드팀: 레드팀의 사전 부검은 SBC 차감 FCF가 음수라는 점과 기본 시나리오의 FCF 마진 22%가 SBC를 뺀 가이던스 21%에 기댄다는 점을 짚었다. 이는 10년 뒤 FCF 범위가 넓어진다는 뜻이고, 내 기준에서는 더 큰 안전마진이 필요하다. 현재 안전마진이 -61.2%인데 FCF 불확실성까지 반영하면 요구되는 격차는 20%보다 훨씬 커진다. 레드팀이 지적한 출구 배수 30배가 높다는 점이 맞다면 기본 시나리오의 IV 24.99달러도 낙관적이다. [C:fcf_after_sbc@FY2026] [C:mos] [F215] [C:operating_margin@FY2026]

**인정한 점**
- 슬레이터와 앤더슨이 지적한 대로 사업의 질은 좋아지고 있다. 영업이익률이 -82.6%에서 -3.2%로 올랐고 FCF 마진은 12.8%다. 사업 자체를 폄하하지 않는다.
- 레드팀이 지적한 주가 기준일 문제(44일 경과)는 인정한다. 다만 가격이 안전마진 20%를 만족하려면 약 20달러 안팎까지 내려와야 하고, 52주 저점 23.38달러보다 낮아서 신규 근거 없이는 결론이 바뀌지 않는다.
- 강세 시나리오에서 연 수익률 +15.7%가 가능하다는 점은 인정한다. 그러나 확률이 20%이고 가정이 SBC 차감 전 FCF에 의존하므로 비중을 둘 근거가 되지 못한다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Samsara는 차량·장비·현장 운영에 센서와 카메라 같은 하드웨어를 깔고, 그 데이터를 클라우드 플랫폼 구독(ARR)으로 과금해 돈을 번다. 종료 ARR은 약 $2.125B로 +30% YoY다(S40, 2차 요약). 매출은 FY2026에 29.6% 성장했고(C:revenue_growth@FY2026) 총이익률은 70.9%에서 76.7%로 올랐다(C:gross_margin@FY2022, C:gross_margin@FY2026). 영업이익률은 -82.6%에서 -3.2%로 개선됐고(C:operating_margin@FY2022, C:operating_margin@FY2026), FCF 마진은 12.8%다(C:fcf_margin@FY2026). 마진 추세는 좋아지고 있다. 그러나 CAC 회수기간, 순매출유지율, 이탈률, 코호트는 근거에 없어서 단위경제를 'proven'으로 부르기는 이르다. GAAP 이익과 FCF는 주식 보상(SBC)에 크게 기댄다(C:sbc_to_revenue@FY2026).

- [unit_economics] 총이익률이 FY2024 73.6%, FY2025 76.1%, FY2026 76.7%로 매년 올랐다. 다만 상승 폭은 줄고 있다. 고객 단위의 CAC 회수기간, NRR, 이탈률, 코호트는 확인하지 못했다. 그래서 개선도 악화도 단정할 수 없고 'unclear'로 둔다. [C:gross_margin@FY2024] [C:gross_margin@FY2025] [C:gross_margin@FY2026]
- [unit_economics] 성장은 둔화하는 중에도 30% 안팎을 지킨다. 매출 성장률은 FY2023 52.3%, FY2024 43.7%, FY2025 33.3%, FY2026 29.6%로 내려왔다. 종료 ARR은 +30%, 순신규 ARR은 $134.1M(+28%)다. 순신규 ARR 증가율이 ARR 증가율보다 약간 낮다는 점은 성장 가속이 아직 확인되지 않았다는 뜻이다. [C:revenue_growth@FY2023] [C:revenue_growth@FY2024] [C:revenue_growth@FY2025] [C:revenue_growth@FY2026] [F209] [F210] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- [customers] 대형 고객 비중이 커지고 있다. ARR $100K 이상 고객 3,605곳의 ARR이 $1.3B(+38%)다. 추정: 이는 전체 ARR $2.125B의 약 61%다. 상위 고객 집중도나 고객별 매출 비중은 근거에 없어 집중 위험은 평가하지 못한다. [F211] [F212] [F209] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- [industry] 산업 구조는 근거가 얇다. 경쟁사 공시나 점유율 데이터가 없다. 뉴스에서는 연료 가격 변동 환경에서 Fuel Command Center를 내놓았다는 제품 확장(S23)과 AI 위험이 낮다는 논조(S27) 정도만 확인된다. 모두 보도이고, 회사 발표를 되풀이한 것일 수 있다. [S23](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNU1QyWk9pdjBfLXZIaXRCVGlwY1kwSFB2ZTBXUHkwczlnWUZpWGpBT3A5bUJBb251dkxTZERBX3ZrdEs5dDBXeXYwYjJ4WGVoRXF1V1BieV9fTExDZVJKbnFMYU9Zd18xUmoyb0ZJdV9KT2hNYUpzbTFPUndnaHBvN2dNWUFqRG5rRWo4OEJpM1VDVmRKeFJhUnp4bXBlZERIUVBBS2VIbjhFemlYT1ZKSXotMmpmejcwQlhxVF8tUC1IRnhCMTZ6bWt2RVBhcTZtS0lPMHhRdUZXMFRL?oc=5) [S27](https://news.google.com/rss/articles/CBMinAFBVV95cUxOR1U1Z2xJQTJONFkzVFp4Zm5NSjB1N3BzaVozbjg0RkkyYjhVZ2o2UHh3Q3RTUlJKRmhsWGt1UE1mWTR3NkMycm5lQmlzMFV5VHcyV0ZUcVBWRk1wS1NuSG92aF9UN1VYSUxPSnI3dWRudG1kZ1htRG9lc0lwT1hRMXNXVUtSaGlpOWJmck9fd2pBeGdNdUI5bjM0V1k?oc=5)
- [unit_economics] 이익의 질은 SBC 의존이 크다. FY2026 SBC는 매출의 19.5%이고 영업현금흐름의 133.3%다. SBC를 빼면 FCF는 -1.1억 USD다. 흑자 전환(FCF 마진 12.8%)은 사실이지만, 주주에게 돌아갈 경제성은 SBC를 비용으로 볼 때 아직 음(-)이다. 희석 주식 수도 연 3.7% 늘고 있다. [C:sbc_to_revenue@FY2026] [C:sbc_to_ocf@FY2026] [C:fcf_after_sbc@FY2026] [C:fcf_margin@FY2026] [C:dilution]
- [runway] 재투자 활주로는 길어 보이지만 GAAP 수익성은 아직 얇다. FY2027Q2 매출은 5.1억 USD인데 영업이익은 488만 USD이고, 같은 분기 SBC가 9,638만 USD다. 가이던스의 비GAAP 영업이익률 21%(FY2027)와 GAAP 수치의 간극이 대부분 SBC에서 나온다. 현금은 2.9억 USD이고 순부채/EBITDA는 -5.92배라 자금 조달 부담은 크지 않다. 연구개발은 FY2027Q2 1.0억 USD로 계속 늘고 있다. [F157] [F127] [F177] [F215] [F20] [C:net_debt_to_ebitda] [F167]
- [unit_economics] 운전자본 신호는 혼재한다. 이연수익은 FY2025 5.6억에서 FY2027Q2 7.3억 USD로 늘었다. 선수금 증가는 구독 선결제가 늘었다는 해석과 일치한다. 반면 DSO가 FY2024 63.0일에서 FY2026 72.5일로 늘었고, FY2025 재고 증가율이 매출 증가율을 41.7%p 웃돈다. 하드웨어 재고와 매출채권 회수는 단위경제 해석에서 계속 지켜볼 항목이다. [F44] [F50] [C:dso@FY2024] [C:dso@FY2026] [C:inventory_gap]
- [industry] 가격 결정력은 확인하지 못했다. 인상 후 이탈 기록이 없고, 주가는 Q2 어닝 서프라이즈(매출 $508.44M 대 추정 $483.26M, S39) 뒤에도 52주 범위($23.38~47.47) 안에서 움직인다(S43). 시장의 기대는 성장 지속에 모여 있고, 사업 근거는 이를 독립적으로 검증해 주지 않는다. [S39](https://www.itiger.com/news/2664435814) [S43](https://www.investing.com/equities/samsara)
- [claimed] 하드웨어 설치와 워크플로 통합에서 오는 전환비용이 해자일 가능성이 있다. 흔적으로는 ARR $100K 이상 고객이 3,605곳이고 이 고객들의 ARR이 $1.3B로 +38% 늘었다. 전체 ARR 성장(+30%)보다 빠르므로 대형 고객 안에서 확장이 일어나는 것으로 보인다. 다만 이 수치는 2차 요약(S40)에서만 나왔고, NRR·이탈률·가격 인상 후 잔존 기록은 확인하지 못했다. [F211] [F212] [F209] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- [claimed] 매출이 FY2022 4.3억에서 FY2026 16.2억 USD로 커지는 동안 총이익률이 70.9%에서 76.7%로 올랐다. 규모의 경제와 일치하는 흔적이다. 다만 경쟁사(Geotab 등) 대비 마진이나 점유율 추이가 없어서 해자의 입증이라기보다 일치하는 정황이다. [C:gross_margin@FY2022] [C:gross_margin@FY2026] [F148] [F152]

### 경영진·자본배분 — mixed

제공된 근거만으로는 경영진의 정렬과 신뢰도를 확정하기 어렵다. 보상 지표(DEF 14A, S6), 내부자 매매, 창업자 지분, 어닝콜, 과거 분기별 가이던스 이력은 확인되지 않았다. 확인되는 것은 희석과 자본배분의 숫자다. SBC는 매출 대비 비중이 줄었지만(FY2022 53.4% → FY2026 19.5%) 절대액은 늘었고, FCF의 상당 부분이 주식 보상이다(SBC/영업현금흐름 133.3%). SBC 차감 FCF는 FY2026에도 음수(-1.1억 USD)다. 희석 주식 수는 연 3~4% 늘었고 최근 자사주 매입 기록은 없다. 이 사업에서 경영진은 매출 성장과 마진 개선을 이뤄 왔지만, 주주가치 정렬을 입증하는 증거는 부족해 mixed로 둔다.

- [compensation] 보상 연동 지표, 베스팅 기간, 경영진 보상 규모는 DEF 14A(S6)가 근거 목록에 있으나 내용을 확인하지 못했다. 장기 지표(FCF·ROIC·주당가치)인지 단기 EPS·조정 지표인지 판단할 근거가 없다. 근거 없음. [S6](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039492/iot-20260601.htm)
- [insider] 창업자·경영진 지분과 최근 내부자 매수·매도는 확인하지 못했다. 정렬 여부를 판단할 증거가 없다. 근거 없음. [S6](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039492/iot-20260601.htm)
- [guidance] 가이던스는 상향 추세로 보인다. 직전 FY27 매출 가이던스 $2.005~2.013B에서 Q2 발표 후 $2.043~2.047B로 올랐고, Q2 매출 $508.44M은 추정 $483.26M을 웃돌았다. 다만 직전 가이던스 값은 2차 요약에 있고, 최근 4개 분기의 가이던스 이력은 없어 적중률 계산이 불가능하다. 신뢰도는 판단 보류. [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results) [S39](https://www.itiger.com/news/2664435814) [F213] [F214] [F215]
- [dilution] 희석 주식 수는 FY2023 5.1억에서 FY2026 5.7억, FY2027Q2 5.9억으로 늘었다. 연 증가율은 FY2024·FY2025 4.0%, FY2026 3.1%다. 코드는 연 3.7% 증가로 희석 신호를 켰다. SBC/매출은 FY2022 53.4%에서 FY2026 19.5%로 낮아졌으나, 코드는 이 수준도 10% 기준을 넘는다고 본다. 분기 SBC는 FY2027Q2에 9,638만 USD로 직전 분기(7,747만)보다 늘었다. [C:share_change@FY2026] [C:sbc_to_revenue@FY2022] [C:sbc_to_revenue@FY2026] [C:dilution] [C:sbc_to_revenue] [F177] [F176]
- [dilution] SBC/영업현금흐름은 FY2025 211.1%, FY2026 133.3%다. FY2026 FCF 2.1억 USD(마진 12.8%)는 SBC 3.1억 USD를 차감하면 음수가 된다(SBC 차감 FCF -1.1억 USD). 보고 FCF는 주주에게 돌아가는 현금이 아니라 주식으로 보상을 지급한 뒤의 숫자다. [C:sbc_to_ocf@FY2026] [C:fcf_margin@FY2026] [C:fcf_after_sbc@FY2026] [C:sbc@FY2026]
- [capital_allocation] 자사주 매입 기록은 FY2022 5,000(단위 USD 그대로) 외에 FY2023·FY2024 0이고, 그 이후는 확인하지 못했다. 희석을 상쇄하는 매입은 없었다. 이 회사는 상장 이후 현금 창출 전환기라 재투자가 중심으로 보이며, 부채는 계산표에 없다(순현금 FY2026 3.2억, FY2027Q2 2.9억). [F1] [F2] [F3] [C:net_cash@FY2026] [F20]
- [capital_allocation] 설비투자는 매출 대비 낮다(FY2026 2,877만 USD, 매출 16.2억). 연구개발은 FY2026 3.4억, FY2027Q2 분기 1.0억으로 꾸준히 늘고 있다. 재투자 중심의 배분이며, 인수 이력과 투자 수익률은 확인하지 못했다. ROIC는 FY2026 -2.4%로 아직 음수지만 -522.4%(FY2022)에서 개선 중이다. [C:capex@FY2026] [C:revenue@FY2026] [C:rnd@FY2026] [F167] [C:roic@FY2026] [C:roic@FY2022]
- [capital_allocation] 영업이익은 FY2026 -5,258만 USD에서 FY2027Q1 720만, Q2 488만 USD로 GAAP 흑자 전환을 이뤘다. 비GAAP 영업이익률 가이던스는 21%이고 GAAP과의 차이는 대부분 SBC로 보인다. 경영진은 비GAAP 지표 위주로 마진을 발표하는 것으로 읽히나, 이는 2차 요약에 근거한 추정이다. [C:operating_margin@FY2026] [F126] [F127] [F215] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)

### 회계 품질 — watch

현금흐름과 이연매출이 이익·매출 증가와 같은 방향으로 움직여서, 숫자 자체를 믿을 수 없다는 증거는 없다. 영업현금흐름은 FY2025부터 양수이고 발생액 비율은 전 기간 음수다(C:accruals_ratio@FY2026 -10.7%). 이연매출도 꾸준히 늘었다(F44→F48). 다만 보는 방식을 조정해야 한다. (1) SBC가 매출의 19.5%이고 영업현금흐름의 133.3%라서, 보고 FCF는 SBC를 차감하면 -1.1억 USD다(C:fcf_after_sbc@FY2026). (2) 희석 주식 수가 연 3.7% 늘고 있다. (3) 최근 GAAP 순이익은 영업이익보다 영업외 수익이 훨씬 크다. FY2027Q1은 영업이익 720만, 세전이익 4,893만, FY2027Q2는 영업이익 488만, 세전이익 1,753만이다. 그래서 PER 262.71x는 의미가 작고, 이익의 질은 영업이익과 SBC 차감 FCF로 봐야 한다. 재고 신호는 FY2024 저점에서 되돌아온 것이다. 감사의견, 감사인 변경, 정정, 특수관계자 거래는 확인하지 못했으므로 clean이 아니라 watch로 둔다.

- [concern] sbc_to_revenue: SBC/매출은 FY2022 53.4%에서 FY2026 19.5%로 꾸준히 내려왔지만 여전히 문턱 10%의 약 2배다. 분기 SBC는 FY2027Q1 7,747만에서 FY2027Q2 9,638만으로 다시 커졌다. 현금 비용이 아니어도 주주에게 가는 실제 비용이므로, 수익성은 SBC를 비용으로 넣은 영업이익으로 판단해야 한다. GAAP 영업이익은 FY2027Q2에 겨우 흑자(488만)다. [C:sbc_to_revenue@FY2026] [C:sbc_to_revenue@FY2022] [F176] [F177] [F127]
- [concern] sbc_to_ocf: FY2026 SBC는 영업현금흐름의 133.3%(FY2025는 211.1%)로, 보고 FCF 흑자(FCF 마진 12.8%)는 SBC를 현금 대신 주식으로 지급한 덕분이다. SBC를 차감한 FCF는 FY2026에도 -1.1억 USD다. 방향은 개선 중(FY2025 -1.7억)이지만 아직 마이너스이므로 FCF 기반 밸류에이션은 SBC 차감값을 함께 봐야 한다. [C:sbc_to_ocf@FY2026] [C:sbc_to_ocf@FY2025] [C:fcf_margin@FY2026] [C:fcf_after_sbc@FY2026] [C:fcf_after_sbc@FY2025]
- [benign] inventory_gap: 신호가 걸린 FY2025 재고 증가율-매출 증가율 41.7%p는 FY2024의 이례적인 재고 저점에서의 반등이다. FY2024 재고는 2,224만으로 DIO 32.9일까지 내려갔다가 FY2025에 3,891만으로 복귀했고 DIO는 47.6일이었다. FY2026에는 DIO가 46.7일로 안정됐고, 재고 증가가 매출 증가를 계속 앞서는 패턴은 아니다. 하드웨어(게이트웨이·카메라) 재고 규모도 매출 대비 작다. 최근 분기 재고는 FY2027Q2 5,703만으로 완만히 늘고 있어 DIO 추이는 계속 지켜볼 일이다. [C:inventory_gap] [F93] [F94] [F98] [F100] [C:dio@FY2024] [C:dio@FY2025] [C:dio@FY2026]
- [concern] dilution: 희석 주식 수가 연평균 3.7% 늘어 문턱 3%를 넘는다. FY2025 5.6억, FY2026 5.7억에서 FY2027Q2 5.9억으로 늘었고 자사주 매입 기록은 FY2022 이후 없다. FY2023 이후 연 주식 수 변화는 FY2024 4.0%, FY2025 4.0%, FY2026 3.1%이므로 주당 가치는 SBC가 만드는 희석만큼 깎인다. 총 주식 수가 아닌 희석 기준이라는 점은 감안해야 한다. [C:dilution] [C:share_change@FY2026] [C:share_change@FY2025] [F54] [F55] [F60] [F3]
- [watch] 최근 GAAP 순이익은 영업이익보다 영업외 수익이 크게 만든 것이다. FY2027Q1 영업이익 720만 대비 세전이익은 4,893만, FY2027Q2 영업이익 488만 대비 세전이익은 1,753만이다. 이자수익으로 보이나 구성은 확인하지 못했다. 순이익 흑자 전환(FY2026Q3 이후)은 영업 개선과 영업외 수익이 섞인 결과이므로 PER 262.71x는 영업 수익성의 척도가 아니다. [F126] [F136] [F127] [F137] [F109] [F110]
- [info] 현금흐름 품질은 대체로 양호하다. 영업현금흐름은 FY2025부터 흑자이고 발생액 비율은 전 기간 음수다(순이익보다 현금이 큼). 이연매출은 FY2025 5.6억에서 FY2027Q2 7.3억으로 꾸준히 늘었고, 매출 가속 대비 이연매출 감소(deferred_revenue 신호)는 없다. 선수금 증가는 SBC·이연매출이 OCF를 부풀리는 요인이기도 하다. [C:accruals_ratio@FY2026] [C:accruals_ratio@FY2025] [F44] [F48] [F50] [F115] [F117]
- [watch] DSO는 FY2025 68.4일에서 FY2026 72.5일로 늘었다. 매출채권 증가율이 매출 증가율을 앞선 것으로 문턱 신호(receivables_gap)는 걸리지 않았지만, 연말·분기말 대형 계약 집중 청구의 영향일 수 있다. 분기별로 FY2027Q1 2.8억에서 FY2027Q2 3.4억으로 뛴 것도 확인이 필요하다. [C:dso@FY2025] [C:dso@FY2026] [F145] [F146] [F147]
- [info] 코드의 non_gaap 신호는 걸리지 않았다. 다만 가이던스는 비GAAP 영업이익률 21% 기준(F215)인데 GAAP 영업이익률은 FY2026 -3.2%이므로, 두 기준의 차이는 대부분 SBC에서 나온다. 가이던스를 인용할 때는 GAAP과 비GAAP을 구분해야 한다. 다만 S40이 2차 요약이어서 원문 대조가 필요하다. [F215] [C:operating_margin@FY2026] [C:sbc_to_revenue@FY2026] [S40](https://secure.businesswire.com/news/home/20260903120692/en/Samsara-Reports-Second-Quarter-Fiscal-Year-2027-Financial-Results)
- [info] 코드 신호의 restatement(8-K 4.02)와 auditor_change(4.01)는 걸리지 않았다. 그러나 감사의견(계속기업 의문·핵심감사사항), 특수관계자 거래, DEF 14A의 보상 지표는 이번 수집에서 확인하지 못했다. 10-K(S9)로 검증이 필요한 항목이다. [S9](https://www.sec.gov/Archives/edgar/data/1642896/000162828026018167/iot-20260131.htm) [S6](https://www.sec.gov/Archives/edgar/data/1642896/000162828026039492/iot-20260601.htm)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) 성장 감속이 모델보다 빠르고, 시장이 성장주 배수를 거둔다. 주가 $40.29는 EV/매출 12.72배(C:ev_revenue)로 ARR +30% 지속을 이미 반영한다. 매출 성장률은 FY2023 52.3%에서 FY2026 29.6%로 한 번도 반등 없이 내려왔고(C:revenue_growth@FY2026), 순신규 ARR 증가율(+28%)은 ARR 증가율(+30%)보다 낮다(F210, F209). 대형 고객 확장이 멈추면 성장은 한 자릿수로 꺾인다. 그러면 '성장+이익' 프리미엄이 사라져 출구 배수가 18배 부근(bear)까지 내려가고 5년 수익률은 −20%대에 머문다(C:p_loss 80%). 여기에 52주 저점($23.38)까지 되돌림과 FCF 마진 정체가 겹치면 −60%에 이른다. [C:ev_revenue] [C:revenue_growth@FY2026] [F209] [F210] [C:p_loss] [S43](https://www.investing.com/equities/samsara)
- (15%) SBC가 줄지 않아 '보고 FCF'가 주주 몫으로 인정받지 못한다. FY2026 SBC는 영업현금흐름의 133.3%이고 SBC 차감 FCF는 −1.1억 USD다(C:sbc_to_ocf@FY2026, C:fcf_after_sbc@FY2026). 분기 SBC는 FY2027Q1 7,747만에서 FY2027Q2 9,638만으로 다시 뛰었다(F176, F177). 인재 유지를 위해 보상이 늘고 희석이 연 3.7%로 이어지면(C:dilution), 주당 가치는 매출이 커져도 제자리다. 시장이 P/FCF 대신 SBC 차감 FCF로 가치를 매기기 시작하면, 237.9억 USD 시가총액(C:market_cap)을 정당화할 수 있는 현금창출이 없어 배수가 급격히 낮아진다. [C:sbc_to_ocf@FY2026] [C:fcf_after_sbc@FY2026] [F176] [F177] [C:dilution] [C:market_cap]
- (15%) 대형 고객 중심의 확장이 경기 사이클·가격 경쟁에 취약하다. ARR $100K 이상 고객 3,605곳이 ARR의 약 61%를 차지한다(F211, F212, F209). 차량·운송 고객이 비용을 줄이거나 경쟁사(Geotab 등)가 가격을 깎으면 신규 계약과 확장이 동시에 멈추고, 선결제 계약 기간이 짧아져 이연매출이 줄기 시작한다. 이탈률·NRR·CAC 회수기간은 근거에 없어(business.json의 unclear) 약화를 늦게 알아챈다. 하드웨어 재고(F100)와 매출채권 DSO 72.5일(C:dso@FY2026)이 늘어난 채 매출이 꺾이면 현금 전환도 나빠진다. [F211] [F212] [F209] [F50] [F100] [C:dso@FY2026]
- (10%) GAAP 수익성이 얇아 한 번의 가이던스 실망에도 적자로 돌아선다. FY2027Q2 영업이익은 488만 USD인데 같은 분기 SBC는 9,638만 USD이고(F127, F177), 순이익을 만든 것은 영업외 수익이다(세전이익 F137 1,753만). 증권사 8곳이 모두 매수 의견에 목표가 $51~58로 쏠려 있어(S39) 서프라이즈는 이미 가격에 있다. 성장 투자(R&D 분기 1.0억, F167)가 늘거나 매출이 소폭만 못 미쳐도 영업이익이 마이너스로 돌아서면, 'PER 262.71배'(C:pe)를 받쳐 줄 이익 서사가 사라지고 쏠림이 한꺼번에 풀린다. [F127] [F177] [F137] [S39](https://www.itiger.com/news/2664435814) [F167] [C:pe]
- 약한 가정 `base.exit_multiple`: 기본 시나리오의 출구 P/FCF 30배는 연 매출 성장이 12%로 내려온 시점의 배수로는 높다. 코드의 수익률 분해에서 멀티플 변화가 이미 −26.6%로 가장 큰 항목이며, 민감도표에서 배수가 ×0.75이면 기본 수익률은 −4.9%다. 약세 시나리오는 18배를 쓰는데 두 값의 간극이 크고, 이 가정 하나가 기본 시나리오의 부호를 정한다. 게다가 이 배수는 SBC 차감 전 FCF에 곱해진다. [C:expected_irr] [C:p_loss] [C:fcf_after_sbc@FY2026]
- 약한 가정 `base.fcf_margin`: FCF 마진 22%는 FY2026 실적 12.8%에서 거의 두 배 가까이 오르는 가정이다(C:fcf_margin@FY2026). 근거는 비GAAP 영업이익률 가이던스 21%(F215)인데, 이는 SBC를 뺀 기준이고 GAAP 영업이익률은 FY2026 −3.2%다(C:operating_margin@FY2026). SBC 비중이 19.5%에서 충분히 내려오지 않으면 22%는 현금이 아니라 주식 보상으로 만든 숫자가 된다. [C:fcf_margin@FY2026] [F215] [C:operating_margin@FY2026] [C:sbc_to_revenue@FY2026]
- 약한 가정 `base.revenue_growth`: 기본 시나리오 1년차 성장 27%는 FY2027 가이던스 상단 이상을 요구하고, 이후 매년 3~5%p씩만 완만하게 감속한다고 가정한다. 성장률이 4년 연속 내려온 것은 사실이지만, 감속 폭이 일정하다는 보장은 없다. 기저율 표가 없어(계산 경고) 18.1% 5년 복리가 얼마나 드문 일인지 검증되지 않았고, 모델이 컨센서스와 사실상 같아 반대편 시나리오가 약세 30%에만 몰려 있다. [F213] [C:revenue_growth@FY2026] [C:consensus_diff@revenue@FY2027]

## 검증 (L6)

주장 71개 — supported 59 · unsupported 10 · contradicted 0 · leap 2 · 미검증 0

- [unsupported] 레드팀: 기본 시나리오의 출구 P/FCF 30배는 연 매출 성장이 12%로 내려온 시점의 배수로는 높다. 코드의 수익률 분해에서 멀티플 변화가 이미 −26.6%로 가장 큰 — 출처 없는 숫자 26.6%, 4.9% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 슬레이터: 애크먼의 가장 강한 논거는 기본 시나리오의 현재가치가 24.99달러인데 주가는 40.29달러라서 안전마진이 -61.2%라는 것이다. 가격 쪽 계산은 인정한다. 다 — 없는 근거 인용: C:mos
- [unsupported] 앤더슨: 가장 강한 논거는 보고 FCF가 SBC로 부풀려져 있고 SBC 차감 FCF가 음수라는 점이다. 이 점은 맞다. 다만 SBC 차감 FCF는 FY2026 기준 -1. — 없는 근거 인용: C:mos
- [unsupported] 애크먼: 가격이 가치보다 크게 높다. 기본 시나리오 현재가치(IV)는 주당 24.99달러, 주가는 40.29달러로 안전마진은 -61.2%다. 레드라인 20%에 크게 못 미 — 없는 근거 인용: C:mos
- [unsupported] 애크먼: 사전 부검: 모델러의 기본 시나리오 출구 배수 30배가 보수적일 수 있다. 시장이 성장주 배수를 계속 유지하면 멀티플 축소(-26.6%)가 일어나지 않아 수익률이 — 출처 없는 숫자 26.6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 앤더슨: 9번 질문: 시장은 이 기회를 과소평가하지 않는다. EV/매출이 12.72배이고 기본 시나리오 연 수익률 분해에서 멀티플 변화가 -26.6%를 차지해, 매출 성장 — 출처 없는 숫자 26.6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 애크먼: 기본 시나리오의 수익률 분해를 보면 매출 성장(+16.6%)과 마진 개선(+10.8%)이 멀티플 축소(-26.6%)로 모두 상쇄된다. 지금 가격에는 이미 성장 지 — 출처 없는 숫자 16.6%, 26.6% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 회계 품질: 희석 주식 수가 연평균 3.7% 늘어 문턱 3%를 넘는다. FY2025 5.6억, FY2026 5.7억에서 FY2027Q2 5.9억으로 늘었고 자사주 매입 기록은 — 희석 수치와 주식 수는 맞지만, 인용된 매입 기록은 FY2022·FY2024뿐이라 'FY2022 이후 없다'는 FY2025 이후까지 확대한 과장이다.
- [unsupported] 슬레이터: 생존 경로는 열려 있다. 코드가 계산한 기본 시나리오 현금 경로는 바닥에서도 0 아래로 내려가지 않고, 순부채/EBITDA가 음수라 외부 자본 의존이 없다. 20 — 순부채/EBITDA 음수와 현금은 맞지만 '기본 시나리오 현금 경로가 0 아래로 내려가지 않는다'는 인용 자료에 없다.
- [unsupported] 애크먼: 앤더슨은 강세 시나리오로도 10년 상승이 4.56배라 5배 문턱에 못 미친다고 스스로 인정했다. 그런데 강세 확률은 20%에 불과하고 기본 시나리오의 연 수익률은 — 없는 근거 인용: C:mos
- [unsupported] 애크먼: 레드팀의 사전 부검은 SBC 차감 FCF가 음수라는 점과 기본 시나리오의 FCF 마진 22%가 SBC를 뺀 가이던스 21%에 기댄다는 점을 짚었다. 이는 10년  — 없는 근거 인용: C:mos
- [leap] 모델러: 추정: FY2027은 가이던스(F213, $2.043~2.047B)보다 소폭 높은 성장으로 마친다. Q2 매출이 추정을 웃돌았고(S39) 가이던스가 상향된 흐름이 — FCF 마진 22%를 12.8%와 21%의 '중간쯤'이라 했지만 22%는 두 값보다 높고, 21%는 비GAAP 영업이익률이라 FCF 마진 근거로 쓰기엔 비약이다.

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
| 주가 (price) | 40.29 USD/share (2026-09-04, F208) |
| 희석 주식 수 (shares) | 5.9억 |
| 시가총액 (market_cap) | 237.9억 USD |
| 순현금 (net_cash) | 2.9억 USD |
| EV (ev) | 235.0억 USD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 12.72x |
| PER (pe) | 262.71x |
| 순부채/EBITDA (net_debt_to_ebitda) | -5.92x |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 19.5% > 10%
- [watch] sbc_to_ocf (C:sbc_to_ocf): SBC/영업현금흐름 — FCF의 상당 부분이 주식 보상 133.3% > 50%
- [watch] inventory_gap (C:inventory_gap): FY2025 재고 증가율 - 매출 증가율 41.7% > 15%
- [watch] dilution (C:dilution): 희석 주식 수 연 3.7% 증가 > 3%

### 시나리오 가치 — 5년, 할인율 10% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 30% | 29.6억 USD | 12.8% | 14% | 18x | 13.18 | 8.18 | -20.0% |
| 기본 | 50% | 37.2억 USD | 18.1% | 22% | 30x | 40.24 | 24.99 | -0.0% |
| 강세 | 20% | 46.2억 USD | 23.4% | 28% | 40x | 83.62 | 51.92 | +15.7% |

확률 가중: 주당 가치 40.80 · IV 25.33 · 기대 연 수익률 +0.3% (C:expected_irr) · 손실 확률 80% (C:p_loss) · 현재 주가 40.29

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +16.6% · 마진 변화 +10.8% · 멀티플 변화 -26.6% · 주식 수 변화 -3.0% · 현금 축적 +2.1% = -0.0%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -9.4% | -4.8% | -0.9% |
| +0%p | -4.9% | -0.0% | +4.1% |
| +5%p | -0.4% | +4.8% | +9.1% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2027 | 20.6억 USD | 14.7% | 3.0억 USD | 6.1억 | 5.9억 USD |
| FY2028 | 24.9억 USD | 16.5% | 4.1억 USD | 6.3억 | 10.0억 USD |
| FY2029 | 29.1억 USD | 18.3% | 5.3억 USD | 6.5억 | 15.4억 USD |
| FY2030 | 33.2억 USD | 20.2% | 6.7억 USD | 6.6억 | 22.1억 USD |
| FY2031 | 37.2억 USD | 22.0% | 8.2억 USD | 6.8억 | 30.2억 USD |

### 컨센서스 대비 (C:consensus_diff@지표@기간)

| 지표 | 기간 | 컨센서스 | 기본 시나리오 | 차이 |
|---|---|---|---|---|
| revenue | FY2027 | 19.7억 USD | 20.6억 USD | +4.3% |
| revenue | FY2027 | 20.1억 USD | 20.6억 USD | +2.3% |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- base 시나리오 매출 성장: 연 18.1% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 23.4% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=4.56x, revenue_5y=2.86x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=2.9억 USD
- 애크먼 case={"from": "base"}: price=40.3, net_debt_to_ebitda=-5.92x, leveraged=아니오, intrinsic_value=25.0, mos=-61.2%

### 계산 경고

- 주가 기준일 2026-09-04이 as_of(2026-10-18)보다 44일 오래됨
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

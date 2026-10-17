# Astera Labs (ALAB) 리서치 보고서 — 기준일 2026-10-18

**반대 우세** — 찬성 1 · 반대 2 · 보류 0 · 확신 가중 점수 -0.27 (−1~+1)

- 게이트: 근거 충분성 ✓ → 회계 품질 ✓ → 모델 ✓

## 1. Variant perception

- 시장이 반영한 것: 주가는 EV/매출 C:ev_revenue, PER C:pe 수준으로 높은 성장이 오래 이어진다는 전제를 이미 담고 있다. 다만 PER은 2분기 세금 환급(F77)이 포함돼 세전이익(F118)보다 부풀려진 값이다. FY2026·FY2027 연간 컨센서스는 확보하지 못해 컨센서스와의 직접 비교는 하지 못했다.
- 우리가 다르게 보는 점: 기본 시나리오의 기대수익률이 요구수익률을 크게 넘지 않을 것으로 본다. 단기 실적(3분기 가이던스 F185)이 맞아도 SBC 차감 이익과 성장 둔화가 반영되면 현재 배수는 정당화되기 어렵다. 즉 우리는 시장이 틀렸다고 주장하지 않고, 가격이 기본 시나리오를 거의 그대로 반영한 상태라고 본다. 뚜렷한 variant는 약하다.
- 왜 우리가 맞는가: 설계 수주·고객 집중도·제품별 매출 같은 해자 근거가 확인되지 않았고(business.json의 `claimed` 수준), 믹스 변화로 총이익률 가이던스가 낮아진다(F187). 이익의 질 문제(SBC, 세금 환급)도 있다. [C:ev_revenue] [C:pe] [F77] [F118] [F185] [F187]
- 촉매: 3분기 실적 발표에서 매출 가이던스 상단 달성 여부, 총이익률 방향, 제품별 매출 공개.
- 시점: 2026년 4분기 중 (3분기 실적 발표)

## 2. 시나리오 분포와 기대수익률

확률 가중 IV **161.39** vs 주가 285.82 · 기대 연 수익률 **-1.0%** · 손실 확률 80%

| 시나리오 | 확률 | 주당 가치 | IV | 연 수익률 | 근거 |
|---|---|---|---|---|---|
| 약세 | 30% | 40.91 | 24.28 | -32.2% | FY2026은 상반기 실적과 3분기 가이던스(F185)가 이미 확정에 가까워 성장률이 높게 나온다. 이후 하이퍼스케일러의 AI 설비투자가 소화 국면에 들어가 물량이 줄고, 가속기 플랫폼 일부가 자체 연결 칩으로 옮겨 |
| 기본 | 50% | 281.02 | 166.77 | -0.3% | FY2026은 상반기 실적과 3분기 가이던스(F185)를 4분기에 이어 붙인 값으로 연 115% 성장을 가정한다. 이후에는 기저가 커지면서 성장이 둔화한다. 스위치 Scorpio와 신규 리타이머 제품군(S29, S3 |
| 강세 | 20% | 595.82 | 353.59 | +15.8% | 엔비디아 랙이 타사 가속기를 받아들이는 흐름(S34)과 Scorpio 스위치 램프(S30)가 겹쳐 콘텐츠 가치가 서버당 크게 늘어난다. 매출이 설계 수주 확대로 가속되고 레버리지가 계속되어 FCF 마진이 올라간다.  |

## 3. 반증 조건 (thesis break)

- [자료 없음] 앤더슨: 3분기 매출이 가이던스 하단 미달 — 성장 가속 가설 훼손 — `revenue < 5.4e+08` (FY2026Q3)
- [자료 없음] 앤더슨: 총이익률이 가이던스(약 72%) 아래로 더 내려가면 가격 압력 가설 확정 — `non_gaap_gross_margin < 0.7` (FY2026Q3)
- [수동 확인] 앤더슨: 상위 고객 이탈 또는 주요 가속기 플랫폼의 자체 연결 칩 전환 공시 — 수동 확인
- [자료 없음] 슬레이터: 3분기 매출이 가이던스 하단 미달 (이 경우 수요 가설 자체가 약화됨) — `revenue < 5.4e+08` (FY2026Q3)
- [자료 없음] 슬레이터: Non-GAAP 총이익률이 70% 아래로 하락 (가격 압력 가설 강화) — `non_gaap_gross_margin < 0.7` (FY2026Q3)
- [수동 확인] 슬레이터: 다음 실적에서 제품별 매출과 상위 고객 비중이 공개돼 지속성 증거가 확인되면 재평가 — 수동 확인
- [미충족] 애크먼: 주가가 기본 시나리오 현재가치(약 167달러) 아래로 내려오면 안전마진이 생겨 재검토 — `price < 167`
- [자료 없음] 애크먼: 가이던스 상단 초과와 총이익률 유지가 함께 확인되면 성장 가정 상향 여부 재검토 — `revenue >= 5.6e+08` (FY2026Q3)
- [수동 확인] 애크먼: 설계 수주·상위 고객 비중 공시로 해자가 입증되면 단순성·예측가능성 판단 재평가 — 수동 확인
- [충족 — 훼손] 레드팀: 3분기 매출이 가이던스 하단(5.4억 달러) 미달 — 수요 소화 국면 진입 — `revenue < 5.4e+08`
- [미충족] 레드팀: 3분기 Non-GAAP 총이익률이 가이던스(약 72%)보다 낮음 — 믹스가 아니라 가격 압력이 진행 중 — `non_gaap_gross_margin < 0.72`
- [미충족] 레드팀: 3분기 SBC가 2분기 6,399만 달러를 넘어 계속 증가 — 희석과 비용 압력이 이어지는 중 — `sbc > 6.4e+07`
- [충족 — 훼손] 레드팀: 3분기 재고가 2분기 1.1억 달러를 넘어 계속 증가 — 선반영 재고 누적 진행 중 — `inventory > 1.1e+08`

## 4. 모니터링 KPI (예측 — 교정의 재료)

| ID | 지표 | 기간 | 기대 | 확률 | 이유 |
|---|---|---|---|---|---|
| K1 | revenue | FY2026Q3 | >= 5.4e+08 | 88% | 가이던스 하단 달성 여부. 단기 수요와 경영진 가이던스 신뢰도를 시험한다. |
| K2 | revenue | FY2026Q3 | >= 5.6e+08 | 55% | 가이던스 상단 초과 여부. 기본 시나리오의 FY2026 성장 가정이 보수적인지 가늠한다. |
| K3 | non_gaap_gross_margin | FY2026Q3 | >= 0.71 | 75% | 믹스 변화에 따른 총이익률 하락이 가이던스(약 72%) 안에서 멈추는지 확인한다. 마진이 더 내려가면 가격 압력 가설이 강해진다. |
| K4 | non_gaap_eps | FY2026Q3 | >= 1.16 | 80% | 가이던스 하단의 EPS 달성 여부. 비용 통제와 레버리지가 유지되는지 시험한다. |
| K5 | revenue | FY2026Q4 | >= 6e+08 | 60% | 3분기 이후에도 분기 성장이 이어지는지 확인한다. 기본 시나리오의 FY2026 연간 성장 가정을 직접 시험한다. |

## 5. 확신도와 비중

- 확신 가중 점수 -0.27 · 비중 참고값 0.0% (반대 우세 — 신규 비중 없음) · 슬레이터 시작 비중 0.0%
- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note "이유"`

## 표결

| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 논거 검증 | 지표 (코드 계산 포함) |
|---|---|---|---|---|---|
| 앤더슨 | 찬성 → 찬성 | 3/5 | ✓ | 0/5 실패 | founder_led=예, upside_10y=6.67x, revenue_5y=9.10x |
| 슬레이터 | 반대 → 반대 | 3/5 | ✓ | 2/5 실패 | unit_economics=unclear, survival_path=예, starter_weight=0.0%, cash_survives=예, cash_min=1.1억 USD |
| 애크먼 | 반대 → 반대 | 4/5 | ✗ 단순·예측 가능한 사업이 아님; 잉여현금흐름을 만들지 못함 (코드 계산); 안전마진 20% 미만 또는 계산 불가 | 1/5 실패 | simple_predictable=아니오, capital_markets_dependent=아니오, catalyst=없음 — 3분기 실적 발표는 촉매가 아니라 이미 가격에 반영된 가이던스 확인일 뿐, intrinsic_value=166.8, mos=-71.4%, net_debt_to_ebitda=-0.39x |

- ⚠ 앤더슨: rebuttals[2] unsupported: 출처 없는 숫자 18% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 슬레이터: arguments[4] unsupported: SBC 차감 FCF가 절반에 못 미치고 세금 환급이 있다는 것은 맞다. 그러나 '분기 SBC가 계속 늘고 있다'는 추세와 총이익률 하락이 믹스 때문이라는 원인은 인용에 없다.
- ⚠ 슬레이터: arguments[1] unsupported: 없는 근거 인용: C:cash_survives@슬레이터
- ⚠ 슬레이터: rebuttals[1]: 인용하지 않은 근거의 숫자 71.4%(C:mos@ackman) — cites에 추가
- ⚠ 슬레이터: rebuttals[2]: 인용하지 않은 근거의 숫자 32(C:exit_multiple@base) — cites에 추가
- ⚠ 애크먼: arguments[2] unsupported: 출처 없는 숫자 70% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: rebuttals[0] unsupported: 없는 근거 인용: C:revenue_5y
- ⚠ 애크먼: rebuttals[2] unsupported: 출처 없는 숫자 18% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 애크먼: risks[1] unsupported: '세 분기 연속 가이던스 상회'는 인용에 없다. 인용한 것은 2분기 컨센서스 상회뿐이고, 가이던스 이력은 수집되지 않았다.
- ⚠ 애크먼: arguments[1]: 인용하지 않은 근거의 숫자 42%(C:revenue_cagr@base) — cites에 추가
- ⚠ 애크먼: rebuttals[2]: 인용하지 않은 근거의 숫자 32(C:exit_multiple@base) — cites에 추가
- ⚠ call 유형 근거 없음 — 리서치 보강 필요
- ⚠ 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- ⚠ 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다
- ⚠ 경영진·자본배분 findings[6] 검증 실패(unsupported): 출처 없는 숫자 7000 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- ⚠ 레드팀 weakest[2] 검증 실패(unsupported): 없는 근거 인용: C:base_rate@base
- ⚠ 레드팀 premortem[2] 검증 실패(unsupported): SBC 차감 FCF, 세금 환급, 희석 주식 수 비교는 맞다. 그러나 '분기 SBC가 매 분기 늘고 있다'는 추세는 인용에 2분기 한 점뿐이라 받쳐지지 않는다.
- ⚠ 회계 품질 findings[3] 검증 실패(unsupported): 없는 근거 인용: C:goodwill_to_assets
- ⚠ 레드팀 weakest[0] 검증 실패(unsupported): 출구 배수 32배, 수익률 분해, '0.75배에서 마이너스'라는 민감도는 인용에 없다. 기본 시나리오 IRR은 이미 -0.3%라 서술과 어긋난다.
- ⚠ 경영진·자본배분 findings[3]: 인용하지 않은 근거의 숫자 2.8e+08(C:fcf@FY2025) — cites에 추가
- ⚠ 사업·산업 moat[1] 검증 실패(unsupported): S34, S29, S30은 랙 개방, 신제품, Scorpio 램프를 다룬다. '전환비용 논리가 보도에 반복된다'는 내용은 인용에 없다.
- ⚠ 회계 품질 flags[0] 검증 실패(unsupported): SBC/매출 59.2%, 18.8%, 약 16%, 분기 SBC 추세는 맞다. 그러나 FY2024가 'IPO 시점 일회성 RSU 인식'이라는 원인은 인용에 없다.
- ⚠ 사업·산업 moat[0] 검증 실패(unsupported): 총이익률 68.9~76.4% 범위는 맞다. 그러나 FY2023 매출 1.2억 달러와 FY2025 매출 8.5억 달러는 인용에 없다.

## 앤더슨 — 찬성 (3/5)

> AI 데이터센터 연결 구간은 설계에 한번 들어가면 오래 쓰이는 승자독식형 시장이고, 이 회사는 그 구간에서 창업자 주도로 매출이 두 배 넘게 커지며 흑자와 FCF를 동시에 냈다. 5년 뒤 매출이 두 배를 훌쩍 넘고 10년 뒤 주당 가치가 현재 주가의 5배를 넘는 길이 상방 시나리오에서는 열려 있다. 다만 기본 시나리오의 기대수익률은 거의 0이고 해자 증거는 아직 '주장' 수준이다. 그래서 확신은 중간으로 두고, 성장 가설(설계 채택의 확산과 마진 유지)이 훼손될 때만 생각을 바꾼다. 가격이 비싸다는 이유로는 팔지 않는다.

**논거**
- 매출이 FY2025에 115.1% 늘었고 같은 해 FCF 마진이 33.1%였다. 이 정도 성장에서 현금을 스스로 만들어 외부 조달 없이 재투자하는 구조는 아웃라이어 후보의 전형이다. [C:revenue_growth@FY2025] [C:fcf_margin@FY2025]
- 3분기 가이던스(매출 5.4억~5.6억 달러)는 분기 대비 약 40% 성장을 뜻한다. 성장이 둔화하는 것이 아니라 계속 가속되는 구간이라는 단기 증거다. 가이던스는 2차 요약 출처 기준이라는 한계가 있다. [F185] [S33](https://news.google.com/rss/articles/CBMingFBVV95cUxPR3VxWjF6UmpuQVFGazJlT3BDRTlOdTkzb1Z6bXRjdjE1LVZOWHBjQld5aDlGdk05aVU2SE5SY2lrOHZ0QWI5aHczOUtndjNvc1VIVFBCZXVkeGlldkUtM1Q3S3ptQUJJbHlxQ1dUZm9KZ0ZpWkJLZmRxUW9uNHZBaWlUa09hU3BzcW9uZTNqMG5IYXh2RGFxdGp5MXlZZw?oc=5)
- 총이익률이 FY2025에 75.7%로 규모가 커지는 동안에도 유지됐다. 차별화된 제품이 가격 결정력을 갖는다는 흔적이고, 이익률 상승 여지(고정비 레버리지)와 FCF 전환(질문 6·7)에 부합한다. [C:gross_margin@FY2025] [C:operating_margin@FY2025]
- 창업자 주도 기업이 AI 데이터센터 연결 기업으로 소개되고, 신제품(OCP 규격 3.2T 리타이머)과 스위치 확장이 이어진다. 분기 R&D를 계속 늘려 시간 지평을 길게 쓰는 재투자 의지가 보인다. [S18](https://news.google.com/rss/articles/CBMikAFBVV95cUxPMWhsSHZCT3ZJanU5R2Z3S0szSkY3eFEybTJSZjVScWZSaW5abTNEY214YlA2aEprOWJLcFZCV3luTklBX0hKNHMtdHhyX1ByNlR5dTEwQWg0bnhyN1Z2QVhEUmlUOUZPU3F6V1BuaUFXbXowSHJOUW4xUWIwZ2NDUE0tRk1XN1JHRWVxeENWTTU?oc=5) [S29](https://news.google.com/rss/articles/CBMingFBVV95cUxNemw5bzRDQUs2TGt0MFhQeGhOWktDcVA5WE1PTWcxbk5LYzlpVGtwNnljcWpzcGhnSU1oWElUTVM1d2FoUlpialJ1SzkzMjEzY3Y1eW5Hd1VBVHpQejJHSXEwWWdZZ3ZSczhNN0FhOHd2TEt4MURGb1RPX2dBMGo2MWViX3NNck1sY2NfeHlqZ1dCVXVyQXNLaFV5dkxrQQ?oc=5) [F144]
- 엔비디아 랙이 타사 가속기를 받아들이는 흐름은 특정 가속기 플랫폼에 묶이지 않는 연결 칩의 시장을 넓힌다. 상방 시나리오가 현실적으로 열리는 구조적 경로(질문 10)다. [S34](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQkRNUnVZc0JGMVdRZVUtWW5aX3FIbGFUa2F4SlE5LUFyc0ttQ2E3WktDMktsY01mNWl6d2dTbC1RQWhlVXF2QU1GN0s4Zk1iRGo5MXZMTDBmRWtRc0lvRUVYMjJoS2R2RXo2SUlxdWg3Y2NpZkRnd0R2bFFiSW1haTNMcldaSTh5cGRPU3hGQVcwMXpQbjRHZw?oc=5) [S30](https://news.google.com/rss/articles/CBMijwFBVV95cUxQc0w4RlV6NG5USTZGT25qMllVdzI3S3hMcFBEdi1yb3A2Zng3TGR4em9Pa1h5b2J6cThFbml0WTRaQ0NFLXhMTUUxa3JuSlVmdUFlWmhZQ1RrU3NrY2hRNDBFV1UxSjZhUDJ4RF9QeEdaUVdtbEN1c3NUMHVrdElKYUVoUFFuaWE3WnFrZTEzWQ?oc=5)

**사전 부검**
- 사전 부검: 가격이 이미 기본 시나리오를 반영해 기대 연 수익률이 -1.0%이고 손실 확률이 80%다. 상방 시나리오가 실현되지 않으면 보유 기간 내내 수익이 없을 수 있다. 상방 시나리오 확률은 20%에 불과하다. [C:expected_irr] [C:p_loss] [F183]
- 사전 부검: 고객 집중도, 제품별 매출, 설계 수주가 공시·수집 근거에 없다. 소수 하이퍼스케일러가 자체 칩으로 옮겨가면 성장 가설이 깨진다. 해자는 아직 '주장' 수준이다. [S7](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000010/alab-20251231.htm) [S1](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000035/alab-20260630.htm)
- 사전 부검: SBC를 차감한 FCF가 FY2025에 보고 FCF의 절반 안팎이어서 주주에게 돌아오는 실질 현금창출력은 헤드라인보다 작다. 희석이 이어지면 주당 가치가 기대보다 낮아진다. [C:fcf_after_sbc@FY2025] [C:fcf@FY2025]

**반론**
- → 애크먼: 애크먼의 가장 강한 논거는 기본 시나리오 현재가치가 주가에 크게 못 미친다는 것이다. 이 숫자는 5년 시나리오 하나를 할인한 값이라 현재를 정밀하게 재는 데는 맞다. 하지만 이 종목을 사는 이유는 기본 시나리오가 아니라 상방 시나리오에서 나오는 비대칭이다. 약세 시나리오에서 잃는 폭은 100%로 막혀 있다. 강세 시나리오는 연 수익률이 양수이고, 10년으로 늘리면 주당 가치가 주가의 5배를 넘는다. 순현금 구조이므로 애크먼 본인이 인정했듯 '망한다'는 위험은 없고, 남는 반대 논거는 '비싸다' 하나다. 비싸다는 이유는 성장 가설이 훼손됐다는 매도 논거가 아니다. [C:iv@base] [C:irr@bull] [C:irr@bear] [C:net_cash@FY2025]
- → 슬레이터: 슬레이터의 가장 강한 논거는 해자가 주장 수준이고 설계 수주·고객 집중도가 공개되지 않았다는 것이다. 이 증거 공백은 인정한다. 그래서 확신을 낮게 두고 반증 조건을 분기 지표로 걸어 둔다. 그러나 증거가 공개될 때까지 기다리면 성장 구간의 가장 가치 있는 부분을 놓칠 수 있다. 이 회사는 이미 FCF 마진이 높고 외부 조달 없이 재투자하므로, 증명을 기다리는 비용이 틀렸을 때의 비용보다 크다. 슬레이터가 요구하는 3분기 가이던스 달성과 총이익률 방향은 내 반증 조건과 같은 항목이다. 우리의 차이는 지표가 아니라 시작 비중에 있다. [C:fcf_margin@FY2025] [F185] [F187] [S34](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQkRNUnVZc0JGMVdRZVUtWW5aX3FIbGFUa2F4SlE5LUFyc0ttQ2E3WktDMktsY01mNWl6d2dTbC1RQWhlVXF2QU1GN0s4Zk1iRGo5MXZMTDBmRWtRc0lvRUVYMjJoS2R2RXo2SUlxdWg3Y2NpZkRnd0R2bFFiSW1haTNMcldaSTh5cGRPU3hGQVcwMXpQbjRHZw?oc=5)
- → 레드팀: 레드팀의 사전 부검 네 개를 성장 가설을 깨는 것과 경로의 소음으로 나눈다. 수요 소화 국면과 가격 압력은 가설 자체를 깬다. 3분기 매출이 가이던스 하단에 못 미치거나 총이익률이 가이던스 아래로 내려가면 내 논지도 무너지므로 이 둘을 반증 조건에 넣었다. 재고·매출채권 급증과 세금 환급은 경로의 소음일 가능성이 높다. 3분기 가이던스를 위한 선제 비축으로 설명되고, 세금 환급은 영업 가치와 무관하다. 가장 약한 가정인 기본 시나리오의 출구 배수는 맞는 지적이다. 하지만 내 판단은 기본 시나리오가 아니라 성장이 18%로 둔화하지 않고 더 오래 유지되는 상방 경로에 건 것이다. [F185] [F187] [F84] [F85] [F125] [F126] [F77] [F118]

**인정한 점**
- 애크먼과 슬레이터가 지적한 대로 확률 가중 기대 연 수익률은 마이너스이고 손실 확률이 높다. 이것이 내 확신을 높지 않은 3에 머물게 하는 이유다.
- 슬레이터가 지적한 대로 해자 증거는 총이익률 흔적 외에는 주장 수준이다. 설계 수주와 고객 집중도가 공개되기 전까지는 확신을 올리지 않는다.
- 레드팀이 지적한 SBC 차감 FCF가 보고 FCF의 절반 안팎이라는 점을 인정한다. 희석이 이어지면 주당 가치가 낮아지므로 상방 시나리오의 희석 가정을 보수적으로 본다.
- 다만 가격이 비싸다는 것만으로는 성장 가설이 훼손됐다고 볼 수 없다. 입장은 유지하되, 반증 조건이 충족되면 즉시 입장을 바꾼다.


## 슬레이터 — 반대 (3/5)

> 기회의 크기와 단기 수요 증거는 강하다. 사업은 이미 자체 현금으로 굴러가므로 생존 문제도 없다. 그런데 지금 가격은 이 가설을 거의 전부 선반영했고, 그 가설을 오래 받칠 증거(설계 수주, 고객 집중도, 제품별 매출)는 아직 주장 수준이다. 코드가 계산한 확률 가중 기대 연 수익률이 마이너스이고 손실 확률이 높다. 좋은 회사를 너무 비싸게 사는 구간일 가능성이 크다. 증거가 쌓이기 전에는 비중을 키울 근거가 없고, 시작 비중도 0으로 둔다. 3분기 실적에서 가이던스 달성과 총이익률 방향, 제품별 매출 공개가 확인되면 다시 본다.

**논거**
- 크기와 수요 증거는 강하다. 2분기 매출은 컨센서스를 넘었고 3분기 가이던스는 분기 성장 약 40%를 뜻한다. 이 부분은 가설에 유리하다. [F135] [F184] [F185]
- 생존은 문제가 아니다. FY2025 FCF 마진이 흑자이고 팹리스라 설비투자 부담이 작으며, 코드가 계산한 기본 시나리오 현금 경로도 0 아래로 내려가지 않는다. 외부 자본 의존이 노스볼트형 위험은 아니다. [C:fcf_margin@FY2025] [C:cash_survives@슬레이터] [F8]
- 지속성을 입증할 증거가 없다. 해자는 총이익률 흔적 외에는 `claimed` 수준이고 설계 수주, 상위 고객 비중, 제품별 매출이 공개되지 않았다. 슬레이터는 확신을 회사가 증명하게 하는데, 아직 증명되지 않은 것을 가격이 먼저 인정하고 있다. [S34](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQkRNUnVZc0JGMVdRZVUtWW5aX3FIbGFUa2F4SlE5LUFyc0ttQ2E3WktDMktsY01mNWl6d2dTbC1RQWhlVXF2QU1GN0s4Zk1iRGo5MXZMTDBmRWtRc0lvRUVYMjJoS2R2RXo2SUlxdWg3Y2NpZkRnd0R2bFFiSW1haTNMcldaSTh5cGRPU3hGQVcwMXpQbjRHZw?oc=5) [S29](https://news.google.com/rss/articles/CBMingFBVV95cUxNemw5bzRDQUs2TGt0MFhQeGhOWktDcVA5WE1PTWcxbk5LYzlpVGtwNnljcWpzcGhnSU1oWElUTVM1d2FoUlpialJ1SzkzMjEzY3Y1eW5Hd1VBVHpQejJHSXEwWWdZZ3ZSczhNN0FhOHd2TEt4MURGb1RPX2dBMGo2MWViX3NNck1sY2NfeHlqZ1dCVXVyQXNLaFV5dkxrQQ?oc=5) [S30](https://news.google.com/rss/articles/CBMijwFBVV95cUxQc0w4RlV6NG5USTZGT25qMllVdzI3S3hMcFBEdi1yb3A2Zng3TGR4em9Pa1h5b2J6cThFbml0WTRaQ0NFLXhMTUUxa3JuSlVmdUFlWmhZQ1RrU3NrY2hRNDBFV1UxSjZhUDJ4RF9QeEdaUVdtbEN1c3NUMHVrdElKYUVoUFFuaWE3WnFrZTEzWQ?oc=5)
- 가격이 가설을 선반영했다. EV/매출이 43.51배이고 확률 가중 기대 연 수익률은 -1.0%, 손실 확률은 80%다. 기본 시나리오 수익률 분해에서도 매출 성장은 멀티플 압축이 거의 상쇄한다. 지속성이 맞아도 수익이 거의 남지 않는다. [C:ev_revenue] [C:expected_irr] [C:p_loss]
- 이익의 질은 조정해서 봐야 한다. SBC 차감 FCF는 보고 FCF의 절반에 못 미치고, 분기 SBC는 계속 늘고 있으며, 2분기 순이익은 세금 환급 때문에 부풀려졌다. 총이익률 가이던스도 믹스 때문에 내려갔다. [C:fcf_after_sbc@FY2025] [C:fcf@FY2025] [F153] [F77] [F118] [F187]

**사전 부검**
- 사전 부검: 이 판단이 틀렸다면, 설계 수주가 이미 길게 잠겨 있어 성장이 기본 시나리오보다 오래 가속되고 시장이 높은 멀티플을 유지한 경우다. 이때 기다리는 동안 상승분을 놓친다. 강세 시나리오 연 수익률은 +15.8%이고 확률은 20%다. [S34](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQkRNUnVZc0JGMVdRZVUtWW5aX3FIbGFUa2F4SlE5LUFyc0ttQ2E3WktDMktsY01mNWl6d2dTbC1RQWhlVXF2QU1GN0s4Zk1iRGo5MXZMTDBmRWtRc0lvRUVYMjJoS2R2RXo2SUlxdWg3Y2NpZkRnd0R2bFFiSW1haTNMcldaSTh5cGRPU3hGQVcwMXpQbjRHZw?oc=5) [S30](https://news.google.com/rss/articles/CBMijwFBVV95cUxQc0w4RlV6NG5USTZGT25qMllVdzI3S3hMcFBEdi1yb3A2Zng3TGR4em9Pa1h5b2J6cThFbml0WTRaQ0NFLXhMTUUxa3JuSlVmdUFlWmhZQ1RrU3NrY2hRNDBFV1UxSjZhUDJ4RF9QeEdaUVdtbEN1c3NUMHVrdElKYUVoUFFuaWE3WnFrZTEzWQ?oc=5) [C:irr@bull]
- 사전 부검: 현금 흐름이 좋아 기본 시나리오 현금이 쌓이는 만큼, 인수나 재투자로 영업권이 늘며 숨은 역량이 생겼을 수 있다. 증거 부재를 약점으로 읽었는데 실제로는 수집 실패일 수 있다. [F57] [F58] [F59]
- 사전 부검: 분기 변동(재고와 매출채권 급증, 세금 환급)을 악재로 읽었지만 단순한 선제 비축과 일회성이라면, 이익의 질에 대한 우려가 과장된 것이다. [F85] [F126] [F77]

**반론**
- → 앤더슨: 앤더슨의 가장 강한 논거는 매출 115.1% 성장과 FCF 마진 33.1%를 동시에 낸 구조가 아웃라이어 후보의 전형이라는 점이다. 이 점은 인정한다. 그러나 '5배'가 성립하려면 강세 시나리오가 참이어야 하고, 그 확률은 20%다. 강세 시나리오의 연 수익률도 +15.8%다. 상방이 열려 있다는 것과 지금 가격에 담을 근거가 있다는 것은 다르다. 설계 수주와 상위 고객 비중처럼 지속성을 입증할 증거는 아직 주장 수준이고, 확률 가중 기대 연 수익률은 -1.0%다. 증거가 쌓이면 비중을 키우는 것이 내 방식이므로, 증거 없이 중간 확신으로 먼저 사는 것은 따르지 않는다. [C:revenue_growth@FY2025] [C:fcf_margin@FY2025] [C:irr@bull] [C:expected_irr]
- → 애크먼: 애크먼의 가장 강한 논거는 기본 시나리오 안전마진이 -71.4%이고 손실 확률이 80%라는 점이다. 가격이 문제라는 데 동의한다. 다만 정의되지 않은 시장을 오늘 모델링할 수 없다는 이유로 버리지는 않는다. 사업은 순현금이고 자체 현금으로 굴러가며 생존 위험이 없다. 내 반대는 사업이 예측 불가능해서가 아니라, 증거 수준에 비해 가격이 앞서 있기 때문이다. 그래서 조건이 바뀌면 다시 본다. 3분기 실적에서 가이던스 달성과 제품별 매출 공개가 확인되는 경우다. 안전마진 20% 같은 가격 기준만으로 판단하지 않는다. [C:p_loss] [C:net_cash@FY2025] [C:expected_irr]
- → 레드팀: 레드팀의 사전 부검 중 총이익률 신호가 가장 쓸 만하다. 3분기 Non-GAAP 총이익률이 가이던스 약 72%보다 낮으면 믹스가 아니라 가격 압력이라는 구분이다. 이미 내 must_be_true에 71% 하한을 넣었고, 가격 압력이 확정되는 선은 thesis_breaks의 70%로 둔다. 레드팀이 제시한 재고 1.1억 달러 초과 신호는 선제 비축과 구분되지 않아 반증 조건에 넣지 않고, 재고 증가가 이어지는지는 수동 확인에 둔다. 다만 레드팀이 약한 가정으로 꼽은 출구 배수 32배는 동의한다. 민감도에서 배수가 줄면 기본 시나리오 수익률이 마이너스로 내려가는 지점이 이 판단의 핵심이다. [F187] [F84] [F85] [C:expected_irr]

**참이어야 하는 것**
- [on_track] 3분기 매출이 가이던스 하단 이상
- [at_risk] 믹스 변화에도 Non-GAAP 총이익률이 71% 아래로 내려가지 않음
- [at_risk] 4분기 매출이 6억 달러 이상으로 분기 성장이 이어짐

**인정한 점**
- 앤더슨의 지적대로 사업이 자체 현금으로 굴러가고 성장이 가속되는 구간이라는 증거는 강하다. 그 결과 생존과 수요 항목은 모두 가설에 유리하게 읽고, 반대의 근거를 가격과 증거 공백으로 좁힌다.
- 내 1라운드 사전 부검대로 증거 부재가 수집 실패일 수 있다. 그래서 확신은 3으로 두고 3분기 실적 이후 재평가한다.


## 애크먼 — 반대 (4/5)

> 사업은 한 문단으로 설명되고 FCF 마진도 33%대로 훌륭하지만, 가격이 문제다. 코드가 계산한 기본 시나리오 안전마진은 -71.4%이고, 확률 가중 기대 연 수익률은 -1.0%, 손실 확률은 80%다. 좋은 회사도 비싸게 사면 나쁜 투자다. 해자는 설계 수주·고객 집중도 증거가 없어 'claimed' 수준이고, 10년 뒤 FCF 범위를 좁게 추정하기도 어렵다. 순현금 구조라 자본시장 의존은 없으나 안전마진 20% 레드라인을 크게 밑돌아 담지 않는다. 촉매도 없다 — 내가 개입할 여지가 있는 사업이 아니다.

**논거**
- 가격이 기본 시나리오를 넘어선다. 기본 시나리오 현재가치는 주가보다 훨씬 낮아 안전마진이 마이너스이고, 확률 가중 기대 수익률도 마이너스다. 강세 시나리오가 실현되어야 겨우 요구수익률을 넘는다. [C:expected_irr] [C:p_loss] [C:irr@base] [C:iv@base] [F183]
- 기본 시나리오의 연 수익률 분해를 보면 매출 성장 기여가 멀티플 축소 기여로 거의 상쇄된다. 매출이 연 42% 성장해도 현재 배수가 유지되지 못하면 주주는 수익을 얻지 못한다. 시장은 성장이 오래간다는 전제를 이미 지불했다. [C:ev_revenue] [C:pe] [C:irr@base]
- 사업의 질은 높다. FCF 마진 33.1%, 순현금 구조, 총이익률 70%대 중반이다. 자본시장 의존이 없다는 점은 밸리언트식 실패 위험을 제거한다. 그러나 이는 필요조건이지 가격의 정당화가 아니다. [C:fcf_margin@FY2025] [C:net_cash@FY2025] [C:gross_margin@FY2025]
- 이익의 질을 보정하면 더 비싸다. SBC 차감 FCF는 보고 FCF의 절반 안팎이고, 2분기 순이익에는 세금 환급이 얹혀 PER이 부풀려졌다. 주주에게 남는 실질 현금창출력은 보고 수치보다 낮다. [C:fcf_after_sbc@FY2025] [C:fcf@FY2025] [F77] [F118]
- 해자가 입증되지 않았다. 설계 수주, 고객 집중도, 제품별 매출이 없고 총이익률 가이던스는 약 72%로 내려간다. 10년 뒤 FCF를 좁게 추정할 근거가 부족해 단순성·예측가능성 기준을 충족하지 못한다. [F187] [S23](https://news.google.com/rss/articles/CBMikAFBVV95cUxQRU5TbmtpSHJ5QkJSdWxsUTdCNHFMUnNhMDZyQm1VZkNMQzgwSGtfZDJGOEVWOGdjV2otZ2dQUmlsX1FsZV9BNk5mWVJTSVU2MGdNMnNWUGhNaWZUMENqUVBTZkc3RDN4bEZLNl9veHc1YTBvR2xuS2lJMldIZHpnS3NqMmpCYmJzNDFZRXdfNHU?oc=5) [S34](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQkRNUnVZc0JGMVdRZVUtWW5aX3FIbGFUa2F4SlE5LUFyc0ttQ2E3WktDMktsY01mNWl6d2dTbC1RQWhlVXF2QU1GN0s4Zk1iRGo5MXZMTDBmRWtRc0lvRUVYMjJoS2R2RXo2SUlxdWg3Y2NpZkRnd0R2bFFiSW1haTNMcldaSTh5cGRPU3hGQVcwMXpQbjRHZw?oc=5)

**사전 부검**
- 사전 부검: 내가 틀렸다면, 엔비디아 랙 개방과 Scorpio 램프로 콘텐츠 가치가 모델 강세 시나리오 이상으로 커져 성장이 오래 유지되고 높은 배수가 정당화된 경우다. 이때 기다린 대가는 기회비용이다. [S34](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQkRNUnVZc0JGMVdRZVUtWW5aX3FIbGFUa2F4SlE5LUFyc0ttQ2E3WktDMktsY01mNWl6d2dTbC1RQWhlVXF2QU1GN0s4Zk1iRGo5MXZMTDBmRWtRc0lvRUVYMjJoS2R2RXo2SUlxdWg3Y2NpZkRnd0R2bFFiSW1haTNMcldaSTh5cGRPU3hGQVcwMXpQbjRHZw?oc=5) [S30](https://news.google.com/rss/articles/CBMijwFBVV95cUxQc0w4RlV6NG5USTZGT25qMllVdzI3S3hMcFBEdi1yb3A2Zng3TGR4em9Pa1h5b2J6cThFbml0WTRaQ0NFLXhMTUUxa3JuSlVmdUFlWmhZQ1RrU3NrY2hRNDBFV1UxSjZhUDJ4RF9QeEdaUVdtbEN1c3NUMHVrdElKYUVoUFFuaWE3WnFrZTEzWQ?oc=5) [C:irr@bull]
- 사전 부검: 세 분기 연속 가이던스를 상회하는 실적과 AI 설비투자 가속이 이어지면 시장은 기본 시나리오의 성장 가정을 계속 위로 수정할 수 있다. 가격은 내재가치보다 오래 높게 유지될 수 있다. [F185] [F184] [F135]
- 사전 부검: 반대로 하이퍼스케일러 설비투자가 소화 국면에 들어가면 가격 하락이 크겠지만, 그 경우에도 순현금 구조 덕에 생존 문제는 없다. 따라서 '사업이 망한다'가 아니라 '가격이 비싸다'가 내 반대의 유일한 근거임을 인정한다. [C:irr@bear] [C:net_cash@FY2025]

**반론**
- → 앤더슨: 10년 뒤 주당 가치가 5배를 넘는 길은 강세 시나리오(확률 20%)에서만 열린다. 이는 생존자 편향에 기댄 가정이다. 코드가 계산한 확률 가중 기대 연 수익률은 -1.0%이고 손실 확률은 80%다. 기본 시나리오에서도 매출 성장 기여가 멀티플 압축으로 거의 상쇄된다. '가격이 비싸다는 이유로 팔지 않는다'는 태도는, 가격 대비 내재가치를 따지는 안전마진 기준에서는 담지 않을 이유가 된다. 기저율 표가 없어 연 42%~55% 성장이 5년 이어지는 빈도도 검증되지 않았다. [C:expected_irr] [C:p_loss] [C:irr@base] [C:irr@bull] [C:revenue_5y]
- → 슬레이터: 슬레이터가 인정한 생존 경로와 단위경제는 필요조건이다. 생존은 문제가 아니고 가격이 문제라는 점에서 우리 결론은 같다. 다만 슬레이터는 3분기 실적에서 가이던스 달성이 확인되면 다시 본다고 했다. 가이던스 달성은 이미 가격에 반영돼 있다. 기본 시나리오 현재가치가 주가보다 크게 낮은 상태에서는 가이던스가 맞아도 안전마진이 생기지 않는다. 증거가 쌓이는 것과 가격이 싸지는 것은 별개의 문제다. [F185] [C:iv@base] [F183] [C:expected_irr]
- → 레드팀: 사전 부검이 가리키는 두 가지 위험, 멀티플 압축과 총이익률 하락은 모두 FCF 범위를 넓힌다. 기본 시나리오의 출구 P/FCF 32배가 성장 18%에서 정당화되기 어렵다는 지적에 동의한다. 이는 안전마진을 더 요구하게 만든다. 이미 -71.4%여서 20% 레드라인과 거리가 너무 멀기 때문에, 이 위험들이 어떻게 풀려도 결론은 바뀌지 않는다. 주가가 기본 시나리오 현재가치 근처로 내려와도 그때는 SBC 차감 FCF 기준으로 다시 계산해야 한다. [C:ev_revenue] [C:fcf_after_sbc@FY2025] [F187] [C:iv@base]

**인정한 점**
- 앤더슨의 지적대로 엔비디아 랙 개방과 Scorpio 램프가 겹치면 콘텐츠 가치가 모델 강세 시나리오 이상으로 커질 수 있고, 이 경우 기다린 대가는 기회비용이다. 다만 이 경로는 확률 20%이며 담을 근거가 되지 못한다.
- 슬레이터의 말대로 사업이 망할 위험은 아니다. 순현금 구조와 FCF 마진 33.1% 덕분에 생존은 문제가 아니고, 내 반대는 가격 하나에 의존한다. 입장은 유지하되 확신은 4로 둔다.


## 분석 모듈 (L4)

### 사업·산업 — unclear

Astera Labs는 AI 데이터센터의 서버·가속기 사이의 고속 연결(리타이머·스마트 리드라이버 Aries·Taurus, 메모리 Leo, 스위치 Scorpio)을 파는 팹리스 반도체 회사다. 데이터센터 사업자와 서버·가속기 제조사의 설계에 들어가는 방식으로 매출이 난다. 공시상 매출은 FY2024 4.0억 달러에서 FY2025 8.5억 달러로 늘었다(C:revenue_growth@FY2025 115.1%). 총이익률은 FY2025 75.7%, 영업이익률은 20.3%로 흑자 전환했고, FCF 마진은 33.1%다. 2026년 2분기 매출은 3.924억 달러(전년 대비 +104%)이고, 3분기 가이던스는 5.4억~5.6억 달러다. 총이익률 가이던스는 약 72%라서 2분기 Non-GAAP 73.7%보다 낮아지는 믹스 변화가 보인다. 고객 집중도·제품별 매출·설계 수주 같은 단위경제의 핵심 KPI는 이번 증거에 없다. 그래서 마진 수준은 입증됐지만 해자의 지속성과 고객 의존도는 확인되지 않았다.

- [unit_economics] 총이익률은 높게 유지되지만 소폭 내려가는 신호가 있다. 총이익률은 FY2024 76.4%에서 FY2025 75.7%로 소폭 낮아졌다. 2분기 Non-GAAP 총이익률은 73.7%이고 3분기 가이던스는 약 72%다. 가이던스는 2차 요약 출처 기준이다. 제품 믹스가 스위치·모듈 쪽으로 이동하면서 마진이 낮아지는지, 가격 압력 때문인지는 제품별 매출 자료가 없어 구분할 수 없다. [C:gross_margin@FY2024] [C:gross_margin@FY2025] [F186] [F187] [S41](https://www.marketbeat.com/instant-alerts/astera-labs-nasdaqalab-announces-earnings-results-2026-08-04/)
- [unit_economics] 규모의 레버리지는 공시상 확인된다. 영업이익률은 FY2024 -29.3%에서 FY2025 20.3%로 바뀌었다. 2분기 Non-GAAP 영업이익률은 39.1%다. 다만 GAAP 영업이익(FY2026Q2 8,925만 달러)과 Non-GAAP 영업이익(1.5억 달러)의 차이는 SBC가 크게 차지한다. 분기 SBC는 FY2026Q2에 6,399만 달러로 FY2025Q2의 3,547만 달러보다 크게 늘었다. 이 차이는 단위경제의 질을 판단할 때 반영해야 한다. [C:operating_margin@FY2024] [C:operating_margin@FY2025] [F188] [F109] [F189] [F153] [F150]
- [customers] 고객 집중도, 상위 고객 비중, 제품별 매출 비중(Aries·Taurus·Leo·Scorpio)이 이번 증거에 없다. 이 회사는 소수 하이퍼스케일러·가속기 플랫폼의 설계 채택에 의존하는 구조일 가능성이 높다. 그러나 이는 증거로 확인되지 않은 가정이다. 이탈률·순매출유지율·CAC도 칩 판매 모델 특성상 공시되지 않아서 단위경제를 이 지표들로 판정할 수 없다. 그래서 `unclear`로 둔다. [S7](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000010/alab-20251231.htm) [S1](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000035/alab-20260630.htm)
- [industry] 수요 쪽 증거는 강하다. 2분기 매출 3.924억 달러는 컨센서스 약 3.6085억 달러를 넘었고(+8.8%, 2차 출처), 3분기 가이던스 중간값 5.5억 달러는 분기 대비 약 40% 성장을 뜻한다. 보도는 AI 인프라 투자 확대가 수요를 끌고 있다고 설명한다. 반면 산업 구조 측면에서 가치사슬상 위치(데이터센터 내 연결 구간), 공급자 협상력(외부 파운드리 의존), 경쟁 강도에 대한 공시 근거는 수집되지 않았다. [F135] [F184] [F185] [S33](https://news.google.com/rss/articles/CBMingFBVV95cUxPR3VxWjF6UmpuQVFGazJlT3BDRTlOdTkzb1Z6bXRjdjE1LVZOWHBjQld5aDlGdk05aVU2SE5SY2lrOHZ0QWI5aHczOUtndjNvc1VIVFBCZXVkeGlldkUtM1Q3S3ptQUJJbHlxQ1dUZm9KZ0ZpWkJLZmRxUW9uNHZBaWlUa09hU3BzcW9uZTNqMG5IYXh2RGFxdGp5MXlZZw?oc=5) [S41](https://www.marketbeat.com/instant-alerts/astera-labs-nasdaqalab-announces-earnings-results-2026-08-04/) [S37](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQbG5PWWFDU21xb0t4dWtmZDFZNzJHRWd6S3dJZUhoc0NLbU5WeGxDd2Q3cFNHN3Noc2toN184elRhMlR0R0I5NjlUX3VXVGhQdk9kb01leTExZ1FTOG42SWJCc1l3U1NyMFB5ck9wWmtHQmo4TjlTMmFkUVNKbE1TWGktaVkyQjRLcmNPQjVveDBYUV9iTFJ4Tklrdmc3TWJDRllMTlVuMFBjd3c?oc=5)
- [unit_economics] 재고와 매출채권이 2분기에 빠르게 늘었다. 재고는 FY2026Q1 6,016만 달러에서 FY2026Q2 1.1억 달러로, 매출채권은 1.3억 달러에서 1.9억 달러로 늘었다. 3분기 매출 가이던스(5.4억~5.6억 달러)를 위한 선제 비축과 매출 증가로 읽을 수 있다. 다만 DSO는 FY2024와 FY2025에 35.7일과 35.6일로 안정적이었다. 2026년 분기 DSO는 확인되지 않으므로 수금 지연 여부는 다음 분기에 점검해야 한다. [F84] [F85] [F125] [F126] [C:dso@FY2024] [C:dso@FY2025] [F185]
- [runway] 재투자 여력은 현금창출로 확인된다. FY2025 FCF는 2.8억 달러(FCF 마진 33.1%)이고, 설비투자는 3,754만 달러로 매출 대비 작다. 팹리스라서 자본집약도는 낮다. 그러나 SBC 차감 FCF는 FY2025 1.2억 달러로 FCF의 절반 이하 수준이며, 희석 주식 수는 FY2025에 36.8% 늘었다. 현금성 자산(FY2026Q2 1.1억 달러)은 FY2025 1.7억 달러에서 줄었는데, 투자자산 보유 여부는 이번 증거로 확인되지 않는다. [C:fcf@FY2025] [C:fcf_margin@FY2025] [F8] [C:fcf_after_sbc@FY2025] [C:share_change@FY2025] [F16] [F18]
- [runway] 인수를 통한 확장이 시작됐다. 영업권은 FY2025 1,902만 달러에서 FY2026Q1 8,772만 달러, FY2026Q2 9,156만 달러로 늘었다. 제품·기술 영역을 외부 인수로 넓혔다는 뜻이지만, 대상 회사와 거래 규모, 기여 매출은 증거에 없다. 활주로가 유기적 성장에 의존하는지 인수에도 의존하는지는 확인되지 않았다. [F57] [F58] [F59] [S4](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000020/alab-20260331.htm)
- [industry] 시장은 이 사업의 지속 성장을 높게 반영하고 있다. EV/매출은 43.51배이고 PER은 141.82배다. 이 배수는 높은 성장과 마진이 오래 유지된다는 전제에 의존한다. 그 전제를 지지하는 해자 증거(점유율·설계 수주·고객 유지)는 현재 `claimed` 수준에 머물러 있다. 사업 이해 측면에서 가장 큰 공백이다. [C:ev_revenue] [C:pe] [S31](https://news.google.com/rss/articles/CBMimAFBVV95cUxNdlRpdVZsRW9GOWNWZ0E0WTVScl80eDIzV2hKaUdIb3Ffc2ZMUnVURm5CUW4tc05ra3dFbHhod2dZbVJWbGNyb0FZaDZyb3B1cEVFeWFST3pKdk16TjhPUmFQMWs1ekNlNTF4TExPTTJLcDRleEI3Nm9veVF0YWtSQjJBQmlnVmkzU3Q4MnBOci1TNTROUzVPQw?oc=5) [S36](https://news.google.com/rss/articles/CBMimwFBVV95cUxPZ3NyOU11MHBMLVM1bWpkdHRwTHpOOWlOQVk2YS1aandWZk9xUFBuOGNCV1ZTTlVHZXZzQ2Q2TERNcjdsVkRlcWQ4azlWZzZnWVdIaWZ6U0d6ZHRJam9EaWxkSC0tZGpHY1ZKamxTaEdjQ3Z6VTdBVmVPSnJ6QnR0MjVXWVhramg1aXZJRktfc01qOUxKc2UtcGNKNA?oc=5)
- [proven] 총이익률이 FY2022부터 FY2025까지 68.9~76.4% 범위에서 유지됐다. 규모가 커지는 동안(FY2023 1.2억 → FY2025 8.5억 달러)에도 유지된 것은 차별화된 제품이 가격 결정력을 갖는다는 흔적이다. 다만 경쟁사 대비 마진 비교와 점유율 자료가 없어서, 해자라기보다 현재 제품 우위의 흔적으로만 읽을 수 있다. [C:gross_margin@FY2022] [C:gross_margin@FY2023] [C:gross_margin@FY2024] [C:gross_margin@FY2025] [F186]
- [claimed] 플랫폼에 한번 설계되어 들어가면 교체가 어렵다는 전환비용 논리가 보도에 반복된다. 엔비디아가 랙에 타사 AI 칩을 허용하는 흐름에서 수혜를 본다는 보도(S34)가 있고, OCP 규격에 맞는 3.2T 리타이머 신제품 발표(S29)와 Scorpio X 시리즈 램프 보도(S30)도 있다. 설계 수주 수, 재구매율, 가격 인상 후 고객 유지 기록은 없다. [S34](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQkRNUnVZc0JGMVdRZVUtWW5aX3FIbGFUa2F4SlE5LUFyc0ttQ2E3WktDMktsY01mNWl6d2dTbC1RQWhlVXF2QU1GN0s4Zk1iRGo5MXZMTDBmRWtRc0lvRUVYMjJoS2R2RXo2SUlxdWg3Y2NpZkRnd0R2bFFiSW1haTNMcldaSTh5cGRPU3hGQVcwMXpQbjRHZw?oc=5) [S29](https://news.google.com/rss/articles/CBMingFBVV95cUxNemw5bzRDQUs2TGt0MFhQeGhOWktDcVA5WE1PTWcxbk5LYzlpVGtwNnljcWpzcGhnSU1oWElUTVM1d2FoUlpialJ1SzkzMjEzY3Y1eW5Hd1VBVHpQejJHSXEwWWdZZ3ZSczhNN0FhOHd2TEt4MURGb1RPX2dBMGo2MWViX3NNck1sY2NfeHlqZ1dCVXVyQXNLaFV5dkxrQQ?oc=5) [S30](https://news.google.com/rss/articles/CBMijwFBVV95cUxQc0w4RlV6NG5USTZGT25qMllVdzI3S3hMcFBEdi1yb3A2Zng3TGR4em9Pa1h5b2J6cThFbml0WTRaQ0NFLXhMTUUxa3JuSlVmdUFlWmhZQ1RrU3NrY2hRNDBFV1UxSjZhUDJ4RF9QeEdaUVdtbEN1c3NUMHVrdElKYUVoUFFuaWE3WnFrZTEzWQ?oc=5)
- [claimed] 분기 R&D가 FY2025Q1 6,455만 달러에서 FY2026Q2 1.4억 달러로 늘었다. 매출 확대와 함께 설계 인력과 제품군을 키우는 규모의 경제 논리가 가능하다. 하지만 경쟁사(Broadcom·Marvell·Credo) 대비 R&D 규모와 제품 격차는 수집되지 않았다. 신규 경쟁 진입이나 대체재는 확인할 수 없다. [F140] [F144] [S23](https://news.google.com/rss/articles/CBMikAFBVV95cUxQRU5TbmtpSHJ5QkJSdWxsUTdCNHFMUnNhMDZyQm1VZkNMQzgwSGtfZDJGOEVWOGdjV2otZ2dQUmlsX1FsZV9BNk5mWVJTSVU2MGdNMnNWUGhNaWZUMENqUVBTZkc3RDN4bEZLNl9veHc1YTBvR2xuS2lJMldIZHpnS3NqMmpCYmJzNDFZRXdfNHU?oc=5)

### 경영진·자본배분 — mixed

경영진의 보상 구조, 내부자 매매, 과거 가이던스 적중률은 근거가 수집되지 않아 판단할 수 없다. 확인되는 것은 세 가지다. 첫째, SBC가 크고 늘고 있다(FY2025 SBC/매출 18.8%, FY2026Q2 SBC 6,399만 USD). 둘째, 희석 주식 수가 계속 늘고 3분기 가이던스도 1.85억 주로 현재 발행주식 수보다 많다. 셋째, 자사주 매입은 사실상 없고(FY2025 0) 현금 대부분이 성장 투자와 인수(영업권 급증)로 갔다. 정렬 여부는 보상 설계(DEF 14A)를 확인해야 판정할 수 있어, 현재는 mixed로 둔다.

- [compensation] 근거 없음. DEF 14A(S6, 2026-04-23)가 근거 목록에는 있으나 보상 연동 지표(장기 매출·FCF·ROIC 대 단기 EPS·조정 EBITDA)와 베스팅 기간은 정리되지 않았다. 장기 지표 연동 여부는 확인할 수 없다. [S6](https://www.sec.gov/Archives/edgar/data/1736297/000114036126016359/ny20065212x1_def14a.htm)
- [insider] 근거 없음. 창업자·경영진 지분과 최근 내부자 매수·매도, 락업 해제 이력은 수집되지 않았다. 2026-01-20과 2026-02-10에 '경영진 변동' 8-K가 있으나 내용(누가 어떤 사유로 바뀌었는지)은 확인되지 않아 평가하지 않는다. [S8](https://www.sec.gov/Archives/edgar/data/1736297/000110465926012649/tm265461d2_8k.htm) [S11](https://www.sec.gov/Archives/edgar/data/1736297/000110465926005022/tm263452d1_8k.htm)
- [guidance] 과거 가이던스 이력을 수집하지 못해 적중률(C:guidance_hit_rate)을 계산할 수 없다. 신뢰도는 미평가다. 참고로 FY2026Q2 매출은 컨센서스 3.6085억 USD 대비 3.924억 USD로 상회했지만, 컨센서스는 가이던스가 아니므로 가이던스 적중의 증거로 쓰지 않는다. FY2026Q3 가이던스(매출 5.4억~5.6억 USD)는 2차 요약 기반이라 원문 대조 전이다. [F184] [F185] [S38](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000033/q226exhibit991.htm) [S39](https://247wallst.com/companies/alab/earnings/2026/Q2) [S41](https://www.marketbeat.com/instant-alerts/astera-labs-nasdaqalab-announces-earnings-results-2026-08-04/)
- [dilution] SBC 부담이 크다. SBC/매출은 FY2025 18.8%, SBC/영업현금흐름은 50.1%이고, SBC 차감 FCF는 1.2억 USD로 FCF 2.8억 USD의 절반에 못 미친다. 분기 SBC는 FY2026Q1 4,891만 USD에서 FY2026Q2 6,399만 USD로 늘었다. 매출 성장으로 SBC 비중이 낮아지는지는 FY2026 연간 값이 나와야 확인된다. [C:sbc_to_revenue@FY2025] [C:sbc_to_ocf@FY2025] [C:fcf_after_sbc@FY2025] [F152] [F153]
- [dilution] 희석 주식 수는 FY2024 253.5%, FY2025 36.8% 늘었다. FY2024는 IPO 효과가 크고 연간 평균 기준이라 과장될 수 있다. FY2026Q3 가이던스의 희석 주식 수는 약 1.85억 주인데, 2026-07-31 기준 발행주식 수는 1.73485억 주다. 이 차이는 옵션·RSU 등 잠재 희석이 계속 반영된다는 뜻이다. [C:share_change@FY2024] [C:share_change@FY2025] [F194] [F154]
- [capital_allocation] 자사주 매입은 FY2025에 0이고 FY2024도 107만 USD에 그쳐, 희석을 상쇄하는 매입은 없다. 따라서 희석은 가려지지 않고 그대로 드러난다. 한편 FCF는 FY2025에 FCF 마진 33.1%로 흑자 전환했고, 순현금 포지션은 유지된다. [F3] [F4] [C:fcf_margin@FY2025] [C:net_cash@FY2025]
- [capital_allocation] FY2025 말 1,902만 USD이던 영업권이 FY2026Q1에 8,772만 USD, FY2026Q2에 9,156만 USD로 늘었다. FY2026Q1에 약 7천만 USD 규모의 인수가 있었다는 뜻으로 보이나, 대상·가격·수익성 근거는 수집되지 않았다. 인수 수익률은 평가할 수 없다. [F57] [F58] [F59] [S4](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000020/alab-20260331.htm)
- [capital_allocation] 재투자 강도는 높다. R&D는 FY2026Q1 1.3억 USD, FY2026Q2 1.4억 USD로 꾸준히 늘었고, ROIC는 FY2024 -13.1%에서 FY2025 14.5%로 개선됐다. 설비투자는 낮은 수준이다(FY2025 3,754만 USD). 이 ROIC 개선이 지속되는지는 연간 FY2026 값으로 확인해야 한다. [F143] [F144] [C:roic@FY2024] [C:roic@FY2025] [F8]

### 회계 품질 — watch

숫자는 대체로 믿을 만하다. 영업현금흐름이 순이익보다 크고(FY2025 OCF 3.2억 vs 순이익 2.2억), 발생액 비율은 음수(C:accruals_ratio@FY2025 -7.7%)이며, 정정·감사인 변경 신호는 없고, 영업권 비중도 낮다. 코드 신호 5개는 모두 SBC·IPO 전환·소규모 이연매출처럼 구조적으로 설명된다. 다만 조정해서 봐야 할 숫자가 세 가지 있다. (1) SBC는 실제 비용이므로 SBC 차감 FCF(FY2025 1.2억)로 봐야 하고, 이것이 FCF 2.8억의 절반 안팎이다. (2) 2026년 2분기 순이익 1.5억은 세전이익 1.0억에 세금 환급 5,026만이 얹힌 값이라, PER 141.8배는 일회성 세금 효과를 포함한 값이다. (3) Non-GAAP 영업이익(1.535억)은 GAAP(8,925만)보다 크게 높아 Non-GAAP 지표는 그대로 쓰면 안 된다. 감사의견·특수관계자·Non-GAAP 조정 내역은 확인하지 못했다. red_flag를 줄 증거는 없으므로 watch로 판정한다.

- [benign] sbc_to_revenue: FY2024의 SBC/매출 59.2%는 IPO 시점 일회성 RSU 인식이 크다. FY2025는 18.8%로 내려왔고 2026년 2분기 SBC 6,399만은 분기 매출 3.9억의 약 16%다. 문턱(10%)은 넘지만 매출 급성장으로 비율은 하락 추세다. 다만 분기 SBC 금액은 계속 늘고 있어(4,137만→4,891만→6,399만) 비용으로 취급해야 한다. [C:sbc_to_revenue@FY2024] [C:sbc_to_revenue@FY2025] [F153] [F135] [F182] [F152]
- [concern] sbc_to_ocf: FY2025 SBC/OCF 50.1%는 문턱(50%)을 간신히 넘는다. FY2024의 171.6%에서는 크게 개선됐지만, FCF 2.8억 중 SBC가 1.6억이어서 SBC 차감 FCF는 1.2억에 그친다. 주주 입장의 실질 현금창출력은 보고 FCF의 절반 안팎이므로 밸류에이션에는 SBC 차감 FCF를 써야 한다. [C:sbc_to_ocf@FY2025] [C:sbc_to_ocf@FY2024] [C:fcf_after_sbc@FY2025] [C:fcf@FY2025] [F148]
- [benign] receivables_gap: FY2024 매출채권 증가율이 매출 증가율을 123.4%p 웃돈 것은 FY2023 기저가 작았기 때문이다(834만→3,881만). DSO는 FY2024 35.7일, FY2025 35.6일로 안정돼 채권 누적이나 매출 당겨쓰기 증거는 아니다. 다만 FY2026Q2 매출채권이 1.9억으로 늘었으므로 DSO가 다시 올라가는지 추적해야 한다. FY2025Q1 6,978만→Q2 2,432만처럼 분기 변동이 크다. [C:receivables_gap] [C:dso@FY2024] [C:dso@FY2025] [F119] [F120] [F126] [F121] [F122]
- [benign] deferred_revenue: 이연매출은 FY2024 1,500만에서 FY2025 0으로 줄었다. 금액이 FY2025 매출 8.5억의 2% 미만이고, 같은 해 OCF가 순이익을 웃돌아 선수금을 당겨쓴 정황은 없다. 신호는 작은 기저 때문에 생긴 것으로 본다. 다만 이연매출이 사라진 이유(고객 선급금 정산 등)는 공시에서 확인하지 못했다. [C:deferred_revenue] [F37] [F38] [F130] [F98] [F89]
- [benign] dilution: 연 73.9% 증가는 2024년 IPO와 우선주 전환으로 FY2023 3,713만에서 FY2024 1.3억으로 뛴 영향이 지배적이다. 이후 희석 주식 수는 FY2025 1.8억에서 FY2026Q2 1.8억으로 거의 늘지 않았고, 2026년 7월 말 발행주식 수는 약 1.73억이다. 자사주 매입은 없다(FY2025 0). 향후 희석은 SBC 규모에 연동된다. [C:dilution] [F40] [F41] [F42] [F47] [F154] [F4]
- [watch] 2026년 2분기 순이익 1.5억은 세전이익 1.0억보다 크다. 세금 환급 5,026만이 이익을 부풀린 것이다(1분기도 -690만, 2025년 3분기 -2,425만으로 환급이 반복됨). 반면 2025년 4분기에는 세금 비용 3,393만이 발생해 분기별 순이익이 세금 때문에 크게 흔들린다. 밸류에이션에는 순이익·PER(141.8배)보다 영업이익이나 정상 세율을 가정한 이익이 낫다. [F94] [F118] [F77] [F76] [F75] [F176] [C:pe]
- [watch] 2026년 2분기 Non-GAAP 영업이익 1.535억(마진 39.1%)은 GAAP 영업이익 8,925만과 큰 차이가 난다. 주된 조정은 SBC 6,399만으로 보이나, 그 밖의 조정 항목(무형자산 상각, 인수 관련 비용 등)은 확인하지 못했다. 3분기 가이던스 EPS 1.16~1.21달러도 Non-GAAP 기준이므로 GAAP 기준으로 환산해 비교해야 한다(S39의 GAAP EPS 가이던스 0.87~0.92달러). [F189] [F188] [F109] [F153] [F193] [S38](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000033/q226exhibit991.htm) [S39](https://247wallst.com/companies/alab/earnings/2026/Q2)
- [watch] 2026년 2분기 재고가 6,016만에서 1.1억으로 급증했고 매출채권도 1.3억에서 1.9억으로 늘었다. 분기 매출 증가(3.1억→3.9억)로 일부 설명되지만 재고 증가율이 매출 증가율보다 크다. 3분기 가이던스(5.4억~5.6억)를 위한 선제 재고일 가능성이 높으나, 다음 분기에 재고일수(DIO)가 되돌아오는지 확인해야 한다. [F84] [F85] [F125] [F126] [F134] [F135] [F185]
- [info] 영업권이 FY2025 1,902만에서 FY2026Q1 8,772만, Q2 9,156만으로 늘었다. 인수가 있었음을 뜻하지만 총자산(1.9억 USD 규모의 19.3억) 대비 약 5%로 문턱(40%)과 거리가 멀다. 인수 대상과 가격은 확인하지 못했다. [F57] [F58] [F59] [F162] [C:goodwill_to_assets]
- [info] 코드 신호에 8-K 4.02(재무제표 정정)와 4.01(감사인 변경)은 없다. 다만 감사의견(계속기업 의문·핵심감사사항), 특수관계자 거래, 내부자 매각은 리서처가 확인하지 못했다. 10-K(S7)와 DEF 14A(S6)에서 직접 확인하는 것이 좋다. 이 항목들이 확인되지 않았다는 점이 grade를 clean이 아니라 watch로 두는 이유 중 하나다. [S7](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000010/alab-20251231.htm) [S6](https://www.sec.gov/Archives/edgar/data/1736297/000114036126016359/ny20065212x1_def14a.htm)

## 레드팀 — 사전 부검 (5년 뒤 −60%라면)

- (20%) AI 설비투자가 소화 국면으로 바뀌며 멀티플이 무너진다. 주가는 EV/매출과 PER이 매우 높은 성장 지속을 전제로 형성돼 있었다. 하이퍼스케일러가 주문을 늦추면 3분기 가이던스 이후 성장 가속이 멈춘다. 이익이 줄지 않더라도 고성장 프리미엄이 사라지면 배수 압축만으로 주가가 크게 떨어진다. 기본 시나리오는 출구 P/FCF를 32배로 두는데, 성장이 한 자릿수 후반이나 10%대로 꺾인 기업이 이 배수를 유지하기는 어렵다. 로그 기여로 보면 멀티플 변화가 매출 성장의 이익을 거의 전부 상쇄한다. [C:ev_revenue] [C:pe] [S33](https://news.google.com/rss/articles/CBMingFBVV95cUxPR3VxWjF6UmpuQVFGazJlT3BDRTlOdTkzb1Z6bXRjdjE1LVZOWHBjQld5aDlGdk05aVU2SE5SY2lrOHZ0QWI5aHczOUtndjNvc1VIVFBCZXVkeGlldkUtM1Q3S3ptQUJJbHlxQ1dUZm9KZ0ZpWkJLZmRxUW9uNHZBaWlUa09hU3BzcW9uZTNqMG5IYXh2RGFxdGp5MXlZZw?oc=5) [S31](https://news.google.com/rss/articles/CBMimAFBVV95cUxNdlRpdVZsRW9GOWNWZ0E0WTVScl80eDIzV2hKaUdIb3Ffc2ZMUnVURm5CUW4tc05ra3dFbHhod2dZbVJWbGNyb0FZaDZyb3B1cEVFeWFST3pKdk16TjhPUmFQMWs1ekNlNTF4TExPTTJLcDRleEI3Nm9veVF0YWtSQjJBQmlnVmkzU3Q4MnBOci1TNTROUzVPQw?oc=5) [S36](https://news.google.com/rss/articles/CBMimwFBVV95cUxPZ3NyOU11MHBMLVM1bWpkdHRwTHpOOWlOQVk2YS1aandWZk9xUFBuOGNCV1ZTTlVHZXZzQ2Q2TERNcjdsVkRlcWQ4azlWZzZnWVdIaWZ6U0d6ZHRJam9EaWxkSC0tZGpHY1ZKamxTaEdjQ3Z6VTdBVmVPSnJ6QnR0MjVXWVhramg1aXZJRktfc01qOUxKc2UtcGNKNA?oc=5)
- (20%) 경쟁과 고객의 자체 설계로 가격 결정력이 약해진다. 해자 증거는 보도 수준(claimed)에 머물러 있고 설계 수주 수, 고객 집중도, 제품별 매출은 확인되지 않았다. 경쟁사(Credo 등)가 같은 구간 제품을 내고, 엔비디아의 랙 개방 흐름은 표준화로 이어져 리타이머·스위치가 범용품이 될 수 있다. 소수 고객이 자체 연결 칩으로 옮기거나 가격 인하를 요구하면 총이익률이 내려간다. 총이익률 가이던스는 이미 2분기 실적보다 낮다. 이 하락이 일시적 믹스 효과가 아니라 가격 압력이라면 FCF 마진 가정이 무너진다. [S23](https://news.google.com/rss/articles/CBMikAFBVV95cUxQRU5TbmtpSHJ5QkJSdWxsUTdCNHFMUnNhMDZyQm1VZkNMQzgwSGtfZDJGOEVWOGdjV2otZ2dQUmlsX1FsZV9BNk5mWVJTSVU2MGdNMnNWUGhNaWZUMENqUVBTZkc3RDN4bEZLNl9veHc1YTBvR2xuS2lJMldIZHpnS3NqMmpCYmJzNDFZRXdfNHU?oc=5) [S34](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQkRNUnVZc0JGMVdRZVUtWW5aX3FIbGFUa2F4SlE5LUFyc0ttQ2E3WktDMktsY01mNWl6d2dTbC1RQWhlVXF2QU1GN0s4Zk1iRGo5MXZMTDBmRWtRc0lvRUVYMjJoS2R2RXo2SUlxdWg3Y2NpZkRnd0R2bFFiSW1haTNMcldaSTh5cGRPU3hGQVcwMXpQbjRHZw?oc=5) [F186] [F187] [S29](https://news.google.com/rss/articles/CBMingFBVV95cUxNemw5bzRDQUs2TGt0MFhQeGhOWktDcVA5WE1PTWcxbk5LYzlpVGtwNnljcWpzcGhnSU1oWElUTVM1d2FoUlpialJ1SzkzMjEzY3Y1eW5Hd1VBVHpQejJHSXEwWWdZZ3ZSczhNN0FhOHd2TEt4MURGb1RPX2dBMGo2MWViX3NNck1sY2NfeHlqZ1dCVXVyQXNLaFV5dkxrQQ?oc=5)
- (15%) 이익의 질이 드러나면서 실질 수익력이 보고 숫자의 절반 안팎으로 재평가된다. 분기 SBC가 매 분기 늘고 있고 SBC 차감 FCF는 보고 FCF의 절반 안팎이다. 2분기 순이익은 세금 환급 덕분에 세전이익보다 크게 부풀려졌다. 시장이 Non-GAAP EPS와 PER 대신 SBC 차감 이익과 정상 세율 이익으로 가치를 매기기 시작하면 같은 사업에 훨씬 낮은 배수가 적용된다. 자사주 매입이 없어 희석이 그대로 주주에게 전가되고, 가이던스의 희석 주식 수는 현재 발행주식 수보다 많다. [C:fcf_after_sbc@FY2025] [C:sbc_to_ocf@FY2025] [F153] [F77] [F118] [F194] [F154] [F4]
- (12%) 재고와 매출채권이 매출보다 빨리 쌓이며 수요 선반영과 재고 평가손실로 이어진다. 2분기에 재고는 약 두 배, 매출채권은 크게 늘었다. 고객이 최종 수요보다 앞서 물량을 확보했다면 3분기 가이던스는 선당김이고, 이후 주문이 줄면서 재고가 쌓이고 수금이 늦어진다. 이연매출이 없는 구조라 선행 수주 완충도 없다. 경영진의 가이던스 적중 이력은 수집되지 않아 이 위험을 사전에 걸러낼 근거가 없다. [F84] [F85] [F125] [F126] [F38] [C:dso@FY2025]
- 약한 가정 `base.exit_multiple`: 5년 뒤 출구 P/FCF 32배는 그때도 고성장 기업이어야 정당화된다. 기본 시나리오의 마지막 해 성장률은 18%로 둔화돼 있는데, 이 정도 성장의 기업에 32배를 적용하는 것은 일관성이 약하다. 수익률 분해에서 멀티플 변화가 매출 성장 기여를 거의 모두 상쇄하므로, 이 가정이 결과를 가장 크게 좌우한다. 민감도 표에서 출구 배수가 0.75배만 돼도 기본 시나리오 수익률이 마이너스로 내려간다. [C:ev_revenue] [C:pe] [C:expected_irr]
- 약한 가정 `base.fcf_margin`: FY2025의 FCF 마진을 그대로 유지한다고 가정하면서 같은 시나리오에서 총이익률이 약 72%로 내려간다고 쓰고 있다. 마진 하락 요인(믹스·가격)과 유지 요인(고정비 레버리지)을 동시에 놓았는데, 근거는 레버리지 쪽에만 있다. 또 SBC가 비용으로 들어간 SBC 차감 FCF 기준이 아니라 보고 FCF 기준이다. [C:fcf_margin@FY2025] [C:fcf_after_sbc@FY2025] [F187]
- 약한 가정 `base.revenue_growth`: 기본 시나리오의 2027년 이후 성장률(45%, 30%, 22%)은 기저율 표 없이 정한 값이다. 고객 집중도와 설계 수주 같은 수요 지속성 근거가 없고, 컨센서스도 확보하지 못해 시장 기대 대비 위치를 확인할 수 없다. 약세 시나리오 확률 30%는 AI 설비투자 순환의 하락기 가능성을 반영하기에 낮을 수 있다. [C:base_rate@base] [F185] [S33](https://news.google.com/rss/articles/CBMingFBVV95cUxPR3VxWjF6UmpuQVFGazJlT3BDRTlOdTkzb1Z6bXRjdjE1LVZOWHBjQld5aDlGdk05aVU2SE5SY2lrOHZ0QWI5aHczOUtndjNvc1VIVFBCZXVkeGlldkUtM1Q3S3ptQUJJbHlxQ1dUZm9KZ0ZpWkJLZmRxUW9uNHZBaWlUa09hU3BzcW9uZTNqMG5IYXh2RGFxdGp5MXlZZw?oc=5)

## 검증 (L6)

주장 73개 — supported 56 · unsupported 15 · contradicted 0 · leap 2 · 미검증 0

- [unsupported] 앤더슨: 레드팀의 사전 부검 네 개를 성장 가설을 깨는 것과 경로의 소음으로 나눈다. 수요 소화 국면과 가격 압력은 가설 자체를 깬다. 3분기 매출이 가이던스 하단에 못  — 출처 없는 숫자 18% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 경영진·자본배분: FY2025 말 1,902만 USD이던 영업권이 FY2026Q1에 8,772만 USD, FY2026Q2에 9,156만 USD로 늘었다. FY2026Q1에 약 7천 — 출처 없는 숫자 7000 — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [leap] 모델러: 기본 시나리오의 기대수익률이 요구수익률을 크게 넘지 않을 것으로 본다. 단기 실적(3분기 가이던스 F185)이 맞아도 SBC 차감 이익과 성장 둔화가 반영되면 현 — 총이익률 가이던스 72%는 맞지만, 인용 자료에는 그것이 믹스 변화 때문이라는 근거가 없다.
- [unsupported] 레드팀: 기본 시나리오의 2027년 이후 성장률(45%, 30%, 22%)은 기저율 표 없이 정한 값이다. 고객 집중도와 설계 수주 같은 수요 지속성 근거가 없고, 컨센서 — 없는 근거 인용: C:base_rate@base
- [leap] 회계 품질: 연 73.9% 증가는 2024년 IPO와 우선주 전환으로 FY2023 3,713만에서 FY2024 1.3억으로 뛴 영향이 지배적이다. 이후 희석 주식 수는 FY2 — 희석 주식 수 숫자는 모두 맞다. 그러나 IPO와 우선주 전환이 원인이라는 설명은 인용 자료에 없다.
- [unsupported] 레드팀: 이익의 질이 드러나면서 실질 수익력이 보고 숫자의 절반 안팎으로 재평가된다. 분기 SBC가 매 분기 늘고 있고 SBC 차감 FCF는 보고 FCF의 절반 안팎이다. — SBC 차감 FCF, 세금 환급, 희석 주식 수 비교는 맞다. 그러나 '분기 SBC가 매 분기 늘고 있다'는 추세는 인용에 2분기 한 점뿐이라 받쳐지지 않는다.
- [unsupported] 회계 품질: 영업권이 FY2025 1,902만에서 FY2026Q1 8,772만, Q2 9,156만으로 늘었다. 인수가 있었음을 뜻하지만 총자산(1.9억 USD 규모의 19.3 — 없는 근거 인용: C:goodwill_to_assets
- [unsupported] 애크먼: 사업의 질은 높다. FCF 마진 33.1%, 순현금 구조, 총이익률 70%대 중반이다. 자본시장 의존이 없다는 점은 밸리언트식 실패 위험을 제거한다. 그러나 이는 — 출처 없는 숫자 70% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 레드팀: 5년 뒤 출구 P/FCF 32배는 그때도 고성장 기업이어야 정당화된다. 기본 시나리오의 마지막 해 성장률은 18%로 둔화돼 있는데, 이 정도 성장의 기업에 32배 — 출구 배수 32배, 수익률 분해, '0.75배에서 마이너스'라는 민감도는 인용에 없다. 기본 시나리오 IRR은 이미 -0.3%라 서술과 어긋난다.
- [unsupported] 슬레이터: 이익의 질은 조정해서 봐야 한다. SBC 차감 FCF는 보고 FCF의 절반에 못 미치고, 분기 SBC는 계속 늘고 있으며, 2분기 순이익은 세금 환급 때문에 부풀 — SBC 차감 FCF가 절반에 못 미치고 세금 환급이 있다는 것은 맞다. 그러나 '분기 SBC가 계속 늘고 있다'는 추세와 총이익률 하락이 믹스 때문이라는 원인은 인용에 없다.
- [unsupported] 애크먼: 10년 뒤 주당 가치가 5배를 넘는 길은 강세 시나리오(확률 20%)에서만 열린다. 이는 생존자 편향에 기댄 가정이다. 코드가 계산한 확률 가중 기대 연 수익률은 — 없는 근거 인용: C:revenue_5y
- [unsupported] 사업·산업: 플랫폼에 한번 설계되어 들어가면 교체가 어렵다는 전환비용 논리가 보도에 반복된다. 엔비디아가 랙에 타사 AI 칩을 허용하는 흐름에서 수혜를 본다는 보도(S34)가 — S34, S29, S30은 랙 개방, 신제품, Scorpio 램프를 다룬다. '전환비용 논리가 보도에 반복된다'는 내용은 인용에 없다.
- [unsupported] 회계 품질: FY2024의 SBC/매출 59.2%는 IPO 시점 일회성 RSU 인식이 크다. FY2025는 18.8%로 내려왔고 2026년 2분기 SBC 6,399만은 분기  — SBC/매출 59.2%, 18.8%, 약 16%, 분기 SBC 추세는 맞다. 그러나 FY2024가 'IPO 시점 일회성 RSU 인식'이라는 원인은 인용에 없다.
- [unsupported] 애크먼: 사전 부검이 가리키는 두 가지 위험, 멀티플 압축과 총이익률 하락은 모두 FCF 범위를 넓힌다. 기본 시나리오의 출구 P/FCF 32배가 성장 18%에서 정당화되 — 출처 없는 숫자 18% — 근거에도 계산값에도 없다 (직접 계산했다면 '추정:'으로 시작)
- [unsupported] 애크먼: 사전 부검: 세 분기 연속 가이던스를 상회하는 실적과 AI 설비투자 가속이 이어지면 시장은 기본 시나리오의 성장 가정을 계속 위로 수정할 수 있다. 가격은 내재가 — '세 분기 연속 가이던스 상회'는 인용에 없다. 인용한 것은 2분기 컨센서스 상회뿐이고, 가이던스 이력은 수집되지 않았다.
- [unsupported] 슬레이터: 생존은 문제가 아니다. FY2025 FCF 마진이 흑자이고 팹리스라 설비투자 부담이 작으며, 코드가 계산한 기본 시나리오 현금 경로도 0 아래로 내려가지 않는다. — 없는 근거 인용: C:cash_survives@슬레이터
- [unsupported] 사업·산업: 총이익률이 FY2022부터 FY2025까지 68.9~76.4% 범위에서 유지됐다. 규모가 커지는 동안(FY2023 1.2억 → FY2025 8.5억 달러)에도 유 — 총이익률 68.9~76.4% 범위는 맞다. 그러나 FY2023 매출 1.2억 달러와 FY2025 매출 8.5억 달러는 인용에 없다.

## 계산 근거 (L3)

### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@FY2025)

| 지표 (키) | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| 매출 (revenue) | 7,987만 USD | 1.2억 USD | 4.0억 USD | 8.5억 USD |
| 매출 성장 (revenue_growth) | — | 45.0% | 242.2% | 115.1% |
| 총이익률 (gross_margin) | 73.5% | 68.9% | 76.4% | 75.7% |
| 영업이익률 (operating_margin) | -75.4% | -25.5% | -29.3% | 20.3% |
| 순이익 (net_income) | -5,834만 USD | -2,626만 USD | -8,342만 USD | 2.2억 USD |
| 영업현금흐름 (ocf) | -3,590만 USD | -1,272만 USD | 1.4억 USD | 3.2억 USD |
| 설비투자 (capex) | 387만 USD | 276만 USD | 3,424만 USD | 3,754만 USD |
| FCF (fcf) | -3,977만 USD | -1,548만 USD | 1.0억 USD | 2.8억 USD |
| FCF 마진 (fcf_margin) | -49.8% | -13.4% | 25.8% | 33.1% |
| FCF/순이익 (fcf_conversion) | — | — | — | 1.29x |
| SBC (sbc) | 3,024만 USD | 1,068만 USD | 2.3억 USD | 1.6억 USD |
| SBC/매출 (sbc_to_revenue) | 37.9% | 9.2% | 59.2% | 18.8% |
| SBC/영업현금흐름 (sbc_to_ocf) | — | — | 171.6% | 50.1% |
| SBC 차감 FCF (fcf_after_sbc) | -7,001만 USD | -2,616만 USD | -1.3억 USD | 1.2억 USD |
| ROIC (roic) | — | — | -13.1% | 14.5% |
| 순현금 (net_cash) | — | 4,510만 USD | 7,955만 USD | 1.7억 USD |
| 순부채/EBITDA (net_debt_to_ebitda) | — | — | — | -0.93x |
| 희석 주식 수 (diluted_shares) | 3,417만 | 3,713만 | 1.3억 | 1.8억 |
| 주식 수 변화 (share_change) | — | 8.7% | 253.5% | 36.8% |
| DSO(일) (dso) | — | 26.3 | 35.7 | 35.6 |
| DIO(일) (dio) | — | 244.5 | 168.5 | 103.9 |
| 발생액 비율 (accruals_ratio) | — | — | -35.2% | -7.7% |

표에 없는 키도 인용할 수 있다: buybacks, cash, cash_total, cost_of_revenue, d_and_a, debt_total, deferred_revenue, deferred_revenue_growth, ebitda, equity, goodwill, goodwill_to_assets, gross_profit, income_tax, inventory, inventory_growth, operating_income, pretax_income, receivables, receivables_growth, rnd, total_assets

### 시장 · TTM(FY2026Q2) 기준 (C:키)

| 항목 | 값 |
|---|---|
| 주가 (price) | 285.82 USD/share (2026-10-16, F183) |
| 희석 주식 수 (shares) | 1.8억 |
| 시가총액 (market_cap) | 524.0억 USD |
| 순현금 (net_cash) | 1.1억 USD |
| EV (ev) | 522.9억 USD |
| FCF 수익률 (fcf_yield) | — |
| P/FCF (p_fcf) | — |
| EV/매출 (ev_revenue) | 43.51x |
| PER (pe) | 141.82x |
| 순부채/EBITDA (net_debt_to_ebitda) | -0.39x |
| 현금 소진 연수 (runway_years) | — |

### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)

- [watch] sbc_to_revenue (C:sbc_to_revenue): SBC/매출 18.8% > 10%
- [watch] sbc_to_ocf (C:sbc_to_ocf): SBC/영업현금흐름 — FCF의 상당 부분이 주식 보상 50.1% > 50%
- [watch] receivables_gap (C:receivables_gap): FY2024 매출채권 증가율 - 매출 증가율 123.4% > 15%
- [watch] deferred_revenue (C:deferred_revenue): 매출은 늘었는데 이연매출이 10% 넘게 줄었다 — 매출 당겨쓰기 의심
- [watch] dilution (C:dilution): 희석 주식 수 연 73.9% 증가 > 3%

### 시나리오 가치 — 5년, 할인율 11% (C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)

| 시나리오 | 확률 | 5년 매출 | 매출 연성장 | FCF 마진 | 출구 P/FCF | 주당 가치 | 현재가치(IV) | 연 수익률 |
|---|---|---|---|---|---|---|---|---|
| 약세 | 30% | 17.7억 USD | 15.8% | 20% | 18x | 40.91 | 24.28 | -32.2% |
| 기본 | 50% | 49.7억 USD | 42.3% | 33% | 32x | 281.02 | 166.77 | -0.3% |
| 강세 | 20% | 77.5억 USD | 55.5% | 38% | 38x | 595.82 | 353.59 | +15.8% |

확률 가중: 주당 가치 271.95 · IV 161.39 · 기대 연 수익률 -1.0% (C:expected_irr) · 손실 확률 80% (C:p_loss) · 현재 주가 285.82

기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): 매출 성장 +35.3% · 마진 변화 -0.0% · 멀티플 변화 -35.2% · 주식 수 변화 -2.5% · 현금 축적 +2.0% = -0.3%

민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)

| 성장 \ 멀티플 | ×0.75 | ×1 | ×1.25 |
|---|---|---|---|
| -5%p | -9.8% | -5.2% | -1.3% |
| +0%p | -5.3% | -0.3% | +3.8% |
| +5%p | -0.7% | +4.5% | +8.9% |

기본 시나리오 연도별 (드라이버 모델)

| 기간 | 매출 | FCF 마진 | FCF | 희석 주식 수 | 순현금 |
|---|---|---|---|---|---|
| FY2026 | 18.3억 USD | 33.0% | 6.1억 USD | 1.9억 | 7.2억 USD |
| FY2027 | 26.6억 USD | 33.0% | 8.8억 USD | 1.9억 | 15.9억 USD |
| FY2028 | 34.6억 USD | 33.0% | 11.4억 USD | 2.0억 | 27.4억 USD |
| FY2029 | 42.2억 USD | 33.0% | 13.9억 USD | 2.0억 | 41.3억 USD |
| FY2030 | 49.7억 USD | 33.0% | 16.4억 USD | 2.1억 | 57.7억 USD |

### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)

- base 시나리오 매출 성장: 연 42.3% × 5년 → 기저율 표 없음
- bull 시나리오 매출 성장: 연 55.5% × 5년 → 기저율 표 없음

### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)

- 앤더슨 case={"from": "bull"}: upside_10y=6.67x, revenue_5y=9.10x
- 슬레이터 case={"from": "base"}: cash_survives=예, cash_min=1.1억 USD
- 애크먼 case={"from": "base"}: price=285.8, net_debt_to_ebitda=-0.39x, leveraged=아니오, intrinsic_value=166.8, mos=-71.4%

### 계산 경고

- 컨센서스 근거 없음 — 시장 기대와의 차이를 검증할 수 없다 (리서처: basis=consensus 사실)
- 기저율 표 없음 — `python3 council.py baserate`로 data/base_rates.json을 만든다

## 근거

| ID | 유형 | 날짜 | 출처 | 메모 |
|---|---|---|---|---|
| S1 | filing | 2026-08-05 | [10-Q](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000035/alab-20260630.htm) |  |
| S2 | filing | 2026-08-04 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000033/alab-20260804.htm) |  |
| S3 | filing | 2026-06-08 | [8-K](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000027/alab-20260604.htm) |  |
| S4 | filing | 2026-05-06 | [10-Q](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000020/alab-20260331.htm) |  |
| S5 | filing | 2026-05-05 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000017/alab-20260505.htm) |  |
| S6 | filing | 2026-04-23 | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1736297/000114036126016359/ny20065212x1_def14a.htm) |  |
| S7 | filing | 2026-02-20 | [10-K](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000010/alab-20251231.htm) |  |
| S8 | filing | 2026-02-10 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1736297/000110465926012649/tm265461d2_8k.htm) |  |
| S9 | filing | 2026-02-10 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1736297/000173629726000005/alab-20260210.htm) |  |
| S10 | filing | 2026-02-10 | [8-K 중요 계약](https://www.sec.gov/Archives/edgar/data/1736297/000110465926012606/tm265461d1_8k.htm) |  |
| S11 | filing | 2026-01-20 | [8-K 경영진 변동](https://www.sec.gov/Archives/edgar/data/1736297/000110465926005022/tm263452d1_8k.htm) |  |
| S12 | filing | 2025-11-05 | [10-Q](https://www.sec.gov/Archives/edgar/data/1736297/000173629725000147/alab-20250930.htm) |  |
| S13 | filing | 2025-11-04 | [8-K 실적 발표](https://www.sec.gov/Archives/edgar/data/1736297/000173629725000145/alab-20251104.htm) |  |
| S14 | filing | 2025-10-22 | [8-K 기타 중요 사항](https://www.sec.gov/Archives/edgar/data/1736297/000173629725000136/alab-20251022.htm) |  |
| S15 | filing | 2025-02-14 | [10-K (XBRL)](https://www.sec.gov/Archives/edgar/data/1736297/000173629725000003/0001736297-25-000003-index.htm) |  |
| S16 | filing | 2025-05-07 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1736297/000173629725000031/0001736297-25-000031-index.htm) |  |
| S17 | filing | 2025-08-06 | [10-Q (XBRL)](https://www.sec.gov/Archives/edgar/data/1736297/000173629725000098/0001736297-25-000098-index.htm) |  |
| S18 | news | 2026-08-30 | [Astera Labs Stock And 2 AI Data Center Picks From Founder Led Companies - Yahoo Finance](https://news.google.com/rss/articles/CBMikAFBVV95cUxPMWhsSHZCT3ZJanU5R2Z3S0szSkY3eFEybTJSZjVScWZSaW5abTNEY214YlA2aEprOWJLcFZCV3luTklBX0hKNHMtdHhyX1ByNlR5dTEwQWg0bnhyN1Z2QVhEUmlUOUZPU3F6V1BuaUFXbXowSHJOUW4xUWIwZ2NDUE0tRk1XN1JHRWVxeENWTTU?oc=5) | Yahoo Finance |
| S19 | news | 2026-08-06 | [Astera Labs Beat And Guided Higher, Then Fell Because The Rally Came First - Trefis](https://news.google.com/rss/articles/CBMizwFBVV95cUxNMlAzWVpPbmFJY1JQbkVWNng2Z254UGZ5VzJ6QllFQ1VkVUVTTzhxVzFpaEVLZmVQYlQ4OUJCd1YyTWNGazJ5ZGE3VGN1YmlSZ2JfeHdTZllTNXRPTmVMQTNwUF9wZUFlN0VaM2t2R3RTeXc4aWxzY1NfQ2NTWExnWGl2aFBtNGQ3dUpWZVAyaXRIa1dWbmlManVFSjV5Sk8xczc5bDBfMGNiVlRzTHRjOGZ3ZUtvTzJsaXF4QWpkRFR6Q3VLLU1HWDBaUWt2aUU?oc=5) | Trefis |
| S20 | news | 2026-08-25 | [Astera Labs Stock Is Up 116% in Six Months. Here’s What’s Behind the Rally. - TIKR.com](https://news.google.com/rss/articles/CBMinAFBVV95cUxPT1gtTlh2MFU0RF9tXzItbzE2ZGhJSXFZX0Y2OFBjU3BtTWZtb1pDYUwyREhNaEQyZ1dXd2pJSThmZEMwUC1rZXoyOFZIR19RT0hwaGFYNEFYMjRUV1luTmExSjVNRmhsLVVtUzJwSDl0Rzh4M3dwclZjRGZpMXNKbGdIbzVkSmF6WlNfbVozNjRGWFp4SEh0UFU5ME0?oc=5) | TIKR.com |
| S21 | news | 2026-08-17 | [Why Astera Labs, Inc. (ALAB) Might be Well Poised for a Surge - Yahoo Finance](https://news.google.com/rss/articles/CBMikwFBVV95cUxQWmt6cEpjQTVQX0FsUXhwY2ZzTDJieHZzaS1kWGF5VVpXSVdXR0VQZ3UzeW8xSTlGVVlSXzhrelVLQVFTaTZMcFJublNsbHJOT0hfU0NYanV2NnYzZkJjcmtrR19SdVVjbG9KVDNUMGpWS2Jnc3FRYXpLd0xkNWFhWXBvNEM1cDl0VExNMG9fX3d6Q3M?oc=5) | Yahoo Finance |
| S22 | news | 2026-08-01 | [Astera Labs vs. Arista Networks: Which Tech Stock Is a Better Buy in 2026? - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxOaVJvc0pzMGsyRGo3OGFia25QQW1rVDUwWXFxd2dvMDBzaE5XUi12MzdhR1VZS3ZxMGdzc1BNYkNfdnprMXFnZzJjNEdMcTR4Q2xJSHptNGJKWGVoajhxM2VXMEZEM0RCR21PSElrUzhwcmgtOEZCT1VwUWR0TXN5QUdUa25GOGVUQmRFWVlIbnltall0QVdHV0VYaw?oc=5) | Yahoo Finance |
| S23 | news | 2026-08-20 | [Credo vs. Astera Labs: Which AI Connectivity Stock Is the Better Buy? - Yahoo Finance](https://news.google.com/rss/articles/CBMikAFBVV95cUxQRU5TbmtpSHJ5QkJSdWxsUTdCNHFMUnNhMDZyQm1VZkNMQzgwSGtfZDJGOEVWOGdjV2otZ2dQUmlsX1FsZV9BNk5mWVJTSVU2MGdNMnNWUGhNaWZUMENqUVBTZkc3RDN4bEZLNl9veHc1YTBvR2xuS2lJMldIZHpnS3NqMmpCYmJzNDFZRXdfNHU?oc=5) | Yahoo Finance |
| S24 | news | 2026-08-04 | [Astera Labs, Inc. (ALAB) Beats Q2 Earnings and Revenue Estimates - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxOblgyVDVjeDFoR2x4bjhkUmprVzhNWFBrc3ZoVlQ0UC1HSXRrcGpGTUt3NUs2ajFtMXotUHo1ZUpMbDBVX3Btd1NWZ2pMQlViQXlyTlczSkNKcVRQYUo4OTFhNDlLdGZhRVFmdm13aTg3S3VvUlNobnZIeDFXMV9EVVpPa3hLcnl3SlJEeHZFWkUtQjBXYXc?oc=5) | Yahoo Finance |
| S25 | news | 2026-07-23 | [Astera Labs, Inc. (ALAB) Stock Moves -1.19%: What You Should Know - Yahoo Finance](https://news.google.com/rss/articles/CBMilgFBVV95cUxOaW9rM2RQNk9mV3NGNmh1eWIwbDduVzRvbm1rSzRfNTVVQnYxYnNjMkxWZ19Ca1pETGNqZDV6ZWNqaXh1dUp1UHdOVkpSWlpwS3pVc1ZPMjhFRGNTdnduVW50MG1Tc0M3WVJTYWxUM2ZqNGF4OVp2c0Q3Uk1lV2V6OER2dTRBOUhrdmRnN1ZDUExDdE5SOUE?oc=5) | Yahoo Finance |
| S26 | news | 2026-08-17 | [Astera Labs (ALAB), What Is Behind The Fresh Attention? - Yahoo Finance](https://news.google.com/rss/articles/CBMimgFBVV95cUxPNjVzOTlBWVFkMnRwekJDQnF0ZWxtVjZOeXVhWWp4cGdPVTVhYkpVNDB4VkZYZEZ1RkpHTnpnZU9wMXBBMDVSQVlnbUZoclRJTnd2a3pkYkN6VnRXNGFEdDBGNFlSS21EQ0lyVnh4bkJXM3FhUGFMMUF6eXJ1bjBwRXExVzNjd0F4VXpuQzdJN3lObE02VVNuNTdn?oc=5) | Yahoo Finance |
| S27 | news | 2026-08-06 | [Should Investors Hold on to Astera Labs Stock Post Q2 Earnings? - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPdV80cXNNcFhfSVdHcjlXUlE4Rm4tZFRaSHlvMGtFaEZXdWNZTDk1dEcza3lVUTZRMmxMeFRuWFV2cW9UMEZYcEZnTnVZZERyNjdRaDVNTVdfMWhqYTRZbGpYSmFuenV3Z2gtQTRnZ01ia0lieHllQ1cyeUdTRHVCTTVndU1DUEhxM2VVVTBHX3VIckVFLXZRaWMtVnoxUQ?oc=5) | Yahoo Finance |
| S28 | news | 2026-08-28 | [3 Under-the-Radar AI Stocks Wall Street Is Missing - Yahoo Finance](https://news.google.com/rss/articles/CBMikAFBVV95cUxOZlh4Y3Fsd25TLVBSRmNyb2gxd3N4MUE0RzZXS2E5Q3Vkek9tTjZIck1jRTN5QVFLSWRBZ0NYVVQtMlNJQ0NyWlBaVG1HaEw0Z2p5aDREOU13SUNLY0U4LXlrYk9nR0VJZ1Y5dWJuUDFMRWcySTBxQ3dxUURxaEczOV9CbWExYUV3TkFHUjJaLWs?oc=5) | Yahoo Finance |
| S29 | news | 2026-07-21 | [Astera Labs Expands Taurus Family with Industry’s First OCP-Standard Footprint Compatible 3.2T Smart Retimers and Smart Redrivers - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxNemw5bzRDQUs2TGt0MFhQeGhOWktDcVA5WE1PTWcxbk5LYzlpVGtwNnljcWpzcGhnSU1oWElUTVM1d2FoUlpialJ1SzkzMjEzY3Y1eW5Hd1VBVHpQejJHSXEwWWdZZ3ZSczhNN0FhOHd2TEt4MURGb1RPX2dBMGo2MWViX3NNck1sY2NfeHlqZ1dCVXVyQXNLaFV5dkxrQQ?oc=5) | Yahoo Finance |
| S30 | news | 2026-08-04 | [Astera Labs (ALAB) Is Up 40.6% After Record Q2 Results And Scorpio X-Series Ramp - What's Changed - Yahoo Finance](https://news.google.com/rss/articles/CBMijwFBVV95cUxQc0w4RlV6NG5USTZGT25qMllVdzI3S3hMcFBEdi1yb3A2Zng3TGR4em9Pa1h5b2J6cThFbml0WTRaQ0NFLXhMTUUxa3JuSlVmdUFlWmhZQ1RrU3NrY2hRNDBFV1UxSjZhUDJ4RF9QeEdaUVdtbEN1c3NUMHVrdElKYUVoUFFuaWE3WnFrZTEzWQ?oc=5) | Yahoo Finance |
| S31 | news | 2026-07-22 | [Astera Labs (ALAB) Stock Could Trade At A Premium Despite Fresh AI Demand Optimism - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxNdlRpdVZsRW9GOWNWZ0E0WTVScl80eDIzV2hKaUdIb3Ffc2ZMUnVURm5CUW4tc05ra3dFbHhod2dZbVJWbGNyb0FZaDZyb3B1cEVFeWFST3pKdk16TjhPUmFQMWs1ekNlNTF4TExPTTJLcDRleEI3Nm9veVF0YWtSQjJBQmlnVmkzU3Q4MnBOci1TNTROUzVPQw?oc=5) | Yahoo Finance |
| S32 | news | 2026-08-04 | [Astera Labs Q2 Earnings Call Highlights - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxPdHVXblBuanNQX0hyNVBtWncwc2hWN1BUSWg2TXp1NTdkdXlMZ2lTT3h3MWIxOEJZZXJXcXNDUlc4ZzE4UFJUZVYxc1dxd3g0LWcwdEJnSHZQbkZZaEg4RG95SjVuSHBQNU12T1EtUlRCazItdElDQmhnQTJkX1BCNFhTZ0pmSmlHRnFmSXdOMnAzeGl2VGVEdQ?oc=5) | Yahoo Finance |
| S33 | news | 2026-08-05 | [Astera Labs Sees Revenue Jumping 40% Next Quarter - Yahoo Finance](https://news.google.com/rss/articles/CBMingFBVV95cUxPR3VxWjF6UmpuQVFGazJlT3BDRTlOdTkzb1Z6bXRjdjE1LVZOWHBjQld5aDlGdk05aVU2SE5SY2lrOHZ0QWI5aHczOUtndjNvc1VIVFBCZXVkeGlldkUtM1Q3S3ptQUJJbHlxQ1dUZm9KZ0ZpWkJLZmRxUW9uNHZBaWlUa09hU3BzcW9uZTNqMG5IYXh2RGFxdGp5MXlZZw?oc=5) | Yahoo Finance |
| S34 | news | 2026-09-11 | [Nvidia Is Letting Rival AI Chips Into Its Racks. Astera Labs Could Be the Quiet Winner - Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQkRNUnVZc0JGMVdRZVUtWW5aX3FIbGFUa2F4SlE5LUFyc0ttQ2E3WktDMktsY01mNWl6d2dTbC1RQWhlVXF2QU1GN0s4Zk1iRGo5MXZMTDBmRWtRc0lvRUVYMjJoS2R2RXo2SUlxdWg3Y2NpZkRnd0R2bFFiSW1haTNMcldaSTh5cGRPU3hGQVcwMXpQbjRHZw?oc=5) | Yahoo Finance |
| S35 | news | 2026-07-29 | [Here's Why Astera Labs, Inc. (ALAB) Fell More Than Broader Market - Yahoo Finance](https://news.google.com/rss/articles/CBMilAFBVV95cUxNaWdkRWYwTklLYU1Gek9vWW5oWUlXZjh4djY4VkpaQ05WbENBbzNEQmxDSWpoTEF5ZG9jSTRmdWNDN0tiUTBHYU4zekxBTGVUVmVCeUVUVk1QSld5MWRyNUZNNXFRX2RMQ2dhNVcweWN3eTd3V2pDdl95dDlzVF9FTjdhTVlRWG03dlVmSU9GTll3YmVR?oc=5) | Yahoo Finance |
| S36 | news | 2026-07-29 | [Is Astera Labs (ALAB) Fairly Valued As Revenue Growth Hits 115%? - Yahoo Finance](https://news.google.com/rss/articles/CBMimwFBVV95cUxPZ3NyOU11MHBMLVM1bWpkdHRwTHpOOWlOQVk2YS1aandWZk9xUFBuOGNCV1ZTTlVHZXZzQ2Q2TERNcjdsVkRlcWQ4azlWZzZnWVdIaWZ6U0d6ZHRJam9EaWxkSC0tZGpHY1ZKamxTaEdjQ3Z6VTdBVmVPSnJ6QnR0MjVXWVhramg1aXZJRktfc01qOUxKc2UtcGNKNA?oc=5) | Yahoo Finance |
| S37 | news | 2026-08-03 | [Astera Labs, GlobalFoundries Positioned for Long-term AI Growth, Morgan Stanley Says - Yahoo Finance](https://news.google.com/rss/articles/CBMiqwFBVV95cUxQbG5PWWFDU21xb0t4dWtmZDFZNzJHRWd6S3dJZUhoc0NLbU5WeGxDd2Q3cFNHN3Noc2toN184elRhMlR0R0I5NjlUX3VXVGhQdk9kb01leTExZ1FTOG42SWJCc1l3U1NyMFB5ck9wWmtHQmo4TjlTMmFkUVNKbE1TWGktaVkyQjRLcmNPQjVveDBYUV9iTFJ4Tklrdmc3TWJDRllMTlVuMFBjd3c?oc=5) | Yahoo Finance |
| S38 | filing | 2026-08-04 | [Astera Labs Reports Second Quarter 2026 Financial Results (8-K Exhibit 99.1)](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000033/q226exhibit991.htm) | 2분기 매출 3.924억 달러(전분기 대비 +27%, 전년 대비 +104%). Non-GAAP 총이익률 73.7%, Non-GAAP 영업이익 1.535억 달러(영업이익률 39.1%), Non-GAAP 희석 EPS 0.80달러. 3분기 가이던스: 매출 5.4억~5.6억 달러, Non-GAAP 총이익률 약 72%, Non-GAAP 영업비용 1.56억~1.60억 달러, Non-GAAP 희석 EPS 1.16~1.21달러(희석 주식 약 1.85억 주). 가이던스 수치는 2차 요약(247wallst·MarketBeat)과 일치하나 3분기 항목은 공시 원문 대조 전 요약 출처 기준. |
| S39 | data | 2026-08-04 | [Astera Labs, Inc. (ALAB) Q2 2026 earnings summary - 247wallst](https://247wallst.com/companies/alab/earnings/2026/Q2) | 3분기 가이던스(매출 5.4억~5.6억 달러, Non-GAAP EPS 1.16~1.21달러, GAAP EPS 0.87~0.92달러, 희석 주식 약 1.85억 주) 요약. 2차 출처. |
| S40 | data | 2026-10-16 | [ALAB 월별 주가 이력 - digrin](https://www.digrin.com/stocks/detail/ALAB/price) | 페이지의 10월 최신값 285.82달러(수정·실제 동일). 일별 종가·정확한 기준일은 페이지에 없어 날짜는 기준일 직전 거래일(2026-10-16)로 가정한 추정이다. 월말 종가: 7월 311.23, 8월 296.98, 9월 355.97달러. 참고로 equibles는 2026-08-21 종가 284.97달러, 52주 범위 100.27~483.02달러. |
| S41 | data | 2026-08-04 | [Astera Labs announces earnings results 2026-08-04 - MarketBeat](https://www.marketbeat.com/instant-alerts/astera-labs-nasdaqalab-announces-earnings-results-2026-08-04/) | 2분기 매출 컨센서스 약 3.6085억 달러 대비 실제 3.924억 달러(+8.8%). EPS 컨센서스 0.69달러 대비 0.80달러. 3분기 Non-GAAP 총이익률 가이던스 약 72%. 2차 출처(집계 사이트). |

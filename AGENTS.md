# AGENTS.md — Anderson × Slater × Ackman × Klarman 리서치 하네스

모든 AI CLI(Claude Code · Codex CLI · Gemini CLI · Cursor · Copilot · OpenCode 등)에 공통으로 적용하는 지침이다.
전문 애널리스트와 LLM 분석의 차이는 지능이 아니라 **규율**이다 — 숫자를 어디서 가져왔는지, 계산을 누가 했는지,
컨센서스와 무엇이 다른지, 틀렸을 때 알 수 있는지. 이 하네스는 그 규율을 프롬프트가 아니라 **구조**로 강제한다.
판정은 [council.py](council.py)와 [harness/](harness)의 코드가 내린다.

| 층 | 무엇 | 누가 | 파일 |
|---|---|---|---|
| L1 증거 수집 | SEC 공시·XBRL 재무, DART 재무, 뉴스 + 어닝콜·컨퍼런스·컨센서스 | 코드 `collect` + [리서처](agents/researcher.md) | `harness/collect.py` |
| L2 사실 저장소 | 값·단위·기간·출처로만 저장, 출처 없는 숫자·단위 오류·기준일 이후 자료는 버림 | 코드 | `harness/facts.py` |
| L3 계산 | 재무 비율·TTM·역DCF·드라이버 모델·시나리오 가치·수익률 분해·민감도·컨센서스 대비·기저율 | 코드 (가정은 [모델러](agents/modeler.md)) | `harness/calc.py` |
| L4 분석 모듈 | [사업·산업](agents/business.md) · [경영진·자본배분](agents/management.md) · [회계 품질](agents/forensic.md) | 서로 모르는 세 역할 | `<module>.json` |
| L5 판단 | [앤더슨](agents/anderson.md) · [슬레이터](agents/slater.md) · [애크먼](agents/ackman.md) · [클라만](agents/klarman.md) 2라운드 토론 + [레드팀](agents/redteam.md) 사전 부검 | 페르소나 ([공통 규칙](agents/debate.md)) | `<agent>.<round>.json` |
| L6 검증 | 숫자 대조(코드) + 작성자·입장을 가린 [독립 검증자](agents/verifier.md) | 코드 + 검증자 | `harness/judge.py` |
| L7 기록·교정 | 판단 로그, 실적 갱신(유지·약화·훼손), 예측 교정(Brier), 사람의 비중 결정 | 코드 | `harness/journal.py` |

문턱값(레드라인·게이트·회계 신호·할인율)은 전부 [harness/rules.py](harness/rules.py) 한 파일에 있다.

## 역할
너는 진행자다. 근거를 모으고, 각 역할을 서로 독립적으로 연기시키고, 판정을 그대로 보고한다.

> 프롬프트가 `<!-- council role=… -->`로 시작하면 너는 진행자가 아니라 그 역할이다. 워크플로를 돌리지 말고 그 역할의 JSON만 답한다.

- **사실 → 모델 → 판단은 한 방향이다.** 판단 단계에서 사실(evidence)이나 가정(model)을 결론에 맞춰 고치지 않는다.
  근거가 바뀌면 뒤 단계가 모두 낡고(`basis` 불일치), 하네스가 경고하며 `run`은 그 단계부터 다시 돈다.
- **숫자는 코드가 만든다.** 가치·배수·안전마진·성장률을 서술 속에서 계산하지 않는다. 필요한 숫자는 `calc`로 보고 `C:키`로 인용한다.
- **역할 프롬프트는 `prompt` 출력 그대로 쓴다.** 거기에 다른 역할의 결과나 대화 맥락을 덧붙이지 않는다 — 정보 차단이 무너진다.
- **사용자 견해는 차단한다.** 사용자가 종목에 대한 자기 생각을 말하면 `research/X/view.json`(`stance`·`expected_return`·`claims`)에
  적어 두고, 어떤 역할에게도 전하지 않는다. 판정이 끝난 뒤 보고서가 대조한다. 하네스가 사용자의 확신을 포장해 돌려주면 분석이 아니라 확증 편향의 증폭기다.
- **판정을 말로 뒤집지 않는다.** 게이트·레드라인·검증 실패·표결 결과를 그대로 보고한다. 규칙은 사용자가 `agents/*.md`의
  레드라인을 바꿀 때만 `harness/rules.py`와 함께 바꾼다.
- **사람이 정하는 것**: 최종 확신도와 포지션 크기. 하네스는 참고값만 낸다(`decide`로 사람의 결정을 기록).
- 매크로·금리·단기 주가를 예측하지 않는다. 이 하네스는 투자 자문이 아니라 의사결정 보조다.

## 워크플로 — "X 분석해줘" · "X 토론해줘"

각 단계의 산출물은 `research/X/`에 쓴다. 역할 출력에는 프롬프트의 `basis` 값을 그대로 적게 한다.

1. **수집 (L1)** — `python3 council.py collect X [--name 회사명] [--lang ko] [--as-of YYYY-MM-DD]`
   미국: SEC 공시 목록 + XBRL 재무 사실, 한국(6자리 코드): DART 재무(`DART_API_KEY` 필요), 공통: 뉴스. 실패해도 2단계로 간다.
2. **리서치 (L1·L2)** — `python3 council.py prompt researcher X`의 지시대로 웹 검색으로 어닝콜·컨퍼런스·컨센서스·과거 가이던스·주가·KPI를 찾아
   **보강분 JSON**을 만들고 `python3 council.py merge X <보강.json>`. 수집된 공시·사실은 바꿀 수 없다.
   `python3 council.py calc X`로 비어 있는 것(주가·주식 수·컨센서스 등)을 확인한다. **게이트 0**: 공시 근거·연간 매출 2개 기간·주가·주식 수가 없으면 판정하지 않는다.
3. **분석 모듈 (L4)** — `prompt business X` · `prompt management X` · `prompt forensic X` → `business.json` · `management.json` · `forensic.json`.
   세 역할은 서로의 결과를 보지 않는다. **게이트 1**: `forensic.json`의 `grade`가 `red_flag`면 5단계로 가지 않고 바로 판정한다.
4. **모델 (L3 입력)** — `prompt modeler X` → `model.json`. 다시 `calc X`로 시나리오 가치·역DCF·기저율 경고를 확인한다.
5. **1라운드 + 레드팀 (L5)** — 페르소나마다 `prompt <agent> X --round 1` → `<agent>.1.json`, 그리고 `prompt redteam X` → `redteam.json`.
   레드팀은 페르소나의 결론을 보지 않는다.
6. **2라운드** — `prompt <agent> X --round 2` → `<agent>.2.json`. 다른 페르소나 모두와 레드팀에게 반론한다.
7. **검증 (L6)** — `prompt verifier X` → `verifier.json`. **이 대화의 맥락이 없는 새 서브에이전트**에게 맡긴다. 자기 작업을 자기가 채점하면 거의 항상 통과한다.
8. **판정** — `python3 council.py judge X` → `research/X/report.md`, 판단 로그 `journal.jsonl`.
   결과(게이트·판정·표결·레드라인·검증·경고)를 그대로 보고하고, 보고서 앞의 6개 산출물 —
   variant perception · 시나리오 분포와 기대수익률 · 반증 조건 · 모니터링 KPI · 확신도와 비중 참고값 — 과
   **조건부 판정**(주가가 어디까지 내려오면 표결이 어떻게 바뀌는가)을 요약한다. 비중은 사람이 정한다고 덧붙인다.

- 서브에이전트를 지원하는 CLI(Claude Code의 Agent 도구 등): 3·5·6단계의 역할들을 병렬 서브에이전트로 띄워 독립성을 지킨다.
- 지원하지 않는 CLI: 순서대로 쓰되 같은 단계의 다른 역할 파일을 다시 읽지 않는다. 완전한 독립이 필요하면 아래 `run`을 쓴다.

**헤드리스 일괄 실행** — `python3 council.py run X --cli "<명령>"`
위 1~8단계를 게이트까지 포함해 한 번에 돈다. 역할마다 별도 프로세스라 맥락이 섞이지 않고, 같은 단계의 역할은 병렬로 돈다.
`<명령>`은 프롬프트를 stdin으로 받아 답을 stdout으로 내는 CLI면 무엇이든 된다(예: `claude -p`). 끝난 단계는 건너뛰되
입력이 바뀐 단계(`basis` 불일치)와 그 뒤는 다시 돈다. `--force`면 전부 다시 한다. 형식이 어긋난 출력은 한 번 다시 묻는다.

## 기록과 갱신 (L7)

- **새 실적·공시가 나오면** — `collect X`(또는 리서치 보강) → `python3 council.py update X`.
  직전 판단의 KPI 적중, 반증 조건, 기본 시나리오 추정 대비 실제를 대조해 **유지 / 약화 / 훼손**을 판정한다(판정을 다시 내리지는 않는다).
  약화·훼손이면 재토론한다: `run X --cli … ` (바뀐 단계부터 다시 돈다). 재토론에서 역할은 직전 판단을 보고, 입장이 바뀌면 `change_reason`을 남긴다.
- **사람의 결정** — `python3 council.py decide X --size 0.02 --note "이유"`.
- **교정** — `python3 council.py calibrate`. 확률을 붙인 KPI 예측이 실제로 몇 % 맞았는지(Brier 점수·구간별 적중률),
  판정 종목 중 찬성 비율(거의 다 찬성이면 필터가 작동하지 않는다), 판정이 자주 뒤집힌 종목.

## 판정 규칙

**게이트** — 앞에서 걸리면 뒤를 돌리지 않는다: 근거 충분성 → 회계 품질(`red_flag`면 반대) → 모델(시나리오 계산 가능).

**레드라인** — 하나라도 어기면 '찬성'은 '반대'로 집계. 지표는 **코드 계산값이 페르소나가 쓴 값을 이긴다**(페르소나는 `case`로 가정만 고른다).

| 에이전트 | 레드라인 | 경고 |
|---|---|---|
| 앤더슨 | `upside_10y`(코드: case의 10년 주당가치 ÷ 주가) ≥ 5 | `revenue_5y`(코드) < 2 |
| 슬레이터 | `unit_economics` ≠ `deteriorating` · `survival_path` ≠ `false` · `cash_survives`(코드: case 현금 경로) ≠ `false` · `must_be_true` 작성 · `broken` 없음(코드가 사실로 대조) | `must_be_true`에 주가·목표가 |
| 애크먼 | `simple_predictable` · `fcf_positive`(코드) · `capital_markets_dependent` = `false`(순부채/EBITDA > 4 또는 FCF 음수·소진 3년 미만이면 코드가 `true`) · `mos`(코드) ≥ 20% | — |
| 클라만 | `mos`(코드: case 내재가치 대비) ≥ 30% · `downside`(코드: 성장이 틀릴 때 단단한 가치까지 하락) ≤ 50% · `leveraged`(코드) = `false` | `growth_premium`(주가 중 성장 몫) > 50% |

**조건부 찬성** — 페르소나는 `stance`를 `conditional`("이 가격 이하라면 찬성")로 쓸 수 있다. 조건 가격 `buy_below`는 가격에 걸린 레드라인
(앤더슨 10년 5배 · 애크먼 안전마진 20% · 클라만 안전마진 30%·하방 50%)을 모두 지키는 가장 높은 주가로 코드가 계산한다.
현재가에서 레드라인을 지키면 찬성, 더 낮은 조건 가격에서는 지키면 `CONDITIONAL_ABOVE`(기본 '보류'), 가격과 무관한 레드라인을 어기면 반대로 집계한다.
보고서의 **조건부 판정**은 가치는 그대로 두고 가격에 걸린 지표만 다시 계산해(`calc.reprice`), 주가가 각 조건 가격까지 내려왔을 때의 표결을 보여 준다.
주가를 예측하지 않는다. `update`는 새 주가가 직전 판단의 조건 가격에 닿으면 알린다(종료 코드 1).

**검증** — 주장마다: 인용 없음 · 없는 근거 · 기준일 이후 근거 · **출처 없는 숫자**(코드가 숫자를 하나씩 대조해 근거·계산값 어디에도 없는 숫자,
퍼센트와 금액을 구분) · 검증자의 `unsupported`·`contradicted`는 실패. 한 페르소나의 논거 절반 이상이 실패하면 그 표는 '보류'로 집계.
`leap`과 '다른 근거에 있는데 인용하지 않은 숫자'는 경고.

**조건 판정** — 반증 조건·참이어야 하는 것(`metric`·`op`·`value`)은 실제 값이 문턱의 ±0.5%(`NEAR`) 안이면 문턱을 넘지 않은 것으로 본다
(최신 실제치를 문턱으로 쓴 조건의 반올림 오경보 방지). `period` 없이 메모에 아직 발표되지 않은 기간('FY2026Q3…', '3분기…')을 적은 반증 조건은
직전 분기 값으로 판정하지 않고 '대기'로 둔다. 컨센서스는 같은 지표·기간이면 가장 최근 것만 쓰고, 회사 가이던스 하단보다 낮거나 최근 실적 발표 전
날짜이거나, 연간 값이 같은 해 분기 합(실적 + 분기 컨센서스)보다 낮으면 '낡은 컨센서스'로 제외한다. 주식 수는 기간 가중평균 희석 주식 수와 현재 주식 수 중 큰 쪽, 순현금에는 단기·장기 투자자산을 넣는다.

**경고** — 2라운드 반론 누락(다른 페르소나 + 레드팀) · 기계 판정 가능한 반증 조건 없음 · 이미 충족된 반증 조건 · 회계 신호 미해명 ·
회사 발표만으로 '입증'한 해자 · 컨센서스와 같은 모델(variant 없음) · 기저율상 드문 기본 시나리오 · 낡은 입력(`basis`) · `filing`·`call` 근거 부재.

**표결** — 찬성 +1 · 반대 −1 · 보류 0, 가중치는 `WEIGHTS`(기본 네 명 동일 — 2:2면 팽팽). 합이 양수면 찬성 우세(종료 코드 0), 아니면 1.
확신 가중 점수 Σ 가중치 × 표 × 확신/5 (−1~+1)와 비중 참고값(요구수익률 초과분의 1/4 켈리, 상한 10%)은 판정을 바꾸지 않는다.
2라운드 값은 1라운드 값을 덮어쓴다(`metrics`·`case`는 필드 단위).

## 파일 구조

```
research/<TICKER>/
  evidence.json        # {ticker, name, as_of, researched, sources: [{id, type, title, url, date, retrieved, note}],
                       #  facts: [{id, metric, value, unit, period, end, basis, source, origin}], gaps}
  business.json  management.json  forensic.json      # L4 — 스키마는 agents/<module>.md
  model.json           # 드라이버·시나리오(bear·base·bull)·variant·kpis — agents/modeler.md
  <agent>.1.json  <agent>.2.json  redteam.json        # L5 — agents/debate.md, agents/redteam.md
  verifier.json        # L6 — agents/verifier.md
  view.json            # (선택) 사용자 견해 — 어떤 프롬프트에도 들어가지 않는다
  report.md            # judge가 쓰는 보고서
  journal.jsonl        # 판단 로그 (judgment · update · decision), 지우지 않는다
  analysis.json        # calc가 쓰는 계산값 (캐시)
```

근거 `type`은 `filing` · `call` · `conference` · `news` · `data`. 사실 `basis`는 `reported` · `guidance` · `consensus` · `market`.
인용 ID는 근거 `S1`, 사실 `F12`, 계산값 `C:fcf_margin@FY2025`. 예시: [examples/NOVA](examples/NOVA) (가상 기업).

## 명령

```sh
python3 council.py collect  <TICKER> [--name 회사명] [--lang en|ko] [--as-of YYYY-MM-DD]
python3 council.py merge    <TICKER> <보강.json>
python3 council.py calc     <TICKER> [--case '{"ackman": {"from": "bear"}}'] [--json]
python3 council.py prompt   <researcher|business|management|forensic|modeler|anderson|slater|ackman|klarman|redteam|verifier> <TICKER> [--round 1|2]
python3 council.py run      <TICKER> --cli "<명령>" [--force] [--json]
python3 council.py judge    <TICKER|폴더> [--json] [--no-log]
python3 council.py update   <TICKER> [--json]
python3 council.py decide   <TICKER> --size 0.02 [--note 이유]
python3 council.py calibrate [폴더 …] [--json]
python3 council.py repro    <TICKER> --cli "<명령>" [--runs 2]     # 재현성: 같은 근거로 N번 → 결론·숫자 편차
python3 council.py audit    <TICKER> --cli "<명령>" [--n 5]        # 오류 주입: 틀린 숫자를 검증이 잡는가
python3 council.py baserate [--from 2010] [--to 2024]             # SEC XBRL로 매출 성장 기저율 표
python3 -m unittest -q
```

종료 코드는 0 찬성 우세·유지·통과 · 1 반대 우세·팽팽·판정 불가·약화·훼손·불통과(collect는 수집 실패) · 2 입력·실행 오류.
결과를 파싱할 때는 `--json`. Windows에서는 `python3` 대신 `py`.

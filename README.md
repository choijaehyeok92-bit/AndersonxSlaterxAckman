# Anderson × Slater × Ackman — 리서치 하네스

> 같은 사실, 코드가 한 계산, 세 개의 철학, 독립 검증, 그리고 기록.

전문 애널리스트와 LLM 분석의 차이는 지능보다 **규율**에 있다. 숫자를 어디서 가져왔는지, 계산을 누가 했는지,
컨센서스와 무엇이 다른지, 틀렸을 때 알 수 있는지. 이 하네스는 "더 똑똑한 프롬프트"가 아니라 그 규율을 **구조로 강제하는 장치**다.

제임스 앤더슨(멱법칙·10년 5배), 톰 슬레이터(무엇이 참이어야 하는가·단위경제), 빌 애크먼(단순·예측 가능·FCF·안전마진)이
토론하는 판단층(L5)은 그대로 두고, 그 아래에 증거·사실·계산·분석 층을, 위에 검증·기록 층을 붙였다.
표준 라이브러리만 쓰는 [council.py](council.py) + [harness/](harness) (Python 3.8+).

```
 L1 수집  collect: SEC 공시·XBRL 재무 · DART 재무 · 뉴스      researcher: 어닝콜·컨퍼런스·컨센서스·가이던스·주가
            └──────────────────────────→ evidence.json ←─────────────────────────────┘
 L2 사실    값·단위·기간·출처만. 출처 없는 숫자·단위 오류(31%→31)·기준일 이후 자료는 코드가 버린다
                                   │
 L3 계산    재무 비율·TTM·역DCF(시장이 가정한 성장)·기저율  ← 코드
                                   │                                     ┌ 게이트 0: 근거 충분성
 L4 분석    business ─┐  management ─┤  forensic ─┐  서로 모른다         │
                                   │             └ 게이트 1: 회계 품질 red_flag면 여기서 '반대'
 L3 모델    modeler: 드라이버·시나리오 가정 → 코드: 시나리오 가치·수익률 분해·민감도·컨센서스 대비
                                   │
 L5 판단    anderson.1  slater.1  ackman.1   redteam(사전 부검, 결론을 모른다)
            anderson.2  slater.2  ackman.2   ← 두 상대 + 레드팀에게 반론
                                   │
 L6 검증    코드: 인용·숫자 대조   verifier: 작성자·입장을 가린 독립 검증
                                   │
            judge: 게이트 · 레드라인(코드 계산 지표) · 검증 실패 → 보류 · 가중 표결 → report.md
 L7 기록    journal.jsonl: 판단 · update(유지/약화/훼손) · decide(사람의 비중) · calibrate(Brier)
```

## 산출물 — 에세이가 아니라 여섯 가지

`report.md` 맨 앞은 항상 같은 형태다. 형태가 고정돼야 종목끼리 비교하고 사후에 검증할 수 있다.

1. **Variant perception** — 시장이 가격에 넣은 것(역DCF의 내재 성장, 컨센서스), 우리가 다르게 보는 점, 왜, 촉매, 시점
2. **시나리오 분포와 기대수익률** — bear/base/bull 확률, 주당 가치·내재가치, 5년 연 수익률을 매출 성장·마진·멀티플·주식 수·현금으로 분해, 민감도
3. **반증 조건** — 페르소나와 레드팀이 쓴, 코드가 분기마다 대조하는 조건
4. **모니터링 KPI** — 확률을 붙인 예측. 쌓이면 교정의 재료가 된다
5. **확신도와 비중 참고값** — 확신 가중 점수, 요구수익률 초과분의 1/4 켈리. **최종 비중은 사람이 정한다**
6. 그 아래 표결·페르소나 논거·분석 모듈·레드팀·검증 결과·계산 근거·출처 전부

## LLM의 실패 모드와 하네스의 대응

| 실패 모드 | 증상 | 대응 |
|---|---|---|
| 낡은·지어낸 숫자 | 학습 시점 데이터, 그럴듯한 수치 | 사실은 출처 ID 필수. 주장 속 숫자를 **코드가 하나씩 대조** — 근거·계산값 어디에도 없으면 그 논거는 실패, 인용만 빠졌으면 고칠 ID를 알려 준다 |
| 산술 오류 | 서술 속 계산 실수 | 가치·배수·안전마진은 코드가 계산. 페르소나는 `case`로 가정만 고르고, 직접 쓴 숫자는 계산값에 진다 |
| 컨센서스 회귀 | 시장 통념을 세련되게 반복 | 역DCF + 컨센서스 대비표. 모델이 컨센서스와 같으면 경고 |
| 서사 과적합 | 좋은 이야기 → 높은 성장 가정 | SEC XBRL로 계산한 기저율과 대조. 기본 시나리오가 드문 성장이면 경고 |
| 사용자 아첨 | 사용자가 믿는 논리를 강화 | 사용자 견해(`view.json`)는 어떤 프롬프트에도 안 들어간다. 판정 후 보고서에서만 대조 |
| 회계 단위 오류 | ADR 비율, 회계연도, 희석 주식 수, 통화 | ADR 비율·환율 사실 없으면 계산 거부, 비율 단위 검사, XBRL 회계연도 라벨, 희석 주식 수 사용 |
| 페르소나 연극 | 근거 없는 확신에 찬 서술 | 페르소나는 L1~L4 위에서만 판단, 레드라인은 코드 계산 지표로 집행 |
| 자기 채점 | 형식적 통과 | 맥락·작성자·입장을 가린 독립 검증자 + 기계 대조 |
| 회계 품질 무시 | 성장주에서 SBC·Non-GAAP·이익-현금 괴리 간과 | 코드가 회계 신호를 계산하고 forensic이 하나씩 해명. `red_flag`면 밸류에이션 전에 멈춘다 |
| 판단의 역류 | 결론에 맞춰 숫자 조정 | 사실 → 모델 → 판단 단방향. 수집 사실은 리서처도 못 바꾸고, 입력이 바뀌면 뒤 단계가 낡았다고 표시(`basis`) |

## 사용법

AI CLI 안에서는 그냥 말하면 된다 — "UBER 분석해줘". 에이전트는 [AGENTS.md](AGENTS.md)의 절차를 따른다.

터미널에서 한 번에 돌리려면 프롬프트를 stdin으로 받는 CLI 아무거나 `--cli`에 넣는다.
역할마다 별도 프로세스로 돌아 서로의 맥락이 섞이지 않고, 같은 단계의 역할은 병렬로 실행된다.

```sh
export SEC_USER_AGENT="이름 이메일"          # SEC는 연락처가 담긴 User-Agent를 요구한다
export DART_API_KEY=...                       # 한국 종목 (opendart.fss.or.kr에서 무료 발급)
python3 council.py run UBER --name "Uber Technologies" --cli "claude -p --allowedTools WebSearch,WebFetch"
python3 council.py run 000660 --name "SK하이닉스" --lang ko --cli "gemini"
```

단계별로 직접 돌릴 수도 있다.

```sh
python3 council.py collect UBER --name "Uber Technologies"   # 공시·XBRL 재무·뉴스 → research/UBER/evidence.json
python3 council.py prompt researcher UBER                     # 리서치 프롬프트 (웹 검색 가능한 CLI에 넣는다)
python3 council.py merge UBER additions.json                  # 리서처 보강분 병합 (형식 검증, 수집 사실 보호)
python3 council.py calc UBER                                  # 코드 계산값 확인 — 비어 있는 것도 알려 준다
python3 council.py prompt forensic UBER | codex exec -        # 어떤 CLI에도 파이프
python3 council.py judge UBER                                 # 판정 + research/UBER/report.md + 판단 로그
python3 council.py judge examples/NOVA --no-log               # 가상 예시
python3 -m unittest -q
```

실적이 나온 뒤에는:

```sh
python3 council.py collect UBER && python3 council.py update UBER   # KPI 적중·반증 조건·추정 대비 실제 → 유지/약화/훼손
python3 council.py decide UBER --size 0.02 --note "작게 시작"        # 사람의 결정을 기록
python3 council.py calibrate                                        # 모든 종목의 예측 교정, 찬성 비율
```

## 하네스 자체를 시험하기

| 시험 | 명령 | 무엇을 보나 |
|---|---|---|
| 재현성 | `repro X --cli … --runs 2` | 같은 근거·같은 기준일로 두 번 돌려 판정·표·내재가치·기대수익률의 편차. 크면 판단이 아니라 소음이다 |
| 오류 주입 | `audit X --cli … --n 5` | 주장 속 숫자를 일부러 틀리게 바꿔 독립 검증자와 기계 대조가 잡는 비율, 기존 검증에서 통과했던 주장을 새로 지적하는 오탐 |
| 과거 시점 | `collect X --as-of 2024-03-31` → `run` | 그날까지 제출된 공시·XBRL만 쓰고, 기준일 이후 자료는 사실층이 버린다. 결과를 실제와 비교 (LLM이 결과를 학습했을 수 있으니 덜 알려진 종목으로) |
| 반대 결론 비율 | `calibrate` | 판정 종목 대부분이 찬성이면 필터가 작동하지 않는다는 신호 |

## CLI별 진입점

| CLI | 대화형 진입 파일 | 헤드리스 `--cli` 예 |
|---|---|---|
| Claude Code | `CLAUDE.md` → `@AGENTS.md` | `claude -p --allowedTools WebSearch,WebFetch` |
| Codex CLI | `AGENTS.md` | `codex exec -` |
| Gemini CLI | `GEMINI.md` → `@AGENTS.md` | `gemini` |
| Cursor · Copilot · OpenCode 등 | `AGENTS.md` | `prompt` 출력을 붙여넣기 |

헤드리스 플래그는 CLI 버전마다 다르다. 웹 검색은 리서치 단계에만 필요하므로, CLI에서 웹 검색 허용 옵션을 켜거나 `prompt researcher`만 대화형으로 돌리면 된다.

## 바꾸고 싶다면

| 무엇 | 어디 |
|---|---|
| 페르소나의 철학·질문·말투 | `agents/<agent>.md` |
| 레드라인·게이트·회계 신호 문턱·할인율·검증 실패 기준·비중 상한 | `harness/rules.py` (+ 해당 `agents/*.md` 절) |
| 표결 가중치 (예: 앤더슨 60 · 슬레이터 40 · 애크먼 0) | `harness/rules.py`의 `WEIGHTS` |
| 분석 모듈·모델러·레드팀·검증자의 질문과 스키마 | `agents/<role>.md` |
| 수집 태그 (XBRL·DART 계정 매핑) | `harness/collect.py`의 `XBRL` · `DART_ACCOUNTS` |
| 기저율 표 | `python3 council.py baserate`로 생성 — 형식은 [data/README.md](data/README.md) |
| 에이전트 추가 | `agents/<name>.md` + `harness/core.py`의 `AGENTS` + `harness/rules.py`의 `WEIGHTS` · `RED_LINES` + `harness/calc.py`의 `DEFAULT_CASE` |

앤더슨·슬레이터 `metrics`의 필드명(`upside_10y` · `revenue_5y` · `unit_economics` · `survival_path` · `must_be_true`)은
[AndersonxSlater](https://github.com/choijaehyeok92-bit/AndersonxSlater) 60/40 하네스의 스키마와 같다. 이제 `upside_10y`·`revenue_5y`는 코드가 계산한다.

## 한계

- 무료 1차 자료만 쓴다. 미국은 SEC, 한국은 DART가 재무를 채우고, 주가·컨센서스·어닝콜은 리서처(웹 검색)가 출처와 함께 넣는다. 다른 시장은 리서처가 재무까지 채운다.
- 모델은 드라이버 → 매출 → FCF 마진 → 현금·주식 수 → 출구 배수의 단순 연결 모델이다. 손익·재무상태·현금흐름 3표를 항목별로 연결하지는 않는다.
- 숫자 대조는 단위·배수가 붙은 숫자(%·배·달러·억·개월 …)만 본다. 단위 없는 숫자와 의미(어느 지표의 숫자인지)는 독립 검증자가 맡는다.
- SEC XBRL 기저율은 두 시점 모두 공시한 기업만 남는 생존 편향이 있다(보고서에 표시). 명목 달러, 인수·매각 미조정.
- 교정은 판단 로그가 1~2년 쌓여야 의미가 있다.

투자 자문이 아닌 의사결정 보조 도구다. 페르소나는 공개된 발언과 운용 방식을 바탕으로 한 해석이며, 본인의 견해가 아니다.

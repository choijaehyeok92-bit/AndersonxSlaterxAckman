# AGENTS.md — Anderson × Slater × Ackman 투자 토론 하네스

모든 AI CLI(Claude Code · Codex CLI · Gemini CLI · Cursor · Copilot · OpenCode 등)에 공통으로 적용하는 지침이다.
세 투자자 에이전트가 같은 근거(`evidence.json`)를 놓고 종목 찬반을 토론한다. 판정은 [council.py](council.py)가 내린다.

| 파일 | 내용 |
|---|---|
| [agents/anderson.md](agents/anderson.md) | 제임스 앤더슨 — 멱법칙, LTGG 10가지 질문, 10년 5배 |
| [agents/slater.md](agents/slater.md) | 톰 슬레이터 — 무엇이 참이어야 하는가, 단위경제, 작게 시작해 키우기 |
| [agents/ackman.md](agents/ackman.md) | 빌 애크먼 — 단순·예측 가능·FCF, 안전마진, 촉매 |
| [agents/debate.md](agents/debate.md) | 공통 토론 규칙과 1·2라운드 JSON 스키마 |
| [agents/researcher.md](agents/researcher.md) | 근거 수집 규칙과 페르소나별 체크리스트 |

## 역할
너는 토론 진행자다. 근거를 모으고, 세 페르소나를 서로 독립적으로 연기시키고, 판정을 그대로 보고한다.

> 프롬프트가 `<!-- council role=… -->`로 시작하면 너는 진행자가 아니라 그 역할이다. 워크플로를 돌리지 말고 그 역할의 JSON만 답한다.

- 페르소나의 논리를 섞지 않는다. 1라운드에서는 다른 페르소나의 의견을 보지 않는다.
- 모든 논거는 `evidence.json`의 출처 ID를 인용한다. 없는 숫자를 만들지 않고 추정은 추정이라고 밝힌다.
- 하네스 판정(레드라인 위반 → 반대 집계, 표결 결과)을 말로 뒤집거나 지표를 고쳐 통과시키지 않는다.
  규칙은 사용자가 `agents/*.md`의 레드라인을 바꿀 때만 `council.py` 상단 상수와 함께 바꾼다.
- 매크로·금리·단기 주가를 예측하지 않는다. 이 하네스는 투자 자문이 아니라 의사결정 보조다.

## 워크플로 — "X 토론해줘" · "X 분석해줘"

1. **수집** — `python3 council.py collect X [--name 회사명] [--lang ko]`
   SEC 공시 목록과 최근 뉴스를 `research/X/evidence.json`에 넣는다. 비미국 종목이거나 네트워크가 막혀 실패해도 2단계로 넘어간다.
2. **리서치** — `python3 council.py prompt researcher X`의 지시대로 웹 검색으로 어닝콜·컨퍼런스·공시 원문 수치를 확인해 `evidence.json`을 보강하고 `"researched": "YYYY-MM-DD"`를 적는다.
3. **1라운드 (독립 의견)** — 에이전트마다 `python3 council.py prompt <agent> X --round 1`의 출력을 그대로 프롬프트로 써서 `research/X/<agent>.1.json`을 만든다.
   - 서브에이전트를 지원하는 CLI(Claude Code의 Agent 도구 등): 세 에이전트를 병렬 서브에이전트로 띄워 독립성을 지킨다.
   - 지원하지 않는 CLI: 순서대로 쓰되 앞서 쓴 다른 에이전트 파일을 다시 읽지 않는다. 완전한 독립이 필요하면 아래 `run`을 쓴다.
4. **2라운드 (반론)** — `prompt <agent> X --round 2` → `research/X/<agent>.2.json`
5. **판정** — `python3 council.py judge X`
   결과(판정·표결·레드라인·경고)를 그대로 보고하고, 각 에이전트의 핵심 논거와 "생각을 바꿀 조건"을 요약한다. 전문은 `research/X/debate.md`.

**헤드리스 일괄 실행** — `python3 council.py run X --cli "<명령>"`
수집 → 리서치 → 1라운드(병렬) → 2라운드(병렬) → 판정을 한 번에 돈다. 에이전트마다 별도 프로세스라 서로의 맥락이 섞이지 않는다.
`<명령>`은 프롬프트를 stdin으로 받아 답을 stdout으로 내는 CLI면 무엇이든 된다(예: `claude -p`). 끝난 단계는 건너뛰고, `--force`면 다시 한다.

**재토론** — 새 실적·공시가 나오면 1~2단계로 `evidence.json`을 갱신하고 라운드 파일을 지운 뒤(또는 `run --force`) 다시 판정한다.

## 판정 규칙 (council.py)

| 에이전트 | 레드라인 — 하나라도 어기면 '찬성'은 '반대'로 집계 | 경고 |
|---|---|---|
| 앤더슨 | `upside_10y` ≥ 5 | `revenue_5y` < 2 |
| 슬레이터 | `unit_economics` ≠ `deteriorating` · `survival_path` ≠ `false` · `must_be_true` 작성 · `broken` 없음 | `must_be_true`에 주가·목표가 |
| 애크먼 | `simple_predictable` · `fcf_positive` · `capital_markets_dependent` = `false` · 안전마진 ≥ 20% | — |
| 공통 | — | 인용 없는 주장 · 없는 출처 인용 · 2라운드에서 반론 누락 · `filing`·`call` 근거 부재 |

- 표결: 찬성 +1 · 반대 −1 · 보류 0, 에이전트 가중치는 `WEIGHTS`(기본 동일). 합이 양수면 찬성 우세(종료 코드 0), 아니면 1.
- 확신 가중 점수: Σ 가중치 × 표 × 확신/5 (−1~+1). 판정을 바꾸지 않는 참고 지표다.
- 2라운드 값은 1라운드 값을 덮어쓴다(`metrics`는 필드 단위). 입장 변화는 "1라운드 → 최종"으로 표시된다.

## 파일 구조

```
research/<TICKER>/
  evidence.json            # {"ticker", "name", "as_of", "researched", "sources": [{"id", "type", "title", "url", "date", "note"}], "gaps"}
  <agent>.1.json           # 1라운드 — 스키마는 agents/debate.md
  <agent>.2.json           # 2라운드
  debate.md                # judge가 쓰는 토론 전문
```

`type`은 `filing` · `call` · `conference` · `news` · `data`. 예시: [examples/NOVA](examples/NOVA) (가상 기업).

## 명령

```sh
python3 council.py collect <TICKER> [--name 회사명] [--lang en|ko]
python3 council.py prompt  <researcher|anderson|slater|ackman> <TICKER> [--round 1|2]
python3 council.py run     <TICKER> --cli "<명령>" [--force] [--json]
python3 council.py judge   <TICKER|폴더> [--json]
python3 -m unittest -q
```

종료 코드는 0 찬성 우세 · 1 반대 우세·팽팽(collect는 수집 실패) · 2 입력·실행 오류. 결과를 파싱할 때는 `--json`. Windows에서는 `python3` 대신 `py`.

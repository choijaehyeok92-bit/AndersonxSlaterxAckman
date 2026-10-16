# Anderson × Slater × Ackman — 투자 토론 하네스

> 같은 근거, 세 개의 철학, 두 번의 라운드, 규칙이 내리는 판정.

제임스 앤더슨(멱법칙·10년 5배), 톰 슬레이터(무엇이 참이어야 하는가·단위경제), 빌 애크먼(단순·예측 가능·FCF·안전마진)을
각각 에이전트로 세워 한 종목의 찬반을 토론시킨다. 공시·어닝콜·컨퍼런스·뉴스를 모아 공통 근거를 만들고,
에이전트는 그 근거만 인용해 독립 의견(1라운드)과 반론(2라운드)을 쓴다.
판정은 단일 파일 [council.py](council.py)(표준 라이브러리만 사용)가 내린다.

```
 collect (SEC EDGAR · Google News)    researcher (웹 검색: 어닝콜 · 컨퍼런스 · 공시 원문 수치)
            └──────────────────→ evidence.json ←──────────────────┘
                                      │  모두 같은 근거
        ┌─────────────────────────────┼─────────────────────────────┐
   anderson.1.json             slater.1.json                 ackman.1.json     1라운드: 서로 모른 채
   anderson.2.json             slater.2.json                 ackman.2.json     2라운드: 반박 · 인정 · 입장 수정
        └─────────────────────────────┼─────────────────────────────┘
                 judge: 인용 검증 · 레드라인 · 가중 표결 → debate.md
```

## 사용법

AI CLI 안에서는 그냥 말하면 된다 — "UBER 토론해줘". 에이전트는 [AGENTS.md](AGENTS.md)의 절차를 따른다.

터미널에서 한 번에 돌리려면 프롬프트를 stdin으로 받는 CLI 아무거나 `--cli`에 넣는다.
에이전트마다 별도 프로세스로 돌아 서로의 맥락이 섞이지 않고, 1·2라운드는 병렬로 실행된다.

```sh
python3 council.py run UBER --name "Uber Technologies" --cli "claude -p --allowedTools WebSearch,WebFetch"
python3 council.py run 000660 --name "SK하이닉스" --lang ko --cli "gemini"
```

단계별로 직접 돌릴 수도 있다.

```sh
python3 council.py collect UBER --name "Uber Technologies"   # 공시·뉴스 → research/UBER/evidence.json
python3 council.py prompt researcher UBER                     # 리서치 프롬프트 (웹 검색 가능한 CLI에 넣는다)
python3 council.py prompt ackman UBER --round 1 | codex exec - # 어떤 CLI에도 파이프
python3 council.py judge UBER                                 # 판정 + research/UBER/debate.md
python3 council.py judge examples/NOVA                        # 가상 예시
python3 -m unittest -q
```

## CLI별 진입점

| CLI | 대화형 진입 파일 | 헤드리스 `--cli` 예 |
|---|---|---|
| Claude Code | `CLAUDE.md` → `@AGENTS.md` | `claude -p --allowedTools WebSearch,WebFetch` |
| Codex CLI | `AGENTS.md` | `codex exec -` |
| Gemini CLI | `GEMINI.md` → `@AGENTS.md` | `gemini` |
| Cursor · Copilot · OpenCode 등 | `AGENTS.md` | `prompt` 출력을 붙여넣기 |

헤드리스 플래그는 CLI 버전마다 다르다(이 저장소에서는 `claude -p`로 전 과정을 검증했다). 웹 검색은 리서치 단계에만 필요하므로,
CLI에서 웹 검색 허용 옵션을 켜거나 `prompt researcher`만 대화형으로 돌리면 된다.
`collect`는 미국 상장사·ADR만 SEC 공시를 찾는다. 다른 시장은 뉴스만 모이고 나머지는 리서처가 채운다.
SEC는 연락처가 담긴 User-Agent를 요구하므로 `SEC_USER_AGENT="이름 이메일"`을 설정해 두는 것이 좋다.

## 바꾸고 싶다면

| 무엇 | 어디 |
|---|---|
| 페르소나의 철학·질문·말투 | `agents/<agent>.md` |
| 레드라인 (찬성을 막는 자기 원칙) | `agents/<agent>.md` 레드라인 절 + `council.py`의 `RED_LINES` · 상단 상수 |
| 표결 가중치 (예: 앤더슨 60 · 슬레이터 40 · 애크먼 0) | `council.py`의 `WEIGHTS` |
| 에이전트 추가 | `agents/<name>.md` + `AGENTS` · `WEIGHTS` · `RED_LINES`에 한 줄씩 |
| 토론 규칙·출력 스키마 | `agents/debate.md` |

앤더슨·슬레이터 `metrics`의 필드명(`upside_10y` · `revenue_5y` · `unit_economics` · `survival_path` · `must_be_true`)은
[AndersonxSlater](https://github.com/choijaehyeok92-bit/AndersonxSlater) 60/40 하네스의 스키마와 같다.

투자 자문이 아닌 의사결정 보조 도구다. 페르소나는 공개된 발언과 운용 방식을 바탕으로 한 해석이며, 본인의 견해가 아니다.

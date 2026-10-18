# 검증 지침 — 「포트폴리오 10종목 심층 리서치 — 4인 위원회」

너는 이 문서를 처음 보는 독립 검증자다. 문서를 쓴 사람이 아니므로 문장을 믿지 말고 숫자와 사실을 원천과 대조한다.
독자는 개인 투자자인 의장이며, 이 문서를 근거로 비중을 정한다. 틀린 숫자 하나가 판단을 바꿀 수 있다.

## 문서
- 컨테이너: `{"kind":"project","id":"fa80d1ae-25b3-4fa6-ad66-a2fb1c015c81"}`
- 탭 노드: 개요 6d14633f-424d · 포트폴리오 비중 30d777db-4efc · 종목별 심층 리서치(상위) c08774e7-e7e6 ·
  UBER c2b75b8d-efc6 · MELI e50098e2-6feb · CRDO 0897b56d-a4ab · NVDA a769f6cb-3260 · SHOP 862a541b-5eb9 ·
  AMZN 2fb740f8-54b2 · PLTR cc14fead-2ae7 · IOT aa9afc3e-14d5 · CBRS 5ee5f35d-bdac · PONY 4502ad49-7252
- 읽기: `mcp__Claude_Docs__read(ref={"object":"node","id":"<NODE>"}, container=…, engine="prose", payload={"kind":"view"})` — 잘리면 결과의 `next`로 이어 읽는다.
  찾기: `payload={"kind":"search","text":"…"}`. 각 종목 탭의 원고 사본은 `research/_deep/tabs4/<T>.md`(문서와 같아야 한다).
- 도구가 바로 안 보이면 ToolSearch로 `select:mcp__Claude_Docs__read,mcp__Claude_Docs__update`.

## 원천 (저장소 루트 /home/claude/choijaehyeok92-bit/andersonxslaterxackman)
1. **하네스 판정·숫자(최종)**: `research/_deep/v4/<T>.md` — 4인 판정·표·조건 가격·클라만 계산값·사다리·위원회 비중·네 위원 비중과 이유·위험·추가 계획.
   `research/_deep/v4/prefix/<T>.md`는 **버그 수정·비중 재실행 전의 옛 값**이다. 문서에 옛 값이 남아 있으면 오류다.
2. 하네스 보고서: `research/<T>/report.md` (시나리오·역DCF·수익률 분해·반증 조건·KPI·클라만 세 질문), 에이전트 파일 `research/<T>/<agent>.1.json`·`.2.json`, `model.json`, `evidence.json`.
   `view.json`은 열지 않는다.
3. 비중 라운드: `research/_portfolio/v4/committee.json`(위원회안·켈리·동일비중·위험 기여·묶음·추가 계획), `sizing.<agent>.json`(비중·이유·would_rather·trim_rules·conditional_adds), `risk.json`(변동성·상관).
   묶음: AI 하드웨어(NVDA·CRDO·CBRS) 15.0% · 자율주행(UBER·PONY) 14.5% · AI 자본조달(NVDA·CRDO·CBRS·AMZN) 23.0% · 커머스(MELI·SHOP) 14.5%. 위원회안 변동성 17.1%.
4. 리서치 노트: `/home/claude/research_notes/포트폴리오 9종목 심층 리서치/<T>.md` — 사업·실적·경쟁·재무 사실과 출처 URL.

## 확인할 것
- 하네스 숫자(판정·표·IV·기대수익·손실확률·켈리·조건 가격·단단한 가치·하락폭·사다리·비중·위험 기여·묶음·추가 계획)가 원천 1·3과 정확히 같은가. 반올림 표기 차이는 문제 삼지 않는다.
- 옛 값(prefix 시트, 또는 'PLTR·IOT 팽팽', 'SHOP 애크먼 반대', '위원회 비중 9.5%/4.5%/9.0%(NVDA)/7.0%(AMZN)/5.0%(PLTR)/3.0%(IOT)/1.5%(CBRS)/2.5%(PONY)' 같은 수정 전 숫자)가 남아 있지 않은가.
- 사업·실적 숫자가 노트·보고서·evidence와 맞는가(기간·단위·부호 포함). 원천에서 찾을 수 없는 숫자는 '출처 미확인'으로 보고한다.
- 섹션끼리, 그리고 개요·비중 탭과 종목 탭끼리 서로 모순되지 않는가.
- 렌더링: 화면에 `**`·`\$`·`$…$` 수식이 그대로 보이거나 표가 깨진 곳이 없는가(검색 `**`, `\\$`).
- 매수·매도 권유, 의장 대신 비중을 정하는 문장이 없는가.

## 고치는 법
- **명백한 오류만 직접 고친다**: 원천과 다른 숫자, 옛 값, 렌더링 깨짐, 오타. 판정·해석·논지는 고치지 않는다.
- 문장 일부 교체: `mcp__Claude_Docs__update(ref={"object":"node","id":"<NODE>"}, container=…, engine="prose", payload={"ops":[{"op":"replace","target":{"kind":"find","text":"<문서에 보이는 그대로의 옛 문구>"},"with":{"text":"<새 문구>"}}]})`.
  `text`는 화면에 보이는 글자 그대로다(마크다운 기호 없음, `$`는 그냥 `$`). 여러 곳에 걸리면 `"nth": k`를 붙이거나 더 긴 문구로 잡는다. `pattern`은 정규식이다.
- 종목 탭을 고쳤으면 `research/_deep/tabs4/<T>.md`의 같은 곳도 고친다(그 파일에서는 `$`가 `\$`로 적혀 있다).
- 판단이 필요한 것(원천끼리 다름, 해석 문제, 확인 불가)은 고치지 말고 보고한다.

## 마지막 답변 (진행자에게, 20줄 이내)
- 고친 것: `탭 — 옛 → 새 (원천)` 한 줄씩
- 고치지 않고 남긴 문제: 무엇이 왜 문제인지와 근거
- 전체 평가 한 줄

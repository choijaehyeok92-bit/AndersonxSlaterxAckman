# 근거 보강 지침 — 심층 리서치 → 하네스 evidence 병합

목표: 심층 리서치 노트에서 확인된 사실과 사건을 하네스의 `research/<T>/evidence.json`에 넣는다. 그래야 다음 하네스 실행에서 모든 역할이 그 근거 위에서 다시 판단한다. 너는 **보강분 JSON만** 만들고, 병합은 코드(`council.py merge`)가 한다. 기존 사실은 바꾸거나 지울 수 없다.

## 순서
1. `agents/researcher.md`를 읽는다. 출력 형식과 사실·근거 규칙이 거기에 있다. 저장소 루트는 `/home/claude/choijaehyeok92-bit/andersonxslaterxackman`이다.
2. `research/<T>/evidence.json`을 읽는다. 기존 근거(URL)와 사실(metric·period·value), 그리고 **기간 라벨 관례**를 확인한다. 회계연도 라벨은 그 회사의 기존 사실과 똑같이 쓴다. 예를 들어 NVDA는 2026년 7월 말에 끝난 분기를 `FY2027Q2`로 쓴다.
3. 노트 `research/_deep/notes/<T>.md`에서 보강할 것을 고른다.
   - **수치 사실**: 노트에 1차 또는 2차 출처 URL과 날짜가 있는 것만 넣는다. 기존 evidence에 같은 metric·period·값이 있으면 넣지 않는다.
     - metric은 snake_case로 쓴다. 기존 사실에 같은 의미의 metric 이름이 있으면 그 이름을 쓴다.
     - unit은 `USD`, `USD/share`, `shares`, `ratio`(31%는 0.31), `count`, `months`, `x` 중 하나다.
     - basis는 reported, guidance(`low`·`high` 범위 포함), consensus, market 중 하나다.
     - end는 기간 종료일이다. market basis는 관측일을 쓴다.
     - 기준일 2026-10-18 이후의 자료는 넣지 않는다.
   - **사건·질적 근거**: 숫자로 담을 수 없는 것(제휴 종료 통보, 수수료 부과, 정책 변경, 규제, 경쟁사 발표, 인수 등)은 `sources` 항목으로 넣는다. 항목의 `note`에 핵심 내용과 날짜를 한국어로 구체적으로 적는다. 역할들은 근거 목록의 title·date·note를 읽는다.
   - 노트가 2차 자료나 추정으로 표시한 것은 source `note`에 "2차"라고 밝힌다. 노트가 "내 계산"이나 "추론"으로 표시한 숫자는 사실로 넣지 않는다.
4. 보강분을 `research/_deep/supp/<T>.json`에 쓴다. 형식은 `{"sources": [...], "facts": [...], "gaps": [...]}`이다. source id는 임시로 `S900`부터 쓴다. 병합할 때 코드가 번호를 다시 매긴다.
5. 병합한다: `cd /home/claude/choijaehyeok92-bit/andersonxslaterxackman && python3 council.py merge <T> research/_deep/supp/<T>.json`. 결과의 `rejected`가 비어 있지 않으면 그 사실을 고쳐 다시 병합한다. 이미 들어간 사실은 중복으로 건너뛴다.
6. 확인한다: `python3 council.py calc <T>`가 오류 없이 도는지 본다. 경고 목록에 무엇이 새로 생겼는지도 본다.

## 하지 말 것
- `view.json`을 열지 않는다.
- `council.py run`이나 `judge`를 돌리지 않는다. 재실행은 진행자가 한다.
- evidence.json을 손으로 고치지 않는다.
- 노트에 없는 숫자를 넣지 않는다. 결론에 맞추려고 사실을 고르지 않는다. 강세 근거와 약세 근거를 똑같이 넣는다.

## 마지막 답변 (진행자에게, 8줄 이내)
- 추가된 근거 수와 사실 수, 거부된 사실(있으면 이유)
- 핵심 보강 항목 목록 (한 줄씩)
- `calc` 경고 중 새로 생기거나 사라진 것

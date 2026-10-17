# 9종목 심층 리서치 (2026-10-18)

- `notes/<TICKER>.md` — 웹 리서치 노트 (출처·날짜 포함, 하네스 주장 대조)
- `tabs/<TICKER>.md` — Claude Docs 문서 종목 탭의 초고. 독립 사실 검증 후 문서에서 고친 소수 문구는 반영되지 않았다 — 최종본은 문서다.
- `writer_guide.md` — 탭 작성 지침

문서: https://claude.ai/code/artifact/3f67e9d9-50e4-43b4-81a2-be7cfb4cb010

리서치가 찾은 하네스 개선점(아직 코드에 반영하지 않음):
1. 문턱값을 최신 실제치에 맞추면 오경보 (UBER 주식 수 0.01%, IOT 이연매출 반올림) — 허용 오차·추세 조건 필요
2. 미발표 분기의 반증 조건을 직전 분기 값으로 판정 (AMZN·SHOP·UBER) — 값이 없으면 '대기'
3. 낡은 컨센서스가 차별적 시각을 만든다 (SHOP·IOT·AMZN) — 컨센서스 기준일 경고
4. 입력 오류: IOT 순현금(투자자산 누락), CBRS 주식 수(IPO 분기 가중평균 희석주식 사용)·주가, UBER Waymo 통보·SHOP ChatGPT 사건 미수집

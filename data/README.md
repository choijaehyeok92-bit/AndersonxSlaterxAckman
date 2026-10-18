# data/ — 기저율 표

`base_rates.json`은 `python3 council.py baserate [--from 2010] [--to 2024]`가 SEC XBRL frames API로 만든다
(미국 상장사 매출 태그의 연간 프레임, 시작 연도와 h년 뒤에 모두 매출을 공시한 기업의 연평균 성장률).
네트워크가 필요하고, `SEC_USER_AGENT="이름 이메일"`을 설정해 두는 것이 좋다. 파일이 없으면 보고서에 "기저율 표 없음"이 뜨고 판정은 그대로 진행된다.

다른 출처(예: Mauboussin·Callahan, *The Base Rate Book*, Credit Suisse 2016)의 표를 쓰려면 같은 형식으로 직접 만들고 `source`에 출처를 적는다.
숫자는 원문에서 옮기고 지어내지 않는다.

```json
{
  "source": "출처",
  "generated": "YYYY-MM-DD",
  "caveats": ["생존 편향 등 해석상 주의"],
  "horizons": {
    "5":  {"buckets": [{"label": "매출 5억 달러 미만", "min": 0, "max": 500000000, "n": 1234, "median": 0.06,
                        "share_at_least": {"0.10": 0.31, "0.20": 0.12, "0.30": 0.05}}],
           "all": {"label": "전체", "min": 0, "max": null, "n": 5000, "share_at_least": {"0.10": 0.25, "0.20": 0.08}}},
    "10": {"buckets": [], "all": {"label": "전체", "min": 0, "max": null, "n": 3000, "share_at_least": {"0.10": 0.15}}}
  }
}
```

- `share_at_least`: 연평균 매출 성장률이 키(소수) **이상**인 기업의 비율. 사이 값은 선형 보간하고, 표의 끝보다 높은 성장은 '최대 X%'로 표시한다.
- `min`·`max`: 시작 연도 매출(달러) 구간. 재무 통화가 달러가 아니면 `fx` 사실(예: 단위 `KRW/USD`)로 환산하고, 없으면 `all`을 쓴다.

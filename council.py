#!/usr/bin/env python3
"""Anderson×Slater×Ackman 투자 토론 하네스 — 세 투자자 에이전트가 같은 근거로 종목 찬반을 논한다.

  python3 council.py collect <TICKER> [--name 회사명] [--lang en|ko]  # SEC 공시·뉴스 → research/<TICKER>/evidence.json
  python3 council.py prompt  <role> <TICKER> [--round 1|2]           # 어떤 CLI·서브에이전트에도 넣을 프롬프트
  python3 council.py run     <TICKER> --cli "<명령>" [--force]        # 수집→리서치→1·2라운드→판정 일괄 실행
  python3 council.py judge   <TICKER> [--json]                        # 인용·레드라인 검증, 표결, debate.md 작성

<TICKER> 자리에는 폴더 경로도 쓸 수 있다. 표준 라이브러리만 사용(Python 3.8+).
종료 코드: 0 찬성 우세 · 1 반대 우세·팽팽(collect는 수집 실패) · 2 입력·실행 오류.
"""
import argparse, json, os, re, subprocess, sys, xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
AGENTS = {"anderson": "앤더슨", "slater": "슬레이터", "ackman": "애크먼"}
WEIGHTS = {"anderson": 1, "slater": 1, "ackman": 1}        # 표결 가중치
UPSIDE, REVENUE_5Y, MOS = 5.0, 2.0, 0.20                   # anderson.md LTGG Q10·Q1, ackman.md 안전마진
STANCE = {"for": ("찬성", 1), "against": ("반대", -1), "abstain": ("보류", 0)}
TYPES = ("filing", "call", "conference", "news", "data")
FORMS = {"10-K", "10-Q", "8-K", "20-F", "6-K", "40-F", "DEF 14A", "S-1", "F-1"}
ITEMS = {"1.01": "중요 계약", "2.01": "인수·매각", "2.02": "실적 발표", "5.02": "경영진 변동",
         "7.01": "IR·컨퍼런스 자료", "8.01": "기타 중요 사항"}
FILING_DAYS, NEWS_DAYS, MAX_FILINGS, MAX_NEWS, TIMEOUT = 400, 90, 30, 20, 1800
NEWS_LANG = {"en": "hl=en-US&gl=US&ceid=US:en", "ko": "hl=ko&gl=KR&ceid=KR:ko"}
UA = os.environ.get("SEC_USER_AGENT", "AndersonxSlaterxAckman research admin@example.com")  # SEC: '이름 이메일'
PRICE = re.compile(r"주가|목표\s*주?가|share price|stock price|price target|target price", re.I)


def mos(m):  # 애크먼 안전마진 = 1 - 주가/내재가치
    iv, p = m.get("intrinsic_value") or 0, m.get("price")
    return 1 - p / iv if iv > 0 and p is not None else None


RED_LINES = {  # '찬성'하려면 자기 원칙을 통과해야 한다 — agents/<agent>.md '레드라인'과 같아야 한다
    "anderson": [(lambda m: m.get("upside_10y", 0) >= UPSIDE, f"10년 상방 {UPSIDE:g}배 미만 (LTGG Q10)")],
    "slater": [(lambda m: m.get("unit_economics") != "deteriorating", "단위경제 악화 — CAC 상승·이탈률 악화"),
               (lambda m: m.get("survival_path") is not False, "외부 자본 없이 생존할 경로가 없음"),
               (lambda m: bool(m.get("must_be_true")), "참이어야 하는 것(must_be_true) 미작성"),
               (lambda m: all(x.get("status") != "broken" for x in m.get("must_be_true", [])), "이미 반증된 가설")],
    "ackman": [(lambda m: m.get("simple_predictable") is True, "단순·예측 가능한 사업이 아님"),
               (lambda m: m.get("fcf_positive") is True, "잉여현금흐름을 만들지 못함"),
               (lambda m: m.get("capital_markets_dependent") is False, "레버리지·자본시장 의존"),
               (lambda m: (mos(m) or -1) >= MOS, f"안전마진 {MOS:.0%} 미만 또는 계산 불가(intrinsic_value·price)")],
}


def soft(a, m):  # 경고만 하는 원칙
    if a == "anderson" and m.get("revenue_5y", 0) < REVENUE_5Y:
        return [f"5년 매출 {m.get('revenue_5y', 0)}배 < {REVENUE_5Y:g}배 (LTGG Q1)"]
    if a == "slater":  # 점검 항목은 가격이 아니라 운영 지표
        return [f"가격 기반 검증 항목 — 운영 지표로 교체: {x.get('claim')}"
                for x in m.get("must_be_true", []) if PRICE.search(x.get("claim", ""))]
    return []


def load(p, default=None):
    if default is not None and not Path(p).exists():
        return default
    return json.loads(Path(p).read_text(encoding="utf-8"))


def save(p, data):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def folder(t):
    return Path(t) if Path(t).is_dir() else ROOT / "research" / t.upper()


# ── 수집: 누구나 쓸 수 있는 무료 1차 자료만. 어닝콜·컨퍼런스는 리서처(웹 검색)가 보강한다 ──

def fetch(url):
    with urlopen(Request(url, headers={"User-Agent": UA}), timeout=30) as r:
        return r.read()


def sec(ticker):  # SEC EDGAR 최근 공시 (미국 상장사·ADR)
    tickers = json.loads(fetch("https://www.sec.gov/files/company_tickers.json")).values()
    cik = next((v["cik_str"] for v in tickers if v["ticker"] == ticker.upper().replace(".", "-")), None)
    if cik is None:
        return []
    r = json.loads(fetch(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))["filings"]["recent"]
    since = (date.today() - timedelta(FILING_DAYS)).isoformat()
    return [dict(type="filing", title=" ".join([f, *(ITEMS[i] for i in items.split(",") if i in ITEMS)]), date=d,
                 url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}")
            for f, d, acc, doc, items in zip(r["form"], r["filingDate"], r["accessionNumber"],
                                             r["primaryDocument"], r["items"]) if f in FORMS and d >= since][:MAX_FILINGS]


def news(query, lang):  # Google News RSS
    xml = fetch(f"https://news.google.com/rss/search?q={quote(f'{query} when:{NEWS_DAYS}d')}&{NEWS_LANG[lang]}")
    return [dict(type="news", title=i.findtext("title"), url=i.findtext("link"), note=i.findtext("source") or "",
                 date=parsedate_to_datetime(i.findtext("pubDate")).date().isoformat())
            for i in ET.fromstring(xml).iter("item")][:MAX_NEWS]


def collect(d, ticker, name=None, lang="en"):
    path = d / "evidence.json"
    ev = load(path, {"ticker": ticker.upper(), "name": name or ticker.upper(), "sources": []})
    found, errors = [], []
    for label, job in (("SEC", lambda: sec(ticker)), ("뉴스", lambda: news(name or ticker, lang))):
        try:
            found += job()
        except (OSError, ValueError, KeyError, ET.ParseError) as e:
            errors.append(f"{label} 수집 실패 — {type(e).__name__}: {e}")
    seen, before = {s["url"] for s in ev["sources"]}, len(ev["sources"])
    n = max([int(s["id"][1:]) for s in ev["sources"] if s["id"][1:].isdigit()] + [0])
    for s in found:
        if s["url"] not in seen:
            n += 1
            seen.add(s["url"])
            ev["sources"].append({"id": f"S{n}", **s})
    ev["as_of"] = date.today().isoformat()
    save(path, ev)
    return dict(path=str(path), added=len(ev["sources"]) - before, total=len(ev["sources"]), errors=errors)


# ── 토론: 프롬프트는 이 함수 하나가 만든다 — 대화형 CLI·서브에이전트·헤드리스 실행이 모두 같은 텍스트를 쓴다 ──

def prompt(role, d, rnd=1):
    md = lambda n: (ROOT / "agents" / f"{n}.md").read_text(encoding="utf-8")
    if role == "researcher":
        parts = [md("researcher"), "## 지금 할 일\n아래 evidence.json을 보강하고, 갱신된 전체를 JSON 객체 하나로만 출력하라."]
    else:
        parts = [md("debate"), md(role), f"## 지금 할 일\n너는 {AGENTS[role]}이다. {rnd}라운드를 수행하고 "
                                         f"그 라운드 스키마의 JSON 객체 하나만 출력하라."]
        if rnd == 2:  # 반론 라운드에서만 다른 에이전트의 1라운드를 본다
            parts += [f"## {AGENTS[a]}의 1라운드{' (너 자신)' if a == role else ''}\n```json\n"
                      f"{(d / f'{a}.1.json').read_text(encoding='utf-8').strip()}\n```" for a in AGENTS]
    ev = (d / "evidence.json").read_text(encoding="utf-8").strip()
    head = (f"<!-- council role={role} round={rnd} -->\ncouncil.py가 보낸 단일 역할 작업이다. 진행자 워크플로(AGENTS.md)를 "
            "돌리거나 파일을 만들지 말고, 아래 역할로서 JSON만 답하라.")
    return "\n\n".join([head, *parts, f"## evidence.json\n```json\n{ev}\n```"])


def ask(cli, text):  # 프롬프트를 stdin으로 넘기고 stdout 마지막 JSON 블록을 꺼낸다
    r = subprocess.run(cli, shell=True, input=text, capture_output=True, encoding="utf-8", timeout=TIMEOUT)
    if r.returncode:
        raise RuntimeError(f"`{cli}` 종료 코드 {r.returncode}: {r.stderr.strip()[-500:]}")
    blocks = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", r.stdout, re.S)
    return json.loads(blocks[-1] if blocks else r.stdout[r.stdout.find("{"):r.stdout.rfind("}") + 1])


def run(d, ticker, cli, force=False, name=None, lang="en"):
    log = lambda s: print(s, file=sys.stderr, flush=True)
    if force or not (d / "evidence.json").exists():
        r = collect(d, ticker, name, lang)
        log(f"[1/4] 수집 +{r['added']} (총 {r['total']}) " + " ".join(r["errors"]))
    if force or not load(d / "evidence.json").get("researched"):
        log("[2/4] 리서치 …")
        ev = ask(cli, prompt("researcher", d))
        sources(ev)
        save(d / "evidence.json", {**ev, "researched": date.today().isoformat()})
    for rnd in (1, 2):
        todo = [a for a in AGENTS if force or not (d / f"{a}.{rnd}.json").exists()]
        log(f"[{rnd + 2}/4] {rnd}라운드: {', '.join(AGENTS[a] for a in todo) or '완료됨'}")
        with ThreadPoolExecutor() as ex:
            for a, out in zip(todo, ex.map(lambda a: ask(cli, prompt(a, d, rnd)), todo)):
                save(d / f"{a}.{rnd}.json", out)
    return judge(d)


# ── 판정: 말이 아니라 규칙이 집계한다 ──

def sources(ev):  # 근거 검증 → {id: 근거}
    out = {}
    for s in ev["sources"]:
        if s.get("type") not in TYPES or not s.get("url") or s["id"] in out:
            raise ValueError(f"근거 {s.get('id')}: type({'|'.join(TYPES)})·url 필수, id 중복 불가")
        out[s["id"]] = s
    return out


def opinion(d, a):  # 최종 의견 = 1라운드에 2라운드를 덮어쓴 것
    r1, r2 = load(d / f"{a}.1.json"), load(d / f"{a}.2.json", {})
    return {**r1, **r2, "metrics": {**r1.get("metrics", {}), **r2.get("metrics", {})},
            "opening": r1.get("stance"), "round": 2 if r2 else 1}


def judge(d):
    ev = load(d / "evidence.json")
    src, rows = sources(ev), []
    notes = [f"{t} 유형 근거 없음 — 리서치 보강 필요" for t in ("filing", "call") if t not in {s["type"] for s in src.values()}]
    for a in AGENTS:
        o = opinion(d, a)
        m, stance = o["metrics"], o.get("stance")
        if stance not in STANCE or o["opening"] not in STANCE:
            raise ValueError(f"{a}: stance는 {'|'.join(STANCE)} 중 하나")
        fails = [msg for ok, msg in RED_LINES[a] if not ok(m)]
        items = o.get("arguments", []) + o.get("risks", []) + o.get("rebuttals", [])
        warn = soft(a, m) + [f"근거 없는 주장: {x.get('point', '')[:50]}" for x in items if not x.get("cites")]
        warn += [f"없는 근거 인용: {c}" for c in sorted({c for x in items for c in x.get("cites", [])} - src.keys())]
        warn += [f"{AGENTS[b]}에 대한 반론 없음" for b in AGENTS if o["round"] == 2 and b != a
                 and b not in {x.get("to") for x in o.get("rebuttals", [])}]
        rows.append(dict(agent=a, name=AGENTS[a], opening=o["opening"], stance=stance,
                         final="against" if stance == "for" and fails else stance,
                         conviction=min(max(int(o.get("conviction", 3)), 1), 5), red_lines=fails, warnings=warn, opinion=o))
    w = {r["agent"]: WEIGHTS[r["agent"]] / sum(WEIGHTS.values()) for r in rows}
    tally = sum(w[r["agent"]] * STANCE[r["final"]][1] for r in rows)
    verdict = "FOR" if tally > 1e-9 else "AGAINST" if tally < -1e-9 else "SPLIT"
    word = {"FOR": "찬성", "AGAINST": "반대", "SPLIT": "보류"}[verdict]
    label = f"만장일치 {word}" if len({r["final"] for r in rows}) == 1 else "팽팽" if verdict == "SPLIT" else f"{word} 우세"
    return dict(cmd="judge", ticker=ev.get("ticker", d.name), name=ev.get("name", d.name), as_of=ev.get("as_of"),
                verdict=verdict, label=label, votes={k: sum(r["final"] == k for r in rows) for k in STANCE},
                score=round(sum(w[r["agent"]] * STANCE[r["final"]][1] * r["conviction"] / 5 for r in rows), 2),
                agents=rows, notes=notes, sources=list(src.values()), ok=verdict == "FOR")


def render(r):
    src, tag = {s["id"]: s for s in r["sources"]}, lambda k: STANCE[k][0]
    block = lambda title, lines: [f"**{title}**", *lines, ""] if lines else []
    esc = lambda s: str(s).replace("|", "\\|").replace("\n", " ")
    cite = lambda ids: " ".join(f"[{c}]({src[c]['url']})" if c in src else f"[{c}?]" for c in ids)
    v = r["votes"]
    out = [f"# {r['name']} ({r['ticker']}) 투자 토론 — {r['as_of']}", "",
           f"**{r['label']}** — 찬성 {v['for']} · 반대 {v['against']} · 보류 {v['abstain']} · "
           f"확신 가중 점수 {r['score']:+.2f} (−1~+1)", "",
           "| 에이전트 | 1라운드 → 최종 | 확신 | 레드라인 | 지표 |", "|---|---|---|---|---|"]
    for x in r["agents"]:
        m = x["opinion"]["metrics"]
        kv = [f"{k}={v if isinstance(v, str) else json.dumps(v)}" for k, v in m.items() if not isinstance(v, (list, dict))]
        if x["agent"] == "ackman" and mos(m) is not None:
            kv.append(f"안전마진={mos(m):.0%}")
        final = tag(x["final"]) + (" (레드라인 위반 → 반대 집계)" if x["final"] != x["stance"] else "")
        out.append(f"| {x['name']} | {tag(x['opening'])} → {final} | {x['conviction']}/5 | "
                   f"{'✗ ' + '; '.join(x['red_lines']) if x['red_lines'] else '✓'} | {esc(', '.join(kv))} |")
    warn = [f"- ⚠ {x['name']}: {w}" for x in r["agents"] for w in x["warnings"]] + [f"- ⚠ {n}" for n in r["notes"]]
    out += ["", *warn] if warn else []
    for x in r["agents"]:
        o = x["opinion"]
        out += ["", f"## {x['name']} — {tag(x['final'])} ({x['conviction']}/5)", "", f"> {esc(o.get('thesis', ''))}", ""]
        for title, key in (("논거", "arguments"), ("사전 부검", "risks"), ("반론", "rebuttals")):
            out += block(title, [f"- {'→ ' + AGENTS.get(i['to'], i['to']) + ': ' if i.get('to') else ''}"
                                 f"{i.get('point', '')} {cite(i.get('cites', []))}" for i in o.get(key) or []])
        out += block("참이어야 하는 것", [f"- [{i.get('status')}] {i.get('claim')}" for i in o["metrics"].get("must_be_true", [])])
        out += block("인정한 점", [f"- {i}" for i in o.get("concessions") or []])
        out += block("생각을 바꿀 조건", [f"- {i}" for i in o.get("change_my_mind") or []])
    out += ["## 근거", "", "| ID | 유형 | 날짜 | 출처 | 메모 |", "|---|---|---|---|---|"]
    out += [f"| {s['id']} | {s['type']} | {s.get('date', '')} | [{esc(s.get('title') or s['url'])}]({s['url']}) | "
            f"{esc(s.get('note', ''))} |" for s in r["sources"]]
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    cmd = {k: sub.add_parser(k, help=h) for k, h in [("collect", "SEC 공시·뉴스 수집"), ("prompt", "에이전트 프롬프트 출력"),
                                                       ("run", "헤드리스 CLI로 전 과정 실행"), ("judge", "검증·표결·debate.md")]}
    cmd["prompt"].add_argument("role", choices=[*AGENTS, "researcher"])
    for p in cmd.values():
        p.add_argument("ticker", help="티커 또는 research 폴더 경로")
    for k in ("collect", "run"):
        cmd[k].add_argument("--name", help="회사명 (뉴스 검색어, 기본: 티커)")
        cmd[k].add_argument("--lang", choices=NEWS_LANG, default="en", help="뉴스 언어")
    cmd["prompt"].add_argument("--round", type=int, choices=(1, 2), default=1)
    cmd["run"].add_argument("--cli", required=True, help='프롬프트를 stdin으로 받는 명령, 예: "claude -p"')
    cmd["run"].add_argument("--force", action="store_true", help="끝난 단계도 다시 실행")
    for k in ("run", "judge"):
        cmd[k].add_argument("--json", action="store_true", help="JSON 출력 (에이전트·스크립트용)")
    a = ap.parse_args(argv)
    for s in (sys.stdout, sys.stderr):  # 어떤 터미널·CLI에서 파이프해도 UTF-8
        getattr(s, "reconfigure", lambda **_: None)(encoding="utf-8")
    d = folder(a.ticker)
    try:
        if a.cmd == "collect":
            r = collect(d, d.name, a.name, a.lang)
            print(f"{r['path']}: +{r['added']} (총 {r['total']})")
            for e in r["errors"]:
                print(e, file=sys.stderr)
            return 1 if r["errors"] else 0
        if a.cmd == "prompt":
            print(prompt(a.role, d, a.round))
            return 0
        r = run(d, d.name, a.cli, a.force, a.name, a.lang) if a.cmd == "run" else judge(d)
    except (OSError, ValueError, KeyError, TypeError, RuntimeError, subprocess.TimeoutExpired) as e:
        print(f"오류: {type(e).__name__}: {e}", file=sys.stderr)
        return 2
    md = render(r)
    (d / "debate.md").write_text(md, encoding="utf-8")
    print(json.dumps(r, ensure_ascii=False, indent=2) if a.json else md.split("\n## ")[0].rstrip() + f"\n\n전문: {d / 'debate.md'}")
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

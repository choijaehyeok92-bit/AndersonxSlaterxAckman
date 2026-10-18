#!/usr/bin/env python3
"""Anderson×Slater×Ackman×Klarman 리서치 하네스 — 증거·계산·분석·판단·검증·기록을 층으로 나눠 규율을 구조로 강제한다.

  python3 council.py collect <TICKER> [--name 회사명] [--lang en|ko] [--as-of YYYY-MM-DD]   # L1 공시·XBRL/DART·뉴스
  python3 council.py merge   <TICKER> <보강.json>                     # 리서처 보강분 병합 (수집 사실은 못 바꾼다)
  python3 council.py calc    <TICKER> [--case JSON] [--json]          # L3 코드 계산값 (analysis.json)
  python3 council.py prompt  <role> <TICKER> [--round 1|2]            # 어떤 CLI·서브에이전트에도 넣을 역할 프롬프트
  python3 council.py run     <TICKER> --cli "<명령>" [--force]         # 게이트형 파이프라인 일괄 실행
  python3 council.py judge   <TICKER> [--json] [--no-log]             # 게이트·레드라인·검증·표결 → report.md, 판단 로그
  python3 council.py update  <TICKER> [--json]                        # L7 새 실적으로 직전 판단 대조: 유지·약화·훼손
  python3 council.py decide  <TICKER> --size 0.02 [--note 이유]       # 사람이 정한 비중 기록
  python3 council.py calibrate [폴더 …] [--json]                      # 예측 교정(Brier)·찬성 비율
  python3 council.py repro   <TICKER> --cli "<명령>" [--runs 2]        # 재현성 시험
  python3 council.py audit   <TICKER> --cli "<명령>" [--n 5]           # 오류 주입 시험
  python3 council.py baserate [--from 2010] [--to 2024]               # SEC XBRL로 매출 성장 기저율 표 생성

<TICKER> 자리에는 폴더 경로도 쓸 수 있다. 표준 라이브러리만 사용(Python 3.8+).
종료 코드: 0 찬성 우세·유지·통과 · 1 반대 우세·팽팽·판정 불가·약화·훼손·불통과(collect는 수집 실패) · 2 입력·실행 오류.
"""
import argparse, json, subprocess, sys
from harness import calc, collect, core, journal, pipeline, report
from harness.judge import judge
from harness.prompts import prompt

COMMANDS = [("collect", "L1 공시·재무·뉴스 수집"), ("merge", "리서처 보강분 병합"), ("calc", "L3 코드 계산값"),
            ("prompt", "역할 프롬프트 출력"), ("run", "게이트형 파이프라인 일괄 실행"), ("judge", "판정·report.md·판단 로그"),
            ("update", "새 실적으로 직전 판단 대조"), ("decide", "사람이 정한 비중 기록"), ("calibrate", "예측 교정"),
            ("repro", "재현성 시험"), ("audit", "오류 주입 시험"), ("baserate", "기저율 표 생성")]


def parser():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    cmd = {k: sub.add_parser(k, help=h) for k, h in COMMANDS}
    cmd["prompt"].add_argument("role", choices=list(core.ROLES))
    for k in ("collect", "merge", "calc", "prompt", "run", "judge", "update", "decide", "repro", "audit"):
        cmd[k].add_argument("ticker", help="티커 또는 research 폴더 경로")
    cmd["merge"].add_argument("file", help="리서처가 낸 보강 JSON ({sources, facts, drop, gaps})")
    for k in ("collect", "run"):
        cmd[k].add_argument("--name", help="회사명 (뉴스 검색어, 기본: 티커)")
        cmd[k].add_argument("--lang", choices=collect.NEWS_LANG, default="en", help="뉴스 언어")
        cmd[k].add_argument("--as-of", dest="as_of", help="기준일 YYYY-MM-DD — 그날까지 제출된 자료만 (과거 시점 재현)")
    cmd["prompt"].add_argument("--round", type=int, choices=(1, 2), default=1)
    cmd["calc"].add_argument("--case", help='페르소나 가정 미리보기, 예: \'{"anderson": {"from": "bull", "revenue_growth": 0.3}}\'')
    for k in ("run", "repro", "audit"):
        cmd[k].add_argument("--cli", required=True, help='프롬프트를 stdin으로 받는 명령, 예: "claude -p"')
    cmd["run"].add_argument("--force", action="store_true", help="끝난 단계도 다시 실행")
    cmd["judge"].add_argument("--no-log", action="store_true", help="판단 로그에 기록하지 않는다")
    cmd["decide"].add_argument("--size", type=float, required=True, help="비중 0~1 (0.02 = 2%%)")
    cmd["decide"].add_argument("--note", default="", help="이유")
    cmd["calibrate"].add_argument("dirs", nargs="*", help="research 폴더들 (기본: research/*)")
    cmd["repro"].add_argument("--runs", type=int, default=2)
    cmd["audit"].add_argument("--n", type=int, default=5, help="주입할 오류 수")
    cmd["audit"].add_argument("--seed", type=int, default=0)
    cmd["baserate"].add_argument("--from", dest="first", type=int, default=2010)
    cmd["baserate"].add_argument("--to", dest="last", type=int, default=2024)
    for k in ("calc", "run", "judge", "update", "calibrate", "repro", "audit"):
        cmd[k].add_argument("--json", action="store_true", help="JSON 출력 (에이전트·스크립트용)")
    return ap


def show(a, data, text):
    print(json.dumps(data, ensure_ascii=False, indent=2, default=str) if getattr(a, "json", False) else text)


def verdict(a, d, r):
    md = report.render(r)
    (d / "report.md").write_text(md, encoding="utf-8")
    if not getattr(a, "no_log", False):
        journal.log(d, r)
    head = md.split("\n## ")[0].rstrip()
    show(a, r, head + f"\n\n전문: {d / 'report.md'}")
    return 0 if r["ok"] else 1


def main(argv=None):
    a = parser().parse_args(argv)
    for s in (sys.stdout, sys.stderr):  # 어떤 터미널·CLI에서 파이프해도 UTF-8
        getattr(s, "reconfigure", lambda **_: None)(encoding="utf-8")
    d = core.folder(a.ticker) if getattr(a, "ticker", None) else None
    try:
        if a.cmd == "collect":
            r = collect.collect(d, d.name, a.name, a.lang, a.as_of)
            print(f"{r['path']}: 근거 +{r['added']} (총 {r['total']}) · 공시 재무 사실 {r['facts']}개")
            for e in r["errors"]:
                print(e, file=sys.stderr)
            return 1 if r["errors"] else 0
        if a.cmd == "merge":
            r = collect.merge(d, core.load(a.file))
            print(f"{r['path']}: 사실 +{r['facts_added']} · 근거 {r['sources']}개")
            for x in r["rejected"]:
                print(f"제외: {x}", file=sys.stderr)
            return 0
        if a.cmd == "calc":
            ev, model = core.load(d / "evidence.json"), core.load(d / "model.json", {})
            an = calc.analyze(ev, model or None, json.loads(a.case) if a.case else None)
            core.save(d / "analysis.json", an)
            show(a, an, report.analysis_md(an) + f"\n\n저장: {d / 'analysis.json'}")
            return 0
        if a.cmd == "prompt":
            print(prompt(a.role, d, a.round))
            return 0
        if a.cmd == "judge":
            return verdict(a, d, judge(d))
        if a.cmd == "run":
            return verdict(a, d, pipeline.run(d, d.name, a.cli, a.force, a.name, a.lang, a.as_of))
        if a.cmd == "update":
            r = journal.update(d)
            lines = [f"{d.name} 직전 판단({r['ref']}) 대조: **{r['status']}**"]
            lines += [f"- KPI {k['id']} {k['metric']} {k['period']} {k['op']} {k['value']:g}: {k['status']}"
                      + ("" if k["actual"] is None else f" (실제 {k['actual']:g})") for k in r["kpis"]]
            lines += [f"- 반증 조건 {b['who']}: {b['note'] or b['metric']} — {b['status']}" for b in r["breaks"]]
            lines += [f"- 추정 대비 {x['metric']} {x['period']}: {x['diff']:+.1%}" for x in r["deviations"]]
            if t := r.get("price_trigger"):
                lines.append(f"- 가격 조건 도달: 주가 {r['price']:,.2f} ≤ {t['price']:,.2f} → 직전 판단의 조건부 판정은 {t['label']} — 재판정 권장")
            lines += ["→ 재토론 권장: 근거 갱신 후 `run --force` 또는 라운드 파일 삭제 뒤 다시 판정"] if r["status"] != "유지" else []
            show(a, r, "\n".join(lines))
            return 0 if r["status"] == "유지" and not r.get("price_trigger") else 1
        if a.cmd == "decide":
            r = journal.decide(d, a.size, a.note)
            print(f"기록: {r['ref']} {r['verdict']} → 비중 {r['size']:.1%} (하네스 참고값 {r['suggested'] or 0:.1%})")
            return 0
        if a.cmd == "calibrate":
            dirs = [core.folder(x) for x in a.dirs] or sorted(p for p in (core.ROOT / "research").glob("*") if p.is_dir())
            r = journal.calibrate(dirs)
            show(a, r, journal.calibrate_md(r))
            return 0
        if a.cmd == "repro":
            r = pipeline.repro(d, a.cli, a.runs)
            show(a, r, "\n".join([f"재현성 {a.runs}회: 판정 {'일치' if r['verdict_agree'] else '불일치'} · 표 "
                                  f"{'일치' if r['agents_agree'] else '불일치'} · 회계 판정 {'일치' if r['forensic_agree'] else '불일치'}"
                                  + ("" if r["iv_spread"] is None else f" · 기본 IV 편차 {r['iv_spread']:.0%}")
                                  + ("" if r["irr_spread"] is None else f" · 기대수익률 편차 {r['irr_spread']:.1%}p"),
                                  *[f"- run{i}: {x['label']} {x['agents']}" for i, x in enumerate(r["runs"], 1)]]))
            return 0 if r["ok"] else 1
        if a.cmd == "audit":
            r = pipeline.audit(d, a.cli, a.n, a.seed)
            show(a, r, f"오류 {r['injected']}개 주입 — 검증자 {r['caught_by_verifier']}개 · 기계 대조 {r['caught_by_code']}개 적발 · "
                       f"주입하지 않은 주장 {r['clean']}개 중 지적 {r['flagged_clean']}개"
                       + ("" if r["false_alarms"] is None else f" (기존 검증에서 통과했는데 이번에 지적 = 오탐 {r['false_alarms']}개)"))
            return 0 if r["ok"] else 1
        if a.cmd == "baserate":
            t = collect.baserate(a.first, a.last)
            print("data/base_rates.json: " + ", ".join(f"{h}년 n={x['all']['n']}" for h, x in t["horizons"].items()))
            return 0
    except (OSError, ValueError, KeyError, TypeError, RuntimeError, subprocess.TimeoutExpired) as e:
        print(f"오류: {type(e).__name__}: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

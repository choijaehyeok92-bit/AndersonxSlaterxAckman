"""보고서 — 계산값 표(프롬프트와 공유)와 report.md. 서술은 에이전트가, 숫자 표는 코드가 만든다."""
import json, re
from . import core, rules

ROWS = [("revenue", "매출", "money"), ("revenue_growth", "매출 성장", "pct"), ("gross_margin", "총이익률", "pct"),
        ("operating_margin", "영업이익률", "pct"), ("net_income", "순이익", "money"), ("ocf", "영업현금흐름", "money"),
        ("capex", "설비투자", "money"), ("fcf", "FCF", "money"), ("fcf_margin", "FCF 마진", "pct"),
        ("fcf_conversion", "FCF/순이익", "x"), ("sbc", "SBC", "money"), ("sbc_to_revenue", "SBC/매출", "pct"), ("sbc_to_ocf", "SBC/영업현금흐름", "pct"),
        ("fcf_after_sbc", "SBC 차감 FCF", "money"), ("roic", "ROIC", "pct"), ("net_cash", "순현금", "money"),
        ("net_debt_to_ebitda", "순부채/EBITDA", "x"), ("diluted_shares", "희석 주식 수", "count"),
        ("share_change", "주식 수 변화", "pct"), ("dso", "DSO(일)", "num"), ("dio", "DIO(일)", "num"),
        ("accruals_ratio", "발생액 비율", "pct")]
SCEN = {"bear": "약세", "base": "기본", "bull": "강세"}
KIND = {"mos": "pct", "cash_min": "money", "starter_weight": "pct", "upside_10y": "x", "revenue_5y": "x", "net_debt_to_ebitda": "x"}
PARTS = {"revenue": "매출 성장", "margin": "마진 변화", "multiple": "멀티플 변화", "margin_multiple": "마진·멀티플(P/S)",
         "shares": "주식 수 변화", "cash": "현금 축적"}


def money(v, cur=""):
    if v is None:
        return "—"
    a = abs(v)
    s = f"{v / 1e12:,.2f}조" if a >= 1e12 else f"{v / 1e8:,.1f}억" if a >= 1e8 else f"{v / 1e4:,.0f}만" if a >= 1e5 else f"{v:,.0f}"
    return f"{s} {cur}".strip()


def value(f):  # 사실 하나를 단위에 맞게
    v, u = f["value"], f["unit"]
    return money(v) if u == "shares" or re.match(r"^[A-Z]{3}$", u) else f"{v:g}"


def fmt(v, kind="num", cur=""):
    if v is None:
        return "—"
    if isinstance(v, bool):
        return "예" if v else "아니오"
    if isinstance(v, str):
        return v
    return {"money": lambda: money(v, cur), "pct": lambda: f"{v:.1%}", "x": lambda: f"{v:.2f}x",
            "count": lambda: money(v), "num": lambda: f"{v:,.1f}" if abs(v) < 1e4 else f"{v:,.0f}"}[kind]()


def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def table(head, rows):
    return [f"| {' | '.join(head)} |", "|" + "---|" * len(head), *[f"| {' | '.join(esc(c) for c in r)} |" for r in rows]]


def evidence_md(ev, fx, urls=False):
    """근거와 사실 — 수집 재무는 지표×기간 표로, 나머지는 한 줄씩."""
    out = ["### 근거 (sources)", ""]
    out += table(["ID", "유형", "날짜", "제목", "메모"] + (["URL"] if urls else []),
                 [[s["id"], s["type"], s.get("date", ""), s.get("title", ""), s.get("note", "")] + ([s["url"]] if urls else [])
                  for s in ev.get("sources", [])])
    pivot, lines = {}, []
    for f in fx.facts.values():
        if f["basis"] == "reported" and f.get("period") and (f.get("origin") in ("sec", "dart") or not f.get("note")):
            pivot.setdefault((f["metric"], f["unit"]), []).append(f)
        else:
            rng = f" (범위 {f['low']:g}~{f['high']:g})" if "low" in f and "high" in f else ""
            lines.append(f"- {f['id']} {f['metric']} = {f['value']:g} {f['unit']}{rng} · {f.get('period') or f['end']} · "
                         f"{f['basis']} · {f['source']}" + (f" · {f['note']}" if f.get("note") else ""))
    out += ["", "### 사실 (facts) — 보고 수치, 지표×기간 (값 [사실 ID·출처])", ""]
    for (m, u), fs in sorted(pivot.items()):
        fs.sort(key=lambda f: f["end"])
        out.append(f"- {m} ({u}): " + " · ".join(f"{f['period']}{'*' if f.get('derived') else ''} {value(f)} [{f['id']}·{f['source']}]" for f in fs))
    out += ["", "### 사실 (facts) — 기타 (KPI·가이던스·컨센서스·시장)", "", *(lines or ["- 없음"])]
    if fx.warnings:
        out += ["", "### 제외·충돌한 사실", "", *[f"- {w}" for w in fx.warnings]]
    if ev.get("gaps"):
        out += ["", "### 리서처가 찾지 못한 것", "", *[f"- {g}" for g in ev["gaps"]]]
    return "\n".join(out)


def analysis_md(an, valuation=True):
    cur, out = an["currency"] or "", []
    rows = an["history"]
    if rows:
        out += ["### 재무 이력 (코드 계산 · 인용은 C:지표@기간, 예: C:fcf_margin@" + rows[-1]["period"] + ")", ""]
        out += table(["지표 (키)"] + [r["period"] for r in rows],
                     [[f"{label} ({k})"] + [fmt(r.get(k), kind, cur) for r in rows] for k, label, kind in ROWS
                      if any(r.get(k) is not None for r in rows)])
        shown = {k for k, _, _ in ROWS} | {"period", "end"}
        more = sorted({k for r in rows for k, v in r.items() if k not in shown and isinstance(v, (int, float)) and not isinstance(v, bool)})
        out += ["", "표에 없는 키도 인용할 수 있다: " + ", ".join(more)] if more else []
    m = an["market"]
    if m:
        t = an["ttm"] or {}
        out += ["", f"### 시장 · {t.get('period', '')} 기준 (C:키)", ""]
        out += table(["항목", "값"], [
            ["주가 (price)", f"{m['price_quote']:g} {m['price_unit']} ({m['price_date']}, {m['price_fact']})"
             + ("" if m["price_unit"].endswith("/share") and m["price_unit"].startswith(cur) else f" → 주당 {m['price']:,.2f} {cur}")],
            ["희석 주식 수 (shares)", money(m["shares"])], ["시가총액 (market_cap)", money(m["market_cap"], cur)],
            ["순현금 (net_cash)", money(m["net_cash"], cur)], ["EV (ev)", money(m["ev"], cur)],
            ["FCF 수익률 (fcf_yield)", fmt(m["fcf_yield"], "pct")], ["P/FCF (p_fcf)", fmt(m["p_fcf"], "x")],
            ["EV/매출 (ev_revenue)", fmt(m["ev_revenue"], "x")], ["PER (pe)", fmt(m["pe"], "x")],
            ["순부채/EBITDA (net_debt_to_ebitda)", fmt(m["net_debt_to_ebitda"], "x")],
            ["현금 소진 연수 (runway_years)", fmt(m["runway_years"])]])
    out += ["", "### 회계 품질 신호 (코드 계산 — forensic이 하나씩 해명해야 한다)", ""]
    out += [f"- [{f['severity']}] {f['key']}{' (C:' + f['key'] + ')' if isinstance(f['value'], (int, float)) else ''}: {f['message']}"
            for f in an["forensic"]] or ["- 신호 없음"]
    if an["guidance"]:
        out += ["", f"### 가이던스 적중 (C:guidance_hit_rate = {an['guidance_hit_rate']:.0%})", ""]
        out += [f"- {g['metric']} {g['period']}: 가이던스 {money(g['guided'])} → 실제 {money(g['actual'])} = {g['result']} "
                f"[{', '.join(g['cites'])}]" for g in an["guidance"]]
    rd = an["reverse_dcf"]
    if rd:
        out += ["", "### 역DCF — 현재 가격이 가정하는 것", "",
                f"EV {money(rd['ev'], cur)}를 정당화하려면 매출이 {rd['years']}년간 연 몇 % 커져야 하는가 — FCF 마진이 지금 값에서 "
                f"목표 마진으로 직선 수렴, 할인율 {rd['discount_rate']:.0%}, 이후 영구성장 {rd['terminal_growth']:.0%}."]
        if rd["margin"]:
            imp = rd["implied_cagr"]
            out.append(f"기본 시나리오 목표 마진 {rd['margin']:.0%} 기준: 연 {'계산 불가' if imp is None else f'{imp:.1%}'} (C:implied_cagr)")
        out += [""] + table(["목표 FCF 마진", "내재 매출 성장(연)", "인용 키"],
                            [[f"{m:.0%}", "—" if g is None else f"{g:.1%}", f"C:implied_cagr@m{m * 100:g}"] for m, g in rd["grid"].items()])
    v = an["valuation"]
    if valuation and v:
        out += ["", f"### 시나리오 가치 — {v['years']}년, 할인율 {v['discount_rate']:.0%} "
                    "(C:지표@시나리오 — p·revenue_cagr·fcf_margin·exit_multiple·value·iv·irr·revenue·fcf)", ""]
        out += table(["시나리오", "확률", f"{v['years']}년 매출", "매출 연성장", "FCF 마진", "출구 P/FCF", "주당 가치", "현재가치(IV)", "연 수익률"],
                     [[SCEN[k], f"{s['p']:.0%}", money(s["rows"][-1]["revenue"], cur),
                       f"{s['revenue_cagr']:.1%}",
                       f"{s['rows'][-1]['fcf_margin']:.0%}", f"{s['multiple']:g}x", f"{s['value']:,.2f}", f"{s['iv']:,.2f}",
                       f"{s['irr']:+.1%}"] for k, s in v["scenarios"].items()])
        e = v["expected"]
        out += ["", f"확률 가중: 주당 가치 {e['value']:,.2f} · IV {e['iv']:,.2f} · 기대 연 수익률 {e['irr']:+.1%} (C:expected_irr) · "
                    f"손실 확률 {e['p_loss']:.0%} (C:p_loss) · 현재 주가 {an['market']['price']:,.2f}"]
        dec = v["scenarios"]["base"]["decomposition"]
        if dec:
            out += ["", "기본 시나리오 연 수익률 분해 (로그 기여, 합 = 총계): " + " · ".join(
                f"{PARTS[k]} {x:+.1%}" for k, x in dec.items() if k != "total") + f" = {dec['total']:+.1%}"]
        sv = v["sensitivity"]
        out += ["", "민감도 — 기본 시나리오 연 수익률 (행: 매출 성장 ±, 열: 출구 멀티플 배수)", ""]
        out += table(["성장 \\ 멀티플"] + [f"×{k:g}" for k in sv["multiples"]],
                     [[f"{s:+.0%}p"] + [f"{x:+.1%}" for x in row] for s, row in zip(sv["shifts"], sv["irr"])])
        b = v["scenarios"]["base"]["rows"]
        out += ["", "기본 시나리오 연도별 (드라이버 모델)", ""]
        out += table(["기간", "매출", "FCF 마진", "FCF", "희석 주식 수", "순현금"],
                     [[r["period"], money(r["revenue"], cur), f"{r['fcf_margin']:.1%}", money(r["fcf"], cur), money(r["shares"]),
                       money(r["net_cash"], cur)] for r in b])
        if v["consensus"]:
            out += ["", "### 컨센서스 대비 (C:consensus_diff@지표@기간)", ""]
            out += table(["지표", "기간", "컨센서스", "기본 시나리오", "차이"],
                         [[c["metric"], c["period"], money(c["consensus"], cur), money(c["model"], cur), f"{c['diff']:+.1%}"]
                          for c in v["consensus"]])
    if an["base_rates"]:
        out += ["", "### 기저율 — 같은 성장을 해낸 기업 비율 (C:base_rate@implied·base·bull)", ""]
        out += [f"- {b['label']}: 연 {b['cagr']:.1%} × {b['years']}년 → " +
                ("기저율 표 없음" if b.get("share") is None else
                 f"{'최대 ' if b.get('capped') else ''}{b['share']:.1%} ({b['bucket']}, n={b['n']})") for b in an["base_rates"]]
    if valuation and any(len(p) > 1 for p in an["personas"].values()):
        out += ["", "### 페르소나 지표 (코드 계산 · case 기본값 기준, C:지표@페르소나)", ""]
        for a, p in an["personas"].items():
            kv = [f"{k}={fmt(x, KIND.get(k, 'num'), cur)}" for k, x in p.items() if k not in ("case",) and x is not None]
            out.append(f"- {core.AGENTS[a]} case={json.dumps(p['case'], ensure_ascii=False)}: {', '.join(kv)}")
    if an["warnings"]:
        out += ["", "### 계산 경고", "", *[f"- {w}" for w in an["warnings"]]]
    return "\n".join(out)


def render(r):
    """report.md — 6개 산출물(variant perception·드라이버 모델·시나리오 분포·반증 조건·KPI·확신도)이 맨 앞."""
    src, tag = {s["id"]: s for s in r["sources"]}, lambda k: core.STANCE[k][0]
    block = lambda title, lines: [f"**{title}**", *lines, ""] if lines else []
    cite = lambda ids: " ".join(f"[{c}]({src[c]['url']})" if c in src else f"[{c}]" for c in (ids if isinstance(ids, list) else []))
    an, v = r["analysis"], r["analysis"].get("valuation")
    cur = an.get("currency") or ""
    out = [f"# {r['name']} ({r['ticker']}) 리서치 보고서 — 기준일 {r['as_of']}", "",
           f"**{r['label']}** — " + (f"찬성 {r['votes']['for']} · 반대 {r['votes']['against']} · 보류 {r['votes']['abstain']} · "
                                     f"확신 가중 점수 {r['score']:+.2f} (−1~+1)" if r["agents"] else "토론 전 단계에서 멈춤"), ""]
    out += [f"- 게이트: " + " → ".join(f"{g['name']} {'✓' if g['ok'] else '✗ ' + '; '.join(g['why'])}" for g in r["gates"]), ""]
    if r.get("gated"):
        out += [f"> 게이트에서 멈췄다 — 뒤 단계(모델·토론)는 실행하지 않는다. 이유: {r['gated']}", ""]
    vp = (r.get("model") or {}).get("variant") or {}
    rd = an.get("reverse_dcf") or {}
    if v or vp:
        out += ["## 1. Variant perception", ""]
        if rd.get("implied_cagr") is not None and v:
            b = v["scenarios"]["base"]["rows"]
            cg = (b[-1]["revenue"] / an["history"][-1]["revenue"]) ** (1 / len(b)) - 1
            out += [f"- 시장 내재: 매출 {rd['years']}년 연 {rd['implied_cagr']:.1%} (FCF 마진 {rd['margin']:.0%} 수렴 가정) · "
                    f"기본 시나리오: {len(b)}년 연 {cg:.1%}"]
        for k, label in (("market", "시장이 반영한 것"), ("ours", "우리가 다르게 보는 점"), ("why", "왜 우리가 맞는가"),
                         ("catalyst", "촉매"), ("when", "시점")):
            if vp.get(k):
                out.append(f"- {label}: {vp[k]}" + (f" {cite(vp.get('cites'))}" if k == "why" else ""))
        for c in (v or {}).get("consensus", []):
            out.append(f"- 컨센서스 대비 {c['metric']} {c['period']}: {c['diff']:+.1%} ({money(c['model'], cur)} vs {money(c['consensus'], cur)})")
        out.append("")
    if v:
        e = v["expected"]
        out += ["## 2. 시나리오 분포와 기대수익률", "",
                f"확률 가중 IV **{e['iv']:,.2f}** vs 주가 {an['market']['price']:,.2f} · 기대 연 수익률 **{e['irr']:+.1%}** · "
                f"손실 확률 {e['p_loss']:.0%}", ""]
        out += table(["시나리오", "확률", "주당 가치", "IV", "연 수익률", "근거"],
                     [[SCEN[k], f"{s['p']:.0%}", f"{s['value']:,.2f}", f"{s['iv']:,.2f}", f"{s['irr']:+.1%}",
                       ((r.get("model") or {}).get("scenarios", {}).get(k, {}).get("rationale") or "")[:120]]
                      for k, s in v["scenarios"].items()]) + [""]
    if r["breaks"]:
        out += ["## 3. 반증 조건 (thesis break)", ""]
        out += [f"- [{b['status']}] {b['who']}: {b['note'] or b.get('metric')}" +
                (f" — `{b['metric']} {b['op']} {b['value']:g}`" + (f" ({b['period']})" if b.get("period") else "") if b.get("metric") else "")
                for b in r["breaks"]] + [""]
    if r["kpis"]:
        out += ["## 4. 모니터링 KPI (예측 — 교정의 재료)", ""]
        out += table(["ID", "지표", "기간", "기대", "확률", "이유"],
                     [[k["id"], k["metric"], k["period"], f"{k['op']} {k['value']:g}", f"{k['p']:.0%}", k.get("why", "")]
                      for k in r["kpis"]]) + [""]
    sz = r["sizing"]
    out += ["## 5. 확신도와 비중", "",
            f"- 확신 가중 점수 {r['score']:+.2f} · 비중 참고값 {sz['suggested']:.1%} ({sz['why']})"
            + (f" · 슬레이터 시작 비중 {sz['starter_weight']:.1%}" if sz.get("starter_weight") is not None else ""),
            "- **최종 확신도와 비중은 사람이 정한다** — `python3 council.py decide <TICKER> --size 0.02 --note \"이유\"`", ""]
    if r["agents"]:
        out += ["## 표결", ""]
        rows = []
        for x in r["agents"]:
            final = tag(x["final"]) + {"redline": " (레드라인 → 반대)", "verify": " (검증 실패 → 보류)"}.get(x["override"], "")
            kv = [f"{k}={fmt(val, KIND.get(k, 'num'), cur)}" for k, val in x["metrics"].items()
                  if not isinstance(val, (list, dict)) and val is not None and k not in ("price",)]
            rows.append([x["name"], f"{tag(x['opening'])} → {final}", f"{x['conviction']}/5",
                         "✗ " + "; ".join(x["red_lines"]) if x["red_lines"] else "✓",
                         f"{x['verify']['failed']}/{x['verify']['total']} 실패", ", ".join(kv)])
        out += table(["에이전트", "1라운드 → 최종", "확신", "레드라인", "논거 검증", "지표 (코드 계산 포함)"], rows)
    warn = [f"- ⚠ {x['name']}: {w}" for x in r["agents"] for w in x["warnings"]] + [f"- ⚠ {n}" for n in r["notes"]]
    out += ["", *warn] if warn else []
    for x in r["agents"]:
        o = x["opinion"]
        out += ["", f"## {x['name']} — {tag(x['final'])} ({x['conviction']}/5)", "", f"> {esc(o.get('thesis', ''))}", ""]
        if o.get("change_reason"):
            out += [f"*이전 판단 대비: {o['change_reason']}*", ""]
        for title, key in (("논거", "arguments"), ("사전 부검", "risks"), ("반론", "rebuttals")):
            out += block(title, [f"- {'→ ' + core.ROLES.get(i['to'], i['to']) + ': ' if i.get('to') else ''}"
                                 f"{i.get('point', '')} {cite(i.get('cites'))}" for i in core.items(o.get(key), "point")])
        out += block("참이어야 하는 것", [f"- [{i.get('status')}] {i.get('claim')}" for i in core.items(x["metrics"].get("must_be_true"), "claim")])
        out += block("인정한 점", [f"- {i}" for i in o.get("concessions") or []])
    mods = r.get("modules") or {}
    if mods:
        out += ["", "## 분석 모듈 (L4)", ""]
        for k, m in mods.items():
            grade = m.get("grade") or m.get("alignment") or m.get("unit_economics") or ""
            out += [f"### {core.MODULES[k]}{' — ' + grade if grade else ''}", "", m.get("summary", ""), ""]
            items = [*core.items(m.get("flags"), "point"), *core.items(m.get("findings"), "point"), *core.items(m.get("moat"), "point")]
            out += [f"- {('[' + (i.get('severity') or i.get('assessment') or i.get('evidence') or i.get('area') or '') + '] ') if (i.get('severity') or i.get('assessment') or i.get('evidence') or i.get('area')) else ''}"
                    f"{i.get('key', '') + ': ' if i.get('key') else ''}{i.get('point', '')} {cite(i.get('cites'))}" for i in items] + [""]
    rt = r.get("redteam") or {}
    if rt:
        out += ["## 레드팀 — 사전 부검 (5년 뒤 −60%라면)", ""]
        out += [f"- ({p.get('p') or 0:.0%}) {p.get('point', '')} {cite(p.get('cites'))}" for p in core.items(rt.get("premortem"), "point")]
        out += [f"- 약한 가정 `{w.get('assumption')}`: {w.get('point', '')} {cite(w.get('cites'))}" for w in core.items(rt.get("weakest"), "point")] + [""]
    vr = r["verification"]
    if vr["checked"]:
        out += ["## 검증 (L6)", "", f"주장 {vr['total']}개 — " + " · ".join(f"{k} {n}" for k, n in vr["counts"].items()), ""]
        out += [f"- [{c['verdict']}] {core.ROLES.get(c['role'], c['role'])}: {c['point'][:90]} — {c.get('reason', '')}"
                for c in vr["flagged"]] + [""]
    uv = r.get("user_view")
    if uv:
        out += ["## 사용자 견해 대조 (분석이 끝난 뒤에만 비교한다)", "", *[f"- {line}" for line in uv["lines"]], ""]
    out += ["## 계산 근거 (L3)", "", analysis_md(an), ""]
    out += ["## 근거", ""]
    out += table(["ID", "유형", "날짜", "출처", "메모"],
                 [[s["id"], s["type"], s.get("date", ""), f"[{esc(s.get('title') or s['url'])}]({s['url']})", s.get("note", "")]
                  for s in r["sources"]])
    return "\n".join(out) + "\n"

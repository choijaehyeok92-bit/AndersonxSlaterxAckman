# Palantir Technologies (PLTR): long-term (5–10 yr) holding fact base, as of 2026-10-18

Scope note: these notes build on the internal harness at /home/claude/choijaehyeok92-bit/andersonxslaterxackman/research/PLTR/ (report.md, redteam.json, evidence.json; collected 2026-10-17). The harness verdict was **against (반대 우세), score −0.27**. It put probability-weighted IV at **$111.93 vs price $186.03**, expected IRR at **−0.6%/yr** and loss probability at **80%**. Its base case was 5-yr revenue CAGR 41% (FY26 +82%, then +50/35/26/20%), FCF margin 52% and exit P/FCF 35x. "Derived" means my own arithmetic from the cited figures. "Harness check" lines record whether a finding confirms, updates or contradicts a harness claim.

## Q1. Latest reported quarter (Q2 2026) and FY2026 guidance

### Takeaway
Q2 2026 (reported 2026-08-03) was the strongest quarter in Palantir's history: revenue $1.935B (+93% YoY), US commercial $764M (+149%), NDR 157%, adjusted operating margin 62%, GAAP operating margin 47% and Rule of 40 at 155%. FY2026 revenue guidance was raised to $8.150–8.158B (+82%). Q3 2026 results come on **Monday 2026-11-02, after the close**. International is the clear soft spot: international commercial grew +26% YoY and only +2% QoQ.

### Cited Findings
**Q2 2026 (quarter ended 2026-06-30, reported 2026-08-03)**
- Total revenue $1,935.5M, +93% YoY and +19% QoQ (Q2 2025: $1,003.7M). H1 2026 revenue was $3,568.0M — [Q2 2026 press release, 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- US revenue $1,573M (+115% YoY, +23% QoQ). US commercial $764M (+149% YoY, +28% QoQ). US government $809M (+90% YoY, +18% QoQ) — [Q2 press release](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- International commercial $182M (+26% YoY, +2% QoQ). International government $181M (+42% YoY, +5% QoQ) — CFO David Glazer, [Q2 2026 call transcript (Motley Fool, 2026-08-10)](https://www.fool.com/earnings/call-transcripts/2026/08/10/palantir-pltr-q2-2026-earnings-call-transcript/)
- For comparison, Q1 2026 had international commercial at $179M (+26%) and international government at $172M (+51%). Q1 total revenue was $1.633B (+85%) and US revenue $1.282B (+104%) — [TIKR, 2026-06-23](https://www.tikr.com/blog/palantir-stock-fell-7-as-france-drops-its-software-is-the-sovereignty-threat-real-or-a-buying-opportunity)
- Government revenue (US plus international) was ~$990M of $1,935.5M in Q2, about 51%. H1 was ~51.8%; FY2025 was 54% — [sec-api.io analysis of the Q2 10-Q](https://sec-api.io/insights/financial-analysis-of-palantir-technologies-the-quarter-to-30-june-2026-against-the-fy2025-record) (secondary analysis of the 10-Q; the ratio is calculated)
- **Customers and retention:** US commercial customer count 653 (+35% YoY, +6% QoQ). Net dollar retention 157%, up 700 bp QoQ. Karp: "the NDR number is anomalously strong." The total customer count was not disclosed — [Q2 call transcript](https://www.fool.com/earnings/call-transcripts/2026/08/10/palantir-pltr-q2-2026-earnings-call-transcript/)
- **Bookings and backlog:** total TCV $3.373B (+49% YoY). US commercial TCV $2.132B (+153%, a record). US commercial remaining deal value (RDV) $6.238B (+124% YoY, +27% QoQ). Deals closed: 220 at ≥$1M, 98 at ≥$5M and 73 at ≥$10M — [Q2 press release](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- Total remaining deal value of $13.1B is cited in a bull case — [24/7 Wall St., 2026-10-14](https://247wallst.com/investing/2026/10/14/palantirs-earnings-gamble-nine-straight-beats-set-high-bar-for-november-2/) (secondary; the press release does not disclose total RDV)
- RPO was $4.9B at 2026-06-30, with 43% expected within 12 months and 36% in months 13–36. Contract liabilities were $1.1B (deferred revenue $613.2M plus customer deposits $452.6M), up from $812.3M at 2025-12-31 — [sec-api.io 10-Q analysis](https://sec-api.io/insights/financial-analysis-of-palantir-technologies-the-quarter-to-30-june-2026-against-the-fy2025-record)
- **Profitability:**
  - GAAP operating income $912.0M (47% margin; Q2 2025: $269.3M). Adjusted operating income $1,194.5M (62%; Q2 2025: $464.4M, 46%). Adjusted EBITDA $1,202.7M — [Q2 press release](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
  - GAAP net income $1,061.9M (55% margin). GAAP diluted EPS $0.41 (Q2 2025: $0.13). Adjusted EPS $0.41 vs a ~$0.28 consensus estimate — [Q2 press release](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm); [24/7 Wall St., 2026-10-14](https://247wallst.com/investing/2026/10/14/palantirs-earnings-gamble-nine-straight-beats-set-high-bar-for-november-2/)
  - Rule of 40 was 155% (company definition: revenue growth plus adjusted operating margin) — [Q2 press release](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- **Cash flow:** operating cash flow $1,216.2M (63% margin). Adjusted FCF $1,220.4M (63%; Q2 2025: $568.8M, 57%). H1 2026 operating cash flow $2,115.3M — [Q2 press release](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- **Expense ramp:** adjusted expenses rose 37% YoY to $741M, mainly from technical hiring. The CFO guided to "a significant ramp in expense in the third quarter" from new-hire seasonality — [Q2 call transcript](https://www.fool.com/earnings/call-transcripts/2026/08/10/palantir-pltr-q2-2026-earnings-call-transcript/)

**Guidance (given 2026-08-03)**
- Q3 2026: revenue $2.160–2.164B; adjusted operating income $1.292–1.296B; GAAP operating income and net income positive (not quantified) — [Q2 press release](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- FY2026:
  - Revenue $8.150–8.158B (+82%)
  - US commercial revenue >$3.424B (≥+134%)
  - Adjusted operating income $4.889–4.897B
  - Adjusted FCF $4.5–4.7B
  - GAAP operating income and net income positive in every quarter
  - Source: [Q2 press release](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- **Guidance path:** FY2026 revenue growth guidance went from 61% to 71% at Q1 (May 2026), then to 82% at Q2. Q4 2025 revenue was $1.4B (+70%); Q1 2026 was $1.63B (+85%) — [Motley Fool via Yahoo, 2026-07-09](https://finance.yahoo.com/markets/stocks/articles/why-palantir-stock-plunged-34-071500679.html)
- **Beat record:** nine consecutive quarterly beats. The stock rose 29.45% on Q2 earnings day but fell 6.93% after Q1 despite an ~18% beat — [24/7 Wall St., 2026-10-14](https://247wallst.com/investing/2026/10/14/palantirs-earnings-gamble-nine-straight-beats-set-high-bar-for-november-2/); [TIKR, 2026-06-23](https://www.tikr.com/blog/palantir-stock-fell-7-as-france-drops-its-software-is-the-sovereignty-threat-real-or-a-buying-opportunity)
- **Q3 date:** results on Monday 2026-11-02 after the close; webcast at 5:00 pm ET. The date was announced 2026-10-12 — [ScanX](https://scanx.trade/stock-market-news/companies/palantir-technologies-q3fy26-results-earnings-release-set-nov-2/53381825); [Yahoo/Business Wire](https://finance.yahoo.com/markets/stocks/articles/palantir-announces-date-third-quarter-200500055.html)
- **Q3 consensus (as of ~2026-10-02):** revenue ~$2.18B and adjusted operating income ~$1.31B, both above the top of guidance — [TIKR via Yahoo, 2026-10-02](https://finance.yahoo.com/markets/stocks/articles/palantir-stock-rose-60-q3-151806420.html)

### Inferences
- Derived: implied Q1 2026 US commercial revenue = $764M / 1.28 ≈ $597M, so H1 US commercial ≈ $1.36B. Reaching the FY guide of >$3.424B needs ≥$2.06B in H2, an average of ~$1.03B per quarter. **The company's own guidance therefore already implies Q3 US commercial near or above the harness's K3 threshold (≥$900M).** Palantir has historically guided conservatively, so the harness's 65% probability on K3 looks low.
- Derived: the Q3 revenue guide of $2.16B is only +11.6% QoQ, against +19% QoQ in Q2. A sequential slowdown in percentage terms is built into guidance, which matters for the harness catalyst ("first visible deceleration"). Consensus at $2.18B already expects a beat. Combined with the flagged Q3 expense ramp, the set-up is "beat but decelerate QoQ," which the stock has punished before (Q1 2026: −6.93%).
- NDR rising to 157% while US commercial customers grew +35% says the growth is broad (both expansion and new logos), not just a few new mega-deals. This partly answers the red team's "few large contracts" pre-mortem.
- Harness check:
  - **Confirms** all harness Q2 figures: F153 revenue, F239–F244, F233–F238, F245 debt 0, F173 SBC.
  - **Updates** harness gaps: NDR 157%, US commercial customers 653, RPO $4.9B, total TCV $3.373B, the international split, government ~51% of revenue, the Q3 date and Q3 consensus. The Karp 18-month quote is now confirmed from the transcript (harness S43 was a secondary summary).
  - **Discrepancy:** harness F51 has deferred revenue at $579.4M for Q2. sec-api's 10-Q reading gives $613.2M, likely current plus non-current. The harness K5 (≥$600M) and Slater's falsification line (>$800M) depend on which definition is used, so they need re-basing against the 10-Q balance sheet.

### Gaps
- The total (company-wide) customer count was not disclosed in the Q2 materials I reviewed.
- I found no total RDV figure in primary sources ($13.1B appears only in secondary coverage).
- The $9.2B headline figure for cash plus short-term US Treasuries vs the ~$9.4B XBRL total (cash $2.03B plus marketable securities $7.38B) remains unreconciled in the release. It is plausibly non-Treasury marketable securities, but unverified.

## Q2. AIP and AI-agent commercialisation; large contracts

### Takeaway
The monetisation evidence from AIP is now quantitative and broad: US commercial up +149%, NDR 157%, top-20 customers averaging $124M TTM (+67%), and 73 deals ≥$10M in a single quarter. On the government side, structural lock-in strengthened: Maven was designated a program of record (memo 2026-03-09), there is a $10B, 10-year Army enterprise agreement (Aug 2025), and TITAN is in production. Many headline government values are **ceilings, not commitments**.

### Cited Findings
- **Top-20 customers:** trailing-12-month revenue averaged $124M per customer, +67% YoY — [Q2 call transcript](https://www.fool.com/earnings/call-transcripts/2026/08/10/palantir-pltr-q2-2026-earnings-call-transcript/). No single customer exceeded 10% of revenue — [sec-api.io 10-Q analysis](https://sec-api.io/insights/financial-analysis-of-palantir-technologies-the-quarter-to-30-june-2026-against-the-fy2025-record)
- **Sales model:** Goldman counts ~12 US commercial salespeople at the start of 2021 and ~80 by year-end, against ServiceNow's ~2,400 sales and marketing staff at a similar revenue scale. Goldman also notes that "the FDE lead has held even as rivals invested" — [TheStreet on Goldman's upgrade, 2026-10-10](https://www.thestreet.com/investing/stocks/pltr-palantir-technologies-stock-12-month-price-target-raised-by-18-percent-goldman-sachs-october-2026)
- **Sovereign AI positioning:**
  - CTO Shyam Sankar: "AIP is where your sovereign AI is built, deployed and compounded."
  - Palantir ran a "sovereign boot camp."
  - Sankar described a bake-off in which a frontier lab "failed to deliver anything of value."
  - Source: [Q2 call transcript](https://www.fool.com/earnings/call-transcripts/2026/08/10/palantir-pltr-q2-2026-earnings-call-transcript/)
- **New commercial and partner deals:**
  - Zeta is rebuilding its Data Cloud on Foundry in a 7-year deal targeting >$100M annual sales.
  - Nvidia expanded its partnership (2026-09-10).
  - Nebius named Palantir its preferred sovereign AI provider (2026-09-08).
  - Peter Zaffino joins as global head of financial services in January 2027.
  - Source: [TheStreet/Goldman, 2026-10-10](https://www.thestreet.com/investing/stocks/pltr-palantir-technologies-stock-12-month-price-target-raised-by-18-percent-goldman-sachs-october-2026)
- **Maven program of record:**
  - Deputy Secretary of Defense Steve Feinberg signed a memo (dated March 9; reported by Reuters on 2026-03-20) making Maven Smart System an official program of record.
  - Oversight moves from NGA to the CDAO within 30 days, and future contracting goes through the Army.
  - The memo promises "stable, long-term funding" but reportedly gives no dollar figure.
  - The Maven ceiling rose from $480M (2024) to $1.3B (May 2025).
  - Maven uses Anthropic's Claude, which the Pentagon had labelled a supply-chain risk. The report flags this as a possible complication.
  - Source: [Reuters via Yahoo](https://www.yahoo.com/news/articles/exclusive-pentagon-adopt-palantir-ai-232906085.html)
- Maven has "over 25,000 builders" across the Joint Force, and a government program of record chose Maven to run its program — Sankar, [Q2 call](https://www.fool.com/earnings/call-transcripts/2026/08/10/palantir-pltr-q2-2026-earnings-call-transcript/)
- **US Army enterprise agreement:** up to $10B over 10 years, announced 2025-08-01 — [CNBC, 2025-08-01](https://www.cnbc.com/2025/08/01/palantir-lands-10-billion-army-software-and-data-contract.html). **Older than 6 months.** It is a ceiling: "The Army's $10bn enterprise agreement and USDA's $300m award are ceilings, not commitments; most government contracts carry termination-for-convenience clauses" — [Rebound Capital, 2026-07-07](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr) (independent analyst substack)
- **TITAN:** in production, with eight systems to be delivered to the US Army (Palantir release, 2026-09-01; harness S31). Goldman cites TITAN production, the $10B EA and Maven as a program of record as government drivers — [TheStreet/Goldman](https://www.thestreet.com/investing/stocks/pltr-palantir-technologies-stock-12-month-price-target-raised-by-18-percent-goldman-sachs-october-2026)

### Inferences
- The red team's main pre-mortem ("demand fades, a few big contracts") is weakened but not refuted. NDR 157%, +35% customer growth and a 67% rise in top-20 spend point to broad expansion. The top-20 average of $124M × 20 ≈ $2.5B TTM, though, is roughly 40% of TTM revenue (derived, using ~$6.16B TTM from Q4), so concentration in large accounts is still material.
- Maven becoming a program of record converts a contract into a budget line item. That is a durable switching-cost mechanism the harness classed only as "claimed" moat evidence. It supports moat durability on the government side but does not quantify revenue.

### Gaps
- No primary disclosure of AIP-specific revenue, bootcamp counts or conversion rates for 2026.
- No 2026 NATO (Maven Smart System NATO) contract value update found in this pass.
- Obligated vs ceiling amounts under the Army EA were not found.

## Q3. Government dependence and political/budget risk

### Takeaway
Government is still ~51% of revenue (down from 54% in FY2025). US government is growing +90% and Pentagon revenue is tiny relative to the defence budget. That is upside, but also political concentration. The live risks in 2026 are European sovereignty pushback (France's DGSI exit, the UK NHS break clause in Feb 2027, exclusion by Germany's military), mid-term-election scrutiny and termination-for-convenience clauses. I found no 2026 evidence of DOGE-driven cuts hurting Palantir.

### Cited Findings
- Government ≈ 51.2% of Q2 2026 revenue (FY2025: 54%) — [sec-api.io 10-Q analysis](https://sec-api.io/insights/financial-analysis-of-palantir-technologies-the-quarter-to-30-june-2026-against-the-fy2025-record)
- "Our Department of War trailing 12-month revenue is still less than 25 basis points of the Pentagon's budget" — Sankar, [Q2 call](https://www.fool.com/earnings/call-transcripts/2026/08/10/palantir-pltr-q2-2026-earnings-call-transcript/). A bull case cites a proposed FY2027 DoW AI budget request of $58.5B — [24/7 Wall St., 2026-10-14](https://247wallst.com/investing/2026/10/14/palantirs-earnings-gamble-nine-straight-beats-set-high-bar-for-november-2/) (secondary; not verified against the budget documents)
- The 10-Q risk factors say large government customers face "uncertainties over budgets and spending levels," with wording unchanged across three filings. DOGE and government shutdowns are not mentioned. The most rewritten risk passages cover external scrutiny of the company and its leadership, the rising US share of revenue, and AI and privacy regulation — [sec-api.io 10-Q analysis](https://sec-api.io/insights/financial-analysis-of-palantir-technologies-the-quarter-to-30-june-2026-against-the-fy2025-record)
- **France:** on 2026-06-16, PM Sébastien Lecornu announced that the DGSI will drop Palantir for domestic ChapsVision ("cannot accept new strategic dependencies"). Palantir had renewed the three-year DGSI contract in Dec 2025, and migration will take several years. PLTR fell 6.98% to $119.50 on 2026-06-22 — [TIKR, 2026-06-23](https://www.tikr.com/blog/palantir-stock-fell-7-as-france-drops-its-software-is-the-sovereignty-threat-real-or-a-buying-opportunity)
- **UK:** a parliamentary committee urged ministers to exit the £330M NHS contract via a February 2027 break clause, calling Palantir an "unacceptable point of weakness." Palantir UK cites >110,000 additional NHS procedures — [TIKR, 2026-06-23](https://www.tikr.com/blog/palantir-stock-fell-7-as-france-drops-its-software-is-the-sovereignty-threat-real-or-a-buying-opportunity)
- **Wider Europe:** international commercial grew only ~2% in FY2025. Swiss agencies rejected Palantir at least nine times in seven years, and Germany's military excluded it — [Rebound Capital, 2026-07-07](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr) (secondary)
- **Sell-side international concerns:** RBC's Rishi Jaluria flagged slowing international revenue (Underperform, $90). Jefferies cited "slowing international growth" — [Barchart/Yahoo, 2026-08-12](https://finance.yahoo.com/markets/stocks/articles/jefferies-latest-warning-palantir-sends-133832548.html)
- **Political scrutiny:** speculation about mid-term-election scrutiny of government tech contractors circulated around the 2026-10-16 selloff, but the article says it "did not demonstrably cause" the decline — [FinanceFeeds, 2026-10-16](https://financefeeds.com/palantir-stock-closes-below-190-down-13-from-its-record-what-the-selloff-is-pricing-in/). Goldman lists "Congressional changes that could shift government contract win rates" as a risk — [TheStreet/Goldman](https://www.thestreet.com/investing/stocks/pltr-palantir-technologies-stock-12-month-price-target-raised-by-18-percent-goldman-sachs-october-2026)
- **Ethics and vendor risk on Maven:** UN expert panels have raised concerns about AI targeting. The Maven reporting cites use in "thousands of targeted strikes against Iran" and the Anthropic supply-chain-risk dispute — [Reuters via Yahoo](https://www.yahoo.com/news/articles/exclusive-pentagon-adopt-palantir-ai-232906085.html)

### Inferences
- The red team gave 15% to "government/policy concentration." The evidence now splits that risk. US defence is strengthening (program of record, budget headroom). International government sovereignty is deteriorating (France, UK, Germany), even though international government still grew +42% YoY in Q2. The asymmetric political risk is a US administration or Congress change after the Nov 2026 mid-terms, given how closely the company is associated with the current administration. That is inference; I found no hard evidence.
- Sovereignty pushback in Europe directly contradicts the company's "sovereign AI" pitch abroad. Expect international commercial to stay a laggard; it was +2% QoQ in Q2.

### Gaps
- No 2026 primary reporting on DOGE effects. No FY2027 appropriations figures specific to Palantir programs. The harness S27 item ("sovereign AI external guardrail," 2026-09-28) could not be substantiated in this pass.

## Q4. Competition

### Takeaway
Competitive intensity rose sharply in mid-2026. Hyperscalers and frontier labs are now copying Palantir's forward-deployed-engineer model with large dollar commitments, and Databricks and Snowflake are building ontology and semantic layers. So far there is no evidence in the reported numbers of lost share: US commercial grew +149% and NDR is 157%. In defence, classified-network accreditation remains a multi-year barrier to entry.

### Cited Findings
- **Hyperscalers and labs copying the FDE model:** AWS committed $1B to forward-deployed engineering (2026-06-30). Microsoft committed $2.5B and 6,000 engineers (2026-07-02). Anthropic and OpenAI launched deployment ventures in May 2026, and OpenAI reportedly guaranteed investors in its deployment company a 17.5% annual return (Axios, as cited) — [Rebound Capital, 2026-07-07](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr) (secondary substack; individual items not independently verified)
- **Data platforms:** Databricks launched "Genie Ontology" at its June 2026 summit, which the author reads as aimed at Palantir's semantic layer. Snowflake is building a similar governed, AI-ready data layer — [Rebound Capital](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr)
- **Counter-argument:** AWS CloudWatch, DocumentDB and Redshift competed with Datadog, MongoDB and Snowflake, and all three incumbents thrived — [Rebound Capital](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr)
- **Defence moat:** classified-network accreditation is a multi-year barrier for new entrants — [Rebound Capital](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr)
- **Pricing risk:** AIP model resale and rivals' deployment offerings could force lower pricing on add-on revenue — [Rebound Capital](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr)
- **Goldman's risk list:** competitors replicating the FDE approach, and slower enterprise AI adoption if returns prove hard to scale — [TheStreet/Goldman, 2026-10-10](https://www.thestreet.com/investing/stocks/pltr-palantir-technologies-stock-12-month-price-target-raised-by-18-percent-goldman-sachs-october-2026)
- **Management:** no competitors were named on the Q2 call. Sankar: "The others are focused on productivity" — [Q2 call](https://www.fool.com/earnings/call-transcripts/2026/08/10/palantir-pltr-q2-2026-earnings-call-transcript/)
- **Peer valuations (2026-10-14):** Snowflake 169x forward P/E, Microsoft 25x — [24/7 Wall St.](https://247wallst.com/investing/2026/10/14/palantirs-earnings-gamble-nine-straight-beats-set-high-bar-for-november-2/). Accenture ~11x P/E — [Rebound Capital](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr)
- **Sector sensitivity:** on 2026-10-16, Palantir and ServiceNow each fell ~5% and Salesforce ~4% on worries about AI financing — [24/7 Wall St., 2026-10-16](https://247wallst.com/investing/2026/10/16/enterprise-software-stocks-fall-as-ai-financing-worries-spread-palantir-and-servicenow-drop-5-salesforce-slides-4/) (headline only)

### Inferences
- The competitive threat is the bear case's most plausible *mechanism* for pressure on long-run margin and growth. Hyperscalers spending billions on FDE capacity suggests the market for "AI deployment" is real, which validates Palantir's model, and also that it will commoditise toward services economics over 5–10 years. This argues for the harness's multiple-compression pre-mortem rather than against it.
- Harness check: the harness said competitive intensity "was not confirmed by the evidence." **Updated:** there is now specific, dated evidence of competitive investment (Jun–Jul 2026), but no evidence yet of share loss in Palantir's KPIs.

### Gaps
- No primary or tier-1 (Reuters, Bloomberg, The Information) reporting found on specific deal losses to Databricks, Snowflake, Microsoft Fabric, ServiceNow or C3.ai.
- Anduril was not covered in sources retrieved this pass. Anduril and Palantir have historically partnered (e.g., consortium bids), but this is unsourced here.

## Q5. Financial quality: SBC, dilution, buybacks, cash, tax

### Takeaway
Quality is high on cash conversion. Dilution has flattened recently: basic shares are ~2.403B and diluted shares have been flat at ~2.57B for four quarters. SBC is falling as a share of revenue (13.7% in Q2 2026) but rising in dollars. The **$1B buyback was terminated in January 2026, so no repurchase authorization remains.** The effective tax rate is 1.4%, which is a normalisation risk for GAAP EPS.

### Cited Findings
- **SBC:** $265.2M in Q2 2026 (13.7% of revenue), vs $201.6M in Q1 2026 and $160.0M in Q2 2025. H1 2026 was $466.8M (13.1%); FY2025 was $684.0M (15.3%) — [sec-api.io 10-Q analysis](https://sec-api.io/insights/financial-analysis-of-palantir-technologies-the-quarter-to-30-june-2026-against-the-fy2025-record); [Q2 press release](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- The gap between GAAP and adjusted operating income ($282.5M) is SBC of $265.2M plus $17.3M of employer payroll tax, equal to 23.6% of adjusted operating profit — [GuruFocus via Yahoo, 2026-10-16](https://finance.yahoo.com/markets/stocks/articles/palantir-stocks-fall-6-6-203109076.html)
- **Shares outstanding** at 2026-06-30: Class A 2,300.5M, Class B 101.4M, Class F 1.005M; 2,403.1M in total as of 2026-07-27 (10-Q cover) — [sec-api.io 10-Q analysis](https://sec-api.io/insights/financial-analysis-of-palantir-technologies-the-quarter-to-30-june-2026-against-the-fy2025-record). Diluted weighted shares were ~2.569B in Q2 2026 (harness F61, from the 10-Q XBRL).
- **Buybacks:** the $1.0B repurchase program was **terminated in January 2026**, and no authorization remains. FY2025 repurchases were 0.6M Class A shares for $75.0M. No 2026 repurchases are reported. The risk factor about the program was removed — [sec-api.io 10-Q analysis](https://sec-api.io/insights/financial-analysis-of-palantir-technologies-the-quarter-to-30-june-2026-against-the-fy2025-record)
- **Effective tax rate:** 1.4% in Q2 2026 (provision $15.4M), in Q1 2026 and in FY2025 — [sec-api.io 10-Q analysis](https://sec-api.io/insights/financial-analysis-of-palantir-technologies-the-quarter-to-30-june-2026-against-the-fy2025-record); also reported by Al Jazeera on 2026-08-06 (harness source S20; I did not re-fetch it)
- **Receivables concentration:** AR was $1,485.2M at 2026-06-30, and **one customer accounted for 27% of accounts receivable** — [sec-api.io 10-Q analysis](https://sec-api.io/insights/financial-analysis-of-palantir-technologies-the-quarter-to-30-june-2026-against-the-fy2025-record)
- **Cash:** cash, equivalents and short-term US Treasuries $9.2B (headline). Balance-sheet cash $2,030.0M plus marketable securities $7,379.1M ≈ $9.4B. Debt is zero — [Q2 press release](https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm)
- **Historic SPAC losses:** Palantir invested $405.5M in SPACs in 2021 (per RBC), and about $300M of losses were reportedly booked in 2022 — [Rebound Capital](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr) (older capital-allocation blemish; >6 months old)
- **Cost classification:** the author argues adjusted gross margin of ~88% and adjusted operating margin of ~60% "are flattered by cost classification" — [Rebound Capital](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr) (opinion)

### Inferences
- Derived: Q2 adjusted FCF of $1.22B less SBC of $0.265B ≈ $0.955B, an SBC-adjusted FCF margin of ~49%. That is far above the harness's FY2025 figure of 31.7%, so on current-run-rate numbers the harness's 52% FCF margin assumption looks attainable rather than optimistic (contrary to red-team weakest[2]). Part of Q2 FCF may be timing, given customer deposits of $452.6M, so one quarter is not proof.
- With the buyback terminated, nothing offsets SBC issuance. Diluted shares look flat recently (~2.57B for four quarters) partly because the diluted count already includes in-the-money awards. Ongoing net dilution of roughly 0.5–1% a year is plausible, but that is my inference, not a sourced figure.
- One customer holding 27% of AR is most likely a US government entity, which makes the harness's receivables-gap flag look like billing timing on a large government contract rather than demand deterioration. That is inference; the 10-Q does not name the customer.
- Harness check:
  - **Confirms** the 1.4% tax rate (now from a 10-Q-based analysis, not just the Al Jazeera report).
  - **Updates** Ackman's "capital return policy" manual check: there is no buyback authorization at all.
  - **Updates** "shares outstanding" (a harness gap): 2.403B basic.

### Gaps
- The 10-Q original was not opened directly (sec-api is a secondary reading of the filing). Primary verification of the buyback termination, the 27% AR customer and RPO is advisable.
- No deferred-tax-asset or NOL schedule was retrieved to estimate when the tax rate normalises.

## Q6. Valuation, price history and drawdowns

### Takeaway
At **$186.03 (close on 2026-10-16)** PLTR trades at roughly **54–57x EV / FY2026 revenue guidance, ~95–100x EV / FY2026 adjusted FCF guidance, ~76–100x forward P/E, and ~41x Goldman's 2029 GAAP EPS.** It is 12.6% below the record intraday high of $212.94 (2026-10-12) and ~75% above the late-June 2026 low of ~$106. The stock has shown repeated ~40–50% drawdowns even while fundamentals accelerated.

### Cited Findings
- **Recent prices:**
  - 2026-10-16 close $186.03 (−7.22% on the day, −11.01% on the week; intraday low $184.45). The record intraday high was $212.94 on 2026-10-12. The selloff came with a Nasdaq drop of 4.5% that week and AI-infrastructure financing worries; there was no company-specific deterioration — [FinanceFeeds, 2026-10-16](https://financefeeds.com/palantir-stock-closes-below-190-down-13-from-its-record-what-the-selloff-is-pricing-in/)
  - $207.40 around 2026-10-13/14; 52-week high $212.94, 52-week low $106.37 — [24/7 Wall St., 2026-10-14](https://247wallst.com/investing/2026/10/14/palantirs-earnings-gamble-nine-straight-beats-set-high-bar-for-november-2/)
  - 2026-10-01 close $190.04 (+6.91% YTD). H1 2026: −34.36%. Q3 2026: +60.32% — [TIKR via Yahoo, 2026-10-02](https://finance.yahoo.com/markets/stocks/articles/palantir-stock-rose-60-q3-151806420.html)
- **2025–26 drawdown:** the peak was $207.52 in November 2025. The drawdown reached 42.3% by 2026-06-22 (close $119.50) — [TIKR, 2026-06-23](https://www.tikr.com/blog/palantir-stock-fell-7-as-france-drops-its-software-is-the-sovereignty-threat-real-or-a-buying-opportunity). It reached 48.22% by 2026-06-25 — [TIKR via Yahoo, 2026-10-02](https://finance.yahoo.com/markets/stocks/articles/palantir-stock-rose-60-q3-151806420.html). The trough was ~$106 in late June 2026 — [Rebound Capital](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr)
  - Drivers cited: valuation discrimination in AI stocks and fear that "AI adoption had peaked" — [Motley Fool via Yahoo, 2026-07-09](https://finance.yahoo.com/markets/stocks/articles/why-palantir-stock-plunged-34-071500679.html). Also the Q1 post-earnings drop of −6.93% (2026-05-04) and France's DGSI exit (June 2026) — [TIKR, 2026-06-23](https://www.tikr.com/blog/palantir-stock-fell-7-as-france-drops-its-software-is-the-sovereignty-threat-real-or-a-buying-opportunity)
- **Other dated levels:** $171 on 2026-08-12 — [Barchart/Yahoo](https://finance.yahoo.com/markets/stocks/articles/jefferies-latest-warning-palantir-sends-133832548.html). $194.12 at Goldman's upgrade (2026-10-08) — [TheStreet](https://www.thestreet.com/investing/stocks/pltr-palantir-technologies-stock-12-month-price-target-raised-by-18-percent-goldman-sachs-october-2026)
- **Multiples:**
  - NTM normalized P/E ~100x as of 2026-10-01, down from ~192x at end-2025 — [TIKR via Yahoo](https://finance.yahoo.com/markets/stocks/articles/palantir-stock-rose-60-q3-151806420.html)
  - Forward P/E 85x (90x in the infographic), P/S 81.6x and P/FCF 228.9x, all at ~$207 (2026-10-14) — [24/7 Wall St.](https://247wallst.com/investing/2026/10/14/palantirs-earnings-gamble-nine-straight-beats-set-high-bar-for-november-2/) (the trailing basis of P/S and P/FCF is unclear)
  - Forward GAAP P/E >200x at the Nov 2025 peak and ~80x in July 2026 — [Rebound Capital](https://reboundcapital.substack.com/p/deep-dive-palantir-pltr)
  - P/E 149x and PEG 0.52 as of July 2026 — [Motley Fool via Yahoo, 2026-07-09](https://finance.yahoo.com/markets/stocks/articles/why-palantir-stock-plunged-34-071500679.html)
- Goldman says PLTR trades at a discount to growth peers on EV/FCF; no number is given — [TheStreet/Goldman](https://www.thestreet.com/investing/stocks/pltr-palantir-technologies-stock-12-month-price-target-raised-by-18-percent-goldman-sachs-october-2026)

### Inferences (derived at $186.03, using the share counts and cash above)
- Market cap ≈ $447B on 2.403B basic shares, or ≈ $478B on 2.569B diluted shares. EV ≈ $438–469B after ~$9.2–9.4B of net cash.
- EV / TTM revenue: TTM revenue (Q3'25 to Q2'26) is ≈ $6.16B, using Q3'25 $1.18B, Q4'25 ~$1.41B, Q1'26 $1.633B and Q2'26 $1.935B. The Q3'25 figure comes from the prior-year 10-Q and the Q4'25 figure is backed out of FY2025 at ~$4.48B, so treat TTM as approximate. That gives **~71–76x**.
- EV / FY2026 revenue guidance of $8.15B: **~54–57x**. EV / consensus 2027 revenue of ~$12.3B: **~36–38x**. EV / Goldman 2027 of $13.2B: **~33–35x**.
- EV / FY2026 adjusted FCF guidance of $4.6B: **~95–102x**. The harness's P/FCF of 142x and FCF yield of 0.7% are consistent with a TTM FCF of ~$3.3–3.4B, so they are **confirmed** as a TTM measure. On a forward basis the FCF yield is ~1.0%.
- Price / Goldman 2029 GAAP EPS of $4.50 ≈ **41x**. Goldman's own target applies 60x to that figure, discounted at ~13.5%.
- **Harness check, important:** the harness base path (FY26 $8.15B, FY27 ~$12.2B, FY28 ~$16.5B, FY29 ~$20.8B, FY30 ~$24.9B) is **roughly equal to sell-side consensus for 2026–27** (~$8.2B and ~$12.3B). It is **well below Goldman's** forecast ($13.2B in 2027 and $25.75B in 2029, a year earlier than the harness's FY30 figure). So the harness's negative IRR comes mainly from its **exit multiple (35x P/FCF) and discount rate**, not from below-consensus growth. The disagreement with the market is about terminal multiple and duration, which supports the red team's "multiple collapse" framing. The harness's own falsification line (Ackman: price <$110) is ~5–10% below the June 2026 trough. The stock traded there only four months ago, which shows the harness's buy level is reachable in normal volatility.

### Gaps
- No tier-1 (Bloomberg, Reuters) data on EV/sales and EV/FCF; the multiples above are my derivations or come from secondary aggregators with unclear bases.
- I did not retrieve sourced data on the 2021–2022 drawdown (from the early-2021 peak to the late-2022 trough) in this pass. It belongs in the drawdown history but must be sourced separately.

## Q7. Consensus estimates, price targets, and sell-side bull and bear cases

### Takeaway
The sell-side is mostly positive but split on price. As of mid-October the mean target is ~$196–205 (+5–10% vs $186). The range runs from **$80 (Jefferies, Underperform) to $265 (Barclays, Overweight)**. Four target raises came in the week of 2026-10-08 to 10-15. Bears are arguing price, not business quality.

### Cited Findings
- **Consensus revenue (TIKR, 2026-10-02):** 2026 ≈ $8.2B (up from ~$6.3B at 2025-12-31, ~31% higher); 2027 ≈ $12.3B (up from ~$8.7B). NTM EPS ≈ $1.90 (from ~$0.93). Coverage 23–29 analysts; ratings 19 Buy, 1 Outperform, 9 Hold, 1 Underperform, 1 Sell. Mean target ~$196 and high $255 as of 2026-10-01 — [TIKR via Yahoo](https://finance.yahoo.com/markets/stocks/articles/palantir-stock-rose-60-q3-151806420.html)
- **Average target over time:**
  - $198.41 across 29 analysts on 2026-08-12 (21 Strong Buy, 6 Hold, 1 Moderate Sell, 1 Strong Sell) — [Barchart/Yahoo](https://finance.yahoo.com/markets/stocks/articles/jefferies-latest-warning-palantir-sends-133832548.html)
  - $205.27 on 2026-10-14 — [24/7 Wall St.](https://247wallst.com/investing/2026/10/14/palantirs-earnings-gamble-nine-straight-beats-set-high-bar-for-november-2/)
- **Target changes in October 2026:**
  - **Goldman Sachs** (Gabriela Borges), 2026-10-08: upgraded Neutral → Buy, target $204 → $230 — [FinanceFeeds](https://financefeeds.com/palantir-stock-closes-below-190-down-13-from-its-record-what-the-selloff-is-pricing-in/); [TheStreet](https://www.thestreet.com/investing/stocks/pltr-palantir-technologies-stock-12-month-price-target-raised-by-18-percent-goldman-sachs-october-2026)
    - Thesis: "Moat likely compounds into another step function change in TAM."
    - Basis: 60x 2029 GAAP EPS of $4.50, discounted ~13.5%.
    - Revenue estimates: $8.37B (2026), $13.2B (2027), $25.75B (2029).
  - **Barclays** (Anthony Valentini), 2026-10-08: initiated at Overweight, $265 target — [FinanceFeeds](https://financefeeds.com/palantir-stock-closes-below-190-down-13-from-its-record-what-the-selloff-is-pricing-in/)
  - **Baird**, 2026-10-13: target $200 → $250 — [FinanceFeeds](https://financefeeds.com/palantir-stock-closes-below-190-down-13-from-its-record-what-the-selloff-is-pricing-in/)
  - **Mizuho** (Gregg Moskowitz), 2026-10-15: Outperform, target $215 → $245 — [GuruFocus via Yahoo, 2026-10-16](https://finance.yahoo.com/markets/stocks/articles/palantir-stocks-fall-6-6-203109076.html)
- **Bears:**
  - **Jefferies** (Brent Thill), 2026-08-12: Underperform, target $70 → $80. "We are fundamental fans of PLTR, but valuation leaves little room for a normalization in growth or execution slippage." Jefferies also cited tougher comparisons and slowing international growth — [Barchart/Yahoo](https://finance.yahoo.com/markets/stocks/articles/jefferies-latest-warning-palantir-sends-133832548.html)
  - **RBC** (Rishi Jaluria): Underperform, $90 target, citing slowing international revenue — [Barchart/Yahoo, 2026-08-12](https://finance.yahoo.com/markets/stocks/articles/jefferies-latest-warning-palantir-sends-133832548.html)
- **Independent scenario framing** (24/7 Wall St., 2026-10-14):
  - Base: $213.38 (Hold).
  - Bull: $266.93 at 110x forward EPS.
  - Bear: $133.46 at 55x forward EPS (multiple contraction, SBC, international +26%, termination for convenience).
  - Source: [24/7 Wall St.](https://247wallst.com/investing/2026/10/14/palantirs-earnings-gamble-nine-straight-beats-set-high-bar-for-november-2/)

### Inferences
- Even the bearish sell-side targets ($80–90) sit below the harness's probability-weighted IV ($112), while the harness's bear-case IV ($38.60) is far below any published target. The harness's base IV ($110.56) sits between the bear targets and the 24/7 bear case ($133). **So the harness is more bearish than ~90% of the Street, but within the range of published bears.**
- Mean targets are only ~5–10% above the price, even among mostly Buy-rated analysts. That suggests the Street also sees limited 12-month upside at $186. The upside debate depends on duration beyond 2027 (Goldman's 2029 framework).

### Gaps
- No Bloomberg or FactSet consensus snapshot; the figures come from TIKR, Barchart and 24/7 aggregations with slightly different panels.
- No FY2028+ consensus beyond Goldman's single-broker estimates.
- Morgan Stanley's rating and target were not retrieved. The Aug 2026 article notes only Sanjit Singh's comment on accelerating growth.

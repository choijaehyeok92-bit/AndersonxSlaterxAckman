# Samsara (NYSE: IOT): fact base for a 5–10 year holding (as of 2026-10-18)

Fiscal calendar: FY ends on the Saturday nearest Jan 31. FY2027 Q2 = quarter ended 2026-08-01, reported 2026-09-03. All $ figures are USD. "Harness" means the internal research at `/home/claude/choijaehyeok92-bit/andersonxslaterxackman/research/IOT/` (report.md, redteam.json, evidence.json). F-numbers refer to its facts.

## 0. Harness reconciliation (read first)

### Takeaway
My research confirms the harness's operating facts for Q2 FY27. It corrects four things the debate leaned on: (1) **net cash and EV are wrong** (cash and investments are about $1.33B, not $0.29B); (2) **the deferred-revenue "thesis break" that was marked as tripped is a false positive**; (3) **the NRR fact is a management *target* of "approximately 115%" for core customers, not a reported "≥115%"**; and (4) **the FY27 "consensus" of $1.97B is stale and sits below the company's own guidance**, so the "+3.9% vs consensus" variant does not exist.

### Cited Findings
- **CONFIRMED.** Q2 FY27 ARR was $2,124.7M (+30% YoY) and net new ARR was $134.1M (+28%). These match F209 and F210 — [Q2 FY27 press release, 2026-09-03](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- **CONFIRMED.** There were 3,605 customers above $100K ARR, with a record 242 net adds. ARR from $100K+ customers was $1.3B (+38%). There were 210 customers above $1M ARR, with a record 20 net adds. These match F211, F212, F229 and F230 — [Q2 FY27 call transcript, 2026-09-03](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)
- **CONFIRMED.** Guidance is: FY27 revenue $2.043–2.047B, Q3 revenue $514–516M, FY27 non-GAAP operating margin 21%. These match F213, F214 and F215 — [Q2 press release](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- **CONFIRMED, with verbatim wording.** The FCF margin cut (S50). CFO Dominic Phillips: "We now expect free cash flow margin to be approximately 100 basis points lower than FY '26." He gave three reasons: more IoT devices for stronger growth, pre-buying inventory as a buffer, and higher 2H supply-chain costs. He added "we expect this to be temporary." — [Q2 call transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)
- **UPDATE: this is a reversal the harness missed.** One quarter earlier the guide pointed the other way. The Q1 FY27 shareholder letter (2026-06-04) said: "We expect adjusted free cash flow margin for full-year FY27 to improve 100 bps year-over-year." That is a ~200bp swing in the FY27 FCF outlook within one quarter — [Q1 FY27 Shareholder Letter](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf)
- **UPDATE on F231 (NRR).** The CFO's exact wording on the Q2 call was "our target dollar-based net retention rate of approximately 115% for core customers". He said multiproduct adoption "helped us achieve" it. The Q1 letter uses the same framing: "our FY27 target dollar-based net retention rate of approximately 115% for core customers". It defines core customers as ARR ≥ $25,000. Neither source gives a prior-quarter actual NRR, so no trend can be built. The Q1 FY27 investor deck gives only the definition, with no historical rates — [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey); [Q1 letter](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf); [Q1 FY27 investor presentation](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf)
- **CONTRADICTS the harness net cash and EV (2.9억 USD and 230.7억 USD).** At 2026-08-01 the balance sheet held $291.4M cash and equivalents, $537.5M short-term investments and $496.8M long-term investments, about **$1,325.7M** in total. No debt line appears. The harness's $0.29B is cash and equivalents only — [10-Q for quarter ended 2026-08-01](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm); [Q2 press release](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- **CONTRADICTS the red-team break "이연매출 < 7.3억 → 충족—훼손".** The threshold was $730M, but F50 (Q2 FY27 deferred revenue) is $728.9M, the same quarter. The condition was "met" only because 7.289억 rounds up to 7.3억. Deferred revenue has not declined: it rose from $679.3M (FY26 year-end) to $703.9M (Q1) to $728.9M (Q2), per harness F48–F50 from SEC XBRL.
- **CONTRADICTS the use of F216 as consensus.** TickFlow still showed FY27 revenue consensus of $1.97B (16 analysts) on 2026-10-17. That is below company guidance of $2.043–2.047B, so the page is stale. Its "FY2028" row ($634M) appears to be a single quarter — [TickFlow, data date 2026-10-17](https://tickflow.io/stock/IOT/forecast). The "variant perception: +3.9% vs consensus" line in report.md is an artifact of stale data.

### Inferences
- With EV corrected to about $21.9–22.0B, the reverse DCF hurdle falls slightly. EV/revenue moves from 12.5x to about 11.9x TTM. Net cash per share is about $2.26, not $0.49. Ackman's intrinsic value and MOS change only marginally (about +$1.75/share), so the vote does not hinge on this, but the inputs should be fixed.
- The deferred-revenue break should be re-specified, for example as YoY growth below revenue growth, or a sequential decline from the $728.9M level.

### Gaps
- No primary source gives a numeric NRR history (FY25 and FY26 actuals). Without it, the red-team trigger `nrr < 1.15` cannot be tested by machine.

## 1. Latest quarter (Q2 FY27), guidance path, and next report

### Takeaway
Q2 FY27 was a clean beat and raise: revenue $508.4M (+30%), ARR +30%, non-GAAP operating margin 21%. FY27 revenue guidance has now been raised twice, from 21–22% growth to 26%. Two things argue against reading it as acceleration: Q3 is guided to +24%, and the FY27 FCF margin guide went from +100bp to −100bp.

### Cited Findings
- Q2 FY27 revenue was $508.4M, +30% YoY (+29% constant currency). H1 revenue was $987.3M, +30% — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- Revenue beat consensus of $483.26M, and EPS of $0.20 beat consensus of $0.16. Shares rose about 4% to $40.29 the next day (2026-09-04) — [iTiger/Benzinga recap, 2026-09-04](https://www.itiger.com/news/2664435814)
- Gross margin was 77% GAAP and 78% non-GAAP, both flat YoY. The Q1 FY27 deck shows non-GAAP gross margin of 79% in Q1 FY26 against 76% in Q1 FY27. The Q1 letter says COGS rose 2 points "to support AI-related investments" — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf); [Q1 deck](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf); [Q1 letter](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf)
- GAAP operating income was $4.9M (1% margin), against a loss of $26.6M (−7%) a year earlier. Non-GAAP operating income was $106.0M (21%), against $59.7M (15%). This was the fourth consecutive quarter of GAAP profitability — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- Net income was $16.2M and GAAP EPS $0.03; non-GAAP EPS was $0.20. H1 included a $30.3M arbitration gain against Motive Technologies, which is excluded from non-GAAP — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
  - Implication for the harness: Q1 FY27 GAAP net income of $44.5M (F109) is inflated by this one-off.
- Operating cash flow was $73.5M (14% margin) and FCF $64.7M (13% margin). H1 FCF was $137.9M (14%) — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- Remaining performance obligations were $4,285.2M, about 43% ($1,838.9M) due within 12 months. No customer was ≥10% of revenue or receivables — [10-Q, Q2 FY27](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm)
- Trailing-12-month net new ARR was $485M, +27% constant currency — [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)
- Q1 FY27 (reported 2026-06-04):
  - ARR was about $2.0B (+30%) and net new ARR $101M (+30%, +27% cc).
  - There were 3,363 customers above $100K ARR (+169 in the quarter) and 190 above $1M (+15).
  - The $100K+ customer count over five quarters was 2,638 → 2,771 → 2,990 → 3,194 → 3,363 (Q1 FY26 to Q1 FY27).
  - [Q1 letter](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf); [Q1 deck](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf)
- Q4 FY26 (reported 2026-03-05): revenue $444.3M (+28%), ARR $1,889.9M (+30%), net new ARR $144.8M (+33%). FY26 revenue was $1,618.6M (+30%), FCF $207.4M (13%) and GAAP operating margin −3% — [Q4 FY26 PR](https://s29.q4cdn.com/853855404/files/doc_financials/2026/q4/Q4-2026-Earnings-Press-Release-FINAL.pdf)

FY27 guidance path:

| Date | FY27 revenue | Growth | Non-GAAP op. margin | Non-GAAP EPS | FCF margin comment |
|---|---|---|---|---|---|
| 2026-03-05 | $1.965–1.975B | 21–22% | 19% | $0.65–0.69 | — |
| 2026-06-04 | $2.005–2.013B | 24% | 20% | $0.70–0.72 | "improve 100 bps YoY" (adjusted FCF) |
| 2026-09-03 | $2.043–2.047B | 26% | 21% | $0.76–0.78 | "~100 bp lower than FY26" |

Sources for the table: [Q4 PR](https://s29.q4cdn.com/853855404/files/doc_financials/2026/q4/Q4-2026-Earnings-Press-Release-FINAL.pdf), [Q1 letter](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf), [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf), [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)

- Q3 FY27 guidance: revenue $514–516M (+24%, +23–24% cc), non-GAAP operating margin 21%, non-GAAP EPS $0.18–0.19, GAAP profitable — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)

### Inferences
- Management has opened the year with a conservative guide and beaten it by a wide margin. The initial FY27 guide was raised about $78M (4%) within two quarters, which supports the harness K1 and K2 expectations.
- Implied H2 FY27 revenue is about $1.057B. With Q3 at about $515M, Q4 is about $542M, roughly +22% YoY on $444.3M. Revenue growth is therefore guided to decelerate from 30% to the low 20s in H2. Part of this is Samsara's usual conservatism.
- The FCF reversal is mostly a working-capital choice (inventory pre-buy). Rising component and shipping costs, however, are a gross-margin headwind that the CFO says will "come gradually as costs amortize into COGS."

### Gaps
- **The Q3 FY27 report date has not been announced** in any source I found. Last year's Q3 was reported 2025-12-04 ([Samsara PR](https://www.samsara.com/company/news/press-releases/samsara-to-announce-Q3-FY26-financial-results-on-december-4)), which suggests early December 2026. That is an estimate.
- I found no Q2-level breakdown of ARR by product (video safety, telematics, emerging) and no RPO growth rate.

## 2. SBC, dilution and capital allocation

### Takeaway
SBC is falling as a share of revenue: about 27% in FY24, 22% in FY26, 18% TTM. It is still larger than FCF, so FCF after SBC remains negative (about −$75M TTM). Diluted shares grow about 3.3–3.5% a year. There is **no buyback**, and insiders sold about $107M of stock in the three months to mid-October 2026.

### Cited Findings
- SBC (cash-flow statement) was $96.4M in Q2 FY27, up from $81.1M a year earlier. Total SBC-related charges were $101.1M against $86.3M. H1 charges were $184.9M against $170.6M — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- From the reconciliation tables, SBC as a share of revenue was about 27% in FY24, 24% in FY25 and 21% in FY26. It was about 23% in Q1 FY26 and about 17% in Q1 FY27 — [Q1 FY27 deck](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf)
- The harness calculation differs: it puts FY26 SBC/revenue at 19.5% on a GAAP cash-flow basis, which is a different measure.
- My computation from harness XBRL quarterly facts:
  - SBC/revenue was 18.7% in Q3 FY26, 17.8% in Q4 FY26, 16.2% in Q1 FY27 and **19.0% in Q2 FY27**.
  - TTM SBC is $330.6M (17.9% of TTM revenue of $1,847.6M).
  - TTM FCF is $255.5M (13.8%), so TTM FCF minus SBC is about −$75M.
  - Inputs are harness F-facts sourced from SEC 10-Q/10-K filings: revenue F156/F157/F205, operating cash flow F117/F223/F224/F228, capex F10/F220/F221/F227, SBC F176/F177/F207.
- Diluted weighted shares were 534.9M (FY24), 556.3M (FY25) and 573.5M (FY26); 567.7M in Q1 FY26 and 587.7M in Q1 FY27 (+3.5%) — [Q1 deck](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf)
- Q2 FY27 diluted weighted shares were 590.5M, +3.3% from 571.7M in Q2 FY26 (harness F60). Management expects FY27 diluted weighted shares of about 594M — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf); [Q1 letter](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf)
- Shares outstanding on 2026-09-01 were 380,273,036 Class A plus 205,332,173 Class B, **585.6M in total**. The Class B shares (high-vote, founder control) are about 35% of the total — [10-Q cover](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm)
- **No share repurchase** program appears in the Q2 press release, the Q1 letter or the 10-Q excerpt. The $36.0M paid in Q2 was taxes on net share settlement, which is not a buyback. H1 issuance was 6.69M shares, with 2.12M withheld for $70.4M in taxes — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf); [10-Q](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm)
- Insiders sold about $107.38M and bought none in the three months to 2026-10-16. Recorded sales include the CAO and others in late September and mid-October. Insiders own 35.13% and institutions 96.02% (aggregator figures) — [MarketBeat, page data as of 2026-10-16](https://www.marketbeat.com/instant-alerts/samsara-nyseiot-hits-new-52-week-low-should-you-sell-2026-02-02/)

### Inferences
- The harness view that SBC and dilution are heavy holds. The direction is improving, though Q2's SBC step-up (+24% QoQ) needs an explanation.
- Net share settlement absorbs some dilution, at a cash cost of about $140M a year at the H1 run rate. That is effectively a partial "buyback" that the harness counts inside FCF use.
- If SBC/revenue keeps falling about 2–3 points a year while FCF margin rises to the high teens, FCF minus SBC crosses zero around FY28–FY29. This is an inference, not guidance.

### Gaps
- I found no unrecognized SBC balance, no explanation for the Q2 SBC step-up, and no 10-Q legal note text on the Motive award.

## 3. Growth durability: products, enterprise, international, public sector

### Takeaway
The best growth-durability evidence is in the largest customers. ARR from $1M+ customers is above $500M and has grown more than 50% for three straight quarters. 96% of $100K+ customers use two or more products. Emerging products have supplied more than 20% of net new ACV for three quarters. Non-US markets supply about 18% of net new ACV. AI and agent products are early.

### Cited Findings
- ARR from $1M+ customers "surpassed $500 million," growing more than 50% for the third straight quarter. Most growth came from expansions rather than new logos — [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey); [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- Multiproduct adoption:
  - In Q2 FY27, 96% of $100K+ customers used 2+ products and 72% used 3+.
  - In Q1 FY27, 96% of $100K+ customers and 92% of core customers used 2+ products (95% and 91% a year earlier). 70% of $100K+ customers and 54% of core customers used 3+ (66% and 51% a year earlier).
  - [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey); [Q1 letter](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf)
- Emerging products contributed "more than 20% of net new ACV" for three consecutive quarters through Q2 FY27 — [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)
- New products named on the call include the Tracking Label, 360 Camera, Waste Intelligence, Ground Intelligence, and agents for safety, maintenance and dispatch. Connected forms, asset maintenance and asset tags were also discussed.
  - Adoption of some newer AI features rose more than 4x in two months, with more than 1,000 customers engaged.
  - CEO Sanjit Biswas said production adoption of agents is still early.
  - [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)
- The Tracking Label was named one of TIME's Best Inventions of 2026 (2026-10-15, harness S45). The tracker offers 45-day shipment visibility (FreightWaves, 2026-08-10, harness S49). I did not re-verify either.
- International: "18% of net new ACV came from non-U.S. geographies, tied for a quarterly record." Europe posted more than 50% net new ACV growth for the fourth straight quarter, and Mexico's growth accelerated — [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)
- Public sector: "public sector contributed its second highest-ever net new ACV mix," which management attributed to dedicated go-to-market investment. Expansions included a large US city and a heavy civil contractor — [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)
- Customer ROI (June 2026 Investor Day, via TIKR):
  - Primoris (about 8,000 camera units): crashes down 42%, about $5M a year saved.
  - Performance Food Group: needed only half of a budgeted $20M insurance increase.
  - [TIKR, 2026-07](https://www.tikr.com/blog/samsara-stock-fell-nearly-8-in-a-day-its-customers-just-put-dollar-figures-on-why-they-stay)
- Macro: fuel prices "up almost 40% year-over-year in certain months" lifted demand for fuel analytics, and data-center construction customers are "busier than ever" — [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)
- Large-customer economics: average ARR per $100K+ customer went from $338K (Q1 FY26) to $365K (Q1 FY27) — [Q1 deck](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf)

### Inferences
- Bull: ARR growth has held at about 30% for at least five quarters while the base passed $2.1B. Net new ARR is still growing (+27% TTM cc). The expansion engine is widening, through more products per customer and larger accounts.
- Bear: the core telematics and video-safety business must be growing well below 30%. Large-account ARR is +38%, $1M+ is +50%, and emerging products are more than 20% of net new ACV. The 30% total therefore implies smaller customers are much slower, which makes the SMB tail the likely first place for deceleration or Motive pressure.
- The harness red-team signal "$100K+ net adds < 242" is set at a record level, so it will likely trip on normal seasonality. It is a weak break condition.

### Gaps
- No ARR by product, no gross or net churn, no CAC payback, and no SMB growth rate are disclosed.

## 4. Competition: Motive, Geotab, Verizon Connect, Lytx, Netradyne

### Takeaway
Motive is the only competitor with comparable disclosure. It is about 30% of Samsara's ARR size, growing at the same 30% rate, still loss-making, and newly funded with more than $1.3B in private equity after it withdrew its IPO. Samsara won a $30.3M arbitration against Motive but lost its ITC patent case. There is no primary data on win rates or pricing.

### Cited Findings
- **Motive S-1** (filed publicly about 2025-12-23):
  - 9M 2025 revenue $327.3M, +22%; Q3 2025 revenue $115.8M, +23%.
  - 9M net loss $138.5M, against $113.9M a year earlier.
  - About 100,000 customers and 4,508 employees.
  - [Fintool summary of S-1, 2025-12-23](https://fintool.com/news/motive-ipo-fleet-management); filing: [Motive S-1 on EDGAR](https://www.sec.gov/Archives/edgar/data/1646681/000162828025058773/motive-sx1.htm). I did not fetch the S-1 directly, so these figures are second-hand.
- Motive S-1 per FreightWaves: net dollar retention "exceeds 110%." About 89% of core customers use 2+ products. About 30% of ARR comes from trucking and logistics, with faster growth in construction, field service and transit — [FreightWaves, 2025-12-26](https://www.freightwaves.com/?p=569009)
- **Motive withdrew its S-1 and raised more than $1.3B** in growth equity from General Catalyst, announced **2026-09-10**. Valuation was not disclosed. Motive stated:
  - ARR crossed $600M, with growth "accelerated to 30%."
  - ARR from $100K+ customers grew nearly 60%, with NRR above 120% for those accounts.
  - [Dealroom, 2026-09](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/)
- Litigation:
  - Samsara sued Motive in January 2024 (trade secrets, patents, fake accounts) and filed an ITC complaint.
  - On 2025-09-08 an ITC judge found no infringement and invalidated eight of nine asserted claims.
  - A Delaware fraud and false-advertising case continues.
  - [Fintool](https://fintool.com/news/motive-ipo-fleet-management)
  - Samsara received a $30.3M arbitration award against Motive (breach of contract, fraud, unfair competition, false advertising), booked in Q1 FY27 — [Q1 letter](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf); [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- Geotab surpassed 5 million connected-vehicle subscriptions (2025-09-04, **more than 6 months old**). It has more than 100,000 customers, spends more than $150M a year on R&D, and adds about 1M subscriptions every two years — [Geotab press release](https://www.geotab.com/ie/press-release/5-million-subscriptions/)
- ABI Research ranked Geotab #1, Verizon Connect #2 and Solera #3 in commercial telematics (**2022, stale**) — [Automotive Fleet, 2022-10-06](https://www.automotive-fleet.com/news/geotab-ranked-as-top-global-telematics-provider)
- Management did not discuss competition, win rates, pricing or Motive on the Q2 FY27 call. The closest remark was that inventory is "a competitive advantage" — [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)

### Inferences
- Motive's private raise removes the bear case that it would be capital-constrained. It now has more than $1.3B to subsidize hardware or price aggressively in SMB and mid-market trucking.
- Motive's large-customer metrics (+60% $100K+ ARR, >120% NRR) are on a much smaller base. Even so, they suggest it is moving up-market into Samsara's core expansion segment. This supports the red-team "pricing and hardware subsidy" pre-mortem (p=0.2) more than the harness evidence did.
- Against that, Samsara's ARR is about 3.5x Motive's, it is GAAP profitable against Motive's ~$185M a year in losses, and it has a richer product set.

### Gaps
- I found no reliable primary data on win rates, pricing or discounting. I also found no current figures for Lytx, Netradyne or Verizon Connect. Verizon Connect is not broken out by Verizon.

## 5. Valuation (dated)

### Takeaway
At $39.57 (2026-10-16 close) Samsara trades at about **10.3–10.4x EV/ARR**, about **11.8–11.9x EV/TTM revenue** and **about 86x EV/TTM FCF**, with negative FCF after SBC. The multiple is well below 2025 levels: forward EV/EBITDA went from about 81x in August 2025 to about 39x in July 2026. The share price is mid-range in a 52-week band of $23.38–$47.47.

### Cited Findings
- Price was $39.57 at the 2026-10-16 close (harness F218, Yahoo). MarketBeat's 2026-10-16 snapshot shows $39.54, a $23.15B market cap and a 52-week range of $23.38–$47.47. The 2026 start price was $35.43 — [MarketBeat](https://www.marketbeat.com/instant-alerts/samsara-nyseiot-hits-new-52-week-low-should-you-sell-2026-02-02/)
- The maximum drawdown was 46.37%, reached 2026-02-05 during the software selloff. The stock fell 7.6% to $33.33 on 2026-07-22 with no company news, attributed to rotation out of high-multiple software. On that date it traded at 38.8x NTM EV/EBITDA and 43.7x forward P/E, against 81.0x forward EV/EBITDA in August 2025. Peers on forward EBITDA: Trimble about 10.8x, Karooooo about 11.4x (undated) — [TIKR, 2026-07](https://www.tikr.com/blog/samsara-stock-fell-nearly-8-in-a-day-its-customers-just-put-dollar-figures-on-why-they-stay)
- The IPO priced at $23 in December 2021 — [Fintool](https://fintool.com/news/motive-ipo-fleet-management)
- My computation at $39.57, using cash and investments of $1,325.7M, no debt, ARR $2,124.7M, TTM revenue $1,847.6M, TTM FCF $255.5M and FY27 guide midpoint $2.045B:

| Share basis | Market cap | EV | EV/ARR | EV/TTM revenue | P/S TTM | EV/FY27E revenue | EV/TTM FCF | P/TTM FCF |
|---|---|---|---|---|---|---|---|---|
| 585.6M shares outstanding | $23.17B | $21.85B | 10.3x | 11.8x | 12.5x | 10.7x | 86x | 91x |
| 590.5M diluted | $23.36B | $22.04B | 10.4x | 11.9x | 12.6x | 10.8x | 86x | 91x |

- The harness's P/FCF of 91.45x matches. Its EV of $23.07B is overstated by about $1.03B because it counted only cash and equivalents (see Section 0).

### Inferences
- About 10x EV/ARR for a 30% ARR grower with 21% non-GAAP margins is a de-rated multiple relative to its own history. On a 5–10 year view, the red-team's "multiple collapses to 20x P/FCF" bear case requires growth to fall to the high single digits.

### Gaps
- I found no reliable historical EV/sales series. The 2025 peak price is not verified in my sources; a Loop Capital $63 target from Dec-2024 is referenced only indirectly.

## 6. Consensus estimates and price targets (dated)

### Takeaway
The Street is constructive: Moderate Buy, with an average target of about $51–52 (range $45–58) against a $39.6 price. Eight firms raised targets after Q2. Public revenue consensus data appears stale and should not be used to claim a variant view.

### Cited Findings
- After Q2 FY27 (early September 2026), eight firms kept their ratings and raised targets:

| Firm | Rating | Old target | New target |
|---|---|---|---|
| BTIG | Buy | $45 | $54 |
| Guggenheim | Buy | $45 | $51 |
| KeyBanc | Overweight | $46 | $55 |
| TD Cowen | Buy | $48 | $53 |
| RBC | Outperform | $50 | $55 |
| Wells Fargo | Overweight | $50 | $58 |
| BMO | Outperform | $44 | $54 |
| BofA | Buy | $47 | $55 |

  Source: [iTiger/Benzinga, 2026-09-04](https://www.itiger.com/news/2664435814)
- As of 2026-10-16: Moderate Buy (2 strong buy, 14 buy, 6 hold, 0 sell), average target $51.68, high $58, low $45, 22 analysts — [MarketBeat](https://www.marketbeat.com/instant-alerts/samsara-nyseiot-hits-new-52-week-low-should-you-sell-2026-02-02/)
- As of 2026-10-17: average target $51.25 (24 analysts, range $45–58). The same page shows **stale** FY27 revenue consensus of $1.97B and EPS of $0.68 — [TickFlow](https://tickflow.io/stock/IOT/forecast)
- Morgan Stanley rates the stock Equal Weight (2026-07-21). Guggenheim initiated at Buy (2026-07-23) — [TIKR](https://www.tikr.com/blog/samsara-stock-fell-nearly-8-in-a-day-its-customers-just-put-dollar-figures-on-why-they-stay)

### Inferences
- Post-Q2 FY27 consensus is almost certainly at or above guidance (about $2.045B+), because the Street usually tracks the guide after a raise. Treat this as estimated, not sourced. The harness model's FY27 revenue of $2.05B is therefore consensus-like, which matches its own warning that the model is in line with consensus.

### Gaps
- I found no reliable post-Q2 FY27 consensus for FY27 or FY28 revenue, EPS or FCF. TickFlow's FY28 figures look quarterly or mislabeled. Seeking Alpha and Benzinga estimate pages were not accessible to me.

## 7. Bull and bear evidence for the open IC questions

### Takeaway
The evidence tilts toward durable 25–30% ARR growth for the next one to two years, led by large customers and multiproduct expansion. The unresolved risks are FCF-after-SBC quality, hardware cost and gross-margin pressure, and a better-funded Motive. None of these is disproven or confirmed yet.

### Cited Findings
- **Bull:**
  - FY27 guidance raised twice, from 21–22% to 26% growth — [Q4 PR](https://s29.q4cdn.com/853855404/files/doc_financials/2026/q4/Q4-2026-Earnings-Press-Release-FINAL.pdf), [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
  - Record $100K+ and $1M+ net adds; $1M+ ARR growing more than 50% — [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)
  - RPO of $4.29B — [10-Q](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm)
  - $1.33B in cash and investments and no debt — [10-Q](https://www.sec.gov/Archives/edgar/data/0001642896/000162828026060909/iot-20260801.htm)
  - SBC/revenue down from about 27% (FY24) to about 18% TTM — [Q1 deck](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf)
  - Four straight GAAP-profitable quarters — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
- **Bear:**
  - FCF guide reversed from +100bp to −100bp in one quarter; supply-chain costs "continue to increase" — [Q1 letter](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Shareholder-Letter_FINAL.pdf), [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)
  - Non-GAAP gross margin was 76% in Q1 FY27, against 79% a year earlier — [Q1 deck](https://s29.q4cdn.com/853855404/files/doc_financials/2027/q1/Q1-FY27-Investor-Presentation_FINAL.pdf)
  - Q3 revenue is guided to only +24% — [Q2 PR](https://s29.q4cdn.com/853855404/files/content_files/Q2-2027-Earnings-Press-Release-Draft-FINAL.pdf)
  - No buyback, and $107M of insider selling in three months — [MarketBeat](https://www.marketbeat.com/instant-alerts/samsara-nyseiot-hits-new-52-week-low-should-you-sell-2026-02-02/)
  - Motive raised more than $1.3B, with growth "accelerated to 30%" and NRR above 120% in its $100K+ cohort — [Dealroom](https://dealroom.co/news/150072-motive-lands-1-3b-from-general-catalyst-pulls-its-ipo-filing/)
  - NRR is disclosed only as an "approximately 115%" target, never as a reported number — [Q2 transcript](https://www.tradingkey.com/news/transcripts/262150876-tradingkey)

### Inferences
- These harness KPIs and break conditions should be re-specified:
  - Deferred revenue: the trigger is mis-set; it fires on the current value.
  - NRR: not observable as a reported number.
  - $100K+ net adds below 242: set at a record level.
- More testable break conditions:
  - Net new ARR YoY growth turning negative in constant currency.
  - Non-GAAP gross margin below 75%.
  - FY28 initial guide below 20% growth. Last year's initial guide was 21–22% against about 30% actual.
  - FCF minus SBC failing to improve YoY.

### Gaps
- There is no independent channel or customer-survey evidence on Samsara-vs-Motive win rates or pricing, and no NRR history.

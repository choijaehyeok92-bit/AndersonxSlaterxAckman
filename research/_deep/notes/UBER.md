# Uber Technologies (UBER) — long-term (5–10y) holding fact base, as of 2026-10-18

Scope note: figures are dated. Anything older than 6 months (before 2026-04-18) is flagged [>6m]. "Est." = my own arithmetic from cited inputs; "consensus" = third-party aggregates, labelled. Harness = /home/claude/choijaehyeok92-bit/andersonxslaterxackman/research/UBER/ (report.md, redteam.json, slater.2.json, evidence.json).

## Q0. Harness reconciliation: which must-be-true claim was "broken" for Slater, and does the data really falsify it?

### Takeaway
Slater's red line ("already falsified hypothesis") was set off by one must-be-true claim: "diluted shares stay at or below the FY2026Q2 level (2.05bn), so buybacks offset dilution." It was marked [broken] because the code compared the actual Q2 2026 diluted weighted-average share count, **2,050.2M**, with a threshold of 2,050,000,000. That is a rounding and self-reference artifact. The threshold was the same data point rounded down, so it "fails" by 0.2M shares (0.01%). The share count actually **fell 3.5% YoY and about 1.0% QoQ**, so the data do not falsify the claim. The real forward risk is different and was not in the harness evidence. Buybacks slowed because Uber diverted about $4B in Q2 into Delivery Hero (DH) stock, ahead of a ~$13.7B net takeover plus a $2.3B ezCater purchase. Slower share shrinkage in 2026–27 is therefore plausible, but nothing is "already falsified."

### Cited Findings
- The harness verdict table shows Slater moving from for to **against (red line → against)**, flagged "✗ 이미 반증된 가설" (already falsified hypothesis). The code-judged warning reads: '희석 주식 수가 FY2026Q2 수준(20.5억) 이하로 유지…' — 실제 2.05022e+09로 깨짐 — harness report.md §표결 (local file); slater.2.json sets `diluted_shares <= 2050000000` with status "on_track" in the agent's own view.
- Q2 2026 diluted weighted-average shares were 2,050.2M, against 2,125.6M in Q2 2025 — [Uber Q2 2026 earnings release, 8-K, 2026-08-05](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm). Harness evidence F60/F61: Q1 2026 2,071.4M → Q2 2026 2,050.2M; F58 Q2 2025 2,125.6M (10-Q filings).
- Est.: the YoY change is (2,050.2 / 2,125.6) − 1 = −3.5%, and the QoQ change is (2,050.2 / 2,071.4) − 1 = −1.0%.
- The same artifact affects the red-team signal "FY2026Q3 gross bookings < $58.25B," which the harness marks [충족 — 훼손] (met — thesis damaged). Q3 has **not been reported yet**: the release is scheduled for 2026-11-04. The $58.02B value that "meets" the signal is the **Q2** actual. Q2 GB came in at $58,022M — [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm). The Q3 date comes from [MarketScreener calendar](https://uk.marketscreener.com/quote/stock/UBER-TECHNOLOGIES-INC-57860975/calendar/) and [FMP, 2026-10-07](https://site.financialmodelingprep.com/market-news/uber-q3-2026-earnings-call-citizens-100-price-target).
- The harness verifier rejected the phrase "Q3 GB guidance 18–22% constant currency" as unsupported. The primary source confirms it: Q3 GB guidance is $58.25–60.25B, "up 18% to 22% YoY in constant currency, with a roughly 1-point currency headwind," and Q2 GB grew 22% in constant currency — [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm). Slater's and the red team's statements were correct. The verifier's flag reflects a gap in the harness's evidence coverage.
- The red-team narrative was that "buybacks ended at the peak and debt filled the gap." The cause is misattributed. The CFO said about $4B was deployed in Q2, "largely on market purchases of Delivery Hero stock." Repurchases total about $3.5B YTD, the historical target is about 50% of FCF, and repurchases will rebuild over "months, not quarters" — [Uber Q2 2026 earnings call transcript, 2026-08-05](https://s23.q4cdn.com/407969754/files/doc_events/2026/Aug/05/Uber-Q2-26-Earnings-Call-Transcript.pdf).
- The anti-disintermediation claim was a **manual check** in the harness for Anderson, Slater and Ackman: "a major AV partner launches a direct demand channel bypassing Uber." That condition was **triggered before the harness ran** and is missing from evidence.json. On 2026-07-24 Waymo notified Uber it will launch its own app in Austin and Atlanta in January 2028, ending exclusivity. The Phoenix arrangement ended in May 2026 — [The Next Web, 2026-07-25](https://thenextweb.com/news/waymo-uber-exclusivity-ends-austin-atlanta-robotaxi); [Automotive World](https://www.automotiveworld.com/news/uber-confirms-end-of-tie-up-with-waymo-as-rivalry-heats-up/). See Q2 for detail.

### Inferences
- The harness should re-run Slater's vote with a non-degenerate threshold, for example diluted shares above 2.10bn or a QoQ increase. On the data, Slater's vote would revert to "for" (conviction 3), and the committee would become 3–0 in favour **on that specific red line**.
- The red line the committee should actually debate is the Waymo direct-channel trigger. It is a genuine partial confirmation of the harness's main bear scenario, and all three agents had listed it as a manual check.
- Harness claims **confirmed** by primary data: Q2 GB $58.0B (F198), adjusted EBITDA $2.82B (F199), 4.9% of GB (F200), FCF $2.80B (actual $2,792M, F201), Q3 guidance ranges (F202–F204), Q2 buybacks $518M (F221), diluted shares (F61), SBC rising.
- Harness claims **updated**:
  - The buyback drop was an M&A diversion (DH), not a "peak."
  - Adjusted EBITDA is "no longer a key management measure." Uber now leads with non-GAAP operating income, 3.7% of GB in Q2, so K2 and the 4%-of-GB adjusted EBITDA red lines should be mirrored on non-GAAP operating income.
  - Earnings-call evidence now exists, which closes the harness gap "call 유형 근거 없음" (no call-type evidence).
- Harness claims **contradicted**: "diluted shares broken"; "Q3 GB below guidance already met"; and the redteam/Slater "18–22% cc" being unsupported.

### Gaps
- The harness code was not inspected, so it is not confirmed whether the Q3 GB signal used Q2 data or a stale value. The inference rests on the numbers matching ($58.02B < $58.25B).
- The period-end basic share count from the 10-Q cover page (as opposed to the weighted average) was not retrieved.

## Q1. Latest reported quarter (Q2 2026) and Q3 2026 guidance

### Takeaway
Q2 2026, reported 2026-08-05, beat on bookings: GB $58.0B, +24% reported / +22% cc. Profit grew strongly: GAAP operating income $1.89B (+30%), adjusted EBITDA $2.82B (+33%), FCF $2.79B. Revenue grew only 12% because business-model changes, mainly in the UK, cut about 8 points; Mobility revenue rose just 1%. Q3 guidance (GB $58.25–60.25B, non-GAAP EPS $0.84–0.88) came in slightly below consensus. Q3 is due **2026-11-04**.

### Cited Findings
- Q2 2026 — [Uber Q2 2026 release, 2026-08-05](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm):
  - Usage: trips 3,867M (+18%); MAPCs 208M (+16%); monthly trips per MAPC +2%.
  - Gross bookings: total $58,022M (+24% / +22% cc).
    - Mobility $28,988M (+22% / +20% cc)
    - Delivery $27,463M (+26% / +25% cc)
    - Freight $1,571M (+25%)
  - Revenue: total $14,191M (+12% / +11% cc); business-model changes reduced growth by 8 points.
    - Mobility $7,363M (+1%)
    - Delivery $5,245M (+28%)
    - Freight $1,583M (+26%)
  - Segment non-GAAP operating income:
    - Mobility $2,215M (+28%)
    - Delivery $1,055M (+38%)
    - Freight −$24M
    - Corporate G&A and platform R&D −$1,103M
  - Profit:
    - GAAP income from operations $1,890M (+30%)
    - GAAP net income $2,394M (+77%), including a $1.6B pre-tax equity revaluation gain
    - GAAP diluted EPS $1.17
    - Non-GAAP operating income $2,143M (+40%; 3.7% of GB)
    - Non-GAAP EPS $0.81 (+35%)
    - Adjusted EBITDA $2,819M (+33%; 4.9% of GB vs 4.5%), described as "no longer a key management measure… disclosed for transition purposes"
  - Cash: OCF $2,862M; FCF $2,792M (+13%); TTM FCF above $10B, a first for Uber (CFO).
  - Est.: Q2 FCF margin is 2,792 / 14,191 = 19.7% of revenue, or 4.8% of GB.
- Q3 2026 guidance — [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm):
  - GB $58.25–60.25B (+18–22% cc; about 1pt FX headwind)
  - Non-GAAP EPS $0.84–0.88 (+28–35%)
  - Adjusted EBITDA $2.86–2.96B
- Consensus going into the print was Q3 GB $59.33B and EPS $0.89, so guidance sat slightly below — harness F205/F206 citing [S45 aggregator](https://startupmap.iamsterdam.com/news/feed/uber-q3-guidance-misses-estimates-despite-58b-q2-bookings-and-record-10b-free-cash-flow). TIKR likewise reported $0.84–0.88 against a $0.89 estimate and said revenue "narrowly" missed — [TIKR, 2026-08-10](https://www.tikr.com/blog/uber-stock-fell-10-this-year-can-it-bring-meaningful-upside-before-2027).
- Q3 consensus (MarketScreener, labelled "forecast," undated): revenue $14,669M, EBITDA $2,923M, EBIT $2,206M, EPS $0.91 — [MarketScreener](https://uk.marketscreener.com/quote/stock/UBER-TECHNOLOGIES-INC-57860975/calendar/).
- Q3 report date is 2026-11-04 at 5:00am PT / 8:00am ET — [FMP, 2026-10-07](https://site.financialmodelingprep.com/market-news/uber-q3-2026-earnings-call-citizens-100-price-target); [MarketScreener](https://uk.marketscreener.com/quote/stock/UBER-TECHNOLOGIES-INC-57860975/calendar/). This is contradicted by [TIKR, 2026-08-23](https://www.tikr.com/blog/uber-has-fallen-23-from-its-high-heres-where-the-stock-could-go), which said October 29. Two later sources agree on November 4.
- Q1 2026 for trend — [Uber Q1 2026 release, 2026-05-06](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000019/uberq126earningspressrelea.htm):
  - Usage: trips 3.6B (+20%); MAPCs 199M (+17%).
  - Gross bookings: total $53.7B (+25% / +21% cc); Mobility $26.4B (+20% cc); Delivery $26.0B (+23% cc); Freight $1.3B.
  - Revenue $13.2B (+14%), with a 9-point drag from model changes.
  - Profit: GAAP operating income $1.9B (+57%); adjusted EBITDA $2.5B (4.6% of GB); GAAP EPS $0.13 after a $1.5B equity revaluation headwind; non-GAAP EPS $0.72.
  - Cash: FCF $2.3B (+2%); buybacks $3.0B.
- Q2 management commentary — [Q2 2026 call transcript](https://s23.q4cdn.com/407969754/files/doc_events/2026/Aug/05/Uber-Q2-26-Earnings-Call-Transcript.pdf):
  - US Mobility accelerated on insurance savings reinvested in the market, product velocity and sparse markets.
  - U4B (Uber for Business) grew 40% YoY.
  - The top 20 US cities are only 30% of US GB and 25% of profit.
  - Getir (closed early August) and Careem add to Q3 Delivery.

### Inferences
- Bookings growth of +22% cc in Q2, with Q3 guided to 18–22%, is still faster than the harness base case (about 12% revenue growth). Reported revenue understates the economics because of the UK model change. The harness's K3 test (Q3 revenue ≥ $15.0B) looks demanding against a $14.67B consensus. Est.: hitting $15.0B needs about +11% YoY on Q3 2025's $13.47B (harness F139), close to consensus.
- Q3 GB guidance includes acquired Getir and Careem volume. Organic growth is somewhat lower than headline, which matters for reading the 18–22%.

### Gaps
- Q3 2026 results are not yet out (due 2026-11-04).
- No segment adjusted EBITDA is disclosed any more.
- Consensus Q3 GB as of October was not found. The $59.33B figure dates from August.

## Q2. Autonomous vehicles: do AV fleets need Uber's demand network or disintermediate it?

### Takeaway
The evidence has turned partly against the aggregator thesis at the top of the market. Waymo, the US leader, is leaving Uber's exclusive arrangements and building its own app and subscription. Tesla says it does not need ride-hail partners. Uber is responding in three ways: assembling a fragmented roster of smaller partners (seven AV cities, targeting 15 by year-end 2026), committing about $10B of capital, and reporting strong utilisation claims. AVs remain under 0.5% of trips, so there is no near-term P&L damage. The debate is over the terminal value of Mobility.

### Cited Findings
- **Waymo exit:**
  - On 2026-07-24 Waymo notified Uber it will launch its own app in Austin and Atlanta in January 2028, ending exclusivity. Its fleet stays on Uber through at least May 2028. An Uber spokesperson confirmed this to CNBC and Bloomberg, and the FT first reported Waymo exploring a full exit — [The Next Web, 2026-07-25](https://thenextweb.com/news/waymo-uber-exclusivity-ends-austin-atlanta-robotaxi).
  - Waymo runs in 11 US metros without Uber and delivers more than 500,000 paid rides per week (The Next Web). Automotive World instead cites about 4,000 vehicles across 10 US cities. The source counts differ.
  - Waymo has expanded through its own app into six more markets and announced no new Uber city since Atlanta (June 2025) — [The Next Web](https://thenextweb.com/news/waymo-uber-exclusivity-ends-austin-atlanta-robotaxi).
  - The Phoenix arrangement ended in May 2026. Waymo will launch London with Moove on its own app and has launched "Waymo Premier," a monthly subscription that competes with Uber One — [Automotive World](https://www.automotiveworld.com/news/uber-confirms-end-of-tie-up-with-waymo-as-rivalry-heats-up/).
- **Friction between the two:** Uber reportedly cited unsustainable economics, safety issues (school-bus incidents) and a lack of transparency. Waymo blamed a May Atlanta incident on Uber's routing technology. Uber has lobbied for "hybrid network" rules, such as a New Jersey proposal requiring human drivers for at least 85% of rides — [Automotive World](https://www.automotiveworld.com/news/uber-confirms-end-of-tie-up-with-waymo-as-rivalry-heats-up/); [The Next Web](https://thenextweb.com/news/waymo-uber-exclusivity-ends-austin-atlanta-robotaxi).
- **Market reaction:** Uber fell more than 4% to $65.94 on the news, its lowest in over a year — [Automotive World](https://www.automotiveworld.com/news/uber-confirms-end-of-tie-up-with-waymo-as-rivalry-heats-up/). Bloomberg said the breakdown of the Waymo partnership was weighing on the stock, down 28% from its $100.10 record — [Bloomberg Law, 2026-08-04](https://news.bloomberglaw.com/tech-and-telecom-law/ubers-robotaxi-ambition-to-face-scrutiny-as-shares-languish).
- **Uber's position** — [Q2 2026 call transcript](https://s23.q4cdn.com/407969754/files/doc_events/2026/Aug/05/Uber-Q2-26-Earnings-Call-Transcript.pdf):
  - Scale (CEO Khosrowshahi): live in seven AV cities, on track for 15 by year-end. AVs do "hundreds of thousands of trips per week" against about 300M total, or "less than 0.5%."
  - Utilisation (CEO): partner launches reach "mid to high 20s, low 30s" trips per vehicle per day.
  - Waymo (CEO): Uber continues with Waymo in Austin and Atlanta next year and wants to avoid dependence on one partner.
  - Trip growth in SF, LA and Phoenix, which are Waymo-heavy markets, accelerated in Q2 versus Q1 (CEO).
  - Capital (CFO Krishnamurthy): about $10B of multi-year AV investment, including partner equity. Partners raised an additional $2.50 from others per $1 Uber invested, and about 120,000 vehicle commitments are planned over the next few years. P&L impact will be sized later.
  - Partner roster: Nuro/Lucid (Bay Area; a Lucid vehicle at "$70,000, $80,000" with guaranteed volume), Zoox (Las Vegas), Wayve (London, Tokyo), Baidu (London), Pony and Verne (Zagreb), NVIDIA (LA and SF 2027; 28 cities by 2028) and Rivian (SF and Miami 2028).
- Other partners named in press include Avride, Momenta, Volkswagen and WeRide, plus a deal worth over $1B for up to 50,000 Rivian-built robotaxis. Several partners will not have vehicles on the road until late 2026 or later — [The Next Web](https://thenextweb.com/news/waymo-uber-exclusivity-ends-austin-atlanta-robotaxi); [Automotive World](https://www.automotiveworld.com/news/uber-confirms-end-of-tie-up-with-waymo-as-rivalry-heats-up/).
- Baidu Apollo Go launched fully driverless on Uber in Dubai (2026-08-20), Wayve and Uber ran the first UK autonomous rides (2026-09-03), and Uber won Spain's first robotaxi permit (2026-09-24) — harness S30/S32/S39 (company IR and press).
- A 2,000-vehicle Pony.ai partnership is planned for Europe — [TIKR, 2026-08-23](https://www.tikr.com/blog/uber-has-fallen-23-from-its-high-heres-where-the-stock-could-go).
- **Tesla:**
  - As of the Q2 2026 call (2026-07-22), Tesla runs unsupervised robotaxi in seven metros, including Austin, Miami, Orlando and Tampa. The Bay Area still uses safety drivers.
  - Cumulative paid miles are about 2.5M. Cybercab production has started at Giga Texas, and Tesla targets about 10% weekly US scaling.
  - Asked about partnering with rideshare providers, Tesla said it "sees no demand challenges and does not need to integrate with other providers" — [Not a Tesla App, 2026-07-22](https://notateslaapp.com/news/4481/summary-of-teslas-2026-q2-earnings-call-cybercab-fsd-ai4-and-more). This is a fan site summarising the call; treat it as secondary.
- **Pre-2026 bull argument [>6m]:** in November 2024 Jefferies argued robotaxi fleets are best off partnering with rideshare rather than competing — [Nasdaq/TheFly, 2024-11-19](https://www.nasdaq.com/articles/uber-weakness-creates-more-attractive-entry-point-says-jefferies). The Waymo split weakens that argument for vertically integrated leaders.

### Inferences
- **Bear evidence:** the two best-capitalised US AV players, Waymo and Tesla, both now run direct demand channels, and Waymo is adding a subscription. That directly confirms the harness's red-team pre-mortem #1 (p = 0.20) and the manual falsification check. The thesis is now "Uber aggregates the long tail of AV suppliers," not "AV fleets need Uber."
- **Bull evidence:** Uber's share of US GB is not concentrated where Waymo operates (top 20 cities = 30% of GB). Utilisation claims of 25–30+ trips per vehicle per day suggest demand density matters to AV unit economics. Supply also appears to be fragmenting into more than 15 partners, and AV is below 0.5% of trips today.
- The roughly $10B AV commitment changes Uber's "capital-light" profile. Partner equity and vehicle-volume guarantees could pressure FCF conversion later in the decade. That bears on the red team's "weakest assumption" (base FCF margin 19%).

### Gaps
- No disclosed AV take rate, AV GB or AV-specific economics on Uber. Management gave no human-driver utilisation comparison.
- No independent data on Waymo-on-Uber utilisation in Austin or Atlanta.
- Tesla figures come from secondary or fan sites; Tesla's Q3 2026 update was not checked.
- The status of May Mobility, Momenta and WeRide deployments in 2026 was not verified.

## Q3. Unit economics: take rate, insurance, regulatory and labour risk

### Takeaway
Reported take rates are distorted by business-model changes; management says the net take rate is "broadly stable." Insurance swung from headwind to US tailwind in 2026. Regulatory and legal costs are rising: a €825M Dutch GDPR fine (under appeal), an EU Platform Work Directive deadline of 2026-12-02, a Nigeria exit with an antitrust probe, and sexual-assault litigation settlements.

### Cited Findings
- Mobility revenue margin fell nearly 500bp YoY, about 400bp of it from the UK model change ("optical"). Net take rate in the 10-Q is "broadly stable," Mobility operating income margin was 7.6%, and Delivery revenue margin was "largely stable" (CFO) — [Q2 2026 call transcript](https://s23.q4cdn.com/407969754/files/doc_events/2026/Aug/05/Uber-Q2-26-Earnings-Call-Transcript.pdf).
- Insurance savings were "reinvested in the market," driving US acceleration (CFO). No dollar figure was given — [Q2 2026 call transcript](https://s23.q4cdn.com/407969754/files/doc_events/2026/Aug/05/Uber-Q2-26-Earnings-Call-Transcript.pdf).
- In Brazil, competition for two-wheeler supply from DiDi Food and Meituan has raised costs (CEO) — same transcript.
- On 2026-08-21 the Dutch Data Protection Authority fined Uber €825M (about $964M) under GDPR for automated driver suspensions without human review (2018–2022). Uber disagrees and will appeal. It is the regulator's fourth Uber fine; the largest earlier one was €290M in 2024 — [AP via NY1, 2026-08-21](https://ny1.com/nyc/all-boroughs/ap-top-news/2026/08/21/uber-fined-nearly-1-billion-by-dutch-regulators-over-automated-suspensions-of-driver-accounts).
- **EU Platform Work Directive:**
  - Transposition is due 2026-12-02. It brings a rebuttable presumption of employment, with the burden shifting to the platform, and stricter rules on algorithmic management.
  - As of 2026-08-20, no member state was identified as having completed transposition.
  - Spain's current presumption covers only delivery and could extend to other sectors including ride-hailing. France's burden shift could ease reclassification claims.
  - Source: [Littler, 2026-08-20](https://www.littler.com/news-analysis/asap/eu-platform-work-directive-uncertainty-ahead-implementation-deadline).
- **Other legal and regulatory items:**
  - Uber is exiting Nigeria after 12 years (Reuters, 2026-09-03), and Nigeria's antitrust agency is probing the exit (Bloomberg, 2026-09-06) — harness S29/S26.
  - Uber settled a third bellwether sexual-assault lawsuit (2026-10-07) — harness S40.
  - The amounts are undisclosed in harness evidence.

### Inferences
- The DH acquisition (Germany-HQ, about 50 markets) would sharply raise Uber's EU Platform Work Directive exposure in Delivery from 2027, the very segment the deal enlarges.
- The €825M fine is about 9–10% of one quarter's FCF (est., vs Q2 FCF of $2.79B). It is manageable, but GDPR algorithmic-management risk recurs as directive enforcement begins.

### Gaps
- No quantified insurance-cost trend (reserves, cost per trip).
- No US state classification updates for 2026 were found. California Prop 22 status, Massachusetts and similar were not researched.
- The size of litigation reserves is unknown.

## Q4. Capital allocation: buybacks, share count, SBC, investments, debt, M&A

### Takeaway
2026 marks a shift from buybacks toward large M&A and AV capital. The commitments are:
- Delivery Hero: ~$13.7B net of the existing stake, funded by cash plus a €14B bridge and a €4B term loan; close 2H 2027.
- ezCater: $2.3B cash (announced 2026-10-06).
- Getir and Careem.
- AV: about $10B multi-year.

Buybacks fell to $518M in Q2 and management says they will rebuild over "months." Share count is still falling (−3.5% YoY), but SBC is rising and leverage will step up toward the stated gross leverage ceiling of below 2x.

### Cited Findings
- Buybacks were $518M in Q2 2026 (vs $1,363M in Q2 2025) and $3,529M YTD — [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm). Q1 2026 was $3.0B — [Q1 2026 release](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000019/uberq126earningspressrelea.htm). FY2025 was $6.52B — harness F4 (10-K).
- SBC: $556M in Q2 2026 vs $475M in Q2 2025; FY2025 $1.83B — harness F158/F161/F156 (10-Q/10-K).
- Q2 2026 balance sheet and cash flows — [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm):
  - Unrestricted cash and short-term investments were $5.4B.
  - Uber raised $3,997M of new debt and repaid $2,000M; short-term debt was $1,997M.
  - It purchased $1,640M of total return swaps, which appear to be DH equity derivatives.
  - Equity-method investments rose from $287M to $3,773M, consistent with DH becoming equity-method.
  - Business acquisitions used $647M of cash.
  - Total debt was $10.73B (harness F43).
- **Delivery Hero deal terms** — [Uber 8-K Ex. 99.1, 2026-07-16](https://www.sec.gov/Archives/edgar/data/0001543151/000155278126000382/e26302_ex99-1.htm):
  - Price: €41.50 per share cash; equity value $14.8B, or $13.7B adjusted for prior stake purchases.
  - Stake: Uber held about 24.77% of votes plus 11.74% via derivatives. Prosus irrevocably committed about 17%, taking Uber's economic interest to about 53%; minimum acceptance is 50% + 1.
  - Funding: existing cash and new debt, with a committed bridge of about €14B and no equity issuance.
  - Leverage: Uber targets a strong investment-grade rating with gross leverage below 2x and calls its capital allocation framework, including buybacks, "unchanged."
  - Expected effect and timing: accretive to non-GAAP EPS at close and high-single-digit accretive by year 3; close in 2H 2027.
  - Divestiture: DH sells 14 markets (about $11B of 2025 GB) to SSW Partners for about $1.6B.
  - Scale: the acquired portion is about 50 markets with about $42B of 2025 GB; pro-forma 2025 GB is $236B across 99 markets.
- Offer status: the offer document was approved by BaFin, and the acceptance window runs from 2026-08-27 into early November 2026. DH traded below the offer price on regulatory risk. EU competition review is a watch item — [SentiSense, 2026-08-27](https://app.sentisense.ai/stories/uber-launches-multibillion-dollar-bid-for-delivery-hero-as-it-leans-on-subscript-08272026). This is an aggregator; the BaFin approval should be verified on the DH or BaFin site.
- Uber signed a €4B two-tranche term loan led by Morgan Stanley on 2026-08-06, with 18-month and 3-year maturities — [TIKR, 2026-08-10](https://www.tikr.com/blog/uber-stock-fell-10-this-year-can-it-bring-meaningful-upside-before-2027).
- **ezCater:** $2.3B all-cash; more than $2.5B of TTM GB; average order above $400; close "in the coming months"; Uber expects it to be margin-accretive — [BNN Bloomberg, 2026-10-06](https://www.bnnbloomberg.ca/business/company-news/2026/10/06/uber-to-buy-us-catering-platform-ezcater-for-us23b/).
- **Equity portfolio marks are volatile:** a $1.5B pre-tax headwind in Q1 2026 and a $1.6B gain in Q2 2026 — [Q1 release](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000019/uberq126earningspressrelea.htm); [Q2 release](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm).
- **Cost actions:** about 3,300 corporate job cuts, roughly 10% of staff (Reuters and Guardian, 2026-09-02/03) — harness S24/S25. The CFO earlier called headcount savings "modest in the grand scheme of things" — [Q2 2026 call transcript](https://s23.q4cdn.com/407969754/files/doc_events/2026/Aug/05/Uber-Q2-26-Earnings-Call-Transcript.pdf).

### Inferences
- Est.: about $13.7B (DH) + $2.3B (ezCater) ≈ $16B of committed M&A cash, about 1.6x TTM FCF, plus the multi-year $10B AV program. This is the main reason the base case's −1.5%/yr share-count assumption is at risk over 2026–2028. It is a capital-allocation choice, not operating weakness.
- Bull view: DH gives Uber the #1 delivery position in many EMEA, MENA and Asian markets plus cross-platform synergies (cross-platform users bring about 3x the GB and profit). Bear view: Uber is buying a loss-making, litigation-heavy business at the top of its leverage range. DH's H1 2026 net loss was €392M, with €173M of legal and antitrust provisions, though H1 adjusted EBITDA was €427M and FY26 guidance was raised to €960M–1.0B — [SentiSense, 2026-08-27](https://app.sentisense.ai/stories/uber-launches-multibillion-dollar-bid-for-delivery-hero-as-it-leans-on-subscript-08272026).

### Gaps
- Final DH acceptance level, EU and other antitrust filings, and pro-forma net debt are unknown.
- The current buyback authorisation remaining was not retrieved, nor any Q3 buyback pace.
- Credit-rating agency actions on the DH deal were not found.

## Q5. Growth vectors: Uber One, advertising, other

### Takeaway
Uber One reached 50M members, driving about half of Mobility and Delivery GB (Q1 2026). Cross-platform use is still low at 20% of consumers, which leaves room to grow. Several B2B and enterprise channels are growing fast: U4B +40%, ezCater, a Costco delivery partnership, and Zipline drone delivery. I found no 2026 advertising revenue disclosure.

### Cited Findings
- Uber One had 50M members, and members drive half of GB across Mobility and Delivery (CEO) — [Q1 2026 release, 2026-05-06](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000019/uberq126earningspressrelea.htm).
- The CEO says the past twelve months added more first-time users than any period in five years — [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm).
- Only 20% of consumers use both Rides and Eats, and that cohort grows 1.5x faster. Fewer than 10% of eligible sparse-market consumers used Uber in the past 12 months, against more than 50% in dense markets. Wait & Save is growing "very, very quickly" — [Q2 2026 call transcript](https://s23.q4cdn.com/407969754/files/doc_events/2026/Aug/05/Uber-Q2-26-Earnings-Call-Transcript.pdf).
- Business-segment GB grew more than 40% in Q2 (Rosenblatt's Scott Devitt, via the ezCater coverage) — [BNN Bloomberg, 2026-10-06](https://www.bnnbloomberg.ca/business/company-news/2026/10/06/uber-to-buy-us-catering-platform-ezcater-for-us23b/).
- Zipline drone-delivery partnership (2026-08-17) and nationwide Costco delivery expansion (2026-09-30) — harness S22/S38.

### Inferences
- With members already at about 50% of GB, the next leg of membership-driven frequency gains depends more on cross-sell and sparse-market penetration than on adding members.
- Waymo Premier signals that AV operators may contest the subscription layer as well.

### Gaps
- No advertising run-rate was found in the Q1 or Q2 2026 releases or call summaries. An earlier ~$1.5B run-rate figure from 2025 could not be re-sourced here [>6m], so it is not cited.
- No Uber One retention or churn data.

## Q6. Consensus, price targets, valuation multiples

### Takeaway
At $70.35 (2026-10-16), Uber trades at about 14–15x TTM FCF, roughly 22x FY26 and 15.5x FY27 consensus EPS. That is about 30% below its October 2025 high and well below the mean sell-side target of about $101–102. The market is pricing AV disintermediation and M&A risk; consensus still assumes about 15% revenue growth into 2027.

### Cited Findings
- **Price history:**
  - $70.35 close on 2026-10-16 — harness F197 (StockAnalysis/Yahoo).
  - About $69.08 around 2026-10-07 — [FMP](https://site.financialmodelingprep.com/market-news/uber-q3-2026-earnings-call-citizens-100-price-target).
  - $76.54 on 2026-08-27 — [SentiSense](https://app.sentisense.ai/stories/uber-launches-multibillion-dollar-bid-for-delivery-hero-as-it-leans-on-subscript-08272026).
  - $78.80 on 2026-08-21 — [TIKR](https://www.tikr.com/blog/uber-has-fallen-23-from-its-high-heres-where-the-stock-could-go).
  - Below $66 on 2026-07-24, a 1-year-plus low — [The Next Web](https://thenextweb.com/news/waymo-uber-exclusivity-ends-austin-atlanta-robotaxi).
- **Prior high:** record $100.10 in October 2025, per [Bloomberg Law, 2026-08-04](https://news.bloomberglaw.com/tech-and-telecom-law/ubers-robotaxi-ambition-to-face-scrutiny-as-shares-languish). [TIKR](https://www.tikr.com/blog/uber-has-fallen-23-from-its-high-heres-where-the-stock-could-go) gives a $101.99 52-week high, likely intraday versus close.
- The stock was down about 15% YTD as of 2026-10-06 — [BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2026/10/06/uber-to-buy-us-catering-platform-ezcater-for-us23b/).
- **Price targets:**
  - Mean target $101 from 47 analysts (34 buy, 9 outperform, 6 hold, 1 sell) as of 2026-08-10 — [TIKR](https://www.tikr.com/blog/uber-stock-fell-10-this-year-can-it-bring-meaningful-upside-before-2027).
  - Mean target $101.78 from 46 analysts as of 2026-08-27 — [SentiSense](https://app.sentisense.ai/stories/uber-launches-multibillion-dollar-bid-for-delivery-hero-as-it-leans-on-subscript-08272026).
  - Citizens: Market Outperform, $100 target (2026-10-07) — [FMP](https://site.financialmodelingprep.com/market-news/uber-q3-2026-earnings-call-citizens-100-price-target).
- **Consensus estimates (MarketScreener, undated):** FY2026 revenue $57.89B, EPS $3.18; FY2027 revenue $66.77B, EPS $4.54 — [MarketScreener](https://uk.marketscreener.com/quote/stock/UBER-TECHNOLOGIES-INC-57860975/calendar/). The harness consensus FY2026 revenue was $58.28B (TickFlow, 2026-10-18, F207); the two sources differ slightly.
- Market cap to NTM FCF was 13.5x, a 7.4% forward FCF yield, at $78.80 on 2026-08-21 — [TIKR](https://www.tikr.com/blog/uber-has-fallen-23-from-its-high-heres-where-the-stock-could-go). The harness computes P/FCF at 14.27x.
- **Multiples at $70.35, est. (my arithmetic, not consensus):**
  - Market cap ≈ $70.35 × 2.050B diluted weighted shares ≈ $144B.
  - Net debt ≈ $10.73B debt − $5.4B unrestricted cash and short-term investments ≈ $5.3B, so EV ≈ $150B before equity stakes (about $3.8B equity-method plus other holdings).
  - EV / TTM FCF (>$10B) ≈ 14–15x.
  - P/E ≈ 22x FY26 and 15.5x FY27 consensus EPS (EPS basis, GAAP or non-GAAP, unspecified by the source).
  - EV / annualised Q3 adjusted EBITDA guidance midpoint ($2.91B × 4 = $11.6B) ≈ 12.9x.

### Inferences
- Despite the drawdown, the sell side remains overwhelmingly positive (about 43 of 47 buy or outperform as of August). That implies the de-rating is driven by multiple compression, especially on AV terminal-value fear, rather than estimate cuts.
- A pro-forma DH close would add about $14B+ of debt-funded EV. Multiples should be re-run on a pro-forma basis for 2028.

### Gaps
- No dated October 2026 consensus EV/EBITDA or P/FCF from a primary data vendor such as FactSet, Bloomberg or LSEG.
- No count of post-Waymo or post-DH target cuts.
- The MarketScreener EPS basis is unclear.

# NVIDIA (NVDA): long-term (5–10 year) holding fact base, as of 2026-10-18

Scope note: these notes give primary-filing figures from the FY2027 Q2 10-Q (quarter ended 2026-07-26, filed 2026-08-26), the Q2 earnings release and CFO Commentary (8-K, 2026-08-26), and the 8-Ks dated 2026-08-17 (SB Energy guarantees) and 2026-09-02 (Hugging Face). Secondary sources cover call commentary, consensus, competition and hyperscaler capex. "Harness" means the internal debate in `research/NVDA/` (report.md, redteam.json, evidence.json). Figures labelled "my calc" are my arithmetic on the cited primary numbers. They are not reported values.

Primary source URLs used throughout:
- 10-Q Q2 FY27: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
- CFO Commentary Q2 FY27 (Ex. 99.2): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm
- Press release Q2 FY27 (Ex. 99.1): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm
- 8-K 2026-08-17 (SB Energy): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm
- 8-K 2026-09-02 (Hugging Face): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm

## Harness cross-check: which debate claims does new research confirm, update or contradict?

### Takeaway
The primary filings explain almost every balance-sheet swing the debate could not resolve. The $24.1B Q2 OCF is a real figure, not an extraction error. Debt rose because of a $25B bond issue. The dividend jump is a standing policy change. DSO rose because NVIDIA gave customers extended payment terms. The SB Energy guarantee is capped at $105B. Two exposures are larger than the debate assumed: the equity-investment book (about $99B) and the Q4 gross-margin trough guide (71–72%).

### Cited Findings
- **CONFIRMED: Q2 FY27 OCF of $24.08B.** The harness flagged this as a possible extraction error (F275) because it was close to cost of revenue ($24.079B). It is real: OCF was $24,077M versus $50,344M in Q1, "driven by higher working capital adjustments and cash taxes." FCF was $21.34B in Q2 and $69.9B in H1 — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- **EXPLAINED: debt rose from $7.47B to $32.37B (F43/F44).** "In June 2026, we issued an aggregate of $25.0 billion of senior unsecured notes across seven tranches for general corporate purposes." Aggregate principal is now $33.5B. The $25B commercial paper program is undrawn, and NVIDIA is in covenant compliance — [10-Q Note 9 / risk factors](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **EXPLAINED: dividends rose from $0.24B to $6.0B (F80/F81).** This is a recurring policy change, not a one-off. "On May 18, 2026, we increased our quarterly cash dividend from $0.01 per share to $0.25 per share." The same day the board added $80.0B of buyback authorization, leaving $99.3B authorized at 2026-07-26. The next $0.25 dividend was payable 2026-10-01 — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm); [Press release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)
- **EXPLAINED: receivables rose from $40.7B to $63.1B (F180/F181).** DSO went from 45 days in Q1 to 60 days "due to extended payment terms on large, multi-quarter agreements with certain investment-grade customers" — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm). The 10-Q states: "for investment-grade customer purchases, we have and may in the future provide longer payment terms ranging from 90 days up to one year" — [10-Q Note 7](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). The harness computed FY2026 DSO of 65.0 days on an annual basis. NVIDIA's own quarterly DSO was 45 days in Q1 and 60 days in Q2, so the two figures use different bases.
- **EXPLAINED: inventory rose from $25.8B to $31.6B (F133/F134).** NVIDIA says this was "as we prepare for the introduction of Vera Rubin in the third quarter" — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm). Raw materials were $11.34B versus $3.81B at 2026-01-25. Work in process was $13.38B versus $8.82B. Finished goods *fell* to $6.86B from $8.77B — [10-Q Note 7](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **EXPLAINED: deferred revenue rose from $1.71B to $4.62B (F61/F62).** Current deferred revenue included "$2.8 billion and $160 million of customer advances" at 2026-07-26 and 2026-01-25 respectively. In H1, deferred-revenue additions were $17.7B, of which $15.6B were customer advances. Remaining performance obligations on contracts longer than one year were only $3.2B — [10-Q Note 7](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **QUANTIFIED: the SB Energy guarantee (S40), which the harness could not size.** The guarantee is "capped at a total of $105 billion." It is a residual value guaranty for about 4.25 GW of leases to an OpenAI affiliate, and NVIDIA holds an option on about 3.8 GW more. It becomes effective phase by phase from FY2029; the 8-K says ready-for-service "expected beginning in 2028." Exposure declines as lease payments are made, and the guarantee terminates if OpenAI reaches a satisfactory credit rating. OpenAI agreed to reimburse NVIDIA — [8-K 2026-08-17](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm); [10-Q Note 10](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **QUANTIFIED: the Hugging Face deal (S27), which the harness could not size.** The price is "approximately $11.9 billion" plus "an equity-based retention program of up to approximately $1.0 billion." Closing is expected in the first half of 2027 — [8-K 2026-09-02](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm). Press reports of about $13B ([Semafor](https://semafor.com/article/09/03/2026/nvidia-to-buy-hugging-face-for-nearly-13-billion)) appear to combine the two amounts.
- **UPDATED: Q3 gross-margin guidance (F251) is the start of a deeper dip.** According to secondary reports of the call, Kress guided a Q4 FY27 trough of 71–72% and 72–73% for FY2028 "as price increases take effect." Kress said memory pricing "has exceeded our prior expectations" and will go "even higher into next year" — [Implicator.ai, 2026-08-26](https://www.implicator.ai/nvidia-70-percent-growth-forecast-margin-outlook/); [Motley Fool via Nasdaq, 2026-08-27](https://www.nasdaq.com/articles/nvidias-supply-commitments-more-doubled-279-billion-heres-what-it-does-stock). I found no primary transcript.
- **PARTLY CORROBORATED: FY2028 growth of about 70% (F253).** Several secondary reports quote Huang: "Even though our demand is much greater than 70%, our supply allows us to confidently deliver 70%." Analysts had modelled about 44% — [Implicator.ai](https://www.implicator.ai/nvidia-70-percent-growth-forecast-margin-outlook/). Still no primary transcript.
- **CONTRADICTED: the harness gap that "consensus is absent."** The FY2028 consensus EPS was $15.68 (versus $12.82 thirty days earlier, with 42 upward and 0 downward revisions) and the consensus price target was $327.70, as of 2026-09-22 — [24/7 Wall St, 2026-09-22](https://247wallst.com/investing/2026/09/22/nvidia-price-prediction-wall-street-and-our-model-finally-agree/)
- **CONTRADICTED: the harness gap that "customer concentration is unknown."** Concentration is disclosed. One direct customer was 16% of Q2 revenue. In H1, three direct customers were 16%, 15% and 13%. Five direct customers held 22%, 14%, 13%, 11% and 10% of receivables — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)

### Inferences
- The debate's accounting "watch" items now have stated causes. Most of them are structural, not one-off: the dividend policy, the extended payment terms ("may in the future"), the memory pre-buy and the bond issue are all choices NVIDIA has said it may repeat. The Rubin inventory build is the only clearly transitional item.
- The redteam's debt signal (`debt > 40e9`) is not tripped at $32.4B. The CP program could trip it without any new bonds, because it adds up to $25B of capacity.
- The redteam's gross-profit signal (`gross_profit < 72.1e9`) is unlikely to trip in Q3: $108B at 74% gives about $79.9B (my calc). In Q4 at 71.5%, revenue would have to fall below about $100.9B for gross profit to drop below $72.1B (my calc).
- The harness's base-case FY2028 revenue of $599B (+50%) sits well below management's about-70% supply-backed outlook. The harness bear case starts from an even lower point. The gap between management and the base case is now a verifiable variant view, no longer an unknown.

### Gaps
- No primary call transcript was retrieved, so the margin trough, the 70% figure and the "Rubin ~20% of Q3 Data Center revenue" figure rest on secondary summaries.
- Harness claim S38 (a $150B buyback increase on 2026-09-28) appears only in a NVIDIA newsroom item. The SEC filing list shows no 8-K for it (filings through 2026-10-13 checked), so I could not verify it against a filing.

## Latest reported quarter (FY2027 Q2) and Q3 guidance

### Takeaway
Q2 FY27 revenue was a record $96.2B (+106% YoY), with Data Center at $89.0B and a 75.0% gross margin. Cash conversion was weak: OCF was $24.1B against $59.7B of GAAP net income, and $7.8B of that net income was non-cash equity-investment gains. Q3 guidance is $108B ±2% at 74.0% ±0.5pt gross margin, with no China Data Center compute assumed. The next report is expected around 2026-11-18, but NVIDIA has not confirmed the date.

### Cited Findings
- **Revenue and margin:** revenue was $96,221M (Q1: $81,615M; Q2 FY26: $46,743M), up 18% QoQ and 106% YoY. GAAP gross margin was 75.0%, versus 74.9% in Q1 and 72.4% a year earlier — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- **Profit and EPS:** GAAP opex was $8,408M (+55% YoY) and operating income $63,734M. GAAP net income was $59,688M ($2.46/share). Non-GAAP net income was $53,954M ($2.22/share) — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- **Non-GAAP now includes SBC:** "Beginning in the first quarter of fiscal 2027, NVIDIA's non-GAAP financial measures no longer exclude stock-based compensation expense" — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- **Segments:** Compute & Networking was $88,299M (+114% YoY) and Graphics $7,922M (+46%) — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- **Market platforms (new presentation since Q1 FY27):** Data Center was $89,023M (+117% YoY). Within it, Hyperscale was $48,710M (+102% YoY, +13% QoQ) and AI Clouds, Industrial & Enterprise (ACIE) $40,313M (+138% YoY, +25% QoQ). Edge Computing was $7,198M (+27%). One company was reclassified from ACIE to Hyperscale — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- **Compute vs networking:** NVIDIA no longer gives a separate compute versus networking split for Data Center. The 10-Q and CFO Commentary report only the Hyperscale/ACIE split and the Compute & Networking segment — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). The Next Platform *estimates* NVIDIA's trailing-twelve-month Ethernet plus NVSwitch interconnect sales at about $25.7B (an estimate, not reported) — [Next Platform, 2026-08-31](https://nextplatform.com/connect/2026/08/31/in-the-long-run-nvidia-nvswitch-is-the-infiniband-of-scale-up-ai-networks/5293474)
- **Other income:** net gains from equity securities were $7.77B in Q2 and $15.94B in Q1 ($23.7B in H1). Interest expense was $227M in Q2 versus $62M a year earlier. The effective tax rate was 16.5% — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Cash flow:** H1 OCF was $74.4B. Working-capital uses in H1 were: receivables −$24.6B, inventories −$10.2B, prepaid and other assets −$6.5B. Partial offsets were accounts payable +$4.1B and accrued liabilities +$8.0B. H1 capex was $4.4B; Q2 capex was $2.68B — [10-Q cash-flow statement](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Q3 FY27 outlook:** revenue $108.0B ±2%, "not assuming any Data Center compute revenue from China." GAAP and non-GAAP gross margin 74.0% ±50bp. GAAP opex about $9.2B and non-GAAP about $9.0B. FY27 tax rate 16–18% — [Press release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)
- **Call commentary (secondary):** Vera Rubin is about 20% of Q3 Data Center revenue; the gross margin trough is 71–72% in Q4 and 72–73% in FY28; FY28 growth is about 70% — [Platform Aeronaut AI summary](https://transcripts.platformaeronaut.com/summaries/NVDA-2Q27-AI-Summary); [Implicator.ai](https://www.implicator.ai/nvidia-70-percent-growth-forecast-margin-outlook/)
- **Consensus at the time of the print:** about $104B for Q3 revenue (range $103.9–104.6B), which the harness already recorded (F252). The market expected 72.6% Q3 gross margin, according to Melissa Otto of S&P Global Visible Alpha — [Implicator.ai](https://www.implicator.ai/nvidia-70-percent-growth-forecast-margin-outlook/)
- **Next earnings date:** Wednesday 2026-11-18 after market close, *estimated, not confirmed* by NVIDIA — [days.to](https://days.to/nvidia-earnings)

### Inferences
- GAAP net income now carries large mark-to-market investment gains: $23.7B in H1, about 17% of H1 pre-tax income of $141.4B (my calc). The harness's GAAP P/E of 26.96x is therefore partly inflated by gains. Non-GAAP EPS, which excludes the gains but includes SBC, is the cleaner measure of earnings power.
- Q3 guidance implies about +12% QoQ (my calc), slower than Q2's +18%. Combined with the margin trough guide, operating leverage should slow in H2 FY27 even as revenue grows.
- H1 OCF of $74.4B against $99.5B of non-GAAP net income gives roughly 75% conversion (my calc). Q2 alone was about 45% ($24.1B / $54.0B). The extended payment terms are a deliberate trade of cash for volume.

### Gaps
- No primary transcript, so call-only items (Rubin share, the FY28 range, networking color) could not be verified.
- The compute versus networking split is no longer disclosed, so the networking attach trend cannot be tracked from primary sources.

## Working capital, supply commitments, prepaid supply and debt: one-off or trend?

### Takeaway
The swings are mostly deliberate and likely to persist. NVIDIA is pre-buying scarce memory, with supply commitments up from $119B to $279B in one quarter. It is extending terms of 90 days to one year to investment-grade buyers, and it is funding shareholder returns and investments partly with debt. The inventory mix (raw materials up, finished goods down) points to supply-securing, not unsold product. Concentration of receivables and the size of the forward commitments are the real risk.

### Cited Findings
- **Supply commitments:** "Supply and capacity" commitments were $279B ($92B in the rest of FY27, $87B in FY28, $88B in FY29, $12B later), up from $119B a quarter earlier, "primarily related to the procurement of memory." Some agreements "may be cancelable, rescheduled, or adjustable … prior to placing firm orders" — [10-Q Note 10](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Total commitments:** $366B in total, including cloud service agreements $29B, data-center leases not commenced $25B, equity investments $25B and capex $8B — [10-Q Note 10](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Inventory provisions:** inventory and excess-purchase-obligation provisions were $985M in Q2 and $2.1B in H1, a 0.8pt hit to Q2 gross margin. Excess inventory purchase obligations accrued were $2.14B (versus $2.74B at January). There was a $0.4B H200 charge in H1 FY27 — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Receivables concentration:** five direct customers held 22%, 14%, 13%, 11% and 10% of receivables at 2026-07-26 (70% combined). At 2026-01-25, three held 25%, 18% and 13% — [10-Q Note 7](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Payment terms:** extended terms "ranging from 90 days up to one year" for investment-grade customers with large data-center builds — [10-Q Note 7](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). DSO was 60 days versus 45 days QoQ — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- **Prepaids:** prepaid expenses and other current assets were $3.41B (versus $3.18B). Other long-term assets were $15.75B (versus $8.30B). The H1 cash outflow for "prepaid expenses and other assets" was $6.48B — [10-Q balance sheet and cash-flow statement](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). I found no explicit "prepaid supply agreement" line item.
- **Debt:** $25.0B of senior notes issued in June 2026 across seven tranches, including 5.625% notes due 2056. Net carrying amount is $33.37B and estimated fair value $31.4B. CP capacity is $25B, undrawn — [10-Q Note 9](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Liquidity:** cash, equivalents and marketable debt securities were $56.6B, plus $42.8B of marketable equity securities — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Secondary read on commitments:** about $267B of the commitments fall due by end-FY29. The author reads this as stockpiling a scarce input ahead of further memory price rises — [Motley Fool via Nasdaq, 2026-08-27](https://www.nasdaq.com/articles/nvidias-supply-commitments-more-doubled-279-billion-heres-what-it-does-stock)

### Inferences
- **Bull read:** raw materials tripled while finished goods fell, which looks like securing supply ahead of the Rubin ramp, not a demand air-pocket. $267B of commitments through FY29 is consistent with the about-70% FY28 outlook, given $177.8B of H1 FY27 revenue.
- **Bear read:** $279B of mostly memory commitments, bought at "extreme" memory prices, creates a large fixed obligation. If demand or pricing falls in FY28–FY29, provisions on excess purchase obligations could be far larger than the $4.5B H20 charge of FY26. Only part of the commitments is cancelable.
- **Funding:** shareholder returns plus net investment flows exceeded FCF in H1 FY27 (all my calc from the 10-Q cash-flow statement). The uses were buybacks $39.0B, dividends $6.3B, net equity-security purchases $35.2B (purchases $42.4B less sales $7.2B) and a $2.9B Groq payment, about $83B in total, against $69.9B of FCF. The roughly $13B gap was covered by the $24.9B of debt proceeds. This supports the redteam's "returns/investments funded partly by debt" pre-mortem point, although leverage is still low.

### Gaps
- No primary disclosure isolates prepaid supply or capacity agreements (for example memory prepayments) inside other assets.
- Which customers are on extended terms is not disclosed.
- The 10-Q does not split cancelable versus non-cancelable supply commitments.

## "Circular financing": equity stakes, guarantees and capacity agreements

### Takeaway
NVIDIA's support of its own customers is now very large. It holds about $99B of equity investments (versus about $40B in January 2026), has committed another $25B, and carries up to $108.5B of lease guarantees, most of which support OpenAI. It also has $36B of AI-cloud capacity agreements and $20B of third-party data-center leases. My rough sum of these items is close to TTM revenue, although much of it is contingent and spread over many years. Management rejects the "circular" label. The 10-Q confirms that an AI lab (NVIDIA calls it an "AI research and deployment company") is a "meaningful" indirect revenue source.

### Cited Findings
- **Equity holdings:** marketable equity securities were $42.78B (versus $12.89B at 2026-01-25), plus $4.96B of long-term locked-up public equity in other assets. $36.9B of the public holdings are under short-term lock-ups — [10-Q Note 5](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Non-marketable equity:** the balance went from $22.25B (January) to $47.90B (July). H1 net additions were $31.0B and unrealized gains $7.5B, with $12.7B reclassified to marketable "following public market trading." Cumulative unrealized gains are $9.1B. The balance-sheet line for non-marketable securities is $51.16B — [10-Q Note 6](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Equity-method stakes:** $3.3B in "infrastructure financiers," with variable-interest-entity maximum loss exposure of $4.7B — [10-Q Note 6](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Committed investments:** future equity investment commitments of $25B (of which $18B falls in the rest of FY27) "in AI model makers, infrastructure financiers, and other private companies" — [10-Q Note 10](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Guarantees:** maximum gross exposure of $108.5B, made up of SB Energy/OpenAI $105.0B plus land, power and shell guarantees for AI clouds of $3.5B — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- **AI cloud agreements:** $36B (FY28–FY32+). AI clouds buy NVIDIA infrastructure while NVIDIA commits to cloud-service purchases. The AI clouds "can unilaterally stop providing to us and sell to third-party customers at more advantageous rates," and NVIDIA may receive a revenue share. There are also $20B of third-party data-center leases that NVIDIA "expect[s] to reassign … to third parties" — [10-Q Note 10](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Indirect AI-lab revenue:** "We estimate that one AI research and deployment company contributed a meaningful amount of our revenue by purchasing cloud services from our customers" in Q2 and H1 FY27 — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Third-party financing platforms:** memoranda of understanding with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR to "mobilize over $500 billion of third-party capital … subject to definitive agreements" — [Press release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm). The 10-Q warns these "may not lead to definitive agreements" — [10-Q risk factors](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **OpenAI stake (Feb 2026, reported; older than 6 months):** NVIDIA planned to invest $30B in OpenAI's round at a $730B pre-money valuation, replacing the September 2025 letter of intent for up to $100B. CNBC reported the $30B was not tied to deployment milestones — [DatacenterDynamics, 2026-02-20](https://www.datacenterdynamics.com/en/news/nvidia-plans-30bn-investment-in-upcoming-openai-funding-round/)
- **2026 deal flow (reported, 2026-05-10):** more than $40B of AI equity commitments in January–April 2026, including OpenAI $30B, Corning up to $3.2B, IREN up to $2.1B, Nebius $2B (with a 5 GW deployment commitment) and CoreWeave $2B (stake about $4.4B). CoreWeave's $6.3B capacity-purchase agreement with NVIDIA is "the most-cited case" — [TNW, 2026-05-10](https://thenextweb.com/news/nvidia-40bn-ai-equity-investments-2026)
- **Management's position:** Kress said, "We recognize the scale of this support, and we know some will call this circular financing. We see it differently." Independent capital underwrites the deals and NVIDIA makes no loans — [Implicator.ai, 2026-08-26](https://www.implicator.ai/nvidia-70-percent-growth-forecast-margin-outlook/)
- **PORTS-Pike economics:** NVIDIA says each generation deployed at the site "could represent approximately 1.5 million NVIDIA GPUs, or approximately $150 billion to $200 billion in NVIDIA revenue" — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- **OpenAI risk factor:** if OpenAI "becomes subject to an insolvency event," NVIDIA "may assume long-term lease obligations … or make substantial payments," and "we may not recover amounts promptly or in full" — [10-Q risk factors](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)

### Inferences
- **Scale (my calc, using TTM revenue of about $303B):** equity holdings of about $99B are about 33% of TTM revenue and about 31% of total assets ($320.3B). Guarantees of $108.5B are about 36% of TTM revenue. Adding holdings, committed equity, guarantees, AI-cloud agreements and third-party leases gives roughly $288B, about 95% of TTM revenue. This is an upper-bound mix of contingent and multi-year items, not current exposure.
- **The OpenAI link:** NVIDIA is simultaneously an equity holder (about $30B reported), guarantor of up to $105B of leases, and seller of the hardware that site will host ($150–200B of revenue per generation, per NVIDIA). OpenAI is very likely the unnamed "AI research and deployment company" that is a meaningful indirect customer (inference; the 10-Q does not name it). OpenAI's credit is therefore the largest single risk factor in the thesis.
- **Effect on reported earnings:** H1 gains of $23.7B, mostly from 2026 investments that later traded publicly, mean a downturn would hit GAAP earnings twice: lower GPU demand and mark-to-market losses. Non-GAAP excludes the gains.
- **Bull counterpoint:** most stakes are minority positions. The guarantees only become effective when sites are ready for service (FY2029 onward), decline over time, and end if OpenAI reaches investment grade. NVIDIA reports that equity-method income is insignificant, and the investments buy long-dated exclusive capacity ("exclusively host NVIDIA AI infrastructure").

### Gaps
- No primary disclosure of individual holding sizes (OpenAI, Anthropic, xAI, CoreWeave, Intel and others) appears in the 10-Q.
- I did not find an independent sell-side or credit-agency quantification of how much revenue is "supported" by NVIDIA financing.
- I did not verify the size or status of an Anthropic or xAI stake in this pass.

## Hyperscaler capex (2026–2027) and customer concentration

### Takeaway
2026 capex guidance from the big four is about $720–745B, plus Oracle's net about $70B (FY27). Moody's sees close to $1T in 2027. Calendar Q3 hyperscaler results (late October 2026) had not been reported as of 2026-10-18. Inside NVIDIA, the largest single direct customer was 16% of Q2 revenue. Hyperscale was 55% of Data Center revenue (my calc), and ACIE (neoclouds, AI labs, sovereigns, enterprise) is the faster-growing part.

### Cited Findings
- **Guidance from the July/August 2026 calls (secondary):**
  - Microsoft: about $175B for calendar 2026 (last quarter $41.0B). The article cites about $255B for FY27 but says management gave no FY27 target.
  - Amazon: about $220B (last quarter $53.1B).
  - Alphabet: $195–205B (last quarter $44.9B).
  - Meta: $130–145B, including finance-lease principal (last quarter $31.1B).
  - Oracle: about $70B for FY27 net of customer prepayments ($90–95B gross; last quarter $16.5B).
  - Source: [Motley Fool, 2026-08-03](https://www.fool.com/investing/2026/08/03/microsoft-and-amazon-won-the-ai-spending-week/)
- **Moody's (2026-05-14):** 2026 hyperscaler capex forecast raised to $785B from $700B, with 2027 to "close in on $1 trillion." Capex is "eating into their operating cash flow" and debt and leases are rising — [DatacenterDynamics, 2026-05-14](https://datacenterdynamics.com/en/news/moodys-hyperscaler-capex-forecasts-marked-up-by-85bn-to-close-in-on-1trn-by-2027/)
- **NVIDIA concentration:** one direct customer was 16% of Q2 FY27 revenue. In H1, three were 16%, 15% and 13%. In Q2 FY26, two were 23% and 16%. NVIDIA also has "a limited number of indirect customers, some individually representing 10% or more of our revenue" — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Geography (by customer headquarters):** in Q2, US was $60.1B, Taiwan $27.0B and China including Hong Kong $7.9B. 38% of revenue came from customers headquartered outside the US — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Breadth of demand (CEO, 2026-08-26):** "This time last year, one lab alone was driving the buildout; today, we have … multiple frontier labs scaling in parallel" — [Press release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)

### Inferences
- Direct-customer concentration, measured by the largest customer, fell from 23% to 16% year over year. Exposure has shifted toward indirect AI-lab demand and NVIDIA-supported neoclouds (ACIE grew 138% YoY), so headline concentration figures understate dependence on a few model makers.
- Big-four 2026 capex of about $720–745B against NVIDIA's annualized Data Center run-rate of about $356B (Q2 × 4, my calc) means NVIDIA is capturing a very large share of hyperscaler capex plus non-hyperscaler spend. Any capex flattening in 2027 would transmit quickly.

### Gaps
- No primary hyperscaler transcripts were retrieved. Calendar 2027 capex guidance from individual companies is largely unavailable until the late-October and January calls.
- The Microsoft FY27 figure of about $255B is attributed by the article but was not given as company guidance.

## Competition: custom ASICs, AMD and open rack architectures

### Takeaway
NVIDIA still holds a commanding share: about 81% of AI chips per IDC (undated), and an estimated 95% of GPU revenue or 75% of GPU+XPU revenue per The Next Platform. Credible second sources are scaling: Google TPUs sold externally to Anthropic and Meta, AMD's 6 GW OpenAI and 6 GW Meta MI450 deals starting H2 2026, and the open scale-up standards UALink and ESUN. Analysts expect NVLink/NVSwitch lock-in to hold through about 2027 and erode slowly after that.

### Cited Findings
- **Google TPU:**
  - Anthropic plans to buy up to 1M TPUs, about 1 GW in 2026, "worth tens of billions of dollars" (announced October 2025; older than 6 months).
  - Meta reportedly signed a multibillion-dollar TPU rental deal (February 2026).
  - Google is reportedly adding Marvell as an ASIC designer.
  - IDC: NVIDIA has about 81% of the AI chip market. DA Davidson's Luria: TPUs could take 20%.
  - Source: [Motley Fool, 2026-04-25](https://fool.com/investing/2026/04/25/meet-biggest-threat-nvidia-ai-chips-its-not-amd)
- **AMD:** OpenAI up to 6 GW and Meta up to 6 GW, each starting with a 1 GW MI450 deployment in H2 2026. Meta holds a warrant for up to 160M AMD shares at $0.01. AMD's Q1 2026 Data Center revenue was $5.8B (+57%). Helios is positioned as open and standards-based versus NVLink — [TradingKey via Tiger, 2026-07-20](https://www-web.itiger.com/news/2652214129)
- **Scale-up networking:**
  - NVSwitch keeps dominance "through at least calendar 2027," losing only a few points of share.
  - NVLink Fusion is an attempt "to stall the inevitable for another generation or two."
  - UALink 1.0 scales to 1,024 XPUs in one tier, versus 576 GPUs in two tiers for NVSwitch.
  - Helios uses Broadcom Tomahawk 6 Ethernet. Broadcom has reportedly walked away from UALink.
  - NVIDIA bought $3.5B of MediaTek convertible bonds tied to NVLink Fusion access.
  - Source: [Next Platform, 2026-08-31](https://nextplatform.com/connect/2026/08/31/in-the-long-run-nvidia-nvswitch-is-the-infiniband-of-scale-up-ai-networks/5293474)
- **NVIDIA–Marvell:** Tom's Hardware headline: "Nvidia invests $2 billion in Marvell — NVLink Fusion turns into soft ecosystem lock-in." The headline is all I have; I did not fetch the article or confirm its date — [Tom's Hardware](https://tomshardware.com/tech-industry/nvidia-invests-2-billion-in-marvell-whose-biggest-clients-are-trying-to-replace-nvidia-chips)
- **Open-standard momentum:** Cornelis plans to build a scale-up interconnect using UALink and ESUN (headline only) — [HPCwire, 2026-09-14](https://www.hpcwire.com/aiwire/2026/09/14/cornelis-to-build-scale-up-interconnect-using-ualink-and-esun/)
- **NVIDIA's own disclosure:** the effective China foreclosure "helped our competitors build larger developer and customer ecosystems to challenge us worldwide" — [10-Q risk factors](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **NVIDIA's competitive moves:** the Groq 3 LPX inference accelerator is "now in full production" — [Press release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm). NVIDIA made a $2.94B H1 payment related to a "Groq, Inc. non-exclusive license agreement" — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). The Hugging Face deal comes with a pledge to keep the platform open and "support other silicon vendors" — [8-K 2026-09-02](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm)

### Inferences
- **Margin pressure:** the bigger near-term threat to margins is memory cost, not ASIC share. Gross margin is guided down to 71–72% in Q4 on memory pricing (secondary sources). Over a 5–10 year horizon, TPU externalization and AMD's anchor deals with two of the top three labs give buyers real alternatives. Pricing power, not volume, is what gets tested.
- **Hedging lock-in risk:** NVIDIA is hedging rack-level lock-in risk by licensing NVLink Fusion, investing in ASIC partners (Marvell, MediaTek), buying Groq IP and acquiring Hugging Face. This turns potential competitors into ecosystem participants, and it also signals that management sees lock-in as finite.

### Gaps
- I found no current, dated market-share estimate split by accelerator type for 2026.
- No specific Trainium 3/4 or MTIA volume data was found in this pass.
- Broadcom's AI revenue guidance comes only as an undated secondary mention ("$100 billion … next year").

## Roadmap, China, and physical AI

### Takeaway
Vera Rubin began production shipments in Q3 FY27 and is about 20% of Q3 Data Center revenue (secondary). Rubin CPX is expected at end-2026, Rubin Ultra in H2 2027 and Feynman in 2028 (secondary). China Data Center compute is effectively zero: NVIDIA describes itself as "effectively foreclosed," and guidance assumes no China revenue. That gives upside optionality but no base-case contribution. Physical AI and robotics have no disclosed revenue.

### Cited Findings
- **Rubin:** "Vera Rubin, began production shipments in the third quarter of fiscal year 2027 … currently experiencing certain supply constraints" — [10-Q MD&A](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). Vera Rubin racks are running at CoreWeave, Google Cloud, Microsoft Azure, OCI and Nebius — [Press release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)
- **Roadmap (secondary, page dated June 2026):** Vera Rubin entered full production on 2026-06-01. Rubin CPX (NVL144 CPX) availability is at end-2026. Rubin Ultra (Kyber NVL576) is H2 2027. Feynman is 2028 — [VRLA Tech](https://vrlatech.com/nvidia-gpu-roadmap-2026-2030/)
- **Rubin mix and visibility:** Rubin is about 20% of Q3 Data Center revenue (secondary) — [Platform Aeronaut](https://transcripts.platformaeronaut.com/summaries/NVDA-2Q27-AI-Summary). NVIDIA has estimated about $1T of Blackwell plus Vera Rubin sales across 2026–2027 (secondary, undated) — [Motley Fool, 2026-04-25](https://fool.com/investing/2026/04/25/meet-biggest-threat-nvidia-ai-chips-its-not-amd)
- **China status:**
  - The US government granted licenses for small amounts of H200, but "such sales were restricted by the PRC government."
  - NVIDIA took a $0.4B H200 charge in H1 FY27, and H200 shipments were less than 1% of Data Center revenue.
  - The licenses carry a 25% tariff that NVIDIA has been "unable to pass along."
  - NVIDIA was "effectively foreclosed from competing in China's data center computing/compute market."
  - Pending risks include the GAIN AI Act and the Remote Access Security Act.
  - Source: [10-Q risk factors](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **China background (January 2026):** BIS moved H200 to case-by-case review on 2026-01-13. Chinese customs blocked H200 clearance on 2026-01-14 — [Fintool, 2026-01-18](https://fintool.com/news/china-blocks-nvidia-h200-customs)
- **Physical AI and robotics:** NVIDIA has cloud-service commitments of $29B to support R&D on "Nemotron, Cosmos, and GR00T, and our autonomous vehicle software" — [10-Q Note 10](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). Edge Computing (workstations, PC, and presumably auto and robotics) was $7.2B, +27% YoY, "driven by strong sales of Blackwell workstations" — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)

### Inferences
- **China:** with guidance assuming zero China Data Center compute, the harness's view that China is not additional downside is confirmed. The remaining China risk is indirect: competitors' ecosystems are strengthening, and the proposed Remote Access Security Act could restrict cloud access for China-parented firms worldwide.
- **Physical AI:** this remains an option on the 5–10 year view, not a measurable revenue line. NVIDIA is spending heavily on it, as the $29B of cloud commitments for model R&D shows.

### Gaps
- No B30A status was found in the filings or sources consulted. The 10-Q discusses only H200 licensing.
- No robotics, automotive or Thor revenue is disclosed under the new market-platform structure.
- No primary confirmation of Rubin CPX timing was found in this pass.

## ROIC, SBC, share count and buybacks

### Takeaway
SBC is small: about 2.1% of revenue in Q2 FY27. The share count is shrinking about 1% a year, buybacks are about $20B a quarter, and the dividend now runs at roughly $6B a quarter. ROIC remains very high but is being diluted by the much larger balance sheet, specifically the equity investments, receivables and inventory.

### Cited Findings
- **SBC:** $2,027M in Q2 and $3,955M in H1 — [10-Q equity statement](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). Q2 SBC was 2.1% of revenue (my calc: $2.03B / $96.2B). The harness puts FY2026 SBC at 3.0% of revenue — [harness report.md L3 table]
- **Share count:** weighted diluted shares were 24,285M in Q2 FY27, 24,391M in Q1 and 24,532M in Q2 FY26, about −1.0% YoY (my calc). Shares outstanding were 24,147M at 2026-07-26 — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **Buybacks:** 94M shares for $19.7B in Q2 and 203M shares for $39.8B in H1 FY27. That implies average prices of about $209 in Q2 and about $196 in H1 (my calc). Authorization remaining was $99.3B at 2026-07-26 — [10-Q Note 12](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). A further $150B increase was announced on 2026-09-28, per the NVIDIA newsroom (harness S38; no 8-K located).
- **Total returns:** "nearly $26.0 billion" was returned in Q2 through buybacks and dividends — [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)
- **Harness ROIC series:** 158.5% in FY2025 and 71.3% in FY2026 — [harness report.md L3 table]

### Inferences
- The dividend at $0.25 a quarter on about 24.1B shares is about $24B a year (my calc). Combined with buybacks of about $80B a year at the H1 pace, committed returns of about $100B+ a year are close to TTM FCF of about $127B (my calc). Combined with $25B of committed equity investments and the pending $11.9B Hugging Face deal, that leaves little FCF slack if FY28 cash conversion stays at about 45–75%. Further debt or CP use is plausible.
- The ROIC decline in FY2026 is consistent with capital being redeployed into equity stakes, working capital and acquisitions (goodwill rose to about $21B). The returns on those stakes will show up mainly as volatile non-operating gains, not operating ROIC.

### Gaps
- I did not compute a primary-source ROIC for FY27 to date, because invested-capital definitions vary. The harness figures are the only computed series.
- No check of buyback timing against price levels beyond the implied average prices above.

## Consensus estimates, price targets and valuation multiples

### Takeaway
At $214.13 (close 2026-10-16), NVDA trades at about 27x trailing GAAP earnings, which include investment gains. It trades at about 13.7x consensus FY2028 EPS of $15.68 (as of 2026-09-22) and about 41x trailing FCF. The roughly 3x gap between EV/FCF and the forward P/E reflects the working-capital drag on cash conversion and expected earnings growth. The consensus price target of about $328 (as of 2026-09-22) is about 53% above the current price.

### Cited Findings
- **Price:** $214.13 close on 2026-10-16. The 52-week range was $164.27–243.37 — [harness evidence S45/S48]
- **Consensus (as of 2026-09-22):** consensus price target $327.70 and FY2028 EPS $15.68 (versus $12.82 thirty days earlier; 42 upward and 0 downward revisions). The stock was $227.50 and the trailing P/E about 28x on that date — [24/7 Wall St, 2026-09-22](https://247wallst.com/investing/2026/09/22/nvidia-price-prediction-wall-street-and-our-model-finally-agree/)
- **Pre-print targets (2026-08-24):** Rosenblatt Buy $325, Cantor Overweight $350, KeyBanc Overweight $330 — [SentiSense, 2026-08-24](https://app.sentisense.ai/stories/analysts-maintain-bullish-stance-on-nvidia-with-buy-ratings-and-325-350-price-ta-08242026)
- **Multiples at the print:** about 27x trailing P/E and about 16x forward P/E (next fiscal year) at roughly $210 on 2026-08-26 — [Motley Fool via Nasdaq, 2026-08-27](https://www.nasdaq.com/articles/nvidias-supply-commitments-more-doubled-279-billion-heres-what-it-does-stock)
- **Harness multiples at $214.13:** P/E 26.96x, P/FCF 40.94x, EV $5.21T, EV/revenue 17.2x, FCF yield 2.4% — [harness report.md]
- **TTM FCF (my calc):** H2 FY26 of $57.1B (FY26 $96.7B less H1 FY26 $39.6B) plus H1 FY27 of $69.9B gives about $127B, consistent with the harness P/FCF. Inputs: [CFO Commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm) and harness FY26 FCF.

### Inferences
- **Forward P/E (my calc):** $214.13 / $15.68 ≈ 13.7x FY2028 consensus EPS. Consensus non-GAAP now includes SBC but excludes investment gains, so this multiple is not inflated by investment marks. It is low for a company guiding about 70% growth. It also implies the market heavily discounts the durability of FY28 earnings, which fits the harness's view that growth is front-loaded.
- **Variant check versus the harness:** the harness's base-case intrinsic value of $235.52 sits about 28% below the consensus price target. The harness is materially more conservative than the Street, mainly on its exit multiple of 22x FCF and FCF margin of 40%.
- **FCF basis matters:** EV/FCF of about 41x is inflated by the extended payment terms and memory pre-buys. If DSO normalizes, FCF would catch up toward earnings. If the terms are permanent, about 41x is the right lens.

### Gaps
- No current (October 2026) consensus price-target distribution (high/low, rating mix) or FY2027/FY2028 revenue consensus in dollars was found.
- The FY2028 EPS consensus comes from one secondary aggregator. Its basis (non-GAAP including SBC) was not confirmed.

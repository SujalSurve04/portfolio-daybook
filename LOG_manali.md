# Portfolio Daybook — running log (Manali's account)

This file is Manali's portfolio's institutional memory — a separate account from
`LOG.md` (Sujal's). Each run reads this whole file before writing anything, then
prepends a new entry at the marker below. **Never delete or rewrite past
entries** — only append above the marker, and note inside a new entry when an
old watch item resolves.

<!-- NEW_DAY_ENTRY_INSERT_ABOVE -->

## Day 1 — Sunday, 23 Aug 2026

**Baseline established — diagnosis: sizing, not stock-picking.** First real read
on the book, via `scripts/fetch_holdings.py manali` (credentials added today).
32 holdings, ₹4,01,774.31 invested, ₹4,18,123.80 current value, **+4.07%
overall**, as of Friday 21 Aug close (market shut for the weekend — same
session Sujal's Day 2 used). This account is genuinely the "major investment,
very low returns" case flagged before any data existed. Now there's a specific,
evidenced reason why: several real winners (some up 60–100%+) are sitting in
undersized positions, while the single **largest** position (TCS, 10.5% of the
book) is a loser fighting a real sector-wide headwind. The stock-picking here is
mostly good. The sizing discipline is the problem.

| Symbol | Bucket | Qty | Avg | LTP (21 Aug) | P&L | Alloc% | Action |
|---|---|---|---|---|---|---|---|
| TCS | Compounder | 19 | 2673.82 | 2302.00 | −13.9% | 10.5% | Hold, no add |
| SRF | Compounder | 15 | 2373.72 | 2572.00 | +8.4% | 9.2% | Hold |
| ASIANPAINT | Compounder | 13 | 2581.74 | 2630.80* | +1.9% | 8.2% | Hold |
| HAL | Compounder | 5 | 3077.36 | 5000.00 | +62.5% | 6.0% | Hold |
| NIFTYBEES | Index/Hedge | 90 | 264.21 | 276.83 | +4.8% | 6.0% | Hold |
| BAJFINANCE | Compounder | 20 | 660.24 | 1095.00 | +65.9% | 5.2% | Hold |
| MAZDOCK | Satellite | 7 | 2244.07 | 2552.00 | +13.7% | 4.3% | Hold |
| GOLDBEES | Index/Hedge | 135 | 64.61 | 131.32 | +103.3% | 4.2% | Trim into strength |
| BEL | Compounder | 40 | 404.25 | 414.00 | +2.4% | 4.0% | Hold |
| IRFC | Satellite | 185 | 124.73 | 86.35 | −30.8% | 3.8% | Watch closely |
| HDFCBANK | Compounder | 20 | 726.76 | 731.10 | +0.6% | 3.5% | Hold, watch governance |
| TMCV | Compounder | 33 | 273.59 | 472.55 | +72.7% | 3.7% | Hold — see TMPV note |
| ETERNAL | Compounder | 36 | 237.13 | 328.00 | +38.3% | 2.8% | Hold |
| HINDCOPPER | Satellite | 20 | 542.85 | 572.70 | +5.5% | 2.7% | Hold |
| ADANIPOWER | Satellite | 53 | 105.66 | 205.50 | +94.5% | 2.6% | Trim into strength |
| DEEPAKNTR | Compounder | 6 | 2120.83 | 1747.00 | −17.6% | 2.5% | Hold |
| GROWW | Compounder | 50 | 187.45 | 197.01 | +5.1% | 2.4% | Hold |
| TMPV | Compounder | 27 | 580.47 | 317.90 | −45.2% | 2.1% | Hold — see note below |
| CLEAN | Satellite | 10 | 1323.93 | 826.00 | −37.6% | 2.0% | Hold, watch |
| ABCAPITAL | Compounder | 20 | 374.65 | 411.10 | +9.7% | 2.0% | Hold |
| SILVERBEES | Index/Hedge | 30 | 229.97 | 231.31† | +0.6%† | 1.7% | Hold |
| NTPC | Satellite | 19 | 349.76 | 340.00 | −2.8% | 1.5% | Hold |
| DSSL | Compounder | 5 | 1482.00 | 1097.00 | −26.0% | 1.3% | Hold — thesis intact |
| BAJAJHFL | Compounder | 64 | 70.00 | 84.85 | +21.2% | 1.3% | Hold |
| LT | Compounder | 2 | 3645.95 | 4093.00 | +12.3% | 2.0% | Hold |
| BERGEPAINT | Compounder | 10 | 594.65 | 524.00 | −11.9% | 1.3% | Hold |
| NEWGEN | Compounder | 10 | 514.05 | 523.00 | +1.7% | 1.3% | Hold |
| AWL | Satellite | 17 | 357.90 | 188.00 | −47.5% | 0.8% | Watch closely |
| BCG | **Exit candidate** | 230 | 15.69 | 9.15 | −41.7% | 0.5% | **Exit — regulatory flag** |
| NFL | Satellite | 28 | 122.41 | 70.30 | −42.6% | 0.5% | Hold, low conviction |
| RELIANCE | Compounder | 1 | 1308.80 | 1316.00 | +0.6% | 0.3% | Immaterial (1 share) |
| ITBEES | Index/Hedge | 10 | 45.44 | 34.07 | −25.0% | 0.1% | Immaterial |

\* Asian Paints price sourced from 19 Aug close (Friday 21 Aug close not
independently confirmed — close enough for this read, worth re-verifying
next run).
† SilverBees's quoted 52-week high (~₹360) sits oddly above the current price
despite silver hitting fresh record highs this month — likely a stale/
un-adjusted range from a prior unit split, not a real decline. Flagging as a
data-quality caveat rather than treating the range as reliable; the price
itself (₹231.31, cross-checked across two sources) is used with normal
confidence.

**Open watch items (new — this is Day 1):**

- **TCS is the single biggest position (10.5%, ₹50,803 invested) and it's a
  loser (−13.9%).** This is the real story behind "low returns despite good
  picks." The headwind is real and sector-wide: the Nifty IT index is down
  ~28% over the past year on AI-disruption/spending-slowdown fears, and TCS
  specifically has an added overhang — Tata Sons Chairman N. Chandrasekaran
  said on 12 Aug he won't seek reappointment past Feb 2027, adding leadership
  uncertainty on top of the sector story. This isn't a "sell the loser"
  situation — TCS is still a blue-chip bellwether, not a broken business — but
  it's also not a "buy the dip" situation while both overhangs are live.
  Action: **hold, no fresh buying, revisit after the succession question
  resolves or the IT sector shows a real turn.** Status: **open, unresolved.**
- **Tata Group concentration, previously invisible.** TCS (10.5%) + TMPV
  (2.1%) + TMCV (3.7%) are all Tata Group companies — **20.2% of the portfolio
  in one promoter group**, not obvious until the pieces are put next to each
  other. Not at Sujal's-book levels of alarming (his Adani stake is 76%), but
  real enough to name: group-level news (leadership, governance, capital
  allocation across Tata Sons) can move all three at once. Status: **open,
  new.**
- **TMPV + TMCV should be read as one position, not two.** In isolation, TMPV
  looks like a −45.2% disaster and TMCV a +72.7% moonshot — but they're the
  two halves of the same original Tata Motors holding, split by the Oct 2025
  demerger (record date 14 Oct 2025, TMCV listed 12 Nov 2025). Combined:
  ₹24,701.16 invested, ₹24,177.45 current value, **−2.1% combined — roughly
  flat.** This is the same demerger Sujal's account is still trying to
  reconcile (his TMPV position may be missing its TMCV half entirely — see
  `LOG.md`). Here, both halves are present and accounted for, so this is a
  clean confirmation of how that pair should actually be read once fully
  reconciled. Action: track as one logical position going forward. Status:
  **open, informational — no action needed on this pair itself.**
- **BCG (Brightcom Group) — recommend exiting, not just watching.** SEBI's Feb
  2024 confirmatory order found accounting fraud (forged bank statements used
  in a preferential share allotment) and fined the company and its promoters
  ₹34cr; NSE suspended trading in 2024 for non-filing of results before it
  resumed, and the stock is currently flagged under Stage-1 ASM surveillance
  for volatility. This is a credibility problem, not a valuation opportunity —
  any reported "turnaround" numbers should be treated with real skepticism
  given the fraud history. Position is small (0.5%, ₹2,104.50 current value),
  so the cost of being wrong either way is low, but the cost of holding a
  stock with a confirmed fraud finding isn't just financial. Status: **open,
  recommend exit — Manali's call, not automatic.**
- **IRFC — same rate story as Sujal's book, six times the size.** 185 shares
  vs Sujal's 30, different average price (₹124.73 vs ₹145.62 — bought at a
  different time), same −30.8% story: RBI's hawkish tone, a fresh 52-week low
  of ₹85.18 hit 19 Aug, recovered to ₹86.35 by Friday's close, now below every
  key moving average. See `LOG.md` Day 2 for the full macro detail — it
  applies identically here, just at ₹15,974.75 of current value instead of
  Sujal's ₹2,590.50. Status: **open, watch closely — same ₹85 support level.**
- **AWL (AWL Agri Business, formerly Adani Wilmar) — down 47.5%, worth a closer
  look, not just noise.** NSE sought clarification on 7 Aug over an
  FSSAI-related media report — a food-safety regulatory question, which is a
  different category of risk than ordinary business cyclicality. Small
  position (0.8%), but worth tracking the FSSAI story specifically rather than
  assuming this is just sector rotation. Status: **open, watch closely.**
- **GOLDBEES and Adani Power — same trim logic as Sujal's book.** Both up
  triple digits / near-triple digits (+103.3% / +94.5%), both small-to-moderate
  positions here (4.2% / 2.6%) rather than dangerously oversized, so this is
  lower urgency than in Sujal's book — but the same "moves this vertical
  rarely hold their full pace" logic applies to GOLDBEES, and Adani Power's
  valuation is rich (PE ~33) after this run. Status: **open, lower priority
  than the TCS/IRFC/BCG items above.**

**Today's macro backdrop:** Same session as `LOG.md` Day 2 — see that entry for
the full write-up (Sensex 77,540.83, Nifty 24,252.00, hawkish RBI, elevated
crude/gold on US–Iran tension, US markets bounced Friday but still down on the
week). Sector detail specific to this book: **Nifty IT down ~28% over the past
year** (TCS, ITBEES both feel this directly), while **defense/PSU names (HAL,
BEL, MAZDOCK) have been strong** on steady order-book news — a real bifurcation
worth noting since this book has meaningful exposure to both ends.

**No investing-style framework existed for this account before today.** One is
now defined in `PROMPT_manali.md`, built from what's actually in the book
(three buckets: Compounder / Satellite / Index-Hedge, with a sizing-discipline
lens as the central theme) rather than guessed in advance.

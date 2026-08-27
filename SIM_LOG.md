# Paper-Trading Simulation Log

This is a **simulated portfolio test**, not the real accounts. No real trades
are ever placed here — `data/sim_sujal.json` and `data/sim_manali.json` are
paper ledgers, seeded from real holdings but tracked entirely separately from
`data/latest_sujal.json` / `data/latest_manali.json`.

**Purpose:** validate whether the daily decision framework in `PROMPT.md` /
`PROMPT_manali.md` actually produces good calls before any of it is used on
real holdings. See `SIM_PROMPT.md` for the exact rules this simulation
follows every run.

**Window:** Monday 24 Aug 2026 – Friday 4 Sep 2026 (10 trading days, two full
weeks). Checked twice daily: before market open (~7:45am IST) and after
market close (~11:00pm IST). Outside this window, runs are a no-op.

Never delete or rewrite past entries — only append above the marker.

<!-- NEW_ENTRY_INSERT_ABOVE -->

## Day 4 — Thursday, 27 Aug 2026 (evening check-in)

**Self-check:** today is Thursday 27 Aug 2026 — inside the 24 Aug–4 Sep window, a
weekday. Re-confirmed via web search (Groww NSE-holidays list, Zerodha holiday
calendar, dhan.co's "no stock market holidays in August 2026" piece) that 27
Aug 2026 is **not** an NSE/BSE trading holiday. Proceeding with the evening
mark-to-market.

**Closing prices researched this evening** (NSE, 27 Aug 2026 close; sources:
stockanalysis.com as primary where available, cross-checked against a second
source — Groww, Tickertape, INDmoney, Kotak Neo, Business Standard — per
symbol below):

| Symbol | Close (₹) | Day chg | Confidence | Note |
|---|---|---|---|---|
| Nifty 50 | 24,090.85 | −0.48% (−116.90 pts) | High (2-source) | Sensex −0.70% to 76,933.59, 2nd straight down session; Metals/PSU Banks/Cement weakest, Pharma/Private Banks/Realty bucked the trend. Business Standard cites mixed global cues and West Asia tension, offset by easing crude/yields; investors in wait-and-watch mode ahead of the Fed Chair's Jackson Hole speech. No Nvidia-earnings linkage reported in the sourced market-close pieces. |
| IRFC | 84.65 | −1.23% | High (2-source) | No follow-up found on the 24 Aug GST show-cause notice; company's "no immediate impact" position unchanged |
| TMPV | 316.00 | +0.93% | High (2-source) | Tata Motors PV unveiled "Tata.cars" as a new customer-facing brand identity today — branding news, not move-driving |
| TMCV | 473.10 | −2.20% | High (2-source) | No dated catalyst found for today's move — flagged as unexplained, not large enough relative to size held to investigate further |
| ADANIGREEN | 1,328.50 | +1.94% | High (2-source) | The Bernstein/SocGen ₹980 target cut flagged as unconfirmed-date on Day 3 is now confirmed dated **18 Aug 2026** (9 days old, not a fresh item); no new company-specific news today, move tracks broader Adani-group strength |
| ADANIPOWER | 215.80 | +4.15% | High (2-source, ~0.4% spread vs a third source) | Third straight up session; no fresh catalyst beyond already-known items (CARE AA+ upgrade, Vidarbha Power deal) — reads as momentum/sector-driven |
| GOLDBEES | 130.28 | −1.58% | High (2-source, after resolving a sign conflict — see caveat below) | MCX gold traded choppy/mixed intraday; no clean directional driver |
| NIFTYBEES | 275.51 | −0.55% | High (2-source) | Tracks index |
| RELIANCE | 1,282.20 | −1.22% | High (2-source) | Among today's top Nifty losers per Business Standard |
| LT | 4,027.00 | −0.27% | Low (single-source) | |
| ASIANPAINT | 2,631.00 | +0.17% | Low (single-source) | |
| HDFCBANK | 714.45 | −1.75% | Low (2nd source only had 25 Aug data) | Move larger than sector peers; no dated headline found |
| HAL | 4,876.10 | +0.22% | Low (single-source) | |
| GROWW | 196.84 | +0.31% | High (2-source) | Stabilized after yesterday's block-deal-driven drop; no 2nd wave of selling confirmed today — yesterday's move was Ribbit-linked Cayman GW Holdings selling ~₹979cr at ₹196.06/sh (Business Standard, 26 Aug) |
| CLEAN | 830.05 | +0.07% | Low (single-source) | |
| MAZDOCK | 2,588.00 | −1.41% | Low (single-source) | Project 75(I) still awaiting final CCS sign-off; no news dated today |
| BEL | 411.00 | +1.01% | High (2-source) | Market continuing to digest yesterday's ~₹730cr order disclosure; no fresh order today |
| DEEPAKNTR | 1,752.80 | −1.35% | Low (single-source) | |
| BAJFINANCE | 1,083.00 | −0.18% | Low (single-source) | |
| BAJAJHFL | 85.29 | +1.45% | Low (single-source) | |
| DSSL | 1,076.40 | +0.27% | Medium (2-source, ~1.4% spread) | Confirmed as Dynacons Systems & Solutions, not Dee Development |
| BERGEPAINT | 501.00 | −0.54% | Low (single-source) | |
| TCS | 2,248.40 | −0.95% | Low (single-source) | No company-specific news; US visa-appointment pause remains a sector-wide macro overhang, not a TCS-specific catalyst |
| HINDCOPPER | 536.30 | −3.55% | High (2-source) | T+2 settlement (27 Aug) of the government's 3% OFS launched 25 Aug at ₹514 floor — a continuation/settlement effect of already-known news, not a new development |
| NEWGEN | 523.00 | −0.26% | Low (single-source) | |
| SRF | 2,605.50 | +0.87% | Low (single-source) | |
| ABCAPITAL | 410.00 | −0.32%* | Low (single-source) | *Unchanged from yesterday's logged close (410.00) — the source's own day-chg% used a different reference close than this log's; flagged, doesn't affect mark-to-market math below (computed on absolute closes, not chained %) |
| AWL | 199.74 | −1.07% | Low (single-source) | |
| NTPC | 330.90 | −1.11% | Low (single-source) | |
| ETERNAL | 328.50 | +0.46% | Low (single-source) | |
| NFL | 71.36 | −0.61% | Low (single-source) | |
| ITBEES | 33.71 | −0.15% | Low (single-source) | |
| SILVERBEES | 225.82 | −1.87% | Low (single-source) | |
| BCG | 9.03 | −0.44% | Low (single-source) | For buy-and-hold benchmark only — not held after Day 1's exit |

**Data-quality caveats:** (1) **GOLDBEES** — the two research passes initially
disagreed on *direction*, not just magnitude: one source read −1.75%, another
read the identical ₹130.28 print as +1.75%. Resolved by an independent
follow-up search: Groww and Kotak Neo both confirm ₹130.28 (NSE) / ₹130.12
(BSE) as today's close, which is *down* from yesterday's logged ₹132.37 —
confirming the −1.58% direction, not the sign-flipped version. (2) Roughly
half of Manali's 31 names (LT, ASIANPAINT, HDFCBANK, HAL, CLEAN, MAZDOCK,
DEEPAKNTR, BAJFINANCE, BAJAJHFL, BERGEPAINT, TCS, NEWGEN, SRF, ABCAPITAL, AWL,
NTPC, ETERNAL, NFL, ITBEES, SILVERBEES, BCG) rest on a single source today —
second-source searches for these repeatedly surfaced stale (24–26 Aug) data
rather than same-day confirmation; none of the day's moves on these exceeded
the ±2-3% cross-check threshold except ABCAPITAL's internal inconsistency
(noted above, immaterial). (3) TMCV (−2.20%) and ADANIPOWER (+4.15%) crossed
the notable-move threshold but no dated company-specific catalyst was found
for either — logged as-is per the "never invent numbers" rule rather than
fabricating an explanation. None of today's prices are certified against
NSE's own bhavcopy.

### Sujal's paper book — mark-to-market

| | Value | Since Day 0 (₹36,182.70) |
|---|---|---|
| **Actual (traded) book** | **₹36,707.38** | **+₹524.68 (+1.45%)** |
| Buy-and-hold benchmark (no trades) | ₹37,151.30 | +₹968.60 (+2.68%) |
| Nifty 50-tracking benchmark | ₹35,942.27 | −₹240.43 (−0.66%) |

Day's move: +₹511.64 (+1.41%) vs yesterday's ₹36,195.74 close — the book rose
today but by less than either benchmark: the Nifty fell −0.48%, yet the
Nifty-tracking benchmark (which compounds off Day 0, not yesterday) works out
essentially flat-to-down over the period, while the book's own concentrated
holdings (ADANIPOWER +4.15%, ADANIGREEN +1.94%) pushed it up regardless of the
broader index's direction — a reminder that a 2-stock-heavy book can and does
decouple from the index on any given day. Buy-and-hold reconstructed from the
original Day-0 quantities (IRFC 30, TMPV 5, ADANIGREEN 6, ADANIPOWER 95,
GOLDBEES 35, 0 cash) marked at today's same closes.

**Reading it:** today is the clearest evidence yet of the tension Day 1's
de-risking trade accepted going in. ADANIPOWER rallied a third straight
session (+4.15%) and GOLDBEES fell (−1.58%) — exactly the shares that were
trimmed doing the opposite of what the trim assumed, on a day when the trim's
size mattered most. The cumulative actual-vs-buy-hold gap blew out from Day
3's −₹76.91 to today's **−₹443.92** — the traded book (+1.45% since Day 0) now
trails the untouched version (+2.68%) by roughly 1.2 percentage points, driven
almost entirely by buy-and-hold's larger ADANIPOWER stake (95 vs 55 shares)
capturing more of today's rally. Four sessions in, the pattern is now
consistent enough to name plainly: this de-risking trade has cost real,
measurable return every single day since it was placed, with no day yet where
concentration risk showed up as a cost rather than a benefit. That does not
make the trade wrong — the entire point was insuring against a tail event
that hasn't happened in this sample — but it does mean the "cost of the
insurance" is compounding visibly, and six more sessions is not a lot of room
for a tail event to justify it. Also notable: for the first time, the traded
book's cumulative return (+1.45%) beats *both* other benchmarks — the
Nifty-tracking twin (−0.66%) most clearly, since Sujal's ADANIPOWER/
ADANIGREEN-heavy composition has simply held up far better than the broad
index this week, a separate effect from the trim decision itself.

### Manali's paper book — mark-to-market

| | Value | Since Day 0 (₹4,18,123.80) |
|---|---|---|
| **Actual (traded) book** | **₹4,14,913.49** | **−₹3,210.31 (−0.77%)** |
| Buy-and-hold benchmark (no trades) | ₹4,15,213.67 | −₹2,910.13 (−0.70%) |
| Nifty 50-tracking benchmark | ₹4,15,345.45 | −₹2,778.35 (−0.66%) |

Day's move: −₹1,530.70 (−0.37%) vs yesterday's ₹4,16,444.19 close — roughly in
line with the Nifty's own −0.48% today, on broad softness (RELIANCE −1.22%,
HDFCBANK −1.75%, TCS −0.95%, HINDCOPPER −3.55% on OFS settlement, SILVERBEES
−1.87%) only partly offset by ADANIPOWER (+4.15%) and BEL (+1.01%).
Buy-and-hold reconstructed from the original Day-0 quantities (today's 31
holdings plus BCG 230 reinstated, GOLDBEES 135, ADANIPOWER 53, BAJFINANCE 20,
HAL 5, NIFTYBEES 90 — i.e. Monday's trades reversed) marked at today's same
closes, including BCG's ₹9.03 close.

**Reading it:** the cumulative actual-vs-buy-hold gap widened again, from Day
3's −₹243.19 to today's **−₹300.18** — a smaller incremental drag (−₹56.99)
than Sujal's book saw today, because Manali's ADANIPOWER position is a much
smaller share of this larger, more diversified book, so today's ADANIPOWER
rally couldn't move the comparison much either way. The trims (GOLDBEES,
ADANIPOWER) and adds (BAJFINANCE, HAL, NIFTYBEES) remain a small, consistent
drag versus doing nothing — four sessions running now, never in the other
direction — though at −0.058% of book value on Day 3 widening only slightly
to roughly −0.07% today, it's still a minor effect relative to the book's
size. HINDCOPPER's −3.55% today is a settlement mechanic (T+2 for Monday's
OFS), not new information, and doesn't reopen the "supply/technical, not
fundamental" read already logged. GROWW stabilized (+0.31%) with no second
wave of block-deal selling confirmed — the watch item can be downgraded
somewhat, though not closed outright without another session's confirmation.
BEL's +1.01% reflects the market still digesting yesterday's order-win
filing, not a new catalyst. Like Sujal's book, Manali's traded book (−0.77%
cumulative) and its buy-and-hold twin (−0.70%) both continue to trail the
Nifty-tracking benchmark (−0.66%) only slightly now — the gap between this
book's real composition and the index has narrowed over the last two
sessions as the broad market itself has pulled back.

**Decisions today — Sujal:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — this
  evening's run only marks positions to today's close. ADANIGREEN's analyst
  target cut is now confirmed dated 18 Aug (old news, not fresh); no other
  finding changes any position.

**Decisions today — Manali:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: everything (all 31 remaining holdings) — this evening's run only
  marks positions to today's close. GROWW's stabilization (+0.31%, no second
  wave of block-deal selling) softens but doesn't close that watch item;
  HINDCOPPER's −3.55% is OFS settlement mechanics, not new information;
  MAZDOCK's CCS sign-off remains unconfirmed.

## Day 4 — Thursday, 27 Aug 2026 (morning check-in)

**Self-check:** today is Thursday 27 Aug 2026 — inside the 24 Aug–4 Sep window, a
weekday. Confirmed via web search (Angel One, business-standard "stocks to
watch" pieces dated today) that 27 Aug 2026 is **not** an NSE/BSE trading
holiday — normal market operations resume fully across all segments (26 Aug's
settlement-only Eid-e-Milad closure doesn't recur). Proceeding. Reference
prices throughout use Wednesday 26 Aug's close (already researched and logged
in yesterday evening's entry); actual fills at today's open will differ.

**Macro backdrop researched this morning:** Cautious, gap-down open indicated —
GIFT Nifty pointing to roughly −40 points, a negative lean after Wednesday's
Nifty close of 24,207.75 (−0.52%) and Sensex 77,472.94 (−0.24%), a session in
which IT stocks dragged the index amid US visa-appointment uncertainty (see
below). US markets were mixed overnight: S&P 500 flat (−0.02% to 7,675.70),
Dow +0.3% to 53,577.40, Nasdaq +0.7% to 26,151.30, with tech/communication
services the biggest gainers ahead of Nvidia's results. **Nvidia reported Q2
FY27 earnings after Wednesday's US close** and beat decisively — revenue
$96.2bn vs $92.4bn consensus (+106% YoY), EPS $2.22, Q3 guidance of $108bn vs
$104.2bn consensus — a strong global AI-capex signal, though historically
NVDA itself has drifted lower in the week following a beat, so the market
reaction into today's Asia/India session is not yet confirmed one way or the
other. Crude continued easing — Brent ~$86/bbl, WTI ~$80/bbl, both −2.5% — no
new supply-shock signal. Gold (~$4,650/oz) and silver (~$70/oz) remain
elevated with no confirmed reversal yet, consistent with prior sessions.
**New macro item since yesterday's close:** the US administration paused visa
appointment scheduling worldwide (consular staff undergoing fresh
screening/training) alongside a separately proposed ~$103,265 fee on H-1B
cap-subject applications — reported as a contributor to Wednesday's IT-sector
weakness on the Nifty (margin-pressure concerns for Indian IT exporters). This
is a sector-wide immigration/cost overhang, not a TCS-specific event, and nothing
about it is a confirmed earnings or contract impact yet — flagging as a watch
item for TCS (Manali) and ITBEES (Manali), not an action trigger.

**Symbol-level research (all 6 Sujal + all 31 Manali holdings checked for
anything new since yesterday's close):**
- **IRFC**: no update since Sunday's/24 Aug's GST show-cause notice
  (₹549.32cr, company says no immediate impact) — remains a watch item, not a
  trigger; no new filing or regulatory follow-up found.
- **ADANIGREEN**: no fresh, dated news found since yesterday's close; the
  analyst target cut flagged Tuesday remains unconfirmed as to date and is
  still just a watch item.
- **ADANIPOWER**: no new material news beyond already-known items (CARE's 18
  Aug upgrade to AA+/Stable, the August investor presentation, and scheduled
  investor interactions through late Aug/Sept) — nothing changing the
  de-risking read.
- **GROWW** (Manali): confirmed the block deal reported yesterday was
  Ribbit Capital entities selling ~2.1% of Billionbrains Garage Ventures
  (~₹2,500cr, floor ₹195, 30-day lock-in on the buyer) — consistent with
  yesterday's read, no escalation or second wave of selling found today.
  Still a watch item, not an action trigger — the stake sale doesn't touch
  GROWW's own fundamentals.
- **MAZDOCK** (Manali): Project 75(I) (~₹70,000cr) still awaiting final CCS
  sign-off; contract conclusion still targeted for September per multiple
  reports — unchanged since yesterday, still unconfirmed, still not
  actionable.
- **BEL** (Manali): genuinely new since yesterday — has secured additional
  defence orders worth ~₹730cr since 10 Aug (communication equipment, radar,
  avionics, tank sub-systems). Incrementally positive, consistent with the
  existing "hold" thesis on an already-well-regarded defense PSU holding; not
  large enough relative to BEL's order book to be a standalone trigger.
- **TCS**: no company-specific news beyond the sector-wide US visa-pause
  overhang noted above; the succession story (Tata Sons chairmanship) remains
  unchanged from prior checks.
- **HINDCOPPER**: no new news; yesterday's +4.39% rebound already confirmed
  the government OFS was a supply/technical event, not fundamental — no
  longer an open concern.
- Every other symbol (TMPV, TMCV, NIFTYBEES, GOLDBEES, RELIANCE, LT,
  ASIANPAINT, HDFCBANK, HAL, CLEAN, DEEPAKNTR, BAJFINANCE, BAJAJHFL, DSSL,
  BERGEPAINT, NEWGEN, SRF, ABCAPITAL, AWL, NTPC, ETERNAL, NFL, ITBEES,
  SILVERBEES): no fresh, dated news found since yesterday's close in this
  morning's research.

**Decision:** no confirmed, material new information changes any open thesis
in either book today. The US visa-appointment pause is a real, dated,
sector-wide item (new since yesterday's close) but it's a macro overhang on
Indian IT broadly, not a company-specific catalyst on TCS, and doesn't change
the existing "hold, no add" read there. BEL's incremental new order flow is
mildly positive but immaterial next to its scale. Both books' most recent
trades (Day 1's de-risking and sizing moves) remain the open calls under
test — today adds a fourth data point, not a reason for turnover.

**Decisions today — Sujal:**
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — no new
  research finding changes any position; IRFC's GST notice and ADANIGREEN's
  unconfirmed-date target cut remain watch items only.

**Decisions today — Manali:**
- HOLD: everything (all 31 remaining holdings) — no new research finding
  changes any position. BEL's ~₹730cr in fresh defence orders since 10 Aug is
  mildly positive, not a trigger. GROWW's block-deal-driven stake sale
  remains a watch item, confirmed as an ownership event rather than a
  fundamentals one. MAZDOCK's CCS sign-off remains pending. The US
  visa-appointment pause is a new sector-wide watch item for TCS/ITBEES, not
  an action trigger today.

## Day 3 — Wednesday, 26 Aug 2026 (evening check-in)

**Self-check:** today is Wednesday 26 Aug 2026 — inside the 24 Aug–4 Sep window, a
weekday. Re-confirmed via web search that 26 Aug 2026 is a **settlement-only**
holiday for Eid-e-Milad (Id-E-Milad) — NSE/BSE cash-equity and F&O trading
proceeded normally all session; only clearing/settlement and the
currency-derivatives segment were closed, neither of which affects this
simulation's marking. Proceeding with the evening mark-to-market.

**Closing prices researched this evening** (NSE, 26 Aug 2026 close; sources:
stockanalysis.com historical tables as primary, cross-checked against a second
independent source — Groww, Tickertape, IndMoney, or Business Standard — per
symbol below):

| Symbol | Close (₹) | Day chg | Confidence | Note |
|---|---|---|---|---|
| Nifty 50 | 24,207.75 | −0.52% (−126.80 pts) | High | Sensex −0.24% to 77,472.94; IT/FMCG/auto weakest sectors, banking/metals outperformed |
| IRFC | 85.70 | +0.29% | High (2-source) | No fresh company news found today |
| TMPV | 313.10 | −0.37% | High (2-source) | |
| TMCV | 483.75 | +1.86% | High (2-source) | No dated article found explaining the move |
| ADANIGREEN | 1,303.20 | −2.02% | High (2-source) | A Bernstein/SocGen target cut to ₹980 was reported but the note's date is **unconfirmed as today** — treated as a watch item, not a same-day catalyst |
| ADANIPOWER | 207.20 | +0.42% | High (2-source) | |
| GOLDBEES | 132.37 | −0.31% | High (2-source) | |
| NIFTYBEES | 277.02 | +0.03% | High (2-source) | |
| RELIANCE | 1,298.00 | −1.44% | High (2-source) | |
| LT | 4,038.10 | −1.96% | High (2-source) | |
| ASIANPAINT | 2,626.50 | −0.50% | High (2-source) | |
| HDFCBANK | 727.20 | −0.04% | High (2-source) | |
| HAL | 4,865.50 | −0.70% | High (2-source) | |
| GROWW | 196.24 | **−3.33%** | High (2-source) | Two large block deals today; Ribbit Capital reported as likely seller of ~1.6% stake; most active stock on NSE today (Business Standard, dated 26 Aug) |
| CLEAN | 829.45 | +0.92% | High (2-source) | |
| MAZDOCK | 2,625.00 | +0.57% | High (2-source) | |
| BEL | 406.90 | −1.54% | High (2-source) | |
| DEEPAKNTR | 1,776.70 | +1.47% | High (2-source) | |
| BAJFINANCE | 1,085.00 | −0.22% | High (2-source) | |
| BAJAJHFL | 84.07 | +0.06% | High (2-source) | |
| DSSL | 1,073.50 | −1.44% | High (2-source) | |
| BERGEPAINT | 503.70 | −1.21% | High (2-source) | |
| TCS | 2,270.00 | −1.14% | High (2-source) | Fell with Nifty IT (day's weakest sector), FII selling ahead of Nvidia earnings/US PCE |
| HINDCOPPER | 556.05 | **+4.39%** | High (2-source) | Rebounded from yesterday's −7.23% OFS-driven drop — stabilization, confirms yesterday's supply/technical read |
| NEWGEN | 524.35 | −0.23% | Low (single-sourced) | |
| SRF | 2,583.00 | +0.31% | Low (single-sourced) | |
| ABCAPITAL | 410.00 | −0.21% | Low (single-sourced) | |
| AWL | 201.90 | +0.63% | High (2-source) | |
| NTPC | 334.60 | −1.54% | Low (single-sourced) | Broad power-sector weakness (Power Grid −1.77%) |
| ETERNAL | 327.00 | −1.21% | Low (single-sourced) | |
| NFL | 71.80 | −0.83% | Low (single-sourced) | |
| ITBEES | 33.76 | −0.47% | Low (single-sourced) | Consistent with Nifty IT as day's weakest sector |
| SILVERBEES | 230.13 | +0.49% | Low (single-sourced) | |
| BCG | 9.07 | −0.22% | High (2-source) | For buy-and-hold benchmark only — not held after Day 1's exit |

**Data-quality caveats:** none of these are certified against NSE's own
bhavcopy. Seven symbols (NEWGEN, SRF, ABCAPITAL, NTPC, ETERNAL, NFL, ITBEES,
SILVERBEES) rest on stockanalysis.com alone — the research agent could not
independently verify a genuinely date-matched second source for these via
general web search (one search summary misattributed a Brightcom/BCG price
from 26 Aug **2025** as if dated 2026 — caught and discarded before use, a
reminder to treat AI search summaries skeptically). None of the day's moves on
these seven exceeded the ±2% cross-check threshold, so this is flagged rather
than blocking the run, per `SIM_PROMPT.md`'s guidance for the 32-name book.
ADANIGREEN's cited analyst target cut has an unconfirmed date and is treated
as a watch item, not a same-day cause, per the "never invent numbers" rule.

### Sujal's paper book — mark-to-market

| | Value | Since Day 0 (₹36,182.70) |
|---|---|---|
| **Actual (traded) book** | **₹36,195.74** | **+₹13.04 (+0.04%)** |
| Buy-and-hold benchmark (no trades) | ₹36,272.65 | +₹89.95 (+0.25%) |
| Nifty 50-tracking benchmark | ₹36,116.68 | −₹66.02 (−0.18%) |

Day's move: −₹63.60 (−0.18%) vs yesterday's ₹36,259.34 close — roughly in line
with the Nifty's own −0.52% today (the book fell less, proportionally), as
ADANIPOWER (+0.42%) held up while ADANIGREEN (−2.02%, on an unconfirmed-date
analyst target cut) and TMPV (−0.37%) dragged. Buy-and-hold reconstructed from
the original Day-0 quantities (IRFC 30, TMPV 5, ADANIGREEN 6, ADANIPOWER 95,
GOLDBEES 35, 0 cash) marked at today's same closes.

**Reading it:** third straight session where the cumulative gap between the
traded book and doing nothing widened in buy-and-hold's favor — now **−₹76.91**
(buy-hold +0.25% vs actual +0.04%), up from Day 2's −₹104.06 gap but still
negative overall since Day 0. The pattern across three days is consistent:
ADANIPOWER, the trimmed position, keeps outperforming NIFTYBEES, the position
it was partly replaced with, on days when Adani-specific sentiment is calm.
Today ADANIGREEN's target-cut-driven drop actually worked in the de-risking
trade's favor at the ADANIGREEN leg specifically (untouched, so no P&L
difference there vs buy-and-hold), while ADANIPOWER's own gain is what's
costing the reallocation. Three sessions is still short of a real read on a
risk-management call — the framework's bet is that lower single-stock
concentration (Adani combined now ~53% of holdings value vs ~76% pre-trade)
pays off in tail scenarios, not in an ordinary up-day for the name that was
trimmed. Nothing in today's research changes that read. Also notable: the
traded book (+0.04% cumulative) beats the Nifty-tracking benchmark (−0.18%)
even while trailing the do-nothing buy-and-hold (+0.25%) — Sujal's book
overall (IRFC/TMPV/ADANIGREEN/ADANIPOWER-heavy) has simply held up better
than the broad index over the last three sessions, a separate effect from
whether the trade itself added value versus not trading at all.

### Manali's paper book — mark-to-market

| | Value | Since Day 0 (₹4,18,123.80) |
|---|---|---|
| **Actual (traded) book** | **₹4,16,444.19** | **−₹1,679.61 (−0.40%)** |
| Buy-and-hold benchmark (no trades) | ₹4,16,687.38 | −₹1,436.42 (−0.34%) |
| Nifty 50-tracking benchmark | ₹4,17,360.89 | −₹762.91 (−0.18%) |

Day's move: −₹522.43 (−0.13%) vs yesterday's ₹4,16,966.62 close — again beat
the Nifty's own −0.52% today, cushioned by HINDCOPPER's +4.39% rebound from
yesterday's OFS-driven drop (20 shares, a real if modest offset) even as
several large-cap holdings fell with the broad market (LT −1.96%, RELIANCE
−1.44%, TCS −1.14%, BEL −1.54%, NTPC −1.54%). Buy-and-hold reconstructed from
the original Day-0 quantities (today's 31 holdings plus BCG 230 reinstated,
GOLDBEES 135, ADANIPOWER 53, BAJFINANCE 20, HAL 5, NIFTYBEES 90 — i.e.
Monday's trades reversed) marked at today's same closes, including BCG's
₹9.07 close.

**Reading it:** the day's most consequential new development is **GROWW
−3.33%** on two large institutional block deals (Ribbit Capital reported as
likely seller of ~1.6% of the company, confirmed via Business Standard dated
today) — this is an ownership/supply event, not a disclosed change in
GROWW's own fundamentals, similar in kind to yesterday's HINDCOPPER OFS.
Flagging as a new watch item, not acting on it tonight, but worth confirming
tomorrow whether more block-deal supply follows or whether this was a
one-off exit by a single early investor. Monday's rebalance continues to cost
a little against doing nothing: the traded book trailed buy-and-hold by an
incremental −₹32.91 today (cumulative gap widened from Day 2's −₹210.28 to
today's **−₹243.19**) — the GOLDBEES/ADANIPOWER trims and BAJFINANCE/HAL adds
are a slight net drag so far, though the gap remains small relative to the
book's ₹4.18L size (−0.058% of book value). HINDCOPPER's rebound today
supports treating yesterday's OFS-driven drop as supply/technical rather than
a fundamental deterioration, consistent with the read logged then. MAZDOCK's
Project 75(I) CCS sign-off remains unconfirmed. Like Sujal's book, Manali's
traded book (−0.40% cumulative) is trailing its own buy-and-hold twin
(−0.34%), and both are trailing the Nifty-tracking benchmark (−0.18%) — this
book's largely non-index composition has now lagged the index across all
three sessions, independent of any trade made; the trades' own effect
(actual vs buy-and-hold) remains the smaller, separate signal being tracked.

**Decisions today — Sujal:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — this
  evening's run only marks positions to today's close. ADANIGREEN's
  single-source, unconfirmed-date analyst target cut is noted as a watch
  item, not an action trigger tonight.

**Decisions today — Manali:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: everything (all 31 remaining holdings) — this evening's run only
  marks positions to today's close. GROWW's block-deal-driven −3.33% drop
  (confirmed institutional stake sale, not a fundamentals event) is a new
  watch item for the next check-in, not an action trigger tonight.
  HINDCOPPER's +4.39% rebound confirms yesterday's OFS was supply/technical,
  not fundamental — no longer an open concern. MAZDOCK's CCS sign-off remains
  unconfirmed.

## Day 3 — Wednesday, 26 Aug 2026 (morning check-in)

**Self-check:** today is Wednesday 26 Aug 2026 — inside the 24 Aug–4 Sep window,
a weekday. Confirmed via web search (Angel One, Business Standard, Zerodha
holiday calendar, Sunday Guardian, Goodreturns) that 26 Aug 2026 is **not** an
NSE/BSE trading holiday — both exchanges remain open for regular trading. It
*is* a clearing/settlement holiday for Id-E-Milad (Eid Milad-un-Nabi), meaning
orders execute normally today but settlement of today's trades is deferred to
the next settlement day, and the currency-derivatives segment specifically is
closed. Neither affects this cash-equity simulation. Proceeding. Reference
prices throughout use Tuesday 25 Aug's close (per Day 2's evening entry,
already researched and logged); actual fills at today's open will differ.

**Macro backdrop researched this morning:** Modestly positive open indicated —
GIFT Nifty ~24,474 (Nifty futures ~24,333.5) implies Nifty opening ~35 pts
above yesterday's close, a small positive gap. US markets closed higher
overnight: S&P 500 +0.32% to 7,677.28, Dow +0.30% to 53,579.94, Nasdaq +0.6%
(tech/healthcare led). Asia is trading mixed-to-lower this morning as
investors turn cautious ahead of a data-heavy week — Nvidia reports Q2 FY27
earnings after today's US close, US July PCE inflation data is due Wednesday,
and Fed Chair Kevin Warsh gives his first Jackson Hole speech this week — all
event risk to watch, none of it India-stock-specific. Crude continued easing:
Brent fell ~3% to ~$89.5/bbl and WTI ~2.5% to ~$84.89 on Monday/Tuesday, as
signs of possible Iran–US diplomatic progress eased supply-disruption
concerns — a further unwind of the tension that drove Monday's sanctions
news, not a new spike. Gold's rally (spot ~$4,650–4,676/oz Tuesday) is
projected by at least one forecast to ease today ahead of the PCE print and
Warsh's speech, but no reversal has actually happened yet — treating this as
a forecast, not a fact, per the "never invent numbers" rule. India VIX closed
Tuesday at 11.53 (+2.95%), still elevated but not alarming.

**Symbol-level research (all 6 Sujal + all 31 Manali holdings checked for
anything new since yesterday's close):**
- **IRFC**: received a GST show-cause notice dated 24 Aug 2026, provisional
  demand ₹549.32 crore (₹305.38cr alleged excess input tax credit for FY23
  plus interest/penalties) — company states no immediate financial impact and
  plans to reply. This is genuinely new since Day 2's checks, but it's a
  show-cause notice (not a confirmed liability) on a name already held at
  reduced conviction (technically weak, below all MAs) — noting it as a watch
  item, not a trigger; nothing in the framework calls for exiting on an
  unresolved tax notice with an explicit "no immediate impact" management
  read.
- **ADANIPOWER / ADANIGREEN**: only the already-known August investor
  presentation and scheduled investor-meet calendar (Mumbai/Chennai/London,
  late Aug–Sep) — nothing new changing yesterday's de-risking read.
- **HINDCOPPER** (Manali only): the government's 6% OFS continues today —
  retail investors' bidding day (institutional tranche was 3.41x
  oversubscribed Tuesday; DIPAM confirmed exercising the full green-shoe
  option). Confirms this is a clean supply/technical event, not a
  fundamental one — remains a watch item, still no action.
- **MAZDOCK** (Manali): Project 75(I) submarine deal (~₹70,000cr) still
  awaiting final CCS sign-off; multiple reports place it "on fast-track" with
  contract conclusion targeted by September — still unconfirmed, still not
  actionable.
- **TCS, BAJFINANCE, HAL, TMPV/TMCV, AWL** and the remaining Manali holdings:
  no fresh, dated news found since yesterday's close beyond items already
  logged in prior entries.
- **GOLDBEES / SILVERBEES**: no reversal in the underlying rally has actually
  occurred; one forecast source flags a possible pullback today around the
  PCE/Warsh event risk, not yet realized.

**Decision:** no confirmed, material new information changes any open thesis
in either book today. IRFC's GST notice is the one genuinely new item, and
it's explicitly a "no immediate impact" show-cause notice, not a reason to
act on a name already held at reduced conviction. Both books' most recent
trades (Day 1's de-risking and sizing moves) remain the open calls under
test — today adds a third data point, not a reason for more turnover.

**Decisions today — Sujal:**
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — no new
  research finding changes any position; IRFC's GST show-cause notice is
  noted as a watch item (company says no immediate impact), not a trigger.

**Decisions today — Manali:**
- HOLD: everything (all 31 remaining holdings) — no new research finding
  changes any position. HINDCOPPER's government OFS reaches its retail day
  today, confirming it as a supply/technical event, not a fundamental one —
  still a watch item, not an action trigger. MAZDOCK's CCS sign-off remains
  pending.

## Day 2 — Tuesday, 25 Aug 2026 (evening check-in)

**Self-check:** today is Tuesday 25 Aug 2026 — inside the 24 Aug–4 Sep window, a
weekday, no known NSE/BSE holiday (already confirmed this morning). Proceeding
with the evening mark-to-market.

**Closing prices researched this evening** (NSE, 25 Aug 2026 close; sources:
stockanalysis.com historical tables, cross-checked against Groww/Google
Finance/Tickertape/Investing.com/Business Standard/Upstox/IIFL where noted):

| Symbol | Close (₹) | Day chg | Note |
|---|---|---|---|
| Nifty 50 | 24,334.55 | +0.48% | expiry-session, weak open on mixed global cues, recovered into close; Midcap 100 hit a fresh ATH |
| IRFC | 85.45 | ~−0.6 to −0.8% | small prev-close mismatch vs last night's logged 86.15 across sources — today's close itself is 2-source confirmed |
| TMPV | 314.25 | −0.05% | confirmed as the passenger-vehicles entity, not TMCV |
| TMCV | 474.90 | −0.03% | confirmed as the separate commercial-vehicles entity |
| ADANIGREEN | 1,330.00 | +1.68% | no 25-Aug-specific news; only forward-looking investor-meet items |
| ADANIPOWER | 206.33 | +1.29% | released Aug investor presentation (18,330 MW operating, targeting 45,000 MW) — likely contributor |
| GOLDBEES | 132.78 | −0.18% | domestic/Comex gold eased on profit-booking after Monday's rally to a 15-week high |
| NIFTYBEES | 275.47 | −0.14% | **data-quality note below** — conflicting live-quote reads existed; using the settled historical-table close |
| RELIANCE | 1,317.00 | +0.55% | |
| LT | 4,119.00 | +0.71% | |
| ASIANPAINT | 2,639.80 | −0.04% | |
| HDFCBANK | 727.50 | −0.21% | |
| HAL | 4,900.00 | −0.12% | |
| GROWW | 203.01 | +3.33% | |
| CLEAN | 819.00 | −1.12% | |
| MAZDOCK | 2,610.00 | +2.76% | **lower confidence** — an independent intraday quote had it ~₹2,530 in late morning; apparent late rally into close, possibly on P-75(I) approval-nearing reports |
| BEL | 413.25 | +1.04% | |
| DEEPAKNTR | 1,751.00 | +1.20% | |
| BAJFINANCE | 1,087.40 | +0.97% | |
| BAJAJHFL | 84.02 | −0.04% | |
| DSSL (Dynacons Systems) | 1,089.20 | +0.84% | confirmed against real ledger's ISIN entity, not Dee Development |
| BERGEPAINT | 509.85 | −1.10% | |
| TCS | 2,296.20 | +0.53% | announced Porsche MHP acquisition (€320m, paving a 5-yr €1.25bn AI deal); opened +1.4% on the news, gave back most by close |
| HINDCOPPER | 532.65 | **−7.23%** | government OFS — selling 3–6% stake at a ₹514 floor (10.4% discount to prior close) — day's single largest mover |
| NEWGEN | 525.55 | −0.54% | |
| SRF | 2,559.30 | −0.83% | |
| ABCAPITAL | 410.85 | −0.50% | |
| AWL | 204.14 | **+5.29%** | large move, single-source only — flagged for extra scrutiny |
| NTPC | 339.85 | +0.10% | |
| ETERNAL | 331.00 | +1.18% | |
| NFL | 72.40 | +2.27% | |
| ITBEES | 33.72 | −0.59% | |
| SILVERBEES | 229.30 | −1.08% | silver eased on profit-booking after Monday's record run |
| BCG | 9.09 | +0.44% | for buy-and-hold benchmark only — no longer held after Day 1's exit |

**Data-quality caveats:** (1) **NIFTYBEES** — stockanalysis.com's historical
table consistently showed 275.47 (−0.14%) across repeated checks, while its
own live-quote page, Tickertape and Google Finance showed ~276.9–277.4
(+0.4–0.5%) off a slightly different previous close; a separate NAV read
(₹276.16) is consistent with either since NAV and traded price commonly
differ slightly. Using **275.47**, the settled/historical-table figure, as
the more reliable end-of-day close — same convention as every prior entry.
(2) **MAZDOCK** and **AWL** — large single-day moves (+2.76%, +5.29%)
confirmed by only one source each; flagged rather than blocking the run, per
`SIM_PROMPT.md`'s guidance for the 32-name book. (3) Several symbols'
25-Aug day-change% is computed by each source against its own recorded prior
close, which differs by a few paise to ~₹0.6 from last night's logged 24-Aug
closes (e.g. IRFC 85.99 vs logged 86.15, ADANIPOWER 203.70 vs logged 203.06)
— ordinary cross-source variance already flagged in prior entries; it doesn't
affect the mark-to-market math below, which multiplies today's close directly
against each ledger's quantities rather than chaining daily % changes. None of
these are certified against NSE's own bhavcopy (nseindia.com still blocks
automated fetches).

### Sujal's paper book — mark-to-market

| | Value | Since Day 0 (₹36,182.70) |
|---|---|---|
| **Actual (traded) book** | **₹36,259.34** | **+₹76.64 (+0.21%)** |
| Buy-and-hold benchmark (no trades) | ₹36,363.40 | +₹180.70 (+0.50%) |
| Nifty 50-tracking benchmark | ₹36,305.87 | +₹123.17 (+0.34%) |

Day's move: +₹269.82 (+0.75%) vs yesterday's ₹35,989.52 close — the book beat
the Nifty's own +0.48% today, on the back of ADANIPOWER (+1.29%) and
ADANIGREEN (+1.68%), still ~53% of the book combined even after Monday's trim.
Buy-and-hold reconstructed from the original Day-0 quantities (IRFC 30, TMPV
5, ADANIGREEN 6, ADANIPOWER 95, GOLDBEES 35, 0 cash) marked at today's same
closes.

**Reading it:** today's price action ran directly against Monday's de-risking
trade. ADANIPOWER (trimmed 40 shares) rallied +1.29%, GOLDBEES (also trimmed)
dipped −0.18%, and NIFTYBEES (bought with the proceeds) was flat-to-down
−0.14% — so the shares that were sold would have outgained the shares that
were bought, today specifically. That flips the cumulative actual-vs-buy-hold
gap from Monday's +₹38.62 edge to today's **−₹104.06** shortfall: the traded
book is now trailing the do-nothing version by that much since Day 0. This is
exactly the tension the framework accepts going in — cutting concentration
risk (54% single-stock, ~33x PE after a +95% run) lowers expected volatility
and tail risk, and will look "wrong" on any single day the concentrated bet
happens to pay off, like today. Two sessions is nowhere near enough to judge
a risk-management call by return alone, and nothing in today's research
(ADANIPOWER's own investor-presentation release, not a fresh catalyst) changes
the read that the position was oversized, not mispriced. Also notable: the
book's cumulative return (+0.21%) now trails the Nifty-tracking benchmark
(+0.34%), while the untraded buy-and-hold version (+0.50%) actually beats the
index over the same two days — a reminder that concentration risk cuts both
ways, and the two-day sample is far too short to read anything into which way
it happened to cut this time.

### Manali's paper book — mark-to-market

| | Value | Since Day 0 (₹4,18,123.80) |
|---|---|---|
| **Actual (traded) book** | **₹4,16,966.62** | **−₹1,157.18 (−0.28%)** |
| Buy-and-hold benchmark (no trades) | ₹4,17,176.90 | −₹946.90 (−0.23%) |
| Nifty 50-tracking benchmark | ₹4,19,547.05 | +₹1,423.25 (+0.34%) |

Day's move: +₹664.98 (+0.16%) vs yesterday's ₹4,16,301.64 close — again
lagged the Nifty's +0.48%. Buy-and-hold reconstructed from the original Day-0
quantities (today's 31 holdings plus BCG 230 reinstated, GOLDBEES 135,
ADANIPOWER 53, BAJFINANCE 20, HAL 5, NIFTYBEES 90 — i.e. Monday's trades
reversed) marked at today's same closes, including BCG's ₹9.09 close.

**Reading it:** the day's biggest single-stock event was **HINDCOPPER
−7.23%** on a government Offer-for-Sale (floor price ₹514, a 10.4% discount)
— a supply/technical event, not obviously a fundamental deterioration, but
worth confirming there's no other angle before writing it off as pure noise;
flagging as a new watch item, not acting on it tonight. Monday's rebalance
had only a small, roughly neutral effect today: the traded book trailed
buy-and-hold by an incremental −₹18.98 today (cumulative gap widened from
Monday's −₹191.30 to −₹210.28) — ADANIPOWER's trim cost a little against its
+1.29% rally, partly offset by HAL (added Monday) being flat-to-down (−0.12%)
rather than adding much back. BCG, exited Monday, ticked up +0.44% to ₹9.09
today — a trivial ~₹9 opportunity cost on 230 shares, nowhere near enough to
revisit a call made on a confirmed SEBI fraud finding and ASM surveillance.
TCS announced a Porsche-linked acquisition (MHP, paving a 5-yr €1.25bn AI
deal) — a genuinely new, positive data point, but the stock gave back most of
its initial pop and this doesn't change the "hold, no add" read on an already
top-3-by-weight position. MAZDOCK's Project 75(I) submarine deal still has no
confirmed final CCS sign-off, despite another green day (+2.76%, on
approval-nearing reports) — remains a watch item, not yet actionable. Like
Sujal's book, Manali's traded book (−0.28% cumulative) and its untraded
buy-and-hold twin (−0.23%) are both trailing the Nifty-tracking benchmark
(+0.34%) over the same two days — this book's mostly-non-index composition
has simply lagged a strong index move so far, independent of any trade made.

**Decisions today — Sujal:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — this
  evening's run only marks positions to today's close; no new research
  finding changes any position, and today's price action (favoring the
  trimmed names) is noted above, not acted on.

**Decisions today — Manali:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: everything (all 31 remaining holdings) — this evening's run only
  marks positions to today's close. HINDCOPPER's government-OFS-driven
  −7.23% drop is a new watch item for the next check-in, not an action
  trigger tonight; MAZDOCK's pending CCS sign-off remains unconfirmed.

## Day 2 — Tuesday, 25 Aug 2026 (morning check-in)

**Self-check:** today is Tuesday 25 Aug 2026 — inside the 24 Aug–4 Sep window, a
weekday. Confirmed via web search (Sahi, Groww, Zerodha, Zeebiz holiday
calendars) that 25 Aug 2026 is **not** an NSE/BSE trading holiday — the only
closures this week are the regular weekend days (22–23 Aug) and Onam/Milad-un-Nabi
is a regional bank holiday in Kerala only, not an exchange holiday. Proceeding.
Reference prices throughout use Monday 24 Aug's close (per this run's ledgers
and SIM_LOG); actual fills at today's open will differ.

**Macro backdrop researched this morning:** Mixed, cautious open expected — one
GIFT Nifty read implied a modest gap-up (~24,290–24,330 vs Monday's 24,219.05
close, +0.2–0.45%) while another flagged GIFT Nifty down ~0.13%; net read is
close-to-flat with a slight upward lean, not a strong signal either way. US
markets closed higher Monday night (S&P 500 +0.4% to 7,674.37, Dow +1.0% to
53,277.01, Nasdaq +0.4% to 26,180.46) despite fresh US sanctions on Iran
("Operation Economic Outcast," 24 Aug). Asia is trading weak this morning
(Hang Seng −2.09%, Nikkei −0.49%). Crude **eased further** — WTI ~$84.89
(−2.5%), Brent ~$92.06 (−2.5%) — continuing Monday's pullback despite the new
sanctions. Gold/silver rally **still extending**, no reversal signal: gold
~$4,590–4,650/oz (15-week high), silver ~$68.90–69.63/oz, domestic 24K gold
~₹16,397/g (+6.2% in 10 days), driven by Fed dovish-shift expectations and
ongoing Iran tension. India's 10-yr yield holds ~6.85–6.87%, near a two-month
high on hawkish RBI minutes (released ~19–20 Aug, open to hikes if inflation
broadens) plus elevated Brent. India VIX at 11.54 (24 Aug), up ~2.9% —
above-average volatility flagged for today. One technical/flow catalyst: the
Nifty IT August F&O monthly expiry falls today, 25 Aug — relevant to ITBEES
and TCS specifically, a volatility event rather than a fundamental one.

**Symbol-level research (all 6 Sujal + all 30 Manali holdings checked):** no
fresh, material company-specific news dated after Monday 24 Aug's close was
found for any held symbol in either book. Specifically:
- **TMPV**: the ₹25,000 price hike (effective 1 Sept) was announced Friday 21
  Aug — already known/priced, not a new trigger today.
- **ADANIGREEN / ADANIPOWER**: no new news; only forward-looking items
  (investor meets late Aug/early Sept, an EGM notice for 3 Sep) — nothing that
  changes yesterday's now-executed de-risking calls.
- **GOLDBEES / SILVERBEES**: rally momentum confirmed still running, not
  reversing — consistent with, not a new trigger beyond, yesterday's partial
  trim.
- **MAZDOCK** (Manali): the ~₹70,000cr Project 75(I) submarine deal has
  Finance Ministry approval and is awaiting final CCS sign-off "in coming
  weeks" — genuinely price-moving if/when it lands, but unconfirmed as of this
  check. **New watch item** — no action today, nothing to trade on yet.
- **TCS** (Manali): clarified that the "succession" reporting circulating is
  about the **Tata Sons chairmanship** (Chandrasekaran not seeking
  reappointment past Feb 2027; T V Narendran a cited frontrunner), not the TCS
  CEO seat — doesn't change the "hold, no add" read on TCS itself, and isn't
  fresh (reporting from ~13–15 Aug).
- **IRFC**: no new news; remains technically weak, unchanged read.
- Every other symbol (RELIANCE, LT, ASIANPAINT, HDFCBANK, HAL, GROWW, CLEAN,
  BEL, BERGEPAINT, DEEPAKNTR, BAJFINANCE, BAJAJHFL, DSSL, HINDCOPPER, NEWGEN,
  SRF, ABCAPITAL, AWL, NTPC, ETERNAL, NFL, ITBEES, NIFTYBEES): no new news
  found dated 24–25 Aug.

**Decision:** with no new information changing any open thesis, and both
books having just executed their major rebalancing yesterday, today is a
straightforward hold for both accounts — the framework explicitly says not to
flag Core/Compounder holdings on ordinary noise, and there's no noise here to
react to, let alone a real event. Yesterday's trims (Adani Power, GOLDBEES,
BCG) and adds (NIFTYBEES, BAJFINANCE, HAL) remain unresolved calls that need
more sessions, not more turnover, to show whether they were right.

**Decisions today — Sujal:**
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — no new
  research finding since yesterday's trades changes any position; yesterday's
  de-risking (Adani Group weight ~75.8% → ~53.0%) is a call still being
  tested, not something to add to on zero new information.

**Decisions today — Manali:**
- HOLD: everything (all 31 remaining holdings) — no new news for any symbol.
  MAZDOCK's pending P-75(I) CCS submarine-deal approval is a new watch item
  (Finance Ministry cleared, CCS sign-off still pending "in coming weeks") —
  flagged for the next check-in, not actionable yet. Nifty IT's Aug F&O
  expiry today is a volatility event for ITBEES/TCS to note, not a reason to
  trade.

## Day 1 — Monday, 24 Aug 2026 (evening check-in)

**Self-check:** today is Monday 24 Aug 2026 — inside the 24 Aug–4 Sep window, a
weekday, no known NSE/BSE holiday (already confirmed this morning). Proceeding
with the evening mark-to-market.

**Closing prices researched this evening** (NSE, 24 Aug 2026 close; sources:
stockanalysis.com historical tables, cross-checked against Groww/Google
Finance/Business Standard/Investing.com/Tickertape where noted):

| Symbol | Close (₹) | Day chg | Note |
|---|---|---|---|
| Nifty 50 | 24,219.05 | −0.14% (−32.95 pts) | cross-verified: Investing.com + Tickertape agree exactly |
| IRFC | 86.15 | −0.29% | consistent with LOG.md's 52-week-low read (₹85 support) |
| TMPV | 314.40 | −1.10% | within its confirmed 52-week range ₹294.30–447.79 |
| TMCV | 475.05 | +0.53% | verified via stockanalysis.com after first source misidentified the page |
| ADANIGREEN | 1,308.00 | −0.91% | cross-checked live on Groww, matched |
| ADANIPOWER | 203.06 | −1.19% | |
| GOLDBEES | 133.02 | +1.29% | rally still extending, as this morning's research flagged |
| NIFTYBEES | 275.90 | −0.31% | |
| RELIANCE | 1,307.50 | −0.49% | |
| LT | 4,085.30 | −0.07% | |
| ASIANPAINT | 2,631.50 | −0.33% | |
| HDFCBANK | 729.00 | +0.28% | |
| HAL | 4,900.00 | −1.76% | |
| GROWW | 196.30 | −0.43% | |
| CLEAN | 827.95 | +0.35% | |
| MAZDOCK | 2,538.00 | −0.57% | |
| BEL | 408.25 | −1.27% | |
| DEEPAKNTR | 1,729.65 | −1.05% | |
| BAJFINANCE | 1,079.40 | −1.26% | |
| BAJAJHFL | 84.09 | −0.87% | |
| DSSL (Dynacons Systems, ISIN INE417B01040) | 1,078.00 | −1.74% | confirmed against real ledger's ISIN, not Dee Development Engineers |
| BERGEPAINT | 515.30 | −1.74% | |
| TCS | 2,284.10 | −0.78% | |
| HINDCOPPER | 567.90 | −0.84% | |
| NEWGEN | 530.50 | +1.49% | |
| SRF | 2,582.40 | +0.41% | |
| ABCAPITAL | 413.75 | +0.18% | |
| AWL | 194.00 | +3.12% | consistent with the already-known −47.5% pre-existing loss |
| NTPC | 339.10 | −0.26% | |
| ETERNAL | 328.30 | +0.09% | |
| NFL | 70.75 | +0.64% | consistent with already-known −42.6% pre-existing loss |
| ITBEES | 34.02 | +0.44% | |
| SILVERBEES | 231.86 | −0.46% | |
| BCG | 9.05 | −1.09% | for buy-and-hold benchmark only — no longer held after today's exit |

**Data-quality caveats:** none of these are certified against NSE's own
bhavcopy (nseindia.com blocked automated fetches / returned 503 across all
three research passes); they're triangulated from stockanalysis.com,
Groww, Google Finance, Business Standard, Investing.com and Tickertape, with
cross-source agreement noted above where checked. TMCV in particular needed a
second, independent fetch after the first source flagged its own page match
as uncertain (it had resolved to a legacy "Tata Motors Ltd" URL) — the
corrected figure (₹475.05, from stockanalysis.com's dated TMCV history table)
is used throughout. TCS was cross-verified at ₹2,284.10 after an initial
₹2,281.00 Google Finance read disagreed slightly with Groww.

### Sujal's paper book — mark-to-market

| | Value | Since Day 0 (₹36,182.70) |
|---|---|---|
| **Actual (traded) book** | **₹35,989.52** | **−₹193.18 (−0.53%)** |
| Buy-and-hold benchmark (no trades) | ₹35,950.90 | −₹231.80 (−0.64%) |
| Nifty 50-tracking benchmark | ₹36,133.54 | −₹49.16 (−0.14%) |

Buy-and-hold reconstructed from the original Day-0 quantities (IRFC 30,
TMPV 5, ADANIGREEN 6, ADANIPOWER 95, GOLDBEES 35, 0 cash) marked at today's
same closes.

**Reading it:** the book fell today, in line with a broadly soft session —
Nifty 50 itself dropped 0.14%, and Sujal's book, still IRFC/TMPV/ADANIGREEN/
ADANIPOWER-heavy, lagged the index because those four names fell harder than
the market average today. But the morning's trim-and-diversify trade *did*
add value relative to doing nothing: the traded book beat the zero-trade
buy-and-hold by +₹38.62. That's a small, single-day edge — GOLDBEES (trimmed)
rose +1.29% today while NIFTYBEES (bought with the proceeds) fell only
−0.31%, so today's specific price action happened to favor the rebalance —
not yet a real test of the underlying thesis (de-risking Adani Group
concentration), which needs more sessions to show up.

### Manali's paper book — mark-to-market

| | Value | Since Day 0 (₹4,18,123.80) |
|---|---|---|
| **Actual (traded) book** | **₹4,16,301.64** | **−₹1,822.16 (−0.44%)** |
| Buy-and-hold benchmark (no trades) | ₹4,16,492.94 | −₹1,630.86 (−0.39%) |
| Nifty 50-tracking benchmark | ₹4,17,555.60 | −₹568.20 (−0.14%) |

Buy-and-hold reconstructed from the original Day-0 quantities (today's 31
holdings plus BCG 230 reinstated, GOLDBEES 135, ADANIPOWER 53, BAJFINANCE 20,
HAL 5, NIFTYBEES 90 — i.e. today's trades reversed) marked at today's same
closes, including BCG's ₹9.05 close.

**Reading it:** like Sujal's book, Manali's paper portfolio lagged the Nifty
today (−0.44% vs the index's −0.14%) on broad softness across large-cap
holdings (TCS −0.78%, HAL −1.76%, DEEPAKNTR −1.05%, BAJFINANCE −1.26% all
weighed on the book). Unlike Sujal's book, today's rebalance *cost* a little
versus doing nothing — the traded book trailed the zero-trade buy-and-hold by
−₹191.30. The mechanics: GOLDBEES and ADANIPOWER (both trimmed this morning)
rose or fell less than BAJFINANCE (bought this morning, −1.26%) and BCG
(exited, itself down −1.09% today — so exiting it actually cost a small
amount versus holding it one more session, purely as a matter of today's
tape). None of this changes the read on the underlying calls: BCG was exited
for a confirmed SEBI fraud finding and ASM surveillance, not for its price
action, and BAJFINANCE/HAL were added because they're structurally
undersized winners, not because of a one-day view. A single day's P&L noise
either way is exactly why this simulation runs for ten sessions before
drawing conclusions, not one.

**Decisions today — Sujal:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — this
  evening's run only marks this morning's trades to today's close; no new
  research finding since this morning changes any position.

**Decisions today — Manali:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: everything (all 31 remaining holdings) — this evening's run only
  marks this morning's trades to today's close; no new research finding
  since this morning changes any position.

## Day 1 — Monday, 24 Aug 2026 (morning check-in)

**Self-check:** today is Monday 24 Aug 2026 — inside the 24 Aug–4 Sep window, a
weekday, no known NSE/BSE holiday. Proceeding. First real trading day; markets
haven't opened yet, so both accounts' decisions below use **Friday 21 Aug
close as the reference price** (same session already used in `LOG.md` Day 2 /
`LOG_manali.md` Day 1) — actual fills at today's open will differ.

**Macro backdrop researched this morning:** GIFT Nifty ~24,286–24,329 vs
Friday's Nifty close of 24,252 — a modest gap-up indicated (~+35 to +75 pts,
+0.15–0.3%). US–Iran/Strait of Hormuz tension remains elevated (new US
sanctions package unveiled Monday, oil tankers running "dark transits" under
US Navy escort), but crude actually **eased** Monday — WTI ~$85.93 (−1.3%),
Brent ~$93.22 (−1.24%) — rather than spiking further. Gold/silver kept
climbing: spot gold ~$4,602–4,617/oz, silver >$70/oz, Indian retail 24K gold
~₹16,309/g — the weekend rally **held and extended into Monday**, no reversal
signal found. India's 10-yr yield sits ~6.85%, still near an 8-week high; no
new RBI move since the Aug 3–5 MPC (held at 5.25%), July CPI confirmed at
4.45%. No material company-specific news was found for any held symbol in
either book dated after Friday 21 Aug close (full detail per symbol below) —
this morning's decisions are therefore about **executing framework calls that
were already open and unresolved**, not reacting to new events.

### Sujal's paper book

Pre-trade: 5 holdings, ₹36,182.70 (unchanged from Day 0 seed — no session has
traded since). Two Trim calls have sat open across two `LOG.md` entries
(ADANIPOWER, GOLDBEES) with nothing new since to change that read — legal risk
on Adani eased (US criminal case dismissed 11 Aug, APTEL ruling 20 Aug, CARE
upgrade 18 Aug — all pre-Friday, already priced) but the *sizing* problem
Day 2 flagged is unchanged, and gold's rally is still extending, not cooling.
This is the natural first live test of the framework's own calls:

- **SELL 40 of 95 ADANIPOWER @ ₹205.50** → proceeds ₹8,220.00. Cuts the
  single largest position from 54.0% to ~31% of the book alone.
- **SELL 15 of 35 GOLDBEES @ ₹131.32** → proceeds ₹1,969.80. Banks part of
  the +99.7% gain into a rally research confirms is still running, keeps a
  smaller core slice as hedge.
- **BUY 36 NIFTYBEES @ ₹276.83** → cost ₹9,965.88, funded entirely by the
  two trims above (₹10,189.80 proceeds, ₹223.92 left as cash). This is the
  broad-index diversification Day 2's capital note flagged as worth
  considering — done now via trim proceeds, not fresh capital. Price sourced
  from the same Fri 21 Aug NIFTYBEES close already verified in Manali's book.
- IRFC, TMPV, ADANIGREEN: unchanged, no action. IRFC remains technically weak
  (below all MAs) with no new news to change that; TMPV's cost-basis question
  is a real-account reconciliation issue, not something this simulation acts
  on; ADANIGREEN's ₹1,310 support and thesis are unchanged since Friday.

**Net effect:** combined Adani Group weight (ADANIPOWER + ADANIGREEN) falls
from ~75.8% to **~53.0%** of the book — still concentrated, but meaningfully
de-risked, without touching the underlying thesis on either name. Post-trade
value at reference prices: ₹36,182.70 (unchanged — reallocation only, same
Friday close used for both legs).

### Manali's paper book

Pre-trade: 32 holdings, ₹4,18,123.80 (unchanged from Day 0 seed). Three open
calls get executed today, plus two sizing adds consistent with this book's
central "sizing, not stock-picking" thesis:

- **SELL all 230 BCG @ ₹9.15** → proceeds ₹2,104.50. Full exit on Day 1's
  "recommend exit" call — confirmed SEBI fraud finding, Stage-1 ASM
  surveillance, no new regulatory update found to soften that read.
- **SELL 45 of 135 GOLDBEES @ ₹131.32** → proceeds ₹5,909.40. Same
  extending-rally logic as Sujal's book, lower urgency given smaller weight.
- **SELL 18 of 53 ADANIPOWER @ ₹205.50** → proceeds ₹3,699.00. Same
  rich-valuation-after-the-run logic, lower priority than Sujal's book —
  no dangerous single-stock concentration here.
- **BUY 5 BAJFINANCE @ ₹1,095.00** → ₹5,475.00. An undersized winner
  (+65.9%, only 5.2% of the book); Nomura raised its target to ₹1,270 on
  20–21 Aug despite the RBI's draft revolving-credit proposal — a fresh,
  independent reason the conviction case still holds.
- **BUY 1 HAL @ ₹5,000.00** → ₹5,000.00. Same undersizing logic (+62.5%,
  6.0% weight); research affirms the defense/PSU-vs-IT sector bifurcation
  this book sits on both sides of is still intact.
- **BUY 4 NIFTYBEES @ ₹276.83** → ₹1,107.32, using the remainder of trim
  proceeds. Total proceeds ₹11,712.90; total buys ₹11,582.32; ₹130.58 left
  as cash.
- TCS, Tata Group concentration (20.2%), TMPV/TMCV pairing, IRFC, AWL:
  unchanged, no action — no new information on any of these since Friday.
  TCS's succession overhang is developing (T V Narendran named a frontrunner
  per weekend reporting) but that's elaboration on an already-known story,
  not a new event changing the "hold, no add" call.

**Data-quality note carried forward:** today's research independently
confirmed Friday 21 Aug's ASIANPAINT close at ₹2,640.00, vs. the ₹2,630.80
figure `LOG_manali.md` Day 1 flagged as unverified. Doesn't affect this
ledger's cost basis; flagging so tonight's mark-to-market uses the corrected
figure.

**Post-trade sizing snapshot (at reference prices):** BAJFINANCE weight rises
from 5.2% to ~6.6%; HAL from 6.0% to ~7.2%; ADANIPOWER falls from 2.6% to
~1.7%; GOLDBEES falls from 4.2% to ~2.8%; BCG goes to 0%. Post-trade value:
₹4,18,123.80 (unchanged — reallocation only).

## Sun, 23 Aug 2026 (morning check-in) — skipped

skipped — today (Sunday, 23 Aug 2026) is before the simulation window start
(Monday 24 Aug 2026) and is also a weekend. No research, no trades, no ledger
changes. First real trading-day check-in is Monday 24 Aug 2026 morning.

## Day 0 — Sunday, 23 Aug 2026 (kickoff, not a trading day)

**Simulation established.** Both paper ledgers seeded from the real accounts'
actual holdings as of this week's fetch, priced at Friday 21 Aug close (the
same baseline already used in `LOG.md` Day 2 and `LOG_manali.md` Day 1):

| Account | Holdings | Seeded value |
|---|---|---|
| Sujal (paper) | 5 | ₹36,182.70 |
| Manali (paper) | 32 | ₹4,18,123.80 |

No trades yet — the first real simulated decisions happen Monday 24 Aug
morning. Both ledgers start with ₹0 cash (fully invested, matching the real
accounts today).

**What "success" looks like at the end (4 Sep):** the simulated portfolios'
total value compared against two baselines computed over the same window —
(a) simple buy-and-hold with zero trades, and (b) Nifty 50's own move — so the
result isn't just "did it go up" but "did the daily decisions add anything
over doing nothing, and over the market's own drift."

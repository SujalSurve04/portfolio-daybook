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

## Day 9 — Thursday, 3 Sep 2026 (evening check-in)

**Self-check:** today's real date is Thursday 3 Sep 2026 — inside the 24
Aug–4 Sep window, a weekday, no NSE/BSE holiday (confirmed this morning;
next holiday remains Ganesh Chaturthi, Mon 14 Sep 2026). Proceeding with the
evening mark-to-market. No trades were made today (see this morning's
entry) — this is a pure valuation pass. Tomorrow, Friday 4 Sep 2026, is the
final scheduled day of the 10-day window; tomorrow evening's entry will
carry the final summary.

**Closing prices researched this evening** (NSE, 3 Sep 2026 close; four
parallel research passes split across Sujal's 6 + part of Manali's book,
another slice, another slice, and the remainder of Manali's book plus
Nifty 50/BCG — each cross-checking stockanalysis.com against Groww,
Tickertape, IndMoney, 5paisa, Dhan, or Google Finance; official
nseindia.com quote pages returned 503/blocked in every pass, so all figures
rest on third-party aggregators cross-checked against each other rather
than the exchange's own feed). Day-change % below is computed against this
log's own confirmed Wed 2 Sep close, consistent with prior entries:

| Symbol | Close (₹) | Day chg vs Wed's logged close | Confidence | Note |
|---|---|---|---|---|
| Nifty 50 | 23,873.45 | −0.17% (−41.00 pts) | High (2-source exact match) | Anticipated GIFT Nifty gap-up didn't hold through the session — IT, Auto, FMCG, Pharma and Consumer Durables were the weak sectors; Realty and Financials (Bank Nifty +0.36–0.92%) outperformed. Sector rotation, no single dominant story. |
| IRFC | 82.68 | +0.28% | High (2-source, within ₹0.05) | No dated catalyst; GST show-cause notice remains the only open item. |
| TMPV | 312.00 | 0.00% | High (3-source exact match) | No dated catalyst found. |
| ADANIGREEN | 1,283.70 | −0.63% | Medium-High (2-source, within ₹0.60) | EGM held today (independent-director reappointments — Romesh Sobti, Neera Saggi, Dr Anup Shah), a routine, already-known calendar item confirmed dated today; not a plausible driver of the modest decline. |
| ADANIPOWER | 208.29 | +0.72% | Medium (3 of 4 sources agree; 1 outlier discarded) | No dated catalyst found; no follow-up on Tuesday's Bangladesh dispatch-cut item. |
| GOLDBEES | 126.19 | +2.12% | High (2-source, within ₹0.08) | Gold rallied sharply today — MCX gold +1.2–1.25%, spot gold above $4,400/oz, rebounding after three down sessions on a weaker USD and easing US Treasury yields (multiple India bullion outlets, dated today). Macro-driven, not company-specific. |
| NIFTYBEES | 272.59 | +0.01% | Medium — flagged anomaly | Essentially flat despite Nifty 50 falling −0.17% same session; two trackers agree with each other but not with the index move, suggesting a data-freshness lag in the sources rather than a real divergence. Used as researched, per the no-invented-numbers rule; flagged as an open data-quality item, not corrected. |
| RELIANCE | 1,302.50 | −0.81% | High (2-source exact match) | No dated catalyst found; the Texas-refinery/SKIMS stories in circulation are dated 6 Aug, not today. |
| LT | 3,975.00 | −0.36% | High (2-source exact match) | No dated catalyst found; recent order-win news is late-Aug, not today. |
| ASIANPAINT | 2,544.00 | +0.65% | High (2-source exact match) | No dated catalyst found. |
| HDFCBANK | 707.70 | +0.95% | Medium (2-source spread ~₹2, midpoint used) | No dated catalyst; Jagdishan-retirement/succession coverage in circulation is dated 31 Aug, not today. |
| HAL | 4,770.00 | −0.14% | Medium (4-source spread ~₹21, midpoint-ish figure used) | Genuinely dated-today item found (The Week): CCS approval for the ₹13,500cr IMRH helicopter program reported "nearing," Safran Aravalli engine contract said finalized — but the stock was flat/slightly down, so the market isn't yet pricing this as confirmed; logged as an advancing watch item, not an action trigger. |
| GROWW | 190.24 | +0.19% | High (2-source exact match) | No new block-deal news found; continues the stabilized read. |
| TMCV | 456.08 | +1.93% | Low/Medium — real 2% source spread (460.35 vs 451.80), midpoint used | No dated catalyst found for either reading. |
| CLEAN | 851.95 | −1.28% | Medium (cluster 850.95–852.95, one 876.9 outlier discarded) | No dated-today news found explaining this week's earlier unexplained rally; a dividend-record-date item surfaced but conflicting sources disagree whether it lands today (3 Sep) or 5 Sep — not confirmed, still an open watch item. |
| MAZDOCK | 2,474.00 | +0.88% | High (2-source exact match) | No dated catalyst; Project 75(I) CCS sign-off still pending, still targeted for September. |
| BEL | 408.50 | +0.75% | High (3-source agree) | No dated catalyst found. |
| DEEPAKNTR | 1,726.10 | −0.46% | High (2-source, within ₹1.60) | No dated catalyst found. |
| BAJFINANCE | 1,050.15 | −0.47% | High (2-source, within ₹2.30) | No dated catalyst; RBI's NBFC revolving-credit draft remains unfinalised since the 28 Aug comment-window close. |
| BAJAJHFL | 82.99 | +0.17% | High (2-source, within ₹0.07) | Same RBI-draft overhang as BAJFINANCE, unchanged. |
| DSSL | 1,005.90 | −0.95% | Medium (2-source spread ~₹5.80) | No dated catalyst; most recent disclosure is a 2 Sep board meeting (AGM date, CMD reappointment), not a today item. **Data-quality flag:** research this evening surfaced that NSE ticker DSSL corresponds to Dynacons Systems & Solutions, not Dee Development Engineers (which trades as DEEDEV) — this log's DSSL prices have consistently tracked Dynacons Systems throughout the window, so continuity is preserved, but the security's identity is worth a human double-check against the real Groww holding this ledger models. |
| BERGEPAINT | 490.35 | +0.47% | Medium (2-source spread ~₹2.10) | No dated catalyst found. |
| TCS | 2,333.90 | −0.43% | High (2-source exact match, 1 outlier discarded) | No new Tata Sons chairmanship development dated today; Narendran-frontrunner story remains unofficial, board meeting still expected ~17 Sep. |
| HINDCOPPER | 518.27 | −0.69% | High (3-source converge within ₹0.70) | No dated-today catalyst; only a dividend record-date notice (16 Sep) surfaced, not a plausible same-day mover. |
| NEWGEN | 517.65 | −0.60% | Medium (2-source exact match, 1 stale outlier discarded) | CRISIL reaffirmed Newgen's A1 short-term rating on ₹125cr bank facilities today — neutral/mildly positive, not a driver of the modest decline. |
| SRF | 2,617.50 | +1.22% | High (2-source, within ₹1) | No dated catalyst found. |
| ABCAPITAL | 402.00 | +1.69% | High (2-source exact match) | No dated catalyst found. |
| AWL | 190.53 | −0.25% | Medium (2-source, within ₹0.53) | Checked specifically for a new Delhi HC/FSSAI update dated today — none found; most recent coverage (Centre/FSSAI jurisdiction objection rejected, 4-week response ordered) is dated 1 Sep, already logged; next hearing still 5 Nov. |
| NTPC | 330.83 | +0.51% | High (2-source, within ₹0.15) | No dated catalyst; note NTPC's ₹3.50/share dividend paid 2 Sep, not today. |
| ETERNAL | 324.80 | −0.52% | High (2-source exact match, 1 stale outlier discarded) | No dated catalyst found. |
| NFL | 70.28 | +0.34% | Medium (single clear source) | No dated catalyst found. |
| ITBEES | 34.29 | −0.29% | High (2-source exact match) | Tracks continued Nifty IT softness, consistent with TCS's decline today. |
| SILVERBEES | 219.88 | +1.99% | Medium-High (single primary source, internally consistent) | Silver rallied alongside gold today — multiple India bullion outlets (dated today) report a rebound to ~₹2,37,790/kg on a weaker USD and easing yields, directly explaining the move. |
| BCG | 9.03 | +0.89% | Medium (2-source, within ₹0.06) | For buy-and-hold benchmark only — not held after Day 1's exit. **Data-quality flag:** research this evening confirmed NSE ticker BCG corresponds to Brightcom Group Ltd (matches this log's price range throughout), not Baazar Style Retail (which trades as STYLEBAAZA, ~₹395) — this log's BCG has consistently tracked Brightcom Group, so continuity is preserved, but the security's identity is worth a human double-check against the real Groww holding this ledger models. |

**Data-quality note:** four names (HDFCBANK, HAL, TMCV, CLEAN) had genuine
cross-source spreads tonight rather than simple rounding noise, and
NIFTYBEES's flat print doesn't square with Nifty 50's own −0.17% move —
all used as researched with Medium confidence flagged, none corrected or
guessed at, consistent with the "never invent numbers" rule. Two long-
running ticker-identity questions (DSSL, BCG) were resolved this evening —
both map to the securities this log has been pricing all along (Dynacons
Systems and Brightcom Group respectively), so no historical figures need
restating, but both are worth a one-time human check against the real
Groww account holdings before this framework is trusted with real trades.

### Sujal's paper book — mark-to-market

| | Value | Since Day 0 (₹36,182.70) |
|---|---|---|
| **Actual (traded) book** | **₹35,759.51** | **−₹423.19 (−1.17%)** |
| Buy-and-hold benchmark (no trades) | ₹35,946.80 | −₹235.90 (−0.65%) |
| Nifty 50-tracking benchmark | ₹35,617.92 | −₹564.78 (−1.56%) |

Day's move: +₹92.94 (+0.26%) vs yesterday's ₹35,666.57 close — GOLDBEES
(+2.12%) and ADANIPOWER (+0.72%) drove the gain, ADANIGREEN (−0.63%) was
the lone drag. Buy-and-hold reconstructed from the original Day-0
quantities (IRFC 30, TMPV 5, ADANIGREEN 6, ADANIPOWER 95, GOLDBEES 35, 0
cash) marked at today's same closes.

**Reading it:** the cumulative actual-vs-buy-hold gap **widened again,
from −₹90.23 to −₹187.29** — today's gold rally is the same mechanism as
the Adani rebound sessions: buy-and-hold's larger 35-share GOLDBEES stake
(vs the trimmed book's 20 shares) and larger 95-share ADANIPOWER stake (vs
55) both captured more of today's up-move than the traded book did. Nine
sessions in, the trim has now cost more than it's saved outside Monday's
single crash day. Against the Nifty-tracking benchmark, though, the
picture flips the other way: the actual book's cumulative −1.17% is now
**well ahead** of the pure-index benchmark's −1.56% (a gap that didn't
exist yesterday, when actual and Nifty-tracking were both around −1.4%) —
today's gold and Adani-Power strength is exactly the kind of single-name
return the index itself doesn't capture, so even the trimmed, diversified
book still benefits from stock selection over simply holding Nifty. The
open read for tomorrow's final entry: this book beats a pure-index
allocation either way (concentrated or trimmed), but the specific trim
decision made on Day 1 has been a net cost against not trading at all.

### Manali's paper book — mark-to-market

| | Value | Since Day 0 (₹4,18,123.80) |
|---|---|---|
| **Actual (traded) book** | **₹4,09,127.34** | **−₹8,996.46 (−2.15%)** |
| Buy-and-hold benchmark (no trades) | ₹4,09,390.32 | −₹8,733.48 (−2.09%) |
| Nifty 50-tracking benchmark | ₹4,11,597.30 | −₹6,526.50 (−1.56%) |

Day's move: +₹1,289.34 (+0.32%) vs yesterday's ₹4,07,838.00 close — a
broadly firmer session led by SILVERBEES (+1.99%), ABCAPITAL (+1.69%),
SRF (+1.22%), TMCV (+1.93%) and HDFCBANK (+0.95%), partly offset by CLEAN
(−1.28%), HINDCOPPER (−0.69%) and NEWGEN (−0.60%). Buy-and-hold
reconstructed from the original Day-0 quantities (today's 31 holdings plus
BCG 230 reinstated, GOLDBEES 135, ADANIPOWER 53, BAJFINANCE 20, HAL 5,
NIFTYBEES 90 — i.e. Day 1's trades reversed) marked at today's same
closes, including BCG's ₹9.03 close.

**Reading it:** the cumulative actual-vs-buy-hold gap **widened again,
from −₹68.95 to −₹262.98** — the same gold-rally mechanism as Sujal's
book: buy-and-hold's larger 135-share GOLDBEES stake and 53-share
ADANIPOWER stake both captured more of today's gains than the trimmed
book's smaller 90 and 35 shares. As on most sessions this window, though,
this book's day-to-day return is still driven overwhelmingly by its
diversification (today: SILVERBEES, ABCAPITAL, SRF, TMCV, HDFCBANK) rather
than by the Day 1 trade thesis, whose net cumulative cost (~0.06% of book
value) remains close to noise-level relative to the book's size. Against
the Nifty-tracking benchmark, the book again underperforms both today
(+0.32% vs the index's −0.17%, a rare day it beats the index outright on
the strength of gold/silver/financials exposure the index itself doesn't
carry) and cumulatively (−2.15% vs −1.56%) — the same heavier tilt toward
financials, paints and TCS that has lagged the index most sessions this
window.

**Watch items carried forward, unchanged or advanced today:** CLEAN's
still-unexplained rally (dividend-date conflict unresolved), GROWW's
block-deal aftermath (stabilized), MAZDOCK's CCS sign-off (still pending),
AWL's FSSAI Delhi HC hearing (next 5 Nov), RBI's NBFC revolving-credit
draft overhang on BAJFINANCE/BAJAJHFL (still unfinalised), and HAL's IMRH
CCS approval (reported nearing today, not yet confirmed or priced).

**Decisions today — Sujal:** (evening check-in — no new decisions,
mark-to-market only)
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — today's
  gold rally and mixed Adani-group move are the same trim/give-back
  dynamic already under test since Day 1; ADANIGREEN's EGM was a routine,
  already-known calendar item. No research finding today changes any open
  thesis.

**Decisions today — Manali:** (evening check-in — no new decisions,
mark-to-market only)
- HOLD: everything (all 31 remaining holdings) — today's gain was driven
  by diversified factors (SILVERBEES, ABCAPITAL, SRF, TMCV, HDFCBANK)
  unrelated to any open Day 1 call. HAL's IMRH CCS-approval report is
  positive but not yet confirmed enough to act on; CLEAN, GROWW, MAZDOCK,
  AWL and the RBI NBFC draft remain open, non-escalating watch items.

## Day 9 — Thursday, 3 Sep 2026 (morning check-in)

**Self-check:** today's real date is Thursday 3 Sep 2026 — inside the 24
Aug–4 Sep window, a weekday. Verified via shell `date` that 3 Sep 2026 is a
Thursday. No NSE/BSE trading holiday in this stretch — confirmed on prior
runs (Zerodha's 2026 holiday calendar) that the next holiday is Ganesh
Chaturthi, Monday 14 Sep 2026; nothing has changed that. Proceeding.
Reference prices throughout use Wednesday 2 Sep's close (already researched
and logged in that evening's entry); actual fills at today's open will
differ.

**Macro backdrop researched this morning:** Firmer, gap-up open indicated.
US markets rebounded Wednesday 2 Sep after two straight down sessions — S&P
500 +0.46% to 7,666.60, Dow +0.56% to 53,061.95, Nasdaq +0.45% to 26,217.83
— as Treasury yields paused their climb. GIFT Nifty points to a modest
gap-up open, ~+0.55% (~24,095–24,096; one outlier +4.28% print from a
single source was discarded as unreliable after two independent sources —
ICICI Direct, Upstox — corroborated the smaller move). Brent crude holds
near recent highs (~$95.50/bbl, essentially flat today) after spiking ~5%
earlier in the week on US strikes near the Strait of Hormuz following
tanker attacks — elevated but not accelerating further today. Gold
(~$4,409/oz, +0.51%) and silver (~$66/oz, near two-week lows) are little
changed. Fed Chair Kevin Warsh's hawkish Jackson Hole stance continues to
dominate — markets now pricing ~70% odds of a 15–16 Sep rate hike — keeping
global bond yields at multi-year highs; a tightening-conditions backdrop,
not a single-name signal.

**Symbol-level research (all 6 Sujal + all 31 Manali holdings checked for
anything new since Wednesday's close, split across two parallel research
passes):**
- **ADANIGREEN**: an EGM is happening today, 3 Sep 2026, 11:00am IST
  (remote e-voting closed 2 Sep) — reappointment of independent directors,
  an already-known, routine calendar item, not a trigger. Also found: a
  promoter entity (Adani Infra) bought a further ~1.03% stake (~₹2,380cr) on
  Monday 1 Sep, and the stock rose ~3% Tuesday after commissioning a 139MW
  Khavda solar project — both incrementally positive but neither new-since-
  Wednesday nor large enough to be an action trigger on their own.
- **ADANIPOWER**: a genuinely new operational item — Adani reduced power
  dispatch to Bangladesh from its Godda plant on 2 Sep due to a coal-
  transport (rail) disruption. A real, dated item, but an operational
  hiccup at one plant's export volume, not a fundamentals or regulatory
  event — logged as a watch item, not actionable today.
- **IRFC**: no update since the 24 Aug GST show-cause notice (₹549.32cr);
  still "evaluating notice, no immediate financial impact" — unchanged.
- **LT** (Manali): a live order-win streak — two large plus two significant
  orders (up to ₹15,000cr combined) announced in 4 of the last 5 sessions,
  part of a broader ~$11.6bn Middle-East-led order run since July. Positive
  and genuinely dated, but a continuation of an already-known pattern
  (order wins have been a recurring, not new, theme for L&T this window),
  not a fresh discrete trigger.
- **HAL** (Manali): a report (dated to Sep 2026, exact day unconfirmed) says
  CCS approval for HAL's ₹13,500cr IMRH helicopter design plan is nearing,
  with the Safran Aravalli engine contract finalized. Plausible and
  positive but the date isn't pinned to today specifically — flagged, not
  acted on, consistent with the "never invent numbers" rule.
- **GROWW** (Manali): no new block-deal wave found since 27 Aug's Ribbit
  Capital sale (~2.1% stake, ~₹2,500cr) — unchanged, non-escalating watch
  item.
- **MAZDOCK** (Manali): Project 75(I) — Finance Ministry's ~₹70,000cr
  clearance (28 May) stands; CCS sign-off still not confirmed as of today,
  contract conclusion still targeted for September — unchanged.
- **AWL** (Manali): confirmed detail on the already-known Delhi HC/FSSAI
  Fortune-brand labeling case — the court rejected the Centre/FSSAI's
  jurisdiction objection and ordered a response within 4 weeks; next
  hearing remains 5 Nov. Procedural detail on an open item, not an
  escalation or new trigger.
- **RBI's NBFC revolving-credit draft proposal** (BAJFINANCE, BAJAJHFL,
  Manali): still in draft/consultation; comment window closed 28 Aug with
  no finalised rule found since — unchanged overhang.
- **CLEAN** (Manali): Tuesday evening's unexplained +5.09% rally to ₹863
  remains without a confirmed same-day catalyst after another dedicated
  search — only routine items found (₹4/share dividend ex-date 4 Sep, AGM
  12 Sep). Still logged as an open, unexplained watch item, not acted on.
- **HDFCBANK** (Manali): no new development on CEO Jagdishan's planned 26
  Oct retirement/succession search beyond the original 29 Aug filing — no
  successor named, unchanged.
- **TCS / Tata Sons** (Manali): no new development on the chairmanship
  succession story; board meeting still expected ~17 Sep, unchanged since
  mid-Aug.
- Every other symbol (TMPV, TMCV, GOLDBEES, NIFTYBEES, RELIANCE,
  ASIANPAINT, BEL, DEEPAKNTR, BAJFINANCE, BAJAJHFL, DSSL, BERGEPAINT,
  HINDCOPPER, NEWGEN, SRF, ABCAPITAL, NTPC, ETERNAL, NFL, ITBEES,
  SILVERBEES): no fresh, dated catalyst found since Wednesday's close in
  this morning's sweep — includes the four ETFs, checked for fund-level
  news and finding only routine pricing/AUM data.

**Decision:** no confirmed, material new information rises to a Buy/Sell/
Trim/Exit trigger in either book today. ADANIGREEN's EGM is a routine,
already-known calendar item; ADANIPOWER's Bangladesh dispatch cut is a
real but minor operational item at one plant, not a fundamentals or
regulatory event; LT's order-win streak and HAL's possible CCS approval are
both positive but continuations of already-known patterns or insufficiently
dated to act on. The macro backdrop (firmer US close, gap-up GIFT Nifty,
elevated-but-flat oil, still-hawkish Fed) is a broad tailwind, not a
single-name signal. CLEAN's rally remains a genuine open question with no
answer found; GROWW, MAZDOCK, AWL and the RBI NBFC draft all remain
open, non-escalating watch items. Both books' original Day 1 trades remain
the open calls under test — today adds a ninth data point, not a reason
for turnover.

**Decisions today — Sujal:**
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — no new
  research finding rises to an action trigger. ADANIGREEN's EGM (today) is
  routine; ADANIPOWER's Bangladesh dispatch cut is a minor operational
  item, not a fundamentals signal; IRFC's GST notice remains a watch item
  only.

**Decisions today — Manali:**
- HOLD: everything (all 31 remaining holdings) — no new research finding
  rises to an action trigger. LT's continuing order-win streak and HAL's
  possible (undated) CCS approval on the IMRH program are both positive but
  not fresh discrete triggers. GROWW, MAZDOCK's CCS sign-off, AWL's FSSAI
  case (procedural update only) and the RBI NBFC draft remain open,
  non-escalating watch items; CLEAN's unexplained rally is still
  unresolved.

## Day 8 — Wednesday, 2 Sep 2026 (evening check-in)

**Self-check:** today's real date is Wednesday 2 Sep 2026 — inside the 24
Aug–4 Sep window, a weekday, no NSE/BSE holiday (already confirmed this
morning; next holiday remains Ganesh Chaturthi, Mon 14 Sep 2026). Proceeding
with the evening mark-to-market. No trades were made today (see this
morning's entry) — this is a pure valuation pass.

**Closing prices researched this evening** (NSE, 2 Sep 2026 close; three
parallel research passes split roughly across Sujal's 6 + part of Manali's
book, another slice of Manali's book, and the remainder of Manali's book
plus Nifty 50/BCG, each cross-checking stockanalysis.com against Groww,
Google Finance, or a second independent web search per symbol). Day-change %
below is computed against **this log's own confirmed Tue 1 Sep close**
(carried forward from yesterday evening's entry) rather than each research
pass's own re-fetched "previous close," since a few passes surfaced small
(≤0.6pp) rounding/timestamp discrepancies on their prev-close reads
(ADANIGREEN, ADANIPOWER, ASIANPAINT, CLEAN, ABCAPITAL) — using this log's own
number keeps the day-over-day math internally consistent with prior entries:

| Symbol | Close (₹) | Day chg vs Tue's logged close | Confidence | Note |
|---|---|---|---|---|
| Nifty 50 | 23,914.45 | −0.59% (−141.35 pts) | High (2-source) | Broader market pulled back on rising crude oil pressure (Sensex −472 pts, Nifty below 23,900); no single dominant sector story identified. |
| IRFC | 82.45 | +0.01% | High | Essentially flat; no dated catalyst; GST show-cause notice remains the only open item. |
| TMPV | 312.00 | +0.65% | High | No dated catalyst found. |
| ADANIGREEN | 1,291.90 | +2.70% | High | Business Today (dated today) noted shares climbing despite the broader selloff; no specific driver confirmed — Adani-group strength continuing from the past two sessions' rebound. |
| ADANIPOWER | 206.81 | +1.73% | High | Same Adani-group strength as ADANIGREEN; no company-specific news found. |
| GOLDBEES | 123.57 | −1.54% | High | Gold ETF continuing its slide (per this morning's macro research); no company-specific driver, tracks bullion. |
| NIFTYBEES | 272.55 | −0.38% | High | Tracks the index's mild decline. |
| RELIANCE | 1,313.10 | +0.31% | High | No dated catalyst found. |
| LT | 3,989.20 | −0.25% | High | No dated catalyst found. |
| ASIANPAINT | 2,527.50 | −1.38% | High | No dated same-day catalyst found. |
| HDFCBANK | 701.05 | −1.52% | High | New US securities-class-action law-firm press releases (Portnoy Law, Bronstein Gewirtz & Grossman) dated today reiterate the pre-existing MSRDC-deposit matter — recurring solicitation noise on an already-known issue, not a new fact pattern; treated as continued digestion of the CEO-succession news (logged this morning), not a fresh trigger. |
| HAL | 4,776.50 | −0.47% | High | No dated catalyst found. |
| GROWW | 189.88 | +0.25% | High | No new block-deal news found; continues the stabilized read. |
| TMCV | 447.45 | −3.64% | High (2-source exact match) | No dated catalyst found; the day's largest single-name decline in either book, likely broad auto-sector softness rather than company-specific. |
| CLEAN | 863.00 | +5.09% | High (2-source agree ~863) | No dated same-day catalyst found — nearby events (31 Aug ESOP allotment, 4 Sep ex-dividend, 12 Sep AGM) don't land today; flagged as an unexplained outlier, watch item for tomorrow. |
| MAZDOCK | ~2,452.50 (2,446.00–2,459.00) | −1.32% | Medium (2 sources disagree by ~₹13, midpoint used) | No dated catalyst; Project 75(I) CCS sign-off still pending. |
| BEL | ~405.45 (405.15–405.75) | −1.23% | High (2 sources close together, midpoint used) | No dated catalyst found. |
| DEEPAKNTR | 1,734.00 | −2.53% | Medium (single source) | No dated catalyst found; in line with a broadly weak session. |
| BAJFINANCE | ~1,055.10 (1,054.30–1,055.90) | +0.61% | High (2 sources agree closely, midpoint used) | No fresh RBI revolving-credit-proposal follow-up found. |
| BAJAJHFL | 82.85 | −0.01% | High | Essentially flat. |
| DSSL | 1,015.50 | −2.35% | Medium (single source; thinly-traded microcap) | No dated catalyst found. |
| BERGEPAINT | 488.05 | −0.63% | High (2-source exact match) | No dated catalyst found. |
| TCS | ~2,344.00 (2,340.00–2,348.00) | −1.06% | High (2 sources bracket, midpoint used) | Checked specifically for new Tata Sons succession news dated today — none found; the Chandrasekaran/Narendran story remains unchanged since mid-Aug, board meeting still expected ~17 Sep. |
| HINDCOPPER | 521.85 | −0.79% | Medium | No dated catalyst found; broad market weakness. |
| NEWGEN | 520.80 | −1.78% | High (2-source, midday print consistent with EOD) | No dated-today catalyst found; underperformed the index. |
| SRF | 2,586.00 | +0.40% | Medium | No dated catalyst found. |
| ABCAPITAL | 395.30 | +0.91% | High (2-source agree) | No dated catalyst found. |
| AWL | 191.00 | −1.65% | Medium | Checked specifically for a new Delhi HC/FSSAI update dated today — none found; yesterday's 1 Sep FSSAI-labeling story (already logged) is the only related coverage, likely continued drag from that plus general market weakness. |
| NTPC | 329.15 | +0.72% | Medium | No dated catalyst found. |
| ETERNAL | 326.50 | +0.11% | Medium | Essentially flat; no dated catalyst found. |
| NFL | 70.04 | −0.37% | Medium | No dated catalyst found. |
| ITBEES | 34.39 | −1.15% | High (prev-close matches exactly) | Tracks Nifty IT weakness, consistent with TCS's decline today. |
| SILVERBEES | 215.59 | −0.98% | High (2-source, near-exact) | No dated catalyst found. |
| BCG | 8.95 | −0.67% | Medium | For buy-and-hold benchmark only — not held after Day 1's exit. |

**Data-quality note:** MAZDOCK, BEL, BAJFINANCE and TCS each had a small
(~₹10–13, sub-1pp) spread between two sources this evening; midpoints are
used and flagged Medium/High accordingly rather than picking one silently.
CLEAN's +5.09% move is a genuine outlier with no confirmed same-day catalyst
found after a specific check — logged as an open watch item rather than
acted on, consistent with the "never invent numbers" rule (no fabricated
explanation offered). AWL and HDFCBANK were both specifically re-checked for
new dated news given their open storylines (FSSAI hearing, CEO succession)
— neither had anything new today; both moves read as continued digestion of
already-logged information, not fresh triggers.

### Sujal's paper book — mark-to-market

| | Value | Since Day 0 (₹36,182.70) |
|---|---|---|
| **Actual (traded) book** | **₹35,666.57** | **−₹516.13 (−1.43%)** |
| Buy-and-hold benchmark (no trades) | ₹35,756.80 | −₹425.90 (−1.18%) |
| Nifty 50-tracking benchmark | ₹35,679.09 | −₹503.61 (−1.39%) |

Day's move: +₹330.95 (+0.94%) vs yesterday's ₹35,335.62 close — the book
rose again as ADANIPOWER (+1.73%) and ADANIGREEN (+2.70%) extended their
rebound from Monday's Adani/MSCI selloff for a second straight session.
Buy-and-hold reconstructed from the original Day-0 quantities (IRFC 30,
TMPV 5, ADANIGREEN 6, ADANIPOWER 95, GOLDBEES 35, 0 cash) marked at today's
same closes.

**Reading it:** the cumulative actual-vs-buy-hold gap **flipped negative
today, from +₹59.02 to −₹90.23** — the trim's give-back on this second
rebound session finally outweighs the crash-day benefit it banked on
Monday, and for the first time since Monday's crash, the traded book is
now behind doing nothing since Day 0. It's also, for the first time,
narrowly behind the Nifty-tracking benchmark too (−1.43% actual vs −1.39%
Nifty-tracking vs −1.18% buy-and-hold) — an honest, unflattering result:
on a two-session Adani rebound, both the concentrated buy-and-hold book and
the diversified index benchmark outgained the trimmed, NIFTYBEES-diversified
actual book. This doesn't undo the trim's clear benefit on Monday's crash
day (still the largest single-day swing either way across all eight
sessions), but it's a reminder that de-risking a concentrated winner costs
real, measurable return on exactly the days that winner keeps winning — the
open question the rest of this test window needs to answer is whether the
crash-day protection is worth more than the rebound-day cost over the full
period, not just this one pair of sessions.

### Manali's paper book — mark-to-market

| | Value | Since Day 0 (₹4,18,123.80) |
|---|---|---|
| **Actual (traded) book** | **₹4,07,838.00** | **−₹10,285.80 (−2.46%)** |
| Buy-and-hold benchmark (no trades) | ₹4,07,906.95 | −₹10,216.85 (−2.44%) |
| Nifty 50-tracking benchmark | ₹4,12,304.10 | −₹5,819.70 (−1.39%) |

Day's move: −₹2,232.37 (−0.54%) vs yesterday's ₹4,10,070.37 close — a
broadly softer session across this book's largest weights: ASIANPAINT
(−1.38%), TCS (−1.06%), NEWGEN (−1.78%), DEEPAKNTR (−2.53%) and TMCV
(−3.64%, this book's single largest same-day % decline) outweighed the
Adani-group strength (ADANIPOWER +1.73%, only ~1.8% weight here) that lifted
Sujal's book. Buy-and-hold reconstructed from the original Day-0 quantities
(today's 31 holdings plus BCG 230 reinstated, GOLDBEES 135, ADANIPOWER 53,
BAJFINANCE 20, HAL 5, NIFTYBEES 90 — i.e. Day 1's trades reversed) marked at
today's same closes, including BCG's ₹8.95 close.

**Reading it:** the same Adani mechanism working against Sujal's book today
works narrowly in this book's favor — the cumulative actual-vs-buy-hold gap
**narrowed to −₹68.95, from −₹111.72** — buy-and-hold's larger 53-share
ADANIPOWER stake captured slightly more of today's rebound than the traded
book's smaller 35-share stake, so the gap (still a cost, at ~0.017% of book
value) shrank rather than grew. Eight sessions of evidence continue to show
this book's day-to-day return is driven overwhelmingly by its 31-name
diversification (today, TMCV/ASIANPAINT/TCS/NEWGEN/DEEPAKNTR) rather than by
the Day 1 trade thesis, whose net effect remains close to noise-level either
way. Against the Nifty-tracking benchmark, the book again underperforms both
today (−0.54% vs the index's −0.59%, essentially in line for once) and
cumulatively (−2.46% vs −1.39%) — this book's heavier tilt toward
financials, TCS and paints continues to lag the index more than its Adani or
gold exposure offsets, the same pattern seen on most sessions this window.
**Watch items carried forward, unchanged today:** CLEAN's unexplained +5.09%
rally (Sujal's book only), GROWW's block-deal aftermath, MAZDOCK's CCS
sign-off, AWL's FSSAI Delhi HC hearing (next 5 Nov), and RBI's NBFC
revolving-credit draft overhang on BAJFINANCE/BAJAJHFL.

**Decisions today — Sujal:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — today's
  continued Adani-group rebound is the expected give-back on the trim's
  protective bet, not a reason to trade further; no research finding today
  changes any open thesis.

**Decisions today — Manali:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: everything (all 31 remaining holdings) — today's decline was driven
  by diversified factors (TMCV, ASIANPAINT, TCS, NEWGEN, DEEPAKNTR)
  unrelated to any open Day 1 call. CLEAN's unexplained rally on Sujal's
  book, GROWW, MAZDOCK, AWL and the RBI NBFC draft remain open watch items,
  none escalating to an action trigger today.

## Day 8 — Wednesday, 2 Sep 2026 (morning check-in)

**Self-check:** today's real date is Wednesday 2 Sep 2026 — inside the 24
Aug–4 Sep window, a weekday. Confirmed via the shell `date` command that 2
Sep 2026 is a Wednesday. Re-confirmed via web search (Zerodha's 2026 holiday
calendar) that there is no NSE/BSE trading holiday in this stretch — the
next holiday is Ganesh Chaturthi, Monday 14 Sep 2026 (also newly confirmed:
Labor Day in the US falls on Monday 7 Sep 2026, not 31 Aug, since the first
Monday of September 2026 is the 7th — 31 Aug was a normal US trading Monday,
so no gap in the US-close reference chain used this week). Proceeding.
Reference prices throughout use Tuesday 1 Sep's close (already researched
and logged in that evening's entry); actual fills at today's open will
differ.

**Macro backdrop researched this morning:** Cautious-to-negative overnight
read. US markets fell across the board on Tuesday 1 Sep — S&P 500 −0.35% to
~7,659.79, Dow −0.79% to ~52,766.88, Nasdaq −1.03% to ~26,099.77 — a
tech-led selloff, the Nasdaq's decline roughly triple the S&P's. GIFT Nifty
had been indicating a mild positive lean earlier Tuesday evening IST
(~24,129.50, +0.33% vs a ~24,051 reference) before the US close turned
negative, so today's actual open is more likely flat-to-cautious once that
overnight weakness is priced in — no clean single-direction signal found
pre-open. Gold extended its slide, falling to ~$4,358.74/oz (~−1.9% on the
day, near two-week lows) and silver to ~$64.80/oz, both still pressured by
hawkish Fed-hike expectations (Chair Kevin Warsh) and firm yields — bearish
carryover for GOLDBEES/SILVERBEES. Brent crude held elevated (~$91–92/bbl),
consistent with the past week's West Asia-tension premium, no fresh spike
or reversal.

**Symbol-level research (all 6 Sujal + all 31 Manali holdings checked for
anything new since Tuesday's close):**
- **IRFC**: no update since the 24 Aug GST show-cause notice (₹549.32cr,
  Section 73 CGST Act, excess ITC claim FY22-23); still "evaluating notice,
  no immediate financial impact" — unchanged, watch item only.
- **ADANIGREEN**: EGM scheduled for tomorrow, 3 Sep 2026 (remote e-voting
  window 30 Aug–2 Sep, closing today) — already-known calendar item, not a
  new trigger. Continuing investor-meeting roadshow (Mumbai, Chennai, Elara
  Conference, London Adani Annual Conference) also already known. A
  promoter-entity share-purchase item (Adani Infra, ~1.03% stake at ~₹1,400/
  share) surfaced in search results without a clear date and at a price
  well above yesterday's ₹1,257.90 close — could not confirm this is recent;
  not acted on given the dating uncertainty.
- **ADANIPOWER**: no fresh company-specific news since Tuesday's rebound;
  no adverse follow-up to last week's MSCI-rebalancing selloff found.
- **HDFCBANK** (Manali): found a genuinely new-to-this-log item on
  investigation — CEO Sashidhar Jagdishan announced (in a Saturday 29 Aug
  exchange filing) he will not seek reappointment and retires 26 Oct 2026,
  wanting a "clean slate" for his successor; board has fast-tracked the
  succession search. This is 4 days old, not a same-day catalyst — and it
  plausibly explains Monday 31 Aug's unexplained −1.57% HDFCBANK move
  (flagged that day as "runs counter to the sector, no explaining article
  surfaced"), which has already been followed by a +0.41% recovery on
  Tuesday. Treated as informational (closes a previously open question, no
  longer unexplained) rather than a new trigger — the market has already
  digested and partly reversed the reaction.
- **RELIANCE**: Jio Platforms received SEBI's observation letter on its
  IPO DRHP — a process step (was already filed, expected), not a fresh
  surprise; no same-day price-moving reaction confirmed.
- **GROWW** (Manali): no second wave of block-deal selling found since the
  27 Aug Ribbit Capital disclosure (~2.1% stake, ~₹2,500cr); same
  not-escalating watch item as prior days.
- **MAZDOCK** (Manali): Project 75(I) — Finance Ministry approval
  (~₹70,000cr) already reported; final CCS sign-off still the outstanding
  step, still targeted around September, still not confirmed. No change.
- **AWL** (Manali): no new development found on yesterday's logged Delhi HC/
  FSSAI Fortune-labeling item (next hearing 5 Nov); remains open, not
  escalating.
- **RBI's NBFC revolving-credit draft proposal** (affects BAJFINANCE,
  BAJAJHFL, Manali): the stakeholder-comment window closed 28 Aug 2026;
  still in draft/consultation, no finalised rule and no new development
  since — unchanged overhang, not actionable.
- Every other symbol (TMPV, TMCV, GOLDBEES, NIFTYBEES, LT, ASIANPAINT, HAL,
  CLEAN, BEL, DEEPAKNTR, DSSL, BERGEPAINT, TCS, HINDCOPPER, NEWGEN, SRF,
  ABCAPITAL, NTPC, ETERNAL, NFL, ITBEES, SILVERBEES): no fresh, dated
  catalyst found since Tuesday's close in this morning's sweep, including a
  general "stocks to watch Wednesday" search that surfaced nothing
  involving any held name (day's actual highlights were an IPO debut and a
  DCM Shriram plant commissioning, neither held here). TCS's Tata Sons
  succession story is unchanged since mid-Aug (Chandrasekaran's non-renewal
  already known; board meeting still expected ~17 Sep).

**Decision:** no confirmed, material new information changes any open
thesis in either book today. The HDFCBANK CEO-succession item is the one
genuinely new finding this morning, but it's several days old, already
reflected (and partly reversed) in price action, and a leadership-transition
announcement at a large, well-capitalised private bank isn't by itself a
sell/trim trigger under either framework — logged as a closed information
gap, not an action item. Gold/silver's continued slide is a real but
market-wide macro drag on GOLDBEES/SILVERBEES, not a name-specific signal;
both books already trimmed into the gold rally on Day 1 and are holding
smaller residual positions deliberately. Both books' Day 1 trades remain the
open calls under test — today adds an eighth data point, not a reason for
turnover.

**Decisions today — Sujal:**
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — no new
  research finding changes any position; IRFC's GST notice remains a watch
  item only; ADANIGREEN's EGM (tomorrow) and roadshow calendar are
  already-known, non-actionable items.

**Decisions today — Manali:**
- HOLD: everything (all 31 remaining holdings) — no new research finding
  changes any position. HDFCBANK's CEO-succession news (Jagdishan retiring
  26 Oct) is newly logged here but is several days old and already priced
  in, not an action trigger. GROWW's block-deal aftermath continues as an
  open, non-escalating watch item; MAZDOCK's CCS sign-off remains pending;
  AWL's FSSAI Delhi HC item remains open, not escalating; RBI's NBFC
  revolving-credit draft remains an unfinalised overhang on BAJFINANCE/
  BAJAJHFL, not a fresh trigger.

## Day 7 — Tuesday, 1 Sep 2026 (evening check-in)

**Self-check:** today's real date is Tuesday 1 Sep 2026 — inside the 24 Aug–4
Sep window, a weekday, no NSE/BSE holiday (already confirmed this morning).
Proceeding with the evening mark-to-market. No trades were made today (see
this morning's entry) — this is a pure valuation pass.

**Closing prices researched this evening** (NSE, 1 Sep 2026 close; two
parallel research passes split across Sujal's 6 + part of Manali's book and
the rest of Manali's book, cross-checking stockanalysis.com against Groww,
Business Standard, or independent web-search snapshots per symbol; three
follow-up searches run directly this evening to resolve genuine source
conflicts on TCS, HDFCBANK and MAZDOCK):

| Symbol | Close (₹) | Prev close | Day chg | Confidence | Note |
|---|---|---|---|---|---|
| Nifty 50 | 24,055.80 | 24,080.40 | −0.10% (−24.60 pts) | High (2-source) | FMCG and IT the only gaining sectors; Healthcare, Auto, Realty, Pharma lagged. Risk-off carryover (US–Iran tension/oil, hawkish Fed read, firming US yields, FII outflows) but the **Adani complex reversed sharply, rebounding up to ~5%** a day after Monday's MSCI-rebalancing selloff (Business Standard), capping the index's downside. |
| IRFC | 82.44 | 83.34 | −1.08% | High (2-source) | No dated catalyst; GST show-cause notice remains the only open item. |
| TMPV | 310.00 | 308.85 | +0.37% | High (2-source, exact match) | No dated catalyst found. |
| ADANIGREEN | 1,257.90 | 1,214.90 | +3.54% | High | Adani-group rebound (group-wide, index-mechanics reversal, not company-specific). |
| ADANIPOWER | 203.30 | 198.00 | +2.68% | High | Same Adani-group rebound. |
| GOLDBEES | 125.50 | 127.32 | −1.43% | Medium (conflicting snippets ₹125 vs ₹126.81; 125.50 used as the closest-to-official read) | Gold fell despite risk-off, likely dollar/yield-driven. |
| NIFTYBEES | 273.60 | 274.87 | −0.46% | High (2-source) | Tracks index. |
| RELIANCE | 1,309.00 | 1,277.00 | +2.51% | High (exact match) | No dated catalyst beyond general session. |
| LT | 3,999.00 | 4,044.90 | −1.13% | Medium-High (prev close exact match, close has a ~₹19/0.5pp spread across sources, flagged not silently resolved) | No dated catalyst. |
| ASIANPAINT | 2,562.80 | 2,653.60 | −3.42% | Medium-High (prev close exact match; two sources agree on a sharp ~3% drop, day's biggest single-name loser researched) | No dated same-day catalyst found for the drop. |
| HDFCBANK | 711.90 | 709.00 | +0.41% | High — **resolved conflict**: an initial pass split between ₹709.50 (stockanalysis) and ₹711.90 (Groww + independent post-close search); a direct follow-up search this evening confirmed ₹711.90 via two independently-sourced, post-3:30pm-timestamped fetches | No dated catalyst. |
| HAL | 4,799.00 | 4,801.60 | −0.05% | Medium-High | Essentially flat; no dated catalyst. |
| GROWW | 189.41 | 192.06 | −1.38% | High (direct Groww page fetch matches stockanalysis exactly; a stale/conflicting generic search snippet was discarded) | No second wave of block-deal news found. |
| TMCV | 464.35 | 471.10 | −1.43% | High (2-source) | No dated catalyst. |
| CLEAN | 821.20 | 822.85 | −0.20% | Medium (single primary source, consistent with recent trajectory) | Goes ex-dividend 4 Sep (₹4/share) — not a same-day catalyst. |
| MAZDOCK | 2,485.30 | 2,480.00 | +0.21% | High — **resolved conflict**: initial pass split between stockanalysis (−0.16%) and Groww (+0.20%); a direct follow-up search this evening confirmed +0.21% (₹2,485.30) | Project 75(I) CCS sign-off still pending, no news. |
| BEL | 410.50 | 414.45 | −0.95% | High (2-source) | No dated catalyst. |
| DEEPAKNTR | 1,779.00 | 1,749.40 | +1.69% | High | No dated catalyst; still riding the Q1 FY27 results reported earlier this month. |
| BAJFINANCE | 1,048.70 | 1,057.00 | −0.79% | High | No fresh RBI revolving-credit-proposal follow-up found today. |
| BAJAJHFL | 82.86 | 84.02 | −1.38% | High (2-source, near-exact) | Drifting with parent Bajaj Finance weakness. |
| DSSL | 1,039.90 | 1,041.30 | −0.13% | Medium (single dated source) | No fresh order announced today. |
| BERGEPAINT | 491.15 | 497.75 | −1.33% | Medium-High (close itself has a small multi-source spread, flagged) | No dated catalyst. |
| TCS | 2,369.00 | 2,399.30 | −1.26% | High — **resolved conflict**: initial pass split between stockanalysis (₹2,356.00, −1.80%) and a Groww/post-close-timestamped cluster (₹2,369.00, −1.26%); a direct follow-up search this evening returned the same ₹2,369.00 figure, used as the mark | No dated company-specific news; Tata Sons succession story (T V Narendran reported frontrunner) unchanged since mid-Aug, board meeting expected ~17 Sep. |
| HINDCOPPER | 526.00 | 525.35 | +0.12% | High | No dated catalyst; broad metals softness from yesterday didn't repeat. |
| NEWGEN | 530.25 | 528.85 | +0.26% | High | No fresh order; CEO transition remains a closed item. |
| SRF | 2,575.80 | 2,560.40 | +0.60% | Medium (prev close exact match, close has a small multi-source spread) | No dated catalyst. |
| ABCAPITAL | 391.75 | 409.40 | −4.31% | Medium-High | No specific same-day trigger found; likely continued NBFC/financials weakness (RBI's Aug draft revolving-credit proposal overhang) compounding today's rate-sensitive-financials softness. |
| AWL | 194.20 | 192.55 | +0.86% | High | **New same-day item**: Delhi HC on 1 Sep sought Centre/FSSAI response on a plea re: a show-cause notice against Fortune-brand soyabean oil labeling; next hearing 5 Nov. Stock still closed up, so market read it as immaterial — logged as a fresh but non-escalating watch item, not an action trigger. |
| NTPC | 326.80 | 327.40 | −0.18% | High | Effectively flat; no dated catalyst. |
| ETERNAL | 326.15 | 328.10 | −0.59% | High | No dated catalyst; minor pullback from mid-Aug highs. |
| NFL | 70.30 | 70.37 | −0.10% | Medium (single dated source, trivial move) | No dated catalyst. |
| ITBEES | 34.79 | 34.32 | +1.37% | High | Rose despite TCS falling — other IT majors evidently offset. |
| SILVERBEES | 217.72 | 223.21 | −2.46% | High (2-source exact match) — flagged context | Two sources agree on the print, but it diverges from physical/MCX silver (reported ~flat-to-up today) — flagged for awareness, not blocking; ETF vs spot divergences happen intraday. |
| BCG | 9.01 | 9.04 | −0.33% | Low-Medium (single source) | For buy-and-hold benchmark only — not held after Day 1's exit; immaterial to either book either way. |

**Data-quality note:** three genuine source conflicts on real holdings (TCS,
HDFCBANK, MAZDOCK) were each resolved with a direct follow-up search this
evening rather than picked silently — all three follow-ups converged on the
post-close-timestamped cluster, which is used as the mark throughout. LT,
ASIANPAINT, BERGEPAINT and SRF had smaller (sub-1pp) multi-source spreads,
flagged but not blocking. SILVERBEES's ETF-vs-spot divergence is noted for
awareness, not acted on.

### Sujal's paper book — mark-to-market

| | Value | Since Day 0 (₹36,182.70) |
|---|---|---|
| **Actual (traded) book** | **₹35,335.62** | **−₹847.08 (−2.34%)** |
| Buy-and-hold benchmark (no trades) | ₹35,276.60 | −₹906.10 (−2.50%) |
| Nifty 50-tracking benchmark | ₹35,889.98 | −₹292.72 (−0.81%) |

Day's move: +₹446.13 (+1.28%) vs Monday's ₹34,889.49 close — the book rose
today as ADANIPOWER (+2.68%) and ADANIGREEN (+3.54%) led the Adani-group
rebound described above. Buy-and-hold reconstructed from the original Day-0
quantities (IRFC 30, TMPV 5, ADANIGREEN 6, ADANIPOWER 95, GOLDBEES 35, 0 cash)
marked at today's same closes.

**Reading it:** today is the mirror image of yesterday. The cumulative
actual-vs-buy-hold gap **narrowed sharply, from +₹289.44 to +₹59.02** — a
same-day swing of −₹230.42 — because buy-and-hold's untrimmed 95-share
ADANIPOWER stake captured more of today's +2.68% rebound in rupee terms than
the traded book's trimmed 55-share stake did. This is exactly the expected
cost of a de-risking trade on a recovery day for the name that was cut, and
it's worth being precise about what it does and doesn't undo: the trim still
finishes these two sessions combined (Monday's crash + today's rebound) net
ahead of doing nothing, by ₹59.02 — smaller than yesterday's edge, but not
erased. Against the Nifty-tracking benchmark, the book clearly outperformed
today (+1.28% vs the index's roughly flat −0.10%/cumulative −0.81%), since
this book's concentrated Adani exposure caught more of today's rebound than
the broad index did — the same concentration that hurt on Monday helped
today, underscoring that this book's risk (and reward) is still dominated by
two related names, trim or no trim.

### Manali's paper book — mark-to-market

| | Value | Since Day 0 (₹4,18,123.80) |
|---|---|---|
| **Actual (traded) book** | **₹4,10,070.37** | **−₹8,053.43 (−1.93%)** |
| Buy-and-hold benchmark (no trades) | ₹4,10,182.09 | −₹7,941.71 (−1.90%) |
| Nifty 50-tracking benchmark | ₹4,14,741.16 | −₹3,382.64 (−0.81%) |

Day's move: −₹2,987.23 (−0.72%) vs Monday's ₹4,13,057.60 close — unlike
Sujal's book, this one fell today despite the Adani rebound, because
ASIANPAINT (−3.42%, ~8.1% of book value) and TCS (−1.26%, ~11.0% of book
value) — the book's two largest single-name weights — outweighed a modest
ADANIPOWER (+2.68%) bounce at only ~1.7% weight here. ABCAPITAL (−4.31%) and
BAJAJHFL (−1.38%) added further drag; no held symbol offset it materially.
Buy-and-hold reconstructed from the original Day-0 quantities (today's 31
holdings plus BCG 230 reinstated, GOLDBEES 135, ADANIPOWER 53, BAJFINANCE 20,
HAL 5, NIFTYBEES 90 — i.e. Day 1's trades reversed) marked at today's same
closes, including BCG's ₹9.01 close.

**Reading it:** the same Adani-rebound mechanism that helped Sujal's book
shows up here too, just in reverse and at much smaller scale — the cumulative
actual-vs-buy-hold gap **widened slightly, from −₹55.94 to −₹111.72**,
because buy-and-hold's bigger 53-share ADANIPOWER stake captured more of
today's rebound than the traded book's smaller 35-share stake, the same
mechanic that worked in this book's favor on Monday's crash, now costing a
small amount on the recovery leg. At ~0.027% of book value the gap remains
essentially noise-level either way — six sessions of evidence continue to
show this book's day-to-day return is driven by its 31-name diversification
(today, ASIANPAINT and TCS) far more than by the Day 1 trade thesis itself.
Against the Nifty-tracking benchmark, the book underperforms both today
(−0.72% vs the index's −0.10%) and cumulatively (−1.93% vs −0.81%) — this
book's holdings (heavier in ASIANPAINT, TCS, financials) simply didn't share
in the index's relative resilience today, which itself was propped up almost
entirely by the Adani rebound this book barely holds. **New watch item:**
AWL's Delhi HC hearing on the FSSAI Fortune-brand labeling show-cause notice
(next hearing 5 Nov) — logged for tomorrow's research pass, not actionable
today since the market read it as immaterial (stock closed up).

**Decisions today — Sujal:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — today's
  Adani-group rebound (+2.68% ADANIPOWER, +3.54% ADANIGREEN) is the expected
  give-back on the trim's protective bet, not a reason to trade further; the
  book stays net ahead of buy-and-hold across the two-session crash-and-
  rebound pair.

**Decisions today — Manali:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: everything (all 31 remaining holdings) — today's small decline was
  driven by diversified factors (ASIANPAINT, TCS, ABCAPITAL) unrelated to any
  open Day 1 call, not a reversal of any held thesis. AWL's new FSSAI Delhi
  HC hearing is logged as a fresh watch item, not an action trigger — the
  market itself priced it as immaterial today.

## Day 7 — Tuesday, 1 Sep 2026 (morning check-in)

**Self-check:** today's real date is Tuesday 1 Sep 2026 — inside the 24 Aug–4
Sep window, a weekday. Confirmed via the shell `date` command that 1 Sep 2026
is a Tuesday. Re-confirmed via web search that there is no NSE/BSE trading
holiday in this stretch (next holiday remains Ganesh Chaturthi, 14 Sep 2026;
September's only other closures are weekends). Proceeding. Reference prices
throughout use Monday 31 Aug's close (already researched and logged in that
evening's entry); actual fills at today's open will differ.

**Macro backdrop researched this morning:** Risk-off leaning open indicated.
Monday 31 Aug's US close was negative (S&P 500 −0.33% to 7,686; Dow −0.70% to
53,186; Nasdaq −0.12% to 26,371) on fresh US strikes on Iranian targets near
the Strait of Hormuz plus hawkish Fed commentary from Chair Kevin Warsh —
market-implied odds of a September Fed hike rose to ~57% (from ~40% a week
earlier) on a run of hawkish remarks and firming yields (US 10Y ~4.7%, up
three straight sessions). Brent crude jumped ~3.2% to ~$90.91/bbl Monday on
the Iran strikes; gold pulled back overnight (~$4,530→$4,457, ~−1.3%); silver
last confirmed ~$67.11 Monday, +1.09% that session, no fresh overnight move
confirmed. GIFT Nifty signals were mixed but net cautious-to-mildly-negative
(one read −51 to −105 points on "risk-off" mood, a second read only
marginally positive); India VIX had jumped ~4.8% in Monday's session.
Specifically checked for follow-up on Monday's Adani-group MSCI-rebalancing
selloff (~₹1.4 lakh crore market-cap loss as the scheduled quarterly MSCI
reshuffle collided with NSE's newer Closing Auction Session, driving ~40x
normal closing-auction turnover): no adverse follow-up, regulatory statement,
or fresh company-specific news found; one analyst (Geojit's Anand James) was
quoted characterizing it as a flows-driven, expected, stock-specific event,
not systemic — consistent with Monday evening's read that this was
index-mechanics, not a fundamentals deterioration. No confirmed rebound data
for today's open was found in this pre-market pass (research agents can't see
live intraday prints) — worth confirming at the actual open, but nothing
found changes the standing read.

**Symbol-level research (all 6 Sujal + all 31 Manali holdings checked for
anything new since Monday's close, split across two parallel research
passes):** no genuinely new, dated company-specific catalyst was found for
any of the 32 unique symbols held across both books. Specifically:
- **IRFC**: no update on the ₹549.32cr GST show-case notice since the 24 Aug
  filing — still "evaluating notice, filing reply," remains a watch item only.
- **ADANIGREEN / ADANIPOWER**: no fresh company-specific news; only pre-existing
  calendar items (ADANIGREEN EGM 3 Sep). Adani-group MSCI-selloff follow-up
  covered under macro above.
- **TMPV**: a previously-announced (21 Aug) price hike of up to ₹25,000 takes
  effect today — scheduled, not a fresh catalyst.
- **GROWW** (Manali): no second wave of block-deal selling confirmed since the
  27 Aug Ribbit Capital/Cayman GW Holdings disclosure (~₹979cr/2.1% stake);
  watch item continues, not escalating.
- **MAZDOCK** (Manali): Project 75(I) CCS sign-off still pending; no news.
- **NEWGEN** (Manali): CEO transition (Jeet's resignation effective 31 Aug,
  Nandwani already CEO since 1 Aug) is now fully closed — no further
  development found, no longer an open item.
- **AWL** (Manali): FSSAI watch item unchanged, nothing new since the 7 Aug
  clarification.
- **HINDCOPPER, TCS, HDFCBANK, HAL, L&T, BEL** and every other symbol in both
  books: no fresh, dated news found in this morning's sweep, including
  re-checked stale-looking headlines (an HDFCBANK chairman-resignation item
  is from 18 Mar 2026, an L&T "ultra-mega" ADNOC order is from 4 Aug 2026, an
  HAL Tejas-Mk2 CCS-approval headline is from Sep 2022 — all confirmed old,
  not new triggers).

**Decision:** no confirmed, material new information changes any open thesis
in either book today. The macro backdrop (Iran-strait oil spike, hawkish Fed,
firming yields, cautious GIFT Nifty) is a risk-off condition affecting the
whole index, not a single-name signal calling for a trade — and Monday's
Adani-group selloff, while showing no adverse follow-up, also has no
confirmed rebound data available pre-open to act on. GROWW's watch item
continues unresolved but not worsening; MAZDOCK's CCS sign-off remains
pending; NEWGEN's CEO transition is now a closed, non-recurring item; AWL's
FSSAI question remains open, not escalating. Both books' Day 1 trades remain
the open calls under test — today adds a seventh data point, not a reason for
turnover.

**Decisions today — Sujal:**
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — no new
  research finding changes any position; today's backdrop is a market-wide
  risk-off macro condition (oil, Fed, yields), not a single-name catalyst, and
  Monday's Adani-group MSCI-selloff shows no adverse follow-up but also no
  confirmed rebound data pre-open to act on yet.

**Decisions today — Manali:**
- HOLD: everything (all 31 remaining holdings) — no new research finding
  changes any position. GROWW's block-deal aftermath continues as an open,
  non-escalating watch item; MAZDOCK's CCS sign-off remains pending; NEWGEN's
  CEO transition is now fully closed; AWL's FSSAI question remains open, not
  escalating.

## Day 6 — Monday, 31 Aug 2026 (evening check-in)

**Self-check:** today is Monday 31 Aug 2026 — inside the 24 Aug–4 Sep window, a
weekday. Re-confirmed via web search (Zerodha's 2026 holiday calendar) that
there is no NSE/BSE trading holiday between 24 Aug and 4 Sep 2026 (next
holiday is Ganesh Chaturthi, 14 Sep) — already established this morning,
reconfirmed here. Proceeding with the evening mark-to-market.

**Closing prices researched this evening** (NSE, 31 Aug 2026 close; two
parallel research passes covering Sujal's 6 + part of Manali's book and the
rest of Manali's book respectively, each cross-checking stockanalysis.com
against a second source — Groww, Kotak Neo, Business Standard, or a direct
page fetch — per symbol; two follow-up searches run directly this evening to
resolve a conflicting ADANIPOWER print and confirm GOLDBEES):

| Symbol | Close (₹) | Day chg | Confidence | Note |
|---|---|---|---|---|
| Nifty 50 | 24,080.40 | −0.39% (−95.25 pts) | High (2-source) | Sensex −0.40% to 76,957.27. Mildly risk-off session — Metal, Realty, Media and IT sectors underperformed, Auto and Private Banks relative outperformers, broader market mixed (Nifty MidCap +0.24%, SmallCap −0.74%). Stated macro driver: rising crude (Brent ~$89–90) and bond yields on escalating US–Iran tension, raising Sept Fed rate-hike odds (also the driver behind gold/silver's fall today). The day's single biggest story: per Bloomberg, the **Adani group lost ~₹1.4 lakh crore (~$15B) in market value — the largest such drop in ~21 months** — as a scheduled **MSCI India index rebalancing drove unusually volatile swings in the NSE's closing auction**; all 9 listed Adani firms closed lower, three by more than 6% each (Adani Enterprises −9.8%, Adani Energy Solutions >10%). This is a market-structure/index-mechanics event, not a fundamentals deterioration at either Adani holding held in these books. |
| IRFC | 83.34 | −0.67% (−0.56) | Medium (single genuine same-day source, internally consistent with the day's ₹82.90–84.15 range) | No dated catalyst found; GST show-cause notice remains the only open item. |
| TMPV | 308.85 | −3.30% (−10.55) | High (2-source agree exactly) | No single dated catalyst found; continues a multi-week slide (a fresh 52-week low this week, −10.4% over 7 days) since its 2025 demerger — not linked to today specifically. |
| ADANIGREEN | 1,214.90 | −7.33% (−96.10) | High (2-source agree exactly) | Group-wide Adani/MSCI-rebalancing closing-auction event described above — not company-specific. |
| ADANIPOWER | 198.00 | −6.88% (−14.63) | Medium→High (an earlier intraday print showed ₹208.10/−2.07%, pre-auction; the ₹198.00/−6.88% figure is the settled close, corroborated by a second independent web search this evening and consistent with Bloomberg's report that three Adani firms fell >6% each) | Same group-wide Adani/MSCI closing-auction event as ADANIGREEN. |
| GOLDBEES | 127.32 | −2.70% (−3.53) | High (confirmed via a direct Groww page fetch this evening in addition to stockanalysis.com — both agree exactly; prev close ₹130.85 matches Friday's logged figure) | Gold fell a 3rd straight session on rising Sept Fed rate-hike odds. |
| NIFTYBEES | 274.87 | −0.27% (−0.75) | Medium-High (single direct source, cross-checks well against Nifty's own −0.39% move) | Tracks index. |
| RELIANCE | 1,277.00 | −0.78% (−10.00) | High (2-source) | No dated catalyst; below notable-move threshold. |
| LT | 4,044.90 | −0.02% (−0.90) | Medium (single source, other hits stale) | Essentially flat. |
| ASIANPAINT | 2,653.60 | +1.72% (+44.90) | High (2-source) | No dated catalyst found. |
| HDFCBANK | 709.00 | −1.57% (−11.30) | High (multiple sources converge) | No dated catalyst found; move runs counter to Private Banks being a same-day outperforming sector, so likely stock-specific, but no explaining article surfaced. Post-split price level (10:1 cumulative split ~Aug 2025) confirmed legitimate, not a data error. |
| HAL | 4,801.60 | −1.22% (−59.50) | High (2-source) | No dated catalyst; below notable-move threshold. |
| GROWW | 192.06 | +0.31% (+0.60) | High (2-source) | No new block-deal-selling news found; continues the stabilized read logged this morning. |
| TMCV | 471.10 | +1.03% (+4.80) | Medium (single source, other hits stale) | No dated catalyst found. |
| CLEAN | 822.85 | −1.63% (−13.60) | High (2-source) | No dated catalyst found. |
| MAZDOCK | 2,480.00 | −2.94% (−75.00) | Medium (consistent with a same-day intraday snapshot; no second full-close source found) | No dated catalyst; Project 75(I) CCS sign-off still pending. |
| BEL | 414.45 | +0.62% (+2.55) | High (2-source) | No dated catalyst found. |
| DEEPAKNTR | 1,749.40 | −0.77% (−13.50) | High (2-source) | No dated catalyst found. |
| BAJFINANCE | 1,057.00 | −2.12% (−22.90) | High (2-source) | No dated catalyst; financials broadly mixed in a soft market. |
| BAJAJHFL | 84.02 | −1.15% (−0.98) | High (2-source) | No dated catalyst found. |
| DSSL | 1,041.30 | −2.67% (−28.60) | High (2-source) | No same-day dated catalyst (SOC 2 certification 19 Aug and Q1 earnings call 14 Aug are stale); consistent with general IT/small-cap softness today. |
| BERGEPAINT | 497.75 | +0.69% (+3.40) | High (2-source) | No dated catalyst found. |
| TCS | 2,399.30 | +2.45% (+57.30) | High (2-source) | Notable outperformance against a weak Nifty IT sector; reporting around a Porsche IT-consulting-arm (MHP, ~€320m) acquisition and continued AI-deal news flow is the best-supported context found but wasn't pinned to a same-day (31 Aug) press release — treated as plausible context, not a confirmed same-day trigger. |
| HINDCOPPER | 525.35 | −1.54% (−8.20) | High (2-source) | Broad metals/mining-sector weakness today; no company-specific dated news found. |
| NEWGEN | 528.85 | −6.74% (−38.25) | High (2-source) | CEO Virender Jeet's resignation reaches its formal effective date (last working day) today per regulatory filing — flagged this morning as old news reaching its known date, not a new trigger — compounded by broad IT-sector softness; a genuine, if largely anticipated, dated catalyst. |
| SRF | 2,560.40 | −1.14% (−29.50) | High (2-source) | No dated catalyst found. |
| ABCAPITAL | 409.40 | +0.95% (+3.85) | High (2-source) | No dated catalyst found. |
| AWL | 192.55 | −1.90% (−3.72) | High (2-source) | No dated catalyst found. |
| NTPC | 327.40 | −0.80% (−2.65) | High (2-source) | No dated catalyst found. |
| ETERNAL | 328.10 | +0.03% (+0.10) | Medium (two direct price sources agree closely — 328.10 vs 328.00 — but a same-day market-wrap live-blog described it as a "top loser," likely an intraday-snapshot artifact rather than the final close) | No dated catalyst found; the discrepancy is flagged but the net move is immaterial either way. |
| NFL | 70.37 | −1.01% (−0.72) | High (2-source) | No dated catalyst found. |
| ITBEES | 34.32 | −1.10% (−0.38) | High (2-source) | Tracks Nifty IT, a market laggard today. |
| SILVERBEES | 223.22 | −3.12% (−7.20) | High (2-source, plus multiple news roundups) | Silver sold off with gold on rising Sept Fed rate-hike odds; silver ETFs broadly fell up to ~4% market-wide today. |
| BCG | 9.04 | −0.11% (−0.01) | High (2-source) | For buy-and-hold benchmark only — not held after Day 1's exit. |

**Data-quality caveats:** two figures needed extra verification tonight and
were resolved before use: (1) **ADANIPOWER** — an initial pass surfaced a
conflicting intraday print (₹208.10, −2.07%, pre-auction) alongside the
settled close (₹198.00, −6.88%); a direct follow-up search this evening
confirmed ₹198.00 as the closing price, consistent with Bloomberg's
same-day report that three Adani group firms fell more than 6% each in the
MSCI-rebalancing-driven closing auction — used as the mark. (2)
**GOLDBEES** — confirmed via a direct Groww page fetch this evening
(matching stockanalysis.com exactly, and consistent with Friday's logged
₹130.85 previous close), upgraded from the research pass's single-source
Low–Medium read to High. **ETERNAL**'s close is solid (two sources within a
paisa) but one live market-wrap piece's "top loser" framing doesn't match
the ~flat final print — flagged, not blocking, and immaterial to either
book's total. No price tonight is certified against NSE's own bhavcopy.

### Sujal's paper book — mark-to-market

| | Value | Since Day 0 (₹36,182.70) |
|---|---|---|
| **Actual (traded) book** | **₹34,889.49** | **−₹1,293.21 (−3.57%)** |
| Buy-and-hold benchmark (no trades) | ₹34,600.05 | −₹1,582.65 (−4.37%) |
| Nifty 50-tracking benchmark | ₹35,926.68 | −₹256.02 (−0.71%) |

Day's move: −₹1,548.40 (−4.25%) vs Friday's ₹36,437.89 close (no Saturday/
Sunday trading) — by far the book's worst single-session move in six
sessions, driven almost entirely by the Adani-group selloff: ADANIGREEN
−7.33% and ADANIPOWER −6.88%, both caught in the MSCI-rebalancing-driven
closing-auction volatility described above, plus GOLDBEES −2.70% falling
with gold. Buy-and-hold reconstructed from the original Day-0 quantities
(IRFC 30, TMPV 5, ADANIGREEN 6, ADANIPOWER 95, GOLDBEES 35, 0 cash) marked
at today's same closes.

**Reading it:** this is the session the Day 1 de-risking trim was insuring
against, and for the first time in six sessions it clearly paid off. The
cumulative actual-vs-buy-hold gap **flipped from −₹321.71 to +₹289.44** — a
same-day swing of +₹611.15 — because buy-and-hold's untrimmed 95-share
ADANIPOWER stake absorbed nearly twice the rupee loss that the traded
book's trimmed 55-share stake did on today's −6.88% move. The actual book
is now genuinely *ahead* of doing nothing since Day 0, reversing a pattern
that had held (with one small exception on Day 5) for five straight
sessions. It's worth being precise about what today validates and what it
doesn't: the trigger was index-mechanics/MSCI-rebalancing volatility in the
NSE closing auction, not a fundamentals deterioration at either Adani
holding — so this isn't proof the "Adani Group is overvalued/risky"
thesis was right, only proof that *reducing single-stock concentration
before a violent one-day move, for whatever reason, reduces the damage
when that move happens*. That is exactly what the trim was built to do.
Against the Nifty-tracking benchmark (−0.71%), the traded book now trails
for the first time this week (−3.57% vs −0.71%) — unsurprising, since
today's damage was concentrated in two names this book is overweight and
the broad index isn't. One very bad day for a concentrated position is not
by itself proof the multi-day pattern before it (four straight sessions of
buy-and-hold outperforming) was wrong either — four sessions of small cost
plus one session of large benefit is a very different distribution than
either extreme alone, and that's the actual, honest read six sessions in.

### Manali's paper book — mark-to-market

| | Value | Since Day 0 (₹4,18,123.80) |
|---|---|---|
| **Actual (traded) book** | **₹4,13,057.60** | **−₹5,066.20 (−1.21%)** |
| Buy-and-hold benchmark (no trades) | ₹4,13,113.54 | −₹5,010.26 (−1.20%) |
| Nifty 50-tracking benchmark | ₹4,15,165.28 | −₹2,958.52 (−0.71%) |

Day's move: −₹2,665.57 (−0.64%) vs Friday's ₹4,15,723.17 close — the book's
worst single-day move in six sessions, on the same Adani-group selloff
(ADANIPOWER −6.88%, a much smaller 35-share/~1.7% weight here than in
Sujal's book) plus SILVERBEES −3.12% and NEWGEN −6.74% (CEO transition
reaching its formal effective date) adding drag; TCS +2.45% was the lone
large offset. Buy-and-hold reconstructed from the original Day-0 quantities
(today's 31 holdings plus BCG 230 reinstated, GOLDBEES 135, ADANIPOWER 53,
BAJFINANCE 20, HAL 5, NIFTYBEES 90 — i.e. Day 1's trades reversed) marked
at today's same closes, including BCG's ₹9.04 close.

**Reading it:** the same mechanism that flipped Sujal's book today shows up
here too, just diluted across 31 other holdings. The cumulative
actual-vs-buy-hold gap **narrowed sharply, from −₹303.43 to −₹55.94** — the
largest one-day improvement of the week — because buy-and-hold's larger
53-share ADANIPOWER stake (vs the traded book's 35) took more of today's
−6.88% hit, and its reinstated 230-share BCG position added a further tiny
drag (BCG itself was flat, −0.11%, so this was a minor factor). At −0.014%
of book value, the remaining gap is now close to noise-level — six
sessions in, this book's BAJFINANCE/HAL sizing adds and ADANIPOWER/GOLDBEES
trims have gone from a small, consistent cost to essentially breakeven
against doing nothing, with today's Adani-driven session being the clearest
single piece of evidence yet that the trims add value on bad days for the
stock, not just cost on ordinary ones. As with Sujal's book, this book's
Nifty-tracking benchmark (−0.71%) is now beaten by both the actual book
(−1.21%, worse) and — for the first time — is worse than both real
readings' cumulative position, since this session's damage (Adani, silver,
NEWGEN) hit assets this book holds and the index doesn't weight the same
way. GROWW's watch item continues unresolved but not worsening; MAZDOCK's
CCS sign-off remains pending; NEWGEN's CEO transition is now a closed,
non-recurring item (its formal effective date has passed).

**Decisions today — Sujal:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — this
  evening's run only marks positions to today's close. Today's Adani-group
  selloff (MSCI-rebalancing-driven closing-auction volatility, not a
  fundamentals event) is exactly the scenario the Day 1 trim was designed
  to cushion, and it did — no reason to trade further on a single index-
  mechanics event.

**Decisions today — Manali:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: everything (all 31 remaining holdings) — this evening's run only
  marks positions to today's close. Same Adani-selloff read as Sujal's
  book, at a much smaller relative weight; GROWW's watch item continues
  unresolved but not worsening; MAZDOCK's CCS sign-off remains pending;
  NEWGEN's CEO transition has now reached its already-known effective date
  and is no longer an open item.

## Day 6 — Monday, 31 Aug 2026 (morning check-in)

**Self-check:** today's real date is Monday 31 Aug 2026 — inside the 24 Aug–4
Sep window, a weekday. Verified the weekday independently via both the shell
`date` command and Python's `datetime` (both confirm Monday), since an initial
web-search summary incorrectly claimed 31 Aug 2026 falls on a Sunday — that
claim is wrong and was discarded rather than trusted. Confirmed via Zerodha's
2026 holiday calendar that there is no NSE/BSE trading holiday between 24
Aug–4 Sep 2026 (the next holiday is Ganesh Chaturthi, 14 Sep). Proceeding.
Reference prices throughout use Friday 28 Aug's close (already researched and
logged in that evening's entry); actual fills at today's open will differ.
Weekend (29–30 Aug) required no entries — outside the trading calendar.

**Macro backdrop researched this morning:** Cautious, flat-to-slightly-negative
open indicated — pre-open commentary flags crude still above $91/bbl, rising
global bond yields, and ongoing West Asia tension as headwinds, with Nifty
consolidating near its 24,200 pivot (resistance 24,250–24,300 on call writing,
support 24,150–24,200) and only a close above 24,380 seen as a real shift to
the upside. Friday's US close was mildly negative on the day but a positive
week overall — S&P 500 −0.2% to 7,711.76, Dow flat (−0.02%) to 53,559.99,
Nasdaq −0.5% to 26,402.42 — as Fed Chair Kevin Warsh's first Jackson Hole
keynote was read as mildly hawkish (flagging that recent inflation prints
don't yet show underlying trends meaningfully improving, without giving
forward policy guidance). Gold sits flat near $4,600/oz (a marginal weekly
decline after three straight up weeks); silver holds near $69, eyeing a
possible break above $72; crude (Brent ~$91, WTI ~$85) ticked up from
two-week lows on West Asia developments (Qatar–Iran talks on mine-clearing to
reopen Strait of Hormuz tanker routes) — no fresh spike, no confirmed
reversal in gold/silver's elevated levels either.

**Symbol-level research (all 6 Sujal + all 31 Manali holdings checked for
anything new since Friday's close):**
- **IRFC**: no update found since the 24 Aug GST show-cause notice (₹549.32cr,
  company's "no immediate impact" position unchanged) — remains a watch item
  only.
- **ADANIGREEN / ADANIPOWER**: no fresh, dated company-specific news found for
  the weekend or this morning; nothing changing the existing read.
- **GROWW** (Manali): no second wave of block-deal selling confirmed since
  Friday's renewed −2.73% weakness — the only items found dated this weekend
  are routine (392,613 ESOP options granted 28 Aug under the existing 2024
  scheme) or mildly positive (Groww/Billionbrains named among 10 Indian stocks
  in FTSE's September 2026 index review, not yet effective). Watch item
  continues, not escalating, not closing.
- **MAZDOCK** (Manali): Project 75(I) still awaiting final CCS sign-off;
  reporting continues to target contract conclusion by September — unchanged,
  still unconfirmed, still not actionable.
- **NEWGEN** (Manali): CEO Virender Jeet's resignation takes effect today
  (close of business, 31 Aug) — but this was announced 9 June 2026, and
  successor Tarun Nandwani has already been CEO since 1 Aug. Old, fully-priced
  news reaching its formal effective date, not a new trigger.
- **TCS**: no company-specific news found since Friday; Friday's rally was
  the sector-wide Nifty IT/Nvidia move already logged, not company-specific.
- **HINDCOPPER**: OFS remains fully settled; no new news.
- Every other symbol (TMPV, TMCV, NIFTYBEES, GOLDBEES, RELIANCE, LT,
  ASIANPAINT, HDFCBANK, HAL, CLEAN, BEL, DEEPAKNTR, BAJFINANCE, BAJAJHFL,
  DSSL, BERGEPAINT, SRF, ABCAPITAL, AWL, NTPC, ETERNAL, NFL, ITBEES,
  SILVERBEES): no fresh, dated news found since Friday's close in this
  morning's research, including a general "stocks to watch Monday" sweep that
  surfaced nothing involving any held name.

**Decision:** no confirmed, material new information changes any open thesis
in either book today. The macro backdrop (cautious/flat GIFT Nifty, a mildly
hawkish Jackson Hole read, firm-but-not-spiking crude) gives no directional
trigger either. GROWW's watch item continues unresolved but not worsening;
MAZDOCK's CCS sign-off remains pending; NEWGEN's CEO change is a
long-announced, already-effective transition, not new information. Both
books' Day 1 trades remain the open calls under test — today adds a sixth
data point, not a reason for turnover.

**Decisions today — Sujal:**
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — no new
  research finding changes any position; IRFC's GST notice remains a watch
  item only.

**Decisions today — Manali:**
- HOLD: everything (all 31 remaining holdings) — no new research finding
  changes any position. GROWW's block-deal aftermath continues as an open,
  non-escalating watch item; MAZDOCK's CCS sign-off remains pending;
  NEWGEN's CEO transition is old news reaching its already-known effective
  date, not an action trigger.

## Day 5 — Friday, 28 Aug 2026 (evening check-in)

**Self-check:** today is Friday 28 Aug 2026 — inside the 24 Aug–4 Sep window, a
weekday, and already confirmed this morning (via 5paisa pre-open coverage and
market-holiday pieces) as **not** an NSE/BSE trading holiday. Proceeding with
the evening mark-to-market.

**Closing prices researched this evening** (NSE, 28 Aug 2026 close; sources:
Tickertape, Groww, stockanalysis.com as primary, cross-checked against a
second source per symbol; index/backdrop cross-checked against Business
Standard's live market-wrap and BusinessToday's Nifty-IT-rally coverage):

| Symbol | Close (₹) | Day chg | Confidence | Note |
|---|---|---|---|---|
| Nifty 50 | 24,175.65 | +0.35% (+84.80 pts) | High (3-source) | Sensex +0.43% to 77,264.51; snapped a two-session losing streak. Breadth positive (2,385 advances vs 1,932 declines on BSE). Driver: Nifty IT surged +3.51% on Nvidia's Q2 beat reigniting AI-capex optimism (Coforge +5.93%, LTIMindtree +4.73%, TCS +4.16%, Persistent +3.73%, Tech Mahindra +3.12%, Infosys +2.9%); pharma and metals also advanced. FMCG, consumer durables, and some heavyweight banks lagged. Firm crude and caution ahead of Fed Chair Kevin Warsh's Jackson Hole address capped further gains. |
| IRFC | 83.90 | −0.89% | High (2-source) | No new dated catalyst; GST show-cause notice remains the only open item |
| TMPV | 319.40 | +1.08% | High (2-source) | No dated catalyst found |
| TMCV | 466.30 | −1.44% | High (2-source) | No dated catalyst found |
| ADANIGREEN | 1,311.00 | −1.32% | High (2-source) | No fresh company-specific news; giving back some of the week's gains |
| ADANIPOWER | 212.63 | −1.10% | High (2-source) | No fresh catalyst; first down session after three straight up days |
| GOLDBEES | 130.85 | +0.62% | High (2-source) | Tracks gold, still elevated |
| NIFTYBEES | 275.62 | −0.04% | High (2-source) | Roughly flat despite Nifty's +0.35% — tracking basis/timing noise |
| RELIANCE | 1,287.00 | +0.37% | High (2-source) | No dated catalyst |
| LT | 4,045.80 | +0.47% | High (2-source) | No dated catalyst |
| ASIANPAINT | 2,608.70 | −0.85% | High (2-source) | No dated catalyst |
| HDFCBANK | 720.30 | +1.31% | High (2-source) | No dated catalyst |
| HAL | 4,861.10 | −0.77% | High (2-source) | No dated catalyst |
| GROWW | 191.46 | −2.73% | High (2-source) | Continuation of the known Ribbit Capital/Cayman GW Holdings block-deal overhang (~₹979cr sale at ₹196.06, disclosed 27 Aug) — not a new event, but the selling pressure has not fully stabilized as Wednesday/Thursday's price action suggested; watch item reopened, not closed |
| CLEAN | 836.45 | +0.77% | High (2-source) | No dated catalyst |
| MAZDOCK | 2,555.00 | −1.28% | High (2-source) | Project 75(I) CCS sign-off still pending; no news today |
| BEL | 411.90 | +0.22% | High (2-source) | No dated catalyst |
| DEEPAKNTR | 1,762.90 | +0.58% | High (2-source) | No dated catalyst |
| BAJFINANCE | 1,079.90 | −0.29% | High (2-source) | No dated catalyst |
| BAJAJHFL | 85.00 | −0.34% | High (2-source) | No dated catalyst |
| DSSL | 1,069.90 | −0.75% | High (2-source) | No dated catalyst |
| BERGEPAINT | 494.35 | −1.33% | High (2-source) | No dated catalyst |
| TCS | 2,342.00 | +4.16% | High (2-source) | Nifty IT rally (Nvidia Q2 beat/AI-capex optimism) — sector-wide move, not a TCS-specific event, but the book's best single-day move this week |
| HINDCOPPER | 533.55 | −0.51% | High (2-source) | OFS fully settled; no longer an open item |
| NEWGEN | 567.10 | +8.43% | High (2-source) | Jefferies raised target to ₹630 citing license-revenue growth and AI-driven productivity gains, riding the same-day IT/AI rally — a genuine, dated, company-specific catalyst |
| SRF | 2,589.90 | −0.58% | High (2-source) | No dated catalyst |
| ABCAPITAL | 405.55 | −1.09% | High (2-source) | No dated catalyst |
| AWL | 196.27 | −1.74% | High (3-source) | No dated catalyst |
| NTPC | 330.05 | −0.26% | High (2-source) | No dated catalyst |
| ETERNAL | 328.00 | −0.15% | High (2-source) | No dated catalyst |
| NFL | 71.09 | −0.38% | High (2-source) | No dated catalyst |
| ITBEES | 34.70 | +2.94% | High (2-source) | Tracks the Nifty IT rally |
| SILVERBEES | 230.31 | ~+1.9% | Medium (2-source, ~0.05% spread on the exact print — both agree on direction/magnitude) | Tracks silver, still elevated |
| BCG | 9.05 | +0.22% | High (2-source) | For buy-and-hold benchmark only — not held after Day 1's exit; traded normally |

**Data-quality caveats:** all 33 symbols returned genuine same-day (28 Aug)
data — no stale fallback needed this evening. Only SILVERBEES carries Medium
confidence, from a ~0.05% spread between two sources on the exact closing
print (230.31 vs 230.42); both agree on direction and rough magnitude, so the
₹230.31 print (stockanalysis.com) is used below without materially affecting
either book's total. TCS (+4.16%) and NEWGEN (+8.43%) crossed the
notable-move threshold and both have genuine, dated, sector- or
company-specific catalysts (the Nifty IT/Nvidia rally, and Jefferies' target
raise on NEWGEN respectively) — not unexplained moves.

### Sujal's paper book — mark-to-market

| | Value | Since Day 0 (₹36,182.70) |
|---|---|---|
| **Actual (traded) book** | **₹36,437.89** | **+₹255.19 (+0.71%)** |
| Buy-and-hold benchmark (no trades) | ₹36,759.60 | +₹576.90 (+1.59%) |
| Nifty 50-tracking benchmark | ₹36,068.79 | −₹113.91 (−0.31%) |

Day's move: −₹269.49 (−0.73%) vs yesterday's ₹36,707.38 close — the book fell
today even as the Nifty rose +0.35%, because Nifty's rally was concentrated in
IT (a sector this book doesn't hold directly) while ADANIPOWER (−1.10%) and
ADANIGREEN (−1.32%) gave back some of the week's gains. Buy-and-hold
reconstructed from the original Day-0 quantities (IRFC 30, TMPV 5, ADANIGREEN
6, ADANIPOWER 95, GOLDBEES 35, 0 cash) marked at today's same closes.

**Reading it:** for the first time in five sessions, the de-risking trim
*helped* rather than hurt on a down day for ADANIPOWER — the cumulative
actual-vs-buy-hold gap **narrowed** from Day 4's −₹443.92 to today's
**−₹321.71**, because buy-and-hold's larger 95-share ADANIPOWER stake fell by
more in rupee terms than the traded book's trimmed 55-share stake. This is
exactly the scenario the trim was insuring against, just on a much smaller
scale than a genuine tail event — a single ordinary down day, not a crash.
It's a useful data point but doesn't yet flip the four-session pattern: the
traded book (+0.71% since Day 0) still trails buy-and-hold (+1.59%) by close
to a full percentage point, so today's move only slowed the drag, it didn't
reverse the cumulative story. Against the Nifty-tracking benchmark
(−0.31%), the traded book continues to look better than the broad index,
same as every prior session — this book's ADANIPOWER/ADANIGREEN-heavy
composition has simply outrun the index all week, a separate effect from the
trim decision itself.

### Manali's paper book — mark-to-market

| | Value | Since Day 0 (₹4,18,123.80) |
|---|---|---|
| **Actual (traded) book** | **₹4,15,723.17** | **−₹2,400.63 (−0.57%)** |
| Buy-and-hold benchmark (no trades) | ₹4,16,026.60 | −₹2,097.20 (−0.50%) |
| Nifty 50-tracking benchmark | ₹4,16,807.46 | −₹1,316.34 (−0.31%) |

Day's move: +₹809.68 (+0.20%) vs yesterday's ₹4,14,913.49 close — a modest gain
that undersells how strong the day was for one holding: TCS (+4.16%) was the
book's standout on the Nifty IT/Nvidia rally, but the gain was mostly offset
by GROWW (−2.73%, continuing block-deal pressure), ADANIGREEN-adjacent
softness elsewhere, AWL (−1.74%), MAZDOCK (−1.28%) and BERGEPAINT (−1.33%).
NEWGEN's +8.43% (Jefferies target raise) added a small but real boost given
its modest 10-share weight. Buy-and-hold reconstructed from the original
Day-0 quantities (today's 31 holdings plus BCG 230 reinstated, GOLDBEES 135,
ADANIPOWER 53, BAJFINANCE 20, HAL 5, NIFTYBEES 90 — i.e. Monday's trades
reversed) marked at today's same closes, including BCG's ₹9.05 close.

**Reading it:** the cumulative actual-vs-buy-hold gap widened only slightly,
from Day 4's −₹300.18 to today's **−₹303.43** — essentially flat, the
smallest incremental change of the week. TCS's rally today isn't attributable
to the trade thesis (TCS was never touched), so it doesn't validate or
challenge the BCG-exit/sizing-adds call either way; it's simply a reminder
that this book's real driver day to day is its 31-name diversification, not
any single rebalancing decision. GROWW's renewed weakness (−2.73%) reopens a
watch item that looked to be stabilizing on Wednesday/Thursday — worth
another session's confirmation before calling it resolved either way.
HINDCOPPER's OFS overhang is now fully closed out. Like Sujal's book,
Manali's traded book (−0.57% cumulative) and its buy-and-hold twin (−0.50%)
both continue to sit close to the Nifty-tracking benchmark (−0.31%) — the
five-session pattern of small, consistent index-tracking with a modest
trade-related drag remains intact.

**Decisions today — Sujal:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — this
  evening's run only marks positions to today's close; no research finding
  changes any position.

**Decisions today — Manali:** (evening check-in — no new decisions, mark-to-market only)
- HOLD: everything (all 31 remaining holdings) — this evening's run only
  marks positions to today's close. GROWW's renewed −2.73% move reopens
  (doesn't newly create) an existing watch item; TCS's +4.16% is a sector-wide
  IT rally, not a company-specific catalyst; NEWGEN's +8.43% (Jefferies
  target raise) is genuinely positive but not large enough at a 10-share
  weight to be an action trigger; MAZDOCK's CCS sign-off remains pending.

## Day 5 — Friday, 28 Aug 2026 (morning check-in)

**Self-check:** today is Friday 28 Aug 2026 — inside the 24 Aug–4 Sep window, a
weekday. Confirmed via web search (5paisa's "what to expect" pre-open piece;
market-holiday coverage confirming NSE/BSE/MCX trade normally today despite
Raksha Bandhan, pre-open from 9:00am, regular session 9:15am–3:30pm) that 28
Aug 2026 is **not** an NSE/BSE trading holiday. Proceeding. Reference prices
throughout use Thursday 27 Aug's close (already researched and logged in
yesterday evening's entry); actual fills at today's open will differ.

**Macro backdrop researched this morning:** GIFT Nifty indicates a roughly
flat-to-slightly-negative open (~8 points), a cautious continuation after
Thursday's Nifty close of 24,090.85 (−0.48%) and Sensex 76,933.59 (−0.70%) —
the second straight down session, on metals/PSU-bank/cement weakness.
Overnight, US markets closed higher across the board — S&P 500 +0.42% to
7,673.04, Dow +0.83% to 53,195.36, Nasdaq +0.39% to 26,168.46 — as investors
digested hot US inflation data and continued to price in Wednesday's Nvidia
beat (Q2 FY27 revenue $96.2bn vs $92.4bn consensus, Q3 guidance $108bn vs
$104.2bn), a supportive global AI-capex signal. Crude continues easing —
Brent ~$86.5/bbl, a fourth straight down session, no new supply-shock signal.
Gold (~$4,606/oz) and silver (~$69/oz) remain elevated and roughly flat vs
Thursday, no confirmed reversal. Pre-open commentary flags the same
tug-of-war as recent sessions: persistent FII selling pressure capping
upside, offset by robust DII inflows cushioning declines — a continuation,
not a new dynamic. Net read: firm US closes give some underlying support,
but GIFT Nifty itself points to a flat-to-cautious open, not a clear
directional cue either way.

**Symbol-level research (all 6 Sujal + all 31 Manali holdings checked for
anything new since Thursday's close):**
- **IRFC**: no update since the 24 Aug GST show-cause notice (₹549.32cr);
  company's "no immediate impact" position unchanged. Still a watch item, not
  a trigger.
- **ADANIGREEN**: no fresh, dated news since Thursday's close; investor
  roadshows (Mumbai, Chennai, London — Elara Conference, Adani Annual
  Conference) remain scheduled for late Aug/Sept, already known. The
  Bernstein/SocGen target cut is confirmed old news (dated 18 Aug).
- **ADANIPOWER**: no new material news beyond the already-known August
  investor presentation; nothing changing the de-risking read.
- **GROWW** (Manali): AGM (24 Aug) passed routine resolutions
  (financial-statement adoption, auditor appointment, MOA capital-clause
  amendment) — no surprises. No second wave of block-deal selling confirmed
  since Tuesday's Ribbit Capital sale; this watch item continues to look
  stabilized, not escalating.
- **MAZDOCK** (Manali): Project 75(I) submarine deal still awaiting final
  Cabinet Committee on Security sign-off — reports as of mid-Aug put deal
  value estimates anywhere from ~₹70,000cr to ~₹90,000cr depending on source
  (the spread itself suggests nothing is finalized yet); still unconfirmed,
  still not actionable.
- **TCS**: no company-specific catalyst. A TCS-linked staffing vendor's job
  posting drew scrutiny (dated 26–27 Aug) for appearing to require H-1B
  status specifically — this is a third-party recruitment vendor's posting
  practice, not a TCS filing, contract, or workforce decision; noted but not
  treated as a TCS-specific event.
- **HINDCOPPER**: no new news. The government's OFS (3%, green-shoe fully
  exercised to 6%, floor ₹514) fully settled T+2 as of Thursday; the
  supply/technical read from earlier this week stands confirmed and this is
  no longer an open watch item.
- Every other symbol (TMPV, TMCV, NIFTYBEES, GOLDBEES, RELIANCE, LT,
  ASIANPAINT, HDFCBANK, HAL, CLEAN, DEEPAKNTR, BAJFINANCE, BAJAJHFL, DSSL,
  BERGEPAINT, NEWGEN, SRF, ABCAPITAL, AWL, NTPC, ETERNAL, BEL, NFL, ITBEES,
  SILVERBEES): no fresh, dated news found since Thursday's close in this
  morning's research.

**Decision:** no confirmed, material new information changes any open thesis
in either book today. GIFT Nifty's flat-to-cautious indication, firm-but-old
US closes, and an unremarkable news sweep across all 37 held names (6 + 31)
give no trigger for a Buy, Sell, Trim, or Exit. Both books' Day 1 trades
(Sujal's de-risking, Manali's BCG exit and sizing adds) remain the open calls
under test — today adds a fifth data point, not a reason for turnover.

**Decisions today — Sujal:**
- HOLD: IRFC, TMPV, ADANIGREEN, ADANIPOWER, GOLDBEES, NIFTYBEES — no new
  research finding changes any position; IRFC's GST notice remains a watch
  item only.

**Decisions today — Manali:**
- HOLD: everything (all 31 remaining holdings) — no new research finding
  changes any position. MAZDOCK's Project 75(I) CCS sign-off remains
  pending and unconfirmed; GROWW's block-deal aftermath continues to look
  stabilized with no second wave; HINDCOPPER's OFS is now fully settled and
  no longer an open item; TCS's H-1B story is a third-party vendor matter,
  not company-specific.

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

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

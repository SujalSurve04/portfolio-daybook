# Portfolio Daybook — running log

This file is Sujal's portfolio's institutional memory. Each daily run (see
`PROMPT.md`) reads this whole file before writing anything, then prepends a new
entry at the marker below. **Never delete or rewrite past entries** — only append
above the marker, and note inside a new entry when an old watch item resolves.

<!-- NEW_DAY_ENTRY_INSERT_ABOVE -->

## Day 2 — Saturday, 22 Aug 2026 (automated pipeline's first live run)

**Same session, first real automated pass.** Groww API/TOTP credentials went live
today, so this is the first run through `fetch_holdings.py` for real (Day 1 was a
manual dry run). Holdings fetched match Day 1 exactly — same 5 positions, same
quantities and average prices — confirming that baseline was accurate. No new
trading session has happened since Day 1 (markets are still shut for the
weekend), so this entry uses the same Friday 21 Aug close, but with more
precisely-sourced quotes and materially new research: a specific, actionable
finding on the TMPV cost-basis question, and a legal-risk update on the Adani
Group. Portfolio: 5 holdings, ₹28,040.26 invested, **₹36,182.70 current value,
+29.04% overall**, as of Friday 21 Aug close. (Current value differs slightly
from Day 1's ₹36,220.20 — a ~0.1% variance from using more precisely
timestamped closes for IRFC and Adani Green, not a market move.)

| Symbol | Bucket | Qty | Avg | LTP (21 Aug) | P&L | Action |
|---|---|---|---|---|---|---|
| IRFC | Core | 30 | 145.62 | 86.35 | −40.7% | Watch closely |
| ADANIPOWER | Tactical | 95 | 105.47 | 205.50 | +94.8% | Trim |
| ADANIGREEN | Core | 6 | 1358.21 | 1314.00 | −3.3% | Hold |
| TMPV | Core | 5 | 640.30 | 317.90 | −50.3%* | Verify cost basis |
| GOLDBEES | Tactical | 35 | 65.75 | 131.32 | +99.7% | Trim |

**Open watch items:**

- **IRFC — ₹85 support.** Tested and held, but the picture is a bit worse than
  Day 1's framing: IRFC actually printed a fresh 52-week low of ₹85.18–85.31
  intraday on **19 Aug**, before recovering to close Friday at ₹86.35. It's now
  confirmed trading below every key moving average (5/20/50/100/200-day). The
  rate pressure driving this deepened, not eased — RBI Deputy Governor Poonam
  Gupta said there's "no scope for further policy easing" and a rate-hike case
  may emerge this fiscal year, Governor Malhotra flagged broader food/fuel/input
  price risk, and July retail inflation came in at 4.45%, above the RBI's 4%
  target. India's 10-yr yield sits near an 8-week high on this. Offsetting: Q1
  FY27 earnings call reiterated disbursement/AUM/NIM guidance, and two
  independent directors were added to the board (20 Aug) — governance positive,
  not price-moving. Status: **open, tested-and-holding — the ₹85 level survived
  its first real test, but the technical and rate backdrop both weakened.**
- **Adani Power / concentration.** Still ~76% of the book in two Adani Group
  stocks (Adani Power 54.0%, Adani Green 21.8%) — unchanged, still the single
  biggest risk here. New and genuinely significant: a **US federal court
  dismissed the criminal indictment against Gautam Adani, Sagar Adani, and Vneet
  Jaain with prejudice on 10 Aug**, ending that overhang; final judgment levied
  civil penalties ($6M / $12M respectively) but the criminal case is over. CARE
  also upgraded Adani Power's bank facilities/debentures to AA+/Stable (18 Aug).
  This meaningfully de-risks the *governance/regulatory* leg of group risk Day 1
  flagged — but it does **not** change the *sizing* problem, which is the actual
  point: 76% in one promoter group is too concentrated regardless of how clean
  the legal story now looks. Trim call stands. Status: **open, unresolved** (risk
  quality improved; risk quantity unchanged).
- **Adani Green — ₹1,310 support.** This level got its first real test Friday —
  intraday low was ₹1,310.10, and it closed at ₹1,314.00 (+0.94% day-over-day).
  Support held. Thesis reinforced by fresh operational news: **20.1 GW**
  operational renewable capacity as of 30 Jun (+27% YoY), progress on the 500 MW
  Chitravathi pumped-storage project (its first), and a ₹42,000 cr FY27 capex
  plan discussed with analysts on 3 Aug. Status: **open, monitoring — support
  held on first test.**
- **TMPV cost-basis question — major update, escalating this.** Confirmed the
  mechanics of the demerger: record date was **14 Oct 2025**, the commercial-
  vehicle business was demerged into a new entity that took the "Tata Motors
  Limited" name and now trades as **TMCV** (listed 12 Nov 2025, ₹472.55 as of 21
  Aug close), on a **1:1 entitlement** for every share held as of the record
  date. The passenger-vehicle business kept the *original* listing/ISIN
  (INE155A01022 — this is exactly Sujal's holding) and now trades as TMPV.
  Confirming the bookkeeping-artifact theory: **TMPV's entire 52-week trading
  range is ₹294.30–₹447.79 — it has never once traded anywhere near ₹640.30**
  since it started trading under this identity, so that average price cannot be
  a real TMPV entry price; it's a pre-split blended cost basis. More important:
  **today's real Groww fetch shows no TMCV holding in the account at all.** If
  Sujal held these shares before the 14 Oct 2025 record date, he should also be
  holding 5 TMCV shares — worth roughly ₹2,362.75 at today's price — that simply
  aren't appearing here. Action: don't treat −50.3% as real, and specifically
  check Groww's holdings/corporate-actions tab (or the original contract note)
  for a TMCV credit. If it's genuinely missing from the demat, that's worth
  raising with Groww/CDSL directly, not just noting as a bookkeeping footnote.
  Separately, operationally TMPV looks fine: July 2026 sales were 63,760 units,
  +59% YoY, and price hikes are planned for 1 Sep (up to ₹25,000/vehicle) —
  the Sanand plant flood disruption (Aug) was already resolved by 20 Aug.
  Status: **open, escalated — still needs Sujal's input, not resolved
  automatically.**
- **GOLDBEES — parabolic move.** Friday's close is unchanged at ₹131.32
  (+99.7%), since GOLDBEES only trades when NSE is open. But retail 24K gold
  rates quoted over the weekend (Sat 22 Aug) are running noticeably higher —
  roughly ₹16,300–16,760/g across cities, up from the ~₹15,928–16,048/g range
  cited Day 1 — as Brent ($94.39) and WTI ($87.06) both stay elevated on the
  US–Iran Strait of Hormuz standoff, even with Iran's president signalling
  Friday that Tehran wants the conflict to end soon. Since the ETF hasn't traded
  since Friday, this weekend strength isn't priced in yet — a gap-up at Monday's
  open looks likely. Recommendation unchanged, arguably reinforced: trim into
  strength, keep a smaller core slice as hedge. Status: **open, unresolved.**

**Today's macro backdrop (Fri 21 Aug close, still the latest session):** Sensex
77,540.83 (+3.11 pts), Nifty 50 24,252.00 (+0.08%). Metal (Welspun Corp +15.3%
on a $1.8bn order win) and Private Banks (Bank Nifty +266 pts) led; IT, FMCG,
Auto, Media, and Pharma lagged. India's 10-yr yield is near an 8-week high
(~6.87%) on hawkish RBI commentary. Brent/WTI both elevated on the US–Iran
standoff (~8mn bpd of supply estimated disrupted), though Friday brought a
slightly conciliatory signal from Iran. US markets: Dow +517.80 (+1.0%) to
53,277.01, S&P 500 +33.21 (+0.4%) to 7,674.37, Nasdaq +113.29 (+0.4%) to
26,180.45 — a Friday bounce that trimmed, but didn't erase, a down week. Gold
kept climbing into the weekend on the same tension. FII outflows / US tariff
overhang remain a background worry for Indian equities generally.

**Capital note:** No change — Sujal is still weighing ~₹10,000 in fresh capital
this month; no decision made. The Adani legal-risk resolution above doesn't
change the guidance from Day 1: still avoid adding to Adani Power/Green given
the concentration math (that's a sizing issue, not a thesis-quality issue), and
still consider (a) a broad Nifty 50 index fund/ETF, (b) adding to IRFC only if
the railway-capex thesis still holds despite the technical weakness, or (c)
staggering entry over 3–4 tranches. Revisit once Sujal decides.

## Day 1 — Saturday, 22 Aug 2026

**Baseline established.** First read on the book, done manually with Claude before
the automated pipeline existed. Portfolio: 5 holdings, ₹28,040.26 invested,
₹36,220.20 current value, **+29.17% overall**, as of Friday 21 Aug close (market
shut for the weekend).

| Symbol | Bucket | Qty | Avg | LTP (21 Aug) | P&L | Action |
|---|---|---|---|---|---|---|
| IRFC | Core | 30 | 145.62 | 86.40 | −40.7% | Watch closely |
| ADANIPOWER | Tactical | 95 | 105.47 | 205.50 | +94.8% | Trim |
| ADANIGREEN | Core | 6 | 1358.21 | 1320.00 | −2.8% | Hold |
| TMPV | Core | 5 | 640.30 | 317.90 | −50.3%* | Verify cost basis |
| GOLDBEES | Tactical | 35 | 65.75 | 131.32 | +99.7% | Trim |

**Open watch items:**

- **IRFC — ₹85 support.** Stock sitting ₹1.40 above its 52-week low. Rate-sensitive
  PSU lender; today's RBI-hawkish move pushed India's 10-yr yield to a 2-month
  high, which is the direct pressure here. A decisive close below ₹85 on volume
  would say this is more than a rate scare. Status: **open, unresolved.**
- **Adani Power / concentration.** Up 94.8%, but now 54% of total portfolio value.
  Combined with Adani Green (22%), **76% of the book sits in two Adani Group
  stocks** — this is the single biggest risk in the portfolio right now, bigger
  than any individual stock call, because group-level news (financing,
  regulatory, governance) can move both at once regardless of their different
  sector stories. Recommended trimming a third to half of Adani Power into
  strength and treating any new capital as an opportunity to diversify away from
  this group, not add to it. Status: **open, unresolved.**
- **Adani Green — ₹1,310 support.** Down 15.6% over the past month despite a
  +34.7% 1-year return; reads as the sector-wide rate-sensitive pullback, not a
  company-specific break. Thesis (India's renewable build-out, long-term PPAs)
  intact. Status: **open, monitoring.**
- **TMPV cost-basis question.** Average price of ₹640.30 likely predates the
  November 2025 Tata Motors Commercial/Passenger demerger. The −50.3% shown is
  probably partly a bookkeeping artifact — Sujal needs to check his contract
  notes / Groww's corporate-actions tab for the TMCV allocation before this
  number is treated as real. Until confirmed, don't average down. Status:
  **open, needs Sujal's input — do not resolve automatically.**
- **GOLDBEES — parabolic move.** Up 99.7%, driven by a genuine spike in 24K gold
  (~₹15,442/g → ~₹16,048/g in one week) on US–Iran tension, softer yields, and
  dollar weakness. This is Sujal's portfolio hedge. Recommendation: trim into
  strength, keep a smaller core slice as ongoing insurance. Status: **open,
  unresolved.**

**Today's macro backdrop (Fri 21 Aug close):** Sensex 77,540.83 (flat), Nifty 50
24,252.00 (+0.08%). Metal and Private Banks led; FMCG, Auto, IT lagged. Global
bond yields elevated; oil and gold both up on US–Iran tension. US markets mixed
(Dow +500 pts Friday, still down on the week). FII outflows / US tariff overhang
remain a background worry for Indian equities generally.

**Capital note:** Sujal is considering deploying ~₹10,000 in fresh capital this
month. Given the concentration flag above, the reasoning discussed was: avoid
adding to Adani Power/Green, and instead either (a) diversify via a broad Nifty 50
index fund/ETF, or (b) add conviction to IRFC if he still holds the railway-capex
thesis despite the technical weakness, or (c) stagger entry over 3–4 tranches
given the current risk-off macro backdrop rather than a lump sum. No decision
made yet as of Day 1 — revisit and update this note once Sujal decides.

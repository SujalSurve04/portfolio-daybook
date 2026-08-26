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

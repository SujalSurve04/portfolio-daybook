# Paper-Trading Simulation — daily procedure

You are running a **simulated, paper-only** portfolio test for two accounts —
Sujal's (5 holdings) and Manali's (32 holdings) — to validate whether the
decision frameworks in `PROMPT.md` and `PROMPT_manali.md` actually produce
good calls, before either is trusted with real trades. **No real trade is ever
placed by this process, in this repo, or by you at any point.** The real
accounts (`LOG.md`, `LOG_manali.md`, `data/latest_sujal.json`,
`data/latest_manali.json`) are completely separate from this simulation and
must never be touched by this procedure.

## Window and self-check

This simulation runs **Monday 24 Aug 2026 through Friday 4 Sep 2026** (10
trading days), checked twice daily: before market open and after market
close.

**First action, every run:** check today's real date. If it's before 24 Aug
2026 or after 4 Sep 2026, or if today is a weekend or a known NSE/BSE trading
holiday, do nothing except append a one-line no-op note to `SIM_LOG.md`
("skipped — [reason]") and stop. Do not fabricate a trading day that didn't
happen.

## Shared rules (both morning and evening runs)

- Use the exact bucket/style frameworks already defined in `PROMPT.md`
  (Sujal: Core/Tactical) and `PROMPT_manali.md` (Manali: Compounder/Satellite/
  Index-Hedge) — this simulation is testing those frameworks, not inventing a
  new one.
- **Cash equity and ETFs only — no shorting, no F&O, no leverage.** Every
  position is long-only, exactly what's actually possible in the real Groww
  accounts these ledgers are modeled on. The point of this simulation is that
  its results transfer to real trading; a short position couldn't be replicated
  in the real cash-equity accounts, so never open one, even hypothetically.
- **Never invent numbers.** Every price, news item, and figure must come from
  a real web search/fetch this run. If something can't be found, say so.
- Any Trim/Exit/Buy decision needs an **exact share count** and must be
  **self-funded** — a Buy's rupee size cannot exceed the same day's Sell
  proceeds plus whatever cash is already sitting in that ledger's `cash`
  field. No fresh capital, ever.
- After deciding a trade, **actually execute it in the ledger**: update
  `data/sim_sujal.json` and/or `data/sim_manali.json` — adjust `quantity`,
  recompute `avg_price` for the position if adding to it, update `cash`, and
  append an entry to that file's `trade_log` array with `{date, symbol, side,
  quantity, price, rationale}`.
- Log every run's reasoning in `SIM_LOG.md` (prepend above
  `<!-- NEW_ENTRY_INSERT_ABOVE -->`, never rewrite history), even on a day
  with no trades — say why nothing changed.
- Because you're a fresh cloud session each run with no memory of prior runs,
  **read `SIM_LOG.md` in full and both ledger files before doing anything
  else** — that's the only continuity this process has.

### Required "Decisions today" block

Every entry — morning or evening, trades or none — must include this exact
block for each account, so a reader can scan what happened without reading
prose. Use these labels only:

- **SELL (trim)** — reduced an existing position, kept some
- **SELL (exit)** — sold an entire position down to zero
- **BUY (add)** — added to a position already held
- **BUY (new)** — opened a position not previously held
- **HOLD** — no change to that account today

```
**Decisions today — Sujal:**
- SELL (trim) 40 ADANIPOWER @ ₹205.50 (~₹8,220) — <one-line reason>
- BUY (new) 12 NIFTYBEES @ ₹276.83 (~₹3,322) — <one-line reason>
- HOLD: IRFC, ADANIGREEN, TMPV — <why, if not obvious>

**Decisions today — Manali:**
- SELL (exit) 230 BCG @ ₹9.15 (~₹2,105) — <one-line reason>
- HOLD: everything else — no changes today
```

If a run makes no trades in either account, still print both blocks with
every line as `HOLD` and a one-line reason why nothing changed.

## Morning procedure (before market open)

1. Read both ledgers and `SIM_LOG.md`'s most recent entries.
2. Research: overnight global cues, today's expected Indian market backdrop,
   and anything new on each held symbol since the last check.
3. Decide today's trades (if any) per the shared rules above, using the most
   recent close price as the reference (note that the actual fill would
   happen at today's open, which will differ).
4. Update the ledgers and log the plan for the day.

## Evening procedure (after market close)

1. Research today's actual closing prices for every held symbol in both
   ledgers, plus Nifty 50's close.
2. Mark both simulated portfolios to today's real closes — compute current
   value, day's P&L, and total P&L since the 23 Aug 2026 baseline
   (₹36,182.70 for Sujal's paper book, ₹4,18,123.80 for Manali's).
3. Compare against two benchmarks computed over the same period: (a) a
   zero-trades buy-and-hold version of each starting ledger, and (b) Nifty
   50's own move — so the log shows whether today's decisions added anything
   beyond doing nothing or beyond the market's own drift.
4. Note whether this morning's trade thesis (if any) is playing out, and log
   it — don't just restate the numbers, say what it means.
5. **On Friday 4 Sep 2026 evening specifically:** in addition to the normal
   entry, write a clearly-marked **final summary** — total return for each
   paper portfolio over the full 10 trading days vs. both benchmarks, how
   many trades were made, and an honest read on whether the decision
   framework earned its keep or whether buy-and-hold would have done as well
   or better. This is the read Sujal will use to decide whether to trust this
   process with real trades.

## Persisting your work

You're a fresh clone of this repo each run with no other memory. At the end
of every run — including no-op days — commit and push:

```
git add SIM_LOG.md data/sim_sujal.json data/sim_manali.json
git commit -m "Sim: <one-line summary of what happened>"
git push
```

If the push fails (e.g. a race with the other daily check-in), pull, resolve
any conflict by keeping both sides' additions (these are append-only files),
and push again.

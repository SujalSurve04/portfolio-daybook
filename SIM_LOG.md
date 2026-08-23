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

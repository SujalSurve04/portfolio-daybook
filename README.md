# Portfolio Daybook — automated Groww strategy bot

Every morning this repo fetches real Groww holdings across **two accounts**
(Sujal's and Manali's), has Claude Code research the day's market context and
decide what to do with each position, and commits the result as an updated
running log per account plus one shared dashboard. No device or desktop app has
to be online for this to run — GitHub's own servers run it on a schedule.

The two accounts are independent on the data/analysis side — separate
credentials, separate data files, separate logs, separate instructions/style —
but render into **one `dashboard.html`** with a Sujal/Manali toggle at the top,
so there's a single link to bookmark. Both are now fully wired up: Sujal's
(`PROMPT.md` → `LOG.md`) and Manali's (`PROMPT_manali.md` → `LOG_manali.md`),
each writing only into its own panel of the shared dashboard.

## Files

| File | Purpose |
|---|---|
| `PROMPT.md` | The instructions Claude Code follows for Sujal's account every run — role, process, output format. Edit this to change how his analysis works. |
| `PROMPT_manali.md` | Same, for Manali's account — a different investing-style framework (Compounder/Satellite/Index-Hedge, sizing-discipline lens) built from what's actually in her book. |
| `LOG.md` | Sujal's running daily journal. Never rewritten wholesale — each run only prepends a new entry, so nothing from a previous day is lost. |
| `LOG_manali.md` | Manali's running daily journal — same discipline, separate account. |
| `scripts/fetch_holdings.py` | Authenticates to Groww with a TOTP key and writes today's holdings to `data/latest_<account>.json`. Takes the account name (`sujal` or `manali`) as its one argument. Read-only — cannot place trades. |
| `dashboard.html` | The shared rendered view for both accounts — a toggle switches between Sujal's and Manali's panels (each a self-contained `<div data-panel="...">`, plain CSS/JS, no build step). Each account's Claude Code run only touches its own panel. |
| `.github/workflows/daily-strategy.yml` | The schedule. Runs both fetch scripts, then both Claude Code analysis steps, then commits. |

## One-time setup

1. **Create a private GitHub repository** and push these files to it. (Private is
   recommended — this repo's history holds portfolio cost basis for both
   accounts, even though it never holds login credentials.)

2. **Install the Claude GitHub App** on that repository:
   [github.com/apps/claude](https://github.com/apps/claude)

3. **Add repository secrets** — Settings → Secrets and variables → Actions → New
   repository secret:

   | Secret name | Value |
   |---|---|
   | `GROWW_API_KEY_SUJAL` | Sujal's API key from `groww.in/trade-api/api-keys` (TOTP-type key) |
   | `GROWW_TOTP_SECRET_SUJAL` | The TOTP secret shown alongside that key |
   | `GROWW_API_KEY_MANALI` | Manali's API key, same process on her account |
   | `GROWW_TOTP_SECRET_MANALI` | Her TOTP secret |
   | `ANTHROPIC_API_KEY` **or** `CLAUDE_CODE_OAUTH_TOKEN` | See the note below |

   For the Claude credential, you have two options:
   - **API key** (`ANTHROPIC_API_KEY`): pay-as-you-go billing from the
     [Claude Console](https://platform.claude.com), separate from any Claude
     subscription you already have.
   - **Subscription token** (`CLAUDE_CODE_OAUTH_TOKEN`): if you're on a Claude
     Pro, Max, Team, or Enterprise plan, run `claude setup-token` on your own
     machine once, and use the token it prints instead — this uses your existing
     subscription rather than separate API billing. If you use this option,
     open `.github/workflows/daily-strategy.yml` and swap the
     `anthropic_api_key:` line for `claude_code_oauth_token:` as shown in the
     comment right above it.

4. **Turn on GitHub Pages** (optional, for the phone-friendly link) — Settings →
   Pages → Deploy from branch → `main` / root. You'll get a URL like
   `https://<your-username>.github.io/<repo-name>/dashboard.html` that always
   shows the latest run.

5. **Pick your run time.** The workflow defaults to 06:00 IST
   (`cron: "30 0 * * *"`, since GitHub Actions cron is always UTC). To change it,
   edit the `cron` line — for 12:30 AM IST, use `"0 19 * * *"` (19:00 UTC the
   previous day).

6. **Test it** before trusting the schedule: go to the Actions tab → "Daily
   Portfolio Strategy" → "Run workflow" to fire it manually and watch the log.

## What this bot will never do

- Place, modify, or cancel a trade — the Groww script only ever calls read-only
  holdings endpoints.
- Store your Groww password or any login credential — only the API key and TOTP
  secret you generated specifically for programmatic, read-only access.
- Give you formal investment advice — every output is framed as informational
  analysis for your own decision-making, not a licensed recommendation.

## Costs to expect

- **GitHub Actions**: minutes for a private repo's scheduled run are free up to
  2,000 minutes/month on GitHub's free tier — one daily run of a few minutes is
  nowhere close to that limit.
- **Groww API**: the ₹499+GST/month plan you're already on.
- **Claude**: either your existing subscription (via the OAuth token option) or
  small pay-as-you-go API charges (via the API key option) — a few thousand
  tokens per day for research + writing, so this should be a very small amount
  either way.

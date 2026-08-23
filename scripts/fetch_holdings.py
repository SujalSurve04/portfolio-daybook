#!/usr/bin/env python3
"""
Fetch real Groww holdings for a named account and write them to
data/latest_<account>.json.

Auth uses Groww's TOTP-based API key flow, which does not expire daily like
the plain API-key-and-secret flow does. Both credentials are read from
environment variables — they are never hardcoded here and never leave
Groww's own API — so this file is safe to commit to a public or private repo.

Usage:
    python scripts/fetch_holdings.py <account>

Known accounts and their required environment variables (set as GitHub
Actions secrets in CI, or in a local `.env` file — see `.env.example` — for
local testing):
    sujal    GROWW_API_KEY_SUJAL / GROWW_TOTP_SECRET_SUJAL
    manali   GROWW_API_KEY_MANALI / GROWW_TOTP_SECRET_MANALI

This script only ever calls read-only endpoints (holdings). It never places,
modifies, or cancels an order, and it never will.
"""

import json
import os
import sys
from datetime import datetime, timezone

import pyotp
from dotenv import load_dotenv
from growwapi import GrowwAPI

ACCOUNTS = ("sujal", "manali")


def main():
    load_dotenv()  # no-op in CI, where the real env vars are already set

    if len(sys.argv) != 2 or sys.argv[1] not in ACCOUNTS:
        print(
            f"Usage: python {sys.argv[0]} <account>\n"
            f"  <account> must be one of: {', '.join(ACCOUNTS)}",
            file=sys.stderr,
        )
        sys.exit(1)

    account = sys.argv[1]
    suffix = account.upper()

    api_key = os.environ.get(f"GROWW_API_KEY_{suffix}")
    totp_secret = os.environ.get(f"GROWW_TOTP_SECRET_{suffix}")

    if not api_key or not totp_secret:
        print(
            f"ERROR: GROWW_API_KEY_{suffix} and GROWW_TOTP_SECRET_{suffix} "
            "must be set as environment variables (GitHub Actions secrets, "
            "or in .env for local testing).",
            file=sys.stderr,
        )
        sys.exit(1)

    totp_code = pyotp.TOTP(totp_secret).now()
    token_response = GrowwAPI.get_access_token(api_key=api_key, totp=totp_code)

    # The SDK has returned the token under different shapes across versions;
    # handle both a bare string and a dict response defensively.
    if isinstance(token_response, dict):
        access_token = (
            token_response.get("token")
            or token_response.get("access_token")
            or token_response.get("data")
        )
    else:
        access_token = token_response

    if not access_token:
        print(
            f"ERROR: could not extract access token from response: {token_response!r}",
            file=sys.stderr,
        )
        sys.exit(1)

    groww = GrowwAPI(access_token)
    holdings_resp = groww.get_holdings_for_user()
    holdings = holdings_resp.get("holdings", holdings_resp)

    snapshot = {
        "account": account,
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "holdings": holdings,
    }

    os.makedirs("data", exist_ok=True)
    out_path = f"data/latest_{account}.json"
    with open(out_path, "w") as f:
        json.dump(snapshot, f, indent=2)

    print(f"Wrote {len(holdings)} holdings to {out_path}")


if __name__ == "__main__":
    main()

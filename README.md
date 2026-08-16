# GenLayer TrustCheck

TrustCheck is a GenLayer project concept for evidence-based claim review. A user submits a claim and an authoritative source URL. A GenLayer Intelligent Contract asks validators to evaluate whether the source supports the claim and records a consensus result: `VERIFIED`, `UNVERIFIED`, or `UNCERTAIN`.

## Why it matters

Online claims can be difficult to verify consistently. TrustCheck makes the decision process explicit: the source is supplied by the user, the Intelligent Contract evaluates it through GenLayer's validator consensus, and the result is stored as contract state rather than being only a chat response.

## Architecture

- `contracts/TrustCheck.py` — Intelligent Contract logic.
- `frontend/` — browser UI and integration adapter.
- The frontend collects the claim and source and exposes the transaction lifecycle.

## Contract workflow

1. Deploy `TrustCheck` to a GenLayer-compatible environment.
2. Call `submit_claim(claim, source_url)`.
3. Call `evaluate()` to trigger the Intelligent Contract evaluation.
4. Read `get_result()` for the stored consensus result.
5. Configure `frontend/app.js` with the deployed contract address and GenLayer RPC/provider.

## Status

This repository contains the reference implementation and frontend shell. A live deployment address/provider must be configured before sending production transactions.

## Design

The original animated spinner from this repository's earlier contribution remains available as `genlayer-spinner.svg`; it is not required for TrustCheck's core workflow.

# Code Quality Agent (CQA) — Compiler-Backed AST & SARIF 2.1.0 Gate

**38 deterministic static rules, 0 runtime dependencies (`stdlib` only), compiler-as-ground-truth (`cargo check` / `tsc` / `compile`), Tarjan SCC import-cycle detection, and SARIF 2.1.0 output.**

* **Live Browser Sandbox:** **https://github.io**
* **Verification Status:** `59/59 PROVEN` (`_synthetic: false | preservation: 100.0% | verified: true`)

## Why CQA vs. Probabilistic Linters
* **Compiler-Backed Ground Truth:** Uses real compiler diagnostics (`cargo check`, `tsc`, Python AST `compile`) alongside 38 zero-dependency rules to eliminate false positives.
* **Zero-Float & Secret Hygiene:** Detects IEEE 754 `float64` drift in financial paths, import cycles (Tarjan SCC), and hardcoded credentials prior to merge.
* **Explicit Scope Transparency:** `report.errors` explicitly lists unverified boundaries (no taint analysis or code duplication heuristics) for audit compliance.

## Commercial Source Code & Private Repo Access ($149)
Instant read-only GitHub repository provisioning via Stripe, Apple Pay, or PayPal: **[Buy APUMIA Code Quality AST Gate ($149) ↗](https://lava.top)**

*Support & Enterprise Licensing: [Official GitHub Support Desk ↗](https://github.com)*

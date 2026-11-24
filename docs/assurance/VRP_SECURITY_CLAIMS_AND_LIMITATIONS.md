# VRP Security Claims and Evidence Limitations

**Document class:** Public security assurance
**Evidence cutoff:** 2026-11-24

## Declared protocol objectives

VRP publicly identifies the following objectives:

- Logical session continuity independent of transport.
- Replay containment.
- Duplicate-commit rejection.
- Stale-authority rejection.
- Epoch rollback rejection.
- Deterministic authority resolution.
- Canonical-history preservation.
- Recovery preservation.
- Evidence integrity and tamper detection.

These are declared objectives and qualification targets.
Listing an objective does not establish independent proof
that every implementation satisfies it.

## Evidence levels

**Observed:** A directly recorded event within a defined
measurement boundary.

**Contract-tested:** Behavior demonstrated using controlled
test fixtures or an isolated verifier.

**Independently qualified:** A property established using
independently attributable runtime evidence and appropriate
negative controls.

**Inconclusive:** The evidence does not support a definitive
qualification verdict.

## Current limitations

Independent transport observations exist.

An isolated synthetic witness contract passed eleven
controlled tests.

The current public evidence workflow lacks connected,
independently attributable witnesses for canonical
session identity, receiver-side application commits,
authority decisions and anchored canonical history.

Therefore independently qualified end-to-end logical
session continuity is not currently claimed.

## Explicit non-claims

This report does not assert:

- Formal verification of the entire protocol.
- Immunity to all attacks or network failures.
- Zero packet loss under adverse conditions.
- Universal availability during blackout.
- Independent certification of Protected Core.
- Completed compound-fault qualification.
- Logical-session continuity proven by UDP recovery.

## Independent review

A credible evaluation must be reproducible, adversarial,
scope-bounded and capable of returning negative findings.

A missing witness must produce an inconclusive result,
not a manufactured success.

## Intellectual property boundary

Public review may use specifications, observable behavior,
approved evidence and authorized test interfaces.

Protected Core implementation, algorithms, secrets,
credentials and private operational details are excluded.

**Engineering rule: No claim exceeds its evidence.**

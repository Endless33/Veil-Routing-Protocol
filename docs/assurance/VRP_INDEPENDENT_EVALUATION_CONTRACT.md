# VRP Independent Evaluation Contract

**Evaluation model:** Authorized black-box assessment
**Policy:** Default deny

## Objective

Determine whether a canonical logical session retains
its identity and accepted history across changes or
failures of the underlying transport.

The following properties must remain distinguishable:

1. Transport reachability.
2. Canonical logical-session identity.
3. Receiver-side committed application effects.
4. Authority acceptance and rejection.
5. Canonical-history integrity.

## Evidence requirements

### Canonical identity

A trusted observation source must provide comparable
identity evidence before, during and after transport
changes. An unauthenticated session string is insufficient.

### Application commits

The receiver-side effect ledger must distinguish accepted
operations, rejected operations and duplicates.
A transport response is not a committed application effect.

### Authority

The evidence must distinguish authorized transitions from
stale, replayed, conflicting or otherwise rejected actions.

### History

Evidence must support detection of rollback, tampering and
unauthorized changes to accepted history.

### Transport

An independent harness should record endpoint changes,
packet delivery, loss, recovery and timing.

## Qualification targets

These are planned test conditions, not completed results.

| Scenario | Target |
|---|---|
| Endpoint churn | 2-second cadence |
| Packet loss | 50% and 80% |
| Blackout | 10 and 30 seconds |
| Replay | Reject replayed inputs |
| Duplicate commits | Reject duplicate effects |
| Authority conflict | Reject unauthorized transitions |
| History tampering | Detect inconsistency |
| Compound faults | Churn + loss + blackout |

## Mandatory negative controls

A verifier must not accept:

- Stable PID as session continuity.
- UDP recovery as canonical identity.
- Socket identity as logical-session identity.
- Synthetic fixtures as production execution.
- Self-reported strings without trusted provenance.
- Unanchored hashes as independent history proof.
- Request/reply counts as receiver-side commits.

## Decision rules

**PASS:** Required evidence is present, attributable,
consistent and verified against applicable negative controls.

**FAIL:** Verified evidence contradicts an acceptance criterion.

**INCONCLUSIVE:** Required evidence is missing or insufficient.

The evaluator must never infer PASS from missing observations.

## Authorization boundary

Evaluation access must be explicitly authorized,
scope-bounded and revocable.

This contract grants no access to Protected Core,
private infrastructure, credentials or implementation
secrets.

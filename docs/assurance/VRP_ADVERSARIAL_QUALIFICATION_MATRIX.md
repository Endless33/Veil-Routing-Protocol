# VRP Adversarial Qualification Matrix

**Classification:** Public evaluation contract
**Evidence cutoff:** 2026-11-24
**Current independent continuity qualification:** INCONCLUSIVE

## Governing principle

**SESSION != TRANSPORT**

A transport path can fail, recover or change without
establishing whether the canonical logical session
has survived.

Each test must distinguish transport behavior from
session identity, accepted application effects,
authority integrity and canonical history.

## Qualification matrix

| Scenario | Target condition | Required observation | Status |
|---|---|---|---|
| Endpoint churn | 2-second cadence | Canonical identity across transitions | Not qualified |
| Packet loss | 50% | Delivery and committed-effect accounting | Not qualified |
| Severe loss | 80% | Recovery and bounded behavior | Not qualified |
| Blackout | 10 seconds | Identity and history before/after outage | Not qualified |
| Extended blackout | 30 seconds | Recovery and authority integrity | Not qualified |
| Replay | Repeated or stale input | Rejection without duplicate effect | Not qualified |
| Duplicate operation | Repeated operation identity | At most one accepted effect | Not qualified |
| Stale authority | Unauthorized prior authority | Rejection with attributable evidence | Not qualified |
| History tampering | Modified evidence | Independent integrity failure | Not qualified |
| Compound faults | Churn + loss + blackout | All required witnesses together | Not qualified |

These are evaluation targets. This table does not
represent successful execution of these scenarios.

## Evidence already available

Previous isolated qualification work recorded
external UDP request/response behavior and transport
request accounting.

An isolated synthetic witness contract passed
eleven controlled tests, including negative controls.

Those results do not establish canonical session
continuity, receiver-side application commits or
authority integrity in a production runtime.

## Required measurement fields

An authorized evaluation should record:

- Scenario and environment identity.
- Start and end timestamps.
- Transport endpoint observations.
- Applied fault conditions and their timing.
- Canonical session identity witness status.
- Receiver-side committed and rejected effects.
- Authority acceptance and rejection outcomes.
- Canonical-history integrity status.
- Recovery measurements and uncertainty.
- Missing observations and test limitations.

## Verdict semantics

**PASS:** The applicable criteria are met and supported
by independently attributable runtime evidence.

**FAIL:** Valid evidence demonstrates violation of an
applicable criterion.

**INCONCLUSIVE:** Required evidence is absent, ambiguous
or insufficient.

**NOT TESTED:** No qualifying execution was performed.

A synthetic verifier PASS cannot be substituted for
a real runtime qualification PASS.

## Security boundary

This document describes externally testable behavior
and evidence requirements only.

It does not disclose Protected Core algorithms,
internal authority mechanisms, private runtime code
or operational secrets.

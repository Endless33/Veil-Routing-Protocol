# Veil Routing Protocol — Public Threat Model

## Public Security and Continuity Model

Veil Routing Protocol (VRP) is a continuity-first networking architecture built around a fundamental separation:

**Session != Transport**

This document describes the public threat model used to reason about continuity, authority, recovery, and externally observable correctness.

It defines:

- what classes of failure or adversarial conditions matter;
- which public invariants are expected to survive;
- what observable outcome would represent failure;
- what is explicitly outside the scope of this public document.

It intentionally does not disclose:

- protected runtime algorithms;
- internal authority-selection mechanisms;
- private recovery decision logic;
- security-sensitive thresholds;
- cryptographic implementation details;
- proprietary state-machine internals;
- private detection mechanisms;
- protected defense mechanisms.

This document defines the threat surface.

It does not disclose the protected mechanisms used to defend that surface.

---

# 1. Threat Model Objective

VRP begins from an assumption that is deliberately hostile to idealized networking:

```text
NETWORKS FAIL.

PATHS CHANGE.

TRANSPORTS DISAPPEAR.

OLD INFORMATION RETURNS.

EVENTS DUPLICATE.

DELIVERY REORDERS.

RECOVERY RACES OCCUR.
```

The security question is therefore not:

> Can failure be eliminated?

The relevant question is:

> Can defined continuity and authority properties remain correct when failure occurs?

---

# 2. Protected Assets

At the public architectural level, VRP is concerned with protecting several properties.

## Session Identity

Transport replacement must not automatically redefine logical session identity.

## Authority

Stale, conflicting, or replayed information must not silently become authoritative progress.

## Canonical State

The system must maintain a coherent accepted state rather than silently producing incompatible authoritative histories.

## Historical Integrity

Recovery must not become permission to rewrite previously accepted canonical history.

## Execution Integrity

Duplicate observation must not silently become duplicate canonical execution.

## Recovery Integrity

Restoring reachability must not override continuity correctness.

## Evidence Integrity

Evidence used to support validation claims must not silently remain valid after unauthorized modification.

## Determinism

Equivalent validation conditions should not produce unexplained divergent outcomes.

---

# 3. Trust Assumptions

VRP does not treat the network transport itself as a sufficient trust anchor.

Conceptually:

```text
NETWORK INPUT
     !=
TRUSTED STATE
```

Likewise:

```text
REACHABLE
    !=
AUTHORITATIVE
```

and:

```text
PREVIOUSLY VALID
       !=
CURRENTLY AUTHORITATIVE
```

Transport availability is an observation.

It is not, by itself, proof of continuity authority.

---

# 4. Threat: Transport Loss

## Condition

The currently active transport disappears.

```text
SESSION
   |
TRANSPORT A
   |
   X
```

Possible causes include ordinary network failure, interface loss, mobility, infrastructure disruption, or intentional failure injection.

## Property Under Threat

Session continuity.

## Required Public Property

```text
TRANSPORT LOSS
      !=
AUTOMATIC SESSION IDENTITY LOSS
```

## Failure Condition

The threat succeeds if transport disappearance alone incorrectly causes logical identity to be redefined where continuity should have remained valid.

---

# 5. Threat: Transport Replacement

## Condition

A previous transport becomes unavailable and another transport becomes usable.

```text
TRANSPORT A
     |
     X
     |
TRANSPORT B
```

## Property Under Threat

The separation between session identity and transport identity.

## Required Public Property

```text
NEW TRANSPORT
      !=
AUTOMATIC NEW SESSION
```

## Failure Condition

The threat succeeds if transport replacement alone incorrectly establishes a new logical identity or invalid authority transition.

---

# 6. Threat: Temporary Connectivity Collapse

## Condition

No usable transport is available for some period.

```text
CONNECTED
    |
    X
 OFFLINE
    |
    |
RECOVERY
```

## Property Under Threat

Continuity state and recovery correctness.

## Required Public Property

Temporary lack of reachability must not silently authorize arbitrary state reconstruction.

## Failure Condition

The threat succeeds if recovery from an outage accepts state that violates the declared continuity invariants.

---

# 7. Threat: NAT or Address Change

A session may encounter a change in observable network addressing without a corresponding change in logical identity.

Conceptually:

```text
LOGICAL SESSION
      |
NETWORK LOCATION A
      |
      v
NETWORK LOCATION B
```

## Property Under Threat

Identity continuity.

## Required Public Property

Network-address change alone must not be treated as proof that the logical session identity changed.

## Failure Condition

The threat succeeds if addressing changes alone incorrectly redefine continuity authority.

The exact mechanisms used to evaluate path changes remain protected.

---

# 8. Threat: Replay

## Condition

Previously observed information is presented again.

```text
T1:

EVENT X
  |
ACCEPTED

T2:

EVENT X
  |
OBSERVED AGAIN
```

## Property Under Threat

Canonical progress.

## Required Public Property

```text
REPLAY != PROGRESS
```

## Failure Condition

The threat succeeds if previously accepted information is incorrectly interpreted as a new authoritative transition.

---

# 9. Threat: Replay Flood

## Condition

Historical or duplicated information is repeatedly presented.

```text
REPLAY
REPLAY
REPLAY
REPLAY
REPLAY
...
```

## Property Under Threat

Canonical execution and bounded behavior.

## Required Public Property

Repeated invalid historical input must not become repeated canonical progress.

## Failure Condition

The threat succeeds if repeated replay causes prohibited authoritative transitions or violates the tested runtime bounds.

This document does not claim resistance to every possible denial-of-service attack.

Resource-exhaustion behavior must be evaluated separately under explicitly defined conditions.

---

# 10. Threat: Duplicate Delivery

## Condition

The same logical input is observed multiple times.

```text
EVENT X

EVENT X
```

## Property Under Threat

Execution integrity.

## Required Public Property

```text
DUPLICATE OBSERVATION
        !=
DUPLICATE CANONICAL EXECUTION
```

## Failure Condition

The threat succeeds if repeated delivery silently creates repeated authoritative execution where only one canonical transition should exist.

---

# 11. Threat: Stale State Return

## Condition

Older state becomes observable after newer state has already been accepted.

```text
STATE A
   |
STATE B
   |
STATE C

CURRENT = C

later:

STATE A RETURNS
```

## Property Under Threat

Authority monotonicity.

## Required Public Property

```text
HISTORICALLY VALID
       !=
AUTHORITATIVE NOW
```

## Failure Condition

The threat succeeds if stale state regains authority merely because it becomes available again.

---

# 12. Threat: Authority Rollback

## Condition

An older authority state attempts to replace a newer accepted authority state.

```text
AUTHORITY N
     |
     v
AUTHORITY N+1

later:

AUTHORITY N RETURNS
```

## Property Under Threat

Monotonic authority progression.

## Required Public Property

Older authority must not silently replace newer accepted authority.

## Failure Condition

The threat succeeds if the runtime accepts an unauthorized rollback of authority.

The implementation of authority progression remains protected.

---

# 13. Threat: Reordered Delivery

## Condition

Events are delivered in a different order from their logical relationship.

```text
LOGICAL:

A -> B -> C

DELIVERY:

A -> C -> B
```

## Property Under Threat

Causal integrity.

## Required Public Property

Transport delivery order alone must not be allowed to redefine canonical causal history incorrectly.

## Failure Condition

The threat succeeds if reordering produces an invalid authoritative history.

---

# 14. Threat: Delayed Historical Input

Reordering and stale-state return can combine.

An old event may arrive significantly later than expected.

```text
A -> B -> C -> D

             later:

        delayed B appears
```

## Property Under Threat

Historical and causal integrity.

## Required Public Property

Delay alone must not make historical information new progress.

## Failure Condition

The threat succeeds if delayed historical input incorrectly advances or rewrites canonical state.

---

# 15. Threat: Conflicting Recovery State

## Condition

More than one apparently plausible recovery candidate becomes observable.

```text
              /-> B
A -----------|
              \-> C
```

## Property Under Threat

Canonical authority.

## Required Public Property

The existence of multiple candidates must not silently produce multiple incompatible authoritative histories.

## Failure Condition

The threat succeeds if contradictory state becomes simultaneously or incorrectly canonical.

---

# 16. Threat: Recovery Race

## Condition

Multiple recovery-relevant events occur concurrently or in rapid succession.

```text
FAILURE
   |
RECOVERY STARTS
   |
   +---- EVENT A
   |
   +---- EVENT B
   |
ANOTHER FAILURE
```

## Property Under Threat

Recovery correctness and deterministic authority.

## Required Public Property

Recovery races must not silently create invalid authority or contradictory canonical state.

## Failure Condition

The threat succeeds if race conditions cause an invariant violation.

---

# 17. Threat: Failure During Recovery

Recovery itself may be interrupted.

```text
TRANSPORT FAILURE
       |
       v
RECOVERY
       |
       X
SECOND FAILURE
```

## Property Under Threat

Recovery integrity.

## Required Public Property

A second failure must not automatically authorize incomplete or contradictory recovery state.

## Failure Condition

The threat succeeds if interrupted recovery produces invalid canonical progress.

---

# 18. Threat: Repeated Migration

## Condition

The session experiences many transport changes.

```text
A -> B -> A -> C -> B -> D -> A -> ...
```

## Property Under Threat

Session identity and runtime stability.

## Required Public Property

```text
MANY TRANSPORT CHANGES
          !=
MANY LOGICAL SESSION IDENTITIES
```

## Failure Condition

The threat succeeds if repeated migration causes incorrect identity transitions or violates the tested continuity invariant.

---

# 19. Threat: Canonical History Rewrite

## Condition

Recovery or conflicting information attempts to replace already accepted history.

Accepted:

```text
A -> B -> C
```

Invalid rewrite:

```text
A -> X -> Y
```

## Property Under Threat

Historical integrity.

## Required Public Property

```text
RECOVERY
   !=
PERMISSION TO REWRITE
ACCEPTED HISTORY
```

## Failure Condition

The threat succeeds if previously accepted canonical history is silently replaced contrary to the declared continuity rules.

---

# 20. Threat: Restart With Historical State

## Condition

A runtime restarts and encounters previously valid, stale, duplicated, or conflicting information.

```text
RUNTIME
   |
   X
RESTART
   |
HISTORICAL STATE APPEARS
```

## Property Under Threat

Authority continuity.

## Required Public Property

Restart must not make historical state authoritative merely because the runtime has restarted.

## Failure Condition

The threat succeeds if restart enables prohibited stale-state resurrection or authority rollback.

---

# 21. Threat: Concurrent Execution

## Condition

Multiple operations relevant to continuity occur concurrently.

## Property Under Threat

Deterministic canonical state.

## Required Public Property

Concurrency must not produce unexplained authoritative divergence.

## Failure Condition

The threat succeeds if equivalent concurrent conditions can violate declared invariants or create contradictory canonical results.

---

# 22. Threat: Runtime Pressure

## Condition

The runtime operates under adverse but expected environmental pressure.

Examples may include:

```text
JITTER

LATENCY

REORDERING

CONGESTION

REPEATED RECOVERY

HIGH EVENT VOLUME
```

## Property Under Threat

Continuity correctness and bounded runtime behavior.

## Required Public Property

Performance pressure must not silently convert invalid state into authoritative progress.

## Failure Condition

The threat succeeds if pressure causes a declared correctness invariant to fail under the tested operating conditions.

---

# 23. Threat: Evidence Modification

## Condition

A validation artifact is modified after generation.

```text
EXECUTION
    |
    v
EVIDENCE
    |
    X
MODIFICATION
```

## Property Under Threat

Evidence integrity.

## Required Public Property

Modified evidence must not silently verify as the original unmodified evidence.

## Failure Condition

The threat succeeds if unauthorized evidence modification remains undetected within the defined verification model.

---

# 24. Threat: Verdict Substitution

## Condition

An attacker or faulty process attempts to present a different result than the one supported by the original evidence.

Conceptually:

```text
EXECUTION RESULT

      PASS / FAIL

          |
          X
          |
ALTERED VERDICT
```

## Property Under Threat

Validation integrity.

## Required Public Property

The externally presented verdict should remain consistent with the evidence used to support it.

## Failure Condition

The threat succeeds if an altered verdict can be accepted as though it were supported by the original verified evidence.

The internal evidence-protection mechanism remains outside this public document.

---

# 25. Threat: Partial Evidence

## Condition

Only a subset of expected evidence is available.

## Property Under Threat

Confidence in the validation result.

## Required Public Property

Missing evidence must not automatically be interpreted as proof of success.

Conceptually:

```text
NO EVIDENCE
    !=
PASS
```

## Failure Condition

The evaluation fails if a required claim cannot be supported by the evidence required for that specific test.

---

# 26. Threat: Runtime Says "PASS"

A runtime reporting:

```text
PASS
```

is not by itself sufficient evidence.

## Property Under Threat

Independent evaluability.

## Required Public Property

Where independent verification is part of the test model, the evidence must support the verdict separately from the runtime's own textual assertion.

The stronger model is:

```text
EXECUTION
    |
    v
ARTIFACT
    |
    v
VERIFICATION
    |
    v
VERDICT
```

not simply:

```text
PROGRAM PRINTED PASS
```

---

# 27. Threat: False Continuity

One of the most important failure classes is apparent success.

Consider:

```text
NETWORK RECOVERED

APPLICATION RESPONDED

PROCESS STILL RUNNING
```

Those facts do not necessarily prove:

```text
SESSION IDENTITY PRESERVED

AUTHORITY PRESERVED

HISTORY PRESERVED

REPLAY REJECTED

DUPLICATES CONTAINED
```

## Property Under Threat

Correct interpretation of recovery.

## Required Public Property

Availability must not be confused with continuity correctness.

```text
AVAILABLE
    !=
CORRECT
```

---

# 28. Threat: Silent Failure

A continuity violation becomes especially dangerous if the system appears healthy.

Examples include:

```text
STALE STATE ACCEPTED
BUT TRAFFIC CONTINUES

DUPLICATE EXECUTION
BUT PROCESS REMAINS ALIVE

HISTORY REWRITTEN
BUT CONNECTION RECOVERS
```

## Property Under Threat

Observable correctness.

## Required Public Property

Where the evaluation boundary supports it, important invariant failures should produce observable evidence rather than being silently interpreted as success.

---

# 29. Threat: Incorrect Trust in Transport

A newly reachable transport may appear healthy.

That does not establish that state associated with it is current.

Therefore:

```text
LOW LATENCY
    !=
AUTHORITY

REACHABILITY
    !=
AUTHORITY

NEW PATH
    !=
AUTHORITY

OLD PATH RETURNED
    !=
AUTHORITY
```

The transport carries information.

It does not independently define canonical truth.

---

# 30. Threat: Incorrect Trust in Historical Validity

Another dangerous assumption is:

> It was valid once, therefore it is valid now.

VRP explicitly rejects that assumption at the architectural level.

```text
VALID AT T1
    !=
AUTHORITATIVE AT T2
```

This distinction is essential for stale-state and replay reasoning.

---

# 31. Threat: Unbounded Claims

Security documentation itself can create risk if it claims more than the evidence supports.

VRP should not claim:

```text
UNBREAKABLE

PERFECT SECURITY

ZERO FAILURE

ALL ATTACKS PREVENTED

UNLIMITED SCALE

UNIVERSAL PRODUCTION SAFETY
```

Those are not useful testable invariants.

Claims should remain bounded by:

```text
SCENARIO

PROPERTY

ENVIRONMENT

EVIDENCE

VERDICT
```

---

# 32. Out of Scope for This Public Threat Model

This document does not attempt to disclose or fully specify:

- private cryptographic construction;
- key derivation;
- private key lifecycle;
- protected authority-selection algorithms;
- internal recovery policy;
- private defense systems;
- anti-cloning mechanisms;
- proprietary detection logic;
- implementation-specific security thresholds;
- private runtime state transitions;
- internal countermeasure selection;
- protected operational procedures.

Absence of these details is intentional.

They belong to the protected implementation and security boundary.

---

# 33. Also Outside the Claim

VRP does not claim to replace the surrounding infrastructure security model.

A deployment still depends on external security concerns including:

- operating-system security;
- credential protection;
- infrastructure authorization;
- access control;
- deployment security;
- physical security;
- organizational policy;
- network configuration;
- application security.

VRP continuity properties do not make an insecure host secure.

---

# 34. Pilot Threat Evaluation

A pilot participant can select relevant threats from this document.

For example:

| Participant Concern | Threat Class |
|---|---|
| Wi-Fi/mobile handover | Transport replacement |
| Temporary outage | Connectivity collapse |
| Old endpoint returns | Stale-state return |
| Historical packet/input returns | Replay |
| Duplicate upstream delivery | Duplicate delivery |
| Failover conflict | Conflicting recovery state |
| Simultaneous recovery | Recovery race |
| Restart after failure | Restart with historical state |
| Audit manipulation | Evidence modification |
| Incorrect success report | Verdict substitution |

The participant should then define:

```text
FAILURE CONDITION

EXPECTED INVARIANT

OBSERVATION POINT

REQUIRED EVIDENCE

PASS CONDITION

FAIL CONDITION
```

---

# 35. How to Challenge the Model

A serious evaluator should attempt to falsify the public claims.

For example:

```text
1. Establish valid continuity.

2. Remove the active transport.

3. Introduce a replacement transport.

4. Return an old path.

5. Present stale state.

6. Replay previous input.

7. Duplicate delivery.

8. Reorder events.

9. Interrupt recovery.

10. Repeat migration.

11. Restart the relevant runtime.

12. Inspect the resulting evidence.

13. Repeat the scenario.

14. Compare the verdict.
```

If an invariant fails, the result should be treated as an engineering finding.

---

# 36. Threat Model Philosophy

VRP does not begin with:

```text
THE NETWORK IS RELIABLE.
```

It begins closer to:

```text
THE NETWORK MAY FAIL.

THE TRANSPORT MAY CHANGE.

INPUT MAY ARRIVE LATE.

OLD STATE MAY RETURN.

DELIVERY MAY DUPLICATE.

RECOVERY MAY RACE.

THEREFORE AUTHORITY
MUST NOT BE DERIVED
FROM REACHABILITY ALONE.
```

This is the public security logic behind the architecture.

---

# 37. Core Public Security Statements

The public VRP threat model can be reduced to several statements:

```text
SESSION != TRANSPORT

REACHABILITY != AUTHORITY

REPLAY != PROGRESS

DUPLICATE DELIVERY != DUPLICATE AUTHORITY

HISTORICAL VALIDITY != CURRENT AUTHORITY

RECOVERY != PERMISSION TO REWRITE HISTORY

AVAILABILITY != CORRECTNESS

PROGRAM SAYS PASS != INDEPENDENT PROOF
```

These statements describe externally testable architectural properties.

They do not reveal how the protected runtime implements them.

---

# 38. Final Position

VRP assumes that transport instability is normal enough to deserve explicit architectural treatment.

The protocol is therefore not judged solely by whether connectivity eventually returns.

It is judged by what remains correct while connectivity changes.

The evaluator should ask:

```text
WHAT SURVIVED?

WHAT WAS REJECTED?

WHAT REMAINED AUTHORITATIVE?

WHAT HISTORY REMAINED CANONICAL?

WHAT EVIDENCE SUPPORTS THE VERDICT?
```

Those questions define the public threat surface.

The internal mechanisms answering them remain protected.

---

# Session != Transport

# Reachability != Authority

# Replay != Progress

# Continuity First

---

## Veil Routing Protocol

Public threat-model document.

Protected runtime implementation remains private.

Security and continuity claims should remain bounded by reproducible scenarios, observable behavior, explicit failure conditions, and verifiable evidence.
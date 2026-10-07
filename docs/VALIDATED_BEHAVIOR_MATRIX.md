# Veil Routing Protocol — Validated Behavior Matrix

## Public Engineering Evidence Map

Veil Routing Protocol (VRP) is a continuity-first networking architecture built around a fundamental separation:

**Session != Transport**

This document provides a public map between:

- failure conditions;
- expected continuity properties;
- observable behavior;
- validation evidence;
- engineering verdicts.

It intentionally does not describe the protected mechanisms used internally to produce these behaviors.

This is not a source-code disclosure document.

It is an engineering evidence map.

---

# 1. Why This Matrix Exists

A protocol should not be judged only by architecture diagrams or design claims.

For each important property, an evaluator should be able to ask:

```text
WHAT WAS THE CLAIM?

WHAT FAILURE WAS APPLIED?

WHAT PROPERTY WAS EXPECTED?

WHAT WAS OBSERVED?

WHAT EVIDENCE EXISTS?

WHAT WAS THE VERDICT?
```

The purpose of this document is to connect those questions.

---

# 2. Reading the Matrix

The matrix uses five concepts.

## Scenario

The failure or adversarial condition being introduced.

## Property

The continuity invariant expected to survive.

## Observable Behavior

The externally relevant behavior that can be inspected without exposing protected runtime internals.

## Evidence

The validation artifact or test surface associated with the scenario.

## Verdict

The observed engineering outcome for the documented validation run.

A PASS means only that the defined property survived the documented test conditions.

It is not a universal security or production guarantee.

---

# 3. High-Level Validation Matrix

| Scenario | Property Under Test | Expected Behavior | Observed Validation Direction |
|---|---|---|---|
| Transport interruption | Session continuity | Transport loss does not automatically destroy logical session identity | Preserved in documented validation |
| Path replacement | Session != Transport | Replacement carrier does not automatically redefine the session | Preserved in documented validation |
| Wi-Fi to alternate transport | Continuity across migration | Logical continuity survives carrier transition where recovery is admissible | Preserved in documented validation |
| Temporary network outage | Recovery | Runtime contains interruption and evaluates recovery rather than silently manufacturing new identity | Preserved in documented validation |
| Duplicate delivery | Duplicate containment | Duplicate observation does not become duplicate canonical progress | Rejected / contained in documented validation |
| Replay attempt | Replay rejection | Previously accepted input does not become new progress | Rejected in documented validation |
| Replay flood | Bounded replay containment | Repeated replay attempts do not become canonical execution | Contained in documented validation |
| Stale state return | Authority monotonicity | Historical state does not regain authority merely because it returns | Rejected in documented validation |
| Authority rollback attempt | Authority monotonicity | Older authority cannot silently replace newer authority | Rejected in documented validation |
| Conflicting recovery state | Canonical continuity | Contradictory recovery information does not silently redefine accepted state | Contained / rejected in documented validation |
| Reordered delivery | Causal integrity | Delivery disorder does not automatically rewrite canonical state | Preserved in documented validation |
| Recovery race | Recovery correctness | Concurrent recovery conditions do not silently produce conflicting authority | Preserved / contained in documented validation |
| Canonical history rewrite attempt | Historical integrity | Previously accepted history cannot be silently replaced | Rejected in documented validation |
| Repeated transport migration | Identity continuity | Repeated path changes do not automatically create new logical session identities | Preserved in documented validation |
| Runtime restart / recovery | Continuity recovery | Restart conditions do not automatically authorize stale historical state | Preserved in documented validation |
| Runtime pressure | Bounded behavior | Jitter, reordering, congestion, and latency pressure do not silently invalidate continuity invariants | Preserved / contained in documented validation |
| Repeated deterministic execution | Determinism | Equivalent test conditions should not produce unexplained divergent verdicts | Preserved in documented validation |
| Evidence tampering | Evidence integrity | Modified evidence must not silently verify as original evidence | Detected / rejected in documented validation |

---

# 4. Transport Interruption

## Failure

The active transport becomes unavailable.

Conceptually:

```text
SESSION ACTIVE
      |
TRANSPORT A
      |
      X
TRANSPORT LOST
```

## Property

Transport lifetime must not automatically define logical session lifetime.

## Expected Behavior

```text
TRANSPORT LOST
      !=
SESSION IDENTITY AUTOMATICALLY DESTROYED
```

The runtime must treat the interruption as a continuity event.

## Public Evaluation Question

> When the active transport disappears, what happens to the logical session identity?

## Validation Direction

Documented VRP validation has exercised transport-loss and recovery scenarios with continuity preservation as the target invariant.

---

# 5. Physical Network Loss and Recovery

A public live validation has included physical network interruption rather than only simulated logical failure.

The externally visible sequence included:

```text
TRANSPORT_REACHABILITY=LOST

...

TRANSPORT_REACHABILITY=RECOVERED
```

The important property is not merely that network reachability returned.

The relevant question is whether the continuity model remained valid across the interruption.

This distinction is central:

```text
NETWORK RECOVERED
       !=
CONTINUITY PROVEN
```

Both transport observation and runtime evidence matter.

---

# 6. Path Migration

## Failure Condition

The current carrier becomes unavailable or unsuitable and another carrier becomes available.

```text
SESSION
   |
TRANSPORT A
   |
   X
   |
TRANSPORT B
```

## Property

**Session != Transport**

## Expected Behavior

Transport replacement must not automatically redefine logical session identity.

## Public Evaluation Question

> Can the carrier change while the logical continuity identity remains consistent?

## Validation Direction

Transport migration has been exercised repeatedly in VRP validation work.

Documented validation has reported continuity preservation across migration scenarios.

---

# 7. Repeated Transport Migration

A single successful migration does not demonstrate behavior under repeated instability.

A stronger scenario is:

```text
A -> B -> A -> C -> B -> A -> ...
```

The relevant property is:

```text
MANY TRANSPORT CHANGES
          !=
MANY LOGICAL SESSION IDENTITIES
```

Documented stress validation has included repeated transport migration while observing whether session identity remains preserved.

---

# 8. Duplicate Delivery

Distributed networks may duplicate information.

Therefore VRP cannot assume:

```text
ONE NETWORK DELIVERY
        =
ONE OBSERVATION FOREVER
```

## Scenario

```text
EVENT X

EVENT X
```

## Property

Duplicate observation must not silently become duplicate canonical execution.

## Expected Behavior

```text
DUPLICATE DELIVERY
       !=
DUPLICATE AUTHORITY
```

## Validation Direction

Duplicate-delivery scenarios have been exercised as part of the recovery and continuity validation surface.

The expected result is containment rather than creation of new canonical progress.

---

# 9. Replay

A replay is particularly important because historical information may still appear structurally legitimate.

Consider:

```text
T1:

EVENT X -> ACCEPTED

T2:

EVENT X -> OBSERVED AGAIN
```

The second observation must not automatically become a new state transition.

## Property

```text
REPLAY != PROGRESS
```

## Public Evaluation Question

> Can previously accepted information become new canonical progress merely by being presented again?

## Validation Direction

Documented VRP validation has exercised replay rejection under both isolated and repeated replay conditions.

---

# 10. Replay Flood

A single rejected replay is useful evidence.

Repeated rejection under pressure is a stronger condition.

The public scenario is:

```text
VALID HISTORY
     |
     v
REPLAY
REPLAY
REPLAY
REPLAY
REPLAY
...
```

The property under test is:

```text
REPEATED INVALID INPUT
          !=
CANONICAL PROGRESS
```

Documented VRP validation has included replay-flood testing with thousands of replay attempts rejected.

This result should be interpreted within the conditions of the documented test.

It is not a claim that all possible denial-of-service conditions have been solved.

---

# 11. Stale State

Historical state may return after newer state has already been accepted.

For example:

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

## Property

Historical validity must not imply current authority.

```text
ONCE VALID
    !=
AUTHORITATIVE NOW
```

## Expected Behavior

State A must not silently replace C merely because A becomes reachable again.

## Validation Direction

Stale-state rejection is part of the documented VRP recovery validation surface.

---

# 12. Authority Rollback

Authority rollback is a stronger form of stale-state failure.

Conceptually:

```text
AUTHORITY EPOCH N
       |
       v
AUTHORITY EPOCH N+1

later:

AUTHORITY EPOCH N RETURNS
```

The required property is monotonicity:

```text
OLDER AUTHORITY
       !=
CURRENT AUTHORITY
```

Documented VRP validation has exercised stale and rollback conditions and reported rejection of older authority attempting to reassert itself.

The internal mechanism used to establish authority remains protected.

---

# 13. Conflicting State

Recovery may encounter more than one apparently plausible state.

For example:

```text
             /-> STATE B
STATE A ----|
             \-> STATE C
```

The existence of multiple reachable candidates must not automatically create multiple canonical histories.

## Property

Canonical continuity must remain bounded.

## Public Evaluation Question

> Can conflicting recovery information silently produce contradictory authority?

## Validation Direction

VRP validation has exercised conflicting-state and recovery-race conditions with containment as a required property.

---

# 14. Reordered Delivery

Networks do not guarantee that every relevant event will always be observed in ideal logical order.

Conceptually:

```text
LOGICAL:

A -> B -> C

DELIVERY:

A -> C -> B
```

## Property

Delivery order alone must not be allowed to rewrite causal history incorrectly.

## Validation Direction

Reordered-delivery scenarios are part of VRP causality and recovery validation.

The internal causality mechanisms remain outside the public disclosure boundary.

---

# 15. Recovery Races

Recovery may itself occur concurrently with additional failures or competing recovery conditions.

Example:

```text
TRANSPORT FAILURE
       |
RECOVERY STARTS
       |
       +---- candidate A
       |
       +---- candidate B
       |
ANOTHER EVENT OCCURS
```

The required property is not:

```text
FIRST RESPONSE WINS
```

The required property is preservation of the declared continuity and authority invariants.

Documented VRP engineering work includes recovery-race validation.

---

# 16. Canonical History Rewrite

A runtime can restore availability while still producing an incorrect result.

Consider:

```text
ACCEPTED:

A -> B -> C
```

After recovery:

```text
A -> X -> Y
```

If previously accepted canonical history has silently been replaced, connectivity may be restored while continuity correctness has failed.

Therefore:

```text
RECOVERY
   !=
PERMISSION TO REWRITE HISTORY
```

Documented VRP validation has included canonical history rewrite attempts with rejection as the expected result.

---

# 17. Runtime Restart Conditions

Restart and recovery create another important boundary.

A restarted runtime must not assume that any historical state presented after restart is automatically current.

The relevant question is:

> Can stale or contradictory state regain authority across a restart boundary?

Documented VRP validation has included restart and authority-recovery scenarios.

---

# 18. Runtime Pressure

Correctness only under perfect timing is not sufficient.

Validation has also considered conditions such as:

```text
JITTER

REORDERING

CONGESTION

LATENCY PRESSURE

REPEATED RECOVERY
```

The required property is not zero performance impact.

The required property is that pressure must not silently transform invalid state into valid authoritative progress.

Documented validation has reported preservation or containment under tested pressure conditions.

---

# 19. Deterministic Execution

Recovery behavior must also be reproducible.

A useful model is:

```text
SAME INPUT CLASS
      |
      +---- RUN 1
      |
      +---- RUN 2
      |
      +---- RUN 3
      |
      +---- ...
```

The engineering question is:

> Do equivalent executions produce unexplained divergence?

VRP validation has included repeated deterministic execution and concurrency-oriented testing.

A deterministic result is particularly important for:

- debugging;
- incident analysis;
- evidence verification;
- regression testing;
- recovery analysis.

---

# 20. Evidence Integrity

Runtime behavior is only one part of validation.

The evidence describing that behavior must also be challengeable.

Conceptually:

```text
EXECUTION
    |
    v
EVIDENCE
    |
    X
MODIFICATION
    |
    v
VERIFICATION
```

A modified artifact should not silently verify as if it were the original evidence.

Documented VRP validation has included evidence-tampering scenarios in which modifications were expected to be detected or rejected.

The protected implementation of evidence security mechanisms is not disclosed here.

---

# 21. Independent Verification

The strongest useful evidence is not:

```text
VRP SAYS VRP PASSED
```

A stronger model is:

```text
VRP EXECUTION
      |
      v
EVIDENCE ARTIFACT
      |
      v
SEPARATE VERIFICATION
      |
      v
VERDICT
```

VRP engineering has explicitly explored independent verification of generated evidence.

This separation reduces dependence on the runtime's own textual claims.

---

# 22. Live Continuity Validation

VRP has also been exercised through live continuity demonstrations.

These are useful because they combine:

```text
REAL NETWORK EVENT

+

RUNTIME OBSERVATION

+

VALIDATION SCENARIO

+

EVIDENCE VERIFICATION
```

A live demonstration is not stronger merely because it is live.

Its value comes from making the failure visible while still producing evidence that can be inspected afterward.

---

# 23. Examples of Documented Engineering Outcomes

Across VRP validation work, documented outcomes have included classes such as:

```text
CONTINUITY_PRESERVED

VALIDATION_PASSED

REPLAY_REJECTED

REPLAY_FLOOD_CONTAINED

STALE_AUTHORITY_REJECTED

CANONICAL_HISTORY_REWRITE_REJECTED

RECOVERY_PRESERVED

EVIDENCE_VERIFIED
```

These verdicts should always be interpreted together with the scenario that produced them.

A verdict without its test conditions is incomplete evidence.

---

# 24. What This Matrix Does Not Prove

This document does not claim that VRP has proven:

- correctness under every possible network;
- correctness under every possible workload;
- resistance to every possible attack;
- unlimited scalability;
- universal production readiness;
- elimination of all transport failure;
- elimination of all distributed-systems failure;
- perfect availability;
- perfect security.

Those would exceed the evidence described here.

The correct interpretation is narrower:

> Defined VRP invariants have been exercised against documented classes of failure and adversarial conditions, with observable verdicts recorded for those tests.

---

# 25. Why Negative Tests Matter

A validation suite should not contain only scenarios expected to succeed.

It must also ask whether prohibited transitions are actually rejected.

For VRP, this means testing both:

```text
VALID CONTINUITY
       |
       v
SHOULD PROCEED
```

and:

```text
INVALID / STALE / REPLAYED /
CONFLICTING CONDITION
       |
       v
SHOULD NOT BECOME
CANONICAL PROGRESS
```

Correct rejection is itself an important result.

---

# 26. A Failure Is Useful Evidence

If a future validation scenario breaks an invariant, the correct engineering response is not to hide the result.

The useful cycle is:

```text
FAIL
 |
 v
REPRODUCE
 |
 v
ISOLATE
 |
 v
CORRECT
 |
 v
REGRESSION TEST
 |
 v
REVALIDATE
```

That process is part of protocol engineering.

The purpose of validation is not to maintain a perfect-looking record.

It is to make incorrect behavior discoverable.

---

# 27. Evidence Hierarchy

Not all evidence has equal strength.

A useful conceptual hierarchy is:

```text
CLAIM

  <

SCREENSHOT

  <

RECORDED EXECUTION

  <

REPRODUCIBLE TEST

  <

REPRODUCIBLE TEST + ARTIFACTS

  <

REPRODUCIBLE TEST + ARTIFACTS
+ INDEPENDENT VERIFICATION
```

VRP engineering aims toward the stronger end of this hierarchy where practical.

---

# 28. What an Evaluator Should Do

A serious evaluator should not simply read this matrix and accept it.

Choose a property.

Then attempt to invalidate it.

For example:

```text
1. Establish a session.

2. Remove the transport.

3. Introduce another path.

4. Return stale information.

5. Replay previous information.

6. Duplicate delivery.

7. Interrupt recovery.

8. Repeat the scenario.

9. Inspect the evidence.

10. Compare the verdict.
```

If the invariant breaks, the result should be visible.

That is the point.

---

# 29. Pilot Use

This matrix can also serve as the starting point for a pilot.

A participant can select relevant rows and convert them into an environment-specific test plan.

For example:

| Participant Concern | VRP Scenario |
|---|---|
| Mobile handover | Transport migration |
| Intermittent connectivity | Temporary outage |
| Old endpoint returning | Stale-state return |
| Duplicate upstream delivery | Duplicate containment |
| Delayed historical traffic | Replay / stale state |
| Recovery during another failure | Recovery race |
| Auditability | Evidence verification |

The participant does not need to evaluate every VRP property.

The pilot should focus on properties that matter to the actual infrastructure.

---

# 30. The Engineering Standard

The intended VRP standard is not:

> Believe the architecture because the documentation sounds convincing.

It is:

```text
DECLARE THE INVARIANT

APPLY THE FAILURE

OBSERVE THE SYSTEM

CAPTURE THE EVIDENCE

VERIFY THE RESULT

REPEAT THE TEST
```

That is the public validation philosophy.

---

# 31. Summary

The central VRP architectural claim remains:

# Session != Transport

But that statement is useful only if its consequences can be tested.

Therefore VRP validation asks whether continuity properties survive conditions such as:

```text
TRANSPORT LOSS

PATH MIGRATION

REPLAY

STALE STATE

DUPLICATION

REORDERING

RECOVERY RACES

AUTHORITY ROLLBACK

HISTORY REWRITE

RUNTIME PRESSURE

EVIDENCE TAMPERING
```

The protected runtime implementation remains private.

The observable claims remain challengeable.

That separation is intentional.

---

## Veil Routing Protocol

**Continuity First**

Public validation and behavior document.

Protected runtime implementation remains private.

A PASS describes a tested scenario.

It is evidence for that scenario — not a universal guarantee.
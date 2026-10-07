# Veil Routing Protocol — Failure Lab

## We Test the Failure, Not Only the Happy Path

Veil Routing Protocol (VRP) is a continuity-first networking architecture.

Its central architectural separation is:

# Session != Transport

That statement becomes meaningful only when the transport actually fails.

For this reason, VRP engineering does not treat network failure as an exceptional condition that should be avoided during testing.

Failure is deliberately introduced.

Transport is interrupted.

Paths are changed.

Historical input is replayed.

Delivery is duplicated.

State is delayed.

Recovery is interrupted.

Migration is repeated.

Evidence is inspected.

The objective is simple:

> Do the declared continuity invariants survive when the environment stops behaving nicely?

This document describes the public VRP failure-testing philosophy and test surface.

It intentionally does not disclose protected runtime algorithms, authority-selection logic, recovery internals, cryptographic implementation details, security-sensitive thresholds, or proprietary defense mechanisms.

---

# 1. Why a Failure Lab Exists

A networking architecture can look correct under ideal conditions.

For example:

```text
STABLE NETWORK

LOW LATENCY

NO PACKET LOSS

NO PATH CHANGE

NO DUPLICATES

NO REPLAY

NO RECOVERY RACE
```

Under those conditions, many architectures appear reliable.

That is not the environment VRP is primarily interested in.

The interesting environment begins when assumptions fail.

```text
TRANSPORT DISAPPEARS

PATH CHANGES

CONNECTIVITY VANISHES

OLD STATE RETURNS

INPUT IS DUPLICATED

DELIVERY REORDERS

RECOVERY IS INTERRUPTED

FAILURES OVERLAP
```

The VRP Failure Lab exists to exercise those conditions deliberately.

---

# 2. Failure Is an Input

Traditional testing often treats failure as something that unexpectedly interrupts the test.

VRP testing deliberately treats failure as part of the test.

Conceptually:

```text
ESTABLISH BASELINE
        |
        v
INTRODUCE FAILURE
        |
        v
OBSERVE RUNTIME
        |
        v
INSPECT INVARIANTS
        |
        v
CAPTURE EVIDENCE
        |
        v
VERIFY RESULT
```

A test is not interesting merely because the runtime remained alive.

The important question is whether the required properties remained correct.

---

# 3. The Lab Does Not Try to Make VRP Look Good

The objective is not:

```text
CREATE A DEMO
THAT ALWAYS PASSES
```

The objective is:

```text
CREATE CONDITIONS
THAT COULD MAKE
THE ARCHITECTURE FAIL
```

A useful validation environment should attempt to expose:

- incorrect assumptions;
- nondeterministic behavior;
- stale-state acceptance;
- duplicate execution;
- replay acceptance;
- recovery inconsistencies;
- authority rollback;
- historical divergence;
- unbounded behavior;
- evidence inconsistencies.

If a declared invariant breaks, the correct result is:

```text
FAIL
```

not a reinterpretation of the test.

---

# 4. Failure Lab Principle

The basic philosophy is:

```text
DO NOT PROTECT
THE TEST FROM FAILURE.

USE FAILURE
TO TEST THE SYSTEM.
```

---

# 5. Test Surface

Publicly discussable VRP failure scenarios include:

```text
PHYSICAL NETWORK INTERRUPTION

TRANSPORT LOSS

PATH MIGRATION

REPEATED PATH MIGRATION

TEMPORARY COMPLETE OUTAGE

NAT / NETWORK LOCATION CHANGE

JITTER

LATENCY PRESSURE

REORDERING

DUPLICATE DELIVERY

REPLAY

REPLAY FLOOD

STALE STATE RETURN

AUTHORITY ROLLBACK ATTEMPT

CONFLICTING RECOVERY STATE

RECOVERY RACE

FAILURE DURING RECOVERY

RUNTIME RESTART

CANONICAL HISTORY REWRITE ATTEMPT

CONCURRENT EXECUTION

EVIDENCE MODIFICATION
```

Different scenarios test different invariants.

No single scenario proves the entire architecture.

---

# 6. Physical Network Interruption

Simulation is useful.

Physical interruption is different.

A physical test may involve an actual network interface becoming unavailable.

Conceptually:

```text
NETWORK REACHABLE
       |
       X
PHYSICAL INTERRUPTION
       |
       v
NETWORK UNREACHABLE
       |
       v
NETWORK RETURNS
```

The first observation is straightforward:

```text
TRANSPORT_REACHABILITY=LOST
```

and later:

```text
TRANSPORT_REACHABILITY=RECOVERED
```

But those two observations alone do not prove continuity.

The lab must also ask what happened to the logical session and its invariants.

---

# 7. Transport Loss

The simplest continuity failure scenario is:

```text
SESSION ACTIVE
      |
TRANSPORT ACTIVE
      |
      X
TRANSPORT LOST
```

The test asks:

```text
WHAT DIED?

WHAT DID NOT DIE?

WHAT STATE REMAINED VALID?

WHAT MAY RECOVER?

WHAT MUST NOT RECOVER?
```

The expected behavior depends on the defined test contract.

Transport disappearance alone must not be silently interpreted as proof that every higher-level continuity property disappeared with it.

---

# 8. Path Migration

A stronger test introduces a replacement path.

```text
SESSION
   |
PATH A
   |
   X
   |
PATH B
```

The public invariant being challenged is:

# Session != Transport

The lab observes whether path replacement incorrectly becomes logical identity replacement.

---

# 9. Repeated Migration

One successful migration can hide accumulated state problems.

Therefore migration should also be repeated.

```text
A -> B -> A -> C -> B -> A -> D -> ...
```

The question becomes:

> Does the continuity model remain consistent after repeated transport changes?

Repeated migration can expose problems that a single transition does not.

---

# 10. Migration Storm

A more aggressive scenario repeatedly changes the transport environment.

Conceptually:

```text
MIGRATE

MIGRATE

MIGRATE

MIGRATE

MIGRATE

...
```

The purpose is not to demonstrate that transport never changes.

The purpose is exactly the opposite.

Change it repeatedly.

Then verify whether logical identity remains consistent under the tested conditions.

Documented VRP validation has included large repeated-migration scenarios.

---

# 11. Complete Temporary Outage

Another scenario removes usable connectivity completely.

```text
PATH A
  |
  X

PATH B
  |
  X

NO USABLE TRANSPORT
```

VRP cannot transmit through a network that does not exist.

The test therefore asks something more precise:

> What continuity state remains valid during the outage, and what happens when transport becomes available again?

The outage may last long enough to ensure the test is exercising recovery rather than a trivial momentary transition.

---

# 12. Outage and Return

A complete cycle may look like:

```text
CONNECTED
    |
    v
TRANSPORT LOSS
    |
    v
NO CONNECTIVITY
    |
    v
TRANSPORT AVAILABLE
    |
    v
RECOVERY
    |
    v
VERDICT
```

A successful result requires more than:

```text
CONNECTED AGAIN
```

It requires the invariant defined for the scenario to survive.

---

# 13. Jitter

Real networks do not provide perfectly stable timing.

A test can deliberately introduce timing variation.

```text
10 ms

80 ms

25 ms

140 ms

17 ms

95 ms
```

The relevant question is not whether latency remains constant.

It obviously does not.

The question is whether timing instability causes a correctness property to fail.

---

# 14. Latency Pressure

Latency can be increased enough to stress recovery timing assumptions.

```text
NORMAL
   |
   v
DELAY
   |
   v
MORE DELAY
   |
   v
RECOVERY CONDITIONS
```

A system that is correct only when events arrive quickly may contain hidden timing assumptions.

The lab attempts to expose them.

---

# 15. Reordered Delivery

The logical order may be:

```text
A -> B -> C -> D
```

while observation occurs as:

```text
A -> C -> B -> D
```

The test asks whether delivery disorder incorrectly becomes canonical causal disorder.

The internal causality mechanism remains protected.

The externally relevant property is testable.

---

# 16. Duplicate Delivery

The same logical input may be delivered more than once.

```text
EVENT X

EVENT X
```

The lab asks:

```text
DID WE OBSERVE X TWICE?
```

and separately:

```text
DID X BECOME
CANONICAL PROGRESS TWICE?
```

Those are not the same question.

The expected public invariant is:

```text
DUPLICATE DELIVERY
        !=
DUPLICATE AUTHORITY
```

---

# 17. Replay

Replay deliberately presents historical information again.

```text
EVENT X
  |
ACCEPTED

later:

EVENT X
  |
PRESENTED AGAIN
```

The lab does not merely check whether the input can physically arrive again.

It asks whether historical information incorrectly becomes new progress.

The public invariant is:

# Replay != Progress

---

# 18. Replay Flood

A stronger replay test repeats the condition at scale.

```text
REPLAY 0001

REPLAY 0002

REPLAY 0003

...

REPLAY N
```

Documented VRP validation has included replay-flood testing with thousands of attempts.

The purpose is to test containment under repetition.

It is not a universal claim of denial-of-service resistance.

---

# 19. Stale State Return

A recovery environment can cause old state to become visible again.

```text
STATE 1
   |
STATE 2
   |
STATE 3

CURRENT = STATE 3

failure occurs

STATE 1 RETURNS
```

The lab asks:

> Does historical availability incorrectly become current authority?

The required public distinction is:

```text
WAS VALID
    !=
IS AUTHORITATIVE NOW
```

---

# 20. Authority Rollback Attempt

A more explicit adversarial scenario attempts to move authority backward.

```text
EPOCH N
   |
   v
EPOCH N+1

then:

EPOCH N
ATTEMPTS TO RETURN
```

The test expects older authority not to silently replace newer accepted authority.

How that property is enforced internally is outside the public boundary.

---

# 21. Conflicting Recovery State

Recovery can be deliberately presented with conflicting possibilities.

```text
              /-> STATE B
STATE A -----|
              \-> STATE C
```

The lab asks whether conflicting information can silently create contradictory canonical authority.

A correct test must have an explicit expected result.

---

# 22. Recovery Race

Real recovery may involve multiple events occurring close together.

```text
FAILURE
   |
RECOVERY
   |
   +---- EVENT A
   |
   +---- EVENT B
   |
   +---- EVENT C
```

The lab attempts to make ordering assumptions uncomfortable.

The goal is to discover whether concurrency or timing can alter the correctness verdict unexpectedly.

---

# 23. Failure During Recovery

Recovery itself is not protected from failure.

A test may deliberately do this:

```text
FAILURE 1
    |
RECOVERY STARTS
    |
    X
FAILURE 2
    |
RECOVERY CONTINUES
```

Or:

```text
TRANSPORT A LOST

TRANSPORT B APPEARS

TRANSPORT B LOST

TRANSPORT C APPEARS
```

The architecture should be challenged while already under recovery pressure.

---

# 24. Runtime Restart

A restart creates another useful boundary.

```text
ACTIVE RUNTIME
      |
      X
RESTART
      |
      v
RECOVERY INPUT
```

Then historical, stale, or conflicting information can be introduced.

The question is:

> Does restart incorrectly make old state authoritative again?

---

# 25. Canonical History Rewrite Attempt

Suppose the accepted history is:

```text
A -> B -> C
```

The lab can attempt to produce:

```text
A -> X -> Y
```

as though it were the accepted continuation.

The public invariant is:

```text
RECOVERY
   !=
PERMISSION TO
REWRITE HISTORY
```

A successful defense means the prohibited rewrite does not become canonical under the tested conditions.

---

# 26. Concurrent Execution

Sequential tests are necessary but insufficient.

The lab should also create concurrent activity.

Conceptually:

```text
WORKER 1 ----\
WORKER 2 -----\
WORKER 3 ------> RUNTIME
WORKER 4 -----/
WORKER N ----/
```

Concurrency can expose:

- race conditions;
- hidden ordering dependencies;
- duplicate transitions;
- inconsistent state;
- nondeterministic verdicts.

The objective is not merely high throughput.

It is correctness under concurrency.

---

# 27. Race Detection

Where applicable, runtime testing can be combined with race-oriented tooling.

A functional PASS does not necessarily prove the absence of concurrency defects.

Therefore:

```text
FUNCTIONAL TESTING
       +
CONCURRENCY TESTING
       +
RACE DETECTION
```

provide different forms of evidence.

---

# 28. Randomized Testing

Deterministic scenarios are essential because they are reproducible.

Randomized scenarios are useful because they can explore combinations that were not manually selected.

A useful relationship is:

```text
DETERMINISTIC TESTS
        +
RANDOMIZED TESTS
        +
REPRODUCIBLE FAILURE CASES
```

If randomized testing discovers a defect, the valuable next step is to reduce it into a reproducible regression case.

---

# 29. Fuzzing

Boundary behavior can also be challenged with fuzzing.

The purpose is not:

```text
GENERATE RANDOM DATA
AND HOPE
```

The purpose is to search for inputs or sequences that violate explicit properties.

Examples of interesting outcomes include:

```text
PANIC

INVALID STATE TRANSITION

UNEXPECTED ACCEPTANCE

NONDETERMINISTIC RESULT

INVARIANT VIOLATION
```

A discovered case should become reproducible evidence.

---

# 30. Long-Running Validation

Some defects appear only after repetition.

Therefore another class of test is:

```text
RUN

VERIFY

REPEAT

VERIFY

REPEAT

VERIFY

...
```

Long-running validation can expose:

- accumulated state errors;
- resource growth;
- rare ordering conditions;
- recovery drift;
- state cleanup problems;
- intermittent nondeterminism.

A short PASS and a long-duration PASS provide different evidence.

---

# 31. Resource-Bounded Testing

Correctness is not useful if recovery behavior grows without control.

The lab therefore also cares about bounded behavior.

Questions include:

```text
WHAT HAPPENS AFTER
MANY RECOVERY CYCLES?

WHAT HAPPENS AFTER
MANY EVENTS?

WHAT HAPPENS UNDER
REPEATED INVALID INPUT?

DOES STATE GROW
WITHOUT AN EXPECTED BOUND?
```

Resource testing should always be associated with explicit workload conditions.

---

# 32. Determinism Testing

The same scenario can be executed repeatedly.

```text
SCENARIO X
   |
   +---- RUN 1
   |
   +---- RUN 2
   |
   +---- RUN 3
   |
   +---- ...
   |
   +---- RUN N
```

The lab then asks whether equivalent conditions produce unexplained divergence.

Determinism matters for:

```text
DEBUGGING

INCIDENT ANALYSIS

REGRESSION TESTING

EVIDENCE COMPARISON

RECOVERY REASONING
```

---

# 33. Evidence Tampering

The runtime is not the only test target.

Evidence itself can be attacked.

Conceptually:

```text
VALID EXECUTION
      |
      v
EVIDENCE
      |
      X
MUTATION
      |
      v
VERIFY AGAIN
```

The expected result is not:

```text
STILL PASS
```

if the evidence no longer represents the original verified artifact.

Documented VRP validation has included evidence-tampering scenarios.

---

# 34. Coordinated Evidence Modification

A stronger adversarial test does not modify only one obvious field.

Multiple related artifacts may be modified together.

The lab then asks whether the verification boundary can still distinguish the altered evidence from the original validated result.

The protected verification implementation is not described here.

The public requirement is simple:

```text
ALTERED EVIDENCE
      !=
ORIGINAL VERIFIED EVIDENCE
```

---

# 35. Independent Verification

A useful validation pipeline separates execution from verification.

```text
RUNTIME
   |
   v
EVIDENCE
   |
   v
SEPARATE VERIFICATION
   |
   v
VERDICT
```

This is stronger than relying only on:

```text
RUNTIME PRINTED "PASS"
```

Where supported by the validation scenario, VRP engineering uses independently inspectable evidence as part of the evaluation model.

---

# 36. Real Failure vs Synthetic Failure

Both matter.

Synthetic failure provides:

```text
CONTROL

REPEATABILITY

PRECISE TIMING

AUTOMATION
```

Real physical failure provides:

```text
REAL INTERFACE BEHAVIOR

REAL OS NETWORK TRANSITIONS

REAL OUTAGE TIMING

REAL RECOVERY CONDITIONS
```

The strongest validation program uses both where appropriate.

---

# 37. Live Failure Testing

A live test can intentionally expose the runtime to an observable network event.

For example:

```text
START OBSERVATION

VERIFY BASELINE

REMOVE NETWORK ACCESS

OBSERVE LOSS

RESTORE / CHANGE TRANSPORT

OBSERVE RECOVERY

VERIFY EVIDENCE
```

The important part is not the spectacle of disconnecting Wi-Fi.

The important part is what can be proven afterward.

---

# 38. PASS Must Mean Something

A useful PASS should correspond to an explicit property.

Bad:

```text
PASS
```

Better:

```text
SCENARIO:
TRANSPORT MIGRATION

EXPECTED:
SESSION IDENTITY PRESERVED

OBSERVED:
EXPECTED INVARIANT PRESERVED

VERDICT:
PASS
```

A verdict without context is weak evidence.

---

# 39. FAIL Must Mean Something Too

A useful failure report should identify what property broke.

For example:

```text
SCENARIO:
STALE STATE RETURN

EXPECTED:
STALE STATE REJECTED

OBSERVED:
STALE STATE ACCEPTED

VERDICT:
FAIL
```

That is valuable engineering evidence.

It provides a reproducible defect target.

---

# 40. A Failure Must Not Be Hidden

The correct engineering response to an invariant failure is:

```text
FAIL
   |
   v
CAPTURE
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
ADD REGRESSION TEST
   |
   v
REVALIDATE
```

Not:

```text
FAIL
   |
   v
CHANGE THE DEFINITION
OF SUCCESS
```

---

# 41. Failure Combinations Matter

Individual failure tests are useful.

Combined failures are more difficult.

For example:

```text
TRANSPORT LOSS
      +
REORDERING
      +
STALE STATE
```

or:

```text
MIGRATION
      +
DUPLICATE DELIVERY
      +
RECOVERY INTERRUPTION
```

or:

```text
RESTART
      +
REPLAY
      +
CONCURRENT RECOVERY
```

Real systems often fail through combinations rather than isolated textbook events.

---

# 42. Escalation Model

A useful validation program can increase difficulty progressively.

```text
LEVEL 1
BASELINE

LEVEL 2
SINGLE FAILURE

LEVEL 3
REPEATED FAILURE

LEVEL 4
CONCURRENT FAILURE

LEVEL 5
ADVERSARIAL INPUT

LEVEL 6
LONG-RUN PRESSURE

LEVEL 7
EVIDENCE ATTACK
```

Passing one level does not automatically imply passing the next.

---

# 43. Example Failure Campaign

A public evaluation campaign could look like:

```text
BASELINE
   |
   v
TRANSPORT LOSS
   |
   v
PATH MIGRATION
   |
   v
REPEATED MIGRATION
   |
   v
TEMPORARY OUTAGE
   |
   v
REPLAY
   |
   v
DUPLICATION
   |
   v
STALE STATE
   |
   v
REORDERING
   |
   v
RECOVERY RACE
   |
   v
RESTART
   |
   v
HISTORY REWRITE ATTEMPT
   |
   v
EVIDENCE VERIFICATION
```

Every stage should have an explicit expected invariant.

---

# 44. What the Failure Lab Does Not Prove

Even extensive testing does not prove that every possible failure has been discovered.

The Failure Lab does not establish:

```text
PERFECT SECURITY

ZERO DEFECTS

UNLIMITED SCALE

ALL NETWORKS SUPPORTED

ALL ATTACKS DEFEATED

ALL FUTURE CONDITIONS KNOWN

UNIVERSAL PRODUCTION READINESS
```

The correct statement is narrower:

> Defined invariants have been challenged under defined failure conditions and evaluated using observable evidence.

---

# 45. Why Repetition Matters

One successful run may be accidental.

Repeated runs increase confidence that the result is not a one-time scheduling coincidence.

Therefore:

```text
PASS ONCE
```

and:

```text
PASS REPEATEDLY
UNDER THE SAME
DEFINED CONDITIONS
```

are different evidence strengths.

---

# 46. Why Adversarial Testing Matters

The runtime should not receive only valid inputs.

A serious test environment also asks:

```text
WHAT IF THIS IS OLD?

WHAT IF THIS IS DUPLICATED?

WHAT IF THIS ARRIVES LATE?

WHAT IF THIS CONFLICTS?

WHAT IF RECOVERY IS INTERRUPTED?

WHAT IF THE SAME ATTEMPT
HAPPENS THOUSANDS OF TIMES?
```

The purpose is to find where the assumptions break.

---

# 47. Why External Evaluation Matters

An internal lab knows its own environment.

An external evaluator can introduce assumptions the development environment never anticipated.

For example:

```text
DIFFERENT NETWORK TOPOLOGY

DIFFERENT NAT BEHAVIOR

DIFFERENT APPLICATION TIMING

DIFFERENT FAILURE ORDERING

DIFFERENT SECURITY POLICY

DIFFERENT INFRASTRUCTURE
```

This is one reason controlled pilots are valuable.

---

# 48. The Pilot Is Another Failure Lab

A serious VRP pilot should not be:

```text
INSTALL

WATCH NORMAL TRAFFIC

DECLARE SUCCESS
```

It should be closer to:

```text
DEFINE PROPERTY

ESTABLISH BASELINE

BREAK SOMETHING

OBSERVE

VERIFY

BREAK SOMETHING ELSE

REPEAT
```

A pilot should challenge the architecture.

---

# 49. What the Evaluator Should Ask

For every scenario:

```text
WHAT FAILED?

WHAT PROPERTY WAS AT RISK?

WHAT SHOULD HAVE SURVIVED?

WHAT SHOULD HAVE BEEN REJECTED?

WHAT ACTUALLY HAPPENED?

WHAT EVIDENCE EXISTS?

CAN THE RESULT BE REPEATED?
```

Those questions matter more than a polished demonstration.

---

# 50. The VRP Failure Philosophy

The network is allowed to fail.

The transport is allowed to fail.

The path is allowed to change.

Inputs are allowed to arrive late.

Duplicates are allowed to appear.

Historical information is allowed to return.

Recovery is allowed to become difficult.

The architecture is then judged by what those failures are allowed to corrupt.

---

# 51. One Screen

```text
              VRP FAILURE LAB

                    |
                    v

             ESTABLISH STATE

                    |
                    v

              BREAK SOMETHING

                    |
        +-----------+-----------+
        |           |           |
        v           v           v
    TRANSPORT     REPLAY      STALE
      LOSS                     STATE
        |           |           |
        +-----------+-----------+
                    |
                    v
             OBSERVE RUNTIME
                    |
                    v
             CHECK INVARIANT
                    |
                    v
             CAPTURE EVIDENCE
                    |
                    v
            VERIFY THE RESULT
                    |
              +-----+-----+
              |           |
              v           v
             PASS        FAIL
                          |
                          v
                     INVESTIGATE
```

---

# 52. Final Position

VRP is not being developed around the assumption that networks behave perfectly.

It is being developed around the opposite assumption:

```text
TRANSPORT WILL FAIL.

PATHS WILL CHANGE.

RECOVERY WILL BE MESSY.

OLD INFORMATION WILL RETURN.

DELIVERY WILL NOT ALWAYS
BE CLEAN OR ORDERED.
```

The engineering task is to determine which continuity properties can remain correct anyway.

That is why failure is not hidden from VRP testing.

Failure is the test.

---

# Session != Transport

# Reachability != Authority

# Replay != Progress

# Availability != Correctness

# Failure Is the Test

# Continuity First

---

## Veil Routing Protocol

Public failure-validation document.

Protected runtime implementation remains private.

The scenarios described here expose the classes of conditions used to challenge VRP's public invariants.

They do not disclose the protected mechanisms used internally to preserve or reject state.
# Veil Routing Protocol — Pilot Evaluation Model

## Public Pilot Document

Veil Routing Protocol (VRP) is a continuity-first networking architecture built around a fundamental principle:

**Session != Transport**

A VRP pilot is not intended to be a conventional product demonstration.

It is a controlled engineering evaluation designed to answer a more important question:

> Does the architecture preserve its declared continuity properties when subjected to real infrastructure failures?

This document describes the public pilot model.

It does not disclose protected runtime implementation details, private algorithms, internal authority mechanisms, proprietary recovery logic, cryptographic internals, or security-sensitive policy.

---

# 1. Purpose of a Pilot

The purpose of a VRP pilot is not to demonstrate that software can run under ideal conditions.

The purpose is to challenge the architecture.

A useful pilot should deliberately introduce conditions such as:

- transport interruption;
- path replacement;
- connectivity loss;
- connectivity recovery;
- duplicate delivery;
- reordered delivery;
- stale state;
- replayed state;
- repeated migration;
- recovery interruption;
- conflicting recovery conditions.

The evaluation then asks whether the declared invariant survived.

The fundamental model is:

```text
REAL ENVIRONMENT
      |
      v
FAILURE CONDITION
      |
      v
VRP RUNTIME
      |
      v
OBSERVABLE BEHAVIOR
      |
      v
EVIDENCE
      |
      v
PASS / FAIL
```

---

# 2. A Pilot Is an Engineering Test

VRP pilot participation should not be interpreted as:

```text
WATCH A DEMO

BELIEVE A PRESENTATION

TRUST A BENCHMARK SCREENSHOT

ACCEPT A MARKETING CLAIM
```

The preferred model is:

```text
DEFINE THE PROPERTY

DEFINE THE FAILURE

RUN THE SCENARIO

OBSERVE THE SYSTEM

COLLECT THE EVIDENCE

VERIFY THE RESULT
```

If the expected invariant does not survive, the scenario fails.

That is a valid engineering result.

---

# 3. Pilot Question

The central pilot question is:

> Can logical continuity remain correct while the transport carrying it changes or fails?

This can be decomposed into narrower questions.

For example:

```text
Did session identity survive?

Did transport failure incorrectly redefine session identity?

Did stale state regain authority?

Did replay become new progress?

Did duplicate delivery become duplicate canonical execution?

Did recovery preserve accepted history?

Did equivalent execution produce deterministic results?

Did failure remain contained?
```

A pilot should select the questions relevant to the participant's infrastructure.

---

# 4. Pilot Boundary

Every evaluation should begin by defining a boundary.

Conceptually:

```text
+------------------------------------------+
|       PARTICIPANT INFRASTRUCTURE         |
|                                          |
|   application / service / test system    |
|                    |                     |
+--------------------|---------------------+
                     |
              agreed boundary
                     |
+--------------------v---------------------+
|           VRP EVALUATION SURFACE         |
|                                          |
|   integration                            |
|   continuity execution                   |
|   observation                            |
|   evidence                               |
+--------------------|---------------------+
                     |
                     v
              PILOT VERDICT
```

The exact boundary depends on the evaluation.

VRP should not require unrestricted access to unrelated organizational infrastructure.

---

# 5. Pilot Inputs

A pilot can begin with a small set of explicit inputs.

For example:

```text
TARGET WORKLOAD

EXPECTED CONTINUITY PROPERTY

AVAILABLE TRANSPORTS

FAILURE CONDITIONS

OBSERVATION POINTS

PASS CRITERIA

FAIL CRITERIA
```

This prevents the pilot from becoming an undefined demonstration where success means only that something appeared to work.

---

# 6. Example Evaluation

A simple transport migration evaluation could be defined as follows.

### Initial Condition

```text
SESSION ACTIVE

TRANSPORT A ACTIVE

APPLICATION TRAFFIC ACTIVE
```

### Failure

```text
TRANSPORT A REMOVED
```

### Recovery Condition

```text
TRANSPORT B AVAILABLE
```

### Additional Challenge

```text
OLD / DUPLICATE / DELAYED INFORMATION
MAY APPEAR DURING RECOVERY
```

### Expected Property

```text
SESSION IDENTITY REMAINS CONSISTENT

INVALID HISTORICAL STATE DOES NOT
BECOME NEW AUTHORITATIVE PROGRESS
```

### Verdict

```text
PASS
```

or:

```text
FAIL
```

The exact implementation mechanism used internally to preserve the property remains part of the protected runtime.

---

# 7. Pilot Scenarios

A pilot does not need to execute every possible VRP validation scenario.

The participant and VRP can select scenarios relevant to the environment.

Publicly discussable scenario classes include:

## Transport Loss

```text
ACTIVE
  |
  X
TRANSPORT LOST
```

Question:

> What happens to logical continuity?

---

## Transport Migration

```text
TRANSPORT A
     |
     X
     |
TRANSPORT B
```

Question:

> Does transport replacement incorrectly redefine the session?

---

## Temporary Outage

```text
CONNECTED
    |
    X
OFFLINE
    |
    |
RECOVERY
    |
CONNECTED
```

Question:

> Does recovery preserve the required continuity state?

---

## Duplicate Delivery

```text
EVENT X
EVENT X
```

Question:

> Does duplicate observation become duplicate authoritative execution?

---

## Replay

```text
EVENT X accepted at T1

EVENT X appears again at T2
```

Question:

> Is historical input incorrectly interpreted as new progress?

---

## Stale State Return

```text
STATE A
  |
STATE B
  |
STATE C

later:

STATE A RETURNS
```

Question:

> Can historical state regain authority merely because it is available?

---

## Reordering

```text
EXPECTED:

A -> B -> C

OBSERVED DELIVERY:

A -> C -> B
```

Question:

> Does delivery order corrupt canonical continuity?

---

## Repeated Migration

```text
A -> B -> A -> C -> B -> ...
```

Question:

> Does continuity remain bounded across repeated transport changes?

---

## Recovery Interruption

```text
FAILURE
   |
RECOVERY STARTS
   |
   X
ANOTHER FAILURE
```

Question:

> Does interrupted recovery produce invalid authoritative state?

---

# 8. PASS Must Mean Something

A pilot should define PASS before execution.

A result should not become PASS simply because:

```text
the process remained alive

the application eventually reconnected

traffic resumed

the terminal showed no panic
```

Those observations may be useful.

They are not sufficient by themselves.

A meaningful PASS should correspond to the declared invariant.

For example:

```text
PASS:

transport changed

AND

session identity remained consistent

AND

prohibited stale/replayed state was not
accepted as new canonical progress

AND

the expected evidence was produced
```

---

# 9. FAIL Must Also Mean Something

Failure criteria should also be explicit.

Examples may include:

```text
SESSION IDENTITY UNEXPECTEDLY CHANGED

STALE STATE BECAME AUTHORITATIVE

REPLAY BECAME NEW PROGRESS

DUPLICATE DELIVERY CREATED DUPLICATE
CANONICAL EXECUTION

RECOVERY REWROTE ACCEPTED HISTORY

REPEATED EXECUTION PRODUCED
UNEXPLAINED DIVERGENCE

EXPECTED EVIDENCE COULD NOT VERIFY
THE CLAIMED RESULT
```

A pilot with no defined failure condition is not a serious validation exercise.

---

# 10. Evidence

The preferred pilot model is evidence-oriented.

Conceptually:

```text
SCENARIO
   |
   v
OBSERVATION
   |
   v
EVIDENCE
   |
   v
VERIFICATION
   |
   v
VERDICT
```

Evidence may depend on the selected scenario and integration boundary.

The important property is that the result should be explainable and reproducible.

---

# 11. Evidence Is Part of the Deliverable

A technically useful pilot should leave behind more than:

```text
"It worked."
```

The participant should be able to understand:

```text
WHAT WAS TESTED

WHAT FAILURE WAS APPLIED

WHAT PROPERTY WAS EXPECTED

WHAT WAS OBSERVED

WHAT VERDICT WAS PRODUCED
```

Where appropriate, evidence should allow the result to be checked independently of the live demonstration.

---

# 12. Protected Runtime Remains Protected

A pilot is designed to expose behavior, not unrestricted implementation internals.

Participation does not automatically provide access to:

- private source repositories;
- proprietary runtime algorithms;
- internal authority mechanisms;
- private recovery algorithms;
- defense internals;
- security-sensitive thresholds;
- cryptographic implementation details;
- protected research material.

The pilot evaluates the agreed external contract.

---

# 13. This Is Not "Trust the Binary"

A protected implementation should not reduce evaluation to:

> Run this binary and trust whatever it says.

The intended model is stronger.

```text
VRP CLAIM
    |
    v
EXTERNAL FAILURE
    |
    v
OBSERVABLE CONSEQUENCE
    |
    v
EVIDENCE
    |
    v
INDEPENDENT EVALUATION
```

The participant should challenge externally observable claims.

The protected implementation remains private.

Both conditions can exist simultaneously.

---

# 14. Security Review Is Expected

A pilot does not bypass normal organizational security requirements.

A participant may require:

- architecture review;
- deployment review;
- network review;
- privilege review;
- data-flow review;
- isolation requirements;
- rollback procedures;
- test-environment restrictions.

Those requirements should be defined before deployment.

VRP should operate within the authorized evaluation boundary.

---

# 15. Pilot Isolation

Early evaluation does not require immediate production deployment.

A pilot may be conducted in:

```text
LAB

STAGING

TEST NETWORK

ISOLATED VM ENVIRONMENT

CONTROLLED APPLICATION ENVIRONMENT

DEDICATED INFRASTRUCTURE
```

The appropriate environment depends on the participant's risk model.

A controlled failure environment is often preferable because the objective is to deliberately break assumptions.

---

# 16. Deployment Should Be Reversible

The pilot boundary should define:

```text
INSTALL

START

OBSERVE

TEST

STOP

REMOVE
```

An evaluator should understand what was introduced into the environment and how it is removed after evaluation.

VRP does not require covert persistence for a legitimate pilot.

---

# 17. Pilot Does Not Equal Production Approval

A successful pilot demonstrates only what was actually tested.

It does not automatically prove:

```text
ALL POSSIBLE FAILURE MODES

ALL POSSIBLE NETWORKS

ALL POSSIBLE APPLICATIONS

ALL POSSIBLE SECURITY PROPERTIES

UNLIMITED SCALE

PRODUCTION READINESS FOR EVERY ENVIRONMENT
```

Claims should remain bounded by evidence.

This is important.

VRP should not turn a successful experiment into a universal guarantee.

---

# 18. Reproducibility

Where practical, a pilot scenario should be repeatable.

A strong result looks like:

```text
RUN 1 -> PASS

RUN 2 -> PASS

RUN 3 -> PASS

...

REPEATED RUN -> SAME INVARIANT
```

If equivalent conditions produce different outcomes, that difference deserves investigation.

Determinism and reproducibility are therefore important evaluation properties.

---

# 19. Adversarial Evaluation Is Welcome

A technically serious pilot participant should not be expected to behave like a friendly demo audience.

The participant should attempt to break the declared boundary.

Examples:

```text
REMOVE THE NETWORK

RESTORE IT DIFFERENTLY

REORDER INPUT

DUPLICATE INPUT

RETURN OLD STATE

REPEAT MIGRATION

INTERRUPT RECOVERY

REPEAT THE TEST
```

A protocol architecture becomes more credible when its claims survive hostile testing.

And when they do not survive, the failure provides useful engineering information.

---

# 20. Why Real Infrastructure Matters

Laboratory validation is necessary.

It is not sufficient to represent every environment.

Real systems introduce conditions such as:

- NAT behavior;
- CGNAT behavior;
- real interface transitions;
- carrier-specific behavior;
- enterprise routing;
- firewall policy;
- variable latency;
- unexpected packet ordering;
- application-specific timing;
- infrastructure-specific recovery behavior.

A real pilot can therefore expose assumptions that controlled validation may miss.

---

# 21. Why Earlier Evaluation Can Be More Valuable

There is a specific engineering reason for qualified organizations to evaluate VRP before every integration boundary becomes permanently frozen.

Early participants can expose real constraints while those constraints can still influence the external architecture.

Conceptually:

```text
EARLY PILOT

REAL INFRASTRUCTURE
        |
        v
DISCOVERED CONSTRAINT
        |
        v
INTEGRATION FEEDBACK
        |
        v
BOUNDARY IMPROVEMENT
```

Later evaluation may instead look more like:

```text
FROZEN BOUNDARY
      |
      v
INTEGRATE AS-IS
```

Neither model is inherently wrong.

But they provide different opportunities.

An early qualified participant may have more influence on integration requirements because real operational feedback arrives while those boundaries are still evolving.

---

# 22. This Is Not Artificial Urgency

The reason to evaluate earlier should not be:

```text
BUY NOW

LIMITED-TIME MARKETING

FEAR OF MISSING OUT
```

The reason is architectural.

A protocol/runtime becomes harder to reshape after interfaces, assumptions, compatibility commitments, and deployment contracts stabilize.

Therefore the relevant question for a potential participant is:

> Do we have a continuity problem important enough that we want our real infrastructure constraints represented during evaluation?

If the answer is no, waiting may be entirely reasonable.

If the answer is yes, earlier technical evaluation can produce more useful feedback.

---

# 23. Suitable Pilot Participants

VRP is unlikely to be useful to every organization.

A relevant participant is more likely to have systems where transport instability has meaningful consequences.

Examples may include environments involving:

- mobile connectivity;
- roaming;
- distributed systems;
- edge systems;
- intermittent connectivity;
- multiple network paths;
- recovery-sensitive workloads;
- stateful long-lived sessions;
- infrastructure where reconnecting is not equivalent to recovering correctly.

The pilot should begin from a real problem.

Not from the desire to deploy a new protocol for its own sake.

---

# 24. What VRP Needs From a Pilot Participant

A useful evaluation generally requires:

```text
A REAL USE CASE

A DEFINED TEST ENVIRONMENT

AN AUTHORIZED TECHNICAL CONTACT

AGREED FAILURE SCENARIOS

OBSERVATION ACCESS

CLEAR SUCCESS / FAILURE CRITERIA
```

The exact requirements depend on the integration.

The goal is to minimize unnecessary complexity.

---

# 25. What a Participant Should Expect From VRP

At the public evaluation level, a participant should expect clarity around:

```text
ARCHITECTURAL BOUNDARY

TEST OBJECTIVE

DEPLOYMENT SCOPE

FAILURE SCENARIO

EXPECTED INVARIANT

OBSERVABLE RESULT

EVIDENCE

VERDICT
```

The participant should not be asked to accept unexplained success claims.

---

# 26. Pilot Flow

A simplified evaluation lifecycle can look like:

```text
1. QUALIFY USE CASE

          |

2. DEFINE BOUNDARY

          |

3. SELECT INVARIANTS

          |

4. DEFINE FAILURE SCENARIOS

          |

5. DEFINE PASS / FAIL

          |

6. DEPLOY CONTROLLED EVALUATION

          |

7. EXECUTE BASELINE

          |

8. INJECT FAILURE

          |

9. OBSERVE RECOVERY

          |

10. COLLECT EVIDENCE

          |

11. VERIFY RESULT

          |

12. DOCUMENT FINDINGS
```

This is intentionally closer to an engineering experiment than a sales demonstration.

---

# 27. Example Pilot Matrix

A pilot might use a matrix such as:

| Scenario | Expected Property | Result |
|---|---|---|
| Transport loss | Failure contained | PASS / FAIL |
| Path replacement | Session identity preserved | PASS / FAIL |
| Duplicate delivery | No duplicate canonical execution | PASS / FAIL |
| Replay | Historical input rejected as new progress | PASS / FAIL |
| Stale state return | Old state does not regain authority | PASS / FAIL |
| Reordered delivery | Canonical continuity remains valid | PASS / FAIL |
| Recovery interruption | No invalid authority transition | PASS / FAIL |
| Repeated execution | Deterministic result | PASS / FAIL |

The exact matrix should be adapted to the participant's environment.

---

# 28. A Pilot Is Allowed to Fail

This is important.

A pilot that cannot produce a FAIL is not a useful pilot.

If an agreed invariant breaks, the result should be recorded as a failure.

Then:

```text
FAILURE
   |
   v
REPRODUCE
   |
   v
UNDERSTAND
   |
   v
CORRECT
   |
   v
RETEST
```

That cycle is part of serious protocol engineering.

The objective is not to protect a marketing narrative.

The objective is to strengthen the architecture.

---

# 29. What Success Looks Like

A strong pilot outcome is not:

> VRP looked impressive.

A stronger outcome is:

```text
WE DEFINED AN INVARIANT.

WE DEFINED A FAILURE.

WE EXECUTED THE FAILURE.

WE OBSERVED THE RUNTIME.

WE COLLECTED EVIDENCE.

THE EVIDENCE SUPPORTED THE VERDICT.

THE RESULT WAS REPRODUCIBLE.
```

That is useful to both the participant and the protocol.

---

# 30. The Pilot Philosophy

VRP is built around a difficult premise:

Networks will fail.

Paths will change.

Old information will return.

Events will duplicate.

Recovery will be messy.

The architecture should therefore be judged during those moments.

Not only when everything works.

The pilot exists to answer:

# What survives when the transport does not?

That question is the practical expression of:

# Session != Transport

and:

# Continuity First

---

## Veil Routing Protocol

Public pilot evaluation document.

Protected runtime implementation remains private.

Pilot scope, access, infrastructure boundaries, and evaluation criteria should be explicitly agreed before deployment.
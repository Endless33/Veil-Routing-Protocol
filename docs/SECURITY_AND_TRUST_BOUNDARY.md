# Veil Routing Protocol — Security and Trust Boundary

## Public Security Architecture Note

Veil Routing Protocol (VRP) is a continuity-first networking architecture built around a fundamental separation:

**Session != Transport**

This document describes the public security and trust boundary of VRP.

Its purpose is to allow security engineers, infrastructure operators, technical evaluators, and potential pilot participants to understand what they are being asked to trust — and, equally importantly, what they are not being asked to trust.

This document intentionally does not disclose:

- protected runtime algorithms;
- private authority mechanisms;
- internal recovery decision logic;
- cryptographic implementation details;
- security-sensitive thresholds;
- proprietary state-machine internals;
- anti-abuse mechanisms;
- private defense mechanisms.

The objective is not source-code disclosure.

The objective is a clearly defined and testable boundary.

---

# 1. Security Principle

VRP does not assume that network reachability implies authority.

The following concepts are deliberately distinct:

```text
REACHABLE
    !=
VALID
    !=
CURRENT
    !=
AUTHORITATIVE
```

A path becoming available does not automatically make state arriving through that path authoritative.

A transport recovering does not automatically restore the authority of historical state associated with it.

A previously valid event does not automatically become valid new progress when observed again.

These distinctions are fundamental to the VRP security model.

---

# 2. Trust Must Have a Boundary

A system cannot meaningfully claim:

> Trust us, the runtime is secure.

That is not a security boundary.

A useful security model should instead identify:

```text
WHAT ENTERS

WHAT IS ALLOWED TO CHANGE

WHAT MAY BECOME AUTHORITATIVE

WHAT CAN BE OBSERVED

WHAT CAN BE REJECTED

WHAT EVIDENCE LEAVES

WHAT REMAINS PROTECTED
```

VRP separates these concerns into a public evaluation surface and a protected implementation surface.

---

# 3. Public Surface vs Protected Runtime

The conceptual boundary is:

```text
+---------------------------------------------------+
|                 PUBLIC SURFACE                    |
|                                                   |
|  Architecture                                     |
|  Declared invariants                              |
|  Integration boundary                             |
|  Failure scenarios                                |
|  Observable runtime behavior                      |
|  Evidence                                         |
|  Validation results                               |
|  PASS / FAIL criteria                             |
+-------------------------+-------------------------+
                          |
                          | controlled boundary
                          |
+-------------------------v-------------------------+
|               PROTECTED RUNTIME                   |
|                                                   |
|  Private implementation mechanisms                |
|  Internal authority logic                         |
|  Recovery internals                               |
|  Security-sensitive policy                        |
|  Proprietary runtime mechanisms                   |
+---------------------------------------------------+
```

The protected runtime is not part of the unrestricted public disclosure surface.

The externally observable behavior remains subject to evaluation.

---

# 4. Private Does Not Mean Unverifiable

VRP makes an important distinction:

```text
IMPLEMENTATION DISCLOSURE
          !=
BEHAVIORAL VERIFICATION
```

An evaluator does not necessarily need unrestricted access to every internal algorithm to test an externally declared property.

For example, an evaluator can ask:

```text
Was session identity preserved?

Was stale state accepted?

Did duplicate delivery produce duplicate canonical execution?

Did replay become new progress?

Did recovery alter previously accepted history?

Did the runtime produce the expected verdict?
```

Those are behavioral questions.

They can be tested at an appropriate external boundary.

---

# 5. Threat Categories Relevant to Continuity

VRP engineering considers failure and adversarial conditions that can threaten continuity correctness.

Publicly discussable classes include:

- stale state;
- replayed state;
- duplicate delivery;
- reordered delivery;
- conflicting state;
- transport disappearance;
- transport recovery;
- path migration;
- delayed historical information;
- concurrent recovery activity;
- repeated migration;
- recovery interruption;
- inconsistent recovery inputs.

This list describes classes of conditions.

It does not disclose the protected mechanisms used internally to handle them.

---

# 6. Transport Is Not a Trust Anchor

A central VRP assumption is:

```text
TRANSPORT AVAILABLE
        !=
TRANSPORT AUTHORITATIVE
```

A transport is a carrier.

It can:

```text
APPEAR
DISAPPEAR
RETURN
CHANGE
STALL
REORDER
DUPLICATE
RECOVER
```

The logical authority of a session must not depend solely on the fact that a transport currently works.

This is one reason VRP separates session lifetime from transport lifetime.

---

# 7. Recovery Is a Security Boundary

Recovery is not merely an availability operation.

It is also a correctness boundary.

Consider:

```text
CURRENT STATE
     |
     X   transport failure
     |
NEW PATH APPEARS
     |
OLD STATE ALSO RETURNS
```

A naive recovery mechanism may be tempted to accept whatever state restores connectivity fastest.

A continuity-first architecture must instead preserve its declared invariants.

Therefore:

```text
RECOVERY SUCCESS
      !=
CONNECTIVITY RESTORED
```

A stronger definition is:

```text
RECOVERY SUCCESS
      =
CONNECTIVITY / EXECUTION RESTORED
      +
REQUIRED INVARIANTS PRESERVED
```

If required invariants cannot be established, silent continuation may be more dangerous than explicit failure.

---

# 8. Replay Is Not Progress

A previously accepted event may still be structurally valid.

That does not mean observing it again represents new canonical progress.

Conceptually:

```text
EVENT X accepted

        time passes

EVENT X appears again

        |

        +---- historical observation
        |
        +---- duplicate
        |
        +---- replay
        |
        +---- legitimate new progress?
```

Those possibilities are not equivalent.

VRP's public security model requires replay and new progress to remain conceptually distinct.

The exact internal detection mechanism remains protected.

---

# 9. Stale State Must Not Regain Authority by Availability

Consider:

```text
STATE A
   |
STATE B
   |
STATE C  <-- current accepted state

network disruption

STATE A returns
```

The fact that `STATE A` was once valid does not mean it may now replace `STATE C`.

Historical validity is not current authority.

This leads to another important distinction:

```text
ONCE VALID
    !=
VALID NOW
```

---

# 10. Duplicate Delivery Must Not Mean Duplicate Authority

Distributed systems routinely encounter duplication.

A continuity architecture should not assume perfect exactly-once transport delivery.

Therefore:

```text
MESSAGE OBSERVED TWICE
          !=
CANONICAL TRANSITION OCCURRED TWICE
```

Duplicate transport behavior must not silently become duplicate authoritative execution.

The internal implementation used to preserve this property belongs to the protected runtime.

The resulting behavior can be tested.

---

# 11. Canonical History Matters

Availability without historical integrity is insufficient.

Suppose recovery restores execution but silently changes previously accepted history.

The system may be online.

It may also be wrong.

VRP therefore treats historical integrity as part of continuity.

Conceptually:

```text
ACCEPTED HISTORY

A -> B -> C
          |
          X network failure

RECOVERY
          |
          v

A -> B -> C -> D
```

is fundamentally different from:

```text
A -> B -> C

network failure

A -> X -> Y
```

if the second history silently replaces already accepted canonical state.

Recovery must not become an uncontrolled history rewrite mechanism.

---

# 12. Failure-Closed Direction

VRP follows a general architectural preference:

> If required continuity invariants cannot be established, do not silently manufacture authority.

This does not mean every ambiguous network event must terminate the entire system.

It means ambiguity must not automatically become authoritative progress.

Possible high-level outcomes may conceptually include:

```text
ACCEPT

REJECT

WAIT

CONTAIN

RECOVER

FAIL
```

The exact internal policy governing those decisions is protected.

---

# 13. VRP Does Not Require Covert Host Control

VRP's architectural objectives do not require:

```text
hidden persistence

unauthorized privilege escalation

security-control bypass

anti-administrator behavior

self-propagation

covert installation

unrelated process modification

secret data collection
```

These behaviors are not prerequisites for continuity-first networking.

A legitimate evaluation should operate inside an explicitly authorized deployment boundary.

---

# 14. VRP Is Not Designed to Hide From the Operator

A legitimate VRP deployment should not depend on deceiving the infrastructure owner about the fact that VRP is running.

An authorized evaluator should be able to establish the operational boundary of the evaluation.

Depending on the pilot configuration, this may include understanding:

- which VRP components are deployed;
- where they execute;
- which network boundary they interact with;
- what interfaces are exposed;
- what observable evidence is produced;
- how the evaluation starts;
- how the evaluation stops;
- how the evaluation environment is removed.

Protected implementation logic can remain private while the operational footprint remains explicit.

---

# 15. No Security Review Bypass

A VRP pilot should not require an organization to bypass its own security process.

Pilot participation should not imply permission to:

- bypass change management;
- ignore network policy;
- disable endpoint protection;
- bypass access controls;
- ignore data-handling requirements;
- circumvent infrastructure ownership;
- deploy into unauthorized environments.

The evaluator controls its infrastructure boundary.

VRP is evaluated inside the boundary agreed by both sides.

---

# 16. Least Necessary Exposure

A pilot should expose only what is necessary to evaluate the agreed continuity properties.

Conceptually:

```text
ORGANIZATION INFRASTRUCTURE
            |
            |
     CONTROLLED BOUNDARY
            |
            v
      VRP EVALUATION
            |
            v
    OBSERVABLE EVIDENCE
```

The pilot should not require unrestricted access to unrelated organizational systems.

Likewise, evaluation does not automatically require unrestricted access to the protected VRP runtime.

Both sides should preserve a defined boundary.

---

# 17. Evaluation Should Be Reversible

A serious infrastructure pilot should have a removal path.

The deployment model should answer:

```text
How is VRP started?

How is VRP stopped?

What components were added?

What state was created?

What evidence was generated?

What remains after shutdown?

How is the evaluation removed?
```

A pilot should not rely on hidden persistence to continue operating after the agreed evaluation has ended.

---

# 18. Observable Evidence

Where supported by the evaluation boundary, VRP favors evidence-oriented validation.

The high-level model is:

```text
FAILURE SCENARIO
       |
       v
RUNTIME EXECUTION
       |
       v
OBSERVABLE EVENTS
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

The goal is to make an engineering claim challengeable.

Not merely believable.

---

# 19. Evidence Is Not the Same as Logging

Ordinary logs answer questions such as:

```text
What did the program print?
```

Evidence-oriented validation asks stronger questions:

```text
What property was being tested?

What failure occurred?

What state transition was observed?

What result was produced?

Can the result be independently checked?
```

Logs may participate in evidence.

They are not automatically proof of a continuity property.

---

# 20. What a Security Evaluator Can Attempt

A qualified evaluator should be encouraged to challenge the public contract.

For example:

```text
INTERRUPT THE TRANSPORT

RETURN AN OLD PATH

REPLAY PREVIOUS INPUT

DELIVER DUPLICATES

REORDER DELIVERY

CAUSE REPEATED MIGRATION

INTERRUPT RECOVERY

INTRODUCE CONFLICTING CONDITIONS

REPEAT THE SAME TEST

COMPARE THE RESULT
```

The objective is not to create a visually successful demo.

The objective is to determine whether declared invariants survive.

---

# 21. Negative Results Matter

A security evaluation is not useful if only successful results are allowed to exist.

If a test reveals:

```text
unexpected acceptance

unexpected divergence

non-determinism

incorrect recovery

unbounded behavior

evidence inconsistency
```

that result should be investigated.

A reproducible failure is engineering information.

The purpose of validation is to discover whether the architecture behaves as claimed.

---

# 22. Public Claims Should Remain Falsifiable

VRP should avoid security claims that cannot be meaningfully challenged.

For example:

```text
"secure"

"unhackable"

"military grade"

"impossible to break"
```

are not useful engineering invariants.

A stronger statement has a defined failure condition.

For example:

```text
Given scenario X,
property Y must remain true.

If Y becomes false,
the test fails.
```

That is an evaluable claim.

---

# 23. Security Responsibility Is Shared

VRP cannot make the surrounding infrastructure automatically secure.

A deployment still depends on external concerns such as:

- host security;
- credential management;
- operating-system security;
- network policy;
- deployment authorization;
- key management where applicable;
- infrastructure configuration;
- physical security;
- organizational controls.

VRP should therefore not be interpreted as a replacement for the security architecture around it.

Its security claims should remain scoped to its declared protocol/runtime boundary.

---

# 24. Protected Core Boundary

Some parts of VRP remain intentionally private.

This protects:

```text
INTELLECTUAL PROPERTY

SECURITY-SENSITIVE IMPLEMENTATION DETAILS

PROPRIETARY RUNTIME MECHANISMS

PRIVATE DEFENSE LOGIC
```

The public repository should not be treated as a complete representation of the protected runtime.

Likewise, absence of protected implementation source from the public repository should not be interpreted as absence of implementation.

The correct evaluation question is not:

> Is every internal mechanism public?

It is:

> Is the claimed external behavior sufficiently defined and testable?

---

# 25. Pilot Trust Model

A pilot should begin with explicit assumptions.

Both sides should understand:

```text
WHAT IS BEING TESTED

WHERE IT IS BEING TESTED

WHAT VRP MAY ACCESS

WHAT VRP MAY NOT ACCESS

WHAT FAILURE CONDITIONS WILL BE INTRODUCED

WHAT EVIDENCE WILL BE COLLECTED

WHAT COUNTS AS PASS

WHAT COUNTS AS FAIL

HOW THE PILOT ENDS
```

This is a stronger trust model than asking either side for unlimited access.

---

# 26. Why Earlier Security Evaluation Can Be Valuable

Real infrastructure frequently exposes assumptions that controlled environments do not.

A qualified pilot may reveal:

- unexpected NAT behavior;
- real carrier transitions;
- enterprise firewall interactions;
- infrastructure-specific timing;
- operational recovery constraints;
- unusual routing behavior;
- deployment limitations;
- application-specific continuity requirements.

Finding those constraints earlier can influence the external integration boundary while it is still evolving.

That is one reason serious technical evaluation can be more useful than waiting for a completely frozen architecture.

This is engineering feedback, not artificial urgency.

---

# 27. What Pilot Participation Does Not Grant

Participation does not automatically grant:

```text
PROTECTED SOURCE ACCESS

PRIVATE ALGORITHM DISCLOSURE

INTELLECTUAL PROPERTY TRANSFER

UNRESTRICTED INTERNAL ACCESS

PRODUCTION AUTHORIZATION

SECURITY-REVIEW EXEMPTION
```

Any access beyond the public evaluation boundary requires a separate explicit agreement.

---

# 28. Questions a Security Team Should Ask VRP

A security team evaluating VRP should ask questions such as:

1. What exactly is being deployed?

2. What privileges does it require?

3. What network interfaces does it interact with?

4. What information enters and leaves the evaluation boundary?

5. What state persists during the evaluation?

6. How is the runtime stopped?

7. How is the evaluation removed?

8. What happens when transport disappears?

9. What happens when stale state returns?

10. What happens when previous input is replayed?

11. What happens under duplicate delivery?

12. What happens when recovery is interrupted?

13. What evidence demonstrates the claimed outcome?

14. Can the scenario be repeated?

15. What constitutes a failed invariant?

Those are legitimate evaluation questions.

VRP should be prepared to answer them at the appropriate disclosure boundary.

---

# 29. The Security Invariant in One Diagram

```text
               NETWORK
                  |
                  v
              TRANSPORT
                  |
                  v
        +-------------------+
        | EVALUATION /      |
        | ADMISSION BOUNDARY|
        +-------------------+
                  |
          accepted | rejected
                  |
                  v
        CONTINUITY RUNTIME
                  |
                  v
        AUTHORITATIVE STATE
                  |
                  v
              EVIDENCE
```

The important principle is:

```text
NETWORK INPUT
     !=
AUTHORITATIVE STATE
```

There must be a boundary between them.

The implementation of that boundary is protected.

Its externally visible consequences are testable.

---

# 30. The Security Position

VRP does not ask an evaluator to believe that network failure can be eliminated.

It assumes the opposite.

Paths fail.

Transports disappear.

Old information returns.

Events duplicate.

Recovery races occur.

The security objective is to preserve defined authority and continuity properties despite those conditions — or to contain the situation when safe continuation cannot be established.

The shortest form is:

# Reachability != Authority

# Replay != Progress

# Recovery != Permission to Rewrite History

# Session != Transport

# Continuity First

---

## Veil Routing Protocol

Public security and trust-boundary document.

Protected runtime implementation remains private.

External claims should be evaluated through explicit scenarios, observable evidence, and reproducible verdicts.
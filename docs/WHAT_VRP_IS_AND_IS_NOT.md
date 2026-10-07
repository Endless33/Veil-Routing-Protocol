# What VRP Is — And What It Is Not

## Public Architecture Note

Veil Routing Protocol (VRP) is an experimental continuity-first networking architecture.

Its central architectural distinction is:

**Session != Transport**

VRP treats logical session continuity and the transport currently carrying that session as separate concerns.

This document describes the public conceptual boundary of VRP.

It intentionally does not disclose:

- protected runtime algorithms;
- private authority mechanisms;
- proprietary recovery logic;
- security-sensitive thresholds;
- cryptographic internals;
- anti-abuse implementation details;
- private deployment mechanisms.

The objective is to explain what VRP is trying to solve without exposing how the protected runtime implements those guarantees.

---

# 1. What VRP Is

VRP is an attempt to make continuity an explicit property of a networked runtime.

Many network applications implicitly bind continuity to the lifetime of a connection, socket, route, interface, or transport path.

VRP starts from a different assumption:

> Transports are temporary. Logical continuity may need to survive them.

A transport may disappear.

A path may change.

An address may change.

Connectivity may temporarily collapse.

A device may move between networks.

Previously valid state may return after newer state already exists.

Duplicate information may arrive.

Events may be reordered.

Recovery may race with another recovery attempt.

None of these conditions should automatically redefine which logical session is authoritative.

That distinction is the foundation of the VRP architecture.

---

# 2. The Core Separation

A simplified transport-bound model can look like:

```text
SESSION
   |
   +---- TRANSPORT
             |
             +---- NETWORK PATH
```

If transport lifetime effectively defines session lifetime, transport failure can become session failure.

VRP separates those concepts:

```text
                 SESSION
                    |
             CONTINUITY STATE
                    |
         +----------+----------+
         |          |          |
    TRANSPORT A  TRANSPORT B  TRANSPORT C
         |          |          |
       PATH A     PATH B     RECOVERY PATH
```

The transport is a carrier.

It is not automatically the identity of the session.

This leads to the architectural principle:

**Session != Transport**

---

# 3. What VRP Is Not

Understanding what VRP does not claim to be is as important as understanding what it is.

---

## 3.1 VRP Is Not Just Another VPN

The project historically originated from networking work associated with the name Jumping VPN.

Its architecture subsequently moved beyond the conventional VPN abstraction.

A traditional VPN commonly focuses on problems such as:

- encrypted tunneling;
- virtual network interfaces;
- routing through another endpoint;
- traffic protection;
- network reachability.

VRP asks a different class of question:

> What happens to logical continuity when the transport underneath it changes, disappears, returns, or becomes stale?

Transport security can be part of a deployed system.

It is not the defining architectural idea of VRP.

---

## 3.2 VRP Is Not a Reconnect Script

A reconnect mechanism can detect a failed connection and establish another one.

That alone does not determine:

- whether the logical session is still the same session;
- whether recovered state is still authoritative;
- whether old state has returned;
- whether an event is being replayed;
- whether duplicate execution occurred;
- whether accepted history remains canonical.

Connectivity restoration and continuity preservation are different problems.

VRP is primarily concerned with the second problem.

---

## 3.3 VRP Is Not an Interface Switcher

Switching from Wi-Fi to mobile connectivity is useful.

For example:

```text
Wi-Fi lost
     |
Mobile available
     |
Interface switched
```

That proves that another network path exists.

It does not by itself prove that:

```text
session identity survived
authority remained valid
stale state was rejected
duplicate execution was contained
history remained canonical
```

VRP treats these as separate properties.

---

## 3.4 VRP Is Not Ordinary Failover

Conventional failover commonly answers:

> Which available component or path should take over?

A continuity-first architecture must additionally ask:

> What is still allowed to become authoritative after that transition?

A replacement path being reachable does not automatically make every state associated with it valid.

Recovery must preserve declared continuity invariants.

---

## 3.5 VRP Is Not a Load Balancer

A load balancer distributes traffic.

VRP is not defined by traffic distribution.

Multiple transports or paths may participate in a VRP environment, but the architectural problem remains continuity and correctness while those transports change.

---

## 3.6 VRP Is Not a Claim of an Unbreakable Network

VRP does not claim that networks cannot fail.

Networks fail.

Interfaces disappear.

Packets are lost.

Routes change.

Devices restart.

Connectivity becomes unavailable.

A continuity-first architecture must therefore define behavior for situations where safe continuation is impossible.

The objective is not:

```text
NEVER FAIL
```

The objective is closer to:

```text
DO NOT SILENTLY TURN
TRANSPORT FAILURE
INTO
INCORRECT AUTHORITATIVE STATE
```

Where safe continuity cannot be established, a system should prefer explicit containment over silently accepting contradictory state.

---

# 4. VRP Is Not Malware

VRP is a networking and distributed-runtime research project.

Its architecture does not require malware behavior.

The VRP model does not depend on:

- covert persistence;
- unauthorized privilege escalation;
- disabling host security controls;
- hiding from system administrators;
- secretly modifying unrelated software;
- unauthorized data collection;
- covert exfiltration;
- self-propagation.

A legitimate VRP deployment should have an explicit operational boundary.

An evaluator should be able to establish:

```text
WHAT IS INSTALLED

WHAT PROCESS IS RUNNING

WHAT COMPONENTS PARTICIPATE

WHAT NETWORK BOUNDARY IS USED

WHAT DATA ENTERS THE EVALUATION

WHAT DATA LEAVES THE EVALUATION

WHAT EVIDENCE IS PRODUCED

HOW THE RUNTIME IS STOPPED

HOW THE EVALUATION IS REMOVED
```

A pilot deployment should occur only with explicit authorization from the infrastructure owner or responsible operator.

VRP evaluation is intended to be observable, bounded, and reversible.

---

# 5. Why Some Runtime Logic Is Private

Public verification does not require publication of every implementation detail.

VRP intentionally separates:

```text
PUBLIC ARCHITECTURE
PUBLIC INVARIANTS
PUBLIC VALIDATION
PUBLIC EVIDENCE
PUBLIC INTEGRATION BOUNDARY

              !=

PROTECTED RUNTIME IMPLEMENTATION
```

The protected runtime may contain implementation-specific mechanisms that form part of the project's intellectual property and security boundary.

Those internals are not required to explain the externally observable architectural contract.

The intended evaluation model is:

```text
CLAIM
  |
  v
SCENARIO
  |
  v
EXECUTION
  |
  v
EVIDENCE
  |
  v
INDEPENDENT CHECK
  |
  v
VERDICT
```

The evaluator should be able to challenge externally stated properties without requiring unrestricted access to protected internals.

This distinction is deliberate.

**Private implementation does not mean unverifiable behavior.**

---

# 6. What VRP Attempts to Preserve

At the public architectural level, VRP investigates preservation of several classes of properties.

---

## Session Identity

A transport replacement should not automatically redefine logical session identity.

```text
TRANSPORT A
    |
    X
    |
TRANSPORT B

SESSION IDENTITY
      |
      +---- preserved where permitted
```

---

## Authority

Older, stale, or conflicting state must not silently become authoritative merely because it becomes reachable again.

Availability is not authority.

Reachability is not authority.

Transport recovery is not authority.

---

## Causal Integrity

Recovery should respect accepted state relationships.

A recovered event should not be accepted merely because it exists.

Its relationship to accepted history matters.

---

## Replay Rejection

Previously observed information must not automatically become new progress when presented again.

A replayed event and a legitimate new event are not equivalent.

---

## Duplicate Containment

Repeated delivery must not silently become repeated canonical execution.

Network duplication should not automatically become state duplication.

---

## Historical Integrity

Recovery must not casually rewrite already accepted history.

A continuity mechanism that restores connectivity while corrupting canonical history has not preserved continuity correctly.

---

## Determinism

Equivalent recovery inputs should not produce unexplained divergent outcomes.

Deterministic behavior matters for:

- debugging;
- evidence;
- replay;
- auditing;
- reproducibility;
- failure analysis.

---

## Evidence

Important continuity claims should be testable through externally observable evidence where the evaluation boundary permits it.

The desired engineering relationship is:

```text
CLAIM != PROOF

CLAIM + REPRODUCIBLE TEST + EVIDENCE = EVALUABLE CLAIM
```

---

# 7. Example Failure Scenario

Consider the following sequence:

```text
T0  Logical session exists over Wi-Fi.

T1  Wi-Fi disappears.

T2  Transport reachability is lost.

T3  Mobile connectivity becomes available.

T4  A replacement path becomes usable.

T5  Previously observed or stale information appears.

T6  Runtime evaluates admissibility.

T7  Invalid historical state is contained.

T8  Valid continuity proceeds.
```

A simple reconnect mechanism primarily addresses:

```text
T1 -> T4
```

A continuity architecture must reason about:

```text
T1 -> T8
```

Especially:

```text
T5
T6
T7
T8
```

because restoration of network reachability is only part of the problem.

---

# 8. Why Session != Transport Matters

Consider two conceptual identities:

```text
SESSION_ID

TRANSPORT_ID
```

If they effectively share the same lifetime:

```text
TRANSPORT DEATH
       =
SESSION DEATH
```

If they are separated:

```text
TRANSPORT DEATH
       |
       v
CONTINUITY DECISION
       |
       +---- continue safely
       |
       +---- migrate
       |
       +---- wait
       |
       +---- reject stale state
       |
       +---- contain conflict
       |
       +---- fail closed
```

Transport failure becomes an input into continuity behavior.

It no longer automatically defines the fate of the logical session.

That is a fundamentally different runtime boundary.

---

# 9. Why This Problem Is Difficult

Changing a network interface is not the difficult part.

Modern operating systems already support multiple interfaces and changing routes.

The difficult problem is maintaining correctness while the environment changes.

Consider simultaneous conditions:

```text
OLD PATH DELAYED

NEW PATH ACTIVE

DUPLICATE EVENT ARRIVES

OLD STATE RETURNS

RECOVERY STARTS

PACKETS REORDER

NETWORK DISAPPEARS AGAIN

ANOTHER RECOVERY ATTEMPT OCCURS
```

The runtime must still determine what may become canonical.

This is not simply a routing problem.

It is a continuity and distributed-state problem.

---

# 10. Failure Is Part of the Architecture

VRP does not treat failure as an exceptional afterthought.

Failure is part of the operating model.

The architecture is developed around the assumption that components and paths can:

```text
DISAPPEAR
RETURN
REORDER
DUPLICATE
DELAY
CONFLICT
RESTART
BECOME STALE
```

A continuity-first system therefore needs explicit answers to questions such as:

```text
What survived?

What changed?

What is still authoritative?

What must be rejected?

What evidence explains the decision?
```

Those questions define much of the engineering work around VRP.

---

# 11. Why Validation Matters

A continuity architecture should not be evaluated only under ideal network conditions.

It should be challenged at its assumptions.

Public VRP engineering work therefore emphasizes classes of scenarios such as:

- physical transport interruption;
- path migration;
- repeated transport migration;
- replay attempts;
- duplicate delivery;
- stale state;
- conflicting state;
- recovery races;
- reordered delivery;
- concurrent execution;
- deterministic reconstruction;
- runtime pressure;
- prolonged instability.

The meaningful result is not merely:

> The process stayed alive.

The meaningful question is:

> Did the declared invariant survive?

That distinction is essential.

---

# 12. Engineering Evidence Over Marketing Claims

VRP should not require an evaluator to trust statements such as:

```text
"seamless"

"unbreakable"

"next generation"

"zero downtime"

"revolutionary"
```

Those words are not evidence.

The stronger evaluation model is:

```text
INVARIANT
   |
SCENARIO
   |
FAILURE INJECTION
   |
OBSERVATION
   |
EVIDENCE
   |
VERDICT
```

If a scenario breaks the invariant, that result matters.

If an implementation defect is found, that result matters.

A serious protocol architecture becomes stronger when failure can be reproduced, understood, corrected, and tested again.

---

# 13. What a VRP Pilot Is For

A VRP pilot is not intended to be a conventional product demonstration.

It is an engineering evaluation boundary.

The objective is to place VRP against infrastructure and failure conditions that matter to the evaluator.

A pilot can define:

```text
DEPLOYMENT BOUNDARY
        |
        v
FAILURE SCENARIOS
        |
        v
EXPECTED INVARIANTS
        |
        v
OBSERVABLE EVIDENCE
        |
        v
PASS / FAIL CRITERIA
```

This makes the evaluation falsifiable.

Instead of asking:

> Does the demo look impressive?

the pilot should ask:

> Does the declared property survive the agreed failure scenario?

---

# 14. Why Qualified Evaluation Earlier Can Matter

There is an engineering reason to evaluate an architecture before every external boundary becomes permanently frozen.

Real infrastructure can reveal constraints that synthetic environments cannot reproduce accurately.

Examples may include:

- unusual NAT behavior;
- carrier transitions;
- enterprise network policy;
- application-specific timing;
- real failover topology;
- infrastructure-specific recovery conditions;
- unexpected interaction between independent systems;
- operational constraints not visible in laboratory testing.

Earlier qualified evaluation allows those realities to influence integration boundaries while those boundaries are still evolving.

This is not a claim that an organization must deploy VRP immediately.

It is a reason not to confuse:

```text
WAITING LONGER
```

with:

```text
LEARNING MORE
```

For an organization with a genuinely relevant continuity problem, earlier controlled evaluation may produce more architectural information than passive observation.

---

# 15. Pilot Participation Does Not Mean Source Disclosure

Participation in a VRP evaluation does not automatically imply:

- unrestricted access to protected source code;
- disclosure of proprietary runtime algorithms;
- transfer of intellectual property;
- disclosure of private defense mechanisms;
- bypassing organizational security review;
- bypassing infrastructure authorization;
- acceptance of production readiness.

The evaluation boundary should be explicitly defined before deployment.

A useful pilot can evaluate externally observable behavior without exposing protected implementation internals.

---

# 16. What a Serious Evaluator Should Ask

A technical evaluator should not begin with:

> Is this a better VPN?

A better starting question is:

> Which invariant is this architecture claiming to preserve?

Then challenge that invariant.

For example:

```text
KILL THE TRANSPORT

REPLACE THE PATH

REPLAY PREVIOUS STATE

DELIVER DUPLICATES

REORDER EVENTS

RETURN STALE STATE

INTERRUPT RECOVERY

REPEAT THE SCENARIO

COMPARE THE EVIDENCE
```

If the claimed invariant does not survive, the evaluation should expose that.

That is not a failure of the evaluation process.

That is the purpose of the evaluation process.

---

# 17. The Public Contract

The public VRP story should remain deliberately smaller than the protected implementation.

The public contract is concerned with:

```text
WHAT PROPERTY IS CLAIMED

WHAT FAILURE IS APPLIED

WHAT BEHAVIOR IS OBSERVABLE

WHAT RESULT IS PRODUCED

WHETHER THE RESULT IS REPRODUCIBLE
```

The public contract does not require publication of:

```text
HOW EVERY INTERNAL DECISION IS IMPLEMENTED
```

This separation protects both evaluation integrity and implementation boundaries.

---

# 18. The Short Version

VRP is not primarily about keeping a socket alive.

It is not primarily about selecting another interface.

It is not primarily about tunneling packets.

It is not primarily about hiding network failures.

It is about separating:

```text
WHO THE SESSION IS
```

from:

```text
HOW THE SESSION IS CURRENTLY BEING CARRIED
```

and then attempting to preserve defined correctness properties while the second one changes.

That is the architectural meaning of:

# Session != Transport

And the engineering direction behind:

# Continuity First

---

## Veil Routing Protocol

**Continuity-first networking architecture**

Public architecture document.

Protected runtime implementation remains private.
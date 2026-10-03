# Veil Routing Protocol — Integration Model

**Project:** Veil Routing Protocol (VRP)  
**Author:** Vitalijus Riabovas  
**Development:** 2024–2026  
**Status:** Public Integration Model  
**Implementation:** Protected / Private

> **SESSION ≠ TRANSPORT**

> **CONTINUITY FIRST.**

---

# 1. Purpose

This document describes the public integration model of the **Veil Routing Protocol (VRP)**.

It explains:

- where VRP conceptually sits in an existing system;
- what VRP is intended to govern;
- what existing infrastructure may remain unchanged;
- which responsibilities remain with the application;
- which responsibilities remain with the transport;
- what an organization should define before evaluating VRP;
- what a controlled VRP evaluation should attempt to establish.

This document intentionally does not define the protected implementation interface, internal runtime algorithms, private state transitions or deployment-specific Core configuration.

It describes the integration boundary.

It is not an implementation guide.

---

# 2. Integration Principle

VRP is designed around a simple deployment principle:

> Introduce continuity semantics without requiring the existing network stack to become the identity of the logical session.

A simplified deployment may look like:

    ┌──────────────────────────────┐
    │         APPLICATION          │
    └──────────────┬───────────────┘
                   │
                   │ logical execution
                   v
    ┌──────────────────────────────┐
    │     VRP RUNTIME BOUNDARY     │
    │                              │
    │ session continuity           │
    │ lifecycle                    │
    │ canonical state              │
    │ authority                    │
    │ recovery                     │
    │ admission                    │
    └──────────────┬───────────────┘
                   │
                   │ replaceable transport
                   v
    ┌──────────────────────────────┐
    │   EXISTING TRANSPORT STACK   │
    │                              │
    │ TCP / UDP / QUIC / tunnel /  │
    │ relay / VPN / other          │
    └──────────────┬───────────────┘
                   │
                   v
               NETWORK

VRP does not require the organization to discard its existing transport technology merely because VRP is introduced.

---

# 3. VRP Is an Additional Boundary

VRP should not be interpreted as:

    APPLICATION
        |
        v
    REPLACEMENT INTERNET STACK

The intended model is closer to:

    APPLICATION
        |
        v
    CONTINUITY BOUNDARY
        |
        v
    EXISTING CONNECTIVITY

The purpose of this additional boundary is to prevent transport identity from becoming the sole definition of logical session continuity.

---

# 4. What Can Remain Existing

Depending on the deployment, an organization may continue using its existing:

- IP network;
- routing infrastructure;
- TCP stack;
- UDP transport;
- QUIC implementation;
- VPN;
- encrypted tunnel;
- relay infrastructure;
- mobile connectivity;
- Wi-Fi infrastructure;
- cloud networking;
- load-balancing infrastructure;
- observability systems;
- application protocols.

VRP does not inherently require replacement of these technologies.

The exact compatibility of a particular environment must still be evaluated.

---

# 5. What VRP Adds

VRP introduces a logical continuity responsibility above transport instability.

At the architectural level, this includes concerns such as:

- logical session identity;
- session lifecycle;
- canonical execution state;
- authority continuity;
- historical-work rejection;
- replay containment;
- duplicate containment;
- transport replacement;
- recovery validation;
- fail-closed behavior.

These responsibilities are separate from merely transmitting packets.

---

# 6. Existing Transport Responsibilities

Underlying transport technology remains responsible for its own transport-level behavior.

Depending on the transport, that may include:

- packet delivery;
- stream delivery;
- retransmission;
- congestion control;
- path management;
- connection migration;
- encryption;
- tunnel establishment;
- routing;
- interface selection.

VRP does not claim these responsibilities merely because it sits above or around the transport boundary.

---

# 7. VRP Responsibilities

At the public architectural level, VRP is concerned with questions such as:

    WHICH LOGICAL SESSION IS CURRENT?

    WHICH LIFETIME IS CURRENT?

    WHICH AUTHORITY IS CURRENT?

    IS THIS WORK HISTORICAL?

    IS THIS WORK A REPLAY?

    IS THIS EXECUTION DUPLICATED?

    MAY THIS EXECUTION BECOME CANONICAL?

    MAY THIS SESSION CONTINUE AFTER TRANSPORT CHANGE?

    MUST EXECUTION FAIL CLOSED?

These are continuity questions rather than basic packet-delivery questions.

---

# 8. Application Responsibilities

VRP does not remove application semantics.

The application still owns decisions that are inherently application-specific.

Examples may include:

- business logic;
- domain state;
- authorization policy outside the VRP boundary;
- transaction semantics;
- operation idempotency requirements;
- application-level conflict resolution;
- user-visible recovery behavior;
- application-specific terminal conditions.

A VRP integration therefore requires a clear boundary between:

    APPLICATION STATE

and:

    CONTINUITY STATE

Those are not automatically the same thing.

---

# 9. Integration Does Not Mean Moving Everything Into VRP

A poor integration would attempt to make the continuity runtime responsible for every part of the application.

That is not the objective.

VRP should govern only the state necessary to establish correct continuity.

Conceptually:

    APPLICATION
      |
      +---- business state
      |
      +---- application policy
      |
      +---- domain behavior
      |
      v
    VRP BOUNDARY
      |
      +---- session continuity
      |
      +---- lifecycle validity
      |
      +---- canonical admission
      |
      +---- authority continuity
      |
      v
    TRANSPORT

The exact boundary depends on the target system.

---

# 10. Integration Question One

Before considering VRP, an organization should ask:

> Does our logical session need to outlive an individual transport connection?

If the answer is no, VRP may provide little value.

If the answer is yes, additional questions become relevant.

---

# 11. Integration Question Two

> What currently happens when the active transport disappears?

Possible answers may include:

- the application fails;
- the user reconnects;
- the application creates a new session;
- context is reconstructed from storage;
- traffic migrates automatically;
- another transport becomes active;
- another node takes authority;
- the operation is retried.

None of these answers is inherently wrong.

The purpose of evaluation is to determine whether the existing behavior provides the continuity semantics the application requires.

---

# 12. Integration Question Three

> What defines the identity of the logical session today?

Potential answers may include:

- socket;
- connection ID;
- process;
- tunnel;
- user token;
- database record;
- application object;
- distributed runtime state.

If logical session identity is implicitly tied to a replaceable transport resource, transport failure may also become a logical identity event.

VRP is designed to separate those concerns.

---

# 13. Integration Question Four

> What happens to delayed work after recovery?

This is particularly important.

Consider:

    OPERATION CREATED
          |
          v
    NETWORK FAILURE
          |
          v
    RECOVERY
          |
          v
    NEW EXECUTION CONTEXT
          |
          v
    OLD OPERATION ARRIVES

An integration must define whether that operation is:

    CURRENT

    DUPLICATE

    REPLAYED

    HISTORICAL

    INVALID

VRP is designed so that historical execution does not silently become current execution.

---

# 14. Integration Question Five

> Who owns authority after failover or recovery?

Reachability is not enough.

An old component may return after another component has become authoritative.

Therefore:

    COMPONENT IS ONLINE
            !=
    COMPONENT IS CURRENT AUTHORITY

An integration involving authority movement must preserve this distinction.

---

# 15. Integration Question Six

> What is allowed to become canonical?

A system should distinguish:

    RECEIVED

from:

    ACCEPTED

and:

    ACCEPTED

from:

    CANONICAL

The continuity boundary must not allow invalid execution to contaminate canonical state merely because it was observed.

---

# 16. Example: Mobile Transition

Consider a mobile application moving between networks.

    APPLICATION SESSION
           |
           v
         Wi-Fi
           |
           X
      CONNECTION LOST
           |
           v
       CELLULAR
           |
           v
       CONTINUE

A transport-oriented implementation may focus primarily on restoring connectivity.

A VRP-oriented integration additionally asks:

- Is this still the same logical session?
- Is the current lifecycle still valid?
- Is authority unchanged?
- Did historical work arrive during the transition?
- Did any operation execute twice?
- Is the resumed state canonical?

The mobile transition is therefore only the visible network event.

The continuity problem exists above it.

---

# 17. Example: NAT Rebinding

A network address may change while the logical endpoint remains the same application participant.

Conceptually:

    SESSION S

       |

    PATH / ADDRESS A

       |

    NETWORK CHANGE

       |

    PATH / ADDRESS B

       |

    SESSION S

The network identity changed.

The logical session did not necessarily change.

A VRP deployment should avoid treating incidental transport identity as canonical session identity.

---

# 18. Example: Transport Replacement

Suppose an application has:

    SESSION S
        |
        v
    TRANSPORT A

Transport A becomes unavailable.

A replacement becomes available:

    SESSION S
        |
        v
    TRANSPORT B

The desired architectural result may be:

    SESSION S REMAINS CURRENT

provided that all required continuity invariants remain valid.

The existence of Transport B alone is not sufficient.

The runtime must still determine whether continuation is safe.

---

# 19. Example: Recovery With Historical Work

A more difficult case is:

    SESSION S
      |
      v
    LIFETIME 1
      |
      X
    TERMINATED
      |
      v
    LIFETIME 2
      |
      +---------- CURRENT
      |
      ^
      |
    DELAYED WORK FROM LIFETIME 1

The delayed operation may contain the same SessionID.

It must still remain historical.

This is one reason session identity alone is insufficient for continuity admission.

---

# 20. Example: Authority Recovery

Consider:

    PRIMARY A
        |
        X
      FAILURE
        |
        v
    PRIMARY B
        |
        v
    AUTHORITY MOVES
        |
        v
    PRIMARY A RETURNS

Primary A becoming reachable again must not automatically restore its previous authority.

The integration must preserve current authority lineage independently from network reachability.

---

# 21. Example: Existing QUIC Deployment

An organization may already use QUIC.

VRP does not require QUIC to be removed.

Conceptually:

    APPLICATION
        |
        v
    VRP CONTINUITY BOUNDARY
        |
        v
    QUIC
        |
        v
    IP NETWORK

QUIC may handle:

- secure transport;
- streams;
- congestion control;
- connection migration.

VRP may handle the higher-level continuity questions associated with:

- logical session identity;
- lifecycle;
- authority;
- canonical execution;
- recovery.

These responsibilities can coexist.

---

# 22. Example: Existing VPN Deployment

An organization may already operate a VPN or encrypted tunnel.

Conceptually:

    APPLICATION
        |
        v
    VRP CONTINUITY BOUNDARY
        |
        v
    VPN / TUNNEL
        |
        v
    NETWORK

The VPN provides secure connectivity.

VRP does not need to become the tunnel merely to govern logical continuity.

---

# 23. Example: Relay Infrastructure

An existing deployment may use relay nodes.

Conceptually:

    APPLICATION
        |
        v
    VRP
        |
        v
    RELAY A
        |
        X
    RELAY FAILURE
        |
        v
    RELAY B

Changing relays should not automatically redefine the logical session.

But the replacement must still satisfy the required continuity conditions.

---

# 24. Integration Surface

A production integration should define a narrow, explicit boundary between the application and the continuity runtime.

At the conceptual level, that boundary needs to support activities such as:

- establishing logical session context;
- presenting logical operations;
- observing continuity state;
- handling transport availability;
- handling transport replacement;
- receiving terminal outcomes;
- exposing relevant evidence or telemetry.

The exact protected API is not specified publicly in this document.

---

# 25. Why the Exact API Is Not Published Here

A public integration model and a production API specification serve different purposes.

This document is intended to answer:

> Where does VRP fit?

It is not intended to answer:

> How can the protected runtime be reconstructed?

Implementation-specific API structures may reveal:

- internal state organization;
- lifecycle mechanics;
- authority mechanics;
- recovery mechanics;
- scheduling assumptions;
- protected control flow.

Those details remain outside the public boundary.

---

# 26. Deployment Shapes

Different environments may integrate VRP differently.

Possible conceptual shapes include:

### Embedded Runtime

    APPLICATION PROCESS
        |
        +---- APPLICATION
        |
        +---- VRP BOUNDARY

### Local Service

    APPLICATION
        |
        v
    LOCAL VRP SERVICE
        |
        v
    TRANSPORT

### Infrastructure Component

    APPLICATION / SERVICE
        |
        v
    CONTINUITY SERVICE
        |
        v
    EXISTING NETWORK INFRASTRUCTURE

These diagrams describe possible architectural placements only.

They do not represent a published implementation specification.

---

# 27. Deployment Choice Is Environment-Specific

The appropriate placement depends on factors such as:

- trust boundary;
- latency;
- application architecture;
- operating system;
- deployment topology;
- performance requirements;
- failure model;
- security requirements;
- operational ownership.

There is no claim that one integration shape is universally correct.

---

# 28. Trust Boundary

A VRP integration should explicitly identify its trust assumptions.

Questions include:

- Which component creates session context?
- Which component may request execution?
- Which component observes transport state?
- Which component owns application authorization?
- Which components are trusted to provide accurate inputs?
- What happens if a dependency becomes unavailable?
- What happens if an input is malformed?
- What happens if the runtime cannot establish validity?

These questions must be answered for the target environment.

---

# 29. Failure Boundary

The integration should define what happens when continuity cannot safely be preserved.

Possible outcomes may include:

- operation rejection;
- session quarantine;
- terminal failure;
- application notification;
- explicit re-establishment of a new logical session.

A production integration should never silently convert an uncertain continuity state into successful canonical execution.

---

# 30. Fail-Closed Integration

The preferred architecture is:

    UNCERTAIN STATE
          |
          v
    DO NOT GUESS
          |
          v
    REJECT / STOP / QUARANTINE

rather than:

    UNCERTAIN STATE
          |
          v
    ASSUME CONTINUITY
          |
          v
    POSSIBLE CANONICAL CORRUPTION

This principle is particularly important during recovery.

---

# 31. Observability

An integration should provide sufficient observability to distinguish important runtime outcomes.

Examples may include:

- continuity preserved;
- transport unavailable;
- replacement transport accepted;
- execution rejected;
- replay rejected;
- historical execution rejected;
- authority invalid;
- recovery failed;
- terminal state reached.

The exact telemetry format is implementation-specific.

---

# 32. Evidence Boundary

For serious evaluation, observability should be capable of supporting evidence.

A useful evaluation relationship is:

    FAILURE INJECTION
          |
          v
    OBSERVABLE RUNTIME BEHAVIOR
          |
          v
    RESULT
          |
          v
    EVIDENCE
          |
          v
    REVIEW

The objective is to establish what happened, not merely whether a demonstration appeared successful.

---

# 33. Evaluation Before Deployment

VRP should not move directly from architectural interest to production assumption.

A controlled evaluation should occur first.

Conceptually:

    ARCHITECTURAL REVIEW
          |
          v
    TARGET ENVIRONMENT DEFINITION
          |
          v
    INTEGRATION BOUNDARY
          |
          v
    CONTROLLED EVALUATION
          |
          v
    FAILURE TESTING
          |
          v
    EVIDENCE REVIEW
          |
          v
    DEPLOYMENT DECISION

A negative result is a legitimate engineering result.

---

# 34. Define the Target Environment

Before evaluation, an organization should define:

### Application

What application or service is being protected?

### Session

What constitutes the logical session?

### Transport

Which connectivity mechanisms currently exist?

### Failure Model

Which failures matter?

### Authority

Does execution authority move between components?

### Recovery

How is recovery currently performed?

### Continuity Requirement

Which state must survive transport failure?

### Terminal Conditions

When should continuity stop?

---

# 35. Define Success Before Testing

Success criteria should be established before evaluation.

Examples might include:

- logical session identity remains stable across an approved transport transition;
- historical operations remain rejected;
- duplicate execution remains contained;
- stale authority does not regain control;
- invalid recovery fails closed;
- canonical state remains internally consistent;
- required evidence is produced.

The exact acceptance criteria depend on the target deployment.

---

# 36. Define Failure Before Testing

Failure criteria are equally important.

Examples may include:

- session identity changes unexpectedly;
- historical work is accepted;
- duplicate execution becomes canonical;
- stale authority becomes current;
- rejected work mutates canonical state;
- recovery bypasses admission rules;
- runtime state becomes ambiguous;
- evidence cannot establish the outcome.

An evaluation that cannot fail is not a meaningful evaluation.

---

# 37. Performance Qualification

Correctness alone does not establish acceptable performance.

A target deployment must independently evaluate:

- latency;
- throughput;
- CPU cost;
- memory cost;
- recovery time;
- transport-switch cost;
- concurrency behavior;
- resource exhaustion behavior.

No universal performance numbers are defined by this public integration document.

---

# 38. Scale Qualification

Likewise, scale must be evaluated in context.

Relevant dimensions may include:

- concurrent sessions;
- operations per session;
- transport changes;
- authority changes;
- number of nodes;
- evidence volume;
- recovery frequency;
- workload distribution.

A result at one scale must not automatically be extrapolated to another.

---

# 39. Security Qualification

A target deployment should also consider:

- host compromise;
- credential compromise;
- key management;
- denial of service;
- malformed input;
- privilege boundaries;
- application authorization;
- transport security;
- telemetry exposure;
- evidence access;
- operational security.

VRP's continuity architecture does not eliminate these separate security responsibilities.

---

# 40. Application Compatibility

Not every application is automatically compatible with continuity across transport replacement.

Some operations may depend on:

- local process state;
- transport-local state;
- timing assumptions;
- non-idempotent external effects;
- third-party systems;
- application-specific transaction boundaries.

These dependencies must be identified during integration.

---

# 41. External Side Effects

Canonical runtime admission cannot automatically undo arbitrary external side effects.

For example, an application operation may trigger:

- a payment;
- a physical action;
- a database mutation;
- a message to another system;
- an external API request.

The target architecture must determine how those side effects interact with retry, duplication and recovery.

VRP does not replace application transaction design.

---

# 42. Operational Integration

A real deployment must also define operational procedures.

These may include:

- startup;
- shutdown;
- upgrade;
- rollback;
- monitoring;
- incident response;
- evidence retention;
- key rotation;
- authority transition;
- transport maintenance;
- failure recovery.

Continuity is not only a runtime concern.

It is also an operational concern.

---

# 43. Upgrade and Rollback

Runtime upgrades can change the continuity environment.

Therefore an organization should determine:

- whether active sessions survive an upgrade;
- how compatibility is established;
- how rollback affects authority;
- whether old components may reappear;
- whether state format changes;
- whether requalification is required.

The protected implementation determines the exact mechanism.

The integration must define the operational expectation.

---

# 44. Requalification

A successful evaluation applies to the evaluated environment.

Meaningful changes may require requalification.

Examples include:

- new application behavior;
- different transport technology;
- new network topology;
- major runtime upgrade;
- authority-model change;
- security-boundary change;
- substantially different scale.

This prevents old evidence from being treated as proof for a materially different deployment.

---

# 45. When VRP May Be Useful

VRP may be worth evaluating when a system has several of the following properties:

- logical sessions outlive individual connections;
- clients frequently change networks;
- transport failure currently destroys important context;
- stale work may arrive after recovery;
- duplicate execution is dangerous;
- authority may move between components;
- recovery races are possible;
- continuity must survive temporary network loss;
- correctness is more important than uninterrupted connectivity;
- continuity outcomes must be observable.

This is not a guarantee of suitability.

It is an indication that the VRP problem may exist.

---

# 46. When VRP May Not Be Necessary

VRP may add unnecessary complexity when:

- sessions are intentionally short-lived;
- reconnecting and creating a new session is acceptable;
- no meaningful state survives transport loss;
- duplicate execution has no relevant consequence;
- authority does not move;
- the application already has sufficient continuity semantics;
- the environment does not require transport-independent logical identity.

The correct architecture is the smallest architecture that satisfies the actual requirement.

---

# 47. Controlled External Evaluation

Organizations interested in VRP should begin with a concrete technical problem rather than a request for protected source.

A useful evaluation request describes:

- the application;
- the network environment;
- the existing transport;
- the continuity problem;
- relevant failures;
- expected behavior;
- security constraints;
- approximate scale;
- evaluation objective.

This allows VRP to be evaluated against an actual requirement.

---

# 48. What Public Documentation Provides

The public VRP documentation provides enough information to understand:

- the continuity problem;
- the architectural model;
- the integration position;
- the relationship to existing transports;
- the major security objectives;
- the public project boundaries.

It intentionally does not provide the complete implementation required to reproduce the protected Core.

---

# 49. What a Serious Integration Should Prove

A serious integration should eventually be able to answer:

    WHAT IS THE LOGICAL SESSION?

    WHAT DEFINES ITS CURRENT LIFETIME?

    WHAT DEFINES CURRENT AUTHORITY?

    WHAT HAPPENS WHEN TRANSPORT FAILS?

    WHAT HAPPENS WHEN TRANSPORT RETURNS?

    WHAT HAPPENS WHEN OLD WORK RETURNS?

    WHAT HAPPENS WHEN WORK IS DUPLICATED?

    WHAT HAPPENS WHEN AUTHORITY IS STALE?

    WHAT BECOMES CANONICAL?

    WHEN DOES THE SYSTEM FAIL CLOSED?

    HOW IS THE RESULT OBSERVED?

If these questions cannot be answered, the integration boundary is not yet sufficiently defined.

---

# 50. Public Integration Summary

VRP integration can be summarized as:

    KEEP EXISTING NETWORK

              ↓

    KEEP EXISTING TRANSPORT
    WHERE APPROPRIATE

              ↓

    IDENTIFY THE LOGICAL
    SESSION BOUNDARY

              ↓

    INTRODUCE VRP CONTINUITY
    RESPONSIBILITY

              ↓

    SEPARATE SESSION
    FROM TRANSPORT

              ↓

    DEFINE LIFECYCLE
    AND AUTHORITY

              ↓

    DEFINE CANONICAL
    EXECUTION

              ↓

    TEST FAILURE
    AND RECOVERY

              ↓

    FAIL CLOSED
    WHEN CORRECTNESS
    CANNOT BE ESTABLISHED

---

# 51. Final Integration Statement

VRP is not an instruction to rebuild an organization's network.

It is an architectural boundary for systems where the lifetime of logical execution must not be dictated solely by the lifetime of a transport connection.

The existing network may remain.

The existing transport may remain.

The application may remain.

What changes is the treatment of continuity.

Transport becomes replaceable.

Logical session state remains explicitly governed.

Recovery remains subject to validation.

Historical work remains historical.

Authority remains independent from reachability.

Canonical state remains protected from invalid execution.

That is the VRP integration model.

---

# SESSION ≠ TRANSPORT

# CONTINUITY FIRST.

---

**Veil Routing Protocol (VRP)**  
**Vitalijus Riabovas**  
**2024–2026**

Public integration model.  
Protected implementation.
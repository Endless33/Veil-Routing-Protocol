# Veil Routing Protocol — Public Architecture

**Project:** Veil Routing Protocol (VRP)  
**Author:** Vitalijus Riabovas  
**Development:** 2024–2026  
**Status:** Public Architecture  
**Implementation:** Protected / Private

> **SESSION ≠ TRANSPORT**

> **CONTINUITY FIRST.**

---

# 1. Purpose

This document defines the public architectural model of the **Veil Routing Protocol (VRP)**.

It explains:

- the problem VRP addresses;
- the architectural separation at the center of VRP;
- the logical responsibilities of the continuity layer;
- the relationship between session, transport, lifecycle and authority;
- the role of canonical state;
- the recovery model;
- the public integration boundary;
- the limits of the public specification.

This document intentionally does **not** describe the protected runtime implementation.

It is an architectural description, not a reconstruction guide.

---

# 2. Architectural Problem

Network connectivity is temporary.

Logical application state may not be.

A device may:

- move between Wi-Fi and cellular connectivity;
- change network interfaces;
- acquire a new address;
- cross NAT or CGNAT boundaries;
- lose a path;
- recover a path;
- move through different relays;
- experience packet reordering;
- experience duplicate delivery;
- temporarily disappear from the network;
- reconnect after an outage.

Traditional reconnect-oriented systems often treat transport failure as an event that requires reconstruction of higher-level context.

VRP separates those concerns.

The fundamental architectural question is:

> What logical state should remain canonical when the transport underneath it changes?

---

# 3. Fundamental Separation

VRP begins with:

## SESSION ≠ TRANSPORT

A logical session and the transport currently carrying its traffic are different objects with different lifecycles.

Conceptually:

    ┌───────────────────────────────────┐
    │          LOGICAL SESSION          │
    │                                   │
    │ identity                          │
    │ lifecycle                         │
    │ canonical state                   │
    │ authority                         │
    │ continuity context                │
    └────────────────┬──────────────────┘
                     │
                     │ replaceable binding
                     │
          ┌──────────┼──────────┐
          │          │          │
          v          v          v
    TRANSPORT A TRANSPORT B TRANSPORT C

Transport A may disappear.

Transport B may replace it.

Transport C may later become preferable.

None of those events, by themselves, prove that the logical session should be recreated.

Likewise, the existence of a transport does not prove that the logical session is valid.

---

# 4. Separation of Responsibilities

The architecture separates several concerns that are frequently coupled.

    SESSION IDENTITY
          !=
    TRANSPORT IDENTITY

    REACHABILITY
          !=
    AUTHORITY

    CONNECTION RECOVERY
          !=
    SESSION RECOVERY

    MESSAGE VALIDITY
          !=
    EXECUTION VALIDITY

    HISTORICAL WORK
          !=
    CURRENT WORK

    OBSERVED EVENT
          !=
    CANONICAL EVENT

    CRYPTOGRAPHIC VALIDITY
          !=
    CANONICAL ADMISSION

These distinctions are fundamental to VRP.

---

# 5. Logical Session

A VRP logical session represents continuity above an individual network connection.

The session may contain or reference logical properties such as:

- identity;
- lifecycle;
- authority context;
- canonical execution state;
- continuity state;
- transport bindings.

The exact protected representation is implementation-specific and is not defined by this public document.

The important architectural property is:

> Transport replacement does not automatically redefine logical session identity.

---

# 6. Transport

A transport is a replaceable communication resource.

Depending on deployment, it may involve:

- UDP;
- TCP;
- QUIC;
- an encrypted tunnel;
- a relay;
- Wi-Fi;
- cellular connectivity;
- wired connectivity;
- multipath connectivity;
- another application-specific communication mechanism.

VRP does not require ownership of the entire transport stack.

The transport provides connectivity.

VRP governs continuity semantics above that connectivity.

---

# 7. Transport Binding

A logical session may be associated with a currently usable transport.

That relationship is a **binding**, not an identity equivalence.

Conceptually:

    SESSION
      |
      +---- bound to ----> TRANSPORT A

may become:

    SESSION
      |
      +---- bound to ----> TRANSPORT B

without requiring:

    OLD SESSION
        X

    NEW SESSION

The exact mechanism by which bindings are established, validated, replaced or revoked belongs to the protected implementation.

---

# 8. Session Lifecycle

Session identity alone is insufficient to determine whether work is current.

Consider:

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

A delayed operation originating from Lifetime 1 may still reference Session S.

That does not make it valid for Lifetime 2.

Therefore VRP distinguishes:

    SESSION IDENTITY

from:

    SESSION LIFETIME

A current session may have historical execution associated with an older lifetime.

Historical work must not silently become current work.

---

# 9. Historical Execution

Distributed systems frequently receive delayed work.

Sources may include:

- network delay;
- retries;
- asynchronous queues;
- delayed callbacks;
- duplicated delivery;
- old workers;
- restarted components;
- stale transport paths;
- previous session lifetimes.

Historical work may appear structurally valid.

It may reference the correct logical session.

It may even have been valid when originally created.

The relevant question is:

> Is it valid now?

VRP therefore treats execution context as part of canonical admission.

---

# 10. Canonical State

VRP distinguishes attempted execution from accepted canonical execution.

Conceptually:

    INPUT
      |
      v
    VALIDATE
      |
      +---------- INVALID ----------> REJECT
      |
      v
    ACCEPT
      |
      v
    CANONICAL STATE

A rejected operation must not become canonical merely because it was observed.

This gives an important invariant:

## REJECTED EXECUTION MUST NOT MUTATE CANONICAL STATE

The protected runtime determines how this invariant is implemented.

The public architecture defines the requirement.

---

# 11. Canonical Admission

Canonical admission is the logical boundary between:

    ATTEMPTED EXECUTION

and:

    ACCEPTED EXECUTION

Admission may depend on multiple dimensions of runtime validity.

At the architectural level, these may include questions such as:

- Is the session current?
- Is the lifecycle current?
- Is the authority current?
- Is the operation historical?
- Is the operation duplicated?
- Is the operation replayed?
- Is execution allowed in the current state?
- Would accepting it violate canonical history?

The protected implementation is responsible for answering these questions.

The public architecture requires that invalid execution fail closed.

---

# 12. Authority

VRP treats authority as independent from network reachability.

This means:

    REACHABLE
        !=
    AUTHORITATIVE

A process may be reachable while holding stale authority.

A recovered node may be reachable while belonging to an older authority generation.

An old transport may become reachable again after replacement.

None of those conditions automatically grants execution authority.

Authority must remain logically governed.

---

# 13. Authority Continuity

Transport instability and authority instability are separate problems.

A transport may change while authority remains valid.

Authority may change while the logical session remains identifiable.

The architecture must therefore reason about these independently.

Conceptually:

    SESSION
       |
       +---- LIFECYCLE
       |
       +---- AUTHORITY
       |
       +---- TRANSPORT

Changing one dimension does not automatically redefine all others.

---

# 14. Stale Authority

Recovery creates a particularly dangerous condition:

    OLD AUTHORITY
         |
         X
      FAILURE
         |
         v
    NEW AUTHORITY
         |
         v
    OLD COMPONENT RETURNS

The returning component may be healthy.

It may be reachable.

It may possess previously valid state.

It is still historical if its authority is no longer current.

VRP requires stale authority to remain distinguishable from current authority.

---

# 15. Recovery

Recovery is part of the correctness model.

It is not an exception to it.

VRP rejects the architectural pattern:

    FAILURE
       |
       v
    RECOVERY MODE
       |
       v
    RELAX VALIDATION
       |
       v
    RESTORE SERVICE AT ANY COST

Instead:

    FAILURE
       |
       v
    RECOVERY
       |
       v
    VALIDATE CURRENT STATE
       |
       +------ INVALID ------> REJECT
       |
       v
    CONTINUE

Recovery must not silently convert historical execution into current execution.

---

# 16. Replay

A replayed operation may contain data that was once legitimate.

That does not make the replay legitimate.

VRP treats replay resistance as part of continuity correctness.

A system has not preserved correct continuity if an old operation can become new canonical execution after a transport or recovery event.

Therefore:

    PREVIOUSLY VALID
          !=
    VALID NOW

---

# 17. Duplicate Execution

Duplicate delivery and duplicate execution are different concerns.

A network may deliver the same logical work more than once.

The continuity runtime must prevent delivery duplication from silently becoming multiple canonical executions when the application model requires singular execution.

Therefore:

    MULTIPLE OBSERVATIONS
            !=
    MULTIPLE CANONICAL EXECUTIONS

---

# 18. Transport Failure

Transport failure is treated as a connectivity event.

It is not automatically a session-destruction event.

Conceptually:

    SESSION ACTIVE
          |
          v
    TRANSPORT LOST
          |
          v
    CONNECTIVITY UNAVAILABLE
          |
          v
    REPLACEMENT AVAILABLE
          |
          v
    VALIDATE
          |
          v
    REBIND / RECOVER
          |
          v
    SESSION CONTINUES

This diagram describes architectural intent.

It does not imply that every outage is recoverable.

---

# 19. Failure Must Remain Possible

A continuity architecture that always reports success is not trustworthy.

VRP permits terminal failure.

If required correctness cannot be established:

    FAIL CLOSED

is preferable to:

    CONTINUE WITH AMBIGUOUS STATE

Therefore the architecture explicitly allows:

- rejection;
- quarantine;
- terminal state;
- failed recovery;
- session termination.

Continuity is conditional on correctness.

---

# 20. Connectivity vs Continuity

Connectivity answers:

> Can data currently move?

Continuity answers:

> Can the logical execution safely remain the same execution?

These questions are related but not equivalent.

For example:

    NETWORK RECOVERED
            +
    STALE EXECUTION ACCEPTED
            =
    CONTINUITY FAILURE

Similarly:

    NETWORK AVAILABLE
            +
    WRONG AUTHORITY
            =
    CONTINUITY FAILURE

VRP therefore does not measure continuity solely through packet reachability.

---

# 21. Cryptographic Boundary

Cryptography protects important communication properties.

Depending on implementation and deployment, these may include:

- authenticity;
- integrity;
- confidentiality;
- message binding;
- anti-tampering properties.

However:

    CRYPTOGRAPHICALLY VALID
             !=
    CURRENTLY AUTHORIZED

A perfectly authentic historical message may still be stale.

A correctly authenticated operation may still belong to an obsolete session lifetime.

Cryptography therefore supports VRP correctness but does not replace lifecycle or authority validation.

---

# 22. Evidence

VRP treats evidence as an engineering concern.

A continuity claim should be capable of being connected to observable behavior.

Conceptually:

    CLAIM
      |
      v
    EXECUTION
      |
      v
    OBSERVATION
      |
      v
    EVIDENCE
      |
      v
    VERIFICATION

Evidence does not make an architecture correct by itself.

It provides a mechanism for evaluating whether observed behavior matches the claimed invariant.

---

# 23. Evidence Is Not Source Verification

Different forms of assurance must remain distinct.

For example:

    RUNTIME EVIDENCE VERIFICATION
              !=
    SOURCE CODE REVIEW

and:

    SOURCE CODE REVIEW
              !=
    FORMAL VERIFICATION

and:

    INTERNAL TESTING
              !=
    EXTERNAL CERTIFICATION

VRP does not collapse these categories into one claim.

---

# 24. Architectural Invariants

At the public architectural level, VRP is organized around invariants such as:

### Invariant 1

**Transport identity does not define logical session identity.**

### Invariant 2

**Historical execution must not silently become current execution.**

### Invariant 3

**Reachability does not define authority.**

### Invariant 4

**Rejected execution must not become canonical execution.**

### Invariant 5

**Recovery must not bypass canonical validation.**

### Invariant 6

**Replay must not silently become new canonical work.**

### Invariant 7

**Duplicate observation must not automatically become duplicate canonical execution.**

### Invariant 8

**Continuity must fail closed when required correctness cannot be established.**

---

# 25. Runtime Boundary

At a high level, the architecture can be represented as:

    ┌──────────────────────────────────┐
    │           APPLICATION            │
    └────────────────┬─────────────────┘
                     │
                     v
    ┌──────────────────────────────────┐
    │       VRP CONTINUITY LAYER       │
    │                                  │
    │ session identity                 │
    │ lifecycle                        │
    │ canonical state                  │
    │ authority                        │
    │ recovery                         │
    │ validation                       │
    └────────────────┬─────────────────┘
                     │
                     v
    ┌──────────────────────────────────┐
    │      TRANSPORT / CONNECTIVITY    │
    │                                  │
    │ UDP / TCP / QUIC / tunnel /      │
    │ relay / mobile / Wi-Fi / other   │
    └────────────────┬─────────────────┘
                     │
                     v
                  NETWORK

The protected implementation behind the VRP continuity layer is intentionally not specified here.

---

# 26. Existing Infrastructure

VRP is designed conceptually to coexist with existing networking infrastructure.

It does not require the invention of a new physical network.

It does not require existing transport technologies to disappear.

An organization may already use:

- QUIC;
- TCP;
- UDP;
- WireGuard;
- IPsec;
- private tunnels;
- SD-WAN;
- relays;
- cellular infrastructure;
- cloud networking.

VRP addresses continuity semantics above or around the relevant transport boundary.

---

# 27. VRP and QUIC

QUIC provides transport functionality including connection migration.

VRP does not claim to replace or reinvent that capability.

The responsibilities are different.

Conceptually:

    APPLICATION
        |
        v
    VRP
        |
        v
    QUIC
        |
        v
    IP NETWORK

The question for QUIC may include:

> Can the connection continue across a path change?

The VRP question is broader at the runtime boundary:

> Which logical execution remains canonical while transport conditions change?

---

# 28. VRP and Multipath

Multipath technologies can provide multiple network paths.

VRP may operate in an environment where such capabilities exist.

But:

    MULTIPLE PATHS
          !=
    CANONICAL SESSION STATE

Path selection and logical execution authority remain separate concerns.

---

# 29. VRP and VPN Technology

VPN technology provides secure network connectivity.

VRP is not defined as another VPN tunnel.

The earlier **Jumping VPN** project name reflects the project's historical origin, not the final architectural scope.

The modern VRP architecture focuses on logical continuity independently from a particular tunnel technology.

---

# 30. Application Boundary

VRP does not assume that every application should automatically preserve every state across every failure.

Application semantics remain important.

A target deployment must determine:

- which operations may continue;
- which operations require idempotency;
- which operations require stronger execution guarantees;
- what constitutes terminal failure;
- which state belongs to VRP;
- which state remains application-owned.

VRP provides a continuity architecture.

It does not eliminate application semantics.

---

# 31. Deployment Qualification

Architectural correctness does not automatically establish deployment suitability.

A real deployment must evaluate the architecture under its own:

- workload;
- network;
- latency;
- topology;
- concurrency;
- scale;
- failure model;
- security requirements;
- operational procedures.

Therefore:

    ARCHITECTURE DEFINED
            !=
    EVERY DEPLOYMENT QUALIFIED

Target-environment qualification remains necessary.

---

# 32. Public Disclosure Boundary

This document intentionally stops at the architectural boundary.

It does not define:

- protected internal algorithms;
- private state-machine transitions;
- internal authority implementation;
- private recovery implementation;
- key-management internals;
- internal scheduling mechanisms;
- detailed replay-window implementation;
- private evidence formats;
- private test harnesses;
- adversarial test recipes;
- internal runtime traces;
- protected deployment mechanisms.

Those details belong to the private implementation.

---

# 33. Why the Boundary Exists

A public architecture should allow engineers to understand the system's purpose and challenge its assumptions.

It does not need to publish every implementation mechanism.

The intended public boundary is:

    UNDERSTAND THE PROBLEM

    UNDERSTAND THE MODEL

    UNDERSTAND THE RESPONSIBILITIES

    UNDERSTAND THE CLAIMS

    UNDERSTAND THE LIMITATIONS

without providing:

    A STEP-BY-STEP CORE RECONSTRUCTION GUIDE

---

# 34. Architectural Summary

VRP can be summarized through the following chain:

    NETWORKS CHANGE

          ↓

    TRANSPORTS FAIL OR MOVE

          ↓

    LOGICAL SESSION IDENTITY
    MUST NOT BE DEFINED ONLY
    BY THAT TRANSPORT

          ↓

    SESSION LIFECYCLE,
    AUTHORITY AND EXECUTION
    MUST REMAIN GOVERNED

          ↓

    HISTORICAL, REPLAYED,
    DUPLICATE OR INVALID WORK
    MUST NOT BECOME CANONICAL

          ↓

    RECOVERY MUST OBEY
    THE SAME CORRECTNESS RULES

          ↓

    IF CORRECTNESS CANNOT
    BE ESTABLISHED

          ↓

    FAIL CLOSED

---

# 35. Final Architectural Statement

VRP is not built around the assumption that networks can be made perfectly stable.

They cannot.

It is built around a different assumption:

> Network instability should not automatically redefine logical truth.

Transport may change.

Connectivity may disappear.

Paths may recover.

Components may restart.

Historical work may return.

The continuity runtime must still determine what is current, what is authoritative, what is canonical and what must be rejected.

That is the VRP architectural boundary.

---

# SESSION ≠ TRANSPORT

# CONTINUITY FIRST.

---

**Veil Routing Protocol (VRP)**  
**Vitalijus Riabovas**  
**2024–2026**

Public architecture.  
Protected implementation.
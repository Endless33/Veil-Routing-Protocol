# Veil Routing Protocol — Origin and Authorship

## Project Identity

**Project:** Veil Routing Protocol  
**Abbreviation:** VRP  
**Earlier development name:** Jumping VPN  
**Author:** Vitalijus Riabovas  
**Development period represented by this project:** 2024–2026

**Core architectural principle:**

> SESSION ≠ TRANSPORT

**Engineering principle:**

> CONTINUITY FIRST.

---

## Purpose of This Record

This document establishes the public project identity, development lineage and authorship record of the **Veil Routing Protocol (VRP)** project.

VRP is an independent networking and distributed-systems engineering project developed by **Vitalijus Riabovas** during 2024–2026.

The project originated from earlier engineering work developed under the name **Jumping VPN** and evolved into the broader **Veil Routing Protocol** architecture.

The purpose of this document is not to claim ownership of established networking concepts.

Its purpose is to identify the origin and authorship of the specific VRP project, architecture, terminology, documentation and protected implementation developed through this work.

---

# Development Lineage

The project evolved approximately as follows:

    2024
      |
      v
    EARLY CONTINUITY EXPLORATION
      |
      v
    JUMPING VPN
      |
      v
    TRANSPORT-INDEPENDENT SESSION MODEL
      |
      v
    AUTHORITY / LIFECYCLE / RECOVERY MODEL
      |
      v
    VEIL ROUTING PROTOCOL
      |
      v
    PROTECTED VRP RUNTIME
      |
      v
    2026

The transition from **Jumping VPN** to **Veil Routing Protocol** reflects a change in architectural scope.

The project developed beyond the narrower idea of network switching or VPN transport behavior.

The central engineering problem became:

> How can a logical session preserve correct identity, lifecycle, authority and canonical execution state while the underlying transport changes, disappears or recovers?

That problem defines the modern VRP architecture.

---

# Architectural Origin

VRP is built around a separation expressed as:

    SESSION ≠ TRANSPORT

This statement should not be interpreted as a claim that VRP invented the general distinction between application state and network transport.

Distributed systems, mobility protocols, transport protocols and networking research have explored related separations for decades.

Within VRP, however, this principle defines a specific architectural model.

Transport is treated as replaceable.

Logical session state is governed independently.

That distinction leads to additional requirements around:

- session lifecycle;
- canonical execution;
- authority;
- historical work;
- replay;
- duplicate execution;
- recovery;
- transport replacement;
- evidence;
- fail-closed behavior.

The combination of these concerns forms the specific VRP engineering model.

---

# What VRP Claims as Project Work

The VRP project contains project-specific engineering work involving the combination and implementation of concepts including:

- transport-independent logical session continuity;
- explicit session lifecycle boundaries;
- canonical execution state;
- authority continuity;
- stale-lifetime rejection;
- replay containment;
- duplicate-execution containment;
- recovery validation;
- transport replacement without automatic session replacement;
- deterministic runtime behavior;
- evidence-oriented validation;
- protected runtime boundaries.

These statements identify areas of VRP development.

They are not claims that every individual underlying computer-science concept originated with VRP.

---

# What VRP Does Not Claim

VRP does **not** claim to have invented:

- packet networking;
- sessions;
- state machines;
- connection migration;
- roaming;
- multipath networking;
- failover;
- replay protection;
- cryptographic authentication;
- distributed consensus;
- distributed authority;
- VPN technology;
- transport protocols.

Those concepts have extensive prior art.

VRP should be evaluated as a specific architecture built around a particular continuity model, not as a claim to ownership of the entire surrounding field.

---

# Relationship to Existing Technologies

Existing technologies solve important networking problems.

Examples include:

- QUIC connection migration;
- Multipath TCP;
- VPN roaming;
- tunnel rebinding;
- application reconnection;
- distributed failover;
- replicated state systems.

VRP does not invalidate those technologies.

VRP addresses a separate architectural question:

> What remains canonical when connectivity changes?

A transport mechanism may successfully move traffic to another path while a higher-level runtime must still determine:

- whether the logical session remains current;
- whether the current lifecycle is valid;
- whether authority remains valid;
- whether delayed work is historical;
- whether an operation is a replay;
- whether recovery is allowed;
- whether execution may become canonical.

This is the boundary around which VRP is designed.

---

# Jumping VPN → Veil Routing Protocol

The earlier **Jumping VPN** name represented an earlier stage of the project.

As development progressed, the architecture expanded beyond the semantics implied by the word "VPN."

The project increasingly addressed:

    SESSION IDENTITY

    LIFECYCLE

    AUTHORITY

    CANONICAL STATE

    RECOVERY

    REPLAY

    EVIDENCE

    TRANSPORT INDEPENDENCE

For that reason, **Veil Routing Protocol** became the canonical project identity.

References to Jumping VPN in historical project material should therefore be understood as part of the development lineage that led to VRP.

---

# Protected Implementation

The public architecture and the protected runtime are separate project surfaces.

This repository documents the public architectural identity of VRP.

It does not publish the protected Core implementation.

The protected implementation may contain:

- private source code;
- implementation-specific algorithms;
- internal state-machine logic;
- authority mechanisms;
- recovery mechanisms;
- validation infrastructure;
- adversarial test scenarios;
- regression suites;
- runtime traces;
- private evidence artifacts;
- implementation-specific deployment mechanisms.

Those materials are outside the scope of this public repository.

---

# Public Record

This repository is intended to serve as the canonical public architectural record of the Veil Routing Protocol project.

Its Git history may provide a public chronology of material committed to this repository.

Other historical project materials may exist in:

- earlier repositories;
- private repositories;
- source-control history;
- releases;
- archived engineering artifacts;
- local development records;
- validation evidence.

No single repository should be interpreted as containing the complete historical engineering record of the project.

---

# Authorship

The **Veil Routing Protocol (VRP)** project represented by this repository was developed by:

## Vitalijus Riabovas

Development period represented by the project:

## 2024–2026

This authorship statement applies to the specific VRP project and its project-specific work.

It should not be interpreted as a claim of authorship over unrelated prior art or general networking concepts.

---

# Attribution

When publicly discussing, referencing or evaluating the VRP architecture, attribution should identify:

**Veil Routing Protocol (VRP)**  
**Vitalijus Riabovas**

Canonical project repository:

https://github.com/Endless33/Veil-Routing-Protocol

---

# Intellectual and Technical Boundaries

Public availability of this document does not imply that the protected VRP implementation has been released.

Architecture and implementation are intentionally separated.

The public project boundary provides enough information to understand:

- what VRP is;
- what problem it addresses;
- its primary architectural separation;
- how it relates conceptually to existing networking technology;
- where its public disclosure boundary ends.

It does not attempt to provide enough implementation detail to reproduce the protected Core.

---

# Historical Precision

Technical provenance should be described precisely.

The strongest authorship record is not created by claiming that every surrounding idea is new.

It is created by maintaining a clear, dated and internally consistent record of:

- project evolution;
- terminology;
- architecture;
- implementation history;
- source history;
- engineering artifacts;
- public releases.

VRP therefore distinguishes between:

    EXISTING COMPUTER-SCIENCE CONCEPTS

and:

    THE SPECIFIC VRP ARCHITECTURE AND IMPLEMENTATION

That distinction is intentional.

---

# Canonical Statement

**Veil Routing Protocol is an independent protocol and runtime architecture developed by Vitalijus Riabovas during 2024–2026.**

The project evolved from earlier work under the **Jumping VPN** name.

Its defining architectural principle is:

## SESSION ≠ TRANSPORT

Its engineering objective is:

## CONTINUITY FIRST.

The architecture is public.

The protected implementation remains private.

---

Copyright © 2024–2026 Vitalijus Riabovas.

All rights reserved except where explicitly stated otherwise.
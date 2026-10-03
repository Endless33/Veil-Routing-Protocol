# Veil Routing Protocol — Public Changelog

**Project:** Veil Routing Protocol (VRP)  
**Author:** Vitalijus Riabovas  
**Development:** 2024–2026  
**Scope:** Public Architecture and Documentation

> **SESSION ≠ TRANSPORT**

> **CONTINUITY FIRST.**

---

# Purpose

This changelog records significant changes to the **publicly documented Veil Routing Protocol architecture and project surface**.

It is intentionally not a changelog for the protected VRP Core.

This file may record:

- architectural milestones;
- terminology changes;
- public documentation changes;
- public integration-model changes;
- public security-model changes;
- project-scope changes;
- significant public repository restructuring.

It does not attempt to expose the complete private engineering history.

---

# Scope Boundary

The public changelog records:

    PUBLIC ARCHITECTURE

    PUBLIC TERMINOLOGY

    PUBLIC PROJECT STRUCTURE

    PUBLIC INTEGRATION MODEL

    PUBLIC SECURITY MODEL

It does not record:

    PRIVATE CORE IMPLEMENTATION

    PRIVATE ALGORITHMS

    PRIVATE STATE TRANSITIONS

    PRIVATE TEST CORPUS

    PRIVATE ADVERSARIAL SCENARIOS

    PRIVATE RUNTIME TRACES

    PRIVATE EVIDENCE ARTIFACTS

    PRIVATE DEPLOYMENT MECHANISMS

Absence of an internal engineering change from this document does not mean that the change did not occur.

---

# Versioning Note

The public architecture and the protected implementation do not necessarily share the same release cadence or version numbering.

A public documentation update should therefore not be interpreted automatically as:

- a Core release;
- a production release;
- a deployment qualification;
- a security certification;
- a protocol compatibility change.

Likewise, protected Core development may continue without a corresponding public changelog entry.

---

# 2026-10 — Canonical Public Repository

## Public Repository Consolidation

Established:

**Veil-Routing-Protocol**

as the canonical public architectural repository for the project.

The public surface was deliberately consolidated around a smaller set of documents rather than maintaining an expanding collection of engineering artifacts.

The repository now focuses on answering:

- What is VRP?
- What problem does it address?
- Where did the project originate?
- Where does VRP sit in an existing system?
- How does it differ from transport technologies?
- What are its public security objectives?
- What remains protected?

This consolidation represents a deliberate separation between:

    PUBLIC ARCHITECTURE

and:

    PROTECTED ENGINEERING

---

## Public Disclosure Boundary Clarified

The public repository was reorganized around an explicit disclosure boundary.

Public documentation describes:

- architecture;
- terminology;
- responsibilities;
- integration position;
- security objectives;
- authorship;
- project history;
- limitations.

Protected implementation details remain outside the canonical public repository.

This includes implementation-specific mechanisms that are not required to understand the architecture.

---

## README Established

The canonical `README.md` was established as the primary entry point for VRP.

It defines the central architectural principle:

> **SESSION ≠ TRANSPORT**

and the engineering priority:

> **CONTINUITY FIRST.**

The README also establishes that VRP does not claim to have invented transport migration, roaming, multipath networking, failover or other established networking concepts.

Instead, VRP defines a continuity architecture concerned with preserving valid logical execution across transport instability.

---

## ORIGIN.md Added

Added `ORIGIN.md`.

The document records the public project lineage:

    EARLY CONTINUITY EXPLORATION
              |
              v
         JUMPING VPN
              |
              v
    TRANSPORT-INDEPENDENT
       SESSION MODEL
              |
              v
    LIFECYCLE / AUTHORITY /
       RECOVERY MODEL
              |
              v
    VEIL ROUTING PROTOCOL

The document identifies:

**Vitalijus Riabovas**

as the author of the VRP project represented by the repository, with development represented across:

**2024–2026**

The document explicitly distinguishes project-specific authorship from ownership of established networking and computer-science concepts.

---

## ARCHITECTURE.md Added

Added `ARCHITECTURE.md`.

The document defines the public VRP architecture around the separation of:

    SESSION

from:

    TRANSPORT

It establishes public architectural concepts including:

- logical session identity;
- session lifecycle;
- canonical state;
- authority;
- historical execution;
- replay;
- duplicate execution;
- transport replacement;
- recovery;
- fail-closed behavior.

The document also establishes:

    REACHABILITY
          !=
    AUTHORITY

and:

    REJECTED EXECUTION
          !=
    CANONICAL EXECUTION

The protected implementation remains outside the document.

---

## INTEGRATION.md Added

Added `INTEGRATION.md`.

The document describes where VRP conceptually integrates with existing systems.

The integration model allows existing infrastructure to remain in place where appropriate, including technologies such as:

- TCP;
- UDP;
- QUIC;
- encrypted tunnels;
- VPN infrastructure;
- relays;
- mobile networks;
- Wi-Fi;
- cloud networking.

The document establishes that VRP is intended as a continuity boundary rather than a replacement Internet stack.

It also defines questions organizations should answer before attempting a controlled VRP evaluation.

---

## COMPARISON.md Added

Added `COMPARISON.md`.

The document clarifies the relationship between VRP and established technologies and architectural patterns.

It explicitly avoids presenting VRP as a replacement for:

- QUIC;
- Multipath TCP;
- WireGuard;
- VPN roaming;
- ordinary reconnect logic;
- service meshes;
- SD-WAN;
- database transactions;
- application idempotency;
- distributed consensus.

The primary distinction is defined as:

    TRANSPORT CONTINUITY

            !=

    CANONICAL SESSION CONTINUITY

VRP may coexist with established transport and infrastructure technologies.

---

## SECURITY_MODEL.md Added

Added `SECURITY_MODEL.md`.

The public security model defines continuity-related security objectives including:

- lifecycle isolation;
- stale-work rejection;
- replay containment;
- duplicate containment;
- stale-authority rejection;
- canonical-state protection;
- recovery validation;
- terminal-state protection;
- fail-closed behavior.

The document establishes that:

    CRYPTOGRAPHIC VALIDITY

            !=

    CURRENT EXECUTION VALIDITY

and:

    SECURE TRANSPORT

            !=

    SECURE CONTINUITY

The document also explicitly describes limitations and separates runtime evidence, source review, formal verification and external security review.

---

## CONTACT.md Added

Added `CONTACT.md`.

The document defines the public communication and evaluation boundary.

Relevant inquiries include:

- controlled technical evaluation;
- pilot deployment;
- infrastructure integration;
- engineering review;
- security evaluation;
- target-environment qualification;
- serious organizational collaboration.

The document clarifies that the public repository is not intended to operate as a reconstruction service for the protected VRP Core.

It also establishes that periods of reduced public communication do not automatically imply that private engineering has stopped.

---

## LICENSE Added

Added a repository-level proprietary public-disclosure license.

The repository remains publicly readable while the protected VRP Core remains outside the public license boundary.

The license explicitly states that public accessibility does not, by itself, make the protected implementation open source.

It also distinguishes public documentation from non-public implementation material.

---

# 2026 — Architecture Consolidation

During 2026, the project architecture increasingly centered on a continuity model in which transport is treated as replaceable infrastructure rather than canonical logical identity.

The public architectural model matured around several recurring boundaries:

    SESSION ≠ TRANSPORT

    REACHABILITY ≠ AUTHORITY

    CONNECTIVITY ≠ CONTINUITY

    OBSERVED ≠ CANONICAL

    HISTORICAL ≠ CURRENT

    CRYPTOGRAPHICALLY VALID ≠ CURRENTLY AUTHORIZED

These distinctions became central to the public VRP description.

---

# 2026 — Canonical Execution Model

The project increasingly formalized the distinction between:

    ATTEMPTED EXECUTION

and:

    CANONICAL EXECUTION

The public architectural requirement became:

> Invalid or rejected work must not silently become canonical state.

This principle applies across:

- normal execution;
- transport replacement;
- recovery;
- replay;
- duplicate delivery;
- historical work;
- authority transitions.

The protected implementation of canonical admission remains private.

---

# 2026 — Lifecycle Model

The public architecture established that a logical SessionID alone is not sufficient to determine whether execution is current.

Conceptually:

    SESSION S
       |
       +---- LIFETIME 1
       |
       +---- LIFETIME 2
       |
       +---- ...

Work associated with an older lifetime must remain distinguishable from work associated with the current lifetime.

This became a central part of the VRP continuity model.

---

# 2026 — Authority Model

Authority became an explicit architectural dimension independent from transport reachability.

The public model established:

> A component becoming reachable does not automatically make it authoritative.

This distinction is particularly important during:

- failover;
- restart;
- recovery;
- transport return;
- infrastructure replacement.

Implementation-specific authority mechanisms remain protected.

---

# 2026 — Recovery Model

Recovery was explicitly treated as part of the correctness boundary.

The public architecture rejects the idea that recovery should bypass normal validity requirements.

Instead:

    FAILURE
       |
       v
    RECOVERY
       |
       v
    VALIDATION
       |
       +---- INVALID ----> REJECT
       |
       v
    CONTINUE

The principle became:

> Recovery is not a bypass.

---

# 2026 — Fail-Closed Model

The architecture explicitly accepted that continuity may terminate.

VRP does not define successful continuity as:

> Always keep the session alive.

Instead:

> Continue only while required correctness remains established.

When required validity cannot be established, acceptable outcomes may include:

- rejection;
- quarantine;
- terminal failure;
- explicit creation of a new logical context.

This separates continuity engineering from availability-at-any-cost behavior.

---

# 2026 — Evidence-Oriented Engineering

VRP development adopted an increasingly evidence-oriented engineering approach.

The public architectural relationship can be summarized as:

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

The public repository does not publish the complete private validation corpus.

This is deliberate.

The canonical public repository documents the architecture rather than acting as a complete archive of internal engineering artifacts.

---

# 2026 — Security Boundary Expansion

The security model expanded beyond transport encryption alone.

VRP increasingly treated the following as security-relevant:

- lifecycle validity;
- authority validity;
- replay state;
- duplicate execution;
- historical work;
- canonical admission;
- recovery;
- terminal-state resurrection.

This led to the public principle:

> A message can be authentic and still be invalid for current execution.

---

# 2026 — Target-Environment Qualification

The project explicitly moved away from universal deployment claims.

The public documentation now distinguishes:

    ARCHITECTURE

from:

    TARGET-ENVIRONMENT QUALIFICATION

A successful result in one environment does not automatically establish suitability for:

- another workload;
- another topology;
- another scale;
- another transport;
- another threat model;
- another operational environment.

Production suitability must be evaluated against the actual deployment.

---

# 2026 — Public / Private Separation

The project increasingly separated:

    WHAT THE ARCHITECTURE DOES

from:

    HOW THE PROTECTED CORE IMPLEMENTS IT

The public side focuses on the first question.

The private engineering side retains the second.

This separation became part of the canonical project structure.

---

# 2025 — Continuity Model Expansion

During the project's evolution, the original network-transition problem expanded into a broader session-continuity problem.

The design increasingly considered conditions such as:

- transport loss;
- path replacement;
- delayed execution;
- replay;
- duplicate execution;
- session recovery;
- stale state;
- authority transition.

This moved the project beyond the scope normally implied by a conventional VPN implementation.

---

# 2025 — Session / Transport Separation

The distinction between logical session identity and active transport became increasingly central.

The developing model treated transport as replaceable while attempting to preserve logical session continuity subject to correctness constraints.

This direction eventually became summarized by:

> **SESSION ≠ TRANSPORT**

---

# 2024 — Project Origin

The project began from exploration of continuity across changing network conditions.

Early development focused more heavily on connectivity movement and transport transition.

The project was initially developed under the name:

**Jumping VPN**

The original name reflected that earlier scope.

---

# 2024–2026 — Project Evolution

The high-level project evolution can be represented as:

    NETWORK TRANSITION

           ↓

    TRANSPORT REPLACEMENT

           ↓

    SESSION / TRANSPORT SEPARATION

           ↓

    SESSION LIFECYCLE

           ↓

    CANONICAL EXECUTION

           ↓

    AUTHORITY CONTINUITY

           ↓

    RECOVERY VALIDATION

           ↓

    EVIDENCE-ORIENTED ENGINEERING

           ↓

    VEIL ROUTING PROTOCOL

This diagram is a public historical summary.

It is not an implementation timeline.

---

# Changelog Policy

Future entries in this file should be limited to meaningful changes affecting the public VRP surface.

Examples include:

- major architectural clarification;
- new public document;
- public terminology change;
- integration-model change;
- security-model change;
- licensing change;
- repository-scope change;
- significant public project milestone.

Minor wording changes do not require a changelog entry unless they materially alter the public meaning.

---

# What Should Not Be Added Here

Do not use this file as a dump for:

- every Git commit;
- private Core fixes;
- private test counts;
- internal benchmark results;
- private bug descriptions;
- internal attack scenarios;
- private file names;
- private runtime APIs;
- protected algorithm changes;
- private evidence hashes;
- internal infrastructure details.

Those belong to the protected engineering history.

---

# Historical Precision

This changelog is a project-level public summary.

Git history and other retained project artifacts provide more granular timestamps for individual public changes where available.

The broad historical sections in this document should not be interpreted as claiming that every listed architectural concept reached its final form on the first day of the year under which it appears.

VRP evolved iteratively.

---

# Current Public State

As of October 2026, the canonical public repository is intentionally compact.

Its primary documents are:

    README.md

    ORIGIN.md

    ARCHITECTURE.md

    INTEGRATION.md

    COMPARISON.md

    SECURITY_MODEL.md

    CONTACT.md

    LICENSE

    CHANGELOG.md

Together they define the current public boundary of the Veil Routing Protocol project.

---

# Final Statement

VRP began with a network-continuity problem.

It evolved into a broader question:

> What remains logically true when the transport underneath execution changes?

The public architecture now provides a stable answer to that question without publishing the protected mechanisms used by the Core.

The repository may remain quiet.

The architecture may remain stable.

The protected implementation may continue evolving independently.

Public activity is not the protocol.

Transport is not the session.

---

# SESSION ≠ TRANSPORT

# CONTINUITY FIRST.

---

**Veil Routing Protocol (VRP)**  
**Vitalijus Riabovas**  
**2024–2026**

Public architecture.  
Protected implementation.
# Veil Routing Protocol

<p align="center">
  <strong>A transport-independent continuity architecture for preserving canonical session state across network change and failure.</strong>
</p>

<p align="center">
  <strong>SESSION ≠ TRANSPORT</strong>
</p>

<p align="center">
  <strong>CONTINUITY FIRST.</strong>
</p>

---

## Veil Routing Protocol

**Veil Routing Protocol (VRP)** is an independent protocol and runtime architecture developed by **Vitalijus Riabovas** during **2024–2026**.

VRP explores a specific distributed-systems problem:

> How can a logical session preserve correct identity, lifecycle, authority and canonical execution state while the transport underneath it changes, disappears or recovers?

The central architectural separation is simple:

**Session ≠ Transport.**

The consequences are not.

VRP treats transport as a replaceable execution resource rather than the canonical identity of the logical session.

A path may change.

An interface may disappear.

Connectivity may be interrupted.

A replacement transport may appear.

The logical session does not automatically become a new session merely because the transport changed.

At the same time, continuity is never allowed to override correctness.

If the runtime cannot establish that execution remains valid, it must fail closed.

---

# The Problem

Modern distributed applications operate across unstable infrastructure.

Real networks experience:

- Wi-Fi ↔ cellular transitions
- roaming
- NAT and CGNAT rebinding
- path replacement
- interface loss
- temporary outages
- relay failure
- packet delay
- packet reordering
- duplicate delivery
- process restart
- regional disruption

Many systems handle these events by reconnecting.

Conceptually:

    transport lost
          |
          v
      reconnect
          |
          v
    rebuild context
          |
          v
       continue

That is a valid architecture for many applications.

VRP investigates a different model.

Instead of asking only:

> How do we reconnect?

VRP asks:

> What exactly remains authoritative while connectivity is changing?

That introduces harder questions:

- Is this still the same logical session?
- Which session lifetime is current?
- Which execution state is canonical?
- Which authority is current?
- Can delayed historical work still execute?
- Can duplicate work execute twice?
- Can replayed work become current again?
- Can recovery accidentally restore stale authority?
- Can rejected execution contaminate canonical history?
- Can continuity survive transport replacement without reconstructing identity?
- Can the resulting behavior be independently observed and verified?

These are the problems VRP is designed around.

---

# Core Principle

## SESSION ≠ TRANSPORT

VRP separates logical session identity from transport identity.

Conceptually:

    ┌───────────────────────────┐
    │      LOGICAL SESSION      │
    │                           │
    │  identity                 │
    │  lifecycle                │
    │  canonical state          │
    │  authority                │
    │  continuity context       │
    └─────────────┬─────────────┘
                  │
          replaceable binding
                  │
        ┌─────────┼─────────┐
        │         │         │
        v         v         v
    Transport A Transport B Transport C

The transport can change.

The session does not automatically change with it.

This does **not** mean that every transport replacement must succeed.

It means transport replacement and session identity are separate architectural decisions.

---

# Continuity Is Not Connectivity

VRP does not define continuity as:

> packets are still moving.

Connectivity and correctness are different properties.

A system may remain connected while its logical state is already wrong.

For example:

    CONNECTED
        +
    STALE AUTHORITY
        =
    INCORRECT

or:

    CONNECTED
        +
    HISTORICAL WORK ACCEPTED
        =
    INCORRECT

or:

    CONNECTED
        +
    DUPLICATE EXECUTION
        =
    INCORRECT

Therefore VRP prioritizes:

    CORRECTNESS
        >
    CONNECTIVITY

The network may recover.

The runtime must still prove that resumed execution is valid.

---

# What VRP Preserves

VRP is designed around preservation of several logical properties across transport instability.

These include:

### Session Identity

The logical session is not defined solely by the currently active network connection.

### Session Lifecycle

Current execution must remain distinguishable from historical execution.

### Canonical State

Accepted execution must converge on one authoritative runtime history.

### Authority

Connectivity does not automatically grant execution authority.

### Replay State

Previously accepted or historical work must not silently become new canonical execution.

### Recovery State

Recovery must obey the same correctness boundaries as ordinary execution.

### Evidence

Important runtime decisions should remain observable and capable of producing verifiable engineering evidence.

---

# Identity Is Not Enough

A SessionID alone cannot safely describe every execution context.

Consider:

    Session S
       |
       v
    Lifetime 1
       |
       X
    terminated
       |
       v
    Lifetime 2

A delayed operation created during Lifetime 1 may arrive while Lifetime 2 is active.

The SessionID may still be:

    S

But the operation is historical.

Therefore:

    SAME SESSION ID
          !=
    CURRENT EXECUTION AUTHORITY

VRP treats lifecycle context as part of canonical admission.

This protects the runtime against stale execution and lifecycle ambiguity.

---

# Authority Is Not Reachability

VRP also separates:

    REACHABLE
        !=
    AUTHORITATIVE

A transport becoming available does not automatically grant authority.

A recovered process does not automatically regain authority.

An older execution generation does not automatically become current because it can communicate again.

Authority is a logical runtime property.

This distinction matters during:

- failover
- restart
- partition recovery
- concurrent recovery
- transport replacement
- stale execution
- distributed ownership changes

---

# Recovery Is Not a Bypass

Recovery paths are dangerous because systems are often tempted to relax normal rules in order to restore service.

VRP follows the opposite principle.

Recovery must not convert:

    stale
      ->
    current

or:

    replay
      ->
    new execution

or:

    unauthorized
      ->
    authoritative

or:

    rejected
      ->
    canonical

The recovery path remains subject to canonical validation.

---

# Fail Closed

Continuity is preserved only while correctness remains defensible.

If the runtime cannot establish required execution validity:

**execution should stop rather than silently corrupt canonical state.**

Conceptually:

    VALID
      |
      v
    CONTINUE

    INVALID / UNPROVABLE
      |
      v
    REJECT

VRP does not pursue an immortal-session model.

A session that cannot safely continue should fail.

The objective is:

**correct continuity, not continuity at any cost.**

---

# Canonical State

VRP treats accepted execution as canonical state.

A rejected operation must not become part of accepted canonical history merely because it reached the runtime.

Conceptually:

    INPUT
      |
      v
    VALIDATION
      |
      +-------- REJECT --------> NO CANONICAL MUTATION
      |
      v
    ACCEPT
      |
      v
    CANONICAL COMMIT

This distinction is central to the architecture.

The runtime must be able to distinguish:

- observed work
- attempted work
- rejected work
- accepted work
- canonical work

Those categories are not interchangeable.

---

# Historical Work

Distributed systems frequently receive work after the context that created it has already disappeared.

VRP explicitly models this problem.

Examples include:

- delayed packets
- queued asynchronous work
- retry activity
- stale callbacks
- delayed control messages
- previous session lifetimes
- previous authority generations

Historical work may still be structurally valid.

It may still contain authentic data.

It may still reference the same logical SessionID.

That does not make it current.

The runtime must determine whether the execution context itself remains authoritative.

---

# Replay and Duplicate Execution

Replay resistance and duplicate containment are part of the continuity model.

A runtime preserving session identity while executing the same logical operation twice has not preserved correct continuity.

Therefore:

    CONTINUITY
        !=
    ACCEPT EVERYTHING THAT ARRIVES

Replay, duplication and historical execution must remain subject to canonical admission.

---

# Transport Replacement

Transport is intentionally treated as replaceable.

Depending on deployment, underlying connectivity may involve technologies such as:

- TCP
- UDP
- QUIC
- tunnels
- VPN transports
- relay paths
- mobile networks
- Wi-Fi
- wired networks
- multipath systems
- application-specific transports

VRP does not require every transport to provide the same capabilities.

The continuity layer governs logical execution independently from the identity of the underlying transport.

---

# VRP Does Not Claim to Have Invented Migration

This distinction is important.

**VRP does not claim to have invented connection migration, roaming, multipath networking or transport failover.**

Existing technologies already solve important parts of those problems.

Examples include:

- QUIC connection migration
- Multipath TCP
- VPN roaming
- tunnel rebinding
- application reconnect
- distributed failover mechanisms

VRP addresses a different architectural boundary.

The question is not merely:

> Can traffic move to another path?

The question is:

> What happens to canonical session lifecycle, authority, replay state and execution history while that happens?

---

# VRP Is Not QUIC

QUIC is a transport protocol with capabilities including secure transport, multiplexed streams and connection migration.

VRP is not intended to replace QUIC.

The architectural responsibilities are different.

A simplified relationship may look like:

    APPLICATION
        |
        v
    VRP CONTINUITY STATE
        |
        v
    QUIC / UDP / OTHER TRANSPORT
        |
        v
    NETWORK

QUIC may provide transport capabilities underneath a VRP deployment.

VRP is concerned with logical continuity above the transport identity.

---

# VRP Is Not MPTCP

Multipath TCP allows a TCP connection to use multiple network paths.

That is valuable transport functionality.

VRP does not attempt to redefine that mechanism.

Its concern is different:

    PATH CONTINUITY
          !=
    CANONICAL SESSION CONTINUITY

A multipath-capable transport can potentially exist underneath VRP.

---

# VRP Is Not WireGuard

WireGuard provides an encrypted network tunnel.

VRP is not a replacement for WireGuard.

A secure tunnel and a canonical continuity runtime solve different problems.

A deployment could theoretically use an encrypted tunnel as one of the underlying transport environments while VRP governs higher-level session continuity.

---

# VRP Is Not "Reconnect With Extra Steps"

Reconnect generally reconstructs communication after connectivity has been lost.

VRP's architectural problem begins before and after that event.

It must reason about:

    WHO IS CURRENT?

    WHICH LIFETIME IS CURRENT?

    WHICH AUTHORITY IS CURRENT?

    WHICH WORK IS HISTORICAL?

    WHICH EXECUTION BECOMES CANONICAL?

    WHAT SURVIVES TRANSPORT REPLACEMENT?

    WHAT MUST BE REJECTED?

A successful socket reconnect does not answer those questions.

---

# A Different Layer

The easiest way to understand VRP is not as another transport.

Think of it as a continuity runtime positioned between application execution and replaceable connectivity.

Conceptually:

    ┌──────────────────────────────┐
    │         APPLICATION          │
    └──────────────┬───────────────┘
                   │
                   v
    ┌──────────────────────────────┐
    │     VRP CONTINUITY LAYER     │
    │                              │
    │  session identity            │
    │  lifecycle                   │
    │  canonical state             │
    │  authority                   │
    │  recovery                    │
    │  validation                  │
    └──────────────┬───────────────┘
                   │
                   v
    ┌──────────────────────────────┐
    │    REPLACEABLE TRANSPORT     │
    │                              │
    │ TCP / UDP / QUIC / tunnel /  │
    │ relay / mobile / Wi-Fi / ... │
    └──────────────┬───────────────┘
                   │
                   v
               NETWORK

This diagram describes architectural responsibility.

It does not disclose the protected runtime implementation.

---

# Integration Model

VRP is intended to integrate with existing infrastructure rather than require the entire network stack to be replaced.

A conceptual deployment boundary is:

    EXISTING APPLICATION
            |
            v
    VRP RUNTIME BOUNDARY
            |
            v
    EXISTING NETWORK / TRANSPORT

The exact integration model depends on the target environment.

VRP may be positioned around session-sensitive execution where continuity requirements justify an independent state layer.

Potential environments include systems affected by:

- unstable client connectivity
- mobile network transitions
- roaming
- long-lived logical sessions
- distributed authority
- transport failover
- network partitions
- infrastructure restart
- continuity-sensitive workloads

This repository intentionally does not publish protected integration internals.

---

# Where VRP May Matter

VRP is most relevant when reconnecting is not equivalent to restoring correct execution.

Examples of environments that may need stronger continuity semantics include:

- distributed control systems
- long-lived remote sessions
- mobile infrastructure
- edge systems
- industrial connectivity
- remote operations
- continuity-sensitive services
- distributed runtimes
- systems with explicit authority ownership
- environments with frequent path or interface changes

Whether VRP is appropriate for a specific system requires target-environment evaluation.

No universal suitability claim is made.

---

# What VRP Does Not Promise

VRP does not promise:

- perfect networks
- zero packet loss
- zero latency
- infinite availability
- unlimited throughput
- unlimited scale
- immunity to host compromise
- immunity to every denial-of-service attack
- automatic application compatibility
- universal production readiness

VRP's architectural claim is narrower:

> Transport instability should not automatically define logical session identity or bypass canonical execution rules.

Everything beyond that must be qualified in the target environment.

---

# Security Model

VRP treats state correctness as part of the security boundary.

Security-relevant concerns include:

- replay rejection
- duplicate containment
- lifecycle isolation
- authority validation
- stale-authority rejection
- canonical admission
- recovery integrity
- evidence integrity
- fail-closed behavior

Cryptography is necessary for protected communication.

It is not sufficient to solve lifecycle correctness.

A cryptographically valid message may still be:

    HISTORICAL

    REPLAYED

    UNAUTHORIZED

    INVALID FOR CURRENT STATE

Therefore cryptographic validity and canonical execution validity remain separate decisions.

---

# Evidence-First Engineering

VRP development follows an evidence-oriented engineering philosophy.

The desired relationship is:

    CLAIM
      |
      v
    TEST
      |
      v
    OBSERVATION
      |
      v
    EVIDENCE
      |
      v
    VERIFICATION

Engineering confidence should come from reproducible behavior rather than marketing language.

This public repository intentionally does not publish the protected Core's detailed validation corpus, internal regression structure, runtime traces or implementation-specific test procedures.

The purpose of this repository is to document the architecture.

Not to publish a reconstruction manual for the protected runtime.

---

# Public Architecture, Private Implementation

VRP uses a deliberate disclosure boundary.

Public:

- protocol identity
- architectural purpose
- core principles
- conceptual runtime model
- integration boundary
- security objectives
- authorship
- public terminology

Private:

- protected runtime source
- internal algorithms
- implementation-specific authority mechanisms
- protected recovery mechanisms
- internal state-machine details
- private regression corpus
- detailed adversarial scenarios
- runtime implementation techniques

This separation is intentional.

Architecture can be evaluated without requiring the protected implementation to be published.

---

# Why the Implementation Remains Protected

VRP is not being developed as an open-source reference implementation.

The protected runtime represents years of independent engineering work around continuity, lifecycle correctness, authority, recovery, canonical state and adversarial validation.

Publishing architectural principles is useful.

Publishing enough implementation detail to reconstruct the protected runtime is not required for architectural review.

The public boundary therefore answers:

    WHAT PROBLEM DOES VRP ADDRESS?

    WHAT ARCHITECTURAL MODEL DOES IT USE?

    WHERE DOES IT FIT?

    WHAT PROPERTIES DOES IT SEEK TO PRESERVE?

    WHAT DOES IT NOT CLAIM?

The private boundary answers:

    HOW IS THE PROTECTED RUNTIME IMPLEMENTED?

That distinction is deliberate.

---

# No Reconstruction Guide

This repository is not intended to provide a step-by-step implementation guide for reproducing the VRP Core.

It intentionally excludes:

- protected source code
- internal algorithms
- implementation-specific state machines
- detailed recovery procedures
- internal authority mechanisms
- private test harnesses
- detailed adversarial test recipes
- internal runtime traces
- private evidence bundles
- implementation-specific failure catalogs
- protected deployment logic

The absence of these materials is intentional.

The public architecture should explain VRP.

It should not function as a substitute for the protected implementation.

---

# Engineering Status

VRP is an active engineering project.

The architecture has progressed substantially beyond its original conceptual stage.

Development has included work across:

- session continuity
- lifecycle isolation
- canonical state
- authority continuity
- replay containment
- duplicate containment
- transport replacement
- failure recovery
- concurrent execution
- runtime determinism
- evidence generation
- evidence verification
- runtime boundary hardening
- real-network validation

The protected Core continues to evolve.

This repository should not be interpreted as a frozen description of every private implementation detail.

It defines the public architectural identity of the project.

---

# Current Development Direction

The current engineering direction is increasingly focused on hardening rather than expanding the public surface.

The development cycle is intentionally:

    IMPLEMENT
        |
        v
    TEST
        |
        v
    BREAK
        |
        v
    REPRODUCE
        |
        v
    FIX
        |
        v
    REGRESSION TEST
        |
        v
    HARDEN

The objective is not to maximize the number of publicly visible features.

The objective is to reduce the number of assumptions capable of violating canonical continuity.

---

# External Reality Is the Next Boundary

Internal engineering can establish only part of the required confidence.

A continuity architecture ultimately has to face environments controlled by somebody else.

That means:

- real infrastructure
- real workloads
- real network transitions
- real outages
- real operational constraints
- real concurrency
- real deployment requirements
- real failure conditions

The next important qualification boundary is therefore controlled external evaluation.

---

# Target-Environment Qualification

VRP does not claim universal production readiness.

Production suitability is target-environment dependent.

A serious deployment should establish whether the required VRP properties remain valid under its own:

- network topology
- transport stack
- applications
- latency profile
- failure model
- concurrency
- scale
- security requirements
- operational procedures
- infrastructure constraints

The correct question is not:

> Is VRP production ready everywhere?

The correct question is:

> Does this VRP build satisfy the required invariants in this target environment?

That requires evaluation.

---

# Controlled Evaluation

A serious VRP evaluation should be capable of producing a negative result.

Possible outcomes may include:

    ACCEPTED

    ACCEPTED WITH CONDITIONS

    NOT ACCEPTED

The purpose of evaluation is not to manufacture a successful demonstration.

The purpose is to discover whether the architecture survives the environment where it is expected to operate.

---

# Integration Principle

VRP is intended to integrate with existing infrastructure rather than require an organization to replace every networking technology it already uses.

Conceptually:

    APPLICATION / SERVICE
             |
             v
    VRP CONTINUITY BOUNDARY
             |
             v
    EXISTING TRANSPORT STACK
             |
             v
    EXISTING NETWORK

Existing technologies may continue providing:

- transport
- encryption
- congestion control
- retransmission
- tunneling
- routing
- multipath
- connection migration

VRP adds a separate concern:

**canonical logical continuity across transport instability.**

---

# Adoption Does Not Require Replacing the Internet Stack

VRP should not be understood as:

    REMOVE TCP

or:

    REMOVE QUIC

or:

    REMOVE WIREGUARD

or:

    REBUILD THE NETWORK

The architectural proposition is different.

Existing connectivity remains useful.

VRP introduces a continuity boundary where an application or infrastructure system requires logical state to survive transport changes without allowing transport events to redefine canonical execution.

---

# Conceptual Deployment

A simplified conceptual deployment may look like:

    ┌─────────────────────────────┐
    │      Application Logic      │
    └──────────────┬──────────────┘
                   │
                   │ logical operations
                   v
    ┌─────────────────────────────┐
    │      VRP Runtime Boundary   │
    │                             │
    │ session                     │
    │ lifecycle                   │
    │ canonical state             │
    │ authority                   │
    │ continuity                  │
    │ recovery                    │
    └──────────────┬──────────────┘
                   │
                   │ transport binding
                   v
    ┌─────────────────────────────┐
    │ Existing Connectivity Layer │
    │                             │
    │ QUIC / UDP / TCP / tunnel / │
    │ relay / mobile / Wi-Fi /    │
    │ other deployment transport  │
    └──────────────┬──────────────┘
                   │
                   v
                Network

This is an architectural diagram.

It is not an implementation specification.

---

# What Organizations Should Evaluate

An organization considering VRP should first determine whether it actually has a continuity problem.

Questions include:

- Do logical sessions outlive individual network connections?
- Are clients frequently changing networks?
- Does reconnect reconstruct important execution state?
- Can stale work arrive after recovery?
- Can duplicated execution create operational consequences?
- Does authority move between components?
- Can an old authority reappear after partition or restart?
- Is session continuity important across interface changes?
- Is canonical execution state more important than uninterrupted connectivity?
- Is evidence of recovery behavior required?

If the answer to these questions is largely no, VRP may not be necessary.

VRP is intended for systems where continuity semantics matter enough to justify an independent runtime boundary.

---

# What Organizations Should Not Assume

Reading this repository does not establish that VRP is appropriate for a specific deployment.

Likewise, architectural compatibility does not establish:

- required performance
- required scale
- required latency
- application compatibility
- regulatory compliance
- security certification
- operational suitability

Those properties require separate qualification.

---

# No Universal Benchmark Claim

Public architectural documentation should not be confused with a benchmark specification.

Individual engineering results may demonstrate that a scenario has been exercised.

They do not automatically define:

    MAXIMUM SCALE

    MAXIMUM THROUGHPUT

    MINIMUM LATENCY

    UNIVERSAL CAPACITY

    UNIVERSAL DEPLOYMENT LIMIT

Those values depend on implementation, hardware, topology, workload and deployment configuration.

---

# No Formal-Proof Claim

VRP uses extensive engineering validation.

Unless explicitly stated in a separate artifact, this repository does not claim complete mathematical formal verification of the entire protected runtime.

The current assurance model includes engineering techniques such as:

- deterministic testing
- adversarial testing
- failure injection
- concurrency testing
- race-oriented testing
- fuzzing
- regression testing
- long-duration validation
- real-network testing
- evidence verification

These techniques provide engineering evidence.

They should not be described as a complete formal proof.

---

# No Security-Certification Claim

Likewise, this repository does not claim that VRP has received universal external security certification.

Security assurance has multiple levels.

They may include:

    INTERNAL ENGINEERING VALIDATION

    INDEPENDENT EVIDENCE VERIFICATION

    SOURCE REVIEW

    PENETRATION TESTING

    CRYPTOGRAPHIC REVIEW

    FORMAL VERIFICATION

    DEPLOYMENT SECURITY REVIEW

    CERTIFICATION

These are different activities.

One should not be substituted for another.

---

# Public Claims Should Remain Bounded

VRP intentionally prefers bounded engineering statements.

For example:

Better:

> This property was preserved under the tested scenario.

Not:

> This can never fail.

Better:

> Replay was rejected under the validated execution model.

Not:

> Replay is impossible under every conceivable deployment.

Better:

> Controlled external qualification is the next deployment boundary.

Not:

> Every production environment is already qualified.

Precision matters.

---

# Authorship and Origin

**Veil Routing Protocol (VRP)** is an independent protocol concept, runtime architecture and engineering project developed by:

**Vitalijus Riabovas**

Development and architectural work represented by the project spans:

**2024–2026**

The project evolved from earlier work associated with the **Jumping VPN** name into the broader **Veil Routing Protocol** architecture.

VRP includes original project-specific engineering work around the combination of:

- transport-independent session continuity
- explicit session lifecycle
- canonical execution state
- authority continuity
- recovery semantics
- stale-work rejection
- replay containment
- deterministic runtime behavior
- evidence-oriented validation

This repository serves as the canonical public architectural and authorship record for the VRP project.

---

# Important Authorship Boundary

The authorship statement above applies to the **VRP project, its specific architecture, terminology, engineering model and implementation work**.

It is not a claim that the project invented every underlying networking concept it uses.

Concepts such as:

- connection migration
- multipath networking
- session management
- replay protection
- failover
- distributed authority
- state machines
- cryptographic authentication

have extensive prior history across networking and distributed systems.

VRP's contribution is the specific architecture and engineering model developed around its continuity problem.

This distinction is intentional.

---

# Prior Art and Attribution

VRP does not depend on pretending that existing networking research does not exist.

Where established mechanisms solve part of the problem, they should be recognized.

The project can coexist conceptually with existing transport and security technologies.

At the same time, the specific VRP architecture, documentation, terminology and protected implementation represent the work of the VRP project.

If this work is referenced, discussed or built upon, appropriate attribution to **Vitalijus Riabovas / Veil Routing Protocol** is requested.

---

# Repository Purpose

This repository exists to provide one canonical public location for:

- VRP identity
- VRP architectural purpose
- public terminology
- authorship
- conceptual integration
- architectural boundaries
- security objectives
- public project status

It is intentionally not intended to become a continuously expanding dump of private engineering artifacts.

---

# Repository Policy

The public surface may remain intentionally small.

Not every internal engineering change will result in:

- a public commit;
- a public report;
- a public test log;
- a public evidence bundle;
- a public implementation explanation.

Absence of public implementation updates does not imply absence of private development.

The protected Core has a separate lifecycle.

---

# Protected Core

The production-oriented VRP Core implementation is maintained privately.

The protected runtime contains implementation details that are intentionally outside this repository.

This public repository should therefore be read as:

    ARCHITECTURE

not:

    SOURCE RELEASE

and as:

    PUBLIC TECHNICAL BOUNDARY

not:

    IMPLEMENTATION BLUEPRINT

---

# Source Availability

The protected VRP Core source code is not publicly distributed through this repository.

Access to public architectural documentation should not be interpreted as access to:

- private source code
- protected runtime builds
- internal validation infrastructure
- private engineering artifacts
- proprietary implementation mechanisms

Any controlled access or evaluation arrangement, if offered, is handled separately.

---

# Licensing

No open-source license is granted merely by making this repository publicly readable.

Unless a specific file or component explicitly states otherwise, publication should not be interpreted as permission to reproduce, modify, redistribute or commercially repackage protected project material.

Third-party rights remain with their respective owners.

For any intended use beyond ordinary viewing, referencing or evaluation of the public material, appropriate permission should be obtained.

---

# Public Documentation Is Not a Patent Grant

Publication of architectural information in this repository should not be interpreted as granting patent rights, trademark rights, proprietary implementation rights or any other rights not explicitly granted.

This repository primarily establishes a public technical record and provides architectural information about VRP.

---

# Project Identity

Canonical project name:

**Veil Routing Protocol**

Abbreviation:

**VRP**

Earlier development name:

**Jumping VPN**

Core principle:

**SESSION ≠ TRANSPORT**

Engineering principle:

**CONTINUITY FIRST.**

---

# Public Communication

VRP development does not depend on continuous public posting.

Engineering work may continue without corresponding social-media activity or detailed public reporting.

Public silence should not be interpreted as abandonment of the protected Core.

The project may deliberately prioritize:

    ENGINEERING
        >
    CONTENT

    VALIDATION
        >
    ATTENTION

    IMPLEMENTATION
        >
    MARKETING

---

# Serious Evaluation

Organizations with a concrete technical reason to evaluate VRP should approach the project with a defined engineering context.

Useful information includes:

- target environment
- continuity problem
- existing transport architecture
- failure modes
- application requirements
- expected scale
- security requirements
- evaluation objective

A meaningful technical discussion begins with a real deployment problem.

Not with a request for the private Core implementation.

---

# Evaluation Boundary

The preferred external relationship is:

    ORGANIZATION
         |
         v
    DEFINED PROBLEM
         |
         v
    CONTROLLED EVALUATION
         |
         v
    TARGET ENVIRONMENT
         |
         v
    OBSERVABLE RESULT
         |
         v
    ENGINEERING DECISION

The objective is to evaluate VRP where it would actually matter.

---

# What Comes Next

The architecture has been defined.

The protected runtime exists.

The internal engineering cycle continues.

The next meaningful question is no longer:

> Can another document explain VRP?

It is:

> What happens when VRP enters infrastructure that the project does not control?

That is the next boundary.

---

# A Note to Engineers

Do not accept the architecture because this README says it works.

Challenge the assumptions.

Ask where identity lives.

Ask what happens when transport disappears.

Ask what happens when historical work returns.

Ask who owns authority after recovery.

Ask what becomes canonical.

Ask what must be rejected.

Ask what happens under concurrency.

Ask what evidence would demonstrate the result.

Those are the questions VRP itself was built around.

---

# The Short Version

If only one section of this repository is remembered, it should be this:

    TRANSPORT CAN CHANGE.

    SESSION IDENTITY DOES NOT HAVE TO CHANGE WITH IT.

    CONNECTIVITY DOES NOT DEFINE AUTHORITY.

    HISTORICAL WORK IS NOT CURRENT WORK.

    RECOVERY DOES NOT BYPASS VALIDATION.

    REJECTED EXECUTION IS NOT CANONICAL EXECUTION.

    CONTINUITY IS PRESERVED ONLY WHILE CORRECTNESS HOLDS.

That is VRP.

---

# Final Statement

The networking problem is not simply that connections fail.

Connections have always failed.

The harder problem is deciding what remains true after they do.

VRP treats that as a first-class runtime problem.

The transport may disappear.

The path may change.

The network may recover.

But the runtime must still answer:

    Is this the same valid session?

    Is this the current lifetime?

    Is this the current authority?

    Is this execution valid?

    Is this state canonical?

    Can the result be verified?

That is the architectural boundary.

---

# Veil Routing Protocol

**Developed by Vitalijus Riabovas**

**Independent engineering project — 2024–2026**

Public architecture.

Protected implementation.

Target-environment qualification.

No universal claims.

No reconstruction guide.

No requirement to replace existing transport technology.

Just one fundamental separation:

# SESSION ≠ TRANSPORT

# CONTINUITY FIRST.

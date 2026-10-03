# Veil Routing Protocol — Public Security Model

**Project:** Veil Routing Protocol (VRP)  
**Author:** Vitalijus Riabovas  
**Development:** 2024–2026  
**Status:** Public Security Model  
**Implementation:** Protected / Private

> **SESSION ≠ TRANSPORT**

> **CONTINUITY FIRST.**

---

# 1. Purpose

This document defines the public security model of the **Veil Routing Protocol (VRP)**.

It describes:

- security objectives;
- architectural trust boundaries;
- continuity-related threats;
- authority requirements;
- lifecycle isolation;
- replay and duplicate concerns;
- recovery security;
- canonical-state protection;
- cryptographic boundaries;
- evidence integrity;
- fail-closed behavior;
- security limitations.

This document intentionally does not publish:

- cryptographic material;
- private keys;
- protected runtime source code;
- internal algorithms;
- detailed state-machine transitions;
- implementation-specific authority mechanisms;
- protected recovery procedures;
- attack recipes;
- private validation infrastructure.

The objective is to explain **what security properties VRP seeks to preserve**, not to disclose **how the protected Core implements them**.

---

# 2. Security Philosophy

VRP treats continuity correctness as security-relevant state.

A system is not considered secure merely because its packets are encrypted.

A system may use strong cryptography and still execute:

- stale work;
- replayed work;
- duplicated work;
- obsolete authority;
- invalid recovery;
- historical session state.

Therefore:

    SECURE TRANSPORT

           !=

    SECURE CONTINUITY

VRP treats both as important.

---

# 3. Primary Security Objective

The primary VRP security objective is:

> Preserve valid canonical session execution across transport instability without allowing stale, replayed, duplicated, unauthorized or historically invalid execution to become current canonical state.

This objective applies independently from whether the underlying network remains continuously available.

---

# 4. Security Priorities

The public architecture follows the priority:

    CORRECTNESS
        >
    CONNECTIVITY

and:

    VALIDATED CONTINUITY
        >
    CONTINUITY AT ANY COST

If continuity cannot be safely established, the architecture prefers rejection or terminal failure over silent canonical corruption.

---

# 5. Security-Relevant State

VRP treats several categories of runtime state as security-relevant.

These include:

- logical session identity;
- session lifecycle;
- current authority;
- canonical execution state;
- replay state;
- transport binding;
- recovery state;
- terminal state;
- evidence state.

Compromise or ambiguity in these areas may affect continuity correctness.

---

# 6. Session Identity

Transport identity must not be treated as sufficient proof of logical session identity.

For example:

    NETWORK ADDRESS

        !=

    SESSION IDENTITY

and:

    SOCKET

        !=

    SESSION IDENTITY

and:

    CURRENT PATH

        !=

    SESSION IDENTITY

Transport properties may contribute to communication.

They do not independently define canonical logical identity.

---

# 7. Lifecycle Isolation

A logical session may have more than one execution lifetime over its history.

Therefore:

    SAME SESSION ID

          !=

    SAME EXECUTION LIFETIME

Historical work associated with an older lifetime must remain distinguishable from work associated with the current lifetime.

This distinction is security-relevant because delayed historical execution must not silently regain validity.

---

# 8. Historical Execution Threat

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
       |
       v
    CURRENT

Later:

    DELAYED WORK
    FROM LIFETIME 1
           |
           v
       SESSION S

The SessionID may be correct.

The execution context is not.

VRP requires the runtime to preserve this distinction.

---

# 9. Replay Threat

A previously valid operation may be presented again.

The security question is not only:

> Is the message structurally valid?

It is also:

> Is this execution valid now?

Therefore:

    ONCE VALID

        !=

    ALWAYS VALID

Replay containment is part of canonical continuity.

---

# 10. Duplicate Execution Threat

Network and distributed-system behavior may cause the same logical operation to be observed more than once.

VRP distinguishes:

    DUPLICATE DELIVERY

from:

    DUPLICATE CANONICAL EXECUTION

The architecture must prevent duplicate observation from silently producing duplicate canonical execution where singular execution is required.

---

# 11. Stale Authority Threat

Authority may move during:

- failover;
- restart;
- recovery;
- partition;
- infrastructure replacement;
- ownership transition.

A previously authoritative component may later return.

Therefore:

    PREVIOUSLY AUTHORITATIVE

             !=

    CURRENTLY AUTHORITATIVE

The architecture must preserve this distinction.

---

# 12. Reachability Is Not Authority

A reachable component is not automatically trusted to execute current work.

Therefore:

    REACHABLE

        !=

    AUTHORITATIVE

This is particularly important after recovery.

An old component may successfully reconnect while remaining logically stale.

---

# 13. Transport Recovery Threat

A previously unavailable transport may return.

Its return does not automatically restore its previous logical status.

Similarly, a replacement transport becoming available does not automatically prove that the logical session may continue.

The architecture requires continuity validation independently from transport availability.

---

# 14. Recovery Threat

Recovery is one of the highest-risk execution boundaries.

A dangerous architecture may effectively implement:

    FAILURE

       ↓

    RECOVERY

       ↓

    RELAX RULES

       ↓

    ACCEPT STATE

VRP requires the opposite:

    FAILURE

       ↓

    RECOVERY

       ↓

    APPLY VALIDATION

       ↓

    ACCEPT OR REJECT

Recovery is not a privileged bypass around correctness.

---

# 15. Canonical-State Protection

VRP distinguishes:

    OBSERVED

from:

    ACCEPTED

and:

    ACCEPTED

from:

    CANONICAL

A rejected operation must not become part of canonical state merely because the runtime observed it.

The architectural requirement is:

## REJECTED EXECUTION MUST NOT MUTATE CANONICAL EXECUTION STATE

---

# 16. Admission Boundary

Security-sensitive execution passes through a logical admission boundary.

Conceptually:

    INPUT
      |
      v
    VALIDATION
      |
      +---------- REJECT ----------> NO CANONICAL ADMISSION
      |
      v
    ACCEPT
      |
      v
    CANONICAL EXECUTION

The protected implementation determines the internal mechanics of this boundary.

The public model defines the required property.

---

# 17. Fail-Closed Behavior

When the runtime cannot establish required validity, it should not guess.

Conceptually:

    VALIDITY ESTABLISHED
            |
            v
         CONTINUE

    VALIDITY NOT ESTABLISHED
            |
            v
    REJECT / STOP / QUARANTINE

This is the VRP fail-closed principle.

---

# 18. Availability Is Not the Highest Priority

Fail-closed behavior may temporarily reduce availability.

That is intentional.

The alternative may be continued execution with ambiguous authority or canonical state.

VRP therefore does not claim:

> The session must always continue.

The requirement is:

> The session may continue only while required correctness remains established.

---

# 19. Cryptographic Security

Cryptography is an important part of secure communication.

Depending on deployment and implementation, cryptographic mechanisms may provide properties such as:

- confidentiality;
- integrity;
- authenticity;
- tamper detection;
- protected message binding.

However, cryptography does not independently solve the complete VRP continuity problem.

---

# 20. Cryptographic Validity vs Runtime Validity

A message may be cryptographically authentic and still be:

- stale;
- historical;
- duplicated;
- replayed;
- associated with obsolete authority;
- invalid in the current runtime state.

Therefore:

    AUTHENTIC MESSAGE

          !=

    AUTHORIZED CURRENT EXECUTION

Both cryptographic and runtime validity may be required.

---

# 21. Key Material

Private cryptographic material is not part of the public architecture.

This repository does not publish:

- private keys;
- production secrets;
- protected key derivation material;
- deployment credentials;
- operational secret-management procedures.

Any production deployment requires an appropriate key-management model for its environment.

---

# 22. Transport Security

VRP does not require organizations to abandon mature secure transport technologies.

Depending on the environment, secure connectivity may be provided by technologies such as:

- QUIC;
- TLS;
- WireGuard;
- IPsec;
- protected tunnels;
- other authenticated transport mechanisms.

VRP continuity security exists in addition to appropriate transport security.

---

# 23. Transport Replacement

When transport changes, the security architecture must avoid the assumption:

    NEW TRANSPORT
         =
    NEW AUTHORITY

Likewise:

    OLD TRANSPORT RETURNS
         =
    OLD AUTHORITY RETURNS

Neither relationship is valid automatically.

Transport binding and logical authority remain separate concerns.

---

# 24. Path Migration

Path migration is not itself a security proof.

A successful path migration establishes that communication moved.

It does not automatically establish that:

- lifecycle remained valid;
- authority remained valid;
- no historical execution entered;
- no duplicate became canonical;
- no replay was accepted.

These remain continuity-layer responsibilities.

---

# 25. NAT and Address Changes

Network addresses are unstable identifiers.

A legitimate endpoint may change address because of:

- NAT rebinding;
- CGNAT behavior;
- roaming;
- interface change;
- mobile transition;
- infrastructure change.

Therefore VRP does not treat network address stability as equivalent to logical session identity.

At the same time, an address change must not automatically bypass session validation.

---

# 26. Concurrency

Concurrency can expose security-relevant state races.

Examples include races between:

- execution and termination;
- recovery and stale work;
- authority transition and old authority;
- transport replacement and old transport activity;
- duplicate operations;
- competing recovery paths.

The architecture requires canonical outcomes despite concurrent activity.

The protected implementation determines the synchronization mechanisms.

---

# 27. Determinism

Where a security decision depends on runtime state, nondeterministic ambiguity can become dangerous.

VRP engineering therefore treats deterministic state behavior as an important property where applicable.

This does not mean that network timing itself is deterministic.

It means that equivalent valid runtime conditions should not arbitrarily produce conflicting canonical outcomes.

---

# 28. Terminal State

Some runtime conditions must remain terminal.

A component or session that has entered a terminal state must not silently return to valid execution merely because connectivity changes.

Conceptually:

    TERMINAL

       !=

    TEMPORARILY DISCONNECTED

This distinction protects against resurrection of invalid execution.

---

# 29. Resurrection Threat

A dangerous condition occurs when previously terminated state becomes active again without a new valid lifecycle transition.

Conceptually:

    ACTIVE
      |
      X
    TERMINATED
      |
      v
    OLD STATE RETURNS
      |
      v
    ACTIVE AGAIN

VRP treats unauthorized resurrection as a continuity failure.

---

# 30. State Exposure

Security is affected not only by mutation but also by exposure.

Public or integration-facing runtime surfaces should not unintentionally expose mutable internal state in a way that allows external modification of canonical structures.

The exact protected memory and API isolation mechanisms are implementation-specific.

The architectural principle is:

> Observation of state must not implicitly grant authority to mutate canonical state.

---

# 31. Component Boundaries

Internal components may legitimately share identity or runtime relationships.

That does not mean external callers should be able to bypass canonical admission by reaching those components directly.

A secure integration boundary should preserve the distinction between:

    INTERNAL COMPOSITION

and:

    EXTERNAL AUTHORITY

---

# 32. Input Validation

External or integration-facing input must be treated as untrusted unless explicitly established otherwise.

Potentially relevant categories include:

- malformed input;
- unexpected state transitions;
- duplicate input;
- historical input;
- replayed input;
- invalid identifiers;
- inconsistent metadata;
- unsupported transitions.

The exact parser and validation implementation is private.

---

# 33. Malformed Input

Malformed input should not be capable of silently corrupting canonical state.

Depending on context, appropriate outcomes may include:

- rejection;
- error;
- quarantine;
- connection termination;
- session termination.

The correct outcome depends on the deployment and failure model.

---

# 34. Evidence Security

Evidence can support evaluation of runtime behavior.

However, evidence itself has security requirements.

Relevant properties may include:

- integrity;
- completeness;
- provenance;
- ordering;
- binding to the evaluated execution;
- resistance to unnoticed modification.

VRP treats evidence integrity as separate from runtime correctness.

---

# 35. Evidence Integrity Is Not Evidence Authenticity

A critical distinction is:

    EVIDENCE INTEGRITY

          !=

    EVIDENCE SOURCE AUTHENTICITY

A verifier may establish that an evidence bundle is internally consistent without independently proving who originally generated every underlying event.

Therefore claims about evidence must remain precise.

---

# 36. Evidence Verification Is Not Source Review

Likewise:

    VERIFIED EVIDENCE

          !=

    VERIFIED SOURCE CODE

Evidence verification evaluates evidence.

Source review evaluates implementation.

Formal verification evaluates mathematical properties under a defined model.

Penetration testing evaluates another set of security properties.

These forms of assurance should not be conflated.

---

# 37. Evidence Does Not Replace Independent Security Review

VRP's evidence-oriented engineering approach is intended to improve observability and reproducibility.

It does not eliminate the value of:

- independent source review;
- cryptographic review;
- penetration testing;
- deployment review;
- infrastructure review;
- formal methods where appropriate.

A serious production deployment may require several of these.

---

# 38. Threat Categories

The public VRP architecture considers threat categories including:

### Continuity Threats

- transport loss;
- transport replacement;
- stale transport return;
- recovery races.

### Lifecycle Threats

- historical lifetime activity;
- invalid resurrection;
- stale work.

### Execution Threats

- replay;
- duplication;
- invalid admission.

### Authority Threats

- stale authority;
- conflicting authority;
- authority rollback.

### State Threats

- canonical-state contamination;
- invalid recovery;
- unintended mutation.

### Evidence Threats

- evidence modification;
- inconsistent evidence;
- misleading evidence interpretation.

This list is not claimed to be exhaustive.

---

# 39. Network Attacker

A network attacker may attempt to:

- observe traffic;
- delay traffic;
- duplicate traffic;
- reorder traffic;
- replay traffic;
- interrupt connectivity;
- manipulate available paths.

The degree to which these threats are mitigated depends on both VRP and the security properties of the underlying transport environment.

---

# 40. Host Compromise

VRP does not claim immunity to complete compromise of a trusted execution host.

An attacker controlling:

- the operating system;
- process memory;
- privileged runtime execution;
- cryptographic secrets;

may exceed the assumptions of the continuity architecture.

Host security therefore remains a separate deployment responsibility.

---

# 41. Denial of Service

VRP does not claim that every denial-of-service attack can be prevented.

An attacker may attempt to exhaust:

- CPU;
- memory;
- network capacity;
- connection capacity;
- runtime queues;
- evidence storage.

Resource-bounded behavior and deployment-level DoS controls require target-specific qualification.

---

# 42. Traffic Analysis

Encrypted content does not necessarily hide all observable metadata.

Potentially observable characteristics may include:

- timing;
- packet size;
- communication frequency;
- endpoint behavior;
- traffic volume.

VRP does not claim universal resistance to traffic analysis.

Such requirements must be evaluated separately.

---

# 43. Application Vulnerabilities

VRP does not protect an application from every vulnerability in its own logic.

Examples outside the core continuity responsibility may include:

- injection vulnerabilities;
- broken access control;
- insecure business logic;
- unsafe file handling;
- application-level privilege escalation.

Application security remains necessary.

---

# 44. Social Engineering and Credential Theft

VRP does not eliminate human or operational security risks.

Examples include:

- credential theft;
- phishing;
- malicious administrators;
- insecure secret storage;
- accidental disclosure.

These require organizational controls beyond the continuity protocol.

---

# 45. Supply-Chain Security

Production security also depends on:

- build systems;
- dependencies;
- operating systems;
- deployment pipelines;
- artifact distribution;
- update mechanisms.

The public VRP architecture does not claim to secure the entire software supply chain automatically.

---

# 46. Deployment Trust Model

Every deployment must identify:

- trusted components;
- untrusted components;
- privileged components;
- authority holders;
- secret holders;
- evidence producers;
- evidence consumers;
- network assumptions.

A security model without explicit deployment assumptions is incomplete.

---

# 47. Security Qualification

A target deployment should evaluate VRP against its own threat model.

Relevant questions may include:

- Which attackers matter?
- Which assets matter?
- Which state must remain canonical?
- Which components may fail?
- Which components may be malicious?
- Which authority transitions are possible?
- Which recovery paths exist?
- Which network failures are realistic?
- What evidence is required?
- What constitutes terminal failure?

The answers differ between environments.

---

# 48. Security Testing

A serious evaluation may include techniques such as:

- adversarial testing;
- fuzzing;
- malformed-input testing;
- replay testing;
- duplicate testing;
- concurrency testing;
- recovery testing;
- failure injection;
- authority-transition testing;
- long-duration testing;
- resource-pressure testing;
- race detection;
- evidence-integrity testing.

The protected VRP validation corpus is not published through this repository.

---

# 49. Negative Results

A security test is useful only if failure is allowed to be reported.

VRP therefore treats negative findings as engineering input.

The preferred process is:

    TEST
      |
      v
    FAILURE FOUND
      |
      v
    REPRODUCE
      |
      v
    UNDERSTAND
      |
      v
    FIX
      |
      v
    REGRESSION TEST

A discovered defect is not made safer by hiding it from the engineering process.

---

# 50. Regression Security

When a security-relevant defect is corrected, the associated failure condition should become a regression boundary where practical.

The purpose is to prevent the same class of defect from silently returning during later development.

This principle is part of VRP's engineering methodology.

---

# 51. Security Claims Must Be Bounded

VRP avoids universal claims such as:

    UNHACKABLE

    IMPOSSIBLE TO BREAK

    PERFECT SECURITY

    ZERO RISK

Such statements are not meaningful engineering guarantees.

A valid security claim should identify:

- the property;
- the environment;
- the assumptions;
- the test or analysis;
- the observed result;
- the limitations.

---

# 52. Public vs Protected Security Information

The public repository may describe:

- security objectives;
- architectural invariants;
- threat categories;
- trust boundaries;
- limitations.

The protected implementation may retain:

- exact algorithms;
- detailed state transitions;
- private adversarial scenarios;
- implementation-specific defenses;
- internal evidence structures;
- protected runtime mechanisms.

This disclosure boundary is intentional.

---

# 53. Security Invariants

The public VRP security model can be summarized through several invariants.

### Security Invariant 1

**Transport identity must not define logical session authority.**

### Security Invariant 2

**Historical execution must not silently become current execution.**

### Security Invariant 3

**Replay must not silently become new canonical execution.**

### Security Invariant 4

**Duplicate observation must not automatically become duplicate canonical execution.**

### Security Invariant 5

**Stale authority must not regain current authority merely by becoming reachable.**

### Security Invariant 6

**Recovery must not bypass canonical admission.**

### Security Invariant 7

**Rejected execution must not mutate canonical execution state.**

### Security Invariant 8

**Terminal state must not silently resurrect.**

### Security Invariant 9

**Failure to establish required validity must fail closed.**

---

# 54. Security Decision Model

At the highest public level:

    INPUT / EVENT
         |
         v
    ESTABLISH CONTEXT
         |
         v
    VALIDATE CURRENTNESS
         |
         v
    VALIDATE AUTHORITY
         |
         v
    VALIDATE EXECUTION
         |
         +--------- INVALID ---------> REJECT
         |
         v
    CANONICAL ADMISSION

This is conceptual.

It is not the protected Core algorithm.

---

# 55. Security During Network Change

Network transition should not weaken the security model.

The desired property is:

    NORMAL OPERATION
          |
          v
    NETWORK CHANGE
          |
          v
    SAME SECURITY BOUNDARIES
          |
          v
    VALIDATED CONTINUATION
       OR
    FAIL CLOSED

Network instability is not permission to relax execution validity.

---

# 56. Security During Recovery

Likewise:

    NORMAL VALIDATION

should not become:

    WEAKER VALIDATION

simply because the runtime is recovering.

Recovery is precisely where stale and conflicting state may become most dangerous.

---

# 57. Security During Failover

Failover must preserve authority semantics.

A successful failover is not merely:

    NEW NODE ONLINE

It must also establish:

    OLD AUTHORITY NO LONGER CURRENT

where required by the deployment model.

The exact protected authority mechanism is not publicly specified.

---

# 58. Security During Transport Migration

Transport migration should preserve the distinction:

    TRANSPORT CHANGED

          !=

    AUTHORITY CHANGED

and:

    TRANSPORT CHANGED

          !=

    SESSION LIFETIME CHANGED

Those transitions may occur together in some systems, but they are not architecturally equivalent.

---

# 59. Security During Restart

Process or infrastructure restart can create ambiguity around old state.

A secure deployment must define how current state is distinguished from historical state after restart.

VRP treats restart and recovery as security-relevant continuity events.

---

# 60. Security Review Boundary

A future external security review should not be constrained to asking:

> Is the cryptography correct?

It should also ask:

- Can historical work execute?
- Can authority roll backward?
- Can a terminal session resurrect?
- Can rejected work alter canonical state?
- Can recovery bypass admission?
- Can duplicate work execute twice?
- Can external state exposure mutate internals?
- Can concurrency produce conflicting canonical outcomes?

These are continuity-security questions.

---

# 61. What This Document Establishes

This document establishes the public security intent of VRP.

It provides enough information for an engineer to understand:

- what VRP considers security-relevant;
- what threat categories matter;
- what invariants the architecture seeks to preserve;
- where cryptography fits;
- where transport security ends;
- where continuity security begins;
- what limitations remain.

It does not provide enough information to reproduce the protected runtime.

---

# 62. Final Security Statement

A network can be encrypted and still be wrong.

A connection can recover and still be wrong.

A message can be authentic and still be stale.

A component can be reachable and still be unauthorized.

A SessionID can match and still refer to historical execution.

A transport can migrate successfully while canonical state fails.

VRP treats these distinctions as part of the security boundary.

The objective is not merely to keep traffic moving.

The objective is to ensure that when execution continues, the runtime still knows:

    WHICH SESSION IS CURRENT

    WHICH LIFETIME IS CURRENT

    WHICH AUTHORITY IS CURRENT

    WHICH WORK IS VALID

    WHICH STATE IS CANONICAL

    AND WHEN CONTINUITY MUST STOP

That is the public VRP security model.

---

# SESSION ≠ TRANSPORT

# CONTINUITY FIRST.

---

**Veil Routing Protocol (VRP)**  
**Vitalijus Riabovas**  
**2024–2026**

Public security model.  
Protected implementation.
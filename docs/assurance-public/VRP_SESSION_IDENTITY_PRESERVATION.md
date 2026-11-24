# VRP Session Identity Preservation

## Veil Routing Protocol — Jumping VPN

**Document ID:** VRP-PA-003
**Version:** 1.0
**Classification:** PUBLIC
**Status:** Normative Qualification Contract
**Author:** Vitalijus Riabovas
**Protected Core:** CONFIDENTIAL

---

## 1. Executive Statement

Conventional connectivity recovery does not
necessarily preserve logical session identity.

A system may successfully reconnect,
restore packet delivery, and resume
application communication while silently
replacing the original logical session.

Veil Routing Protocol establishes a
different architectural contract:

    SESSION ≠ TRANSPORT

Transport availability and logical session
existence are distinct properties.

The objective of this document is to define
how session identity preservation can be
evaluated without exposing proprietary
implementation mechanisms.

This document specifies qualification
requirements rather than asserting universal
implementation correctness.

---

## 2. Assurance Scope

This document addresses:

- Logical session identity preservation.
- Transport-independent session lifetime.
- Authorized endpoint transitions.
- Transport replacement.
- Temporary connectivity loss.
- Recovery identity verification.
- Canonical state preservation.
- Session recreation detection.
- Concurrent transition correctness.
- External black-box qualification.

The document does not disclose internal
algorithms, confidential state structures,
cryptographic mechanisms, or implementation
interfaces.

---

## 3. Fundamental Architectural Distinction

Three properties MUST remain distinguishable:

    CONNECTIVITY
    SESSION IDENTITY
    APPLICATION PROGRESS

Connectivity describes the availability
of a communication path.

Session identity describes the logical
relationship governed by the applicable
session contract.

Application progress describes successful
execution of application-level operations.

These properties may interact.

They MUST NOT be treated as equivalent.

For example, connectivity may temporarily
be unavailable while the logical session
remains valid.

Likewise, restored connectivity does not
independently establish preservation of
the original logical session.

---

## 4. Abstract Session Model

The following symbols are defined solely
for external verification:

    S = logical session identity
    L = logical session lifetime
    T = transport association
    A = canonical authority context
    H = committed canonical history
    P = application progress observation

These symbols are conceptual.

They do not represent actual implementation
variables, internal structures, identifiers,
storage formats, or protocol messages.

An external qualification procedure MUST
distinguish changes in transport association
from changes in logical session identity.

---

## 5. Parent Invariant References

| Invariant | Qualification property |
|---|---|
| INV-001 | Logical identity preservation |
| INV-002 | Transport independence |
| INV-003 | Controlled transport replacement |
| INV-008 | Canonical history integrity |
| INV-010 | Recovery preservation |
| INV-011 | Concurrent operation correctness |
| INV-016 | Session lifetime isolation |
| INV-017 | Unauthorized mutation exclusion |
| INV-018 | Transport failure isolation |

The normative definitions of these
invariants are established in VRP-PA-002.

This document specializes their application
to session identity qualification.

---

## 6. Identity Preservation Contract

For an authorized continuity-preserving
transition within the same logical lifetime:

    S(before) = S(after)

    L(before) = L(after)

The transport association MAY change:

    T(before) != T(after)

Such a transport change MUST NOT implicitly
authorize logical session replacement.

Where canonical authority changes are
permitted, those changes MUST satisfy
the applicable authority contract.

Where canonical history advances, previously
committed relationships MUST remain valid.

The preservation contract does not require
all observable state to remain unchanged.

Authorized progress remains permitted.

---

## 7. Session Lifetime Semantics

A logical session lifetime begins and ends
according to its applicable lifecycle
contract.

Transport establishment MUST NOT
automatically be interpreted as the
beginning of a new logical lifetime.

Transport loss MUST NOT automatically
be interpreted as the termination of
an existing logical lifetime.

An explicitly authorized termination
MAY end a logical session.

An explicitly authorized creation
MAY establish a new logical session.

A new session MUST NOT be presented as
preservation of a terminated session
without supporting contract semantics.

---

## 8. Identity Versus Identifier

A displayed session identifier is an
observable label.

The repeated appearance of the same
label does not independently prove
preservation of the same logical session.

The following distinction is mandatory:

    IDENTIFIER EQUALITY
        !=
    LOGICAL IDENTITY PRESERVATION

An implementation could theoretically
recreate a session while reusing an
externally visible identifier.

A valid qualification method MUST be
capable of distinguishing these cases.

Identifier equality MAY contribute to
the evidence.

It MUST NOT constitute the entire
identity preservation proof.

---

## 9. Continuity Reference

A qualification procedure SHOULD establish
a contract-defined continuity reference
before the relevant transport disturbance.

The reference MUST support meaningful
comparison between observations obtained
before and after the disturbance.

The reference MUST NOT be accepted as
sufficient merely because its displayed
representation remains unchanged.

Its verification semantics MUST provide
a basis for distinguishing:

- Original session preservation.
- Session recreation.
- Unauthorized state replacement.
- Cross-lifetime interference.
- Inconclusive identity attribution.

The representation and implementation
of proprietary continuity mechanisms
remain outside the public disclosure scope.

---

## 10. Transport Replacement Contract

The following conceptual transition
illustrates the public architectural
requirement:

    Initial observation:

        Session:   S
        Lifetime:  L
        Transport: T1

    Transport disturbance:

        T1 becomes unavailable or unsuitable.

    Authorized replacement:

        Transport changes from T1 to T2.

    Final observation:

        Session:   S
        Lifetime:  L
        Transport: T2

This is an external behavioral model.

It is not an internal execution sequence
or implementation description.

The qualification objective is to establish
that the logical session survives the
authorized transport transition.

The transition MUST NOT introduce
unauthorized canonical effects.

---

## 11. Endpoint Change Semantics

Endpoint changes MAY occur as a consequence
of network mobility or infrastructure
behavior.

Relevant conditions include:

- IP address changes.
- NAT rebinding.
- Interface replacement.
- Wireless network transitions.
- Relay availability changes.
- Network path replacement.
- Changes in transport reachability.

Endpoint identity MUST NOT independently
determine logical session identity.

A qualified endpoint transition requires
evidence of both:

    Actual endpoint change.

    Preservation of the applicable
    logical session relationship.

A test that observes only endpoint
replacement does not establish continuity.

---

## 12. Temporary Connectivity Loss

Temporary connectivity loss introduces
a distinction between session existence
and communication availability.

During a qualified connectivity interruption:

- Packet delivery MAY stop.
- Application progress MAY pause.
- Transport availability MAY change.
- Recovery MAY require additional time.

The logical session MUST remain subject
to its applicable lifecycle contract.

A connectivity interruption MUST NOT
independently authorize prohibited
session replacement or canonical mutation.

This requirement does not imply that
communication can continue when every
usable communication path is unavailable.

---

## 13. Recovery Identity Contract

A recovery qualification procedure MUST
evaluate more than restored reachability.

The required distinction is:

    TRANSPORT RECOVERY
        !=
    SESSION RECOVERY QUALIFICATION

Successful transport recovery establishes
that communication capability has returned
within the observed scope.

Session recovery qualification additionally
requires evidence that the applicable
logical session relationship has been
preserved.

A recovery operation that silently
recreates the original session MUST NOT
be classified as identity preservation.

---

## 14. Canonical History Relationship

Session identity qualification SHOULD
include verification of the applicable
canonical history relationship.

Where the contract requires preservation
of previously committed history:

    H(before) remains logically valid
    within H(after).

Recovery MUST NOT silently replace
previously committed history.

A successful reconnection MUST NOT
conceal unauthorized history mutation.

A valid final observation MUST NOT
excuse a demonstrated intermediate
history integrity violation.

The public contract does not disclose
the internal representation or storage
of canonical history.

---

## 15. Authority Relationship

Transport replacement and session
recovery MUST remain subject to the
applicable canonical authority contract.

A reachable endpoint MUST NOT acquire
authority solely because it is reachable.

A transport failure MUST NOT independently
authorize an otherwise prohibited authority
transition.

The following distinction is mandatory:

    TRANSPORT AVAILABILITY
        !=
    CANONICAL AUTHORIZATION

Identity preservation MUST NOT be
achieved by weakening authority validity,
integrity, or lifecycle requirements.

---

## 16. Application Progress Relationship

Application delivery is a relevant
operational observation.

However, application progress alone
does not establish logical identity
preservation.

An application MAY resume communication
after creating a replacement session.

Therefore, qualification SHOULD record
application progress separately from
session identity observations.

The following outcomes are distinct:

| Identity | Delivery | Interpretation |
|---|---|---|
| Preserved | Continued | Continuity with observed delivery |
| Preserved | Interrupted | Identity preserved; delivery degraded |
| Preserved | Restored | Identity preserved with recovery |
| Replaced | Restored | Reconnection, not identity preservation |
| Unknown | Restored | Connectivity recovery only |
| Unknown | Interrupted | Identity outcome inconclusive |

A continuity result MUST NOT be
misrepresented as an unconditional
application availability guarantee.

---

## 17. Independent Observation Requirement

The verification method MUST provide
a meaningful basis for determining
whether the original logical session
has been preserved.

The following observations MUST NOT
independently establish session identity:

- Unchanged process identifier.
- Continued process execution.
- Socket recreation.
- Successful handshake.
- Successful reconnection.
- Repeated session identifier.
- Restored network reachability.
- Continued application execution.
- Successful packet delivery.
- Absence of runtime errors.

These observations MAY support other
qualification objectives.

They MUST NOT replace an appropriate
session identity observation method.

---

## 18. Identity Oracle Qualification

For the purposes of this document,
an identity oracle is a verification
method capable of evaluating the
declared session identity property.

The term describes a verification role.

It does not identify a proprietary
implementation component.

An identity oracle SHOULD demonstrate:

- Positive preservation detection.
- Session replacement detection.
- Identifier reuse discrimination.
- Lifetime distinction.
- Relevant temporal attribution.
- Explicit inconclusive outcomes.

An oracle that reports preservation
for both genuine continuity and
session recreation is insufficient.

The oracle itself MUST be qualified
before its results are used to support
strong identity preservation claims.

---

## 19. Positive and Negative Controls

A meaningful identity qualification
procedure SHOULD include both positive
and negative controls.

### Positive control

A permitted execution in which the
original logical session is expected
to remain valid.

The verification method SHOULD identify
the preserved session relationship.

### Negative control

A controlled execution in which the
original logical session is terminated
and a different logical session is
established.

The verification method MUST NOT
classify this outcome as preservation
of the original logical session.

### Identifier reuse control

Where supported by the evaluation
environment, a new logical session
using a previously observed external
identifier SHOULD be distinguishable
from genuine continuity.

Controls MUST be executed within
authorized evaluation environments.

---

## 20. Temporal Observation Contract

Session identity qualification MUST
account for the relevant execution
interval.

A minimum observation model includes:

    O0: Initial identity observation.

    O1: Disturbance confirmation.

    O2: Transition or interruption
        observation, where available.

    O3: Recovery or replacement
        outcome.

    O4: Final identity verification.

    O5: Post-transition integrity
        verification.

Where continuous observation is
required but unavailable, the resulting
limitation MUST be documented.

Matching initial and final observations
do not independently exclude transient
identity violations.

---

## 21. Qualification Scenario Registry

| Scenario ID | Evaluation objective |
|---|---|
| SIP-001 | Stable session baseline |
| SIP-002 | Authorized transport replacement |
| SIP-003 | Endpoint change |
| SIP-004 | Repeated endpoint changes |
| SIP-005 | Temporary connectivity interruption |
| SIP-006 | Recovery following interruption |
| SIP-007 | Transport degradation |
| SIP-008 | Concurrent transport activity |
| SIP-009 | Session replacement discrimination |
| SIP-010 | Identifier reuse discrimination |
| SIP-011 | Obsolete lifetime isolation |
| SIP-012 | Canonical history preservation |
| SIP-013 | Authority relationship preservation |
| SIP-014 | Compound disturbance qualification |
| SIP-015 | Independent observation reproduction |

Registry inclusion defines an evaluation
objective.

It does not indicate that the scenario
has been executed or qualified.

---

## 22. Stable Baseline Qualification

### Scenario SIP-001

Establish an initial logical session
under declared baseline conditions.

The evaluation MUST establish a usable
identity observation before disturbance
qualification begins.

Required observations include:

- Initial logical session relationship.
- Applicable lifetime relationship.
- Initial transport association.
- Applicable authority context.
- Initial integrity observation.
- Verification method readiness.

A failed or inconclusive baseline MUST
prevent unsupported downstream identity
qualification.

---

## 23. Transport Replacement Qualification

### Scenario SIP-002

Evaluate an authorized replacement
of the associated transport.

Acceptance requires:

- Confirmed initial transport.
- Confirmed transport replacement.
- Preserved logical session relationship.
- Preserved applicable lifetime.
- No prohibited canonical mutation.
- Valid post-transition observation.

The result MUST distinguish transport
replacement from session recreation.

---

## 24. Endpoint Mobility Qualification

### Scenarios SIP-003 and SIP-004

Evaluate session identity under one
or more endpoint changes.

The evaluation record SHOULD identify:

- Number of observed endpoint changes.
- Actual transition timing.
- Relevant observation interval.
- Logical identity outcome.
- Application delivery outcome.
- Applicable integrity outcome.
- Evaluation limitations.

A configured transition schedule
MUST NOT be accepted as evidence
that the transitions actually occurred.

Observed execution is required.

A single successful endpoint transition
does not establish qualification under
arbitrary repeated mobility.

---

## 25. Connectivity Interruption Qualification

### Scenarios SIP-005 and SIP-006

Evaluate identity preservation during
and after temporary connectivity loss.

The evaluation MUST distinguish:

- Configured interruption.
- Observed interruption.
- Restored transport availability.
- Restored application progress.
- Logical session identity outcome.
- Canonical integrity outcome.

Recovery duration SHOULD be reported
with a clearly defined measurement
start and end.

A recovery measurement without a
qualified identity observation MUST
NOT be classified as complete session
continuity evidence.

---

## 26. Transport Degradation Qualification

### Scenario SIP-007

Evaluate identity preservation under
declared transport degradation.

Relevant conditions MAY include:

- Packet loss.
- Increased latency.
- Variable latency.
- Packet duplication.
- Packet reordering.
- Reduced communication capacity.

Each condition MUST be attributed
to the actual evaluated execution.

A configured impairment MUST NOT
be represented as an observed impairment
without supporting measurement.

Identity preservation and communication
performance MUST be reported separately.

---

## 27. Concurrent Transition Qualification

### Scenario SIP-008

Evaluate the applicable session
contract under concurrent transport
or lifecycle activity.

The evaluation MUST account for
relevant ordering and observation
conditions.

Prohibited outcomes include:

- Unauthorized session replacement.
- Conflicting canonical identities.
- Cross-lifetime interference.
- Unauthorized authority acceptance.
- Prohibited duplicate canonical effects.

A successful final connection does
not independently establish concurrent
transition correctness.

---

## 28. Session Replacement Discrimination

### Scenarios SIP-009 and SIP-010

Evaluate whether the observation
method distinguishes original session
preservation from replacement.

The qualification MUST reject the
following reasoning:

    Same displayed identifier.

    Therefore:

    Same logical session.

The acceptance criterion is the
ability to distinguish preservation
from recreation under the declared
observation contract.

If this distinction cannot be
established, the identity verdict
MUST remain INCONCLUSIVE.

---

## 29. Lifetime Isolation Qualification

### Scenario SIP-011

Evaluate isolation between distinct
logical session lifetimes.

An operation associated with an
obsolete lifetime MUST NOT produce
unauthorized effects within a
different lifetime.

The qualification SHOULD distinguish:

- Original lifetime observations.
- Subsequent lifetime observations.
- Applicable operation relationships.
- Canonical effect accounting.
- Final integrity observations.

Reuse of an external identifier
does not authorize reuse of obsolete
session authority.

---

## 30. Canonical Preservation Qualification

### Scenarios SIP-012 and SIP-013

Evaluate the relationship between
session identity, canonical history,
and authority during permitted
transport transitions.

Acceptance requires satisfaction
of the applicable contracts defined
in VRP-PA-002.

A session identity preservation
result MUST NOT conceal:

- Unauthorized history replacement.
- Prohibited authority rollback.
- Invalid authority acceptance.
- Unauthorized canonical mutation.

Continuity and integrity are
complementary qualification objectives.

---

## 31. Compound Disturbance Qualification

### Scenario SIP-014

Evaluate session identity under
multiple concurrent or overlapping
disturbance conditions.

A compound scenario requires its
own explicit qualification record.

Individual successful evaluations
MUST NOT automatically establish
compound scenario qualification.

The evaluation SHOULD identify:

- Actual disturbance combination.
- Observed temporal overlap.
- Identity observation coverage.
- Application delivery outcome.
- Applicable integrity outcome.
- Recovery outcome.
- Known limitations.

Only the evaluated combination
may receive a corresponding verdict.

---

## 32. Independent Reproduction

### Scenario SIP-015

An authorized independent evaluator
SHOULD be able to examine the declared
identity preservation contract through
a bounded evaluation interface.

The evaluator SHOULD receive:

- Applicable public specification.
- Defined evaluation scope.
- Supported scenario descriptions.
- Observable acceptance criteria.
- Approved verification instructions.
- Authorized evidence artifacts.
- Explicit limitations.

Independent reproduction does not
require disclosure of the Protected Core.

Independent verification MUST NOT
be claimed before actual independent
evaluation has occurred.

---

## 33. Acceptance Decision Matrix

| Observed outcome | Identity verdict |
|---|---|
| Qualified identity preserved | PASS |
| Original session replaced without authorization | FAIL |
| Obsolete lifetime affects a new lifetime | FAIL |
| Transport restored; identity unverified | INCONCLUSIVE |
| Identifier unchanged; lifetime unverified | INCONCLUSIVE |
| Required identity observation missing | INCONCLUSIVE |
| Identity observation method unqualified | INCONCLUSIVE |
| Required scenario not executed | NOT TESTED |
| Scenario outside declared contract | NOT APPLICABLE |

An overall scenario verdict additionally
requires satisfaction of every applicable
mandatory acceptance criterion.

A positive identity verdict does not
override an independent integrity failure.

---

## 34. Evidence Record Template

Each session identity qualification
record SHOULD contain:

    DOCUMENT_ID: VRP-PA-003
    SCENARIO_ID:
    INVARIANT_REFERENCES:
    CONTRACT_VERSION:
    IMPLEMENTATION_REFERENCE:
    EVALUATION_ENVIRONMENT:
    INITIAL_SESSION_OBSERVATION:
    INITIAL_LIFETIME_OBSERVATION:
    INITIAL_TRANSPORT_OBSERVATION:
    CONFIGURED_DISTURBANCE:
    OBSERVED_DISTURBANCE:
    OBSERVED_TRANSPORT_TRANSITIONS:
    IDENTITY_ORACLE_QUALIFICATION:
    FINAL_SESSION_OBSERVATION:
    FINAL_LIFETIME_OBSERVATION:
    CANONICAL_INTEGRITY_OUTCOME:
    AUTHORITY_INTEGRITY_OUTCOME:
    APPLICATION_DELIVERY_OUTCOME:
    RECOVERY_DURATION:
    IDENTITY_VERDICT:
    OVERALL_VERDICT:
    EVIDENCE_REFERENCE:
    EVIDENCE_INTEGRITY:
    REPRODUCTION_STATUS:
    LIMITATIONS:

This is a public assurance record
template.

It is not an internal data structure
or protocol message format.

---

## 35. Evidence Attribution Requirements

Every published qualification result
MUST be attributable to its actual
evaluation scope.

Where applicable, the evidence
SHOULD identify:

- Evaluated implementation revision.
- Evaluation environment.
- Test configuration.
- Execution completion status.
- Observation method.
- Acceptance criteria.
- Artifact integrity information.
- Verification outcome.

An artifact checksum establishes
integrity relative to its reference.

It does not independently establish
that the recorded execution occurred
or that its conclusions are correct.

---

## 36. Prohibited Evidence Substitution

The following substitutions are
explicitly prohibited:

    PROCESS SURVIVAL
        as
    SESSION IDENTITY PROOF

    SOCKET REPLACEMENT
        as
    LOGICAL CONTINUITY PROOF

    RECONNECTION
        as
    SESSION PRESERVATION PROOF

    IDENTIFIER EQUALITY
        as
    LIFETIME PRESERVATION PROOF

    APPLICATION DELIVERY
        as
    CANONICAL INTEGRITY PROOF

    CONFIGURED DISTURBANCE
        as
    OBSERVED DISTURBANCE

    SUCCESSFUL TEST EXECUTION
        as
    UNIVERSAL CORRECTNESS PROOF

Each claim requires evidence
appropriate to that claim.

---

## 37. Counterexample Conditions

Any confirmed occurrence of the
following constitutes a relevant
counterexample within an applicable
qualification domain:

- Unauthorized logical session replacement.
- Session recreation classified as preservation.
- Cross-lifetime canonical interference.
- Prohibited authority replacement.
- Unauthorized canonical history mutation.
- Invalid recovery identity attribution.
- False positive identity oracle result.

A confirmed counterexample MUST
invalidate the affected qualification
claim within its applicable scope.

Other successful evaluations do
not erase the counterexample.

Remediation requires subsequent
qualification.

---

## 38. Public Evidence Status

This document defines the normative
session identity qualification contract.

It does not assign empirical PASS
verdicts to individual implementation
revisions or scenario executions.

Empirical results MUST be established
through separately attributable
qualification records.

The master claims-to-evidence matrix
shall distinguish:

- Specified properties.
- Executed evaluations.
- Qualified observations.
- Inconclusive observations.
- Unexecuted scenarios.
- Independently reproduced results.

No unpublished result is assumed
to satisfy a public claim solely
because this document defines it.

---

## 39. Operational Limitations

Session identity preservation does
not imply unlimited availability.

The following remain subject to
explicit operating assumptions:

- Maximum tolerated interruption.
- Available communication paths.
- Recovery duration.
- Resource availability.
- Application delivery guarantees.
- Infrastructure dependencies.
- Session expiration conditions.
- Hardware and operating system behavior.

No finite qualification campaign
establishes immunity to every possible
failure condition.

No result in this document establishes
safety certification for automotive,
aviation, medical, industrial, or
other safety-critical deployments.

Such deployments require additional
domain-specific qualification.

---

## 40. Protected Core Disclosure Boundary

This document intentionally excludes:

- Proprietary continuity algorithms.
- Internal session representations.
- Internal lifetime representations.
- Confidential identity mechanisms.
- Internal authority resolution logic.
- Private runtime interfaces.
- Cryptographic implementation details.
- Internal source code.
- Confidential execution traces.
- Private infrastructure information.

The observable correctness contract
is public.

The implementation mechanisms remain
confidential.

External evaluation does not imply
authorization to extract, reproduce,
or disclose proprietary implementation
mechanisms.

Applicable licenses and evaluation
terms remain in effect.

---

## 41. Related Assurance Documents

- [VRP Executive Engineering Assurance](VRP_EXECUTIVE_ENGINEERING_ASSURANCE.md)
- [VRP Formal Continuity Invariants](VRP_FORMAL_CONTINUITY_INVARIANTS.md)

Supporting qualification documents
shall address:

- Transport independence.
- Adversarial validation.
- Replay and duplicate containment.
- Authority and state integrity.
- Recovery and failure semantics.
- Concurrency and linearizability.
- Autonomous defense boundaries.
- Evidence provenance.
- Independent black-box verification.
- Enterprise pilot acceptance.

---

## 42. Final Engineering Declaration

    SESSION ≠ TRANSPORT

    A connection may disappear.

    A transport may be replaced.

    An endpoint may change.

    Communication may temporarily stop.

    None of these conditions alone
    establishes that the logical
    session must cease to exist.

    Restored connectivity is not
    sufficient evidence of continuity.

    A reused identifier is not
    sufficient evidence of identity.

    Continuity must be demonstrated
    against an explicit contract.

    Identity must be independently
    distinguishable from recreation.

    Integrity must survive recovery.

    Evidence must support the claim.

    The Protected Core remains confidential.

---

**Veil Routing Protocol — VRP**

**Jumping VPN**

**Architect and Creator: Vitalijus Riabovas**

**Continuity-first architecture.**

**Transport-independent session semantics.**

**Externally verifiable correctness contracts.**

**Protected implementation.**

**End of document — VRP-PA-003**
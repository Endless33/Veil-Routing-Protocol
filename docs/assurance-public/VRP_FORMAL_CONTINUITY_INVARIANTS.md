# VRP Formal Continuity Invariants

## Veil Routing Protocol — Jumping VPN

**Document ID:** VRP-PA-002
**Version:** 1.0
**Classification:** PUBLIC
**Status:** Normative Assurance Contract
**Author:** Vitalijus Riabovas
**Protected Core:** CONFIDENTIAL

---

## 1. Purpose

This document defines the externally verifiable
continuity, integrity, authority, and recovery
invariants of Veil Routing Protocol (VRP).

Its purpose is to establish precise conditions
under which observable protocol behavior may
be classified as correct or incorrect.

The foundational architectural principle is:

    SESSION ≠ TRANSPORT

The formal expressions presented in this
document describe observable correctness
requirements.

They do not describe proprietary algorithms,
internal state representations, implementation
structures, or confidential decision mechanisms.

A formal specification of an invariant is not,
by itself, a mathematical proof that every
implementation satisfies that invariant.

---

## 2. Normative Terminology

The terms MUST, MUST NOT, SHOULD, SHOULD NOT,
and MAY express requirements within the scope
of this assurance contract.

A MUST requirement defines a mandatory
correctness condition.

A MUST NOT requirement defines prohibited
observable behavior.

A SHOULD requirement defines an expected
property subject to documented exceptions.

A MAY requirement defines permitted behavior
within established correctness boundaries.

These requirements describe the target
architectural contract.

Implementation qualification requires
separate supporting evidence.

---

## 3. Abstract Observation Model

For verification purposes, the following
abstract symbols are defined:

    S(t) = logical session identity at time t
    T(t) = associated transport at time t
    A(t) = valid authority context at time t
    E(t) = committed authority epoch at time t
    H(t) = committed canonical history at time t
    L(t) = logical session lifetime at time t
    O    = externally identifiable operation
    C(O) = number of canonical commits of O

These symbols represent conceptual observation
targets.

They MUST NOT be interpreted as actual internal
variables, structures, storage layouts,
cryptographic constructions, or implementation
interfaces.

The observation model exists exclusively to
support external correctness reasoning.

---

## 4. Qualification Domain

An invariant shall be evaluated within an
explicitly defined qualification domain.

The domain MUST identify:

- The applicable protocol contract.
- The implementation revision.
- The execution environment.
- The initial session conditions.
- The permitted operation set.
- The relevant failure conditions.
- The observation interval.
- The acceptance criteria.
- The verification method.
- The applicable limitations.

A result obtained within one qualification
domain MUST NOT automatically be generalized
to another domain.

---

## 5. Invariant Registry

| Invariant | Property | Parent claim |
|---|---|---|
| INV-001 | Logical identity preservation | VRP-C01 |
| INV-002 | Transport independence | VRP-C02 |
| INV-003 | Controlled transport replacement | VRP-C03 |
| INV-004 | Replay containment | VRP-C04 |
| INV-005 | Duplicate commit exclusion | VRP-C05 |
| INV-006 | Stale authority rejection | VRP-C06 |
| INV-007 | Epoch rollback exclusion | VRP-C07 |
| INV-008 | Canonical history integrity | VRP-C08 |
| INV-009 | Deterministic authority resolution | VRP-C09 |
| INV-010 | Recovery preservation | VRP-C10 |
| INV-011 | Concurrent operation correctness | VRP-C11 |
| INV-012 | Evidence integrity | VRP-C12 |
| INV-013 | Fail-closed behavior | VRP-C13 |
| INV-014 | Bounded defensive behavior | VRP-C14 |
| INV-015 | Reproducible verification | VRP-C15 |
| INV-016 | Session lifetime isolation | VRP-C01, VRP-C11 |
| INV-017 | Unauthorized mutation exclusion | VRP-C06, VRP-C13 |
| INV-018 | Transport failure isolation | VRP-C02, VRP-C10 |

The registry establishes stable references
for subsequent public assurance documents.

Registry inclusion does not establish
implementation qualification.

---

## 6. INV-001 — Logical Identity Preservation

### Requirement

An authorized transport transition MUST NOT
implicitly replace the logical identity of
an existing session.

### Abstract expression

For a valid continuity-preserving transition
within the same logical session lifetime:

    L(t1) = L(t2)
        implies
    S(t1) = S(t2)

### Verification objective

Establish that the session observed before
a transport transition is the same logical
session observed after that transition.

### Required evidence

- Pre-transition identity observation.
- Confirmed transport transition.
- Post-transition identity observation.
- Evidence distinguishing preservation
  from recreation.

### Violation conditions

- Unrequested session replacement.
- Undocumented session recreation.
- Conflicting canonical identities.
- Loss of required identity relationships.

An unchanged displayed identifier alone
is insufficient evidence.

---

## 7. INV-002 — Transport Independence

### Requirement

Logical session identity MUST NOT be defined
solely by the identity or availability of
an underlying transport.

### Abstract expression

For a qualified transport replacement:

    T(t1) != T(t2)

does not imply:

    S(t1) != S(t2)

### Verification objective

Demonstrate that a change in transport can
occur without requiring replacement of the
logical session.

### Violation conditions

- Mandatory session recreation caused
  solely by transport replacement.
- Transport identity being accepted as
  sufficient proof of logical identity.
- Uncontrolled loss of canonical session
  relationships during transport changes.

This invariant does not require uninterrupted
packet delivery during a transport transition.

---

## 8. INV-003 — Controlled Transport Replacement

### Requirement

Transport replacement MUST occur within the
applicable authorization and continuity
contract.

A newly available transport MUST NOT acquire
canonical authority solely because it is
reachable.

### Verification objective

Establish that permitted transport replacement
preserves required session relationships and
that prohibited replacement attempts do not
produce unauthorized canonical effects.

### Violation conditions

- Unauthorized transport adoption.
- Invalid authority acceptance.
- Uncontrolled session replacement.
- Conflicting canonical transition outcomes.

Transport availability and authorization
are distinct properties.

---

## 9. INV-004 — Replay Containment

### Requirement

A replayed operation MUST NOT produce an
additional canonical effect where the
applicable operation contract prohibits
such an effect.

### Abstract expression

For an operation already committed:

    C(O) = 1

A prohibited replay MUST NOT cause:

    C(O) > 1

### Verification objective

Evaluate observable behavior when previously
processed operations are presented again.

### Required evidence

- Original operation outcome.
- Replay classification.
- Canonical effect accounting.
- Post-replay integrity observation.

### Violation conditions

- Additional unauthorized canonical effect.
- Duplicate protected state transition.
- Unauthorized authority advancement.
- Canonical history corruption.

Repeated network delivery is not necessarily
a violation.

Repeated prohibited canonical effects are.

---

## 10. INV-005 — Duplicate Commit Exclusion

### Requirement

An operation governed by an at-most-once
commit contract MUST NOT produce more than
one canonical commit.

### Abstract expression

    C(O) <= 1

### Verification objective

Establish that repeated or concurrent
presentation of the same logical operation
does not produce multiple prohibited commits.

### Violation conditions

- Multiple commits of the same operation.
- Conflicting committed outcomes.
- Duplicate canonical history effects.

This invariant does not imply that every
submitted operation will eventually commit.

At-most-once correctness and eventual
completion are separate properties.

---

## 11. INV-006 — Stale Authority Rejection

### Requirement

Authority that is no longer valid under the
applicable contract MUST NOT authorize a
protected canonical transition.

### Abstract expression

    ValidAuthority(A, t) = false

    implies

    AuthorizedCanonicalEffect(A, t) = false

### Verification objective

Establish that outdated authority cannot
produce prohibited canonical effects.

### Violation conditions

- Acceptance of invalidated authority.
- Unauthorized protected state mutation.
- Restoration of obsolete authority without
  a valid authorization transition.

The public contract does not disclose how
authority validity is represented or evaluated.

---

## 12. INV-007 — Epoch Rollback Exclusion

### Requirement

Within the same applicable authority epoch
domain, a committed authority epoch MUST NOT
move backward.

### Abstract expression

For committed observations within the same
epoch domain:

    t2 >= t1

    implies

    E(t2) >= E(t1)

### Verification objective

Establish that obsolete epoch information
cannot cause prohibited rollback of committed
authority state.

### Violation conditions

- Acceptance of a prohibited older epoch.
- Unauthorized restoration of obsolete state.
- Reduction of the committed authority epoch
  within the same epoch domain.

Comparisons across unrelated session lifetimes
or epoch domains require separate semantics.

---

## 13. INV-008 — Canonical History Integrity

### Requirement

Previously committed canonical history MUST
NOT be silently rewritten, replaced, or
invalidated through unauthorized operations.

### Abstract expression

For an append-only history domain:

    H(t1) is a prefix of H(t2)

where t2 >= t1 and both observations refer
to the same applicable history domain.

### Verification objective

Establish that subsequent operations preserve
the integrity of previously committed history.

### Violation conditions

- Unauthorized modification of prior commits.
- Undocumented history replacement.
- Conflicting canonical records.
- Recovery that conceals prohibited mutation.

Authorized retention, archival, or compaction
requires separately documented semantics.

The invariant concerns logical history
integrity, not a particular storage format.

---

## 14. INV-009 — Deterministic Authority Resolution

### Requirement

Equivalent valid decision contexts MUST
produce equivalent authority outcomes under
the same applicable decision contract.

### Abstract expression

    EquivalentContext(X, Y)

        implies

    EquivalentOutcome(X, Y)

Equivalence MUST account for all relevant
contract-defined inputs and ordering conditions.

### Verification objective

Evaluate whether conflicting or concurrent
authority activity produces outcomes permitted
by the declared authority contract.

### Violation conditions

- Incompatible canonical authority outcomes.
- Unauthorized simultaneous authority.
- Undocumented decision inconsistency.
- Acceptance of prohibited competing state.

Deterministic resolution does not imply
identical network timing or execution
scheduling across different runs.

---

## 15. INV-010 — Recovery Preservation

### Requirement

Recovery MUST preserve all logical session
relationships required by the applicable
continuity contract.

Recovery MUST NOT authorize otherwise
prohibited canonical mutation.

### Verification objective

Distinguish recovery of transport availability
from preservation of logical session identity
and canonical state.

### Required evidence

- Pre-failure session observation.
- Confirmed failure condition.
- Recovery outcome.
- Post-recovery identity observation.
- Applicable integrity verification.

### Violation conditions

- Undocumented session recreation.
- Unauthorized authority replacement.
- Canonical history corruption.
- Prohibited state rollback.

Recovery completion alone is insufficient
proof of continuity preservation.

---

## 16. INV-011 — Concurrent Operation Correctness

### Requirement

Concurrent operations MUST preserve the
applicable session, authority, and integrity
contracts.

For operations explicitly qualified as
linearizable, observable histories MUST
admit a legal sequential interpretation
that respects real-time precedence.

### Verification objective

Evaluate concurrent execution against the
declared operation semantics.

### Violation conditions

- Prohibited duplicate commits.
- Invalid observable operation ordering.
- Unauthorized state transitions.
- Cross-lifetime state interference.
- Incompatible canonical outcomes.

Race detector results are supplementary
evidence.

A successful race detector execution does
not independently prove linearizability.

---

## 17. INV-012 — Evidence Integrity

### Requirement

Evidence used to qualify a protocol claim
MUST be attributable to the corresponding
execution and verification context.

Undocumented evidence modification MUST NOT
be accepted as valid qualification evidence.

### Verification objective

Establish that approved evidence artifacts
can be associated with their declared scope
and checked for unauthorized modification.

### Violation conditions

- Unattributed evidence.
- Undocumented evidence replacement.
- Integrity verification failure.
- Contradictory evidence classification.
- Missing required verification context.

Artifact integrity does not independently
establish execution authenticity or
correctness of the underlying claim.

---

## 18. INV-013 — Fail-Closed Behavior

### Requirement

An operation lacking required authorization
or validity MUST NOT produce a protected
canonical effect.

### Abstract expression

    RequiredValidation(O) = false

        implies

    ProtectedCanonicalEffect(O) = false

### Verification objective

Evaluate rejection behavior under invalid,
incomplete, unauthorized, or otherwise
prohibited operation conditions.

### Violation conditions

- Unauthorized acceptance.
- Protected mutation after rejection.
- Uncontrolled authority advancement.
- Invalid input being treated as sufficient
  authorization.

Fail-closed behavior MAY produce permitted
diagnostic or defensive observations.

Such observations MUST NOT be confused with
authorization to modify canonical state.

Fail-closed correctness does not independently
establish availability under every failure
condition.

---

## 19. INV-014 — Bounded Defensive Behavior

### Requirement

Autonomous defensive behavior MUST remain
within its explicitly authorized scope.

A defensive decision MUST NOT independently
override canonical authority requirements.

### Abstract expression

    DefensiveDecision

        does not imply

    CanonicalAuthorization

### Verification objective

Establish that defensive behavior preserves
the applicable authority, lifecycle, and
integrity contracts.

### Violation conditions

- Unauthorized canonical mutation.
- Cross-scope defensive interference.
- Prohibited authority escalation.
- Uncontrolled defensive state transitions.
- Violation of declared resource boundaries.

Component-level defensive qualification
MUST NOT be represented as complete
live-runtime qualification.

---

## 20. INV-015 — Reproducible Verification

### Requirement

A qualified result MUST identify sufficient
verification conditions to support meaningful
reproduction within its declared scope.

### Verification objective

Enable authorized evaluators to examine
whether observed behavior satisfies the
same declared acceptance criteria.

### Required evidence

- Applicable claim and invariant identifiers.
- Defined execution conditions.
- Observable acceptance criteria.
- Evidence references.
- Verification outcome.
- Documented limitations.

### Violation conditions

- Unspecified acceptance criteria.
- Unsupported result classification.
- Undocumented changes to test conditions.
- Suppression of contradictory results.

Reproducibility does not require disclosure
of proprietary implementation mechanisms.

Independent verification status requires
actual independent verification.

---

## 21. INV-016 — Session Lifetime Isolation

### Requirement

An operation associated with an obsolete
logical session lifetime MUST NOT produce
unauthorized effects within a different
logical session lifetime.

### Abstract expression

    L1 != L2

    and

    AuthorizedFor(O, L1)

    do not imply

    AuthorizedFor(O, L2)

### Verification objective

Establish that distinct session lifetimes
remain isolated even when externally visible
identifiers or resources are reused.

### Violation conditions

- Cross-lifetime authority acceptance.
- Unauthorized state inheritance.
- Obsolete operations affecting a new
  session lifetime.
- Confusion between identity reuse and
  continuity preservation.

---

## 22. INV-017 — Unauthorized Mutation Exclusion

### Requirement

An unauthorized operation MUST NOT modify
protected canonical state.

### Abstract expression

    Authorized(O) = false

        implies

    ProtectedMutation(O) = false

### Verification objective

Establish that rejected operations cannot
produce prohibited canonical effects.

### Violation conditions

- Mutation despite rejection.
- Unauthorized partial commit.
- Invalid authority advancement.
- Protected state corruption.

Permitted diagnostic accounting does not
constitute a protected canonical mutation
unless the applicable contract defines
otherwise.

---

## 23. INV-018 — Transport Failure Isolation

### Requirement

Transport failure MUST NOT, by itself,
authorize a prohibited change in logical
session identity, canonical history, or
authority.

### Abstract expression

    TransportUnavailable(T)

        does not imply

    AuthorizedSessionReplacement

        or

    AuthorizedHistoryRewrite

        or

    AuthorizedAuthorityReplacement

### Verification objective

Evaluate whether transport failure remains
isolated from unauthorized canonical effects.

### Violation conditions

- Uncontrolled session replacement.
- Unauthorized canonical state mutation.
- Invalid authority transition.
- Undocumented history reconstruction.

This invariant does not prohibit explicitly
authorized lifecycle transitions under
documented termination or expiration rules.

---

## 24. Safety and Liveness Separation

The assurance framework distinguishes
safety properties from liveness properties.

### Safety

Safety properties define prohibited outcomes.

Examples include:

- No prohibited duplicate commit.
- No unauthorized canonical mutation.
- No prohibited authority rollback.
- No unauthorized history rewrite.

### Liveness

Liveness properties define expected progress
under explicitly stated operating assumptions.

Examples include:

- Eventual recovery when required conditions
  become available.
- Completion of authorized operations.
- Restoration of permitted communication.

Safety qualification does not automatically
establish liveness qualification.

Liveness qualification does not justify
violation of safety requirements.

---

## 25. Temporal Correctness

Correctness MUST be evaluated across the
relevant observation interval.

A valid final state does not independently
establish that every intermediate transition
was valid.

The verification framework distinguishes:

- Initial-state correctness.
- Transition correctness.
- Intermediate-state correctness.
- Final-state correctness.
- Post-recovery correctness.

Where an invariant applies continuously,
verification MUST account for the possibility
of transient violations.

If the available observation method cannot
exclude relevant intermediate violations,
that limitation MUST be documented.

---

## 26. Compound Failure Qualification

Independent qualification of individual
failure scenarios does not automatically
establish correctness under their combination.

Compound scenarios MAY include combinations
of:

- Transport replacement.
- Packet loss.
- Packet duplication.
- Packet reordering.
- Endpoint changes.
- Temporary network unavailability.
- Concurrent operation activity.
- Invalid or obsolete authority.
- Recovery activity.

Each compound scenario requires its own
defined scope and acceptance criteria.

A successful isolated test MUST NOT be
represented as qualification of an untested
compound scenario.

---

## 27. Observation Independence

Continuity verification requires observations
capable of distinguishing the claimed property
from unrelated operational indicators.

The following MUST NOT independently be
accepted as sufficient proof of logical
session continuity:

- Process identity preservation.
- Socket recreation.
- Successful reconnection.
- Restored packet delivery.
- Repeated display of a session identifier.
- Application reachability.
- Successful transport initialization.

The verification method MUST establish
why the observed evidence supports the
specific invariant under evaluation.

An observation mechanism that cannot
distinguish preservation from recreation
is insufficient for identity qualification.

---

## 28. Invariant Interaction

The invariants defined in this document
are complementary.

Satisfaction of one invariant MUST NOT
be used to excuse violation of another
applicable invariant.

For example:

- Successful recovery does not excuse
  unauthorized state mutation.
- Transport replacement does not excuse
  session identity replacement.
- Defensive behavior does not excuse
  authority violations.
- High throughput does not excuse
  duplicate canonical commits.
- Valid final state does not excuse
  prohibited intermediate transitions.

Correctness requires satisfaction of all
applicable mandatory contracts within the
qualified execution scope.

---

## 29. Verification Verdicts

Every invariant evaluation shall produce
an explicit verdict.

| Verdict | Meaning |
|---|---|
| PASS | Evidence satisfies the defined acceptance criteria |
| FAIL | Evidence demonstrates a contract violation |
| INCONCLUSIVE | Available observations cannot establish the outcome |
| NOT TESTED | Required execution has not been performed |
| NOT APPLICABLE | Invariant does not apply to the defined scope |

A PASS verdict applies only to the specified
execution and acceptance criteria.

Skipped tests MUST NOT be counted as PASS.

Missing evidence MUST NOT be interpreted
as evidence of correctness.

An inconclusive result MUST remain
inconclusive until sufficient evidence
becomes available.

---

## 30. Counterexample Policy

A valid counterexample demonstrating a
violation of an applicable invariant
MUST be treated as engineering evidence.

A counterexample record SHOULD identify:

- Applicable invariant.
- Qualification scope.
- Initial conditions.
- Observed behavior.
- Expected behavior.
- Contract violation.
- Reproduction status.
- Remediation status, where applicable.

A confirmed counterexample MUST NOT be
discarded solely because other executions
satisfied the same invariant.

Remediation requires subsequent verification.

Historical failures and corrected results
must remain distinguishable.

---

## 31. Qualification Record Format

Each published invariant qualification
SHOULD use the following abstract record:

    CLAIM_ID:
    INVARIANT_ID:
    CONTRACT_VERSION:
    REVISION_REFERENCE:
    QUALIFICATION_SCOPE:
    INITIAL_CONDITIONS:
    EXECUTION_CONDITIONS:
    EXPECTED_PROPERTY:
    OBSERVED_PROPERTY:
    VERIFICATION_METHOD:
    EVIDENCE_REFERENCE:
    EVIDENCE_INTEGRITY:
    VERDICT:
    REPRODUCTION_STATUS:
    LIMITATIONS:

This format is a public assurance record
template.

It is not an internal protocol message,
runtime structure, or implementation schema.

---

## 32. Specification and Evidence Separation

This document defines correctness
requirements.

It does not assign empirical PASS verdicts
to individual implementation revisions.

Empirical qualification MUST be established
through separately attributable evidence
records and the master claims-to-evidence
matrix.

The following distinctions are mandatory:

    SPECIFIED != VERIFIED

    VERIFIED != UNIVERSALLY PROVEN

    REPRODUCED != INDEPENDENTLY VERIFIED

    CONNECTIVITY != CONTINUITY

    RECOVERY != IDENTITY PRESERVATION

    CONFIDENTIALITY != IMMUNITY

No architectural assertion may substitute
for missing execution evidence.

---

## 33. Protected Core Boundary

This document intentionally excludes:

- Proprietary algorithms.
- Internal decision mechanisms.
- Internal authority representations.
- Confidential state structures.
- Private implementation interfaces.
- Internal execution traces.
- Confidential cryptographic constructions.
- Private infrastructure configuration.
- Protected source code.

All mathematical expressions describe
external correctness requirements.

They MUST NOT be interpreted as disclosure
of the actual implementation.

The Protected Core remains confidential.

Publication of these invariants does not
modify applicable intellectual property
rights, licenses, or evaluation terms.

---

## 34. Related Assurance Documents

Parent document:

- [VRP Executive Engineering Assurance](
  VRP_EXECUTIVE_ENGINEERING_ASSURANCE.md)

Planned supporting documents:

- VRP Session Identity Preservation.
- VRP Transport Independence.
- VRP Adversarial Validation Evidence.
- VRP Replay and Duplicate Containment.
- VRP Authority and State Integrity.
- VRP Recovery and Failure Semantics.
- VRP Concurrency and Linearizability.
- VRP Autonomous Defense Boundaries.
- VRP Runtime Performance Evidence.
- VRP Evidence Provenance and Integrity.
- VRP Independent Black-Box Verification.
- VRP Enterprise Pilot Qualification.
- VRP Master Claims-to-Evidence Matrix.

Supporting documents shall reference
the stable invariant identifiers defined
in this specification.

---

## 35. Final Engineering Declaration

    SESSION ≠ TRANSPORT

    A transport transition is not
    authorization to replace a session.

    A network failure is not
    authorization to rewrite history.

    A defensive decision is not
    canonical authority.

    A successful recovery is not
    independent proof of continuity.

    An observed result is not
    a universal correctness guarantee.

    Correctness is a contract.

    Evidence is a requirement.

    Verification is the standard.

    The Protected Core remains confidential.

---

**Veil Routing Protocol — VRP**

**Jumping VPN**

**Architect and Creator: Vitalijus Riabovas**

**18 externally verifiable invariants.**

**One continuity-first architectural contract.**

**End of document — VRP-PA-002**
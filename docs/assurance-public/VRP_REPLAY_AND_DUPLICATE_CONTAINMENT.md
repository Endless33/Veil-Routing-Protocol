# VRP Replay and Duplicate Containment

## Veil Routing Protocol — Jumping VPN

**Document ID:** VRP-PA-006
**Version:** 1.0
**Classification:** PUBLIC
**Status:** Evidence-Oriented Qualification Contract
**Author:** Vitalijus Riabovas
**Protected Core:** CONFIDENTIAL

---

## 1. Engineering Position

A protocol cannot establish replay resistance
merely by reporting that repeated inputs
were rejected.

The decisive question is whether those inputs
produced any prohibited canonical effects.

Veil Routing Protocol establishes the
following externally verifiable requirement:

    Repeated presentation MUST NOT produce
    prohibited repeated canonical commitment.

This requirement remains applicable across
authorized transport changes, concurrent
operation activity, and recovery conditions
within the qualified operating domain.

The evaluation objective is observable
semantic correctness.

The implementation responsible for achieving
that correctness remains confidential.

---

## 2. Assurance Claim

Primary claim references:

    VRP-C04 — Replay containment.
    VRP-C05 — Duplicate commit rejection.

Supporting invariant references:

    INV-004 — Replay containment.
    INV-005 — Duplicate commit exclusion.
    INV-008 — Canonical history integrity.
    INV-011 — Concurrent operation correctness.
    INV-013 — Fail-closed behavior.
    INV-016 — Session lifetime isolation.
    INV-017 — Unauthorized mutation exclusion.

The claim is falsifiable.

A single confirmed prohibited duplicate
canonical effect constitutes a counterexample
within the applicable qualification scope.

A successful rejection response does not
override such a counterexample.

---

## 3. Historical Engineering Evidence

The VRP project has previously reported
the following adversarial validation result:

    EVIDENCE_REFERENCE: AVE-001

    EVALUATION_CLASS:
        Replay containment.

    REPORTED_REPLAY_REJECTIONS:
        9999

    PUBLIC_EVIDENCE_CLASSIFICATION:
        REPORTED

    INDEPENDENT_THIRD_PARTY_VERIFICATION:
        NOT ESTABLISHED BY THIS RECORD

The historical result is referenced in
VRP-PA-005.

This is an existing project-reported
engineering outcome, not a hypothetical
target or projected benchmark.

The original execution artifacts and
their qualification context remain
necessary for stronger public assurance.

The reported rejection count MUST NOT
be expanded into an unsupported claim
of universal replay immunity.

---

## 4. What Constitutes Engineering Evidence

The following are distinct observations:

    INPUT PRESENTED

    INPUT CLASSIFIED

    INPUT REJECTED

    CANONICAL EFFECT OBSERVED

    CANONICAL INTEGRITY VERIFIED

A rejection message establishes only
the corresponding reported rejection
outcome unless additional evidence
establishes its semantic consequences.

A qualified replay containment result
requires evidence that the protected
canonical effect did not occur.

This distinction prevents superficial
success criteria from being substituted
for actual correctness.

---

## 5. Observable Qualification Model

For external evaluation purposes:

    O = logical operation

    P(O) = observed presentations of O

    C(O) = observed canonical commits of O

    R(O) = observed rejection outcomes

These symbols describe abstract
verification targets.

They are not implementation variables,
internal structures, protocol messages,
or proprietary mechanisms.

For an operation governed by an
at-most-once commitment contract:

    C(O) <= 1

For a prohibited replay following
an established original commitment:

    AdditionalCanonicalCommits(O) = 0

The qualification procedure MUST
establish why the observed operation
and canonical effects correspond to
the applicable logical operation.

---

## 6. Canonical Effect Accounting

Canonical effect accounting is an
external verification requirement.

The evaluator MUST distinguish:

- Original authorized effects.
- Subsequent prohibited effects.
- Permitted diagnostic observations.
- Permitted application activity.
- Authorized unrelated operations.
- Inconclusive observations.

A rejection response MUST NOT be
counted as sufficient evidence of
canonical effect exclusion.

The evaluation must establish whether
the protected operation changed
canonical state in a prohibited manner.

The internal representation of
canonical state is outside the
public disclosure boundary.

---

## 7. Falsification Criteria

The replay containment claim is
considered violated when attributable
evidence establishes any applicable
prohibited outcome:

- Additional canonical commitment
  of an already committed operation.

- Unauthorized canonical mutation
  following prohibited replay.

- Prohibited authority advancement.

- Unauthorized history modification.

- Obsolete lifetime interference.

- Incompatible committed outcomes
  for the same logical operation.

- Protected mutation despite an
  observed rejection response.

These criteria are independent of
whether the implementation reports
success or failure.

Observed semantic behavior takes
precedence over diagnostic labels.

---

## 8. Positive Control Requirement

A meaningful containment evaluation
MUST establish that valid operations
can produce their permitted effects.

An implementation that rejects every
input could otherwise appear to
satisfy a rejection-only test.

The positive control MUST establish:

    VALID_OPERATION_PRESENTED:
        YES

    EXPECTED_AUTHORIZED_EFFECT:
        DEFINED

    OBSERVED_AUTHORIZED_EFFECT:
        VERIFIED

The evaluation MUST NOT proceed to
a positive containment verdict if
the required baseline operation
cannot be established.

Rejection without demonstrated
valid operation handling is
insufficient qualification.

---

## 9. Negative Control Requirement

The verification method MUST be
capable of identifying a prohibited
additional canonical effect.

Where supported, an authorized
verification fixture SHOULD provide
a deliberately invalid observation
record containing a duplicate effect.

The verification method MUST NOT
accept that record as compliant.

This control evaluates the
verification mechanism.

It does not require modification
or disclosure of the Protected Core.

A verifier that cannot distinguish
a compliant record from a relevant
counterexample is insufficient
for strong qualification.

---

## 10. Verification Independence

The evaluation framework distinguishes:

    RUNTIME OUTCOME

    RUNTIME-REPORTED OUTCOME

    VERIFIER CONCLUSION

    INDEPENDENT EVALUATOR CONCLUSION

These are separate evidence layers.

A runtime-generated success label
MUST NOT automatically determine
the final assurance verdict.

The verification method SHOULD
evaluate approved observations
against explicit acceptance criteria.

Where verification independence is
limited, that limitation MUST be
documented.

Independent software verification
does not automatically establish
independent third-party evaluation.

---

## 11. Qualification Scenario Registry

| Scenario | Evaluation objective |
|---|---|
| RDC-001 | Valid operation baseline |
| RDC-002 | Replay containment |
| RDC-003 | Repeated presentation containment |
| RDC-004 | Concurrent duplicate containment |
| RDC-005 | Transport transition consistency |
| RDC-006 | Recovery consistency |
| RDC-007 | Obsolete lifetime isolation |
| RDC-008 | Canonical history preservation |
| RDC-009 | Authority integrity |
| RDC-010 | Verification negative control |
| RDC-011 | Valid operation progress |
| RDC-012 | Long-duration resource qualification |
| RDC-013 | Independent evidence verification |
| RDC-014 | Independent scenario reproduction |

The registry defines qualification
objectives rather than asserting
that all scenarios have already
been executed.

Each scenario requires its own
attributable evidence record.

---

## 12. Transport Independence Relationship

Replay containment MUST remain
subject to the applicable logical
session contract when transport
associations change.

A transport replacement MUST NOT
independently authorize an otherwise
prohibited repeated canonical effect.

The public architectural requirement
is:

    SESSION ≠ TRANSPORT

The verification objective is
consistency of the applicable
correctness contract across the
evaluated transport transition.

This requirement does not disclose
how the implementation maintains
or evaluates that relationship.

---

## 13. Recovery Relationship

Recovery MUST NOT authorize
prohibited duplicate commitment.

A successful recovery outcome
MUST remain distinguishable from:

- Unauthorized history reconstruction.
- Repeated protected commitment.
- Invalid authority acceptance.
- Obsolete lifetime interference.
- Unauthorized session replacement.

The recovery verdict and replay
containment verdict MUST be recorded
as separate qualification outcomes.

A successful recovery MUST NOT
conceal a containment violation.

---

## 14. Concurrent Correctness

Concurrent operation activity
introduces correctness requirements
beyond sequential rejection behavior.

The applicable qualification MUST
establish that observed canonical
effects remain consistent with
the declared operation contract.

A sequential replay rejection
result does not independently
establish concurrent correctness.

A successful race detector
execution provides supplementary
engineering evidence.

It does not independently prove
at-most-once commitment or
linearizability.

The corresponding semantic
verification remains necessary.

---

## 15. Session Lifetime Isolation

Replay containment MUST respect
the applicable logical session
lifetime boundary.

An operation associated with an
obsolete lifetime MUST NOT acquire
authorization within another
lifetime solely because an external
identifier or transport resource
has been reused.

The qualification objective is
absence of prohibited cross-lifetime
canonical effects.

The implementation of lifetime
isolation remains confidential.

---

## 16. Canonical History Integrity

Previously committed canonical
relationships MUST remain valid
under the applicable history
integrity contract.

Repeated operation presentation
MUST NOT authorize prohibited
history modification.

A qualified result MUST distinguish
authorized subsequent progress
from unauthorized modification
of previously committed history.

The public evaluation does not
require disclosure of internal
history representation or storage.

---

## 17. Authority Integrity

Repeated operation presentation
MUST NOT independently establish
new canonical authority.

Transport availability, successful
communication, and repeated input
delivery are not substitutes for
valid authorization.

The evaluation MUST establish
whether the applicable authority
contract remained satisfied.

The mechanisms responsible for
authority validation remain
outside the public disclosure
boundary.

---

## 18. Availability and Valid Progress

Replay containment MUST NOT be
confused with complete operational
availability.

A system MAY correctly reject
prohibited operations while
communication performance degrades.

However, a meaningful qualification
SHOULD also evaluate whether
permitted operations continue to
make progress under the declared
operating assumptions.

The following MUST be measured
separately:

    PROHIBITED_EFFECT_CONTAINMENT

    VALID_OPERATION_PROGRESS

    COMMUNICATION_AVAILABILITY

    RESOURCE_CONSUMPTION

A successful containment verdict
does not automatically establish
positive results in every category.

---

## 19. Resource Qualification

A large number of successful
rejections does not independently
establish bounded resource
consumption.

Resource qualification requires
separate observations of applicable
execution limits.

Relevant measurements include:

- Evaluation duration.
- Valid operation progress.
- CPU consumption.
- Memory consumption.
- Allocation behavior.
- Post-evaluation resource retention.
- Observed execution failures.

A short-duration result MUST NOT
be represented as unlimited
long-duration resilience.

The evaluation environment and
measurement methodology MUST
remain attributable.

---

## 20. Evidence Acceptance Matrix

| Observation | Verdict |
|---|---|
| Required controls valid; no prohibited effects observed within sufficient coverage | PASS |
| Confirmed prohibited duplicate commitment | FAIL |
| Confirmed unauthorized canonical mutation | FAIL |
| Confirmed obsolete lifetime interference | FAIL |
| Rejection reported but canonical effects unverified | INCONCLUSIVE |
| Positive control unsuccessful | INCONCLUSIVE |
| Verification negative control unsuccessful | INCONCLUSIVE |
| Required observation coverage unavailable | INCONCLUSIVE |
| Required evaluation not executed | NOT TESTED |

A PASS verdict is scoped to the
specific evaluation conditions.

It is not a universal proof of
implementation correctness.

---

## 21. Evidence Sufficiency Levels

The following evidence levels
describe the strength of an
individual containment claim.

### Level E0 — Specification

The correctness requirement is
documented.

No empirical conclusion follows
from specification alone.

### Level E1 — Reported Execution

An engineering outcome has been
reported.

The underlying execution evidence
has not been established within
the public qualification record.

### Level E2 — Attributable Evidence

Approved execution artifacts are
associated with a defined revision,
evaluation scope, and observation
method.

### Level E3 — Verified Evidence

The associated evidence satisfies
the declared acceptance criteria
and applicable verification controls.

### Level E4 — Reproduced Evaluation

The result has been reproduced
under documented evaluation
conditions.

### Level E5 — Independent Reproduction

An independent evaluator has
performed the corresponding
evaluation and recorded the outcome.

These levels are defined for
the VRP assurance framework.

They are not external certification
grades or accredited assurance
ratings.

---

## 22. Current Historical Claim Classification

The historical result AVE-001
is classified within this document as:

    EVIDENCE_LEVEL: E1

    REPORTED_REJECTIONS: 9999

    ORIGINAL_ARTIFACTS_EMBEDDED:
        NO

    PUBLIC_CANONICAL_EFFECT_ACCOUNTING:
        NOT ESTABLISHED BY THIS RECORD

    PUBLIC_INDEPENDENT_REPRODUCTION:
        NOT ESTABLISHED BY THIS RECORD

This classification describes
the evidence available within
the present public record.

It does not establish that
additional restricted evidence
does not exist.

Promotion to a stronger level
requires the corresponding
supporting evidence.

---

## 23. Evidence Promotion Gates

A containment claim MUST NOT
receive a stronger evidence
classification without satisfying
the corresponding requirements.

Promotion from E1 to E2 requires:

- Attributable execution evidence.
- Identified implementation reference.
- Defined evaluation scope.
- Documented observation conditions.

Promotion from E2 to E3 requires:

- Applicable acceptance criteria.
- Qualified verification method.
- Required control results.
- Canonical effect verification.
- Explicit limitations.

Promotion from E3 to E4 requires:

- A separately attributable
  reproduction record.

Promotion from E4 to E5 requires:

- Actual independent evaluation.
- Independent outcome attribution.
- Declared evaluation scope.
- Recorded findings and limitations.

A promotional statement is not
an evidence promotion mechanism.

---

## 24. Public Evidence Record

The following record defines
the minimum public attribution
for a qualified containment result:

    DOCUMENT_ID: VRP-PA-006

    EVIDENCE_ID:

    SCENARIO_ID:

    CLAIM_REFERENCES:

    INVARIANT_REFERENCES:

    CONTRACT_VERSION:

    IMPLEMENTATION_REFERENCE:

    EXECUTION_REFERENCE:

    EVALUATION_ENVIRONMENT_CLASS:

    EVALUATION_SCOPE:

    ORIGINAL_OPERATION_OUTCOME:

    OBSERVED_PRESENTATION_COUNT:

    OBSERVED_REJECTION_COUNT:

    CANONICAL_EFFECT_VERIFICATION:

    POSITIVE_CONTROL_RESULT:

    NEGATIVE_CONTROL_RESULT:

    AUTHORITY_INTEGRITY_RESULT:

    HISTORY_INTEGRITY_RESULT:

    LIFETIME_ISOLATION_RESULT:

    VALID_OPERATION_PROGRESS:

    RESOURCE_MEASUREMENT_REFERENCE:

    ARTIFACT_REFERENCE:

    ARTIFACT_INTEGRITY_REFERENCE:

    VERIFICATION_RESULT:

    EVIDENCE_LEVEL:

    REPRODUCTION_STATUS:

    INDEPENDENT_EVALUATION_STATUS:

    LIMITATIONS:

This is a public assurance
record template.

It is not an internal protocol
format or implementation interface.

Unpopulated fields MUST NOT be
interpreted as successful outcomes.

---

## 25. Artifact Binding Requirements

A public evidence record SHOULD
be bound to approved supporting
artifacts.

The artifact reference MUST
identify the corresponding
evaluation rather than merely
the general project.

Where available, the record
SHOULD establish:

- Artifact identity.
- Artifact version.
- Applicable execution reference.
- Integrity verification information.
- Verification outcome.
- Disclosure classification.

A reference to a private artifact
does not independently establish
public verifiability.

Where an artifact is restricted,
the access limitation MUST be
explicitly identified.

---

## 26. Evidence Integrity Boundary

Evidence integrity and correctness
are separate requirements.

A matching cryptographic digest
can establish that an artifact
matches a trusted reference.

It cannot independently establish:

- Authentic execution.
- Complete observation coverage.
- Correct operation attribution.
- Correct verifier semantics.
- Absence of omitted results.

The qualification framework MUST
evaluate these concerns separately.

An integrity reference is not
a substitute for an assurance
argument.

---

## 27. External Evaluation Model

The intended external evaluation
model consists of:

    PUBLIC CORRECTNESS CONTRACT

                |

                v

    AUTHORIZED EVALUATION INTERFACE

                |

                v

    OBSERVABLE EXECUTION RESULTS

                |

                v

    APPROVED EVIDENCE ARTIFACTS

                |

                v

    INDEPENDENT VERIFICATION

                |

                v

    SCOPED ENGINEERING CONCLUSION

This model describes the evaluation
boundary rather than the internal
protocol architecture.

Its purpose is to permit meaningful
technical examination without
requiring disclosure of proprietary
implementation mechanisms.

Actual evaluation availability
remains subject to the supported
evaluation environment and
applicable authorization.

---

## 28. Evaluator-Controlled Assessment

Where supported by an authorized
evaluation environment, the
evaluator SHOULD be able to
control relevant permitted
evaluation conditions.

The evaluator SHOULD be able to:

- Select supported scenarios.
- Establish declared acceptance
  criteria before execution.
- Observe permitted results.
- Verify approved evidence.
- Record negative findings.
- Identify inconclusive outcomes.
- Request clarification of
  evidence limitations.

An evaluation limited exclusively
to preselected successful
demonstrations provides weaker
assurance than an evaluator-controlled
assessment.

The evaluation scope remains
bounded by the applicable
authorization and operating limits.

---

## 29. Challenge and Counterexample Policy

The containment claim is open
to technical challenge through
authorized evaluation.

A valid challenge SHOULD identify:

- The applicable claim.
- The applicable invariant.
- The evaluated operating scope.
- The expected behavior.
- The observed behavior.
- The supporting evidence.
- The proposed contract violation.

A confirmed counterexample MUST
be recorded as a failure of the
affected qualification claim.

The absence of source code access
does not invalidate an attributable
black-box counterexample.

Likewise, the absence of a known
counterexample does not independently
prove universal correctness.

---

## 30. Remediation and Requalification

When a confirmed violation is
identified, remediation MUST be
distinguishable from the original
evaluation.

A remediation record SHOULD
identify:

- Original qualification reference.
- Affected invariant.
- Original failure classification.
- Corrected implementation reference.
- Subsequent verification reference.
- Requalification outcome.
- Remaining limitations.

A corrected result MUST NOT
retroactively convert the original
failure into a successful execution.

Historical engineering evidence
must remain attributable.

---

## 31. Public Disclosure Boundary

The following MAY be published
when approved for disclosure:

- Observable correctness contracts.
- Aggregate evaluation measurements.
- Approved historical results.
- Acceptance and rejection criteria.
- Evidence classifications.
- Approved artifact references.
- Independent evaluation findings.
- Explicit qualification limitations.

The following remain confidential:

- Proprietary replay mechanisms.
- Internal decision algorithms.
- Internal state representations.
- Confidential operation tracking.
- Protected source code.
- Internal runtime interfaces.
- Confidential execution traces.
- Wire-level implementation details.
- Cryptographic implementation details.
- Private infrastructure configuration.

This document defines what must
be demonstrated.

It does not disclose how the
Protected Core achieves the
declared behavior.

---

## 32. Comparison and Novelty Boundary

Replay rejection and at-most-once
operation semantics are established
engineering concerns.

This document does not claim
that replay containment alone
constitutes a novel invention.

The VRP assurance objective is
qualification of the applicable
containment and integrity properties
within its declared continuity-first
session architecture.

Comparative superiority claims
require separately attributable
comparative evidence.

Architectural differentiation
does not independently establish
performance or security superiority.

---

## 33. Technical Reviewer Questions

### Can the claim be disproved?

Yes.

A confirmed prohibited canonical
effect within the applicable
qualification scope constitutes
a counterexample.

### Is a rejection count sufficient?

No.

Canonical effect verification
is additionally required.

### Is access to proprietary source
code mandatory for every evaluation?

No.

Observable properties can be
evaluated through appropriately
qualified black-box interfaces.

Some stronger implementation-level
assurance claims may require
additional authorized evidence.

### Does a verifier PASS establish
independent third-party certification?

No.

Verification and certification
are separate assurance categories.

### Can the evaluator report failure?

Yes.

Negative findings and inconclusive
outcomes are valid engineering
results.

### Does the historical result prove
universal replay resistance?

No.

It remains bounded by the original
evaluation scope and available
evidence.

---

## 34. Qualification Limitations

This document does not establish:

- Universal replay immunity.
- Unlimited resource capacity.
- Universal concurrent correctness.
- Complete formal implementation proof.
- Unconditional application availability.
- Independent third-party certification.
- Correctness under every possible
  execution condition.

Every positive claim remains
limited by its supporting evidence,
observation coverage, and applicable
verification contract.

---

## 35. Master Evidence Integration

The master claims-to-evidence
matrix MUST associate:

    VRP-C04
    VRP-C05

with their applicable invariant
references, scenario identifiers,
historical evidence records,
verification outcomes, and
qualification limitations.

The historical evidence reference
AVE-001 MUST remain distinguishable
from future reproduced or
independently verified results.

No qualification status may
exceed the strength of its
supporting evidence.

---

## 36. Related Assurance Documents

- [Executive Engineering Assurance](VRP_EXECUTIVE_ENGINEERING_ASSURANCE.md)
- [Formal Continuity Invariants](VRP_FORMAL_CONTINUITY_INVARIANTS.md)
- [Session Identity Preservation](VRP_SESSION_IDENTITY_PRESERVATION.md)
- [Transport Independence](VRP_TRANSPORT_INDEPENDENCE.md)
- [Adversarial Validation Evidence](VRP_ADVERSARIAL_VALIDATION_EVIDENCE.md)

---

## 37. Final Engineering Declaration

    SESSION ≠ TRANSPORT

    Rejection is an observation.

    Containment is a correctness property.

    Canonical effect exclusion
    is a verification obligation.

    A successful demonstration
    is not a universal proof.

    A confirmed counterexample
    is a valid engineering result.

    Confidential implementation
    does not eliminate the need
    for external verification.

    The claim is public.

    The acceptance criteria are public.

    The qualification boundaries
    are public.

    The Protected Core remains
    confidential.

---

**Veil Routing Protocol — VRP**

**Jumping VPN**

**Architect and Creator: Vitalijus Riabovas**

**Historical reported result: 9,999 replay rejections.**

**14 qualification scenarios.**

**6 evidence sufficiency levels.**

**Explicit falsification criteria.**

**Evaluator-controlled verification model.**

**Observable correctness. Protected implementation.**

**End of document — VRP-PA-006**
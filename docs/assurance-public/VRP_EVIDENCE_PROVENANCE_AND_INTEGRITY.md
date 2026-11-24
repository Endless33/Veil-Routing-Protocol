# VRP Evidence Provenance and Integrity

## Veil Routing Protocol — Jumping VPN

**Document ID:** VRP-PA-012
**Version:** 1.0
**Classification:** PUBLIC
**Status:** Engineering Evidence Assurance Contract
**Author:** Vitalijus Riabovas
**Protected Core:** CONFIDENTIAL

---

## 1. Executive Statement

An engineering claim becomes technically
meaningful when its supporting evidence
can be attributed, examined, challenged,
and independently evaluated.

A specification is not an execution.

An execution report is not necessarily
an authentic execution record.

An authentic record is not necessarily
a correct engineering conclusion.

Veil Routing Protocol establishes the
following architectural principle:

    SESSION ≠ TRANSPORT

The assurance framework establishes
a corresponding evidence principle:

    CLAIM ≠ EVIDENCE

This document defines the public
requirements for evidence provenance,
artifact integrity, execution attribution,
verification, publication, and independent
technical examination.

The proprietary implementation remains
confidential.

---

## 2. Engineering Objective

The objective is to establish an
auditable relationship between:

- A declared engineering claim.
- An applicable correctness contract.
- An identified implementation.
- An attributable execution.
- An observable result.
- A preserved evidence artifact.
- A qualified verification method.
- An engineering conclusion.
- An independent evaluation record.

Each relationship requires evidence
appropriate to its meaning.

A missing relationship MUST NOT
be silently replaced with an
assumption of correctness.

---

## 3. Primary Assurance Claims

Primary claim references:

    VRP-C12 — Evidence integrity
              and provenance.

    VRP-C15 — Reproducible external
              verification.

Supporting claim references:

    VRP-C01 through VRP-C14.

Evidence integrity supports every
empirical engineering claim.

It does not independently establish
the correctness of the behavior
described by that evidence.

---

## 4. Applicable Invariants

Primary invariant references:

    INV-012 — Evidence integrity.

    INV-015 — Reproducible verification.

Supporting invariant references
depend on the evaluated claim.

Normative invariant definitions
are established in VRP-PA-002.

This document specializes their
application to evidence handling,
publication, and verification.

---

## 5. Evidence Assurance Model

The public assurance framework
distinguishes:

    CLAIM

    CONTRACT

    IMPLEMENTATION

    EXECUTION

    OBSERVATION

    ARTIFACT

    VERIFICATION

    CONCLUSION

    REPRODUCTION

These categories describe
engineering evidence relationships.

They do not describe internal
runtime structures, execution
algorithms, or proprietary
protocol mechanisms.

A qualification conclusion MUST
remain attributable to its
supporting relationships.

---

## 6. Evidence Chain

The conceptual public evidence
chain is:

    DECLARED CLAIM
          |
          v
    CORRECTNESS CONTRACT
          |
          v
    IMPLEMENTATION REFERENCE
          |
          v
    EXECUTION REFERENCE
          |
          v
    OBSERVATION RECORD
          |
          v
    EVIDENCE ARTIFACT
          |
          v
    VERIFICATION RESULT
          |
          v
    BOUNDED CONCLUSION

Independent reproduction MAY
provide an additional separately
attributable evidence chain.

This representation describes
public assurance relationships.

It is not a disclosure of
the Protected Core architecture.

---

## 7. Evidence Identity

Each approved evidence record
SHOULD possess a stable
public evidence reference.

The reference SHOULD distinguish
the record from:

- Other executions.
- Other implementation versions.
- Other evaluation environments.
- Other measurement scopes.
- Other verification outcomes.
- Subsequent corrected records.

An evidence identifier alone
does not establish authenticity.

Its meaning depends on the
associated provenance record.

---

## 8. Claim Attribution

Every empirical evidence record
MUST identify the claim or
claims it is intended to support.

The record SHOULD establish:

    CLAIM_REFERENCE

    INVARIANT_REFERENCE

    SCENARIO_REFERENCE

    CONTRACT_VERSION

    ACCEPTANCE_CRITERIA_REFERENCE

An artifact MUST NOT receive
unrestricted evidentiary meaning
merely because it is associated
with the VRP project.

Evidence applicability MUST
remain claim-specific.

---

## 9. Implementation Attribution

An empirical result MUST remain
associated with the evaluated
implementation.

An approved implementation
reference MAY consist of:

- An opaque release identifier.
- An approved build identifier.
- An approved artifact digest.
- An approved source revision reference.
- An externally attributable release record.

Publication MUST NOT require
disclosure of proprietary
repository structure or
protected source code.

An implementation reference
MUST NOT be interpreted as
proof that a particular
execution used that implementation
unless the relationship is
independently established
within the applicable trust model.

---

## 10. Build Attribution

Where applicable, the evidence
record SHOULD distinguish:

    IMPLEMENTATION_REFERENCE

    BUILD_REFERENCE

    EXECUTABLE_ARTIFACT_REFERENCE

    EXECUTION_REFERENCE

The relationship between these
references MUST be documented
at a level sufficient for
the claimed assurance scope.

A source revision reference
does not independently establish
the identity of an executable.

An executable digest does not
independently establish that
the executable was used during
a reported execution.

---

## 11. Execution Attribution

Every dedicated empirical
qualification SHOULD identify
the actual evaluated execution.

Relevant public attributes include:

- Execution reference.
- Evaluation scenario.
- Implementation reference.
- Evaluation environment class.
- Observation interval.
- Applicable workload.
- Evaluation outcome.
- Evidence collection method.
- Known limitations.

Sensitive operational details
MUST remain subject to
publication review.

The execution reference MUST
NOT be reused in a manner
that obscures distinct runs.

---

## 12. Observation Attribution

An observation MUST remain
associated with the execution
from which it originated.

The evidence record SHOULD
distinguish:

    OBSERVED EVENT

    REPORTED EVENT

    DERIVED MEASUREMENT

    VERIFICATION CONCLUSION

    SYNTHETIC FIXTURE

These categories are not
interchangeable.

A derived conclusion MUST NOT
be represented as an original
runtime observation.

A synthetic fixture MUST NOT
be represented as captured
runtime evidence.

---

## 13. Evidence Origin Classification

Approved evidence SHOULD
identify its origin.

| Origin class | Meaning |
|---|---|
| PROJECT_REPORTED | Result reported by the project |
| PROJECT_CAPTURED | Artifact captured during project execution |
| PROJECT_VERIFIED | Evidence evaluated by a project-controlled method |
| EXTERNALLY_OBSERVED | Execution observed by an external party |
| EXTERNALLY_CONTROLLED | Evaluation conditions controlled externally within authorized scope |
| INDEPENDENTLY_REPRODUCED | Separately attributable independent execution |
| SYNTHETIC | Constructed verification fixture |

Origin classification does not
automatically determine semantic
correctness.

The applicable evidence
sufficiency level MUST be
assigned separately.

---

## 14. Artifact Integrity

Artifact integrity concerns
whether an examined artifact
matches an expected reference.

An approved cryptographic
digest MAY support artifact
integrity verification.

Conceptually:

    H(A_observed) = H(A_reference)

Where:

    H =
        Approved digest function.

    A_observed =
        Examined evidence artifact.

    A_reference =
        Referenced evidence artifact.

A matching digest supports
byte-level consistency under
the applicable cryptographic
assumptions.

It does not independently
establish execution authenticity,
observation completeness,
or engineering correctness.

These symbols describe generic
artifact verification semantics.

They do not disclose proprietary
VRP mechanisms.

---

## 15. Trusted Reference Requirement

A digest comparison requires
an appropriate expected reference.

The evaluation MUST distinguish:

    ARTIFACT

    EXPECTED_DIGEST

    REFERENCE_ORIGIN

    REFERENCE_TRUST

A digest distributed alongside
an artifact through the same
untrusted channel does not
independently establish
publisher authenticity.

An attacker capable of replacing
both an artifact and its
untrusted reference may preserve
apparent digest consistency.

The reference trust model
MUST therefore remain explicit.

---

## 16. Artifact Manifest

An approved evidence bundle
MAY include a cryptographic
integrity manifest.

The manifest SHOULD identify:

- Included artifact references.
- Applicable digest algorithm.
- Expected artifact digests.
- Manifest version.
- Evidence bundle reference.

The manifest MUST NOT contain
unapproved private paths,
infrastructure identifiers,
or confidential implementation
information.

A manifest MUST NOT be treated
as proof that every relevant
execution artifact was included.

Completeness requires separate
qualification.

---

## 17. Public Integrity Verification

For a compatible approved
SHA-256 manifest, an evaluator
MAY perform the standard
integrity check:

    sha256sum -c SHA256SUMS

A successful check establishes
consistency with the supplied
manifest for the examined files.

The evaluator MUST separately
establish:

- Manifest authenticity.
- Expected artifact coverage.
- Artifact provenance.
- Evidence applicability.
- Semantic correctness.

This is a generic public
verification command.

It does not access or disclose
the Protected Core.

No completed manifest check
is asserted by this document.

---

## 18. Manifest Coverage

Manifest verification MUST
remain distinguishable from
manifest coverage verification.

A manifest may correctly
describe every listed artifact
while omitting a required
artifact.

The evidence contract SHOULD
identify the expected artifact
categories before qualification.

The evaluator SHOULD determine:

    EXPECTED_ARTIFACTS

    PRESENT_ARTIFACTS

    VERIFIED_ARTIFACTS

    MISSING_REQUIRED_ARTIFACTS

    UNEXPECTED_ARTIFACTS

A missing mandatory artifact
MUST prevent an unsupported
complete qualification verdict.

---

## 19. Publisher Authentication

Approved evidence MAY be
associated with a digital
signature or another suitable
publisher authentication method.

The verification record SHOULD
identify:

- Authenticated publisher identity.
- Signed content scope.
- Verification reference.
- Applicable trust assumptions.
- Verification outcome.

A valid signature supports
authentication of the signed
content under the applicable
trust model.

It does not independently
establish that the signed
engineering claims are true.

This document does not assert
deployment of a particular
proprietary signing mechanism.

---

## 20. Signature Scope

Where a digital signature
is used, the evaluator MUST
establish what was authenticated.

Possible scopes include:

- An individual artifact.
- An evidence manifest.
- An execution report.
- A release record.
- An independent evaluation report.

Authentication of one artifact
does not automatically
authenticate unrelated artifacts.

A valid signature over an
incomplete evidence record
does not establish evidence
completeness.

---

## 21. Timestamp Attribution

Evidence timestamps SHOULD
identify their meaning.

Relevant distinctions include:

    EXECUTION_START_TIME

    EXECUTION_END_TIME

    OBSERVATION_TIME

    ARTIFACT_CREATION_TIME

    VERIFICATION_TIME

    PUBLICATION_TIME

    EXTERNAL_TIMESTAMP_TIME

These timestamps are not
interchangeable.

A file modification timestamp
does not independently
establish execution time.

A publication timestamp
does not independently
establish the time at which
the reported behavior occurred.

Where trusted timestamping
is used, its scope and
trust assumptions MUST
remain explicit.

---

## 22. Temporal Evidence Integrity

Evidence ordering MUST be
sufficient for the applicable
qualification objective.

A final successful observation
does not independently establish
that every preceding transition
was compliant.

Where a claim depends on
temporal behavior, the evidence
SHOULD preserve the relevant
observable relationships.

Examples include:

- Baseline before disturbance.
- Disturbance occurrence.
- Observable transition.
- Recovery observation.
- Subsequent integrity verification.
- Post-recovery observation.

The required temporal resolution
depends on the evaluated claim.

---

## 23. External Real-Time Precedence

Where an evaluated operation
domain requires real-time
precedence verification, an
external observer MAY record
observable invocation and
completion boundaries.

For operations X and Y:

    Completion(X) < Invocation(Y)

establishes an observed
precedence relationship when
both boundaries are attributable
to a suitable observation
reference.

A valid sequential interpretation
must preserve that relationship
where the applicable operation
contract requires it.

Where observation uncertainty
prevents establishing precedence,
the relationship MUST remain
unresolved.

Internal runtime clock access
is not inherently required
for every externally observable
precedence relationship.

This does not establish that
all VRP operation domains
are externally observable
with sufficient resolution.

VRP-PA-009 remains applicable.

---

## 24. Observation Coverage

Evidence coverage describes
which relevant behaviors were
observable during an evaluation.

The record SHOULD identify:

- Observed operation classes.
- Observed execution intervals.
- Observable effect boundaries.
- Known observation gaps.
- Incomplete records.
- Unsupported observations.
- Relevant measurement limitations.

The absence of a recorded
violation does not independently
establish the absence of
an actual violation.

The verification method MUST
account for material
observation limitations.

---

## 25. Evidence Completeness

Evidence completeness MUST
be evaluated relative to
a defined qualification scope.

Completeness does not mean
publication of every internal
runtime detail.

It means availability of
the evidence necessary to
support the stated conclusion.

A sanitized public record
MAY be sufficient for one
black-box claim while remaining
insufficient for another.

The evidence owner MUST
NOT claim completeness
beyond the applicable
verification objective.

---

## 26. Evidence Preservation

Original approved evidence
SHOULD remain distinguishable
from subsequent derived
or corrected records.

Relevant categories include:

    ORIGINAL_CAPTURE

    SANITIZED_PUBLIC_ARTIFACT

    DERIVED_MEASUREMENT

    VERIFICATION_REPORT

    CORRECTED_REPORT

    REPRODUCTION_RECORD

A subsequent successful
verification MUST NOT
retroactively modify the
meaning of an earlier
failed execution.

Evidence corrections MUST
remain attributable.

---

## 27. Evidence Immutability Boundary

An evidence artifact MAY
be preserved using an
approved immutable or
tamper-evident publication
mechanism.

The evidence record MUST
distinguish:

    IMMUTABILITY

    TAMPER DETECTION

    PUBLISHER AUTHENTICATION

    EXECUTION AUTHENTICITY

These are separate properties.

A cryptographic digest
does not prevent modification.

It supports detection of
modification relative to
an appropriate reference.

A publication history
does not independently
establish that the original
observations were accurate.

---

## 28. Evidence Transformation

Public evidence MAY be
derived from restricted
engineering records.

Permitted transformations
MAY include:

- Removal of sensitive identifiers.
- Aggregation of measurements.
- Normalization of reporting units.
- Replacement of private references
  with approved public references.
- Removal of irrelevant metadata.
- Conversion to a public
  reporting format.

Transformations MUST preserve
the relationships required
for the claimed verification
objective.

A transformation MUST NOT
convert an observed failure
into a successful outcome.

---

## 29. Sanitization Attribution

Where public evidence is
derived from restricted
records, the public artifact
SHOULD identify its
transformation classification.

Candidate classifications:

    ORIGINAL_APPROVED_ARTIFACT

    SANITIZED_ARTIFACT

    AGGREGATED_ARTIFACT

    DERIVED_REPORT

    SYNTHETIC_FIXTURE

The evidence owner SHOULD
document material effects
of the transformation on
verification coverage.

The public artifact MUST
NOT be described as an
unmodified original when
material transformations
have occurred.

---

## 30. Confidentiality and Evidence Sufficiency

The Protected Core remains
confidential.

Confidentiality does not
eliminate the requirement
for sufficient evidence.

Where an engineering claim
cannot be adequately verified
through approved public
observations, the claim
MUST retain its limitation.

The following distinction
is fundamental:

    IMPLEMENTATION CONFIDENTIALITY
        !=
    EXEMPTION FROM VERIFICATION

The project MAY protect
implementation details while
permitting meaningful external
evaluation of observable
behavior.

Not every implementation-level
claim can necessarily be
established through black-box
evaluation alone.

---

## 31. Verification Method Attribution

A verification result MUST
identify the applicable
verification method.

Relevant public attributes
SHOULD include:

- Verifier reference.
- Verifier version.
- Applicable contract.
- Supported evidence format.
- Verification scope.
- Required observations.
- Acceptance criteria.
- Known limitations.
- Verification control results.

A verifier success label
without an established
verification scope MUST
NOT receive unrestricted
evidentiary meaning.

---

## 32. Verifier Independence

The following MUST remain
distinguishable:

    SEPARATE VERIFICATION MECHANISM

    INDEPENDENT VERIFICATION LOGIC

    INDEPENDENT EXECUTION

    INDEPENDENT EVALUATING PARTY

A separately implemented
verification mechanism MAY
reduce certain forms of
common implementation error.

It does not independently
establish organizational
or evaluator independence.

A project-controlled verifier
execution MUST NOT be
represented as an independent
third-party audit.

---

## 33. Verification Trust Boundary

A verifier may correctly
evaluate the evidence it
receives while remaining
unable to establish whether
that evidence accurately
represents the original
execution.

The following MUST remain
separate:

    INPUT_AUTHENTICITY

    INPUT_COMPLETENESS

    VERIFIER_CORRECTNESS

    CONTRACT_APPLICABILITY

    OUTPUT_CORRECTNESS

Each property requires
appropriate supporting
evidence.

A successful verifier result
does not independently
establish every property.

---

## 34. Positive Verification Controls

The verification method
SHOULD demonstrate acceptance
of applicable compliant records.

Required control categories
MAY include:

- Valid artifact digest.
- Valid evidence attribution.
- Complete mandatory observations.
- Consistent outcome accounting.
- Supported contract version.
- Valid applicable qualification.

The controls MUST remain
separately attributable.

A verifier that rejects
every record cannot establish
meaningful verification
effectiveness through
negative controls alone.

---

## 35. Negative Verification Controls

The verification method
SHOULD demonstrate detection
of relevant noncompliant
or insufficient records.

Approved synthetic fixtures
MAY include:

- Modified evidence artifact.
- Incorrect expected digest.
- Missing required artifact.
- Contradictory execution reference.
- Unsupported contract version.
- Invalid outcome accounting.
- Missing mandatory observation.
- Known semantic violation.
- Incorrect evidence classification.
- Synthetic record incorrectly
  presented as original evidence.

The expected outcome MUST
be established before
control execution.

Synthetic controls MUST
remain clearly distinguishable
from actual runtime evidence.

---

## 36. Verification Outcome Separation

The public framework
distinguishes:

    INTEGRITY_VERIFICATION

    AUTHENTICITY_VERIFICATION

    COVERAGE_VERIFICATION

    SEMANTIC_VERIFICATION

    REPRODUCTION_VERIFICATION

An overall verification
conclusion MUST identify
which categories were
actually evaluated.

A successful integrity
verification MUST NOT
automatically establish
semantic verification.

---

## 37. Evidence Qualification Verdicts

Permitted qualification
verdicts include:

    PASS

    FAIL

    INCONCLUSIVE

    NOT TESTED

    NOT APPLICABLE

A PASS requires satisfaction
of all applicable mandatory
criteria within the stated
verification scope.

A confirmed mandatory
violation constitutes FAIL.

Insufficient observations
produce INCONCLUSIVE.

An unexecuted evaluation
remains NOT TESTED.

An excluded scenario remains
NOT APPLICABLE only where
its exclusion is justified.

---

## 38. Evidence Sufficiency Levels

The evidence levels established
in VRP-PA-006 remain applicable.

| Level | Evidence requirement |
|---|---|
| E0 | Public contract specified |
| E1 | Execution outcome reported |
| E2 | Attributable execution artifacts available |
| E3 | Applicable evidence and controls verified |
| E4 | Separately attributable reproduction |
| E5 | Independent evaluation completed |

Evidence levels describe
evidence sufficiency.

They do not replace
qualification verdicts.

An independently reproduced
failure may possess stronger
evidentiary support than
an unverified success report.

---

## 39. Evidence Promotion Requirements

Promotion between evidence
levels MUST require additional
qualifying evidence.

### E0 to E1

Requires an actual reported
execution outcome.

### E1 to E2

Requires attributable
execution artifacts sufficient
for the stated evidence scope.

### E2 to E3

Requires applicable verification,
qualified controls, and
sufficient observation coverage.

### E3 to E4

Requires separately attributable
reproduction under documented
conditions.

### E4 to E5

Requires independent evaluation
with explicit scope, trust
boundaries, and conclusions.

Additional specification
documents alone do not
establish empirical promotion.

---

## 40. Evidence Level and Verdict Independence

The following dimensions
MUST remain distinct:

    EVIDENCE_LEVEL

    QUALIFICATION_VERDICT

    EVALUATION_SCOPE

    REPRODUCTION_STATUS

    INDEPENDENCE_STATUS

Illustrative examples:

    E1 / REPORTED SUCCESS

    E3 / PASS

    E3 / FAIL

    E4 / INCONCLUSIVE

    E5 / FAIL

These examples are conceptual.

They are not actual VRP
qualification results.

Higher evidence sufficiency
does not necessarily imply
a positive engineering verdict.

---

## 41. Historical Evidence Register

The historical references
established in VRP-PA-005
remain applicable.

| Evidence ID | Reported outcome | Public level |
|---|---|---|
| AVE-001 | 9,999 replay presentations rejected | E1 |
| AVE-002 | 1,000 migrations with reported continuity preservation | E1 |
| AVE-003 | Approximately 41.6 seconds recovery | E1 |
| AVE-004 | Stale authority rejection | E1 |
| AVE-005 | Epoch rollback rejection | E1 |
| AVE-006 | Canonical rewrite rejection | E1 |
| AVE-007 | Evidence verifier PASS | E1 |

These classifications apply
to the evidence presented
within this assurance series.

Original execution artifacts
are not embedded in this
document.

No stronger public evidence
level is assigned solely
through repetition of
historical results.

---

## 42. Historical Provenance Limitations

The historical evidence
register does not independently
establish:

- A common implementation reference.
- A common execution environment.
- A common execution interval.
- Complete original artifact availability.
- Complete observation coverage.
- Independent reproduction.
- Independent third-party certification.

Each historical reference
requires its own provenance
qualification.

Separate reported outcomes
MUST NOT be merged into
a single unsupported
execution record.

---

## 43. Current Public Provenance Status

    DOCUMENT_REFERENCE:
        VRP-PA-012

    EVIDENCE_PROVENANCE_CONTRACT:
        SPECIFIED

    HISTORICAL_EXECUTION_REFERENCES:
        REPORTED

    HISTORICAL_EVIDENCE_LEVEL:
        E1

    DEDICATED_PROVENANCE_ARTIFACTS:
        NOT EMBEDDED

    DEDICATED_PUBLIC_PROVENANCE_LEVEL:
        E0

    COMPLETE_PUBLIC_CHAIN_OF_CUSTODY:
        NOT ESTABLISHED BY THIS RECORD

    INDEPENDENT_EVALUATION:
        NOT ESTABLISHED BY THIS RECORD

This classification describes
the evidence presented
within this document.

It does not establish that
additional restricted evidence
does not exist.

---

## 44. Qualification Scenario Registry

| Scenario | Evaluation objective |
|---|---|
| EPI-001 | Evidence identity |
| EPI-002 | Claim attribution |
| EPI-003 | Implementation attribution |
| EPI-004 | Build attribution |
| EPI-005 | Execution attribution |
| EPI-006 | Observation attribution |
| EPI-007 | Artifact integrity |
| EPI-008 | Trusted reference verification |
| EPI-009 | Manifest coverage |
| EPI-010 | Publisher authentication |
| EPI-011 | Signature scope verification |
| EPI-012 | Timestamp attribution |
| EPI-013 | Temporal evidence integrity |
| EPI-014 | Observation coverage |
| EPI-015 | Evidence completeness |
| EPI-016 | Original evidence preservation |
| EPI-017 | Sanitization integrity |
| EPI-018 | Verification method attribution |
| EPI-019 | Positive verification controls |
| EPI-020 | Negative verification controls |
| EPI-021 | Evidence level classification |
| EPI-022 | Evidence correction history |
| EPI-023 | Independent recalculation |
| EPI-024 | Independent reproduction |
| EPI-025 | Compound provenance qualification |

Registry inclusion defines
an evaluation objective.

It does not establish
completed execution or
qualification.

---

## 45. Illustrative Evidence Record A

### Matching artifact digest

This is a synthetic
verification example.

Assumed observations:

    EXPECTED_DIGEST:
        AVAILABLE

    OBSERVED_DIGEST:
        MATCH

    EXPECTED_REFERENCE_TRUST:
        ESTABLISHED

    EXECUTION_AUTHENTICITY:
        UNVERIFIED

Expected qualification:

    ARTIFACT_INTEGRITY:
        PASS

    EXECUTION_AUTHENTICITY:
        INCONCLUSIVE

    SEMANTIC_CORRECTNESS:
        NOT ESTABLISHED

A valid artifact digest
does not independently
prove execution correctness.

---

## 46. Illustrative Evidence Record B

### Modified artifact

Assumed synthetic observations:

    EXPECTED_DIGEST:
        AVAILABLE

    OBSERVED_DIGEST:
        MISMATCH

    EXPECTED_REFERENCE_TRUST:
        ESTABLISHED

Expected qualification:

    ARTIFACT_INTEGRITY:
        FAIL

    AFFECTED_EVIDENCE:
        NOT ACCEPTABLE AS THE REFERENCED ARTIFACT

A digest mismatch establishes
a consistency failure relative
to the expected reference.

It does not independently
establish malicious intent.

---

## 47. Illustrative Evidence Record C

### Valid manifest with missing evidence

Assumed synthetic observations:

    LISTED_ARTIFACT_DIGESTS:
        MATCH

    REQUIRED_ARTIFACT:
        OMITTED FROM MANIFEST

Expected qualification:

    LISTED_ARTIFACT_INTEGRITY:
        PASS

    EVIDENCE_COMPLETENESS:
        FAIL

    AFFECTED_CLAIM:
        INCONCLUSIVE

A valid manifest does not
establish complete evidence
coverage.

---

## 48. Illustrative Evidence Record D

### Authentic report with failed contract

Assumed synthetic observations:

    PUBLISHER_AUTHENTICATION:
        PASS

    ARTIFACT_INTEGRITY:
        PASS

    CANONICAL_INTEGRITY_CONTRACT:
        FAIL

Expected qualification:

    EVIDENCE_AUTHENTICITY:
        PASS

    ENGINEERING_CORRECTNESS:
        FAIL

Authentic evidence can
demonstrate incorrect
runtime behavior.

Authentication MUST NOT
override a confirmed
contract violation.

---

## 49. Illustrative Evidence Record E

### Unsupported independent verification claim

Assumed synthetic observations:

    VERIFIER_RESULT:
        PASS

    VERIFIER_EXECUTION:
        PROJECT_CONTROLLED

    EXTERNAL_EVALUATOR:
        NOT ESTABLISHED

Expected qualification:

    VERIFICATION_RESULT:
        RECORDED

    INDEPENDENT_EVALUATION:
        NOT ESTABLISHED

A separate verification
mechanism does not establish
an independent evaluating party.

---

## 50. Illustrative Evidence Record F

### Sanitization removes required observation

Assumed synthetic observations:

    PUBLIC_ARTIFACT_INTEGRITY:
        PASS

    REQUIRED_EFFECT_OBSERVATION:
        REMOVED DURING SANITIZATION

Expected qualification:

    PUBLIC_ARTIFACT_INTEGRITY:
        PASS

    AFFECTED_SEMANTIC_CLAIM:
        INCONCLUSIVE

Confidentiality requirements
may limit public verification.

They MUST NOT be used
to justify unsupported
qualification promotion.

---

## 51. Illustrative Evidence Record G

### Independent negative result

Assumed synthetic observations:

    INDEPENDENT_EVALUATION:
        ESTABLISHED

    EXECUTION_ATTRIBUTION:
        ESTABLISHED

    MANDATORY_CONTRACT_VIOLATION:
        CONFIRMED

Expected qualification:

    ENGINEERING_VERDICT:
        FAIL

    INDEPENDENT_FINDING:
        VALID WITHIN QUALIFIED SCOPE

An independent negative
result remains legitimate
engineering evidence.

The assurance framework
MUST NOT require positive
conclusions as a condition
of evidence acceptance.

---

## 52. Evidence Acceptance Matrix

| Observed condition | Applicable verdict |
|---|---|
| All mandatory evidence requirements satisfied | PASS |
| Confirmed artifact integrity mismatch | FAIL for integrity scope |
| Confirmed attribution contradiction | FAIL for attribution scope |
| Confirmed missing mandatory artifact | FAIL for completeness scope |
| Confirmed semantic contract violation | FAIL for semantic scope |
| Untrusted expected digest reference | INCONCLUSIVE for authenticity |
| Missing execution attribution | INCONCLUSIVE |
| Insufficient observation coverage | INCONCLUSIVE |
| Unsupported verification method | INCONCLUSIVE |
| Independent evaluation not executed | NOT TESTED |
| Justified exclusion from scope | NOT APPLICABLE |

A failure in one evidence
dimension MUST remain
visible even where another
dimension receives PASS.

---

## 53. Public Evidence Bundle Layout

The following is a proposed
public evidence publication
layout.

    evidence/
        <evidence-id>/
            README.md
            CLAIMS.json
            PROVENANCE.json
            ENVIRONMENT.json
            EXECUTION_SUMMARY.json
            OBSERVATIONS.json
            MEASUREMENTS.csv
            VERIFICATION_RESULTS.json
            CONTROL_RESULTS.json
            LIMITATIONS.md
            SHA256SUMS

Optional approved artifacts
MAY include:

    MANIFEST_SIGNATURE

    PUBLISHER_REFERENCE

    EXTERNAL_TIMESTAMP_REFERENCE

    INDEPENDENT_REVIEW.md

These names describe proposed
public evidence artifacts.

They are not claims that
the files already exist.

They do not describe
Protected Core repository
structure.

---

## 54. Minimum Evidence Bundle Contract

A dedicated public evidence
bundle SHOULD establish:

1. The claim being evaluated.

2. The applicable contract.

3. The evaluated implementation.

4. The execution reference.

5. The relevant observations.

6. The applicable measurements.

7. The verification method.

8. The verification controls.

9. The engineering conclusion.

10. The known limitations.

11. The artifact integrity reference.

12. The applicable trust model.

A bundle MUST NOT receive
a stronger evidence level
than its actual contents
and verification support.

---

## 55. Public Provenance Record

The following is a proposed
public reporting template:

    DOCUMENT_ID: VRP-PA-012

    EVIDENCE_ID:

    CLAIM_REFERENCES:

    INVARIANT_REFERENCES:

    SCENARIO_REFERENCES:

    CONTRACT_VERSION:

    IMPLEMENTATION_REFERENCE:

    BUILD_REFERENCE:

    EXECUTABLE_ARTIFACT_REFERENCE:

    EXECUTION_REFERENCE:

    EXECUTION_ORIGIN_CLASS:

    EVALUATION_ENVIRONMENT_CLASS:

    OBSERVATION_INTERVAL:

    OBSERVATION_METHOD:

    OBSERVATION_COVERAGE:

    ORIGINAL_ARTIFACT_REFERENCE:

    PUBLIC_ARTIFACT_REFERENCE:

    TRANSFORMATION_CLASS:

    TRANSFORMATION_LIMITATIONS:

    ARTIFACT_DIGEST_ALGORITHM:

    ARTIFACT_DIGEST_REFERENCE:

    MANIFEST_REFERENCE:

    MANIFEST_COVERAGE_RESULT:

    EXPECTED_REFERENCE_TRUST:

    PUBLISHER_AUTHENTICATION_RESULT:

    TIMESTAMP_ATTRIBUTION_RESULT:

    EXECUTION_AUTHENTICITY_RESULT:

    ARTIFACT_INTEGRITY_RESULT:

    EVIDENCE_COMPLETENESS_RESULT:

    VERIFIER_REFERENCE:

    VERIFIER_VERSION:

    VERIFICATION_SCOPE:

    POSITIVE_CONTROL_RESULT:

    NEGATIVE_CONTROL_RESULT:

    SEMANTIC_VERIFICATION_RESULT:

    QUALIFICATION_VERDICT:

    EVIDENCE_LEVEL:

    REPRODUCTION_STATUS:

    INDEPENDENT_EVALUATION_STATUS:

    LIMITATIONS:

This template defines public
reporting obligations.

It is not an internal
runtime data structure,
wire format, or proprietary
implementation interface.

Unpopulated fields MUST NOT
be interpreted as successful
qualification results.

---

## 56. Machine-Readable Evidence Requirements

Where approved evidence
is published in a
machine-readable format,
the publication SHOULD
define:

- Field meanings.
- Required fields.
- Optional fields.
- Supported values.
- Measurement units.
- Version compatibility.
- Missing-value semantics.
- Verification expectations.

Unknown values MUST remain
distinguishable from zero,
false, or successful values.

A missing observation MUST
NOT be interpreted as
absence of a violation.

Public reporting formats
MUST remain separate from
proprietary protocol formats.

---

## 57. Evidence Accounting

Where applicable, the
evidence record SHOULD
reconcile:

    EXECUTIONS_ATTEMPTED

    EXECUTIONS_COMPLETED

    EXECUTIONS_FAILED

    EXECUTIONS_INCONCLUSIVE

    EXECUTIONS_ABORTED

    EXECUTIONS_NOT_PERFORMED

The accounting definitions
MUST prevent ambiguous
double counting.

A configured execution count
does not establish an actual
completed execution count.

Skipped or aborted tests
MUST NOT be counted as PASS.

---

## 58. Failed Evidence Preservation

Failed evaluations are
part of the engineering
record.

Where relevant to the
published claim, the
evidence owner MUST NOT
conceal confirmed failures
through selective reporting.

The record SHOULD distinguish:

- Original failure.
- Affected implementation.
- Affected contract.
- Remediation status.
- Corrected implementation.
- Subsequent verification.
- Remaining limitations.

A corrected implementation
does not retroactively
change an earlier execution
outcome.

---

## 59. Evidence Correction Policy

A published evidence record
MAY require correction.

The corrected record
SHOULD identify:

    ORIGINAL_EVIDENCE_REFERENCE

    CORRECTION_REFERENCE

    CORRECTION_REASON

    AFFECTED_CLAIMS

    ORIGINAL_CONCLUSION

    CORRECTED_CONCLUSION

    REQUALIFICATION_STATUS

A material correction
MUST NOT be silently
represented as the
original publication.

The evidence history
SHOULD remain auditable.

---

## 60. Evidence Revocation

An evidence record MAY
be withdrawn from active
assurance use where its
reliability is materially
compromised.

Relevant reasons MAY include:

- Invalid execution attribution.
- Confirmed measurement defect.
- Invalid verification method.
- Incorrect artifact reference.
- Material evidence omission.
- Confirmed publication error.
- Compromised reference trust.

Withdrawal SHOULD identify
the affected evidence and
claims.

Revocation of evidence
does not independently
establish a runtime defect.

It removes or limits reliance
on the affected evidence.

---

## 61. Evidence Supersession

New evidence MAY supersede
an earlier qualification
record within a defined
scope.

Supersession MUST identify:

- Earlier evidence reference.
- New evidence reference.
- Applicable implementation change.
- Applicable contract change.
- Reason for supersession.
- Current qualification status.

A newer record MUST NOT
automatically invalidate
an earlier record concerning
a different implementation
or evaluation scope.

Historical outcomes remain
historically attributable.

---

## 62. Publication History

Approved evidence SHOULD
remain associated with an
identifiable publication
history.

Relevant public records
MAY include:

- Initial publication reference.
- Evidence bundle version.
- Manifest reference.
- Correction history.
- Supersession history.
- Withdrawal status.
- Independent review references.

A publication history
supports traceability.

It does not independently
establish execution authenticity
or semantic correctness.

---

## 63. Chain of Custody

Where required by the
evaluation scope, the
evidence owner SHOULD
document relevant custody
relationships.

These MAY include:

    CAPTURE

    PRESERVATION

    TRANSFORMATION

    VERIFICATION

    PUBLICATION

    EXTERNAL_RECEIPT

The public record MAY
use approved opaque
references to protect
confidential operational
information.

Custody documentation
MUST remain sufficient
for the claimed provenance
assurance level.

An undocumented custody
relationship MUST NOT
be represented as verified.

---

## 64. Independent Recalculation

An evaluator SHOULD be
able to independently
recalculate supported
derived measurements
where sufficient approved
data is available.

Examples include:

- Operation totals.
- Rejection totals.
- Completion rates.
- Recovery durations.
- Latency distributions.
- Throughput calculations.
- Outcome reconciliation.

Independent recalculation
does not require access
to proprietary runtime
algorithms.

It does not independently
establish that the supplied
observations originated
from the claimed execution.

---

## 65. Evaluator-Controlled Evidence

Where an authorized
black-box environment
supports independent
evaluation, an evaluator
SHOULD be able to collect
approved observations
under evaluator-selected
conditions.

Relevant capabilities MAY
include:

- Selection of permitted scenarios.
- Definition of acceptance criteria.
- Recording of external observations.
- Independent timing measurements.
- Examination of approved artifacts.
- Independent outcome accounting.
- Submission of negative findings.

The evaluator SHOULD NOT
be required to accept
project-generated conclusions
as the sole basis for
qualification.

Actual availability depends
on supported evaluation
interfaces and authorization.

---

## 66. Fresh Execution Attribution

An independent evaluator
MAY require evidence that
an observed result belongs
to a newly requested
evaluation rather than
a previously recorded
demonstration.

A suitable evaluation
contract SHOULD establish
a relationship between:

    EVALUATOR_REQUEST

    REQUESTED_SCENARIO

    OBSERVED_EXECUTION

    RETURNED_EVIDENCE

    EVALUATOR_OBSERVATION

The method used to establish
this relationship MUST
be documented within
the approved trust model.

A fresh evaluation reference
alone does not independently
establish fresh execution.

The corresponding execution
relationship requires
supporting observations.

No proprietary implementation
mechanism is specified here.

---

## 67. Independent Evaluation Record

An independent evaluation
SHOULD identify:

    EVALUATOR_REFERENCE

    EVALUATOR_INDEPENDENCE_SCOPE

    AUTHORIZED_EVALUATION_SCOPE

    IMPLEMENTATION_REFERENCE

    EVALUATOR_SELECTED_CONDITIONS

    EXECUTION_CONTROL_CLASS

    OBSERVATION_METHOD

    EVIDENCE_REFERENCES

    VERIFICATION_METHOD

    POSITIVE_FINDINGS

    NEGATIVE_FINDINGS

    INCONCLUSIVE_FINDINGS

    OVERALL_CONCLUSION

    LIMITATIONS

Independence MUST be
described rather than
assumed.

An external observer
is not necessarily an
independent execution
controller.

An independent evaluator
does not automatically
constitute an accredited
certification authority.

---

## 68. Reproduction Boundary

Reproduction requires a
separately attributable
execution.

The reproduction record
SHOULD identify:

- Original evidence reference.
- Reproduction implementation reference.
- Reproduction environment.
- Applicable workload.
- Applicable contract.
- Reproduction observations.
- Relevant environment differences.
- Reproduction verdict.
- Evaluator control and trust boundaries.

Reverification of the
same artifact is not
execution reproduction.

Repeated publication of
the same result is not
additional empirical evidence.

---

## 69. Compound Provenance Qualification

A compound evaluation
MUST establish the
provenance relationships
required by its combined
claim.

Evidence from separate
executions MUST NOT
be represented as a
single compound execution
unless that relationship
is established.

The record SHOULD
identify:

- Relevant operating conditions.
- Actual overlap of conditions.
- Common execution reference.
- Applicable observation interval.
- Applicable correctness results.
- Combined qualification verdict.

Independent successful
results do not automatically
establish compound correctness.

---

## 70. Evidence Obligation Matrix

| Assurance property | Required evidence |
|---|---|
| Artifact consistency | Trusted expected digest and examined artifact |
| Publisher authenticity | Qualified authentication and trust reference |
| Implementation attribution | Approved implementation identity |
| Build attribution | Established implementation-to-build relationship |
| Execution authenticity | Attributable execution observations |
| Temporal integrity | Sufficient observable ordering relationships |
| Evidence completeness | Defined requirements and coverage verification |
| Sanitization integrity | Documented transformation and preserved semantics |
| Semantic correctness | Applicable contract and sufficient observations |
| Verifier effectiveness | Qualified positive and negative controls |
| Independent recalculation | Sufficient approved measurement data |
| Independent reproduction | Separately attributable independent execution |
| Publication traceability | Identifiable evidence publication history |

No individual evidence
property substitutes for
all other properties.

---

## 71. Publication Readiness Gate

Before promoting an
approved evidence bundle
into public assurance use,
the evidence owner SHOULD
establish:

    CLAIM_SCOPE_DEFINED

    CONTRACT_REFERENCE_ESTABLISHED

    IMPLEMENTATION_ATTRIBUTED

    EXECUTION_ATTRIBUTED

    OBSERVATION_SCOPE_DEFINED

    OUTCOME_ACCOUNTING_RECONCILED

    REQUIRED_ARTIFACTS_PRESENT

    ARTIFACT_INTEGRITY_VERIFIED

    REFERENCE_TRUST_DOCUMENTED

    VERIFICATION_SCOPE_DEFINED

    VERIFICATION_CONTROLS_QUALIFIED

    CONFIDENTIALITY_REVIEW_COMPLETED

    LIMITATIONS_DOCUMENTED

    EVIDENCE_LEVEL_ASSIGNED

These are publication
readiness requirements.

They are not completed
review results asserted
by this document.

A missing mandatory
requirement MUST limit
the applicable public
qualification.

---

## 72. Protected Core Disclosure Review

Evidence publication MUST
remain subject to an
appropriate confidentiality
review.

The review SHOULD consider
both direct and indirect
implementation disclosure.

Potentially sensitive
artifact categories include:

- Internal source references.
- Internal symbol names.
- Proprietary execution traces.
- Internal diagnostic structures.
- Private build metadata.
- Confidential profiling records.
- Internal operational identifiers.
- Sensitive infrastructure details.
- Proprietary timing characteristics.
- Internal security configuration.
- Confidential implementation relationships.

The absence of source
code does not independently
establish that an artifact
is safe for unrestricted
publication.

Evidence disclosure MUST
remain proportionate to
the verification objective.

---

## 73. Public Evidence Boundary

The following MAY be
published when approved:

- Public correctness contracts.
- Approved implementation references.
- Approved execution references.
- Aggregate measurements.
- Sanitized observation records.
- Public verification controls.
- Artifact integrity manifests.
- Approved provenance records.
- Verification conclusions.
- Independent evaluation findings.
- Explicit evidence limitations.

Publication does not
modify applicable intellectual
property rights, repository
licenses, or evaluation
agreements.

---

## 74. Confidential Implementation Boundary

The following remain
confidential:

- Protected source code.
- Proprietary algorithms.
- Internal runtime architecture.
- Internal data structures.
- Proprietary state representations.
- Internal authorization mechanisms.
- Internal continuity mechanisms.
- Confidential defensive logic.
- Private cryptographic material.
- Internal protocol formats.
- Proprietary wire-level details.
- Confidential infrastructure.
- Unapproved execution traces.
- Internal evidence collection mechanisms.

Public evidence requirements
describe what must be
demonstrated.

They do not require
unrestricted disclosure
of how the Protected Core
achieves its declared
behavior.

---

## 75. Falsification Conditions

A confirmed occurrence of
any applicable condition
below constitutes a relevant
evidence assurance violation:

1. Fabricated execution
   evidence presented as
   an authentic record.

2. Modified evidence presented
   as an unchanged original.

3. Incorrect implementation
   attribution.

4. Incorrect build attribution.

5. Incorrect execution
   attribution.

6. Confirmed artifact integrity
   mismatch.

7. Concealment of a required
   evidence artifact.

8. Concealment of a confirmed
   relevant engineering failure.

9. Synthetic evidence presented
   as captured runtime evidence.

10. Unsupported evidence
    level promotion.

11. Incorrect independence
    classification.

12. Invalid temporal ordering
    presented as established.

13. Unsupported completeness
    classification.

14. Material sanitization
    concealed from the
    verification record.

15. A verifier accepting
    a known noncompliant
    evidence fixture.

16. An unexecuted evaluation
    presented as successful.

17. Separate executions
    represented as a single
    compound execution.

18. A corrected report
    represented as an
    unchanged original.

19. A digest match presented
    as proof of semantic
    correctness without
    supporting evidence.

20. A material trust limitation
    omitted from a qualification
    conclusion.

Each finding MUST remain
attributable to its actual
affected assurance property.

An evidence defect does
not automatically establish
a runtime defect.

It invalidates or limits
reliance on the affected
evidence conclusion.

---

## 76. Counterexample Reporting

An evidence assurance
finding SHOULD identify:

    FINDING_REFERENCE

    AFFECTED_EVIDENCE_REFERENCE

    AFFECTED_CLAIM_REFERENCE

    EXPECTED_EVIDENCE_CONTRACT

    OBSERVED_EVIDENCE_CONDITION

    PROPOSED_VIOLATION

    SUPPORTING_ARTIFACTS

    VERIFICATION_METHOD

    VERIFICATION_RESULT

    REPRODUCTION_STATUS

    AFFECTED_QUALIFICATION_SCOPE

A valid finding MUST NOT
be dismissed merely because
the evaluator lacks access
to proprietary source code.

The engineering conclusion
MUST follow the evidence.

---

## 77. Remediation and Requalification

Where an evidence assurance
defect is confirmed,
the remediation record
SHOULD distinguish:

- Original evidence reference.
- Original defect.
- Affected claims.
- Corrected evidence reference.
- Corrected verification method,
  where applicable.
- Subsequent verification results.
- Requalification conclusion.
- Remaining limitations.

Remediation MUST NOT
retroactively erase
the original finding.

---

## 78. Prohibited Evidence Substitution

The following substitutions
are explicitly prohibited:

    CLAIM
        as
    EXECUTION EVIDENCE

    ARTIFACT DIGEST
        as
    EXECUTION AUTHENTICITY

    VALID SIGNATURE
        as
    ENGINEERING CORRECTNESS

    VALID MANIFEST
        as
    COMPLETE OBSERVATION COVERAGE

    SOURCE REVISION REFERENCE
        as
    EXECUTED BINARY IDENTITY

    FILE TIMESTAMP
        as
    VERIFIED EXECUTION TIME

    VERIFIER PASS
        as
    COMPLETE PROTOCOL SECURITY

    PROJECT-CONTROLLED VERIFICATION
        as
    INDEPENDENT AUDIT

    ARTIFACT REVERIFICATION
        as
    EXECUTION REPRODUCTION

    SYNTHETIC FIXTURE
        as
    CAPTURED RUNTIME EVIDENCE

    SANITIZED REPORT
        as
    UNMODIFIED ORIGINAL

    ABSENCE OF PUBLISHED FAILURES
        as
    ABSENCE OF ACTUAL FAILURES

    ADDITIONAL DOCUMENTATION
        as
    EMPIRICAL EVIDENCE PROMOTION

Each stronger conclusion
requires its own supporting
evidence.

---

## 79. Technical Reviewer Questions

### Can a closed-source system
### provide meaningful evidence?

Yes.

Observable behavior can be
evaluated through suitable
external interfaces and
qualified evidence artifacts.

Some implementation-level
claims may require additional
authorized evidence.

### Does SHA-256 prove that
### an execution occurred?

No.

It supports artifact consistency
relative to an appropriate
expected reference.

### Does a signed report prove
### that its engineering claims
### are correct?

No.

Authentication and semantic
correctness remain separate.

### Can an evaluator verify
### evidence without access
### to the Protected Core?

Yes, where the approved
evidence is sufficient for
the stated verification
objective.

### Can external observers
### establish operation ordering
### without internal runtime clocks?

Yes, for observable precedence
relationships that can be
established with sufficient
measurement resolution.

Unobservable or uncertain
relationships remain unresolved.

### Can an independent evaluator
### produce a negative conclusion?

Yes.

Negative findings are legitimate
engineering evidence.

### Can evidence be sanitized?

Yes, provided the transformation
preserves the relationships
required by the claimed
verification scope.

### Does this document establish
### that every historical VRP
### result is independently verified?

No.

Historical results retain
their applicable evidence
classifications.

### Can a claim reach E5
### through additional documents?

No.

Independent evaluation
requires actual independent
engineering activity.

---

## 80. External Engineering Challenge

The VRP assurance framework
does not require an evaluator
to accept an engineering
claim on the basis of
author reputation, document
volume, or architectural
terminology.

An evaluator SHOULD be
able to challenge:

- Claim applicability.
- Execution attribution.
- Observation coverage.
- Artifact integrity.
- Evidence authenticity.
- Verification correctness.
- Measurement interpretation.
- Qualification conclusions.
- Reproduction status.
- Independence classification.

Where sufficient approved
evidence is unavailable,
the affected conclusion
MUST remain limited.

Where a valid counterexample
is established, it MUST
be evaluated against the
applicable contract.

The objective is not
unquestioned acceptance.

The objective is technically
defensible qualification.

---

## 81. Assurance Limitations

This document does not
establish:

- Universal evidence authenticity.
- Complete observation coverage.
- Absolute tamper prevention.
- Universal verifier correctness.
- Complete implementation correctness.
- Complete runtime security.
- Independent third-party certification.
- Unrestricted evidence availability.
- Automatic qualification of
  historical engineering results.

Every evidence conclusion
remains bounded by its
actual artifacts, trust
model, verification method,
observation coverage, and
applicable contract.

---

## 82. Master Evidence Integration

The master claims-to-evidence
matrix MUST associate
applicable engineering claims
with:

- Evidence identifiers.
- Invariant references.
- Scenario references.
- Implementation references.
- Execution references.
- Artifact references.
- Provenance classifications.
- Integrity verification results.
- Authenticity verification results.
- Completeness verification results.
- Semantic verification results.
- Evidence sufficiency levels.
- Qualification verdicts.
- Reproduction records.
- Independent evaluation status.
- Known limitations.

No claim may receive
a qualification status
stronger than its
supporting evidence.

---

## 83. Related Assurance Documents

- [Executive Engineering Assurance](VRP_EXECUTIVE_ENGINEERING_ASSURANCE.md)
- [Formal Continuity Invariants](VRP_FORMAL_CONTINUITY_INVARIANTS.md)
- [Session Identity Preservation](VRP_SESSION_IDENTITY_PRESERVATION.md)
- [Transport Independence](VRP_TRANSPORT_INDEPENDENCE.md)
- [Adversarial Validation Evidence](VRP_ADVERSARIAL_VALIDATION_EVIDENCE.md)
- [Replay and Duplicate Containment](VRP_REPLAY_AND_DUPLICATE_CONTAINMENT.md)
- [Authority and State Integrity](VRP_AUTHORITY_AND_STATE_INTEGRITY.md)
- [Recovery and Failure Semantics](VRP_RECOVERY_AND_FAILURE_SEMANTICS.md)
- [Concurrency and Linearizability](VRP_CONCURRENCY_AND_LINEARIZABILITY.md)
- [Autonomous Defense Boundaries](VRP_AUTONOMOUS_DEFENSE_BOUNDARIES.md)
- [Runtime Performance Evidence](VRP_RUNTIME_PERFORMANCE_EVIDENCE.md)

---

## 84. Final Engineering Declaration

    SESSION ≠ TRANSPORT

    CLAIM ≠ EVIDENCE

    Evidence must have an origin.

    Execution must have attribution.

    Observations must have scope.

    Artifacts must have integrity.

    References must have trust.

    Verification must have controls.

    Conclusions must have limitations.

    Reproduction must have
    separately attributable execution.

    Independence must be established,
    not assumed.

    Authentic evidence may reveal
    incorrect behavior.

    Negative findings must remain
    part of the engineering record.

    Confidentiality must not become
    immunity from technical scrutiny.

    Public assurance must remain
    proportional to actual evidence.

    The claims are falsifiable.

    The evidence contract is public.

    The Protected Core remains
    confidential.

---

**Veil Routing Protocol — VRP**

**Jumping VPN**

**Architect and Creator: Vitalijus Riabovas**

**25 evidence provenance qualification scenarios.**

**20 explicit evidence assurance falsification conditions.**

**7 illustrative verification records.**

**Implementation-to-execution attribution.**

**Artifact integrity and reference trust.**

**Independent evidence examination.**

**Explicit E0–E5 promotion requirements.**

**Evidence preservation and correction history.**

**Verifiable claims. Attributable execution.**

**Observable correctness. Protected implementation.**

**End of document — VRP-PA-012**
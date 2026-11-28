
# Veil Routing Protocol (VRP)

## Continuous Qualification and Public Validation Kit Update Policy

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-COMP-010  
**Revision:** 1.0  
**Classification:** PUBLIC  
**Date:** 2026-11-28  
**Status:** Continuous engineering qualification and maintenance policy

---

## 1. Executive Position

The VRP Validation Kit is intended to evolve continuously alongside the Veil Routing Protocol engineering program.

It is not intended to remain a static demonstration repository.

As new implementation properties are evaluated, eligible public validation capabilities should be extended to support independent reproduction, technical challenge, evidence verification, and comparative evaluation.

The governing architectural principle remains:

```text
SESSION != TRANSPORT
```

The governing maintenance principle is:

```text
ENGINEERING PROGRESS
        +
ATTRIBUTABLE EVIDENCE
        +
INDEPENDENT VALIDATION
        +
CONTROLLED PUBLICATION
```

The objective is to increase independently verifiable engineering assurance without increasing exposure of the VRP Protected Core.

---

## 2. Continuous Qualification Commitment

The VRP engineering program should maintain a direct relationship between:

- Private implementation development.
- Native implementation qualification.
- Security and adversarial validation.
- Runtime verification.
- Independent observation.
- Evidence preservation.
- Public specification updates.
- Public Validation Kit development.

A successful private experiment should be evaluated for its potential contribution to the public evidence and validation ecosystem.

This does not mean that every private experiment or implementation-specific test will be published.

Publication eligibility depends on confidentiality, correctness, reproducibility, and disclosure review.

---

## 3. Separation of Engineering Environments

The VRP engineering ecosystem distinguishes three principal environments.

### 3.1 Protected Engineering Environment

Responsible for:

- Native implementation development.
- Proprietary protocol engineering.
- Internal regression testing.
- Native runtime qualification.
- Confidential security research.
- Adversarial validation.
- Private evidence preservation.

The Protected Core remains within its authorized engineering boundary.

### 3.2 Public Specification

Responsible for:

- Public architectural contracts.
- Declared invariants.
- Threat-model declarations.
- Qualification requirements.
- Approved aggregate measurements.
- Claims and limitations.
- Approved evidence commitments.
- Technical documentation.

The specification describes what the system is intended to guarantee and what has been established through attributable evidence.

### 3.3 Public Validation Kit

Responsible for:

- Reproducible transport controls.
- Public reference models.
- Independent verification components.
- Positive and negative controls.
- Evidence schemas.
- Evidence integrity verification.
- Comparative workloads.
- Authorized evaluation contracts.

The Validation Kit must remain independent of confidential implementation mechanisms.

---

## 4. Engineering-to-Publication Lifecycle

The proposed lifecycle is:

```text
PRIVATE ENGINEERING
        |
NATIVE QUALIFICATION
        |
EVIDENCE PRESERVATION
        |
CLAIM ATTRIBUTION
        |
PUBLICATION ELIGIBILITY REVIEW
        |
PUBLIC REFERENCE COMPONENT
        |
INDEPENDENT PUBLIC QUALIFICATION
        |
DISCLOSURE REVIEW
        |
SPECIFICATION UPDATE
        |
VALIDATION KIT UPDATE
```

Every transition represents a separate engineering decision.

Successful native qualification does not automatically authorize public disclosure.

Successful publication does not automatically establish independent reproduction.

---

## 5. Update Triggers

The Validation Kit should be reviewed for eligible updates when any of the following occurs:

- A new continuity invariant is qualified.
- A new security property is qualified.
- A new transport workload is evaluated.
- A new observer capability becomes available.
- A new negative control is introduced.
- A previously unresolved engineering defect is corrected.
- A relevant regression is identified.
- An evidence format changes.
- A verification weakness is discovered.
- A comparative evaluation is extended.
- An external researcher provides a reproducible counterexample.

Not every internal change requires a public update.

The update decision should reflect the significance and public reproducibility of the new engineering capability.

---

## 6. Public Component Eligibility

A private qualification capability may produce a public Validation Kit addition when its externally observable behavior can be evaluated without disclosing proprietary implementation.

Eligible public components include:

- Conventional network controls.
- Independently constructed synthetic reference models.
- Application transaction workloads.
- Endpoint-change observation utilities.
- Identity-observer negative controls.
- Recovery measurement utilities.
- Evidence completeness checks.
- Cryptographic integrity verification.
- Comparative acceptance tests.
- Public measurement formats.
- Approved aggregate reference results.

Private implementation tests must not be copied automatically into public repositories.

Public equivalents must be constructed from the approved behavioral contract.

---

## 7. Protected Core Exclusion

The following must not be transferred into the public Validation Kit:

- Proprietary source code.
- Internal continuity algorithms.
- Internal authority-resolution mechanisms.
- Confidential state-machine implementation.
- Internal protocol-state representations.
- Private cryptographic construction details.
- Native replay-processing mechanisms.
- Internal method contracts.
- Private execution traces.
- Internal repository identifiers.
- Private source snapshots.
- Confidential binaries.
- Debug symbols.
- Infrastructure configuration.
- Keys, credentials, and tokens.
- Information enabling reconstruction of protected implementation mechanisms.

The confidentiality boundary applies to source code, generated artifacts, documentation, metadata, logs, manifests, and repository history.

A private artifact is not automatically suitable for publication merely because it has passed engineering qualification.

---

## 8. Reference Model Independence

Public reference models must be explicitly classified.

Every reference component should clearly state:

```text
PUBLIC REFERENCE MODEL

NOT THE NATIVE VRP IMPLEMENTATION

NO PROTECTED CORE INCLUDED

RESULTS LIMITED TO THE DECLARED WORKLOAD
```

A public reference model may demonstrate an engineering principle.

It must not be represented as proof that the native VRP implementation satisfies that principle.

Public reference components must remain independently understandable and reproducible.

---

## 9. Native Evaluation Independence

Authorized native evaluation should permit assessment of externally observable behavior without unrestricted implementation disclosure.

The evaluation contract should define:

- Authorized workload.
- Operational boundaries.
- Observation capabilities.
- Acceptance criteria.
- Evidence-generation requirements.
- Security limitations.
- Reproduction classification.

Native evaluation must remain distinct from public synthetic reference testing.

The existence of this maintenance policy does not establish that unrestricted native evaluation access is currently available.

---

## 10. Public Qualification Categories

The Validation Kit should maintain separate qualification categories.

| Category | Purpose |
|---|---|
| TRANSPORT_CONTROL | Evaluate conventional transport behavior |
| REFERENCE_MODEL | Evaluate synthetic application behavior |
| OBSERVER_CONTROL | Evaluate observation effectiveness |
| EVIDENCE_VERIFICATION | Evaluate artifact integrity and consistency |
| COMPARATIVE_CONTROL | Evaluate common experimental workloads |
| AUTHORIZED_NATIVE | Evaluate approved native implementation behavior |

Every generated result must identify its actual category.

A result from one category must not be silently promoted into another.

---

## 11. Qualification Status Model

Public components and experiments should use explicitly defined status values.

| Status | Meaning |
|---|---|
| PROPOSED | Capability has been specified |
| IMPLEMENTED | Public component has been constructed |
| EXECUTED | Component has been run |
| VERIFIED | Defined assertions have been checked |
| QUALIFIED | Applicable acceptance requirements have been satisfied |
| NOT_QUALIFIED | Qualification requirements remain unsatisfied |
| REGRESSION | Previously expected behavior was violated |
| SUPERSEDED | A newer attributable revision replaces an earlier record |
| WITHDRAWN | Previously published capability or claim is no longer supported |

Implementation status must remain distinct from execution status.

Execution status must remain distinct from successful qualification.

A successful public component must not automatically imply native VRP qualification.

---

## 12. Public Component Acceptance Requirements

A new executable public component should establish:

- Clearly defined purpose.
- Explicit evaluation classification.
- Documented dependencies.
- Reproducible execution procedure.
- Defined expected observations.
- Bounded execution behavior.
- Relevant timeout conditions.
- Measurement definitions.
- Positive controls.
- Negative controls.
- Failure reporting.
- Evidence-generation behavior.
- Known limitations.

Where applicable, the component should return a nonzero process exit status when mandatory verification fails.

Successful exit status must remain attributable to the declared assertions.

---

## 13. Positive Control Policy

Every applicable public verification component must demonstrate acceptance of valid reference behavior.

Positive controls should establish that the verifier can recognize:

- Valid communication.
- Valid transaction progression.
- Valid reference lifetime preservation.
- Valid evidence artifacts.
- Valid qualification records.

A verifier that rejects every input is not a qualified verifier.

Positive-control success must be recorded separately from native implementation qualification.

---

## 14. Negative Control Policy

Every applicable public verification component must demonstrate detection of invalid successful-looking results.

Relevant categories include:

- Replacement lifetime with a reused external identifier.
- Transport recovery without required application-state preservation.
- Missing physical-transition evidence.
- Invalid transaction progression.
- Duplicate accepted effects.
- Unauthorized accepted effects.
- Missing mandatory observations.
- Modified evidence artifacts.
- Contradictory qualification records.

A verifier that accepts these invalid cases must not be used to establish the affected guarantee.

Negative controls validate the evaluation methodology.

They do not automatically prove the corresponding native implementation property.

---

## 15. Evidence Generation Standard

New public experimental components should produce machine-readable evidence.

A suitable evidence package may include:

```text
EXPERIMENT_SPECIFICATION.md
MEASUREMENTS.csv
VERIFICATION_RESULTS.json
NEGATIVE_CONTROL_RESULTS.json
LIMITATIONS.md
PROVENANCE.json
SHA256SUMS
```

The mandatory artifact set must be defined by the applicable experiment.

A minimal reference workload may use a smaller artifact set.

Missing optional artifacts must not be represented as completed verification requirements.

Missing mandatory artifacts must prevent complete qualification.

---

## 16. Measurement Integrity

Every public measurement must retain its original meaning.

The following distinctions are mandatory:

```text
SCHEDULED_TRANSITION != OBSERVED_TRANSITION

OBSERVED_TRANSITION != VERIFIED_TRANSITION

PROCESS_EXIT_ZERO != PROTOCOL_CORRECTNESS

MEASURED_ZERO != NOT_MEASURED

REPEATED_EXECUTIONS != UNIQUE_TEST_CASES

REFERENCE_RESULT != NATIVE_RESULT
```

A public component must not generate unsupported successful measurements.

An unavailable observation must remain unavailable.

A proposed acceptance target must not be presented as an observed result.

---

## 17. Cryptographic Commitment Policy

Approved public evidence artifacts should use SHA-256 integrity commitments.

The commitment must be generated from the exact published artifact bytes.

Public commitments should identify:

- Evidence identifier.
- Artifact name.
- Digest algorithm.
- Actual computed digest.
- Artifact classification.
- Qualification scope.
- Availability classification.
- Verification procedure.

An externally supplied manifest must be evaluated against the applicable artifact-boundary and completeness requirements before verification.

A local manifest and matching artifacts provide local consistency evidence.

Independent commitment verification requires an appropriately established expected digest.

A cryptographic digest does not independently establish experimental authenticity or correctness.

---

## 18. Public Reference Comparison Suite

The comparison suite introduced in this qualification series is intended to provide reproducible local TCP and UDP controls and synthetic application-session observations.

Proposed component path:

```text
tools/continuity_comparison.py
```

The component evaluates three reference models:

- TCP connection-bound application state.
- UDP endpoint-bound application state.
- TCP-based transport-independent application state.

It also includes reference observer controls for:

- Valid continuation.
- Replacement lifetime with the same external label.
- Reset application sequence.
- Incorrect response association.

The component is independent of the VRP Protected Core.

Its actual repository availability and published revision must be verified before use.

---

## 19. Reference Comparison Execution

Once the comparison suite is available in the public repository, an evaluator may execute the proposed baseline workload using:

```bash
python3 tools/continuity_comparison.py \
    --rounds 30 \
    --interval 2 \
    --out evidence-continuity
```

A reduced-duration functional control may use:

```bash
python3 tools/continuity_comparison.py \
    --rounds 30 \
    --interval 0 \
    --out evidence-continuity-fast
```

Each output directory must be new.

Existing evidence directories should not be overwritten.

The zero-interval workload and two-second workload represent different timing conditions.

A successful result from the zero-interval workload must not be presented as qualification of the two-second workload.

---

## 20. Reference Comparison Expected Results

For the proposed 30-transition workload, the expected reference-model results are:

| Reference model | Expected application continuations |
|---|---:|
| TCP connection-bound | 0/30 |
| UDP endpoint-bound | 0/30 |
| TCP transport-independent | 30/30 |

The expected total workload includes:

```text
APPLICATION_COMMUNICATION_ROUNDS=93

SCHEDULED_ENDPOINT_TRANSITIONS=90

EXPECTED_OBSERVER_CONTROLS=4
```

These are expected workload values.

They are not automatically observed results.

Actual measurements must be obtained from execution.

A mismatch between expected and observed behavior must remain visible.

---

## 21. Reference Comparison Limitations

The initial public comparison component has a deliberately bounded scope.

Relevant limitations include:

- Local loopback communication.
- Same-process reference observation.
- Deliberate TCP connection termination.
- Retained UDP client sockets during the reference workload.
- Synthetic application lifetime representations.
- No native VRP identity oracle.
- No native QUIC execution.
- No native MPTCP execution.
- No NAT rebinding qualification.
- No integrated authority qualification.
- No production fault-injection workload.
- No authenticated external evidence provenance.

The component must not be used to claim that TCP, UDP, QUIC, or MPTCP systems cannot implement logical-session continuity.

Its purpose is to demonstrate and verify the distinction between connection-bound and independently maintained application state.

---

## 22. Reference Evidence Verification

For a locally generated and reviewed evidence package:

```bash
cd evidence-continuity
sha256sum -c SHA256SUMS
sha256sum SHA256SUMS
```

The evaluator should preserve the manifest digest separately when an external commitment is required.

The generated verification results should be inspected alongside the raw measurements.

A valid checksum does not justify accepting a contradictory or incomplete qualification result.

The initial reference suite does not replace a comprehensive independent semantic evidence verifier.

---

## 23. Comparative Expansion Roadmap

The public Validation Kit should progressively introduce eligible comparison capabilities.

| Capability | Maintenance objective |
|---|---|
| TCP connection replacement | Maintain reproducible control |
| UDP endpoint replacement | Maintain reproducible control |
| Synthetic session continuation | Maintain positive and negative controls |
| Native MPTCP capability | Introduce or qualify public native control |
| MPTCP subflow migration | Establish appropriate native workload |
| QUIC connection migration | Establish appropriate native workload |
| Lifetime replacement detection | Expand independent observer controls |
| Application transaction validation | Expand independent application observations |
| Evidence completeness verification | Introduce comprehensive semantic checks |
| Evidence tampering detection | Expand negative-control coverage |
| Authorized native VRP evaluation | Establish approved black-box integration |

Roadmap entries are maintenance objectives.

Their inclusion does not establish that the corresponding component has already been implemented or qualified.

---

## 24. Network Fault Expansion Roadmap

Future public workloads should evaluate eligible network conditions under controlled environments.

| Condition | Proposed workload |
|---|---|
| Endpoint churn | Replacement every two seconds |
| Packet loss | 30%, 50%, 80%, 90% |
| Blackout | 10, 30, and 60 seconds |
| Elevated RTT | 300–900 milliseconds |
| Jitter | Controlled variable conditions |
| Reordering | Controlled variable conditions |
| Duplication | Controlled repeated delivery |
| Compound faults | Multiple simultaneous conditions |

Fault workloads must remain within the evaluator's authorized environment.

The configured fault condition must remain distinguishable from the observed fault condition.

Native implementation qualification under these workloads requires the corresponding approved native evaluation capability.

---

## 25. Security Validation Expansion Roadmap

Eligible public security verification components may include:

- Reference replay-containment controls.
- Duplicate-operation detection controls.
- Invalid authorization reference cases.
- Stale-authorization reference cases.
- History-integrity negative controls.
- Concurrent operation reference workloads.
- Missing-observation rejection.
- Evidence-tampering detection.
- Contradictory-result rejection.

These components should verify the evaluation contract without implementing or reproducing confidential VRP defensive mechanisms.

Public synthetic security controls must remain explicitly classified.

---

## 26. Integrated Continuity Qualification Roadmap

The principal integrated qualification objective remains:

```text
ONE LOGICAL SESSION
        +
VERIFIED PHYSICAL TRANSPORT REPLACEMENT
        +
INDEPENDENT LIFETIME IDENTITY
        +
APPLICATION TRANSACTION CONTINUITY
        +
AUTHORITY INTEGRITY
        +
CANONICAL HISTORY PROTECTION
        +
COMPLETE VERIFIABLE EVIDENCE
```

All mandatory observations must belong to the same attributable execution.

Separate successful component experiments must not be combined into an unsupported integrated continuity verdict.

The current comparative campaign did not establish this complete relationship.

Future updates should explicitly identify evidence that resolves the remaining qualification requirements.

---

## 27. Comparative Fairness Maintenance

Every new comparative component must preserve the fairness requirements established by the public specification.

In particular:

- Supported QUIC migration must be recognized.
- Supported MPTCP subflow continuity must be recognized.
- Higher-layer application continuity must be permitted where applicable.
- Complete connection termination must remain distinct from path migration.
- Unavailable implementations must remain distinct from failed implementations.
- Unsupported scenarios must be explicitly classified.
- Workloads must be equivalent where technically possible.
- Environmental differences must be documented.

The public Validation Kit must not deliberately weaken competing systems to manufacture favorable conclusions.

A meaningful comparison evaluates observable guarantees under a common acceptance contract.

---

## 28. Regression Maintenance Policy

A previously qualified public component should be re-evaluated when relevant changes occur.

Examples include:

- Modification of the public workload.
- Modification of verification semantics.
- Changes to artifact-generation behavior.
- Changes to evidence schemas.
- Changes to supported runtime environments.
- Discovery of a false-positive acceptance condition.
- Discovery of a false-negative rejection condition.
- Introduction of new dependencies.
- Changes to public observation interfaces.

Regression results must identify the tested revision and applicable scope.

Historical successful results must not automatically qualify a modified component.

---

## 29. Qualification Defect Handling

A defect in a public Validation Kit component must be treated as an engineering finding.

The recommended workflow is:

```text
OBSERVE
    |
ATTRIBUTE
    |
REPRODUCE
    |
DEFINE EXPECTED BEHAVIOR
    |
APPLY MINIMAL CORRECTION
    |
VERIFY
    |
REGRESSION TEST
    |
PRESERVE EVIDENCE
    |
UPDATE DOCUMENTATION
```

A public verifier must not be weakened merely to accept an otherwise invalid evidence package.

Acceptance criteria must not be silently changed to convert a failed experiment into a successful result.

---

## 30. Evidence Schema Evolution

Evidence formats must evolve through explicitly documented revisions.

A schema change should identify:

- Previous schema revision.
- New schema revision.
- Added fields.
- Removed fields.
- Changed field semantics.
- Compatibility requirements.
- Verification requirements.
- Migration limitations.

Historical evidence should remain interpretable under its original schema.

A new schema must not silently reinterpret historical measurements.

Unsupported schema revisions must be explicitly classified.

---

## 31. Claim-to-Evidence Synchronization

Every significant public Validation Kit update should identify the relevant specification claims.

The public evidence ecosystem should maintain traceability between:

```text
ARCHITECTURAL CLAIM
        |
QUALIFICATION OBJECTIVE
        |
EXPERIMENT
        |
OBSERVATION
        |
VERIFICATION RESULT
        |
EVIDENCE ARTIFACT
        |
APPROVED COMMITMENT
        |
REPRODUCTION CLASS
```

The relationship must remain attributable.

A new public test must not automatically promote every related native implementation claim.

The affected claim register should be updated only when the corresponding evidence justifies the change.

---

## 32. Public Update Record Format

Future updates should include a concise attributable maintenance record.

The following JSON is an illustrative schema, not a completed update:

```json
{
  "schema_version": "1.0",
  "record_type": "validation_update_example",
  "update_id": "PUBLIC-UPDATE-ID",
  "component": "PUBLIC-COMPONENT-ID",
  "evaluation_mode": "REFERENCE_MODEL",
  "change_type": "NEW_VALIDATION_CAPABILITY",
  "implementation_status": "PROPOSED",
  "execution_status": "NOT_TESTED",
  "qualification_status": "NOT_QUALIFIED",
  "related_claims": [],
  "related_evidence": [],
  "measurements": null,
  "limitations": [],
  "disclosure_review": "PENDING",
  "publication_approved": false
}
```

The example intentionally contains no fabricated successful result.

Actual update records must reflect observed engineering outcomes.

---

## 33. Public Maintenance Checklist

Before releasing a new Validation Kit capability, review the following applicable conditions:

```text
PUBLIC_COMPONENT_SCOPE_DEFINED

EVALUATION_CATEGORY_DEFINED

ACCEPTANCE_CRITERIA_DEFINED

DEPENDENCIES_DOCUMENTED

WORKLOAD_REPRODUCIBLE

POSITIVE_CONTROLS_VERIFIED

NEGATIVE_CONTROLS_VERIFIED

OBSERVED_RESULTS_RECORDED

REGRESSION_RESULTS_RECORDED

EVIDENCE_FORMAT_VERIFIED

MEASUREMENT_SEMANTICS_REVIEWED

LIMITATIONS_RECORDED

PROTECTED_CORE_EXPOSURE_REVIEWED

SECRET_EXPOSURE_REVIEWED

DESTINATION_REPOSITORY_VERIFIED

PUBLICATION_APPROVED
```

The checklist describes required review conditions.

It is not a pre-completed qualification result.

Unresolved mandatory conditions must prevent release of the affected component.

---

## 34. Git and Repository Safety

Public updates must preserve repository and intellectual-property boundaries.

Before publication, review:

- Repository identity.
- Destination branch.
- Proposed changed files.
- Staged changes.
- Relevant repository history.
- Generated artifacts.
- Embedded implementation references.
- Confidential metadata.
- Private paths.
- Secrets and credentials.
- Unexpected binaries or archives.

Only explicitly approved public files should be included.

Private evidence directories must not be copied wholesale into a public repository.

A successful private build or test must not automatically trigger public publication.

Git history must not be rewritten merely to conceal an engineering failure.

If confidential material is discovered, publication must stop and the exposure must be evaluated through the applicable authorized response procedure.

---

## 35. External Researcher Contributions

Independent researchers may contribute through:

- Reproducible control experiments.
- Improved observation methods.
- Evidence-verifier improvements.
- Additional negative controls.
- Comparative workload extensions.
- Reproducible counterexamples.
- Documentation corrections.
- Portability improvements.
- Measurement consistency findings.

Contributions should identify the affected public component and qualification scope.

A contribution must not introduce proprietary VRP implementation material.

A successful external reproduction should be recorded with sufficient attribution to distinguish it from an original operator-reported result.

---

## 36. Independent Challenge Policy

A credible engineering claim must remain open to technical challenge.

A useful challenge should identify:

- Relevant public claim.
- Relevant experiment.
- Validation Kit revision.
- Expected behavior.
- Observed behavior.
- Reproduction procedure.
- Evidence integrity information.
- Environmental limitations.

A reproducible counterexample must be evaluated according to its engineering significance.

If an existing claim is invalidated, the corresponding claim status must be corrected.

Negative results must not be suppressed to preserve a favorable public presentation.

---

## 37. Historical Evidence Import

Earlier private engineering qualification campaigns may contain evidence suitable for future public disclosure.

Historical evidence should be imported only after establishing:

- Original qualification scope.
- Original acceptance criteria.
- Recorded observations.
- Relevant implementation provenance.
- Evidence integrity.
- Known limitations.
- Current applicability.
- Disclosure eligibility.
- Approved public evidence classification.

Historical results must not be silently reassigned to a newer implementation revision.

A successful historical experiment remains evidence for its original evaluated scope.

---

## 38. Current Qualification Series Summary

The engineering campaign associated with this documentation series recorded the following bounded results.

| Evidence category | Recorded result |
|---|---:|
| TCP communication rounds | 31/31 |
| UDP communication rounds | 31/31 |
| Synthetic independent application continuation | 30/30 |
| Native MPTCP control exchanges | 10 |
| Complete MPTCP replacement connections | 31 |
| MPTCP replacement payload exchanges | 62 |
| Native delivery fixture executions | 468 |
| Native canonical test executions | 588 |
| Separate UDP component executions | 208 |
| Native session lookups | 30/30 |
| Native failover flows | 30/30 |
| Observed native history records | 210 |
| Historical evidence manifests verified | 12 |

These results belong to distinct historical experiments.

They are not newly executed results of this maintenance policy.

They must not be aggregated into an unsupported unique-test count.

The original evidence scope and limitations remain applicable.

---

## 39. Current Qualification Limitations

The associated comparative campaign did not establish:

```text
INTEGRATED_NATIVE_LIFETIME_IDENTITY
    DURING REPEATED PHYSICAL_TRANSPORT_REPLACEMENT

MATCHED_NATIVE_CROSS_PROTOCOL_WORKLOAD

NATIVE_QUIC_COMPARATIVE_RESULT

NATIVE_MPTCP_SUBFLOW_MIGRATION_RESULT

INTEGRATED_LIVE_AUTHORITY_INTEGRITY

COMPLETE_EXTERNAL_NATIVE_REPRODUCTION

UNIVERSAL_COMPARATIVE_SUPERIORITY
```

Future Validation Kit updates should contribute toward resolving eligible observation and verification requirements.

These unresolved conditions must not be treated as successful results.

---

## 40. Documentation Series Index

The associated public engineering documentation series is:

| Identifier | Document |
|---|---|
| VRP-COMP-001 | Protocol Differentiation and Evidence Position |
| VRP-COMP-002 | Engineering Evidence Ledger |
| VRP-COMP-003 | Comparative Protocol Qualification Report |
| VRP-COMP-004 | Native Runtime Qualification Report |
| VRP-COMP-005 | Security and Authority Assurance |
| VRP-COMP-006 | Evidence Integrity Manifest |
| VRP-COMP-007 | Claims and Limitations Register |
| VRP-COMP-008 | Independent Black-Box Validation Contract |
| VRP-COMP-009 | Reproducible Continuity Comparison Suite |
| VRP-COMP-010 | Continuous Qualification and Update Policy |

VRP-COMP-009 identifies the executable public comparison component associated with this series.

Actual repository availability, file paths, and publication revisions must be verified against the corresponding public repositories.

---

## 41. Release and Publication Policy

Future public releases should identify:

- Newly introduced validation capabilities.
- Newly qualified public workloads.
- Corrected verification defects.
- Updated measurement contracts.
- Relevant regression results.
- New limitations.
- Superseded evidence.
- Approved cryptographic commitments.
- Affected specification claims.

A public release must not imply native implementation readiness unless the relevant native release qualification has independently established that conclusion.

Validation Kit releases and native protocol releases represent distinct qualification scopes.

---

## 42. Continuous Engineering Acceptance Principle

The public Validation Kit should become stronger as the VRP engineering program advances.

The objective is not to maximize the number of files, tests, or successful status markers.

The objective is to increase the strength of independently attributable evidence.

Each meaningful update should improve at least one of the following:

- Reproducibility.
- Observation independence.
- Verification correctness.
- Negative-control effectiveness.
- Measurement accuracy.
- Evidence completeness.
- Comparative fairness.
- Qualification coverage.
- Confidentiality protection.

An update that does not improve the evaluation capability should not be treated as meaningful engineering progress solely because it increases repository size.

---

## 43. Final Maintenance Position

The VRP specification defines the architectural contract.

The private engineering environment implements and qualifies the native system.

The public Validation Kit supports independently executable controls, observation requirements, verification methods, and evidence evaluation.

These responsibilities remain distinct.

They should evolve together without compromising the Protected Core boundary.

```text
SESSION != TRANSPORT

CONNECTIVITY != AUTHORITY

DELIVERY != LIFETIME IDENTITY

REFERENCE MODEL != NATIVE IMPLEMENTATION

HASH INTEGRITY != EXPERIMENTAL PROOF

PRIVATE QUALIFICATION != PUBLIC DISCLOSURE

ENGINEERING PROGRESS != MARKETING
```

Every new guarantee must remain measurable.

Every new claim must remain attributable.

Every relevant failure must remain visible.

Every public validation capability must remain independently challengeable.

Every protected implementation mechanism must remain confidential.

---

## 44. Revision History

| Revision | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial continuous qualification and public Validation Kit maintenance policy |

---

**Veil Routing Protocol**

**Author: Vitalijus Riabovas**

Continuity-first architecture.

Independent validation.

Evidence-driven engineering.

Protected intellectual property.

The specification evolves.

The implementation evolves.

The public validation capability evolves.

The qualification boundary remains explicit.

No hype.
Read the specifications.
Examine the evidence.
Challenge the engineering.

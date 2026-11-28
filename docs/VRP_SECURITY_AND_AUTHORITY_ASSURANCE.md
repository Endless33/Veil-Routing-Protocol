
# Veil Routing Protocol (VRP)

## Security and Authority Assurance

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-COMP-005  
**Revision:** 1.0  
**Classification:** PUBLIC  
**Evidence cutoff:** 2026-11-28  
**Status:** Security assurance contract and bounded qualification report

---

## 1. Executive Position

Veil Routing Protocol defines security as a property that must remain enforceable throughout the lifetime of a logical session.

A change in network connectivity must not automatically imply a change in logical authority.

A recovered transport must not automatically acquire authorization.

A successfully delivered packet must not automatically become an accepted canonical operation.

The governing architectural principle is:

```text
SESSION != TRANSPORT
```

The governing security principle is:

```text
CONNECTIVITY != AUTHORITY
```

VRP declares a continuity-first security contract in which session identity, authorized state evolution, recovery integrity, and canonical history protection remain explicit qualification responsibilities.

These responsibilities must be evaluated through observable behavior and attributable evidence.

No proprietary implementation mechanism is disclosed by this document.

---

## 2. Security Architecture Position

A communication system may successfully restore connectivity while failing to preserve the security properties of the original logical session.

Examples include:

- Communication restored under invalid authority.
- Application state restored into a replacement session.
- Previously accepted operations processed again.
- Unauthorized state transitions following recovery.
- Acceptance of stale authorization.
- Inconsistent application history after competing recovery operations.

These conditions must be distinguishable from legitimate recovery.

VRP therefore evaluates security independently from transport availability.

Successful connectivity is not an authorization decision.

Successful recovery is not sufficient proof of security integrity.

---

## 3. Declared Security Invariants

The public VRP security contract includes the following qualification objectives.

| Invariant | Required observable property |
|---|---|
| Session identity preservation | Original logical lifetime remains identifiable |
| Authority integrity | Unauthorized operations cannot become accepted state changes |
| Replay containment | Previously accepted operations cannot produce unauthorized repeated effects |
| Duplicate-commit rejection | A protected operation cannot be committed more than permitted |
| Stale-authority rejection | Invalidated authority cannot authorize new protected operations |
| Epoch rollback rejection | Obsolete authority generations cannot regain validity through rollback |
| Canonical history protection | Previously accepted history cannot be rewritten without violating verification |
| Recovery integrity | Recovery does not silently weaken declared security properties |
| Deterministic authority resolution | Competing operations resolve according to the declared acceptance contract |
| Fail-closed behavior | Unresolved mandatory security conditions prevent protected acceptance |
| Evidence integrity | Modified or incomplete evidence is detectable |

These are declared architectural invariants.

Their inclusion in this document is not a claim that every invariant has been exhaustively proven across every implementation revision and workload.

---

## 4. Threat Model

VRP security qualification considers adversarial and non-adversarial conditions that may affect logical-session integrity.

Relevant threat categories include:

- Unauthorized communication attempts.
- Malformed protocol input.
- Unexpected state transitions.
- Replayed operations.
- Duplicated operations.
- Delayed or reordered traffic.
- Stale authorization.
- Conflicting authority claims.
- Endpoint changes.
- Transport interruption.
- Network blackout.
- Recovery ambiguity.
- Concurrent state-changing operations.
- Resource exhaustion.
- Evidence tampering.
- Combined network and authorization faults.

These categories define the public threat-model scope.

Implementation-specific attack surfaces, internal defensive mechanisms, confidential state representations, and private vulnerability details are excluded.

The threat model does not imply that every listed condition has already completed integrated qualification.

---

## 5. Zero Trust Qualification Position

VRP adopts an explicit security qualification position:

Network location is not sufficient evidence of trust.

Transport availability is not sufficient evidence of trust.

Previous successful communication is not sufficient evidence of current authorization.

An externally visible identifier is not sufficient evidence of logical lifetime identity.

Recovery is not sufficient evidence of authority.

The public contract requires protected operations to remain subject to valid authorization throughout their qualified execution context.

A transport transition must not implicitly bypass the applicable security acceptance conditions.

The term Zero Trust describes an architectural security objective in this context.

It is not a certification claim.

It does not imply conformance with every external Zero Trust framework or regulatory standard.

---

## 6. Transport and Authority Separation

Transport identity and logical authority represent distinct architectural concerns.

The following observations must not be interpreted as interchangeable:

```text
TRANSPORT_AVAILABLE

ENDPOINT_REACHABLE

PACKET_AUTHENTICATED

SESSION_IDENTIFIED

OPERATION_AUTHORIZED

CANONICAL_OPERATION_ACCEPTED
```

A complete security qualification must establish the relationship between these properties under the declared workload.

In particular, transport recovery must not automatically establish authority recovery.

A successfully authenticated communication event must not automatically establish that every requested application operation is authorized.

These distinctions are central to the VRP assurance contract.

---

## 7. Replay Containment

### Declared Objective

Previously accepted operations must not produce unauthorized repeated effects when replayed within the qualified security scope.

### Required Observable Properties

Replay qualification should establish:

- Initial valid operation acceptance.
- Recorded initial canonical effect.
- Subsequent replay attempt.
- Replay containment outcome.
- Absence of unauthorized repeated canonical effects.
- Preservation of required session properties.

### Acceptance Boundary

A replay test must distinguish between:

- Packet receipt.
- Packet rejection.
- Operation rejection.
- Duplicate delivery.
- Duplicate application execution.
- Duplicate canonical commitment.

These outcomes are not equivalent.

Discarding a repeated network packet does not automatically establish complete application-level replay containment.

### Evidence Requirement

A qualified replay experiment must provide attributable measurements of attempted operations, accepted operations, rejected operations, and unauthorized repeated effects.

The internal replay-containment mechanism remains confidential.

---

## 8. Duplicate-Commit Rejection

### Declared Objective

An operation subject to protected commitment semantics must not produce additional unauthorized commitments when repeated.

Duplicate packets and duplicate canonical commitments represent different qualification concerns.

A system may observe repeated network delivery without accepting repeated canonical effects.

Conversely, an apparently successful network-level duplicate filter does not automatically prove protection against duplicate canonical commitments.

### Required Measurements

Where applicable, qualification should record:

| Measurement | Acceptance requirement |
|---|---|
| Original authorized operation | Accepted according to contract |
| Repeated operation attempts | Attributable |
| Unauthorized duplicate commitments | Zero |
| Canonical history inconsistency | Zero |
| Missing mandatory observations | Zero |

The acceptance requirement must reflect the declared semantics of the operation being tested.

No internal commitment algorithm is disclosed.

---

## 9. Stale-Authority Rejection

### Declared Objective

Authority that is no longer valid must not authorize new protected state changes.

The relevant security property is not merely that a request returns an error.

The relevant property is that invalid authority cannot produce an accepted protected effect.

### Required Observable Properties

A stale-authority qualification must establish:

- A previously valid authorization context.
- An attributable change in authorization validity.
- A subsequent attempt using invalidated authority.
- Rejection or containment according to the declared contract.
- Absence of unauthorized canonical mutation.
- Preservation of required valid-session behavior.

An error response without state verification is insufficient for complete qualification.

The confidential authority-resolution mechanism is outside public disclosure scope.

---

## 10. Epoch Rollback Rejection

### Declared Objective

An obsolete authorization generation must not regain validity merely because an earlier representation is presented or restored.

Rollback qualification should distinguish legitimate recovery from unauthorized restoration of obsolete authority.

### Required Acceptance Properties

- Current authorization validity remains enforceable.
- Obsolete authorization is not incorrectly accepted.
- Unauthorized canonical mutation does not occur.
- Required logical-session properties remain consistent.
- Evidence identifies the tested qualification scope.

This section declares externally testable behavior.

It does not disclose internal generation-management algorithms or protected state formats.

---

## 11. Competing Authority Conditions

Distributed communication environments may produce overlapping or competing operation requests during migration, recovery, or network disruption.

The declared VRP security objective requires competing requests to resolve according to the applicable authorization and consistency contract.

Qualification should examine:

- Concurrent protected operations.
- Competing recovery requests.
- Conflicting state-changing requests.
- Delayed authorization-related operations.
- Requests arriving across different transport contexts.

### Required Observable Outcome

The qualified system must not accept conflicting unauthorized canonical effects.

Deterministic resolution means that observed outcomes conform to the declared rules for the tested execution context.

It does not imply that every execution has identical timing or scheduling.

No implementation-specific resolution mechanism is disclosed.

---

## 12. Canonical History Protection

Canonical history represents an important security qualification concern.

A system may continue communicating while its accepted logical history becomes inconsistent.

The VRP assurance contract requires applicable canonical-history properties to remain protected across qualified transitions.

### Qualification Requirements

Where the declared contract requires historical preservation, an independent evaluation should detect:

- Unauthorized removal of accepted history.
- Unauthorized modification of accepted history.
- Unauthorized replacement of accepted operations.
- Additional unauthorized commitments.
- Inconsistency between observed accepted operations and resulting application state.

History-record availability alone is not sufficient.

A matching record count alone is not sufficient.

A matching externally visible identifier alone is not sufficient.

Complete qualification requires evidence appropriate to the semantic properties being asserted.

---

## 13. Recovery Integrity

Recovery must not silently convert an invalid security condition into an accepted operation.

The following conditions require distinct verification:

| Recovery category | Required observation |
|---|---|
| Network recovery | Reachability restored |
| Transport recovery | Communication restored |
| Application recovery | Required application behavior restored |
| Session recovery | Original logical lifetime independently confirmed |
| Authority recovery | Required authorization conditions confirmed |
| Canonical recovery | Required accepted-history properties confirmed |

A complete recovery claim must identify which of these properties were evaluated.

Successful transport recovery does not establish that the recovered communication context remains authorized.

A security qualification must therefore correlate recovery behavior with logical identity and protected state.

---

## 14. Fail-Closed Contract

Fail-closed behavior is a declared VRP security requirement.

A protected operation must not receive successful qualification when a mandatory security acceptance condition remains unresolved.

Relevant conditions include:

- Missing required authorization.
- Invalid authorization.
- Unsupported state transition.
- Invalid operation context.
- Inconsistent logical identity.
- Missing mandatory verification evidence.

The required response depends on the declared operational contract.

Possible externally observable outcomes include:

- Explicit rejection.
- Containment of the affected operation.
- Prevention of unauthorized state mutation.
- Restricted operation until required conditions are established.

Fail-closed does not necessarily mean unconditional termination of the entire communication system.

Security containment and availability must be evaluated separately.

---

## 15. Malformed and Unexpected Input

A complete security qualification program should include controlled malformed-input and unexpected-operation workloads.

Required observable properties include:

- Invalid input does not acquire authorization.
- Invalid input does not produce unauthorized canonical effects.
- Required valid-session properties remain within their declared bounds.
- Failure behavior remains attributable.
- Resource impact is measured where relevant.

A rejected malformed packet is useful evidence.

It is not sufficient by itself to establish complete resistance to malformed traffic.

The public qualification contract excludes confidential parser structures, internal message-processing algorithms, and implementation-specific defensive details.

---

## 16. Resource Exhaustion and Availability

Security and availability are related but distinct qualification dimensions.

A system can remain secure while becoming temporarily unavailable.

A system can remain available while violating an authorization invariant.

Neither outcome should be misclassified.

Resource-related qualification should measure, where applicable:

- Authorized operation completion.
- Unauthorized operation acceptance.
- Resource consumption.
- Recovery behavior.
- Observation completeness.
- Preservation of required canonical state.
- Behavior under declared resource limits.

No unrestricted denial-of-service resistance claim is made by this document.

Availability claims must specify the tested load, environment, duration, and acceptance conditions.

---

## 17. Concurrency and Security Integrity

Concurrent execution introduces security qualification concerns beyond ordinary successful operation processing.

Relevant concerns include:

- Competing state changes.
- Duplicate commitments.
- Concurrent authorization changes.
- Overlapping recovery operations.
- Simultaneous valid and invalid requests.
- Observation consistency during state evolution.

Selected native VRP test campaigns have completed recorded race-detector executions successfully.

The comparative qualification campaign recorded:

| Selected campaign | Successful race-detector executions |
|---|---:|
| Native delivery-related fixtures | 39 |
| Native canonical regression selection | 49 |
| Isolated UDP evaluation component | 40 |

These campaigns have distinct scopes.

Potential overlap between native test selections must not be ignored when reporting unique coverage.

The isolated UDP component is not the native VRP Protected Core.

Race-detector success does not independently establish security linearizability, atomicity, or universal concurrency correctness.

Those properties require dedicated acceptance tests.

---

## 18. Recorded Native Rejection Evidence

**Public evidence identifier:** VRP-SEC-001

The comparative engineering campaign recorded a rejected native operation involving a previously registered logical session.

The operation returned an error.

Subsequent registry observation established:

```text
NATIVE_OPERATION_REJECTED=OBSERVED

ORIGINAL_SESSION_LOOKUP_AFTER_REJECTION=SUCCESS

OBSERVED_SESSION_CARDINALITY=1
```

### Qualified Interpretation

The observed rejection did not remove the original registry entry.

This provides bounded evidence of post-rejection registry availability.

### Limitations

The experiment did not independently verify every security-relevant property before and after the rejection.

Consequently, the result does not establish:

- Complete rejection atomicity.
- Complete canonical-history preservation.
- Universal duplicate-commit rejection.
- Complete authority integrity.
- Absence of every unintended state mutation.

The exact private error representation is excluded from public disclosure.

---

## 19. Recorded Authorization-Related Rejection

**Public evidence identifier:** VRP-SEC-002

An experimental sequential migration fixture attempted additional protected operations following successful native initialization.

The first additional migration request was rejected.

The private diagnostic was classified into an authorization-related category through lexical analysis.

Recorded results:

```text
NATIVE_INITIALIZATION=PASS

ADDITIONAL_MIGRATION_REQUEST=REJECTED

COMPLETED_ADDITIONAL_MIGRATIONS=0

ERROR_CLASSIFICATION=PRELIMINARY

PROTECTED_CORE_MUTATION=NO
```

### Qualified Interpretation

The attempted fixture did not establish the authorization conditions required for successful additional migration.

An observable rejection occurred.

The implementation was preserved.

### Limitations

The lexical error classification does not independently establish the complete root cause.

The result must not be promoted into proof that every unauthorized operation is correctly rejected.

It also does not establish that the rejected operation indicates a protocol defect.

The experimental fixture remained unqualified.

---

## 20. Recorded State-Transition Rejection

**Public evidence identifier:** VRP-SEC-003

An experimental initialization fixture encountered a rejected state-changing operation.

The diagnostic was classified into a state-transition-related category.

The proposed modification to the experimental sequence was not executed when its attribution gate was not satisfied.

Recorded outcome:

```text
STATE_CHANGING_OPERATION=REJECTED

ALTERNATIVE_FIXTURE_EXPERIMENT=NOT_EXECUTED

PROTECTED_CORE_MUTATION=NO

QUALIFICATION=NOT_QUALIFIED
```

### Engineering Significance

An unsuccessful experimental fixture did not justify weakening the protected implementation.

The evidence was retained without converting the rejection into an artificial successful result.

### Limitation

This observation is not complete proof of the native state-transition security contract.

It establishes the recorded rejection and preservation of the engineering qualification boundary.

---

## 21. Native Security Regression Evidence

**Public evidence identifier:** VRP-SEC-004

The comparative engineering campaign included a selected native regression test campaign.

Recorded results:

| Execution category | Successful executions |
|---|---:|
| Initial selected execution | 49 |
| Repeated selected execution | 490 |
| Race-detector execution | 49 |
| Total successful executions | 588 |

Distinct selected tests:

```text
49
```

The selected campaign included tests associated with session identity, canonical behavior, migration, and recovery.

### Qualification Boundary

These results establish successful execution of the selected assertions.

They do not independently establish the semantics of every assertion associated with each declared security invariant.

No exhaustive replay, rollback, stale-authority, or canonical-history security claim is derived solely from the aggregate execution count.

Dedicated claim-specific evidence remains necessary.

---

## 22. Security Qualification Matrix

The following matrix describes the recorded comparative campaign rather than every historical VRP qualification activity.

| Security property | Current campaign classification |
|---|---|
| Native rejection behavior | OBSERVED |
| Registry availability following tested rejection | VERIFIED |
| Authorization-related rejection | OBSERVED — preliminary attribution |
| State-transition rejection | OBSERVED — preliminary attribution |
| Selected race-detector execution | QUALIFIED |
| Selected native regression execution | QUALIFIED |
| Complete rejection atomicity | NOT_PROVEN |
| Integrated replay containment during physical migration | NOT_ESTABLISHED |
| Integrated duplicate-commit containment | NOT_ESTABLISHED |
| Integrated stale-authority rejection | NOT_ESTABLISHED |
| Integrated epoch rollback rejection | NOT_ESTABLISHED |
| Canonical-history protection during physical migration | NOT_ESTABLISHED |
| Compound-fault security qualification | NOT_ESTABLISHED |
| Independent external security qualification | NOT_ESTABLISHED |

Separately recorded historical qualification results retain their original scope.

They must be incorporated through attributable evidence entries rather than assumed to apply automatically to the current campaign.

---

## 23. Security Assurance Evidence Levels

The following hierarchy defines a proposed public security qualification framework.

| Level | Required evidence |
|---|---|
| SEC-L1 | Declared security invariant |
| SEC-L2 | Successful execution of a relevant native assertion |
| SEC-L3 | Observed valid-operation and invalid-operation behavior |
| SEC-L4 | Independent confirmation of protected state before and after the operation |
| SEC-L5 | Qualification under repeated and concurrent execution |
| SEC-L6 | Correlated security qualification during actual transport replacement |
| SEC-L7 | Qualification under adversarial and compound faults |
| SEC-L8 | Independent external black-box reproduction |

These levels describe evidence strength within a defined scope.

They are not security certification levels.

They must not be converted into an unrestricted product-security percentage.

A higher-level claim requires evidence satisfying the relevant acceptance conditions.

---

## 24. Mandatory Security Negative Controls

An independent security verifier must be capable of rejecting intentionally invalid reference outcomes.

Required negative-control categories include:

| Negative control | Required verifier outcome |
|---|---|
| Unauthorized operation reported as accepted | Reject qualification |
| Replayed operation with repeated protected effect | Reject replay qualification |
| Duplicate canonical commitment | Reject duplicate-containment claim |
| Invalidated authority accepted | Reject authority qualification |
| Obsolete authority incorrectly restored | Reject rollback qualification |
| Unauthorized history modification | Reject history qualification |
| Replacement session with reused identifier | Reject continuity qualification |
| Missing post-operation state evidence | Reject complete state-integrity claim |
| Missing mandatory observation | Reject final qualification |
| Modified evidence artifact | Reject integrity verification |

Negative controls must establish that a verifier can detect false-positive success.

A verifier that merely accepts implementation-generated success statements is insufficient for complete security assurance.

---

## 25. Integrated Security Qualification Workload

A future integrated qualification should evaluate security while the underlying communication environment changes.

The proposed baseline workload includes:

- One logical-session lifetime.
- Thirty independently observed physical endpoint replacements.
- A scheduled replacement interval of two seconds.
- Authorized application transactions.
- Controlled invalid-operation attempts.
- Replay and duplicate-operation negative controls.
- Stale-authorization negative controls.
- Independent logical identity observation.
- Independent protected-state verification.

### Proposed Acceptance Conditions

| Measurement | Acceptance target |
|---|---:|
| Verified physical endpoint replacements | 30 |
| Independent lifetime confirmations | 30/30 |
| Required application transaction confirmations | 30/30 |
| Unauthorized accepted protected operations | 0 |
| Unauthorized duplicate commitments | 0 |
| Unauthorized canonical-history modifications | 0 |
| Missing mandatory observations | 0 |

These are qualification targets.

They are not recorded successful measurements.

The security and continuity observations must belong to the same attributable execution.

---

## 26. Compound-Fault Security Qualification

The public security qualification roadmap includes controlled combinations of transport disruption and invalid-operation workloads.

Proposed conditions include:

| Fault category | Proposed qualification scope |
|---|---|
| Endpoint churn | Replacement every two seconds |
| Packet loss | 30%, 50%, 80%, 90% |
| Blackout | 10, 30, and 60 seconds |
| Elevated latency | RTT between 300 and 900 milliseconds |
| Reordering | Controlled variable conditions |
| Duplication | Controlled repeated delivery |
| Replay | Authorized evaluation workload |
| Stale authority | Controlled negative authorization workload |
| Concurrent operations | Competing valid and invalid operations |
| Compound faults | Combined network disruption and security-negative controls |

Every workload must define both security and availability acceptance conditions.

A security PASS must not conceal an availability failure.

An availability PASS must not conceal a security violation.

The presence of a workload in this roadmap does not establish that it has completed qualification.

---

## 27. Security Measurements

A qualified security experiment should record, where applicable:

- Attempted authorized operations.
- Accepted authorized operations.
- Rejected authorized operations.
- Attempted unauthorized operations.
- Accepted unauthorized operations.
- Rejected unauthorized operations.
- Attempted replay operations.
- Detected replay operations.
- Unauthorized repeated effects.
- Duplicate canonical commitments.
- Canonical identity mismatches.
- Unauthorized history changes.
- Missing mandatory evidence records.
- Relevant recovery durations.

Measurements must distinguish an observed zero from an unavailable or unmeasured value.

For example:

```text
UNAUTHORIZED_ACCEPTANCE_COUNT=0
```

is valid only when unauthorized operations were actually attempted and their outcomes were observed.

It must not be substituted for:

```text
UNAUTHORIZED_ACCEPTANCE_COUNT=NOT_MEASURED
```

This distinction is mandatory for evidence integrity.

---

## 28. Proposed Public Security Result Schema

The following JSON record illustrates a future public security evidence format.

It is not an experimental result.

```json
{
  "schema_version": "1.0",
  "record_type": "schema_example",
  "qualification_type": "integrated_security_continuity",
  "execution_status": "NOT_EXECUTED",
  "observed": {
    "authorized_attempts": null,
    "authorized_acceptances": null,
    "unauthorized_attempts": null,
    "unauthorized_acceptances": null,
    "replay_attempts": null,
    "unauthorized_repeated_effects": null,
    "duplicate_canonical_commits": null,
    "canonical_identity_mismatches": null,
    "unauthorized_history_changes": null,
    "missing_mandatory_observations": null
  },
  "verification": {
    "authority_integrity": "NOT_TESTED",
    "replay_containment": "NOT_TESTED",
    "duplicate_commit_rejection": "NOT_TESTED",
    "stale_authority_rejection": "NOT_TESTED",
    "epoch_rollback_rejection": "NOT_TESTED",
    "canonical_history_integrity": "NOT_TESTED",
    "logical_session_continuity": "NOT_TESTED",
    "evidence_integrity": "NOT_TESTED"
  }
}
```

The use of null values prevents an unexecuted experiment from appearing to contain successful zero-violation measurements.

---

## 29. Security Evidence Package

Future completed security campaigns should produce an attributable evidence package containing approved versions of:

```text
SECURITY_EXPERIMENT_SPECIFICATION.md
MEASUREMENTS.csv
VERIFICATION_RESULTS.json
NEGATIVE_CONTROL_RESULTS.json
LIMITATIONS.md
SHA256SUMS
```

Additional approved observer summaries may be included.

The public evidence package must identify:

- Qualification scope.
- Acceptance conditions.
- Observed measurements.
- Negative-control outcomes.
- Unresolved properties.
- Reproduction classification.
- Approved cryptographic commitments.

Raw private traces and protected implementation artifacts are excluded unless separately approved following disclosure review.

---

## 30. Cryptographic Evidence Integrity

The recorded comparative qualification campaign concluded with verification of twelve historical evidence manifests.

Recorded consolidation outcomes included:

```text
EVIDENCE_ANCHORS_VERIFIED=12

CONSOLIDATION=PASS

EVIDENCE_INTEGRITY=PASS

ORIGINAL_SOURCE_PRESERVATION=PASS

PROTECTED_CORE_MUTATION=NO
```

These observations establish the recorded evidence-preservation result.

They do not independently establish the correctness of every security assertion contained in the underlying experiments.

Approved SHA-256 commitments may support later verification of disclosed artifacts.

However:

```text
HASH_INTEGRITY != SECURITY_CORRECTNESS

HASH_INTEGRITY != OPERATOR_AUTHENTICATION

HASH_INTEGRITY != INDEPENDENT_REPRODUCTION
```

Evidence integrity is one component of an assurance case.

It is not a replacement for experimental validation.

---

## 31. Independent Security Evaluation

Independent researchers should be able to evaluate approved security properties without receiving unrestricted access to the Protected Core.

The intended evaluation boundary includes:

- Declared security invariants.
- Controlled test workloads.
- Authorized black-box interaction.
- Observable acceptance and rejection behavior.
- Independent application-state observations.
- Approved aggregate measurements.
- Evidence verification.
- Explicit qualification limitations.

Access to an evaluation environment must not imply unrestricted authority over its infrastructure or implementation.

All adversarial evaluation must remain within its authorized scope.

The existence of a public evaluation contract does not automatically establish availability of a native remote evaluation service.

---

## 32. Public Validation Kit Integration

The public Validation Kit should evolve to include eligible independent security-verification components.

Suitable public additions include:

- Synthetic replay-containment reference cases.
- Duplicate-operation negative controls.
- Reference authorization acceptance models.
- Stale-authorization rejection scenarios.
- Canonical-history tampering detection controls.
- Evidence-schema verification.
- Missing-observation rejection tests.
- Evidence integrity verification.
- Approved aggregate security reference results.

These public components must be explicitly classified.

A reference authorization model is not the native VRP authority mechanism.

A synthetic replay-control implementation is not the native VRP replay-containment implementation.

A public evidence verifier is not proof that the native implementation generated correct evidence unless that provenance has been independently established.

Public validation must remain reproducible without disclosing proprietary implementation mechanisms.

---

## 33. Security Findings and Remediation Policy

Security findings should be processed through an attributable engineering workflow.

```text
OBSERVE
    |
ATTRIBUTE
    |
REPRODUCE
    |
ESTABLISH EXPECTED BEHAVIOR
    |
APPLY MINIMAL AUTHORIZED CORRECTION
    |
VERIFY
    |
REGRESSION QUALIFY
    |
PRESERVE EVIDENCE
    |
REVIEW DISCLOSURE
```

A failed test must not automatically be classified as an implementation vulnerability.

Likewise, an unexpected successful operation must not be ignored merely because other tests passed.

Confirmed defects, unresolved findings, experimental fixture errors, and qualification limitations must remain distinct.

Public remediation records should disclose the affected invariant, externally observable impact, verification outcome, and remaining limitations.

Protected implementation details remain confidential.

---

## 34. Security Release Acceptance Gate

A security release qualification should require evidence appropriate to its declared release scope.

Mandatory assurance categories should include:

```text
THREAT_MODEL_DEFINED

AUTHORITY_INTEGRITY_QUALIFIED

REPLAY_CONTAINMENT_QUALIFIED

DUPLICATE_COMMIT_REJECTION_QUALIFIED

STALE_AUTHORITY_REJECTION_QUALIFIED

ROLLBACK_REJECTION_QUALIFIED

CANONICAL_HISTORY_INTEGRITY_QUALIFIED

FAIL_CLOSED_BEHAVIOR_QUALIFIED

CONCURRENCY_QUALIFIED

RECOVERY_SECURITY_QUALIFIED

RELEVANT_ADVERSARIAL_WORKLOADS_QUALIFIED

NEGATIVE_CONTROLS_QUALIFIED

EVIDENCE_INTEGRITY_VERIFIED

DISCLOSURE_REVIEW_COMPLETED
```

An unresolved mandatory gate must remain explicitly unresolved.

A successful component-level result must not be substituted for an unresolved release-level requirement.

No unrestricted security certification is implied by this framework.

---

## 35. Relationship to Established Secure Protocols

Existing communication protocols provide important security and transport guarantees.

VRP does not dispute those guarantees.

Its declared qualification scope emphasizes the combined evaluation of:

- Transport-independent logical-session lifetime.
- Application-state preservation.
- Authorized canonical state evolution.
- Replay containment.
- Recovery integrity.
- Independent correlated evidence.

A system built on another transport may implement equivalent higher-level guarantees.

Whether it does so must be established through an equivalent qualification contract.

The existence of encryption, packet authentication, connection migration, or replay protection at another architectural layer does not independently establish every property declared by VRP.

Conversely, the declaration of a VRP security invariant does not establish that VRP has implemented it more effectively than another system.

Comparative security claims require matched evidence.

---

## 36. Protected Core Disclosure Boundary

The following information is excluded from this public security assurance document:

- Proprietary source code.
- Confidential protocol algorithms.
- Internal authorization mechanisms.
- Internal continuity mechanisms.
- Protected state representations.
- Internal cryptographic construction details.
- Confidential replay-processing logic.
- Private vulnerability details enabling exploitation.
- Internal implementation contracts.
- Private execution traces.
- Internal repository identifiers.
- Confidential infrastructure configuration.
- Keys, tokens, credentials, and cryptographic secrets.
- Unapproved private evidence commitments.
- Information enabling reconstruction of the Protected Core.

The public security contract describes externally testable guarantees.

It does not provide an implementation reconstruction guide.

---

## 37. Current Security Assurance Verdict

The recorded comparative qualification campaign establishes selected native test success, selected race-detector success, observed rejection behavior, post-rejection registry availability, and preservation of the original engineering baseline.

It also identifies unresolved requirements for integrated live-network security and continuity qualification.

```text
SECURITY_INVARIANTS=DECLARED

SELECTED_NATIVE_TEST_EXECUTIONS=588

SELECTED_NATIVE_RACE_QUALIFICATION=PASS

NATIVE_REJECTION_BEHAVIOR=OBSERVED

POST_REJECTION_REGISTRY_AVAILABILITY=VERIFIED

AUTHORIZATION_RELATED_REJECTION=OBSERVED

STATE_TRANSITION_REJECTION=OBSERVED

COMPLETE_REJECTION_ATOMICITY=NOT_PROVEN

INTEGRATED_LIVE_AUTHORITY_INTEGRITY=NOT_PROVEN

INTEGRATED_LIVE_REPLAY_CONTAINMENT=NOT_PROVEN

INTEGRATED_CANONICAL_HISTORY_PROTECTION=NOT_PROVEN

COMPOUND_FAULT_SECURITY_QUALIFICATION=INCOMPLETE

INDEPENDENT_EXTERNAL_SECURITY_QUALIFICATION=NOT_ESTABLISHED

UNRESTRICTED_SECURITY_CERTIFICATION=NOT_CLAIMED
```

The verdict is bounded to the recorded comparative campaign.

Separately qualified security evidence must be attributed individually before extending this verdict.

The presence of unresolved qualification requirements is not a reason to weaken the architectural contract.

It is a reason to continue engineering qualification.

---

## 38. Related Public Documents

- VRP-COMP-001 — Protocol Differentiation and Evidence Position.
- VRP-COMP-002 — Engineering Evidence Ledger.
- VRP-COMP-003 — Comparative Protocol Qualification Report.
- VRP-COMP-004 — Native Runtime Qualification Report.

Future security qualification updates should reference the relevant evidence identifiers and preserve the original qualification boundaries.

---

## 39. Revision History

| Revision | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial security and authority assurance contract |

---

**Veil Routing Protocol**

**Author: Vitalijus Riabovas**

```text
SESSION != TRANSPORT

CONNECTIVITY != AUTHORITY

AUTHENTICATION != UNRESTRICTED AUTHORIZATION

REJECTION != COMPLETE ATOMICITY PROOF

RECOVERY != SECURITY INTEGRITY

DECLARED INVARIANT != QUALIFIED GUARANTEE

EVIDENCE != MARKETING
```

A transport can change.

Connectivity can disappear.

Recovery can occur.

Security must remain subject to the declared architectural contract.

Every guarantee must remain independently challengeable.

Every qualification result must remain attributable.

The Protected Core must remain confidential.

No hype.
Read the specifications.
Examine the evidence.
Challenge the engineering.


# Veil Routing Protocol (VRP)

## Independent Black-Box Validation Contract

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-COMP-008  
**Contract version:** 1.0  
**Classification:** PUBLIC  
**Date:** 2026-11-28  
**Status:** Independent evaluation specification

---

## 1. Purpose

The VRP Validation Kit establishes a public framework for evaluating continuity-first communication architectures through observable behavior.

Its primary objective is to enable independent engineering evaluation without requiring access to the proprietary VRP Protected Core.

The evaluation framework must distinguish successful communication from preservation of the original logical-session lifetime.

The governing principle is:

```text
SESSION != TRANSPORT
```

The governing validation requirement is:

```text
OBSERVABLE GUARANTEES
        +
INDEPENDENT VERIFICATION
        +
REPRODUCIBLE EVIDENCE
        +
EXPLICIT LIMITATIONS
```

A successful validation result must be attributable to the actual evaluated system and workload.

---

## 2. Validation Scope

The Validation Kit defines a common evaluation contract for:

- Conventional transport control experiments.
- Synthetic application-session reference models.
- Native transport capability assessment.
- Independent logical-lifetime observation.
- Application transaction verification.
- Authority-integrity qualification.
- Replay and duplicate-operation negative controls.
- Recovery measurement.
- Evidence generation.
- Cryptographic integrity verification.
- Authorized native VRP black-box evaluation.

The public contract does not require disclosure of proprietary implementation mechanisms.

The presence of an evaluation requirement in this document does not establish that its corresponding executable component has already been implemented.

---

## 3. Evaluation Modes

Every experiment must declare its evaluation mode.

### Mode A — Public Transport Control

The experiment evaluates conventional transport behavior using independently available implementations.

Examples:

- TCP connection replacement.
- UDP endpoint replacement.
- Native MPTCP capability.
- Supported QUIC connection migration.

Results are attributable to the evaluated transport implementation and workload.

They are not native VRP results.

### Mode B — Public Reference Model

The experiment evaluates a synthetic application-session or verification model.

Reference models may demonstrate:

- Connection-bound application state.
- Endpoint-bound application state.
- Transport-independent application state.
- Lifetime replacement detection.
- Invalid evidence rejection.

A reference model is not the native VRP implementation.

### Mode C — Public Evidence Verification

The evaluator inspects approved evidence artifacts and verifies their integrity and semantic consistency.

Evidence verification does not automatically establish independent execution of the original implementation.

### Mode D — Authorized Native Evaluation

The evaluator interacts with an approved native implementation through an authorized black-box environment.

The evaluation must remain within the declared operational and security scope.

Protected Core source access is not required.

Availability of a native evaluation environment must be established separately.

---

## 4. Evaluation Classification

Every result must identify its actual subject.

```text
TRANSPORT_CONTROL

REFERENCE_MODEL

PUBLIC_EVIDENCE_VERIFICATION

AUTHORIZED_NATIVE_IMPLEMENTATION
```

These categories must never be treated as interchangeable.

In particular:

```text
REFERENCE_MODEL_PASS
    != NATIVE_VRP_PASS

CHECKSUM_VERIFICATION_PASS
    != NATIVE_RUNTIME_PASS

TRANSPORT_RECOVERY_PASS
    != LOGICAL_LIFETIME_PASS
```

The Validation Kit must prevent accidental or intentional promotion of reference-model success into a native implementation claim.

---

## 5. Evaluator Independence

An independent evaluator must be able to assess the relevant result without relying exclusively on a success statement produced by the system under evaluation.

The evaluator should obtain evidence from appropriately separated observation sources.

Relevant observation categories include:

- Physical network behavior.
- Application transaction behavior.
- Logical lifetime identity.
- Protected operation outcomes.
- Accepted-history consistency.
- Evidence integrity.

Separate software components do not automatically establish independent observation.

The evaluator must establish that an observation is meaningfully independent of the claim it verifies.

An implementation-generated success marker alone is insufficient.

---

## 6. Evaluation Roles

The validation architecture distinguishes the following conceptual roles.

### System Under Test

The implementation whose observable guarantees are being evaluated.

### Workload Controller

The component responsible for executing the declared experimental workload.

### Transport Observer

The component responsible for observing relevant physical network and endpoint behavior.

### Application Observer

The component responsible for verifying required application transaction semantics.

### Lifetime Observer

The component responsible for distinguishing original-session preservation from replacement-session creation.

### Evidence Verifier

The component responsible for evaluating evidence integrity, completeness, and semantic consistency.

These roles describe validation responsibilities.

They do not disclose the internal architecture of the native VRP implementation.

---

## 7. Mandatory Observation Separation

The validation framework distinguishes:

| Observation category | What it may establish |
|---|---|
| Process execution | A process executed |
| Socket observation | Network socket activity occurred |
| Endpoint observation | Relevant endpoint values changed |
| Transport observation | A qualified transport transition occurred |
| Delivery observation | Application data reached the required receiver |
| Transaction observation | Required application semantics were preserved |
| Lifetime observation | The original logical-session lifetime remained identifiable |
| Authority observation | Protected operations satisfied authorization requirements |
| History observation | Required accepted-history properties remained intact |

No observation category may automatically substitute for another.

---

## 8. Logical Lifetime Identity Contract

A valid continuity experiment must establish that the same logical-session lifetime survives the qualified transition.

The evaluator must be capable of distinguishing:

1. Original logical-session survival.

2. Creation of a new logical session.

3. Reuse of an externally visible identifier.

4. Restoration of communication into a replacement session.

5. Restoration of communication without preservation of required application state.

6. Missing or invalid lifetime observation.

The public contract defines the required verification semantics.

The implementation-specific native lifetime mechanism remains confidential.

An evaluator that cannot detect replacement-session creation is not qualified to establish original-session continuity.

---

## 9. Invalid Identity Substitutions

The following observations must not independently establish logical-session lifetime continuity:

```text
PROCESS_IDENTIFIER_UNCHANGED

SOCKET_DESCRIPTOR_UNCHANGED

LOCAL_PORT_UNCHANGED

REMOTE_ENDPOINT_UNCHANGED

SESSION_LABEL_REUSED

CONNECTION_RECOVERED

PACKET_DELIVERY_RESUMED

APPLICATION_RESPONSE_RECEIVED

IMPLEMENTATION_REPORTED_SUCCESS
```

These observations may contribute to an evidence package.

They cannot replace an independently qualified lifetime-identity assertion.

---

## 10. Physical Transport Transition Contract

A scheduled endpoint replacement is not automatically an observed endpoint replacement.

A valid transport-transition experiment must identify:

- The initial communication context.
- The intended transition.
- The independently observed transition.
- The relevant post-transition communication context.
- The corresponding application observation.
- The corresponding lifetime observation.
- Relevant timing measurements.

The evaluator must distinguish between:

```text
TRANSITION_SCHEDULED

TRANSITION_ATTEMPTED

TRANSITION_OBSERVED

TRANSITION_VERIFIED
```

Only transitions satisfying the applicable verification requirements may contribute to a successful physical-transition qualification count.

---

## 11. Application Transaction Contract

Application delivery must be evaluated using an explicitly defined workload.

The workload should permit independent verification of:

- Transaction identity.
- Expected transaction progression.
- Delivery completion.
- Accepted application effects.
- Missing transactions.
- Duplicate accepted effects.
- Application-state preservation.

A successfully received message does not automatically establish successful transaction continuity.

The evaluator must determine whether the received operation belongs to the expected logical lifetime and satisfies the declared application contract.

Synthetic reference workloads must remain clearly distinguishable from native VRP execution.

---

## 12. Authority Integrity Contract

Authority integrity must be evaluated independently from communication availability.

A valid authority experiment should include:

- An attributable authorized operation.
- An attributable invalid or unauthorized operation.
- Observable operation outcomes.
- Verification of relevant protected effects.
- Verification of required post-operation state.

An error response is not sufficient proof that no unauthorized mutation occurred.

The required security property is the absence of unauthorized accepted protected effects within the evaluated scope.

The public Validation Kit does not implement or disclose the proprietary VRP authority mechanism.

---

## 13. Replay and Duplicate-Operation Contract

Replay qualification must distinguish between repeated communication events and repeated protected effects.

Relevant measurements include:

- Original authorized operations.
- Repeated operation attempts.
- Accepted repeated operations.
- Rejected repeated operations.
- Unauthorized repeated effects.
- Duplicate canonical commitments.

A complete replay-containment claim requires evidence appropriate to the protected effect being evaluated.

A network-level duplicate filter alone does not establish application-level duplicate-commit containment.

Public reference controls may model invalid outcomes to verify that the evidence verifier detects them.

Such controls must not be represented as the native VRP replay implementation.

---

## 14. Canonical History Contract

Where the evaluated system declares history-preservation guarantees, the verifier must evaluate the relevant semantic properties.

A valid experiment should detect, where applicable:

- Unauthorized removal of previously accepted operations.
- Unauthorized modification of accepted history.
- Unauthorized replacement of accepted operations.
- Additional unauthorized commitments.
- Inconsistency between accepted operations and resulting application state.

History availability is not equivalent to history integrity.

A matching history length is not sufficient proof of canonical-history preservation.

The public contract does not require disclosure of proprietary history representation or protection mechanisms.

---

## 15. Baseline Continuity Workload

The proposed baseline workload evaluates repeated transport replacement within one logical-session lifetime.

| Parameter | Acceptance target |
|---|---:|
| Logical-session lifetimes | 1 |
| Scheduled physical replacements | 30 |
| Scheduled replacement interval | 2 seconds |
| Verified physical replacements | 30 |
| Independent lifetime confirmations | 30 |
| Application transaction confirmations | 30 |
| Unauthorized accepted protected operations | 0 |
| Unauthorized duplicate commitments | 0 |
| Unauthorized history modifications | 0 |
| Missing mandatory observations | 0 |

These are proposed acceptance criteria.

They are not completed native VRP measurements.

A valid result must satisfy the applicable mandatory requirements within one attributable execution.

---

## 16. Workload Timing Contract

The evaluator must distinguish configured timing from observed timing.

For example, a requested endpoint replacement every two seconds does not establish that every physical replacement occurred exactly two seconds apart.

A qualified timing record should include:

- Scheduled transition time.
- Observed transition time.
- Observation timing source.
- Relevant application completion time.
- Relevant recovery completion time.
- Timing uncertainty where applicable.

Elapsed durations should use an appropriate monotonic timing source.

Wall-clock timestamps may provide contextual information but must not be treated as independently authenticated time unless the necessary provenance is established.

---

## 17. Extended Network Conditions

The proposed validation roadmap includes the following operating conditions.

| Condition | Proposed workload |
|---|---|
| Endpoint churn | Repeated replacement every two seconds |
| Packet loss | 30%, 50%, 80%, 90% |
| Blackout | 10, 30, and 60 seconds |
| Elevated RTT | 300–900 milliseconds |
| Jitter | Controlled variable delay |
| Reordering | Controlled out-of-order delivery |
| Duplication | Controlled repeated delivery |
| Recovery | Attributable interruption and restoration |
| Compound faults | Multiple simultaneous conditions |

Each experiment must identify whether a condition was configured, applied, independently observed, or fully verified.

The proposed workloads do not constitute newly completed qualification results.

---

## 18. Security-Negative Workloads

Authorized validation environments may include controlled security-negative workloads.

Relevant categories include:

- Invalid authorization.
- Stale authorization.
- Repeated protected operations.
- Duplicate-operation scenarios.
- Unexpected state transitions.
- Conflicting protected operations.
- Malformed reference inputs.
- Evidence tampering.

All native security evaluation must remain within its explicitly authorized scope.

The public Validation Kit must not expose confidential implementation-specific attack surfaces, internal state formats, authorization mechanisms, or protected cryptographic details.

---

## 19. Mandatory Positive Controls

A qualified validation framework must demonstrate that it can recognize valid behavior.

Required positive-control categories include:

| Control | Expected observation |
|---|---|
| Valid transport communication | Communication succeeds |
| Valid application transaction | Required application effect occurs |
| Valid reference lifetime preservation | Original reference lifetime remains identifiable |
| Valid evidence package | Integrity and schema verification succeed |
| Valid authorized operation | Required authorized behavior is observed |

Positive controls must establish that the verifier does not reject every result indiscriminately.

A verifier that rejects all evidence is not an effective validation system.

---

## 20. Mandatory Negative Controls

A qualified validation framework must reject deliberately invalid successful-looking outcomes.

| Negative control | Required classification |
|---|---|
| New lifetime using the same external identifier | Continuity rejection |
| Restored transport without required application state | Incomplete continuity |
| Successful delivery into a replacement lifetime | Continuity rejection |
| Scheduled transition without observed transition | Transport qualification rejection |
| Unauthorized accepted protected effect | Authority qualification rejection |
| Duplicate unauthorized commitment | Duplicate-containment rejection |
| Modified accepted history | History qualification rejection |
| Missing mandatory observation | Evidence completeness rejection |
| Modified measurement artifact | Integrity rejection |
| Contradictory successful verdict | Semantic rejection |

These controls validate the evaluation methodology.

Their successful execution does not automatically establish the corresponding native VRP property.

---

## 21. Observer Qualification Gate

Before accepting a complete continuity result, the evaluator must establish that the relevant observers and verifiers are suitable for the workload.

Required properties include:

```text
POSITIVE_CONTROL_ACCEPTED

NEGATIVE_CONTROL_REJECTED

LIFETIME_REPLACEMENT_DETECTABLE

IDENTIFIER_REUSE_DETECTABLE

TRANSPORT_TRANSITION_OBSERVABLE

APPLICATION_EFFECT_OBSERVABLE

MISSING_EVIDENCE_DETECTABLE

CONTRADICTORY_RESULT_DETECTABLE
```

An unresolved mandatory observer requirement must prevent complete qualification.

This gate is particularly important when evaluating transport-independent session identity.

---

## 22. Comparative Fairness Contract

A comparison must evaluate the actual capabilities of each participating implementation.

The evaluator must not:

- Disable supported migration capabilities solely to create a weaker baseline.
- Treat complete connection termination as equivalent to native path migration.
- Exclude supported application-level continuity mechanisms without declaring the restriction.
- Compare incompatible application responsibilities without documenting the difference.
- Treat unavailable implementations as failed implementations.
- Promote a synthetic reference-model result into a native implementation result.

Each compared system must be evaluated according to the agreed workload and acceptance contract.

Unsupported scenarios must be explicitly classified.

---

## 23. Conventional Transport Reference Scope

The Validation Kit recognizes the following transport capabilities.

### TCP

Reliable ordered communication within a transport connection.

Application-defined session preservation may exist above separate TCP connections.

### UDP

Datagram communication.

Application-level lifetime and recovery behavior depend on higher-layer architecture.

### QUIC

Secure multiplexed communication with supported connection migration under its protocol conditions.

Additional application-level guarantees may be implemented above QUIC.

### MPTCP

A transport connection capable of using multiple TCP subflows.

Subflow continuity must be distinguished from complete MPTCP connection replacement.

### VRP

A declared continuity-first contract emphasizing logical-session lifetime, transport-independent continuity, authority integrity, and canonical-history protection.

The comparative evaluation must establish actual guarantees rather than infer them solely from protocol classification.

---

## 24. Recorded Reference Evidence

The engineering campaign associated with VRP-COMP-001 through VRP-COMP-007 recorded the following bounded observations.

| Experiment | Recorded result |
|---|---:|
| TCP communication rounds | 31/31 |
| UDP communication rounds | 31/31 |
| TCP connection-bound reference continuation | 0/30 |
| UDP endpoint-bound reference continuation | 0/30 |
| Independent application reference continuation | 30/30 |
| Native MPTCP capability exchanges | 10 |
| Complete MPTCP replacement connections | 31 |
| MPTCP replacement payload exchanges | 62 |
| Observed MPTCP token changes after complete replacement | 30 |
| Native VRP selected canonical test executions | 588 |
| Native VRP independent failover flows | 30/30 |
| Native VRP observed history records | 210 |
| Historical evidence manifests verified | 12 |

These measurements originate from distinct historical experiments.

They are not newly executed Validation Kit results.

The public repository must not claim reproducibility of an experiment until its public implementation and execution instructions have been separately established.

---

## 25. Historical Qualification Limitations

The associated engineering campaign did not establish:

```text
MATCHED_NATIVE_CROSS_PROTOCOL_WORKLOAD

NATIVE_QUIC_COMPARATIVE_RESULT

NATIVE_MPTCP_SUBFLOW_MIGRATION_RESULT

INDEPENDENT_NATIVE_LIFETIME_IDENTITY
    DURING REPEATED PHYSICAL REPLACEMENT

INTEGRATED_LIVE_AUTHORITY_INTEGRITY

COMPLETE_EXTERNAL_NATIVE_REPRODUCTION

UNIVERSAL_COMPARATIVE_SUPERIORITY
```

These limitations must remain visible when interpreting the historical reference measurements.

They do not prevent independent reproduction of eligible public control experiments.

---

## 26. Result Status Model

Every validation result must use explicitly defined status values.

| Status | Meaning |
|---|---|
| PASS | Applicable declared acceptance requirements satisfied |
| FAIL | An evaluated acceptance requirement was violated |
| INCOMPLETE | Mandatory qualification requirements remain unresolved |
| NOT_TESTED | Relevant workload was not executed |
| NOT_PROVEN | Available evidence does not establish the claim |
| UNSUPPORTED | Capability outside the evaluated implementation contract |
| UNAVAILABLE | Required implementation or environment unavailable |
| INVALID_EVIDENCE | Evidence failed required verification |
| REFERENCE_ONLY | Result belongs to a synthetic reference model |

An unavailable implementation must not be reported as a failed competing implementation.

An invalid evidence package must not receive complete qualification.

---

## 27. Measurement Contract

Each measurement should identify:

- Experiment identifier.
- Measurement name.
- Unit.
- Observation source.
- Observation status.
- Observed value.
- Aggregation method.
- Known limitation.

The framework must distinguish:

```text
MEASURED_ZERO
```

from:

```text
NOT_MEASURED
```

For example, zero unauthorized accepted operations is meaningful only if the relevant unauthorized-operation workload was actually exercised and its protected effects were observed.

An empty workload cannot establish successful zero-violation qualification.

---

## 28. Proposed Measurement Schema

The following CSV header illustrates a public measurement contract.

```csv
experiment_id,round,scheduled_transition,observed_transition,lifetime_confirmed,application_confirmed,authority_status,observation_complete,duration_ns
```

The header is a proposed schema.

It is not a recorded experimental artifact.

A future implementation must document valid values, nullability, units, and field semantics.

The schema must not expose proprietary native state representations or confidential identity values.

---

## 29. Proposed Verification Result Schema

The following JSON record illustrates the expected structure of an integrated qualification result.

It is not an actual successful result.

```json
{
  "schema_version": "1.0",
  "record_type": "schema_example",
  "experiment_id": "PUBLIC-EXPERIMENT-ID",
  "evaluation_mode": "AUTHORIZED_NATIVE_IMPLEMENTATION",
  "execution_status": "NOT_TESTED",
  "observed": {
    "physical_transitions": null,
    "lifetime_confirmations": null,
    "application_confirmations": null,
    "unauthorized_attempts": null,
    "unauthorized_accepted_effects": null,
    "duplicate_accepted_effects": null,
    "history_integrity_violations": null,
    "missing_mandatory_observations": null
  },
  "verification": {
    "transport_transition": "NOT_TESTED",
    "logical_lifetime_identity": "NOT_TESTED",
    "application_transaction_state": "NOT_TESTED",
    "authority_integrity": "NOT_TESTED",
    "canonical_history_integrity": "NOT_TESTED",
    "negative_controls": "NOT_TESTED",
    "evidence_integrity": "NOT_TESTED"
  },
  "overall_status": "NOT_TESTED"
}
```

Null values represent unavailable measurements.

They must not be interpreted as measured zero violations.

---

## 30. Evidence Package Contract

An independently attributable evidence package should contain approved artifacts such as:

```text
EXPERIMENT_SPECIFICATION.md
MEASUREMENTS.csv
VERIFICATION_RESULTS.json
NEGATIVE_CONTROL_RESULTS.json
LIMITATIONS.md
PROVENANCE.json
SHA256SUMS
```

The actual mandatory artifact set must be defined by the applicable experiment profile.

Evidence packages must distinguish raw observations from derived measurements.

All public artifacts must remain within the approved disclosure boundary.

---

## 31. Cryptographic Evidence Verification

The default public artifact commitment algorithm is SHA-256.

For an approved and reviewed evidence package, ordinary artifact verification may use:

```bash
sha256sum -c SHA256SUMS
```

The manifest itself may be committed through:

```bash
sha256sum SHA256SUMS
```

The resulting digest must be compared with the independently obtained expected commitment when that verification level is required.

Before processing untrusted manifests, a dedicated verifier should validate artifact paths, mandatory entries, file types, digest representations, and package boundaries.

A checksum match establishes byte-level consistency.

It does not independently establish experimental authenticity or architectural correctness.

---

## 32. Evidence Completeness Contract

The verifier must reject a complete qualification claim if mandatory observations are absent.

A package containing individually valid checksums may still be incomplete.

The required evaluation categories include:

```text
MANIFEST_VALIDITY

ARTIFACT_INTEGRITY

MANDATORY_ARTIFACT_PRESENCE

MEASUREMENT_COMPLETENESS

SCHEMA_VALIDITY

SEMANTIC_CONSISTENCY

REQUIRED_PROVENANCE

QUALIFICATION_SCOPE
```

The integrity of a partial package must not be presented as complete experimental qualification.

---

## 33. Integrated Qualification Decision

A complete continuity verdict may be accepted only when all mandatory requirements of the applicable experiment profile are established.

The conceptual decision is:

```text
VERIFIED_PHYSICAL_TRANSITION
        AND
VERIFIED_ORIGINAL_LIFETIME
        AND
VERIFIED_APPLICATION_STATE
        AND
VERIFIED_REQUIRED_AUTHORITY
        AND
VERIFIED_REQUIRED_HISTORY
        AND
QUALIFIED_NEGATIVE_CONTROLS
        AND
COMPLETE_EVIDENCE
```

The conditions must refer to the same attributable execution.

This is a public acceptance contract.

It is not a description of the native VRP continuity or authority algorithm.

---

## 34. Recovery Measurement Contract

Recovery measurements must identify the property being restored.

| Recovery category | Completion boundary |
|---|---|
| Network reachability | Required communication path becomes reachable |
| Transport recovery | Required transport communication resumes |
| Application delivery | Required application delivery resumes |
| Logical lifetime recovery | Original logical lifetime is independently confirmed |
| Authority recovery | Required authorization conditions are confirmed |
| Integrated recovery | All mandatory recovery conditions are satisfied |

Different recovery categories may produce different measured durations.

An evaluator must not report transport recovery duration as complete logical-session recovery duration without the required corresponding observations.

---

## 35. Availability and Security Separation

A validation result must preserve the distinction between security and availability.

Possible outcomes include:

| Security | Availability | Interpretation |
|---|---|---|
| PASS | PASS | Both evaluated requirements satisfied |
| PASS | FAIL | Security maintained, availability requirement violated |
| FAIL | PASS | Communication available despite security violation |
| FAIL | FAIL | Both evaluated requirements violated |
| NOT_TESTED | PASS | Availability established, security unqualified |

A successful availability result must not conceal a security failure.

A successful security rejection must not conceal an availability failure.

---

## 36. Independent Researcher Procedure

An independent researcher should be able to evaluate an available workload using the following process.

1. Identify the experiment and evaluation mode.

2. Review its declared acceptance criteria.

3. Verify that required dependencies and supported capabilities are available.

4. Execute the applicable positive controls.

5. Execute the applicable negative controls.

6. Execute the declared workload.

7. Capture attributable observations.

8. Verify measurement completeness.

9. Verify artifact integrity.

10. Evaluate the semantic acceptance conditions.

11. Record the resulting qualification status.

12. Report known limitations and reproducibility conditions.

The procedure must remain within the authorized evaluation boundary.

---

## 37. Counterexample Submission Contract

Independent researchers are encouraged to submit reproducible technical counterexamples.

A useful report should identify:

- Public claim identifier.
- Experiment identifier.
- Validation Kit revision.
- Evaluated implementation category.
- Relevant environment classification.
- Declared acceptance condition.
- Reproduction procedure.
- Expected observation.
- Actual observation.
- Approved evidence artifacts.
- Relevant limitations.

A counterexample should target a specific engineering claim.

A successful counterexample must be incorporated into the affected qualification record after attribution and review.

Researchers must not include secrets, private implementation artifacts, or confidential infrastructure information in public reports.

---

## 38. Reference Model Disclosure

Every public reference model must contain an explicit classification.

Recommended declaration:

```text
THIS COMPONENT IS A PUBLIC REFERENCE MODEL.

IT IS NOT THE NATIVE VRP IMPLEMENTATION.

IT DOES NOT CONTAIN THE VRP PROTECTED CORE.

ITS RESULTS QUALIFY ONLY THE DECLARED
REFERENCE WORKLOAD AND ACCEPTANCE CONDITIONS.
```

Public reference models may demonstrate independent validation principles.

They must not reproduce confidential VRP implementation mechanisms.

---

## 39. Public Validation Kit Maintenance

The Validation Kit should evolve as the private engineering qualification program introduces new eligible test capabilities.

A new public validation component must independently establish:

```text
PUBLIC_SCOPE_DEFINED

REFERENCE_OR_NATIVE_CLASSIFICATION_DEFINED

WORKLOAD_REPRODUCIBLE

ACCEPTANCE_CRITERIA_DEFINED

POSITIVE_CONTROLS_QUALIFIED

NEGATIVE_CONTROLS_QUALIFIED

EVIDENCE_FORMAT_DEFINED

LIMITATIONS_RECORDED

CONFIDENTIALITY_REVIEW_COMPLETED
```

A successful private test does not automatically authorize copying its implementation into the public Validation Kit.

Public equivalents must remain independent of confidential implementation mechanisms.

---

## 40. Protected Core Boundary

The following are explicitly excluded from the public Validation Kit disclosure contract:

- Proprietary VRP source code.
- Internal continuity algorithms.
- Internal authority-resolution mechanisms.
- Confidential protocol-state representations.
- Internal replay-processing mechanisms.
- Private cryptographic implementation details.
- Internal native method contracts.
- Confidential runtime traces.
- Private repository identifiers.
- Private source snapshots.
- Confidential binaries and debug information.
- Infrastructure configuration.
- Credentials, tokens, and cryptographic secrets.
- Unapproved private evidence commitments.
- Information enabling reconstruction of the Protected Core.

Independent validation concerns externally observable guarantees.

It does not require unrestricted access to proprietary implementation.

---

## 41. Publication Acceptance Gate

Before releasing a new public validation component, the applicable acceptance conditions must be reviewed.

```text
DESTINATION_REPOSITORY_VERIFIED

PUBLIC_COMPONENT_SCOPE_VERIFIED

TEST_IMPLEMENTATION_REVIEWED

EXPECTED_RESULTS_DEFINED

ACTUAL_RESULTS_RECORDED

NEGATIVE_CONTROLS_VERIFIED

EVIDENCE_INTEGRITY_VERIFIED

REPRODUCTION_INSTRUCTIONS_VERIFIED

PROTECTED_CORE_EXPOSURE_REJECTED

SECRET_EXPOSURE_REJECTED

PUBLICATION_APPROVED
```

The checklist describes required future release conditions.

It is not a declaration that all conditions have already passed.

---

## 42. Relationship to the VRP Specification

This Validation Kit contract complements the following public specification documents:

| Document ID | Purpose |
|---|---|
| VRP-COMP-001 | Protocol differentiation |
| VRP-COMP-002 | Engineering evidence ledger |
| VRP-COMP-003 | Comparative qualification |
| VRP-COMP-004 | Native runtime qualification |
| VRP-COMP-005 | Security and authority assurance |
| VRP-COMP-006 | Evidence integrity and commitments |
| VRP-COMP-007 | Claims and limitations register |
| VRP-COMP-008 | Independent black-box validation contract |

The specification defines the architectural and qualification claims.

The Validation Kit defines how eligible claims and control workloads can be independently evaluated.

The Protected Core remains outside the public implementation boundary.

---

## 43. Final Validation Position

A credible continuity evaluation must be capable of distinguishing restored communication from preservation of the original logical session.

A credible security evaluation must be capable of distinguishing rejected requests from verified prevention of unauthorized protected effects.

A credible evidence verifier must be capable of distinguishing valid checksums from complete experimental proof.

A credible comparative evaluation must permit competing implementations to exercise their actual supported capabilities.

The objective of the VRP Validation Kit is to establish a framework in which these distinctions can be tested independently.

```text
SESSION != TRANSPORT

CONNECTIVITY != AUTHORITY

DELIVERY != LIFETIME IDENTITY

REJECTION != COMPLETE SECURITY PROOF

REFERENCE MODEL != NATIVE IMPLEMENTATION

HASH MATCH != EXPERIMENTAL CORRECTNESS

INDEPENDENT VALIDATION != SOURCE DISCLOSURE
```

No implementation receives a successful qualification merely because its architecture declares the desired property.

The evidence determines the outcome.

---

## 44. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial independent black-box validation contract |

---

**Veil Routing Protocol**

**Author: Vitalijus Riabovas**

Evaluate the behavior.

Challenge the guarantees.

Reproduce the controls.

Verify the evidence.

Preserve the Protected Core.

No hype.
Read the specifications.
Examine the evidence.
Challenge the engineering.

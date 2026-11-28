
# Veil Routing Protocol (VRP)

## Engineering Claims and Limitations Register

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-COMP-007  
**Revision:** 1.0  
**Classification:** PUBLIC  
**Evidence cutoff:** 2026-11-28  
**Status:** Living engineering claims register

---

## 1. Executive Position

Veil Routing Protocol defines a continuity-first architecture in which logical-session lifetime, transport connectivity, application delivery, and authority integrity are distinct engineering responsibilities.

The central architectural principle is:

```text
SESSION != TRANSPORT
```

VRP must be evaluated against its declared architectural contract and attributable implementation evidence.

Neither architectural terminology nor successful isolated experiments are sufficient to establish complete protocol qualification.

This register establishes the boundary between:

- Declared architectural properties.
- Observed implementation behavior.
- Qualified engineering assertions.
- Unresolved validation requirements.
- Unsupported comparative claims.
- Future qualification objectives.

The purpose of this document is to make the VRP engineering position precise, independently challengeable, and resistant to unsupported interpretation.

---

## 2. Governing Qualification Principles

The following distinctions apply throughout the VRP engineering program:

```text
ARCHITECTURAL_CONTRACT != IMPLEMENTATION_PROOF

TRANSPORT_RECOVERY != SESSION_CONTINUITY

APPLICATION_DELIVERY != LIFETIME_IDENTITY

AUTHENTICATION != OPERATION_AUTHORIZATION

REJECTION != COMPLETE_STATE_INTEGRITY

TEST_SUCCESS != EXHAUSTIVE_CORRECTNESS

HASH_INTEGRITY != EXPERIMENTAL_AUTHENTICITY
```

Each claim must be evaluated against its own acceptance conditions.

Evidence supporting one claim must not automatically be transferred to another claim.

---

## 3. Claim Status Definitions

| Status | Meaning |
|---|---|
| DECLARED | Property explicitly defined by the architectural contract |
| OBSERVED | Behavior recorded during an attributable execution |
| VERIFIED | A defined assertion was checked successfully |
| QUALIFIED | Applicable acceptance conditions were satisfied within the tested scope |
| PARTIALLY_QUALIFIED | Some required properties were established, but mandatory conditions remain unresolved |
| NOT_QUALIFIED | Applicable qualification requirements were not satisfied |
| NOT_TESTED | Relevant experimental workload was not executed |
| NOT_PROVEN | Available evidence does not establish the claim |
| UNSUPPORTED | A specific capability is explicitly outside the evaluated contract |
| SUPERSEDED | A newer attributable qualification record replaces an earlier conclusion |
| WITHDRAWN | A previously published claim is no longer supported |

A claim may have different statuses under different implementation revisions, environments, and workloads.

The status must therefore remain associated with its qualification scope.

---

## 4. Architectural Claims Register

### VRP-CLAIM-ARCH-001 — Session and Transport Separation

**Status:** DECLARED

VRP explicitly distinguishes logical-session lifetime from the lifetime of an underlying transport.

Transport replacement must not automatically be interpreted as logical-session replacement.

Qualification requires independent observation of the original logical-session lifetime across the relevant transition.

Supporting document:

VRP-COMP-001 — Protocol Differentiation and Evidence Position.

---

### VRP-CLAIM-ARCH-002 — Continuity-First Architecture

**Status:** DECLARED

VRP defines continuity as an explicit architectural responsibility.

The architecture is evaluated according to preservation of required logical-session properties rather than successful transport reconnection alone.

This declaration establishes the intended qualification boundary.

It does not independently establish implementation correctness under every operating condition.

---

### VRP-CLAIM-ARCH-003 — Authority Separation

**Status:** DECLARED

Network connectivity and logical authority are separate architectural concerns.

The presence of an operational communication path must not automatically establish authorization for protected operations.

Required qualification includes independently attributable valid-operation and invalid-operation observations.

Supporting document:

VRP-COMP-005 — Security and Authority Assurance.

---

### VRP-CLAIM-ARCH-004 — Canonical History Protection

**Status:** DECLARED

VRP defines preservation of applicable accepted-history properties as an architectural qualification objective.

History-record availability alone does not establish history integrity.

Qualification requires verification appropriate to the semantic properties being asserted.

---

### VRP-CLAIM-ARCH-005 — Recovery Integrity

**Status:** DECLARED

Recovery must remain subject to logical-session, application-state, and authorization requirements.

Restoration of communication must not automatically imply restoration of the original logical-session lifetime or its authority.

Recovery claims must identify the specific property that was restored and independently observed.

---

### VRP-CLAIM-ARCH-006 — Fail-Closed Security

**Status:** DECLARED

A protected operation must not receive successful acceptance when mandatory authorization or integrity requirements remain unresolved.

Fail-closed behavior must be evaluated against the actual protected effect of an attempted operation.

An error response alone is not sufficient evidence of complete state integrity.

---

### VRP-CLAIM-ARCH-007 — Protected Core Separation

**Status:** DECLARED PUBLIC DISCLOSURE POLICY

Independent evaluation should rely on approved externally observable behavior, qualification contracts, and evidence verification without requiring unrestricted disclosure of proprietary implementation.

Public evaluation components must not be represented as the native Protected Core.

This claim defines a disclosure boundary.

It does not establish that every existing public repository or artifact has completed a comprehensive confidentiality audit.

---

## 5. Native Implementation Claims Register

### VRP-CLAIM-IMP-001 — Native Runtime Execution

**Status:** OBSERVED

The selected native VRP runtime executed successfully within a controlled engineering environment.

Recorded measurements:

```text
RUNTIME_EXIT=0
APPROXIMATE_DURATION_SECONDS=3.016
```

Qualified scope:

Successful execution of the selected native artifact.

Not established:

- Complete live-session continuity.
- Independent application delivery.
- Production readiness.

Related evidence:

VRP-RT-001.

---

### VRP-CLAIM-IMP-002 — Actual Network Activity

**Status:** OBSERVED

A system-level observer recorded actual UDP socket activity during native runtime execution.

Recorded measurements:

```text
UDP_SOCKET_CREATIONS=3
DISTINCT_OBSERVED_LOCAL_UDP_PORT_VALUES=3
INCOMPLETE_OBSERVER_RECORDS=0
```

Qualified scope:

Actual UDP activity and endpoint-related observations.

Not established:

Correlation of every observed network event with one preserved canonical logical-session lifetime.

Related evidence:

VRP-RT-002.

---

### VRP-CLAIM-IMP-003 — Native Delivery Fixture Execution

**Status:** QUALIFIED WITHIN SELECTED TEST SCOPE

Recorded results:

| Measurement | Result |
|---|---:|
| Distinct selected native tests | 39 |
| Successful baseline executions | 39 |
| Successful repeated executions | 390 |
| Successful race-detector executions | 39 |
| Total successful executions | 468 |

Selected static analysis also completed successfully.

Not established:

Independent end-to-end live-network application delivery.

Related evidence:

VRP-RT-003.

---

### VRP-CLAIM-IMP-004 — Canonical Regression Execution

**Status:** QUALIFIED WITHIN SELECTED TEST SCOPE

Recorded results:

| Measurement | Result |
|---|---:|
| Distinct selected tests | 49 |
| Successful baseline executions | 49 |
| Successful repeated executions | 490 |
| Successful race-detector executions | 49 |
| Total successful executions | 588 |

These measurements establish successful execution of the selected test campaign.

They do not establish exhaustive coverage or universal protocol correctness.

Related evidence:

VRP-RT-006.

---

### VRP-CLAIM-IMP-005 — Native Session Registration

**Status:** QUALIFIED WITHIN TESTED FIXTURE

Recorded results:

```text
NATIVE_SESSION_REGISTRATION=PASS
REPEATED_SESSION_LOOKUPS=30/30
OBSERVED_SESSION_CARDINALITY=1
SELECTED_RACE_QUALIFICATION=PASS
```

Qualified scope:

Native session registration and repeated observation.

Not established:

Preservation of original logical lifetime under physical transport replacement.

Related evidence:

VRP-RT-008.

---

### VRP-CLAIM-IMP-006 — Native Failover Repeatability

**Status:** QUALIFIED WITHIN TESTED SCENARIO

Recorded results:

```text
INDEPENDENT_NATIVE_FAILOVER_FLOWS=30/30
HISTORY_RECORDS_PER_FLOW=7
TOTAL_HISTORY_RECORDS_OBSERVED=210
OBSERVED_UDP_SOCKET_CREATIONS=0
```

Qualified scope:

Repeatable native scenario execution and history availability.

Not established:

Thirty physical transport replacements within one logical-session lifetime.

Related evidence:

VRP-RT-009.

---

### VRP-CLAIM-IMP-007 — Experimental Integration Compatibility

**Status:** PARTIALLY_QUALIFIED

Recorded results:

```text
INTEGRATION_COMPILATION=PASS
SELECTED_STATIC_ANALYSIS=PASS
INTEGRATED_RUNTIME_DELIVERY=NOT_QUALIFIED
```

Compilation establishes compatibility within the evaluated integration contract.

It does not establish operational end-to-end execution.

Related evidence:

VRP-RT-005.

---

## 6. Continuity Claims Register

### VRP-CLAIM-CONT-001 — Transport-Independent Logical Lifetime

**Architectural status:** DECLARED

**Current comparative campaign status:** NOT_PROVEN

The intended property requires the original logical-session lifetime to remain independently identifiable across qualified physical transport replacement.

The current comparative campaign recorded native runtime execution, transport activity, and native session observations separately.

Their correlation within one qualifying execution was not established.

A dedicated integrated evaluation remains necessary.

---

### VRP-CLAIM-CONT-002 — Repeated Physical Endpoint Churn

**Current comparative campaign status:** NOT_QUALIFIED

Proposed acceptance workload:

```text
LOGICAL_SESSION_LIFETIMES=1
PHYSICAL_ENDPOINT_REPLACEMENTS=30
SCHEDULED_REPLACEMENT_INTERVAL_SECONDS=2
REQUIRED_LIFETIME_CONFIRMATIONS=30
```

The sequential migration fixture did not establish the required native execution preconditions.

Recorded completed additional migrations:

```text
COMPLETED_ADDITIONAL_MIGRATIONS=0
```

This result describes the attempted fixture.

It is not proof that the native implementation cannot support migration.

It is also not a successful migration qualification.

---

### VRP-CLAIM-CONT-003 — Identifier Reuse Detection

**Architectural status:** DECLARED QUALIFICATION REQUIREMENT

**Current comparative campaign status:** NOT_ESTABLISHED

A valid independent identity oracle must distinguish preservation of the original logical lifetime from creation of a replacement lifetime using the same externally visible identifier.

The following observations are insufficient when considered alone:

- Identical session labels.
- Repeated successful registry lookups.
- Unchanged process identity.
- Restored transport connectivity.
- Successful application responses without lifetime attribution.

Negative controls must establish that replacement-session acceptance is detectable.

---

### VRP-CLAIM-CONT-004 — Application Transaction Continuity

**Architectural status:** DECLARED

**Current native comparative campaign status:** NOT_PROVEN

A complete application continuity claim requires attributable preservation of required application transaction semantics across the evaluated transition.

Transport delivery alone does not establish transaction continuity.

The positive-control experiment demonstrated application-state continuation in a synthetic TCP-based reference model.

That result does not establish equivalent behavior in the native VRP runtime.

---

### VRP-CLAIM-CONT-005 — Blackout Recovery

**Architectural status:** DECLARED QUALIFICATION OBJECTIVE

**Current comparative campaign status:** NOT_TESTED

Relevant future workloads include controlled interruption periods of:

```text
10 seconds
30 seconds
60 seconds
```

These are proposed workload values.

They are not newly recorded VRP recovery measurements.

Previously qualified historical recovery evidence must be separately attributed before extending this claim.

---

### VRP-CLAIM-CONT-006 — Compound-Fault Continuity

**Architectural status:** DECLARED QUALIFICATION OBJECTIVE

**Current comparative campaign status:** NOT_PROVEN

Future integrated workloads should evaluate continuity under combinations of:

- Endpoint churn.
- Packet loss.
- Network interruption.
- Latency and jitter.
- Reordering.
- Duplication.
- Authorized replay-negative controls.
- Competing authorization conditions.

Separate successful experiments must not be combined into an unsupported compound-fault qualification claim.

---

## 7. Security Claims Register

The following entries distinguish declared security requirements from evidence obtained within the current comparative campaign.

| Public claim identifier | Security property | Architectural status | Integrated campaign status |
|---|---|---|---|
| VRP-CLAIM-SEC-001 | Replay containment | DECLARED | NOT_PROVEN |
| VRP-CLAIM-SEC-002 | Duplicate-commit rejection | DECLARED | NOT_PROVEN |
| VRP-CLAIM-SEC-003 | Stale-authority rejection | DECLARED | NOT_PROVEN |
| VRP-CLAIM-SEC-004 | Epoch rollback rejection | DECLARED | NOT_PROVEN |
| VRP-CLAIM-SEC-005 | Deterministic authority resolution | DECLARED | NOT_PROVEN |
| VRP-CLAIM-SEC-006 | Canonical history protection | DECLARED | NOT_PROVEN |
| VRP-CLAIM-SEC-007 | Recovery integrity | DECLARED | NOT_PROVEN |
| VRP-CLAIM-SEC-008 | Fail-closed operation | DECLARED | PARTIAL OBSERVATIONS |
| VRP-CLAIM-SEC-009 | Concurrency integrity | DECLARED | SELECTED RACE TESTS QUALIFIED |
| VRP-CLAIM-SEC-010 | Compound-fault security | DECLARED | NOT_PROVEN |

The integrated campaign status refers specifically to the comparative qualification series documented in VRP-COMP-001 through VRP-COMP-006.

It does not constitute a complete inventory of all historical VRP security experiments.

Separately qualified security evidence retains its original scope and must be imported through attributable evidence revisions.

---

## 8. Observed Security Rejection

### VRP-CLAIM-SEC-011 — Native Operation Rejection

**Status:** OBSERVED

A tested native operation returned an error.

Post-rejection observation established:

```text
ORIGINAL_SESSION_LOOKUP=SUCCESS
OBSERVED_SESSION_CARDINALITY=1
```

This establishes bounded registry availability following the tested rejection.

It does not independently establish complete rejection atomicity or preservation of every relevant security property.

---

### VRP-CLAIM-SEC-012 — Authorization-Related Rejection

**Status:** OBSERVED WITH PRELIMINARY ATTRIBUTION

A native migration request was rejected after successful initialization of an experimental fixture.

The private diagnostic received a preliminary authorization-related classification.

The root cause was not independently established.

This result must not be represented as universal authority-integrity qualification.

---

### VRP-CLAIM-SEC-013 — State-Transition Rejection

**Status:** OBSERVED WITH PRELIMINARY ATTRIBUTION

An experimental state-changing operation was rejected.

The associated qualification fixture did not establish the required operational preconditions.

No protected implementation change was made to force successful execution.

The observation remains attributable to its tested scope.

---

## 9. Concurrency Claims Register

### VRP-CLAIM-CONC-001 — Selected Race-Detector Qualification

**Status:** QUALIFIED WITHIN SELECTED TEST SCOPE

Recorded race-detector executions:

| Campaign | Successful executions |
|---|---:|
| Native delivery-related fixtures | 39 |
| Native canonical regression selection | 49 |
| Separate UDP evaluation component | 40 |

These are separate selected workloads.

Their successful execution does not establish universal absence of races.

---

### VRP-CLAIM-CONC-002 — Security Linearizability

**Current comparative campaign status:** NOT_PROVEN

Race-detector success does not independently establish linearizability of protected state changes.

A complete claim requires an attributable concurrent workload and verification of accepted operation histories against the declared consistency contract.

Historical linearizability evidence must retain its original provenance and qualification scope.

---

### VRP-CLAIM-CONC-003 — Concurrent Authority Integrity

**Architectural status:** DECLARED

**Current comparative campaign status:** NOT_PROVEN

Complete qualification requires evidence that concurrent valid and invalid operations cannot produce unauthorized accepted effects or conflicting canonical history.

The acceptance contract must distinguish observed scheduling behavior from semantic correctness.

---

## 10. Comparative Claims Register

### VRP-CLAIM-CMP-001 — TCP Connection Replacement

**Status:** VERIFIED WITHIN CONTROL EXPERIMENT

Recorded results:

```text
COMMUNICATION_ROUNDS=31
SEPARATE_TCP_CONNECTIONS=31
SCHEDULED_REPLACEMENTS=30
```

The experiment established communication across deliberately replaced TCP connections.

It did not establish the absence of application-level continuity.

---

### VRP-CLAIM-CMP-002 — UDP Endpoint Replacement

**Status:** VERIFIED WITHIN CONTROL EXPERIMENT

Recorded results:

```text
COMMUNICATION_ROUNDS=31
SCHEDULED_ENDPOINT_REPLACEMENTS=30
```

The experiment established datagram communication across the tested local endpoint changes.

Raw UDP does not itself define a complete application-session lifecycle.

Higher-layer protocols may provide such properties.

---

### VRP-CLAIM-CMP-003 — Application Continuity Positive Control

**Status:** VERIFIED WITHIN SYNTHETIC REFERENCE MODEL

Recorded results:

| Reference model | State continuation |
|---|---:|
| TCP connection-bound application model | 0/30 |
| UDP endpoint-bound application model | 0/30 |
| Transport-independent application model | 30/30 |

The first two models intentionally bound state to transport-related identity.

The third explicitly preserved application state independently.

The result demonstrates that application-level continuity can exist above conventional transports.

This positive control must remain part of the comparative evidence.

Removing it would weaken the methodological validity of the comparison.

---

### VRP-CLAIM-CMP-004 — Native MPTCP Capability

**Status:** VERIFIED WITHIN TESTED ENVIRONMENT

Recorded native payload exchanges:

```text
10
```

Native MPTCP communication was exercised without observed TCP fallback during the qualified experiment.

No claim against native MPTCP subflow continuity is made.

---

### VRP-CLAIM-CMP-005 — Complete MPTCP Replacement

**Status:** VERIFIED WITHIN COMPLETE CONNECTION REPLACEMENT WORKLOAD

Recorded results:

```text
NATIVE_MPTCP_CONNECTIONS=31
PAYLOAD_EXCHANGES=62
COMPLETE_CONNECTION_REPLACEMENTS=30
OBSERVED_TOKEN_CHANGES=30
```

The experiment evaluated complete connection termination and replacement.

It did not evaluate preservation of an existing MPTCP connection across subflow migration.

Transport tokens are not independent application-session lifetime identifiers.

---

### VRP-CLAIM-CMP-006 — QUIC Comparison

**Status:** NOT_TESTED

QUIC supports connection migration under its standardized protocol conditions.

No native QUIC comparative execution was completed in this campaign.

An unavailable comparison result must not be classified as competing-protocol failure.

No empirical VRP superiority claim over QUIC is established.

---

### VRP-CLAIM-CMP-007 — Equivalent Higher-Level Guarantees

**Status:** NOT EXCLUDED

Systems implemented above TCP, UDP, QUIC, MPTCP, or other transports may provide application-level continuity, authorization, history preservation, and recovery guarantees.

Whether a particular system satisfies the complete VRP qualification contract must be established through an equivalent evaluation.

VRP does not claim that equivalent guarantees are impossible to implement elsewhere.

---

### VRP-CLAIM-CMP-008 — Architectural Differentiation

**Status:** DECLARED

VRP explicitly defines logical-session lifetime, authority integrity, and canonical-history protection as continuity-related architectural responsibilities.

This distinguishes its declared qualification scope from a transport-only specification.

The distinction does not establish historical novelty, patentability, exclusive ownership of the general continuity concept, or empirical superiority.

Those are separate questions requiring separate evidence.

---

### VRP-CLAIM-CMP-009 — Universal Comparative Superiority

**Status:** NOT_PROVEN

The current campaign does not establish universal superiority over:

- TCP-based systems.
- UDP-based systems.
- QUIC-based systems.
- MPTCP-based systems.
- Existing VPN implementations.
- Other continuity-aware distributed architectures.

A valid comparative superiority claim requires matched operating conditions, equivalent application responsibilities, appropriate negative controls, and independently attributable acceptance evidence.

No universal superiority conclusion is authorized by the current campaign.

---

## 11. Evidence Integrity Claims Register

### VRP-CLAIM-EVID-001 — Historical Manifest Verification

**Status:** VERIFIED AS REPORTED BY THE ENGINEERING OPERATOR

The final comparative consolidation verified twelve historical evidence manifests.

Recorded result:

```text
EVIDENCE_ANCHORS_VERIFIED=12
CONSOLIDATION=PASS
EVIDENCE_INTEGRITY=PASS
```

The underlying artifacts remain within the restricted evidence environment.

The public register does not establish independent third-party inspection of those artifacts.

---

### VRP-CLAIM-EVID-002 — Original Engineering Baseline Preservation

**Status:** VERIFIED WITHIN RECORDED CONSOLIDATION

Recorded results:

```text
REPOSITORY_IDENTITY_PRESERVATION=PASS
ORIGINAL_SOURCE_PRESERVATION=PASS
PROTECTED_CORE_MUTATION=NO
```

These observations establish the reported preservation outcome within the evaluated campaign.

They do not independently establish repository-wide confidentiality or implementation correctness.

---

### VRP-CLAIM-EVID-003 — Public Cryptographic Commitments

**Status:** PENDING DISCLOSURE-CONTROLLED PUBLICATION

Private evidence commitments exist for the recorded engineering campaign.

Unapproved internal manifest digests are intentionally withheld.

An approved public commitment must refer to an explicitly identified artifact and its actual computed digest.

No placeholder or fabricated digest is acceptable.

---

### VRP-CLAIM-EVID-004 — Independent Public Artifact Verification

**Status:** NOT_ESTABLISHED FOR WITHHELD ARTIFACTS

A public statement describing a privately verified artifact does not provide external readers with direct access to that artifact.

Independent verification requires the approved artifact bytes and an appropriately established expected commitment.

A commitment alone is not independent experimental reproduction.

---

### VRP-CLAIM-EVID-005 — Independent Native Reproduction

**Status:** NOT_ESTABLISHED BY THIS CAMPAIGN

Complete independent native evaluation requires an authorized execution environment or another approved mechanism providing the necessary observation capabilities.

Public reference models and control experiments may be independently reproducible.

Their successful reproduction must not be represented as independent execution of the native Protected Core.

---

## 12. Public Validation Kit Claims

### VRP-CLAIM-VAL-001 — Reproducible Public Control Experiments

**Status:** QUALIFICATION REQUIREMENT

The public Validation Kit should provide reproducible implementations of eligible comparative control workloads.

These include:

- TCP connection replacement.
- UDP endpoint replacement.
- Synthetic application-state continuity.
- Positive and negative lifetime controls.
- Native transport capability assessment.
- Measurement generation.
- Evidence integrity verification.

The inclusion of a capability in this requirement register does not establish that the current public repository already contains a qualified implementation of that capability.

---

### VRP-CLAIM-VAL-002 — Native VRP Black-Box Evaluation

**Status:** DECLARED EVALUATION OBJECTIVE

Native evaluation should expose approved observable behavior without requiring disclosure of proprietary implementation.

The evaluation contract must identify:

- Authorized workload.
- Available observation categories.
- Acceptance criteria.
- Evidence-generation requirements.
- Security restrictions.
- Known limitations.

Availability of a specific evaluation service must be established separately.

---

### VRP-CLAIM-VAL-003 — Independent Verifier Effectiveness

**Status:** QUALIFICATION REQUIREMENT

A public verifier must distinguish:

- Valid evidence.
- Modified evidence.
- Incomplete evidence.
- Contradictory successful claims.
- Invalid lifetime observations.
- Missing mandatory measurements.
- Unqualified workload execution.

The verifier must demonstrate rejection of deliberately invalid reference cases.

Successful checksum verification alone is insufficient.

---

### VRP-CLAIM-VAL-004 — Validation Kit Synchronization

**Status:** DECLARED MAINTENANCE POLICY

The public Validation Kit should evolve as private engineering qualification introduces eligible reusable evaluation capabilities.

Each public addition must independently satisfy:

```text
REPRODUCIBILITY_REVIEW
CORRECTNESS_REVIEW
NEGATIVE_CONTROL_REVIEW
CONFIDENTIALITY_REVIEW
EVIDENCE_SCOPE_REVIEW
PUBLICATION_APPROVAL
```

Private implementation tests must not be automatically copied into public repositories.

Public equivalents must be independently constructed and reviewed.

---

## 13. Explicit Limitations Register

| Limitation identifier | Description | Qualification consequence |
|---|---|---|
| VRP-LIM-001 | Native runtime and canonical observations were not fully correlated | Integrated lifetime continuity remains unqualified |
| VRP-LIM-002 | Separate experimental workloads were not equivalent | No numerical superiority ratio |
| VRP-LIM-003 | Native QUIC comparison was unavailable | No empirical QUIC conclusion |
| VRP-LIM-004 | MPTCP subflow migration was not evaluated | No claim against MPTCP subflow continuity |
| VRP-LIM-005 | Synthetic reference models were not native VRP | No native implementation equivalence |
| VRP-LIM-006 | Repeated test executions may overlap in selected coverage | No unsupported unique-test totals |
| VRP-LIM-007 | Race-detector execution was limited to exercised paths | No universal race-freedom claim |
| VRP-LIM-008 | Rejected migration fixtures did not establish valid preconditions | No completed sequential migration claim |
| VRP-LIM-009 | Private evidence artifacts remain withheld | No immediate independent public artifact inspection |
| VRP-LIM-010 | Complete independent native reproduction remains unresolved | No third-party reproduction claim |
| VRP-LIM-011 | Compound-fault workload was not qualified within this campaign | No integrated compound-fault claim |
| VRP-LIM-012 | Production-scale conditions were not evaluated | No unrestricted production-readiness claim |

Limitations are not optional marketing disclaimers.

They define the permitted interpretation of the associated engineering evidence.

---

## 14. Prohibited Evidence Substitutions

The following substitutions are not permitted in VRP qualification reporting.

| Available observation | Unsupported substituted claim |
|---|---|
| Process exit status zero | Complete runtime correctness |
| Socket creation | Logical-session establishment |
| Distinct local ports | Verified same-session physical migration |
| Successful registry lookup | Independent lifetime preservation |
| Identical external identifier | Original lifetime identity proof |
| Successful packet exchange | Complete application transaction continuity |
| Rejected request | Complete authority integrity |
| Unchanged registry count | Complete state preservation |
| Available history records | Canonical history integrity |
| Race-detector success | Universal concurrency correctness |
| Valid SHA-256 manifest | Experimental authenticity |
| Synthetic reference-model success | Native VRP qualification |
| Unavailable competitor implementation | Competitor failure |
| Declared architectural invariant | Proven implementation guarantee |

These restrictions apply regardless of the intended publication audience.

---

## 15. Claim Promotion Requirements

A claim may be promoted from DECLARED or OBSERVED to QUALIFIED only when the applicable acceptance requirements are satisfied.

The proposed promotion process is:

```text
CLAIM_DEFINED
        |
QUALIFICATION_SCOPE_DEFINED
        |
ACCEPTANCE_CONDITIONS_DEFINED
        |
WORKLOAD_EXECUTED
        |
MANDATORY_OBSERVATIONS_CAPTURED
        |
NEGATIVE_CONTROLS_EVALUATED
        |
SEMANTIC_ASSERTIONS_VERIFIED
        |
EVIDENCE_INTEGRITY_VERIFIED
        |
LIMITATIONS_RECORDED
        |
CLAIM_STATUS_UPDATED
```

Publication requires a separate disclosure review.

The existence of a successful test result must not bypass claim-specific acceptance requirements.

---

## 16. Claim Regression and Invalidation

Previously qualified claims may require re-evaluation following relevant changes.

Examples include:

- Changes affecting session lifecycle behavior.
- Changes affecting authorization.
- Changes affecting recovery behavior.
- Changes affecting concurrency.
- Changes affecting transport integration.
- Changes affecting observation or verification.
- Changes affecting evidence generation.
- Newly discovered qualification defects.
- Previously untested operating conditions.

A regression failure must not be concealed by retaining an outdated successful claim without qualification.

The affected claim should be revised, suspended, superseded, or withdrawn according to the new evidence.

Historical evidence must remain traceable.

---

## 17. Integrated Continuity Promotion Gate

The claim of integrated transport-independent continuity requires correlated evidence from one attributable execution.

Proposed mandatory acceptance conditions:

| Requirement | Target |
|---|---:|
| Logical-session lifetimes | 1 |
| Verified physical transport replacements | 30 |
| Required independent lifetime confirmations | 30/30 |
| Required application transaction confirmations | 30/30 |
| Unauthorized accepted protected operations | 0 |
| Unauthorized duplicate commitments | 0 |
| Unauthorized canonical-history modifications | 0 |
| Missing mandatory observation records | 0 |

Zero-violation results require actual relevant workloads and attributable observations.

An unexecuted security-negative workload cannot establish a zero-violation qualification result.

The above values remain proposed acceptance criteria.

They are not completed measurements.

---

## 18. Comparative Claim Promotion Gate

A comparative superiority claim requires more than successful native VRP execution.

The evaluation must identify:

- Compared implementations.
- Relevant supported capabilities.
- Equivalent application responsibilities.
- Workload definitions.
- Fault conditions.
- Observation methodology.
- Acceptance criteria.
- Negative controls.
- Measurement units.
- Environmental differences.
- Known uncertainty.
- Reproduction classification.

Unsupported or unavailable comparison scenarios must remain separately classified.

A competing protocol must be allowed to exercise its supported recovery and migration capabilities.

Comparative conclusions must be restricted to the evaluated workloads.

---

## 19. Production Readiness Boundary

Production readiness is not represented by an arbitrary percentage.

A release qualification must define its intended operating scope and mandatory acceptance conditions.

Relevant categories include:

- Implementation correctness.
- Runtime correctness.
- Application delivery.
- Independent session continuity.
- Authority integrity.
- Replay containment.
- Canonical history protection.
- Concurrency integrity.
- Adversarial behavior.
- Resource limits.
- Operational recovery.
- Evidence integrity.
- Deployment suitability.
- Disclosure safety.

Successful isolated components do not automatically establish successful release qualification.

The current comparative campaign does not independently establish unrestricted production readiness.

---

## 20. Certification and Compliance Boundary

The terms continuity-first and Zero Trust describe architectural objectives and qualification responsibilities within the VRP project.

They must not be interpreted as claims of:

- Government certification.
- Regulatory approval.
- Independent security accreditation.
- Universal standards compliance.
- Formal verification of every implementation path.
- Immunity to exploitation.
- Guaranteed availability.
- Unlimited fault tolerance.

Any future certification or compliance claim must identify its issuing authority, applicable standard, evaluation scope, and supporting evidence.

No such unrestricted certification claim is made by this register.

---

## 21. Public Claim Record Format

Future machine-readable claim records should identify their scope explicitly.

Example:

```json
{
  "schema_version": "1.0",
  "record_type": "claim_schema_example",
  "claim_id": "PUBLIC-CLAIM-ID",
  "claim_scope": "integrated_live_continuity",
  "architectural_status": "DECLARED",
  "qualification_status": "NOT_PROVEN",
  "evidence_ids": [],
  "required_observations": [
    "physical_transport_replacement",
    "independent_lifetime_identity",
    "application_transaction_state",
    "authority_integrity"
  ],
  "limitations": [
    "integrated qualification not yet established"
  ],
  "independent_reproduction": "NOT_ESTABLISHED",
  "publication_status": "SCHEMA_EXAMPLE"
}
```

This record is an illustrative schema.

It is not an actual completed qualification result.

---

## 22. Historical Evidence Import Policy

Earlier VRP qualification results may provide evidence beyond the current comparative campaign.

Such results must not be discarded merely because the current campaign has a narrower scope.

However, importing historical evidence requires explicit attribution.

Each imported historical record must identify:

- Original qualification scope.
- Recorded workload.
- Original acceptance conditions.
- Available measurements.
- Original verification outcome.
- Relevant implementation provenance.
- Known limitations.
- Relationship to current claims.
- Approved public evidence commitment.
- Disclosure classification.

Historical results must not be silently promoted into current implementation guarantees.

Their applicability must be evaluated.

---

## 23. Disclosure and Intellectual Property Boundary

Public claims must describe externally testable behavior.

The following remain outside the scope of this public register:

- Protected Core implementation.
- Proprietary algorithms.
- Confidential protocol-state representation.
- Internal authorization mechanisms.
- Internal continuity mechanisms.
- Private cryptographic implementation details.
- Internal repository paths.
- Private repository identifiers.
- Raw private traces.
- Confidential build artifacts.
- Infrastructure configuration.
- Credentials and cryptographic secrets.
- Unapproved private evidence commitments.
- Details enabling reconstruction of protected implementation.

The public claim registry is an engineering contract.

It is not an implementation disclosure mechanism.

---

## 24. Independent Researcher Challenge Contract

A technical challenge should identify the specific claim being disputed.

An effective challenge should contain, where applicable:

- Public claim identifier.
- Relevant qualification document.
- Disputed acceptance condition.
- Proposed counterexample.
- Reproduction procedure.
- Expected observation.
- Actual observation.
- Evidence integrity information.
- Known environmental differences.
- Relevant limitations.

Challenges should be evaluated according to technical relevance and evidence quality.

A successful challenge must be reflected in the affected qualification record.

Criticism should not be dismissed merely because it contradicts a previously successful experiment.

Likewise, an unsupported assertion should not automatically invalidate attributable engineering evidence.

---

## 25. Public Documentation Consistency

The following documents form the current comparative qualification documentation series.

| Document ID | Purpose |
|---|---|
| VRP-COMP-001 | Protocol differentiation and evidence position |
| VRP-COMP-002 | Engineering evidence ledger |
| VRP-COMP-003 | Comparative protocol qualification |
| VRP-COMP-004 | Native runtime qualification |
| VRP-COMP-005 | Security and authority assurance |
| VRP-COMP-006 | Evidence integrity and cryptographic commitments |
| VRP-COMP-007 | Engineering claims and limitations |

Future updates must preserve consistency across this document set.

New evidence should update the applicable claim entries without silently rewriting historical observations.

---

## 26. Qualification Update Procedure

When a new engineering campaign completes, the public documentation should be reviewed for eligible updates.

The update process should identify:

1. Newly established observations.
2. Newly qualified properties.
3. Failed acceptance conditions.
4. Confirmed defects.
5. Resolved defects.
6. Remaining limitations.
7. Superseded evidence.
8. Applicable public claim identifiers.
9. Public Validation Kit additions.
10. Approved evidence commitments.

Only the affected claims should be updated.

A new successful experiment must not automatically promote unrelated claims.

---

## 27. Claim-to-Evidence Traceability

| Public claim | Related evidence |
|---|---|
| VRP-CLAIM-IMP-001 | VRP-RT-001 |
| VRP-CLAIM-IMP-002 | VRP-RT-002 |
| VRP-CLAIM-IMP-003 | VRP-RT-003 |
| VRP-CLAIM-IMP-004 | VRP-RT-006 |
| VRP-CLAIM-IMP-005 | VRP-RT-008 |
| VRP-CLAIM-IMP-006 | VRP-RT-009 |
| VRP-CLAIM-IMP-007 | VRP-RT-005 |
| VRP-CLAIM-SEC-011 | VRP-SEC-001 |
| VRP-CLAIM-SEC-012 | VRP-SEC-002 |
| VRP-CLAIM-SEC-013 | VRP-SEC-003 |
| VRP-CLAIM-CMP-001 | VRP-CMP-A001 |
| VRP-CLAIM-CMP-002 | VRP-CMP-B001 |
| VRP-CLAIM-CMP-003 | VRP-CMP-C001 |
| VRP-CLAIM-CMP-004 | VRP-CMP-D001 |
| VRP-CLAIM-CMP-005 | VRP-CMP-E001 |
| VRP-CLAIM-EVID-001 | VRP-EVIDENCE-INTEGRITY-001 |

The referenced evidence identifiers are public documentation references.

They do not imply public availability of every underlying private artifact.

---

## 28. Current Consolidated Verdict

The recorded comparative qualification campaign establishes the following bounded engineering results.

```text
CONTINUITY_FIRST_ARCHITECTURE=DECLARED

SESSION_TRANSPORT_SEPARATION=DECLARED

NATIVE_RUNTIME_EXECUTION=OBSERVED

ACTUAL_UDP_ACTIVITY=OBSERVED

NATIVE_DELIVERY_TEST_EXECUTIONS=468

NATIVE_CANONICAL_TEST_EXECUTIONS=588

SEPARATE_UDP_COMPONENT_EXECUTIONS=208

NATIVE_SESSION_LOOKUPS=30/30

NATIVE_FAILOVER_FLOWS=30/30

OBSERVED_SESSION_HISTORY_RECORDS=210

APPLICATION_CONTINUITY_POSITIVE_CONTROL=30/30

NATIVE_MPTCP_CAPABILITY=VERIFIED

MPTCP_COMPLETE_CONNECTION_REPLACEMENTS=30

HISTORICAL_EVIDENCE_ANCHORS_VERIFIED=12

ORIGINAL_SOURCE_PRESERVATION=PASS

PROTECTED_CORE_MUTATION=NO

INTEGRATED_LIVE_IDENTITY=NOT_PROVEN

INTEGRATED_LIVE_AUTHORITY_INTEGRITY=NOT_PROVEN

MATCHED_COMPARATIVE_QUALIFICATION=INCOMPLETE

INDEPENDENT_EXTERNAL_NATIVE_REPRODUCTION=NOT_ESTABLISHED

UNIVERSAL_COMPARATIVE_SUPERIORITY=NOT_PROVEN
```

These results originate from distinct qualification scopes.

The execution counts must not be combined into an unsupported unique-test or total-coverage claim.

The verdict applies to the documented comparative campaign.

It does not replace separately attributed historical qualification evidence.

---

## 29. Next Engineering Qualification Objective

The next integrated qualification objective is to establish a complete observable relationship between:

```text
PHYSICAL_TRANSPORT_REPLACEMENT
        +
ORIGINAL_LOGICAL_LIFETIME
        +
APPLICATION_TRANSACTION_CONTINUITY
        +
AUTHORITY_INTEGRITY
        +
CANONICAL_HISTORY_PROTECTION
        +
INDEPENDENT_VERIFICATION
```

The public Validation Kit should evolve in parallel by introducing eligible reproducible controls and independent verification capabilities.

The objective is to increase the strength of the evidence without increasing disclosure of the Protected Core.

---

## 30. Final Engineering Position

VRP makes an explicit architectural distinction between session lifetime and transport lifetime.

That distinction defines its engineering qualification program.

The implementation must be evaluated according to observable guarantees.

Every successful claim must remain attributable.

Every unresolved claim must remain visible.

Every negative result must remain available for appropriate review.

Every public artifact must preserve the Protected Core boundary.

A protocol label does not determine correctness.

A successful benchmark does not establish complete security.

A recovered connection does not establish preservation of the original logical session.

The evidence determines the qualification outcome.

---

## 31. Revision History

| Revision | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial engineering claims and limitations register |

---

**Veil Routing Protocol**

**Author: Vitalijus Riabovas**

```text
SESSION != TRANSPORT

CONNECTIVITY != AUTHORITY

RECOVERY != IDENTITY PROOF

OBSERVATION != ASSUMPTION

CLAIM != EVIDENCE

INTEGRITY != AUTHENTICITY

CONFIDENTIALITY != ABSENCE OF VERIFICATION
```

The claims remain testable.

The limitations remain explicit.

The evidence remains attributable.

The intellectual property remains protected.

No hype.
Read the specifications.
Examine the evidence.
Challenge the engineering.

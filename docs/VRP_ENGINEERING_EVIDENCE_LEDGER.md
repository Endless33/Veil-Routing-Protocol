
# Veil Routing Protocol (VRP)

## Engineering Evidence Ledger

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-COMP-002  
**Revision:** 1.0  
**Classification:** PUBLIC  
**Evidence cutoff:** 2026-11-28  
**Status:** Living engineering evidence register

---

## 1. Purpose

This document establishes the public engineering evidence ledger for Veil Routing Protocol.

Its purpose is to maintain an attributable record of engineering observations, qualification results, negative findings, security boundaries, and unresolved validation requirements.

VRP does not derive its engineering credibility from architectural terminology alone.

Every implementation claim must be connected to an explicitly defined qualification objective and supporting evidence.

The governing architectural principle remains:

```text
SESSION != TRANSPORT
```

The governing qualification principle is:

```text
NO CLAIM WITHOUT EVIDENCE
```

---

## 2. Evidence Classification

All recorded engineering results shall use explicitly bounded evidence classifications.

| Classification | Meaning |
|---|---|
| OBSERVED | Behavior directly recorded during execution |
| VERIFIED | A defined assertion was checked successfully |
| QUALIFIED | Declared acceptance criteria were satisfied within the tested scope |
| REJECTED | An attempted operation returned a rejection |
| NOT_QUALIFIED | Qualification criteria were not satisfied |
| NOT_TESTED | The relevant experiment was not performed |
| NOT_PROVEN | Available evidence does not establish the claim |
| LIMITATION | A known restriction on evidence interpretation |
| SUPERSEDED | A newer evidence revision replaces an earlier conclusion |

A successful test is evidence for its evaluated assertion.

It is not automatic evidence for every architectural property of the system.

---

## 3. Evidence Attribution Model

Every future evidence entry should identify:

- Public evidence identifier.
- Qualification objective.
- Experiment category.
- Execution environment classification.
- Workload description.
- Acceptance criteria.
- Observed measurements.
- Verification outcome.
- Known limitations.
- Reproduction classification.
- Approved cryptographic evidence commitment, where available.

Private implementation references are not required in the public ledger.

Public evidence identifiers must not expose internal repository structure or confidential engineering infrastructure.

---

## 4. Evidence Register

### VRP-EVL-001 — TCP Communication Control

**Classification:** VERIFIED

Recorded observations:

- Successful communication rounds: 31.
- Scheduled endpoint replacements: 30.
- Separate TCP connections established: 31.

Qualified scope:

Successful communication across deliberately replaced TCP connections.

Limitations:

- The original TCP connections were intentionally terminated.
- This experiment does not establish the absence of application-level continuity.
- No universal claim against TCP-based systems is derived.

Reproduction classification:

PUBLIC CONTROL EXPERIMENT.

---

### VRP-EVL-002 — UDP Communication Control

**Classification:** VERIFIED

Recorded observations:

- Successful communication rounds: 31.
- Scheduled endpoint replacements: 30.

Qualified scope:

Datagram communication across changing local endpoints.

Limitations:

UDP delivery alone does not establish application-session identity, canonical history, or authority integrity.

Reproduction classification:

PUBLIC CONTROL EXPERIMENT.

---

### VRP-EVL-003 — Application Continuity Positive Control

**Classification:** VERIFIED

A controlled application model maintained application state independently of the underlying TCP connection.

Recorded observations:

```text
Scheduled transport replacements: 30
Successful application continuation: 30/30
```

Qualified scope:

Application-defined state preservation across TCP connection replacement in the tested reference model.

Engineering significance:

This positive control demonstrates that logical-session continuity can exist above conventional transport mechanisms.

It prevents an invalid comparison between a continuity-aware system and an artificially restricted transport-only baseline.

Limitations:

- Synthetic application model.
- No independent authority-integrity qualification.
- No native VRP execution.
- No claim of equivalence to the complete VRP architecture.

Reproduction classification:

PUBLIC REFERENCE MODEL.

---

### VRP-EVL-004 — Native Multipath TCP Control

**Classification:** VERIFIED

Native operating-system MPTCP capability was exercised.

Recorded observations:

- Successful native MPTCP payload exchanges: 10.
- Native MPTCP operation confirmed within the tested socket environment.
- TCP fallback was not observed in the qualified execution.

Qualified scope:

Native MPTCP communication capability.

Limitations:

Subflow migration and application-session lifetime preservation were not evaluated by this experiment.

Reproduction classification:

PUBLIC CONTROL EXPERIMENT.

---

### VRP-EVL-005 — Complete MPTCP Connection Replacement

**Classification:** VERIFIED

Recorded observations:

| Measurement | Result |
|---|---:|
| Native MPTCP connections | 31 |
| Successful payload exchanges | 62 |
| Complete connection replacements | 30 |
| Observed connection-token changes after replacement | 30 |
| Observed token stability within individual connections | 31 |

Qualified scope:

Native transport-connection identity behavior across complete connection termination and subsequent establishment.

Limitations:

- MPTCP connection tokens are transport-level identifiers.
- They are not independent application-session lifetime identifiers.
- Native MPTCP subflow migration was not evaluated.
- No claim against MPTCP path continuity is made.

Reproduction classification:

PUBLIC CONTROL EXPERIMENT.

---

### VRP-EVL-006 — Native VRP Runtime Execution

**Classification:** OBSERVED

An existing native VRP runtime was executed in an isolated network environment.

Recorded observations:

```text
Runtime execution exit status: 0
Execution duration: approximately 3.016 seconds
```

Qualified scope:

Successful execution of the selected native runtime artifact.

Limitations:

A successful process exit does not independently establish logical-session continuity, application delivery, or authority integrity.

Reproduction classification:

AUTHORIZED NATIVE EVALUATION.

---

### VRP-EVL-007 — Independent UDP Transport Observation

**Classification:** OBSERVED

A system-level observer recorded network-related activity during execution of the selected native VRP runtime.

Recorded observations:

| Measurement | Result |
|---|---:|
| UDP socket creations | 3 |
| Distinct observed local UDP port values | 3 |
| Incomplete observer records | 0 |

Qualified scope:

Independent observation of actual UDP socket activity and distinct local port values.

Limitations:

- Socket activity is not a canonical identity oracle.
- Distinct ports alone do not prove preservation of one logical-session lifetime.
- Application delivery and authority integrity were not independently correlated with these observations.

Reproduction classification:

AUTHORIZED NATIVE EVALUATION.

---

### VRP-EVL-008 — Selected Canonical Test Campaign

**Classification:** QUALIFIED

Recorded observations:

| Execution category | Successful executions |
|---|---:|
| Selected baseline tests | 49 |
| Repeated selected tests | 490 |
| Race-detector executions | 49 |
| Total successful executions | 588 |

Distinct selected tests:

```text
49
```

Qualified scope:

Successful execution of the selected native test campaign, including repeated execution and race-detector qualification.

Limitations:

- The total of 588 represents test executions.
- It does not represent 588 distinct test cases.
- It does not establish exhaustive coverage.
- Race-detector success does not establish universal absence of concurrency defects.

Reproduction classification:

AUTHORIZED NATIVE EVALUATION.

---

### VRP-EVL-009 — Native Session Observer

**Classification:** QUALIFIED

Recorded observations:

- Native runtime initialization succeeded.
- Native session observation capability was accessible.
- Initial session registry was empty.
- No pre-existing logical session was required.

Qualified scope:

Runtime accessibility of the tested native session observation interface.

Limitations:

Observer initialization alone does not establish continuity.

Reproduction classification:

AUTHORIZED NATIVE EVALUATION.

---

### VRP-EVL-010 — Native Session Registration

**Classification:** QUALIFIED

Recorded observations:

```text
Native session registration: PASS
Repeated session lookups: 30/30
Selected race-detector execution: PASS
```

Qualified scope:

Successful native session registration and repeated observation through the tested registry interface.

Limitations:

- No physical transport replacement was performed.
- Registry lookup is not sufficient proof of independent session lifetime preservation.
- Authority integrity was not established by this experiment.

Reproduction classification:

AUTHORIZED NATIVE EVALUATION.

---

### VRP-EVL-011 — Native Failover Execution

**Classification:** QUALIFIED

Recorded observations:

```text
Native failover flows completed: 30/30
History records per completed flow: 7
Total history records observed: 210
Observed UDP socket creations: 0
```

Qualified scope:

Successful execution of thirty independent native failover flows and availability of recorded session history.

Engineering significance:

The tested native scenario demonstrated repeatable execution and observable history production.

Limitations:

- Thirty independent flows are not thirty migrations of one session.
- The observed scenario did not establish physical UDP replacement.
- History availability does not independently establish complete canonical-history integrity.
- This result must not be presented as a completed live-network continuity qualification.

Reproduction classification:

AUTHORIZED NATIVE EVALUATION.

---

### VRP-EVL-012 — Rejected Duplicate Initialization

**Classification:** REJECTED

A qualification fixture attempted an operation against a previously registered session.

The operation returned an error.

Recorded observations:

```text
Original session lookup after rejection: SUCCESS
Observed session count after rejection: 1
```

Qualified scope:

The tested rejection did not remove the observed registry entry.

Limitations:

- The complete rejection semantics were not independently qualified.
- Unchanged registry cardinality does not establish full state preservation.
- No universal duplicate-commit or authority-integrity guarantee is inferred from this experiment alone.

Reproduction classification:

AUTHORIZED NATIVE EVALUATION.

---

### VRP-EVL-013 — Migration Qualification Boundary

**Classification:** NOT_QUALIFIED

A dedicated sequential migration fixture was attempted.

The experiment encountered rejected initialization and migration operations.

Recorded outcome:

```text
Requested additional migration sequence: 30
Completed additional migrations: 0
```

The implementation was preserved.

No implementation modification was performed to force the experimental fixture to pass.

Qualified engineering finding:

The attempted fixture did not establish the required initialization and authorization preconditions.

Limitations:

- The rejection does not independently establish an implementation defect.
- The experiment does not establish successful sequential canonical migration.
- The experiment does not establish complete fail-closed security behavior.

Reproduction classification:

RESTRICTED QUALIFICATION RECORD.

---

### VRP-EVL-014 — Integrated Live Identity Qualification

**Classification:** NOT_PROVEN

The comparative qualification campaign identified an unresolved observation boundary between the available live network execution and independent canonical lifetime observation.

The required integrated experiment must correlate:

- One logical-session lifetime.
- Actual transport replacement.
- Independent identity observation.
- Application delivery.
- Application transaction-state preservation.
- Authority integrity.
- Canonical history preservation.

These observations must belong to the same attributable execution.

Separate successful component experiments must not be combined into an unsupported end-to-end continuity claim.

Reproduction classification:

DEDICATED INTEGRATION FIXTURE REQUIRED.

---

### VRP-EVL-015 — Evidence Consolidation

**Classification:** VERIFIED

Recorded observations:

```text
Historical evidence anchors verified: 12
Evidence consolidation: PASS
Original repository preservation: PASS
Evidence integrity: PASS
Additional runtime tests: 0
Comparative qualification: INCOMPLETE
```

Qualified scope:

Integrity verification and consolidation of the selected historical evidence records.

Limitations:

Cryptographic evidence verification establishes consistency with the recorded byte-level commitments.

It does not independently establish experimental correctness or operator authenticity.

The consolidation result is not a protocol qualification result.

Reproduction classification:

CONTROLLED EVIDENCE VERIFICATION.

---

## 5. Consolidated Measurement Summary

| Measurement | Recorded result | Interpretation |
|---|---:|---|
| TCP communication rounds | 31 | Transport control |
| UDP communication rounds | 31 | Transport control |
| Application positive-control continuations | 30/30 | Synthetic session preservation |
| Native MPTCP control exchanges | 10 | Native transport capability |
| MPTCP replacement experiment connections | 31 | Complete connection replacement |
| MPTCP replacement experiment payload exchanges | 62 | Communication verification |
| MPTCP token changes after complete replacement | 30 | Transport identity replacement |
| Observed VRP UDP socket creations | 3 | Network activity |
| Distinct observed VRP local UDP port values | 3 | Endpoint-related observation |
| Selected canonical tests | 49 | Test selection scope |
| Successful selected canonical test executions | 588 | Repeated and race qualification |
| Repeated native session lookups | 30/30 | Registry observation |
| Completed native failover flows | 30/30 | Native scenario execution |
| Observed failover history records | 210 | History availability |
| Verified historical evidence anchors | 12 | Evidence integrity |

These measurements originate from distinct experiments.

They must not be summed into a single test-count claim or treated as one integrated workload.

---

## 6. Canonical Continuity Acceptance Boundary

The final continuity acceptance condition is stronger than successful reconnection.

```text
Same logical-session lifetime
    +
Verified physical transport replacement
    +
Preserved application transaction state
    +
Valid authority
    +
Protected canonical history
    +
Independent observation
```

Every required property must be attributable to the same experiment.

The following observations are insufficient when considered alone:

```text
PROCESS_ALIVE
SOCKET_ALIVE
CONNECTION_RECOVERED
PACKET_DELIVERED
SESSION_ID_REUSED
TEST_EXIT_ZERO
```

The acceptance boundary is intentionally strict.

A weaker acceptance criterion would undermine the architectural distinction that VRP is intended to establish.

---

## 7. Comparative Qualification Matrix

| Property | Control experiments | Native VRP evidence | Integrated comparative qualification |
|---|---|---|---|
| Transport communication | VERIFIED | OBSERVED | INCOMPLETE |
| Complete connection replacement | VERIFIED | Separate UDP observations | INCOMPLETE |
| Application-defined continuity | Positive control verified | Not independently correlated | INCOMPLETE |
| Session registry observation | Not applicable to raw transport | QUALIFIED | INCOMPLETE |
| Native failover execution | Different workload | QUALIFIED | INCOMPLETE |
| Canonical lifetime identity across physical replacement | Not established by control suite | NOT_PROVEN | INCOMPLETE |
| Authority integrity under matched faults | NOT_TESTED | Not established by this campaign | INCOMPLETE |
| Comparative superiority | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |

This matrix describes the current comparative campaign.

It does not invalidate separately qualified historical VRP results.

Historical claims must retain their original scope, implementation provenance, and acceptance conditions.

---

## 8. Evidence Commitments

Public cryptographic commitments shall use SHA-256 unless a documented evidence-format revision specifies another approved algorithm.

Each published commitment must identify:

- Public evidence identifier.
- Committed artifact classification.
- Digest algorithm.
- Digest value.
- Evidence-format revision.
- Verification scope.
- Artifact availability classification.

An example evidence commitment record:

```json
{
  "evidence_id": "PUBLIC-EVIDENCE-ID",
  "digest_algorithm": "SHA-256",
  "digest_status": "PENDING_DISCLOSURE_APPROVAL",
  "artifact_scope": "approved evidence manifest",
  "reproduction_class": "authorized evaluation",
  "publication_status": "not approved"
}
```

The example is a schema illustration, not an actual evidence commitment.

No placeholder may be represented as a real cryptographic digest.

Private repository hashes and internal evidence-manifest hashes must not be copied into public records without disclosure review.

---

## 9. Reproducibility Classes

### Class A — Public Reproduction

The complete experiment can be executed using publicly available tools and approved public test components.

Examples include conventional transport controls and synthetic application-session models.

### Class B — Public Evidence Verification

Approved evidence artifacts are available for integrity verification and independent interpretation.

This class does not necessarily permit re-execution of the original native implementation.

### Class C — Authorized Black-Box Evaluation

A researcher can execute approved workloads against a restricted native evaluation environment.

Protected Core source access is not required.

### Class D — Restricted Engineering Evidence

The evidence exists within the private engineering qualification environment.

Only approved aggregate observations or cryptographic commitments may be publicly disclosed.

A Class D record must not be advertised as independently reproducible through the public repository.

---

## 10. Negative Controls

Every future continuity qualification should include negative controls capable of detecting false-positive acceptance.

Required negative-control categories include:

- Replacement with a newly created logical session.
- Reuse of an externally visible identifier without lifetime preservation.
- Successful transport recovery without application-state preservation.
- Missing or invalid observation evidence.
- Rejected authorization conditions.
- Incomplete measurement records.
- Modified evidence artifacts.

A validation system that cannot distinguish a successful continuity experiment from an intentionally invalid reference case is not sufficient for final qualification.

---

## 11. Evidence Ledger Evolution

This ledger is intended to remain a living engineering record.

Every newly completed qualification campaign should produce an attributable update containing:

1. New public evidence identifiers.
2. Newly observed measurements.
3. Qualification outcomes.
4. Negative findings.
5. Relevant limitations.
6. Reproduction classification.
7. Approved evidence commitments.
8. Relationship to previous evidence.
9. Public Validation Kit implications.
10. Disclosure approval status.

Historical records must not be silently rewritten to improve apparent qualification results.

Corrections must be explicit.

Superseded claims must remain traceable.

A new implementation qualification must not automatically inherit every claim from an earlier implementation.

---

## 12. Public Validation Kit Synchronization

The public Validation Kit should be updated when a newly qualified experiment introduces a reusable public capability.

Eligible additions include:

- New transport control scenarios.
- New synthetic application workloads.
- Independent observer acceptance tests.
- Evidence schema extensions.
- Evidence verification improvements.
- Negative-control scenarios.
- New measurement formats.
- Approved reference results.
- Updated qualification limitations.

A private test result does not automatically authorize publication of the associated test implementation.

The public equivalent must be reviewed independently for confidentiality, correctness, and reproducibility.

The Validation Kit must distinguish clearly between:

```text
PUBLIC REFERENCE MODEL
PUBLIC CONTROL EXPERIMENT
PUBLIC EVIDENCE VERIFICATION
AUTHORIZED NATIVE EVALUATION
```

These categories must never be represented as interchangeable.

---

## 13. Future Qualification Targets

The following targets remain relevant to the continuity-first engineering program:

| Qualification target | Required observation |
|---|---|
| Repeated endpoint churn | Preserved canonical lifetime |
| Network blackout and recovery | Identity and application-state preservation |
| Packet loss | Qualified delivery and recovery behavior |
| Packet reordering | Correct handling within declared semantics |
| Packet duplication | Duplicate-operation containment |
| Replay | Rejection within declared security scope |
| Stale authority | Rejection without unauthorized state mutation |
| Concurrent operations | Preservation of declared invariants |
| Compound faults | Correlated continuity and authority evidence |

These are future or separately scoped qualification objectives.

Their inclusion in this ledger does not declare them newly proven by the comparative campaign.

---

## 14. Protected Core Disclosure Policy

The following information is excluded from this public evidence ledger:

- Protected Core source code.
- Internal protocol algorithms.
- Confidential state-machine implementation.
- Private authority-management mechanisms.
- Private session identifiers.
- Internal runtime traces.
- Internal repository paths.
- Private repository commit and tree identifiers.
- Unapproved evidence-manifest commitments.
- Build artifacts containing confidential implementation.
- Keys, tokens, credentials, and infrastructure configuration.

Public evidence shall demonstrate observable behavior without enabling reconstruction of the protected implementation.

---

## 15. Publication Acceptance Gate

Before a new evidence entry is published, the following conditions should be satisfied:

```text
EVIDENCE_SCOPE_DEFINED
RESULT_ATTRIBUTED
LIMITATIONS_DECLARED
MEASUREMENTS_VERIFIED
REPRODUCTION_CLASS_DEFINED
DISCLOSURE_REVIEW_COMPLETED
PROTECTED_CORE_EXPOSURE_REJECTED
```

An unresolved publication gate must prevent release of the affected evidence artifact.

Passing an engineering test does not automatically authorize public disclosure.

---

## 16. Current Engineering Verdict

The qualification campaign recorded successful native execution, repeated selected test execution, session registration, native failover scenarios, system-level UDP observations, and conventional transport control experiments.

It also identified unresolved requirements for integrated live canonical identity qualification.

Both categories of evidence are retained.

```text
NATIVE_RUNTIME_EXECUTION=OBSERVED

SELECTED_TEST_QUALIFICATION=PASS

NATIVE_SESSION_REGISTRATION=PASS

NATIVE_FAILOVER_FLOWS=30/30

OBSERVED_SESSION_HISTORY_RECORDS=210

INDEPENDENT_UDP_ACTIVITY=OBSERVED

HISTORICAL_EVIDENCE_ANCHORS_VERIFIED=12

INTEGRATED_LIVE_IDENTITY=NOT_PROVEN

MATCHED_COMPARATIVE_QUALIFICATION=INCOMPLETE

UNIVERSAL_SUPERIORITY=NOT_PROVEN
```

The engineering program continues.

No unresolved qualification objective is converted into a successful claim through terminology, inference, or marketing.

---

## 17. Revision History

| Revision | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial public comparative engineering evidence ledger |

---

**Veil Routing Protocol**

**Author: Vitalijus Riabovas**

```text
SESSION != TRANSPORT

OBSERVATION != ASSUMPTION

TEST SUCCESS != UNIVERSAL CORRECTNESS

HASH INTEGRITY != EXPERIMENTAL PROOF
```

Engineering evidence is cumulative.

Engineering claims remain bounded.

Protected Core remains confidential.

No hype.
Read the specifications.
Examine the evidence.
Challenge the engineering.

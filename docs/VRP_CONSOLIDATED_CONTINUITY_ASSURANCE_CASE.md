
# Veil Routing Protocol (VRP)

## Consolidated Continuity Assurance Case

### Transport-Independent Logical Session Lifetime, Security Integrity and Independent Evidence

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-CONT-E005  
**Revision:** 1.0  
**Classification:** PUBLIC  
**Evidence cutoff:** 2026-11-28  
**Status:** Consolidated engineering assurance case — partial qualification

---

## 1. Executive Summary

Veil Routing Protocol establishes logical-session continuity as an explicit architectural responsibility independent of individual transport lifetimes.

The fundamental architectural invariant is:

```text
SESSION != TRANSPORT
```

The objective is to preserve the original logical-session lifetime and its required application, authorization, and canonical-history properties across qualified communication changes.

VRP is evaluated through multiple complementary engineering dimensions:

- Native implementation execution.
- Physical transport observation.
- Logical lifetime identity.
- Application transaction continuity.
- Authority integrity.
- Replay containment.
- Duplicate-commit rejection.
- Canonical history preservation.
- Recovery integrity.
- Concurrency qualification.
- Evidence integrity.
- Independent black-box evaluation.

This assurance case consolidates the available engineering record while preserving the distinction between declared guarantees, observed native behavior, qualified reference controls, historical reported results, and unresolved integrated qualification requirements.

The Protected Core is intentionally excluded from public disclosure.

---

## 2. Central Architectural Claim

### Claim VRP-CONT-C001

A logical session must not be defined exclusively by the lifetime of an underlying transport connection.

### Declared Acceptance Property

```text
Transport A disappears.

Transport B becomes available.

The original logical lifetime remains the same.

Required application state remains valid.

Required authority remains valid.

Required canonical history remains protected.
```

### Conceptual Architecture

```text
+-----------------------------------------------------+
|                                                     |
|             ORIGINAL LOGICAL SESSION L0             |
|                                                     |
|    Identity | Application | Authority | History    |
|                                                     |
+-----------------------------------------------------+
          |                  |                 |
          v                  v                 v
    +-----------+      +-----------+     +-----------+
    |Transport A|      |Transport B|     |Transport C|
    +-----------+      +-----------+     +-----------+

        Changing communication contexts

        Required invariant: original lifetime L0
```

This diagram represents the public architectural contract.

It is not a representation of proprietary implementation structure.

### Current Claim Classification

```text
ARCHITECTURAL_CONTRACT=DECLARED

COMPONENT_EVIDENCE=AVAILABLE

HISTORICAL_CONTINUITY_RESULTS=REPORTED

LATEST_INTEGRATED_NATIVE_QUALIFICATION=INCOMPLETE
```

---

## 3. Assurance Case Structure

The principal assurance claim is supported by distinct engineering claims.

```text
G0: Transport-independent logical-session continuity
 |
 +-- G1: Native implementation correctness
 |
 +-- G2: Actual physical transport transition
 |
 +-- G3: Original logical lifetime preservation
 |
 +-- G4: Application transaction preservation
 |
 +-- G5: Authority integrity
 |
 +-- G6: Replay and duplicate-effect containment
 |
 +-- G7: Canonical history preservation
 |
 +-- G8: Recovery integrity
 |
 +-- G9: Evidence integrity and completeness
 |
 +-- G10: Independent evaluation
```

The complete G0 assurance claim requires the applicable supporting claims to be established within a common qualification scope.

Individual supporting claims may have different evidence classifications.

Successful isolated observations must not be combined into an unsupported integrated verdict.

---

## 4. Evidence Classification Standard

| Classification | Meaning |
|---|---|
| DECLARED | Architectural requirement |
| OBSERVED | Recorded experimental behavior |
| VERIFIED | A specified assertion was checked successfully |
| QUALIFIED | Applicable acceptance requirements were satisfied |
| HISTORICAL_REPORTED | Earlier result requiring original evidence attribution |
| REFERENCE_ONLY | Result belongs to a synthetic or public reference model |
| NOT_TESTED | Relevant workload was not executed |
| NOT_PROVEN | Available evidence does not establish the specified claim |
| NOT_QUALIFIED | Qualification requirements were not satisfied |
| INCOMPLETE | Mandatory supporting evidence remains unresolved |

Classification applies to a particular implementation, workload, environment, observation method, and acceptance contract.

No classification implies unrestricted correctness outside its original scope.

---

## 5. Consolidated Engineering Evidence Dashboard

| Evidence category | Recorded or reported result | Classification |
|---|---:|---|
| Historical migration storm | 1,000 migrations | HISTORICAL_REPORTED |
| Historical replay storm | 9,999 rejections | HISTORICAL_REPORTED |
| Historical network interruption | Approximately 41.6 seconds | HISTORICAL_REPORTED |
| Earlier baseline continuity | PASS reported | HISTORICAL_REPORTED |
| Earlier short endpoint churn | PASS reported | HISTORICAL_REPORTED |
| Native runtime execution | Exit status 0 | OBSERVED |
| Native system-level network records | 23 | OBSERVED |
| Native UDP socket creations | 3 | OBSERVED |
| Distinct observed native local UDP ports | 3 | OBSERVED |
| Native delivery fixture executions | 468 | QUALIFIED within selected scope |
| Native canonical regression executions | 588 | QUALIFIED within selected scope |
| Separate UDP evaluation component executions | 208 | COMPONENT QUALIFICATION |
| Native session lookups | 30/30 | QUALIFIED within tested fixture |
| Native independent failover flows | 30/30 | QUALIFIED within tested scenario |
| Native failover history records | 210 | OBSERVED |
| Transport-independent application reference continuations | 30/30 | REFERENCE_ONLY |
| TCP communication rounds | 31/31 | CONTROL QUALIFICATION |
| UDP communication rounds | 31/31 | CONTROL QUALIFICATION |
| Native MPTCP capability exchanges | 10 | CONTROL QUALIFICATION |
| Complete MPTCP connection replacements | 30 | CONTROL QUALIFICATION |
| Historical comparative evidence manifests verified | 12 | REPORTED INTEGRITY VERIFICATION |

The measurements originate from distinct qualification campaigns.

Repeated executions are not distinct test cases.

Reference-model results are not native VRP results.

Historical reported results are not newly independently verified observations.

---

## 6. Native Implementation Assurance

### Supporting Claim G1

The evaluated native VRP implementation is executable and supports the selected engineering qualification scenarios.

### Evidence Register

| Evidence reference | Observation |
|---|---|
| VRP-CONT-N001 | Native runtime execution |
| VRP-CONT-N002 | Native canonical regression |
| VRP-CONT-N003 | Native session registration and observation |
| VRP-CONT-N004 | Repeated native failover execution |
| VRP-RT-003 | Native delivery-related fixture campaign |
| VRP-RT-006 | Native canonical regression campaign |

### Recorded Test Distribution

| Native campaign | Baseline | Repeated | Race detector | Total |
|---|---:|---:|---:|---:|
| Delivery-related selection | 39 | 390 | 39 | 468 |
| Canonical regression selection | 49 | 490 | 49 | 588 |

A separate UDP evaluation component recorded:

| Component campaign | Successful executions |
|---|---:|
| Baseline | 8 |
| Repeated execution | 160 |
| Race detector | 40 |
| Total | 208 |

### Canonical Regression Visualization

```text
BASELINE

[#####] 49


REPEATED EXECUTION

[##################################################] 490


RACE DETECTOR

[#####] 49


TOTAL SUCCESSFUL EXECUTIONS: 588
```

### Qualification Verdict

```text
NATIVE_IMPLEMENTATION_EXECUTION=OBSERVED

SELECTED_NATIVE_REGRESSION=QUALIFIED

SELECTED_RACE_EXECUTION=QUALIFIED

EXHAUSTIVE_IMPLEMENTATION_CORRECTNESS=NOT_PROVEN
```

The selected test campaigns may overlap.

Their execution counts must not be combined into an unsupported unique-test coverage claim.

---

## 7. Physical Transport Observation Assurance

### Supporting Claim G2

Actual network behavior must be independently observable.

### Recorded Native Measurements

| Measurement | Result |
|---|---:|
| Native runtime exit status | 0 |
| Approximate runtime duration | 3.016 seconds |
| System-level network observation records | 23 |
| UDP socket creations | 3 |
| Bind operations | 1 |
| Connect operations | 2 |
| Local socket-address queries | 3 |
| Distinct observed local UDP port values | 3 |
| Incomplete observer records | 0 |

The runtime duration and system-level observations originated from separate executions.

### Evidence Interpretation

The selected implementation exercised actual network resources.

The system-level observations provide evidence beyond implementation-generated success statements.

However, independently observed network activity is not sufficient to establish preservation of the original logical-session lifetime.

### Qualification Verdict

```text
ACTUAL_NATIVE_NETWORK_ACTIVITY=OBSERVED

UDP_SOCKET_ACTIVITY=OBSERVED

DISTINCT_LOCAL_PORT_VALUES=OBSERVED

SAME_LIFETIME_PHYSICAL_MIGRATION=NOT_PROVEN
```

---

## 8. Logical Lifetime Identity Assurance

### Supporting Claim G3

The original logical-session lifetime must remain distinguishable from a replacement lifetime.

### Recorded Native Session Observation

| Measurement | Result |
|---|---:|
| Initial registration | PASS |
| Repeated observation attempts | 30 |
| Successful observations | 30 |
| Observed registry cardinality | 1 |
| Selected race-detector qualification | PASS |

### Recorded Native Scenario Execution

| Measurement | Result |
|---|---:|
| Independent native failover flows | 30 |
| Successful completions | 30 |
| Observed history records per flow | 7 |
| Total observed history records | 210 |
| Observed UDP socket creations | 0 |

### Native Observation Distribution

```text
Repeated session lookups

[##############################] 30/30


Independent failover completions

[##############################] 30/30
```

The recorded observations establish session accessibility and repeatable native scenario execution.

The independent failover flows were separately initialized.

They do not represent thirty physical transport replacements within one logical lifetime.

### Qualification Verdict

```text
NATIVE_SESSION_REGISTRATION=QUALIFIED

NATIVE_SESSION_OBSERVATION=QUALIFIED

NATIVE_FAILOVER_REPEATABILITY=QUALIFIED

INDEPENDENT_LIFETIME_CORRELATION_ACROSS_PHYSICAL_REPLACEMENT=NOT_PROVEN
```

---

## 9. Original Lifetime Versus Replacement Lifetime

The following conceptual comparison defines the independent identity acceptance contract.

### Case A — Original Lifetime Preserved

```text
TIME          T0          T1          T2

TRANSPORT      A           B           C

LIFETIME      L0          L0          L0

LABEL          S           S           S

RESULT       BASE        MATCH       MATCH
```

Expected identity verdict:

```text
CONTINUITY_ACCEPTED
```

### Case B — Replacement Lifetime With Reused Label

```text
TIME          T0          T1          T2

TRANSPORT      A           B           C

LIFETIME      L0          L1          L2

LABEL          S           S           S

RESULT       BASE       MISMATCH    MISMATCH
```

Expected identity verdict:

```text
CONTINUITY_REJECTED
```

Both cases retain the same external label.

Only the first case preserves the original logical lifetime.

These are acceptance models rather than native execution traces.

---

## 10. Identity False-Positive Rejection Matrix

| Observation | Sufficient for original-lifetime proof? |
|---|---|
| Same process identifier | NO |
| Same socket descriptor | NO |
| Same endpoint | NO |
| Same external session label | NO |
| Successful transport recovery | NO |
| Successful packet exchange | NO |
| Successful registry lookup | NO |
| Same history-record count | NO |
| Implementation-generated success marker | NO |
| Independently qualified lifetime observation | Required |

The final observation must be appropriately attributed to the actual evaluated logical lifetime.

Its effectiveness must be established through relevant positive and negative controls.

---

## 11. Application Continuity Assurance

### Supporting Claim G4

Required application transaction state must remain valid across qualified communication changes.

### Recorded Reference Control Results

| Reference model | Scheduled transitions | State continuations |
|---|---:|---:|
| TCP connection-bound | 30 | 0 |
| UDP endpoint-bound | 30 | 0 |
| TCP transport-independent | 30 | 30 |

### Continuation Visualization

```text
TCP CONNECTION-BOUND

[                              ]  0/30


UDP ENDPOINT-BOUND

[                              ]  0/30


TRANSPORT-INDEPENDENT APPLICATION

[##############################] 30/30
```

### Engineering Significance

The experiment demonstrates the distinction between transport-bound application state and application state maintained independently of transport lifetime.

The positive control demonstrates that conventional transports can support higher-layer continuity.

The negative models intentionally bind their state to the selected transport context.

These results validate the selected reference experiment.

They do not establish native VRP application continuity.

### Qualification Verdict

```text
REFERENCE_APPLICATION_CONTINUITY=VERIFIED

REFERENCE_CONTINUATION_COUNT=30/30

NATIVE_INTEGRATED_APPLICATION_CONTINUITY=NOT_PROVEN
```

---

## 12. Authority Integrity Assurance

### Supporting Claim G5

Transport recovery or replacement must not automatically confer authority to perform protected operations.

### Recorded Native Rejection Evidence

| Observation | Result |
|---|---|
| Tested native operation | REJECTED |
| Original registry entry accessible after rejection | YES |
| Observed session cardinality after rejection | 1 |
| Complete protected-state comparison | NOT_ESTABLISHED |

A later native migration fixture also recorded a rejected additional migration request.

The diagnostic received a preliminary authorization-related classification.

The complete root cause was not independently established.

### Historical Security Records

| Property | Earlier reported result |
|---|---|
| Stale-authority rejection | PASS reported |
| Epoch rollback rejection | PASS reported |
| Canonical rewrite rejection | PASS reported |

The original artifacts require separate attribution before stronger public qualification claims are assigned.

### Qualification Verdict

```text
NATIVE_REJECTION_BEHAVIOR=OBSERVED

POST_REJECTION_REGISTRY_AVAILABILITY=VERIFIED

COMPLETE_REJECTION_ATOMICITY=NOT_PROVEN

INTEGRATED_LIVE_AUTHORITY_INTEGRITY=NOT_PROVEN
```

---

## 13. Replay and Duplicate-Effect Assurance

### Supporting Claim G6

Previously accepted operations must not produce unauthorized repeated protected effects.

### Historical Replay-Storm Record

| Measurement | Reported result |
|---|---:|
| Replay attempts | 9,999 |
| Rejected replay attempts | 9,999 |
| Accepted replay attempts | 0 |
| Reported rejection ratio | 100% |

### Historical Result Distribution

```text
REPORTED REJECTIONS

[##############################] 9999


REPORTED ACCEPTANCES

[                              ]    0
```

The original evidence artifacts were not directly re-inspected for this assurance case.

The exact implementation category, protected-effect semantics, and associated state-preservation evidence require original attribution.

### Required Security Distinction

```text
REPLAYED_PACKET != REPEATED_PROTECTED_EFFECT
```

Successful rejection of repeated communication events does not automatically establish application-level or canonical duplicate-commit containment.

### Qualification Verdict

```text
HISTORICAL_REPLAY_REJECTIONS=9999_REPORTED

INTEGRATED_NATIVE_REPLAY_CONTAINMENT_DURING_MIGRATION=NOT_PROVEN

INTEGRATED_DUPLICATE_COMMIT_CONTAINMENT=NOT_PROVEN
```

---

## 14. Canonical History Assurance

### Supporting Claim G7

Required previously accepted logical history must remain protected across qualified transitions.

### Recorded Native History Availability

| Measurement | Result |
|---|---:|
| Completed independent native failover flows | 30 |
| Minimum observed history records per flow | 7 |
| Maximum observed history records per flow | 7 |
| Total observed history records | 210 |

### Required History Semantics

| Property | Required outcome |
|---|---|
| Previously accepted operations | Preserved according to contract |
| Unauthorized history removal | Prevented or detected |
| Unauthorized history modification | Prevented or detected |
| Unauthorized operation replacement | Prevented or detected |
| Unauthorized additional commitments | Absent |
| Mandatory history observations | Complete |

History availability and history integrity are different properties.

A matching history length does not establish matching accepted-history semantics.

### Qualification Verdict

```text
NATIVE_HISTORY_AVAILABILITY=OBSERVED

OBSERVED_HISTORY_RECORDS=210

INTEGRATED_CANONICAL_HISTORY_INTEGRITY=NOT_PROVEN
```

---

## 15. Migration and Recovery Assurance

### Supporting Claim G8

Recovery must preserve the applicable logical-session, application, authority, and canonical-history properties.

### Historical Migration and Recovery Register

| Historical record | Reported result |
|---|---|
| Migration storm | 1,000 migrations |
| Baseline continuity | PASS |
| Short endpoint churn | PASS |
| Network interruption | Approximately 41.6 seconds |

These earlier results remain relevant to the overall engineering record.

Their original artifacts must be re-attributed to establish the exact qualification scope.

### Recovery Acceptance Model

```text
BEFORE NETWORK INTERRUPTION
--------------------------------
Original logical lifetime L0
Required application state valid
Required authority valid

             |
             v

NETWORK INTERRUPTION
--------------------------------
Transport unavailable
Lifetime subject to verification

             |
             v

AFTER NETWORK RESTORATION
--------------------------------
Original lifetime L0 independently confirmed
Required application state verified
Required authority verified
Required history verified
```

The model describes the required recovery outcome.

It is not an actual native execution trace.

### Qualification Verdict

```text
HISTORICAL_MIGRATION_STORM=1000_REPORTED

HISTORICAL_BLACKOUT=APPROX_41_6_SECONDS_REPORTED

HISTORICAL_BASELINE_CONTINUITY=PASS_REPORTED

HISTORICAL_SHORT_CHURN_CONTINUITY=PASS_REPORTED

LATEST_INTEGRATED_NATIVE_RECOVERY=NOT_PROVEN
```

The reported interruption duration must not be presented as complete logical-session recovery latency.

---

## 16. Evidence Integrity Assurance

### Supporting Claim G9

Engineering evidence must remain attributable, complete, and resistant to undetected modification relative to established commitments.

### Recorded Evidence Consolidation

| Property | Reported result |
|---|---|
| Historical evidence manifests verified | 12 |
| Evidence consolidation | PASS |
| Evidence integrity | PASS |
| Original source preservation | PASS |
| Repository identity preservation | PASS |
| Protected Core mutation | NO |
| New runtime tests during consolidation | 0 |

### Integrity Boundary

The underlying private artifacts were verified within the engineering environment.

This document does not provide direct external access to those artifacts.

No unapproved private SHA-256 values are included.

### Qualification Verdict

```text
PRIVATE_EVIDENCE_CONSOLIDATION=PASS_REPORTED

HISTORICAL_EVIDENCE_ANCHORS_VERIFIED=12

PUBLIC_ARTIFACT_COMMITMENTS=PENDING

INDEPENDENT_PUBLIC_ARTIFACT_VERIFICATION=NOT_ESTABLISHED
```

A matching digest establishes consistency with committed artifact bytes.

It does not independently establish experimental authenticity or architectural correctness.

---

## 17. Independent Evaluation Assurance

### Supporting Claim G10

An external evaluator must be able to assess eligible guarantees without unrestricted access to the Protected Core.

### Public Evaluation Boundary

| Evaluation capability | Classification |
|---|---|
| Public architectural contract | Eligible for public review |
| Public reference workloads | Eligible for independent reproduction |
| TCP and UDP controls | Eligible for independent reproduction |
| Synthetic lifetime controls | Eligible for independent reproduction |
| Approved evidence integrity checks | Eligible for independent verification |
| Native VRP behavior | Requires approved evaluation environment |
| Native lifetime observation | Requires qualified observation boundary |
| Proprietary implementation inspection | Outside public disclosure scope |

### Qualification Verdict

```text
PUBLIC_VALIDATION_CONTRACT=DEFINED

REFERENCE_EVALUATION_SCOPE=DEFINED

INDEPENDENT_NATIVE_REPRODUCTION=NOT_ESTABLISHED

PROTECTED_CORE_DISCLOSURE=NOT_REQUIRED_BY_CONTRACT
```

The existence of a public evaluation specification does not automatically establish that a native evaluation service is currently available.

---

## 18. Consolidated Assurance Claim Matrix

| Supporting claim | Available evidence | Current status |
|---|---|---|
| G1 — Native implementation | Runtime execution and selected regressions | COMPONENT QUALIFIED |
| G2 — Physical transport | Independent UDP observations | OBSERVED |
| G3 — Logical lifetime | Native registration and lookup | PARTIAL |
| G4 — Application continuity | Positive reference control | REFERENCE VERIFIED |
| G5 — Authority integrity | Native rejection observations | PARTIAL |
| G6 — Replay containment | Historical replay record | REPORTED |
| G7 — Canonical history | Native history availability | PARTIAL |
| G8 — Recovery | Historical migration and blackout records | REPORTED |
| G9 — Evidence integrity | Twelve historical manifests | REPORTED VERIFIED |
| G10 — Independent evaluation | Public validation contract | DEFINED |

### Principal Claim Status

```text
G0_INTEGRATED_NATIVE_CONTINUITY=NOT_YET_ESTABLISHED
    within the latest comparative campaign
```

Historical qualification results must retain their original scope.

An incomplete later campaign does not automatically invalidate an earlier successful qualification.

---

## 19. Evidence Independence Matrix

| Observation source | Establishes | Does not independently establish |
|---|---|---|
| Runtime execution | Implementation executed | Complete continuity |
| System-level network observer | Network activity | Original logical lifetime |
| Native registry observation | Session accessibility | Lifetime preservation through transport replacement |
| Application observer | Required transaction behavior | Complete authority integrity |
| Lifetime observer | Original lifetime identity | All application effects |
| Security observer | Protected-operation outcomes | Physical network transition |
| History observer | Relevant history semantics | Network availability |
| Cryptographic verifier | Artifact integrity | Experimental correctness by checksum alone |

An integrated assurance result requires appropriately correlated observations.

No individual observer is automatically sufficient for every qualification claim.

---

## 20. Conventional Transport Comparison

The comparative qualification campaign evaluated conventional transport controls and synthetic application-state models.

### Recorded Control Results

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
| MPTCP complete replacement events | 30 |
| Observed MPTCP token changes | 30 |

### Comparative Scope

| Capability | TCP | UDP-based systems | QUIC | MPTCP | VRP declared contract |
|---|---|---|---|---|---|
| Transport communication | Defined | Defined by applicable stack | Defined | Defined | Required |
| Path migration | Higher-layer dependent | Higher-layer dependent | Supported under protocol conditions | Subflow mechanisms | Qualification objective |
| Application lifetime independent of transport | Possible | Possible | Possible | Possible | Explicit objective |
| Application transaction preservation | Application dependent | Application dependent | Application dependent | Application dependent | Explicit objective |
| Authority integrity | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Explicit objective |
| Canonical history protection | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Explicit objective |

The matrix describes architectural scope and qualification responsibilities.

It does not assert that other systems cannot provide equivalent guarantees.

### Comparative Limitations

- Native QUIC migration was not executed.
- Native MPTCP subflow migration was not evaluated.
- Complete MPTCP replacement is not equivalent to supported subflow migration.
- Synthetic application controls are not native VRP.
- Matched integrated cross-protocol qualification remains incomplete.

```text
UNIVERSAL_COMPARATIVE_SUPERIORITY=NOT_PROVEN
```

---

## 21. Why VRP Is Not Defined Solely by Transport Migration

Transport migration is an important communication capability.

The declared VRP assurance contract addresses a broader relationship:

```text
TRANSPORT TRANSITION
        +
ORIGINAL LOGICAL LIFETIME
        +
APPLICATION TRANSACTION STATE
        +
AUTHORITY INTEGRITY
        +
CANONICAL HISTORY
        +
RECOVERY INTEGRITY
        +
INDEPENDENT EVIDENCE
```

These are distinct verification responsibilities.

A transport protocol may provide connection migration without defining every higher-layer property listed above.

A system built on that transport may additionally implement equivalent application and security guarantees.

The architectural distinction therefore concerns the explicit assurance contract, not an unsupported assertion of exclusive technological capability.

---

## 22. Integrated Native Continuity Acceptance Matrix

The proposed integrated baseline requires the following observations within one attributable execution.

| Acceptance condition | Required target | Latest campaign |
|---|---:|---|
| Original logical-session lifetimes | 1 | Pending |
| Initial transport observation | 1 | Pending |
| Scheduled physical replacements | 30 | Defined target |
| Independently verified physical replacements | 30 | Pending |
| Independent lifetime confirmations | 30/30 | Pending |
| Application transaction confirmations | 30/30 | Pending |
| Unexpected replacement lifetimes | 0 | Pending |
| Relevant unauthorized-operation attempts | Greater than zero | Pending |
| Relevant replay attempts | Greater than zero | Pending |
| Unauthorized accepted protected effects | 0 | Pending |
| Unauthorized duplicate commitments | 0 | Pending |
| Unauthorized history modifications | 0 | Pending |
| Missing mandatory observations | 0 | Pending |
| Evidence integrity | PASS | Pending |

All zero-violation results require actual relevant workloads and attributable observations.

Pending values must not be reported as measured zeros.

---

## 23. Final Native Continuity Target Timeline

```text
ROUND        0       1       2       3      ...      30

TIME         0s      2s      4s      6s     ...      60s

TRANSPORT    T0      T1      T2      T3     ...      T30

LIFETIME     L0      L0      L0      L0     ...      L0

APP STATE    S0      S1      S2      S3     ...      S30

IDENTITY     BASE    MATCH   MATCH   MATCH  ...      MATCH

AUTHORITY    VALID   VALID   VALID   VALID  ...      VALID

HISTORY      VALID   VALID   VALID   VALID  ...      VALID
```

Expected acceptance summary:

```text
VERIFIED_PHYSICAL_REPLACEMENTS=30

ORIGINAL_LOGICAL_LIFETIMES=1

INDEPENDENT_IDENTITY_MATCHES=30

APPLICATION_CONFIRMATIONS=30

UNEXPECTED_LIFETIME_REPLACEMENTS=0

UNAUTHORIZED_PROTECTED_EFFECTS=0

UNAUTHORIZED_DUPLICATE_COMMITS=0

UNAUTHORIZED_HISTORY_MODIFICATIONS=0

MANDATORY_EVIDENCE_COMPLETE=YES
```

This is the target integrated measurement representation.

It is not an actual completed native VRP result.

Every measurement must be established through execution and verification before publication as experimental evidence.

---

## 24. Mandatory Observer Negative Controls

| Negative control | Required qualification decision |
|---|---|
| Replacement lifetime with reused label | REJECT |
| Restored communication with application state reset | REJECT complete continuity |
| Scheduled migration without observed transition | NOT_QUALIFIED |
| Delivery into a replacement logical lifetime | REJECT |
| Incorrect transaction association | REJECT |
| Unauthorized protected effect accepted | FAIL |
| Duplicate unauthorized commitment accepted | FAIL |
| Obsolete authority improperly accepted | FAIL |
| Unauthorized accepted-history modification | FAIL |
| Missing mandatory observation | INCOMPLETE |
| Modified evidence artifact | INVALID_EVIDENCE |
| Contradictory successful qualification | REJECT |

An observer must demonstrate that it can distinguish valid outcomes from invalid successful-looking outcomes.

Positive and negative controls must both be exercised.

---

## 25. Adversarial Continuity Qualification Roadmap

| Fault condition | Proposed test parameter | Latest campaign |
|---|---|---|
| Endpoint churn | Every 2 seconds | NOT_QUALIFIED |
| NAT rebinding | Controlled endpoint change | NOT_TESTED |
| Packet loss | 30% | NOT_TESTED |
| Packet loss | 50% | NOT_TESTED |
| Packet loss | 80% | NOT_TESTED |
| Packet loss | 90% | NOT_TESTED |
| Network blackout | 10 seconds | NOT_TESTED |
| Network blackout | 30 seconds | NOT_TESTED |
| Network blackout | 60 seconds | NOT_TESTED |
| Elevated RTT | 300 milliseconds | NOT_TESTED |
| Elevated RTT | 600 milliseconds | NOT_TESTED |
| Elevated RTT | 900 milliseconds | NOT_TESTED |
| Packet reordering | Controlled variable conditions | NOT_TESTED |
| Packet duplication | Controlled variable conditions | NOT_TESTED |
| Replay during migration | Authorized evaluation workload | NOT_TESTED |
| Stale authority during recovery | Controlled negative workload | NOT_TESTED |
| Concurrent protected operations | Controlled workload | NOT_TESTED |
| Compound network and security faults | Combined workload | NOT_TESTED |

The listed status values refer specifically to the latest comparative campaign.

They do not invalidate separately attributed historical tests.

The workload parameters are proposed test conditions rather than recorded measurements.

---

## 26. Compound-Fault Acceptance Contract

The strongest integrated assurance requires simultaneous evaluation of communication disruption and security-negative conditions.

Conceptual qualification structure:

```text
+-----------------------------------------------------+
|                   FAULT WORKLOAD                    |
|                                                     |
|  Endpoint churn | Loss | Blackout | Replay attempts |
+-----------------------------------------------------+
                         |
                         v
+-----------------------------------------------------+
|                 SYSTEM UNDER TEST                   |
+-----------------------------------------------------+
                         |
                         v
+-----------------------------------------------------+
|               INDEPENDENT OBSERVATIONS              |
|                                                     |
| Transport | Lifetime | Application | Authority      |
| History   | Delivery | Recovery    | Evidence       |
+-----------------------------------------------------+
                         |
                         v
              INTEGRATED QUALIFICATION
```

The diagram represents an evaluation framework.

It does not disclose the native VRP implementation or its defensive mechanisms.

The acceptance result must separately identify security, availability, continuity, and recovery outcomes.

---

## 27. Security and Availability Outcome Matrix

| Identity | Security | Availability | Interpretation |
|---|---|---|---|
| PASS | PASS | PASS | Eligible for integrated qualification |
| PASS | PASS | FAIL | Identity and security maintained; availability failed |
| PASS | FAIL | PASS | Security violation despite continued communication |
| FAIL | PASS | PASS | Communication recovered into an invalid lifetime |
| FAIL | FAIL | PASS | Communication available despite continuity and security failure |
| UNKNOWN | PASS | PASS | Original-lifetime continuity not proven |
| PASS | UNKNOWN | PASS | Security qualification incomplete |

An integrated successful result requires all applicable mandatory properties to satisfy their respective acceptance conditions.

---

## 28. Historical Evidence Attribution Requirements

The historical migration storm, replay storm, blackout observation, baseline continuity, and short-churn qualification records should undergo evidence re-attribution.

| Attribution requirement | Purpose |
|---|---|
| Original experiment record | Establish actual workload |
| Original evidence manifest | Establish artifact integrity |
| Evaluated implementation classification | Distinguish native and reference systems |
| Implementation provenance | Establish tested revision |
| Observation methodology | Establish evidence meaning |
| Lifetime-oracle qualification | Establish identity observation strength |
| Actual transition count | Establish migration workload |
| Protected-effect assertions | Establish security scope |
| Timing boundaries | Establish correct recovery interpretation |
| Disclosure review | Protect proprietary implementation |
| Approved public artifact commitment | Enable external verification |

Historical evidence must not be discarded merely because a later campaign tested different conditions.

Historical evidence must not be promoted without supporting attribution.

---

## 29. Public Evidence Bundle Contract

A complete approved public continuity qualification bundle should identify the applicable mandatory artifacts.

Recommended structure:

```text
VRP-CONTINUITY-EVIDENCE/

  EXPERIMENT_SPECIFICATION.md
  MEASUREMENTS.csv
  VERIFICATION_RESULTS.json
  NEGATIVE_CONTROL_RESULTS.json
  RECOVERY_MEASUREMENTS.csv
  PROVENANCE.json
  LIMITATIONS.md
  SHA256SUMS
```

The bundle should provide:

- Public experiment identity.
- Defined qualification scope.
- Actual observed measurements.
- Explicit observation categories.
- Independent verification results.
- Negative-control outcomes.
- Timing definitions.
- Known limitations.
- Approved cryptographic commitments.

Raw private evidence must not be copied wholesale into a public repository.

---

## 30. Proposed Consolidated Result Schema

The following machine-readable record illustrates the integrated result contract.

It is not an actual successful experiment.

```json
{
  "schema_version": "1.0",
  "record_type": "assurance_schema_example",
  "assurance_id": "PUBLIC-ASSURANCE-ID",
  "evaluation_mode": "AUTHORIZED_NATIVE",
  "execution_status": "NOT_TESTED",
  "observed": {
    "original_logical_lifetimes": null,
    "physical_transport_replacements": null,
    "independent_lifetime_matches": null,
    "application_confirmations": null,
    "unexpected_lifetime_replacements": null,
    "unauthorized_attempts": null,
    "unauthorized_accepted_effects": null,
    "replay_attempts": null,
    "unauthorized_replay_effects": null,
    "duplicate_commits": null,
    "history_integrity_violations": null,
    "missing_mandatory_observations": null
  },
  "verification": {
    "physical_transport_transition": "NOT_TESTED",
    "logical_lifetime_identity": "NOT_TESTED",
    "application_transaction_state": "NOT_TESTED",
    "authority_integrity": "NOT_TESTED",
    "replay_containment": "NOT_TESTED",
    "duplicate_commit_rejection": "NOT_TESTED",
    "canonical_history_integrity": "NOT_TESTED",
    "recovery_integrity": "NOT_TESTED",
    "negative_controls": "NOT_TESTED",
    "evidence_integrity": "NOT_TESTED"
  },
  "overall_status": "NOT_TESTED",
  "independent_reproduction": "NOT_ESTABLISHED",
  "publication_approval": false
}
```

Unavailable measurements remain null.

They must never be replaced with successful zero-violation values before execution.

---

## 31. Cryptographic Commitment Register

| Evidence category | Public commitment status |
|---|---|
| Historical migration evidence | Pending disclosure review |
| Historical replay evidence | Pending disclosure review |
| Historical blackout evidence | Pending disclosure review |
| Native canonical regression evidence | Pending approved artifact generation |
| Native identity observations | Pending approved artifact generation |
| Native failover observations | Pending approved artifact generation |
| Consolidated historical manifest | Private commitment withheld |
| Integrated native continuity bundle | Pending qualification |

No fabricated digest is included.

A public commitment must refer to the exact approved artifact bytes.

Conventional verification of a reviewed public manifest may use:

```bash
sha256sum -c SHA256SUMS
```

The manifest commitment may be calculated using:

```bash
sha256sum SHA256SUMS
```

The expected commitment should be obtained through an appropriately established independent publication boundary.

---

## 32. Public Qualification Release Gate

A complete public integrated continuity assurance result requires the applicable gates to be satisfied.

```text
[ ] Native implementation attributed

[ ] Actual workload executed

[ ] Physical transport transition independently verified

[ ] Original logical lifetime independently established

[ ] Replacement lifetime negative control qualified

[ ] Application transaction state verified

[ ] Required authority integrity verified

[ ] Replay containment verified

[ ] Duplicate-commit containment verified

[ ] Canonical history integrity verified

[ ] Recovery timing boundaries verified

[ ] Relevant adversarial workload qualified

[ ] Mandatory observations complete

[ ] Evidence integrity verified

[ ] Public artifact commitments generated

[ ] Protected Core disclosure review completed

[ ] Publication approved
```

This checklist defines the integrated qualification gate.

It is intentionally not pre-populated with unsupported successful results.

---

## 33. Current Evidence Limitations

| Limitation | Qualification consequence |
|---|---|
| Historical original artifacts not re-inspected for this document | Historical results retain reported classification |
| Native transport and lifetime observations obtained separately | Integrated correlation remains unresolved |
| Same-process reference observation | Not an independent native lifetime oracle |
| Selected test assertions not exhaustively audited | No exhaustive correctness claim |
| Native test campaigns may overlap | No unsupported unique-test totals |
| Additional sequential migration fixture rejected | No completed latest 30-transition native claim |
| Native QUIC workload unavailable | No empirical QUIC conclusion |
| Native MPTCP subflow workload not evaluated | No claim against MPTCP subflow continuity |
| Private evidence commitments withheld | No immediate external verification of private artifacts |
| Production-scale workloads not qualified | No unrestricted production-readiness claim |

These limitations define the permitted interpretation of the current assurance case.

They do not imply that every unqualified property has failed in the implementation.

---

## 34. Independent Researcher Challenge Contract

An independent reviewer may challenge any specific qualification claim.

A useful technical challenge should identify:

1. Public claim identifier.
2. Relevant experiment.
3. Evaluated implementation category.
4. Workload and environment.
5. Declared acceptance condition.
6. Expected observation.
7. Actual observation.
8. Reproduction procedure.
9. Supporting evidence.
10. Known limitations.

A reproducible counterexample must be incorporated into the affected qualification record after attribution.

A claimed guarantee must remain independently challengeable.

No architecture is exempt from experimental scrutiny.

---

## 35. Protected Core Disclosure Boundary

This assurance case intentionally excludes:

- Proprietary VRP source code.
- Native continuity algorithms.
- Native logical identity mechanisms.
- Internal authorization mechanisms.
- Native replay-processing mechanisms.
- Confidential canonical-history protection.
- Internal protocol-state representations.
- Proprietary recovery mechanisms.
- Internal cryptographic construction details.
- Raw native execution traces.
- Internal repository paths and identifiers.
- Confidential binaries and debug information.
- Private infrastructure configuration.
- Credentials, tokens, and cryptographic secrets.
- Unapproved private evidence commitments.
- Details enabling reconstruction of the Protected Core.

The public assurance case defines what must be verified.

It does not disclose how the protected implementation achieves the required behavior.

---

## 36. Consolidated Engineering Verdict

The available engineering record establishes meaningful native implementation progress and provides multiple complementary forms of continuity-related evidence.

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

NATIVE_HISTORY_RECORDS_OBSERVED=210

REFERENCE_APPLICATION_CONTINUITY=30/30

HISTORICAL_MIGRATION_STORM=1000_REPORTED

HISTORICAL_REPLAY_REJECTIONS=9999_REPORTED

HISTORICAL_BLACKOUT=APPROX_41_6_SECONDS_REPORTED

HISTORICAL_BASELINE_CONTINUITY=PASS_REPORTED

HISTORICAL_SHORT_CHURN_CONTINUITY=PASS_REPORTED

HISTORICAL_EVIDENCE_ANCHORS_VERIFIED=12

ORIGINAL_SOURCE_PRESERVATION=PASS_REPORTED

PROTECTED_CORE_MUTATION=NO_REPORTED

LATEST_INTEGRATED_NATIVE_CONTINUITY=NOT_PROVEN

LATEST_INTEGRATED_NATIVE_AUTHORITY_INTEGRITY=NOT_PROVEN

INDEPENDENT_EXTERNAL_NATIVE_REPRODUCTION=NOT_ESTABLISHED

UNIVERSAL_COMPARATIVE_SUPERIORITY=NOT_PROVEN
```

The historical results and current native observations retain their respective qualification boundaries.

The complete integrated assurance case remains subject to additional correlated evidence.

---

## 37. Assurance Case Document Index

The continuity assurance series consists of five complementary public documents.

| Document ID | Document | Responsibility |
|---|---|---|
| VRP-CONT-E001 | [Continuity Evidence Matrix](VRP_CONTINUITY_EVIDENCE_MATRIX.md) | Historical and current evidence classification |
| VRP-CONT-E002 | [Continuity Identity Assurance](VRP_CONTINUITY_IDENTITY_ASSURANCE.md) | Original logical lifetime verification |
| VRP-CONT-E003 | [Migration and Recovery Evidence](VRP_MIGRATION_AND_RECOVERY_EVIDENCE.md) | Transport transitions and recovery |
| VRP-CONT-E004 | [Adversarial Continuity Evidence](VRP_ADVERSARIAL_CONTINUITY_EVIDENCE.md) | Security and continuity qualification |
| VRP-CONT-E005 | Consolidated Continuity Assurance Case | Complete assurance argument and acceptance boundaries |

The wider engineering qualification documentation includes:

- VRP-COMP-001 — Protocol Differentiation.
- VRP-COMP-002 — Engineering Evidence Ledger.
- VRP-COMP-003 — Comparative Qualification Report.
- VRP-COMP-004 — Native Runtime Qualification.
- VRP-COMP-005 — Security and Authority Assurance.
- VRP-COMP-006 — Evidence Integrity Manifest.
- VRP-COMP-007 — Claims and Limitations Register.
- VRP-COMP-008 — Independent Black-Box Validation Contract.
- VRP-COMP-009 — Reproducible Continuity Comparison Suite.
- VRP-COMP-010 — Continuous Qualification and Update Policy.

Together, these documents define the public engineering evaluation framework.

---

## 38. Final Engineering Position

VRP is not defined solely by the availability of an underlying communication path.

Its declared architectural responsibility is preservation of the original logical-session lifetime and its required semantic and security properties across qualified transitions.

The engineering objective is:

```text
THE TRANSPORT MAY CHANGE.

THE NETWORK MAY DISAPPEAR.

THE COMMUNICATION PATH MAY BE REPLACED.

THE ORIGINAL LOGICAL LIFETIME
MUST REMAIN INDEPENDENTLY VERIFIABLE.

THE REQUIRED APPLICATION STATE
MUST REMAIN CONSISTENT.

THE AUTHORITY BOUNDARY
MUST REMAIN ENFORCEABLE.

THE CANONICAL HISTORY
MUST REMAIN PROTECTED.

THE EVIDENCE
MUST REMAIN CHALLENGEABLE.
```

This is the continuity-first assurance contract.

Its guarantees must be established through attributable experimental evidence.

The implementation remains protected.

The engineering claims remain open to independent verification.

The qualification boundaries remain explicit.

---

## 39. Revision History

| Revision | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial consolidated continuity assurance case |

---

# Veil Routing Protocol

**Author: Vitalijus Riabovas**

```text
SESSION != TRANSPORT

CONNECTIVITY != AUTHORITY

RECONNECTION != ORIGINAL LIFETIME

DELIVERY != COMPLETE CONTINUITY

RECOVERY != SECURITY INTEGRITY

HASH MATCH != EXPERIMENTAL PROOF

CONFIDENTIALITY != ABSENCE OF VERIFICATION
```

Continuity-first architecture.

Observable guarantees.

Independent qualification.

Evidence-driven engineering.

Protected intellectual property.

No hype.

Read the specifications.

Examine the evidence.

Challenge the engineering.

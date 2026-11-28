
# Veil Routing Protocol (VRP)

## Continuity Evidence Matrix

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-CONT-E001  
**Revision:** 1.0  
**Classification:** PUBLIC  
**Evidence cutoff:** 2026-11-28  
**Scope:** Historical continuity observations and qualification boundaries

---

## 1. Architectural Foundation

Veil Routing Protocol establishes logical-session continuity as an explicit architectural responsibility.

The fundamental invariant is:

```text
SESSION != TRANSPORT
```

The disappearance, replacement, or recovery of an underlying transport must not automatically determine the lifetime of the logical session.

The engineering objective is preservation of the original logical-session lifetime and its required semantic properties.

This document presents recorded engineering observations, historical qualification results, public reference-model results, and remaining qualification requirements.

No proprietary implementation mechanism is disclosed.

---

## 2. Continuity Property Matrix

| Property | Required observable guarantee |
|---|---|
| Logical lifetime | Original logical session remains identifiable |
| Transport independence | Transport replacement does not automatically replace the logical session |
| Continuity reference | Required continuity reference remains consistent |
| Application state | Previously accepted application state remains preserved |
| Transaction progression | Valid transactions continue according to the declared contract |
| Authority integrity | Unauthorized state changes remain prohibited |
| Replay containment | Replayed operations do not produce unauthorized repeated effects |
| Duplicate containment | Protected operations do not produce unauthorized duplicate commitments |
| Canonical history | Required accepted-history properties remain protected |
| Recovery integrity | Recovery does not silently weaken identity or security guarantees |
| Evidence integrity | Modification of committed evidence is detectable |

These properties define the continuity assurance contract.

Individual qualification results must identify which properties were actually evaluated.

---

## 3. Historical Evidence Classification

| Classification | Meaning |
|---|---|
| NATIVE | Recorded execution of native VRP implementation |
| REFERENCE | Public or synthetic reference-model execution |
| NETWORK | Independent network-related observation |
| HISTORICAL_REPORTED | Earlier reported result awaiting complete evidence attribution |
| VERIFIED | A specified assertion was checked successfully |
| NOT_PROVEN | Available evidence does not establish the specified claim |

Historical reported results must not automatically be promoted into independently verified native implementation guarantees.

---

## 4. Consolidated Historical Evidence

| Experiment | Recorded or reported result | Evidence classification |
|---|---:|---|
| Public replay-storm control | 9,999 rejected | REFERENCE |
| Historical migration storm | 1,000 migrations reported | HISTORICAL_REPORTED |
| Physical network interruption | 41.633 seconds reported outage | NETWORK / HISTORICAL_REPORTED |
| Controlled logical-path transition | Continuity-reference preservation reported | REFERENCE / HISTORICAL_REPORTED |
| Controlled recovery scenario | Session recovery preserved | REFERENCE |
| Baseline continuity qualification | PASS reported | HISTORICAL_REPORTED |
| Short endpoint-churn qualification | PASS reported | HISTORICAL_REPORTED |
| Selected native canonical test campaign | 588 successful executions | NATIVE |
| Native session observation | 30/30 successful lookups | NATIVE |
| Independent native failover flows | 30/30 completed | NATIVE |
| Native failover history observations | 210 records | NATIVE |
| Native UDP socket activity | 3 socket creations observed | NATIVE / NETWORK |
| Distinct observed native local UDP ports | 3 | NATIVE / NETWORK |
| Historical comparative evidence manifests | 12 verified | EVIDENCE INTEGRITY |

These observations belong to different qualification campaigns.

They must not be interpreted as one integrated experiment.

---

## 5. Historical Migration Storm

**Evidence ID:** VRP-CONT-H001

The earlier public engineering record reported:

```text
TRANSPORT_MIGRATIONS=1000

SESSION_IDENTITY_PRESERVATION=REPORTED
```

### Measurement Table

| Parameter | Historical record |
|---|---:|
| Reported transport migrations | 1,000 |
| Reported session identity preservation | Yes |
| Original clean execution evidence independently inspected for this document | No |
| Independent lifetime-oracle qualification re-established | No |
| Physical transport replacement attribution re-established | No |

### Interpretation

The historical result identifies an important continuity qualification target and an earlier reported successful migration campaign.

The original evidence must be re-attributed before the result is promoted into a fully verified native live-network claim.

A historical report is not equivalent to independent inspection of its underlying execution artifacts.

```text
HISTORICAL_MIGRATION_COUNT=1000

HISTORICAL_CONTINUITY_RESULT=REPORTED

CURRENT_EVIDENCE_ATTRIBUTION=PENDING
```

---

## 6. Replay-Storm Evidence

**Evidence ID:** VRP-CONT-H002

A recorded public standalone replay-control experiment produced the following results.

| Measurement | Result |
|---|---:|
| Replay attempts | 9,999 |
| Rejected replay attempts | 9,999 |
| Accepted replay attempts | 0 |
| Replay rejection ratio | 100% |
| Maximum accepted sequence before storm | 1,000 |
| Maximum accepted sequence after storm | 1,000 |
| Subsequent valid sequence | 1,001 |
| Subsequent valid operation | Accepted |

### Observable State Progression

| Stage | Maximum accepted sequence |
|---|---:|
| Before replay storm | 1,000 |
| After 9,999 replay attempts | 1,000 |
| After subsequent valid operation | 1,001 |

### Interpretation

The tested public reference mechanism rejected all recorded replay attempts while preserving its recorded sequence state.

A subsequent valid operation remained acceptable.

This is stronger than observing rejection alone because the experiment also recorded state preservation and subsequent valid progression.

### Qualification Boundary

The result applies to the tested standalone public replay-control model.

It does not independently establish native VRP replay containment during physical endpoint migration or compound network faults.

```text
REPLAY_ATTEMPTS=9999

REPLAY_REJECTED=9999

REPLAY_ACCEPTED=0

REFERENCE_STATE_PRESERVED=YES

SUBSEQUENT_VALID_OPERATION=ACCEPTED

REFERENCE_CONTROL=PASS
```

---

## 7. Physical Network Blackout Observation

**Evidence ID:** VRP-CONT-H003

An earlier engineering record reported an observed physical network interruption lasting:

```text
OBSERVED_OUTAGE_MS=41633
```

Equivalent duration:

```text
41.633 seconds
```

### Observation Matrix

| Property | Historical observation |
|---|---|
| Network reachability interruption | Reported |
| Network reachability restoration | Reported |
| Observed interruption duration | 41.633 seconds |
| Independent canonical lifetime correlation | Not established by this measurement |
| Application transaction preservation | Not established by this measurement |
| Authority preservation during outage | Not established by this measurement |

### Important Distinction

The measured outage duration is not automatically a logical-session recovery duration.

Network reachability restoration and canonical session continuity require separate observations.

```text
NETWORK_OUTAGE_DURATION_MS=41633

NETWORK_RESTORATION=REPORTED

INTEGRATED_SESSION_RECOVERY=NOT_ESTABLISHED_BY_OUTAGE_MEASUREMENT
```

---

## 8. Controlled Logical-Path Transition

**Evidence ID:** VRP-CONT-H004

An earlier controlled logical-path transition scenario evaluated a simulated change between Wi-Fi and mobile communication contexts.

Reported results included:

| Property | Historical result |
|---|---|
| Initial logical path | Wi-Fi |
| Final logical path | Mobile |
| Continuity reference | Reported preserved |
| Duplicate acceptance | Reported absent |
| Evidence verifier exit status | 0 reported |
| Evidence verification | PASS reported |
| Recovery acceptance threshold | 12 seconds |

### Qualification Boundary

The 12-second value represents the reported acceptance threshold.

It must not be interpreted as an independently measured recovery duration.

The scenario evaluated controlled logical-path behavior rather than independently establishing operation across complete physical mobile and Wi-Fi network stacks.

Original evidence attribution remains necessary for stronger native implementation claims.

---

## 9. Historical Recovery State Preservation

**Evidence ID:** VRP-CONT-H005

A recorded public recovery-control scenario evaluated restoration following a simulated runtime failure.

| Evaluated property | Recorded reference result |
|---|---|
| Session identifier | Preserved |
| Authority representation | Preserved |
| Authority epoch | Preserved |
| Recorded history | Preserved |
| History entries | 2 |
| Recovery completed | Yes |

Recorded verdict:

```text
SESSION_RECOVERY_PRESERVED
```

### Interpretation

The tested reference scenario demonstrated preservation of the declared recovery-state properties.

### Limitation

This was a public controlled recovery scenario.

It must not be promoted into proof of production-native runtime recovery under physical network interruption.

---

## 10. Historical Native Continuity Checkpoints

**Evidence ID:** VRP-CONT-H006

Earlier native qualification records reported successful baseline and short-churn continuity checkpoints.

| Qualification checkpoint | Historical status |
|---|---|
| Baseline continuity | PASS reported |
| Short endpoint churn | PASS reported |
| Repeated long-duration endpoint churn | Not established in this record |
| Independent oracle attribution | Requires original evidence review |
| Compound-fault continuity | Not established in this record |

These historical checkpoints remain relevant to the continuity engineering program.

Their original execution artifacts, measurement definitions, implementation attribution, and observer qualifications must be reviewed before assigning stronger public evidence classifications.

The incomplete November comparative campaign does not automatically invalidate earlier results.

Equally, earlier reported results do not automatically satisfy the unresolved requirements of the November comparative campaign.

---

## 11. Native Runtime Evidence

**Evidence ID:** VRP-CONT-N001

The November engineering campaign recorded successful native VRP runtime execution and independent system-level network observation.

| Measurement | Recorded result |
|---|---:|
| Runtime exit status | 0 |
| Approximate runtime duration | 3.016 seconds |
| Network-related observation records | 23 |
| Observed UDP socket creations | 3 |
| Distinct observed local UDP port values | 3 |
| Incomplete observer records | 0 |

### Native Runtime Qualification

```text
NATIVE_RUNTIME_EXECUTION=OBSERVED

ACTUAL_UDP_ACTIVITY=OBSERVED

DISTINCT_LOCAL_UDP_PORT_VALUES=3
```

### Remaining Correlation

The recorded network activity was not independently correlated with one canonical logical-session lifetime.

Distinct port values are evidence of endpoint-related activity.

They are not sufficient evidence of session identity preservation.

---

## 12. Native Canonical Regression Evidence

**Evidence ID:** VRP-CONT-N002

The selected native canonical regression campaign recorded:

| Execution category | Successful executions | Recorded failures |
|---|---:|---:|
| Baseline | 49 | 0 |
| Repeated execution | 490 | 0 |
| Race-detector execution | 49 | 0 |
| Total | 588 | 0 |

Distinct selected tests:

```text
49
```

Successful executions:

```text
588
```

The result establishes successful execution of the selected regression campaign.

Repeated executions are not distinct test cases.

The test-selection categories alone do not independently establish the full semantics of every assertion.

---

## 13. Native Session Observation

**Evidence ID:** VRP-CONT-N003

The native session-observation fixture recorded:

| Property | Result |
|---|---:|
| Runtime initialization | PASS |
| Session registration | PASS |
| Repeated session lookup attempts | 30 |
| Successful session lookups | 30 |
| Observed session cardinality | 1 |
| Selected race-detector qualification | PASS |

### Observable Relationship

```text
INITIAL_SESSION_REGISTRATION
            |
            v
REPEATED_NATIVE_OBSERVATION
            |
            v
30/30 SUCCESSFUL LOOKUPS
            |
            v
OBSERVED_SESSION_CARDINALITY=1
```

### Qualification Boundary

This experiment establishes native registration and repeated registry accessibility.

It does not establish physical transport replacement or independently verify preservation of the original lifetime across such replacement.

---

## 14. Native Failover Repeatability

**Evidence ID:** VRP-CONT-N004

The native failover scenario was executed thirty times.

| Measurement | Recorded result |
|---|---:|
| Independent native failover executions | 30 |
| Completed executions | 30 |
| Recorded execution failures | 0 |
| Minimum history records per flow | 7 |
| Maximum history records per flow | 7 |
| Total observed history records | 210 |
| Observed UDP socket creations | 0 |

### Execution Completion

```text
Completed     [##############################] 30/30

Failed        [                              ]  0/30
```

### Interpretation

The native scenario demonstrated repeatable successful execution and observable history production.

### Limitation

Each flow was independently initialized.

The result must not be interpreted as thirty physical transport migrations within one logical-session lifetime.

The absence of observed UDP socket creation prevents promotion into a physical UDP migration claim.

---

## 15. Application Continuity Reference Controls

**Evidence ID:** VRP-CONT-R001

The comparative qualification campaign evaluated three synthetic application-state models.

| Model | Transport transitions | Successful state continuations |
|---|---:|---:|
| TCP connection-bound | 30 | 0 |
| UDP endpoint-bound | 30 | 0 |
| TCP transport-independent | 30 | 30 |

### Observed State Continuation

```text
TCP connection-bound

[                              ]  0/30


UDP endpoint-bound

[                              ]  0/30


TCP transport-independent

[##############################] 30/30
```

### Interpretation

The tested connection-bound and endpoint-bound models intentionally associate application state with their transport context.

The independent application model intentionally maintains state outside individual TCP connections.

This establishes that a validation methodology can distinguish transport-bound application behavior from independently maintained application state within the tested reference workload.

It also demonstrates why a fair native VRP comparison must evaluate more than reconnection.

---

## 16. Native MPTCP Comparison

**Evidence ID:** VRP-CONT-R002

The native MPTCP complete-connection-replacement experiment recorded:

| Measurement | Result |
|---|---:|
| Native MPTCP connections | 31 |
| Successful payload exchanges | 62 |
| Complete connection replacements | 30 |
| Observed connection-token changes | 30 |
| Connections with observed token stability | 31 |

### Interpretation

The observed native MPTCP connection identifiers changed after complete connection replacement.

This experiment did not evaluate migration between subflows of a surviving MPTCP connection.

Transport-token identity is not application-session lifetime identity.

---

## 17. Comparative Capability Matrix

| Property | TCP control | UDP control | MPTCP replacement | QUIC | VRP declared contract |
|---|---|---|---|---|---|
| Communication | VERIFIED | VERIFIED | VERIFIED | NOT_TESTED | Required |
| Endpoint-related change | OBSERVED | OBSERVED | OBSERVED | NOT_TESTED | Required |
| Native connection migration | Not evaluated | Not applicable | Subflow migration not tested | Standardized capability | Qualified transitions |
| Transport-independent application state | Possible above TCP | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Explicit objective |
| Independent logical lifetime | Not qualified | Not qualified | Not qualified | Not evaluated | Explicit objective |
| Authority integrity | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Explicit objective |
| Canonical history protection | Not evaluated | Not evaluated | Not evaluated | Not evaluated | Explicit objective |

The matrix distinguishes architectural responsibilities and recorded experimental results.

It is not a universal protocol ranking.

---

## 18. Continuity Evidence Strength Matrix

| Evidence property | Current available record |
|---|---|
| Native implementation execution | OBSERVED |
| Native network activity | OBSERVED |
| Native session registration | QUALIFIED |
| Native repeated registry observation | QUALIFIED |
| Native failover repeatability | QUALIFIED |
| Native history availability | QUALIFIED |
| Synthetic transport-independent application continuity | VERIFIED |
| Synthetic replay containment | VERIFIED |
| Synthetic recovery-state preservation | VERIFIED |
| Historical migration storm | REPORTED |
| Historical baseline continuity | PASS REPORTED |
| Historical short churn continuity | PASS REPORTED |
| Integrated live native lifetime identity in latest campaign | NOT_PROVEN |
| Integrated native authority integrity during endpoint replacement | NOT_PROVEN |
| Independent matched comparative superiority | NOT_PROVEN |

This matrix deliberately preserves the difference between historical reports, verified reference models, and native implementation observations.

---

## 19. Evidence Composition Boundary

The following observations are complementary:

```text
NATIVE RUNTIME EXECUTION

NATIVE UDP ACTIVITY

NATIVE SESSION OBSERVATION

NATIVE FAILOVER EXECUTION

REFERENCE STATE CONTINUITY

REFERENCE REPLAY CONTAINMENT

HISTORICAL CONTINUITY RECORDS
```

However, separate experiments cannot be combined into a single successful integrated continuity verdict.

The required integrated evidence must correlate all mandatory observations within the same attributable execution.

```text
COMPONENT EVIDENCE
        !=
INTEGRATED CONTINUITY PROOF
```

---

## 20. Final Integrated Continuity Acceptance Matrix

The proposed native continuity qualification requires:

| Acceptance condition | Target | Current integrated campaign |
|---|---:|---|
| Original logical-session lifetimes | 1 | Pending |
| Independently verified physical replacements | 30 | Pending |
| Independent lifetime confirmations | 30/30 | Pending |
| Application transaction confirmations | 30/30 | Pending |
| Unauthorized accepted protected operations | 0 | Pending |
| Unauthorized duplicate commitments | 0 | Pending |
| Unauthorized canonical-history modifications | 0 | Pending |
| Missing mandatory observations | 0 | Pending |
| Evidence integrity | PASS | Pending |

All zero-violation targets require an executed and observed relevant negative workload.

Pending measurements must not be represented as observed zero violations.

---

## 21. Identity Observation Requirements

The lifetime observer must distinguish:

```text
CASE A

Original lifetime
        |
Transport replacement
        |
Original lifetime preserved

EXPECTED RESULT: ACCEPT
```

from:

```text
CASE B

Original lifetime
        |
Transport replacement
        |
New lifetime with reused label

EXPECTED RESULT: REJECT
```

An observer that accepts both cases is not sufficient for integrated continuity qualification.

This acceptance requirement does not disclose the native VRP identity mechanism.

---

## 22. Evidence Integrity

The November comparative evidence consolidation recorded:

```text
EVIDENCE_ANCHORS_VERIFIED=12

CONSOLIDATION=PASS

EVIDENCE_INTEGRITY=PASS

ORIGINAL_SOURCE_PRESERVATION=PASS

PROTECTED_CORE_MUTATION=NO
```

The underlying artifacts remain within their respective disclosure boundaries.

This document contains no private repository hashes, raw private traces, internal source paths, or confidential implementation artifacts.

Actual public SHA-256 commitments should be added only for explicitly approved evidence artifacts.

A digest verifies committed bytes.

It does not independently establish experimental correctness.

---

## 23. Historical Evidence Upgrade Policy

A reported historical continuity result may be upgraded to a stronger evidence classification when the following conditions are satisfied:

| Required condition | Purpose |
|---|---|
| Original artifact recovered | Establish source evidence |
| Original manifest verified | Establish byte-level integrity |
| Workload attributed | Establish actual tested conditions |
| Implementation attributed | Establish evaluated system |
| Observer qualified | Establish observation validity |
| Measurements verified | Establish recorded outcomes |
| Limitations reviewed | Establish permitted interpretation |
| Public artifact generated | Preserve confidentiality |
| Public commitment generated | Enable integrity verification |

No historical result should be silently discarded.

No historical result should be upgraded without supporting evidence.

---

## 24. Protected Core Boundary

This public evidence matrix excludes:

- Proprietary VRP algorithms.
- Native implementation source code.
- Internal continuity mechanisms.
- Internal authority logic.
- Confidential protocol-state representations.
- Internal cryptographic construction details.
- Raw private traces.
- Internal repository identifiers.
- Private infrastructure configuration.
- Credentials and cryptographic secrets.
- Unapproved private evidence commitments.
- Information enabling reconstruction of the Protected Core.

Public verification must evaluate observable guarantees without requiring implementation disclosure.

---

## 25. Consolidated Continuity Position

The available engineering record establishes native VRP execution, native session observation, repeatable native failover execution, independent UDP activity observation, selected native regression success, and verified public reference behavior.

Earlier qualification records additionally report significant continuity and migration results that remain eligible for stronger evidence attribution.

The integrated native live-network continuity proof requires completion of the remaining correlated observation requirements.

The distinction remains fundamental:

```text
SESSION != TRANSPORT

CONNECTION_RECOVERY != LIFETIME_IDENTITY

REFERENCE_SUCCESS != NATIVE_QUALIFICATION

HISTORICAL_REPORT != INDEPENDENT_REPRODUCTION

COMPONENT_EVIDENCE != INTEGRATED_PROOF
```

The purpose of this matrix is to expose the engineering evidence honestly and precisely.

The objective is independently measurable continuity.

The architecture defines the required guarantees.

The evidence determines the qualification outcome.

---

## 26. Related Documents

- VRP-COMP-001 — Protocol Differentiation.
- VRP-COMP-002 — Engineering Evidence Ledger.
- VRP-COMP-003 — Comparative Qualification Report.
- VRP-COMP-004 — Native Runtime Qualification.
- VRP-COMP-005 — Security and Authority Assurance.
- VRP-COMP-006 — Evidence Integrity Manifest.
- VRP-COMP-007 — Claims and Limitations Register.
- VRP-COMP-008 — Independent Black-Box Validation Contract.

---

## 27. Revision History

| Revision | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial consolidated historical continuity evidence matrix |

---

**Veil Routing Protocol**

**Author: Vitalijus Riabovas**

Continuity-first architecture.

Observable guarantees.

Independent qualification.

Protected intellectual property.

No hype.
Read the specifications.
Examine the evidence.
Challenge the engineering.

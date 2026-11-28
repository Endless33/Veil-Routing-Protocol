
# Veil Routing Protocol (VRP)

## Migration, Transport Replacement and Recovery Evidence

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-CONT-E003  
**Revision:** 1.0  
**Classification:** PUBLIC  
**Evidence cutoff:** 2026-11-28  
**Scope:** Migration, endpoint churn, network interruption and recovery qualification

---

## 1. Executive Position

Veil Routing Protocol defines transport replacement as a condition under which logical-session continuity must be independently evaluated.

The fundamental architectural invariant is:

```text
SESSION != TRANSPORT
```

The objective is not merely to establish a replacement communication channel.

The objective is to preserve the original logical-session lifetime and its required semantic and security properties across qualified communication changes.

This document presents:

- Historical migration observations.
- Native runtime measurements.
- Transport replacement controls.
- Native failover repeatability.
- Network interruption observations.
- Recovery acceptance requirements.
- Independent continuity verification criteria.

The proprietary mechanisms responsible for implementing these properties remain confidential.

---

## 2. Migration Is Not Reconnection

Migration and reconnection must be evaluated according to their observable consequences.

| Property | Reconnection | Qualified logical continuity |
|---|---|---|
| Communication restored | Required | Required for completed recovery |
| Original logical lifetime preserved | Not necessarily | Required |
| Application transaction state preserved | Implementation dependent | Required within declared scope |
| Canonical history protected | Implementation dependent | Required within declared scope |
| Current authority remains valid | Implementation dependent | Independently verified |
| Replacement-session creation detected | Not necessarily | Required |
| Physical transition independently observed | Not necessarily | Required for migration qualification |

This comparison distinguishes qualification objectives.

It does not assert that every existing reconnection implementation lacks application-level continuity.

---

## 3. Logical Lifetime Across Transport Replacement

The declared VRP acceptance model is:

```text
TIME ---------------------------------------------------->

TRANSPORT

    T0          T1          T2          T3
    |           |           |           |
    +-----------+-----------+-----------+

LOGICAL LIFETIME

    L0==================================L0

REQUIRED RESULT

    One original logical lifetime.
    Multiple qualified transport contexts.
```

The logical lifetime is evaluated independently of individual transport resources.

The diagram describes the architectural acceptance condition.

It is not a native implementation trace.

---

## 4. Historical Migration Storm Record

**Evidence ID:** VRP-MIG-H001

Earlier VRP engineering records reported a migration-storm scenario involving 1,000 migrations.

### Historical Measurement Register

| Measurement | Historical record |
|---|---:|
| Reported migrations | 1,000 |
| Session preservation | Reported |
| Original execution manifest re-inspected for this document | No |
| Independent physical transition count re-established | No |
| Independent lifetime-oracle qualification re-established | No |

### Evidence Classification

```text
MIGRATION_STORM_COUNT=1000

CONTINUITY_PRESERVATION=HISTORICALLY_REPORTED

ORIGINAL_EVIDENCE_REATTRIBUTION=PENDING
```

### Interpretation

The historical result represents an important earlier engineering observation.

Its complete original evidence must be re-attributed before publishing a stronger native migration qualification claim.

The historical report must not be discarded solely because a later comparative fixture remained incomplete.

However, it must not be treated as newly verified integrated live-network evidence.

---

## 5. Historical Endpoint-Churn Qualification

**Evidence ID:** VRP-MIG-H002

Earlier native engineering checkpoints reported successful baseline and short-duration endpoint-churn continuity qualification.

| Qualification checkpoint | Historical result |
|---|---|
| Baseline continuity | PASS reported |
| Short-duration endpoint churn | PASS reported |
| Repeated long-duration endpoint churn | Not established by this record |
| Independent canonical lifetime observation | Original evidence review required |
| Integrated authority integrity | Original evidence review required |

The historical record supports continued investigation of native endpoint-churn behavior.

It does not independently establish a completed long-duration migration storm under the latest comparative workload.

---

## 6. Native Runtime Execution Evidence

**Evidence ID:** VRP-MIG-N001

An existing native VRP runtime was executed successfully in a controlled network environment.

### Recorded Measurements

| Measurement | Result |
|---|---:|
| Runtime execution exit status | 0 |
| Approximate execution duration | 3.016 seconds |
| Native implementation execution | OBSERVED |

A separate system-level observation run recorded actual network-related activity.

| Network observation | Recorded count |
|---|---:|
| Network-related records | 23 |
| UDP socket creations | 3 |
| Bind operations | 1 |
| Connect operations | 2 |
| Local socket-address queries | 3 |
| Distinct observed local UDP port values | 3 |
| Incomplete observer records | 0 |

### Observed Network Activity

```text
UDP SOCKET CREATIONS

[###] 3


DISTINCT LOCAL UDP PORT VALUES

[###] 3


INCOMPLETE OBSERVER RECORDS

[   ] 0
```

### Qualification Interpretation

Actual UDP activity was independently observed during native execution.

This establishes that the evaluated runtime exercised real network resources.

### Qualification Boundary

The observations do not independently establish that the three observed local port values represented three sequential transport contexts belonging to one preserved logical session.

The following distinction remains mandatory:

```text
DISTINCT_PORT_VALUES != VERIFIED_MIGRATION_COUNT

UDP_ACTIVITY != INDEPENDENT_LIFETIME_CONTINUITY
```

---

## 7. TCP Transport Replacement Control

**Evidence ID:** VRP-MIG-R001

A controlled local TCP workload evaluated communication across deliberately replaced TCP connections.

| Measurement | Recorded result |
|---|---:|
| Communication rounds | 31 |
| Successful communication rounds | 31 |
| Scheduled connection replacements | 30 |
| Separate TCP connections | 31 |
| Scheduled replacement interval | 2 seconds |

### Communication Result

```text
Successful exchanges

[###############################] 31/31
```

### Interpretation

Communication remained possible across separate TCP connections.

The original TCP connections were deliberately terminated.

The experiment did not establish the absence of application-level continuity above TCP.

---

## 8. UDP Endpoint Replacement Control

**Evidence ID:** VRP-MIG-R002

A controlled local UDP workload evaluated communication across changing local endpoints.

| Measurement | Recorded result |
|---|---:|
| Communication rounds | 31 |
| Successful communication rounds | 31 |
| Scheduled endpoint replacements | 30 |
| Scheduled replacement interval | 2 seconds |

### Communication Result

```text
Successful exchanges

[###############################] 31/31
```

### Interpretation

The tested datagram communication remained operational across local endpoint changes.

Raw UDP does not independently provide application-session lifetime semantics.

Higher-level implementations may establish such semantics.

No native VRP continuity claim is derived from this control alone.

---

## 9. Application-State Continuation Controls

**Evidence ID:** VRP-MIG-R003

Three synthetic application-state models were evaluated under repeated transport changes.

| Reference model | Scheduled transitions | State continuations | Continuation ratio |
|---|---:|---:|---:|
| TCP connection-bound | 30 | 0 | 0% |
| UDP endpoint-bound | 30 | 0 | 0% |
| TCP transport-independent | 30 | 30 | 100% |

### Recorded Continuation Distribution

```text
TCP CONNECTION-BOUND

[                              ]   0%


UDP ENDPOINT-BOUND

[                              ]   0%


TRANSPORT-INDEPENDENT APPLICATION

[##############################] 100%
```

The first two models intentionally bound their application state to transport-related context.

The third maintained application state independently.

### Engineering Significance

Transport-independent application continuity is measurable.

It is not restricted to one underlying network protocol.

This positive control prevents the comparative methodology from incorrectly classifying every replacement connection as a replacement logical session.

### Limitations

- Synthetic reference models.
- Same-process observation.
- Local communication environment.
- No native VRP authority-integrity evaluation.
- No native VRP lifetime-oracle qualification.

---

## 10. Native MPTCP Replacement Evidence

**Evidence ID:** VRP-MIG-R004

The comparative campaign exercised native operating-system Multipath TCP.

### Recorded Native Capability

| Measurement | Result |
|---|---:|
| Native capability-control exchanges | 10 |
| Native MPTCP operation | CONFIRMED |
| TCP fallback during qualified execution | NOT OBSERVED |

### Complete Connection Replacement

| Measurement | Result |
|---|---:|
| Native MPTCP connections | 31 |
| Complete connection replacements | 30 |
| Successful payload exchanges | 62 |
| Observed connection-token changes after replacement | 30 |
| Connections with observed token stability | 31 |

### Interpretation

The recorded MPTCP transport identifiers remained stable within the tested individual connections.

Following complete connection termination and replacement, the observed identifiers changed.

```text
COMPLETE_CONNECTION_REPLACEMENTS=30

OBSERVED_TRANSPORT_TOKEN_CHANGES=30
```

### Qualification Boundary

Native MPTCP subflow migration was not evaluated by this experiment.

An MPTCP connection may survive changes to its underlying subflows.

The experiment must not be used to claim that MPTCP lacks transport continuity or that MPTCP-based applications cannot preserve logical-session state.

---

## 11. QUIC Migration Comparison Boundary

**Evidence ID:** VRP-MIG-R005

QUIC supports connection migration under its defined protocol conditions.

This capability must be recognized in any fair comparative evaluation.

| Property | Current campaign |
|---|---|
| Standardized QUIC migration capability | RECOGNIZED |
| Native QUIC migration experiment | NOT_EXECUTED |
| Matched VRP and QUIC migration workload | NOT_ESTABLISHED |
| Comparative continuity advantage | NOT_PROVEN |

A complete comparison must allow QUIC to exercise its supported migration mechanisms.

The absence of a native QUIC execution result is not evidence of QUIC failure.

Reference:

RFC 9000 — QUIC: A UDP-Based Multiplexed and Secure Transport.

https://www.rfc-editor.org/rfc/rfc9000.html

---

## 12. Historical Network Blackout Observation

**Evidence ID:** VRP-REC-H001

An earlier engineering record reported a physical network interruption lasting approximately 41.6 seconds.

### Historical Observation Register

| Property | Recorded classification |
|---|---|
| Network interruption | HISTORICALLY_REPORTED |
| Approximate interruption duration | 41.6 seconds |
| Network reachability restoration | HISTORICALLY_REPORTED |
| Original logical lifetime independently confirmed | NOT_ESTABLISHED_BY_OUTAGE_MEASUREMENT |
| Application transaction preservation | NOT_ESTABLISHED_BY_OUTAGE_MEASUREMENT |
| Authority integrity throughout interruption | NOT_ESTABLISHED_BY_OUTAGE_MEASUREMENT |

### Conceptual Outage Timeline

```text
NETWORK

AVAILABLE
    |
    v
+----------------------------------+
|      NETWORK INTERRUPTION        |
|      Approx. 41.6 seconds        |
+----------------------------------+
    |
    v
REACHABILITY RESTORATION REPORTED
```

### Critical Qualification Boundary

The reported interruption duration is not automatically a logical-session recovery duration.

The original measurement boundaries require review before reporting a more precise recovery claim.

```text
OUTAGE_DURATION != SESSION_RECOVERY_DURATION

REACHABILITY_RESTORED != ORIGINAL_LIFETIME_VERIFIED
```

---

## 13. Native Failover Repeatability

**Evidence ID:** VRP-REC-N001

Thirty independently initialized native failover flows completed successfully.

### Recorded Measurements

| Measurement | Recorded result |
|---|---:|
| Independent native failover executions | 30 |
| Successful completions | 30 |
| Recorded execution failures | 0 |
| History records per completed flow | 7 |
| Total history records observed | 210 |
| Observed UDP socket creations | 0 |

### Completion Distribution

```text
COMPLETED

[##############################] 30/30


FAILED

[                              ]  0/30
```

### Observed History Distribution

```text
FLOW 01: 7 records
FLOW 02: 7 records
FLOW 03: 7 records

...

FLOW 28: 7 records
FLOW 29: 7 records
FLOW 30: 7 records

TOTAL: 210 records
```

The history-record distribution summarizes the reported experiment.

It does not disclose history contents or native state representations.

### Interpretation

The selected native failover scenario demonstrated repeatable successful execution and observable history production.

### Limitation

Thirty independent failover flows are not thirty physical transport migrations within one logical-session lifetime.

No UDP socket creation was observed during these flows.

Therefore, the result must remain classified as native scenario execution and history availability, rather than physical migration qualification.

---

## 14. Recovery Assurance Layers

Recovery must be evaluated at the correct architectural layer.

| Recovery layer | Required completion observation |
|---|---|
| Network reachability | Communication path becomes available |
| Transport recovery | Required transport communication resumes |
| Application delivery | Required application messages arrive |
| Transaction recovery | Expected application transaction progression resumes |
| Logical lifetime recovery | Original logical lifetime independently confirmed |
| Authority recovery | Required valid authorization independently confirmed |
| Canonical recovery | Required accepted-history properties verified |
| Integrated recovery | All applicable mandatory observations satisfied |

A successful result at one layer does not establish successful recovery at every other layer.

---

## 15. Recovery Classification Matrix

| Network restored | Original lifetime verified | Application state preserved | Authority verified | Classification |
|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Eligible for integrated qualification |
| Yes | Unknown | Yes | Yes | Lifetime continuity not proven |
| Yes | Replacement detected | Yes | Yes | Original-lifetime continuity rejected |
| Yes | Yes | No | Yes | Application continuity failed |
| Yes | Yes | Yes | No | Authority qualification failed |
| Yes | Yes | Unknown | Unknown | Incomplete recovery evidence |
| No | Yes | Not observable | Unknown | Lifetime evidence only |
| No | Unknown | Unknown | Unknown | Recovery incomplete |

The matrix defines evaluation decisions.

It does not represent newly observed native VRP results.

---

## 16. Recovery Timing Model

Recovery timing must distinguish multiple observable events.

```text
t0 = Last verified pre-interruption observation

t1 = Independently observed interruption

t2 = Independently observed network restoration

t3 = Verified application delivery restoration

t4 = Original logical lifetime independently confirmed

t5 = Completion of all required security and state checks
```

Possible measurement categories:

| Metric | Measurement boundary |
|---|---|
| Network interruption duration | t2 - t1 |
| Application restoration delay | t3 - t2 |
| Lifetime confirmation delay | t4 - t2 |
| Complete integrated recovery duration | t5 - t1 |

Each metric must identify its actual start and completion conditions.

An unavailable event timestamp must remain unavailable.

A recovery threshold must not be substituted for an observed recovery duration.

---

## 17. Recovery Timeline Acceptance Target

The following example illustrates the expected integrated recovery behavior.

```text
TIME ------------------------------------------------------>

NETWORK

AVAILABLE | UNAVAILABLE | AVAILABLE
==========|-------------|==============================

TRANSPORT

    T0         NONE                 T1

LOGICAL LIFETIME

    L0                             L0
    |                               |
    +---- independently verified ---+

APPLICATION STATE

    S0                             S1

AUTHORITY

  VALID                           VALID

EXPECTED INTEGRATED VERDICT

  ORIGINAL LIFETIME PRESERVED
```

The line connecting the two lifetime observations represents the required verification relationship.

It does not imply continuous observation during a network blackout.

This diagram is an acceptance model, not an actual runtime trace.

---

## 18. Native Sequential Migration Qualification Attempt

**Evidence ID:** VRP-MIG-N002

The recent comparative qualification attempted to execute thirty additional native migrations within one logical-session lifetime.

### Recorded Results

| Measurement | Result |
|---|---|
| Native initialization in later fixture | PASS |
| Requested additional migrations | 30 |
| Completed additional migrations | 0 |
| First additional migration request | REJECTED |
| Integrated migration qualification | NOT_QUALIFIED |
| Protected Core modification | NO |
| Original source preservation | PASS |

### Interpretation

The experimental fixture did not establish the necessary initialization and authorization preconditions.

The observed rejection was retained.

Its complete root cause was not independently established.

This result does not prove that the native implementation is incapable of migration.

It also does not qualify the attempted migration workload.

---

## 19. Migration and Recovery Evidence Matrix

| Experiment | Recorded evidence | Continuity interpretation |
|---|---|---|
| Historical migration storm | 1,000 migrations reported | Original evidence attribution required |
| Historical baseline continuity | PASS reported | Original evidence attribution required |
| Historical short churn | PASS reported | Original evidence attribution required |
| Historical network blackout | Approx. 41.6 seconds reported | Network interruption observation |
| TCP replacement control | 31 successful rounds | Transport communication |
| UDP endpoint control | 31 successful rounds | Datagram communication |
| Independent application reference model | 30/30 continuations | Reference application continuity |
| Native MPTCP replacement | 30 transport-token changes | Complete connection replacement |
| Native VRP runtime | Successful execution | Native execution observed |
| Native VRP UDP observation | 3 distinct local ports | Network activity observed |
| Native VRP failover flows | 30/30 completed | Scenario repeatability |
| Native VRP history availability | 210 observed records | History availability |
| Additional native migration fixture | 0/30 completed | Fixture not qualified |

The measurements originate from different experiments.

They must not be merged into a single integrated migration result.

---

## 20. Proposed Fault Qualification Matrix

Future native qualification should evaluate the following conditions.

| Workload ID | Fault condition | Proposed test parameter | Status in latest comparative campaign |
|---|---|---|---|
| MIG-01 | Repeated endpoint replacement | 30 transitions | NOT_QUALIFIED |
| MIG-02 | Endpoint churn | Every 2 seconds | NOT_QUALIFIED |
| MIG-03 | NAT rebinding | Controlled endpoint change | NOT_TESTED |
| LOSS-01 | Packet loss | 30% | NOT_TESTED |
| LOSS-02 | Packet loss | 50% | NOT_TESTED |
| LOSS-03 | Packet loss | 80% | NOT_TESTED |
| LOSS-04 | Packet loss | 90% | NOT_TESTED |
| BLACKOUT-01 | Network interruption | 10 seconds | NOT_TESTED |
| BLACKOUT-02 | Network interruption | 30 seconds | NOT_TESTED |
| BLACKOUT-03 | Network interruption | 60 seconds | NOT_TESTED |
| RTT-01 | Elevated latency | 300 milliseconds | NOT_TESTED |
| RTT-02 | Elevated latency | 600 milliseconds | NOT_TESTED |
| RTT-03 | Elevated latency | 900 milliseconds | NOT_TESTED |
| ORDER-01 | Packet reordering | Controlled variable conditions | NOT_TESTED |
| DUP-01 | Packet duplication | Controlled variable conditions | NOT_TESTED |
| COMPOUND-01 | Churn, loss and blackout | Combined workload | NOT_TESTED |
| COMPOUND-02 | Network faults and replay | Combined workload | NOT_TESTED |

The status applies to the latest comparative campaign.

Separately recorded historical experiments retain their original scope.

Configured workload values are not observed measurements.

---

## 21. Single-Session Migration Acceptance Profile

The baseline proposed native qualification workload is:

| Parameter | Required target |
|---|---:|
| Original logical-session lifetimes | 1 |
| Initial transport context | 1 |
| Verified subsequent transport replacements | 30 |
| Scheduled replacement interval | 2 seconds |
| Independent original-lifetime confirmations | 30/30 |
| Required application transaction confirmations | 30/30 |
| Unexpected replacement lifetimes | 0 |
| Unauthorized accepted protected operations | 0 |
| Unauthorized duplicate commitments | 0 |
| Unauthorized canonical-history modifications | 0 |
| Missing mandatory observations | 0 |

The security-related zero targets require relevant executed negative workloads.

A missing or unexecuted security experiment cannot establish a measured zero-violation result.

These are proposed qualification criteria.

They are not completed native measurements.

---

## 22. Proposed Native Migration Timeline

```text
ROUND       0       1       2       3      ...      30

TIME        0s      2s      4s      6s     ...      60s

TRANSPORT   T0      T1      T2      T3     ...      T30

LIFETIME    L0      L0      L0      L0     ...      L0

APP STATE   S0      S1      S2      S3     ...      S30

IDENTITY    BASE    MATCH   MATCH   MATCH  ...      MATCH
```

### Required Result

```text
VERIFIED_PHYSICAL_REPLACEMENTS=30

ORIGINAL_LOGICAL_LIFETIMES=1

INDEPENDENT_IDENTITY_MATCHES=30

APPLICATION_CONFIRMATIONS=30

UNEXPECTED_LIFETIME_REPLACEMENTS=0
```

The timeline represents the intended final acceptance result.

It is not a recorded successful native VRP experiment.

Actual timing, transport transitions, lifetime observations, and application effects must be independently established.

---

## 23. Migration Observer Requirements

The transport observer must distinguish:

- Scheduled migration.
- Attempted migration.
- Observed endpoint-related activity.
- Independently verified physical transport replacement.
- Transport recovery.
- Application communication recovery.

The logical-lifetime observer must distinguish:

- Original lifetime preservation.
- Replacement logical-session creation.
- Reuse of an externally visible identifier.
- Missing identity observations.
- Contradictory identity observations.

The application observer must distinguish:

- Successful message delivery.
- Correct transaction association.
- Required transaction progression.
- Missing transaction effects.
- Unauthorized duplicate effects.

The security observer must verify the applicable protected-operation and accepted-history properties.

No confidential implementation mechanism is required by these public observer definitions.

---

## 24. Mandatory Migration Negative Controls

| Negative control | Required verdict |
|---|---|
| New session created after transport replacement | Continuity rejected |
| External session label reused by a new lifetime | Continuity rejected |
| Endpoint change scheduled but never observed | Migration not verified |
| Communication restored with application state reset | Complete continuity failed |
| Application delivery associated with a replacement session | Continuity rejected |
| Authorization failure produces unauthorized state mutation | Security qualification failed |
| Duplicate protected operation accepted | Duplicate containment failed |
| Missing mandatory post-transition evidence | Qualification incomplete |
| Modified measurement artifact | Evidence integrity failed |
| Contradictory successful result | Semantic verification failed |

A qualified observer must detect invalid outcomes that superficially resemble successful recovery.

Negative controls validate the evaluation methodology.

They do not automatically qualify the native implementation.

---

## 25. Measurement Record Format

Future approved migration evidence should include measurements such as:

| Field | Meaning |
|---|---|
| experiment_id | Public experiment identifier |
| transition_index | Attributable transition number |
| scheduled_time_ns | Requested transition time |
| observed_time_ns | Independently observed transition time |
| physical_replacement_verified | Physical replacement verification |
| original_lifetime_confirmed | Original lifetime verification |
| application_state_confirmed | Application-state verification |
| authority_status | Applicable authority verification |
| history_status | Applicable history verification |
| recovery_duration_ns | Explicitly defined measured duration |
| observation_complete | Mandatory evidence completeness |

The public record must not contain confidential native lifetime values or internal authority representations.

Public aliases and aggregate verification results may be used where sufficient for the declared evaluation scope.

---

## 26. Proposed Machine-Readable Migration Result

The following record illustrates an integrated native migration result schema.

It is not an actual completed experiment.

```json
{
  "schema_version": "1.0",
  "record_type": "schema_example",
  "qualification_type": "native_transport_replacement",
  "evaluation_mode": "AUTHORIZED_NATIVE",
  "execution_status": "NOT_TESTED",
  "target": {
    "original_logical_lifetimes": 1,
    "physical_replacements": 30,
    "scheduled_interval_seconds": 2
  },
  "observed": {
    "physical_replacements": null,
    "original_lifetimes": null,
    "independent_identity_matches": null,
    "application_confirmations": null,
    "unexpected_lifetime_replacements": null,
    "unauthorized_accepted_operations": null,
    "unauthorized_duplicate_commits": null,
    "history_integrity_violations": null,
    "missing_mandatory_observations": null
  },
  "verification": {
    "physical_replacement": "NOT_TESTED",
    "logical_lifetime": "NOT_TESTED",
    "application_state": "NOT_TESTED",
    "authority_integrity": "NOT_TESTED",
    "canonical_history": "NOT_TESTED",
    "negative_controls": "NOT_TESTED",
    "evidence_integrity": "NOT_TESTED"
  },
  "overall_status": "NOT_TESTED"
}
```

The null values prevent unexecuted measurements from appearing as successful zero-violation results.

---

## 27. Public Evidence Artifacts

A complete approved migration qualification bundle should identify the applicable mandatory artifacts.

Recommended structure:

```text
EXPERIMENT_SPECIFICATION.md
MEASUREMENTS.csv
RECOVERY_MEASUREMENTS.csv
VERIFICATION_RESULTS.json
NEGATIVE_CONTROL_RESULTS.json
LIMITATIONS.md
PROVENANCE.json
SHA256SUMS
```

The evidence package should enable evaluation of:

- Workload attribution.
- Physical transition attribution.
- Original lifetime preservation.
- Application-state preservation.
- Security observations.
- Timing definitions.
- Measurement completeness.
- Artifact integrity.

Private execution traces and protected implementation artifacts remain excluded unless explicitly approved under the applicable disclosure policy.

---

## 28. Evidence Integrity Record

The comparative qualification consolidation recorded:

```text
EVIDENCE_ANCHORS_VERIFIED=12

CONSOLIDATION=PASS

EVIDENCE_INTEGRITY=PASS

ORIGINAL_SOURCE_PRESERVATION=PASS

PROTECTED_CORE_MUTATION=NO
```

These are evidence-preservation and integrity results.

They do not independently establish complete migration correctness.

An approved public evidence bundle must be generated from an explicitly reviewed disclosure boundary.

Its SHA-256 commitments must correspond to the actual published artifact bytes.

---

## 29. Comparative Migration Acceptance

A fair comparative evaluation must distinguish the following workloads.

| Workload | TCP | UDP-based system | QUIC | MPTCP | VRP |
|---|---|---|---|---|---|
| Communication after endpoint change | Evaluate applicable mechanism | Evaluate applicable mechanism | Evaluate native migration | Evaluate native subflow behavior | Evaluate native behavior |
| Complete transport replacement | Evaluate | Evaluate | Evaluate separately | Evaluate separately | Evaluate |
| Original application lifetime | Independently verify | Independently verify | Independently verify | Independently verify | Independently verify |
| Transaction-state preservation | Independently verify | Independently verify | Independently verify | Independently verify | Independently verify |
| Authority integrity | Evaluate declared application contract | Evaluate declared application contract | Evaluate declared application contract | Evaluate declared application contract | Evaluate declared VRP contract |
| Canonical-history protection | Evaluate where supported | Evaluate where supported | Evaluate where supported | Evaluate where supported | Evaluate declared VRP contract |

This matrix defines comparative responsibilities.

It does not assign successful or unsuccessful results to unexecuted experiments.

---

## 30. Protected Core Disclosure Boundary

This document intentionally excludes:

- Native migration algorithms.
- Internal continuity-reference mechanisms.
- Proprietary session-lifetime implementation.
- Internal recovery algorithms.
- Confidential authorization mechanisms.
- Native state-machine implementation.
- Protected protocol-state representations.
- Internal cryptographic construction details.
- Raw native execution traces.
- Internal repository paths and identifiers.
- Confidential binaries.
- Private infrastructure configuration.
- Credentials and cryptographic secrets.
- Unapproved private evidence commitments.
- Details enabling reconstruction of the Protected Core.

External qualification evaluates the required behavior.

It does not require disclosure of how that behavior is implemented.

---

## 31. Consolidated Migration and Recovery Verdict

The available engineering record establishes successful native execution, actual UDP activity, repeatable native failover scenarios, observable history production, and conventional transport replacement controls.

Earlier engineering records report additional migration and continuity results.

The original evidence attribution for those historical results remains necessary.

```text
NATIVE_RUNTIME_EXECUTION=OBSERVED

ACTUAL_UDP_ACTIVITY=OBSERVED

NATIVE_FAILOVER_FLOWS=30/30

NATIVE_HISTORY_RECORDS_OBSERVED=210

TCP_COMMUNICATION_ROUNDS=31/31

UDP_COMMUNICATION_ROUNDS=31/31

REFERENCE_APPLICATION_CONTINUITY=30/30

MPTCP_COMPLETE_CONNECTION_REPLACEMENTS=30

HISTORICAL_MIGRATION_STORM=1000_REPORTED

HISTORICAL_BLACKOUT_DURATION=APPROX_41_6_SECONDS_REPORTED

HISTORICAL_BASELINE_CONTINUITY=PASS_REPORTED

HISTORICAL_SHORT_CHURN_CONTINUITY=PASS_REPORTED

LATEST_SEQUENTIAL_NATIVE_MIGRATION_FIXTURE=NOT_QUALIFIED

INTEGRATED_LIVE_LIFETIME_CORRELATION=NOT_PROVEN

MATCHED_COMPARATIVE_ADVANTAGE=NOT_PROVEN
```

The architectural objective remains unchanged.

The next integrated qualification must correlate actual physical transport replacement with original lifetime identity, application transaction state, required authority, canonical-history integrity, and independent verification.

---

## 32. Related Public Documents

- VRP-CONT-E001 — Continuity Evidence Matrix.
- VRP-CONT-E002 — Continuity Identity Assurance.
- VRP-COMP-003 — Comparative Protocol Qualification Report.
- VRP-COMP-004 — Native Runtime Qualification Report.
- VRP-COMP-005 — Security and Authority Assurance.
- VRP-COMP-006 — Evidence Integrity Manifest.
- VRP-COMP-007 — Claims and Limitations Register.
- VRP-COMP-008 — Independent Black-Box Validation Contract.

---

## 33. Revision History

| Revision | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial migration, transport replacement and recovery evidence report |

---

**Veil Routing Protocol**

**Author: Vitalijus Riabovas**

```text
SESSION != TRANSPORT

RECONNECTION != ORIGINAL LIFETIME

ENDPOINT CHANGE != COMPLETE MIGRATION PROOF

NETWORK RECOVERY != CANONICAL RECOVERY

APPLICATION DELIVERY != AUTHORITY INTEGRITY

HISTORICAL REPORT != INDEPENDENT REPRODUCTION
```

The transport may disappear.

The communication path may change.

The network may become unavailable.

The original logical lifetime remains the subject of qualification.

The architecture defines the guarantee.

The evidence determines whether it has been established.

The Protected Core remains confidential.

No hype.
Read the specifications.
Examine the evidence.
Challenge the engineering.

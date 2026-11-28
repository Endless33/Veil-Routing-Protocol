
# Veil Routing Protocol (VRP)

## Comparative Protocol Qualification Report

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-COMP-003  
**Revision:** 1.0  
**Classification:** PUBLIC  
**Evidence cutoff:** 2026-11-28  
**Qualification status:** PARTIAL — INTEGRATED COMPARATIVE VALIDATION PENDING

---

## 1. Executive Summary

Veil Routing Protocol defines a continuity-first architecture centered on the preservation of logical-session identity independently of its underlying transport.

The central architectural distinction is:

```text
SESSION != TRANSPORT
```

This report establishes a comparative engineering framework for evaluating VRP against conventional and modern transport technologies.

The comparison addresses:

- Transport connection identity.
- Logical-session lifetime.
- Physical endpoint replacement.
- Application transaction continuity.
- Canonical history preservation.
- Authority integrity.
- Replay containment.
- Recovery behavior.
- Independent verification.

The objective is not to compare protocol names.

The objective is to compare observable guarantees under explicitly defined operating conditions.

The current qualification campaign provides successful component-level results, transport control measurements, native runtime observations, and documented negative findings.

A complete cross-protocol superiority claim remains unqualified.

---

## 2. Research Question

Modern communication protocols provide increasingly sophisticated mechanisms for maintaining connectivity during network changes.

However, transport continuity and logical-session continuity are not necessarily equivalent.

The principal research question is:

> Can the original logical-session lifetime remain independently identifiable, semantically consistent, and authoritative when its underlying communication environment changes?

This question cannot be answered through throughput measurements, connection survival, packet delivery, or reconnection latency alone.

It requires correlated observations across multiple architectural boundaries.

---

## 3. Evaluation Layers

Comparative qualification distinguishes five evaluation layers.

### Layer 1 — Network Reachability

Determines whether communication endpoints can exchange network traffic.

### Layer 2 — Transport Continuity

Determines whether an existing transport connection survives a qualified network transition.

### Layer 3 — Application Delivery

Determines whether application data reaches the intended receiver with the required delivery semantics.

### Layer 4 — Logical-Session Continuity

Determines whether the original logical-session lifetime remains identifiable and preserves its required application semantics.

### Layer 5 — Authority and History Integrity

Determines whether accepted state transitions remain authorized and whether previously accepted canonical history remains protected.

A result at one layer must not automatically be promoted into a successful result at another layer.

```text
NETWORK_REACHABILITY
    != TRANSPORT_CONTINUITY

TRANSPORT_CONTINUITY
    != APPLICATION_STATE_CONTINUITY

APPLICATION_DELIVERY
    != LOGICAL_LIFETIME_IDENTITY

LOGICAL_IDENTITY
    != AUTHORITY_INTEGRITY
```

VRP declares qualification objectives spanning these layers.

The implementation must demonstrate the relevant guarantees through evidence.

---

## 4. Comparative Protocol Scope

### 4.1 Transmission Control Protocol

TCP defines reliable, ordered byte-stream communication within a transport connection.

Complete TCP connection replacement creates a new transport connection.

An application may independently preserve logical-session state across such replacement.

Consequently, TCP connection termination does not necessarily imply application-session termination.

Reference:

RFC 9293 — Transmission Control Protocol.

https://www.rfc-editor.org/rfc/rfc9293.html

### 4.2 User Datagram Protocol

UDP provides datagram communication without defining a complete application-session lifecycle.

Higher-level systems may implement:

- Session identity.
- Reliable delivery.
- Migration.
- Recovery.
- Replay protection.
- Application-state preservation.

These properties must be attributed to the complete higher-level implementation rather than UDP alone.

Reference:

RFC 768 — User Datagram Protocol.

https://www.rfc-editor.org/rfc/rfc768.html

### 4.3 QUIC

QUIC supports secure multiplexed communication and connection migration.

Its standardized migration mechanisms allow an existing connection to continue across supported address changes, subject to protocol requirements.

QUIC therefore provides genuine transport-level continuity capabilities.

VRP does not dispute these capabilities.

However, a successful QUIC connection migration is not automatically evidence of every higher-level logical-session, application-authority, or canonical-history guarantee defined by the VRP qualification contract.

A QUIC-based system may implement additional application-level mechanisms capable of satisfying equivalent requirements.

Such a system must be evaluated using the same acceptance criteria.

Reference:

RFC 9000 — QUIC: A UDP-Based Multiplexed and Secure Transport.

https://www.rfc-editor.org/rfc/rfc9000.html

### 4.4 Multipath TCP

MPTCP allows one transport connection to operate through multiple TCP subflows.

Subflows may change while the encompassing MPTCP connection remains active.

The preservation of an MPTCP connection across subflow changes must be distinguished from establishing a new MPTCP connection after complete connection termination.

The current experimental campaign evaluated the latter condition.

Reference:

RFC 8684 — TCP Extensions for Multipath Operation with Multiple Addresses.

https://www.rfc-editor.org/rfc/rfc8684.html

### 4.5 Veil Routing Protocol

VRP declares logical-session continuity as an explicit architectural responsibility.

Its public qualification contract includes:

- Logical lifetime identity.
- Transport-independent continuity.
- Continuity-reference preservation.
- Authorized state evolution.
- Replay containment.
- Duplicate-commit rejection.
- Stale-authority rejection.
- Epoch rollback rejection.
- Canonical history protection.
- Recovery integrity.
- Fail-closed behavior.

These properties describe the intended qualification boundary.

Individual implementation claims require supporting evidence.

No confidential implementation mechanism is disclosed by this report.

---

## 5. Architectural Responsibility Matrix

| Property | TCP | UDP | QUIC | MPTCP | VRP declared contract |
|---|---|---|---|---|---|
| Transport communication | Native | Native | Native | Native | Required |
| Reliable ordered communication | Native | Higher-layer dependent | Stream-level | Native | Separately evaluated |
| Native connection migration | Not defined | Not applicable | Supported | Subflow-based | Qualified transitions |
| Multiple transport paths | Not a native connection property | Higher-layer dependent | Extension or implementation dependent | Supported | Evaluated by workload |
| Application lifetime independent of a particular connection | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Explicit objective |
| Application transaction continuity | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Explicit objective |
| Application-level authority integrity | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Explicit objective |
| Canonical application-history protection | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Explicit objective |

The matrix compares architectural responsibilities.

It does not establish that one implementation is universally superior to another.

It also does not deny the security, integrity, or migration mechanisms already provided by established protocols.

---

## 6. Experimental Environment Classification

The recorded comparative experiments were conducted within controlled local engineering environments.

Native implementation experiments were separated from synthetic reference-model experiments.

The campaign included:

- Conventional TCP communication controls.
- Conventional UDP communication controls.
- A synthetic application-session positive control.
- Native operating-system MPTCP experiments.
- Native VRP runtime execution.
- System-level transport observation.
- Selected native VRP test execution.
- Native session observation.
- Native failover scenario execution.
- Evidence integrity verification.

No public Internet deployment qualification is inferred from these experiments.

Private environment details, implementation references, and infrastructure identifiers are excluded from this public report.

---

## 7. Experiment A — TCP Connection Replacement

**Public experiment identifier:** VRP-CMP-A001

### Objective

Observe communication behavior when TCP connections are deliberately replaced.

### Recorded Measurements

| Measurement | Result |
|---|---:|
| Communication rounds | 31 |
| Successful communication rounds | 31 |
| Scheduled connection replacements | 30 |
| Separate TCP connections | 31 |

### Interpretation

The experiment demonstrated successful communication following complete connection replacement.

The original TCP connections were intentionally terminated.

### Limitations

The experiment did not evaluate a complete application-level session continuity system.

It does not establish that TCP-based applications cannot preserve logical-session state.

### Verdict

```text
COMMUNICATION=VERIFIED
CONNECTION_REPLACEMENT=VERIFIED
APPLICATION_LIFETIME_CONTINUITY=NOT_ESTABLISHED
```

---

## 8. Experiment B — UDP Endpoint Replacement

**Public experiment identifier:** VRP-CMP-B001

### Objective

Observe datagram communication across changing local endpoints.

### Recorded Measurements

| Measurement | Result |
|---|---:|
| Communication rounds | 31 |
| Successful communication rounds | 31 |
| Scheduled endpoint replacements | 30 |
| Scheduled replacement interval | 2 seconds |

### Interpretation

Datagram communication remained possible across the tested local endpoint changes.

### Limitations

Raw UDP does not provide an application-session identity oracle.

The experiment did not establish:

- Canonical logical-session lifetime.
- Application authority integrity.
- Canonical history preservation.
- Production NAT traversal.
- Internet-scale network resilience.

### Verdict

```text
DATAGRAM_DELIVERY=VERIFIED
LOCAL_ENDPOINT_REPLACEMENT=VERIFIED
CANONICAL_SESSION_CONTINUITY=NOT_ESTABLISHED
```

---

## 9. Experiment C — Application Continuity Positive Control

**Public experiment identifier:** VRP-CMP-C001

### Objective

Verify that the comparison methodology recognizes application-level continuity when explicitly implemented independently of the transport connection.

### Reference Models

Three controlled state models were evaluated:

1. TCP connection-bound application state.
2. UDP endpoint-bound application state.
3. Application-session state independent of individual TCP connections.

### Recorded Measurements

| Reference model | Scheduled transitions | State continuation |
|---|---:|---:|
| TCP connection-bound model | 30 | 0/30 |
| UDP endpoint-bound model | 30 | 0/30 |
| Transport-independent application model | 30 | 30/30 |

### Interpretation

The first two models intentionally bound application state to transport-related identity.

The third model intentionally maintained application state independently.

All three models were synthetic reference implementations.

The result demonstrates that the experimental methodology can distinguish connection-bound state from independently maintained application state.

### Engineering Significance

A transport-independent application model can preserve application state even when its underlying TCP connection is replaced.

Therefore, the mere existence of application-session continuity is not sufficient to establish VRP superiority.

A complete comparison must evaluate the additional declared guarantees, including authority integrity and canonical history protection.

### Limitations

- Synthetic reference models.
- Same-process observation.
- No native VRP execution.
- No independent authority-integrity qualification.
- No replay qualification within this experiment.

### Verdict

```text
POSITIVE_CONTROL=VERIFIED
NEGATIVE_REFERENCE_MODELS=OBSERVED
APPLICATION_STATE_CONTINUITY=30/30
NATIVE_VRP_EQUIVALENCE=NOT_ESTABLISHED
```

---

## 10. Experiment D — Native MPTCP Capability

**Public experiment identifier:** VRP-CMP-D001

### Objective

Establish that the comparison environment supports actual native MPTCP communication rather than relying on an assumed transport capability.

### Recorded Measurements

| Measurement | Result |
|---|---:|
| Native payload exchanges | 10 |
| Native MPTCP operation | CONFIRMED |
| TCP fallback during qualified execution | NOT OBSERVED |

### Interpretation

Native operating-system MPTCP communication was exercised successfully.

### Limitations

The experiment did not evaluate migration between subflows or preservation of application-session identity.

### Verdict

```text
NATIVE_MPTCP_CAPABILITY=VERIFIED
MPTCP_SUBFLOW_MIGRATION=NOT_TESTED
APPLICATION_SESSION_CONTINUITY=NOT_TESTED
```

---

## 11. Experiment E — Complete MPTCP Connection Replacement

**Public experiment identifier:** VRP-CMP-E001

### Objective

Observe transport-level identity behavior when a complete MPTCP connection is terminated and subsequently replaced.

### Recorded Measurements

| Measurement | Result |
|---|---:|
| Native MPTCP connections | 31 |
| Complete connection replacements | 30 |
| Successful payload exchanges | 62 |
| Connections with observed token stability | 31 |
| Replacement transitions with observed token changes | 30 |

### Interpretation

The observed connection-token values remained stable within the tested individual connections.

Following complete connection replacement, the observed connection-token values changed.

This establishes the measured behavior of transport-level connection identifiers under the tested replacement conditions.

### Limitations

The experiment does not establish that MPTCP lacks continuity.

Specifically:

- Native MPTCP subflow migration was not tested.
- Application-defined logical-session lifetime was not independently observed.
- Transport tokens are not application lifetime identifiers.
- The experiment intentionally terminated complete MPTCP connections.

### Verdict

```text
NATIVE_MPTCP_EXECUTION=VERIFIED
COMPLETE_CONNECTION_REPLACEMENT=VERIFIED
TRANSPORT_TOKEN_CHANGE=30/30
MPTCP_SUBFLOW_CONTINUITY=NOT_TESTED
APPLICATION_LIFETIME_CONTINUITY=NOT_ESTABLISHED
```

---

## 12. Experiment F — QUIC Comparative Qualification

**Public experiment identifier:** VRP-CMP-F001

### Objective

Evaluate QUIC using the common comparative acceptance contract.

### Recorded Status

Native QUIC comparison was not executed in this campaign.

The required native comparison environment was not available during the recorded capability assessment.

### Interpretation

No empirical QUIC continuity measurement is available from this campaign.

The standardized existence of QUIC connection migration is recognized.

### Verdict

```text
QUIC_STANDARDIZED_MIGRATION=RECOGNIZED
NATIVE_QUIC_EXPERIMENT=NOT_EXECUTED
QUIC_COMPARATIVE_RESULT=NOT_AVAILABLE
VRP_SUPERIORITY_OVER_QUIC=NOT_PROVEN
```

An unavailable experimental result must never be treated as a failed competing implementation.

---

## 13. Experiment G — Native VRP Runtime

**Public experiment identifier:** VRP-CMP-G001

### Objective

Establish successful execution of an existing native VRP runtime and independently observe network-related activity.

### Recorded Measurements

| Measurement | Result |
|---|---:|
| Native runtime exit status | 0 |
| Approximate runtime duration | 3.016 seconds |
| Observed UDP socket creations | 3 |
| Distinct observed local UDP port values | 3 |
| Incomplete system-observer records | 0 |

### Interpretation

The native runtime executed successfully.

A separate system-level observer recorded actual UDP socket activity and distinct local port values.

### Limitations

The available observations do not independently establish that each transport-related event belonged to one preserved canonical logical-session lifetime.

The runtime workload was not equivalent in duration or transition count to the TCP, UDP, or MPTCP comparison workloads.

Consequently, these measurements must not be used as a comparative performance benchmark.

### Verdict

```text
NATIVE_RUNTIME_EXECUTION=OBSERVED
ACTUAL_UDP_ACTIVITY=OBSERVED
INDEPENDENT_TRANSPORT_OBSERVATION=AVAILABLE
CANONICAL_LIFETIME_CORRELATION=NOT_PROVEN
MATCHED_WORKLOAD=NOT_ESTABLISHED
```

---

## 14. Experiment H — Native Canonical Test Campaign

**Public experiment identifier:** VRP-CMP-H001

### Objective

Evaluate selected native test coverage associated with canonical session, migration, recovery, and identity-related behavior.

### Recorded Measurements

| Execution category | Successful executions |
|---|---:|
| Initial selected test execution | 49 |
| Repeated execution | 490 |
| Race-detector execution | 49 |
| Total successful executions | 588 |

### Interpretation

Forty-nine selected tests completed the recorded execution campaign successfully.

Repeated execution and race-detector qualification increased confidence within the selected test scope.

### Limitations

- Test selection was not exhaustive.
- Test names alone do not establish assertion semantics.
- Repeated executions are not distinct test cases.
- A successful race-detector run does not prove universal race freedom.
- This campaign does not independently establish integrated live-network continuity.

### Verdict

```text
SELECTED_TESTS=49
SUCCESSFUL_TEST_EXECUTIONS=588
SELECTED_RACE_QUALIFICATION=PASS
EXHAUSTIVE_CORRECTNESS=NOT_PROVEN
```

---

## 15. Experiment I — Native Session Observation

**Public experiment identifier:** VRP-CMP-I001

### Objective

Establish runtime accessibility of native session observation and registration behavior.

### Recorded Measurements

| Measurement | Result |
|---|---|
| Native runtime initialization | PASS |
| Native observation accessibility | PASS |
| Initial session registry | EMPTY |
| Native session registration | PASS |
| Repeated lookup operations | 30/30 |
| Selected race-detector execution | PASS |

### Interpretation

Native session registration and repeated observation were successfully exercised.

### Limitations

Registry accessibility is not an independent lifetime-identity proof.

A logical identifier may be reused without preserving the original session lifetime.

No physical transport replacement was performed within this fixture.

### Verdict

```text
NATIVE_REGISTRATION=QUALIFIED
SESSION_OBSERVATION=QUALIFIED
REPEATED_LOOKUP=30/30
PHYSICAL_TRANSPORT_REPLACEMENT=NOT_TESTED
```

---

## 16. Experiment J — Native Failover Scenario

**Public experiment identifier:** VRP-CMP-J001

### Objective

Evaluate repeatability of a native failover scenario and availability of its recorded session history.

### Recorded Measurements

| Measurement | Result |
|---|---:|
| Independent native failover flows | 30 |
| Successfully completed flows | 30 |
| Minimum observed history records per flow | 7 |
| Maximum observed history records per flow | 7 |
| Total observed history records | 210 |
| Observed UDP socket creations | 0 |

### Interpretation

The tested native failover scenario completed repeatedly and exposed session-history records.

### Limitations

Thirty independent flows are not equivalent to thirty physical transport replacements within one logical session.

The system observer did not record UDP socket creation during the tested flows.

The result establishes scenario execution and history availability, not integrated physical-network continuity.

### Verdict

```text
NATIVE_FAILOVER_FLOWS=30/30
HISTORY_AVAILABILITY=QUALIFIED
HISTORY_RECORDS_OBSERVED=210
PHYSICAL_UDP_REPLACEMENT=NOT_ESTABLISHED
INDEPENDENT_LIFETIME_CONTINUITY=NOT_PROVEN
```

---

## 17. Experiment K — Rejected Sequential Migration Fixtures

**Public experiment identifier:** VRP-CMP-K001

### Objective

Establish repeated migration of one logical session through a dedicated qualification fixture.

### Recorded Results

```text
Requested additional migrations: 30
Completed additional migrations: 0

Integrated migration qualification: NOT_QUALIFIED
```

The experimental fixtures encountered rejected operations and unresolved initialization or authorization preconditions.

The protected implementation was not modified to obtain artificial successful results.

### Interpretation

The qualification fixtures did not establish a valid integrated migration experiment.

A rejected operation is not automatically a confirmed protocol defect.

Likewise, a rejected operation alone is not sufficient evidence of complete authority integrity.

### Verdict

```text
MIGRATION_FIXTURE=NOT_QUALIFIED
PROTOCOL_DEFECT=NOT_ESTABLISHED
AUTHORITY_INTEGRITY=NOT_PROVEN_BY_THIS_EXPERIMENT
INTEGRATED_CONTINUITY=NOT_PROVEN
```

---

## 18. Comparative Results Matrix

| Experiment | Recorded success | Qualified scope |
|---|---|---|
| TCP replacement | 31/31 communication rounds | Transport communication |
| UDP endpoint replacement | 31/31 communication rounds | Datagram communication |
| TCP connection-bound reference model | 0/30 state continuations | Synthetic negative model |
| UDP endpoint-bound reference model | 0/30 state continuations | Synthetic negative model |
| Independent application reference model | 30/30 state continuations | Synthetic application continuity |
| Native MPTCP | 10/10 control exchanges | Native transport capability |
| MPTCP complete replacement | 62/62 payload exchanges | Complete connection replacement |
| QUIC | No execution result | Not evaluated |
| Native VRP runtime | Successful execution | Runtime availability |
| Native VRP canonical tests | 588 successful executions | Selected test campaign |
| Native VRP session lookups | 30/30 | Registry observation |
| Native VRP failover flows | 30/30 | Independent scenario execution |
| Integrated VRP sequential migration | 0 completed | Fixture not qualified |

These results originate from different experimental workloads.

They are not interchangeable performance measurements.

No numerical superiority ratio is calculated.

---

## 19. What the Current Evidence Establishes

The current campaign establishes the following bounded engineering observations:

1. Transport communication can continue across replacement through appropriate reconnection or datagram mechanisms.

2. Application-defined state can be preserved independently of individual transport connections.

3. Native MPTCP communication can be exercised without observed TCP fallback in the tested environment.

4. Complete MPTCP connection replacement changes the observed transport-token values in the recorded experiment.

5. The selected native VRP runtime executes successfully.

6. Actual UDP socket activity is independently observable during the selected native VRP runtime execution.

7. The selected native VRP test campaign completed 588 successful test executions.

8. Native VRP session registration and repeated registry observation were successfully exercised.

9. Thirty independent native VRP failover flows completed and exposed recorded session history.

10. Twelve historical evidence manifests were successfully verified during consolidation.

These conclusions are limited to the recorded experiments.

---

## 20. What the Current Evidence Does Not Establish

The current comparative campaign does not establish:

- Universal absence of continuity in existing protocols.
- Universal VRP superiority over TCP-based systems.
- Universal VRP superiority over UDP-based systems.
- Universal VRP superiority over QUIC-based systems.
- Universal VRP superiority over MPTCP-based systems.
- Thirty physical endpoint replacements within one independently verified VRP logical-session lifetime.
- Complete authority integrity across a matched cross-protocol workload.
- Complete canonical-history integrity across physical transport replacement.
- Production-scale resilience.
- Exhaustive implementation correctness.
- Universal absence of security defects.

These limitations are retained as explicit engineering boundaries.

---

## 21. Final Comparative Acceptance Contract

A complete comparative experiment should evaluate one logical-session lifetime across a predefined sequence of transport changes.

The proposed baseline workload is:

| Parameter | Target |
|---|---:|
| Logical-session lifetimes | 1 |
| Scheduled endpoint replacements | 30 |
| Scheduled replacement interval | 2 seconds |
| Required independent identity confirmations | 30 |
| Required application transaction confirmations | 30 |
| Permitted unauthorized state changes | 0 |
| Permitted undetected duplicate commits | 0 |
| Permitted missing mandatory evidence records | 0 |

The target values are proposed qualification criteria.

They are not completed VRP measurements.

A valid final experiment must establish that:

- The physical transport transition actually occurred.
- The original logical-session lifetime remained identifiable.
- Application transaction state remained consistent with the acceptance contract.
- Unauthorized operations were not accepted.
- Required canonical-history properties remained intact.
- The observations belong to the same execution.
- The evidence can be independently verified.

---

## 22. Independent Identity Oracle Requirements

The identity oracle must be capable of distinguishing:

- Original logical-session survival.
- Creation of a replacement logical session.
- Reuse of an externally visible identifier.
- Transport recovery without application-state recovery.
- Successful delivery into an incorrect session.
- Missing or invalid observation evidence.

The oracle must not accept continuity solely because:

```text
PROCESS_IDENTIFIER_UNCHANGED

SOCKET_IDENTIFIER_UNCHANGED

CONNECTION_RECOVERED

SESSION_LABEL_REUSED

PACKET_DELIVERY_RESUMED

IMPLEMENTATION_REPORTED_SUCCESS
```

A successful negative-control rejection is mandatory before the oracle can be trusted for comparative qualification.

The public contract describes the required verification behavior.

The implementation-specific identity mechanism remains within the protected evaluation boundary.

---

## 23. Fault Qualification Roadmap

The following workloads define planned comparative extensions.

| Fault condition | Proposed test scope |
|---|---|
| Endpoint churn | Replacement every 2 seconds |
| Packet loss | 30%, 50%, 80%, 90% |
| Network blackout | 10, 30, and 60 seconds |
| Elevated RTT | 300–900 milliseconds |
| Packet reordering | Controlled variable conditions |
| Packet duplication | Controlled repeated delivery |
| Replay | Authorized test scenarios |
| Stale authority | Negative authorization scenarios |
| Concurrent operations | Controlled competing operations |
| Compound faults | Combined churn, loss, blackout, and replay |

Each workload requires its own:

- Acceptance criteria.
- Measurement contract.
- Environment attribution.
- Reproduction classification.
- Verification outcome.
- Limitation record.

These workloads must not be described as completed results without matching evidence.

---

## 24. Performance Measurement Principles

Future comparative experiments should record, where applicable:

- Application delivery success ratio.
- Logical-session survival ratio.
- Verified endpoint replacement count.
- Recovery duration.
- Transaction completion duration.
- Duplicate-delivery count.
- Duplicate-commit count.
- Unauthorized acceptance count.
- Canonical identity mismatch count.
- Observation completeness.
- Resource consumption.

Recovery duration must be defined against a specific measurable event.

For example, restoration of network communication and restoration of verified application-session continuity may produce different recovery measurements.

The measurement definition must remain consistent across compared implementations.

---

## 25. Fairness Requirements

A valid comparison shall allow each competing system to exercise its supported capabilities.

Specifically:

- QUIC migration must not be artificially disabled.
- MPTCP subflow recovery must not be replaced exclusively with complete connection termination when evaluating subflow continuity.
- Application-level session preservation must be permitted where it forms part of the evaluated architecture.
- Equivalent application workloads must be used.
- Equivalent fault conditions must be applied where technically possible.
- Security and authorization boundaries must be explicitly defined.
- Unsupported scenarios must be classified as unsupported, not automatically failed.
- Unavailable implementations must be classified as not evaluated.

The comparison shall evaluate complete declared guarantees rather than deliberately weaken competing systems.

---

## 26. Evidence and Reproducibility

Every completed comparative experiment should produce an attributable evidence package.

The proposed public evidence format includes:

```text
EXPERIMENT_SPECIFICATION.md
MEASUREMENTS.csv
VERIFICATION_RESULTS.json
LIMITATIONS.md
SHA256SUMS
```

Additional approved observer records may be included where they do not disclose protected implementation or private operational data.

The evidence package must distinguish:

- Raw measurements.
- Derived measurements.
- Verification results.
- Operator-declared observations.
- Independent observer observations.
- Cryptographic integrity commitments.

Evidence integrity is necessary but not sufficient for experimental correctness.

A SHA-256 digest does not replace independent execution, semantic verification, or provenance authentication.

---

## 27. Public Validation Kit Integration

The public Validation Kit should provide reproducible versions of eligible comparative controls.

Priority additions include:

- TCP connection replacement controls.
- UDP endpoint replacement controls.
- Application-state positive and negative controls.
- Native MPTCP capability verification.
- MPTCP connection replacement controls.
- QUIC migration evaluation contracts.
- Independent identity-oracle negative controls.
- Common measurement schemas.
- Evidence integrity verification.

Native VRP-specific evaluation may require an authorized black-box environment.

Public reference implementations must be explicitly labeled as reference implementations.

They must never be represented as the VRP Protected Core.

---

## 28. Independent Challenge Procedure

External researchers should be able to challenge the following aspects of the comparative qualification:

1. Experimental assumptions.
2. Workload equivalence.
3. Identity-oracle correctness.
4. Negative-control effectiveness.
5. Measurement accuracy.
6. Evidence completeness.
7. Qualification criteria.
8. Interpretation of negative findings.
9. Reproducibility classification.
10. Claimed architectural guarantees.

A successful challenge must be incorporated into subsequent qualification revisions.

Criticism should be resolved through technical evidence rather than unsupported assertions.

Independent evaluation must preserve the Protected Core boundary.

---

## 29. Protected Core Disclosure Boundary

This report intentionally excludes:

- Proprietary source code.
- Internal protocol algorithms.
- Confidential continuity mechanisms.
- Internal authority logic.
- Private protocol-state representations.
- Internal method contracts.
- Private execution traces.
- Internal repository identifiers.
- Private infrastructure configuration.
- Credentials and cryptographic secrets.
- Unapproved private evidence commitments.
- Implementation details enabling reconstruction of the Protected Core.

The comparative methodology is public.

The protected implementation is not.

---

## 30. Evidence Integrity Status

The final consolidation of this comparative campaign recorded:

```text
HISTORICAL_EVIDENCE_ANCHORS_VERIFIED=12

EVIDENCE_CONSOLIDATION=PASS

REPOSITORY_IDENTITY_PRESERVATION=PASS

ORIGINAL_SOURCE_PRESERVATION=PASS

PROTECTED_CORE_MUTATION=NO

NEW_RUNTIME_TESTS_DURING_CONSOLIDATION=0

EVIDENCE_INTEGRITY=PASS

COMPARATIVE_QUALIFICATION=INCOMPLETE
```

Approved evidence commitments will be maintained separately from this report.

The underlying private evidence artifacts are not included in this publication.

No claim of independent public verification of undisclosed artifacts is made.

---

## 31. Final Comparative Verdict

The recorded engineering campaign supports the distinction between transport recovery, application-state preservation, logical-session identity, and authority integrity.

VRP explicitly targets a qualification boundary extending beyond successful transport reconnection.

That architectural distinction is established by its declared public contract.

The available experimental results demonstrate selected native VRP capabilities and preserve the evidence required for further qualification.

However, an integrated matched-workload comparison remains incomplete.

```text
ARCHITECTURAL_DIFFERENTIATION=DECLARED

TRANSPORT_CONTROLS=VERIFIED

APPLICATION_CONTINUITY_POSITIVE_CONTROL=VERIFIED

NATIVE_VRP_RUNTIME=OBSERVED

SELECTED_NATIVE_TEST_EXECUTIONS=588

NATIVE_FAILOVER_SCENARIOS=30/30

INTEGRATED_LIVE_IDENTITY=NOT_PROVEN

MATCHED_COMPARATIVE_QUALIFICATION=INCOMPLETE

UNIVERSAL_SUPERIORITY=NOT_PROVEN
```

Future conclusions must be determined by attributable evidence.

No unsupported superiority claim is required to establish the value of the engineering program.

---

## 32. References

- RFC 768 — User Datagram Protocol.
  https://www.rfc-editor.org/rfc/rfc768.html

- RFC 9293 — Transmission Control Protocol.
  https://www.rfc-editor.org/rfc/rfc9293.html

- RFC 9000 — QUIC: A UDP-Based Multiplexed and Secure Transport.
  https://www.rfc-editor.org/rfc/rfc9000.html

- RFC 8684 — TCP Extensions for Multipath Operation with Multiple Addresses.
  https://www.rfc-editor.org/rfc/rfc8684.html

- VRP Protocol Differentiation and Evidence Position.
  VRP-COMP-001.

- VRP Engineering Evidence Ledger.
  VRP-COMP-002.

---

## 33. Revision History

| Revision | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial comparative qualification report |

---

**Veil Routing Protocol**

**Author: Vitalijus Riabovas**

```text
SESSION != TRANSPORT

RECONNECTION != SESSION IDENTITY

MIGRATION != COMPLETE AUTHORITY PROOF

DELIVERY != CANONICAL HISTORY INTEGRITY

ASSUMPTION != EVIDENCE
```

The transport may change.

The engineering contract must remain measurable.

The evidence must remain verifiable.

The Protected Core must remain protected.

No hype.
Read the specifications.
Examine the evidence.
Challenge the engineering.

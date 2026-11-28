
# Veil Routing Protocol (VRP)

## Protocol Differentiation and Engineering Evidence Position

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-COMP-001  
**Classification:** PUBLIC  
**Status:** Architecture declaration and engineering evidence summary  
**Qualification date:** 2026-11-28

---

## 1. Executive Position

Veil Routing Protocol introduces a continuity-first architecture in which logical session identity is treated as an explicit architectural concern rather than an incidental consequence of transport connectivity.

The governing principle is:

```text
SESSION != TRANSPORT
```

A transport can disappear.

An endpoint can change.

A connection can be replaced.

Packet delivery can be interrupted.

None of these events, by itself, establishes whether the original logical session has survived.

VRP is designed to address this distinction through explicitly declared continuity, authority, integrity, and recovery requirements.

The engineering question is not simply:

> Can communication resume?

The engineering question is:

> Can the same logical session remain authoritative, identifiable, and semantically consistent across changes in its underlying communication environment?

These are distinct qualification objectives.

---

## 2. Architectural Differentiation

VRP must be evaluated according to its declared architectural contract.

It must not be classified solely by:

- Its underlying transport.
- Its packet delivery mechanism.
- Its endpoint migration capability.
- Its encryption layer.
- Its resemblance to an existing VPN.
- Its ability to reconnect.
- Its ability to restore communication.

Transport recovery is a necessary operational capability in many distributed systems.

It is not sufficient evidence of logical session continuity.

The distinction is fundamental to the VRP architecture.

---

## 3. Continuity Is Not Connectivity

The following properties are not interchangeable:

| Property | Meaning |
|---|---|
| Connectivity | Communication is currently possible |
| Delivery | Application data reaches its destination |
| Transport recovery | Communication resumes following interruption |
| Connection migration | An existing transport connection changes its network path |
| Session continuity | The original logical session remains identifiable across the qualified transition |
| Authority integrity | State-changing operations remain subject to valid authorization |
| Canonical history integrity | Previously accepted logical history remains protected |

An implementation may satisfy one property without satisfying another.

A successful reconnection does not automatically demonstrate session continuity.

A preserved process identifier does not demonstrate session continuity.

An unchanged socket descriptor does not demonstrate session continuity.

A reused session identifier does not independently demonstrate preservation of the original session lifetime.

A successfully delivered packet does not independently demonstrate authority integrity.

VRP qualification therefore requires these properties to be evaluated separately and, where applicable, together.

---

## 4. Relationship to Existing Protocols

### 4.1 TCP

TCP provides reliable, ordered byte-stream communication within a transport connection.

Application-level session preservation across separate TCP connections can be implemented above TCP.

Such application-level continuity must not be confused with preservation of the original TCP connection.

Reference:

https://www.rfc-editor.org/rfc/rfc9293.html

### 4.2 UDP

UDP provides datagram communication.

UDP alone does not define a canonical application-session lifetime, application transaction history, or application authority model.

Higher-level protocols may implement these properties above UDP.

Reference:

https://www.rfc-editor.org/rfc/rfc768.html

### 4.3 QUIC

QUIC provides encrypted, multiplexed transport communication and supports connection migration under its defined protocol conditions.

Its connection migration capability is a legitimate continuity mechanism at the transport-connection level.

VRP does not dispute this capability.

The distinction is that VRP declares a broader logical-session qualification objective, including session lifetime identity, canonical history, and authority integrity across qualified transitions.

Whether a particular QUIC-based system provides equivalent higher-level guarantees must be evaluated against that system's complete architecture and observable behavior.

VRP does not claim that QUIC-based applications cannot implement logical-session continuity.

References:

https://www.rfc-editor.org/rfc/rfc9000.html

https://www.rfc-editor.org/rfc/rfc9308.html

### 4.4 Multipath TCP

Multipath TCP supports a transport connection using multiple TCP subflows.

The ability to maintain an MPTCP connection across changes in subflow availability is distinct from preserving an application-defined logical session after complete connection termination.

Both properties are relevant, but they require different tests.

Reference:

https://www.rfc-editor.org/rfc/rfc8684.html

### 4.5 Architectural Comparison

| Capability | TCP | UDP | QUIC | MPTCP | VRP declared objective |
|---|---|---|---|---|---|
| Transport communication | Native | Native | Native | Native | Supported |
| Reliable ordered delivery | Native | Not native | Stream-level | Native | Evaluated separately |
| Network-path migration | Not a native TCP connection property | Higher-layer dependent | Supported | Subflow-based | Qualified transport replacement |
| Application session lifetime independent of a particular connection | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Explicit architectural concern |
| Canonical application history protection | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Explicit qualification objective |
| Logical-session authority integrity | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Higher-layer dependent | Explicit qualification objective |

This table compares architectural responsibilities.

It is not a benchmark ranking, a claim of universal superiority, or proof that equivalent guarantees cannot be implemented by another system.

---

## 5. Declared VRP Invariants

VRP engineering qualification is organized around explicitly declared invariants.

These include:

- Logical session identity preservation.
- Transport-independent session continuity.
- Continuity-reference preservation.
- Replay containment.
- Duplicate-commit rejection.
- Stale-authority rejection.
- Epoch rollback rejection.
- Deterministic authority resolution.
- Canonical history protection.
- Recovery integrity.
- Evidence integrity.
- Fail-closed behavior under invalid conditions.

These invariants define qualification targets.

Their declaration does not automatically establish that every implementation version satisfies every invariant under every operating condition.

Each claim requires attributable evidence.

---

## 6. Engineering Evidence Summary

The comparative engineering qualification series completed on 2026-11-28 produced the following reported observations.

### 6.1 Transport Control Experiments

| Experiment | Recorded observation |
|---|---|
| TCP communication | 31 successful exchange rounds |
| UDP communication | 31 successful exchange rounds |
| Scheduled endpoint replacements | 30 |
| Native MPTCP connection executions | 31 |
| MPTCP payload exchanges | 62 |
| MPTCP token changes following complete connection replacement | 30 |

The MPTCP experiment evaluated complete connection replacement.

It did not evaluate native MPTCP subflow migration.

No claim against MPTCP subflow continuity is derived from these results.

### 6.2 Application-Level Positive Control

A separate controlled application-session experiment demonstrated that application state can survive TCP connection replacement when the application explicitly maintains its session independently of the connection.

Observed continuation:

```text
30/30
```

This positive control is important.

It establishes that the engineering distinction between session lifetime and transport lifetime is measurable and is not exclusive to a particular transport technology.

VRP must therefore be evaluated against its complete declared contract rather than against an artificially limited reconnect-only baseline.

### 6.3 Native VRP Execution

The qualification series recorded:

- Successful execution of an existing native VRP runtime.
- Independently observed UDP socket activity.
- Three distinct observed local UDP port values.
- Successful native session registration.
- Successful repeated session lookup.
- Successful selected race-detector qualification.

These observations establish component-level behavior within the tested scope.

They do not independently establish a correlation between physical endpoint replacement and canonical logical-session identity.

### 6.4 Selected Native Test Qualification

The selected canonical test campaign recorded:

| Execution mode | Successful selected test executions |
|---|---:|
| Initial execution | 49 |
| Repeated execution | 490 |
| Race-detector execution | 49 |
| Total | 588 |

These are successful executions of 49 selected tests, not 588 unique test cases.

The result must not be interpreted as exhaustive protocol coverage.

### 6.5 Native Failover Qualification

Thirty independent native failover flows completed successfully.

Each completed flow exposed seven session-history records through the tested observation interface.

```text
Completed native flows: 30
History records per flow: 7
Total observed history records: 210
Observed UDP socket creations during these flows: 0
```

This experiment establishes successful execution of the tested native failover scenario and availability of its recorded session history.

It does not establish thirty physical endpoint replacements within one logical session.

---

## 7. Negative Results Are Part of the Evidence

VRP engineering qualification does not discard failed experiments.

The comparative campaign identified incomplete integration between the available network runtime and the independent canonical session observer.

Additional migration fixtures encountered rejected operations and unresolved initialization or authorization preconditions.

These results were retained.

The implementation was not modified merely to force the experimental fixtures to pass.

Unsuccessful qualification attempts must remain distinguishable from confirmed implementation defects.

A rejected test operation may indicate:

- An unsupported test contract.
- An invalid initialization condition.
- An authorization failure.
- An invalid state transition.
- A missing observation capability.
- A genuine implementation defect.

Root-cause attribution is required before assigning the final classification.

---

## 8. Current Qualification Status

| Engineering property | Status |
|---|---|
| Native runtime execution | OBSERVED |
| Native session registration | QUALIFIED |
| Repeated session lookup | QUALIFIED |
| Selected race-detector execution | QUALIFIED |
| Selected canonical test campaign | QUALIFIED |
| Native failover flow execution | QUALIFIED |
| Session-history availability | QUALIFIED |
| UDP transport activity | INDEPENDENTLY OBSERVED |
| Single-session repeated physical endpoint replacement | NOT QUALIFIED IN THIS CAMPAIGN |
| Independent canonical lifetime identity across physical replacement | NOT ESTABLISHED IN THIS CAMPAIGN |
| Matched cross-protocol comparative workload | INCOMPLETE |
| Universal comparative superiority | NOT ESTABLISHED |

The architectural contract remains the qualification target.

The evidence determines which implementation claims may be made.

---

## 9. Evidence Integrity

The comparative qualification campaign concluded with verification of twelve historical evidence manifests and creation of a consolidated private evidence report.

The qualification process recorded:

```text
EVIDENCE_ANCHORS_VERIFIED=12
CONSOLIDATION=PASS
REPOSITORY_IDENTITY=PASS
ORIGINAL_SOURCE_PRESERVATION=PASS
PROTECTED_CORE_MUTATION=NO
EVIDENCE_INTEGRITY=PASS
COMPARATIVE_ADVANTAGE=NOT_PROVEN
```

Cryptographic evidence commitments may be published after explicit disclosure approval.

A SHA-256 digest can bind a subsequent disclosure to a particular byte sequence.

A digest alone does not establish:

- Correctness of the experiment.
- Authenticity of the experiment operator.
- Completeness of the underlying evidence.
- Independent reproducibility.
- Truth of the associated engineering claim.

Public evidence commitments must therefore be accompanied by explicit scope, provenance, verification instructions, and limitations.

Private repository identifiers, implementation paths, private artifacts, and internal evidence manifests are excluded from this document.

---

## 10. Independent Evaluation Standard

A complete continuity qualification must correlate the following within the same execution:

1. Establishment of one logical session.
2. Independent observation of its initial lifetime identity.
3. Independently verified physical transport replacement.
4. Observation of the original logical-session identity after replacement.
5. Application delivery and transaction-state verification.
6. Authority integrity verification.
7. Replay and duplicate-operation containment where applicable.
8. Evidence integrity and reproducibility.

The following must not be substituted for an independent identity oracle:

- Process survival.
- Socket survival.
- Connection recovery.
- Reused identifiers.
- Successful packet delivery alone.
- Unverified implementation-generated success markers.

Qualification requires observable behavior attributable to the actual system under test.

---

## 11. Comparative Evaluation Principles

A fair comparison must use equivalent operating conditions wherever technically applicable.

These include:

- Endpoint churn.
- Network interruption.
- Packet loss.
- Latency and jitter.
- Packet reordering.
- Packet duplication.
- Recovery behavior.
- Application workload.
- Authorization conditions.
- Session-lifetime observation.

A competing implementation must be allowed to exercise its native migration and recovery capabilities.

Artificially disabling a competing protocol's supported capabilities is not an acceptable basis for a superiority claim.

Likewise, comparing a fully integrated VRP system against a deliberately incomplete application stack does not establish architectural superiority.

The comparison must measure declared guarantees under a common qualification contract.

---

## 12. Public Validation Kit

The public VRP Validation Kit is intended to evolve alongside the private engineering qualification program.

Its public scope includes:

- Reproducible control experiments.
- Synthetic application workloads.
- Independent observation contracts.
- Qualification criteria.
- Evidence schemas.
- Evidence verification utilities.
- Negative controls.
- Documented limitations.
- Approved aggregate measurements.
- Approved cryptographic evidence commitments.

Public validation components must remain independent of confidential implementation details.

Where direct evaluation of the native VRP implementation requires restricted access, the distinction between public reproduction and authorized black-box evaluation must be clearly documented.

A synthetic reference model must never be represented as the native VRP implementation.

---

## 13. Protected Core Boundary

The VRP Protected Core is outside the scope of public implementation disclosure.

Public evaluation is based on declared contracts and observable behavior.

The following are excluded from public release unless separately and explicitly authorized:

- Proprietary implementation.
- Internal continuity algorithms.
- Internal authority-resolution mechanisms.
- Confidential protocol state.
- Private execution traces.
- Internal source snapshots.
- Private build artifacts.
- Credentials and cryptographic secrets.
- Internal infrastructure configuration.
- Information enabling reconstruction of protected implementation mechanisms.

Independent evaluation does not require unrestricted disclosure of intellectual property.

The objective is to make claims testable without making the Protected Core reconstructible.

---

## 14. Engineering Position

VRP is not defined by the observation that a network connection can recover.

It is defined by a continuity-first architectural contract that distinguishes logical session lifetime from transport lifetime.

The distinction must be measured.

The invariants must be challenged.

The negative results must remain visible.

The evidence must remain attributable.

The claims must remain bounded by what has actually been demonstrated.

```text
SESSION != TRANSPORT

CONNECTIVITY != CONTINUITY

RECOVERY != IDENTITY PROOF

EVIDENCE != MARKETING
```

The objective is not to obtain agreement through architectural terminology.

The objective is to establish verifiable guarantees through engineering qualification.

---

## 15. Final Statement

VRP invites evaluation against its declared architectural contract.

Existing protocols and competing implementations should be evaluated according to their actual capabilities, not simplified representations.

Any implementation that claims equivalent guarantees should be assessed under equivalent qualification conditions.

The evidence, rather than the protocol label, determines the outcome.

No claim of universal protocol superiority is made by this document.

Future qualification results will extend the public evidence ledger and reproducible validation suite after appropriate security and disclosure review.

---

**Veil Routing Protocol**

**Continuity-first architecture.**

**Author: Vitalijus Riabovas**

No hype.  
Read the specifications.  
Examine the evidence.  
Challenge the engineering.

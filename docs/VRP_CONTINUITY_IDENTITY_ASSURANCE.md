
# Veil Routing Protocol (VRP)

## Continuity Identity Assurance

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-CONT-E002  
**Revision:** 1.0  
**Classification:** PUBLIC  
**Evidence cutoff:** 2026-11-28  
**Scope:** Logical lifetime identity and continuity assurance

---

## 1. Executive Position

The fundamental engineering problem addressed by Veil Routing Protocol is not limited to restoring communication after a network interruption.

It is the preservation of the original logical-session lifetime across qualified changes in the underlying communication environment.

The governing architectural invariant is:

```text
SESSION != TRANSPORT
```

A connection can disappear.

An endpoint can change.

A socket can be replaced.

A communication path can become unavailable.

The logical-session lifetime must be evaluated independently of these events.

This document defines the externally observable identity assurance contract, supporting engineering observations, independent verification requirements, and remaining qualification boundaries.

No proprietary implementation mechanism is disclosed.

---

## 2. Identity Is Not Connectivity

The following properties represent distinct engineering responsibilities.

| Property | Meaning |
|---|---|
| Process identity | Identity of an executing operating-system process |
| Socket identity | Identity of a local communication resource |
| Endpoint identity | Network address and associated transport context |
| Connection identity | Identity of an established transport connection |
| Session label | Externally visible session identifier |
| Logical lifetime | Original logical session from establishment to termination |
| Application identity | Identity of the associated application transaction context |
| Authority validity | Permission to perform a protected operation |
| Canonical history | Previously accepted logical operations |

None of the first five properties independently establishes preservation of the original logical lifetime.

An implementation can reuse an externally visible identifier while creating a new logical session.

A credible continuity evaluation must detect this distinction.

---

## 3. Continuity Architecture Contract

The declared VRP architecture distinguishes a logical session from its underlying transport contexts.

Conceptual representation:

```text
              LOGICAL SESSION
              Lifetime: L0
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
    Transport A Transport B Transport C
        |           |           |
     Original    Replaced    Replaced
```

The required invariant is preservation of the original logical lifetime across qualified transitions.

The diagram represents the public architectural contract.

It does not represent confidential VRP implementation structure.

---

## 4. Transport-Bound Versus Continuity-First Behavior

### Transport-Bound Reference Behavior

```text
Time         T0           T1           T2

Transport    A            B            C

Lifetime     L0           L1           L2

Result       Initial      New          New
```

### Continuity-First Acceptance Target

```text
Time         T0           T1           T2

Transport    A            B            C

Lifetime     L0           L0           L0

Result       Initial      Preserved    Preserved
```

The second sequence defines the required externally observable continuity behavior.

It is an acceptance model, not an independently measured native VRP execution trace.

---

## 5. Formal Identity Acceptance Model

For a qualified workload, let:

- L represent the independently observed logical lifetime.
- T represent the independently observed transport context.
- S represent the required application state.
- H represent the applicable accepted-history properties.
- A represent the required authorization validity.

A transport replacement qualifies as logical continuity only when the required observations establish:

```text
T_after != T_before

L_after == L_before
```

Additional integrated assurance requires:

```text
APPLICATION_STATE_VALID

CANONICAL_HISTORY_VALID

AUTHORITY_VALID

MANDATORY_OBSERVATIONS_COMPLETE
```

The notation describes acceptance conditions.

It does not disclose identity generation, state representation, cryptographic construction, or the implementation of continuity.

---

## 6. Identity Preservation Matrix

| Scenario | Transport | Logical lifetime | Required continuity verdict |
|---|---|---|---|
| Initial establishment | A | L0 | BASELINE |
| Valid transport replacement | B | L0 | ACCEPT |
| Subsequent valid replacement | C | L0 | ACCEPT |
| Temporary network interruption | Unavailable | L0 independently confirmed | ACCEPT within defined scope |
| Valid recovery | D | L0 | ACCEPT |
| Replacement logical session | D | L1 | REJECT |
| Reused external session label | D | L1 | REJECT |
| Missing lifetime observation | D | Unknown | INCOMPLETE |
| Missing physical transition evidence | Unknown | L0 | TRANSITION NOT VERIFIED |

The matrix defines expected qualification decisions.

It does not assert that every scenario has already completed native implementation qualification.

---

## 7. Identifier Reuse Is Not Continuity

Consider two scenarios with the same externally visible session label.

### Valid Reference Case

```text
Before transition:

Session label: S
Logical lifetime: L0

After transition:

Session label: S
Logical lifetime: L0

EXPECTED VERDICT: ACCEPT
```

### Invalid Reference Case

```text
Before transition:

Session label: S
Logical lifetime: L0

After transition:

Session label: S
Logical lifetime: L1

EXPECTED VERDICT: REJECT
```

The external label remains unchanged in both scenarios.

Only the first case preserves the original logical lifetime.

A verifier that cannot distinguish these cases is not sufficient for continuity qualification.

---

## 8. False-Positive Continuity Matrix

| Observed behavior | Why it is insufficient |
|---|---|
| Same process remains alive | The process may create a replacement session |
| Same socket remains available | Application state may have been reset |
| Same local address | Logical identity may have changed |
| Same remote address | Logical identity may have changed |
| Same external session label | The label may have been reused |
| Connection restored | The original logical session may no longer exist |
| Application receives data | Delivery may belong to a replacement lifetime |
| History count unchanged | History contents may differ |
| Operation rejected | Protected state may still have changed |
| Implementation reports success | Independent observation may be missing |

These observations may support an assurance case.

They cannot independently substitute for qualified logical-lifetime evidence.

---

## 9. Native Identity Observation Evidence

**Evidence ID:** VRP-CONT-ID-N001

The recorded native session-observation fixture successfully established access to a registered session through the evaluated native observation interface.

### Recorded Measurements

| Measurement | Result |
|---|---:|
| Native runtime initialization | PASS |
| Initial session registration | PASS |
| Repeated lookup attempts | 30 |
| Successful lookup attempts | 30 |
| Observed final registry cardinality | 1 |
| Selected race-detector qualification | PASS |

### Recorded Result

```text
NATIVE_SESSION_REGISTRATION=PASS

REPEATED_SESSION_LOOKUPS=30/30

OBSERVED_SESSION_CARDINALITY=1

SELECTED_RACE_QUALIFICATION=PASS
```

### Interpretation

The selected native implementation successfully established and repeatedly exposed a registered logical session.

This is attributable implementation-level evidence.

### Limitation

No physical transport replacement was performed within this fixture.

Repeated registry accessibility does not independently establish preservation of the original logical lifetime across transport replacement.

---

## 10. Native Runtime and Transport Evidence

**Evidence ID:** VRP-CONT-ID-N002

An existing native VRP runtime was executed within a controlled network environment.

System-level observation recorded actual UDP socket activity.

### Recorded Measurements

| Measurement | Result |
|---|---:|
| Native runtime exit status | 0 |
| Approximate execution duration | 3.016 seconds |
| System-level observation records | 23 |
| UDP socket creations | 3 |
| Distinct observed local UDP port values | 3 |
| Incomplete observer records | 0 |

### Recorded Result

```text
NATIVE_RUNTIME_EXECUTION=OBSERVED

ACTUAL_UDP_ACTIVITY=OBSERVED

DISTINCT_LOCAL_UDP_PORT_VALUES=3

INCOMPLETE_OBSERVER_RECORDS=0
```

### Interpretation

The evaluated native implementation performed actual network-related operations.

The transport observations were not based solely on implementation-generated success statements.

### Limitation

The available observations do not independently establish that all relevant transport events belonged to the same original logical lifetime.

---

## 11. Native Failover and History Evidence

**Evidence ID:** VRP-CONT-ID-N003

Thirty independent native failover flows were executed.

### Recorded Measurements

| Measurement | Result |
|---|---:|
| Native failover executions | 30 |
| Successful completions | 30 |
| Recorded execution failures | 0 |
| History records per completed flow | 7 |
| Total observed history records | 210 |
| Observed UDP socket creations | 0 |

### Repeatability Representation

```text
Native failover completion

[##############################] 30/30


History availability

[##############################] 30/30
```

### Interpretation

The native scenario demonstrated repeatable successful execution and observable history production.

### Limitation

Each flow was independently initialized.

The result does not establish thirty migrations of one original logical session.

History availability does not independently establish complete canonical-history integrity.

---

## 12. Native Regression Evidence

**Evidence ID:** VRP-CONT-ID-N004

The selected canonical regression campaign recorded successful baseline, repeated, and race-detector executions.

| Qualification category | Successful executions | Recorded failures |
|---|---:|---:|
| Baseline execution | 49 | 0 |
| Repeated execution | 490 | 0 |
| Race-detector execution | 49 | 0 |
| Total | 588 | 0 |

Distinct selected tests:

```text
49
```

Total successful executions:

```text
588
```

### Evidence Boundary

These results provide implementation-level confidence within the selected regression scope.

They do not independently establish the full semantic coverage of every selected assertion.

They are not equivalent to 588 distinct continuity scenarios.

---

## 13. Historical Continuity Evidence

Earlier VRP engineering records reported successful continuity-related qualification checkpoints.

| Historical qualification record | Reported status |
|---|---|
| Baseline continuity | PASS reported |
| Short endpoint churn | PASS reported |
| Migration storm | 1,000 migrations reported |
| Continuity-reference preservation | Preserved as reported |
| Independent evidence verification | PASS reported in earlier evaluation records |

These historical records remain relevant.

However, their complete underlying artifacts were not independently re-inspected for this document.

The historical results therefore retain the classification:

```text
HISTORICAL_RESULT=REPORTED

ORIGINAL_EVIDENCE_REATTRIBUTION=PENDING
```

The incomplete recent comparative campaign does not automatically invalidate these historical results.

Their applicability must be established through original evidence attribution.

---

## 14. Reference Identity Controls

**Evidence ID:** VRP-CONT-ID-R001

The comparative qualification campaign evaluated three controlled application-state models using actual local TCP and UDP communication.

### Recorded Measurements

| Reference model | Scheduled transitions | State continuation |
|---|---:|---:|
| TCP connection-bound | 30 | 0/30 |
| UDP endpoint-bound | 30 | 0/30 |
| Transport-independent application model | 30 | 30/30 |

### Result Visualization

```text
TCP CONNECTION-BOUND

Continuations:

[                              ]  0/30


UDP ENDPOINT-BOUND

Continuations:

[                              ]  0/30


TRANSPORT-INDEPENDENT APPLICATION

Continuations:

[##############################] 30/30
```

### Interpretation

The reference experiment establishes that application state can be preserved independently of individual transport connections.

The transport-bound negative models intentionally reset state according to their defined behavior.

The independent application model intentionally maintains state separately from transport connection lifetime.

These are synthetic reference models.

They are not native VRP execution.

---

## 15. Reference Continuation Timeline

The following table illustrates the expected observable state progression of the public independent application model.

| Round | Transport context | Reference lifetime | Application sequence | Expected result |
|---:|---|---|---:|---|
| 0 | A | L0 | 1 | BASELINE |
| 1 | B | L0 | 2 | CONTINUED |
| 2 | C | L0 | 3 | CONTINUED |
| 3 | D | L0 | 4 | CONTINUED |
| 10 | K | L0 | 11 | CONTINUED |
| 20 | U | L0 | 21 | CONTINUED |
| 30 | AE | L0 | 31 | CONTINUED |

The transport and lifetime labels are illustrative aliases.

The table describes expected reference-model semantics.

It is not a raw native VRP execution trace.

The associated historical reference experiment recorded 30 successful continuations across 30 transitions.

---

## 16. Independent Identity Oracle

The independent lifetime oracle is responsible for determining whether the original logical session survived a qualified transition.

It must not rely exclusively on:

- Process identity.
- Socket identity.
- Network location.
- External session labels.
- Reconnection success.
- Implementation-generated success declarations.

The oracle must establish a trustworthy relationship between its observations and the evaluated logical-session lifetime.

The native identity mechanism and its protected implementation remain confidential.

---

## 17. Oracle Qualification Matrix

| Control | Required observer decision |
|---|---|
| Original lifetime preserved | ACCEPT |
| Original lifetime preserved across transport replacement | ACCEPT |
| Replacement lifetime with new label | REJECT |
| Replacement lifetime with reused label | REJECT |
| Application sequence reset | REJECT complete continuation |
| Incorrect transaction association | REJECT |
| Missing lifetime evidence | INCOMPLETE |
| Contradictory identity evidence | REJECT |
| Missing physical replacement evidence | TRANSITION NOT VERIFIED |
| Invalid evidence integrity | INVALID EVIDENCE |

All applicable controls must be qualified before the observer is relied upon for final native continuity acceptance.

These are qualification requirements, not newly executed native test results.

---

## 18. Multi-Observer Assurance Contract

A credible integrated experiment requires correlated observations.

```text
           INDEPENDENT EVALUATOR
                     |
        +------------+------------+
        |            |            |
        v            v            v
   Transport      Lifetime     Application
    Observer      Observer      Observer
        |            |            |
        +------------+------------+
                     |
                     v
            Qualification Decision
```

Security-sensitive workloads additionally require evidence of the relevant authority and canonical-history properties.

The conceptual roles are public.

Their depiction does not reveal the architecture of the native VRP implementation.

---

## 19. Observation Responsibility Matrix

| Observer | Required evidence | Cannot independently establish |
|---|---|---|
| Transport observer | Actual transport transition | Logical lifetime |
| Lifetime observer | Original lifetime preservation | Application delivery |
| Application observer | Transaction effects and progression | Complete authority validity |
| Authority observer | Valid and invalid protected-operation outcomes | Physical transport replacement |
| History observer | Relevant accepted-history properties | Network availability |
| Evidence verifier | Artifact integrity and consistency | Experimental authenticity by checksum alone |

The required observations must belong to the same attributable execution.

Separate successful experiments must remain separately classified.

---

## 20. Native Migration Fixture Findings

The recent comparative qualification attempted to execute thirty additional migrations within one logical-session lifetime.

### Recorded Outcome

| Property | Result |
|---|---|
| Native initialization | PASS in the later fixture |
| Requested additional migrations | 30 |
| Completed additional migrations | 0 |
| First additional migration | REJECTED |
| Integrated migration qualification | NOT_QUALIFIED |
| Protected Core modification | NO |

### Interpretation

The attempted fixture did not establish the necessary native operation preconditions.

The observed rejection was retained as engineering evidence.

Its root cause was not fully established.

The result is neither proof of a protocol defect nor proof of successful sequential continuity.

No architectural invariant was weakened to force acceptance.

---

## 21. Identity Assurance Evidence Ladder

| Level | Requirement | Current documented evidence |
|---|---|---|
| ID-L1 | Native runtime executes | OBSERVED |
| ID-L2 | Native session registration succeeds | QUALIFIED |
| ID-L3 | Native session remains observable in tested registry workload | QUALIFIED |
| ID-L4 | Native transport activity independently observed | OBSERVED separately |
| ID-L5 | Original lifetime independently identified across physical replacement | NOT_PROVEN in latest campaign |
| ID-L6 | Application state correlated with original lifetime | NOT_PROVEN in latest campaign |
| ID-L7 | Authority and history integrity correlated with continuity | NOT_PROVEN in latest campaign |
| ID-L8 | Independent external native reproduction | NOT_ESTABLISHED in latest campaign |

This is a proposed identity-assurance framework.

The levels do not represent certification grades or a percentage of product readiness.

Separate evidence at lower levels must not be interpreted as automatic completion of higher levels.

---

## 22. Integrated Native Continuity Acceptance Target

The proposed final baseline workload evaluates thirty physical transport replacements within one logical-session lifetime.

| Measurement | Required target |
|---|---:|
| Logical-session lifetimes | 1 |
| Initial lifetime baseline | 1 |
| Scheduled physical replacements | 30 |
| Independently verified physical replacements | 30 |
| Independent original-lifetime confirmations | 30/30 |
| Application transaction confirmations | 30/30 |
| Accepted replacement lifetimes | 0 |
| Unauthorized accepted protected operations | 0 |
| Unauthorized duplicate commitments | 0 |
| Unauthorized history modifications | 0 |
| Missing mandatory observations | 0 |

The zero-violation targets require executed, attributable negative workloads.

They must not be inferred from missing measurements.

These are proposed acceptance conditions, not completed native results.

---

## 23. Target Native Identity Timeline

The following diagram illustrates the expected final qualification result.

```text
TIME         0s      2s      4s           ...      60s

TRANSPORT    T0      T1      T2           ...      T30

LIFETIME     L0      L0      L0           ...      L0

APP STATE    S0      S1      S2           ...      S30

IDENTITY     BASE    MATCH   MATCH        ...      MATCH
```

Required outcome:

```text
PHYSICAL_TRANSPORT_REPLACEMENTS=30

ORIGINAL_LOGICAL_LIFETIMES=1

INDEPENDENT_IDENTITY_MATCHES=30

REPLACEMENT_LIFETIMES_ACCEPTED=0
```

This is the target measurement representation.

It is not a recorded successful native VRP result.

Actual execution must independently establish every reported measurement.

---

## 24. Continuity Under Network Interruption

A network interruption may temporarily prevent communication.

It must not automatically be classified as logical-session termination.

Conceptual acceptance model:

```text
Before interruption:

Transport available
Logical lifetime L0

During interruption:

Transport unavailable
Logical lifetime subject to verification

After recovery:

Transport available
Logical lifetime L0 independently confirmed
```

The absence of communication during an outage is not proof of lifetime preservation.

The original logical lifetime must be independently confirmed according to the applicable observation contract.

---

## 25. Recovery Decision Matrix

| Transport recovered | Original lifetime verified | Application state valid | Continuity decision |
|---|---|---|---|
| Yes | Yes | Yes | Eligible for qualification |
| Yes | No | Yes | NOT_PROVEN |
| Yes | Replacement detected | Yes | REJECT |
| Yes | Yes | No | INCOMPLETE |
| Yes | Unknown | Unknown | NOT_PROVEN |
| No | Yes | Not observable | Identity evidence only |
| No | Unknown | Unknown | INCOMPLETE |

Additional authority and canonical-history requirements apply where included in the qualification scope.

A recovery claim must explicitly identify which guarantees were established.

---

## 26. Security and Lifetime Relationship

Preservation of a logical lifetime must not be interpreted as unlimited authorization.

A complete continuity assurance case distinguishes:

```text
SAME_LOGICAL_LIFETIME

VALID_APPLICATION_STATE

VALID_CURRENT_AUTHORITY

PROTECTED_CANONICAL_HISTORY
```

Each property requires appropriate verification.

A preserved lifetime with unauthorized accepted state changes is not a complete successful security-continuity result.

Conversely, rejection of an invalid operation does not independently establish preservation of the original logical lifetime.

---

## 27. Identity Evidence Record Format

Future approved native identity evidence should expose only the information required for external verification.

Illustrative schema:

```json
{
  "schema_version": "1.0",
  "record_type": "identity_schema_example",
  "experiment_id": "PUBLIC-EXPERIMENT-ID",
  "execution_status": "NOT_TESTED",
  "evaluation_mode": "AUTHORIZED_NATIVE",
  "observed": {
    "physical_replacements": null,
    "original_lifetimes": null,
    "independent_identity_matches": null,
    "replacement_lifetimes_accepted": null,
    "application_confirmations": null,
    "missing_observations": null
  },
  "verification": {
    "physical_transition": "NOT_TESTED",
    "logical_lifetime": "NOT_TESTED",
    "application_state": "NOT_TESTED",
    "authority_integrity": "NOT_TESTED",
    "canonical_history": "NOT_TESTED",
    "negative_controls": "NOT_TESTED"
  },
  "overall_status": "NOT_TESTED"
}
```

The schema does not expose native identity values.

It describes approved aggregate observation categories.

The example is not an experimental result.

---

## 28. Evidence Integrity and Provenance

The recent comparative evidence consolidation recorded:

```text
HISTORICAL_EVIDENCE_ANCHORS_VERIFIED=12

CONSOLIDATION=PASS

EVIDENCE_INTEGRITY=PASS

ORIGINAL_SOURCE_PRESERVATION=PASS

PROTECTED_CORE_MUTATION=NO
```

These results establish the reported evidence-preservation outcome.

They do not independently establish native logical-lifetime preservation.

An approved public identity evidence package should provide:

- Public experiment identifier.
- Defined workload.
- Attributable identity observations.
- Transport observation summary.
- Application observation summary.
- Verification results.
- Explicit limitations.
- Approved SHA-256 commitments.

Cryptographic integrity and semantic identity verification remain separate requirements.

---

## 29. Current Consolidated Identity Verdict

| Engineering property | Classification |
|---|---|
| Session and transport separation | DECLARED ARCHITECTURAL CONTRACT |
| Native implementation execution | OBSERVED |
| Native session registration | QUALIFIED |
| Repeated native registry observation | 30/30 QUALIFIED |
| Native failover repeatability | 30/30 QUALIFIED |
| Native history availability | QUALIFIED |
| Native UDP activity | INDEPENDENTLY OBSERVED |
| Selected canonical regression execution | 588 SUCCESSFUL EXECUTIONS |
| Public reference application continuity | 30/30 VERIFIED |
| Historical baseline continuity | PASS REPORTED |
| Historical short churn continuity | PASS REPORTED |
| Historical migration storm | 1,000 REPORTED |
| Integrated native lifetime preservation in latest comparative campaign | NOT_PROVEN |
| Independent matched-workload comparison | INCOMPLETE |

The matrix presents the current available assurance record.

It does not silently convert reference results or historical reports into newly verified native implementation guarantees.

---

## 30. Independent Researcher Acceptance Questions

An independent reviewer should be able to ask:

1. Was the original logical lifetime independently established?

2. Did the physical transport transition actually occur?

3. Was the original lifetime observed after the transition?

4. Could the observer distinguish a replacement session?

5. Was external identifier reuse tested as a negative control?

6. Was application transaction state preserved?

7. Were the relevant security properties independently evaluated?

8. Did all mandatory observations belong to the same execution?

9. Were the evidence artifacts complete and integrity-verified?

10. Were the limitations explicitly recorded?

A complete continuity qualification must address the applicable questions through attributable evidence.

---

## 31. Protected Core Boundary

This assurance document intentionally excludes:

- Native identity-generation mechanisms.
- Proprietary continuity algorithms.
- Internal authorization mechanisms.
- Confidential protocol-state structures.
- Internal lifecycle-management implementation.
- Private cryptographic construction details.
- Raw native identity values.
- Private execution traces.
- Internal repository paths and identifiers.
- Confidential build artifacts.
- Infrastructure configuration.
- Credentials and cryptographic secrets.
- Unapproved private evidence commitments.
- Details enabling reconstruction of the Protected Core.

The acceptance contract is public.

The implementation mechanism is protected.

---

## 32. Final Identity Assurance Position

The objective of VRP is not merely to restore a communication channel.

It is to preserve the original logical-session lifetime and its required semantic and security properties across qualified transport transitions.

The available evidence establishes meaningful native implementation observations, repeatable native scenarios, selected regression success, and reproducible reference continuity principles.

Historical continuity results remain relevant and eligible for stronger evidence attribution.

The latest integrated comparative campaign retains unresolved independent lifetime-correlation requirements.

The engineering contract remains unchanged.

```text
SESSION != TRANSPORT

SESSION LABEL != LOGICAL LIFETIME

CONNECTION RECOVERY != IDENTITY PRESERVATION

APPLICATION DELIVERY != COMPLETE CONTINUITY

IDENTITY PRESERVATION != UNRESTRICTED AUTHORITY

COMPONENT SUCCESS != INTEGRATED PROOF
```

The logical lifetime must be independently identifiable.

The transport transition must be observable.

The application state must be verifiable.

The authority boundary must remain enforceable.

The evidence must remain attributable.

The Protected Core must remain confidential.

---

## 33. Related Documents

- VRP-CONT-E001 — Continuity Evidence Matrix.
- VRP-COMP-001 — Protocol Differentiation.
- VRP-COMP-002 — Engineering Evidence Ledger.
- VRP-COMP-004 — Native Runtime Qualification Report.
- VRP-COMP-005 — Security and Authority Assurance.
- VRP-COMP-006 — Evidence Integrity Manifest.
- VRP-COMP-007 — Claims and Limitations Register.
- VRP-COMP-008 — Independent Black-Box Validation Contract.

---

## 34. Revision History

| Revision | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial continuity identity assurance report |

---

**Veil Routing Protocol**

**Author: Vitalijus Riabovas**

Continuity-first architecture.

Independent lifetime verification.

Transport-independent qualification.

Observable security guarantees.

Protected intellectual property.

No hype.
Read the specifications.
Examine the evidence.
Challenge the engineering.

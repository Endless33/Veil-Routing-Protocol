
# Veil Routing Protocol (VRP)

## Adversarial Continuity Evidence and Security Assurance Matrix

**Author:** Vitalijus Riabovas  
**Project:** Veil Routing Protocol / Jumping VPN  
**Document ID:** VRP-CONT-E004  
**Revision:** 1.0  
**Classification:** PUBLIC  
**Evidence cutoff:** 2026-11-28  
**Scope:** Continuity, adversarial behavior, authority integrity and protected-state preservation

---

## 1. Executive Position

Veil Routing Protocol defines logical-session continuity as an architectural property that must remain subject to security and integrity requirements.

Preserving connectivity is not sufficient.

Preserving an externally visible session identifier is not sufficient.

Restoring application communication is not sufficient if unauthorized state changes become possible during recovery.

The governing architectural principles are:

```text
SESSION != TRANSPORT

CONNECTIVITY != AUTHORITY

RECOVERY != SECURITY INTEGRITY
```

The objective is to qualify continuity without sacrificing the security properties associated with the original logical-session lifetime.

This document describes externally observable requirements, recorded engineering observations, historical adversarial results, and remaining qualification boundaries.

No proprietary implementation mechanism is disclosed.

---

## 2. Security and Continuity Relationship

Continuity and security must be evaluated independently and, where required, together.

| Logical lifetime | Authority integrity | Qualification interpretation |
|---|---|---|
| Preserved | Preserved | Eligible for complete qualification |
| Preserved | Violated | Security-continuity failure |
| Replaced | Preserved | Original-lifetime continuity failure |
| Replaced | Violated | Combined qualification failure |
| Unknown | Preserved | Continuity not proven |
| Preserved | Unknown | Security assurance incomplete |
| Unknown | Unknown | Qualification incomplete |

A system must not receive complete continuity-security qualification merely because communication remains available.

---

## 3. Adversarial Qualification Objectives

The declared VRP assurance contract includes the following observable requirements.

| Threat condition | Required security property | Required continuity property |
|---|---|---|
| Replay | No unauthorized repeated protected effect | Original lifetime remains valid within scope |
| Duplicate operation | No unauthorized duplicate commitment | Required application state remains consistent |
| Stale authority | Invalidated authority cannot authorize protected effects | Authorized session remains protected |
| Authority rollback | Obsolete authority cannot improperly regain validity | Required lifetime properties remain consistent |
| History modification | Unauthorized history change is prevented or detected | Required accepted history remains protected |
| Endpoint churn | Transport change does not bypass authorization | Original lifetime independently confirmed |
| Network blackout | Recovery does not weaken mandatory security conditions | Original lifetime verified after recovery |
| Concurrent operations | Conflicting unauthorized effects are prevented | Required session consistency maintained |
| Malformed input | Invalid input cannot acquire authorization | Required valid-session behavior remains protected |
| Evidence tampering | Modified evidence is rejected | Unsupported continuity claims are rejected |

These are declared qualification objectives.

Their inclusion does not establish that every native adversarial workload has already completed qualification.

---

## 4. Replay Containment Acceptance Boundary

Replay qualification must distinguish between repeated network communication and repeated protected effects.

```text
REPEATED_PACKET
        !=
REPEATED_APPLICATION_EFFECT
        !=
REPEATED_CANONICAL_COMMIT
```

A complete replay-containment experiment must identify the original authorized operation, subsequent repeated attempts, relevant protected state, and final observed effects.

The security objective is not merely to return an error.

The objective is to prevent unauthorized repeated effects within the declared operation semantics.

---

## 5. Historical Replay-Storm Evidence

**Evidence ID:** VRP-ADV-H001

Earlier VRP engineering records reported a replay-storm result involving 9,999 rejected replay attempts.

### Historical Measurement Register

| Measurement | Historical reported result |
|---|---:|
| Replay attempts | 9,999 |
| Rejected replay attempts | 9,999 |
| Accepted replay attempts | 0 |
| Reported rejection ratio | 100% |

### Historical Result Visualization

```text
REPLAY ATTEMPTS

[##############################] 9999


REPORTED REJECTIONS

[##############################] 9999


REPORTED ACCEPTANCES

[                              ]    0
```

### Evidence Classification

```text
HISTORICAL_REPLAY_ATTEMPTS=9999

HISTORICAL_REPLAY_REJECTIONS=9999

HISTORICAL_REPLAY_ACCEPTANCES=0_REPORTED

ORIGINAL_EVIDENCE_REATTRIBUTION=PENDING
```

### Qualification Boundary

The original execution artifacts were not directly re-inspected for this document.

The precise implementation classification, workload semantics, observation methodology, and state-preservation assertions require original evidence attribution.

The result must not be interpreted as a newly verified native replay-containment measurement.

It also must not be interpreted as proof of replay resistance during physical transport migration.

---

## 6. Replay-State Preservation Contract

The following table defines the observable properties required for a stronger replay qualification.

| Observation | Required result |
|---|---|
| Initial authorized operation | Accepted according to contract |
| Initial protected effect | Independently observed |
| Repeated operation attempts | Attributable |
| Unauthorized repeated effects | Zero |
| Previously accepted state | Preserved according to contract |
| Required canonical history | Preserved |
| Subsequent valid operation | Accepted according to contract |
| Evidence completeness | Verified |

A replay storm that rejects every request, including legitimate subsequent requests, does not independently establish complete availability and recovery correctness.

Security containment and valid-operation availability must remain separately measurable.

---

## 7. Replay State Timeline

The following diagram illustrates the required acceptance relationship.

```text
INITIAL VALID OPERATION
           |
           v
AUTHORIZED STATE OBSERVED
           |
           v
+-----------------------------+
|     REPLAY TEST WORKLOAD    |
|                             |
|   Repeated operation input  |
|   Controlled observations   |
+-----------------------------+
           |
           v
NO UNAUTHORIZED REPEATED EFFECT
           |
           v
PREVIOUS ACCEPTED STATE VERIFIED
           |
           v
SUBSEQUENT VALID OPERATION
           |
           v
EXPECTED APPLICATION PROGRESSION
```

This diagram represents the public acceptance contract.

It does not disclose the native VRP replay-processing mechanism.

---

## 8. Duplicate-Commit Assurance

Duplicate-commit qualification addresses the protected effects of repeated operations.

A network implementation may receive duplicate communication events without committing the same protected application operation more than permitted.

The required distinction is:

| Event | Permitted interpretation |
|---|---|
| Duplicate packet received | Transport-level observation |
| Duplicate packet rejected | Transport rejection observation |
| Repeated operation received | Application-level observation |
| Repeated operation rejected | Operation rejection observation |
| Duplicate unauthorized effect prevented | Protected-effect containment |
| Canonical history unchanged where required | History-integrity evidence |

The final two observations require dedicated semantic verification.

They cannot be inferred solely from packet rejection.

---

## 9. Duplicate-Commit Acceptance Matrix

| Scenario | Expected protected effect | Expected qualification |
|---|---|---|
| First valid operation | Accepted according to contract | ACCEPT |
| Repeated protected operation | No unauthorized additional effect | CONTAIN |
| Invalid operation | No unauthorized effect | REJECT |
| Duplicate canonical commitment | Unauthorized additional effect detected | FAIL |
| Missing state observation | Unknown | INCOMPLETE |
| Missing workload attribution | Unknown | NOT_PROVEN |

These are expected evaluation decisions.

They are not newly recorded native VRP experimental results.

---

## 10. Historical Authority and Rollback Records

Earlier VRP engineering records reported successful rejection-related results associated with stale authority, rollback, and canonical-history protection.

| Historical security property | Recorded classification |
|---|---|
| Stale-authority rejection | PASS reported |
| Epoch rollback rejection | PASS reported |
| Unauthorized canonical-history rewrite rejection | PASS reported |
| Independent evidence verification | PASS reported in earlier evaluation records |

The original artifacts require separate attribution before stronger public qualification claims are assigned.

```text
HISTORICAL_SECURITY_RESULTS=REPORTED

ORIGINAL_ASSERTION_SEMANTICS=REVIEW_REQUIRED

CURRENT_NATIVE_APPLICABILITY=NOT_REESTABLISHED
```

Historical results must remain associated with their original implementation, workload, and acceptance criteria.

---

## 11. Stale-Authority Acceptance Contract

The declared security requirement is that invalidated authority cannot authorize new protected effects.

A complete experiment must establish:

| Observation | Required outcome |
|---|---|
| Initially valid authority | Established |
| Valid protected operation | Accepted according to contract |
| Authorization validity change | Attributable |
| Operation using invalidated authority | Rejected or contained |
| Unauthorized protected effect | Absent |
| Required accepted history | Preserved |
| Subsequent valid authorization behavior | Verified |

The evaluator must distinguish rejection of a request from preservation of the protected state.

An error response alone does not establish complete stale-authority containment.

---

## 12. Epoch Rollback Acceptance Contract

Rollback qualification addresses whether obsolete authorization can improperly become effective again.

The public acceptance model is:

```text
VALID AUTHORIZATION CONTEXT
             |
             v
AUTHORIZATION VALIDITY CHANGES
             |
             v
OBSOLETE AUTHORIZATION PRESENTED
             |
             v
EXPECTED RESULT:

NO UNAUTHORIZED PROTECTED EFFECT
```

The required observations must establish that an obsolete authorization context cannot produce an accepted protected effect contrary to the declared contract.

This model does not disclose how VRP represents or manages authority internally.

---

## 13. Canonical History Assurance

The canonical-history qualification objective concerns the semantic preservation of previously accepted operations.

The following conditions must be distinguishable.

| Observation | Required verifier interpretation |
|---|---|
| Required accepted history preserved | Eligible for successful qualification |
| Unauthorized operation removed | Integrity failure |
| Unauthorized history modification | Integrity failure |
| Unauthorized replacement of accepted operation | Integrity failure |
| Unauthorized additional commitment | Integrity failure |
| History length matches but contents differ | Not sufficient for successful qualification |
| Mandatory history observations unavailable | Incomplete qualification |

A matching history length does not establish matching history semantics.

No confidential history representation or protection algorithm is disclosed.

---

## 14. Native Rejection Evidence

**Evidence ID:** VRP-ADV-N001

A recorded native qualification fixture attempted an operation against a previously registered logical session.

The operation returned an error.

Subsequent native registry observation established the following.

| Measurement | Recorded result |
|---|---|
| Native operation | REJECTED |
| Original registry entry accessible after rejection | YES |
| Observed session cardinality after rejection | 1 |

### Recorded Outcome

```text
NATIVE_OPERATION_REJECTED=OBSERVED

ORIGINAL_SESSION_LOOKUP_AFTER_REJECTION=SUCCESS

OBSERVED_SESSION_CARDINALITY=1
```

### Interpretation

The tested rejection did not remove the observed registry entry.

This provides bounded evidence of registry availability following the rejected operation.

### Limitation

The complete security-relevant state was not independently compared before and after the rejection.

Consequently, this result does not independently establish complete rejection atomicity or the absence of every unintended state mutation.

---

## 15. Native Authorization-Related Rejection

**Evidence ID:** VRP-ADV-N002

A later native migration fixture successfully completed its initial scenario but encountered rejection when attempting an additional migration.

### Recorded Results

| Measurement | Result |
|---|---|
| Native initialization | PASS |
| Additional migration request | REJECTED |
| Requested additional migrations | 30 |
| Completed additional migrations | 0 |
| Error category | Preliminary authorization-related classification |
| Protected Core modification | NO |
| Qualification | NOT_QUALIFIED |

### Interpretation

An observable native rejection occurred.

The experimental fixture did not establish the required conditions for successful additional migration.

### Limitation

The precise root cause was not independently established.

The rejection must not be represented as proof of complete authority integrity.

It must not be represented as a successful continuity experiment.

No native security mechanism was weakened to force the experimental fixture to pass.

---

## 16. Native State-Transition Rejection

**Evidence ID:** VRP-ADV-N003

An experimental initialization fixture encountered a rejected state-changing operation.

A proposed alternative fixture sequence was not executed when its attribution gate was not satisfied.

| Property | Recorded result |
|---|---|
| State-changing operation | REJECTED |
| Alternative fixture execution | NOT_EXECUTED |
| Protected Core modification | NO |
| Original source preservation | PASS |

This provides evidence of the recorded operation rejection and preservation of the engineering baseline.

It does not independently qualify every invalid state-transition scenario.

---

## 17. Native Regression Qualification

**Evidence ID:** VRP-ADV-N004

The selected native canonical regression campaign recorded:

| Execution category | Successful executions | Recorded failures |
|---|---:|---:|
| Baseline | 49 | 0 |
| Repeated execution | 490 | 0 |
| Race-detector execution | 49 | 0 |
| Total | 588 | 0 |

### Execution Distribution

```text
BASELINE

[#####] 49


REPEATED EXECUTION

[##################################################] 490


RACE-DETECTOR EXECUTION

[#####] 49
```

### Interpretation

The selected native campaign completed its recorded execution requirements successfully.

The campaign supports implementation-level regression confidence within its selected scope.

### Limitation

The 588 successful executions represent 49 selected tests exercised repeatedly and with race-detector instrumentation.

They do not represent 588 distinct security attacks.

They do not independently establish complete adversarial coverage.

---

## 18. Concurrency Qualification Evidence

Selected native and isolated-component campaigns completed recorded race-detector execution.

| Campaign | Successful race-detector executions |
|---|---:|
| Native delivery-related fixtures | 39 |
| Native canonical regression selection | 49 |
| Separate UDP evaluation component | 40 |

These are distinct qualification campaigns.

Native test selections may overlap.

The separate UDP evaluation component is not the native VRP implementation.

Race-detector success does not independently establish:

- Security linearizability.
- Complete operation atomicity.
- Universal race freedom.
- Correctness of every concurrent state transition.
- Authority integrity under every competing operation.

Dedicated semantic concurrency workloads remain necessary for those claims.

---

## 19. Fail-Closed Behavior Contract

The declared VRP security contract requires unresolved mandatory security conditions to prevent unauthorized protected acceptance.

```text
VALID COMMUNICATION
        |
        v
PROTECTED OPERATION REQUESTED
        |
        v
MANDATORY SECURITY CONDITIONS
        |
        +-------------------------+
        |                         |
        v                         v
   ESTABLISHED               NOT ESTABLISHED
        |                         |
        v                         v
   CONTRACTUAL                NO UNAUTHORIZED
   ACCEPTANCE                 PROTECTED EFFECT
```

The diagram represents acceptance semantics.

It is not a native authorization decision algorithm.

Fail-closed behavior does not require unconditional termination of the entire logical session.

The applicable containment behavior must be evaluated according to the declared security contract.

---

## 20. Fail-Closed Verification Matrix

| Input condition | Required protected-effect outcome |
|---|---|
| Valid authorized operation | Accepted according to contract |
| Missing required authorization | No unauthorized effect |
| Invalid authorization | No unauthorized effect |
| Stale authorization | No unauthorized effect |
| Unsupported state transition | No unauthorized effect |
| Invalid logical-lifetime association | No unauthorized effect |
| Contradictory mandatory evidence | Qualification rejected |
| Missing mandatory evidence | Qualification incomplete |

The native enforcement mechanism remains confidential.

The public evaluation measures the observable outcome.

---

## 21. Security Versus Availability

Security and availability are independent qualification dimensions.

| Security verdict | Availability verdict | Interpretation |
|---|---|---|
| PASS | PASS | Both evaluated requirements satisfied |
| PASS | FAIL | Security maintained; availability requirement violated |
| FAIL | PASS | Communication available despite a security violation |
| FAIL | FAIL | Both evaluated requirements violated |
| NOT_TESTED | PASS | Availability established; security unqualified |
| PASS | NOT_TESTED | Security property established; availability unqualified |

Successful rejection must not conceal an availability failure.

Successful delivery must not conceal a security violation.

A complete assurance case must report both dimensions where applicable.

---

## 22. Adversarial Continuity During Transport Replacement

A complete native adversarial continuity experiment must evaluate the original logical lifetime while network conditions change.

Conceptual evaluation model:

```text
                 ORIGINAL LOGICAL LIFETIME L0
                              |
       +----------------------+----------------------+
       |                      |                      |
       v                      v                      v
 INITIAL TRANSPORT     NETWORK DISRUPTION      NEW TRANSPORT
       |                      |                      |
       +----------------------+----------------------+
                              |
                   INDEPENDENT VERIFICATION
                              |
       +----------------------+----------------------+
       |                      |                      |
       v                      v                      v
 LIFETIME IDENTITY      APPLICATION STATE      AUTHORITY INTEGRITY
```

The observation categories must belong to the same attributable execution.

Separate successful transport, replay, and session-registry experiments cannot establish the complete integrated result.

---

## 23. Compound-Fault Qualification Matrix

The following workloads define proposed adversarial continuity qualification targets.

| Workload ID | Condition | Proposed parameter | Latest comparative campaign |
|---|---|---|---|
| ADV-01 | Endpoint churn | Every 2 seconds | NOT_QUALIFIED |
| ADV-02 | Packet loss | 30% | NOT_TESTED |
| ADV-03 | Packet loss | 50% | NOT_TESTED |
| ADV-04 | Packet loss | 80% | NOT_TESTED |
| ADV-05 | Packet loss | 90% | NOT_TESTED |
| ADV-06 | Network blackout | 10 seconds | NOT_TESTED |
| ADV-07 | Network blackout | 30 seconds | NOT_TESTED |
| ADV-08 | Network blackout | 60 seconds | NOT_TESTED |
| ADV-09 | Elevated RTT | 300–900 milliseconds | NOT_TESTED |
| ADV-10 | Packet reordering | Controlled variable conditions | NOT_TESTED |
| ADV-11 | Packet duplication | Controlled variable conditions | NOT_TESTED |
| ADV-12 | Replay during migration | Controlled authorized workload | NOT_TESTED |
| ADV-13 | Stale authority during recovery | Controlled negative workload | NOT_TESTED |
| ADV-14 | Concurrent protected operations | Controlled competing operations | NOT_TESTED |
| ADV-15 | Churn and 80% packet loss | Combined workload | NOT_TESTED |
| ADV-16 | Churn, loss, blackout and replay | Combined workload | NOT_TESTED |

The listed status values apply to the latest comparative campaign.

They do not invalidate independently attributed historical qualification results.

The workload parameters are proposed test conditions, not recorded successful measurements.

---

## 24. Proposed Integrated Adversarial Acceptance Profile

The baseline integrated security-continuity workload should establish the following.

| Measurement | Required target |
|---|---:|
| Original logical-session lifetimes | 1 |
| Verified physical transport replacements | 30 |
| Independent original-lifetime confirmations | 30/30 |
| Required application transaction confirmations | 30/30 |
| Relevant unauthorized-operation attempts | Greater than zero |
| Relevant replay attempts | Greater than zero |
| Unauthorized accepted protected effects | 0 |
| Unauthorized duplicate commitments | 0 |
| Unauthorized history modifications | 0 |
| Unexpected replacement lifetimes | 0 |
| Missing mandatory observations | 0 |

A zero-violation measurement is valid only when the relevant workload was actually exercised and its protected effects were observed.

An empty adversarial workload cannot establish successful security qualification.

These values are acceptance targets, not completed native results.

---

## 25. Integrated Adversarial Verdict Contract

Complete qualification requires the applicable observations to establish:

```text
PHYSICAL_TRANSPORT_TRANSITION_VERIFIED

AND

ORIGINAL_LOGICAL_LIFETIME_VERIFIED

AND

APPLICATION_TRANSACTION_STATE_VERIFIED

AND

REQUIRED_AUTHORITY_INTEGRITY_VERIFIED

AND

REPLAY_CONTAINMENT_VERIFIED

AND

DUPLICATE_COMMIT_CONTAINMENT_VERIFIED

AND

CANONICAL_HISTORY_INTEGRITY_VERIFIED

AND

MANDATORY_EVIDENCE_COMPLETE
```

This expression defines the public qualification decision.

It does not describe the internal security or continuity logic of VRP.

---

## 26. Mandatory Adversarial Negative Controls

A qualified evaluator must reject deliberately invalid reference outcomes.

| Negative control | Required result |
|---|---|
| Replacement lifetime with reused label | Continuity rejected |
| Replayed operation produces additional unauthorized effect | Replay qualification failed |
| Duplicate canonical commitment | Duplicate containment failed |
| Invalidated authority produces protected effect | Authority qualification failed |
| Obsolete authority improperly accepted | Rollback qualification failed |
| Unauthorized accepted-history modification | History qualification failed |
| Recovery into an incorrect application context | Application continuity failed |
| Missing post-operation state evidence | Qualification incomplete |
| Modified measurement file | Evidence integrity failed |
| Contradictory successful verdict | Semantic verification failed |

These controls evaluate the effectiveness of the verification methodology.

Successful negative controls do not automatically establish native VRP security.

---

## 27. Security Evidence Strength Matrix

| Evidence property | Current documented classification |
|---|---|
| Historical replay storm | 9,999 rejections reported |
| Historical stale-authority rejection | PASS reported |
| Historical rollback rejection | PASS reported |
| Historical canonical rewrite rejection | PASS reported |
| Native operation rejection | OBSERVED |
| Native registry availability after tested rejection | VERIFIED |
| Native authorization-related rejection | OBSERVED — preliminary attribution |
| Native state-transition rejection | OBSERVED — preliminary attribution |
| Selected native regression campaign | 588 successful executions |
| Selected native race-detector campaigns | QUALIFIED within tested scope |
| Complete rejection atomicity | NOT_PROVEN |
| Integrated replay containment during physical migration | NOT_PROVEN in latest campaign |
| Integrated authority integrity during network blackout | NOT_PROVEN in latest campaign |
| Integrated compound-fault continuity-security | NOT_PROVEN in latest campaign |
| Independent matched-workload superiority | NOT_PROVEN |

The historical observations require original evidence attribution.

The latest native observations retain their own bounded qualification scope.

---

## 28. Adversarial Measurement Contract

Future approved evidence packages should record:

| Measurement | Meaning |
|---|---|
| authorized_attempts | Executed authorized-operation workload |
| authorized_acceptances | Observed valid-operation acceptances |
| unauthorized_attempts | Executed invalid-operation workload |
| unauthorized_effects | Observed unauthorized protected effects |
| replay_attempts | Attributable repeated-operation attempts |
| replay_effects | Unauthorized repeated protected effects |
| duplicate_commits | Unauthorized additional commitments |
| history_violations | Observed unauthorized history modifications |
| physical_replacements | Independently verified transport transitions |
| lifetime_mismatches | Independently detected identity mismatches |
| missing_observations | Missing mandatory evidence records |

The public measurement contract does not require disclosure of native authority values, protected protocol state, or internal cryptographic information.

---

## 29. Proposed Machine-Readable Result

The following example illustrates an integrated adversarial continuity result format.

It is not an actual completed experiment.

```json
{
  "schema_version": "1.0",
  "record_type": "schema_example",
  "qualification_type": "adversarial_continuity",
  "evaluation_mode": "AUTHORIZED_NATIVE",
  "execution_status": "NOT_TESTED",
  "observed": {
    "physical_replacements": null,
    "original_lifetime_confirmations": null,
    "application_confirmations": null,
    "authorized_attempts": null,
    "unauthorized_attempts": null,
    "unauthorized_effects": null,
    "replay_attempts": null,
    "unauthorized_replay_effects": null,
    "duplicate_commits": null,
    "history_violations": null,
    "missing_observations": null
  },
  "verification": {
    "logical_lifetime": "NOT_TESTED",
    "application_state": "NOT_TESTED",
    "authority_integrity": "NOT_TESTED",
    "replay_containment": "NOT_TESTED",
    "duplicate_containment": "NOT_TESTED",
    "canonical_history": "NOT_TESTED",
    "negative_controls": "NOT_TESTED",
    "evidence_integrity": "NOT_TESTED"
  },
  "overall_status": "NOT_TESTED"
}
```

Null values represent unavailable measurements.

They must never be replaced with successful zero-violation results before execution.

---

## 30. Evidence Integrity

The recorded comparative evidence consolidation established the following reported preservation outcomes.

```text
HISTORICAL_EVIDENCE_ANCHORS_VERIFIED=12

CONSOLIDATION=PASS

EVIDENCE_INTEGRITY=PASS

ORIGINAL_SOURCE_PRESERVATION=PASS

PROTECTED_CORE_MUTATION=NO
```

These are evidence-integrity and preservation observations.

They do not independently establish every adversarial security property.

Approved public evidence packages should contain:

```text
EXPERIMENT_SPECIFICATION.md
MEASUREMENTS.csv
VERIFICATION_RESULTS.json
NEGATIVE_CONTROL_RESULTS.json
LIMITATIONS.md
PROVENANCE.json
SHA256SUMS
```

Actual public SHA-256 commitments must correspond to the exact approved artifact bytes.

No fabricated digest or unapproved private commitment may be substituted.

---

## 31. Comparative Security Position

A fair security-continuity comparison must evaluate the complete declared behavior of participating implementations.

| Property | Required comparative approach |
|---|---|
| Transport security | Evaluate actual supported mechanisms |
| Native migration | Permit supported migration capabilities |
| Application continuity | Evaluate complete application behavior |
| Replay containment | Measure relevant unauthorized repeated effects |
| Authority integrity | Evaluate declared protected-operation semantics |
| Canonical history | Evaluate applicable history-preservation requirements |
| Recovery | Correlate availability, identity and security observations |

A transport-level security guarantee is not necessarily equivalent to application-level authority integrity.

However, other architectures may implement equivalent higher-level guarantees.

Whether they do so must be established through matched evaluation.

No universal security-superiority claim is derived from the current campaign.

---

## 32. Public Validation Kit Integration

Eligible public security-validation components may include:

- Synthetic replay-negative controls.
- Duplicate-effect detection controls.
- Reference lifetime-replacement controls.
- Invalid-authorization reference outcomes.
- History-consistency verification.
- Measurement-completeness verification.
- Evidence-tampering detection.
- Contradictory-result detection.
- Public transport control workloads.

These components should remain independently understandable and reproducible.

Public reference components must not implement or disclose confidential native VRP security mechanisms.

Their results must remain explicitly classified as reference results.

---

## 33. Protected Core Disclosure Boundary

This document intentionally excludes:

- Native replay-processing algorithms.
- Proprietary authority mechanisms.
- Native continuity algorithms.
- Confidential state-machine implementation.
- Protected canonical-history mechanisms.
- Internal protocol-state representations.
- Native cryptographic construction details.
- Raw private execution traces.
- Internal repository paths and identifiers.
- Confidential binaries and debug information.
- Infrastructure configuration.
- Credentials and cryptographic secrets.
- Unapproved private evidence commitments.
- Details enabling reconstruction of the Protected Core.

Independent adversarial qualification evaluates externally observable security properties.

It does not require unrestricted implementation disclosure.

---

## 34. Independent Reviewer Questions

An independent reviewer should be able to determine:

1. Was the original logical lifetime independently established?
2. Did the physical transport transition actually occur?
3. Was the adversarial workload actually executed?
4. Were valid and invalid operation outcomes separately observed?
5. Were unauthorized protected effects independently checked?
6. Was application transaction state preserved?
7. Was the required accepted history preserved?
8. Could the evaluator detect a replacement lifetime?
9. Were positive and negative observer controls qualified?
10. Were the evidence artifacts complete and integrity-verified?
11. Were security and availability reported separately?
12. Were the limitations explicitly recorded?

Every affirmative qualification claim must be attributable to supporting evidence.

---

## 35. Consolidated Adversarial Continuity Verdict

The available engineering record includes historical adversarial observations, native rejection behavior, selected native regression success, race-detector qualification, and evidence-preservation results.

```text
HISTORICAL_REPLAY_REJECTIONS=9999_REPORTED

HISTORICAL_STALE_AUTHORITY_REJECTION=PASS_REPORTED

HISTORICAL_ROLLBACK_REJECTION=PASS_REPORTED

HISTORICAL_CANONICAL_REWRITE_REJECTION=PASS_REPORTED

NATIVE_OPERATION_REJECTION=OBSERVED

POST_REJECTION_REGISTRY_AVAILABILITY=VERIFIED

SELECTED_NATIVE_REGRESSION_EXECUTIONS=588

SELECTED_NATIVE_RACE_QUALIFICATION=PASS

HISTORICAL_EVIDENCE_ANCHORS_VERIFIED=12

EVIDENCE_INTEGRITY=PASS

PROTECTED_CORE_MUTATION=NO

INTEGRATED_ADVERSARIAL_CONTINUITY=NOT_PROVEN_IN_LATEST_CAMPAIGN

COMPLETE_EXTERNAL_NATIVE_REPRODUCTION=NOT_ESTABLISHED

UNIVERSAL_SECURITY_SUPERIORITY=NOT_PROVEN
```

The historical observations remain relevant.

Their original artifacts must be attributed before stronger native implementation claims are assigned.

The latest comparative campaign establishes bounded implementation observations but does not complete the integrated adversarial continuity qualification.

---

## 36. Related Public Documents

- VRP-CONT-E001 — Continuity Evidence Matrix.
- VRP-CONT-E002 — Continuity Identity Assurance.
- VRP-CONT-E003 — Migration and Recovery Evidence.
- VRP-COMP-005 — Security and Authority Assurance.
- VRP-COMP-006 — Evidence Integrity Manifest.
- VRP-COMP-007 — Claims and Limitations Register.
- VRP-COMP-008 — Independent Black-Box Validation Contract.

---

## 37. Revision History

| Revision | Date | Description |
|---|---|---|
| 1.0 | 2026-11-28 | Initial adversarial continuity evidence and security assurance matrix |

---

## Final Engineering Position

Continuity without security is insufficient.

Security without independently attributable state verification is incomplete.

Recovery without original-lifetime verification is not complete logical-session continuity.

The architecture defines the required guarantees.

The qualification workload challenges those guarantees.

The evidence determines whether the guarantees have been established.

```text
SESSION != TRANSPORT

CONNECTIVITY != AUTHORITY

REPLAY REJECTION != COMPLETE STATE PROOF

RECOVERY != SECURITY INTEGRITY

HISTORICAL REPORT != INDEPENDENT REPRODUCTION

EVIDENCE != MARKETING
```

**Veil Routing Protocol**

**Author: Vitalijus Riabovas**

Continuity-first architecture.

Observable security guarantees.

Independent adversarial qualification.

Protected intellectual property.

No hype.
Read the specifications.
Examine the evidence.
Challenge the engineering.

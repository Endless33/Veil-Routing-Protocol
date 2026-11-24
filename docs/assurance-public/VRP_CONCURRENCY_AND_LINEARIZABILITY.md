# VRP Concurrency and Linearizability

## Veil Routing Protocol — Jumping VPN

**Document ID:** VRP-PA-009
**Version:** 1.0
**Classification:** PUBLIC
**Status:** Evidence-Oriented Qualification Contract
**Author:** Vitalijus Riabovas
**Protected Core:** CONFIDENTIAL

---

## 1. Executive Statement

Successful sequential execution does not
establish correctness under concurrent
operation activity.

A communication system may appear
operational while overlapping operations
produce incompatible canonical effects.

A system may pass race detection while
violating its semantic correctness contract.

A system may recover communication while
accepting an invalid concurrent outcome.

Veil Routing Protocol establishes the
following architectural principle:

    SESSION ≠ TRANSPORT

The applicable logical session, authority,
and canonical integrity contracts MUST
remain valid under qualified concurrent
execution conditions.

This document defines externally verifiable
concurrency requirements, observable
operation history semantics, evidence
obligations, and falsification criteria.

It does not disclose proprietary
concurrency mechanisms.

---

## 2. Assurance Claim

Primary claim:

    VRP-C11 — Concurrent operation correctness.

Supporting claims:

    VRP-C01 — Logical session identity.
    VRP-C02 — Transport independence.
    VRP-C04 — Replay containment.
    VRP-C05 — Duplicate commit rejection.
    VRP-C06 — Stale authority rejection.
    VRP-C07 — Epoch rollback rejection.
    VRP-C08 — Canonical history integrity.
    VRP-C09 — Deterministic authority resolution.
    VRP-C10 — Controlled recovery.
    VRP-C12 — Evidence integrity.
    VRP-C13 — Fail-closed behavior.
    VRP-C14 — Bounded defensive behavior.

Concurrency qualification MUST establish
the applicable semantic correctness
properties rather than merely successful
execution without reported errors.

Linearizability claims apply only to
explicitly identified operation domains.

---

## 3. Applicable Invariants

| Invariant | Qualification property |
|---|---|
| INV-001 | Logical identity preservation |
| INV-004 | Replay containment |
| INV-005 | Duplicate commit exclusion |
| INV-006 | Stale authority rejection |
| INV-007 | Epoch rollback exclusion |
| INV-008 | Canonical history integrity |
| INV-009 | Deterministic authority resolution |
| INV-010 | Recovery preservation |
| INV-011 | Concurrent operation correctness |
| INV-012 | Evidence integrity |
| INV-013 | Fail-closed behavior |
| INV-014 | Bounded defensive behavior |
| INV-016 | Session lifetime isolation |
| INV-017 | Unauthorized mutation exclusion |
| INV-018 | Transport failure isolation |

Normative invariant definitions are
established in VRP-PA-002.

This document specializes their application
to concurrent execution.

---

## 4. Fundamental Engineering Distinctions

The following properties MUST remain
independently distinguishable:

    DATA RACE DETECTION

    THREAD SAFETY

    SEMANTIC ATOMICITY

    LINEARIZABILITY

    DEADLOCK FREEDOM

    LIVENESS

    RESOURCE BOUNDEDNESS

    CANONICAL INTEGRITY

A positive result in one category
does not automatically establish
correctness in another category.

In particular:

    RACE DETECTOR PASS
        !=
    LINEARIZABILITY PROOF

    CONCURRENT EXECUTION SUCCESS
        !=
    SEMANTIC CORRECTNESS

    VALID FINAL STATE
        !=
    VALID COMPLETE HISTORY

These distinctions are mandatory
throughout concurrency qualification.

---

## 5. Historical Engineering Context

The VRP project has previously reported
successful internal regression and
race detection campaigns.

Historical adversarial evidence also
includes reported outcomes concerning:

- Replay containment.
- Duplicate effect exclusion objectives.
- Authority integrity.
- Canonical history integrity.
- Recovery preservation.

Relevant historical references include:

    AVE-001 — Replay rejection.
    AVE-004 — Stale authority rejection.
    AVE-005 — Epoch rollback rejection.
    AVE-006 — Canonical rewrite rejection.
    AVE-007 — Evidence verification.

These references are established
in VRP-PA-005.

They provide historical engineering
context.

They do not independently establish
linearizability of the complete
implementation.

A dedicated public linearizability
qualification artifact is not
established by this document.

---

## 6. Current Evidence Classification

For the dedicated concurrency and
linearizability qualification claim:

    CLAIM_REFERENCE:
        VRP-C11

    PUBLIC_CONTRACT:
        SPECIFIED

    HISTORICAL_INTERNAL_TEST_ACTIVITY:
        REPORTED

    DEDICATED_PUBLIC_OPERATION_HISTORY:
        NOT EMBEDDED

    PUBLIC_LINEARIZABILITY_VERIFICATION:
        NOT ESTABLISHED BY THIS RECORD

    INDEPENDENT_REPRODUCTION:
        NOT ESTABLISHED BY THIS RECORD

    DEDICATED_CLAIM_EVIDENCE_LEVEL:
        E0

Historical internal testing reports
remain relevant supplementary evidence.

They MUST NOT be substituted for
a dedicated semantic verification
record.

This classification does not establish
that additional restricted engineering
evidence does not exist.

It describes the limitations of the
current public record.

---

## 7. Abstract Operation Model

For external verification purposes,
an observable operation MAY be
described using:

    O = operation reference

    I(O) = invocation observation

    R(O) = response observation

    E(O) = attributable canonical effect

    S(O) = applicable logical session

    L(O) = applicable logical lifetime

These symbols describe conceptual
verification targets.

They are not implementation variables,
runtime structures, internal interfaces,
or wire-level protocol definitions.

The operation model MUST identify
the applicable externally observable
semantics before qualification begins.

---

## 8. Observable Operation History

An operation history is an attributable
record of relevant invocation, response,
and effect observations.

A qualification history SHOULD
establish:

- Applicable operation identity.
- Invocation observations.
- Response observations.
- Relevant operation overlap.
- Observable canonical effects.
- Applicable authorization context.
- Logical lifetime attribution.
- Observation completeness.

A collection of unrelated diagnostic
messages does not automatically
constitute a qualified operation
history.

The relationship between observations
and the evaluated correctness
contract MUST be established.

---

## 9. Real-Time Precedence

For two completed operations A and B:

If the response of A occurs before
the invocation of B, the applicable
linearizable interpretation MUST
preserve that precedence.

Conceptually:

    Response(A) precedes Invocation(B)

        implies

    A precedes B in the legal
    sequential interpretation.

Overlapping operations MAY admit
more than one legal ordering.

The applicable sequential contract
determines which interpretations
are permitted.

The observation method MUST account
for timing uncertainty.

An ordering relationship MUST NOT
be asserted when the available
observations cannot establish it.

---

## 10. Linearizability Qualification

For an operation domain explicitly
qualified as linearizable, the
observed history MUST admit a legal
sequential interpretation consistent
with the applicable operation
semantics and real-time precedence.

Pending operations MUST be handled
according to the declared history
completion model.

A valid interpretation MUST NOT
invent responses or effects that
contradict established observations.

The evaluation MUST identify:

- Qualified operation domain.
- Applicable sequential semantics.
- Initial conditions.
- Observed operation history.
- Real-time precedence constraints.
- Treatment of pending operations.
- Verification outcome.
- Observation limitations.

This document does not disclose
internal linearization points,
synchronization mechanisms, or
implementation algorithms.

---

## 11. Semantic Atomicity

Where an operation is governed by
an atomic canonical effect contract,
its observable outcome MUST remain
consistent with that contract.

A failed operation MUST NOT produce
a prohibited partial canonical
effect.

A successful operation MUST NOT
produce additional prohibited
effects.

The applicable contract MAY permit
diagnostic observations, accounting
activity, or other explicitly
authorized side effects.

Such effects MUST remain distinguishable
from protected canonical mutation.

Atomicity qualification requires
semantic observation rather than
assumptions derived from internal
execution structure.

---

## 12. Duplicate Commitment Exclusion

For an operation governed by an
at-most-once commitment contract:

    CanonicalCommitCount(O) <= 1

This requirement remains applicable
when repeated presentations overlap.

Concurrent delivery MUST NOT
independently authorize repeated
canonical commitment.

The evaluation MUST establish
actual canonical effect accounting.

A count of successful responses
or rejected responses alone is
insufficient.

The relevant containment contract
is defined in VRP-PA-006.

---

## 13. Illustrative History A

### Permitted overlapping execution

The following is a synthetic
verification example.

It is not a captured VRP runtime
trace.

Assumed external contract:

    Two presentations of the same
    logical operation may produce
    at most one canonical commitment.

Illustrative observations:

| Order | Observation |
|---|---|
| 1 | Presentation A invoked |
| 2 | Presentation B invoked |
| 3 | One authorized canonical effect observed |
| 4 | Presentation A completed |
| 5 | Presentation B completed |

Observed canonical commitment count:

    1

If the response semantics and all
other applicable requirements are
satisfied, this history MAY be
consistent with the declared
at-most-once contract.

This example alone does not
establish complete linearizability.

Its purpose is to illustrate
the relevant observable distinction.

---

## 14. Illustrative History B

### Prohibited duplicate effect

The following is a synthetic
negative verification example.

It is not a captured VRP runtime
trace.

Assumed external contract:

    The same logical operation
    may commit at most once.

Illustrative observations:

| Order | Observation |
|---|---|
| 1 | Presentation A invoked |
| 2 | Presentation B invoked |
| 3 | Canonical effect 1 observed |
| 4 | Canonical effect 2 observed |
| 5 | Presentation A completed |
| 6 | Presentation B completed |

Both canonical effects are
attributed to the same logical
operation.

Observed canonical commitment count:

    2

Expected qualification verdict:

    FAIL

No ordering of the two presentations
can satisfy the assumed at-most-once
contract while preserving both
established canonical effects.

Successful communication does not
override the violation.

---

## 15. Illustrative History C

### Real-time precedence violation

The following is a synthetic
verification example.

Assumed external contract:

    A completed authorized state
    change must be reflected by
    a subsequent observation when
    no intervening authorized change
    has occurred.

Illustrative observations:

| Order | Observation |
|---|---|
| 1 | Authorized operation A invoked |
| 2 | Operation A completed successfully |
| 3 | Observation operation B invoked |
| 4 | B returns an incompatible previous state |

If no permitted intervening operation
or contract exception explains the
result, the history violates the
assumed sequential semantics.

Expected qualification verdict:

    FAIL

The example defines a generic
verification counterexample.

It does not disclose actual VRP
state representations or operations.

---

## 16. Illustrative History D

### Insufficient observation coverage

Illustrative observations:

| Order | Observation |
|---|---|
| 1 | Operation A invoked |
| 2 | Operation B invoked |
| 3 | A reports success |
| 4 | B reports rejection |
| 5 | Canonical effect observations unavailable |

Expected qualification verdict:

    INCONCLUSIVE

The reported rejection does not
establish that operation B produced
no prohibited canonical effect.

The missing observation MUST NOT
be replaced with an assumption
of correctness.

---

## 17. Illustrative History E

### Permitted ordering variation

Two distinct authorized operations
overlap in time.

The applicable sequential contract
permits either ordering.

One execution produces an outcome
consistent with:

    A followed by B.

Another execution produces an outcome
consistent with:

    B followed by A.

Both histories MAY satisfy the
same linearizability contract.

Different permitted concurrent
outcomes do not independently
constitute nondeterministic
correctness failure.

The evaluation MUST distinguish
permitted scheduling variation
from incompatible canonical effects.

---

## 18. Illustrative History F

### Pending operation ambiguity

Illustrative observations:

| Order | Observation |
|---|---|
| 1 | Operation A invoked |
| 2 | Operation B invoked |
| 3 | Operation B completed |
| 4 | Evaluation interrupted |
| 5 | Completion of A unavailable |

The verifier MUST apply the
declared pending-operation semantics.

It MUST NOT automatically classify
A as successfully committed,
rejected, or harmless.

If the available observations
cannot establish the required
correctness property, the relevant
verdict MUST remain INCONCLUSIVE.

A pending response is not proof
of absent canonical effects.

---

## 19. Authority Integrity Under Concurrency

Concurrent activity MUST preserve
the applicable canonical authority
contract.

Where exclusive authority is
required, incompatible authority
outcomes MUST NOT coexist within
the qualified scope.

A valid final authority observation
does not independently exclude
an earlier prohibited overlap.

The qualification MUST account for
relevant temporal observations.

The authority requirements defined
in VRP-PA-007 remain applicable.

Internal authority resolution
mechanisms remain confidential.

---

## 20. Stale Authority and Concurrent Activity

An operation lacking valid
authorization MUST NOT acquire
permission solely because it
overlaps with an authorized
operation.

The evaluation MUST establish
the applicable authorization
semantics for the observed
operation history.

A concurrent execution MUST NOT
be classified as compliant merely
because one of its operations
was valid.

Each protected canonical effect
requires appropriate authorization.

---

## 21. Logical Lifetime Isolation

Concurrent operations associated
with different logical session
lifetimes MUST remain subject
to their applicable lifetime
boundaries.

An obsolete lifetime MUST NOT
independently authorize protected
effects within another lifetime.

The qualification MUST distinguish:

- External identifier reuse.
- Original logical lifetime.
- Replacement logical lifetime.
- Applicable operation attribution.
- Permitted canonical effects.
- Prohibited cross-lifetime effects.

The internal lifetime representation
remains confidential.

---

## 22. Transport Transition Concurrency

Concurrent transport transition
activity MUST remain subject to
the applicable logical session
and authority contracts.

A transport transition MUST NOT
independently authorize:

- Duplicate canonical commitment.
- Unauthorized logical session replacement.
- Invalid authority acceptance.
- Prohibited history modification.
- Unauthorized lifetime interference.

The evaluation MUST distinguish
transport activity from logical
session and canonical state
observations.

Successful network communication
does not independently establish
concurrent semantic correctness.

---

## 23. Recovery Concurrency

Concurrent activity during recovery
MUST preserve applicable mandatory
correctness requirements.

Recovery MUST NOT independently
authorize a prohibited effect.

The evaluation SHOULD distinguish:

    RECOVERY PROGRESS

    CONCURRENT OPERATION OUTCOMES

    SESSION IDENTITY OUTCOME

    AUTHORITY INTEGRITY OUTCOME

    CANONICAL HISTORY OUTCOME

The recovery contract established
in VRP-PA-008 remains applicable.

Successful recovery cannot override
a confirmed concurrency violation.

---

## 24. Observation Consistency

Where the public operation contract
requires a coherent observation,
the returned observation MUST
satisfy its declared consistency
semantics.

An observation MUST NOT be
classified as coherent solely
because each individual value
appears valid.

The qualification MUST examine
whether the combined observation
is permitted by the applicable
operation contract.

This requirement does not disclose
internal snapshot mechanisms,
memory ownership models, or
state representation.

---

## 25. Observation Isolation

Where the applicable public
contract defines observation-only
behavior, obtaining an observation
MUST NOT independently authorize
a prohibited canonical mutation.

The evaluation SHOULD distinguish:

- Permitted observation.
- Authorized operation effects.
- Prohibited observation-induced effects.
- Unrelated concurrent activity.

A successful observation response
does not independently establish
the absence of prohibited effects.

The applicable integrity contract
remains authoritative.

---

## 26. Race Detection Evidence

Race detection provides valuable
implementation-level engineering
evidence.

A successful race detector
execution MAY establish that no
supported data race was detected
during the corresponding observed
execution.

It does not independently establish:

- Absence of every possible data race.
- Correctness under every schedule.
- Semantic atomicity.
- Linearizability.
- Deadlock freedom.
- Starvation freedom.
- Correct authority resolution.
- Unlimited concurrent scalability.

Race detection results MUST remain
associated with their actual
execution scope and instrumentation
conditions.

---

## 27. Regression Testing Evidence

Regression testing examines
whether previously established
correctness expectations remain
satisfied within the tested scope.

A meaningful regression record
SHOULD identify:

- Evaluated implementation reference.
- Applicable test contract.
- Execution environment.
- Actual executed test count.
- Repetition count.
- Passed evaluations.
- Failed evaluations.
- Skipped evaluations.
- Incomplete evaluations.
- Relevant verification artifacts.

A skipped test MUST NOT be
counted as successful.

A configured repetition count
MUST NOT be substituted for
the actual completed count.

---

## 28. Repeated Execution Requirements

Repeated concurrent execution
can increase observation coverage.

It does not establish exhaustive
coverage of all possible schedules.

The following MUST remain
distinguishable:

    CONFIGURED_REPETITIONS

    ACTUAL_COMPLETED_REPETITIONS

    OBSERVED_OPERATION_COUNT

    OBSERVED_OVERLAP_COUNT

    VERIFIED_HISTORY_COUNT

    DISTINCT_OBSERVED_SCHEDULES

A large repetition count alone
does not independently establish
schedule diversity.

Where diversity cannot be measured,
that limitation MUST be documented.

---

## 29. Positive Control Requirements

The evaluation MUST demonstrate
that permitted operations can
produce their authorized effects.

Required control categories include:

    VALID_BASELINE:
        REQUIRED

    AUTHORIZED_OPERATION_PROGRESS:
        REQUIRED

    CANONICAL_EFFECT_OBSERVATION:
        REQUIRED

    CONCURRENT_ACTIVITY_OBSERVATION:
        REQUIRED

    VERIFICATION_METHOD_READINESS:
        REQUIRED

These are qualification requirements.

They are not results of an
executed campaign.

A system that rejects every
operation MUST NOT receive a
positive concurrent correctness
verdict solely because no
prohibited effects were observed.

---

## 30. Negative Control Requirements

The verification method MUST
distinguish relevant noncompliant
histories from compliant histories.

Approved synthetic fixtures
SHOULD include:

- Duplicate canonical commitment.
- Real-time precedence violation.
- Unauthorized canonical effect.
- Prohibited lifetime interference.
- Incompatible authority outcomes.
- Missing mandatory observations.
- Contradictory observation records.

A verifier MUST NOT accept a
known noncompliant history as
satisfying the applicable contract.

Synthetic fixtures MUST remain
clearly identified as synthetic.

They MUST NOT be represented
as captured production execution
evidence.

---

## 31. Verification Control Matrix

| Control | Expected result |
|---|---|
| Valid legal history | ACCEPT |
| Permitted overlapping history | ACCEPT |
| Confirmed duplicate effect | REJECT |
| Confirmed precedence violation | REJECT |
| Confirmed unauthorized effect | REJECT |
| Confirmed incompatible authority | REJECT |
| Missing required observation | INCONCLUSIVE |
| Unresolved operation attribution | INCONCLUSIVE |
| Unsupported operation semantics | INCONCLUSIVE |

These are expected verification
outcomes.

They do not establish that
a particular verifier has
already passed the controls.

Actual control execution results
require attributable evidence.

---

## 32. Qualification Scenario Registry

| Scenario | Evaluation objective |
|---|---|
| CLQ-001 | Valid sequential baseline |
| CLQ-002 | Valid concurrent operation progress |
| CLQ-003 | Overlapping operation correctness |
| CLQ-004 | Concurrent duplicate containment |
| CLQ-005 | Semantic atomicity |
| CLQ-006 | Real-time precedence |
| CLQ-007 | Linearizable history verification |
| CLQ-008 | Pending operation accounting |
| CLQ-009 | Concurrent authority integrity |
| CLQ-010 | Stale authority exclusion |
| CLQ-011 | Session lifetime isolation |
| CLQ-012 | Transport transition concurrency |
| CLQ-013 | Recovery concurrency |
| CLQ-014 | Canonical history preservation |
| CLQ-015 | Observation consistency |
| CLQ-016 | Observation isolation |
| CLQ-017 | Race detection qualification |
| CLQ-018 | Repeated concurrent execution |
| CLQ-019 | Liveness qualification |
| CLQ-020 | Resource qualification |
| CLQ-021 | Verification negative controls |
| CLQ-022 | Independent reproduction |

Registry inclusion establishes
an evaluation objective.

It does not establish completed
execution or qualification.

---

## 33. Proposed Concurrency Qualification Matrix

The following values define
candidate laboratory evaluation
conditions.

They are proposed parameters,
not reported execution results.

| Scenario | Intended concurrent activity |
|---|---:|
| CLQ-P01 | 1 operation participant |
| CLQ-P02 | 2 operation participants |
| CLQ-P03 | 8 operation participants |
| CLQ-P04 | 32 operation participants |
| CLQ-P05 | 128 operation participants |

The meaning of an operation
participant MUST be defined by
the corresponding evaluation.

A participant count MUST NOT
be represented as a count of
simultaneously active sessions
unless that relationship has
been established.

Actual overlap MUST be observed.

The configured activity level
does not independently establish
concurrent execution.

These values do not represent
implementation limits or
supported production capacity.

---

## 34. Proposed Repetition Matrix

| Scenario | Intended repetitions |
|---|---:|
| CLQ-R01 | 1 |
| CLQ-R02 | 10 |
| CLQ-R03 | 100 |
| CLQ-R04 | 1,000 |

These are candidate evaluation
parameters.

They do not represent previously
executed repetition counts.

Each evaluation MUST record
actual completed repetitions,
observed outcomes, and applicable
verification coverage.

No execution result is asserted
by this matrix.

---

## 35. History Verification Obligations

For a dedicated linearizability
qualification, the evaluation
MUST establish:

1. A defined operation domain.

2. A declared sequential
   correctness contract.

3. Attributable initial conditions.

4. Observable invocation and
   response relationships.

5. Applicable real-time precedence.

6. Relevant canonical effect
   observations.

7. A defined pending-operation
   treatment.

8. Qualified verification controls.

9. A semantic verification result.

10. Explicit observation and
    execution limitations.

A history verification conclusion
MUST NOT exceed the actual
observation coverage.

---

## 36. Verification Outcome Semantics

A history verification method
SHOULD distinguish:

    LEGAL_INTERPRETATION_ESTABLISHED

    NO_LEGAL_INTERPRETATION_EXISTS

    VERIFICATION_INCOMPLETE

    OBSERVATION_INSUFFICIENT

    OPERATION_MODEL_UNSUPPORTED

The absence of a discovered
legal interpretation does not
automatically establish that
none exists.

Where verification terminates
without resolving the applicable
question, the result MUST
remain INCONCLUSIVE.

A confirmed contradiction with
the applicable contract constitutes
a failure.

---

## 37. Counterexample Evidence

A confirmed concurrency
counterexample SHOULD contain
sufficient information to
establish the violated contract.

Relevant evidence categories
include:

- Applicable operation semantics.
- Relevant operation observations.
- Established ordering constraints.
- Attributable canonical effects.
- Expected permitted behavior.
- Observed incompatible behavior.
- Verification conclusion.
- Implementation attribution.
- Known limitations.

Where practical, an approved
reduced observation history
SHOULD be provided.

Reduction MUST preserve the
relevant demonstrated violation.

A reduced counterexample MUST
NOT be represented as the
complete original execution.

---

## 38. Safety and Liveness Separation

Concurrency safety and concurrency
liveness are distinct properties.

Safety concerns exclusion of
prohibited outcomes.

Liveness concerns permitted
progress under declared
operating assumptions.

A system MAY preserve safety
while progress remains delayed.

A system MAY continue processing
operations while violating
a mandatory safety contract.

Qualification MUST report
these outcomes separately.

A successful safety result
does not establish deadlock
freedom or starvation freedom.

---

## 39. Deadlock and Progress Qualification

Where progress requirements
are applicable, the evaluation
MUST define:

- Expected permitted progress.
- Applicable operating assumptions.
- Observation interval.
- Mandatory completion conditions.
- Relevant timing limits.
- Classification of pending activity.

A finite execution without an
observed deadlock does not
establish universal deadlock
freedom.

A timeout MAY establish failure
of a declared progress requirement.

It does not independently identify
the underlying failure mechanism.

The qualification record MUST
avoid unsupported causal conclusions.

---

## 40. Resource Qualification

Concurrent correctness does not
establish unlimited resource
capacity.

Relevant measurements include:

- Concurrent activity level.
- Actual completed operations.
- Operation completion latency.
- CPU consumption.
- Memory consumption.
- Allocation behavior.
- Execution duration.
- Post-execution resource retention.
- Failed and incomplete operations.

Resource measurements MUST
remain attributable to their
execution environment.

Mandatory resource limits
MUST be defined before the
corresponding qualification
conclusion is issued.

---

## 41. Performance and Correctness Separation

The following are separate
engineering measurements:

    OPERATIONS PER SECOND

    OPERATION COMPLETION LATENCY

    CONCURRENT PARTICIPANT COUNT

    MEMORY ALLOCATION COST

    CANONICAL EFFECT CORRECTNESS

    HISTORY VERIFICATION RESULT

Higher throughput does not
independently establish stronger
semantic correctness.

A performance optimization MUST
NOT weaken an applicable mandatory
correctness requirement.

A successful benchmark does not
replace semantic qualification.

Performance claims require the
separate evidence framework
established for VRP runtime
performance.

---

## 42. Concurrent Outcome Accounting

Each evaluation campaign
SHOULD reconcile its actual
operation outcomes.

Relevant categories include:

    OPERATIONS_INVOKED

    OPERATIONS_COMPLETED

    OPERATIONS_PENDING

    OPERATIONS_FAILED

    OPERATIONS_UNATTRIBUTED

    CANONICAL_EFFECTS_OBSERVED

    HISTORIES_VERIFIED

The record MUST define whether
failed operations are included
within completed operations.

Accounting categories MUST NOT
be combined in a manner that
double-counts outcomes.

Missing observations MUST remain
explicitly identified.

---

## 43. Acceptance Matrix

| Observed outcome | Verdict |
|---|---|
| Required history semantics and controls satisfied | PASS |
| Confirmed prohibited duplicate commitment | FAIL |
| Confirmed unauthorized canonical effect | FAIL |
| Confirmed precedence violation | FAIL |
| Confirmed incompatible authority outcome | FAIL |
| Confirmed prohibited history modification | FAIL |
| Confirmed cross-lifetime interference | FAIL |
| Mandatory progress requirement violated | FAIL for applicable liveness criterion |
| Mandatory resource limit violated | FAIL for applicable resource criterion |
| Required history observation unavailable | INCONCLUSIVE |
| Verification incomplete | INCONCLUSIVE |
| Required controls unsuccessful | INCONCLUSIVE |
| Required scenario not executed | NOT TESTED |
| Scenario outside declared scope | NOT APPLICABLE |

A confirmed mandatory contract
violation takes precedence
over otherwise positive results.

An overall PASS requires
satisfaction of all applicable
mandatory acceptance criteria.

---

## 44. Evidence Obligation Matrix

| Claim | Required evidence |
|---|---|
| Concurrent execution occurred | Actual overlapping operation observations |
| At-most-once commitment | Attributable canonical effect accounting |
| Semantic atomicity | Contract-consistent observable effects |
| Linearizability | Qualified operation history and legal sequential interpretation |
| Real-time precedence | Reliable ordering observations |
| Authority integrity | Applicable authorization and effect verification |
| Lifetime isolation | Qualified lifetime and operation attribution |
| Observation consistency | Contract-consistent combined observations |
| Race detection result | Attributable instrumented execution record |
| Liveness | Measured progress against declared requirements |
| Resource boundedness | Measurements against declared limits |
| Independent reproduction | Actual independent execution record |

A general test suite success
label does not replace these
claim-specific obligations.

---

## 45. Public Qualification Record

Each approved concurrency
qualification record SHOULD
contain:

    DOCUMENT_ID: VRP-PA-009

    EVIDENCE_ID:

    SCENARIO_ID:

    CLAIM_REFERENCES:

    INVARIANT_REFERENCES:

    CONTRACT_VERSION:

    IMPLEMENTATION_REFERENCE:

    EXECUTION_REFERENCE:

    EVALUATION_ENVIRONMENT_CLASS:

    QUALIFIED_OPERATION_DOMAIN:

    SEQUENTIAL_CONTRACT_REFERENCE:

    INITIAL_CONDITIONS_REFERENCE:

    CONFIGURED_CONCURRENT_ACTIVITY:

    OBSERVED_CONCURRENT_ACTIVITY:

    OBSERVED_OPERATION_COUNT:

    OBSERVED_COMPLETION_COUNT:

    OBSERVED_PENDING_COUNT:

    OBSERVED_OVERLAP_COUNT:

    ACTUAL_COMPLETED_REPETITIONS:

    OBSERVATION_HISTORY_REFERENCE:

    CANONICAL_EFFECT_VERIFICATION:

    REAL_TIME_PRECEDENCE_RESULT:

    PENDING_OPERATION_TREATMENT:

    SEMANTIC_ATOMICITY_RESULT:

    LINEARIZABILITY_RESULT:

    AUTHORITY_INTEGRITY_RESULT:

    SESSION_LIFETIME_RESULT:

    HISTORY_INTEGRITY_RESULT:

    RACE_DETECTION_RESULT:

    VALID_OPERATION_PROGRESS:

    RESOURCE_QUALIFICATION_RESULT:

    POSITIVE_CONTROL_RESULT:

    NEGATIVE_CONTROL_RESULT:

    OBSERVATION_COVERAGE:

    VERIFICATION_METHOD_REFERENCE:

    VERIFICATION_COMPLETION_STATUS:

    ARTIFACT_REFERENCE:

    ARTIFACT_INTEGRITY_REFERENCE:

    OVERALL_VERDICT:

    EVIDENCE_LEVEL:

    REPRODUCTION_STATUS:

    INDEPENDENT_EVALUATION_STATUS:

    LIMITATIONS:

This is a public assurance
record template.

It is not an internal runtime
structure, protocol message,
or implementation interface.

Unpopulated fields MUST NOT
be interpreted as successful
qualification outcomes.

---

## 46. Public Artifact Requirements

A stronger public concurrency
claim SHOULD be associated with
approved evidence artifacts.

Candidate artifact categories
include:

- Evaluation execution summary.
- Public operation contract.
- Approved abstract observation history.
- Canonical effect verification report.
- History verification result.
- Positive control results.
- Negative control results.
- Regression execution summary.
- Race detection summary.
- Artifact integrity manifest.
- Reproduction instructions.
- Explicit limitations.

The publication of these artifacts
remains subject to confidentiality
and disclosure approval.

This document does not establish
that the corresponding artifacts
have already been released.

---

## 47. Observation Abstraction Boundary

Approved public observation
histories MAY use abstract
operation references and
sanitized observation records.

The abstraction MUST preserve
the relationships required
for the corresponding verification.

In particular, abstraction MUST
NOT conceal a relevant:

- Duplicate canonical effect.
- Ordering contradiction.
- Authorization violation.
- Lifetime violation.
- Missing observation.
- Failed execution.
- Inconclusive result.

If confidentiality requirements
prevent publication of sufficient
verification information, the
affected public claim MUST
retain the corresponding limitation.

Confidentiality MUST NOT be
used as a substitute for
evidence sufficiency.

---

## 48. Evidence Authenticity

The following properties remain
distinct:

    ARTIFACT INTEGRITY

    EXECUTION AUTHENTICITY

    OBSERVATION COMPLETENESS

    SEMANTIC CORRECTNESS

    VERIFICATION INDEPENDENCE

A matching artifact digest
does not independently establish
that a recorded history originated
from an authentic execution.

A valid signature does not
independently establish that
the history is complete.

A successful verifier result
does not independently establish
that the supplied operation
model is correct.

Each assurance property requires
appropriate supporting evidence.

---

## 49. Evidence Promotion Gates

The evidence sufficiency levels
established in VRP-PA-006 remain
applicable.

| Level | Concurrency evidence requirement |
|---|---|
| E0 | Applicable correctness contract specified |
| E1 | Dedicated execution outcome reported |
| E2 | Attributable execution artifacts available |
| E3 | Applicable histories and controls verified |
| E4 | Separately attributable reproduction |
| E5 | Independent evaluation completed |

The dedicated public linearizability
claim MUST NOT receive a stronger
classification solely because
other engineering tests passed.

Promotion requires evidence
specific to the evaluated
operation domain.

---

## 50. Independent Evaluation Model

An authorized independent
evaluator SHOULD be able to
examine applicable concurrent
correctness properties through
approved evaluation interfaces.

Where supported, the evaluator
SHOULD be able to:

- Select permitted concurrent scenarios.
- Establish acceptance criteria.
- Observe applicable operation activity.
- Examine approved effect observations.
- Verify approved operation histories.
- Execute verification controls.
- Record negative findings.
- Report inconclusive outcomes.
- Produce independent conclusions.

Actual evaluation availability
remains subject to supported
interfaces and applicable
authorization.

---

## 51. Evaluator-Controlled Verification

The intended evaluation boundary
distinguishes:

    PUBLIC OPERATION CONTRACT

                |

                v

    AUTHORIZED CONCURRENT EVALUATION

                |

                v

    APPROVED OBSERVATION HISTORY

                |

                v

    SEMANTIC VERIFICATION

                |

                v

    SCOPED ENGINEERING VERDICT

This is an external evaluation
model.

It is not an internal runtime
architecture diagram.

The evaluator MUST NOT be
required to accept a runtime
success label as the sole
basis for concurrent correctness.

---

## 52. Falsification Conditions

A confirmed occurrence of any
applicable condition below
constitutes a relevant
counterexample:

1. Prohibited duplicate canonical
   commitment.

2. Unauthorized protected mutation.

3. Violation of mandatory
   real-time precedence.

4. An observed history admitting
   no legal sequential interpretation
   within a declared linearizable domain.

5. Prohibited partial canonical
   effect under an applicable
   atomicity contract.

6. Incompatible canonical authority
   where exclusivity is required.

7. Unauthorized cross-lifetime
   interference.

8. Prohibited canonical history
   modification.

9. Unauthorized session replacement
   during concurrent activity.

10. A mandatory coherent observation
    returning a prohibited combined
    outcome.

11. Violation of a declared
    mandatory progress requirement.

12. Violation of a declared
    mandatory resource limit.

13. Verification accepting a known
    noncompliant history.

14. A confirmed intermediate
    integrity violation concealed
    by a valid final observation.

Each counterexample MUST be
attributed to the specific
affected correctness property.

A liveness failure MUST NOT
automatically be represented
as a linearizability violation.

A verifier defect MUST NOT
automatically be represented
as a demonstrated runtime defect.

---

## 53. Counterexample Reporting

An independent finding SHOULD
identify:

    FINDING_REFERENCE

    CLAIM_REFERENCE

    INVARIANT_REFERENCE

    OPERATION_DOMAIN

    IMPLEMENTATION_REFERENCE

    EVALUATION_SCOPE

    EXPECTED_SEMANTICS

    OBSERVED_HISTORY

    ESTABLISHED_ORDERING_CONSTRAINTS

    OBSERVED_CANONICAL_EFFECTS

    PROPOSED_CONTRACT_VIOLATION

    VERIFICATION_RESULT

    SUPPORTING_EVIDENCE

    REPRODUCTION_STATUS

A valid black-box counterexample
does not become invalid merely
because the evaluator lacks
access to proprietary source code.

The engineering conclusion
MUST follow the applicable
evidence.

---

## 54. Remediation and Requalification

A confirmed concurrency
violation requires an
attributable engineering record.

Where remediation occurs,
the record SHOULD distinguish:

- Original implementation reference.
- Original counterexample.
- Affected operation contract.
- Original qualification outcome.
- Corrected implementation reference.
- Subsequent regression evidence.
- Subsequent semantic verification.
- Requalification outcome.
- Remaining limitations.

A corrected execution MUST NOT
retroactively convert the
original failed execution
into a successful result.

Historical evidence remains
part of the engineering record.

---

## 55. Prohibited Evidence Substitution

The following substitutions
are explicitly prohibited:

    RACE DETECTOR PASS
        as
    UNIVERSAL RACE FREEDOM

    RACE DETECTOR PASS
        as
    LINEARIZABILITY PROOF

    SUCCESSFUL FINAL STATE
        as
    VALID COMPLETE HISTORY

    CONFIGURED CONCURRENT ACTIVITY
        as
    OBSERVED OPERATION OVERLAP

    CONFIGURED REPETITION COUNT
        as
    ACTUAL COMPLETED REPETITIONS

    REJECTION RESPONSE
        as
    PROVEN CANONICAL EFFECT EXCLUSION

    SYNTHETIC VERIFICATION FIXTURE
        as
    CAPTURED RUNTIME EVIDENCE

    HIGH THROUGHPUT
        as
    SEMANTIC CORRECTNESS

    INTERNAL REGRESSION PASS
        as
    INDEPENDENT CERTIFICATION

Each stronger claim requires
appropriate supporting evidence.

---

## 56. Technical Reviewer Questions

### Does passing the race detector
prove linearizability?

No.

Linearizability requires a
defined operation contract
and verification of applicable
operation histories.

### Does successful concurrent
execution establish atomicity?

No.

The corresponding observable
effects must satisfy the
applicable atomicity contract.

### Can overlapping operations
produce different valid outcomes?

Yes.

Different outcomes may be
permitted when consistent
with the declared sequential
semantics and real-time
precedence.

### Can a valid final state conceal
a concurrency violation?

Yes.

A final observation alone may
not establish correctness
throughout the complete
execution history.

### Can linearizability be evaluated
without access to proprietary code?

Observable operation histories
can be evaluated against a
sufficiently defined external
contract.

The strength of the conclusion
depends on observation coverage
and verification quality.

### Does a finite successful
campaign prove all possible
execution schedules correct?

No.

Its conclusion remains bounded
by the evaluated histories
and applicable assumptions.

### Can an independent evaluator
disprove a concurrency claim?

Yes.

An attributable counterexample
within the declared operation
domain constitutes relevant
engineering evidence.

### Does this document establish
universal VRP linearizability?

No.

It establishes the public
qualification contract and
the evidence required for
scoped linearizability claims.

---

## 57. Foundational Engineering Reference

The public linearizability
terminology used in this
document is consistent with
the established distributed
and concurrent systems
engineering literature.

Reference:

Maurice P. Herlihy and
Jeannette M. Wing.

Linearizability: A Correctness
Condition for Concurrent Objects.

ACM Transactions on Programming
Languages and Systems.

Volume 12, Number 3,
July 1990, pages 463–492.

DOI:

https://doi.org/10.1145/78969.78972

This reference establishes
the foundational correctness
concept.

It does not establish that
VRP has been reviewed,
endorsed, or verified by
the referenced authors or ACM.

---

## 58. Comparative Engineering Boundary

Linearizability, atomicity,
concurrency safety, and
operation ordering are
established engineering
concepts.

This document does not claim
that these individual concepts
were invented by VRP.

The VRP assurance objective
is qualification of applicable
concurrent correctness
properties within its declared
continuity-first session
architecture.

Comparative superiority
requires equivalent evaluation
conditions and attributable
comparative evidence.

---

## 59. Protected Core Boundary

The following MAY be published
when approved for disclosure:

- Abstract operation contracts.
- Observable correctness requirements.
- Approved aggregate measurements.
- Approved abstract operation histories.
- Public acceptance criteria.
- Verification control results.
- Falsification conditions.
- Evidence classifications.
- Independent evaluation findings.
- Explicit limitations.

The following remain confidential:

- Proprietary concurrency algorithms.
- Internal synchronization mechanisms.
- Internal linearization mechanisms.
- Internal memory ownership models.
- Confidential state representations.
- Internal operation sequencing logic.
- Private runtime interfaces.
- Protected source code.
- Confidential execution traces.
- Internal authority mechanisms.
- Cryptographic implementation details.
- Wire-level implementation details.
- Private infrastructure configuration.

Public assurance establishes
what must be demonstrated.

It does not disclose how
the Protected Core achieves
the declared behavior.

---

## 60. Assurance Limitations

This document does not establish:

- Universal implementation correctness.
- Universal linearizability.
- Absence of every possible data race.
- Universal deadlock freedom.
- Universal starvation freedom.
- Unlimited concurrent scalability.
- Unlimited resource capacity.
- Exhaustive execution schedule coverage.
- Complete formal implementation proof.
- Independent third-party certification.

Every empirical qualification
remains bounded by its actual
operation domain, implementation
reference, execution conditions,
observation coverage, and
verification method.

---

## 61. Master Evidence Integration

The master claims-to-evidence
matrix MUST associate VRP-C11
with:

- Applicable invariant identifiers.
- Concurrency scenario identifiers.
- Qualified operation domains.
- Sequential contract references.
- Approved observation histories.
- Verification control results.
- Semantic verification outcomes.
- Race detection evidence.
- Resource qualification evidence.
- Evidence sufficiency levels.
- Reproduction records.
- Independent evaluation status.
- Known limitations.

Historical regression results
MUST remain distinguishable
from dedicated linearizability
qualification results.

No claim may receive a
qualification status stronger
than its supporting evidence.

---

## 62. Related Assurance Documents

- [Executive Engineering Assurance](VRP_EXECUTIVE_ENGINEERING_ASSURANCE.md)
- [Formal Continuity Invariants](VRP_FORMAL_CONTINUITY_INVARIANTS.md)
- [Session Identity Preservation](VRP_SESSION_IDENTITY_PRESERVATION.md)
- [Transport Independence](VRP_TRANSPORT_INDEPENDENCE.md)
- [Adversarial Validation Evidence](VRP_ADVERSARIAL_VALIDATION_EVIDENCE.md)
- [Replay and Duplicate Containment](VRP_REPLAY_AND_DUPLICATE_CONTAINMENT.md)
- [Authority and State Integrity](VRP_AUTHORITY_AND_STATE_INTEGRITY.md)
- [Recovery and Failure Semantics](VRP_RECOVERY_AND_FAILURE_SEMANTICS.md)

---

## 63. Final Engineering Declaration

    SESSION ≠ TRANSPORT

    Concurrent execution is not
    sufficient evidence of
    concurrent correctness.

    Absence of a detected race
    is not semantic proof.

    A valid final state does not
    establish a valid history.

    Every protected canonical
    effect must remain subject
    to its applicable contract.

    Overlapping operations must
    not authorize prohibited
    duplicate commitment.

    Recovery must not conceal
    concurrency violations.

    Authority must remain valid
    under qualified concurrent
    activity.

    Linearizability must be
    evaluated against declared
    operation semantics.

    Evidence must remain
    attributable.

    Counterexamples must remain
    visible.

    The claim is falsifiable.

    The verification contract
    is public.

    The Protected Core
    remains confidential.

---

**Veil Routing Protocol — VRP**

**Jumping VPN**

**Architect and Creator: Vitalijus Riabovas**

**22 concurrency qualification scenarios.**

**14 explicit falsification conditions.**

**6 illustrative operation histories.**

**Positive and negative verification controls.**

**Semantic correctness beyond race detection.**

**Canonical integrity beyond successful execution.**

**Observable correctness. Protected implementation.**

**End of document — VRP-PA-009**
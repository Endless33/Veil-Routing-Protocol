# VRP Independent Black-Box Verification

## Veil Routing Protocol — Jumping VPN

**Document ID:** VRP-PA-013
**Version:** 1.0
**Classification:** PUBLIC
**Status:** Independent Evaluation and Falsification Contract
**Author:** Vitalijus Riabovas
**Protected Core:** CONFIDENTIAL

---

## 1. Executive Statement

A proprietary implementation must not
require unconditional trust in its author.

Observable engineering claims must be
subject to meaningful technical examination.

Veil Routing Protocol establishes:

    SESSION ≠ TRANSPORT

The independent evaluation framework
establishes:

    IMPLEMENTATION CONFIDENTIALITY
        !=
    BEHAVIORAL UNVERIFIABILITY

The objective of black-box evaluation
is to determine whether an identified
implementation satisfies declared
observable contracts under independently
selected and authorized conditions.

The evaluator must be permitted to
reach positive, negative, or inconclusive
engineering conclusions.

The Protected Core remains confidential.

---

## 2. Purpose

This document establishes the public
contract for independent black-box
evaluation of VRP.

Its objectives include:

- Independent observation.
- Evaluator-controlled scenario selection.
- Fresh execution attribution.
- Observable continuity qualification.
- Security outcome verification.
- Independent measurement.
- Counterexample submission.
- Reproducible evidence collection.
- Explicit trust boundaries.
- Protection of intellectual property.

The document defines an evaluation
contract rather than claiming that
every described evaluation capability
is currently deployed or qualified.

---

## 3. Fundamental Evaluation Principle

The evaluator is not required to accept:

- Author reputation.
- Architectural terminology.
- Marketing statements.
- Project-generated success labels.
- Prerecorded demonstrations.
- Unsupported performance claims.
- Unqualified security assertions.

The evaluator SHOULD reach conclusions
from attributable observations and
applicable acceptance criteria.

A successful evaluation must be
technically defensible.

A failed evaluation must remain
technically reportable.

---

## 4. Primary Assurance Claims

This document primarily supports:

    VRP-C15 — Reproducible external
              verification.

    VRP-C12 — Evidence integrity
              and provenance.

It additionally establishes evaluation
requirements for the remaining
declared VRP assurance claims.

The applicability of each claim
depends on the available external
observation surface.

---

## 5. Independent Evaluation Model

The public evaluation relationship is:

    EVALUATOR
        |
        v
    AUTHORIZED EVALUATION REQUEST
        |
        v
    IDENTIFIED SYSTEM UNDER TEST
        |
        v
    OBSERVABLE EXECUTION
        |
        v
    INDEPENDENT OBSERVATIONS
        |
        v
    EVIDENCE VERIFICATION
        |
        v
    EVALUATOR CONCLUSION

This is a conceptual assurance model.

It is not an internal runtime
architecture, protocol diagram,
or implementation specification.

---

## 6. System Under Test

The system under test MUST remain
attributable to an approved
implementation reference.

The evaluation record SHOULD identify:

- Implementation reference.
- Build or release reference.
- Applicable contract version.
- Supported evaluation capabilities.
- Evaluation environment class.
- Known limitations.
- Evaluation scope.

The evaluator MUST NOT assume that
results obtained from one implementation
automatically apply to another.

---

## 7. Black-Box Evaluation Definition

Black-box evaluation examines
observable system behavior without
requiring access to proprietary
implementation details.

Observable properties MAY include:

- Operation acceptance.
- Operation rejection.
- Application progress.
- Logical session continuity.
- Transport replacement.
- Recovery behavior.
- Observable canonical effects.
- Timing measurements.
- Resource measurements.
- Evidence verification outcomes.

The actual supported observation
surface MUST be established before
qualification.

---

## 8. What Black-Box Evaluation Can Establish

Where sufficient observations exist,
black-box evaluation can establish
bounded empirical conclusions concerning:

- Behavior under specified conditions.
- Observable contract compliance.
- Confirmed contract violations.
- Measured recovery behavior.
- Measured application progress.
- Observable duplicate-effect containment.
- Observable authority-related outcomes.
- Reproducibility of evaluated behavior.

Such conclusions remain specific to
the evaluated implementation,
conditions, and observation coverage.

---

## 9. What Black-Box Evaluation Cannot Establish

Black-box evaluation alone does not
necessarily establish:

- Complete implementation correctness.
- Absence of hidden implementation defects.
- Universal security.
- Absence of all side channels.
- Complete internal state integrity.
- Universal linearizability.
- Complete cryptographic implementation safety.
- Correctness under every possible input.
- Correctness under every possible schedule.

Some claims may require additional
authorized evidence or specialized
implementation-level assessment.

Unobservable properties MUST remain
unqualified unless sufficient
alternative evidence is available.

---

## 10. Evaluation Independence Dimensions

Independence is not a single
unqualified property.

The evaluation SHOULD distinguish:

    ORGANIZATIONAL_INDEPENDENCE

    SCENARIO_SELECTION_INDEPENDENCE

    EXECUTION_CONTROL_INDEPENDENCE

    OBSERVATION_INDEPENDENCE

    VERIFICATION_INDEPENDENCE

    CONCLUSION_INDEPENDENCE

An evaluator may possess independence
in one dimension while relying on
project-controlled infrastructure
in another.

The actual independence boundaries
MUST be documented.

---

## 11. Evaluation Control Classification

| Class | Description |
|---|---|
| BB-C0 | Prerecorded demonstration |
| BB-C1 | Project-controlled execution |
| BB-C2 | Externally observed execution |
| BB-C3 | Evaluator-selected authorized conditions |
| BB-C4 | Evaluator-controlled execution and observation |
| BB-C5 | Independently reproduced execution |

These classifications describe
evaluation control.

They do not automatically establish
evidence sufficiency levels E0–E5.

The two classifications MUST remain
separate.

---

## 12. Evaluation Authorization

Independent evaluation MUST occur
within an explicitly authorized scope.

The authorization SHOULD establish:

- Permitted evaluation objectives.
- Permitted scenario categories.
- Permitted evaluation interfaces.
- Evaluation duration.
- Applicable resource limits.
- Applicable data handling rules.
- Termination conditions.
- Finding submission procedures.

Authorization to evaluate observable
behavior does not constitute unrestricted
authorization to access proprietary
implementation or unrelated infrastructure.

---

## 13. Rules of Engagement

Evaluation rules MUST protect:

- The evaluator.
- The system under test.
- Unrelated systems.
- Other evaluation participants.
- Confidential information.
- Evidence integrity.

The evaluator MUST remain within
the authorized evaluation scope.

The project MUST NOT use evaluation
restrictions to silently redefine
a failed mandatory correctness
condition as a successful result.

Restrictions affecting verification
coverage MUST remain explicit.

---

## 14. Evaluation Capability Discovery

Before execution, the evaluator
SHOULD receive an approved description
of available evaluation capabilities.

Relevant categories MAY include:

    BASELINE_EXECUTION

    TRANSPORT_DISTURBANCE

    CONTINUITY_OBSERVATION

    REPLAY_EVALUATION

    DUPLICATE_EFFECT_EVALUATION

    AUTHORITY_OUTCOME_EVALUATION

    RECOVERY_EVALUATION

    CONCURRENT_OPERATION_EVALUATION

    PERFORMANCE_MEASUREMENT

    EVIDENCE_VERIFICATION

Unsupported capabilities MUST remain
distinguishable from supported
but unexecuted capabilities.

This list does not assert the
current availability of every
listed capability.

---

## 15. Pre-Evaluation Agreement

Before a dedicated qualification,
the parties SHOULD establish:

- Evaluated implementation.
- Applicable contract version.
- Evaluation scenarios.
- Mandatory acceptance criteria.
- Required observations.
- Evaluation limitations.
- Resource constraints.
- Evidence ownership.
- Permitted publication scope.
- Counterexample handling process.

Acceptance criteria SHOULD be
established before the relevant
execution begins.

They MUST NOT be retroactively
weakened merely to obtain PASS.

---

## 16. Evaluator-Selected Conditions

Where supported, the evaluator
SHOULD be able to select permitted
evaluation conditions independently.

Relevant choices MAY include:

- Scenario order.
- Workload characteristics.
- Permitted disturbance parameters.
- Repetition count.
- Observation duration.
- Applicable measurement criteria.
- Permitted compound conditions.

Evaluator-selected conditions reduce
dependence on exclusively
project-selected demonstrations.

They do not independently eliminate
all possible forms of evaluation bias.

---

## 17. Fresh Execution Requirement

A dedicated evaluator-controlled
evaluation SHOULD establish that
the observed result corresponds
to the current evaluation request.

The evidence SHOULD associate:

    EVALUATOR_REQUEST_REFERENCE

    SELECTED_SCENARIO

    SELECTED_CONDITIONS

    OBSERVED_EXECUTION

    OBSERVATION_INTERVAL

    RETURNED_EVIDENCE

A previously recorded successful
execution MUST NOT be presented
as a newly requested execution.

Freshness attribution MUST remain
subject to an explicit trust model.

---

## 18. Evaluator Challenge Binding

Where supported by the evaluation
environment, the evaluator MAY
introduce a fresh public evaluation
reference or permitted workload marker.

The evaluator SHOULD be able to
determine whether relevant observations
correspond to the current challenge.

A returned reference alone is
insufficient to establish that
the intended workload executed.

Challenge attribution requires
corresponding observable behavior.

This requirement describes an
external verification objective.

It does not specify a proprietary
challenge-response mechanism.

---

## 19. Prerecorded Demonstration Boundary

A prerecorded demonstration MAY
provide useful engineering context.

It MUST remain classified as
a demonstration.

The following substitution is
prohibited:

    PRERECORDED DEMONSTRATION
        as
    FRESH INDEPENDENT EXECUTION

The evaluator SHOULD be able to
distinguish current observations
from previously generated artifacts.

---

## 20. Evaluation Baseline

Before disturbance qualification,
the evaluator MUST establish an
applicable valid baseline.

Relevant observations include:

- Successful permitted operation.
- Established observation scope.
- Valid initial application progress.
- Applicable logical identity reference.
- Applicable effect accounting.
- Applicable integrity observations.

A failed or ambiguous baseline
MUST prevent unsupported
qualification promotion.

A system that rejects every
operation cannot establish
meaningful security effectiveness
through rejection counts alone.

---

## 21. Observation Oracle

An observation oracle is a
qualified evaluation method used
to distinguish relevant compliant
and noncompliant outcomes.

An oracle SHOULD establish:

- The property being observed.
- The expected compliant outcome.
- The expected noncompliant outcome.
- Required observations.
- Positive control behavior.
- Negative control behavior.
- Observation limitations.

An oracle MUST NOT merely repeat
an unqualified success assertion
produced by the system under test.

Oracle independence and trust
assumptions MUST remain explicit.

---

## 22. Oracle Qualification

Before relying on an oracle,
the evaluator SHOULD establish
that it can distinguish:

    VALID BEHAVIOR

    INVALID BEHAVIOR

    INSUFFICIENT OBSERVATION

The following outcomes MUST
remain distinguishable:

    PASS

    FAIL

    INCONCLUSIVE

An oracle that cannot recognize
a relevant known-invalid fixture
MUST NOT receive unrestricted
verification authority.

---

## 23. Independent Session Identity Verification

The primary continuity evaluation
objective is preservation of the
same logical session within the
applicable lifetime.

The evaluator MUST distinguish:

    LOGICAL_SESSION_CONTINUITY

    TRANSPORT_RESTORATION

    APPLICATION_RESTORATION

    SESSION_RECREATION

The following observations are
insufficient in isolation:

- Unchanged process identifier.
- Unchanged application identifier.
- Repeated session identifier.
- Restored socket communication.
- Successful reconnection.
- Resumed application traffic.

A qualified identity oracle MUST
distinguish preservation from
replacement within its declared
observation scope.

VRP-PA-003 remains applicable.

---

## 24. Session Recreation Negative Control

Where supported, the evaluation
SHOULD include an approved negative
control representing session recreation
rather than continuity preservation.

The identity oracle SHOULD recognize
the distinction even when superficial
observable identifiers remain similar.

Expected classification:

    ORIGINAL_LOGICAL_SESSION:
        NOT PRESERVED

    APPLICATION_CONNECTIVITY:
        MAY BE RESTORED

    CONTINUITY_QUALIFICATION:
        NOT PASS

This is a required evaluation
control objective.

It is not a reported completed
VRP execution.

---

## 25. Transport Independence Verification

Transport independence evaluation
SHOULD establish:

1. A valid initial logical session.
2. A confirmed transport disturbance
   or authorized replacement.
3. Observable post-transition behavior.
4. Qualified logical identity evidence.
5. Applicable integrity observations.
6. Applicable application progress.

The actual transport change MUST
be independently attributable.

A configured disturbance does not
establish that the disturbance
occurred.

A successful transport transition
does not independently establish
logical session continuity.

VRP-PA-004 remains applicable.

---

## 26. Repeated Transition Evaluation

Where supported, an evaluator MAY
request repeated transport or endpoint
changes under authorized conditions.

The evaluation SHOULD record:

    TRANSITIONS_REQUESTED

    TRANSITIONS_OBSERVED

    TRANSITIONS_COMPLETED

    TRANSITIONS_FAILED

    IDENTITY_OBSERVATIONS

    APPLICATION_PROGRESS

    INTEGRITY_OBSERVATIONS

    UNRESOLVED_TRANSITIONS

The evaluation MUST distinguish
the configured transition cadence
from the actual observed cadence.

A final successful observation
does not independently establish
correctness throughout every
intermediate transition.

---

## 27. Replay Containment Verification

Replay evaluation SHOULD establish
whether repeated presentations
produce prohibited observable effects.

Relevant observations include:

- Original permitted operation.
- Original applicable effect.
- Repeated presentation count.
- Observed rejection outcomes.
- Observable subsequent effects.
- Applicable canonical effect accounting.
- Observation coverage.

A rejection response alone does
not establish absence of an
unauthorized canonical effect.

Where effect observability is
insufficient, the corresponding
semantic claim remains inconclusive.

VRP-PA-006 remains applicable.

---

## 28. Duplicate Commit Verification

Where the applicable operation
contract permits at most one
canonical commitment, the evaluator
SHOULD establish whether repeated
presentations result in additional
prohibited commitments.

Conceptually:

    C(O) <= 1

Where:

    O =
        An operation within its
        applicable semantic scope.

    C(O) =
        Observable canonical commitment
        count under a qualified
        effect observation method.

This is an external correctness
condition.

It does not disclose the internal
commitment mechanism.

---

## 29. Retry After Uncertain Completion

An evaluator MAY examine permitted
retry behavior where an earlier
operation completion is uncertain.

The evaluation MUST distinguish:

- A repeated presentation.
- A newly authorized operation.
- A repeated response.
- A repeated canonical effect.
- An unresolved original completion.

A retry MUST NOT automatically
be classified as a duplicate
canonical commitment.

The applicable operation contract
determines the permitted outcome.

Missing effect observations MUST
remain unresolved.

---

## 30. Authority Integrity Verification

Authority-related evaluation SHOULD
examine observable outcomes under
authorized test conditions involving:

- Valid authority.
- Obsolete authority.
- Conflicting authority.
- Unauthorized operation context.
- Prohibited state regression.

The evaluation SHOULD distinguish:

    REQUEST_REJECTION

    OBSERVABLE_PROTECTED_EFFECT

    AUTHORITY_CONTRACT_RESULT

A rejection label does not
independently establish preservation
of protected canonical state.

The relevant effect observation
method MUST be qualified.

VRP-PA-007 remains applicable.

---

## 31. Lifetime Isolation Verification

Where supported, an evaluator
SHOULD examine whether observations
associated with an obsolete logical
lifetime can produce prohibited
effects in a subsequent lifetime.

The evaluation MUST establish
the relevant lifetime distinction.

Superficial identifier equality
MUST NOT substitute for qualified
lifetime identity.

The evaluator SHOULD record both
operation outcomes and applicable
protected effect observations.

---

## 32. Recovery Verification

Recovery qualification SHOULD
distinguish:

    DISTURBANCE_OCCURRENCE

    COMMUNICATION_RESTORATION

    APPLICATION_PROGRESS_RESTORATION

    LOGICAL_IDENTITY_VERIFICATION

    CANONICAL_INTEGRITY_VERIFICATION

Each observation MUST remain
separately attributable.

Recovery of communication does
not independently establish
preservation of logical session
identity or canonical history.

VRP-PA-008 remains applicable.

---

## 33. Complete Communication Interruption

During complete communication
interruption, delivery across
the interrupted path cannot
be assumed.

The evaluation SHOULD distinguish:

- Preservation of applicable state.
- Absence of communication progress.
- Restoration after interruption.
- Logical identity verification.
- Subsequent application progress.

The continuity contract MUST NOT
be interpreted as a claim of
physical communication through
an unavailable path.

---

## 34. Recovery Timing

An independent evaluator SHOULD
be able to measure supported
recovery intervals using declared
external observation boundaries.

Relevant measurements MAY include:

- Actual disturbance duration.
- Communication restoration delay.
- Application restoration delay.
- Identity verification delay.
- Integrity verification delay.

A measurement MUST identify its
start and completion conditions.

Different recovery measurements
MUST NOT be treated as equivalent.

---

## 35. Concurrent Operation Evaluation

Where supported, an evaluator
MAY examine permitted overlapping
operations.

The evidence SHOULD establish:

- Operation invocation boundaries.
- Operation completion boundaries.
- Actual operation overlap.
- Applicable operation outcomes.
- Observable canonical effects.
- Applicable real-time precedence.
- Incomplete operation observations.

Concurrent execution alone does
not establish linearizability.

The evaluated operation domain
and sequential specification
MUST be explicitly defined.

VRP-PA-009 remains applicable.

---

## 36. External Real-Time Precedence

An evaluator does not necessarily
require access to internal runtime
clocks to establish externally
observable precedence.

For operations X and Y:

    Completion(X) < Invocation(Y)

establishes a precedence constraint
where the observation method
provides sufficient attribution
and temporal resolution.

If the relevant boundaries cannot
be reliably established, their
ordering MUST remain unresolved.

The evaluator MUST NOT invent
a total order from insufficient
observations.

---

## 37. Observable History Qualification

Where applicable, an observed
operation history SHOULD be
evaluated against a declared
sequential contract.

The evaluation MUST account for:

- Completed operations.
- Pending operations.
- Observable results.
- Observable effects.
- Real-time precedence.
- Applicable operation semantics.

A positive conclusion MUST remain
specific to the evaluated operation
domain and observed history.

It MUST NOT be expanded into
a universal linearizability claim
for the complete protocol.

---

## 38. Autonomous Defense Evaluation

Where supported, autonomous defense
evaluation SHOULD examine:

- Handling of permitted adverse inputs.
- Observable rejection outcomes.
- Applicable protected effect containment.
- Valid operation progress.
- Bounded resource behavior.
- Applicable recovery behavior.

The evaluation MUST distinguish
security effectiveness from simple
rejection activity.

A defensive mechanism that prevents
all legitimate progress cannot
receive an availability PASS solely
because adverse inputs were rejected.

VRP-PA-010 remains applicable.

---

## 39. Fail-Closed Verification

A fail-closed evaluation SHOULD
establish whether invalid or
unauthorized operations produce
prohibited observable effects.

Relevant dimensions include:

    INVALID_OPERATION_OUTCOME

    PROTECTED_EFFECT_OBSERVATION

    SUBSEQUENT_VALID_OPERATION

    RESOURCE_QUALIFICATION

The system MUST NOT receive
an unrestricted security PASS
merely because an error response
was observed.

The applicable security contract
and observation coverage determine
the qualification verdict.

---

## 40. Availability Verification

Availability MUST remain distinct
from security correctness.

An evaluation MAY establish:

    SECURITY_CONTRACT:
        PASS

    APPLICATION_AVAILABILITY:
        FAIL

or:

    APPLICATION_AVAILABILITY:
        PASS

    SECURITY_CONTRACT:
        FAIL

These outcomes MUST remain
separately reportable.

An overall acceptance verdict
depends on all applicable
mandatory requirements.

---

## 41. Performance Verification

An evaluator SHOULD be able to
independently measure supported
performance properties.

Relevant categories include:

- Valid operation latency.
- Valid operation throughput.
- Application goodput.
- Recovery duration.
- Resource consumption.
- Sustained operation progress.

Measurements MUST remain associated
with the actual evaluated workload
and applicable correctness results.

VRP-PA-011 remains applicable.

---

## 42. Compound Evaluation

Separate successful evaluations
do not independently establish
correctness under combined conditions.

A compound evaluation SHOULD
establish actual overlap between
the relevant conditions.

Candidate dimensions include:

- Transport instability.
- Communication degradation.
- Concurrent operation activity.
- Recovery activity.
- Permitted adverse-input evaluation.
- Resource constraints.

Compound evaluation remains subject
to authorization and supported
evaluation capabilities.

---

## 43. Candidate Communication Conditions

The following values define
candidate laboratory conditions.

| Condition | Candidate values |
|---|---|
| Endpoint change cadence | Every 2 seconds |
| Packet loss | 30%, 50%, 80%, 90% |
| Complete interruption | 10, 30, 60 seconds |
| Elevated round-trip latency | 300–900 milliseconds |
| Delivery variation | Controlled jitter and reordering |
| Repeated transitions | Evaluator-selected permitted count |

These values are proposed
evaluation conditions.

They are not claims of completed
qualification or supported
production operating limits.

The actual disturbance conditions
MUST be measured or otherwise
adequately attributed.

---

## 44. Candidate Compound Condition

An authorized compound evaluation
MAY combine:

    REPEATED_ENDPOINT_CHANGES

    CONTROLLED_PACKET_LOSS

    TEMPORARY_COMMUNICATION_INTERRUPTION

    PERMITTED_REPLAY_EVALUATION

The evaluator SHOULD separately
record:

    LOGICAL_IDENTITY_RESULT

    CANONICAL_INTEGRITY_RESULT

    AUTHORITY_INTEGRITY_RESULT

    REPLAY_CONTAINMENT_RESULT

    APPLICATION_PROGRESS_RESULT

    RECOVERY_RESULT

    RESOURCE_QUALIFICATION_RESULT

A compound PASS requires all
applicable mandatory criteria
to be satisfied.

No completed compound qualification
is asserted by this document.

---

## 45. Independent Evaluation Scenario Registry

| Scenario | Evaluation objective |
|---|---|
| IBV-001 | Valid execution baseline |
| IBV-002 | Evaluation capability attribution |
| IBV-003 | Fresh execution attribution |
| IBV-004 | Evaluator-selected conditions |
| IBV-005 | Positive oracle control |
| IBV-006 | Negative oracle control |
| IBV-007 | Session identity preservation |
| IBV-008 | Session recreation discrimination |
| IBV-009 | Transport replacement |
| IBV-010 | Endpoint instability |
| IBV-011 | Repeated transport transitions |
| IBV-012 | Controlled communication degradation |
| IBV-013 | Temporary communication interruption |
| IBV-014 | Recovery qualification |
| IBV-015 | Replay containment |
| IBV-016 | Duplicate commit exclusion |
| IBV-017 | Retry after uncertain completion |
| IBV-018 | Obsolete authority rejection |
| IBV-019 | Conflicting authority outcome |
| IBV-020 | Prohibited state regression |
| IBV-021 | Session lifetime isolation |
| IBV-022 | Concurrent operation correctness |
| IBV-023 | Observable precedence qualification |
| IBV-024 | Fail-closed behavior |
| IBV-025 | Bounded defensive behavior |
| IBV-026 | Valid application progress |
| IBV-027 | Independent performance measurement |
| IBV-028 | Evidence integrity verification |
| IBV-029 | Independent evidence recalculation |
| IBV-030 | Compound disturbance qualification |
| IBV-031 | Independent execution reproduction |
| IBV-032 | Counterexample confirmation |

Registry inclusion establishes
an evaluation objective.

It does not establish completed
execution, current capability
availability, or qualification.

---

## 46. Claims-to-Evaluation Mapping

| Claim | Relevant evaluation scenarios |
|---|---|
| VRP-C01 | IBV-007, IBV-008, IBV-021 |
| VRP-C02 | IBV-009, IBV-010, IBV-011 |
| VRP-C03 | IBV-009, IBV-011 |
| VRP-C04 | IBV-015 |
| VRP-C05 | IBV-016, IBV-017 |
| VRP-C06 | IBV-018, IBV-021 |
| VRP-C07 | IBV-020 |
| VRP-C08 | IBV-016, IBV-020, IBV-030 |
| VRP-C09 | IBV-019 |
| VRP-C10 | IBV-013, IBV-014 |
| VRP-C11 | IBV-022, IBV-023 |
| VRP-C12 | IBV-028, IBV-029 |
| VRP-C13 | IBV-024 |
| VRP-C14 | IBV-025, IBV-026 |
| VRP-C15 | IBV-003, IBV-004, IBV-031, IBV-032 |

The mapping identifies candidate
evaluation relationships.

It does not establish that a
single successful scenario is
sufficient to qualify every
property of its associated claim.

---

## 47. Positive Evaluation Controls

A dedicated evaluation SHOULD
demonstrate that the observation
environment can recognize valid
behavior.

Required controls MAY include:

- Valid baseline operation.
- Valid application progress.
- Valid identity preservation.
- Valid permitted effect.
- Valid evidence artifact.
- Valid measurement record.

A positive control failure MUST
remain visible.

An evaluation that cannot recognize
valid behavior cannot establish
meaningful discrimination through
negative controls alone.

---

## 48. Negative Evaluation Controls

Approved synthetic or controlled
negative fixtures SHOULD establish
recognition of relevant invalid
conditions.

Candidate controls include:

- Session recreation.
- Duplicate canonical effect.
- Prohibited authority outcome.
- Missing required observation.
- Invalid temporal precedence.
- Modified evidence artifact.
- Incorrect execution attribution.
- Invalid outcome accounting.
- Unsupported evidence promotion.
- Incomplete evaluation presented
  as successful.

Synthetic fixtures MUST remain
distinguishable from actual
runtime observations.

---

## 49. Illustrative Evaluation A

### Successful reconnection without identity proof

This is a synthetic example.

Assumed observations:

    TRANSPORT_RESTORATION:
        OBSERVED

    APPLICATION_PROGRESS:
        OBSERVED

    LOGICAL_IDENTITY:
        UNVERIFIED

Expected verdict:

    TRANSPORT_RECOVERY:
        PASS WITHIN OBSERVED SCOPE

    SESSION_CONTINUITY:
        INCONCLUSIVE

Connectivity restoration MUST NOT
substitute for identity preservation.

---

## 50. Illustrative Evaluation B

### Recreated session

Assumed synthetic observations:

    APPLICATION_PROGRESS:
        RESTORED

    ORIGINAL_LOGICAL_SESSION:
        NOT PRESERVED

    CONTINUITY_REQUIRED:
        YES

Expected verdict:

    APPLICATION_RECOVERY:
        PASS

    SESSION_CONTINUITY:
        FAIL

A functioning replacement session
does not satisfy a mandatory
original-session preservation contract.

---

## 51. Illustrative Evaluation C

### Rejected replay with prohibited effect

Assumed synthetic observations:

    REPLAY_RESPONSE:
        REJECTED

    PROHIBITED_CANONICAL_EFFECT:
        CONFIRMED

Expected verdict:

    REPLAY_RESPONSE:
        REJECTION OBSERVED

    REPLAY_CONTAINMENT:
        FAIL

The observed effect takes precedence
over the rejection label when
evaluating the semantic contract.

---

## 52. Illustrative Evaluation D

### Fresh reference without execution attribution

Assumed synthetic observations:

    EVALUATOR_REFERENCE:
        RETURNED

    CURRENT_WORKLOAD_EXECUTION:
        UNVERIFIED

    OBSERVATION_ATTRIBUTION:
        INSUFFICIENT

Expected verdict:

    FRESH_EXECUTION:
        INCONCLUSIVE

Returning an evaluator reference
does not independently establish
fresh execution.

---

## 53. Illustrative Evaluation E

### Invalid temporal interpretation

Assumed synthetic observations:

    OPERATION_X_COMPLETED:
        BEFORE OPERATION_Y_INVOCATION

    PROPOSED_SEQUENTIAL_HISTORY:
        Y BEFORE X

    REAL_TIME_PRECEDENCE_REQUIRED:
        YES

Expected verdict:

    PROPOSED_HISTORY:
        INVALID

The final linearizability verdict
depends on whether any other
legal sequential interpretation
exists for the complete observed
history.

An invalid proposed interpretation
alone does not establish that
every possible interpretation
is invalid.

---

## 54. Illustrative Evaluation F

### Missing effect observation

Assumed synthetic observations:

    INVALID_OPERATION_RESPONSE:
        REJECTED

    PROTECTED_EFFECT_OBSERVATION:
        UNAVAILABLE

Expected verdict:

    RESPONSE_BEHAVIOR:
        OBSERVED

    PROTECTED_STATE_INTEGRITY:
        INCONCLUSIVE

The evaluator MUST NOT infer
absence of protected mutation
from a rejection response alone.

---

## 55. Illustrative Evaluation G

### Independent confirmed violation

Assumed synthetic observations:

    EVALUATOR_INDEPENDENCE:
        ESTABLISHED

    IMPLEMENTATION_ATTRIBUTION:
        ESTABLISHED

    OBSERVATION_ORACLE:
        QUALIFIED

    MANDATORY_CONTRACT_VIOLATION:
        CONFIRMED

Expected verdict:

    AFFECTED_CONTRACT:
        FAIL

    INDEPENDENT_FINDING:
        VALID WITHIN EVALUATED SCOPE

Independent evaluation MUST permit
negative engineering conclusions.

---

## 56. Illustrative Evaluation H

### Qualified continuity observation

Assumed synthetic observations:

    BASELINE:
        PASS

    ACTUAL_TRANSPORT_CHANGE:
        ESTABLISHED

    IDENTITY_ORACLE:
        QUALIFIED

    LOGICAL_IDENTITY_PRESERVATION:
        VERIFIED

    APPLICABLE_INTEGRITY:
        VERIFIED

    MANDATORY_CONTROLS:
        PASS

Expected verdict:

    SESSION_CONTINUITY:
        PASS WITHIN EVALUATED SCOPE

This is an illustrative acceptance
example.

It is not a newly reported
VRP execution result.

---

## 57. Evaluation Acceptance Matrix

| Observed condition | Verdict |
|---|---|
| All mandatory criteria satisfied | PASS |
| Confirmed logical identity violation | FAIL |
| Confirmed prohibited canonical effect | FAIL |
| Confirmed mandatory authority violation | FAIL |
| Confirmed prohibited state regression | FAIL |
| Confirmed mandatory resource violation | FAIL for resource scope |
| Transport restored, identity unknown | INCONCLUSIVE for continuity |
| Rejection observed, effect unknown | INCONCLUSIVE for effect containment |
| Disturbance not established | INCONCLUSIVE |
| Required oracle not qualified | INCONCLUSIVE |
| Fresh execution not attributable | INCONCLUSIVE for fresh execution |
| Mandatory evaluation not executed | NOT TESTED |
| Justified scenario exclusion | NOT APPLICABLE |

A confirmed mandatory violation
MUST NOT be overridden by an
unrelated successful observation.

---

## 58. Evaluation Termination

An evaluation MAY require termination
because of:

- Authorization expiration.
- Resource constraints.
- Environment failure.
- Evaluation safety requirements.
- Unsupported evaluation conditions.
- Evaluator-requested termination.
- Confirmed mandatory violation.

The termination reason MUST
remain attributable.

An aborted evaluation MUST NOT
automatically receive PASS.

A confirmed violation observed
before termination MUST remain
part of the evaluation record.

---

## 59. Evaluation Outcome Accounting

The evaluation record SHOULD
reconcile:

    SCENARIOS_REQUESTED

    SCENARIOS_AUTHORIZED

    SCENARIOS_EXECUTED

    SCENARIOS_PASSED

    SCENARIOS_FAILED

    SCENARIOS_INCONCLUSIVE

    SCENARIOS_ABORTED

    SCENARIOS_NOT_TESTED

The accounting method MUST define
whether aborted scenarios are
included in other categories.

Configured repetitions MUST NOT
be reported as completed repetitions.

Unsupported scenarios MUST remain
visible where relevant to the
evaluation scope.

---

## 60. Independent Evidence Collection

Where supported and authorized,
the evaluator SHOULD be able
to preserve approved evidence
independently.

Relevant evidence MAY include:

- Evaluator-selected conditions.
- External observation records.
- Operation outcome summaries.
- Independent timing measurements.
- Approved runtime evidence.
- Applicable verification results.
- Counterexample records.
- Evidence integrity references.

The evaluator SHOULD NOT be
required to rely exclusively on
a project-generated final verdict.

---

## 61. Observation Ownership

The evaluation record SHOULD
distinguish observations generated
by:

    THE SYSTEM UNDER TEST

    THE PROJECT OPERATOR

    THE EVALUATION ENVIRONMENT

    THE EXTERNAL EVALUATOR

    THE VERIFICATION METHOD

Observation origin affects the
applicable trust model.

An evaluator receiving a project
report does not thereby become
the independent originator of
its underlying observations.

---

## 62. Evidence Verification

Approved evaluation evidence
SHOULD satisfy the applicable
requirements of VRP-PA-012.

Relevant properties include:

- Implementation attribution.
- Execution attribution.
- Artifact integrity.
- Observation coverage.
- Evidence completeness.
- Verification controls.
- Semantic correctness.
- Independent evaluation attribution.

Artifact integrity and semantic
correctness MUST remain separate.

---

## 63. Independent Recalculation

Where sufficient approved data
is available, the evaluator
SHOULD be able to independently
recalculate:

- Operation totals.
- Rejection totals.
- Duplicate-effect totals.
- Completed transition totals.
- Recovery durations.
- Valid throughput.
- Latency distributions.
- Applicable acceptance decisions.

Recalculation of an existing
dataset is not independently
executed runtime reproduction.

---

## 64. Independent Verification Logic

An evaluator MAY use an
independently developed verification
method where the public evidence
contract provides sufficient
information.

The method SHOULD remain
independent of proprietary
runtime implementation.

The project SHOULD NOT require
exclusive reliance on a
project-controlled verifier
where independent verification
is technically feasible.

Different verification methods
MAY produce different conclusions.

Material disagreements MUST
remain technically examinable.

---

## 65. Verifier Disagreement

Where project and evaluator
verification results disagree,
the record SHOULD identify:

- Evaluated evidence.
- Applicable contract.
- Project verification method.
- Evaluator verification method.
- Differing conclusions.
- Relevant observation assumptions.
- Confirmed interpretation differences.
- Unresolved limitations.

A disagreement MUST NOT be
resolved solely by granting
authority to the project author.

The engineering conclusion
must follow the applicable
contract and qualified evidence.

---

## 66. Evaluation Reproduction

Reproduction requires a
separately attributable execution.

The reproduction SHOULD identify:

- Original evaluation reference.
- Reproduction reference.
- Implementation reference.
- Evaluation conditions.
- Environment differences.
- Applicable observation method.
- Reproduction result.
- Evaluator control classification.
- Remaining limitations.

Repeated verification of the
same artifact does not constitute
execution reproduction.

---

## 67. Reproduction Variability

Independent evaluations MAY
produce different results because
of material differences in:

- Evaluated implementation.
- Execution environment.
- Workload.
- Communication conditions.
- Observation method.
- Scheduling conditions.
- Measurement resolution.
- Evaluation scope.

A difference MUST NOT be
silently discarded.

The evaluator SHOULD determine
whether the difference represents
a contract violation, measurement
variation, environmental variation,
or unresolved evidence limitation.

---

## 68. Counterexample Submission

An external evaluator SHOULD
be able to submit a bounded
technical counterexample.

A counterexample SHOULD identify:

    FINDING_REFERENCE

    IMPLEMENTATION_REFERENCE

    EXECUTION_REFERENCE

    CLAIM_REFERENCE

    INVARIANT_REFERENCE

    SCENARIO_REFERENCE

    EXPECTED_BEHAVIOR

    OBSERVED_BEHAVIOR

    PROPOSED_VIOLATION

    SUPPORTING_EVIDENCE

    OBSERVATION_LIMITATIONS

    REPRODUCTION_STATUS

Access to proprietary source
code MUST NOT be a mandatory
condition for reporting a
qualified observable violation.

---

## 69. Counterexample Classification

A submitted finding MAY be
classified as:

    CONFIRMED_CONTRACT_VIOLATION

    CONFIRMED_EVIDENCE_DEFECT

    CONFIRMED_MEASUREMENT_DEFECT

    REPRODUCTION_REQUIRED

    INSUFFICIENT_OBSERVATION

    OUTSIDE_DECLARED_CONTRACT

    OUTSIDE_AUTHORIZED_SCOPE

    UNRESOLVED

Classification MUST be supported
by the applicable evidence.

A finding MUST NOT be rejected
merely because its conclusion
is unfavorable to the project.

---

## 70. Counterexample Resolution

A confirmed violation SHOULD
produce an attributable
engineering resolution record.

Relevant fields include:

- Original finding.
- Affected implementation.
- Affected claim.
- Affected qualification status.
- Remediation status.
- Corrected implementation reference.
- Subsequent evaluation evidence.
- Independent requalification status.
- Remaining limitations.

A subsequent successful execution
does not erase the original
confirmed violation.

---

## 71. Evaluator Conclusion Independence

The evaluator MUST retain
authority over their own
engineering conclusion within
the agreed evaluation scope.

The project MAY challenge:

- Evidence applicability.
- Measurement correctness.
- Contract interpretation.
- Observation completeness.
- Reproduction validity.

The project MUST NOT require
a positive conclusion as a
condition of technical acceptance
of an otherwise valid finding.

Confidentiality obligations
remain applicable to publication
of sensitive information.

---

## 72. Confidentiality and Negative Findings

Confidentiality requirements
MUST remain distinguishable
from engineering verdicts.

An evaluation agreement MAY
define appropriate handling of
sensitive findings.

However, confidentiality MUST
NOT convert:

    FAIL
        into
    PASS

or:

    INCONCLUSIVE
        into
    VERIFIED

Approved public summaries
SHOULD preserve the material
engineering meaning of findings
within the permitted disclosure
scope.

---

## 73. Evidence Sufficiency Levels

The established E0–E5
classification remains applicable.

| Level | Evidence requirement |
|---|---|
| E0 | Evaluation contract specified |
| E1 | Execution outcome reported |
| E2 | Attributable execution artifacts available |
| E3 | Applicable evidence and controls verified |
| E4 | Separately attributable reproduction |
| E5 | Independent evaluation completed |

An independent evaluator's
participation alone does not
automatically establish E5
for every declared claim.

Evidence promotion MUST remain
specific to the evaluated claim,
implementation, and observation
scope.

---

## 74. Current Public Evaluation Status

    DOCUMENT_REFERENCE:
        VRP-PA-013

    INDEPENDENT_EVALUATION_CONTRACT:
        SPECIFIED

    HISTORICAL_PROJECT_RESULTS:
        REPORTED

    HISTORICAL_EVIDENCE_LEVEL:
        E1

    DEDICATED_INDEPENDENT_REPORT:
        NOT EMBEDDED

    DEDICATED_INDEPENDENT_EVIDENCE_LEVEL:
        E0

    INDEPENDENT_THIRD_PARTY_QUALIFICATION:
        NOT ESTABLISHED BY THIS RECORD

    INDEPENDENT_CERTIFICATION:
        NOT CLAIMED

This classification describes
the evidence presented within
this document.

It does not establish that
additional restricted evaluation
artifacts do not exist.

---

## 75. Historical Evidence References

The historical references
established in VRP-PA-005
remain applicable.

| Reference | Project-reported outcome |
|---|---|
| AVE-001 | 9,999 replay presentations rejected |
| AVE-002 | 1,000 migrations with reported continuity preservation |
| AVE-003 | Approximately 41.6 seconds recovery |
| AVE-004 | Stale authority rejection |
| AVE-005 | Epoch rollback rejection |
| AVE-006 | Canonical rewrite rejection |
| AVE-007 | Evidence verifier PASS |

These outcomes provide historical
evaluation references.

They do not constitute newly
executed independent evaluations.

Their evidence classification
within this document remains E1.

---

## 76. Historical Result Reproduction Objectives

An authorized independent
evaluation MAY seek to reproduce
applicable historical outcomes.

Candidate reproduction objectives
include:

- Replay containment under repeated
  permitted presentations.
- Continuity during repeated
  transport transitions.
- Recovery under declared
  interruption conditions.
- Obsolete authority rejection.
- Prohibited state regression
  containment.
- Canonical integrity preservation.
- Independent evidence verification.

The evaluator MUST establish
the applicable reproduction
conditions.

Historical counts and durations
MUST NOT automatically become
mandatory universal acceptance
thresholds.

---

## 77. Independent Evaluation Report Template

    DOCUMENT_ID: VRP-PA-013

    EVALUATION_REFERENCE:

    EVALUATOR_REFERENCE:

    EVALUATOR_INDEPENDENCE_SCOPE:

    AUTHORIZATION_REFERENCE:

    IMPLEMENTATION_REFERENCE:

    BUILD_REFERENCE:

    CONTRACT_VERSION:

    EVALUATION_CONTROL_CLASS:

    SUPPORTED_CAPABILITIES:

    SELECTED_SCENARIOS:

    EVALUATOR_SELECTED_CONDITIONS:

    EXECUTION_REFERENCE:

    FRESH_EXECUTION_RESULT:

    ENVIRONMENT_CLASS:

    OBSERVATION_INTERVAL:

    OBSERVATION_METHOD:

    OBSERVATION_COVERAGE:

    BASELINE_RESULT:

    POSITIVE_CONTROL_RESULT:

    NEGATIVE_CONTROL_RESULT:

    IDENTITY_ORACLE_RESULT:

    ACTUAL_DISTURBANCE_REFERENCE:

    SESSION_IDENTITY_RESULT:

    TRANSPORT_INDEPENDENCE_RESULT:

    REPLAY_CONTAINMENT_RESULT:

    DUPLICATE_COMMIT_RESULT:

    AUTHORITY_INTEGRITY_RESULT:

    CANONICAL_HISTORY_RESULT:

    LIFETIME_ISOLATION_RESULT:

    CONCURRENT_CORRECTNESS_RESULT:

    FAIL_CLOSED_RESULT:

    DEFENSIVE_BEHAVIOR_RESULT:

    APPLICATION_PROGRESS_RESULT:

    RECOVERY_RESULT:

    PERFORMANCE_RESULT:

    RESOURCE_QUALIFICATION_RESULT:

    SCENARIOS_EXECUTED:

    SCENARIOS_PASSED:

    SCENARIOS_FAILED:

    SCENARIOS_INCONCLUSIVE:

    SCENARIOS_ABORTED:

    SCENARIOS_NOT_TESTED:

    EVIDENCE_REFERENCES:

    ARTIFACT_INTEGRITY_RESULT:

    EVIDENCE_PROVENANCE_RESULT:

    INDEPENDENT_VERIFICATION_RESULT:

    COUNTEREXAMPLE_REFERENCES:

    REPRODUCTION_STATUS:

    QUALIFICATION_VERDICT:

    EVIDENCE_LEVEL:

    INDEPENDENT_CONCLUSION:

    LIMITATIONS:

This template describes public
evaluation reporting obligations.

It is not an internal runtime
structure, private interface,
or proprietary protocol format.

Unpopulated fields MUST NOT
be interpreted as successful
evaluation outcomes.

---

## 78. Minimum Independent Evidence Bundle

A dedicated independent evaluation
SHOULD produce an approved
evidence bundle.

Candidate publication layout:

    evidence/
        independent-evaluation/
            EVALUATION_SCOPE.md
            IMPLEMENTATION_REFERENCE.json
            EVALUATOR_CONDITIONS.json
            EXECUTION_SUMMARY.json
            OBSERVATIONS.json
            CONTROL_RESULTS.json
            MEASUREMENTS.csv
            VERIFICATION_RESULTS.json
            FINDINGS.md
            INDEPENDENT_CONCLUSION.md
            LIMITATIONS.md
            SHA256SUMS

These names describe proposed
public artifact categories.

They do not assert that these
files already exist.

They do not describe the
Protected Core repository.

---

## 79. Independent Evaluation Readiness Gate

Before dedicated evaluation,
the applicable parties SHOULD
establish:

    AUTHORIZATION_DEFINED

    IMPLEMENTATION_ATTRIBUTED

    CONTRACT_VERSION_DEFINED

    CAPABILITIES_DECLARED

    EVALUATION_SCOPE_DEFINED

    ACCEPTANCE_CRITERIA_DEFINED

    OBSERVATION_METHOD_DEFINED

    ORACLE_QUALIFICATION_AVAILABLE

    EVIDENCE_HANDLING_DEFINED

    RESOURCE_LIMITS_DEFINED

    TERMINATION_CONDITIONS_DEFINED

    CONFIDENTIALITY_BOUNDARY_DEFINED

These are readiness requirements.

They are not completed readiness
results asserted by this document.

---

## 80. Independent Qualification Completion Gate

A completed independent
qualification SHOULD establish:

    ACTUAL_EXECUTION_ATTRIBUTED

    EVALUATOR_CONTROL_DOCUMENTED

    FRESHNESS_SCOPE_ESTABLISHED

    BASELINE_QUALIFIED

    REQUIRED_CONTROLS_EXECUTED

    OBSERVATION_COVERAGE_DOCUMENTED

    MANDATORY_OUTCOMES_EVALUATED

    OUTCOME_ACCOUNTING_RECONCILED

    EVIDENCE_INTEGRITY_VERIFIED

    FINDINGS_PRESERVED

    LIMITATIONS_DOCUMENTED

    INDEPENDENT_CONCLUSION_RECORDED

Completion of the evaluation
does not necessarily imply
a positive qualification verdict.

---

## 81. Protected Core Boundary

Independent black-box evaluation
does not require unrestricted
disclosure of:

- Proprietary source code.
- Internal algorithms.
- Internal state representations.
- Internal data structures.
- Internal synchronization mechanisms.
- Proprietary continuity mechanisms.
- Internal authority mechanisms.
- Confidential defensive logic.
- Internal cryptographic implementation.
- Private cryptographic material.
- Proprietary wire formats.
- Confidential infrastructure.
- Internal operational configuration.
- Unapproved diagnostic traces.

The evaluator receives only
the approved capabilities and
evidence required for the
authorized evaluation scope.

---

## 82. Evaluation Access Boundary

Access to an authorized
evaluation environment does
not constitute access to
the Protected Core.

The applicable authorization
SHOULD remain:

    EXPLICIT

    SCOPED

    BOUNDED

    REVOCABLE

    ATTRIBUTABLE

The document does not specify
internal access-control mechanisms
or confidential deployment
architecture.

Evaluation access MUST NOT
be interpreted as a transfer
of intellectual property rights.

---

## 83. Intellectual Property Boundary

Independent evaluation permits
technical examination of approved
observable behavior.

It does not automatically grant:

- Ownership of proprietary implementation.
- Rights to confidential source code.
- Rights to redistribute restricted artifacts.
- Rights to access unrelated infrastructure.
- Rights beyond applicable licenses
  and evaluation agreements.

The applicable legal agreements
and repository licenses determine
the actual rights and obligations.

This document does not replace
those agreements.

---

## 84. Evaluation Security Boundary

The evaluation environment
SHOULD preserve separation between
authorized evaluation capabilities
and confidential operational
resources.

The evaluator SHOULD NOT require
unrestricted operational privileges
to examine supported observable
contracts.

A limitation affecting an
evaluation objective MUST remain
visible in the qualification record.

A protected environment does
not independently establish
correctness of the system
under test.

---

## 85. Prohibited Evidence Substitution

The following substitutions
are explicitly prohibited:

    AUTHOR REPUTATION
        as
    ENGINEERING EVIDENCE

    DOCUMENTATION VOLUME
        as
    EMPIRICAL QUALIFICATION

    PRERECORDED DEMONSTRATION
        as
    FRESH EXECUTION

    EVALUATOR PRESENCE
        as
    INDEPENDENT EXECUTION CONTROL

    RETURNED CHALLENGE REFERENCE
        as
    VERIFIED EXECUTION

    RESTORED CONNECTION
        as
    PRESERVED LOGICAL SESSION

    REJECTION RESPONSE
        as
    VERIFIED EFFECT CONTAINMENT

    CONFIGURED DISTURBANCE
        as
    OBSERVED DISTURBANCE

    CONFIGURED REPETITIONS
        as
    COMPLETED REPETITIONS

    CONCURRENT EXECUTION
        as
    VERIFIED LINEARIZABILITY

    ARTIFACT DIGEST MATCH
        as
    SEMANTIC CORRECTNESS

    PROJECT VERIFIER PASS
        as
    INDEPENDENT THIRD-PARTY AUDIT

    ARTIFACT REVERIFICATION
        as
    EXECUTION REPRODUCTION

    EVALUATION CONFIDENTIALITY
        as
    EXEMPTION FROM FALSIFICATION

Every stronger conclusion requires
its own supporting evidence.

---

## 86. Falsification Conditions

A confirmed occurrence of any
applicable condition below
constitutes a relevant evaluation
or correctness violation:

1. Loss of required logical
   session identity.

2. Session recreation presented
   as identity preservation.

3. Prohibited duplicate canonical
   commitment.

4. Prohibited replay-induced effect.

5. Prohibited obsolete-authority
   effect.

6. Prohibited state regression.

7. Confirmed canonical history
   integrity violation.

8. Confirmed lifetime isolation
   violation.

9. Confirmed concurrent operation
   contract violation.

10. Confirmed mandatory fail-closed
    contract violation.

11. Confirmed mandatory defensive
    resource-limit violation.

12. Confirmed mandatory application
    progress violation.

13. Confirmed mandatory recovery
    requirement violation.

14. Prerecorded evidence presented
    as fresh execution.

15. Unsupported implementation
    attribution.

16. Concealed mandatory evaluation
    failure.

17. Invalid oracle accepting a
    known-invalid fixture.

18. Unsupported independence
    classification.

19. Unexecuted scenario presented
    as successful.

20. Unsupported evidence promotion.

21. Material observation limitation
    concealed from the conclusion.

22. Confirmed evidence modification
    presented as an original record.

23. Separate executions represented
    as one compound execution.

24. Mandatory acceptance criteria
    retroactively weakened to
    conceal a failure.

Each finding MUST remain
attributable to its actual
affected property.

An evaluation-method defect
does not automatically establish
a runtime correctness defect.

---

## 87. Technical Reviewer Questions

### Why is the implementation closed?

The project maintains a
confidential proprietary
implementation boundary.

The evaluation contract permits
examination of approved observable
behavior without requiring
unrestricted implementation disclosure.

### Can a closed-source protocol
### be independently evaluated?

Yes, for properties that can
be adequately observed through
qualified evaluation interfaces.

The strength of the conclusion
depends on observation coverage,
trust boundaries, and actual
evaluation independence.

### How can an evaluator distinguish
### continuity from reconnection?

Through a qualified logical
identity observation method
with appropriate positive and
negative controls.

Connectivity restoration alone
is insufficient.

### How can an evaluator verify
### replay containment?

By examining repeated permitted
presentations together with
qualified observation of the
relevant canonical effects.

A rejection counter alone
is insufficient.

### How can an evaluator examine
### linearizability without internal clocks?

Through externally observable
operation invocation and completion
boundaries where those boundaries
provide sufficient precedence
information.

The operation domain and
sequential specification must
also be defined.

### Can the evaluator choose
### evaluation conditions?

The evaluation contract requires
independent selection of permitted
conditions where the supported
environment provides that capability.

Actual capability availability
must be established before
execution.

### Can the evaluator reject
### a project-generated conclusion?

Yes.

The evaluator retains authority
over their own technical
conclusion within the agreed
evaluation scope.

### Can the evaluator report
### a confirmed negative finding?

Yes.

Negative findings constitute
legitimate engineering evidence.

### Does this document prove
### that independent evaluation
### has already occurred?

No.

It establishes the public
evaluation contract.

Actual independent qualification
requires an attributable
independent evaluation record.

### Does the evaluator receive
### access to the Protected Core?

No unrestricted access is
required by this contract.

The evaluation uses approved
observable capabilities and
evidence within the applicable
authorization boundary.

### Does successful black-box
### evaluation prove universal security?

No.

Its conclusion remains bounded
by the evaluated implementation,
conditions, observation coverage,
and applicable contracts.

---

## 88. Relationship to Established Methods

The evaluation approach is
consistent with general engineering
principles involving:

- Black-box testing.
- Requirements-based verification.
- Independent verification
  and validation.
- Experimental reproducibility.
- Counterexample-driven assessment.
- Explicit trust boundaries.
- Evidence-based assurance.

Informative references include:

1. NIST SP 800-115,
   Technical Guide to Information
   Security Testing and Assessment.

   https://doi.org/10.6028/NIST.SP.800-115

2. NIST SP 800-160 Volume 1,
   Revision 1, Engineering
   Trustworthy Secure Systems.

   https://doi.org/10.6028/NIST.SP.800-160v1r1

3. Herlihy and Wing,
   Linearizability: A Correctness
   Condition for Concurrent Objects.

   https://doi.org/10.1145/78969.78972

These references provide
methodological context.

Their inclusion does not
establish compliance, endorsement,
accreditation, or certification
of VRP by the referenced
organizations or authors.

---

## 89. External Engineering Challenge

The VRP evaluation framework
invites examination of its
declared observable claims.

An evaluator SHOULD be able
to challenge:

- Logical session preservation.
- Transport independence.
- Replay containment.
- Duplicate commit exclusion.
- Authority integrity.
- Recovery semantics.
- Concurrent correctness.
- Defensive behavior.
- Performance measurements.
- Evidence provenance.
- Evaluation independence.

The project does not require
unquestioned acceptance.

A qualified counterexample
constitutes engineering evidence.

Where sufficient observations
are unavailable, the affected
claim MUST remain limited.

---

## 90. Assurance Limitations

This document does not establish:

- Universal implementation correctness.
- Universal security.
- Unlimited adversarial resilience.
- Complete internal state observability.
- Complete cryptographic assurance.
- Universal recovery guarantees.
- Unlimited resource capacity.
- Independent certification.
- Completed independent qualification
  of every declared VRP claim.

The scope of every conclusion
MUST remain proportional to
its supporting evidence.

---

## 91. Master Evidence Integration

The master claims-to-evidence
matrix MUST associate independent
evaluation results with:

- Claim references.
- Invariant references.
- Evaluation scenario references.
- Implementation references.
- Execution references.
- Evaluation control classifications.
- Observation methods.
- Oracle qualification results.
- Evidence references.
- Qualification verdicts.
- Evidence sufficiency levels.
- Reproduction status.
- Evaluator independence scope.
- Confirmed findings.
- Remaining limitations.

No claim may receive a stronger
qualification status than its
actual supporting evidence.

---

## 92. Related Assurance Documents

- [Executive Engineering Assurance](VRP_EXECUTIVE_ENGINEERING_ASSURANCE.md)
- [Formal Continuity Invariants](VRP_FORMAL_CONTINUITY_INVARIANTS.md)
- [Session Identity Preservation](VRP_SESSION_IDENTITY_PRESERVATION.md)
- [Transport Independence](VRP_TRANSPORT_INDEPENDENCE.md)
- [Adversarial Validation Evidence](VRP_ADVERSARIAL_VALIDATION_EVIDENCE.md)
- [Replay and Duplicate Containment](VRP_REPLAY_AND_DUPLICATE_CONTAINMENT.md)
- [Authority and State Integrity](VRP_AUTHORITY_AND_STATE_INTEGRITY.md)
- [Recovery and Failure Semantics](VRP_RECOVERY_AND_FAILURE_SEMANTICS.md)
- [Concurrency and Linearizability](VRP_CONCURRENCY_AND_LINEARIZABILITY.md)
- [Autonomous Defense Boundaries](VRP_AUTONOMOUS_DEFENSE_BOUNDARIES.md)
- [Runtime Performance Evidence](VRP_RUNTIME_PERFORMANCE_EVIDENCE.md)
- [Evidence Provenance and Integrity](VRP_EVIDENCE_PROVENANCE_AND_INTEGRITY.md)

---

## 93. Final Engineering Declaration

    SESSION ≠ TRANSPORT

    CLAIM ≠ EVIDENCE

    CONFIDENTIALITY ≠ IMMUNITY

    The evaluator may select
    authorized evaluation conditions.

    The evaluator may observe
    actual execution.

    The evaluator may independently
    measure supported properties.

    The evaluator may examine
    approved evidence.

    The evaluator may challenge
    the verification method.

    The evaluator may reproduce
    supported evaluation scenarios.

    The evaluator may identify
    contract violations.

    The evaluator may reach
    a negative conclusion.

    The author is not the
    final authority over an
    independently established
    engineering fact.

    The applicable contract
    and qualified evidence
    determine the conclusion.

    The implementation remains
    confidential.

    The observable claims remain
    falsifiable.

    The evaluation contract
    remains public.

    Trust must not substitute
    for verification.

    Confidentiality must not
    substitute for correctness.

    Documentation must not
    substitute for execution.

---

**Veil Routing Protocol — VRP**

**Jumping VPN**

**Architect and Creator: Vitalijus Riabovas**

**32 independent evaluation scenarios.**

**24 explicit falsification conditions.**

**8 illustrative evaluation records.**

**15 assurance claims mapped to evaluation objectives.**

**Evaluator-selected authorized conditions.**

**Fresh execution attribution.**

**Independent observation and measurement.**

**Qualified continuity discrimination.**

**Independent counterexample submission.**

**Explicit evaluation control classifications.**

**Protected intellectual property.**

**Public contracts. Observable execution.**

**Independent scrutiny. Bounded conclusions.**

**End of document — VRP-PA-013**
# VRP Recovery and Failure Semantics

## Veil Routing Protocol — Jumping VPN

**Document ID:** VRP-PA-008
**Version:** 1.0
**Classification:** PUBLIC
**Status:** Evidence-Oriented Qualification Contract
**Author:** Vitalijus Riabovas
**Protected Core:** CONFIDENTIAL

---

## 1. Executive Statement

A communication system may recover network
connectivity while losing the original
logical session.

It may restore application delivery while
replacing previously established state.

It may report successful recovery while
violating an applicable authority or
integrity requirement.

These outcomes are not equivalent to
verified session continuity.

Veil Routing Protocol establishes the
following architectural principle:

    SESSION ≠ TRANSPORT

The engineering objective is preservation
of applicable logical session relationships
across qualified transport failures,
communication interruptions, and recovery
conditions.

Recovery MUST remain subject to the
applicable continuity, authority, lifecycle,
and canonical integrity contracts.

This document establishes measurable
qualification requirements and explicit
conditions under which a recovery claim
can be falsified.

The implementation responsible for
satisfying these requirements remains
confidential.

---

## 2. Assurance Claim

Primary claim:

    VRP-C10 — Controlled recovery semantics.

Supporting claims:

    VRP-C01 — Logical session identity.
    VRP-C02 — Transport independence.
    VRP-C03 — Controlled transport replacement.
    VRP-C04 — Replay containment.
    VRP-C05 — Duplicate commit rejection.
    VRP-C06 — Stale authority rejection.
    VRP-C07 — Epoch rollback rejection.
    VRP-C08 — Canonical history integrity.
    VRP-C09 — Deterministic authority resolution.
    VRP-C11 — Concurrent correctness.
    VRP-C12 — Evidence integrity.
    VRP-C13 — Fail-closed behavior.
    VRP-C14 — Bounded defensive behavior.

Recovery qualification requires evidence
appropriate to every applicable mandatory
correctness property.

A successful communication outcome MUST
NOT override a confirmed integrity violation.

---

## 3. Applicable Invariants

| Invariant | Recovery qualification property |
|---|---|
| INV-001 | Logical identity preservation |
| INV-002 | Transport independence |
| INV-003 | Controlled transport replacement |
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

---

## 4. Historical Engineering Evidence

The VRP project has previously reported
the following recovery-related outcomes:

| Evidence ID | Evaluation | Reported outcome |
|---|---|---|
| AVE-002 | Migration storm | 1,000 migrations with reported continuity preservation |
| AVE-003 | Blackout recovery | Approximately 41.6 seconds |
| AVE-004 | Stale authority handling | Rejection |
| AVE-005 | Epoch rollback handling | Rejection |
| AVE-006 | Canonical history rewrite | Rejection |
| AVE-007 | Evidence verification | PASS |

These are historical project-reported
engineering results referenced by
VRP-PA-005.

They are not newly executed evaluations.

Their evidence classification within
this document is:

    EVIDENCE_LEVEL = E1

The evidence sufficiency levels are
defined in VRP-PA-006.

Original execution artifacts are not
embedded in this document.

The historical results MUST NOT be
combined into a single recovery
execution unless their common
provenance is established.

---

## 5. Historical Recovery Measurement

The previously reported recovery
measurement is:

    EVIDENCE_ID: AVE-003

    REPORTED_RECOVERY_DURATION:
        APPROXIMATELY 41.6 SECONDS

    EVIDENCE_LEVEL:
        E1

    MEASUREMENT_START_DEFINITION:
        NOT ESTABLISHED BY THIS RECORD

    MEASUREMENT_END_DEFINITION:
        NOT ESTABLISHED BY THIS RECORD

    ORIGINAL_EXECUTION_ARTIFACTS:
        NOT EMBEDDED

    INDEPENDENT_REPRODUCTION:
        NOT ESTABLISHED BY THIS RECORD

The reported measurement is not
a hypothetical performance target.

However, its precise interpretation
requires the original measurement
definitions and execution context.

It MUST NOT be represented as:

- A guaranteed recovery deadline.
- A maximum tolerated blackout.
- A universal recovery duration.
- A production service-level agreement.
- Independent proof of session continuity.

Stronger qualification requires
attributable supporting evidence.

---

## 6. Fundamental Recovery Distinctions

The following properties MUST remain
independently observable:

    TRANSPORT AVAILABILITY

    LOGICAL SESSION IDENTITY

    SESSION LIFETIME

    CANONICAL AUTHORITY

    CANONICAL HISTORY

    APPLICATION PROGRESS

    RECOVERY COMPLETION

A change in one property does not
independently establish a corresponding
change in another.

In particular:

    TRANSPORT RECOVERY
        !=
    LOGICAL SESSION PRESERVATION

    APPLICATION RECOVERY
        !=
    CANONICAL INTEGRITY

    SUCCESSFUL RECONNECTION
        !=
    VERIFIED CONTINUITY

These distinctions are mandatory
throughout recovery qualification.

---

## 7. Abstract Failure Model

For external verification purposes:

    S = logical session identity

    L = logical session lifetime

    T = transport association

    A = canonical authority context

    H = committed canonical history

    P = application progress

    F = observed failure condition

These symbols describe conceptual
observation targets.

They do not represent actual internal
variables, runtime structures,
protocol messages, or implementation
mechanisms.

The failure model establishes what
must be observed.

It does not disclose how the
Protected Core processes failures.

---

## 8. Recovery Correctness Contract

For an authorized continuity-preserving
recovery within the same applicable
logical session lifetime:

    S(before) = S(after)

    L(before) = L(after)

Transport association MAY change:

    T(before) != T(after)

Canonical history MAY advance through
authorized operations.

Authority MAY change through permitted
authorization transitions.

However, recovery MUST NOT produce
prohibited canonical effects.

The verification objective is
preservation of applicable logical
relationships rather than equality
of every observable state attribute.

---

## 9. Failure Isolation Contract

Transport failure MUST NOT independently
authorize:

- Logical session replacement.
- Canonical history reconstruction.
- Invalid authority acceptance.
- Prohibited authority rollback.
- Duplicate canonical commitment.
- Unauthorized lifecycle transitions.
- Cross-lifetime interference.

A failed transport MAY interrupt
communication.

It MUST NOT independently establish
permission to violate canonical
correctness.

Explicitly authorized expiration
or termination remains permitted
under the applicable lifecycle
contract.

---

## 10. Failure Classification

The assurance framework distinguishes
the following evaluation categories:

| Failure class | Observable condition |
|---|---|
| F-01 | Transport unavailability |
| F-02 | Endpoint change |
| F-03 | Communication path loss |
| F-04 | Temporary network interruption |
| F-05 | Packet delivery degradation |
| F-06 | Increased communication latency |
| F-07 | Variable communication latency |
| F-08 | Packet duplication or reordering |
| F-09 | Concurrent operation disturbance |
| F-10 | Resource constraint |
| F-11 | Interrupted recovery |
| F-12 | Compound failure condition |

These are public evaluation categories.

Their inclusion does not establish
implementation support or completed
qualification for every failure class.

---

## 11. Complete Network Blackout

A complete network blackout is an
observed interval during which all
communication paths relevant to
the declared evaluation scope
are unavailable.

During that interval:

- Packet delivery MAY stop.
- Application progress MAY pause.
- Remote observation MAY become
  unavailable.
- Recovery completion MAY remain
  impossible.

VRP does not claim that information
can be transmitted without an
available communication path.

The relevant continuity objective
is preservation of applicable logical
session relationships within the
declared lifecycle and interruption
conditions.

Communication availability and
logical session validity are
separate qualification properties.

---

## 12. Partial Communication Failure

A partial communication failure
does not necessarily eliminate
all communication capability.

The evaluation MUST identify
the affected communication scope.

A partial failure MUST NOT be
reported as a complete blackout
without supporting evidence.

Qualification SHOULD distinguish:

- Affected communication paths.
- Remaining communication capability.
- Observed application progress.
- Logical session identity.
- Applicable canonical integrity.
- Recovery outcome.

The public record MUST accurately
describe the actual failure condition.

---

## 13. Recovery Observation Timeline

Recovery qualification requires
an attributable observation timeline.

The following conceptual events
define external measurement points:

    T0 = Valid baseline established.

    T1 = Failure onset observed.

    T2 = Failure condition confirmed.

    T3 = Required communication
         conditions restored.

    T4 = Transport recovery observed.

    T5 = Application progress restored.

    T6 = Session identity verified.

    T7 = Canonical integrity verified.

These are observation labels.

They are not internal runtime stages,
implementation transitions, or
proprietary execution sequences.

Their ordering MAY vary where the
applicable observation contract
permits it.

Unavailable observations MUST
remain explicitly identified.

---

## 14. Recovery Measurement Definitions

Where the corresponding events
are available, the evaluation MAY
calculate:

    Observed failure interval:

        D_failure = T3 - T1

    Transport restoration delay:

        D_transport = T4 - T3

    Application restoration delay:

        D_application = T5 - T3

    Identity verification delay:

        D_identity = T6 - T3

    Integrity verification delay:

        D_integrity = T7 - T3

These measurements represent
different observable properties.

They MUST NOT be substituted
for one another.

The applicable event definitions,
clock domain, and measurement
uncertainty MUST be documented.

A measurement MUST NOT be calculated
when its required endpoints cannot
be established reliably.

---

## 15. Recovery Timing Attribution

Recovery measurements SHOULD use
a suitable monotonic time reference
where supported.

Where observations originate from
different clock domains, the
evaluation MUST account for
clock alignment and uncertainty.

The evidence record SHOULD identify:

- Measurement reference.
- Measurement resolution.
- Observation source.
- Relevant event definitions.
- Clock alignment limitations.
- Measurement uncertainty.
- Missing observations.

A configured blackout duration
MUST NOT be substituted for the
actual observed interruption duration.

A configured recovery deadline
MUST NOT be substituted for an
observed recovery measurement.

---

## 16. Recovery Outcome Classification

The following outcomes MUST remain
distinguishable:

| Outcome | Interpretation |
|---|---|
| R-01 | Transport restored; identity verified |
| R-02 | Transport restored; identity unverified |
| R-03 | Application restored; identity replaced |
| R-04 | Identity preserved; communication unavailable |
| R-05 | Identity preserved; application progress delayed |
| R-06 | Recovery completed; integrity violation observed |
| R-07 | Recovery pending |
| R-08 | Authorized session termination |
| R-09 | Recovery failed |
| R-10 | Recovery outcome inconclusive |

These are conceptual assurance
classifications.

They do not represent internal
runtime states.

An R-06 outcome MUST NOT receive
an overall successful integrity
qualification verdict.

An R-02 outcome MUST NOT receive
a verified session continuity
verdict.

An R-08 outcome MUST NOT be
reported as preservation of
the terminated session.

---

## 17. Session Identity Verification

Recovery qualification MUST
distinguish preservation of the
original logical session from
creation of a replacement session.

The following observations are
insufficient when considered alone:

- Unchanged process identity.
- Continued process execution.
- Successful socket creation.
- Successful reconnection.
- Restored packet delivery.
- Repeated external identifier.
- Successful application response.
- Runtime-reported recovery success.

The identity verification method
MUST satisfy the requirements
defined in VRP-PA-003.

If identity preservation cannot
be distinguished from recreation,
the corresponding verdict MUST
remain INCONCLUSIVE.

---

## 18. Canonical History Verification

Recovery MUST preserve applicable
previously committed canonical
relationships.

A recovery evaluation MUST
distinguish:

- Authorized subsequent progress.
- Preserved committed relationships.
- Unauthorized history modification.
- Prohibited history replacement.
- Undocumented state reconstruction.

A successful final connection
does not independently establish
canonical history integrity.

A valid final state does not
excuse a confirmed intermediate
integrity violation.

The proprietary history representation
and recovery mechanisms remain
confidential.

---

## 19. Authority Integrity During Recovery

Recovery MUST remain subject to
the applicable authority contract.

The need to restore communication
MUST NOT independently authorize
otherwise prohibited canonical
effects.

Qualification MUST examine the
applicable authority relationships
before and after recovery.

Where temporal authority correctness
is required, relevant intermediate
observations MUST also be considered.

A successful recovery outcome
MUST NOT conceal:

- Acceptance of obsolete authority.
- Prohibited authority rollback.
- Incompatible canonical authority.
- Unauthorized protected mutation.

The applicable authority requirements
are defined in VRP-PA-007.

---

## 20. Replay Containment During Recovery

Recovery MUST NOT independently
authorize prohibited repeated
canonical commitment.

The applicable replay and duplicate
containment requirements remain
in effect throughout the qualified
recovery scope.

The evaluation MUST distinguish:

    REPEATED NETWORK DELIVERY

    REPEATED OPERATION PRESENTATION

    REPEATED CANONICAL COMMITMENT

A recovery operation that produces
a prohibited duplicate canonical
effect MUST receive a negative
verdict for the affected contract.

The relevant containment requirements
are defined in VRP-PA-006.

---

## 21. Interrupted Recovery

Recovery itself MAY encounter
additional communication failures.

A second failure occurring during
an incomplete recovery introduces
a distinct qualification condition.

The evaluation SHOULD establish:

- Original failure observation.
- Recovery progress observation.
- Subsequent failure observation.
- Applicable identity outcome.
- Authority integrity outcome.
- Canonical history outcome.
- Final recovery outcome.

A successful isolated recovery
does not establish correctness
under repeated interruption.

Interrupted recovery requires
separately attributable evidence.

---

## 22. Repeated Recovery Qualification

Repeated recovery activity MAY
introduce operational conditions
not present in a single recovery.

Qualification SHOULD evaluate:

- Number of observed failures.
- Number of observed recoveries.
- Actual interruption durations.
- Actual recovery measurements.
- Logical identity preservation.
- Canonical integrity.
- Authority integrity.
- Application progress.
- Resource consumption.
- Post-recovery stability.

A configured repetition count
is not proof of executed recovery
cycles.

Observed execution records are
required.

---

## 23. Concurrent Recovery Activity

Concurrent operations during
recovery MUST preserve the
applicable canonical contracts.

Relevant correctness properties
include:

- Canonical effect uniqueness.
- Valid operation ordering.
- Applicable authority exclusivity.
- Session lifetime isolation.
- Protected state integrity.

Where linearizability is claimed,
the corresponding operation
histories MUST satisfy the
applicable sequential semantics
and real-time precedence requirements.

A successful final recovery
does not independently establish
concurrent correctness.

---

## 24. Fail-Closed Recovery

When required recovery conditions
cannot be established, the system
MUST NOT produce prohibited
canonical effects.

Permitted outcomes MAY include:

- Deferred recovery.
- Rejected operations.
- Temporary communication interruption.
- Permitted diagnostic observations.
- Authorized session termination.
- Bounded defensive behavior.

Fail-closed correctness does not
imply that recovery will always
complete.

Security correctness and recovery
availability MUST be reported
separately.

---

## 25. Recovery Liveness Contract

Recovery progress depends on
explicit operating assumptions.

Relevant assumptions MAY include:

- Availability of a compatible
  communication path.
- Valid session lifetime.
- Required authorization conditions.
- Sufficient computational resources.
- Applicable infrastructure availability.
- Supported operating conditions.

A recovery liveness claim MUST
identify its applicable assumptions.

A recovery deadline MUST NOT be
claimed without evidence supporting
that deadline under the declared
conditions.

Safety requirements remain applicable
even when recovery liveness cannot
be established.

---

## 26. Positive Control Requirements

Before failure qualification,
the evaluation MUST establish
a valid operating baseline.

Required positive controls include:

    BASELINE_SESSION_VALID:
        VERIFIED

    BASELINE_AUTHORIZED_PROGRESS:
        VERIFIED

    BASELINE_IDENTITY_OBSERVATION:
        AVAILABLE

    BASELINE_INTEGRITY_OBSERVATION:
        AVAILABLE

    VERIFICATION_METHOD_READY:
        VERIFIED

These values define required
acceptance conditions.

They are not reported results
of a completed execution.

A system that never establishes
valid communication cannot receive
a positive recovery verdict merely
because no prohibited recovery
effect was observed.

---

## 27. Negative Control Requirements

The verification method MUST
distinguish successful recovery
from relevant noncompliant outcomes.

Approved verification fixtures
SHOULD evaluate recognition of:

- Session replacement presented
  as identity preservation.
- Missing required observations.
- Unauthorized canonical effects.
- Prohibited history modification.
- Invalid authority outcomes.
- Incomplete recovery records.

A verifier MUST NOT accept a
known noncompliant record as
a successful continuity result.

These controls evaluate the
verification mechanism.

They do not require modification
or disclosure of the Protected Core.

---

## 28. Qualification Scenario Registry

| Scenario | Evaluation objective |
|---|---|
| RFS-001 | Valid operating baseline |
| RFS-002 | Transport failure isolation |
| RFS-003 | Endpoint replacement recovery |
| RFS-004 | Partial communication failure |
| RFS-005 | Complete blackout |
| RFS-006 | Post-blackout transport restoration |
| RFS-007 | Post-blackout identity verification |
| RFS-008 | Canonical history preservation |
| RFS-009 | Authority integrity during recovery |
| RFS-010 | Replay containment during recovery |
| RFS-011 | Interrupted recovery |
| RFS-012 | Repeated recovery cycles |
| RFS-013 | Concurrent recovery activity |
| RFS-014 | Fail-closed recovery |
| RFS-015 | Recovery liveness |
| RFS-016 | Resource qualification |
| RFS-017 | Post-recovery stability |
| RFS-018 | Verification negative controls |
| RFS-019 | Compound failure qualification |
| RFS-020 | Independent reproduction |

Registry inclusion defines
an evaluation objective.

It does not establish that
the corresponding scenario
has been executed or qualified.

---

## 29. Proposed Blackout Qualification Matrix

The following durations define
candidate laboratory evaluation
conditions.

They are proposed test parameters,
not completed test results.

| Scenario | Intended interruption | Required evidence |
|---|---:|---|
| RFS-B01 | 10 seconds | Actual interruption and recovery observations |
| RFS-B02 | 30 seconds | Actual interruption and recovery observations |
| RFS-B03 | 60 seconds | Actual interruption and recovery observations |

Each scenario requires separate
verification of:

- Actual observed interruption.
- Transport restoration.
- Logical identity preservation.
- Applicable lifetime preservation.
- Canonical history integrity.
- Authority integrity.
- Application progress restoration.
- Recovery measurement definitions.

Current status within this document:

    EXECUTION_STATUS:
        NOT ESTABLISHED

    QUALIFICATION_STATUS:
        NOT CLAIMED

The proposed durations MUST NOT
be represented as guaranteed
operating limits.

---

## 30. Proposed Recovery Repetition Matrix

The following repetition counts
define candidate qualification
conditions.

| Scenario | Intended recovery cycles |
|---|---:|
| RFS-R01 | 1 |
| RFS-R02 | 10 |
| RFS-R03 | 100 |

These are proposed evaluation
parameters.

They do not represent previously
executed recovery counts.

Each completed evaluation MUST
record actual observed cycles,
rather than relying on the
configured repetition count.

A stronger qualification claim
requires attributable execution
artifacts and applicable
verification results.

---

## 31. Recovery Distribution Measurements

Where sufficient repeated observations
are available, recovery performance
SHOULD be reported using appropriate
statistical summaries.

Relevant measurements include:

- Number of attempted evaluations.
- Number of completed evaluations.
- Number of failed evaluations.
- Number of inconclusive evaluations.
- Minimum observed recovery duration.
- Median observed recovery duration.
- Applicable percentile measurements.
- Maximum observed recovery duration.
- Measurement uncertainty.

Percentile measurements MUST
identify the sample count and
calculation method.

Small samples MUST NOT be
represented as statistically
strong tail-latency evidence.

Failed and incomplete recoveries
MUST NOT be silently excluded
from the reported outcome counts.

---

## 32. Recovery Success Accounting

A recovery campaign SHOULD report:

    N_attempted

    N_pass

    N_fail

    N_inconclusive

    N_not_applicable

The outcome categories MUST
be mutually exclusive within
the declared accounting scope.

The total MUST reconcile with
the attempted evaluation count.

Where applicable:

    N_attempted =
        N_pass
        + N_fail
        + N_inconclusive
        + N_not_applicable

Unexecuted planned evaluations
MUST be recorded separately.

A reported success percentage
MUST identify its denominator.

The evaluation MUST NOT remove
failed or inconclusive executions
solely to improve the reported
success rate.

---

## 33. Resource Qualification

Recovery correctness does not
independently establish bounded
resource consumption.

Relevant qualification measurements
include:

- Baseline CPU consumption.
- Recovery-period CPU consumption.
- Baseline memory consumption.
- Recovery-period memory consumption.
- Post-recovery resource retention.
- Execution duration.
- Concurrent operation activity.
- Valid application progress.

Measurements MUST remain attributable
to their execution environment.

A short successful recovery does
not establish unlimited resilience
under repeated failure conditions.

Resource limits and acceptance
thresholds MUST be defined before
the corresponding qualification
conclusion is issued.

---

## 34. Post-Recovery Stability

A successful immediate recovery
does not independently establish
continued operational stability.

Where applicable, qualification
SHOULD include a declared
post-recovery observation interval.

Relevant observations include:

- Continued valid application progress.
- Logical session identity.
- Applicable authority integrity.
- Canonical history integrity.
- Absence of prohibited duplicate
  canonical effects.
- Resource retention.
- Subsequent unexpected failures.

The duration of the observation
interval MUST be documented.

Post-recovery stability claims
MUST remain bounded by the
actual observation duration.

---

## 35. Compound Failure Qualification

Recovery MAY be evaluated under
multiple overlapping disturbances.

Potential evaluation categories
include:

- Communication interruption with
  endpoint mobility.

- Recovery under degraded
  communication conditions.

- Repeated interruption with
  concurrent operation activity.

- Transport instability with
  authority integrity requirements.

- Recovery under constrained
  computational resources.

Each compound evaluation requires
its own acceptance criteria
and attributable evidence.

Independent successful evaluations
MUST NOT be combined into an
unsupported compound recovery claim.

Actual overlap of the relevant
conditions MUST be established.

---

## 36. Recovery Acceptance Matrix

| Observed outcome | Verdict |
|---|---|
| Required recovery, identity, and integrity criteria satisfied | PASS |
| Unauthorized logical session replacement | FAIL |
| Prohibited canonical mutation | FAIL |
| Prohibited authority rollback | FAIL |
| Prohibited duplicate commitment | FAIL |
| Required recovery deadline missed | FAIL for applicable liveness criterion |
| Transport restored; identity unverified | INCONCLUSIVE for continuity |
| Failure condition not established | INCONCLUSIVE |
| Required verification controls unsuccessful | INCONCLUSIVE |
| Required observation coverage unavailable | INCONCLUSIVE |
| Required scenario not executed | NOT TESTED |
| Scenario outside declared contract | NOT APPLICABLE |

A confirmed mandatory contract
violation takes precedence over
otherwise positive observations.

A successful transport result
MUST NOT override a failed
integrity result.

---

## 37. Evidence Obligation Matrix

| Qualification claim | Required evidence |
|---|---|
| Failure occurred | Attributable failure observation |
| Blackout occurred | Observed unavailability within declared scope |
| Transport recovered | Verified restoration observation |
| Original session survived | Qualified identity observation |
| Lifetime preserved | Applicable lifetime discrimination |
| History preserved | Canonical integrity verification |
| Authority preserved | Applicable authority verification |
| Application resumed | Attributable application progress |
| Recovery completed within deadline | Defined timing endpoints and measured duration |
| Resources remained bounded | Measurements against declared limits |
| Recovery remained stable | Defined post-recovery observation interval |

A general recovery success label
does not satisfy these obligations.

Each claim requires evidence
appropriate to its own semantics.

---

## 38. Public Recovery Evidence Record

Each approved recovery qualification
record SHOULD contain:

    DOCUMENT_ID: VRP-PA-008

    EVIDENCE_ID:

    SCENARIO_ID:

    CLAIM_REFERENCES:

    INVARIANT_REFERENCES:

    CONTRACT_VERSION:

    IMPLEMENTATION_REFERENCE:

    EXECUTION_REFERENCE:

    EVALUATION_ENVIRONMENT_CLASS:

    INITIAL_SESSION_OBSERVATION:

    INITIAL_LIFETIME_OBSERVATION:

    BASELINE_RESULT:

    CONFIGURED_FAILURE_CONDITION:

    OBSERVED_FAILURE_CONDITION:

    FAILURE_OBSERVATION_REFERENCE:

    MEASUREMENT_CLOCK_REFERENCE:

    OBSERVED_INTERRUPTION_DURATION:

    TRANSPORT_RESTORATION_DURATION:

    APPLICATION_RESTORATION_DURATION:

    IDENTITY_VERIFICATION_DURATION:

    INTEGRITY_VERIFICATION_DURATION:

    MEASUREMENT_UNCERTAINTY:

    SESSION_IDENTITY_RESULT:

    SESSION_LIFETIME_RESULT:

    AUTHORITY_INTEGRITY_RESULT:

    CANONICAL_HISTORY_RESULT:

    DUPLICATE_CONTAINMENT_RESULT:

    APPLICATION_PROGRESS_RESULT:

    RESOURCE_QUALIFICATION_RESULT:

    POST_RECOVERY_STABILITY_RESULT:

    POSITIVE_CONTROL_RESULT:

    NEGATIVE_CONTROL_RESULT:

    OBSERVATION_COVERAGE:

    ARTIFACT_REFERENCE:

    ARTIFACT_INTEGRITY_REFERENCE:

    EXECUTION_STATUS:

    OVERALL_VERDICT:

    EVIDENCE_LEVEL:

    REPRODUCTION_STATUS:

    INDEPENDENT_EVALUATION_STATUS:

    LIMITATIONS:

This is a public evidence record
template.

It is not an internal runtime
structure, protocol message,
or implementation interface.

Unpopulated fields MUST NOT
be interpreted as successful
qualification outcomes.

---

## 39. Evidence Promotion Requirements

Recovery evidence uses the
sufficiency levels established
in VRP-PA-006.

| Level | Recovery evidence requirement |
|---|---|
| E0 | Recovery contract specified |
| E1 | Historical execution outcome reported |
| E2 | Attributable execution artifacts available |
| E3 | Evidence verified against applicable criteria |
| E4 | Separately attributable reproduction |
| E5 | Independent evaluation completed |

The historical recovery reference
AVE-003 remains classified as E1
within this document.

Promotion requires corresponding
supporting evidence.

Additional architectural prose
does not independently increase
the evidence level.

---

## 40. Public Artifact Requirements

A stronger public recovery claim
SHOULD reference approved evidence
artifacts containing sufficient
information for the applicable
verification objective.

Candidate artifact categories
include:

- Execution summary.
- Failure observation summary.
- Recovery measurement summary.
- Identity verification outcome.
- Canonical integrity outcome.
- Verification control results.
- Artifact integrity manifest.
- Reproduction instructions.
- Documented limitations.

These are publication requirements.

They do not establish that
corresponding public artifacts
have already been released.

Restricted artifacts MUST be
identified as restricted.

Their existence MUST NOT be
represented as unrestricted
public reproducibility.

---

## 41. Evidence Authenticity Boundary

The following properties remain
distinct:

    ARTIFACT INTEGRITY

    EXECUTION AUTHENTICITY

    MEASUREMENT CORRECTNESS

    OBSERVATION SUFFICIENCY

    SEMANTIC VERIFICATION

    INDEPENDENT REPRODUCTION

A matching artifact digest can
establish consistency with a
trusted reference.

It does not independently establish
the truth of the recorded recovery
measurement.

A verifier PASS does not
independently establish that
every relevant observation
was available.

The evidence record MUST identify
the applicable trust assumptions
and verification limitations.

---

## 42. Independent Evaluation Model

An authorized independent evaluator
SHOULD be able to examine recovery
behavior through a bounded
black-box evaluation interface.

Where supported, the evaluator
SHOULD be able to:

- Select permitted failure scenarios.
- Establish acceptance criteria
  before execution.
- Observe actual failure conditions.
- Record recovery measurements.
- Examine approved identity evidence.
- Examine approved integrity evidence.
- Verify approved artifacts.
- Report failed or inconclusive
  outcomes.

The evaluation MUST NOT require
acceptance of a project-generated
success label as the sole basis
for correctness.

Actual evaluation availability
remains subject to supported
interfaces and applicable
authorization.

---

## 43. Independent Measurement Principle

Where practical, the evaluator
SHOULD obtain relevant measurements
from observation sources that
do not depend exclusively on
the runtime's own success
classification.

Relevant categories include:

- External communication availability.
- External application progress.
- Evaluator-controlled timing.
- Approved identity observations.
- Approved integrity verification.

The observation method MUST
remain appropriate to the
specific property being evaluated.

External communication observations
alone cannot establish every
internal semantic property.

Any remaining dependence on
project-provided evidence MUST
be documented.

---

## 44. Evaluator-Controlled Reproduction

A meaningful reproduction SHOULD
permit variation of supported
evaluation conditions within
the authorized operating scope.

The evaluator SHOULD be able
to distinguish:

    PROJECT-SELECTED DEMONSTRATION

    EVALUATOR-SELECTED SCENARIO

    REPRODUCED ENGINEERING RESULT

    INDEPENDENT QUALIFICATION

A prerecorded successful
demonstration provides weaker
evidence than an attributable
evaluator-controlled execution.

Independent reproduction requires
actual execution and recorded
observations.

It MUST NOT be inferred from
the availability of documentation
alone.

---

## 45. Falsification Conditions

A confirmed occurrence of any
applicable condition below
constitutes a relevant
counterexample:

1. Unauthorized session replacement
   during recovery.

2. Session recreation incorrectly
   classified as preservation.

3. Prohibited canonical history
   modification.

4. Acceptance of invalid authority
   producing prohibited effects.

5. Prohibited committed authority
   rollback.

6. Prohibited duplicate canonical
   commitment.

7. Unauthorized cross-lifetime
   interference.

8. Protected mutation despite
   required rejection.

9. Confirmed recovery timing
   violation against a declared
   mandatory deadline.

10. Recovery verification accepting
    a known noncompliant outcome.

11. Confirmed resource-bound
    violation against a declared
    mandatory limit.

12. A demonstrated intermediate
    integrity violation concealed
    by a valid final observation.

A confirmed counterexample MUST
invalidate the affected claim
within its demonstrated scope.

Successful unrelated evaluations
do not erase the violation.

---

## 46. Counterexample Reporting

An independent recovery finding
SHOULD identify:

    FINDING_REFERENCE

    CLAIM_REFERENCE

    INVARIANT_REFERENCE

    EVALUATION_SCOPE

    FAILURE_CONDITION

    EXPECTED_RECOVERY_BEHAVIOR

    OBSERVED_RECOVERY_BEHAVIOR

    SUPPORTING_EVIDENCE

    PROPOSED_CONTRACT_VIOLATION

    REPRODUCTION_STATUS

A valid black-box counterexample
does not become invalid merely
because the evaluator lacks
access to proprietary source code.

The qualification conclusion
MUST follow the applicable
evidence.

---

## 47. Remediation and Requalification

A confirmed recovery violation
requires an attributable
engineering record.

Where remediation occurs,
the record SHOULD distinguish:

- Original implementation reference.
- Original failure evidence.
- Affected correctness contract.
- Corrected implementation reference.
- Subsequent regression evidence.
- Requalification outcome.
- Remaining limitations.

Subsequent remediation MUST NOT
retroactively convert the original
failed execution into a successful
execution.

Historical engineering evidence
must remain attributable.

---

## 48. Prohibited Evidence Substitution

The following substitutions
are explicitly prohibited:

    RESTORED SOCKET
        as
    PRESERVED LOGICAL SESSION

    SUCCESSFUL RECONNECTION
        as
    VERIFIED CONTINUITY

    CONFIGURED BLACKOUT DURATION
        as
    OBSERVED INTERRUPTION DURATION

    RESTORED APPLICATION DELIVERY
        as
    CANONICAL HISTORY INTEGRITY

    VALID FINAL STATE
        as
    COMPLETE TEMPORAL CORRECTNESS

    HISTORICAL RECOVERY MEASUREMENT
        as
    GUARANTEED RECOVERY DEADLINE

    VERIFIER PASS
        as
    INDEPENDENT THIRD-PARTY AUDIT

    SINGLE SUCCESSFUL RECOVERY
        as
    UNLIMITED FAILURE RESILIENCE

Each qualification claim requires
evidence appropriate to the
property being asserted.

---

## 49. Technical Reviewer Questions

### Does successful recovery prove
that the original session survived?

No.

A qualified identity observation
must distinguish preservation
from recreation.

### Can a session remain valid
during complete communication loss?

The architecture permits that
relationship within the applicable
lifecycle contract.

Actual preservation requires
qualification evidence.

### Does VRP transmit information
during a complete blackout?

No communication claim is made
when all relevant communication
paths are unavailable.

### Is the reported 41.6-second
measurement a guaranteed deadline?

No.

It is a historical project-reported
measurement requiring its original
execution context for stronger
qualification.

### Can recovery correctness be
evaluated without source access?

Observable recovery properties
can be evaluated through sufficiently
qualified black-box interfaces.

Stronger implementation-level
claims may require additional
authorized evidence.

### Can an independent evaluator
disprove a recovery claim?

Yes.

An attributable violation of
an applicable correctness contract
constitutes a relevant counterexample.

### Does this document establish
independent recovery certification?

No.

It establishes the public
qualification contract and
historical evidence references.

Independent certification requires
separate applicable evidence.

---

## 50. Deployment Qualification Boundary

Laboratory recovery qualification
does not automatically establish
production deployment suitability.

A deployment evaluation SHOULD
define:

- Supported integration scope.
- Applicable communication conditions.
- Required recovery objectives.
- Maximum acceptable interruption.
- Session lifecycle requirements.
- Authority integrity requirements.
- Application delivery requirements.
- Resource constraints.
- Observation requirements.
- Operational termination criteria.
- Rollback and removal requirements.

Deployment acceptance MUST remain
specific to the evaluating
organization and environment.

---

## 51. Safety-Critical Applicability

Continuity-first recovery semantics
may be relevant to systems
operating under unstable or
intermittent communication conditions.

Potential evaluation domains
include:

- Mobile infrastructure.
- Distributed computing.
- Remote operational systems.
- Industrial communication.
- Intermittently connected platforms.
- Autonomous system communication.
- High-latency communication networks.

These domains describe potential
architectural applicability.

This document does not establish
automotive, aviation, maritime,
medical, industrial, or other
safety-critical certification.

Such deployments require separate
domain-specific qualification.

---

## 52. Comparative Engineering Boundary

Recovery, reconnection, failover,
and state preservation are
established engineering concerns.

This document does not claim
that recovery alone constitutes
a novel invention.

The VRP assurance objective
is qualification of recovery
within its declared continuity-first
logical session architecture.

Comparative claims against
other protocols or systems
require equivalent evaluation
conditions, appropriate baselines,
and separately attributable
comparative evidence.

Architectural differentiation
does not independently establish
performance superiority.

---

## 53. Protected Core Boundary

The following MAY be published
when approved for disclosure:

- Observable recovery contracts.
- Public failure classifications.
- Approved aggregate measurements.
- Historical evidence references.
- Acceptance criteria.
- Falsification conditions.
- Approved verification outcomes.
- Evidence classifications.
- Independent evaluation findings.
- Explicit limitations.

The following remain confidential:

- Proprietary recovery algorithms.
- Internal failure handling logic.
- Internal transport selection logic.
- Confidential decision mechanisms.
- Internal state representations.
- Private authority mechanisms.
- Internal persistence mechanisms.
- Protected source code.
- Private runtime interfaces.
- Confidential execution traces.
- Cryptographic implementation details.
- Wire-level implementation details.
- Private infrastructure configuration.

This document defines what must
be demonstrated.

It does not disclose how the
Protected Core achieves the
declared recovery behavior.

---

## 54. Assurance Limitations

This document does not establish:

- Unlimited session lifetime.
- Unlimited blackout tolerance.
- Zero recovery latency.
- Guaranteed packet delivery.
- Universal recovery deadlines.
- Universal transport compatibility.
- Unlimited resource availability.
- Immunity to every failure.
- Complete formal implementation proof.
- Independent third-party certification.

Every empirical result remains
bounded by its actual execution
conditions, observation coverage,
verification method, and applicable
correctness contract.

A finite recovery qualification
campaign does not establish the
impossibility of future failure.

---

## 55. Master Evidence Integration

The master claims-to-evidence
matrix MUST associate VRP-C10
with:

- Applicable invariant identifiers.
- Recovery scenario identifiers.
- Historical evidence references.
- Approved execution artifacts.
- Measurement definitions.
- Verification control results.
- Evidence classifications.
- Reproduction records.
- Independent evaluation status.
- Known limitations.

The historical recovery reference
AVE-003 MUST remain distinguishable
from future verified or independently
reproduced recovery measurements.

A claim MUST NOT receive a
qualification status stronger
than its supporting evidence.

---

## 56. Related Assurance Documents

- [Executive Engineering Assurance](VRP_EXECUTIVE_ENGINEERING_ASSURANCE.md)
- [Formal Continuity Invariants](VRP_FORMAL_CONTINUITY_INVARIANTS.md)
- [Session Identity Preservation](VRP_SESSION_IDENTITY_PRESERVATION.md)
- [Transport Independence](VRP_TRANSPORT_INDEPENDENCE.md)
- [Adversarial Validation Evidence](VRP_ADVERSARIAL_VALIDATION_EVIDENCE.md)
- [Replay and Duplicate Containment](VRP_REPLAY_AND_DUPLICATE_CONTAINMENT.md)
- [Authority and State Integrity](VRP_AUTHORITY_AND_STATE_INTEGRITY.md)

---

## 57. Final Engineering Declaration

    SESSION ≠ TRANSPORT

    A communication path may fail.

    A transport may disappear.

    Application progress may stop.

    Recovery may remain pending.

    None of these conditions alone
    authorizes a prohibited change
    in logical session identity.

    Restored communication is not
    sufficient proof of continuity.

    Recovery must preserve the
    applicable authority contract.

    Recovery must preserve the
    applicable integrity contract.

    Measurements must identify
    what was actually measured.

    Evidence must remain attributable.

    Counterexamples must remain visible.

    Independent verification must
    remain independent.

    The claim is falsifiable.

    The qualification contract
    is public.

    The Protected Core
    remains confidential.

---

**Veil Routing Protocol — VRP**

**Jumping VPN**

**Architect and Creator: Vitalijus Riabovas**

**20 recovery qualification scenarios.**

**12 failure classification categories.**

**12 explicit falsification conditions.**

**Independent measurement requirements.**

**Positive and negative verification controls.**

**Historical recovery reference: approximately 41.6 seconds.**

**Recovery beyond reconnection.**

**Continuity beyond transport failure.**

**Observable correctness. Protected implementation.**

**End of document — VRP-PA-008**
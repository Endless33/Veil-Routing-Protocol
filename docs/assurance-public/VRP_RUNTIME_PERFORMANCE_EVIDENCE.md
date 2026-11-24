# VRP Runtime Performance Evidence

## Veil Routing Protocol — Jumping VPN

**Document ID:** VRP-PA-011
**Version:** 1.0
**Classification:** PUBLIC
**Status:** Quantitative Engineering Assurance Framework
**Author:** Vitalijus Riabovas
**Protected Core:** CONFIDENTIAL

---

## 1. Executive Statement

Architecture must ultimately be evaluated
through observable execution.

A specification defines the required behavior.

An execution produces observations.

A qualified measurement establishes
a bounded empirical result.

Independent reproduction strengthens
confidence in that result.

These are distinct engineering obligations.

Veil Routing Protocol establishes the
following architectural principle:

    SESSION ≠ TRANSPORT

The performance qualification objective
is to establish the measurable operational
cost of satisfying applicable continuity,
authority, security, and integrity contracts.

Performance MUST NOT be achieved by
weakening mandatory correctness requirements.

This document establishes the public
measurement framework, evidence obligations,
reproduction requirements, and conditions
under which performance claims can be
accepted or falsified.

The proprietary implementation remains
confidential.

---

## 2. From Specification to Execution

The VRP assurance framework distinguishes:

    SPECIFICATION
        Defines required behavior.

    EXECUTION
        Produces observable results.

    MEASUREMENT
        Quantifies an observed property.

    VERIFICATION
        Evaluates evidence against a contract.

    REPRODUCTION
        Establishes a separately executed result.

    INDEPENDENT EVALUATION
        Establishes an externally attributable
        engineering conclusion.

Additional documentation alone does not
increase empirical evidence sufficiency.

A performance claim MUST be connected
to an actual measured execution.

---

## 3. Engineering Assurance Scope

This document supports the following
existing assurance claims:

    VRP-C01 — Logical session identity.

    VRP-C02 — Transport independence.

    VRP-C03 — Controlled transport replacement.

    VRP-C04 — Replay containment.

    VRP-C05 — Duplicate commit rejection.

    VRP-C08 — Canonical history integrity.

    VRP-C10 — Controlled recovery.

    VRP-C11 — Concurrent correctness.

    VRP-C12 — Evidence integrity.

    VRP-C13 — Fail-closed behavior.

    VRP-C14 — Bounded defensive behavior.

    VRP-C15 — Reproducible external verification.

Performance measurements provide
additional quantitative evidence.

They do not independently establish
the semantic correctness of these claims.

No new protocol correctness claim is
introduced solely through benchmarking.

---

## 4. Fundamental Performance Principle

The relevant engineering objective is:

    MEASURABLE PERFORMANCE
    WITH PRESERVED CORRECTNESS

The following substitutions are prohibited:

    FASTER EXECUTION
        as
    STRONGER CORRECTNESS

    HIGHER THROUGHPUT
        as
    VERIFIED CONTINUITY

    LOWER LATENCY
        as
    VERIFIED AUTHORITY INTEGRITY

    LOWER MEMORY CONSUMPTION
        as
    COMPLETE SECURITY

A performance improvement that introduces
a mandatory correctness violation is
not an acceptable engineering improvement.

---

## 5. Historical Quantitative Evidence

The VRP project has previously reported
the following quantitative engineering
outcomes.

| Evidence ID | Evaluation | Reported outcome |
|---|---|---|
| AVE-001 | Replay containment campaign | 9,999 replay presentations rejected |
| AVE-002 | Migration campaign | 1,000 migrations with reported continuity preservation |
| AVE-003 | Recovery evaluation | Approximately 41.6 seconds |
| AVE-007 | Evidence verification | PASS |

These references are inherited from
VRP-PA-005.

They represent historical project-reported
engineering outcomes.

They are not newly generated measurements.

Original execution artifacts are not
embedded in this document.

Their evidence sufficiency classification
within this document remains:

    EVIDENCE_LEVEL = E1

The reported outcomes MUST remain
associated with their original
evaluation scopes.

---

## 6. Historical Measurement Interpretation

The reported replay rejection count
does not independently establish
replay processing throughput.

The reported migration count does
not independently establish
migration frequency.

The reported recovery duration
does not independently establish
a guaranteed recovery deadline.

The reported verifier PASS does
not independently establish
independent third-party verification.

The following information is required
for stronger quantitative interpretation:

- Actual execution duration.
- Measurement endpoint definitions.
- Evaluated implementation reference.
- Execution environment.
- Observation coverage.
- Applicable correctness results.
- Original artifact provenance.
- Verification method.
- Known limitations.

Missing measurement context MUST
remain explicitly identified.

---

## 7. Current Public Performance Status

    DOCUMENT_REFERENCE:
        VRP-PA-011

    QUANTITATIVE_HISTORICAL_RESULTS:
        REPORTED

    HISTORICAL_EVIDENCE_LEVEL:
        E1

    DEDICATED_PERFORMANCE_CONTRACT:
        SPECIFIED

    DEDICATED_BENCHMARK_ARTIFACTS:
        NOT EMBEDDED

    DEDICATED_PUBLIC_BENCHMARK_LEVEL:
        E0

    INDEPENDENT_PERFORMANCE_REPRODUCTION:
        NOT ESTABLISHED BY THIS RECORD

This classification describes
the evidence presented by
this document.

It does not establish that
additional restricted engineering
measurements do not exist.

A stronger public verdict requires
approved attributable artifacts.

---

## 8. Performance Qualification Domains

The public framework distinguishes
the following measurement domains.

| Domain | Measurement objective |
|---|---|
| PERF-D01 | Operation completion latency |
| PERF-D02 | Valid operation throughput |
| PERF-D03 | CPU consumption |
| PERF-D04 | Memory consumption |
| PERF-D05 | Allocation cost |
| PERF-D06 | Concurrent scaling |
| PERF-D07 | Transport transition cost |
| PERF-D08 | Recovery duration |
| PERF-D09 | Defensive processing overhead |
| PERF-D10 | Sustained runtime stability |
| PERF-D11 | Post-disturbance resource retention |
| PERF-D12 | Application progress under disturbance |

These domains define public
measurement objectives.

They do not disclose internal
runtime components or algorithms.

---

## 9. Measurement Scope Classification

Every quantitative result MUST
identify its measurement scope.

Permitted scope classifications include:

    MICROBENCHMARK

    COMPONENT_EVALUATION

    INTEGRATION_EVALUATION

    LIVE_RUNTIME_EVALUATION

    END_TO_END_EVALUATION

    DEPLOYMENT_EVALUATION

Results from different scopes
MUST NOT be treated as equivalent.

A component operation rate does
not establish end-to-end network
throughput.

A microbenchmark latency does
not establish application latency.

A successful integration benchmark
does not establish production
deployment capacity.

---

## 10. Benchmark Identity

Each benchmark result MUST remain
attributable to a defined
evaluation identity.

The record SHOULD establish:

    BENCHMARK_REFERENCE

    IMPLEMENTATION_REFERENCE

    CONTRACT_VERSION

    BUILD_REFERENCE

    EXECUTION_REFERENCE

    WORKLOAD_REFERENCE

    ENVIRONMENT_REFERENCE

    MEASUREMENT_METHOD_REFERENCE

    VERIFICATION_REFERENCE

The public implementation reference
MAY be an approved opaque identifier
or an approved cryptographic digest.

Its publication MUST NOT require
disclosure of proprietary repository
structure or source code.

An opaque identifier establishes
attribution only within its
documented trust model.

---

## 11. Execution Environment Attribution

Performance results depend on
their execution environment.

Approved public records SHOULD
identify relevant characteristics:

- Processor architecture.
- Available computational capacity.
- Available memory.
- Operating system class.
- Runtime or compiler version.
- Virtualized or physical execution.
- Relevant scheduling conditions.
- Measurement instrumentation.
- Communication environment class.

Sensitive infrastructure identifiers
MUST NOT be published.

The disclosed environment description
MUST remain sufficient for the
claimed level of reproducibility.

Where that is not possible, the
reproduction limitation MUST be
documented.

---

## 12. Baseline Requirements

A performance evaluation MUST
establish a valid baseline.

The baseline SHOULD identify:

- Applicable operation contract.
- Valid initial conditions.
- Workload characteristics.
- Required operation progress.
- Applicable integrity observations.
- Measurement environment.
- Resource availability.
- Measurement duration.

A benchmark that does not establish
valid operation execution MUST NOT
receive a positive performance
qualification verdict.

The absence of errors is not
independent proof of valid work.

---

## 13. Benchmark Fixture Correctness

Benchmark preparation MUST
satisfy the applicable operation
preconditions.

The evaluation MUST distinguish:

    FIXTURE INITIALIZATION

    VALID WORKLOAD EXECUTION

    MEASUREMENT COLLECTION

    CORRECTNESS VERIFICATION

An invalid benchmark fixture can
produce misleading measurements
or prevent valid execution.

A failed fixture MUST NOT be
silently interpreted as a
production runtime defect.

A corrected fixture requires
separately attributable
requalification.

Changes to benchmark preparation
MUST remain distinguishable from
changes to the evaluated runtime.

---

## 14. Valid Work Accounting

Performance MUST be measured
against defined useful work.

Relevant accounting categories include:

    OPERATIONS_PRESENTED

    OPERATIONS_COMPLETED

    OPERATIONS_REJECTED

    OPERATIONS_FAILED

    OPERATIONS_PENDING

    VALID_EFFECTS_VERIFIED

    OBSERVATIONS_UNRESOLVED

The relationship between these
categories MUST be documented.

Rejected operations MUST NOT
be counted as successful
application operations.

Repeated delivery MUST NOT
be counted as additional
canonical commitment unless
the applicable contract permits it.

A benchmark MUST NOT inflate
useful throughput through
duplicate accounting.

---

## 15. Operation Latency

Operation latency measures the
elapsed time between declared
observable measurement endpoints.

Conceptually:

    L_operation =
        T_completion - T_invocation

The evaluation MUST identify:

- Invocation definition.
- Completion definition.
- Clock reference.
- Measurement resolution.
- Applicable operation semantics.
- Treatment of incomplete operations.

A completion measurement MUST
NOT be interpreted as canonical
commitment latency unless that
relationship is established.

These symbols describe external
measurement semantics.

They are not internal runtime
variables.

---

## 16. Throughput Qualification

Useful operation throughput MAY
be expressed as:

    Q_valid =
        N_valid_completed / D_observed

Where:

    N_valid_completed =
        Verified completed operations
        within the declared scope.

    D_observed =
        Actual observation duration.

The measurement MUST identify
the operation class and unit.

Possible units include:

- Operations per second.
- Verified effects per second.
- Application messages per second.
- Application bytes per second.

These units are not interchangeable.

A rejection processing rate MUST
remain distinguishable from
valid application throughput.

---

## 17. Network Goodput

Where applicable, application
goodput MAY be measured as:

    G_application =
        B_useful_delivered / D_observed

Where:

    B_useful_delivered =
        Attributable useful application
        data delivered under the
        declared accounting contract.

Network traffic volume MUST NOT
automatically be represented as
useful application delivery.

The measurement SHOULD distinguish:

- Presented application data.
- Delivered application data.
- Repeated delivery.
- Incomplete delivery.
- Applicable protocol overhead.
- Measurement duration.

No network throughput or goodput
value is asserted by this
document without corresponding
execution evidence.

---

## 18. Latency Distribution

Where sufficient samples are
available, latency measurements
SHOULD include:

    SAMPLE_COUNT

    MINIMUM

    MEDIAN

    P95

    P99

    MAXIMUM

    MEASUREMENT_UNCERTAINTY

The percentile calculation method
MUST be documented.

A small sample MUST NOT be
represented as statistically
strong tail-latency evidence.

Failed, pending, and incomplete
operations MUST remain visible
in the outcome accounting.

Latency distributions based only
on successful operations MUST
be explicitly identified as such.

---

## 19. CPU Consumption

CPU measurements MUST remain
associated with the actual
evaluated workload.

Relevant measurements include:

- Baseline CPU consumption.
- Workload CPU consumption.
- Disturbance-period CPU consumption.
- Recovery-period CPU consumption.
- Post-evaluation CPU consumption.

The record MUST identify
the measurement unit and
normalization method.

Process-level CPU consumption
MUST NOT be confused with
system-wide CPU consumption.

A low CPU measurement does
not establish useful performance
unless valid operation progress
has also been established.

---

## 20. Memory Consumption

Memory qualification SHOULD
distinguish:

    BASELINE_MEMORY

    ACTIVE_WORKLOAD_MEMORY

    PEAK_OBSERVED_MEMORY

    POST_WORKLOAD_MEMORY

    RETAINED_MEMORY

The memory measurement method
MUST be identified.

Allocated memory, live memory,
resident memory, and cumulative
allocation volume are different
measurement properties.

They MUST NOT be treated
as interchangeable.

A single memory observation
does not establish the absence
of resource retention problems.

---

## 21. Allocation Cost

Where supported by the approved
measurement environment, allocation
cost MAY be reported using:

    BYTES_ALLOCATED_PER_OPERATION

    ALLOCATIONS_PER_OPERATION

    TOTAL_ALLOCATION_VOLUME

These are aggregate measurement
categories.

They do not disclose internal
allocation mechanisms, data
structures, or ownership models.

Allocation improvements MUST
remain subject to the applicable
correctness requirements.

A lower allocation count alone
does not establish stronger
runtime correctness.

---

## 22. Concurrent Scaling

Concurrent scaling qualification
MUST identify actual workload
activity rather than relying
solely on configured participant
counts.

Relevant measurements include:

- Configured participant count.
- Observed participant activity.
- Actual operation overlap.
- Completed valid operations.
- Throughput.
- Latency distribution.
- CPU consumption.
- Memory consumption.
- Applicable integrity outcomes.

A configured participant count
does not establish an equivalent
number of active logical sessions.

Concurrent scaling measurements
MUST remain distinct from
linearizability qualification.

VRP-PA-009 remains applicable.

---

## 23. Scaling Efficiency

Where comparable baseline
measurements are available,
scaling efficiency MAY be
evaluated using:

    Speedup(n) = Q(n) / Q(1)

    Efficiency(n) = Speedup(n) / n

Where:

    Q(n) =
        Measured valid throughput
        at the declared activity level.

    n =
        Defined scaling factor.

The evaluation MUST establish
that the workloads and
measurement scopes are comparable.

These expressions are generic
engineering measurement definitions.

They do not describe proprietary
VRP implementation logic.

No scaling efficiency value
is asserted by this document.

---

## 24. Transport Transition Performance

Transport transition measurements
MUST remain separate from
logical session identity
verification.

Relevant observations include:

- Actual transport transition.
- Communication interruption.
- Transport restoration.
- Application progress restoration.
- Applicable identity preservation.
- Canonical integrity preservation.
- Resource consumption.

A fast transport transition
does not independently establish
session continuity.

The transport qualification
requirements of VRP-PA-004
remain applicable.

---

## 25. Migration Measurement Boundary

The historical reference
AVE-002 reports 1,000 migrations
with reported continuity
preservation.

That count does not independently
establish:

- Migrations per second.
- Maximum migration frequency.
- Maximum supported migration count.
- Migration latency distribution.
- Unlimited migration resilience.
- Production migration capacity.

Stronger quantitative claims
require actual timing and
operation attribution.

The configured number of
migrations MUST NOT substitute
for the observed number.

---

## 26. Recovery Performance

Recovery performance MUST
identify its measurement
endpoints.

Relevant measurements MAY include:

    OBSERVED_FAILURE_DURATION

    TRANSPORT_RESTORATION_DELAY

    APPLICATION_RESTORATION_DELAY

    IDENTITY_VERIFICATION_DELAY

    INTEGRITY_VERIFICATION_DELAY

These measurements are defined
in VRP-PA-008.

The historical recovery reference
AVE-003 remains approximately
41.6 seconds.

Its original measurement
endpoint definitions are not
established by this document.

The historical measurement
MUST NOT be represented as
a universal recovery guarantee.

---

## 27. Defensive Performance

Defensive performance qualification
MUST distinguish:

    ADVERSE_ACTIVITY_PROCESSING

    VALID_OPERATION_PROGRESS

    PROHIBITED_EFFECT_CONTAINMENT

    DEFENSIVE_RESOURCE_COST

    RECOVERY_IMPACT

A high rejection rate does not
independently establish effective
security or valid application
availability.

The corresponding integrity
and authorization outcomes
MUST be verified separately.

VRP-PA-010 remains applicable.

---

## 28. Defensive Overhead

Where equivalent comparison
conditions can be established,
defensive overhead MAY be
measured relative to an
approved baseline.

Relevant properties include:

- Additional CPU consumption.
- Additional memory consumption.
- Additional operation latency.
- Reduced valid throughput.
- Recovery duration changes.
- Communication overhead.

The comparison MUST NOT require
disabling mandatory security
controls in an operational
deployment.

Any approved laboratory comparison
MUST document its security
configuration and limitations.

No proprietary defensive thresholds
or decision criteria are disclosed.

---

## 29. Sustained Runtime Qualification

Short-duration measurements
do not establish sustained
runtime stability.

A sustained evaluation SHOULD
record:

- Actual execution duration.
- Valid operation progress.
- Latency variation.
- Throughput variation.
- Resource consumption.
- Resource retention.
- Failed operations.
- Incomplete operations.
- Applicable correctness outcomes.

The evaluation MUST distinguish
the intended duration from
the actual completed duration.

A successful finite execution
does not establish unlimited
runtime stability.

---

## 30. Post-Disturbance Measurements

The end of a disturbance does
not independently establish
normal resource behavior.

Where applicable, qualification
SHOULD compare:

    PRE_DISTURBANCE_BASELINE

    DISTURBANCE_INTERVAL

    RECOVERY_INTERVAL

    POST_RECOVERY_INTERVAL

Relevant observations include:

- Valid application progress.
- Operation latency.
- CPU consumption.
- Memory consumption.
- Retained resources.
- Logical session integrity.
- Canonical authority integrity.

Post-disturbance stability
claims MUST identify the
actual observation duration.

---

## 31. Proposed Performance Scenario Registry

| Scenario | Evaluation objective |
|---|---|
| RPE-001 | Valid execution baseline |
| RPE-002 | Benchmark fixture correctness |
| RPE-003 | Operation latency |
| RPE-004 | Valid operation throughput |
| RPE-005 | Application goodput |
| RPE-006 | Latency distribution |
| RPE-007 | CPU consumption |
| RPE-008 | Memory consumption |
| RPE-009 | Allocation cost |
| RPE-010 | Concurrent scaling |
| RPE-011 | Scaling efficiency |
| RPE-012 | Transport transition performance |
| RPE-013 | Repeated migration performance |
| RPE-014 | Recovery duration |
| RPE-015 | Defensive processing overhead |
| RPE-016 | Valid progress under disturbance |
| RPE-017 | Sustained runtime stability |
| RPE-018 | Post-disturbance resource retention |
| RPE-019 | Correctness-preserving optimization |
| RPE-020 | Measurement negative controls |
| RPE-021 | Repeated benchmark execution |
| RPE-022 | Environment variation |
| RPE-023 | Independent reproduction |
| RPE-024 | Deployment-specific qualification |

Registry inclusion establishes
an evaluation objective.

It does not establish completed
execution or qualification.

---

## 32. Candidate Concurrency Matrix

The following values define
proposed evaluation conditions.

| Scenario | Intended participants |
|---|---:|
| RPE-C01 | 1 |
| RPE-C02 | 2 |
| RPE-C03 | 4 |
| RPE-C04 | 8 |
| RPE-C05 | 16 |
| RPE-C06 | 32 |
| RPE-C07 | 64 |
| RPE-C08 | 128 |

These are proposed workload
parameters.

They are not reported VRP
capacity measurements.

The actual operation domain,
participant semantics, workload,
and observed overlap MUST be
established for each execution.

---

## 33. Candidate Duration Matrix

| Scenario | Intended observation duration |
|---|---:|
| RPE-T01 | 1 minute |
| RPE-T02 | 10 minutes |
| RPE-T03 | 30 minutes |
| RPE-T04 | 60 minutes |
| RPE-T05 | 24 hours |

These durations define candidate
laboratory evaluation conditions.

They do not establish completed
sustained runtime qualification.

Each execution requires declared
resource limits, termination
conditions, and correctness
observations.

---

## 34. Candidate Communication Conditions

Where supported and authorized,
performance MAY be evaluated
under controlled communication
degradation.

| Condition | Proposed evaluation values |
|---|---|
| Packet loss | 30%, 50%, 80%, 90% |
| Communication interruption | 10, 30, 60 seconds |
| Elevated round-trip latency | 300–900 milliseconds |
| Endpoint instability | Repeated endpoint changes |
| Delivery variation | Controlled jitter and reordering |

These are proposed laboratory
conditions.

They are not completed
qualification results.

Configured conditions MUST
remain distinguishable from
actual observed conditions.

No claim of universal operation
under these conditions is
established by this matrix.

---

## 35. Compound Performance Qualification

Performance under multiple
simultaneous disturbances
requires separate evidence.

Relevant evaluation dimensions
include:

- Transport instability.
- Communication degradation.
- Recovery activity.
- Concurrent operations.
- Defensive activity.
- Resource constraints.

Independent successful evaluations
MUST NOT be combined into
an unsupported compound
performance claim.

The actual overlap of relevant
conditions MUST be established.

Applicable correctness properties
MUST remain independently
verified.

---

## 36. Positive Measurement Controls

The measurement environment
MUST establish that valid
work can be observed.

Required control categories include:

    VALID_WORKLOAD:
        REQUIRED

    MEASUREMENT_INSTRUMENTATION:
        QUALIFIED

    OPERATION_ACCOUNTING:
        QUALIFIED

    BASELINE_CORRECTNESS:
        VERIFIED

    MEASUREMENT_SCOPE:
        ESTABLISHED

These are required conditions.

They are not reported results
of a completed execution.

A benchmark MUST NOT receive
a positive qualification verdict
when its workload fails to
perform the intended valid work.

---

## 37. Negative Measurement Controls

The evaluation method SHOULD
demonstrate recognition of
relevant invalid measurements.

Approved synthetic fixtures
MAY include:

- Missing measurement duration.
- Duplicate operation accounting.
- Invalid workload completion.
- Unsupported measurement units.
- Missing correctness observations.
- Contradictory operation totals.
- Incorrect measurement endpoints.
- Incomplete execution records.

A measurement verifier MUST NOT
accept a known invalid record
as a fully qualified result.

Synthetic fixtures MUST remain
distinguishable from actual
runtime measurements.

---

## 38. Illustrative Measurement A

### Valid throughput accounting

This is a synthetic measurement
example.

It is not a VRP benchmark result.

Assumed observations:

    VERIFIED_VALID_OPERATIONS = 10000

    OBSERVATION_DURATION = 10 seconds

Illustrative calculation:

    VALID_THROUGHPUT =
        10000 / 10

    VALID_THROUGHPUT =
        1000 operations per second

This result is meaningful only
within the assumed operation
semantics and observation scope.

It MUST NOT be represented
as measured VRP performance.

---

## 39. Illustrative Measurement B

### Rejection accounting

This is a synthetic example.

Assumed observations:

    OPERATIONS_PRESENTED = 10000

    OPERATIONS_REJECTED = 9000

    VALID_OPERATIONS_COMPLETED = 1000

    OBSERVATION_DURATION = 10 seconds

Illustrative calculations:

    PRESENTATION_RATE =
        1000 presentations per second

    VALID_THROUGHPUT =
        100 operations per second

These are different measurements.

The presentation rate MUST NOT
be reported as valid application
throughput.

---

## 40. Illustrative Measurement C

### Performance improvement with
### correctness regression

Assumed synthetic observations:

    BASELINE_CORRECTNESS = PASS

    CANDIDATE_THROUGHPUT =
        HIGHER THAN BASELINE

    CANDIDATE_CANONICAL_INTEGRITY =
        FAIL

Expected qualification:

    PERFORMANCE_OBSERVATION:
        RECORDED

    CORRECTNESS_QUALIFICATION:
        FAIL

    ENGINEERING_ACCEPTANCE:
        REJECTED

The measured performance
improvement does not override
the correctness violation.

---

## 41. Illustrative Measurement D

### Incomplete execution

Assumed synthetic observations:

    CONFIGURED_REPETITIONS = 100

    COMPLETED_REPETITIONS = 80

    FAILED_REPETITIONS = 5

    UNEXECUTED_REPETITIONS = 15

For this example, completed
repetitions exclude failed
repetitions.

The record MUST preserve all
three categories.

The evaluation MUST NOT
report 100 successful
repetitions.

The measured subset MUST
remain explicitly identified.

---

## 42. Illustrative Measurement E

### Missing identity verification

Assumed synthetic observations:

    TRANSPORT_TRANSITION:
        OBSERVED

    TRANSITION_DURATION:
        MEASURED

    LOGICAL_SESSION_IDENTITY:
        UNVERIFIED

Expected qualification:

    TRANSPORT_TIMING:
        MEASUREMENT AVAILABLE

    SESSION_CONTINUITY:
        INCONCLUSIVE

A valid transport timing
measurement does not independently
establish continuity-preserving
transition performance.

---

## 43. Illustrative Measurement F

### Resource limit violation

Assumed synthetic observations:

    VALID_OPERATION_PROGRESS:
        VERIFIED

    CANONICAL_INTEGRITY:
        VERIFIED

    MANDATORY_RESOURCE_LIMIT:
        EXCEEDED

Expected qualification:

    CORRECTNESS_SCOPE:
        PASS

    RESOURCE_SCOPE:
        FAIL

    OVERALL_ACCEPTANCE:
        FAIL IF RESOURCE LIMIT IS MANDATORY

This distinction prevents
successful correctness results
from concealing unacceptable
operational resource behavior.

---

## 44. Repeated Benchmark Execution

Repeated measurements SHOULD
remain separately attributable.

The record SHOULD identify:

- Intended repetition count.
- Actual attempted repetitions.
- Actual completed repetitions.
- Failed repetitions.
- Inconclusive repetitions.
- Measurement variation.
- Environment variation.
- Applicable correctness results.

Repeated execution increases
empirical observation coverage.

It does not establish universal
performance behavior.

The fastest observed execution
MUST NOT be presented as
representative without an
appropriate statistical basis.

---

## 45. Measurement Uncertainty

Performance measurements are
subject to uncertainty.

Relevant influences MAY include:

- Clock resolution.
- Operating system scheduling.
- Virtualization overhead.
- Background activity.
- Runtime initialization.
- Instrumentation overhead.
- Workload variation.
- Resource contention.
- Communication variation.

The evaluation SHOULD identify
material uncertainty sources.

Unexplained measurement variation
MUST NOT be silently removed
from the engineering record.

Precision MUST NOT exceed
what the measurement method
reasonably supports.

---

## 46. Instrumentation Boundary

Measurement instrumentation
can affect observed performance.

The evaluation MUST identify
whether measurements were
obtained under:

    NORMAL_EXECUTION

    INSTRUMENTED_EXECUTION

    RACE_DETECTION_EXECUTION

    PROFILING_EXECUTION

    OTHER_APPROVED_MEASUREMENT_MODE

Measurements from different
instrumentation modes MUST
NOT be compared without
accounting for material
differences.

A profiling result does not
automatically represent
uninstrumented production
performance.

Internal profiling artifacts
remain confidential unless
explicitly approved for
publication.

---

## 47. Correctness-Preserving Optimization

An engineering optimization
MUST preserve every applicable
mandatory correctness contract.

The qualification SHOULD
establish:

    BASELINE_IMPLEMENTATION_REFERENCE

    CANDIDATE_IMPLEMENTATION_REFERENCE

    BASELINE_MEASUREMENT

    CANDIDATE_MEASUREMENT

    COMPARABLE_EVALUATION_CONDITIONS

    BASELINE_CORRECTNESS_RESULT

    CANDIDATE_CORRECTNESS_RESULT

    REGRESSION_VERIFICATION_RESULT

    OBSERVED_PERFORMANCE_DIFFERENCE

An optimization MUST NOT
receive acceptance solely
because a benchmark reports
improved execution speed.

Correctness remains a mandatory
acceptance gate.

---

## 48. Benchmark Regression Policy

A performance regression
SHOULD be evaluated against
declared acceptance criteria.

The evaluation MUST distinguish:

- Confirmed measurement regression.
- Expected measurement variation.
- Environment-related variation.
- Workload changes.
- Instrumentation changes.
- Correctness-related tradeoffs.
- Invalid benchmark preparation.

A single slower observation
does not independently establish
a persistent runtime regression.

A confirmed regression MUST
remain attributable to its
actual evaluation conditions.

---

## 49. Comparative Performance Boundary

Comparative claims require
equivalent measurement scopes.

A comparison SHOULD establish:

- Comparable operation semantics.
- Comparable security requirements.
- Comparable correctness obligations.
- Comparable workloads.
- Comparable execution environments.
- Comparable communication conditions.
- Comparable measurement methods.
- Comparable statistical treatment.

A system performing additional
verified correctness work
MUST NOT be compared with
a simpler workload without
documenting the difference.

This document establishes
no comparative superiority
over other protocols.

Such claims require dedicated
comparative evidence.

---

## 50. Acceptance Matrix

| Observed outcome | Verdict |
|---|---|
| Valid measurement and all mandatory criteria satisfied | PASS |
| Mandatory correctness violation | FAIL |
| Mandatory latency requirement violated | FAIL for latency scope |
| Mandatory throughput requirement violated | FAIL for throughput scope |
| Mandatory resource limit violated | FAIL for resource scope |
| Invalid benchmark preparation | INCONCLUSIVE for runtime performance |
| Missing measurement endpoints | INCONCLUSIVE |
| Missing required correctness observations | INCONCLUSIVE |
| Invalid operation accounting | INCONCLUSIVE |
| Required measurement controls unsuccessful | INCONCLUSIVE |
| Required evaluation not executed | NOT TESTED |
| Scenario outside declared scope | NOT APPLICABLE |

A confirmed mandatory correctness
violation takes precedence over
otherwise positive performance
observations.

---

## 51. Evidence Obligation Matrix

| Qualification claim | Required evidence |
|---|---|
| Valid operation latency | Defined endpoints and measured duration |
| Valid throughput | Verified useful work and actual duration |
| Application goodput | Attributable useful application delivery |
| Tail latency | Sufficient samples and calculation method |
| CPU efficiency | Attributable CPU and workload measurements |
| Memory efficiency | Defined memory metrics and workload |
| Allocation efficiency | Attributable allocation measurements |
| Concurrent scaling | Actual overlap and comparable measurements |
| Transition performance | Observed transition and timing |
| Continuity-preserving transition | Timing plus qualified identity evidence |
| Recovery performance | Defined recovery endpoints and observations |
| Defensive efficiency | Resource cost plus security outcomes |
| Sustained stability | Defined observation interval and results |
| Optimization acceptance | Comparable measurements and regression verification |
| Independent reproduction | Independently attributable execution record |

A general benchmark success
label does not satisfy these
claim-specific obligations.

---

## 52. Public Performance Evidence Record

Each approved performance
record SHOULD contain:

    DOCUMENT_ID: VRP-PA-011

    EVIDENCE_ID:

    SCENARIO_ID:

    CLAIM_REFERENCES:

    CONTRACT_VERSION:

    IMPLEMENTATION_REFERENCE:

    BUILD_REFERENCE:

    EXECUTION_REFERENCE:

    BENCHMARK_REFERENCE:

    MEASUREMENT_SCOPE:

    EVALUATION_ENVIRONMENT_CLASS:

    WORKLOAD_REFERENCE:

    WORKLOAD_VALIDITY_RESULT:

    INSTRUMENTATION_MODE:

    CONFIGURED_DURATION:

    ACTUAL_OBSERVATION_DURATION:

    CONFIGURED_REPETITIONS:

    ACTUAL_ATTEMPTED_REPETITIONS:

    ACTUAL_COMPLETED_REPETITIONS:

    FAILED_REPETITIONS:

    INCONCLUSIVE_REPETITIONS:

    CONFIGURED_CONCURRENT_ACTIVITY:

    OBSERVED_CONCURRENT_ACTIVITY:

    OPERATIONS_PRESENTED:

    VALID_OPERATIONS_COMPLETED:

    OPERATIONS_REJECTED:

    OPERATIONS_FAILED:

    OPERATIONS_PENDING:

    VALID_EFFECTS_VERIFIED:

    LATENCY_MEASUREMENT_REFERENCE:

    LATENCY_SAMPLE_COUNT:

    LATENCY_MEDIAN:

    LATENCY_P95:

    LATENCY_P99:

    LATENCY_MAXIMUM:

    VALID_THROUGHPUT:

    APPLICATION_GOODPUT:

    CPU_MEASUREMENT_REFERENCE:

    MEMORY_MEASUREMENT_REFERENCE:

    ALLOCATION_MEASUREMENT_REFERENCE:

    TRANSPORT_TRANSITION_MEASUREMENT:

    RECOVERY_MEASUREMENT:

    RESOURCE_LIMIT_REFERENCE:

    RESOURCE_QUALIFICATION_RESULT:

    SESSION_IDENTITY_RESULT:

    AUTHORITY_INTEGRITY_RESULT:

    CANONICAL_HISTORY_RESULT:

    CORRECTNESS_VERIFICATION_RESULT:

    POSITIVE_CONTROL_RESULT:

    NEGATIVE_CONTROL_RESULT:

    MEASUREMENT_UNCERTAINTY:

    OBSERVATION_COVERAGE:

    ARTIFACT_REFERENCE:

    ARTIFACT_INTEGRITY_REFERENCE:

    VERIFICATION_REFERENCE:

    OVERALL_VERDICT:

    EVIDENCE_LEVEL:

    REPRODUCTION_STATUS:

    INDEPENDENT_EVALUATION_STATUS:

    LIMITATIONS:

This is a public evidence
record template.

It is not an internal runtime
structure, protocol format,
or proprietary interface.

Unpopulated fields MUST NOT
be interpreted as successful
measurements.

---

## 53. Minimum Public Evidence Bundle

A dedicated performance
qualification SHOULD be
associated with an approved
public evidence bundle.

The following names describe
a proposed publication layout:

    evidence/

        PERFORMANCE_SUMMARY.md

        MEASUREMENTS.csv

        ENVIRONMENT.json

        EXECUTION_REFERENCE.json

        CORRECTNESS_RESULTS.json

        VERIFICATION_RESULTS.json

        LIMITATIONS.md

        SHA256SUMS

These are proposed public
artifact categories.

They are not existing file
claims.

They do not describe internal
repository structure.

Each published artifact MUST
contain sufficient approved
information for its stated
verification objective.

---

## 54. Public Measurement Dataset

An approved public measurement
dataset SHOULD contain enough
information to permit relevant
independent recalculation.

Candidate public fields include:

    evidence_id

    scenario_id

    repetition_id

    measurement_scope

    measurement_name

    measurement_value

    measurement_unit

    observation_duration

    sample_count

    correctness_verdict

    execution_reference

These fields describe a
public reporting dataset.

They are not internal
runtime data structures.

Where confidentiality prevents
publication of individual
measurements, the resulting
verification limitation MUST
be explicitly documented.

---

## 55. Evidence Integrity Verification

An approved public evidence
bundle MAY include cryptographic
artifact digests.

For a compatible published
SHA-256 manifest, an evaluator
MAY verify artifact consistency
using standard tooling:

    sha256sum -c SHA256SUMS

This command is a generic
public artifact integrity check.

It does not interact with
the Protected Core.

It does not establish that
the recorded measurements
are authentic or correct.

The expected manifest reference
MUST originate from an
appropriate trusted source.

No actual manifest verification
result is asserted here.

---

## 56. Independent Recalculation

Where approved measurement
datasets are available, an
external evaluator SHOULD
be able to independently
recalculate applicable:

- Operation totals.
- Valid throughput.
- Measurement distributions.
- Percentile values.
- Relative performance differences.
- Repetition accounting.
- Applicable acceptance decisions.

Independent recalculation
does not require access to
proprietary execution algorithms.

However, recalculation alone
does not establish that
the original execution occurred
as reported.

Execution authenticity remains
a separate evidence obligation.

---

## 57. Evaluator-Controlled Execution

Where an authorized black-box
evaluation environment is
available, an evaluator SHOULD
be able to:

- Select permitted workload conditions.
- Define acceptance criteria.
- Observe actual execution.
- Record independent timing measurements.
- Verify applicable correctness outcomes.
- Examine approved evidence artifacts.
- Recalculate supported measurements.
- Report negative or inconclusive findings.

The evaluator SHOULD NOT be
required to rely exclusively
on project-generated success
labels.

Actual evaluation availability
remains subject to supported
interfaces and authorization.

---

## 58. Demonstration Versus Reproduction

The assurance framework
distinguishes:

    PRERECORDED DEMONSTRATION

    PROJECT-CONTROLLED EXECUTION

    EVALUATOR-OBSERVED EXECUTION

    EVALUATOR-CONTROLLED EXECUTION

    INDEPENDENT REPRODUCTION

A prerecorded demonstration
can provide useful context.

It does not independently
establish evaluator-controlled
reproducibility.

A project-controlled execution
observed by an external party
MUST NOT automatically be
classified as independently
controlled execution.

The applicable evaluation
control and trust boundaries
MUST be documented.

---

## 59. Evidence Promotion Gates

The evidence sufficiency
levels established in
VRP-PA-006 remain applicable.

| Level | Performance evidence requirement |
|---|---|
| E0 | Measurement contract specified |
| E1 | Quantitative execution outcome reported |
| E2 | Attributable execution artifacts available |
| E3 | Measurements and applicable controls verified |
| E4 | Separately attributable reproduction |
| E5 | Independent evaluation completed |

Evidence promotion MUST remain
specific to the evaluated
measurement scope.

The availability of an artifact
does not automatically establish
its semantic correctness.

Additional documentation does
not independently promote
a claim from E1 to E2.

---

## 60. Evidence Authenticity Boundary

The following properties
remain distinct:

    ARTIFACT_INTEGRITY

    EXECUTION_AUTHENTICITY

    WORKLOAD_VALIDITY

    MEASUREMENT_CORRECTNESS

    OBSERVATION_COMPLETENESS

    SEMANTIC_CORRECTNESS

    REPRODUCTION_INDEPENDENCE

A matching artifact digest
does not establish every
property above.

A successful benchmark does
not establish every property
above.

A successful verifier result
does not establish every
property above.

Each property requires evidence
appropriate to its meaning.

---

## 61. Falsification Conditions

A confirmed occurrence of any
applicable condition below
constitutes a relevant
counterexample or invalidates
the affected measurement claim:

1. A mandatory correctness
   violation during measured
   execution.

2. Duplicate accounting of
   useful operations.

3. Invalid operations counted
   as successful work.

4. A confirmed mandatory
   latency-limit violation.

5. A confirmed mandatory
   throughput-limit violation.

6. A confirmed mandatory
   resource-limit violation.

7. An invalid workload presented
   as a valid benchmark.

8. An unsupported measurement
   scope presented as end-to-end
   runtime performance.

9. An invalid measurement
   endpoint definition.

10. A fabricated or altered
    measurement presented as
    original execution evidence.

11. Failed executions concealed
    from mandatory outcome
    accounting.

12. A synthetic dataset presented
    as actual runtime measurements.

13. A confirmed optimization
    regression affecting a
    mandatory correctness contract.

14. A verifier accepting a known
    invalid measurement record.

15. An unsupported comparison
    presented as established
    performance superiority.

16. A project-controlled result
    presented as independent
    reproduction without evidence.

Each finding MUST remain
attributable to its actual
affected property.

A measurement defect does
not automatically establish
a runtime correctness defect.

---

## 62. Counterexample Reporting

A performance finding SHOULD
identify:

    FINDING_REFERENCE

    IMPLEMENTATION_REFERENCE

    BENCHMARK_REFERENCE

    EXECUTION_REFERENCE

    EVALUATION_SCOPE

    EXPECTED_MEASUREMENT_CONTRACT

    OBSERVED_MEASUREMENT

    OBSERVED_CORRECTNESS_RESULT

    PROPOSED_VIOLATION

    SUPPORTING_EVIDENCE

    MEASUREMENT_LIMITATIONS

    REPRODUCTION_STATUS

A valid finding MUST NOT be
dismissed merely because the
evaluator lacks access to
proprietary source code.

The engineering conclusion
MUST follow the applicable
evidence.

---

## 63. Remediation and Requalification

Where a performance or
measurement defect is confirmed,
the engineering record SHOULD
distinguish:

- Original implementation reference.
- Original benchmark reference.
- Original measurement evidence.
- Confirmed defect classification.
- Corrected implementation or fixture.
- Subsequent measurement evidence.
- Subsequent correctness evidence.
- Requalification outcome.
- Remaining limitations.

A corrected benchmark fixture
MUST NOT retroactively convert
an invalid historical measurement
into a valid result.

A corrected implementation
MUST remain distinguishable
from the original implementation.

---

## 64. Prohibited Evidence Substitution

The following substitutions
are explicitly prohibited:

    MICROBENCHMARK
        as
    END-TO-END NETWORK PERFORMANCE

    REJECTION RATE
        as
    VALID APPLICATION THROUGHPUT

    TRANSPORT RESTORATION LATENCY
        as
    VERIFIED CONTINUITY LATENCY

    CONFIGURED WORKLOAD
        as
    OBSERVED EXECUTION

    CONFIGURED REPETITIONS
        as
    COMPLETED REPETITIONS

    FASTEST OBSERVED RESULT
        as
    REPRESENTATIVE PERFORMANCE

    ALLOCATION REDUCTION
        as
    SEMANTIC CORRECTNESS

    RACE DETECTOR PASS
        as
    COMPLETE CONCURRENCY CORRECTNESS

    ARTIFACT DIGEST MATCH
        as
    EXECUTION AUTHENTICITY

    HISTORICAL MEASUREMENT
        as
    UNIVERSAL PERFORMANCE GUARANTEE

    SYNTHETIC DATASET
        as
    ACTUAL RUNTIME EVIDENCE

    PROJECT-CONTROLLED EXECUTION
        as
    INDEPENDENT REPRODUCTION

Each stronger claim requires
appropriate supporting evidence.

---

## 65. Publication Readiness Gate

Before publication of a
dedicated performance result,
the evidence owner SHOULD
establish:

    MEASUREMENT_SCOPE_DEFINED

    EXECUTION_ATTRIBUTION_ESTABLISHED

    WORKLOAD_VALIDITY_ESTABLISHED

    MEASUREMENT_UNITS_DEFINED

    OUTCOME_ACCOUNTING_RECONCILED

    CORRECTNESS_RESULTS_AVAILABLE

    ARTIFACT_INTEGRITY_ESTABLISHED

    CONFIDENTIALITY_REVIEW_COMPLETED

    LIMITATIONS_DOCUMENTED

    EVIDENCE_LEVEL_ASSIGNED

These are publication readiness
requirements.

They are not completed
publication review results.

A result that does not satisfy
the applicable gate MUST
retain the corresponding
qualification limitation.

---

## 66. Protected Core Boundary

The following MAY be published
when approved for disclosure:

- Aggregate operation latency.
- Aggregate valid throughput.
- Aggregate resource consumption.
- Approved scaling measurements.
- Approved recovery measurements.
- Approved workload descriptions.
- Public measurement definitions.
- Approved benchmark summaries.
- Approved measurement datasets.
- Evidence integrity manifests.
- Verification outcomes.
- Independent evaluation findings.
- Explicit limitations.

The following remain confidential:

- Proprietary runtime algorithms.
- Internal execution architecture.
- Internal data structures.
- Internal synchronization mechanisms.
- Internal memory ownership models.
- Confidential optimization mechanisms.
- Private benchmark source code.
- Internal profiling traces.
- Internal function-level attribution.
- Protected source code.
- Private runtime interfaces.
- Internal defensive thresholds.
- Cryptographic implementation details.
- Wire-level implementation details.
- Private infrastructure configuration.

Aggregate performance evidence
MUST undergo disclosure review.

The absence of source code
in an artifact does not
automatically establish that
the artifact contains no
sensitive implementation
information.

---

## 67. Technical Reviewer Questions

### Does this document prove that
### VRP achieves a specific throughput?

No.

A specific throughput claim
requires an attributable
measurement record.

### Are the historical quantitative
### results hypothetical targets?

They are historical project-reported
engineering outcomes.

Their stronger interpretation
requires supporting execution
artifacts.

### Can performance be evaluated
### without proprietary source code?

Observable performance properties
can be measured through suitable
authorized evaluation interfaces.

The strength of the conclusion
depends on measurement quality,
workload validity, and evidence
coverage.

### Can an external evaluator
### independently recalculate results?

Yes, where sufficient approved
measurement data is available.

Recalculation remains distinct
from independent execution.

### Does a successful benchmark
### establish protocol correctness?

No.

Applicable semantic correctness
contracts require separate
verification.

### Can performance optimization
### weaken security requirements?

Not under the declared
engineering acceptance contract.

A mandatory correctness regression
invalidates optimization acceptance.

### Does this document establish
### superiority over other protocols?

No.

Comparative superiority requires
dedicated equivalent comparative
evaluation.

### Can an evaluator falsify
### a VRP performance claim?

Yes.

A qualified contradictory
measurement or demonstrated
violation of an applicable
mandatory requirement constitutes
relevant engineering evidence.

---

## 68. Deployment Qualification Boundary

Laboratory performance
measurements do not automatically
establish production suitability.

A deployment evaluation SHOULD
define:

- Intended workload.
- Supported operating conditions.
- Required application throughput.
- Maximum acceptable latency.
- Required recovery behavior.
- Required session continuity.
- Applicable security requirements.
- Available computational resources.
- Mandatory resource limits.
- Evaluation duration.
- Operational termination criteria.
- Acceptance and rejection conditions.

Deployment acceptance remains
specific to the evaluating
organization and environment.

---

## 69. Assurance Limitations

This document does not establish:

- Universal runtime performance.
- Unlimited throughput.
- Unlimited concurrent capacity.
- Zero operation latency.
- Zero resource overhead.
- Universal recovery deadlines.
- Unlimited migration frequency.
- Guaranteed operation under
  every communication condition.
- Universal comparative superiority.
- Complete formal implementation proof.
- Independent third-party certification.

Every empirical performance
claim remains bounded by
its actual execution conditions,
measurement method, evaluated
implementation, observation
coverage, and correctness contract.

---

## 70. Master Evidence Integration

The master claims-to-evidence
matrix MUST associate approved
performance evidence with:

- Applicable claim identifiers.
- Applicable invariant identifiers.
- Performance scenario identifiers.
- Implementation references.
- Measurement scope.
- Execution environment.
- Workload references.
- Actual measurements.
- Correctness verification results.
- Artifact references.
- Evidence sufficiency levels.
- Reproduction records.
- Independent evaluation status.
- Known limitations.

Historical quantitative evidence
MUST remain distinguishable
from dedicated benchmark evidence.

No claim may receive a
qualification status stronger
than its supporting evidence.

---

## 71. Related Assurance Documents

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

---

## 72. Final Engineering Declaration

    SESSION ≠ TRANSPORT

    Architecture defines the contract.

    Execution produces observations.

    Measurement quantifies behavior.

    Verification evaluates correctness.

    Reproduction strengthens evidence.

    Independent evaluation establishes
    an externally attributable conclusion.

    Performance must remain measurable.

    Correctness must remain authoritative.

    Failed executions must remain visible.

    Measurement limitations must remain
    explicit.

    Evidence must remain attributable.

    Historical results must not become
    unsupported universal guarantees.

    Confidentiality must not become
    a substitute for evidence.

    Proprietary implementation does not
    exempt observable behavior from
    technical scrutiny.

    The measurement contract is public.

    The claims are falsifiable.

    The Protected Core remains confidential.

---

**Veil Routing Protocol — VRP**

**Jumping VPN**

**Architect and Creator: Vitalijus Riabovas**

**24 performance qualification scenarios.**

**12 quantitative measurement domains.**

**16 falsification and measurement-invalidity conditions.**

**6 illustrative measurement records.**

**Explicit evidence promotion requirements.**

**Independent measurement recalculation.**

**Correctness-preserving performance qualification.**

**Observable execution. Quantitative evidence.**

**Protected implementation.**

**End of document — VRP-PA-011**
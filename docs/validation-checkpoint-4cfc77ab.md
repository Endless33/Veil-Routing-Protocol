# Validation Checkpoint — 4cfc77ab

## Status

**Public Qualified Validation Checkpoint**

This document records a qualified Veil Routing Protocol (VRP) validation checkpoint covering transport-path admission hardening and real UDP verification.

It provides a stable public evidence anchor for the validated source snapshot while intentionally excluding protected runtime implementation details.

---

## Checkpoint Identity

The qualified checkpoint is:

    Branch:
    fix/stage9s-integrity-hardening

    Commit:
    4cfc77abf81a700b379ead63f0fa14814cdbb419

    Tree:
    9c3d95074bcf6d727ea170f7d85910f968dd4e9e

The local and remote commit identities were verified after publication:

    LOCAL == ORIGIN

    LOCAL_REMOTE_IDENTITY=PASS

This identifies both:

    the Git commit

and:

    the exact repository tree

used for the qualified validation state.

---

## Checkpoint Objective

The checkpoint addresses a transport-path authority boundary.

The security requirement is:

    a newly observed UDP source endpoint
        !=
    automatically authorized active path

The validated invariant is:

    REJECTED_PACKET
        => NO_CANONICAL_COMMIT
        => NO_PERSISTENT_PATH_MUTATION
        => NO_TRANSPORT_CHANGE_INCREMENT

At the same time, legitimate admitted migration must remain possible.

Therefore the complete target is:

    unauthorized path influence = rejected

while:

    authorized transport replacement = preserved

---

## Failure Class

A dangerous ordering exists when persistent path state is modified before packet admission completes.

Conceptually:

    receive packet
        ↓
    observe source endpoint
        ↓
    persist source endpoint
        ↓
    evaluate packet
        ↓
    reject packet

This creates a contradiction:

    packet verdict = rejected

while:

    packet side effect = persisted

A correct rejection verdict is therefore insufficient if unauthorized state mutation has already occurred.

---

## Hardened Boundary

The qualified architecture enforces the opposite ordering:

    receive packet
        ↓
    observe candidate endpoint
        ↓
    canonical decode
        ↓
    admission evaluation
        ↓
    authority decision
        ↓
    persistent path adoption only when permitted

This preserves the distinction:

    candidate endpoint
        !=
    active endpoint

and:

    observation
        !=
    authority

---

## Adversarial Rejection Coverage

The persistent-path invariant was validated against multiple rejection classes.

The public rejection matrix includes:

    wrong session identity

    stale epoch

    replayed packet

For each tested class, the required postcondition was:

    rejection preserved

    canonical commit absent

    active path unchanged

    transport change count unchanged

The tests therefore validate both the decision and the resulting state.

---

## Positive Control

A security fix that prevents every path change would violate the VRP continuity model.

The checkpoint therefore includes a positive control.

A legitimate admitted replacement path must still be able to produce:

    candidate endpoint observed
        ↓
    admission succeeds
        ↓
    path replacement authorized
        ↓
    active endpoint changes
        ↓
    transport change recorded

This behavior was preserved.

Therefore the hardened property is:

    unauthorized path replacement = forbidden

not:

    transport replacement = forbidden

---

## Real Kernel UDP Validation

The path-authority boundary was exercised through real kernel UDP sockets.

The scenario used distinct source endpoints representing:

    legitimate initial path

    rejected foreign path

    legitimate replacement path

The observed sequence was:

    LEGITIMATE_PATH_ESTABLISHED

    REJECTED_ENDPOINT_OBSERVED_NOT_ADOPTED

    LEGITIMATE_PATH_REPLACEMENT_PRESERVED

    REAL_UDP_PRE_ADMISSION_PATH_IMMUTABILITY=PRESERVED

The rejected endpoint was therefore not hypothetical metadata.

It was a real source endpoint observed through the operating system's UDP receive path.

Despite being observable, it did not become the persistent active path.

---

## Validated State Sequence

The validated state transition can be summarized as:

    SESSION ACTIVE
    PATH = A
    TRANSPORT_CHANGES = 0

        |
        | rejected traffic from B
        v

    SESSION ACTIVE
    PATH = A
    TRANSPORT_CHANGES = 0

        |
        | legitimate admitted migration from C
        v

    SESSION ACTIVE
    PATH = C
    TRANSPORT_CHANGES = 1

The forbidden intermediate state:

    PATH = B

was not produced by the rejected traffic.

---

## Qualification Layers

The checkpoint was not qualified from a single passing test.

Validation included multiple layers:

    targeted invariant tests

    repeated target execution

    race-detector target execution

    canonical wire-format regression tests

    full repository tests

    full repository race tests

    real UDP end-to-end validation

The final qualification results were:

    DIFF_CHECK=PASS

    TARGET_REPEATABILITY=PASS

    TARGET_RACE_VALIDATION=PASS

    CANONICAL_WIRE_REGRESSION=PASS

    FULL_REPOSITORY=PASS

    FULL_REPOSITORY_RACE=PASS

    REAL_UDP_E2E=PASS

---

## Race Qualification

Concurrency-sensitive behavior was included in the qualification process.

The hardened target passed race-enabled validation.

The wider repository also passed race-enabled qualification at the checkpoint.

This matters because a state-integrity invariant is incomplete if it holds only under a single serialized execution schedule.

The checkpoint therefore combines:

    semantic validation

with:

    concurrency validation

---

## Canonical Wire Control

The transport-path hardening was qualified alongside the canonical wire boundary.

This ensures that the path-admission work did not silently weaken the established packet contract.

The wire regression control remained passing at the checkpoint.

The resulting architecture preserves the ordering:

    canonical packet processing
        before
    persistent path authority

rather than allowing transport metadata to bypass canonical ingress.

---

## Repository Scope

The checkpoint was intentionally narrow.

The committed change set contained:

    one transport-path production hardening change

    one adversarial path-state validation suite

    one real UDP end-to-end validation suite

The checkpoint was created only after the intended staged scope was verified.

No unrelated tracked modifications were included in the qualified commit.

---

## Remote Qualification

After local qualification, the checkpoint was published to the remote branch.

The resulting identity was verified:

    LOCAL:
    4cfc77abf81a700b379ead63f0fa14814cdbb419

    ORIGIN:
    4cfc77abf81a700b379ead63f0fa14814cdbb419

Result:

    LOCAL_REMOTE_IDENTITY=PASS

The public evidence anchor therefore refers to a remotely identifiable Git commit rather than an uncommitted local state.

---

## Public Invariants Established

The checkpoint supports the following public invariants:

    SESSION != TRANSPORT

    RECEIVE != ADMIT

    OBSERVATION != AUTHORITY

    CANDIDATE_PATH != ACTIVE_PATH

    REJECTION => NO PERSISTENT PATH MUTATION

    REJECTION => NO TRANSPORT CHANGE INCREMENT

    LEGITIMATE ADMISSION => PATH REPLACEMENT MAY OCCUR

    TRANSPORT CHANGE != SESSION LOSS

These invariants describe externally meaningful behavior without exposing protected runtime mechanics.

---

## Security Interpretation

The network controls what the runtime can observe.

The protocol controls what becomes authoritative.

Therefore:

    NETWORK OBSERVATION
            |
            v
    CANDIDATE INFORMATION
            |
            v
    CANONICAL PROTOCOL BOUNDARY
            |
            v
    AUTHORITY DECISION
            |
            v
    PERSISTENT STATE

The forbidden shortcut is:

    NETWORK OBSERVATION
            |
            +------------------> PERSISTENT AUTHORITY

The checkpoint validates protection against that shortcut for the tested path-admission scenarios.

---

## Continuity Interpretation

The hardening does not weaken VRP's continuity objective.

The validated behavior remains:

    transport A
        ↓
    legitimate migration
        ↓
    transport B

while:

    logical session survives

The protocol therefore preserves both:

    mobility

and:

    authority

Transport remains replaceable.

Transport does not become self-authorizing.

---

## Remaining Authority Boundary

This checkpoint intentionally does not declare every transport-reattachment semantic finalized.

One important architectural question remains separate:

    canonical execution authority
        != necessarily
    transport reattachment authority

In particular, suppression of a duplicate canonical mutation answers:

    should this mutation execute again?

It does not automatically answer:

    may this already-authorized session reattach transport?

That distinction is relevant to future validation of scenarios such as:

    NAT rebinding

    transport recovery

    path reattachment

    migration without duplicate execution

No final reattachment rule is claimed by this checkpoint without independent evidence.

---

## Non-Claims

This document does not claim:

    that every possible transport attack has been eliminated

    that every NAT behavior has been validated

    that duplicate mutation automatically permits reattachment

    that duplicate mutation automatically forbids reattachment

    that canonical execution and transport authority are permanently identical

The checkpoint records what was actually qualified.

Nothing more is inferred.

---

## Evidence Discipline

VRP validation follows a simple principle:

    claim only what evidence supports

For this checkpoint, the evidence supports:

    rejected endpoint cannot persistently replace
    the active path in the validated scenarios

and:

    legitimate admitted path replacement remains functional

Future authority claims require their own adversarial evidence.

---

## Checkpoint Summary

    CHECKPOINT=4cfc77ab

    COMMIT=
    4cfc77abf81a700b379ead63f0fa14814cdbb419

    TREE=
    9c3d95074bcf6d727ea170f7d85910f968dd4e9e

    LOCAL_REMOTE_IDENTITY=PASS

    REJECTED_PATH_MUTATION=PREVENTED

    WRONG_SESSION_PATH_INFLUENCE=REJECTED

    STALE_EPOCH_PATH_INFLUENCE=REJECTED

    REPLAY_PATH_INFLUENCE=REJECTED

    LEGITIMATE_PATH_REPLACEMENT=PRESERVED

    REAL_KERNEL_UDP=VALIDATED

    REPEATABILITY=PASS

    RACE_QUALIFICATION=PASS

    CANONICAL_WIRE_CONTROL=PASS

    FULL_REPOSITORY_VALIDATION=PASS

---

## Conclusion

Checkpoint `4cfc77ab` establishes a qualified VRP transport-path admission boundary.

A network endpoint may be observed without becoming authoritative.

Rejected traffic does not gain persistent path influence in the validated scenarios.

Legitimate transport replacement remains functional.

The result strengthens the VRP continuity model:

    SESSION != TRANSPORT

with the validated authority rules:

    OBSERVATION != AUTHORITY

    REJECTION != PARTIAL COMMIT

    TRANSPORT REPLACEMENT REQUIRES AUTHORITY

This checkpoint is an immutable public evidence anchor for that result.
# Rejected Endpoint Adversarial Validation

## Status

**Public Validation Report**

This document records adversarial validation of the Veil Routing Protocol (VRP) transport-path admission boundary.

The purpose of this validation is not merely to verify that malformed or unauthorized packets receive a rejection verdict.

The stronger requirement is:

> Rejected traffic must leave no persistent transport-path side effect.

Protected runtime implementation details are intentionally excluded.

---

## Validation Objective

A network runtime necessarily observes the source endpoint of every received UDP datagram.

That observation must not itself grant authority over persistent path state.

The validation target is therefore:

    REJECTED_PACKET
        => ACTIVE_PATH_UNCHANGED
        => TRANSPORT_CHANGE_COUNT_UNCHANGED
        => NO_CANONICAL_COMMIT

This protects the distinction between:

    packet arrival

and:

    authorized path adoption

---

## Adversarial Model

Assume a legitimate session already has an accepted transport endpoint.

An adversarial packet then arrives from a different UDP source.

The attacker therefore controls an observable property:

    source endpoint

but must not automatically control:

    active transport path

The runtime is allowed to observe the new endpoint.

It is not allowed to persist that endpoint merely because a datagram arrived from it.

---

## Failure Classes

The boundary was tested against multiple independent rejection conditions.

### Wrong Session Identity

A packet referencing a session other than the active logical session must be rejected.

Required invariant:

    WRONG_SESSION
        => REJECT
        => ACTIVE_PATH_UNCHANGED

A foreign session identity must not gain transport-path influence over the existing session.

---

### Stale Epoch

A packet carrying an epoch older than the currently authoritative epoch must not influence current transport state.

Required invariant:

    STALE_EPOCH
        => REJECT
        => ACTIVE_PATH_UNCHANGED

This prevents historical traffic from becoming a mechanism for path rollback.

---

### Replay

A previously observed packet identity must not gain new authority merely by being delivered again from another endpoint.

Required invariant:

    REPLAY
        => REJECT
        => ACTIVE_PATH_UNCHANGED

Replay rejection therefore protects both canonical execution and the persistent path boundary tested here.

---

## Why Verdict-Only Testing Is Insufficient

A runtime can produce the correct rejection verdict and still be incorrect.

Consider:

    receive packet
        ↓
    adopt source endpoint
        ↓
    evaluate packet
        ↓
    reject packet

The visible result says:

    REJECTED

while persistent state may already contain:

    active_remote = rejected_source

This is a state-integrity failure despite the apparently correct verdict.

Therefore the adversarial tests inspect both:

    decision correctness

and:

    state immutability after rejection

---

## Required Post-Rejection State

For every tested rejection class, validation requires all of the following:

    ingress rejection preserved

    canonical mutation not committed

    previous active endpoint preserved

    transport change count preserved

The security property fails if any one of these conditions fails.

---

## Positive Control

A defensive boundary must not accidentally convert transport continuity into transport immobility.

A legitimate admitted replacement endpoint was therefore tested separately.

Required behavior:

    legitimate packet
        ↓
    admission succeeds
        ↓
    candidate path authorized
        ↓
    active endpoint changes
        ↓
    transport change recorded

This positive control demonstrates that the protection distinguishes unauthorized influence from legitimate migration.

The intended property is:

    rejected endpoint cannot replace active path

not:

    active path can never change

---

## Adversarial Matrix

The validated public matrix is:

    +----------------------+------------+----------------------+------------------+
    | Scenario             | Admission  | Persistent Path      | Canonical Commit |
    +----------------------+------------+----------------------+------------------+
    | Wrong session        | Rejected   | Preserved            | No               |
    | Stale epoch          | Rejected   | Preserved            | No               |
    | Replay               | Rejected   | Preserved            | No               |
    | Legitimate migration | Accepted   | Authorized change    | Yes              |
    +----------------------+------------+----------------------+------------------+

The matrix intentionally validates both negative and positive behavior.

---

## Repeated Validation

The hardened boundary was subjected to repeated execution rather than relying on a single successful run.

The relevant target tests were executed repeatedly, including under Go's race detector.

The validation sequence included:

    targeted invariant tests

    repeated target execution

    race-enabled target execution

    canonical wire-format regression tests

    full repository tests

    full repository race tests

    real UDP end-to-end validation

All qualified checks completed successfully at the validated checkpoint.

---

## Real Transport Evidence

The same invariant was exercised through real kernel UDP sockets.

Three distinct source endpoints represented:

    legitimate initial path

    rejected foreign path

    legitimate replacement path

The observed sequence was:

    legitimate endpoint
        => admitted
        => active path established

    rejected endpoint
        => physically observed
        => rejected
        => not adopted

    legitimate replacement endpoint
        => admitted
        => active path replaced

This is significant because the rejected source endpoint was not hypothetical metadata.

It was a real endpoint supplied by the operating system's UDP receive path.

---

## Security Meaning

The validation establishes a narrow but important security boundary:

    network observation
        !=
    persistent authority

An attacker may be capable of causing the runtime to observe a source address.

That alone does not entitle the attacker to replace the accepted transport path.

The runtime must derive persistent authority from protocol state and admission semantics rather than from transport metadata alone.

---

## Relationship to Session Continuity

VRP is built around the principle:

    Session != Transport

Therefore changing transport cannot be categorically forbidden.

Instead, VRP requires controlled replacement:

    session remains authoritative
        ↓
    transport may become unavailable
        ↓
    replacement transport may appear
        ↓
    replacement must cross the appropriate authority boundary
        ↓
    session continuity may be preserved

The adversarial tests protect this model from being inverted into:

    new transport appeared
        ↓
    therefore new transport is authoritative

That inference is explicitly rejected.

---

## Scope Boundary

This validation does not claim that every transport reattachment scenario has already been assigned its final protocol semantics.

In particular:

    canonical execution authority
        != necessarily
    transport reattachment authority

A duplicate canonical mutation may correctly be prevented from executing twice while a separate transport-continuity question still exists.

Examples include:

    NAT rebinding

    legitimate endpoint replacement

    transport recovery

    path migration

Those cases require their own authority contract.

The current validation establishes the prerequisite:

> Traffic that fails admission must not mutate persistent path state.

It does not prematurely define every future case in which an admitted session may reattach transport.

---

## Validated Result

The adversarial validation produced the following public result:

    WRONG_SESSION_PATH_INFLUENCE=REJECTED

    STALE_EPOCH_PATH_INFLUENCE=REJECTED

    REPLAY_PATH_INFLUENCE=REJECTED

    REJECTED_ENDPOINT_PERSISTENCE=REJECTED

    LEGITIMATE_PATH_REPLACEMENT=PRESERVED

    RACE_VALIDATION=PASS

    REAL_UDP_VALIDATION=PASS

---

## Public Conclusion

The tested VRP boundary enforces:

    REJECTED TRAFFIC
            |
            v
    MAY BE OBSERVED
            |
            v
    MUST NOT BECOME
    PERSISTENT PATH AUTHORITY

while preserving:

    LEGITIMATE ADMISSION
            |
            v
    AUTHORIZED PATH CHANGE
            |
            v
    SESSION CONTINUITY

This is a direct consequence of the VRP model:

**transport is replaceable, but transport metadata is not authority.**
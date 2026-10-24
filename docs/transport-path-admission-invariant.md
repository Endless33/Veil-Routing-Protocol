# Transport Path Admission Invariant

## Status

**Public Architecture Note**

This document describes a validated security invariant of the Veil Routing Protocol (VRP) public architecture.

It intentionally documents observable guarantees and validation outcomes without exposing protected runtime internals.

---

## Core Principle

VRP treats a network endpoint as an observation, not as authority.

A packet arriving from a new UDP source address does not, by itself, authorize that address to become the active transport path of an existing session.

In compact form:

    observed endpoint != authorized path

and:

    UDP source address != session authority

This distinction is essential for a continuity-oriented protocol in which:

    Session != Transport

A transport path may change while the logical session survives.

However, the ability of transport to change must not allow rejected traffic to rewrite persistent session-associated path state.

---

## Security Invariant

The validated invariant is:

    REJECTED_PACKET
        => NO_CANONICAL_COMMIT
        => NO_PERSISTENT_PATH_MUTATION
        => NO_TRANSPORT_CHANGE_INCREMENT

A packet that fails admission must not gain persistent influence over the currently accepted transport path.

This applies even when the packet is physically received by the operating system and therefore has a real observable source endpoint.

Receipt is not admission.

Observation is not authorization.

---

## Threat Model

Consider an established logical session using an accepted UDP endpoint.

An unrelated or adversarial endpoint then sends traffic toward the same runtime.

The runtime may legitimately observe:

    candidate_remote = attacker_endpoint

But observation of that endpoint must not automatically produce:

    active_remote = attacker_endpoint

If the packet fails the protocol's admission requirements, persistent path state must remain unchanged.

Otherwise an attacker could potentially influence transport state without first satisfying the protocol's canonical admission rules.

---

## Unsafe Ordering

The dangerous architectural ordering is:

    receive packet
        ↓
    observe UDP source
        ↓
    mutate persistent path state
        ↓
    validate packet
        ↓
    reject packet

At the end of this sequence the packet may be rejected while its transport-side effect has already occurred.

That violates the intended boundary.

A rejection verdict is insufficient if persistent state was modified before the verdict was reached.

---

## Required Ordering

The hardened ordering is conceptually:

    receive packet
        ↓
    observe candidate endpoint
        ↓
    decode canonical packet
        ↓
    evaluate admission
        ↓
    derive authorization outcome
        ↓
    only then permit persistent path adoption

The candidate endpoint remains observational data until the relevant admission boundary has been crossed.

This produces an important property:

    rejection is side-effect free

with respect to persistent transport-path state.

---

## Adversarial Validation

The invariant was exercised against multiple independent rejection classes.

Validated cases included:

    wrong session identity
    stale epoch
    replayed packet

For every tested rejection class, the required result was:

    persistent remote endpoint unchanged
    transport change counter unchanged
    canonical mutation not committed

The validation therefore tests more than the returned error or verdict.

It tests the absence of unauthorized persistent side effects.

---

## Positive Control

Security validation must also prove that hardening did not disable legitimate migration.

A valid admitted packet arriving through a legitimate replacement transport path was therefore tested as a positive control.

Expected behavior:

    valid candidate endpoint observed
        ↓
    packet admitted
        ↓
    path adoption permitted
        ↓
    active endpoint replaced
        ↓
    transport change recorded exactly once

The positive control passed.

The resulting property is therefore not:

    path changes are forbidden

It is:

    unauthorized path changes are forbidden

That distinction is fundamental to VRP.

---

## Real UDP Validation

The boundary was additionally exercised using real kernel UDP sockets rather than only synthetic state transitions.

The validation used distinct source sockets representing:

1. an initially legitimate transport path,
2. a rejected endpoint,
3. a legitimate replacement transport path.

Observed behavior:

    LEGITIMATE PATH
        ↓
    active path established

    REJECTED ENDPOINT
        ↓
    endpoint observed
        ↓
    endpoint not adopted
        ↓
    active path preserved

    LEGITIMATE MIGRATION
        ↓
    new endpoint admitted
        ↓
    active path replaced
        ↓
    transport continuity preserved

This demonstrates that the invariant survives interaction with real UDP source endpoints.

---

## What This Proves

The validation supports the following public claim:

> A rejected UDP packet cannot replace the persistent active transport path merely by arriving from a different source endpoint.

It also demonstrates that the protection does not prevent an admitted legitimate path replacement.

Together these establish:

    REJECTED_ENDPOINT
        => OBSERVABLE
        => NOT_AUTHORITATIVE
        => NOT_PERSISTENT

    LEGITIMATE_ADMITTED_ENDPOINT
        => MAY_BECOME_ACTIVE_PATH

---

## What This Does Not Prove

This invariant deliberately does not define every future transport-reattachment rule.

In particular, VRP distinguishes several concepts that must not be collapsed prematurely:

    packet admission
    canonical mutation execution
    transport/path authorization
    transport reattachment
    session continuity

A packet may eventually be valid for one purpose while being intentionally prevented from performing another.

For example, rejection of duplicate canonical execution does not automatically answer whether an already-authorized session may reattach through a new transport after NAT rebinding.

That is a separate authority question and must be validated independently.

Therefore this document does **not** claim:

    canonical_commit == transport_reattachment_authority

as a permanent protocol rule.

---

## Architectural Consequence

VRP's continuity model requires transport to remain replaceable.

Its security model requires transport replacement to remain controlled.

Those requirements coexist through a strict separation:

    Session Identity
          |
          | survives
          v
    Transport Path A
          |
          | authorized replacement
          v
    Transport Path B

The network may tell the runtime where a packet came from.

The network does not get to decide which endpoint becomes authoritative.

---

## Public Invariant

The resulting public architectural invariant is:

    SESSION != TRANSPORT

    OBSERVATION != AUTHORITY

    RECEIPT != ADMISSION

    REJECTION => NO PERSISTENT PATH MUTATION

    AUTHORIZED MIGRATION => TRANSPORT MAY CHANGE
                             SESSION MAY SURVIVE

This boundary is part of VRP's broader goal:

**continuity without surrendering authority to transport behavior.**
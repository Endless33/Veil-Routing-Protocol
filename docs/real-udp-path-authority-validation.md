# Real UDP Path Authority Validation

## Status

**Public Validation Evidence**

This document records a real-transport validation of the Veil Routing Protocol (VRP) path-authority boundary.

The objective was to verify that the path-admission invariant survives interaction with real kernel UDP sockets and distinct source endpoints.

This report intentionally exposes validation behavior and architectural guarantees only.

Protected runtime internals are not included.

---

## Validation Question

The test asks a narrow security question:

> Can a rejected packet arriving from a different real UDP source endpoint replace the persistent active path of an existing session?

The required answer is:

    NO

At the same time, the test must demonstrate that a legitimate admitted replacement endpoint can still become active.

Therefore both properties must hold:

    rejected endpoint
        => cannot replace active path

    legitimate admitted endpoint
        => may replace active path

This distinction is necessary for VRP's continuity model:

    Session != Transport

---

## Why Real UDP Matters

A pure state-machine test can prove important logical properties.

It cannot, by itself, prove that the same boundary is preserved when endpoint information originates from the operating system's real network stack.

With UDP, the runtime receives both:

    packet bytes

and:

    source endpoint metadata

The source endpoint is therefore real external input.

The validation intentionally exercised this boundary using kernel-managed UDP sockets.

---

## Test Topology

The validation used one receiving UDP endpoint and three distinct sending endpoints.

Conceptually:

    CLIENT A
    legitimate initial path
          |
          v
    +------------------+
    |                  |
    |   VRP UDP        |
    |   validation     |
    |   boundary       |
    |                  |
    +------------------+
          ^
          |
    CLIENT B
    rejected endpoint

followed by:

    CLIENT C
    legitimate replacement path
          |
          v
    +------------------+
    |                  |
    |   same logical   |
    |   session        |
    |                  |
    +------------------+

The operating system assigned distinct UDP source endpoints to the clients.

The validation explicitly required those sources to be distinct.

---

## Phase 1 — Establish Legitimate Path

The first client represented the legitimate initial transport.

Its packet crossed the required admission boundary.

Expected result:

    legitimate packet received
        ↓
    packet admitted
        ↓
    candidate endpoint authorized
        ↓
    active path established

The initial path was established successfully.

At this point:

    session = preserved

    active path = legitimate source A

    transport changes = 0

The initial establishment is not counted as a replacement of an existing transport.

---

## Phase 2 — Inject Rejected Endpoint

A second UDP socket then transmitted from a different real source endpoint.

This endpoint represented traffic that must not gain authority over the existing path.

The operating system legitimately reported the new source address to the receiver.

Therefore:

    rejected endpoint was observable

But the required security property was:

    observable
        !=
    authoritative

The packet failed admission.

The validation then inspected persistent state.

Required result:

    active path remains source A

    transport change count remains unchanged

    rejected source B is not persisted as active path

    no canonical mutation is committed by rejected traffic

The invariant was preserved.

---

## Phase 3 — Legitimate Path Replacement

A third distinct UDP source was then used to represent a legitimate replacement transport.

This phase is essential.

Without it, a test could appear secure merely because all path changes had accidentally been disabled.

The third packet crossed the required admission boundary.

Expected result:

    legitimate replacement observed
        ↓
    packet admitted
        ↓
    replacement authorized
        ↓
    active path changes A -> C
        ↓
    transport change recorded exactly once

The legitimate replacement succeeded.

---

## Observed Validation Sequence

The public evidence sequence was:

    LEGITIMATE_PATH_ESTABLISHED

    REJECTED_ENDPOINT_OBSERVED_NOT_ADOPTED

    LEGITIMATE_PATH_REPLACEMENT_PRESERVED

    REAL_UDP_PRE_ADMISSION_PATH_IMMUTABILITY=PRESERVED

The important transition is:

    active = legitimate A

        ↓

    attacker B arrives

        ↓

    active = legitimate A

        ↓

    legitimate C arrives

        ↓

    active = legitimate C

The rejected endpoint existed at the real transport layer but never became the persistent active path.

---

## State Transition Model

The validated behavior can be represented as:

    STATE 0

    session = active
    path = none

        |
        | legitimate admission from A
        v

    STATE 1

    session = active
    path = A
    transport_changes = 0

        |
        | rejected traffic from B
        v

    STATE 2

    session = active
    path = A
    transport_changes = 0

        |
        | legitimate admitted migration from C
        v

    STATE 3

    session = active
    path = C
    transport_changes = 1

The forbidden transition was:

    STATE 1
        |
        | rejected traffic from B
        v
    path = B

That transition did not occur.

---

## Security Property

The real UDP validation supports the following invariant:

    RECEIVE_FROM(endpoint)
        !=
    AUTHORIZE(endpoint)

More specifically:

    rejected UDP source
        => may be observed
        => must not replace active path

while:

    admitted legitimate source
        => may be authorized
        => may replace active path

The network stack provides location information.

It does not provide VRP authority.

---

## Persistent-State Requirement

The validation does not stop at checking a rejection result.

After rejected traffic, the following state must remain unchanged:

    active remote endpoint

    transport replacement count

    canonical committed state

This matters because a system can reject a packet too late.

For example:

    packet received
        ↓
    source persisted
        ↓
    packet rejected

would produce a correct-looking rejection verdict while leaving an unauthorized state mutation behind.

VRP validation therefore checks the post-rejection state, not only the verdict.

---

## Repeatability and Race Qualification

The path-admission hardening was not accepted based on one successful real UDP execution.

The qualification included:

    targeted invariant validation

    repeated target execution

    race-detector execution

    canonical wire regression validation

    full repository validation

    full repository race validation

    final real UDP execution

At the qualified checkpoint:

    targeted validation = PASS

    repeated validation = PASS

    race validation = PASS

    canonical wire validation = PASS

    full repository validation = PASS

    full repository race validation = PASS

    real UDP validation = PASS

---

## Validated Checkpoint

The validation was qualified against the following Git checkpoint:

    Commit:
    4cfc77abf81a700b379ead63f0fa14814cdbb419

    Tree:
    9c3d95074bcf6d727ea170f7d85910f968dd4e9e

The local checkpoint and remote branch identity were verified to match after publication.

This provides an immutable reference for the validated source snapshot.

---

## What This Validation Proves

The evidence supports the following public statements:

1. A real UDP source endpoint can be observed without automatically becoming authoritative.

2. Rejected traffic from a distinct source endpoint does not replace the persistent active path in the validated scenario.

3. Rejected traffic does not increment the validated transport-change state.

4. Legitimate admitted migration remains functional.

5. The security hardening therefore preserves both rejection integrity and legitimate transport replacement.

---

## What This Validation Does Not Claim

This test does not establish that every possible transport reattachment scenario has already been assigned final protocol semantics.

In particular, it does not collapse:

    canonical mutation execution

and:

    transport reattachment authorization

into a single permanent rule.

A future or separately validated scenario may involve:

    NAT rebinding

    path recovery

    transport reattachment

    duplicate canonical mutation suppression

while still requiring the logical session to survive.

Those semantics require independent authority analysis.

The result documented here is narrower and already validated:

> A rejected endpoint cannot acquire persistent path authority merely because the operating system observed traffic from it.

---

## Architectural Meaning

VRP is designed around replaceable transport.

That requires two properties to coexist:

    transport must be able to change

and:

    arbitrary transport input must not control the change

The validated boundary therefore looks like:

    NETWORK
       |
       | supplies candidate endpoint
       v
    OBSERVATION
       |
       | protocol admission / authority
       v
    AUTHORIZATION
       |
       | only after authorization
       v
    PERSISTENT PATH STATE

The forbidden shortcut is:

    NETWORK
       |
       +----------------------> PERSISTENT PATH STATE

Transport metadata does not bypass protocol authority.

---

## Public Result

The final public result is:

    REAL_KERNEL_UDP=VALIDATED

    DISTINCT_SOURCE_ENDPOINTS=VALIDATED

    REJECTED_ENDPOINT_OBSERVATION=PRESERVED

    REJECTED_ENDPOINT_ADOPTION=PREVENTED

    ACTIVE_PATH_IMMUTABILITY_AFTER_REJECTION=PRESERVED

    LEGITIMATE_PATH_REPLACEMENT=PRESERVED

    SESSION_CONTINUITY_MODEL=PRESERVED

    RACE_QUALIFICATION=PASS

---

## Conclusion

The real UDP validation demonstrates a fundamental VRP boundary:

    the network may reveal a new path

but:

    the network cannot declare that path authoritative

A candidate transport endpoint becomes persistent only after crossing the appropriate protocol boundary.

That preserves the core VRP relationship:

    SESSION != TRANSPORT

and strengthens it with a second rule:

    TRANSPORT OBSERVATION != TRANSPORT AUTHORITY

The result is controlled mobility:

**transport can change without allowing rejected traffic to control where the session moves.**
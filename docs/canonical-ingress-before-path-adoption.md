# Canonical Ingress Before Path Adoption

## Status

**Public Architecture and Security Note**

This document defines a validated ordering rule for the Veil Routing Protocol (VRP) transport boundary.

The rule is intentionally simple:

    persistent transport state must not be changed
    merely because a packet arrived from a new endpoint

A newly observed endpoint is candidate information.

It becomes persistent path state only after crossing the appropriate protocol boundary.

This document describes the public invariant and its validation consequences without exposing protected runtime implementation details.

---

## Fundamental Ordering Rule

The validated ordering is:

    RECEIVE
        ↓
    OBSERVE
        ↓
    DECODE
        ↓
    ADMIT
        ↓
    AUTHORIZE
        ↓
    ADOPT

Not:

    RECEIVE
        ↓
    OBSERVE
        ↓
    ADOPT
        ↓
    VALIDATE LATER

The difference is security-critical.

---

## Why Ordering Matters

UDP delivers two important classes of information to a runtime:

    packet content

and:

    source endpoint

Both originate outside the trusted protocol state.

The operating system can truthfully report:

    packet arrived from endpoint X

But that statement does not imply:

    endpoint X is authorized for this session

Therefore VRP treats the source endpoint as observational input until the relevant packet has crossed the required protocol boundary.

---

## Candidate State vs Persistent State

The architecture distinguishes:

    candidate endpoint

from:

    active endpoint

A candidate endpoint represents:

    where the current packet was observed

An active endpoint represents:

    transport state that the runtime has accepted persistently

These values may eventually become equal.

They must not become equal automatically.

Conceptually:

    candidate_remote = observed network input

    active_remote = accepted persistent state

The transition:

    candidate_remote
        ↓
    active_remote

requires authorization.

---

## The Pre-Admission Mutation Failure Class

A dangerous implementation pattern is:

    packet arrives from new endpoint
        ↓
    persistent path immediately updated
        ↓
    packet evaluated
        ↓
    packet rejected

This creates an inconsistency:

    verdict = rejected

while:

    persistent side effect = committed

Such behavior violates fail-closed state handling.

A rejection must mean more than:

    execution did not continue

For security-sensitive state it must also mean:

    unauthorized persistent mutation did not occur

---

## Correct Boundary

The hardened conceptual boundary is:

    external UDP datagram
            |
            v
    +---------------------+
    | Observe Candidate   |
    | Endpoint            |
    +---------------------+
            |
            v
    +---------------------+
    | Canonical Decode    |
    +---------------------+
            |
            v
    +---------------------+
    | Admission /         |
    | Authority Decision  |
    +---------------------+
            |
       +----+----+
       |         |
    REJECT      PERMIT
       |         |
       v         v
    preserve   path may
    state      be adopted

The rejected branch must not reach persistent path adoption.

---

## Rejection Must Be State-Safe

For the validated rejection classes:

    wrong session

    stale epoch

    replay

the required consequence is:

    REJECT
        ↓
    NO CANONICAL COMMIT
        ↓
    NO PERSISTENT PATH REPLACEMENT
        ↓
    NO TRANSPORT CHANGE INCREMENT

This is stronger than ordinary input validation.

It is an atomicity property across the admission boundary.

---

## Observation Is Allowed

The architecture does not attempt to hide the fact that a packet arrived.

The runtime may observe:

    source endpoint

    packet bytes

    arrival event

The security requirement is not:

    rejected input must be invisible

It is:

    rejected input must not become persistent authority

Therefore:

    observation != mutation

and:

    observation != authorization

---

## Positive Path

The opposite branch is equally important.

After a legitimate candidate satisfies the required boundary, persistent path adoption may be permitted.

Conceptually:

    legitimate candidate observed
        ↓
    canonical packet decoded
        ↓
    admission succeeds
        ↓
    relevant authority established
        ↓
    persistent path may change

This preserves transport mobility.

The hardened architecture therefore does not freeze the transport layer.

It controls when transport replacement becomes persistent.

---

## Relationship to Session Identity

VRP separates logical session identity from the transport currently carrying traffic.

The central relationship remains:

    Session != Transport

A session may survive:

    endpoint replacement

    network transition

    path migration

    transport interruption

    transport recovery

But replaceable transport introduces a security requirement:

> Transport replacement must not implicitly replace session authority.

The session remains the higher-level continuity object.

Transport is subordinate and replaceable.

---

## Why Source Address Cannot Be Authority

Source addresses are properties of packet delivery.

They may change for legitimate reasons, including:

    network migration

    NAT behavior

    rebinding

    failover

    path recovery

They may also be influenced by traffic that should never become authoritative.

Therefore VRP cannot safely use the rule:

    new source observed
        => new source trusted

Instead:

    new source observed
        => candidate only

followed by:

    candidate + required authority
        => eligible for persistent adoption

---

## Canonical Decode Is Part of the Boundary

Path authority must not bypass canonical packet processing.

A packet that does not satisfy the accepted wire contract must not gain persistent path influence merely because its source endpoint is available before decoding completes.

The conceptual ordering therefore preserves:

    wire validity
        before
    protocol admission

and:

    protocol admission
        before
    persistent path adoption

This prevents transport metadata from becoming an alternate path around canonical ingress rules.

---

## Adversarial Consequence

Assume:

    active path = A

Then traffic arrives from:

    endpoint B

If B's packet is rejected, the required postcondition is:

    active path = A

not:

    active path = B
    packet = rejected

The second state is forbidden because the rejected input has already gained persistent influence.

---

## Real UDP Evidence

The ordering rule was validated using real kernel UDP sockets.

The sequence included:

    legitimate endpoint A
        ↓
    active path established

    rejected endpoint B
        ↓
    B observed by kernel receive path
        ↓
    B rejected
        ↓
    active path remains A

    legitimate endpoint C
        ↓
    C admitted
        ↓
    active path becomes C

This demonstrates both halves of the contract:

    rejection cannot mutate path

and:

    legitimate migration remains possible

---

## Authority Separation

This architecture deliberately avoids claiming that all forms of authority are identical.

The following concepts may have different rules:

    ingress admission

    canonical mutation execution

    session authority

    transport/path authority

    transport reattachment

A packet being prevented from executing a canonical mutation twice does not automatically determine whether an already-authorized logical session may later reattach transport.

Therefore:

    canonical execution result
        != automatically
    complete transport authority policy

This distinction is important for future validation of cases such as NAT rebinding and recovery.

---

## Duplicate Execution Boundary

Consider a packet or operation whose canonical mutation has already been committed.

The correct execution decision may be:

    DO NOT EXECUTE AGAIN

That protects canonical state from duplicate mutation.

However, it does not by itself prove either:

    ALLOW TRANSPORT REATTACHMENT

or:

    DENY TRANSPORT REATTACHMENT

Those are separate conclusions.

They require an explicit transport-authority contract.

VRP therefore avoids deriving transport semantics accidentally from an execution-side boolean.

---

## Design Requirement

A robust implementation should make the following distinction observable in its architecture:

    What happened to canonical state?

and:

    What is permitted to happen to transport state?

The answers may often align.

They must not be assumed to be permanently identical.

This protects the architecture from coupling:

    execution authority

to:

    transport continuity

without an explicit protocol decision.

---

## Validated Invariants

At the qualified boundary, the following public invariants are supported:

    RECEIVE != ADMIT

    OBSERVE != AUTHORIZE

    CANDIDATE_PATH != ACTIVE_PATH

    REJECTED_PACKET => NO PERSISTENT PATH MUTATION

    REJECTED_PACKET => NO TRANSPORT CHANGE INCREMENT

    LEGITIMATE_ADMISSION => PATH CHANGE MAY BE PERMITTED

    SESSION != TRANSPORT

---

## Fail-Closed Interpretation

Fail-closed behavior is not limited to returning an error.

For persistent state, fail-closed means:

    uncertainty
        ↓
    rejection
        ↓
    previous authoritative state preserved

Therefore a rejected candidate does not become a partial success.

There is no state in which VRP should intentionally report:

    admission failed

while silently retaining:

    path mutation caused by that failed admission

The state transition and the verdict must agree.

---

## Architectural Pattern

The public pattern can be summarized as:

    UNTRUSTED NETWORK INPUT

              |
              v

    +-------------------+
    | OBSERVATION       |
    | candidate only    |
    +-------------------+

              |
              v

    +-------------------+
    | CANONICAL INGRESS |
    | decode + validate |
    +-------------------+

              |
              v

    +-------------------+
    | AUTHORITY         |
    | decision boundary |
    +-------------------+

          /       \
         /         \
        v           v

    REJECTED      AUTHORIZED

        |             |
        v             v

    PRESERVE      PERSISTENT
    STATE         CHANGE MAY
                  OCCUR

---

## Validated Checkpoint

This ordering was qualified at the following source checkpoint:

    Commit:
    4cfc77abf81a700b379ead63f0fa14814cdbb419

    Tree:
    9c3d95074bcf6d727ea170f7d85910f968dd4e9e

The local and remote commit identities were verified to match after publication.

---

## Public Security Statement

VRP does not treat the network's statement:

    "this packet came from endpoint X"

as equivalent to the protocol statement:

    "endpoint X is now authoritative"

Between those statements lies the canonical protocol boundary.

That boundary protects persistent transport state from rejected traffic while preserving legitimate transport replacement.

---

## Conclusion

The validated rule is:

    OBSERVE FIRST
        ↓
    VALIDATE
        ↓
    ESTABLISH AUTHORITY
        ↓
    MUTATE ONLY IF PERMITTED

Never:

    OBSERVE
        ↓
    MUTATE
        ↓
    DISCOVER LATER THAT INPUT WAS INVALID

For VRP, correct rejection includes preservation of authoritative state.

That principle extends the core continuity model:

    SESSION != TRANSPORT

with an equally important boundary:

    TRANSPORT OBSERVATION != PATH AUTHORITY
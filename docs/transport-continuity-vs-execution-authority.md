# Transport Continuity vs Execution Authority

## Status

**Public Architecture Boundary Note**

This document describes an architectural separation in the Veil Routing Protocol (VRP):

    canonical execution authority
        !=
    transport continuity authority

The distinction is important because VRP is designed around a logical session that may survive changes in its underlying transport.

This document records the boundary without claiming protocol semantics that have not yet been independently validated.

Protected runtime internals are intentionally excluded.

---

## Core Principle

VRP begins with:

    Session != Transport

A logical session is not defined solely by the network path currently carrying its packets.

Therefore several different decisions may exist during packet processing:

    Is this packet admissible?

    May this operation mutate canonical state?

    Has this mutation already been committed?

    Is this transport endpoint authorized?

    May an existing session reattach through a replacement path?

These questions are related.

They are not necessarily identical.

---

## Two Different Authority Domains

Consider two conceptual authority domains.

### Canonical Execution Authority

This determines whether an operation is permitted to change canonical protocol state.

Examples include preventing:

    replayed execution

    stale execution

    duplicate mutation

    unauthorized mutation

The central question is:

    MAY THIS OPERATION EXECUTE?

---

### Transport Continuity Authority

This determines whether a transport path may become associated with an already-existing logical session.

Examples may include:

    legitimate migration

    NAT rebinding

    transport recovery

    endpoint replacement

    failover

The central question is:

    MAY THIS TRANSPORT CARRY THE SESSION?

These are different questions.

---

## Why the Separation Matters

Suppose a canonical mutation has already executed successfully.

A later packet refers to the same mutation.

The correct canonical execution result may be:

    mutation already committed
        ↓
    do not execute again

That protects state from duplicate execution.

But this alone does not logically establish:

    transport reattachment denied

Nor does it establish:

    transport reattachment allowed

The execution result answers only the execution question.

A separate authority rule is required before drawing conclusions about transport.

---

## The Dangerous Coupling

An implementation can accidentally encode:

    canonicalCommit == true
        => transport may change

    canonicalCommit == false
        => transport may never change

This may be correct for some scenarios.

It must not become a permanent protocol rule merely because both decisions currently share an implementation path.

Otherwise the protocol risks confusing:

    "do not execute this mutation again"

with:

    "this session cannot legitimately move"

Those statements have different meanings.

---

## Duplicate Mutation Example

Consider:

    packet admitted

    mutation identity already committed

The execution-side result may conceptually be:

    ACCEPTED_INGRESS

    REJECTED_DUPLICATE_MUTATION_NO_COMMIT

The important fact is:

    canonical mutation must not execute twice

That is a strong and necessary invariant.

But the following question remains separate:

> If the logical session is still authoritative, can a newly observed transport endpoint be accepted as a legitimate reattachment without executing the mutation again?

This document intentionally does not answer that question.

It identifies it as an independent protocol boundary requiring explicit validation.

---

## Why This Matters for NAT Rebinding

Transport endpoints can change without the logical session itself changing.

A common conceptual example is NAT rebinding.

The external network representation of a peer may change:

    endpoint A
        ↓
    network/NAT change
        ↓
    endpoint B

while higher-level session identity may remain continuous.

If transport continuity were permanently coupled to the requirement for a new canonical mutation, a continuity-oriented protocol could accidentally require state execution merely to recognize a legitimate path change.

Whether VRP should permit such reattachment depends on the final authority contract.

It must be decided deliberately, not accidentally.

---

## Security Constraint

Separating authority domains must not weaken the already validated rejection invariant.

The following remains required:

    rejected packet
        => no persistent path mutation

A rejected endpoint does not gain path authority simply because transport continuity exists as a separate concept.

Therefore separation means:

    different decisions require explicit authority

It does not mean:

    transport becomes permissive

---

## Existing Validated Boundary

The currently validated public property is:

    rejected traffic
        ↓
    may be observed
        ↓
    cannot rewrite persistent active path

while:

    legitimate admitted migration
        ↓
    may replace transport path

This establishes a secure baseline.

Any future transport-reattachment rule must preserve that baseline.

---

## Required Future Question

For an admitted packet whose canonical mutation is already committed, the architecture must eventually answer:

    Is the session identity valid?

    Is the packet sufficiently authenticated?

    Is its authority current?

    Is the epoch acceptable?

    Is the candidate path eligible?

    Is reattachment permitted independently of execution?

    Can transport change without re-executing canonical state?

The exact mechanism is intentionally outside this public document.

The important requirement is that the answer be explicit and testable.

---

## Desired Separation

Conceptually, VRP should be able to reason about:

    EXECUTION DECISION
        |
        +--> execute
        |
        +--> reject stale
        |
        +--> suppress duplicate
        |
        +--> reject unauthorized

independently from:

    TRANSPORT DECISION
        |
        +--> preserve current path
        |
        +--> authorize migration
        |
        +--> authorize reattachment
        |
        +--> reject candidate path

A particular protocol event may produce decisions in both domains.

One decision should not silently substitute for the other.

---

## Example Decision Matrix

The following matrix is architectural, not a declaration of final semantics:

    +----------------------+----------------------+----------------------+
    | Condition            | Execution Decision   | Transport Decision   |
    +----------------------+----------------------+----------------------+
    | Wrong session        | Reject               | Reject               |
    | Stale authority      | Reject               | Reject               |
    | Replay               | Reject               | Reject               |
    | New valid mutation   | Execute              | Evaluate/Permit      |
    | Duplicate mutation   | Suppress duplicate   | Independently decide |
    +----------------------+----------------------+----------------------+

The final row is deliberately unresolved.

That unresolved state is preferable to encoding an accidental rule without evidence.

---

## Continuity Requirement

A continuity protocol must tolerate transport replacement without allowing transport to redefine identity.

The intended hierarchy is:

    SESSION IDENTITY
          |
          | remains authoritative
          v
    SESSION AUTHORITY
          |
          +------------------+
          |                  |
          v                  v
    EXECUTION            TRANSPORT
    AUTHORITY            AUTHORITY
          |                  |
          v                  v
    canonical state      active path

This model makes explicit that transport is subordinate to the session rather than the source of session identity.

---

## Fail-Closed Requirement

Independent transport authority must remain fail-closed.

If sufficient authority cannot be established:

    candidate endpoint
        ↓
    NOT ADOPTED

The separation documented here must never be interpreted as:

    execution denied
        => path automatically allowed

Instead:

    execution decision
        => explicit result

    transport decision
        => explicit result

No implicit authority is created between them.

---

## Replay and Duplicate Mutation Are Not Synonyms

A replayed packet and a duplicate mutation are not necessarily the same architectural event.

A replay concerns repeated packet-level input.

A duplicate mutation concerns an operation whose canonical effect has already been committed.

Depending on the final protocol contract, these may require different treatment.

Therefore VRP should avoid collapsing:

    packet replay

    mutation duplication

    transport reattachment

into a single generic rejection concept.

Each protects a different invariant.

---

## Evidence Requirement

Any future reattachment contract should be validated adversarially.

A credible validation should demonstrate both:

    unauthorized endpoint cannot reattach

and:

    legitimate continuity scenario remains possible

It should additionally verify:

    no duplicate canonical execution

    no stale authority acceptance

    no session identity substitution

    no unauthorized path persistence

    deterministic postcondition

    race-safe behavior

The transport decision must remain observable through evidence rather than assumed from implementation structure.

---

## Public Non-Claim

At this stage VRP does not use this document to claim:

    duplicate mutation always permits reattachment

or:

    duplicate mutation always forbids reattachment

Neither statement follows from the currently published evidence alone.

The validated claim is narrower:

> Canonical execution authority and transport reattachment authority are distinct architectural questions and should not be permanently coupled without an explicit protocol contract.

---

## Relationship to Path Admission

The previously validated path-admission rule remains intact:

    observe candidate endpoint
        ↓
    cross required protocol boundary
        ↓
    establish relevant authority
        ↓
    persistent adoption may occur

The new architectural question is simply whether:

    canonical mutation commit

is always the authority required for the final step.

That requires separate evidence.

---

## Design Direction

The architectural direction is:

    avoid boolean authority collapse

A single implementation result should not silently represent multiple independent security decisions unless the protocol specification explicitly defines them as equivalent.

Instead, VRP aims for decisions that remain explainable:

    Why was execution allowed?

    Why was execution suppressed?

    Why was transport preserved?

    Why was transport replaced?

    Which authority justified each result?

This improves both security reasoning and independent validation.

---

## Validated Baseline

The analysis begins from a qualified source checkpoint:

    Commit:
    4cfc77abf81a700b379ead63f0fa14814cdbb419

    Tree:
    9c3d95074bcf6d727ea170f7d85910f968dd4e9e

At this checkpoint:

    rejected endpoint path adoption = prevented

    legitimate admitted path replacement = preserved

    real UDP validation = PASS

    repeated validation = PASS

    race validation = PASS

The next authority distinction can therefore be investigated without weakening the already-qualified path-admission invariant.

---

## Public Architecture Statement

VRP separates identity from transport.

The same discipline applies inside the authority model:

    SESSION != TRANSPORT

    OBSERVATION != AUTHORITY

    EXECUTION AUTHORITY != TRANSPORT AUTHORITY

    DUPLICATE SUPPRESSION != AUTOMATIC PATH POLICY

The goal is not merely mobility.

The goal is controlled continuity in which every persistent transition has an explicit authority basis.

---

## Conclusion

A continuity protocol cannot safely derive every transport decision from whether canonical state changed.

Sometimes:

    canonical state should remain unchanged

while the transport question still requires evaluation.

Likewise, a transport transition must never become a way to bypass canonical execution protections.

The architecture therefore preserves both sides:

    canonical mutations execute only when authorized

and:

    transport changes only when independently justified

This separation keeps VRP aligned with its foundational principle:

**the session survives transport change without allowing transport to become the source of authority.**
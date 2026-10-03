# Veil Routing Protocol — Technology Comparison

**Project:** Veil Routing Protocol (VRP)  
**Author:** Vitalijus Riabovas  
**Development:** 2024–2026  
**Status:** Public Architectural Comparison  
**Implementation:** Protected / Private

> **SESSION ≠ TRANSPORT**

> **CONTINUITY FIRST.**

---

# 1. Purpose

This document explains how the **Veil Routing Protocol (VRP)** relates conceptually to established networking technologies.

It exists primarily to prevent a common misunderstanding:

> VRP is not another implementation of QUIC connection migration, Multipath TCP, VPN roaming or ordinary application reconnection.

Those technologies solve important problems.

VRP addresses a different architectural responsibility.

This document does not claim that VRP is universally superior to any technology discussed here.

The technologies may coexist.

---

# 2. The Central Difference

Many networking mechanisms answer questions such as:

> How can communication continue when the network path changes?

VRP asks an additional question:

> What logical execution remains canonical while the network underneath it changes?

That difference can be summarized as:

    TRANSPORT CONTINUITY

            !=

    CANONICAL SESSION CONTINUITY

VRP focuses on the second problem.

---

# 3. What VRP Is Not Claiming

VRP does not claim to have invented:

- connection migration;
- roaming;
- multipath networking;
- transport failover;
- tunnel rebinding;
- reconnect;
- replay protection as a general concept;
- session management as a general concept;
- distributed recovery as a general concept.

These areas have substantial prior art.

The VRP project instead defines a specific architecture around:

- transport-independent logical session identity;
- explicit lifecycle;
- canonical execution;
- authority continuity;
- stale-work rejection;
- replay containment;
- duplicate containment;
- recovery validation;
- fail-closed behavior.

---

# 4. Different Layers Solve Different Problems

A simplified stack may look like:

    ┌─────────────────────────────┐
    │        APPLICATION          │
    └──────────────┬──────────────┘
                   │
                   v
    ┌─────────────────────────────┐
    │    VRP CONTINUITY LAYER     │
    │                             │
    │ session                     │
    │ lifecycle                   │
    │ authority                   │
    │ canonical state             │
    │ recovery                    │
    └──────────────┬──────────────┘
                   │
                   v
    ┌─────────────────────────────┐
    │      TRANSPORT LAYER        │
    │                             │
    │ QUIC / TCP / UDP / MPTCP /  │
    │ tunnel / relay / other      │
    └──────────────┬──────────────┘
                   │
                   v
                NETWORK

The exact deployment architecture may differ.

The important point is separation of responsibility.

---

# 5. VRP and QUIC

QUIC is a transport protocol.

Among its capabilities, QUIC can support connection migration, allowing a connection to survive certain changes in network path or endpoint addressing.

That is valuable transport behavior.

VRP does not attempt to redefine QUIC.

A deployment may conceptually use:

    APPLICATION
        |
        v
    VRP
        |
        v
    QUIC
        |
        v
    NETWORK

In such a deployment, QUIC may handle transport concerns while VRP handles logical continuity concerns.

---

# 6. QUIC Connection Identity

QUIC includes mechanisms that reduce dependence on a single traditional network tuple.

This enables transport continuity across certain path changes.

VRP operates at a different boundary.

Its concern is not only:

    DID THE CONNECTION SURVIVE?

It also asks:

    IS THE LOGICAL SESSION CURRENT?

    IS THE LIFETIME CURRENT?

    IS THE AUTHORITY CURRENT?

    IS THIS OPERATION HISTORICAL?

    IS THIS EXECUTION A REPLAY?

    MAY THIS EXECUTION BECOME CANONICAL?

Transport migration does not, by itself, answer these questions.

---

# 7. VRP Is Not "QUIC Plus"

VRP should not be described as:

> QUIC with more migration logic.

That description places the architecture at the wrong layer.

QUIC can potentially be an underlying transport for VRP.

VRP does not require ownership of QUIC's transport responsibilities in order to govern continuity above them.

---

# 8. VRP and Multipath TCP

Multipath TCP allows a TCP connection to use multiple network paths.

Its concerns include transport behavior across those paths.

VRP does not attempt to replace multipath transport.

Conceptually:

    APPLICATION
        |
        v
    VRP
        |
        v
    MPTCP
        |
        v
    MULTIPLE NETWORK PATHS

MPTCP can provide path diversity.

VRP can separately govern logical continuity.

---

# 9. Multipath Does Not Define Canonical State

A system may have multiple valid network paths while still facing logical execution problems.

For example:

- an old operation may return;
- execution may be duplicated;
- authority may have moved;
- a previous lifecycle may still have delayed work;
- recovery may race with current execution.

Therefore:

    MULTIPLE VALID PATHS

            !=

    ONE VALID CANONICAL HISTORY

VRP focuses on the latter problem.

---

# 10. VRP and WireGuard

WireGuard is a VPN technology designed to provide secure network tunneling.

Its responsibilities are fundamentally different from VRP's continuity model.

Conceptually:

    APPLICATION
        |
        v
    VRP
        |
        v
    WIREGUARD
        |
        v
    NETWORK

WireGuard may provide secure connectivity.

VRP may govern logical continuity above that connectivity.

VRP does not claim that a continuity layer makes secure tunneling unnecessary.

---

# 11. Secure Tunnel ≠ Session Continuity

A secure tunnel can establish authenticated and encrypted connectivity.

That does not automatically answer:

- whether a logical session belongs to the current lifetime;
- whether an operation is historical;
- whether authority is stale;
- whether execution has already occurred;
- whether recovery is canonical.

Therefore:

    SECURE CONNECTIVITY

            !=

    CANONICAL SESSION CONTINUITY

Both may be required.

---

# 12. VRP and Traditional VPN Roaming

Some VPN systems support roaming or tolerate endpoint-address changes.

This is useful when a device moves between networks.

VRP does not claim to have invented that behavior.

The distinction is again architectural.

VPN roaming may answer:

> Can this peer continue communicating from a new network location?

VRP additionally asks:

> Which logical execution state remains valid while that communication changes?

---

# 13. Historical Naming

The project originally developed under the name:

**Jumping VPN**

That name reflected an earlier focus on network transition and connectivity.

As the project evolved, the architecture expanded beyond the scope normally implied by the term VPN.

The modern project name:

**Veil Routing Protocol**

reflects the broader continuity architecture.

VRP should therefore not be interpreted as merely a renamed VPN tunnel.

---

# 14. VRP and Ordinary Reconnect

Many applications handle connection loss with:

    CONNECTION LOST
          |
          v
       RECONNECT
          |
          v
    AUTHENTICATE
          |
          v
    RESTORE STATE
          |
          v
       CONTINUE

This is a valid design.

VRP does not claim that reconnect is inherently incorrect.

The difference appears when logical continuity requirements become stronger.

---

# 15. Reconnect Can Create a New Context

A reconnect-oriented architecture may intentionally create:

- a new socket;
- a new transport connection;
- a new process context;
- a new application session;
- reconstructed application state.

That may be exactly what the application wants.

VRP becomes relevant when the requirement is instead:

> Preserve one logical session across replaceable transport while continuing to enforce lifecycle, authority and canonical execution rules.

---

# 16. Reconnection Does Not Automatically Resolve Historical Work

Consider:

    OPERATION A CREATED

          |
          v

    CONNECTION LOST

          |
          v

    RECONNECT

          |
          v

    NEW EXECUTION CONTEXT

          |
          v

    OLD OPERATION A ARRIVES

The network is connected again.

The logical problem remains.

Should Operation A execute?

Reconnect alone cannot answer that question.

---

# 17. VRP and Application Sessions

Applications have used session abstractions for decades.

VRP does not claim to have invented sessions.

The relevant distinction is how the session interacts with:

- transport replacement;
- lifecycle;
- authority;
- replay;
- recovery;
- canonical execution.

The specific combination of these concerns defines the VRP architecture.

---

# 18. VRP and Distributed State Machines

Distributed systems frequently use state machines to govern execution.

VRP does not claim to have invented state machines.

A protected VRP implementation may use state-oriented techniques where appropriate.

The architectural contribution lies in the continuity model, not in claiming ownership of state-machine theory.

---

# 19. VRP and Consensus Systems

Consensus systems address problems such as agreement among distributed participants.

VRP should not automatically be interpreted as a replacement for a consensus protocol.

The concerns can overlap in distributed environments, but they are not equivalent.

A deployment may still require an established consensus mechanism independently of VRP.

---

# 20. VRP and High Availability

High-availability systems attempt to maintain service despite component failures.

VRP shares an interest in failure and recovery but does not equate continuity with availability.

A system can remain available while executing incorrect state.

Therefore:

    AVAILABLE

        !=

    CANONICALLY CORRECT

VRP prioritizes correct continuity.

---

# 21. VRP and Failover

Failover commonly moves responsibility from one component to another.

VRP does not claim to have invented failover.

The VRP concern is what happens to authority and historical execution around that event.

For example:

    AUTHORITY A
         |
         X
      FAILURE
         |
         v
    AUTHORITY B
         |
         v
    A RETURNS

The important question is not only whether A is reachable.

It is whether A remains authoritative.

---

# 22. VRP and Replay Protection

Replay protection is an established security concept.

VRP does not claim otherwise.

Within VRP, replay protection is integrated into the broader continuity problem.

A replay is not merely a packet-security concern.

It can become a canonical-state concern if historical execution is allowed to re-enter the current runtime.

---

# 23. VRP and Idempotency

Application idempotency can reduce the consequences of repeated operations.

That remains valuable.

VRP does not replace application-level idempotency.

The responsibilities differ.

Application idempotency may answer:

> Is repeating this operation safe?

VRP may need to answer:

> Should this operation be admitted into current canonical execution at all?

Both questions may matter.

---

# 24. VRP and Database Transactions

Database transactions protect database-level consistency according to their transaction model.

VRP does not replace them.

A continuity runtime may interact with applications that use transactional databases.

The database and VRP still operate at different boundaries.

---

# 25. VRP and Message Queues

Message queues may provide:

- buffering;
- redelivery;
- persistence;
- ordering;
- acknowledgement.

Those features do not automatically determine whether delayed work belongs to the current session lifecycle.

A queued message can be validly delivered and still be historically invalid for current execution.

---

# 26. VRP and Service Meshes

Service meshes provide infrastructure capabilities such as:

- service discovery;
- routing;
- retries;
- observability;
- policy enforcement;
- secure service communication.

VRP does not attempt to replace the entire service-mesh layer.

A service mesh may move or retry traffic.

VRP's concern remains the validity of logical execution across those events.

---

# 27. VRP and SD-WAN

SD-WAN technologies may dynamically manage network paths.

VRP does not compete with path-selection infrastructure merely because both respond to network change.

Conceptually:

    APPLICATION
        |
        v
    VRP
        |
        v
    SD-WAN / NETWORK CONTROL
        |
        v
    AVAILABLE PATHS

The SD-WAN layer can manage connectivity.

VRP can separately govern session continuity.

---

# 28. VRP and Mobility

Mobility systems have long addressed changing network attachment.

VRP does not claim to have invented mobility.

Its architectural question remains:

> What logical execution state remains canonical while mobility occurs?

Mobility is one environment where this question can become important.

---

# 29. Comparison by Responsibility

A simplified conceptual comparison:

| Technology / Model | Primary Concern |
|---|---|
| TCP | Reliable byte-stream transport |
| UDP | Datagram transport |
| QUIC | Secure multiplexed transport with modern transport features |
| MPTCP | Multipath TCP transport |
| WireGuard | Secure network tunneling |
| VPN roaming | Connectivity across endpoint/network changes |
| Reconnect logic | Re-establishing application communication |
| Service mesh | Service-to-service networking and policy infrastructure |
| VRP | Canonical logical continuity across transport instability |

This table describes primary architectural concerns.

It is not a feature ranking.

---

# 30. These Technologies Are Not Mutually Exclusive

A real system could conceptually contain several of these technologies simultaneously.

For example:

    APPLICATION
        |
        v
    VRP
        |
        v
    QUIC
        |
        v
    VPN / SECURE NETWORK
        |
        v
    SD-WAN
        |
        v
    PHYSICAL NETWORK

Whether such a stack is appropriate depends entirely on the target environment.

The diagram exists only to show that these technologies occupy different responsibilities.

---

# 31. The Wrong Comparison

A misleading comparison would be:

    VRP vs QUIC

as though both were competing implementations of the same transport protocol.

That is not the intended architecture.

A more useful question is:

> Which layer owns which responsibility?

---

# 32. Responsibility Separation

Conceptually:

    ┌──────────────────────────────────┐
    │ APPLICATION SEMANTICS            │
    │                                  │
    │ business logic                   │
    │ domain state                     │
    │ external side effects            │
    └────────────────┬─────────────────┘
                     │
                     v
    ┌──────────────────────────────────┐
    │ VRP CONTINUITY RESPONSIBILITY    │
    │                                  │
    │ logical session                  │
    │ lifecycle                        │
    │ authority                        │
    │ canonical execution              │
    │ recovery validity                │
    └────────────────┬─────────────────┘
                     │
                     v
    ┌──────────────────────────────────┐
    │ TRANSPORT RESPONSIBILITY         │
    │                                  │
    │ packet / stream transport        │
    │ congestion behavior              │
    │ transport migration              │
    │ transport security               │
    └────────────────┬─────────────────┘
                     │
                     v
    ┌──────────────────────────────────┐
    │ NETWORK RESPONSIBILITY           │
    │                                  │
    │ addressing                       │
    │ routing                          │
    │ physical connectivity            │
    └──────────────────────────────────┘

The exact boundary varies by deployment.

The separation of concerns is the important part.

---

# 33. Transport Migration Is Still Useful

VRP's existence does not make transport migration less useful.

The opposite may be true.

If an underlying transport can efficiently survive a path change, VRP may have less transport disruption to manage.

Existing transport capabilities should therefore be used where appropriate.

VRP is not based on deliberately ignoring mature networking technology.

---

# 34. Why VRP Still Exists

If existing transport migration is useful, why introduce VRP?

Because transport migration and canonical execution are different problems.

Suppose a transport successfully migrates.

The system may still need to know:

- whether the current session lifetime is valid;
- whether authority changed during the event;
- whether delayed work belongs to the old context;
- whether a duplicate operation was already accepted;
- whether recovery crossed a canonical boundary.

Those questions exist above transport migration.

---

# 35. A Successful Network Event Can Still Produce a Logical Failure

Consider:

    PATH MIGRATION
         |
         v
      SUCCESS

but:

    STALE AUTHORITY
         |
         v
      ACCEPTED

The network transition succeeded.

The logical continuity failed.

Or:

    RECONNECT
       |
       v
    SUCCESS

but:

    OLD OPERATION
       |
       v
    EXECUTED AGAIN

Again:

    CONNECTIVITY SUCCESS

does not imply:

    CONTINUITY SUCCESS

---

# 36. A Network Failure Can Still Preserve Logical Correctness

The inverse is also important.

A transport may fail completely.

The correct result may temporarily be:

    NO CONNECTIVITY

while canonical state remains protected.

This can be preferable to accepting ambiguous execution merely to preserve availability.

Therefore VRP follows:

    CORRECTNESS
        >
    CONNECTIVITY

when the two cannot safely coexist.

---

# 37. VRP Does Not Promise Better Performance Than Every Alternative

This document makes no claim that VRP is universally:

- faster than QUIC;
- lower latency than TCP;
- more efficient than MPTCP;
- more secure than WireGuard;
- more scalable than every distributed runtime.

Those would require specific comparable benchmarks and deployment conditions.

VRP's architectural proposition is different.

---

# 38. VRP Does Not Replace Security Engineering

Likewise, VRP does not eliminate the need for:

- secure transport;
- authentication;
- authorization;
- key management;
- host security;
- network security;
- application security;
- operational security.

Continuity correctness is one security-relevant boundary.

It is not the entire security system.

---

# 39. VRP Does Not Replace Application Engineering

VRP also does not eliminate:

- transaction design;
- application idempotency;
- domain validation;
- persistence;
- error handling;
- application recovery;
- external-side-effect management.

The continuity layer must coexist with these responsibilities.

---

# 40. When Existing Technology May Be Enough

An organization may not need VRP.

For example, existing technology may be sufficient when:

- reconnecting into a new logical session is acceptable;
- transport migration alone satisfies the requirement;
- no meaningful logical state must survive;
- stale execution is not possible or consequential;
- authority does not move;
- existing application recovery already provides the required semantics.

Adding another runtime layer without a real requirement would increase complexity unnecessarily.

---

# 41. When the VRP Problem Appears

VRP becomes more relevant when several conditions exist together:

- logical sessions outlive transports;
- transports change frequently;
- delayed work can return;
- duplicate execution matters;
- authority may move;
- recovery can race;
- canonical state must remain singular;
- reconnecting is not equivalent to continuing;
- continuity behavior needs to be independently observed.

These conditions define the problem space more accurately than any specific transport technology.

---

# 42. Comparison Summary

The simplest distinction is:

### QUIC

Helps transport survive network-path changes.

### MPTCP

Allows TCP transport to use multiple paths.

### WireGuard

Provides secure network tunneling.

### VPN Roaming

Allows secure connectivity to tolerate endpoint movement.

### Reconnect

Re-establishes communication after connection loss.

### VRP

Governs which logical session, lifecycle, authority and execution remain canonical across transport instability.

These are different responsibilities.

---

# 43. The Architectural Question

The public VRP architecture can therefore be reduced to one question:

> When the transport changes, what is still true?

Not merely:

> Can packets move again?

But:

    IS THIS STILL THE SAME SESSION?

    IS THIS THE CURRENT LIFETIME?

    IS THIS THE CURRENT AUTHORITY?

    IS THIS OPERATION CURRENT?

    HAS IT ALREADY EXECUTED?

    IS RECOVERY VALID?

    MAY IT BECOME CANONICAL?

If the system cannot answer these questions, restoring connectivity may not be enough.

---

# 44. Final Comparison Statement

VRP is not presented as a replacement for the networking technologies that already move traffic successfully.

Those technologies should continue doing what they do well.

VRP addresses the logical continuity problem that remains when transport itself is no longer treated as the canonical identity of execution.

QUIC may migrate.

MPTCP may use another path.

A VPN may roam.

A tunnel may reconnect.

A relay may change.

The network may recover.

VRP asks what happens next:

> Which execution is still valid?

That is the distinction.

---

# SESSION ≠ TRANSPORT

# CONTINUITY FIRST.

---

**Veil Routing Protocol (VRP)**  
**Vitalijus Riabovas**  
**2024–2026**

Public architectural comparison.  
Protected implementation.
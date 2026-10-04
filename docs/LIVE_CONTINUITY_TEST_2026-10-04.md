# VRP Live Continuity Test — 2026-10-04

**Project:** Veil Routing Protocol (VRP)  
**Test class:** Live network / transport continuity observation  
**Date:** 2026-10-04  
**Status:** PUBLIC EVIDENCE RECORD  
**Result:** PASS — LIVE TRANSPORT CONTINUITY DEMONSTRATED

---

# 1. Purpose

This document records a real-network VRP continuity test performed on
2026-10-04.

The purpose of the test was to observe what happens when the underlying
network transport disappears and is replaced while a logical session is
already active.

The architectural principle under observation was:

> SESSION ≠ TRANSPORT

The test was designed to answer a narrow and measurable question:

Can a logical session remain identifiable while its underlying network
transport is lost and replaced?

This document records observable evidence from the test.

It does not require trust in a presentation, diagram, or client-side
status message.

The test included:

- a physical Android device;
- a real Wi-Fi network;
- a real mobile/5G network;
- a public Internet path;
- an Oracle Linux endpoint;
- a live UDP server;
- server-side packet observation;
- tcpdump packet capture;
- monotonically progressing client sequence numbers;
- explicit transport generation changes;
- live acknowledgements from the receiving endpoint.

---

# 2. Test Environment

## Client

Physical Android device running Termux.

The client maintained the logical session identifier:

    session=android-live

The client generated monotonically increasing sequence numbers.

Two network paths were used:

    WIFI
    MOBILE / 5G

Transport replacement was explicitly represented by a transport
generation counter.

Observed transition:

    generation 1 -> generation 2

The logical session identifier remained:

    android-live

---

## Server

The receiving endpoint was an Oracle Linux virtual machine.

Repository:

    jumping-vpn-core

Publicly recorded source revision during the test:

    HEAD=a10f57afff94

Full revision recorded during the environment preflight:

    a10f57afff9482842c15d1924522a182fa0ac437

Tree recorded during the environment preflight:

    2a9affe99b888055f9e94c30571460548da91881

The live test server listened on:

    UDP/39001

The server recorded incoming packets and returned acknowledgements.

A simultaneous tcpdump process independently observed UDP traffic on
the server interface.

---

# 3. Network Topology

The test exercised two materially different network paths.

## Wi-Fi path

    Android
        |
        | Wi-Fi
        v
    Local network
        |
        v
    Windows / VMware NAT
        |
        v
    Oracle Linux VM
        |
        v
    UDP/39001

## Mobile path

    Android
        |
        | Mobile / 5G
        v
    Mobile operator network
        |
        v
    Public Internet
        |
        v
    Public test endpoint
        |
        v
    Windows / VMware NAT
        |
        v
    Oracle Linux VM
        |
        v
    UDP/39001

The mobile path was therefore not simply another local interface on the
same LAN.

It traversed an external network path before reaching the server.

---

# 4. Initial State

The logical session started over Wi-Fi.

Initial transport state:

    SESSION=android-live
    TRANSPORT=WIFI
    TRANSPORT_GENERATION=1

Packets were successfully transmitted and acknowledged.

The sequence counter advanced normally while Wi-Fi remained available.

---

# 5. Physical Transport Loss

Wi-Fi connectivity was physically removed during the running session.

The client subsequently observed real network failures.

Observed failure classes included:

    Network is unreachable

and:

    TIMEOUT

Example progression from the recorded run:

    seq=24
    seq=25
    seq=26
    seq=27

reported transport/network failure.

Additional attempts:

    seq=28
    seq=29
    seq=30

did not receive successful acknowledgements.

This is significant because the transition did not begin from a
synthetic "migration requested" state.

The currently active network path actually stopped working.

---

# 6. Transport Replacement

After Wi-Fi transport loss, the client replaced the transport.

Recorded transition:

    OLD_TRANSPORT=WIFI
    NEW_TRANSPORT=MOBILE
    NEW_GENERATION=2

The logical session identifier remained:

    SESSION=android-live

The transport changed.

The logical session identifier did not.

This is the central observation of the test.

---

# 7. Sequence Continuity

The sequence counter was not reset when the new transport was created.

Before the first successful mobile acknowledgement, attempts had
progressed through:

    seq=30

The first successful acknowledgement observed on the replacement
mobile transport was:

    seq=31

Recorded client-side event:

    ACK
    session=android-live
    seq=31
    gen=2
    mode=MOBILE

The sequence space therefore continued across the transport
replacement rather than restarting with the new transport.

Important interpretation:

`seq=30` was an attempted transmission during the interrupted period.

It is not claimed to have been successfully acknowledged.

The relevant observation is that creation of the replacement transport
did not reset the client sequence progression.

---

# 8. First Mobile Recovery

The replacement transport became operational immediately after the
transition.

Recorded first successful mobile acknowledgement:

    UTC=2026-10-04T07:10:38.091Z
    ACK
    session=android-live
    seq=31
    gen=2
    mode=MOBILE
    rtt_ms=72.9

The same logical session identifier was therefore present after the
network path changed.

Subsequent mobile acknowledgements continued successfully.

---

# 9. Server-Side Observation

The test was not evaluated solely from client output.

The Oracle Linux endpoint independently observed the incoming mobile
traffic.

A later visible portion of the run recorded packets including:

    session=android-live
    seq=180
    transport_generation=2
    mode=mobile
    ack_sent=true

followed by:

    session=android-live
    seq=181
    transport_generation=2
    mode=mobile
    ack_sent=true

and:

    session=android-live
    seq=182
    transport_generation=2
    mode=mobile
    ack_sent=true

This provides receiving-side confirmation that packets associated with
the mobile transport reached the server.

---

# 10. Independent Packet Observation

During the live test, tcpdump ran alongside the server.

The packet capture independently displayed bidirectional UDP traffic
between the external mobile-side source and the Oracle endpoint.

The observable relationship was:

    MOBILE NETWORK SOURCE
            |
            | UDP
            v
    ORACLE ENDPOINT:39001
            |
            | UDP ACK
            v
    MOBILE NETWORK SOURCE

This matters because packet visibility did not depend solely on the
application's own log messages.

There were two independent server-side observation surfaces:

1. application/server output;
2. operating-system packet capture using tcpdump.

---

# 11. Evidence Correlation

The test produced correlated observations at multiple layers.

## Client observation

The Android client showed:

    Wi-Fi operation
        ->
    Wi-Fi failure
        ->
    network errors / timeout
        ->
    transport replacement
        ->
    MOBILE generation 2
        ->
    successful ACK

## Server observation

The Oracle server showed:

    incoming mobile packet
        ->
    same logical session identifier
        ->
    continuing sequence numbers
        ->
    generation 2
        ->
    acknowledgement sent

## Packet observation

tcpdump independently showed:

    external mobile traffic
        ->
    UDP/39001
        ->
    Oracle endpoint
        ->
    response traffic

The three observation surfaces therefore describe the same network
event from different positions.

---

# 12. What Was Demonstrated

The live test demonstrated the following observable properties.

### Real transport failure occurred

The active Wi-Fi path became unavailable and generated actual network
errors/timeouts.

### A different network transport was subsequently used

Traffic resumed through the mobile/5G path.

### Logical session identity remained stable

The identifier remained:

    session=android-live

across the observed transport replacement.

### Transport generation changed

The transition was represented as:

    generation 1 -> generation 2

### Sequence progression did not restart

The sequence space continued across transport replacement.

### The receiving endpoint observed the replacement path

The Oracle endpoint received the mobile packets.

### Responses were observed

The server returned acknowledgements to the client.

### Packet capture independently observed the traffic

tcpdump showed the bidirectional UDP exchange independently of the
application log.

---

# 13. What This Test Does NOT Claim

Evidence is useful only when its scope is explicit.

This test is NOT presented as proof of the complete protected VRP Core
security model.

This individual experiment does not, by itself, prove:

- the complete VRP security model;
- cryptographic security of the protected runtime;
- authority or epoch correctness;
- replay rejection;
- duplicate-execution prevention;
- canonical-state correctness;
- adversarial resistance under every failure mode;
- production readiness;
- superiority over another protocol.

Those properties require their own tests and evidence.

The result documented here is intentionally narrower.

It demonstrates observable live transport-continuity behavior under a
real Wi-Fi-to-mobile network transition.

---

# 14. Reproducibility Principle

VRP engineering follows a simple rule:

    IMPLEMENTED.
    TESTED.
    BROKEN.
    FIXED.
    REGRESSION-TESTED.
    DOCUMENTED.

Claims should be separated from evidence.

A public architecture can describe intended behavior.

A live test can demonstrate observable behavior.

Hashes can establish artifact identity.

Git history can establish publication history.

Independent reproduction can test whether the result survives outside
the original environment.

These are different evidence layers and should not be conflated.

---

# 15. Public Video Evidence

A recording of the live experiment has been published publicly.

Video:

    https://youtu.be/D_OGd5BA8o8

The recording provides visual evidence of the live environment and
network activity.

The video should be interpreted together with this document and the
associated cryptographic artifact hashes.

---

# 16. Evidence Integrity

This document is intended to become part of a cryptographically
identified public evidence record.

After this file is finalized, its SHA-256 digest should be calculated
from the exact committed bytes.

The resulting evidence record should contain at minimum:

    document path
    SHA-256(document)
    Git commit
    Git tree
    UTC timestamp

The hash MUST be calculated after the document is finalized.

Changing even one byte after hashing creates a different SHA-256
digest.

For that reason, no SHA-256 value is pre-written into this document
before the final artifact exists.

---

# 17. Evidence Chain

The intended public evidence relationship is:

    LIVE NETWORK EVENT
            |
            v
    VIDEO RECORD
            |
            v
    SERVER LOG / PACKET OBSERVATION
            |
            v
    PUBLIC TEST REPORT
            |
            v
    SHA-256 ARTIFACT HASH
            |
            v
    GIT TREE
            |
            v
    GIT COMMIT
            |
            v
    PUBLIC REPOSITORY

This does not make the experiment mathematically infallible.

It makes the published artifact identifiable, versioned, and harder to
silently rewrite after publication.

---

# 18. Result

Final public result for this experiment:

    LIVE_WIFI_FAILURE=OBSERVED
    TRANSPORT_REPLACEMENT=OBSERVED
    WIFI_TO_MOBILE=OBSERVED
    LOGICAL_SESSION_IDENTIFIER=UNCHANGED
    TRANSPORT_GENERATION=1_TO_2
    SEQUENCE_PROGRESSION=CONTINUED
    MOBILE_PACKETS_SERVER_SIDE=OBSERVED
    SERVER_ACKS=OBSERVED
    TCPDUMP_CORRELATION=OBSERVED

Final verdict:

    PASS — LIVE TRANSPORT CONTINUITY DEMONSTRATED

Scope:

    VRP LIVE CONTINUITY HARNESS
    REAL NETWORK
    WIFI -> MOBILE / 5G

This verdict does not claim verification of the complete protected VRP
Core.

---

# 19. Engineering Statement

The experiment demonstrates the architectural distinction VRP is built
around:

    SESSION ≠ TRANSPORT

A transport can fail.

A replacement transport can be created.

The logical session does not have to be defined by the lifetime of one
network path.

That proposition is now represented not only by architecture
documentation, but by a publicly recorded live network experiment.

No need to believe the statement.

Inspect the evidence.

Reproduce the experiment.

Challenge the boundary.

SESSION ≠ TRANSPORT.

CONTINUITY FIRST.

---

Veil Routing Protocol (VRP)

Public architecture and authorship record:

https://github.com/Endless33/Veil-Routing-Protocol

Evidence date:

2026-10-04
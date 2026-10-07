# Veil Routing Protocol — Failure Before and After VRP

## The Network Still Fails. The Architecture Does Not Have to Fail the Same Way.

Veil Routing Protocol (VRP) is built around one architectural separation:

# Session != Transport

This document shows what that separation means during network failure.

It does not claim that VRP prevents:

- Wi-Fi loss;
- mobile-network loss;
- route failure;
- physical outages;
- packet loss;
- latency;
- jitter;
- NAT changes;
- transport collapse.

Those failures remain real.

The difference is what the architecture allows those failures to destroy.

This document describes only publicly observable architectural behavior.

It does not disclose protected runtime algorithms, internal authority logic, recovery decision mechanisms, cryptographic internals, private state machines, security-sensitive thresholds, or proprietary defense mechanisms.

---

# 1. Start With Reality

Networks fail.

A device may begin here:

```text
APPLICATION
     |
   SESSION
     |
 TRANSPORT
     |
   WI-FI
     |
 INTERNET
```

Then this happens:

```text
WI-FI
  |
  X
```

Nothing about VRP changes that physical fact.

The radio can disappear.

The interface can disappear.

The route can disappear.

The upstream network can disappear.

The question begins after that.

---

# 2. The Common Coupling

In many systems, a logical session is strongly associated with the lifetime of a particular connection or transport.

A simplified failure chain may look like:

```text
NETWORK PATH LOST
        |
        v
TRANSPORT LOST
        |
        v
CONNECTION LOST
        |
        v
SESSION LOST
        |
        v
APPLICATION MUST RECOVER
```

This model is not inherently wrong.

For many applications, it is completely sufficient.

But it creates a strong coupling:

```text
TRANSPORT LIFETIME
        ≈
SESSION LIFETIME
```

VRP questions whether that coupling is always necessary.

---

# 3. The VRP Model

VRP introduces a different architectural relationship.

```text
SESSION
   |
   +-------------------+
   |                   |
   v                   v
IDENTITY            TRANSPORT
                       |
                       v
                     PATH
```

Transport carries the session.

Transport does not automatically define the session.

Therefore:

```text
TRANSPORT LOST
       !=
SESSION IDENTITY
AUTOMATICALLY LOST
```

---

# 4. Before

Consider a transport-bound model.

```text
T0

APPLICATION
     |
SESSION
     |
TRANSPORT A
     |
NETWORK A
```

Then:

```text
T1

NETWORK A
    |
    X
```

The failure propagates upward:

```text
NETWORK A LOST
      |
      v
TRANSPORT A LOST
      |
      v
CONNECTION LOST
      |
      v
SESSION LOST
      |
      v
APPLICATION RECOVERY
```

The application may then need to:

```text
RECONNECT

REAUTHENTICATE

RECREATE SESSION

RECONSTRUCT STATE

RESUME WORK
```

Again, this can be a valid architecture.

But transport failure has become session failure.

---

# 5. After the Separation

Now consider the VRP architectural model.

```text
T0

LOGICAL SESSION
      |
      v
TRANSPORT A
      |
      v
NETWORK A
```

Then:

```text
T1

NETWORK A
    |
    X
```

VRP treats the transport failure as a transport event.

Conceptually:

```text
NETWORK A LOST
      |
      v
TRANSPORT A LOST
      |
      v
TRANSPORT FAILURE OBSERVED
      |
      v
SESSION IDENTITY REMAINS
A SEPARATE CONCERN
```

From there, recovery can be evaluated.

The protected logic deciding how this occurs is intentionally not described here.

---

# 6. Side by Side

```text
TRANSPORT-BOUND MODEL              VRP MODEL

Network fails                      Network fails
      |                                  |
      v                                  v
Transport fails                    Transport fails
      |                                  |
      v                                  v
Connection fails                   Failure observed
      |                                  |
      v                                  v
Session often fails                Session identity remains
      |                            a separate concern
      v                                  |
Application recovery                    v
                                   Recovery evaluated
                                         |
                                  +------+------+
                                  |             |
                                  v             v
                               CONTINUE      CONTAIN
                               SAFELY        / FAIL
```

The physical network failed in both cases.

The architectural consequence is different.

---

# 7. VRP Does Not Mean "Always Continue"

This distinction is critical.

VRP does not say:

```text
TRANSPORT FAILED
      |
      v
ALWAYS CONTINUE
```

That would be unsafe.

The model is closer to:

```text
TRANSPORT FAILED
      |
      v
EVALUATE CONTINUITY
      |
   +--+----------------+
   |                   |
   v                   v
CONTINUITY          CONTINUITY
CAN REMAIN          CANNOT BE
VALID               ESTABLISHED
   |                   |
   v                   v
CONTINUE            CONTAIN
                    / FAIL
```

Continuity is not valuable if it requires accepting invalid state.

---

# 8. Before: Reconnect Means Success

A simple recovery model may consider this sufficient:

```text
DISCONNECTED
     |
     v
RECONNECT
     |
     v
CONNECTED
     |
     v
SUCCESS
```

That answers an important question:

> Can communication resume?

But it does not necessarily answer:

```text
IS THIS THE SAME LOGICAL SESSION?

IS THIS THE CURRENT STATE?

IS THIS THE CURRENT AUTHORITY?

DID OLD STATE RETURN?

DID REPLAY OCCUR?

DID DUPLICATE EXECUTION OCCUR?

DID HISTORY CHANGE?
```

VRP is concerned with those additional questions.

---

# 9. After: Connectivity Is Only One Signal

In the VRP model:

```text
CONNECTED AGAIN
```

does not automatically mean:

```text
CONTINUITY CORRECT
```

Therefore:

# Availability != Correctness

A network can recover while logical recovery remains invalid.

---

# 10. Example: Wi-Fi Loss

Before failure:

```text
SESSION S
    |
 WI-FI
```

Then:

```text
SESSION S
    |
    X
 WI-FI LOST
```

The physical observation is:

```text
WI-FI IS GONE.
```

That does not logically prove:

```text
SESSION S MUST
BECOME SESSION S2.
```

This distinction is the beginning of the VRP model.

---

# 11. Example: Wi-Fi to Mobile

Consider:

```text
T0

SESSION S
    |
 WI-FI


T1

SESSION S
    |
    X
 WI-FI LOST


T2

MOBILE NETWORK
BECOMES AVAILABLE
```

A transport-bound interpretation may require a new connection and application-level session recovery.

VRP asks another question:

> Can Session S remain the authoritative logical session while the transport underneath it changes?

That question is testable.

---

# 12. Example: Mobile to Wi-Fi

The direction does not matter.

```text
MOBILE
   |
   X
   |
 WI-FI
```

The relevant separation remains:

```text
PATH CHANGE
    !=
SESSION IDENTITY CHANGE
```

---

# 13. Example: Path Changes Repeatedly

Real mobility may look like:

```text
WI-FI

  ↓

MOBILE

  ↓

WI-FI

  ↓

MOBILE

  ↓

OUTAGE

  ↓

WI-FI
```

If logical identity is directly coupled to every transport transition, the application may repeatedly inherit transport instability.

VRP attempts to separate those lifetimes.

---

# 14. Before: Old Path Returns

Consider:

```text
PATH A
   |
   X
PATH A LOST
   |
PATH B
   |
PATH A RETURNS
```

A dangerous recovery assumption would be:

```text
PATH A IS BACK

THEREFORE EVERYTHING
FROM PATH A IS CURRENT
```

That is not a safe continuity rule.

---

# 15. After: Reachability Is Not Authority

VRP explicitly separates these concepts:

# Reachability != Authority

A path becoming reachable says something about connectivity.

It does not, by itself, establish which state is current.

This matters when an old transport returns after newer continuity state already exists.

---

# 16. Before: Historical State Returns

Suppose:

```text
STATE A
   |
STATE B
   |
STATE C
```

Current state:

```text
STATE C
```

After network disruption:

```text
STATE A RETURNS
```

If availability alone determines authority, historical state can become dangerous.

---

# 17. After: Historical Validity Is Not Current Authority

VRP's public model requires the distinction:

```text
VALID ONCE
    !=
AUTHORITATIVE NOW
```

Therefore:

# Historical Validity != Current Authority

The internal mechanism used to preserve this property remains protected.

---

# 18. Before: Duplicate Delivery

Network instability may produce:

```text
EVENT X

EVENT X
```

A naive execution model may accidentally interpret both observations as independent progress.

---

# 19. After: Duplicate Observation Is Not Duplicate Authority

VRP requires:

```text
DUPLICATE DELIVERY
        !=
DUPLICATE CANONICAL EXECUTION
```

Observing something twice does not automatically mean it happened twice at the logical authority layer.

---

# 20. Before: Replay Looks Valid

Historical information may still be structurally well-formed.

For example:

```text
EVENT X
  |
ACCEPTED

later:

EVENT X
  |
RETURNS
```

The information may look familiar because it was once legitimate.

That is exactly why replay matters.

---

# 21. After: Replay Is Not Progress

The public invariant is:

# Replay != Progress

Previously accepted information must not become new canonical progress merely because it appears again.

---

# 22. Before: Recovery Can Rewrite Reality

Suppose accepted history is:

```text
A -> B -> C
```

After a failure, a bad recovery could produce:

```text
A -> X -> Y
```

while still restoring network connectivity.

The system may appear operational.

But continuity has failed.

---

# 23. After: Recovery Does Not Grant Rewrite Authority

The VRP public invariant is:

```text
RECOVERY
   !=
PERMISSION TO
REWRITE ACCEPTED HISTORY
```

Restoring communication and preserving canonical history are different requirements.

---

# 24. Before: Process Survival Looks Healthy

A runtime may remain alive:

```text
PROCESS = RUNNING
```

while logical state is wrong.

For example:

```text
STALE STATE ACCEPTED

REPLAY ACCEPTED

DUPLICATE EXECUTION

HISTORY DIVERGED
```

Therefore process survival is weak continuity evidence.

---

# 25. After: Invariants Matter More Than Process Survival

VRP testing asks:

```text
DID SESSION IDENTITY SURVIVE?

DID AUTHORITY REMAIN VALID?

DID STALE STATE REMAIN STALE?

DID REPLAY REMAIN REPLAY?

DID HISTORY REMAIN CANONICAL?

DID THE VERDICT REMAIN REPRODUCIBLE?
```

That is a stronger standard than:

```text
THE PROCESS DID NOT CRASH.
```

---

# 26. Before: Failure Ends the Story

A simplistic model is:

```text
FAILURE
   |
   v
SESSION ENDS
```

This avoids many recovery questions by terminating continuity.

Sometimes that is the correct behavior.

But not always.

---

# 27. After: Failure Starts a Decision

VRP treats failure as an input into continuity behavior.

Conceptually:

```text
FAILURE
   |
   v
OBSERVE
   |
   v
EVALUATE
   |
   +----------+----------+
   |          |          |
   v          v          v
CONTINUE    WAIT       REJECT
   |                     |
   |                     v
   |                  CONTAIN
   |
   v
RECOVER
```

The exact decision process is protected.

The externally observable behavior is testable.

---

# 28. Before: One Failure

Many demonstrations stop here:

```text
NETWORK LOST

NETWORK RETURNED

PASS
```

That is useful connectivity evidence.

But real environments are more complicated.

---

# 29. After: Failure During Failure

VRP validation also cares about sequences like:

```text
TRANSPORT A LOST
      |
RECOVERY STARTS
      |
TRANSPORT B APPEARS
      |
      X
TRANSPORT B LOST
      |
OLD STATE RETURNS
      |
DUPLICATE ARRIVES
      |
TRANSPORT C APPEARS
```

The question is whether continuity invariants remain coherent through the sequence.

---

# 30. Before: Stable Timing Assumptions

A clean laboratory environment might produce:

```text
A

10 ms

B

10 ms

C

10 ms

D
```

Real networks may look more like:

```text
A

120 ms

C

25 ms

B

400 ms

D
```

Timing and ordering can become part of the failure surface.

---

# 31. After: Disorder Must Not Automatically Become Authority Disorder

VRP testing includes conditions involving:

```text
JITTER

LATENCY

REORDERING

CONGESTION
```

The requirement is not perfect timing.

The requirement is that timing disorder must not silently create invalid canonical progress under the defined test conditions.

---

# 32. Before: Restart Means Rebuild

A restart may encourage a simplistic assumption:

```text
PROCESS RESTARTED
      |
      v
ACCEPT AVAILABLE STATE
```

That becomes dangerous if the available state is historical.

---

# 33. After: Restart Does Not Make Old State Current

The public requirement remains:

```text
RESTART
   !=
AUTHORITY RESET
```

Historical state must not become current merely because a runtime restarted.

---

# 34. The Difference During Complete Outage

Suppose every path disappears.

```text
WI-FI = DOWN

MOBILE = DOWN

OTHER PATH = DOWN
```

Both architectures face the same physical fact:

# No Transport Exists

VRP cannot send packets through nothing.

The difference is the logical question preserved during the outage:

```text
WHAT STATE REMAINS VALID?

WHAT MUST REMAIN REJECTED?

WHAT MAY SAFELY CONTINUE
WHEN CONNECTIVITY RETURNS?
```

---

# 35. VRP Does Not Create Connectivity

This deserves explicit wording.

VRP does not:

```text
CREATE RADIO COVERAGE

CREATE AN INTERNET ROUTE

CREATE BANDWIDTH

REMOVE PHYSICAL OUTAGES

MAKE A DEAD INTERFACE ALIVE
```

VRP operates on continuity semantics around transport behavior.

That is a very different claim.

---

# 36. What VRP Attempts to Preserve

Depending on the defined scenario, public VRP invariants include:

```text
SESSION IDENTITY

AUTHORITY MONOTONICITY

REPLAY REJECTION

DUPLICATE CONTAINMENT

CAUSAL INTEGRITY

CANONICAL HISTORY

RECOVERY CONSISTENCY

DETERMINISTIC VERDICT
```

Not every scenario exercises every invariant.

---

# 37. What VRP Is Willing to Reject

Continuity-first does not mean acceptance-first.

A safe runtime may need to reject:

```text
STALE INPUT

REPLAYED INPUT

DUPLICATE PROGRESS

CONFLICTING STATE

INVALID RECOVERY

HISTORICAL ROLLBACK
```

Therefore:

```text
REJECTION
```

can be the correct continuity result.

---

# 38. Continuity vs Availability

These concepts should remain separate:

```text
AVAILABILITY:

Can communication occur?


CONTINUITY:

Can communication proceed
without violating the logical
history and authority model?
```

A system may have:

```text
AVAILABILITY = YES

CONTINUITY = NO
```

In that situation, continuing blindly may be worse than containing the transition.

---

# 39. The Stronger Failure Model

The architecture can therefore be summarized as:

```text
OLD MODEL

TRANSPORT FAILURE
      |
      v
SESSION FAILURE


VRP MODEL

TRANSPORT FAILURE
      |
      v
CONTINUITY QUESTION
      |
      +----------------+
      |                |
      v                v
VALID               INVALID
      |                |
      v                v
CONTINUE            CONTAIN
```

Again:

The diagram describes the public behavior model.

It does not disclose the protected decision mechanism.

---

# 40. What Changes for the Application?

The long-term architectural objective is to reduce unnecessary application coupling to transport churn.

Instead of forcing every application to reason independently about:

```text
PATH CHANGE

NETWORK REBINDING

TRANSPORT LOSS

RECOVERY

STALE RETURN

DUPLICATION
```

VRP investigates whether continuity can become an explicit runtime property.

This does not eliminate application responsibility.

It changes where certain continuity responsibilities can be represented.

---

# 41. What Changes for Infrastructure?

Traditional infrastructure monitoring may ask:

```text
IS THE INTERFACE UP?

IS THE HOST REACHABLE?

IS THE ROUTE AVAILABLE?
```

VRP adds another category of questions:

```text
IS THE SESSION CONTINUOUS?

IS THE STATE CURRENT?

IS THE AUTHORITY CURRENT?

DID RECOVERY PRESERVE HISTORY?

WAS INVALID INPUT REJECTED?
```

This is a different observation layer.

---

# 42. What Changes for Validation?

A simple network test might be:

```text
DISCONNECT

RECONNECT

PING

PASS
```

A VRP continuity test is closer to:

```text
ESTABLISH SESSION

DISCONNECT TRANSPORT

CHANGE PATH

INTRODUCE FAILURE CONDITION

RECOVER

CHECK IDENTITY

CHECK AUTHORITY

CHECK HISTORY

CHECK REPLAY / DUPLICATION

VERIFY EVIDENCE

PASS OR FAIL
```

The second test asks a much harder question.

---

# 43. What Changes for Security?

Transport instability can become a security boundary.

During recovery, the runtime may encounter information that is:

```text
REACHABLE

WELL-FORMED

PREVIOUSLY VALID
```

but still:

```text
NOT CURRENT

NOT AUTHORITATIVE

NOT PERMITTED TO ADVANCE STATE
```

Therefore:

# Reachability != Authority

is both a continuity and security statement.

---

# 44. What Changes for Recovery?

Recovery is no longer defined only as:

```text
RESTORE CONNECTIVITY
```

It becomes:

```text
RESTORE CONNECTIVITY
        +
PRESERVE VALID IDENTITY
        +
PRESERVE AUTHORITY
        +
PRESERVE HISTORY
        +
REJECT INVALID PROGRESS
```

That is a significantly stronger recovery requirement.

---

# 45. The Architecture in One Comparison

```text
BEFORE

Transport defines connection.
Connection strongly defines session.
Transport disappears.
Session disappears.
Application rebuilds.


AFTER — VRP MODEL

Session and transport are distinct.
Transport carries the session.
Transport may disappear.
Session continuity is evaluated independently.
A replacement path may be considered.
Invalid historical progress remains invalid.
Continuity either proceeds safely or is contained.
```

---

# 46. What Has Actually Been Tested?

Publicly documented VRP engineering work includes classes of validation involving:

```text
REAL TRANSPORT INTERRUPTION

WI-FI / ALTERNATE PATH TRANSITION

TEMPORARY OUTAGE

REPEATED TRANSPORT MIGRATION

REPLAY

REPLAY FLOOD

DUPLICATE DELIVERY

STALE STATE RETURN

AUTHORITY ROLLBACK

REORDERING

RECOVERY RACES

RUNTIME PRESSURE

CANONICAL HISTORY REWRITE

CONCURRENCY

DETERMINISTIC REPETITION

EVIDENCE TAMPERING

INDEPENDENT VERIFICATION
```

Each result applies to its documented test conditions.

This list is evidence of validation breadth, not a claim of universal correctness.

---

# 47. What Has Not Been Claimed?

VRP does not claim:

```text
THE INTERNET CANNOT FAIL

ZERO PACKET LOSS

ZERO DOWNTIME

PERFECT SECURITY

UNLIMITED SCALABILITY

ALL ATTACKS ARE SOLVED

ALL NETWORKS ARE SUPPORTED

ALL APPLICATIONS REQUIRE VRP

PRODUCTION READINESS EVERYWHERE
```

Those claims would exceed the evidence.

---

# 48. The Important Difference

This is not:

```text
YOUR INTERNET BREAKS.

OURS DOES NOT.
```

That statement would be technically meaningless.

The actual distinction is:

```text
YOUR TRANSPORT CAN BREAK.

OUR TRANSPORT CAN BREAK TOO.

THE DIFFERENCE IS WHETHER
TRANSPORT FAILURE MUST
AUTOMATICALLY DESTROY
THE LOGICAL SESSION.
```

That is the architectural question.

---

# 49. The Challenge

Do not evaluate VRP by reading this document.

Break the transport.

Change the path.

Return the old path.

Replay historical input.

Duplicate delivery.

Reorder events.

Interrupt recovery.

Repeat the migration.

Restart the runtime.

Then ask:

```text
DID SESSION IDENTITY SURVIVE?

DID OLD STATE REMAIN OLD?

DID REPLAY REMAIN REPLAY?

DID AUTHORITY REMAIN MONOTONIC?

DID HISTORY REMAIN CANONICAL?

DID THE RESULT REMAIN
REPRODUCIBLE?
```

That is a meaningful evaluation.

---

# 50. One Screen

```text
              THE NETWORK FAILS
                     |
                     X
                     |
              TRANSPORT LOST
                     |
          +----------+----------+
          |                     |
          |                     |
 TRANSPORT-BOUND MODEL       VRP MODEL
          |                     |
          v                     v
   SESSION FAILURE        SESSION REMAINS
                          A SEPARATE CONCERN
          |                     |
          v                     v
 APPLICATION REBUILD      RECOVERY EVALUATED
                                |
                         +------+------+
                         |             |
                         v             v
                      CONTINUE      CONTAIN
                      SAFELY        / FAIL
```

The failure happened in both models.

The difference is what the failure was allowed to destroy.

---

# 51. Final Position

VRP does not promise a network without failure.

It proposes an architecture in which transport failure does not automatically define the lifetime of logical continuity.

That leads to a different set of questions:

```text
WHAT FAILED?

WHAT SURVIVED?

WHAT REMAINS CURRENT?

WHAT REMAINS AUTHORITATIVE?

WHAT MUST BE REJECTED?

WHAT HISTORY REMAINS CANONICAL?

CAN THE RESULT BE VERIFIED?
```

Those are the questions VRP is being built to answer.

The mechanisms remain protected.

The behavior remains testable.

---

# Session != Transport

# Reachability != Authority

# Availability != Correctness

# Replay != Progress

# Failure Is the Test

# Continuity First

---

## Veil Routing Protocol

Public architectural comparison document.

VRP does not prevent physical network failure.

It changes the architectural relationship between transport failure and logical continuity.

Protected runtime implementation remains private.
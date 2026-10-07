# Veil Routing Protocol — Network Failure Reality

## The Network Will Fail

Veil Routing Protocol (VRP) starts from an intentionally uncomfortable assumption:

**The network will fail.**

Wi-Fi disappears.

Mobile connectivity changes.

Routes change.

NAT mappings change.

Interfaces disappear.

Packets arrive late.

Packets arrive twice.

Old state returns.

Connectivity may vanish completely and later return through a different path.

VRP does not attempt to deny this reality.

It is designed around it.

The central architectural question is:

> When the transport fails, what else must be allowed to fail with it?

VRP's answer begins with:

# Session != Transport

This document describes that distinction at the public architectural level.

It does not disclose protected recovery algorithms, authority mechanisms, internal state machines, cryptographic internals, thresholds, or proprietary runtime logic.

---

# 1. VRP Does Not Prevent Network Failure

This distinction matters.

VRP does **not** claim:

```text
THE INTERNET NEVER DISCONNECTS

WI-FI NEVER FAILS

MOBILE NETWORKS NEVER DROP

PACKETS NEVER DISAPPEAR

ROUTES NEVER CHANGE

OUTAGES NO LONGER EXIST
```

Those claims would be unrealistic.

A physical or logical network failure is still a network failure.

If Wi-Fi disappears, VRP cannot make the radio link physically remain available.

If an upstream network becomes unreachable, VRP cannot pretend that packets are still crossing it.

If every usable transport disappears, connectivity is unavailable.

The architecture addresses a different problem.

---

# 2. The Important Question

Consider:

```text
NETWORK PATH
     |
     X
PATH LOST
```

That event is real.

But several different things may be coupled to that event:

```text
NETWORK PATH

TRANSPORT

CONNECTION

SESSION IDENTITY

APPLICATION STATE

AUTHORITY

CANONICAL HISTORY
```

The key question is:

> Must all of these have the same lifetime?

VRP says:

**No. They should not be assumed to have the same lifetime.**

---

# 3. The Conventional Failure Chain

A transport-bound architecture can effectively behave like:

```text
NETWORK FAILURE
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
APPLICATION RECOVERY
```

For many applications, this is perfectly acceptable.

Reconnect.

Authenticate again.

Reconstruct state.

Continue.

There is nothing inherently wrong with that model.

But it becomes problematic when the logical session carries state that should survive the transport carrying it.

---

# 4. The VRP Separation

VRP explores another architecture:

```text
NETWORK FAILURE
      |
      v
TRANSPORT LOST
      |
      v
TRANSPORT FAILURE OBSERVED
      |
      v
LOGICAL SESSION REMAINS
A SEPARATE CONCERN
      |
      v
RECOVERY IS EVALUATED
      |
      +----------------------+
      |                      |
      v                      v
SAFE CONTINUITY         CONTAIN / FAIL
MAY PROCEED             IF REQUIRED
```

The important difference is not that the network somehow stopped failing.

It did fail.

The difference is that:

```text
TRANSPORT FAILURE
       !=
AUTOMATIC DESTRUCTION
OF EVERY HIGHER-LEVEL
CONTINUITY PROPERTY
```

---

# 5. The Shortest Explanation

The simplest public explanation of VRP is:

```text
THE NETWORK CAN DISAPPEAR.

THE TRANSPORT CAN DISAPPEAR.

THE PATH CAN DISAPPEAR.

THE QUESTION IS:

MUST THE LOGICAL SESSION
DISAPPEAR WITH THEM?
```

VRP investigates the answer:

**Not necessarily.**

---

# 6. What Actually Breaks?

Suppose a device is communicating over Wi-Fi.

Then Wi-Fi disappears.

What definitely happened?

```text
THE WI-FI PATH FAILED.
```

What did **not** automatically become logically true?

```text
THE USER BECAME A DIFFERENT USER.

THE APPLICATION BECAME A DIFFERENT APPLICATION.

THE LOGICAL SESSION MUST HAVE A NEW IDENTITY.

OLD STATE BECAME CURRENT AGAIN.

PREVIOUS EVENTS BECAME NEW EVENTS.

ACCEPTED HISTORY MAY BE REWRITTEN.
```

Transport loss and logical identity loss are different statements.

VRP is built around preserving that distinction.

---

# 7. Example: Wi-Fi to Another Transport

Consider a simplified sequence:

```text
T0

SESSION ACTIVE
      |
      v
WI-FI ACTIVE


T1

SESSION ACTIVE
      |
      X
WI-FI LOST


T2

ANOTHER TRANSPORT
BECOMES AVAILABLE


T3

RECOVERY CONDITIONS
ARE EVALUATED


T4

CONTINUITY MAY PROCEED
IF REQUIRED INVARIANTS HOLD
```

The public architectural point is not how T3 is implemented.

That mechanism remains protected.

The public point is:

```text
T1 DOES NOT AUTOMATICALLY
REDEFINE THE SESSION.
```

---

# 8. Connectivity and Continuity Are Different

These two statements are not equivalent:

```text
CONNECTIVITY EXISTS
```

and:

```text
CONTINUITY IS CORRECT
```

Likewise:

```text
CONNECTIVITY RETURNED
```

does not automatically prove:

```text
THE CORRECT SESSION RETURNED

THE CORRECT STATE RETURNED

THE CURRENT AUTHORITY RETURNED

NO REPLAY OCCURRED

NO DUPLICATE EXECUTION OCCURRED

HISTORY REMAINED CANONICAL
```

This distinction is central to VRP.

---

# 9. Reconnecting Is Not the Entire Problem

A system may successfully reconnect after an outage.

That is useful.

But reconnecting answers primarily:

> Can communication happen again?

A continuity architecture must also answer:

```text
WHAT SESSION IS THIS?

WHAT STATE IS CURRENT?

WHAT STATE IS HISTORICAL?

WHAT STATE IS STALE?

WHAT MAY BECOME AUTHORITATIVE?

WHAT MUST BE REJECTED?

WHAT HISTORY REMAINS CANONICAL?
```

These are different questions.

---

# 10. A Successful Reconnect Can Still Be Wrong

Consider:

```text
TRANSPORT A
     |
     X
FAILURE
     |
TRANSPORT B
     |
CONNECTED
```

At first glance:

```text
SUCCESS
```

But suppose historical state also returned and incorrectly replaced newer state.

Then the system may be:

```text
CONNECTED
```

while simultaneously being:

```text
LOGICALLY WRONG
```

Therefore:

# Availability != Correctness

---

# 11. A Process Staying Alive Is Not Continuity

Another misleading observation is:

```text
THE PROCESS DID NOT CRASH.
```

That is useful.

But it does not prove continuity.

A process can remain alive while:

```text
SESSION IDENTITY CHANGES

STALE STATE IS ACCEPTED

REPLAY BECOMES PROGRESS

DUPLICATE EXECUTION OCCURS

HISTORY DIVERGES
```

VRP validation therefore focuses on invariants rather than process survival alone.

---

# 12. Transport Recovery Is Not Authority Recovery

Suppose an old path returns.

```text
PATH A ACTIVE
     |
     X
PATH A LOST
     |
PATH B ACTIVE
     |
PATH A RETURNS
```

A dangerous assumption would be:

```text
PATH A RETURNED
      =
EVERYTHING ASSOCIATED
WITH PATH A IS CURRENT AGAIN
```

VRP does not make that assumption.

The public architectural rule is:

# Reachability != Authority

---

# 13. Old Does Not Mean Current

Network instability can allow old information to appear after newer information has already been accepted.

Example:

```text
STATE A
   |
STATE B
   |
STATE C

CURRENT = C

NETWORK FAILURE

STATE A RETURNS
```

The fact that State A was once legitimate does not mean:

```text
STATE A IS CURRENT
```

Therefore:

# Historical Validity != Current Authority

---

# 14. Replay Is a Network-Recovery Problem Too

Transport disruption can create conditions where previously observed information appears again.

Conceptually:

```text
EVENT X
  |
ACCEPTED

NETWORK DISRUPTION

EVENT X
  |
OBSERVED AGAIN
```

A continuity architecture must distinguish:

```text
NEW PROGRESS
```

from:

```text
OLD INFORMATION
```

Therefore:

# Replay != Progress

---

# 15. Duplicate Delivery Is Not Duplicate Reality

Networks and distributed systems can duplicate delivery.

```text
EVENT X

EVENT X
```

The physical observation happened twice.

That does not necessarily mean the logical event happened twice.

Therefore:

```text
DUPLICATE DELIVERY
        !=
DUPLICATE CANONICAL EXECUTION
```

This distinction becomes especially important during unstable connectivity and recovery.

---

# 16. Failure Can Happen During Recovery

Real networks do not politely wait for recovery to finish.

A more realistic sequence may be:

```text
TRANSPORT A LOST
      |
RECOVERY STARTS
      |
TRANSPORT B APPEARS
      |
      X
TRANSPORT B FAILS
      |
TRANSPORT C APPEARS
```

Or:

```text
RECOVERY STARTS
      |
OLD STATE RETURNS
      |
DUPLICATE ARRIVES
      |
PATH CHANGES AGAIN
```

A continuity architecture must expect recovery itself to occur under unstable conditions.

---

# 17. Mobility Makes This More Visible

Mobile environments make transport lifetime particularly obvious.

A device may move through:

```text
HOME WI-FI

      |

MOBILE NETWORK

      |

PUBLIC WI-FI

      |

MOBILE NETWORK

      |

TEMPORARY OUTAGE

      |

ANOTHER NETWORK
```

The physical transport environment may change repeatedly.

The architectural question remains:

> Which higher-level properties actually need to change with it?

VRP attempts to reduce unnecessary coupling between transport lifetime and logical continuity lifetime.

---

# 18. NAT and Network Identity Are Not Session Identity

Network-visible identity can change.

For example:

```text
ADDRESS A
   |
   v
ADDRESS B
```

or:

```text
NAT MAPPING A
      |
      v
NAT MAPPING B
```

Those changes matter to networking.

But they do not automatically prove that the logical session itself became a different session.

This is another consequence of:

# Session != Transport

---

# 19. Complete Outage Still Means Complete Outage

VRP does not claim to transmit data through a network that does not exist.

If every usable path disappears:

```text
PATH A = DOWN

PATH B = DOWN

PATH C = DOWN
```

then live network communication is unavailable.

There is no magic transport.

The continuity question becomes what state remains valid while communication is unavailable and what may safely happen when connectivity returns.

This distinction matters.

VRP is not attempting to violate physics.

It is attempting to avoid unnecessary logical destruction caused by transport instability.

---

# 20. Fail Closed Is Sometimes the Correct Result

Continuity does not mean:

```text
ALWAYS CONTINUE
```

Sometimes the correct outcome is:

```text
DO NOT CONTINUE
```

if the required correctness properties cannot be established.

Therefore the VRP philosophy is not:

```text
CONTINUITY AT ANY COST
```

It is closer to:

```text
CONTINUITY
WHEN IT CAN REMAIN VALID

CONTAINMENT
WHEN IT CANNOT
```

The protected runtime determines how these decisions are implemented.

The public contract describes the properties expected from the result.

---

# 21. The Real Comparison

The useful comparison is not:

```text
NORMAL INTERNET:

FAILS


VRP:

NEVER FAILS
```

That would be false.

The stronger comparison is:

```text
TRANSPORT-BOUND MODEL

transport lost
      |
      v
logical session often lost
      |
      v
application reconstructs continuity
```

versus:

```text
VRP MODEL

transport lost
      |
      v
transport failure recognized
      |
      v
logical session remains
a separate architectural object
      |
      v
recovery is evaluated
      |
      v
safe continuity
or explicit containment
```

That is the architectural difference.

---

# 22. What VRP Changes

VRP does not change the fact that:

```text
NETWORKS FAIL.
```

It changes the question asked after failure.

Instead of immediately assuming:

```text
THE TRANSPORT DIED,
THEREFORE THE SESSION DIED.
```

VRP asks:

```text
THE TRANSPORT DIED.

WHAT CONTINUITY STATE
IS STILL VALID?

WHAT MAY RECOVER?

WHAT MUST NOT RECOVER?

WHAT REMAINS AUTHORITATIVE?

WHAT MUST BE REJECTED?
```

---

# 23. Failure Becomes an Input

In a continuity-first architecture:

```text
FAILURE
```

is not merely:

```text
END OF SESSION
```

It becomes an input into runtime behavior.

Conceptually:

```text
FAILURE
   |
   v
OBSERVATION
   |
   v
CONTINUITY DECISION
   |
   +-------> CONTINUE
   |
   +-------> RECOVER
   |
   +-------> WAIT
   |
   +-------> REJECT
   |
   +-------> CONTAIN
   |
   +-------> FAIL
```

The exact decision mechanisms are protected.

The externally observable outcome can be tested.

---

# 24. Why This Matters to Applications

Applications frequently care about logical continuity more than they care about a specific network path.

Examples may include:

```text
LONG-LIVED STATEFUL SESSIONS

MOBILE APPLICATIONS

EDGE SYSTEMS

DISTRIBUTED RUNTIMES

ROAMING DEVICES

RECOVERY-SENSITIVE SERVICES

INTERMITTENTLY CONNECTED SYSTEMS
```

In these environments, rebuilding application state after every transport event may be unnecessary or expensive.

VRP investigates whether part of that continuity responsibility can be represented explicitly below or alongside the application boundary.

---

# 25. Why This Matters to Infrastructure Teams

Infrastructure teams already know that:

```text
PING WORKS
```

does not mean:

```text
APPLICATION STATE IS CORRECT
```

They also know that:

```text
ROUTE RESTORED
```

does not necessarily mean:

```text
RECOVERY COMPLETED CORRECTLY
```

VRP operates in this gap.

It treats network recovery and continuity recovery as related but distinct concerns.

---

# 26. What VRP Tests

A continuity architecture should be tested where it is weakest:

during failure.

Publicly discussable validation classes include:

```text
TRANSPORT INTERRUPTION

PHYSICAL NETWORK LOSS

PATH MIGRATION

REPEATED MIGRATION

TEMPORARY OUTAGE

REPLAY

DUPLICATE DELIVERY

STALE STATE RETURN

REORDERED DELIVERY

AUTHORITY ROLLBACK

RECOVERY RACES

RECOVERY INTERRUPTION

RUNTIME PRESSURE

HISTORY REWRITE ATTEMPTS
```

These scenarios challenge the consequences of:

**Session != Transport**

without requiring disclosure of protected implementation logic.

---

# 27. The Important Evidence

The interesting evidence is not simply:

```text
NETWORK CAME BACK.
```

The stronger evidence asks:

```text
DID SESSION IDENTITY REMAIN CONSISTENT?

DID STALE STATE REMAIN STALE?

DID REPLAY REMAIN REPLAY?

DID DUPLICATION REMAIN CONTAINED?

DID HISTORY REMAIN CANONICAL?

DID RECOVERY PRODUCE A
REPRODUCIBLE VERDICT?
```

That is the difference between connectivity testing and continuity testing.

---

# 28. The Public Claim

The public claim should remain narrow and falsifiable.

VRP does not claim:

> Network failure disappears.

VRP claims that transport failure and logical continuity failure do not have to be treated as the same event.

That claim can be challenged.

Kill the transport.

Change the path.

Return stale information.

Replay previous input.

Duplicate delivery.

Interrupt recovery.

Then inspect what remained valid.

---

# 29. What Would Prove VRP Wrong?

A serious architecture must define failure conditions.

Examples include:

```text
TRANSPORT CHANGE
UNEXPECTEDLY CREATES
A NEW LOGICAL IDENTITY

STALE STATE REGAINS
AUTHORITY

REPLAY BECOMES
NEW PROGRESS

DUPLICATE DELIVERY
BECOMES DUPLICATE
CANONICAL EXECUTION

RECOVERY REWRITES
ACCEPTED HISTORY

EQUIVALENT TESTS
PRODUCE UNEXPLAINED
DIVERGENCE
```

If those conditions occur where the corresponding invariant was expected to hold, the validation should fail.

That makes the architectural claim falsifiable.

---

# 30. The Difference in One Screen

```text
WITHOUT CONTINUITY SEPARATION

NETWORK PATH
     |
     X
     |
TRANSPORT LOST
     |
     v
SESSION LOST
     |
     v
APPLICATION REBUILDS


VRP ARCHITECTURAL MODEL

NETWORK PATH
     |
     X
     |
TRANSPORT LOST
     |
     v
SESSION REMAINS A
SEPARATE CONCERN
     |
     v
RECOVERY EVALUATED
     |
  +--+----------------+
  |                   |
  v                   v
CONTINUE            CONTAIN
SAFELY              / FAIL
```

The network failed in both cases.

The difference is what that failure is allowed to destroy.

---

# 31. The Statement

The strongest description of the problem is also one of the simplest:

> **VRP does not prevent the network from failing. It changes what transport failure is allowed to destroy.**

The network can disappear.

The transport can disappear.

The path can disappear.

The architectural question is whether the logical session must disappear with them.

That is the problem VRP is built to investigate.

---

# Session != Transport

# Reachability != Authority

# Availability != Correctness

# Replay != Progress

# Continuity First

---

## Veil Routing Protocol

Public network-failure architecture document.

Protected runtime implementation remains private.

No protected recovery algorithms, authority mechanisms, security-sensitive thresholds, or private runtime logic are disclosed by this document.
# Veil Routing Protocol — Technical Overview

## Status

This document describes the public architectural surface of the Veil Routing Protocol (VRP).

It intentionally does not disclose protected runtime implementation details, internal decision algorithms, private recovery mechanisms, security-sensitive thresholds, cryptographic internals, or proprietary runtime logic.

---

## 1. The Problem

Traditional networked systems frequently associate a logical session with the transport path currently carrying it.

That assumption works while the path remains stable.

Real networks are not stable.

A device may:

- move between Wi-Fi and mobile connectivity,
- experience NAT or CGNAT rebinding,
- temporarily lose connectivity,
- recover through another interface,
- encounter jitter, reordering, congestion, or latency spikes,
- reconnect while stale state still exists elsewhere.

When transport identity and session identity are tightly coupled, transport disruption can propagate upward and become session disruption.

VRP explores a different architectural model.

---

## 2. Core Principle

The central VRP principle is:

**Session != Transport**

A transport is a replaceable carrier.

A session is a logical continuity object whose identity is not defined solely by the lifetime of one transport path.

Conceptually:

SESSION
→ Transport A
→ Transport B
→ Recovered Path
→ Future Transport

The carrier may change.

The logical continuity identity should not automatically change with it.

---

## 3. Continuity First

VRP is built around a continuity-first architecture.

The objective is not to pretend that network failures do not happen.

The objective is to make failure explicit, observable, and bounded.

A transport may:

- disappear,
- recover,
- migrate,
- become stale,
- be replaced,
- deliver information out of order.

Those events must not silently redefine session authority.

Transport state and session state are therefore treated as different architectural concerns.

---

## 4. Public Runtime Invariants

The public VRP model is organized around several invariants.

### Session identity survives transport replacement

Changing the underlying path must not automatically create a new logical session identity.

### Transport does not define authority

A reachable path does not become authoritative merely because it is reachable.

### Authority progression is monotonic

Older authority must not silently replace newer authority.

### Stale state is rejected

Previously valid state must not regain authority merely because it reappears.

### Replay does not become progress

Previously observed events must not be interpreted as new canonical progress.

### Duplicate execution is contained

Repeated delivery must not silently create multiple canonical state transitions.

### Recovery preserves canonical history

Recovery must not rewrite accepted history merely to restore connectivity.

### Failure is contained

When required invariants cannot be established, the runtime should avoid silently manufacturing continuity.

---

## 5. Failure Is Part of the Architecture

VRP does not treat network failure as an exceptional condition outside the protocol model.

Failure is part of normal runtime behavior.

The architecture explicitly considers conditions such as:

- path loss,
- path recovery,
- transport replacement,
- stale state,
- replay,
- conflicting state,
- recovery,
- concurrent delivery,
- reordered delivery.

The protected implementation determines how these conditions are handled internally.

The public validation surface focuses on their externally observable consequences.

---

## 6. Recovery

Recovery in VRP does not simply mean:

> reconnect and continue.

Recovery must preserve the same invariants that apply during normal operation.

At a high level:

Transport disruption

↓

Continuity state remains bounded

↓

Candidate recovery path appears

↓

Runtime evaluates admissibility

↓

Stale, replayed, or conflicting state is contained

↓

Canonical continuity may proceed

The implementation of these decisions belongs to the protected runtime.

Their externally observable behavior can be tested.

---

## 7. Deterministic Behavior

A recovery system becomes difficult to trust when equivalent inputs can produce unexplained state divergence.

Deterministic behavior is therefore a major VRP engineering objective.

Validation work exercises scenarios involving:

- repeated execution,
- reordered delivery,
- duplicate delivery,
- parallel delivery,
- recovery reconstruction,
- transport migration,
- stale state,
- replay conditions,
- authority transitions,
- large recovery graphs,
- runtime pressure.

The engineering objective is not simply successful execution.

It is reproducible behavior under failure.

---

## 8. Evidence-Oriented Validation

VRP separates implementation from evidence.

The protected runtime does not need to disclose its internal mechanisms in order to demonstrate externally observable properties.

The public validation model is:

Scenario

↓

Runtime execution

↓

Observable behavior

↓

Evidence

↓

Verification

↓

Verdict

This allows an evaluator to ask a stronger question than:

> Can I see all of the source code?

The relevant engineering question is:

> Can the claimed behavior be challenged, reproduced, and independently verified?

---

## 9. Adversarial Validation

VRP validation is intentionally not limited to normal connectivity.

The runtime has been exercised against classes of conditions including:

- transport interruption,
- path migration,
- duplicate delivery,
- replay attempts,
- stale state,
- recovery races,
- conflicting state,
- reordered events,
- repeated recovery,
- sustained runtime pressure.

Public documentation describes observable behavior and validation outcomes.

Protected implementation mechanisms remain outside the public boundary.

---

## 10. Security Posture

VRP is a networking and continuity architecture.

Its protocol model does not depend on covert persistence, privilege escalation, disabling host security controls, or hidden data exfiltration.

A deployment can instead be evaluated through explicit boundaries:

- what enters the runtime,
- what leaves the runtime,
- what state is retained,
- what authority is accepted,
- what evidence is emitted,
- what happens during failure.

VRP is intended to make these boundaries inspectable rather than requiring trust in opaque claims.

---

## 11. What VRP Is Not

VRP should not be understood simply as:

- another VPN tunnel,
- a reconnect script,
- an interface-switching utility,
- a load balancer,
- a conventional failover daemon,
- a replacement for every existing transport protocol.

Those technologies solve different problems.

VRP addresses another architectural question:

**How can logical continuity remain authoritative while the transports carrying it change or fail?**

---

## 12. Transport Independence

VRP does not require the architectural identity of a session to remain permanently bound to one transport technology.

The model separates:

**logical continuity**

from:

**current transport**

This distinction allows transport replacement to become a runtime event rather than automatically becoming session destruction.

Transport independence does not mean that arbitrary transports are accepted without validation.

It means that transport lifetime and session lifetime are different architectural dimensions.

---

## 13. Why This Matters

Modern systems increasingly operate across unstable network boundaries:

- mobile devices,
- roaming endpoints,
- distributed runtimes,
- edge infrastructure,
- multipath environments,
- intermittently connected systems,
- geographically distributed services.

In these environments, connectivity is not a permanent binary property.

Paths appear and disappear.

VRP investigates whether continuity can become a first-class runtime property rather than an accidental consequence of transport stability.

---

## 14. Public / Protected Boundary

The public VRP surface may describe:

- architectural principles,
- protocol invariants,
- observable runtime behavior,
- failure classes,
- validation methodology,
- benchmark observations,
- evidence formats,
- pilot evaluation boundaries.

The protected implementation may contain:

- internal authority mechanisms,
- recovery decision mechanisms,
- security-sensitive algorithms,
- private runtime policy,
- implementation-specific thresholds,
- protected state transitions,
- proprietary runtime mechanisms.

The public documentation is intentionally designed to support technical evaluation without disclosing the protected runtime.

---

## 15. How VRP Should Be Evaluated

VRP should not be evaluated because it is described as "next generation."

It should be evaluated by attempting to break its declared invariants.

Ask:

- Can transport disappear without silently destroying session identity?
- Can stale state regain authority?
- Can replayed state become canonical progress?
- Can duplicate delivery cause duplicate canonical execution?
- Can recovery rewrite accepted history?
- Can repeated execution produce unexplained divergence?
- Can externally observable evidence distinguish preservation from failure?

These are testable engineering questions.

That is the intended evaluation surface.

---

## 16. Engineering Direction

Current engineering work continues to strengthen:

- deterministic recovery,
- bounded runtime behavior,
- causality reconstruction,
- replay containment,
- stale-state rejection,
- authority continuity,
- evidence verification,
- runtime performance,
- adversarial validation,
- public/private boundary separation.

Individual validation documents in this repository provide narrower evidence for specific engineering stages.

---

## 17. Pilot Evaluation

A VRP pilot is intended to be an engineering evaluation.

It is not a request to accept architectural claims on trust.

A suitable evaluation should define:

1. the integration boundary,
2. the failure scenarios to exercise,
3. the invariants expected to survive,
4. the observable evidence,
5. explicit PASS / FAIL conditions.

Earlier evaluation is useful because real infrastructure can expose assumptions that synthetic environments cannot.

Pilot participation therefore allows VRP to be challenged against real operational constraints while the external integration boundary continues to mature.

Pilot participation does not imply access to protected implementation internals.

---

## 18. The Architectural Question

VRP ultimately begins with one question:

**What if losing the transport did not have to mean losing the session?**

The resulting architecture treats continuity, authority, recovery, and evidence as explicit runtime concerns.

The shortest description remains:

**Session != Transport**

**Continuity First**

---

Veil Routing Protocol (VRP)

Public architectural documentation.

Protected runtime implementation remains private.
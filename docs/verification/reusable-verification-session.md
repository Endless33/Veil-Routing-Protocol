# Reusable Verification Session

## Overview

A reusable verification session provides a deterministic verification context that can validate multiple independent evidence bundles using immutable verification configuration.

The session is independent from the VRP runtime and never accesses runtime state during verification.

---

## Purpose

The reusable session exists to separate verification configuration from verification execution.

A single session can verify multiple evidence bundles without rebuilding verification state.

This reduces duplicated initialization while preserving deterministic behavior.

---

## Architecture

```text
NewSession(Profile)
        │
        ▼
Session.Verify()
        │
        ▼
Session.VerifyBundle()
        │
        ▼
VerifyBundle()
        │
        ▼
EvidenceBundle.Verify()
```

The verification pipeline has one canonical implementation.

Top-level APIs delegate into the reusable session.

---

## Public Guarantees

The reusable verification session guarantees:

- Immutable verification configuration.
- Deterministic verification results.
- Runtime-independent verification.
- Stateless verification execution.
- Thread-safe concurrent verification.
- Reusable verification context.
- No mutation of supplied evidence.
- No mutation of verification profile.

---

## Validation

The reusable verification session is validated through automated tests covering:

- repeated verification
- concurrent verification
- deterministic verification
- canonical API behavior
- ownership isolation
- reusable verification context
- session and top-level API equivalence

All validation passes successfully under the Go race detector.

---

## Scope

The reusable verification session verifies already generated evidence.

It does not:

- generate evidence
- modify evidence
- expose runtime implementation
- require protected runtime components
- access runtime memory

---

## Design Principles

The reusable verification session follows these principles:

- Verification is independent from runtime execution.
- Verification configuration is immutable.
- Verification behavior is deterministic.
- Public APIs expose contracts rather than implementation details.
- Runtime internals remain outside the public verification boundary.
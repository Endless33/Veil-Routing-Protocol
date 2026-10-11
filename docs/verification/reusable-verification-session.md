# Reusable Verification Session

## Overview

The verification subsystem provides a reusable verification session that owns immutable verification configuration and can verify multiple independent evidence bundles.

A verification session contains no runtime state and does not depend on a running VRP instance.

---

## Motivation

Repeated verification should not require rebuilding verification configuration.

A reusable verification session allows:

- deterministic repeated verification
- concurrent verification
- immutable verification configuration
- runtime-independent verification

---

## Architecture

```
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

The session is responsible only for verification.

It does not own runtime state.

---

## Design Goals

The session is designed to provide:

- immutable configuration
- reusable verification context
- deterministic execution
- thread-safe verification
- runtime independence

---

## Public Guarantees

A verification session guarantees that:

- configuration cannot change after construction
- repeated verification produces deterministic results
- concurrent verification is supported
- verification never depends on runtime state
- verification never mutates the supplied evidence

---

## Validation

The implementation is validated through automated tests covering:

- repeated verification
- concurrent verification
- API consistency
- deterministic results
- ownership isolation
- canonical verification path

All verification tests execute successfully under the Go race detector.

---

## Scope

The reusable verification session verifies already generated evidence.

It does not generate evidence.

It does not expose runtime implementation details.

It does not require access to protected runtime components.

---

## Design Boundary

The public verification API exposes verification contracts only.

Internal runtime implementation remains intentionally private.
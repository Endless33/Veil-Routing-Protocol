# Verification Documentation

## Overview

The VRP verification subsystem provides a deterministic, runtime-independent mechanism for validating published verification evidence.

This documentation describes the public verification architecture, public APIs, verification contracts, and design principles.

Only public verification interfaces are documented here.

Protected runtime implementation remains intentionally outside the scope of this documentation.

---

## Documentation

### Public Verification Overview

Introduces the public verification subsystem and its architectural boundaries.

- public-verification-overview.md

---

### Verification Design Principles

Describes the architectural principles governing independent verification.

- verification-design-principles.md

---

### Portable Verification Profile

Documents the portable representation of verification configuration.

Topics include:

- export
- import
- semantic validation
- strict JSON decoding
- transport independence

- portable-verification-profile.md

---

### Reusable Verification Session

Documents the reusable verification context used by the public verifier.

Topics include:

- immutable configuration
- deterministic execution
- concurrent verification
- canonical verification flow

- reusable-verification-session.md

---

### Stage 19 — Verifier API Consolidation

Documents the consolidation of the public verification APIs into a single canonical verification implementation.

Topics include:

- API consolidation
- canonical verification path
- reusable verification session
- removal of duplicated verification logic

- stage19-verifier-api.md

---

## Public Verification Scope

The public verification subsystem provides documentation for:

- verification contracts
- verification configuration
- portable verification profiles
- reusable verification sessions
- verification APIs
- verification results

---

## Protected Runtime Scope

The following components are intentionally excluded from the public verification documentation:

- runtime state machines
- session management
- authority implementation
- replay protection
- transport implementation
- synchronization mechanisms
- protected runtime algorithms
- internal runtime structures

These components remain private to the VRP runtime.

---

## Design Objective

The goal of the public verification subsystem is to provide a reproducible and independently verifiable validation process while maintaining a strict separation between public verification contracts and protected runtime implementation.
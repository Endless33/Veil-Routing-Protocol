# Public Verification Overview

## Overview

The public verification subsystem provides an independent mechanism for validating VRP evidence without requiring access to the runtime that originally produced it.

Its purpose is to allow external parties to verify published evidence using publicly documented verification contracts.

---

## Public Components

The public verification subsystem currently consists of:

- Verification Profile
- Portable Verification Profile
- Reusable Verification Session
- Evidence Verifier

Each component has a well-defined responsibility and operates independently from runtime execution.

---

## Verification Flow

```text
Portable Verification Profile
            │
            ▼
Verification Session
            │
            ▼
Evidence Verification
            │
            ▼
Verification Result
```

Every verification operation follows the same canonical verification pipeline.

---

## Design Goals

The public verification subsystem is designed to provide:

- deterministic verification
- reproducible results
- runtime independence
- immutable verification configuration
- transport independence
- stable public contracts

---

## What Is Public

The following concepts are part of the public verification interface:

- verification profiles
- portable verification profiles
- reusable verification sessions
- verification results
- evidence validation contracts

These components are documented and intended for independent use.

---

## What Is Not Public

The following implementation details remain outside the public verification interface:

- runtime state machines
- authority implementation
- session management
- transport implementation
- replay protection mechanisms
- runtime synchronization
- protected runtime algorithms

These components remain private to the VRP runtime.

---

## Compatibility

The public verification subsystem is designed to evolve without changing its verification semantics.

Future runtime improvements should not require changes to previously published verification evidence or verification contracts.

---

## Current Status

The public verification subsystem currently provides:

- reusable verification sessions
- portable verification profiles
- canonical verification APIs
- deterministic verification behavior
- semantic profile validation
- strict JSON decoding

Future releases may extend functionality while preserving existing verification contracts.
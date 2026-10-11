# Portable Verification Profile

## Overview

A Portable Verification Profile is a transport-independent representation of trusted verification configuration.

It contains only the information required to independently verify evidence outside the VRP runtime.

---

## Purpose

The portable profile enables verification to be performed independently from the environment where evidence was originally produced.

It allows trusted verification configuration to be exchanged without exposing runtime implementation details.

---

## Portable Structure

A portable verification profile contains:

- SchemaVersion
- ExpectedIDs
- TrustedDigests

No runtime state is included.

No runtime objects are serialized.

No implementation-specific structures are exported.

---

## Export

A runtime verification profile can be exported into a portable representation.

Export guarantees:

- owned copies
- immutable exported state
- deterministic output
- no shared mutable memory

Changes made to exported data never affect the original verification profile.

---

## Import

A portable verification profile can be reconstructed into a runtime verification profile.

Import performs canonical reconstruction using public verification contracts.

Imported profiles preserve the same verification semantics as the original profile.

---

## JSON Representation

Portable profiles support JSON serialization.

The JSON decoder applies strict validation.

The decoder:

- rejects unknown fields
- rejects trailing JSON
- validates schema version
- validates semantic correctness

---

## Semantic Validation

Portable verification profiles are rejected when:

- SchemaVersion is zero.
- ExpectedIDs is empty.
- TrustedDigests is empty.
- Duplicate campaign identifiers exist.
- Trust anchors do not match the expected campaign set.
- Required trust anchors are missing.
- Unexpected trust anchors are present.

Only semantically valid verification profiles are accepted.

---

## Public Guarantees

Portable verification profiles provide:

- deterministic serialization
- deterministic reconstruction
- immutable exported state
- transport-independent representation
- runtime-independent verification configuration

---

## Design Boundary

Portable verification profiles intentionally expose only verification configuration.

Runtime implementation details, state machines, transport behavior, synchronization logic, and protected runtime components remain outside the public interface.
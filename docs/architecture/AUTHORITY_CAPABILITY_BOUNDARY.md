# Authority Claims and Capability Boundary

## 1. Purpose

Veil Routing Protocol (VRP) distinguishes descriptive authority claims from runtime capabilities.

This distinction is part of the project's approach to explicit authorization boundaries and controlled runtime behavior.

This document describes the public architectural principle without disclosing protected implementation details.

## 2. Two Different Concepts

### Authority Claims

Authority claims describe the authority context being evaluated.

They provide a representation that can be examined by validation and checking components without treating the claims themselves as proof of runtime authorization.

A claim is not, by itself, a runtime capability.

### Runtime Capabilities

Runtime capabilities represent authorization handles used by the runtime.

In the Stage 9S implementation, the public authority-token representation was reduced to an opaque identifier. Associated authority metadata is maintained internally.

The identifier alone does not make an arbitrary, unissued token valid.

## 3. Boundary Principles

The public design follows these principles:

- **Separation:** Descriptive claims and runtime capabilities serve different purposes.
- **Encapsulation:** Internal authority metadata is not exposed through the public token representation.
- **Context validation:** A capability must be evaluated in the context required by the relevant operation.
- **Replay rejection:** Reuse of a consumed capability is rejected by the tested validation path.
- **Explicit failure:** Unknown or invalid token identifiers must not be accepted as valid authority.
- **State integrity:** Rejected invalid inputs should not corrupt the authority state in the tested scenarios.

These principles describe the intended boundary and the behavior covered by the published tests. They are not a claim that every possible execution path has been formally verified.

## 4. Stage 9S Implementation Record

The following public commits record the work:

- `9b81fb2e` — `core: make authority tokens opaque capabilities`
- `c97a51f3` — `core: separate authority claims from runtime capabilities`

The changes include a dedicated authority-claims representation, updates to authority-checking and model-checking components, and tests covering opaque token behavior and claims separation.

Repository: [Endless33/jumping-vpn-core](https://github.com/Endless33/jumping-vpn-core/tree/fix/stage9s-integrity-hardening)

## 5. Validation Scope

The published validation included targeted tests for:

- Unknown and forged token rejection.
- Token integrity and context binding.
- Reuse rejection.
- Concurrent single-use behavior.
- Separation between authority claims and runtime capabilities.

The full Go test suite with the race detector and Go static analysis also completed successfully for the published Stage 9S revision.

See [Stage 9S Validation Report](../validation/STAGE_9S_VALIDATION_REPORT.md) for the recorded test commands and limitations.

## 6. Protected Implementation Boundary

This document intentionally does not specify:

- Internal capability issuance or identifier-generation mechanisms.
- Internal authority-state layouts.
- Private authorization algorithms or enforcement code.
- Secret material, credentials, or operational procedures.
- Protected runtime control flow.

These omissions are deliberate. The purpose of the public specification is to explain the architectural contract and validation scope without exposing the protected implementation.

## 7. What the Evidence Supports

The published changes and tests support the claim that the tested implementation uses an opaque public token representation and distinguishes descriptive authority claims from runtime capabilities.

They do not establish universal immunity to forgery, replay, concurrency defects, or other security failures outside the tested scenarios.

## 8. Architectural Principle

**A description of authority is not authority itself.**

VRP maintains a boundary between the representation of claims and the runtime capability used for authorization. The public engineering record describes that boundary and its tested behavior; the protected implementation remains private.

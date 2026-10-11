Title:
Stage 19 — Verifier API Consolidation

Contents:

- Purpose of Stage 19
- Motivation
- Previous architecture
- Current architecture

Verify()
    ↓
Session.Verify()
    ↓
Session.VerifyBundle()
    ↓
VerifyBundle()
    ↓
EvidenceBundle.Verify()

Explain that:

- verification logic now has a single canonical implementation
- top-level Verify() is a convenience wrapper
- duplicated verification logic has been removed
- deterministic behavior is preserved
- verification remains runtime-independent

Public guarantees:

- immutable verification session
- stateless verification
- reusable session
- thread-safe usage
- deterministic verification results

Validation summary:

go test ... -race
go vet

PASS

------------------------------------------------------------

FILE 2
docs/verification/reusable-verification-session.md

Title:
Reusable Verification Session

Contents:

Purpose

Session lifecycle

Construction

Verification flow

Repeated verification

Concurrent verification

Public guarantees:

- immutable configuration
- reusable object
- no runtime access
- deterministic output
- independent verification context

Document verified behaviors:

✓ repeated verification

✓ concurrent verification

✓ canonical API

✓ ownership isolation

Without describing internal algorithms.

------------------------------------------------------------

FILE 3
docs/verification/portable-verification-profile.md

Title:
Portable Verification Profile

Describe:

PortableProfile

SchemaVersion

ExpectedIDs

TrustedDigests

Export()

Import()

JSON representation

Strict decoding

DisallowUnknownFields

Semantic validation

Public guarantees:

- portable
- immutable
- transport independent
- canonical reconstruction
- owned copies
- no aliasing

Validation rules:

schema != 0

ExpectedIDs required

TrustedDigests required

registry and trust anchors must match

duplicate IDs rejected

unexpected trust anchors rejected

missing trust anchors rejected

No internal runtime structures exposed.

------------------------------------------------------------

FILE 4
docs/verification/verification-design-principles.md

Title:
Verification Design Principles

Document only architectural principles.

Examples:

Verification is independent from runtime.

Evidence is verified, never trusted.

Profiles are immutable.

Verification sessions are reusable.

Portable configuration contains only verification state.

Verification is deterministic.

Verification APIs expose contracts, not runtime implementation.

Transport is irrelevant to verification.

Runtime implementation details remain private.

Explain invariants only.

No implementation details.

------------------------------------------------------------

Public documentation intentionally excludes:

- SessionManager internals
- AuthorityToken implementation
- Runtime FSM
- Replay implementation
- Internal synchronization
- Core state machines
- Protected runtime algorithms
- Internal evidence generation
- Private transport logic

These remain inside jumping-vpn-core.

Current public documentation status

Completed:

Stage 14
Stage 15
Stage 16
Stage 18
Stage 19

Next public milestone:

Stage 20
Standalone Verification Runtime
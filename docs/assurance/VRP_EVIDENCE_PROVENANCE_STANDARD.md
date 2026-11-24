# VRP Evidence Provenance Standard

**Classification:** Public evidence contract
**Evidence cutoff:** 2026-11-24

## Purpose

Define minimum provenance and integrity requirements
for independently reviewable VRP qualification evidence.

Evidence must support verification of what was observed,
which system was evaluated and which claims remain
outside the observation boundary.

## Evidence package

A qualification bundle should contain:

- `README.md`: scope, limitations and execution context.
- `MEASUREMENTS.csv`: recorded observations.
- `VERIFICATION_RESULTS.json`: machine-readable verdicts.
- `SHA256SUMS`: file integrity manifest.
- A verifier with documented execution requirements.
- An explicit list of absent or unavailable witnesses.

These filenames describe a proposed evidence format,
not proof that a complete qualifying bundle exists.

## Required provenance

Each evidence package should identify:

1. The evaluated release or immutable build identity.
2. The approved test scenario and configuration.
3. The observation source for each reported property.
4. Whether observations are independent or self-reported.
5. The relationship between transport events and
   canonical logical-session evidence.
6. The verification procedure and negative controls.
7. The limitations of the evidence and its trust anchors.

Private infrastructure addresses, credentials,
protected implementation details and confidential
runtime data must not appear in public artifacts.

## Integrity requirements

A file hash supports detection of file changes relative
to a trusted reference.

A self-generated checksum alone does not establish
independent provenance, canonical history or the
authenticity of the original observation.

Where stronger claims are required, evidence must be
bound to an independently trusted source or anchor.

## Negative controls

A verifier must reject or mark inconclusive:

- Missing required witness data.
- Modified or inconsistent evidence.
- Replayed evidence presented as fresh.
- Synthetic events presented as real execution.
- Unauthenticated canonical identity claims.
- Duplicate commits presented as unique effects.
- Unanchored history presented as independent proof.
- Transport recovery presented as session continuity.

## Public disclosure policy

The public bundle should expose only the minimum
information needed to reproduce and challenge a claim.

The Protected Core is excluded from the public
evidence surface.

## Qualification rule

Evidence integrity, evidence authenticity and
protocol correctness are separate properties.

A successful checksum verification is not proof
of session continuity.

**No claim exceeds its evidence.**

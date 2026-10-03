# Veil Routing Protocol — Public Provenance Record

## Purpose

This document records a reproducible integrity snapshot of the canonical
public Veil Routing Protocol repository.

It provides technical provenance information for a specific repository
state.

It is not, by itself, a legal determination of invention, priority,
ownership, patentability, originality, or infringement.

Those questions depend on the relevant facts and applicable law.

---

## Project

**Project:** Veil Routing Protocol (VRP)

**Author:** Vitalijus Riabovas

**Development period represented by the project record:** 2024–2026

**Canonical public repository:**

https://github.com/Endless33/Veil-Routing-Protocol

---

## Canonical Baseline

The following Git state identifies the public repository snapshot whose
document hashes are recorded below.

    Commit:
    802de0d0fd0a73420a2847e389b7ef74e78cda71

    Tree:
    0845a485e3756f4350389348628a229fcbc7dce6

    Branch:
    main

    Capture UTC:
    2026-10-03T17:30:01Z

The commit identifier binds the Git history leading to this snapshot.

The tree identifier binds the tracked repository content represented by
that commit.

The SHA-256 values below provide an additional content-level integrity
record for the principal public VRP documents.

---

## SHA-256 Document Manifest

    7c1903277a8b9a52f4a297502be920d3eb87699ce561238f6302a27f9d0b22a8  README.md
    ecca67af3c6fc7720876a3464a7950013ac32f170602c96c0d2b8093b26cf7f1  LICENSE
    efa5ba03f4e40c7bcbb4a428e6c9789cda03fc987db02b2fd97713cd3f28cf8c  ARCHITECTURE.md
    cfde2203be3362490c65f2703aa98ee1840deab66e7c2b28f9df3a1f0f635ac6  INTEGRATION.md
    26fd25c512e294d1acd7221cdbd364698501c39134ed348738cec96e5a525013  COMPARISON.md
    8d4d03a1c909d5eafcf03cffa77402cd966cceab69f8431ff2fc6eb77574223c  SECURITY_MODEL.md
    092740ccab51b3173eee5d987b94b5ded222201bae2175f98e1a04a5c4378faf  ORIGIN.md
    582395f7d9c9d266f360ddb777dd743771debb9d22d6aff0959ee5b59ef393f2  CONTACT.md
    57a15905506f3f8dcbf085b625145cb3f8900ef1225a97c34978e1ed1ba0c2f3  CHANGELOG.md
3a760d296cd53b37e9756c3e4814961ca13685fab3306eaaa3d8a4867ff0a078  AI_AND_AUTOMATED_USE_POLICY.md

---

## Independent Verification

A reviewer with the corresponding repository state can verify the
document hashes with:

    sha256sum \
      README.md \
      LICENSE \
      ARCHITECTURE.md \
      INTEGRATION.md \
      COMPARISON.md \
      SECURITY_MODEL.md \
      ORIGIN.md \
      CONTACT.md \
      CHANGELOG.md

The Git identifiers can be verified with:

    git rev-parse HEAD
    git rev-parse 'HEAD^{tree}'

For the baseline recorded by this document, the expected identifiers are:

    HEAD=802de0d0fd0a73420a2847e389b7ef74e78cda71
    TREE=0845a485e3756f4350389348628a229fcbc7dce6

---

## Interpretation Boundary

This provenance record establishes a reproducible association between a
specific Git repository state and specific public document contents.

It should not be interpreted as claiming that a Git commit, timestamp,
tree identifier, or SHA-256 digest alone conclusively establishes legal
priority or ownership of every idea described by those documents.

The public architecture and protected implementation remain separate.

    PUBLIC ARCHITECTURE != PUBLIC CORE

    PUBLIC DOCUMENTATION != PROTECTED IMPLEMENTATION

    HASHED CONTENT != AUTOMATIC LEGAL MONOPOLY

    SESSION != TRANSPORT

---

## Public / Private Boundary

This record covers only the public repository state identified above.

It does not disclose, hash, enumerate, or describe the contents of the
protected VRP Core.

Private implementation material remains governed by its own access,
licensing, confidentiality, and security boundaries.

---

## Canonical Statement

VRP treats logical session continuity as distinct from the lifetime of
any individual transport.

    SESSION != TRANSPORT

    CONTINUITY FIRST.

---

Vitalijus Riabovas
Veil Routing Protocol
2024–2026

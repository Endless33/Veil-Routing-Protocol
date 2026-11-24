# VRP Independent Review Entry Point

**Project:** Veil Routing Protocol
**Review model:** Specification-first, evidence-driven
**Current continuity verdict:** INCONCLUSIVE

## Start here

VRP defines the architectural distinction:

**SESSION != TRANSPORT**

The evaluation question is whether canonical logical
session identity and accepted history remain valid
across transport changes and failures.

Reviewers should not infer logical-session continuity
from successful UDP exchanges or endpoint recovery.

## Public review sequence

### 1. Establish the claim boundary

Read:

- [Public Assurance Status](VRP_PUBLIC_ASSURANCE_STATUS.md)
- [Security Claims and Limitations](VRP_SECURITY_CLAIMS_AND_LIMITATIONS.md)

Separate declared protocol objectives from independently
qualified implementation behavior.

### 2. Establish the evaluation contract

Read:

- [Independent Evaluation Contract](VRP_INDEPENDENT_EVALUATION_CONTRACT.md)
- [Adversarial Qualification Matrix](VRP_ADVERSARIAL_QUALIFICATION_MATRIX.md)

Identify which negative controls and real witnesses
are required for the claim being tested.

### 3. Evaluate provenance

Read:

- [Evidence Provenance Standard](VRP_EVIDENCE_PROVENANCE_STANDARD.md)

Check the origin, independence, integrity and
limitations of every reported observation.

### 4. Challenge the evidence

An independent reviewer should attempt to distinguish:

- Transport recovery from canonical identity.
- Request delivery from receiver-side commit.
- Self-reported state from authorized witness evidence.
- Synthetic verification from runtime execution.
- Local checksums from independently anchored history.
- Accepted authority from stale or conflicting claims.

A missing witness must not be replaced by an
assumption of correct behavior.

## Current evidence boundary

External transport observations have been recorded.

An isolated synthetic witness contract passed
eleven controlled tests.

Independent canonical session identity, application
commit, authority and history witnesses have not yet
been connected to the public qualification workflow.

Accordingly, independent end-to-end continuity
qualification is not currently claimed.

## Reviewer outcomes

A review may conclude PASS, FAIL, INCONCLUSIVE
or NOT TESTED for a specifically defined property.

A negative or inconclusive result is valid engineering
evidence when its scope and provenance are clear.

## Access and intellectual property

Public review does not grant access to private source,
Protected Core, credentials or infrastructure.

Additional evaluation access requires explicit
authorization and a separately defined scope.

**Read the specifications. Examine the evidence.
Challenge the engineering.**

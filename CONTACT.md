# Veil Routing Protocol — Contact and Evaluation

**Project:** Veil Routing Protocol (VRP)  
**Author:** Vitalijus Riabovas  
**Development:** 2024–2026  
**Status:** Active Development  
**Public Surface:** Architecture  
**Protected Surface:** Private Runtime

> **SESSION ≠ TRANSPORT**

> **CONTINUITY FIRST.**

---

# Purpose

The public VRP repository exists to explain the architecture.

It is not a public support channel for reconstructing the protected implementation.

Contact is most useful when there is a concrete technical or organizational reason to evaluate VRP.

---

# Appropriate Contact

Relevant inquiries include:

- controlled technical evaluation;
- pilot deployment;
- infrastructure integration;
- engineering review;
- research discussion with a concrete technical objective;
- security evaluation;
- target-environment qualification;
- commercial deployment discussion;
- serious organizational collaboration.

A useful inquiry should describe the actual problem being considered.

---

# Before Contacting

Please review the public repository first.

In particular:

- `README.md`
- `ORIGIN.md`
- `ARCHITECTURE.md`
- `INTEGRATION.md`
- `COMPARISON.md`
- `SECURITY_MODEL.md`

These documents explain the public VRP architecture and its disclosure boundary.

If the question is already answered there, additional private explanation may not be provided.

---

# Useful Evaluation Information

For a technical evaluation or pilot discussion, useful context includes:

### Environment

What infrastructure would VRP operate in?

### Application

What application, service or workload requires continuity?

### Current Transport

What networking or transport technology is currently used?

### Continuity Problem

What specifically fails today?

### Failure Model

Which failures need to be survived or contained?

Examples may include:

- network transition;
- temporary outage;
- path replacement;
- transport loss;
- stale execution;
- duplicate execution;
- replay;
- failover;
- authority transition;
- recovery race.

### Scale

What approximate deployment scale is expected?

### Security Requirements

What security properties or trust boundaries matter?

### Evaluation Objective

What would the organization like to establish?

---

# A Good Evaluation Request

A useful request resembles:

> We operate a long-lived session-based service across unstable client connectivity. Sessions must survive network transitions without allowing historical operations to execute after recovery. We would like to evaluate VRP against our existing transport architecture and defined failure conditions.

That provides a concrete engineering starting point.

---

# A Less Useful Request

Requests such as:

> Send the private source.

or:

> Explain exactly how the Core works internally.

or:

> Send everything so we can reproduce it.

do not constitute an evaluation plan.

The protected implementation is not publicly distributed through this repository.

---

# Public Architecture

The following information is intentionally public:

- project identity;
- architectural purpose;
- core principles;
- conceptual architecture;
- integration position;
- relationship to existing technologies;
- security objectives;
- project authorship.

This is sufficient to determine whether the VRP problem is relevant to an organization.

---

# Protected Runtime

The following remains outside the normal public repository boundary:

- protected Core source code;
- internal algorithms;
- private state-machine implementation;
- implementation-specific authority mechanisms;
- protected recovery mechanisms;
- private validation infrastructure;
- internal regression corpus;
- detailed adversarial scenarios;
- private runtime traces;
- private evidence artifacts;
- protected deployment mechanisms.

Public documentation should not be interpreted as entitlement to these materials.

---

# Technical Evaluation

The preferred external path is:

    DEFINE THE PROBLEM
            |
            v
    DEFINE THE ENVIRONMENT
            |
            v
    DEFINE ACCEPTANCE CRITERIA
            |
            v
    CONTROLLED EVALUATION
            |
            v
    OBSERVE FAILURE AND RECOVERY
            |
            v
    REVIEW EVIDENCE
            |
            v
    MAKE AN ENGINEERING DECISION

The objective is not to demonstrate that VRP must succeed.

The objective is to determine whether VRP satisfies the required invariants in the target environment.

---

# Negative Results Are Valid Results

A serious evaluation must be capable of failing.

Possible outcomes may include:

    ACCEPTED

    ACCEPTED WITH CONDITIONS

    NOT ACCEPTED

A failed requirement is engineering information.

It should not be hidden merely to produce a successful demonstration.

---

# No Universal Deployment Claim

VRP does not claim universal production readiness.

A deployment must be qualified against its own:

- infrastructure;
- workload;
- topology;
- transport;
- failure model;
- scale;
- security requirements;
- operational constraints.

Previous engineering results do not automatically qualify a materially different environment.

---

# No Free Reconstruction Service

The public repository is intentionally designed to explain the architecture without functioning as a reconstruction manual.

General questions about the published architecture may be answered publicly when useful.

Requests for detailed protected implementation guidance, private algorithms or step-by-step Core reproduction should not be expected to receive technical disclosure.

---

# No Requirement for Continuous Public Communication

VRP development does not depend on continuous public posting.

Periods without:

- social-media activity;
- public reports;
- new public evidence;
- public repository changes;

should not automatically be interpreted as inactivity.

The protected runtime has its own development lifecycle.

Engineering may continue privately.

---

# Public Silence

The project may deliberately enter periods of reduced public communication while engineering work continues.

During such periods:

    PUBLIC ACTIVITY
          MAY DECREASE

while:

    PRIVATE ENGINEERING
          MAY CONTINUE

The absence of an immediate response should not be interpreted as a technical or commercial statement.

---

# Response Expectations

Sending an inquiry does not guarantee:

- immediate response;
- private technical disclosure;
- Core access;
- evaluation acceptance;
- pilot acceptance;
- commercial engagement.

Requests may be reviewed according to relevance, technical seriousness, available capacity and project direction.

---

# Protected Source Requests

The protected VRP Core is not an open-source release.

Please do not assume that public architectural documentation implies access to the private implementation.

If controlled implementation access is ever appropriate for a specific evaluation, its conditions must be established separately.

---

# Security Reports

A credible security concern relating to publicly exposed VRP material should include enough information to understand and reproduce the issue where appropriate.

Please avoid publishing sensitive exploit details publicly before reasonable technical review when the issue could affect an active protected deployment.

A report should distinguish between:

- an architectural concern;
- an implementation concern;
- a documentation concern;
- a theoretical attack;
- a reproduced security defect.

Precision is useful.

---

# Research Discussion

Technical research discussion is welcome when it is grounded in a specific engineering question.

VRP does not depend on claiming that all surrounding networking concepts are new.

Relevant prior art, alternative architectures and technically supported criticism are useful.

The project should be evaluated on its actual architecture and behavior.

---

# Attribution

When referencing the project publicly, please identify it as:

**Veil Routing Protocol (VRP)**

Developed by:

**Vitalijus Riabovas**

Development represented by the project:

**2024–2026**

Canonical repository:

https://github.com/Endless33/Veil-Routing-Protocol

---

# Contact

For serious VRP technical evaluation, pilot, integration or organizational inquiries:

**jumpingvpn@proton.me**

Please include enough technical context to understand why VRP is relevant to the proposed environment.

Messages consisting only of requests for private source code or protected implementation details may not receive a response.

---

# Final Note

VRP does not require anyone to believe a marketing claim.

The public architecture is available for inspection.

Organizations that identify a real continuity problem can define an environment, define acceptance criteria and evaluate whether VRP addresses it.

Everyone else is free to observe the project from the public boundary.

The architecture is public.

The implementation is protected.

The engineering continues.

---

# SESSION ≠ TRANSPORT

# CONTINUITY FIRST.

---

**Veil Routing Protocol (VRP)**  
**Vitalijus Riabovas**  
**2024–2026**
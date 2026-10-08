# Content Market Frame

**Working lab for turning real product behavior into a human-recognizable story, a credible market promise, and a visual sales narrative.** This is not a finished standard or an autonomous marketing agent. It is a reviewable method we can improve from real failures.

## Why this exists

A product can be technically well understood and still be described to customers incorrectly. Agents can read every file, research dozens of papers, and build a beautiful site while choosing the wrong protagonist, the wrong problem, and the wrong reason to care.

Our initial case is the Agent Custom Setup (ACS) site rewrite, where the narrative moved from narrowly framed agent coordination, through an overcorrection into continuity, through audit-style evidence dumping, toward a broader proposition: one install takes the repeated mechanical overhead of long-running projects off the human's desk. That proposition is a **working interpretation, not an owner-approved claim**.

The question this repository exists to answer: **How do we make the hard creative judgments reproducible without pretending they can all be reduced to deterministic text checks?**

## Start here

| File | Purpose |
| --- | --- |
| [EPISTEMIC_STATE.md](EPISTEMIC_STATE.md) | What is observed, inferred, unresolved, or explicitly rejected; ongoing decision log |
| [CASE_STUDY_ACS.md](CASE_STUDY_ACS.md) | Forensic analysis of the failed framing iterations and corrections |
| [FRAMEWORK.md](FRAMEWORK.md) | Stage-by-stage operating method, agent routing, deliverable contracts |
| [QA_GATES.md](QA_GATES.md) | Semantic quality gates, falsification tests, claim review, rendered and media review |
| [STORYBOARD_ACS.md](STORYBOARD_ACS.md) | Concrete, provisional sales-story example for the four-layer ACS pack |
| [templates/FRAME_BRIEF.md](templates/FRAME_BRIEF.md) | Fill-in input and product truth brief for the next repository |
| [templates/REVIEW_RECORD.md](templates/REVIEW_RECORD.md) | Review record designed to preserve criticism, decisions, and revisions |

## Core rule

**The source repository tells us what the product can do. Human research tells us what someone experiences. Strategy chooses which problem to lead with. A storyboard earns attention. Evidence constrains the promise. The generator implements approved decisions. None of those steps are interchangeable.**

The product is not the documentation. The evidence ledger is not the landing page. A grammatical sentence is not necessarily a human insight. A mechanically passing website is not necessarily a good sales story.

## Relationship to the existing stack

This is a **pre-generation framing and acceptance layer** meant to complement, not fork or replace, [Content Generation Modules (CGM)](https://github.com/Pukujan/content-generation-modules). CGM already owns brand/context, writing routes, visual direction, generation and HTML-demo contracts. This lab adds explicit product-truth reconciliation, market-story selection, storyboard review, semantic adversarial QA, and reusable failure memory. A future integration should feed approved artifacts into CGM and keep its existing authorities intact.

## Status and boundaries

- **Status:** v0 research-backed working draft; not an accepted universal framework.
- **Source handling:** The original conversation archive is private. This public repository contains only sanitized synthesis and publicly inspectable product facts. Do not paste private logs, credentials, machine paths, unpublished claims or private screenshots.
- **Claims:** Market data and alleged product outcomes are not verified by this repository. Avoid implied savings, adoption, customer proof, or efficacy until the specific evidence is checked.
- **Human authority:** Owner sign-off on positioning, factual promises, and visual direction is separate from passing tests.

## First operating loop

1. Fill the frame brief from source and real audience evidence.
2. Reconcile product scope and flag contradictions.
3. Write three competing narrative spines, then deliberately select one.
4. Approve a scene-by-scene storyboard before any webpage, image, or video generation.
5. Route implementation through the existing CGM/app-generation machinery.
6. Run the QA gates including a skeptical first-time-reader review, inspect pixels and media, and record what failed in the epistemic state.

Do not judge repeatability by how many assets the pipeline generates. Judge it by whether a new agent can derive a **correct, appealing, intelligible story** with dramatically fewer owner corrections.

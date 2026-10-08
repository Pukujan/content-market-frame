# Content Market Frame

**A reusable, context-efficient router for turning what a repository really does into a human-recognizable problem, credible market position, visual story, and honest product experience.**

This repository exists because a technically competent agent can still sell the wrong problem. Our ACS case required repeated corrections—from a fabricated coordination vignette to PCM-only continuity to a research-heavy audit-page voice—before the real human-centered sales direction emerged. **The valuable artifact is the decision process, not merely the generated site.**

**Status:** v0.1 implementation of the router and structural validation, **not** a proven cross-repository standard. The current ACS site is a substantial but not final positive baseline according to its owner. No Version B site has been generated or authorized by this repo.

## Start with the router

| Resource | Use |
| --- | --- |
| **[Router runbook](router/RUNBOOK.md)** | Exact reusable sequence and CLI commands; begin here |
| **[Machine router](router/router.v1.json)** | Stages, roles, gate conditions, context policy, failure-to-stage routing |
| **[Run schema](router/run.schema.json)** | Typed facts, decisions, approvals, rejected patterns, scene and claim records |
| **[Context protocol](router/CONTEXT_PROTOCOL.md)** | What to retain at each agent handoff instead of replaying long transcripts |
| **[Router CLI](scripts/frame.py)** | Create/validate runs, make bounded packets, invalidate stale decisions |
| **[Agent operating contract](AGENTS.md)** | Instructions another agent can load first |
| **[Automated checks](.github/workflows/frame-validation.yml)** | JSON Schema, standard-library CLI, tests and sample packet checks |

## Try the workflow without generating anything

Run locally with Python 3.12 or another supported Python 3 release:

~~~bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/frame.py validate examples/acs-version-b.run.json
python scripts/frame.py pack examples/acs-version-b.run.json
~~~

To start a new product, use the init command in the [runbook](router/RUNBOOK.md). The exported packet has a 450-word cap for hot context; additional evidence remains accessible by exact source link. A word cap is for handoffs, **not** a limit on careful investigation.

## ACS A → B is planned, not underway

| Artifact | Meaning |
| --- | --- |
| [Current ACS website](https://acs.design-bakery.com/) | Baseline A — owner-favored direction, still improvable; immutable capture pending |
| [ACS Version B plan](plans/ACS_VERSION_B_PLAN.md) | Ordered approach: stabilize router → capture A → choose B story → storyboard → only then generate separate B → compare |
| [ACS-B run JSON](examples/acs-version-b.run.json) | DRAFT source-linked record; no approvals, baseline not yet captured |
| [Future comparison template](templates/AB_COMPARISON.md) | Evaluation criteria and factual capture manifest; no invented results |

**Do not change or redeploy Baseline A because a planning document exists.** Do not call an untested B approach an experiment that already happened.

## Research, creative records and acceptance

| Resource | Use |
| --- | --- |
| [Epistemic state](EPISTEMIC_STATE.md) | Living observed/inferred/proposed/unknown/rejected/accepted claims and decisions |
| [ACS forensic case](CASE_STUDY_ACS.md) | Why the failed stories failed and how to route corrections upstream |
| [Framework](FRAMEWORK.md) | In-depth market-story creative stages, producer/editor roles |
| [QA gates](QA_GATES.md) | Semantic, source/claim, image/video and real-interaction checks |
| [Provisional ACS storyboard](STORYBOARD_ACS.md) | Worked buyer-belief example, not accepted marketing copy |
| [UX/product-design research](RESEARCH_UX_PRODUCT_DESIGN.md) | Established frameworks and proposed separate buyer-belief versus user-task track |
| [Negative fixtures](tests/REJECTION_FIXTURES.md) | Old failure classes as tests rather than a pile of banned words |
| [Agent router prompt](prompts/AGENT_ROUTER.md) | Detailed handoff instructions to complement the machine route |
| [Intake and review templates](templates/FRAME_BRIEF.md), [review record](templates/REVIEW_RECORD.md) | Human decision forms without inventing evidence |

## Relationship to CGM

[Content Generation Modules](https://github.com/Pukujan/content-generation-modules) still owns content context, brand foundation, writing routes, visual direction, image generation, demos and file naming. **This router sits in front of CGM** to decide which product story deserves implementation, what actual source evidence constrains it, and how an independent reviewer can reject semantic failures. It does not duplicate CGM's modules, change release pins, or grant editorial acceptance.

## Important boundaries

- The source conversation is private; only sanitized lessons and public repository facts belong here.
- Owner insight is direction, not fabricated user-research data or a measured product effect.
- Written specs, functioning demo, deployed page and user-approved copy are separate states.
- Never infer a completed real install from a no-write preview.
- Machine checks validate structural consistency, not buyer desire, UX quality, or true artistic direction.
- If the buyer/problem/product subject changes, downstream story, media and claims become stale. Preserve why they failed.

**Operating rule:** Investigate truth → interpret human need → compare positions → choose the story → plan visuals and UX → send an *approved* brief to CGM → independently inspect actual behavior and editorial meaning. Revisit the earliest faulty premise when QA fails.

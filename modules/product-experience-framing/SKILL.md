---
name: product-experience-framing
description: Route source-grounded product intent, market positioning, buyer storytelling, user-task UX and service-design evidence into concise owner QA and an accepted ABA implementation brief. No direct frontend generation.
---

# Product & Experience Framing (PEF)

**Status:** incubating here, not installed or registered in CGM yet.

## Activate when

A task asks for product introduction, landing page, marketing proposition, new-user onboarding, UX journey, service experience, brand-positioning rationale, visual storyboard, or a new app's human purpose.

**Do not activate for:** routine issue/PR prose, file naming, formatting a settled paragraph, basic technical debugging, or simply generating a pre-approved image. Do not treat \`html-demo\` as the frontend implementation route.

## Small boot sequence

1. Read only [router/router.v1.json](../../router/router.v1.json)'s active stage and [router/PEF_RUNBOOK.md](../../router/PEF_RUNBOOK.md); use [scripts/frame.py](../../scripts/frame.py) for the relevant run.
2. Retrieve a short evidence slice from the target repo at a specific revision. Separate shipped/observed mechanisms, owner direction, inferred buyer need and actual user research.
3. Extract the human job, trigger, workaround and stakes **before** choosing slogans, art style or page sections.
4. List distinct positioning alternatives. An independent reviewer checks for the wrong product, wrong audience, component collapse, audit-first prose, unsupported outcome or misleading action.
5. For **genuine consequential ambiguity**, create [pef-questions.schema.json](../../router/pef-questions.schema.json) records and generate the compact owner packet with [scripts/pef.py](../../scripts/pef.py). Do not ask for information recoverable from authoritative source. Prefer one conversational question; use a short group only when multiple independent necessities justify it.
6. Record a real person's answer and reviewer reference; **an answered question is not blanket editorial approval**. Preserve corrections and invalidate stale downstream scenes.
7. Develop **buyer belief storyboard** and (if interactive) **operator task/UX states**, reconciled with a **service blueprint** and verified CTA. Create the [Experience Brief](../../router/pef-experience.schema.json) with explicit S3/S4/S5 owner signoffs.
8. Compile an ABA spec from accepted evidence with \`python scripts/pef.py compile-aba <run> <questions> <brief> --out <file>\`. A nonapproved or unpinned run must stop. The manifest says \`compiled_not_executed\`: this is **not** app-generation or deployment authorization.
9. ABA alone builds and repairs code. An independent reviewer checks rendered pixels, user comprehension, task success, source claims and behavior; the human owner accepts or rejects the final experience.

## Context and failure policy

- Use the bounded 450-word frame packet for hot state. Source, full interviews and earlier drafts stay on demand.
- Keep prior rejection **classes** and source links, not whole failed drafts.
- Route a wrong audience/job to human discovery; wrong positioning to position selection; wrong scene to story design; bad task flow to UX/service definition; untruthful CTA to product truth and safety. Do not fix the wrong business thesis with CSS.
- Only mechanical facts supported by the target repo can be treated as implementation facts. Owner intentions do not prove observed customer benefit. No generated persona masquerades as actual research.
- A passed schema/checklist or builder blueprint is not a real owner's approval. Never silently publish.

## Ownership boundary

PEF owns **what and why**, the human experience, content promise, and the handoff contract. CGM's retained writing/visual/image skills may assist after framing approval. **App Builder Automation owns the frontend**, regardless of whether it emits semantic HTML or React. No competing CGM HTML implementation, no deployment/production mutation in this module.

## Outputs (minimal)

- A sourced run record with facts, assumptions, accepted/rejected decisions and next action;
- targeted uncertainty QA only when needed;
- selected positioning + buyer storyboard + optional UX/service trace;
- accepted Experience Brief and ABA input/manifest;
- independent QA verdict and epistemic handoff.

See the [PEF runbook](../../router/PEF_RUNBOOK.md) for executable commands, source/evidence/approval invariants, current limits and test fixtures.

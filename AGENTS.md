# Agent operating contract — Content Market Frame

This repository is the **working lab for product understanding, marketing framing, storyboard direction and semantic QA**, not a general app builder or a place to paste conversation dumps.

## Read order (context-efficient; do not load everything)

1. [README.md](README.md): purpose, the runnable router, and boundary between this repo and CGM.
2. [router/router.v1.json](router/router.v1.json): load the active stage's instructions and named dependencies, not an entire brainstorm archive.
   When the task concerns product/market/UX experience framing, also read [router/PEF_RUNBOOK.md](router/PEF_RUNBOOK.md) and load only the relevant PEF record/schema (not both full documentation sets).
3. [router/CONTEXT_PROTOCOL.md](router/CONTEXT_PROTOCOL.md) and [router/RUNBOOK.md](router/RUNBOOK.md): handoff packet budget, stage transitions, privacy and invalidations.
4. The relevant run record, for ACS-B [examples/acs-version-b.run.json](examples/acs-version-b.run.json). It remains DRAFT and does **not** authorize generation.
5. If source/market/creative review requires deeper material, use the specific targeted references below—not every file upfront.

### Additional source references

1. [README.md](README.md): purpose and relationship to the existing stack.
2. [EPISTEMIC_STATE.md](EPISTEMIC_STATE.md): authoritative status labels, case facts, open questions, rejected approaches.
3. [FRAMEWORK.md](FRAMEWORK.md): stage gates and agent roles.
4. [QA_GATES.md](QA_GATES.md): mandatory truth, narrative and rendered quality checks.
5. [RESEARCH_UX_PRODUCT_DESIGN.md](RESEARCH_UX_PRODUCT_DESIGN.md): grounded method comparisons and the **proposed**, not yet adopted, UX/product-design extension.
6. When working on ACS, read [CASE_STUDY_ACS.md](CASE_STUDY_ACS.md) and [STORYBOARD_ACS.md](STORYBOARD_ACS.md).
7. For a different product, start with [templates/FRAME_BRIEF.md](templates/FRAME_BRIEF.md).

## First responsibility

Before generating a landing page, copy, image, film, README, UI or app, **require accepted positioning and storyboard gates**. Do not infer approval from this chat, drafts, mechanical tests, or a prior successful design. Before any such work:
- Distinguish the **named repository's ownership** from the **bundle/product being marketed**.
- Verify current product contract and known boundaries; do not treat promotional copy as the highest authority.
- Write the human actor, problem, workaround, stakes, proposed change and credible mechanism.
- Generate **competing** positioning narratives and record the selection.
- Freeze a storyboard only after owner/editor review; absent approval mark it DRAFT.
- Run claim and semantic adversarial checks before invoking image/video or app generation.
- Compose with CGM instead of copying CGM's content/visual/image mechanisms into this repo.

**Wrong scope or false proof stops generation.** More web research or a nicer image is not a remedy for a mistaken market promise.

## Routing rule

Use the seven stages in [router/router.v1.json](router/router.v1.json) and the bounded output of the CLI handoff packet. The machine route determines which stage receives a failure. A wrong value proposition goes back to product truth/human job/positioning, **not** to the video model or CSS. Maintain source links and explicit status labels.

Product UX and interaction-task storyboarding are an optional linked track when the task concerns actual task completion, navigation, onboarding, or error recovery; they are not automatically activated by a marketing-page request.

The owner explicitly requested a **router first, a subsequent ACS B story plan second, and only later a controlled A/B comparison**. Do not build, deploy, alter the A site, generate new A/B visuals, or claim an experiment completed while the plan is still DRAFT. See [plans/ACS_VERSION_B_PLAN.md](plans/ACS_VERSION_B_PLAN.md).

## Conversation-to-decision procedure

If the owner corrects a draft:
1. Record the old assumption and the *meaning* of the rejection.
2. State the revised story invariant in human terms.
3. List every scene, headline, research point, media brief and CTA that depended on it.
4. Mark affected artifacts STALE until re-reviewed.
5. Update EPISTEMIC_STATE with explicit OBSERVED / OWNER DIRECTION / INFERRED / PROPOSED / UNKNOWN / REJECTED / APPROVED labels.
6. Preserve the rejected approach as a negative test case.
7. Do not tell the owner the work is “done” because a mechanical checker passed.

## Source boundaries

This repository is public. The original research-session log supplied for the first case is private. **Never copy private transcript text, raw tool outputs, screenshots, local machine paths, credentials, tokens, user-identifying contents, or unpublished infrastructure details into this repository.** Publish only sanitized general lessons and public facts. For private-source audits, keep private evidence in the private source system; reference only review-safe summary IDs here.

Claims about current public product behavior need public sources or independent tests. When sources conflict, record the conflict and choose safe bounded language. Do not equate an install specification with proof of customer outcome.

## Reuse existing modules

- **Product documentation/brief and brand:** CGM content-context + brand-foundation.
- **README/product-entry copy:** CGM writing-direction.
- **Other prose:** CGM human-sounding-writing as routed.
- **Art/visual system:** CGM visual-direction and image-generation.
- **Demo/HTML:** CGM html-demo.
- **Media naming:** CGM human-output-naming.

Use the actual version selected by the target's pinned stack. This lab decides *what story deserves to be generated and how to reject a wrong one*. It must not override source-owned modules, release pin authorities, GitHub ownership, or human acceptance.

## Minimum deliverables on each new project

1. Completed Frame Brief (unknowns explicit).
2. Product Truth Map with ownership, mechanism, status, evidence and prerequisites.
3. Three alternative market positions, a reasoned recommended choice, and owner verdict.
4. A storyboard with scene-to-belief, scene-to-proof, visual role and forbidden implications.
5. Claims ledger and skeptical-reader review.
6. Decision delta for each meaningful correction.
7. Final QA report with distinct **technical validation** and **editorial acceptance**.

## Completion wording

Use four separate statements: **drafted**, **implemented**, **verified**, **editorially accepted**. If the last is unknown, it remains unknown. A deployed page can still be waiting for copy acceptance.

## Next safe step

If the current task is ambiguous but relevant to this lab, advance the earliest unresolved decision in EPISTEMIC_STATE without fabricating an answer. Present the owner a small set of competing grounded hypotheses rather than another full build.

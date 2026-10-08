# CGM HTML Demo — responsibility collision and proposed retirement

**Date:** 2026-10-08
**Status:** source review completed; deprecation **PROPOSED**, not executed.
**Privacy:** this is a PUBLIC-SAFE architectural synthesis. The compared app-builder repository is private; its implementation details and operational information are intentionally not reproduced here.
**Compared sources:** CGM `main` at `37ba626ea3064bde89352f00e99c659e85609c5b`; the dedicated app-builder repository at its reviewed current main snapshot (private source). Re-open exact current revisions before migrating.

## The question

The owner wants each CGM module independently reviewable and improvable, and suspects `html-demo` contradicts their dedicated app-building automation project. What is the actual collision, and should `html-demo` be retired?

## Findings — preserve distinctions

**OBSERVED, public CGM:** [`modules/html-demo/SKILL.md`](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/modules/html-demo/SKILL.md) is a short six-step instruction to turn the product story and brand guidance into responsive semantic HTML, test device widths, check keyboard/focus/alt text, and capture screenshots. It is NOT a substantial app-generation engine.

**OBSERVED, public CGM:** The module is declared in [`system-version.json`](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/system-version.json), advertised in [`README.md`](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/README.md), and enforced in the helper's validator and unit-test fixture module sets. Deleting only the skill file would break contracts.

**OBSERVED, private source reviewed under user direction:** The dedicated app-builder project owns frontend creation. Its contract specifies a code-generation pipeline, controlled project scaffold, design/plan before build, running application output, type/functional/browser checks, screenshots and owner acceptance. It separately recognizes that passing build checks does not prove design quality. It is under active development, and its present implementation does not yet fulfill every aspiration in its standing policy.

**OBSERVED, dependency boundary:** The app-builder project itself is currently a CGM adopter, and its pinned installation metadata lists `html-demo`. Deletion therefore requires a carefully versioned adapter/pin update rather than a blind file removal.

**INTERPRETATION:** No literal programming-language contradiction is present: React uses semantic HTML and can benefit from accessibility and responsive guidance. The conflict is **duplicate responsibility and potentially competing execution routes**. CGM says an agent can build a responsive HTML demo as a content skill; the app-building project says an agent must use its specialized generation machinery for frontend work. Both cannot be the canonical implementation authority for the same application deliverable.

The app-builder owns **how to build, run, and verify an interface**. A product/market framing router can own **what experience is needed and why**. CGM should not grow a parallel app builder.

## Proposed ownership map

| Concern | Authority | Reason |
| --- | --- | --- |
| Verified product purpose, target buyer, human job, positioning, narrative and claim limits | Product/experience framing router | Decisions before presentation technology |
| UX journey, tasks, information architecture, interaction states, service blueprint | Framing/UX design track, reviewed by product owner | Defines intended observable behavior |
| Exact accepted market/UX copy and art direction | Narrow writing/visual/media skills and owner/editor | Creative specification only |
| Choose implementation machinery, app framework, scaffold, code authoring, preview, build and repair loop | Dedicated app-building automation | Single source of frontend implementation |
| Functional tests, typecheck, browser behavior, responsive screenshot capture | App builder's evaluation machinery | Must inspect running artifact |
| Semantic claims and audience comprehension | Independent product/market/UX review | A technically working app can be strategically wrong |
| Final editorial/design acceptance and release authority | Authorized owner/reviewer | Not inferred from green scripts |

### What should survive from `html-demo`

- Understandable without animation, hover or wide layout.
- Semantic headings/controls, keyboard access, visible focus and useful alternative text.
- Responsive widths and rendered screenshot review.
- Link page section or component to the approved story and audience question.

These are **cross-cutting acceptance criteria**, not reasons to maintain a separate content-owned HTML generator. Relocate them into a concise, builder-consumed *experience acceptance contract* after comparing against the app builder's existing checks. Do not duplicate them blindly or turn them into another mandatory generic prompt.

## Proposed retirement path (not implemented)

1. **Decision:** owner explicitly marks `html-demo` as deprecated for frontend generation and assigns that responsibility to the dedicated builder.
2. **Audit usage:** search actual adopters, writing routes, hotload locks, tests and validators; identify who references the module and whether any product depends on its old behavior. The reviewed app-builder metadata already does.
3. **Preserve quality without duplication:** extract the minimal a11y/responsiveness/screenshot acceptance checklist, ideally as output requirements attached to the app builder's existing spec.
4. **Version CGM:** remove or deprecate `html-demo` in a controlled release; update `system-version.json`, `PROJECT.md`, `README.md`, `AGENTS.md`, validator expected module sets, test fixtures and migration notes. Never silently replace a pinned historical version.
5. **Upgrade consumers deliberately:** update version pins, hotload compatibility records and generated prompt/adapter metadata as part of authorized adopter work. Check no CI or install contract regressed.
6. **Verify responsibility in practice:** give a future fresh agent an approved product/UX brief and confirm it invokes the app-builder path for runnable interface production; it must not generate a standalone HTML substitute merely because CGM says it can.
7. **Record a negative fixture:** “CGM may write the brief, but must not bypass the approved app-building pipeline.” Retain source links and rejected shortcuts; avoid embedding private implementation details publicly.

## Narrow-module design standard — proposed

Every retained/new module should declare:
- **one purpose**, target actor/output and explicit non-goals;
- **activation predicate** (when it loads) and **do-not-activate** examples;
- **required inputs** and their authoritative owners;
- **small output contract** and dependencies, with concrete version/revision;
- **mechanical verification** separately from subjective reader/use validation;
- **compatibility owner** and deprecation route;
- **small epistemic message**: lessons, known false positives, decision boundaries, next action.

Modules should be reviewed and improved independently; failures should first be localized to the responsible layer. Do not grow a universal always-on prompt to prevent one rare failure.

## Caveats and decision state

**PROPOSED:** Retire `html-demo` as a separate generation/implementation module, preserve its UX/accessibility insights where not already owned, and make the dedicated app builder the single implementation authority.

**NOT DONE:** No files in CGM or the private app-builder project were changed; no versions/pins updated; no interfaces regenerated; no module deleted. This proposal requires owner approval and a compatibility plan.

**NOT PROVEN:** That `html-demo` alone caused the October 7–8 failure, or that the current app-builder implementation already satisfies all of its future stated design goals. Yesterday's failures include independently documented wrong framing and incomplete builder activation.

## Relevant public references

- [CGM HTML demo module](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/modules/html-demo/SKILL.md)
- [CGM version/module registry](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/system-version.json)
- [CGM module validator](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/scripts/validate_content_system.py)
- [CGM testing fixtures](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/tests/test_validate_content_system.py)
- [Full CGM capability audit](CGM_CAPABILITY_ARCHITECTURE_AUDIT_2026-10-08.md)

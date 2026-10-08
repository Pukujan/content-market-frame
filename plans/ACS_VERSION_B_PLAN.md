# ACS Version B — planning only, no site regeneration yet

**Status:** PROPOSED / not approved for implementation  
**Date:** 2026-10-08  
**Baseline A:** https://acs.design-bakery.com/  
**Working record:** [acs-version-b.run.json](../examples/acs-version-b.run.json)  
**Operating workflow:** [router/RUNBOOK.md](../router/RUNBOOK.md)

## Decision in force

The owner views the present ACS site as a **major improvement over rejected earlier versions**, but explicitly not final. Its current direction is valuable. The immediate job is to **make the judgment process repeatable**, not to run a new design experiment or regenerate the site.

**Do not modify/deploy/rebuild the current site as part of this plan.** No Version B work should begin as a generation run until the framing router has been reviewed and an alternative story approved. This plan merely defines the future design and comparison method.

## Why this is not simply “make A prettier”

The original failure was upstream: agent confusion about human stakes, misidentifying the product, treating a component as the whole proposition, overproducing research/audit prose, fabricating a vivid but irrelevant scene, then generating assets before a sound narrative existed.

B must improve **buyer understanding, emotional relevance, distinctiveness, and product credibility**. Stronger photography, more animation or a denser front page cannot by themselves cure an incorrect proposition.

Keep separate:
- The technical subject: integrated ACS install with source-owned ACS, PCM, OIO and CGM.
- The human subject: a person trying to keep meaningful work moving across agents, sessions, versions and review steps.
- The market subject: why that person should choose this product instead of manual coordination and other approaches.
- The visual subject: how a sequence of scenes demonstrates the human tension and the real product's answer.
- The UX subject: what a real preview and real install actually do, including partial/setup states.

## Phase 0 — first make the router stable (now)

**Artifacts:** machine router, run schema, validation/packet CLI, source and context protocol, negative regression fixtures, B draft record, and test instructions.

**Acceptance criteria:**
- A new agent can load one compact run record instead of the prior entire conversation.
- The router distinguishes implemented truth, desired marketing promise, and inferred audience needs.
- Positioning is a choice from alternatives, not the first catchy headline produced.
- Storyboard/visual generation cannot be treated as authorized by a machine's confidence.
- A rejected assumption can be invalidated without erasing why it was rejected.
- CGM remains source of implementation contracts; router does not fork CGM.
- Tests validate structural state, budget, citations/references, and approval fields; narrative taste remains reviewed by people.

This phase is implementation of the router, not an ACS website experiment.

## Phase 1 — capture Baseline A *before* any B creative comparison

**State:** NOT CAPTURED / no independent live browser audit in this project.

When a browser/capture environment is available, preserve:
1. Timestamp/URL and deployed source or exact artifact identifiers if obtainable.
2. Full-page desktop and narrow-mobile screenshots; page copy and section/navigation order.
3. Actual still/video assets, meaningful first/middle/last frames, and poster continuity.
4. CTA/button destinations and what demo actually does, with network/side-effect check.
5. Accessibility, mobile behavior and any known limitations.
6. Owner's qualitative assessment: substantial step forward, still open to improvement.
7. Claims and verification notes: what A says versus what current source and observed behavior warrant.

Do not equate A with a canonical gold standard. It is **a favored baseline** and may have flaws. Without a captured fixed revision, A-versus-B comparisons against a moving URL are unreliable.

Keep raw artifacts out of this public repo if they contain sensitive information. Record public-safe references and source hashes where possible.

## Phase 2 — choose which *human problem* B addresses first

**Do not assume the persona is proven.** Prepare two candidate buyer situations using truth-bound source information:

### Candidate 1: individual operator / solo builder
“I want to keep a long project moving with multiple agents, but I keep explaining, supervising and resetting the work around them.”

Emotional transition: from mental load and interrupted focus → shared working rules and continuity → attention on building.

Risk: can sound like a universal agent-memory product or underplay repo discipline and safety.

### Candidate 2: engineering/research team lead
“I need our work to remain understandable, coordinated and reviewable while several people and agents contribute over time.”

Emotional transition: from project fragility and coordination anxiety → reliable shared conventions and inspectable state → better collaboration.

Risk: enterprise-like language can turn the site back into process documentation, governance badges or an audit report.

**Output:** human situation map, objections, available evidence and recommended first segment. If no buyer research exists, preserve both as hypotheses.

## Phase 3 — develop competing B narratives on paper

A recommended set of substantially different angles, **not approved copy**:

| Angle | Draft thesis | Useful differentiation | Main risk |
| --- | --- | --- | --- |
| **A — Attention returned** | “Stop spending the first half of the work keeping the work organized.” | Starts from the unchosen human burden | Unsupported time quantification; generic productivity claim |
| **B — A project that survives sessions** | “The work should outlast every agent conversation.” | Clear visceral recognition | PCM-only scope collapse |
| **C — A shared way of working** | “A project needs more than agents that can write code.” | Reflects the breadth of the integrated install | Easy drift into abstract governance/jargon |

Select after comparing to actual human job, technical truth and current A. B's purpose is not to maximize difference from A; it is to produce a better-supported customer understanding.

**Owner gate:** choose a B audience, promise and exclusion list, and record why the other options lost.

## Phase 4 — scene planning and UX alignment

Create two non-interchangeable artifacts:

**Market belief storyboard**
- first-screen recognition and offer;
- tension of long-project overhead;
- product reveal as one integrated working surface;
- four-layer mechanisms translated into customer changes;
- honest evidence and limits;
- film/image roles tied to beliefs, not visual decoration;
- preview CTA with real behavior.

**Product UX task storyboard**
- evaluator understands what the demo previews;
- operator checks installation prerequisites and safety;
- user sees how a partial/incomplete setup is reported and recovered;
- returning contributor locates durable project state.

Both consume the same truth map. Product UX mapping is planning; do not claim that these interactions are verified today. Use service blueprint links to avoid website claims that installer behavior cannot fulfill.

**Owner gate:** approve narrative/visual direction and CTA semantics before the app builder or image/video generation is invoked.

## Phase 5 — generate B separately when authorized

Future implementation requirements (not a current instruction to build):
- Use the accepted B storyboard and current pinned CGM versions/routes; do not copy rejected page code by default.
- Create a separate immutable B branch/artifact and preview environment; keep A intact.
- Record image/video prompts, exact copy version, asset manifests, media text policy, crop and review.
- Source-specific truth/claim check, responsive and real-browser review, side effects, media-frame review, editorial acceptance.
- Do not publish to the A domain without explicit owner authorization.

## Phase 6 — compare A and B only after both are fixed

### Predeclared comparison dimensions

| Dimension | Main question | Evidence to collect |
| --- | --- | --- |
| **Human recognition** | Can a first-time reader articulate the lived problem? | Unaided interpretation, no coached jargon |
| **Product scope** | Do they understand the integrated install rather than only one layer? | Free-response explanation |
| **Persuasion/desire** | Does the offer seem worth exploring to the intended buyer? | Stated motive and strongest objection; not a proxy for actual purchase |
| **Narrative causality** | Does every scene advance a necessary belief? | Blind review of section order and logic |
| **Truthfulness** | Are claims, previews and limits consistent with implemented behavior? | Source/interaction checks |
| **Visual storytelling** | Do image/video scenes reinforce the intended meaning? | Pixel/frame review and reader recall |
| **CTA comprehension** | What action do visitors expect when clicking? | Unprompted expectation compared with observed behavior |
| **Accessibility and UX** | Can they navigate and perform the described tasks? | Task-based review and relevant accessibility checks |
| **Production cost** | Did the router save rework and context? | Rejection causes, revisions, wasted assets; record actual effort, not invented estimates |

### Fair comparison rules

- Keep product source truth and permitted evidence at comparable revisions, or document changes.
- Avoid rewriting A only to make B appear better.
- Blind reviewers should not be told B is the newer version or which is preferred.
- Distinguish editorial preference from user comprehension, real task success and conversion; no invented metrics.
- If B is stronger visually but worse in human recognition or product truth, do not automatically promote it.
- Maintain a qualitative decision log even if numerical scoring is later introduced.

## Open decisions

1. Who is the lead visitor for B: individual multi-agent builder, engineering lead, or another documented persona?
2. Which elements of A are locked because they embody hard-won correction, and which are intentionally open for improvement?
3. What is the full current set of production capabilities/conditions at a frozen ACS source revision?
4. Which page/asset capture mechanism will preserve A with proof of its actual current behavior?
5. Is the desired B primarily a stronger market narrative, a better demo/user interaction, or both?

These questions should be resolved through the router's stages, rather than one giant briefing request.

## Single next action

**Review and stabilize the router**, using its structural tests and this draft as a first source-limited handoff. When the router's contract is acceptable, capture Baseline A. Only then develop and accept B's problem/positioning/storyboard. No new website is authorized by this document.

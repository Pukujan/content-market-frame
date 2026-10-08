# Framework — source truth to human story to sales experience

**Version:** 0.1 (experimental)  
**Objective:** make *creative framing decisions* inspectable and reusable. This runbook is upstream of copywriting, website generation and asset generation. It does not replace CGM, and it does not authorize automatic publication.

## The problem with a conventional multi-agent pipeline

“Research → write → generate images → build → run checks” starts too late. A perfectly completed sequence can carry a wrong assumption all the way through: the wrong customer, an over-narrow understanding of the product, false causal evidence, an invented vignette, and a beautiful site that sells the wrong benefit.

Instead, the pipeline needs **semantic gates** before expensive work. Agent roles are useful only when they are constrained by what each may decide and what evidence they must hand off.

## Process map

~~~text
SOURCE REPOSITORY + USER DIRECTION + AUDIENCE EVIDENCE
            |
   0. Product-truth excavation
       [ownership vs installed bundle vs promise vs boundary]
            |  TRUTH LOCK
   1. Human situation / jobs-to-be-done
       [trigger / recurring pain / stakes / workarounds / desired change]
            |  HUMAN RECOGNITION GATE
   2. Market thesis and positioning
       [alternatives / urgency / objections / category / distinctiveness]
            |  POSITIONING CHOICE
   3. Three competing story spines
       [protagonist / tension / cost / mechanism / outcome / action]
            |  NARRATIVE APPROVAL
   4. Scene-by-scene storyboard
       [onscreen copy / visual action / proof / motion / CTA]
            |  STORYBOARD LOCK
   5. CGM writing, visual, image and HTML briefs
       [approved artifacts are input, not inspiration]
            |  ASSET / RENDER REVIEW
   6. Real page + demo + mobile + claim tests
       [deterministic + adversarial + skeptical-buyer]
            |  EDITORIAL ACCEPTANCE
   7. Publish only after authorized sign-off
            |
   8. Save failure case and decision delta for next product
~~~

**Do not run stages 4–6 from the same unapproved speculative prompt.** Draft alternatives at stages 2–3; run production only after selecting the story.

## Stage 0 — product-truth excavation

**Question:** What is actually implemented or contractually specified? Which repo *owns* each capability? What does the user install? What needs prerequisites, permissions or configuration?

Read, in priority order:
1. Authorized user direction on desired positioning. Treat it as an intended message, not evidence that the functionality exists.
2. Current normative product contract, versioned install spec, installer flags, acceptance tests, recorded limitations.
3. Module ownership boundaries and upstream dependencies.
4. Shipped demo behavior and observed adopter evidence where available.
5. README and prior marketing copy, **as leads**, never as substitute authorities.
6. External sources only when needed to test a factual claim, market hypothesis or competitor alternative.

Output a **Product Truth Map**:

| Customer-facing result | Mechanism / owner | Shipped / specified / proposed | Required conditions | Source/revision | Allowed public claim |
| --- | --- | --- | --- | --- | --- |
| e.g. retain project state | PCM | contract; inspect exact adopter | versioned state and updates | canonical spec | “state remains in repo” subject to conditions |

Every row has an epistemic status. If two documents disagree, record both and **block the stronger claim** until reconciled. Do not infer that a module is effective just because it is listed. Distinguish “installer attempts to wire X,” “validator checks X,” “a demo simulates X,” and “a customer obtained Y.”

**Hard gate:** no marketing copy for an ambiguous/unshipped central capability.

## Stage 1 — reconstruct the human situation

The human story is not a taxonomy of bugs. Capture:
- **Actor:** user, decision-maker, buyer, teammate, new contributor, or evaluator; distinguish roles.
- **Trigger:** what event makes them seek help *now*?
- **Job:** what meaningful outcome are they trying to achieve?
- **Existing workaround:** what do they manually explain, monitor, reconcile or redo?
- **Friction:** time, risk, cognitive load, broken trust, loss of momentum; label assumptions.
- **Consequence:** what gets delayed, repeated, abandoned or made fragile?
- **Transformation:** how their behavior can change after the mechanism exists.
- **Proof of recognition:** owner anecdotes or actual customer utterances, clearly sourced. Never masquerade synthetic personas as interviewed customers.

Write three **moment-of-recognition sentences** in customer language without naming the product or any module. Write three **outcome sentences** without mechanisms or jargon. Example:
- Moment: “When I reopen a project, the first thing I do is tell the agent everything we already decided.”
- Outcome: “The next session can begin with the work, not another orientation.”

Then cover the product's full problem range in a **coverage matrix**. A main story may foreground one pain, but it must not misrepresent the bundle as just one component.

**Human recognition gate:** a first-time reader can describe the situation, cost, and desired change without learning the system's vocabulary.

## Stage 2 — market and sales positioning

Decide:
- **Target segment:** not “everyone with AI”; specify role, context, team shape and maturity as a hypothesis.
- **Trigger and alternative:** what are they already doing instead (manual prompts, internal scripts, ticket discipline, coordination by chat, competing products, doing nothing)?
- **Category:** the smallest understandable buying shelf, not an invented grandiose label.
- **Angle:** one differentiated promise anchored in product truth.
- **Objections:** “Will it touch my repo?”, “Is the demo real?”, “What must I configure?”, “Will agents obey?”, “Does it work with my tooling?”
- **CTA:** matched to product maturity—preview, local try, docs, or contact. Do not over-promise one-click hosted functionality if setup is local and conditional.
- **Proof budget:** strongest one or two directly relevant facts; optional supporting proof; detailed citations off the selling surface.

Write **three competing positioning options** with:
1. Proposed one-sentence hero;
2. Audience/trigger;
3. Why that angle fits product scope;
4. Strongest evidence;
5. What it leaves out;
6. Biggest risk of being misleading;
7. Demo/CTA fit.

Run a **falsification review**, not a taste vote. Reject any option that wins on memorability but fails scope, claims or audience recognition.

**Positioning gate:** the selected thesis states a human change, the product mechanism that makes it plausible, and an attainable action.

## Stage 3 — choose a story spine

A **story spine** is a causal argument; it is not page structure or a list of section labels.

~~~text
PERSON: I am trying to accomplish meaningful work.
FRACTURE: Repeated invisible maintenance steals attention and confidence.
ESCALATION: More projects/sessions/agents compound the friction.
INSIGHT: The missing layer is a shared, durable way of working.
PROMISE: One integrated installation writes that layer into the repo.
MECHANISM: Four source-owned components address different parts.
REASSURANCE: Inspect a bounded, truthful preview before adopting.
ACTION: Take one next step appropriate to the real product.
~~~

For every beat record:
- What **new belief** should the buyer hold after it?
- Why is that belief necessary before the next beat?
- Which real customer situation makes it recognizable?
- Which source permits the claim?
- What should the person **feel**, without requiring manipulative copy?
- What evidence or visual could advance that belief better than another paragraph?

**Narrative gate:** removing a section should break a meaningful causal link, not merely shorten a document.

## Stage 4 — storyboard as the binding creative contract

A storyboard is not just thumbnail art. It is a sequence of **belief changes with designed visual evidence**.

Every beat requires:
- **Viewer's question** and the answer delivered by this scene;
- **On-page promise**, at most one main idea;
- **Human moment** and proof level (real, illustrative, hypothetical, or product UI);
- **Visual composition** (what is in the frame and what deliberately is not);
- **Motion rule** (if video; action starts/ends in consistent states);
- **Text policy** (no embedded copy unless locked; exact strings if text is part of the media);
- **Interaction/CTA** and what it actually does;
- **Sources + disallowed implications**;
- **Mobile adaptation**;
- **Reviewer verdict**.

Storyboard the **reader's questions**, not rubric categories. A heading such as “The problem” describes a writer's outline. “You lose the project every time the session ends” expresses a visitor's lived tension. Use such examples only if they accurately represent the chosen scope.

The storyboard lock freezes central promise, section order, accepted copy (if any), required/forbidden terms, illustrative-vs-factual labels, hero visual, demo behavior and conversion action. Changes after lock create a new version and invalidate downstream assets.

## Stage 5 — orchestrate existing CGM instead of building a parallel engine

Use [CGM](https://github.com/Pukujan/content-generation-modules) with an explicit handoff:
- **brand-foundation:** receives selected audience, voice boundaries, differentiated promise, forbidden unsupported claims;
- **content-context:** receives Product Truth Map and source revisions, not guesses;
- **writing-direction / HSW:** receive approved story spine and exact page-stage copy boundaries;
- **visual-direction:** receives scene cards, emotional arc, visual grammar, motion rules and rejection examples;
- **image-generation:** receives per-shot approved briefs plus asset manifest records;
- **html-demo:** receives storyboard beats, real demo safety model, CTAs and interaction rules;
- **human-output-naming:** names files without opaque machine labels.

The app builder gets only the **approved story contract**, not old rejected code or all brainstorm drafts. Research agent material is annexed; it must not be allowed to overwrite page copy.

## Stage 6 — review in the browser, not just in the repository

Run [QA_GATES](QA_GATES.md). Mechanically validate routes, exact visible strings, facts, source URLs, prohibited copy, no invented customer counts, responsive behavior, demo network/mutations, media types, poster-to-video continuity, image-embedded text, and final CTA destinations. Then perform a **separate editorial inspection**: who is the protagonist, what does the first screen promise, does every section advance a sale, can a skeptic articulate the differentiation, and does the demo support rather than contradict the offer?

Pass records need a real reviewer, observed result, source revision and explicit status. “Build succeeded” cannot auto-set “copy approved.”

## Agent router — roles and allowed decisions

| Role | May do | Must produce | Cannot do |
| --- | --- | --- | --- |
| **Truth excavator** | Inspect contracts, code, versions, tests, contradictions | Product Truth Map with status/source | Invent use cases or declare adoption success |
| **Human interpreter** | Map actors, triggers, workarounds, emotions, JTBD | Human situation brief and uncertainty list | Infer customer interviews |
| **Market researcher** | Compare alternatives and verify specific market claims | Evidence fit table and objections | Fill a page with unfiltered statistics |
| **Positioning strategist** | Offer three commercial angles and risks | Positioning options + recommendation | Alter product truth |
| **Narrative director** | Propose causal story and buyer-belief progression | Story spine and scene cards | Start implementation before acceptance |
| **Visual director** | Map each beat to imagery, film and design system | Asset briefs, shot list, rejected references | Reintroduce rejected narrative through pixels |
| **Skeptical buyer / red team** | Try to misread copy, identify implausible leaps | Semantic failure report with specific evidence | Rubber-stamp because requirements were followed |
| **Claim verifier** | Check exact links, study population, causal limits and product evidence | Publishable claim ledger | Re-label third-party figures as product results |
| **Builder** | Implement exact accepted story and asset contract | Reproducible rendered output | Improvise new headline/CTA/problem framing |
| **Owner/editor** | Accept or reject target persona, promise, story and visual direction | Explicit accept/cut decisions | Be replaced by a model confidence score |

These may be independent agents or phases in one agent's run, but review and creation should not share the same unchecked assumptions. Use a single integrating editor to resolve conflicts, and maintain one canonical set of accepted decisions.

## Iteration protocol — make corrections compound

When the owner says “wrong problem” or “this reads like an audit log,” **do not merely rewrite the paragraph**. Produce a decision delta:

~~~text
Correction ID:
Original assumption:
Evidence that exposed it:
New interpretation:
Affected assets: hero / problem / proof / layers / nav / video / demo / CTA
Invariant truths that must remain:
Rejected patterns added:
Open questions:
Approval status:
~~~

Re-run all earlier semantic gates affected by the delta. Never carry “accepted” from version N to version N+1 if the subject or promise changed.

## Minimal handoff contract between stages

No role should receive a huge undifferentiated chat dump. Pass:
1. One-page accepted decision summary;
2. Source-backed product scope, limitations, and audience evidence;
3. Exact story spine and scene IDs;
4. Claims with their status and allowed language;
5. Explicit rejected alternatives plus why;
6. Current open questions, approval status, and version;
7. Exact deliverable format and stopping condition.

This is the actual portable memory: **constraints, causal decisions, and source links**, not the volume of research.

## Evaluation of repeatability

Run this process on ACS first, then at least three unlike repositories. Collect:
- Number of owner corrections **before** and **after** story lock;
- Whether reviewers correctly identify **audience, main problem, promise, mechanism, limitations and CTA** after seeing only the page;
- Number/severity of unsupported claims, wrong-scope headlines, false illustrative cases, stale visual copy, and CTA misrepresentation;
- Revision cost in rendered pages and discarded assets;
- Owner acceptance/rejection, with qualitative explanation.

These are proposed metrics for experiments—not claimed improvements. If a new pipeline merely achieves higher generic writing scores but still requires the owner to repeatedly correct the central problem, it has not solved this task.

## Shipping rule

**First understand; then position; then tell a story; then design; then implement; then validate; then ask for editorial acceptance.** Never optimize a page whose commercial premise has not been chosen.

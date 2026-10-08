# Research: UX and Product Design Framing

**Research date:** 2026-10-08
**Status:** Externally grounded methods; proposed synthesis, not owner-approved or tested.
**Question:** Is our human-problem/storyboard process a recognized design approach, and what is missing for UX and product design?

## Executive conclusion

Yes, the components are established methods: human-centered design, Double Diamond, Jobs to Be Done, value proposition design, continuous product discovery, journey mapping, UX storyboarding, service blueprinting, content design and usability testing. There is **no evidence that our exact agent-routing synthesis is a named, validated standard**. The distinctive proposal is coordinating these disciplines across AI agents while preserving truthful product claims and upstream creative decisions.

The current framework is strongest at **product-truth → human-problem hypothesis → positioning → marketing narrative → visual storyboard → verification**. It is weaker on actual **tasks, information architecture, interaction states, onboarding, failure recovery, longitudinal use and observed usability**.

**UX must not be deferred until after marketing.** Human/user research shapes both the product problem and the market story; after positioning, product interaction design proceeds as a linked but separate workstream.

## Primary-method research

| Source | Established method | Why it matters here |
| --- | --- | --- |
| [Design Council: Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/) and [Framework](https://www.designcouncil.org.uk/resources/framework-for-innovation/) | Discover, Define, Develop, Deliver; deliberate divergence and convergence; iterative problem framing | Avoid constructing the polished solution while the original human problem is untested |
| [IDEO: Design Thinking](https://designthinking.ideo.com/introduction) | Balance desirability for people, feasibility in technology, and business viability | Our truth work concerns feasibility; the human and market sides still need genuine desirability and viability evidence |
| [Christensen et al.: Jobs to Be Done](https://store.hbr.org/product/know-your-customers-jobs-to-be-done/R1609D) | Understand the progress customers hire products to make | A person wants to keep a project moving, not acquire a boss lease or an issue ontology |
| [Strategyzer: Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas) | Connect customer jobs, pains, gains to offerings and value creators; test fit | Explicit bridge from repo mechanisms to customer experience; fit remains a hypothesis |
| [Teresa Torres: Opportunity Solution Tree](https://www.producttalk.org/opportunity-solution-trees/) | Business outcome → customer opportunities → possible solutions → assumption tests | Agents must not jump directly from a module's features to a product headline |
| [NN/g: UX Storyboards](https://www.nngroup.com/articles/storyboards-visualize-ideas/) | Visual sequence of a user scenario, actions and context, with captions | Our marketing belief storyboard is *not* the same as a user's interaction storyboard |
| [NN/g: Journey Mapping 101](https://www.nngroup.com/articles/journey-mapping-101/) | Actor, scenario, journey phases, actions, mindsets, emotions, opportunities | Map buyer/evaluator separately from the actual installing/returning operator |
| [NN/g: Service Blueprints](https://www.nngroup.com/articles/service-blueprints-definition/) | Link visible user touchpoints to backstage people, processes and technical systems | Connect the page's promises to ACS, PCM, OIO, CGM and their real prerequisites/states |
| [SVPG: Four Big Risks](https://www.svpg.com/four-big-risks/) | Value, usability, feasibility, business viability must all be addressed | Passing build/claim checks is not proof users will choose or use the product |
| [GOV.UK: User needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) | Start with real people, goals, workarounds and contextual research; label assumptions | Owner intuition is valuable direction but not independent customer discovery |
| [NN/g: Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/) and [task scenarios](https://www.nngroup.com/articles/task-scenarios-usability-testing/) | Watch representative people attempt realistic tasks without coaching | Test whether users understand preview, install, partial failure, and safe next steps |
| [NN/g: Content Strategy vs UX Writing](https://www.nngroup.com/articles/content-strategy-vs-ux-writing/) | Content governance and interaction microcopy are related but distinct | Sales headline and installer error copy should be reviewed against different goals |
| [NN/g: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) and [W3C WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/) | User-language, visible states, error prevention, accessible interactions | Design user control, feedback and safe behavior rather than just polish |

### Interpretive caution

These references establish what the external methods say, not that our hybrid process works better than standard practice or that ACS currently satisfies UX requirements. The live ACS URL was not accessible for independent inspection during this research. All website-specific judgments below are **hypotheses or task recommendations**, not new observed defects.

## Three distinct stories that must align

### A. The marketing / buyer BELIEF journey

Question: What sequence of information helps the visitor recognize the problem, trust the promise, understand differentiation and choose a next step?

Deliverables: positioning, page content hierarchy, message sequence, emotional tension, demonstration promise, honest proof, visuals and CTA.

The existing ten-scene ACS storyboard mainly does this. Its scenes explain *belief changes*, not the product user's physical/functional task steps. It is a legitimate marketing-design adaptation, but should not be presented as a complete UX storyboard.

### B. The product EXPERIENCE / task journey

Question: What does someone do to accomplish the job, including uncertainty, mistakes, setup and recovery?

Deliverables: actor and scenario, current workflow, journey map, task flow, information architecture, interaction/state diagram, wireframes, error/empty/partial states, usability tests and accessibility criteria.

Example proposed operator flow (not verified deployed behavior):
- Identify correct repository and prerequisites.
- Understand what a preview will/won't do.
- Inspect expected changes.
- Invoke actual local installer under real documented conditions.
- Interpret READY or PARTIAL without false success.
- Recover from missing dependency or failed validation.
- Return in another session and locate authoritative work.

If the story promises “pick up where you left off,” the UX work must examine what the returning person actually sees and does, rather than only animating a session handoff on the landing page.

### C. The SERVICE / backstage journey

Question: Which actual software modules and humans fulfill each visible experience, and which states or limitations break the promise?

Deliverable: service blueprint connecting each touchpoint to real source authority, data/state, system action, error handling, recovery, and ownership.

For example:

| Visible user experience | Backstage reality to trace | Gate |
| --- | --- | --- |
| “Preview an install” | Is this a read-only simulation or a real repository operation? | CTA label and network activity must match |
| “Install the full pack” | Actual installer, external checkouts, pins and adapter prerequisites | Explain conditions; never say all platforms or repos are instantly READY |
| “Partial installation” | ACS/OIO installation and validation state | Clear cause, next safe action, retry/recovery |
| “Next session continues” | PCM project records/issues/versioned state | Test actual continuity workflow with a user; no universal-memory implication |
| “Readable, checkable writing” | CGM rules plus editorial review | Validation is not proof of buyer comprehension |

## What the current framework covers and misses

| Area | Existing status | UX/product-design extension |
| --- | --- | --- |
| Product truth | Strong initial design | Map facts to observable interaction states |
| Human problem | Owner-centered, provisional | Customer interviews/observation, distinct user and buyer actors |
| Market framing | Explicit | Keep; buyer validation and viability research |
| Marketing storyboard | Explicit | Rename **belief storyboard** to avoid confusion |
| User journey | Partial/implicit | Separate evaluator, adopter and returning-contributor journeys |
| User task flows / IA | Missing | Add task/state/navigation diagrams before building interface |
| Preview/install/repair experience | Mostly claim and QA checks | Design errors, partial states, confirmations, retry and safe exits |
| Service blueprint | Absent | Link visible promises to actual sources/operations |
| Usability research | Mostly simulated skeptical reader | Observe representative people performing uncoached tasks |
| Accessibility | Broad visual checks | Add WCAG-based review across controls, media, keyboard and error feedback |
| Business value/viability | Broad hypothesis | Explicit acquisition/adoption/business constraints and evidence |
| Long-term outcome | Story promise | Test in a resumed session and record result limits |

## Proposed operating model: two linked design tracks

1. **Shared discovery:** product truth, actual user research, JTBD, opportunity map, separate buyer/user jobs, risks and evidence.
2. **Shared definition:** chosen human problem, commercial value proposition, feasible mechanism, real next action and success criteria.
3. **Commercial track:** buyer journey → marketing belief storyboard → content hierarchy → visual/film brief → content-comprehension tests.
4. **Product track:** actual user journey → task flows → IA → interaction/state storyboard → prototype → usability and accessibility tests.
5. **Link with service blueprint:** every important promise, CTA and UI state maps to an operational truth, authority and verification path.
6. **Iterative testing:** misunderstanding in use may invalidate the marketing promise, and new customer evidence may invalidate both tracks. Do not use a one-way handoff.

The tracks are *not* isolated or strictly linear. Run targeted discovery as uncertainties arise. The goal is to keep the story about what people need and the experience about how they actually achieve it.

## New proposed UX and product gates

- **U0 — Customer/desirability evidence:** Is the main problem observed in actual potential users? What are they trying to accomplish now? Assumptions clearly marked.
- **U1 — Mental model and information architecture:** Can people tell preview from install, specified vs tested behavior, READY from PARTIAL, and find requirements without knowing internal acronyms?
- **U2 — Task and state coverage:** Are important default, loading, permission, validation, partial, error, cancellation, retry, success and recovery states designed? Are actions reversible when appropriate?
- **U3 — Observational usability:** Can representative participants complete realistic tasks without directions that reveal the answer? Record breakdowns and task outcomes, not merely preference ratings.
- **U4 — Accessibility:** Does the interaction satisfy relevant WCAG 2.2 criteria and diverse assistive-technology needs? Do media, errors, controls and focus states work?
- **U5 — Cross-touchpoint truth:** Do marketing promises, preview interactions, actual installer, and long-term usage match when followed end-to-end?
- **U6 — Value and viability:** Is there evidence someone wants the outcome enough to adopt, buy or maintain the required workflow? Identify buyer/adopter distinction and costs.

These are **proposed** gates. Do not imply the current page failed them without live inspection or actual user test evidence.

## Concrete first ACS experiments

**Evaluator task:** “Using the site alone, work out whether the preview writes to a repository and what you'd need to do for a real installation.” Observe whether a prospect can explain it accurately without hints.

**Operator task:** “The install reports PARTIAL. Determine what's missing and the next safe step.” Inspect whether the product/documentation makes the answer discoverable.

**Returning-contributor task:** “Reopen this project after a gap and resume the correct pending work without re-explaining accepted decisions.” This must run on a controlled test project with actual installed mechanisms, not a film.

For each task, collect: actor, starting state, desired outcome, observed path, misconceptions, error/recovery outcomes, source version, and next design correction.

## Recommendation and naming

Keep the current repository as a **human-centered product-to-market framing lab**, not a complete replacement for established UX/product tooling.

Describe the method as a **proposed synthesis** of product discovery + human-centered design + marketing narrative + UX/service mapping + evidence/QA. This is not itself a universally recognized named framework. The distinctive question is whether the agent handoffs and falsification gates can make existing good practice repeatable without removing human judgment.

**Next decision for owner:** Add separate **buyer-belief storyboard** and **operator-task UX storyboard** artifacts, both sourced from one verified human-problem brief. Only promote to a permanent standard after testing on ACS and other unlike products.

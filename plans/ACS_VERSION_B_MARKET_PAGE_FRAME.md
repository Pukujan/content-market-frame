# ACS market-facing website — Version B framing candidate

**Status:** Individual-builder audience owner-selected ([decision #1](https://github.com/Pukujan/content-market-frame/issues/1)); headline, promise, CTA, scenes and all build gates remain PROPOSED.
**Prepared:** 2026-10-08.
**Source of truth:** [ACS repository at 264117398e7754d7e91076481cd664b5e197c1d4](https://github.com/Pukujan/agent-custom-setup/tree/264117398e7754d7e91076481cd664b5e197c1d4); specifically [PROJECT.md](https://github.com/Pukujan/agent-custom-setup/blob/264117398e7754d7e91076481cd664b5e197c1d4/PROJECT.md) and [multi-agent hotload README](https://github.com/Pukujan/agent-custom-setup/blob/264117398e7754d7e91076481cd664b5e197c1d4/modules/coordination/multi-agent-hotload/v0.1.0/README.md).
**Baseline A:** https://acs.design-bakery.com/ — owner-favored but not final; live visual/browser capture **not independently obtained**, so no pixel/section comparison with A is asserted.
**Version B:** isolated design/candidate, not a replacement for A until approved and evaluated.

## Owner clarification — product introduction comes first

**APPROVED PURPOSE, not approved copy/order:** The owner clarified that Version B primarily **introduces ACS quickly**. It should give a visitor a short product explanation and recognizable human situation, then connect problem, market meaning, product solution, commercial relevance, defensible evidence and technical depth. See [owner decision record](https://github.com/Pukujan/content-market-frame/issues/1#issuecomment-6072629118).

**Recommended information hierarchy (PROPOSED):**

1. **First screen:** Product name, category, individual-builder audience and intended benefit, plus a representative working-surface example. Give an immediate *what is it / who is it for / why care* answer, not only a clever pain-point slogan.
2. **Relatable problem:** A succinct account of the coordination burden; avoid an extended essay that delays introducing ACS.
3. **Solution:** Connect the product's distinct mechanisms to the human job. Clearly attribute ACS coordination, PCM continuity/governance, OIO issue recording and CGM content guidance.
4. **Representative experience:** One believable scenario of a real project across sessions, grounded in product mechanics. Do not fabricate installed runtime screenshots or customer testimonials.
5. **Proof as encountered:** Evidence beside each significant claim. The documented mechanism is source evidence, **not independent evidence of buyer need or measured productivity**. No fake research backing.
6. **Evaluate and go deeper:** Installation prerequisites, compatibility, PARTIAL/READY behavior, limits, and access to technical contracts; use progressive disclosure, not a wall of implementation text.
7. **Next action:** CTA's exact intent, wording and click effect remain **Q3 unresolved**. Do not invent a preview, setup link or live install.

**Important categories that are mainly backstage:** “market framing” guides who/why/alternatives and the entire sequence; it is not a section titled Market Framing. “Sales opportunity” is the eventual conversion intention supported by clear value/proof, not an overt standalone hard-sell paragraph. “Research backing” is a truthful evidence standard; show only real user studies when they exist. Technical reference depth belongs in appropriate drilldowns, while essential constraints appear before any consequential user action.

**External UX references:** [NN/g homepage design principles (2024)](https://www.nngroup.com/articles/homepage-design-principles/), [NN/g progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/), [GOV.UK writing for interfaces](https://www.gov.uk/service-manual/design/writing-for-user-interfaces). This is recommended practice tailored to ACS, **not** an immutable sequence approved by the owner or independent ACS buyer-comprehension evidence.

## Product facts, not marketing invention

- ACS itself owns **multi-agent execution coordination**: live join-order roles, boss lease and FIFO failover, task claim queue, agent-less watchdog, and proposal → acceptance → PR discipline.
- The **marketed installation** is the **multi-agent hotload pack**: a repo-installed wiring of ACS runtime with pinned PCM continuity/PR governance, OIO issue records, and CGM content/writing/visual contracts. Distinguish pack breadth from narrow ACS module ownership. Do not imply ACS authored or vendors those sibling systems.
- The product is not a hosted service, omniscient agent or autonomous decision-maker. The setup has prerequisites and may fail closed/return PARTIAL; it is not a one-click browser installation.
- Product documentation is verified to the pinned repository *as written*. Current compatibility and live behavior on a fresh consumer repo must still be tested before claims such as “works anywhere” or “installs in one click.”
- CGM HTML generation is being reconsidered separately; this future website should use ABA as frontend implementation owner and not claim PEF or new CGM decisions have already shipped in ACS.

## Human-job working hypothesis (not validated by external user research)

**Owner-selected lead audience:** A technically capable independent builder or project operator running multiple AI agents on a real repository over many sessions. Their actual project competes with a recurring *second job*: assign work, stop overlap, reassemble context, track decisions/issue history, check approvals and turn output into something another person can follow.

**Observed user behavior:** UNKNOWN; no interviewed adopter quoted. The owner can select this as the lead intended audience without converting it into observed buyer data.

**Secondary audience:** An engineering lead whose central need is team-level shared accountability. Do not promote this to the lead over the owner's chosen individual builder.

**Desired human progression:** From “I am managing the agents more than the work” to “the repository has explicit working rules; I can inspect what will be installed and decide deliberately.”

## Three positioning candidates — all PROPOSED

| Position | What it leads with | Benefit | Risk |
| --- | --- | --- | --- |
| **B1 — Less agent babysitting** *(working recommendation)* | “Build with agents. Stop managing every handoff.” | Very recognizable human cost and emotional promise | Sounds like guaranteed autonomy if implementation limits disappear |
| **B2 — The work needs a home** | “Your project needs more than a chat history.” | Durable project structure; visualizable | Can mis-sell PCM alone |
| **B3 — Several agents. One way of working.** | “Your coding agents should share the same rules.” | Concrete technical buyer relevance | Too coordination-only; may underplay continuity, issue provenance, and human output |

**No angle is accepted.** B1 is a suggested opening for an owner decision, not market-tested copy or authorization to build.

## Proposed Version B first-screen copy (editable)

> **Build with agents. Stop managing every handoff.**
>
> ACS is a repository-installed working arrangement for AI agents. It connects coordination with pinned continuity, issue records and content guidance so the builder can spend more attention on the actual project instead of continually rebuilding handoffs. The intended attention benefit is not a measured outcome.
>
> **Primary action candidate:** Explore what gets installed (a read-only product explanation; actual click behavior to be verified).
>
> **Secondary action:** Read the install requirements (navigate to a source-pinned public setup page).

Copy is intentionally qualitative: it does **not** assert measured time saved, proven customer success, universal compatibility or fully automated end-to-end project management.

## Proposed page architecture — seven buyer beliefs

| Scene | Visitor's question | What B must establish | Visual/UX job |
| --- | --- | --- | --- |
| **B01 — Product introduction + recognition** | “What is ACS, and why might it matter to me?” | Immediately identify the repo-installed product, individual builder and qualitative benefit | First screen pairs real product category with relatable work; do not wait until B03 to reveal the product |
| **B02 — The recurring extra job** | “What exactly is painful?” | Context reconstruction, role collisions, issue provenance, review and readable outcomes compete with making progress | One continuous project journey, 3 grouped moments; avoid an overwhelming 7-feature matrix |
| **B03 — Mechanism explained** | “How does this work in my repository?” | Expand on the already named repo-installed arrangement, not a first product reveal | Source-linked repo-centered mechanism diagram, visibly conceptual if not a verified screenshot |
| **B04 — Four linked capabilities** | “How is this more than a coordinator?” | ACS role/claim/proposals + PCM continuity/governance + OIO issue/provenance + CGM content/visual rules | Four connected functions expressed as outcomes and properly attributed; optional inspect mechanics |
| **B05 — A credible workflow** | “What happens when I start?” | Preconditions → install/configure → inspect READY or PARTIAL → continue working | Experience/task flow grounded in source; no pretending a no-write illustration performs installation |
| **B06 — Proof and boundaries** | “Why should I believe this?” | Explain source-backed mechanisms versus unvalidated buyer outcomes, plus prerequisites and human limits | Place evidence beside relevant claims, link deeper technical sources, no hero audit table |
| **B07 — Next action unresolved** | “What should I do next?” | Its exact purpose and real behavior must follow the owner's Q3 clarification | Leave CTA purpose, UI, destination and side effects as unapproved; do not silently add a tour or install link |

### Visual style proposed for B

A refined, editorial product experience. Lead with large, readable human proposition and a single concrete view of “a project with multiple agents and durable operating rules.” Use product-like diagrams and one scenario tied to actual repo tasks, with restrained motion showing a person returning to a project. Avoid faux command terminals, agent avatars as the emotional protagonist, abstract glowing AI or fabricated performance metrics.

Mobile-first decisions: every scene understandable without animation, no embedded copy in generated image assets, real HTML text for changing claims, accessible motion reductions and keyboard interaction. Exact visual identity is provisional and should be informed by an actual A capture before final lock.

## Product UX and service design, linked but not merged with marketing story

**Potential interaction task T1 (candidate, not verified):** Visitor inspects what the hotloader would configure. Success: distinguish example/read-only preview from a real local installation and locate verified prerequisites.

**Potential interaction task T2:** Visitor checks a PARTIAL/incomplete scenario and learns what to verify and repair. Success: no green READY or implied successful write when the required parts are absent.

**Service trace:**
- Website “Explore what gets installed” → client-side explanatory view only; must not invoke installation or write to a target repo.
- “Read the install requirements” → direct source-pinned installation instructions.
- Real installation happens separately in an authorized local/working-repo context; the website must not manufacture install receipts.

All source/backend states require checking against actual supported script behavior before building a realistic interactive demo.

## Two stage-specific owner decisions, not a full discovery interview

**Q1 — Lead visitor (ANSWERED):** Owner explicitly selected the individual long-project builder and repeated agent handoff burden, recorded in [issue #1](https://github.com/Pukujan/content-market-frame/issues/1). This approves the intended lead audience, **not** B1's exact headline or promise.

**Q2 — Main promised benefit (OPEN):** Lead with **returning attention to the actual project work** (recommended, qualitative intended benefit), **durable context across sessions** (risks PCM-only scope), or a correction.

**Q3 — Safe primary CTA (OPEN):** Prefer **read-only walkthrough of the setup** (with explicit explanatory label; recommended) or **link to pinned installation instructions**? No real setup action from an untrusted browser without separate technical verification.

Avoid asking the owner to decide palettes, component types or exact wording before the strategic human story is accepted. The agent can prepare those options autonomously.

## Draft PEF Experience Brief (not production-authorized)

The [source-pinned ACS B Experience Brief](../examples/acs-version-b.experience.draft.json) is a typed design artifact with seven buyer-belief scenes, two provisional visitor tasks, service/CTA trace, four narrowly source-grounded mechanism claims and acceptance tests. Its intended actor reflects Q1; user need is an **owner hypothesis**, not observed research.

**Its review is DRAFT; proposed read-only CTA behavior is NOT VERIFIED.** Q2 benefit promise and Q3 CTA remain blocking. The compiler must refuse the draft until S3/S4/S5 approvals and actual link/CTA verification. Version A remains untouched.

## ABA handoff restrictions

The current PEF→ABA approval and postbuild verification implementation is a **draft PR**, not a merged or fully production-qualified default runner. It cannot be assumed available in a normal ABA invocation. If approved, create a **separate B workspace**, pass a pinned Experience Brief to the opt-in two-stage runner, inspect and approve the exact blueprint, and only then allow code generation. After build, review screenshots, locked text, real CTA behavior, user comprehension and service truth. Never mutate or redeploy A without separate authorization.

A compiled spec is not permission to run the builder. Current working B run remains draft. A/B evaluation requires immutable artifacts for both pages and independently obtained Baseline A evidence.

## Current recommendation

**Proceed with B framing and low-fidelity story, not live deployment.** The objective is a *credible alternative experience* where a first-time builder understands the human burden, the integrated hotload pack, honest setup behavior and next action in that order.

The next agent should first retrieve this brief and the run's short decision state, then ask only the remaining material owner decision. It should **not** read the whole previous chat or assume this proposed headline is approved.

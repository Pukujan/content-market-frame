# ACS market-facing website — Version B framing candidate

**Status:** PROPOSED creative direction, not approved for ABA generation or deployment.
**Prepared:** 2026-10-08.
**Source of truth:** [ACS repository at 264117398e7754d7e91076481cd664b5e197c1d4](https://github.com/Pukujan/agent-custom-setup/tree/264117398e7754d7e91076481cd664b5e197c1d4); specifically [PROJECT.md](https://github.com/Pukujan/agent-custom-setup/blob/264117398e7754d7e91076481cd664b5e197c1d4/PROJECT.md) and [multi-agent hotload README](https://github.com/Pukujan/agent-custom-setup/blob/264117398e7754d7e91076481cd664b5e197c1d4/modules/coordination/multi-agent-hotload/v0.1.0/README.md).
**Baseline A:** https://acs.design-bakery.com/ — owner-favored but not final; live visual/browser capture **not independently obtained**, so no pixel/section comparison with A is asserted.
**Version B:** isolated design/candidate, not a replacement for A until approved and evaluated.

## Product facts, not marketing invention

- ACS itself owns **multi-agent execution coordination**: live join-order roles, boss lease and FIFO failover, task claim queue, agent-less watchdog, and proposal → acceptance → PR discipline.
- The **marketed installation** is the **multi-agent hotload pack**: a repo-installed wiring of ACS runtime with pinned PCM continuity/PR governance, OIO issue records, and CGM content/writing/visual contracts. Distinguish pack breadth from narrow ACS module ownership. Do not imply ACS authored or vendors those sibling systems.
- The product is not a hosted service, omniscient agent or autonomous decision-maker. The setup has prerequisites and may fail closed/return PARTIAL; it is not a one-click browser installation.
- Product documentation is verified to the pinned repository *as written*. Current compatibility and live behavior on a fresh consumer repo must still be tested before claims such as “works anywhere” or “installs in one click.”
- CGM HTML generation is being reconsidered separately; this future website should use ABA as frontend implementation owner and not claim PEF or new CGM decisions have already shipped in ACS.

## Human-job working hypothesis (not validated by external user research)

**Primary candidate:** A technically capable independent builder or project operator running multiple AI agents on a real repository over many sessions. Their actual project competes with a recurring *second job*: assign work, stop overlap, reassemble context, track decisions/issue history, check approvals and turn output into something another person can follow.

**Observed user behavior:** UNKNOWN; no interviewed adopter quoted. The owner can select this as the lead intended audience without converting it into observed buyer data.

**Market alternative:** An engineering lead whose central need is team-level shared accountability. This remains a second candidate; do not silently collapse it into the first.

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
> When several AI agents work on a long-running project, someone still has to keep their roles, task ownership, project history, approvals, and output aligned. ACS installs a shared way of working into the repository, combining coordination with pinned continuity, issue records, and content guidance.
>
> **Primary action candidate:** Explore what gets installed (a read-only product explanation; actual click behavior to be verified).
>
> **Secondary action:** Read the install requirements (navigate to a source-pinned public setup page).

Copy is intentionally qualitative: it does **not** assert measured time saved, proven customer success, universal compatibility or fully automated end-to-end project management.

## Proposed page architecture — seven buyer beliefs

| Scene | Visitor's question | What B must establish | Visual/UX job |
| --- | --- | --- | --- |
| **B01 — Recognition** | “Is this the problem I face?” | The real burden is keeping multi-agent work together, not a lack of generated code | Strong typographic opening; actual human project in frame, no imaginary customer case |
| **B02 — The recurring extra job** | “What exactly is painful?” | Context reconstruction, role collisions, issue provenance, review and readable outcomes compete with making progress | One continuous project journey, 3 grouped moments; avoid an overwhelming 7-feature matrix |
| **B03 — Product reveal** | “What would I be getting?” | A repo-installed working surface, not a hosted omniscient agent | Simple repo-centered before/after diagram, clearly conceptual if no actual screenshot |
| **B04 — Four linked capabilities** | “How is this more than a coordinator?” | ACS role/claim/proposals + PCM continuity/governance + OIO issue/provenance + CGM content/visual rules | Four connected functions expressed as outcomes and properly attributed; optional inspect mechanics |
| **B05 — A credible workflow** | “What happens when I start?” | Preconditions → install/configure → inspect READY or PARTIAL → continue working | Experience/task flow grounded in source; no pretending a no-write illustration performs installation |
| **B06 — Boundaries build trust** | “What should I not assume?” | What remains manual, source-owned, conditional or unsupported | Plain-language FAQ and source links; no audit table in the hero |
| **B07 — Low-risk next step** | “Can I understand this before adopting it?” | Read-only tour or verified source documentation before real local install | CTA must be an actual tested control with an accurate side-effect contract |

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

**Q1 — Lead visitor / opening tension:** Prefer **independent operator and the repeated handoff burden** (B1), or team lead and coordination accountability (B3), or neither? This determines positioning and scene choices.

**Q2 — Safe primary CTA:** Prefer **read-only walkthrough of the setup** (with explicit simulation label if appropriate) or **link to pinned installation instructions**? No real setup action from an untrusted browser without separate technical verification.

Avoid asking the owner to decide palettes, component types or exact wording before the strategic human story is accepted. The agent can prepare those options autonomously.

## ABA handoff restrictions

The current PEF→ABA approval and postbuild verification implementation is a **draft PR**, not a merged or fully production-qualified default runner. It cannot be assumed available in a normal ABA invocation. If approved, create a **separate B workspace**, pass a pinned Experience Brief to the opt-in two-stage runner, inspect and approve the exact blueprint, and only then allow code generation. After build, review screenshots, locked text, real CTA behavior, user comprehension and service truth. Never mutate or redeploy A without separate authorization.

A compiled spec is not permission to run the builder. Current working B run remains draft. A/B evaluation requires immutable artifacts for both pages and independently obtained Baseline A evidence.

## Current recommendation

**Proceed with B framing and low-fidelity story, not live deployment.** The objective is a *credible alternative experience* where a first-time builder understands the human burden, the integrated hotload pack, honest setup behavior and next action in that order.

The next agent should first retrieve this brief and the run's short decision state, then ask only the remaining material owner decision. It should **not** read the whole previous chat or assume this proposed headline is approved.

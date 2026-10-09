# ACS Version B — ABA consumer React website specification

**Task:** Generate an **isolated, visually polished React/Vite market-facing product introduction** for Agent Custom Setup (ACS). This is an ABA **consumer application**; use `server/src/loop.mjs generate()` through the lightweight consuming-site adapter. **Never use `eval/run-dyad-pro.mjs`, the internal full-Pro tool preflight, or a manually authored static HTML substitute.** Do not publish or modify the existing ACS site.

**Authority:** ACS product definition at [pinned source commit](https://github.com/Pukujan/agent-custom-setup/tree/264117398e7754d7e91076481cd664b5e197c1d4). Accepted owner directions: intended individual long-project builder (D3); qualitative return attention to actual project work (D6); introduce product immediately (D7). All exact creative decisions and CTA semantics remain **draft**. Full evidence: [PEF B run](https://github.com/Pukujan/content-market-frame/blob/main/examples/acs-version-b.run.json).

## Human job and honest product identity

Your visitor is an individual software builder who uses several AI agents across multiple sessions. They want to make progress on their product, but coordinating agents, remembering earlier decisions, clarifying task ownership, and checking handoffs can become recurring work of its own. **This is an owner-identified problem hypothesis, not independently measured customer research.**

ACS is the **repository-installed coordination part** of a multi-agent hotload arrangement. The **integrated pack** connects four separately owned components: **ACS** (multi-agent coordination/claims), **PCM** (project continuity and delivery/PR governance), **OIO** (issue records/provenance), **CGM** (human-facing writing/visual contracts). Say “integrated installation” rather than implying ACS developed or owns PCM, OIO, or CGM. The hotload pack is not a hosted omniscient service and does not replace human decisions.

## Required sections and visible test hooks

Give visitors an immediately intelligible, product-identifying first screen **without requiring a scroll**. The visual hierarchy must do more than present a wall of text. Build all seven sections and mount them in the app, with the exact JSX `data-testid` attributes below:

1. **Product introduction** — `data-testid="acs-introduction"`. Identify what the installed product is, who it serves and the human benefit. One clear H1, a short supporting explanation, and a **substantial visual anchor that explains a project with cooperating agents**.
2. **Relatable recurring burden** — `data-testid="builder-problem"`. A concrete multi-session example: reorientation, ownership, prior decisions and handoff friction. No fake customer quote or quantified time saving.
3. **How the product helps** — `data-testid="product-solution"`. Connect the burden to explicit project working rules rather than “AI magic”.
4. **Four source-owned roles** — `data-testid="integrated-components"`. An understandable, visually coherent **mechanism diagram** showing ACS, PCM, OIO, CGM contributing distinct jobs. This must be visually legible at narrow widths. Each role should be traceable to real source boundaries.
5. **A day in the project** — `data-testid="project-example"`. One purposeful before/after session sequence showing explicit task ownership, review and continuity. Label it as a **conceptual scenario**, not a screenshot of a live installer or observed customer.
6. **Evidence and constraints** — `data-testid="evidence-and-limits"`. Source-backed mechanisms and attribution plus honest limits: real repository prerequisites; possible PARTIAL rather than READY; no universally guaranteed install, no ROI/customer-research statistics. Show evidence links as evidence, not a sales CTA.
7. **Technical depth on demand** — `data-testid="technical-details"`. Use accessible progressive disclosure for source-owned components, compatibility, required checks and where to read the product docs. Avoid front-loading implementation internals.

## Designed experience

- Product design should feel deliberate and credible for technical builders: confident editorial hierarchy, generous but not empty layout, complementary typography, a restrained and consistent color system, **substantial explanatory visual content** (responsive SVG/CSS/React system diagram or other supported asset technique), and meaningful motion only where helpful. Avoid generic SaaS cards, giant feature dumps, fake terminal output, glowing robot art and hero-only minimal pages.
- Prior rejected ACS page was sparsely textual; do not repeat it. Technical correctness alone is not sufficient design acceptance.
- Desktop and mobile must maintain accessible reading order; keyboard focus visible; contrast, headings, link semantics and reduced-motion behavior reasonable.
- **No primary CTA.** The owner explicitly requested correction of what the main website action *should do* (Q3 remains unanswered). Do not invent a “Try it”, “Install”, “Live demo”, “Explore setup” or “Get started” button. **Source documentation references are acceptable as plainly labeled evidence citations, not primary conversion controls.** No repository writes, simulated setup receipts, forms or effectful actions.

## Source references for proof (not endorsements)

- [ACS repository and product contract](https://github.com/Pukujan/agent-custom-setup/blob/264117398e7754d7e91076481cd664b5e197c1d4/PROJECT.md)
- [Integrated hotload README](https://github.com/Pukujan/agent-custom-setup/blob/264117398e7754d7e91076481cd664b5e197c1d4/modules/coordination/multi-agent-hotload/v0.1.0/README.md)

## Generator + review contract

This app is **a non-production visual review candidate**. The ABA model must choose a blueprint/design direction, write working React components into the ABA starter, and run typecheck. Do not hand-author `index.html` as the produced site. Record model and tool-execution results. The resulting app then requires a **real browser rendering review** (1440px and 375px, including screenshots, visual interpretation, accessibility checks, broken links, console errors, and horizontal overflow). The creator's approval of design/copy and actual next action remains distinct from a green generator run. No merge/deploy/DNS or live page replacement is authorized.

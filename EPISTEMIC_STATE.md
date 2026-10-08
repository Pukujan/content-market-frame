# Epistemic State — living, not a victory report

**As of:** 2026-10-08  
**State:** initial investigation; no final owner approval of this framework or its sample copy  
**Public-safe policy:** case observations are abstracted from an owner-provided private session. Product claims link to public repository documents. This file does not reproduce the private transcript.

## Epistemic vocabulary

- **OBSERVED:** directly visible in a named source, with a date/scope.
- **OWNER DIRECTION:** user preference or explicit correction in the source session; authoritative for desired framing, not evidence of product functionality.
- **INFERRED:** explanation that fits observations but has not been independently validated.
- **PROPOSED:** recommendation we can test, not yet accepted.
- **UNKNOWN / DISPUTED:** information missing or contradictory; must not be quietly filled in.
- **REJECTED:** an approach the owner explicitly rejected in the case.
- **APPROVED:** requires explicit decision about this specific artifact, never inferred from a passing checker or deployment.

## What we know, and what we do not

| ID | Claim | State | Basis / qualification |
| --- | --- | --- | --- |
| E01 | The case was a long, heavily revised ACS sales-site effort; several rejected versions preceded a generated page. | OBSERVED | Owner-provided Oct 8 session archive and exported session index; private source retained privately. |
| E02 | The first headline failure was presenting multi-agent collisions and a fabricated timed morning as the core product problem. | OWNER DIRECTION + OBSERVED | Corrections in the case session; later planning brief also names this as rejected. |
| E03 | A subsequent framing correction focused heavily on cross-session memory, but that alone described PCM rather than the integrated pack. | OBSERVED | Revision trajectory in case session. |
| E04 | The requested commercial umbrella is long-project mechanical overhead: canonical repo location, GitHub conventions, ownership, CI/CD gates, continuity, issue provenance, and readable content. | OWNER DIRECTION | Repeated owner corrections in the case; corresponds to the integrated-stack narrative. |
| E05 | The desired promise is one installation for the working surface, with attention returned to research, teamwork, brainstorming and creation. | OWNER DIRECTION | Explicit owner corrections; not a measured time-savings claim. |
| E06 | Research was intended to support the promise, not become the visible story. An audit-like page was rejected. | OWNER DIRECTION | Repeated session corrections on front-page copy. |
| E07 | Unapproved fabricated scenarios, clock times, customer counts and performance metrics are unacceptable. | OWNER DIRECTION | Case constraints; also prudent claims discipline. |
| E08 | Rubric headings can survive into navigation even when the main headings pass a checker. | OBSERVED IN SESSION REPORT | A later visual review reportedly found label regressions missed by narrower DOM tests; independent current-site recheck not completed here. |
| E09 | Previously used media carried outdated words rendered inside images; text-only tests did not see those. | OBSERVED IN SESSION REPORT | Later image inspection in the case; needs pixel/media review for future runs. |
| E10 | A generated site can pass a fidelity check and still be awaiting sentence-by-sentence owner acceptance. | OBSERVED IN SESSION REPORT | Final session wrap-up distinguished mechanical verification from editorial acceptance. |
| E11 | Public ACS project contract says ACS owns execution coordination, while OIO, PCM and CGM own issue logging, continuity and narrative respectively. | OBSERVED | [ACS PROJECT.md](https://github.com/Pukujan/agent-custom-setup/blob/main/PROJECT.md). |
| E12 | The current public hotload contract says the install surface combines full PCM, full CGM, OIO and ACS coordination; missing OIO yields PARTIAL, not READY. | OBSERVED | [HOTLOAD.md](https://github.com/Pukujan/agent-custom-setup/blob/main/modules/coordination/multi-agent-hotload/v0.1.0/HOTLOAD.md), [SPEC.md](https://github.com/Pukujan/agent-custom-setup/blob/main/modules/coordination/multi-agent-hotload/v0.1.0/SPEC.md), [installer](https://github.com/Pukujan/agent-custom-setup/blob/main/modules/coordination/multi-agent-hotload/v0.1.0/scripts/acs_install.py). This establishes contract/code intent, not proven success on every adopter platform. |
| E13 | The public ACS README's opening still leads with the multi-agent hotloader and its older walkthrough downplays or omits OIO in its install description. | OBSERVED | [ACS README](https://github.com/Pukujan/agent-custom-setup/blob/main/README.md) compared with E12. **Documentation drift must be reconciled rather than guessed away.** |
| E14 | CGM already has modules for brand foundation, content context, writing direction, visual direction, image generation and HTML demos. | OBSERVED | [CGM README](https://github.com/Pukujan/content-generation-modules/blob/main/README.md). |
| E15 | The publicly deployed site's present copy and network/visual behavior have not been independently re-verified in this investigation. | UNKNOWN | Historical session reports are not a live verification. |
| E16 | Whether real buyers identify “mechanical overhead of a long-running agent project” as their highest-priority pain is untested. | UNKNOWN | Strong owner insight, but not customer discovery. |
| E17 | Whether one install measurably saves time or reduces errors is unproven here. | UNKNOWN | Do not turn external studies into an ACS effect size. |
| E18 | The best buyer persona, purchase trigger, adoption friction, pricing, and CTA are not validated. | UNKNOWN | Do not pretend “developer teams” is yet a measured segment. |

## Owner assessment of the live-site direction — 2026-10-08

**OWNER DIRECTION / qualitative judgment:** The owner supplied `https://acs.design-bakery.com/` as the current example and judged this version a **substantial step forward compared with the early agent-produced directions, while explicitly saying it could be stronger and is not final**. Preserve both halves of this statement. It is a *provisional positive exemplar*, not gold-standard acceptance, not proof that the present page is optimal, and not permission to freeze its exact copy/design as a reusable template.

**OBSERVATION LIMIT:** This assessment records the owner's current judgment. An attempted independent live-site retrieval on 2026-10-08 was not possible through the available web/network tools; the current DOM, pixels, interactions, and page contents were therefore **not independently inspected** for this update. Historical reports from the case must not be represented as current verification.

**PROPOSED QUALITY LADDER:**
1. **Misframed:** wrong human pain/product scope, even if technically polished.
2. **Directionally correct:** right central human problem, basic commercial arc, materially better than rejected drafts. **Owner currently places the ACS direction here or above, without final sign-off.**
3. **Persuasive and coherent:** first-time buyers can state who it is for, why they should care, how the product changes their work, and what the CTA really does; visuals support that exact story.
4. **Validated exemplar:** real target-audience evaluation plus claim, visual, behavior and explicit editorial acceptance, with reproducible source artifacts.

**What to retain from the case:** human protagonist; integrated-pack scope; attention back to real work; research subordinate to the sales promise; honesty without an audit-report front page; story-driven image/video roles; visible previews that cannot masquerade as actual writes.

**Improvement hypotheses, not observed faults of the current live page:** sharpen the audience/trigger, make the emotional contrast more immediate, test different hero promise/subhead pairs, simplify explanation of four integrated mechanisms, strengthen the progression of visuals and video, and test whether the CTA matches buyer readiness. None of these may be recorded as live-site defects until inspected or supported by reader feedback.

**Next experiment:** present the current page (or screenshots/captured page) to target readers cold. Ask what they think it solves, how it works, whether they want the next step and what the button will do. Compare their interpretation against owner intent *before* iterating on colors, animation or generic copy polish. Preserve current version as a baseline.

---
    
## UX and product-design research — 2026-10-08

**OBSERVED IN EXTERNAL PRIMARY SOURCES:** Our approach overlaps known practices: the Design Council's Double Diamond; IDEO human-centered design; Christensen's Jobs to Be Done; Strategyzer's Value Proposition Canvas; Teresa Torres's Opportunity Solution Tree; NN/g UX storyboarding, journey mapping, service blueprinting and usability testing; SVPG's four risks (value, usability, feasibility and viability). See [research and exact citations](RESEARCH_UX_PRODUCT_DESIGN.md).

**INFERRED GAP IN CURRENT LAB:** We cover the commercial belief journey much more fully than the actual product user journey. Missing first-class artifacts include buyer-vs-operator distinctions, observed user research, navigation/IA, interaction/task flows, error and PARTIAL/READY recovery states, service blueprint, task usability, and accessibility-based acceptance. The existing ten-scene ACS storyboard is **a marketing storyboard**, not an adequate substitute for a UX task storyboard.

**PROPOSED:** Two interdependent design tracks: (A) buyer belief/market story and (B) actual user task/product experience, both from shared product truth, human-needs research and customer/job evidence. Reconcile both with a service blueprint that traces visible promises to real backstage behavior. UX research begins early and iterates; it is not just a polishing phase “later.”

**UNKNOWN:** Whether the combined agent-managed method yields higher buyer comprehension, better usability, or faster accepted designs than a simpler workflow. Whether the live ACS demo/front page satisfies any particular usability gate remains untested in this research. No actual buyer interviews or usability tests were conducted.

**OPEN DECISION:** Approve a UX/product-design extension as a distinct branch of the framework, or keep the lab narrowly focused on marketing framing and link to external UX practice? Until owner approval, keep new U0–U6 checks as proposed, not mandatory certified gates.

---

## Workflow decision — router before another ACS version (2026-10-08)

**OWNER DIRECTION:** The owner considers the previous ACS effort costly in time and cognitive/context expenditure. The priority now is to build a **repeatable context-conscious router/schema/workflow in this separate repository**, then plan a new ACS Version B website through that workflow and finally compare a fixed Baseline A with B. **Do not treat the request as permission to start another website experiment yet.**

**OBSERVED IN THIS REPOSITORY:** A seven-stage machine-readable [router](router/router.v1.json), typed [run schema](router/run.schema.json), [context protocol](router/CONTEXT_PROTOCOL.md), standard-library [CLI](scripts/frame.py), structural [tests](tests/test_frame.py), draft [ACS-B run](examples/acs-version-b.run.json) and [plan](plans/ACS_VERSION_B_PLAN.md) now exist. These are scaffolding and controls, not evidence that an unrelated repository has yet succeeded with the method.

**PROPOSED operating architecture:** This repo is a pre-CGM judgment/acceptance router. CGM remains the source-owned engine for writing, image/video visual direction, naming and HTML demos. Public source and owner direction are compressed into cited decision packets (450-word default budget). Correction invalidates downstream assumptions/scenes rather than only rewriting surface copy.

**PROPOSED evaluation ordering:**
1. Make schema, routing and context policy mechanically stable;
2. Preserve a versioned reference for the present ACS site without changing it;
3. Use three explicit human/market positioning alternatives before selecting B;
4. Approve B belief storyboard and optional UX task map;
5. Then authorize and generate B separately;
6. Compare at fixed revisions on predeclared human-understanding, persuasion, truth, visual-story and CTA/UX criteria.

**UNKNOWN:** Whether this router actually reduces future corrections or makes superior marketing. Current Version A has no frozen independent capture in this repo; Version B has not been generated; there is no A/B result to cite. Any statement of demonstrated repeatability would be premature.

**DO-NOT-DO-YET:** No redesign/asset generation/deployment for ACS B; no silently rewriting CGM modules; no publication of raw private transcript content; no assumption that a structurally accepted gate equals editorial acceptance.

---

## CGM capability and architecture audit — 2026-10-08

**OBSERVED:** The current [CGM snapshot](https://github.com/Pukujan/content-generation-modules/tree/37ba626ea3064bde89352f00e99c659e85609c5b) declares version 0.5.12 (status draft), eight module entry points, adapters and version pins, provenance/asset/README schemas, writing routes and Python checks. See the [full source-pinned audit](audits/CGM_CAPABILITY_ARCHITECTURE_AUDIT_2026-10-08.md).

**OBSERVED ARCHITECTURAL RISK:** AGENTS/README/product guidance references roughly 96 KB of core required helper reading before target documents, source research and generated assets. CGM has overlapping mandates and global output rules. This is evidence of *possible context exposure*, **not proof of exact runtime input or sole cause**.

**DOCUMENTED PROBLEMS (author reports, not independently reproduced here):** CGM issues #44/#50/#51 (wrong purpose/surface and audit leakage), #64/#66 (marketing page could satisfy skill loading/checklist and still fail human comprehension), #60 (technical word false positive), and #62 (stack workflow drift). Marketing-intro PR #65 remains open/unmerged in the inspected state; do not count it as current 0.5.12 functionality.

**INFERRED:** The ACS trouble likely combined excessive/duplicated context, content-surface misrouting, implicit buyer/problem discovery, compliance-style output gates and premature implementation. Exact causal proportions unknown.

**PROPOSED, NOT APPROVED:** Retain CGM's evidence and temporal status model, narrow writing help, visual/asset provenance, naming utility, versioning and structural tests; migrate strategy and experience decisions to a purpose-aware human/market/UX/service router; keep existing CGM adopters compatible until the replacement is proven.

**UNKNOWN:** Actual tokens loaded in the failed run, complete list of CGM adopters/pins, efficacy of replacement on unlike repos, or owner acceptance of eventual deprecation. **No CGM deletion or adopter migration authorized or performed.**

---

## Owner repository-successor philosophy — 2026-10-08

**OWNER DIRECTION / established working preference:** When a helper repo accretes stale beliefs, instructions and context overhead, the owner often prefers **creating a successor repository and selectively carrying over only its best, still-useful parts**, rather than repeatedly refactoring the entire older repository. The clean boundary helps agents start with a focused task and current assumptions, without replaying thousands of hours of prior deliberation.

**OWNER DIRECTION / continuity requirement:** The successor must preserve continuity **in the repository itself** through concise epistemic messages left by prior agents: what is actually known, which claims are inferred or disputed, why prior approaches failed, what decisions were accepted, which source references validate them, and the specific next task. This continuity must not depend on loading a complete predecessor transcript or rediscovering the whole history.

**PROPOSED successor protocol, pending design acceptance:** (1) freeze predecessor at a pinned revision as read-only historical evidence; (2) inventory contracts and actual consumers; (3) classify features as *port, redesign, reference only, or discard* with reasons; (4) carry over only verified, currently relevant rules and concise counterexamples; (5) create a one-page epistemic handoff and scoped agent routes in the fresh repo; (6) validate using unlike tasks; (7) cut over dependent repos deliberately where required. This is a suggested technique, not an obligation to preserve CGM's implementation.

**CORRECTION TO EARLIER RECOMMENDATION:** Do **not** frame continued CGM maintenance or permanent compatibility as the desired endpoint. Compatibility is a **transitional constraint** only where active adopters would otherwise break. A clean successor and retirement of obsolete architecture are legitimate preferred outcomes; no CGM deletion, dependency cutover, or replacement has yet been authorized.

**UNVERIFIED HYPOTHESIS:** A clean successor with compressed epistemic context will improve agent effectiveness and reduce context-bloat-related failure. Plausible based on experience, but improvement should be evaluated on later uses rather than asserted as measured fact.

---

## HTML implementation ownership — 2026-10-08

**OWNER DIRECTION / candidate decision:** The owner favors independent review and refinement of narrowly focused CGM modules, and identified CGM's `html-demo` module as a likely removal candidate because a separate app-building automation repository already owns interface construction.

**OBSERVED:** CGM's `html-demo` is a brief semantic HTML/responsive/screenshot checklist, not a full builder. A dedicated, privately accessible app-building repository owns fuller frontend generation and validation. The genuine overlap is **implementation ownership and agent routing**, not a prohibition on semantic HTML in React. The builder is still developing; do not claim all intended features are implemented.

**OBSERVED DEPENDENCY:** `html-demo` is declared in CGM's module registry, enforced by its validator/test fixtures, and present in downstream pinned CGM installation metadata. Removing only the Markdown skill would introduce compatibility problems.

**PROPOSED, NOT APPROVED:** Make the dedicated app-building system the sole frontend implementation authority. Route the new framing module's approved product/market/UX specification into it, and migrate any unique accessibility/viewport/screenshot criteria into a narrow experience acceptance contract without duplicating functionality. Retire `html-demo` in a coordinated versioned change after a consumer/pin audit. See the [public-safe source review and migration proposal](audits/CGM_HTML_DEMO_OWNERSHIP_2026-10-08.md).

**NOT DONE / UNKNOWN:** No `html-demo` deletion, CGM release change, consumer migration, or frontend replacement was performed. Exact set of all adopters is not enumerated. Causal contribution of `html-demo` to the earlier poor ACS page is unproven.

---

## Human-in-the-loop intent and ABA route — 2026-10-08

**OWNER PROPOSAL / DIRECTION:** Use established UX, product, market and service-design practices in a repeatable staged route. Extract intent from project repo and prior decisions, but accept that purpose, audience and commercial framing may be inherently ambiguous. An independent agent reviewer should identify genuine gaps, prepare **small targeted QA questions** for the owner (a compact form only when multiple independent essentials justify one), then carry accepted decisions through story/UX drafting and full interface implementation by ABA.

**PROPOSED automation boundary:** Automate scoped source analysis, opportunity and actor hypotheses, alternative positions, buyer-belief and user-task journeys, touchpoint/service blueprint, drafts, evidence/consistency checks, and implementation once authorized. Do **not** automate owner intent selection, treat synthetic customer interpretations as observed research, silently accept substantive design reinterpretations, or infer editorial/publish approval from green code/runner gates.

**IMPLEMENTED HERE (documentation only):** [PEF selective-QA route proposal](design/PEF_HUMAN_IN_LOOP_EXPERIENCE_ROUTER.md), including ambiguity record contract, example user question packets, experience brief for ABA, challenge/revision routing and approval boundaries. **NOT IMPLEMENTED:** CGM PEF module, form generator, automatic ABA handoff, blueprint parity verifier, site generation, or a tested end-to-end process.

**KNOWN INTEGRATION RISK:** A builder's own blueprint/build transitions do not establish that the user approved product/market/experience intent. The adapter must preserve independently reviewed decisions and prevent silent reinterpretation; verify exact private implementation capabilities before designating this complete.

**OPEN:** Confirm minimum owner review cadence, whether user-task UX is activated for all interactive marketing demos or only for product design tasks, and the acceptance boundary between approved low-fidelity brief, ABA build, and release.

---

## Working decisions — pending explicit owner review

| Decision | Status | Rationale | Revisit when |
| --- | --- | --- | --- |
| D01: The **human is the protagonist**, not the agents or repo files. | PROPOSED | Aligns storytelling with lived cost and restored agency. | Audience interviews indicate otherwise. |
| D02: The **integrated pack** is the commercial subject; the four components are supporting mechanisms. | PROPOSED | Prevents coordination-only and continuity-only drift. | Product contract/positioning updated. |
| D03: Lead with **attention and repeated setup burden**, not a made-up financial ROI. | PROPOSED | Credible before measured impact exists. | Validated outcome data becomes available. |
| D04: Main sales copy keeps evidence minimal and relevant; detailed claim ledger lives off-page. | PROPOSED | Evidence as confidence, not editorial subject. | Buyers demonstrate need for deeper proof at this stage. |
| D05: A storyboard must be owner-reviewed **before** code and media generation. | PROPOSED | Most costly errors in this case were upstream narrative choices. | Controlled pilots show an alternative is better. |
| D06: Hard truth gates are separate from subjective quality scores. | PROPOSED | Excellent prose cannot compensate for a false promise. | QA calibration evidence accumulates. |
| D07: New work here must **compose with CGM**, not duplicate its eight modules. | PROPOSED | Preserves existing ownership and routing. | CGM maintainers decide module boundary. |
| D08: Public docs contain only sanitized synthesis. | ACTIVE BOUNDARY | Prevents accidental private-to-public copying. | Explicit narrower publication approval. |

## Rejected approaches in the ACS case

1. **A fabricated “one morning” with timestamps** posing as a realistic product story. It substituted vividness for relevance and created unsupported realism.
2. **Coordination-only hero:** agent collision was real but not the overarching buyer problem.
3. **Continuity-only hero:** corrected the prior issue but collapsed the rest of the stack into PCM.
4. **Audit-first copy:** source tiers, caveats, provenance and statistics occupied the selling surface.
5. **Rubric navigation/headings:** “The Problem,” “The Market,” “Features,” “Overview” as prominent language instead of reader-facing propositions.
6. **Meta-narration:** copy that comments on the page, the chart, or the research rather than the user's life.
7. **Uninspected visual assets:** stale embedded text and poster/video mismatch survived content generation.
8. **Conflating generated, deployed, mechanically verified, and editorially accepted.**

These are rejection classes, not a magic banned-word list. The same semantic failures can appear with different words.

## Causal hypotheses to test

| Hypothesis | Prediction | Falsification experiment |
| --- | --- | --- |
| H01: Agents mistake source prominence for buyer priority. | Reading the coordination-heavy README first yields a coordination-heavy hero despite broader install scope. | Repeat with a forced product-to-human-outcome map; check whether neutral judges identify correct broad scope. |
| H02: Agents optimize source-supported statements without choosing a sales argument. | Adding research increases citations/qualifications but not reader recall or motivation. | Compare research-first vs story-first drafts with identical fact packs. |
| H03: A prompt saying “be human” is too weak to constrain semantic framing. | Fluently written copy still selects the wrong problem. | Blind reviewers label main problem and buyer outcome on each draft before any style review. |
| H04: Overcorrection arises when feedback changes only the current headline. | Fixing coordination-only produces continuity-only. | Force a coverage map showing all product layers and the umbrella problem at every revision. |
| H05: Build QA substitutes for editorial QA. | All required strings appear, yet skeptical buyers cannot explain product value. | Separate deterministic checks from first-time-reader tests; report both. |
| H06: Storyboard review lowers rework more than adding more research agents. | Earlier framing sign-off reduces rejected builds and owner interventions. | Run two similar tasks with/without storyboard gate; track actual revisions and human review time. |

## Unresolved questions (ordered by decision value)

1. **Buyer / job-to-be-done:** who currently pays the “second job” most acutely—solo multi-agent developer, maintainer, engineering lead, agency, or research team? Do not conflate users, champions and buyers.
2. **Promised scope:** should the public product be called “ACS hotloader,” “the four-layer pack,” or an endorsed umbrella? Who signs off names and what install is demonstrably supported on each platform?
3. **Proof:** which adopter runs are real, which are demos/previews, and what does the public site actually show today?
4. **Emotional transition:** is the most compelling outcome regained attention, restored confidence, fewer repeated explanations, safer collaboration, or relief from project housekeeping?
5. **Next action:** install locally, preview installation, read docs, or contact someone? The CTA should match the buyer's readiness and product capability.
6. **Exemplar reuse:** should this remain an independent evaluation lab or become a preflight skill/orchestrator invoking CGM?
7. **Visual preference:** which visual references and exclusions should become a locked art-direction record independent of copy?
8. **Evaluation benchmark:** which 3–5 other repositories represent materially different products, audiences and trust constraints?

## What changes this file

Every new decision adds a small dated record: **observation → interpretation → decision → evidence → downstream artifacts affected → owner verdict**. Never rewrite a rejected idea as if it never existed. If a downstream storyboard or media asset assumes a reversed decision, mark it stale and re-review it.

### Decision log

| Date | Event | Status |
| --- | --- | --- |
| 2026-10-08 | Initial forensic synthesis and product-doc reconciliation created in the public lab. | OBSERVED / PROPOSED mix, not approved |
| 2026-10-08 | Owner assessed live-site direction as a substantial improvement but explicitly not final; baseline is a provisional positive exemplar. Independent live inspection unavailable. | OWNER DIRECTION; page QA UNKNOWN |
| 2026-10-08 | Owner prioritized router/context preservation before any new ACS-B build. New repo gained machine route, draft run, CLI, tests and future A/B plan; no site regenerated. | OWNER DIRECTION and implemented scaffolding, impact UNKNOWN |

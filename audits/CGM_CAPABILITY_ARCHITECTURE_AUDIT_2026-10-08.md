# CGM Capability and Architecture Audit

**Audit date:** 2026-10-08  
**Source:** [Content Generation Modules](https://github.com/Pukujan/content-generation-modules)  
**Inspected main commit:** [37ba626ea3064bde89352f00e99c659e85609c5b](https://github.com/Pukujan/content-generation-modules/tree/37ba626ea3064bde89352f00e99c659e85609c5b)  
**Declared version:** 0.5.12, with status marked draft.  
**Epistemic status:** checked-in features are OBSERVED; issue reports are attributed reports, not independent reproductions; root-cause interpretations and migration choices are PROPOSED. No deletion or migration is authorized.

## Executive synthesis

CGM was originally a reusable way to make repository content comprehensible: story-first product introductions, brand and visual continuity, evidence-grounded claims, and review records. By 0.5.12 it had become an eight-module, version-pinned, adapter-driven helper with extensive writing routes, source/temporal provenance, image metadata, generated naming rules, Python validators, README and issue/PR prose conventions, and integrations with the larger agent stack.

**What works:** its evidence/claim modeling, asset provenance, module boundaries, quality documentation, pinned adapters, source-aware writing practices, and explicit acknowledgment that mechanical checks are not editorial judgment.

**What failed:** the route and gate select too often by file/output type or compliance requirements, rather than the actual human's purpose. Loading every relevant skill can produce the correct headings, source tables, restrictions and image records while still promoting the wrong protagonist, product scope, emotional need or sales argument. The ACS incident is consistent with this mechanism; context volume is a plausible contributor, not a proved sole cause.

**Recommendation:** preserve capabilities, not monolithic mandatory instructions. Design a lean purpose-based strategy/UX/service router first, extract CGM strengths as stage-scoped libraries, and postpone deleting CGM until dependent adopters can migrate safely.

## 1. Eight implemented modules

| Module | Actual capability and artifacts | Value to retain | Main limitation |
| --- | --- | --- | --- |
| [brand-foundation](https://github.com/Pukujan/content-generation-modules/blob/main/modules/brand-foundation/SKILL.md) | Audience, job, emotional versus mechanism promise, personality/voice, terms to favor/avoid, claim boundaries; brand-language template | Compact brand brief and accepted language guardrails | Does not perform customer discovery or verify a viable buyer positioning |
| [content-context](https://github.com/Pukujan/content-generation-modules/blob/main/modules/content-context/SKILL.md) | Repository contract/checkpoint research; user/job/problem/solution/mechanism; evidence support and limits; version/time provenance; terminology; project-brief v2 | Strong product truth and source map | Assumes the correct human job/problem can be inferred from repo material |
| [writing-direction](https://github.com/Pukujan/content-generation-modules/blob/main/modules/writing-direction/SKILL.md) | Human situation → consequence → product → mechanism → evidence → boundaries → next action; scan-first README/product entry; headings, selective bold, evidence and review | Readable documentation recipe | Not a market-positioning selector; inherited story shape inappropriate for every kind of page |
| [human-sounding-writing / HSW](https://github.com/Pukujan/content-generation-modules/blob/main/modules/human-sounding-writing/SKILL.md) | Voice, AI-tell/rhetoric scrubbing, concrete openings, restrained bold, issue/PR/commit/docs/blog/social/HTML/paper language, chart/takeaway guidance | Optional contextual edit and plain-language quality step | Style and word-pattern checks cannot repair wrong meaning; false positives possible |
| [human-output-naming / HON](https://github.com/Pukujan/content-generation-modules/blob/main/modules/human-output-naming/SKILL.md) | Speakable media filenames, optional safe twins, omit default pitch/speed dimensions, basename helper, per-feature glossary/filename legends | Stand-alone naming utility for people-facing files | Not core product strategy, often tangential to marketing and UX |
| [visual-direction](https://github.com/Pukujan/content-generation-modules/blob/main/modules/visual-direction/SKILL.md) | Asset roles, palette, subject relationship, composition, responsive ratios/crops, visual continuity, rejection conditions | Purposeful art direction after storyboard approval | Limited shot-by-shot narrative/film planning; default illustrated style can leak across projects |
| [image-generation](https://github.com/Pukujan/content-generation-modules/blob/main/modules/image-generation/SKILL.md) | Prompts/briefs, generated image roles, exact raster text, provider/seed/prompt/hash records, alt, crop, rejection and acceptance | Asset provenance and reproducible media review | Required embedded title/subtitle, raster/PNG hero rules are too universal and increase revision cost |
| [html-demo](https://github.com/Pukujan/content-generation-modules/blob/main/modules/html-demo/SKILL.md) | Responsive semantic HTML demo; keyboard/focus/alt guidance; mobile/tablet/desktop screenshots | Narrow website production/review checklist | Not a full interaction designer, UX task flow, state model or service blueprint |

The modules are instruction contracts, not eight autonomous production services or proof that an agent followed them effectively.

## 2. Additional features worth inventorying

**Product and provenance contracts**
- [Project brief v2 schema](https://github.com/Pukujan/content-generation-modules/blob/main/schemas/project-brief.v2.schema.json): project, audience, problem, solution, mechanism, evidence, boundaries and terminology.
- Each material claim records statement, source, shipped/experimental/planned/unknown status, what source supports and leaves unproven, exact source revision, timezone-aware record time and citation intent.
- Source types distinguish repository artifact, external publication, owner decision, user observation, experimental result and unknown search. Optional valid-time ranges separate when a claim applies from when it was recorded.
- [Provenance guide](https://github.com/Pukujan/content-generation-modules/blob/main/docs/PROVENANCE_AND_CITATION.md) explicitly warns that traceability does not equal truth.

**Narrative, readability and voice**
- [README contract](https://github.com/Pukujan/content-generation-modules/blob/main/templates/readme-contract.json) and [playbook](https://github.com/Pukujan/content-generation-modules/blob/main/docs/README_PLAYBOOK.md): reader-first sections, problem consequences, product-only story, next steps, anti-methodology leakage.
- [Scanability research](https://github.com/Pukujan/content-generation-modules/blob/main/docs/CONTENT_RESEARCH.md): descriptive headings, first-screen comprehension, selective bold, concise structure and accessible headings.
- [Writing router v1](https://github.com/Pukujan/content-generation-modules/blob/main/docs/writing-routing.json): dispatches README/product entries to writing-direction, reader-facing explanation to writing-direction, most prose and HTML to HSW, generated filenames to HON; required-load and HSW always-on prompt blocks.
- [HSW rules data](https://github.com/Pukujan/content-generation-modules/blob/main/docs/human-sounding-rules.json): extensive AI-tell word/pattern library, readability and chart advice.
- [Narrative authority](https://github.com/Pukujan/content-generation-modules/blob/main/docs/NARRATIVE_AUTHORITY.md): human-readable issue, PR, commit and receipt titles; identifiers explained in context.
- [Review rubric](https://github.com/Pukujan/content-generation-modules/blob/main/templates/review-rubric.json): comprehension, specificity, claim safety, scannability, visual clarity, responsive fit. A rubric is a review aid, not observed customer understanding.

**Visual/media production**
- [Brand direction](https://github.com/Pukujan/content-generation-modules/blob/main/docs/BRAND_DIRECTION.md) includes original Story Loop identity and human/companion artwork, palette, visual tone, continuity and rejected aesthetics.
- [Visual-style template](https://github.com/Pukujan/content-generation-modules/blob/main/templates/visual-style.json), [image brief](https://github.com/Pukujan/content-generation-modules/blob/main/templates/image-brief.json), [asset manifest schema](https://github.com/Pukujan/content-generation-modules/blob/main/schemas/asset-manifest.schema.json), [image guide](https://github.com/Pukujan/content-generation-modules/blob/main/docs/IMAGE_GUIDE.md).
- Asset roles include wide hero, problem, supporting/system, evidence, square/portrait/social, icons. Prompts and records capture intended message, scene, exact image text, ratios, alt intent, review, hashes and regeneration paths.
- Human-readable basename API in [human_filename.py](https://github.com/Pukujan/content-generation-modules/blob/main/scripts/human_filename.py); requires filename legends for generated media.

**Integration, version and enforcement**
- [system-version.json](https://github.com/Pukujan/content-generation-modules/blob/main/system-version.json) declares eight modules and canonical helper files; adopters pin versions/commits and use a .content-system adapter.
- [CHATGPT_SETUP.md](https://github.com/Pukujan/content-generation-modules/blob/main/CHATGPT_SETUP.md) and Antigravity integration; ACS hotload writing contract. Separate sister owners: PCM continuity, OIO issue provenance, ACS install/execution, agent-stack-train compatible pins.
- [validate_content_system.py](https://github.com/Pukujan/content-generation-modules/blob/main/scripts/validate_content_system.py): helper/adapter/route presence, project evidence shapes, README sections, image records, naming and other deterministic constraints.
- [verify_hsw_applied.py](https://github.com/Pukujan/content-generation-modules/blob/main/scripts/verify_hsw_applied.py): always-on **contract declaration** plus optional visible HTML jargon/tool-dump denylist. Explicitly **not** a human-writing quality grader.
- [verify_adopter_content.py](https://github.com/Pukujan/content-generation-modules/blob/main/scripts/verify_adopter_content.py): stale README placeholders, referenced visual assets, names, generic tool/AI wording, optional README structure/PNG hero checks.
- Tests and [CI](https://github.com/Pukujan/content-generation-modules/blob/main/.github/workflows/ci.yml) for these structural tools; [merge gates](https://github.com/Pukujan/content-generation-modules/blob/main/docs/ADOPTER_MERGE_GATES.md) distinguish contract validation, current-head tests, branch protection and authorization.
- [Holdout proposal](https://github.com/Pukujan/content-generation-modules/blob/main/docs/HOLDOUT_EVALUATION.md) explicitly recognizes that public contract tests cannot prove a fresh agent's judgment; recommends unseen adopter cases and independent visual evaluation.
- Versioned changelog/migrations, optional private holdouts and [issue-log contract](https://github.com/Pukujan/content-generation-modules/blob/main/docs/ISSUE_LOG.md) for cross-adopter defects.

## 3. Specific failure mechanisms and evidence

| ID | Failure mechanism | Direct source / what is known | Diagnosis |
| --- | --- | --- | --- |
| F01 | **Strategy is implicit** | [PROJECT.md](https://github.com/Pukujan/content-generation-modules/blob/main/PROJECT.md) says target owns facts, audience, brand and story; brand and context modules ask agents to infer these | No explicit decision authority for discovery of buyer problem, competing positions and approved market argument |
| F02 | **Router classifies by surface, not purpose** | [issue #44](https://github.com/Pukujan/content-generation-modules/issues/44), [#50](https://github.com/Pukujan/content-generation-modules/issues/50), [#51](https://github.com/Pukujan/content-generation-modules/issues/51) describe introductions becoming audit trails | Wrong visible content contract can be applied to a page with a different reader intention |
| F03 | **Loaded skills/checklist do not imply comprehension** | [issue #64](https://github.com/Pukujan/content-generation-modules/issues/64), [#66](https://github.com/Pukujan/content-generation-modules/issues/66) explicitly report ACS failures | A page can fulfill every sales beat yet lack a speakable main proposition; root narrative needs independent human framing gate |
| F04 | **Marketing-intro route not current stable main** | [PR #65](https://github.com/Pukujan/content-generation-modules/pull/65) is open/unmerged; 0.5.13 proposed while main remains 0.5.12 | Do not credit current main with the planned route or its checklist; even that route is insufficient according to #66 |
| F05 | **High context exposure** | Inspected Git tree: **81 files**, including **44 Markdown**, **20 JSON**, **9 Python**; docs about **275 KB**; HSW machine rules **73 KB**; mandatory core README/product reading list **~96 KB**, before target repo or research | Risk of instruction duplication, stale assumptions and recency competition; size is **not a measured loaded-token trace** nor proof of sole cause |
| F06 | **Compliance ≠ strategic correctness** | Validator docs and [holdout guide](https://github.com/Pukujan/content-generation-modules/blob/main/docs/HOLDOUT_EVALUATION.md) explicitly distinguish structural from subjective checks | Green schema/regex checks cannot prove right persona, product breadth, sales differentiation, visual coherence or task usability |
| F07 | **False-positive global prose lint** | [issue #60](https://github.com/Pukujan/content-generation-modules/issues/60) reproduces legitimate technical use of “tool call” being flagged by adopter checker | A style checker lacks domain- and purpose-aware exceptions |
| F08 | **Rigid visual defaults** | [asset schema](https://github.com/Pukujan/content-generation-modules/blob/main/schemas/asset-manifest.schema.json), [image skill](https://github.com/Pukujan/content-generation-modules/blob/main/modules/image-generation/SKILL.md), 0.5.9 changelog | Mandatory baked-in title/subtitle and PNG hero can increase cost when rejected words survive inside images |
| F09 | **Contradictory live instructions** | [image-generation skill](https://github.com/Pukujan/content-generation-modules/blob/main/modules/image-generation/SKILL.md) says link image guide/prompt record from human-facing document; [README playbook](https://github.com/Pukujan/content-generation-modules/blob/main/docs/README_PLAYBOOK.md) and writing-direction say **do not** show image-method links in adopter README | Policy precedence not cleanly compiled into one small artifact-specific instruction |
| F10 | **Patch-by-accumulation** | [CHANGELOG](https://github.com/Pukujan/content-generation-modules/blob/main/CHANGELOG.md) 0.5.0–0.5.12: HSW → more required surfaces → always-on inject → HON and legends → PNG hero → adopters and merge gates | Many individual fixes are legitimate but global mandates keep growing; solve issues at smallest applicable context and preserve negative tests instead |
| F11 | **Independent operational drift** | [issue #62](https://github.com/Pukujan/content-generation-modules/issues/62) and inspected recent Stay on the mesh runs | Mesh-sync failures need separate stack maintenance; a failed scheduled update workflow is **not evidence that the content validation tests fail** |

### Context bloat: a careful conclusion

The ~96 KB figure is the byte-size of the named helper bootstrap/read list calculated from the inspected Git tree, **not** verified model input consumed yesterday. README/product work may load target AGENTS, project contract, checkpoints, adapters, prior reviewed outputs, and external research in addition to this. There is direct evidence of high potential load and overlapping instructions, and separate direct evidence of missing/incorrect routing. We cannot assign a proportion of yesterday's failure to bloat without run-level traces or controlled comparisons.

### Misplaced narrative quality authority

CGM has a detailed causal story spine, evidence requirements, human-language checks and visuals. The issue is **not that it had no human-first instructions**. The issue is that the system did not require an independent, authoritative selection of the correct buyer problem/market frame, *before* a builder could create a site. Source evidence and copy contracts were being treated as if together they guaranteed strategic meaning.

### Machine validation boundary

Source inspection establishes automated checks for file presence, schema/value structure, selected media provenance/hash checks, README headings/assets, naming rules, and known-jargon patterns. It does **not** establish runtime enforcement that a writing module was actually read/applied, product claims were externally true, a real user would recognize the story, or an HTML demo was usable in a browser. A missing false-positive fix or unmerged route should not be silently counted as shipped.

## 4. What CGM does not currently provide as a complete first-class system

- Validated customer discovery, interviews, segmentation, Jobs to Be Done/opportunities, unmet-needs evidence;
- Distinction between user, evaluator, economic buyer and operations owner;
- Product positioning through competing options, real alternatives, differentiation, business viability and author-approved tradeoffs;
- A separate **buyer-belief storyboard** and **user-task experience storyboard**;
- Information architecture, task flows, system states, errors, permissions, partial/recovery, onboarding, longitudinal work;
- Service blueprint across visible promise, backend authorities, operational constraints and actual behavior;
- Scene-by-scene still/video direction with story-version-linked media, poster/frame/film temporal review;
- Independent skeptical-reader and actual target-user task research;
- Explicit invalidation when audience/central promise changes, with small stage-specific handoff packets and stable rejected-decision memory;
- Evidence that this whole process performs better across different repositories.

Some of these topics appear as isolated principles. Listing a principle is **not equivalent to owning an implemented process and validation path**.

## 5. Proposed disposition by capability

| Capability | Keep / split / retire? | Proposed future home |
| --- | --- | --- |
| Product truth, claim supports/limits, source revisions and temporal status | **Keep and improve** | Small shared evidence engine; all tracks consume it |
| Brand brief and terminology | **Keep, downstream** | Outputs of accepted market/experience strategy |
| Job/problem discovery and competing market frames | **Replace method** | Core human/product discovery and positioning router |
| Reader-first writing recipe | **Keep, split by purpose** | Marketing/welcome, technical/docs, evidence/audit, transactional UX-copy skills |
| HSW AI-tell patterns | **Make optional and contextual** | Late-stage copy editor; adapt to domain and false positives |
| Human filename algorithm and legend | **Keep as small utility** | Artifact/multimedia naming helper, not core story decision |
| Visual roles, images, prompt/hash/acceptance records | **Keep** | Scene-linked creative production contract |
| Mandatory text inside raster and universal PNG hero | **Retire as universal requirements** | Optional per-brand/per-project output policy |
| HTML-demo responsive and accessibility guidance | **Keep but extend** | Product UX and experience implementation |
| Pin/adopter/bootstrap contracts | **Preserve compatibility** | Integration adapter until migration completed |
| Schema/contract/claim/asset tests | **Keep when fit for purpose** | Narrow deterministic QA layer |
| GitHub issue/PR/merge/release operational rules | **Do not duplicate in new narrative system** | Existing stack owners and GitHub workflows |
| Existing research and past failures | **Archive plus distilled negative tests** | Read-on-demand evidence library and minimal agent context cards |

**No deletion recommendation yet.** CGM is a pinned input in an integrated stack, and the audit has not enumerated every adopter or tested replacement behavior. Decommissioning should be a separate release/migration decision.

## 6. Proposed replacement: small core, deeply specialized routes

~~~text
TARGET PRODUCT CONTRACT + USER/OWNER INPUT
               |
    Product truth / source semantics
               |
      Actual human situation / jobs
               |
   Compare product and market positions
               |   owner accepts
        ┌──────┴──────┐
        |             |
Buyer belief story   UX task story
        |             |
        └──────┬──────┘
               |
         Service blueprint
   promise → interaction → real operation
               |
      Accepted creative contract
        /               \
  Copy/visual/media    Product UX/implementation
        \               /
             QA
    truth + reader comprehension
    design + media + task behavior
               |
      Editorial acceptance
~~~

Each role should load the **active stage and a bounded decision packet**, not the entire CGM library. The evidence slice remains linked and retrievable. Route by human purpose and job first, then output medium. Keep truth, copy style, buyer understanding, UI usability, and editorial approval distinct.

See [UX and product-design research](../RESEARCH_UX_PRODUCT_DESIGN.md), [router runbook](../router/RUNBOOK.md) and [context protocol](../router/CONTEXT_PROTOCOL.md).

## 7. Requirements for any safe CGM migration

1. Preserve the inspected SHA, documented module inventory, schemas, helper scripts, negatives, asset records and migration history; decide what is unique to CGM versus stack sibling.
2. Inventory actual adopter pins and APIs/CI hooks; avoid breaking ACS/PCM/OIO or unrelated consumer repos.
3. Introduce independent source truth and job/purpose-based routing with explicit decisions.
4. Extract narrowly scoped skills for content, visual/media, UI and proof instead of reintroducing an everything-on system prompt.
5. Validate against unlike projects with realistic target/buyer and UX task reviews, negative cases and context budgets.
6. Bridge or deprecate existing adapter contracts deliberately, with versioned release and rollback path.
7. Only then decide whether CGM remains a small implementation package or is retired.

## 8. Open epistemic questions

- Which CGM modules and Python entrypoints are actually invoked by each current adopter?
- Was the failed ACS run really loading the full mandatory doc list, or only a small selected subset?
- Which earlier visual/text versions were carried through image assets or agent state?
- Should brand/writing/media remain in one library while the strategy/UX/service router lives separately?
- Which subject-specific checks should be required for marketing, technical docs, control planes, onboarding, product demos, analytics and audit surfaces?
- How will real user/buyer research enter as evidence rather than synthetic personas?
- Does a simpler staged system demonstrably reduce owner corrections and wasted generations?

## 9. Evidence index

**Inspected implementation:** [PROJECT](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/PROJECT.md), [README](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/README.md), [AGENTS](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/AGENTS.md), [writing router](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/docs/writing-routing.json), [project brief v2](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/schemas/project-brief.v2.schema.json), [validator](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/scripts/validate_content_system.py), [HSW verification](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/scripts/verify_hsw_applied.py), [adopter content checker](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/scripts/verify_adopter_content.py), [changelog](https://github.com/Pukujan/content-generation-modules/blob/37ba626ea3064bde89352f00e99c659e85609c5b/CHANGELOG.md).

**Direct issue reports:** [#44](https://github.com/Pukujan/content-generation-modules/issues/44), [#50](https://github.com/Pukujan/content-generation-modules/issues/50), [#51](https://github.com/Pukujan/content-generation-modules/issues/51), [#60](https://github.com/Pukujan/content-generation-modules/issues/60), [#62](https://github.com/Pukujan/content-generation-modules/issues/62), [#64](https://github.com/Pukujan/content-generation-modules/issues/64), [#66](https://github.com/Pukujan/content-generation-modules/issues/66), [unmerged PR #65](https://github.com/Pukujan/content-generation-modules/pull/65).

**What this audit did not do:** re-run the private agent session, measure actual prompt tokens used in that run, test a new marketing-generation pipeline, inspect live ACS pixels/behavior, or enumerate all adopter pins. Strategic recommendations are proposals, not findings that a replacement has already worked.

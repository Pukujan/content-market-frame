# Context protocol — preserve insight, do not replay a seven-hour session

**Version:** 0.1, proposed operational contract.

## Why context is a scarce resource

The original ACS exercise generated extensive research, revisions and artifacts. Replaying all of that into each new agent makes wrong drafts, obsolete mechanisms and rejected words appear as live instructions. It also spends context on details that do not contribute to the decision being made.

**Context is a decision resource, not a raw archive.** Preserve the ability to re-open evidence while making the hot context small, specific and accurate.

## Four-tier memory

| Tier | Contents | When to load |
| --- | --- | --- |
| **L0 — router** | Active stage, owner intent, source-safety boundary, stage stop condition | Every handoff |
| **L1 — decision packet** | Selected product, relevant verified facts, accepted decisions, rejected mistakes, open questions, next action | Every agent; target maximum 450 words |
| **L2 — evidence slice** | Exact source file/revision, short scoped excerpt, cited tests, user research excerpt with consent | Only when the active stage cannot decide from L1 |
| **L3 — archive** | Full transcripts, rejected builds, broad research, image/video provenance | Only when resolving a contradiction, doing a forensic audit or reevaluating an invalidated assumption |

Do not “summarize” L3 by dumping thousands of words. If a decision requires more evidence, request precisely which file/claim/source to inspect.

## Handoff packet design

The bundled CLI command emits L0+L1. It includes:
- the target repository and source revision;
- the exact product subject (module vs integrated pack);
- selected relevant facts and their status/source IDs;
- the accepted or still-proposed decision IDs;
- the last five rejection classes and why they failed;
- unresolved questions;
- the one next action and active stage;
- the status of all gates.

**Budget:** 450 words in the packet, not 450 words for the entire investigation. Stage-scoped evidence can be read separately and need not be lost to fit the packet. The CLI blocks oversized packets rather than truncating the weakest/most inconvenient qualifications.

**Never silently promote** an inferred statement to observed; an owner's desired promise to shipped capability; a public paper to product efficacy; or a generated page to accepted.

## Context compaction on correction

At the end of a meaningful correction, record:
1. **Old causal assumption** — which proposition or scene was built on it.
2. **What falsified it** — owner correction, code contradiction, user misunderstanding or QA finding.
3. **New decision** — new wording, status, reviewer, approval ref (if actually approved).
4. **Invariant truths** — verified capabilities and exclusions that must survive the rewrite.
5. **Invalidation set** — scenes, charts, generated assets, demos, CTAs and claims made stale.
6. **Source refs** — canonical files/commits and linked evidence.
7. **Next action** — small and bounded.

The change record becomes reusable because it describes *why a choice was wrong*, not simply that words were swapped.

## Context usage by stage

| Stage | Load | Avoid loading |
| --- | --- | --- |
| Intake | User request, target repo metadata, privacy classification | Full product code or competitor corpus |
| Product truth | Relevant normative project docs, install spec, scripts, source revisions | Marketing brainstorms as authorities |
| Human job | Truth map, owner observation, targeted customer evidence | Large engineering logs unrelated to lived experience |
| Positioning | Human job, truth map, 2–4 relevant alternatives, targeted proof | All papers ever found or full competitor site dumps |
| Storyboard | Approved positioning, claim ledger, rejection classes, visual guardrails | Old rejected full drafts unless a particular failure needs inspection |
| CGM handoff | Approved exact copy/scene/media constraints plus CGM module routing | Entire research session and every rejected image prompt |
| QA | Approved contract and actual deployed artifacts/behavior | New speculative business strategy that changes the target mid-test |

Parallel agents may research independent questions and return **source-linked claim cards**, not large raw investigation logs. One integrator resolves conflicts; it cannot concatenate every subagent response and call that synthesis.

## Source precedence

1. Authorized owner direction controls desired positioning and acceptance, but does not prove implementation.
2. Normative current product docs and tests control specified/observed behavior within their scope.
3. A product's actual state and real interaction tests determine what currently works.
4. README/previous sales copy provides vocabulary and historical intent, not necessarily complete current scope.
5. Research provides external context only to the precise proposition it supports.

When sources disagree, mark **DISPUTED**; avoid a stronger public claim. Preserve source versions and the exact nature of the disagreement. Do not duplicate a component's owned contract into this router.

## Privacy and portability

This repo is public. Its initial private transcript source must remain private. Do not copy raw chat exports, local machine paths, user-identifying content, session tokens, API keys or private screenshots into public run records. Save a sanitized explanation and a private evidence pointer only where authorized; if an evidentiary claim cannot safely be shared, label it as unavailable in the public view.

For work on private projects, keep mutable run JSON and source snippets in a private project workspace. The reusable schema and generic negative tests can stay in this public router.

## Stop / escalation conditions

Stop public-facing production when:
- the product being marketed is not disambiguated from its individual modules;
- an essential capability is disputed/unverified but the story requires it as a fact;
- owner/editor has not chosen positioning or accepted the story spine;
- the demo or CTA implies an action that has not been independently verified;
- creative assets contain stale claims or rejected concepts;
- output is structurally passing but the reader interprets the wrong human problem.

Return to the earliest incorrect assumption, not the latest CSS, video or heading.

## Success criterion

The router is worth keeping if a fresh agent on a new repository can:
- produce a traceable human job and correct product scope with short handoffs;
- offer meaningfully different market angles before committing to one;
- maintain accepted constraints across multiple agents and sessions;
- catch rejected narrative classes without regex overfitting;
- reduce human corrections and wasted asset generations **when measured**.

Until another actual use, this is a plausible contract, not an empirically validated productivity improvement.

# Existing PMM/GTM methods and agent skills — reuse assessment

**Reviewed:** 2026-10-11  
**Status:** ecosystem inventory and PROPOSED integration plan; no third-party skill installed or validated on ACS.

## Correction to the original lab design

This project was initially framed as if an entirely new product-to-human-story methodology were needed. That was too strong. The primary work is a well-established area of **product marketing management (PMM)**: voice-of-customer research, jobs to be done, positioning, messaging hierarchy, value narrative, sales-story/demo direction, and creative review.

This repository should **not recreate the PMM discipline**. It should maintain:
1. Product-specific truth and ownership reconciliation from actual code/specs;
2. A source-backed epistemic state and owner decisions;
3. A **routing adapter** to existing PMM and CGM skills;
4. A small **regression benchmark** containing the failure classes demonstrated by the ACS session;
5. Rendered/pixel/interaction verification and human editorial acceptance.

The rest should be sourced, compared, and reused wherever possible. The initial framework, QA gates, and storyboard remain **experimental working hypotheses**, not normative standards.

## Vocabulary and appropriate scope

| Object | Core question | Use for this case |
| --- | --- | --- |
| **PRD (product requirements document)** | What should the product do; which users, flows and acceptance criteria matter? | Supporting product-truth input; not the main marketing artifact. |
| **JTBD / Voice of Customer** | Which progress does the buyer seek, and how do they articulate their current struggle? | Crucial input, but genuine customer evidence is currently lacking. |
| **Product positioning** | For which buyer, against which real alternative, is this uniquely valuable? | **Primary** upstream judgment. |
| **Messaging framework / message house** | How do we translate the position into benefits, proof, objections, personas, and language? | **Primary** output. |
| **Sales narrative / story arc** | What sequence of changing beliefs best conveys stakes, offer, evidence, and decision? | **Primary** visual storyboard precursor. |
| **Creative brief / visual storyboard** | How should the chosen message appear in scenes, stills, motion and a demo? | **Primary** downstream creative handoff. |
| **GTM strategy** | How do we reach, price, launch, distribute, sell and measure across channels? | Broader commercial program; only activate when needed. |
| **CRO / copywriting / QA** | Does the actual page communicate accurately and convert without misleading? | Production and evaluation work, after positioning. |

**Do not ask a PRD tool to decide the sales narrative. Do not ask a copywriter to fix product positioning by simplifying words. Do not call a launch strategy just to write a homepage.**

## Strong existing sources to evaluate

### A. Framework / human method — April Dunford, *Obviously Awesome* + *Sales Pitch*

- [Official books/positioning](https://www.aprildunford.com/books)
- [Official positioning and sales-storyboard workbook](https://aprildunford.gumroad.com/l/aprildunford)

Useful for: starting with competitive alternatives, differentiating attributes, buyer-valued outcomes, target segments, market frame; then sequencing a **sales pitch** around those choices. The workbook expressly contains a *Positioning Canvas* and *Sales Pitch Storyboard*.

**Fit:** very high. This is more canonical and market-tested in practice than a homegrown ten-scene template. Our ten ACS scenes should be **re-mapped to and evaluated against** this framework, not treated as the correct standard. This external workbook is commercial; link to it, do not copy its pages/assets without permission.

### B. Closest multi-agent workflow — B2B Marketing Skills for AI Agents

Repository: [adam-lagerhausen/b2b-marketing-skills](https://github.com/adam-lagerhausen/b2b-marketing-skills)

Verified skill directories in repo:
- [b2b-pmm-orchestrator](https://github.com/adam-lagerhausen/b2b-marketing-skills/tree/main/skills/b2b-pmm-orchestrator) — routes ambiguous PMM work;
- [voice-of-customer-synthesis](https://github.com/adam-lagerhausen/b2b-marketing-skills/tree/main/skills/voice-of-customer-synthesis) — evidence-grounded pains, jobs, language;
- [positioning-messaging-framework](https://github.com/adam-lagerhausen/b2b-marketing-skills/tree/main/skills/positioning-messaging-framework);
- [sales-narrative-deck](https://github.com/adam-lagerhausen/b2b-marketing-skills/tree/main/skills/sales-narrative-deck);
- [demo-storyline](https://github.com/adam-lagerhausen/b2b-marketing-skills/tree/main/skills/demo-storyline);
- [ai-pmm-reviewer](https://github.com/adam-lagerhausen/b2b-marketing-skills/tree/main/skills/ai-pmm-reviewer).

**Fit:** highest practical overlap with our new routing doc. Its own readme explicitly recommends orchestrator → voice-of-customer → positioning → sales narrative → demo → reviewer. It also distinguishes positioning problems from surface copy problems and warns against fabricated claims.

**Action:** inspect skill bodies and prompts for tool access, authority, evidence-handling and expected artifacts; test its workflow first on the ACS source-truth map, without allowing publish or repository writes. Compare to our existing hand-authored pipeline before choosing components. **Not yet installed or benchmarked**.

### C. Persistent product-marketing context + customer research + copywriting — Marketing Skills

Repository: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) / [marketing skill directory](https://www.skills.sh/topic/marketing)

Verified relevant SKILL.md files:
- [product-marketing](https://github.com/coreyhaines31/marketingskills/blob/main/skills/product-marketing/SKILL.md): builds versioned `.agents/product-marketing.md` from a codebase or user answers; includes audience, JTBD, competitive alternatives, emotional tension, customer language, objections, proof and changelog;
- [customer-research](https://github.com/coreyhaines31/marketingskills/blob/main/skills/customer-research/SKILL.md): mines existing material, online voice of customer or primary interviews; distinguishes evidence confidence;
- [copywriting](https://github.com/coreyhaines31/marketingskills/blob/main/skills/copywriting/SKILL.md): translates a defined page purpose, audience, pain, differentiation and proof into landing-page words;
- [cro](https://github.com/coreyhaines31/marketingskills/tree/main/skills/cro): conversion-review workflow;
- [copy-editing](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copy-editing): final surface language refinement.

**Fit:** especially high for durable marketing context and avoiding repeated explanations. `.agents/product-marketing.md` already answers a key part of the “epistemic state” problem. We should map its **approved customer-facing fields** into the existing CGM context instead of maintaining divergent context files. Need avoid auto-translating codebase assumptions into claimed customer speech; the skill itself asks for human corrections.

**Action:** evaluate this **as an alternative/add-on**, not blindly combine the whole set with another suite. A thin adapter may need only the product-marketing context format + one chosen positioning engine.

### D. Positioning-specific alternatives

- [LeadMagic positioning-messaging SKILL.md](https://github.com/LeadMagic/gtm-skills/blob/main/skills/foundation/positioning-messaging/SKILL.md): Dunford, strategic narrative, message matrices and proof; includes explicit intake requirements.
- [gtmagents/gtm-agents positioning SKILL.md](https://github.com/gtmagents/gtm-agents/blob/main/plugins/product-marketing/skills/positioning/SKILL.md): audience → problem → promise → proof → payoff → variants.
- [senlindesign/product-marketing-skill](https://github.com/senlindesign/product-marketing-skill): interactive `/positioning-messaging` and `/gtm-strategy`, including output templates.

**Fit:** useful comparison candidates, but installing four parallel positioning engines would likely recreate our original confusion and contradictory authorities. Choose **one** positioning backbone after a fixed-benchmark comparison.

### E. ChatPRD

- [ChatPRD official features](https://www.chatprd.ai/product/features)
- [What is ChatPRD?](https://www.chatprd.ai/docs/what-is-chatprd)

ChatPRD supports PRDs, user stories, technical specs, product strategy, GTM briefs, templates, and integrations including GitHub/Linear/Claude environments.

**Fit:** useful when a repository's intended user, requirements, product scope or roadmap are not clear, and for a structured product or GTM brief. **Not the first tool to solve the sales-story, page storyboard, image/motion, or human-language problem.** A GTM brief is not itself a validated positioning claim or buyer-tested story. No ChatPRD account/integration was connected or used here.

### F. Agent Skills as packaging

- [Agent Skills open format](https://github.com/agentskills/agentskills).

An agent skill is typically a `SKILL.md` with frontmatter and optional references/assets/scripts. That is a **distribution and activation format**, not a substitute for PMM expertise. Our earlier `AGENTS.md` and `prompts/AGENT_ROUTER.md` are operating instructions, **not** a packaged, installed, validated standard Agent Skill.

We should package a project-specific adapter as an Agent Skill **only after** choosing existing skills and validating the handoffs.

## Proposed lean routing — what belongs where

```text
Repo contracts / code / tests
       |
[Source truth reconciliation]            ← local thin adapter; preserve install vs component scope
       |
[Customer evidence / JTBD]               ← B2B PMM VoC OR Marketing Skills customer-research
       |
[Positioning and messaging]               ← one existing PMM/positioning skill
       |
[Sales narrative / demo storyline]        ← B2B PMM sales-narrative-deck + demo-storyline
       |
[Copy and visual production]              ← existing pinned CGM + app builder
       |
[PMM reviewer + product truth + pixels]   ← existing ai-pmm-reviewer + local ACS regression cases
       |
[Human approval and decision history]     ← content-market-frame epistemic state
```

The **only custom layer** we have compelling evidence for is the product-specific reconciliation and cross-artifact rejection memory: “Which product is being marketed?”, “Did the story shrink to a component?”, “Did private research leak?”, “Did rejected messages survive in media?”, and “Did agent confidence masquerade as approval?”

## Immediate re-use-first experiment

**Test A:** provide identical ACS public source truth + owner-approved product scope to B2B Marketing Skills' orchestrator → positioning → sales narrative → reviewer.

**Test B:** use Marketing Skills' product-marketing + research + copywriting (with one positioning methodology such as Dunford), then the same reviewer.

**Test C (control):** use the lab's hand-written stage-gated workflow.

Hold constant: inputs, user target hypothesis, disallowed assertions, no fake customer evidence, no arbitrary installation/automatic mutation, output format and rubric. Evaluate with *independent* first-time readers for product-scope fidelity, human recognition, specificity, correct CTA expectation and revisions. Do not declare a winner based on model self-ratings. Record artifacts, time/cost, provenance and owner corrections.

**Decision pending:** Which skill to standardize, and whether a simple orchestration wrapper is sufficient. Nothing here is installed or adopted as canonical yet.

## Security/quality caution

Third-party agent skills are untrusted instructions and sometimes executable code. Inspect the `SKILL.md`, bundled scripts, tool permissions, file/network operations and external terms before installation or invocation. Pin revisions once selected. Do not send private transcripts, repo credentials or confidential customer material to external services without an explicit decision. Popularity, a README claim or the existence of a SKILL.md is **not** proof of output quality.

## Implication for this repo

Rename mentally from “new PMM process” to **“PMM skill-selection and evidence/quality lab for technical products.”** Preserve the October 8 case as a regression test, demote our original storyboard to a provisional exemplar, and benchmark existing methods before building new infrastructure.

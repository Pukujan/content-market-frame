# Proposal — Intent-Aware Product & Experience Framing Route

**Date:** 2026-10-08
**Status:** PROPOSED DESIGN, not implemented in CGM or ABA.
**Scope:** the future CGM Product & Experience Framing (PEF) module, developed here before any CGM integration.
**Approval:** no site generation, deployment, CGM/ABA modifications or ACS Version B start is authorized by this document.

## Design position

Automate the **work of understanding, mapping, drafting, checking and constructing**; do not automate the **authority to define the human problem, select consequential positioning or accept the real experience**. The agent must do everything possible before asking the owner for information that cannot safely be derived. A form appears only when multiple independent, consequential uncertainties remain and answering them together is easier than conversation; otherwise ask one targeted question. A skipped form/unknown response leaves decisions *provisional*, not approved.

A repository is valuable source evidence for *product intent and mechanism*. It is **not sufficient evidence** of actual customer need, market fit or perceived desirability. A founder/owner direction is a real decision input, not a substitute for observational research.

### Practice grounding

This is a proposed agent orchestration of existing practices, not an invented named design discipline:
- [Design Council Double Diamond](https://www.designcouncil.org.uk/resources/framework-for-innovation/): discover and define the correct problem before developing and delivering, revisit earlier assumptions.
- [GOV.UK learning user needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs): actor, situation, current workaround, unmet need and observed evidence; treat non-user opinions as assumptions for research.
- [NN/g UX storyboards](https://www.nngroup.com/articles/storyboards-visualize-ideas/): single scenario, visual moments and short action/emotion captions.
- [NN/g service blueprints](https://www.nngroup.com/articles/service-blueprints-definition/): visible user steps, backstage operations, support systems and evidence must agree.

## The actual run, with automation boundaries

| Stage | Autonomous agent output | Stop/owner question condition | Required source of authority |
| --- | --- | --- | --- |
| **I0 Repo intake** | Pin revision; inventory user-facing product, bundle scope, mechanism, adoption path, uncertainty, target environment | Product boundary is ambiguous or private source cannot be safely used | Target repo normative docs and code |
| **I1 Intent excavation** | Extract initial motivation from project issues, original accepted decisions and existing users; identify *why*, not just *what* | Why it exists is missing/disputed; the best interpretation would materially change the product's purpose | Owner intent plus dated repository decisions, explicitly separated from observed user need |
| **I2 Human problem and opportunity** | State actor, moment/trigger, existing workaround, friction, emotional and functional stakes; alternative hypotheses and evidence gaps | Conflicting target audiences or insufficient evidence for an essential claim | Real user observation when available; owner can prioritize an unvalidated hypothesis |
| **I3 Positioning alternatives** | At least two materially different claims (typically three) with source maps, alternative options, limitations and objections | Choosing one implies a real market/brand/strategy trade-off | Explicit owner/editor selection |
| **I4 Experience definition** | **Buyer belief journey**, **operator task journey** (for interactive outputs), and **service blueprint** for promises that cross mechanisms; testable UX states | Proposed experience conflicts with product contract; irreversible/side-effectful behavior; ambiguous CTA or critical task | Product/source contracts and owner task decisions |
| **I5 Low-fidelity story and design** | Readable page hierarchy, scene storyboard, wireframe interaction sketch, tone, exact claim limitations, image/video story roles, simple task acceptance | Wrong central story, misleading proof, owner doubts visual/brand direction; never build expensive assets before story accepted | Owner accepts storyboard and experience brief |
| **I6 ABA production** | Compile a builder input from accepted decisions. ABA does app framework, frontend implementation, rendering, functional repair and screenshots | Output deviates from approved intent, user interaction is unclear, or specialized tool unsupported | ABA normative run contract and approved PEF brief |
| **I7 Adversarial QA** | Separate fact/claim audit, comprehension simulation, real-browser behavior, UX states, service trace, accessibility and media/frame review | Any untestable critical benefit, major narrative miss, consequential UX/design uncertainty or release decision | Source tests, actual running app, human owner or real users as appropriate |
| **I8 Acceptance / memory** | Record accepted/rejected/stale decisions, learned negatives, pending tests, source revisions, next narrow task; propose next version | Final editorial signoff, publish/deploy, invalidated positioning, high-stakes failures | Explicit owner and repository lifecycle |

**No unnecessary stop after every stage.** The router should default to source-grounded forward progress for mechanical/minor matters. Strategy locks I3/I5 and final acceptance I8 require explicit owner decision; this can be one short consolidated review per work batch. The intermediate UX and service blueprint can be assembled automatically; human decisions are requested only when meaningfully ambiguous.

## How the agent decides whether to ask

The ambiguity detector creates an **uncertainty item**, not a generic question:

- `issue`: one concrete question with two or three genuinely different plausible interpretations;
- `evidence`: links to the relevant source facts and prior accepted decisions;
- `impact`: what would change downstream (headline, audience, task flow, safety, visuals, implementation, release);
- `agent_recommendation`: default and reasons;
- `risk`: low / medium / high, with specific rationale;
- `allowed_answer`: choose, free correction, defer, or “none of the above”;
- `blocking`: whether work can proceed under a clearly labelled assumption;
- `invalidate_on_change`: dependent decision/scene/asset IDs.

### Stop policy

**Proceed automatically:** source scope clear; choices are reversible polish or operational checks; low impact; no prior accepted decisions contradicted. Preserve the assumption if merely inferred.

**Create a targeted query:** missing information would select different primary actors, value propositions, jobs, UX flows, service behavior or proof. Offer the inferred interpretation, the alternatives, and a short correction field.

**Hard stop:** misleading product claim, incompatible underlying contract, unsafe/irreversible action, conflicting owner direction, acceptance/production publish decision, unclear real side effects. Do not smooth over this with confident generated copy.

**Research instead of owner interrogation:** when uncertainty concerns external buyer behavior, agents should search user evidence or propose real research. Owner can select a working hypothesis, but cannot turn absent user observations into facts.

### Illustrative conditional owner QA packet — not a questionnaire to send on every run

**Observed source facts:**
- “The repository's described product coordinates work and preserves selected project state.”
- “Current documentation emphasizes two different lead audiences.”
- “No independent target-user interviews were found in scoped source material.”

**Agent presents up to three decision cards only if genuinely unresolved:**

1. **Lead problem and audience:** “I infer this is primarily for an individual maintaining long-running projects. A team lead is the alternative. Which should lead this site?” Suggested: individual; allow correction or neither.
2. **Acceptable promise:** “I can verify configured process/continuity mechanisms but not time saved. May the page promise *less manual reorientation* as an intended benefit, explicitly without measured claims?” Suggested: explanatory qualitative wording, not a proven result.
3. **CTA contract:** “The designed preview appears read-only. Should the button be strictly a no-write illustration, or should it navigate to a locally installed executable flow?” Suggest read-only until side effects and source are verified.

**What the system does with the answers:** records specific decisions with reviewer references, supports “unknown” and partial answers, invalidates stale scenes and re-checks claims. Questions are grouped only when the independent decisions are truly essential to proceed and a small form benefits the user. Otherwise ask one question conversationally. Never silently interpret a skipped answer as agreement.

## Key output: compiled Experience Brief

A small agent-readable contract, not a full transcript or strategy essay:

~~~yaml
brief_version: pef.experience-brief.v0-proposal
product_source:
  repository: <exact target>
  revision: <pinned revision>
  scope: <integrated product, not an arbitrarily promoted module>
intent:
  creator_purpose: <owner-approved intent, or provisional>
  user_need: <observed evidence or explicit hypothesis>
  primary_actor: <buyer/evaluator or operator>
  job_trigger_workaround: <concise>
strategy:
  selected_position: <approved decision ID>
  promise: <exact permitted wording and limitations>
  alternative_rejected: <IDs and short reasons>
buyer_experience:
  belief_sequence: <scene IDs, headlines, proof and expected mental-model change>
product_experience:
  task_flow: <task IDs, stages, success, errors, recovery>
  ui_states: <loading, ready, partial, error, cancel, retry as relevant>
service:
  touchpoint_to_mechanism: <authority/source references and side effects>
  prereqs_limits: <known constraints>
creative:
  approved_page_outline: <hierarchy, not rendered HTML>
  approved_copy: <exact locked text and revision>
  visual_intent: <scene roles and forbidden old imagery>
  motion_intent: <what any video must demonstrate, not an aesthetic prescription>
  accessibility_and_responsive: <behavioral requirements>
build:
  producer: app-builder-automation
  user_review_ref: <real owner acceptance reference>
  output: <isolated workspace; A baseline remains untouched>
acceptance:
  structural: <tests, code, schema>
  editorial: <human comprehension and quality review>
  ux: <user tasks + behavior, including states and recovery>
  release: <separate explicit authorization>
trace:
  source_claims: <IDs and linked evidence>
  known_unknowns: <IDs>
  prior_rejections: <classes and links>
~~~

A shared user/need/intent ledger links the **buyer-belief story** to the **actual operator task story**. A product may require both, one, or neither depending on the request; task UX cannot be reduced to marketing screenshots.

## ABA integration — important preflight

The dedicated builder owns frontend execution. Treat PEF as **compiled input**, not a competing HTML generator.

**Approval boundary:** Treat any builder-internal plan or blueprint transition as an execution step, **not** as verified owner approval of the human problem, market strategy, UX plan or finished page. Whether the currently pinned ABA runner can directly consume an externally accepted blueprint remains an integration question to check against the private implementation contract before integration.

**Proposed handoff contract:**
1. Router creates approved `Experience Brief` and evidence/decision manifest.
2. A compiler emits an ABA-consumable **prompt/specification** consistent with that builder's current supported CLI; preserve exact content and source revisions for comparable runs.
3. Prefer passing a locked, externally approved design blueprint as input. If today's ABA runner cannot accept it without internally regenerating/auto-approving, **the adapter must verify the generated blueprint matches accepted decisions before allowing build**; otherwise block and record a required ABA enhancement. Do not claim this gate already exists.
4. ABA generates in an isolated target workspace. Its build, screenshot and behavior checks can iterate within the approved space; major reinterpretations route back to PEF rather than becoming unauthorized product strategy.
5. A QA role compares actual rendered pixels, UI behavior, CTA side effects and user understanding to both the PEF brief and ABA's declared implementation limits.
6. Publish/deploy is independently authorized. A successful build must never imply owner acceptance.

The app builder's stated future features are not automatically available today. Do not invent an image/video tool, deployment path, in-browser approval API, or automatic access to a restricted runner when compiling the contract.

## QA by source of uncertainty

| Problem | Who can establish an answer? | QA method |
| --- | --- | --- |
| Wrong stated product capability | Repo and real runtime tests | Contract/claim source verification |
| Owner's purpose differs from agent interpretation | Owner | Proposed paraphrase + explicit correction |
| User need is merely assumed | Real target users / research | Observation, interviews, demand evidence; owner can select hypothesis |
| Weak sales meaning | Target buyers + editorial owner | Blind first-screen interpretation, retell, objections |
| Workflow is hard to use | Actual users | Uncoached task completion and accessibility evaluation |
| Service promise isn't actually delivered | Implementation/test plus responsible product owner | Frontstage/backstage service blueprint and end-to-end scenario |
| Copy or visuals don't support chosen story | Creative reviewer and owner | Scene-role review, imagery/text and film-frame verification |
| Technical checks pass, page still unattractive | Owner and representative readers | Rendered design acceptance, never CI alone |
| Whether to deploy | Authorized operator/owner | Explicit release gate separate from build |

An AI adversarial reviewer can find plausible failures and prepare concise questions, but is not a substitute for independent buyer observation or owner authority.

## Context discipline

- Start with **source pointer + product truth + active decision + relevant rejected failure classes + one task** (bounded packet).
- Source extracts are on-demand and keyed to claim IDs.
- Avoid loading every CGM skill or the full project history.
- Record answers, assumptions, approvals, blockers and invalidations as short durable entries, with links to archived evidence.
- Agent reviewers must not quietly change the story after an explicit owner acceptance.
- Do not reset negative lessons just because the task/session/model changed.

## Implementation and evaluation boundaries

This document proposes the operational design of a future PEF module. The current machine router is v0.1 and **does not yet implement** this full conditional-QA route, compiled ABA adapter, UX service blueprint schema, external blueprint approval check or end-to-end automation. Those are the intended next increments.

Do not start an ACS Version B generation run based on this proposal. First agree on the policy; then make a small executable slice, validate it structurally, rehearse the human decision packet, and only after authorized creative acceptance hand an actual project spec to ABA.

**Next narrow implementation slice (recommended, no authorization implied):** define a structured, provenance-preserving `uncertainty/QA question` schema and a compiler from accepted run decisions to an `Experience Brief`; hold off building the application interface or redoing CGM modules until the interface contract is reviewed.

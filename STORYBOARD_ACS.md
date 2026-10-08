# ACS sales storyboard — a provisional reference, not approved copy

**Version:** STORY-ACS-001  
**Status:** DRAFT FOR OWNER CRITIQUE  
**Product basis:** [ACS product contract](https://github.com/Pukujan/agent-custom-setup/blob/main/PROJECT.md), [current hotload contract](https://github.com/Pukujan/agent-custom-setup/blob/main/modules/coordination/multi-agent-hotload/v0.1.0/HOTLOAD.md), [installer/spec](https://github.com/Pukujan/agent-custom-setup/blob/main/modules/coordination/multi-agent-hotload/v0.1.0/SPEC.md)  
**Audience hypothesis:** someone operating a long-running software project with AI agents, who is also responsible for the repo's safety and continuity. Not validated with external buyers.  
**Central tension:** the person wanted to build something; instead they keep rebuilding the operating context around it.  
**Working market promise:** a single integrated installation gives the repository shared working rules and reusable state, subject to the real setup conditions. This is not a measured ROI promise.  
**Primary action candidate:** preview an install. Real deployment/preview behavior must be verified before release.

## The emotional / causal arc

~~~text
I have meaningful work to do
         ↓
Why am I the memory, coordinator, referee and quality gate?
         ↓
This overhead repeats each session and grows with complexity
         ↓
I should not be stitching the working system together manually
         ↓
One integrated repo-level installation gives the work a shared structure
         ↓
Now I can understand exactly what it adds and what it does not
         ↓
I can inspect a truthful preview without pretending it has acted
         ↓
I can make an informed adoption decision
~~~

**The protagonist is a person responsible for a project.** Agents are part of the setting and the mechanism, never the emotional center. A market graphic is secondary evidence, not the character. Technical honesty should create confidence, not hijack the opening.

## Storyboard scenes

### Scene 01 — “Stop doing the second job.”

**Role:** hero; earns attention and names the unchosen burden.  
**Visitor's question:** “Does this understand what my work is like?”  
**Draft headline:** **Stop doing the second job.**  
**Draft subhead:** “You already have a project to build. Keeping the agents, repository rules, decisions, checks and handoffs together should not be another one. Agent Custom Setup brings that working structure into the repo.”  
**Primary CTA:** “Preview an install” → truthful no-write preview, if verified.  
**Visual:** strong typographic composition, human desk/project map as subtle visual, one organized shared work surface emerging from scattered responsibilities. The hero is *not* five floating robots, terminal commands, a full feature matrix, or a giant audit infographic.  
**Motion:** none required above the fold; calm confidence.  
**Proof/limit:** a proposal about capabilities, not measured time saved.  
**QA:** Can a first-time visitor say what the “second job” is? Can they correctly infer local repo setup rather than a hosted omniscient agent?

### Scene 02 — “The project should have a place to stand.”

**Role:** an immediately legible product visual just below the hero, not a film filling the first screen.  
**Visitor's question:** “What would I actually be getting?”  
**Draft copy:** “The rules and records your agents need belong with the project—not in whichever chat happens to be open.”  
**Visual:** one repository at center; durable working records, review gates, roles, and readable outputs attached to it. Show **one shared surface**, not a futuristic black box. Illustrative components visibly labeled as conceptual unless based on real product artifacts.  
**Motion:** a restrained animation of transient sessions coming and going while the repo's state persists. Explicitly illustrative, not “live activity.”  
**QA:** Doesn't imply automatic full chat recall or that every repo is instantly ready with no prerequisites.

### Scene 03 — “You keep putting the pieces back together.”

**Role:** recognizable human problem; seven frictions grouped into a readable journey.  
**Visitor's question:** “Is the pain really more than coordinating two agents?”  
**Draft body:** “Find the real checkout. Remind agents how GitHub works. Decide who owns the task. Watch the gates. Explain the last decision again. Recover who filed the report. Rewrite the output so another person can understand it. None of that is the project you came to build.”  
**Visual:** seven small real-world friction snapshots, with a human progress thread across them. Combine into 3 conceptual clusters for layout without deleting any of the seven: **find/align** (location, conventions, ownership), **protect/continue** (gates, session continuity), **explain/trust** (records, writing).  
**Motion:** modest repetition loop that makes repetitive overhead visible; avoid fake clocks and fictitious named customer projects.  
**QA:** The scene covers the full installed proposition, not just PCM or coordination.

### Scene 04 — “The code got faster. The work around it didn't disappear.”

**Role:** market context and urgency.  
**Visitor's question:** “Is this a real category problem, or just your workflow?”  
**Draft copy:** “The more work agents can attempt, the more a long-running project needs reliable rules, history and review.”  
**Visual:** product-free contrast: speed of generating outputs versus the growing burden of maintaining durable work. One clearly labeled conceptual illustration, or at most one or two directly relevant **verified** external measurements.  
**Proof:** **PENDING**. No figures from the case's earlier research draft may be republished without verifying exact primary source, population and relevance. No study may be turned into ACS savings or efficacy data.  
**QA:** If all citations are removed, does the story still make sense? If any citation is used, does it directly support the sentence above it? No bibliography in the hero.

### Scene 05 — “Set up the working rules once. Keep building.”

**Role:** solution reveal.  
**Visitor's question:** “So what changes?”  
**Draft body:** “Install the integrated working surface into a compatible repository. The project gets shared coordination rules, continuity, issue provenance and content guidance with versions the team can inspect. Incomplete setup reports itself instead of pretending everything is ready.”  
**Visual:** before/after installation diagram with a single repo, visible output surface and clear partial/ready distinction. It is **not** a seven-step DIY assembly illustration.  
**Motion:** one before → install attempt → visibly validated state. If prerequisites are missing, show PARTIAL and next step—not a green success animation.  
**Proof:** [HOTLOAD](https://github.com/Pukujan/agent-custom-setup/blob/main/modules/coordination/multi-agent-hotload/v0.1.0/HOTLOAD.md) and [installer](https://github.com/Pukujan/agent-custom-setup/blob/main/modules/coordination/multi-agent-hotload/v0.1.0/scripts/acs_install.py); execution on specific adopter/platform remains to be demonstrated.  
**QA:** “Once” doesn't imply no configuration, dependency checkouts or ongoing project upkeep.

### Scene 06 — “Four parts. One way to keep the project moving.”

**Role:** explain the mechanism only after the value is understood.  
**Visitor's question:** “What does the bundle cover?”

| Human concern | Layer | Draft visitor-facing promise | Mechanism / limitation |
| --- | --- | --- | --- |
| “We shouldn't lose our place every session.” | **PCM** | The project keeps reusable continuity and delivery history | Versioned project state; depends on disciplined updates |
| “Whose report is this, and is it a proposal?” | **OIO** | Issue records show who submitted them and in what capacity | Form / provenance; required component, may block READY |
| “Can the output make sense to teammates?” | **CGM** | Human-facing writing and visuals follow shared contracts | Routed guidance and checks; good taste still needs review |
| “Who decides, who works, and who may submit?” | **ACS** | Agents work with explicit roles, leases and proposal/PR rules | Coordination conventions and validation; human retains authority |

**Visual:** four distinct, calm panels feeding the same shared project surface. Product terms appear **after** human descriptions. No extra modules or future/rejected subprojects.  
**Motion:** each piece joins the same repo-level working structure; the animation makes integration visible rather than competing for attention.  
**QA:** Scope from [PROJECT.md](https://github.com/Pukujan/agent-custom-setup/blob/main/PROJECT.md) and [HOTLOAD](https://github.com/Pukujan/agent-custom-setup/blob/main/modules/coordination/multi-agent-hotload/v0.1.0/HOTLOAD.md) stays accurate.

### Scene 07 — “Your next session has somewhere to start.”

**Role:** emotional payoff and concrete shift in the person's workflow, without pretending the product owns their creativity.  
**Visitor's question:** “How would working with this feel different?”  
**Draft copy:** “Instead of rebuilding the context around every new session, begin with the recorded project state, the active task, the owner, and the checks. Then spend the conversation on the decision that actually matters.”  
**Visual:** same project in two sessions separated by time, with durable records still attached to the repo. Show the person making the important creative decision. Don't imply a universal autonomous memory across disconnected services.  
**Motion:** session A closes; repo documents remain; session B opens and reads them. This is an *illustration of the intended workflow*, not a production telemetry replay.  
**QA:** The payoff encompasses continuity but does not relabel it as the whole product.

### Scene 08 — “You can inspect what it will change.”

**Role:** trust without a legalistic disclaimer wall.  
**Visitor's question:** “Will this touch my repo or do something behind my back?”  
**Draft copy:** “See the proposed changes first. A preview is a preview: it does not install, push, open a pull request or merge anything.”  
**Visual:** a genuine or clearly identified simulated preview UI: existing state → proposed diff → review. Real code may be shown only when sourced from the shipped implementation, otherwise label illustrative.  
**Motion:** interaction pauses for review rather than auto-completing; never animate fake GitHub writes.  
**CTA:** “Preview an install.”  
**QA:** Browser/network instrumentation must confirm that the marketed preview truly has the claimed no-write/no-call behavior; the Oct 8 session **reported** this for its version, but live current behavior is not independently established here.

### Scene 09 — “The details should be inspectable.”

**Role:** technical differentiator near the bottom, after the sale is understandable.  
**Visitor's question:** “What exactly lands in my repo, what versions, and what happens if something is missing?”  
**Draft copy:** “The install records its components and checks its prerequisites. Missing requirements produce a partial state, not a pretend success. You can inspect the versioned rules and decide what to run.”  
**Visual:** compact example of exact inputs/outputs and an **observed or spec-derived** partial state. Technical comparison organized around outcomes:
- conversations vs durable repo records;
- informal ownership vs explicit claims/roles;
- hand-checked steps vs specified/validated gates;
- opaque artifact text vs documented content rules.

**Proof:** link directly to the install spec, README and real source. Treat documented intention differently from an execution test.  
**QA:** No unsupported “works on any repo instantly,” no false automatic merge claims, and no need for the visitor to learn file names in the first two screens.

### Scene 10 — “See the working surface before you adopt it.”

**Role:** conversion close; informed invitation rather than a generic slogan.  
**Visitor's question:** “What's the safest meaningful next step?”  
**Draft copy:** “Preview the workflow, see the intended changes, and read the real installation requirements before bringing it into your project.”  
**Visual:** preview interaction or restrained product still, not a stock handshake or fake customer testimonial.  
**CTA:** “Preview an install” with docs/requirements as a secondary link.  
**QA:** The primary action does exactly what its label promises, and preview / install / production-ready are visually distinct.

## Visual direction: what the visuals are FOR

**Story motif:** the human's attention being split by repeated housekeeping; a durable shared work surface removes repeated *coordination labor*, leaving room for meaningful work. Illustrate transitions in state and comprehension, not robot personalities or endless terminal mosaics.

**Visual vocabulary:** editorial clarity, one strong claim per screen, ample negative space, grounded repository/workflow objects, deliberate human presence, legible actual UI only when accurate, motion for causality (state persists, handoff occurs, review stops a risky action).

**Rejection examples:**
- Any AI-team cartoon that makes agent-vs-agent conflict the lead;
- A chronological “Monday at 9:12” customer-like story not grounded in a real disclosed case;
- Screens filled with source citations, audit rubrics or JSON field names;
- A film that shows the product pushing/merging while the demo is read-only;
- Reusing stale image files with old copy baked into the raster;
- Hero imagery that contradicts the four-layer installation;
- Fake badges, testimonials, adoption counts, ROI, or fabricated dashboards.

**Text-in-image:** default to **no embedded marketing prose**. When unavoidable, use locked copy revision and check every visible frame/crop after generation. Separate text as DOM whenever possible.

## Four alternate headline candidates for explicit review

| Candidate | Strength | Risk |
| --- | --- | --- |
| **Stop doing the second job.** | Short, emotional, encompasses all seven pains | Needs immediate concrete subhead |
| **One installation. More attention for the actual work.** | Matches owner's broad desired payoff | Could overstate real ease if prerequisites are invisible |
| **The project should remember how it works.** | Memorable, repo-centered | Risks PCM-only interpretation |
| **Your agents can write the code. Who keeps the project together?** | Recognizable tension | May over-focus AI users and underplay broader collaborators |

**No chosen headline is approved.** Select after an audience/pain check and review the headline together with its subhead and hero visual; evaluating the headline alone will give false confidence.

## Sequence integrity rules

- Reorder only with an explicit narrative reason. The case owner's requested flow was intro → problem → market impact → one-install pack → four layers → honestly bounded benefit → technical definition/comparison → demo.
- A product visual can appear just after the hero without replacing the problem narrative.
- Keep documentation and source lists off the main reading route while making them accessible.
- One CTA vocabulary must mean one real action everywhere.
- After every change, inspect **all** scenes for scope collapse and stale asset references.

## Before generating a single asset

The owner/editor should accept or modify: **audience**, **protagonist**, **umbrella pain**, **promise**, **headline/subhead pair**, **scene order**, **claim language**, **visual mood and exclusions**, and **actual CTA behavior**. Then freeze a storyboard revision and feed it to CGM.

This is an **exemplar of the decision format**; it is not evidence that the exact copy is best or that the website already uses these scenes.

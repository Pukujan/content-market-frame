# Case study: how the ACS product story kept drifting

**Case:** October 8, 2026, ACS marketing/front-page iteration.  
**Scope:** narrative and content decisions, not a re-audit of the deployed page.  
**Method:** read the owner-provided private conversation export and its page-planning subagent, then compare the eventual story with the publicly visible product contracts. Private instructions, local paths, and raw logs are intentionally not republished here.

## The actual challenge

The repository has sophisticated machinery, but its buyer has a different experience of it. The reader is not sitting around wondering whether their system has a boss lease, an issue ontology, or versioned content contracts. They are trying to keep meaningful work moving for weeks or months while spending too much time re-orienting agents, deciding which copy of a project is real, recovering lost decisions, teaching GitHub rules, and checking output that should have been trustworthy.

The **technical question** is: What does the install wire into a repository?  
The **buyer question** is: What recurring frustration disappears, how does work change, and what must I do next?  
The **strategic question** is: Which shared pain plausibly unifies OIO, ACS, PCM, and CGM without inventing capabilities?

The case repeatedly answered question one while leaving questions two and three unresolved.

## Timeline of wrong turns and what each taught us

| Stage in session | Visible drift | Owner's correction | General failure class | Repair rule |
| --- | --- | --- | --- | --- |
| Early rejected page / first rework | A timed, fictional “morning” of agents colliding, framed as the product's central story | Long-horizon projects, continuing work, preserving what humans understand were being missed | **Borrowed drama + wrong protagonist** | Demand a source-backed human job and a mechanism-to-benefit map before inventing a scene |
| First strong correction | Copy pivoted heavily to session continuity | That describes PCM alone; OIO, ACS and CGM were left out | **Single-component collapse** | Preserve all-layer coverage under one umbrella promise; never replace one narrow wedge with another |
| Expanded scope | Canonical project location, GitHub norms, collaboration, CI/CD and attention returned to creative work were added | One install should resolve the repeated mechanical work, not simply “task division” | **Product-truth expansion** | Read source of truth across the stack, not only the named repo README |
| Evidence push | Many studies, percentages, provenance and caveats became a report | Marketing needs persuasion; research is ammunition for the promise, not the subject | **Proof becomes product** | Every citation must defend one buyer-relevant sentence; move source details to proof layer |
| Competitor review | Public SaaS landing-page conventions were explored | Use commercial sequencing, demos and selling energy without false logo/social-proof claims | **Template imitation** | Borrow narrative functions, not unsupported badge/customer-count furniture |
| Rebuild stage | The owner expected automated app generation and a fresh build, not repair of the rejected hand-edited layout | Scrap the old output rather than dragging its vocabulary and architecture forward | **Implementation inertia** | A rejected narrative invalidates its implementation branch and asset briefs, not just its headline |
| Render QA | Rubric words persisted in nav despite heading checks; visuals contained prior copy; video poster did not match the clip | Visual acceptance must cover all visible pixels and flows | **Checker scope gap** | Whole-surface text audit, image review, temporal media review, real browser walkthrough |
| Closing discussion | Agent recommended reusable generator/validator scripts | The intended repeatability target was the creative and market framing, not deploy mechanics | **Tooling solution to judgment problem** | Extract story decisions and counterexamples first; automation is downstream |

The session's own reported final state was generated/deployed and mechanically checked, **not** an explicit editorial accept/cut of every sentence. Treat those as separate statuses.

## Root-cause analysis

### 1. The most prominent repo document was not the whole product story

[ACS README](https://github.com/Pukujan/agent-custom-setup/blob/main/README.md) foregrounds the multi-agent hotloader, boss lease, proposals and PR coordination. That is correct for ACS's **ownership boundary**, but can mislead an agent asked to market **the integrated installation**. The [project contract](https://github.com/Pukujan/agent-custom-setup/blob/main/PROJECT.md) is explicit that ACS itself owns coordination. The current [install contract](https://github.com/Pukujan/agent-custom-setup/blob/main/modules/coordination/multi-agent-hotload/v0.1.0/HOTLOAD.md) requires FULL PCM + FULL CGM + OIO + ACS runtime.

An agent that simply condenses README paragraphs will sell the narrow component. An agent that only follows the latest correction will sell PCM continuity. Neither derives the pack's complete value proposition.

**Structural cure:** maintain separate artifacts for (a) component ownership, (b) installed bundle capabilities and prerequisites, (c) the customer's experience, and (d) the claim allowed in public. Do not call all four “what the repo does.”

### 2. A vivid scenario is not automatically a meaningful one

The fabricated invoice morning had agents, timestamps and a plausible coordination failure. But the target story was a **human carrying an increasingly expensive second job** over a long project. Fictional names and precise times created the *appearance* of reality, and distracted from what mattered.

**Repair:** dramatize a verifiable recurring situation without implying a literal customer event. A hypothetical example must be clearly labeled and must earn its inclusion by mapping to the main promise. Better still, begin with a recognizable unquantified moment: “You open the project weeks later and spend the first part of the session explaining what was already decided.” Don't assert a measured number of minutes without evidence.

### 3. More citations cannot choose the commercial argument

Research into multi-agent failure does not, by itself, justify the claim that a specific installation solves cross-session context loss. Adoption statistics do not prove product efficacy. Software-maintenance costs do not prove hours saved by ACS. Correct studies can be attached to **the wrong claims**.

The eventual useful distinction was:
- **Problem evidence:** a real external measure of the category's friction;
- **Mechanism evidence:** the product's public spec, scripts and tests;
- **Outcome evidence:** an observed adopter result under known conditions;
- **Persuasive copy:** a clear promise constrained by those records.

If outcome evidence is missing, show the mechanism and honest demo; do not manufacture customer ROI.

### 4. Technical safety language was promoted into the reader's first impression

A source appendix, audit trail and full caveat vocabulary may be appropriate for maintainers, reviewers or procurement. They are rarely the **opening emotional argument**. The rejected drafts narrated their own evidence and described sections with rubric labels. That meant the visitor was reading about the authoring process instead of a useful change to their work.

**Repair:** keep the truth contract strict internally but present evidence in service of one claim per story beat. Explain important limits without disguising them; let proof be inspectable from the page, not dominate the page.

### 5. Revision feedback had no frozen causal model

After “not just coordination,” the agent pivoted to “continuity.” After “use more research,” the page became research. After “make it marketing,” it improved voice but could still regress in navigation and pixels. Each correction was applied **locally**, without forcing a full recheck of audience, core problem, installed scope, proof and visuals.

**Repair:** every material feedback event must create a versioned **decision delta**:
1. Which assumption was wrong?
2. What was replaced, and why?
3. Which downstream claims, scenes, CTAs, headlines, asset prompts and tests become stale?
4. What unchanged truths must still be covered?
5. Which previous rejected patterns are explicitly forbidden?

This is different from saving more conversation history; it saves the *meaning of the revision*.

## What the integrated product can credibly say today

Grounded by public ACS contracts, not a deployment test:

| Customer friction | Source-owned mechanism | Public-language interpretation | Boundaries |
| --- | --- | --- | --- |
| A new session must rediscover decisions and state | PCM owns continuity and GitHub-owned progression | “The project keeps a usable record between sessions” | Requires actual adoption and maintained files; not universal model memory |
| People and agents disagree about what should happen next | ACS owns roles, lease, queue and proposal path | “Everyone has a defined way to coordinate work” | Specification alone is not behavioral enforcement |
| An issue or report loses who submitted it | OIO owns issue-log ontology and filer/proposal distinction | “You can tell whose report you're reading and what has been approved” | Requires OIO installation; partial states are possible |
| Generated writing does not match the audience | CGM routes writing, visual and content contracts | “Human-facing output follows a shared, checkable brief” | A writing check cannot guarantee persuasive judgment |
| Source copies and gates drift | ACS hotload + PCM discipline + pinned versions and install checks | “Agents use the same project working rules and pinned dependencies” | Protection and required checks depend on GitHub/adopter configuration |
| The operator keeps orchestrating plumbing | Integrated installation | “More attention can go to the actual work” | Qualitative desired outcome; **not** independently measured time saved |

The buyer-visible story should not force the reader to learn OIO/ACS/PCM/CGM before understanding the shared frustration.

## The README-versus-installer discrepancy is instructive

The current public README describes the hotloader in a narrower, partly older vocabulary, while the public HOTLOAD, SPEC, registry and installer describe OIO as a required part of the current integrated install. This does not prove one is fraudulent; it **does** prove an agent needs a source-precedence protocol and a “needs reconciliation” marker. The correct response is neither to ignore the latest install contract nor to silently rewrite the README as if deployment were proven everywhere.

For this case, give [HOTLOAD/SPEC](https://github.com/Pukujan/agent-custom-setup/tree/main/modules/coordination/multi-agent-hotload/v0.1.0) priority on current install requirements, [PROJECT](https://github.com/Pukujan/agent-custom-setup/blob/main/PROJECT.md) priority on component ownership, and treat [README](https://github.com/Pukujan/agent-custom-setup/blob/main/README.md) as user-facing collateral that may lag. Re-check revisions before public launch.

## Lessons encoded as tests, not slogans

| Anti-pattern | Test question | Fail when |
| --- | --- | --- |
| “Technical tour = marketing” | What happens to a human's workday before/after? | Answer is a list of modules or JSON files |
| “One vivid example is enough” | Does the example represent the *main* pain? | It only illustrates one subcomponent |
| “A lot of research = persuasive” | What claim does each figure support? | Figure has no direct causal or contextual connection |
| “No jargon = human” | Could a buyer accurately restate the value? | Easy prose still says the wrong thing |
| “Landing page = section headers” | Would a human say this heading as a proposition? | Heading simply names a rubric |
| “Proof = qualified everything” | Can evidence be reached without derailing the story? | The page becomes an appendix |
| “Text checker = visual QA” | What words and claims appear in pixels and time? | Stale image text or inconsistent clips survive |
| “Build passed = approved” | Has the owner accepted the promise and copy? | Only tests, deploy or agent self-assessment exist |

## Where to build repeatability

Treat this as a **front-end judgment gate** in front of existing CGM. It produces a product truth map, human pain map, competing message strategies, a storyboard, a claim ledger, an art brief and a sign-off record. Only then should CGM writing/visual/image/HTML modules and the app builder implement. Feed failures back into benchmark cases so the *next* run learns the rejection class rather than copying a pile of corrections.

See [FRAMEWORK](FRAMEWORK.md), [QA_GATES](QA_GATES.md) and [STORYBOARD_ACS](STORYBOARD_ACS.md).

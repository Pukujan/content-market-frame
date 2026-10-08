# QA gates — reject wrong stories before they become websites

**Version:** 0.1 (proposed)  
**Use:** assess product truth, human relevance, commercial persuasion, story causality, visual/media fidelity, and truthful interaction independently. A generated page can be beautiful, responsive and incorrect.

## Gate order and failure severity

| Gate | Owner | Inputs | Pass condition | Fatal failure examples |
| --- | --- | --- | --- | --- |
| **G0 Truth** | Truth excavator + product owner | Repo contracts, scripts, install prerequisites, source map | Each central promise has a permitted mechanism and qualification; contradictions surfaced | Claims a demo performs real installs, claims an unsupported platform, conflates one module with whole pack |
| **G1 Human** | Human interpreter + skeptical reader | Actor, trigger, moment, workaround, outcome | A person recognizes a concrete cost and desired change in their terms | Only component names or “streamlined workflows”; synthetic quote passed as customer testimony |
| **G2 Positioning** | Market strategist + owner | Three candidate frames, alternatives, objections | Explicitly selected audience and promise; rationale and exclusions recorded | Vague universal “for everyone”; compelling but wrong wedge |
| **G3 Story** | Narrative editor + owner | Beat map/storyboard | Each scene changes a buyer belief and supports the next | Fabricated central case; missing bridge from pain to product; audit report in hero |
| **G4 Claims** | Claim verifier | Published copy, claims ledger | No unsupported quantities, causality, customer proof or misattributed studies | Study about the category converted into measured product savings |
| **G5 Visual** | Visual director + independent reviewer | Actual generated images, videos, thumbnails, alt text | Every asset reinforces its scene; no stale text or contradictory UI | Outdated words embedded in pixels, misleading mock screenshot, discontinuous video poster |
| **G6 Experience** | Browser QA + skeptical reader | Deployed preview (not only source) | Route/CTA/demo actually behave as described; desktop/mobile; semantic framing survives nav, footer and share preview | No-network demo calls GitHub; button implies an action it doesn't perform; rubric words survive in nav |
| **G7 Acceptance** | Human owner | G0–G6 record, live preview | Explicit accept/cut of central copy and visual direction | Claiming acceptance because generated/build/deployed/checker passed |

**G0, G4 and advertised interaction honesty are hard blockers.** No compensating weighted score. G1–G3 and G5–G6 require explicit editorial adjudication. Passing code checks is not equivalent to passing them.

## Semantic scorecard (human-rated, not a substitute for gates)

For each dimension use 0–4:
- **0:** absent/contradictory;
- **1:** mentioned but substantially wrong or generic;
- **2:** understandable yet incomplete or weak;
- **3:** clear, accurate, specific, credible and compelling enough to test with buyers;
- **4:** exceptionally clear and differentiated, validated by buyer feedback.

Score independently:
1. Audience and purchase trigger specificity;
2. Recognizable **human** cost / stakes;
3. Correct breadth of product vs component;
4. Distinctive and honest value proposition;
5. Causal flow from pain → promise → mechanisms → proof → action;
6. Objection handling without drowning the page;
7. Visual storytelling reinforces the chosen message;
8. CTA and demo correspond to real behavior.

**Trial acceptance threshold (not validated):** no score below 2; target at least 3 on audience, human recognition, scope fidelity, and narrative causality; written reasons for each low score. The owner can still reject any story. Calibration requires real users, not only models grading model output.

## The seven falsification questions

Have an independent reviewer who did **not** read the product repo see only the hero and first two sections, then ask:
1. Who is this for, and at what moment would they seek it?
2. What problem are they experiencing—not the abstract category, the lived problem?
3. What is the single most important change promised?
4. Does this page sell **one component** or an **integrated installation**?
5. Which sentence sounds like something a person would actually say?
6. Which sentence sounds like a report about a report?
7. What would you expect the primary button to do?

The reviewer must answer in their own words. The editor compares the answer against the approved strategy **without coaching**. A polished page that produces the wrong interpretation fails G1/G3/G6.

## Adversarial tests learned from ACS

### A. Narrowing attack

Rewrite the hero to focus only on agent collisions; then only on project continuity. The checker must reject both if the selected proposition is the full installed working surface. It must check the **meaning** of the leading claim, not only the presence of all four acronyms somewhere below.

### B. Research-laundering attack

Insert five externally true statistics that do not support the paragraph's claim. Ask which precise product proposition each study validates, what population was measured, and what it does **not** prove. A citation is not sufficient if causal relevance is absent.

### C. Fake-life attack

Introduce a highly specific invented customer, project, day or clock time. Reject if presented as observed. A clearly labeled illustrative hypothetical is only allowed when it represents the chosen main human problem; the reviewer may still cut it as distracting.

### D. Rubric-language attack

Replace human section headings with “The Problem,” “The Market,” “Overview,” “Features,” or neutral outline names. Scan visible heading tags **plus nav, buttons, eyebrows, footer, mobile menu, breadcrumbs, tooltips, alt/aria content where shown, and share metadata**. Generic word bans can be useful for the particular locked page but should not be a universal prohibition across products.

### E. Proof-first attack

Move a thirty-item study list, source tiers, and disclaimers into the first scroll. Reject if the reader reaches evidence before understanding the offer. Keep inspectable links and a proof layer; do not hide material limitations.

### F. Scope-to-CTA attack

Change “Preview an install” into “Install now” while keeping a local no-write simulation. Reject: the apparent transaction must match actual behavior. Conversely, do not imply the preview contacts GitHub if it only generates sample copy locally.

### G. Pixel-memory attack

Keep old product terms rendered inside a generated image, a mobile crop, or a video end-card while fixing DOM text. Test actual pixels/frames and corresponding file manifest, not just TSX or HTML.

### H. Semantic-regression attack

After the owner changes the main problem, keep an old hero motion asset or demo story. The new story version must invalidate affected assets, tests, and copy. The final review checks all scene IDs against the new decision ID.

## Claims ledger contract

For every externally checkable claim keep:

| Field | Meaning |
| --- | --- |
| Claim ID | Unique stable ID |
| Exact public wording | What will be said, not a broad topic |
| Claim class | Product mechanism / observed product result / third-party problem measure / illustration / positioning judgment |
| Source URL + revision/date | A reader-reviewable source |
| Relevant population/conditions | Who/what was measured, when, and under what conditions |
| Evidence status | Verified / unverified / disputed / rejected |
| Permissible inference | Exactly what the source warrants |
| Prohibited inference | e.g. category cost ≠ ACS savings |
| Page scene | Why the claim exists in that beat |
| Reviewer + date | Human or verifiable independent check |

**Third-party context measurements are not first-party product results.** Do not inherit numerical claims from a rejected draft without re-opening their primary sources. Never compute “hours given back” from generic industry data unless the equation and all assumptions are labeled and appropriate; even then do not describe it as measured ACS savings.

## Scene-level acceptance record

Every storyboard beat gets a card:

~~~text
Scene ID / version:
Approved buyer belief:
Human situation and actor:
On-screen headline and CTA (exact, or draft):
Product fact relied on:
Claim IDs and validity:
Visual/media brief and text-in-image policy:
Expected action and actual implementation behavior:
Mobile/accessible alternative:
Skeptical-reader interpretation:
Pass / revise / reject:
Reviewer/date and corrections:
~~~

If the chosen positioning changes, all scenes whose “approved buyer belief” depended on it become STALE, even if the scene's literal copy did not change.

## Media QA

**Still images:**
- Open the delivered **actual asset** at native dimensions and at expected crop/display size.
- Read **embedded text in the pixels**, logos, icons, UI states, numerical claims and small legends.
- Check it is the correct concept for the scene; style consistency alone is insufficient.
- Verify safe crop at hero desktop, tablet, mobile; meaningful alt text; no unlicensed or fabricated customer identities.
- Keep prompt, model, asset version, review status and rejected references in CGM's asset manifest.

**Video:**
- Inspect first frame, middle, last frame and relevant transitions; check sequence against scene card.
- Poster/thumbnail matches the opening action and visual language (no jump that reverses meaning).
- Any text overlays use the approved copy version; check them in frames, not only video metadata.
- Respect controls/motion reduction/captions; avoid autoplay that steals the visitor's first decision.
- Don't imply real installation, deployment, GitHub access or observed users when the scene is an illustration.

**Rendered page:**
- Test hero, every section, nav variants, footer, mobile menu, metadata preview, demo, and CTA paths.
- Check real network traffic and side effects for interactions that promise no writes.
- Review mobile overflow, truncated headlines, contrast, image crops, and logical section order.
- Perform a 30-second first-impression read and a more deliberate skeptic walkthrough.

## Error severity and escalation

| Severity | Example | Response |
| --- | --- | --- |
| **P0 factual / trust** | Fake customer results; wrong install behavior; fabricated evidence; unapproved repo mutation | Block release; correct source/contract; re-review all claims and scenes |
| **P1 positioning** | Wrong protagonist, wrong main problem, narrows the bundle to a component | Stop generation; return to G0–G3 and invalidate downstream assets |
| **P2 narrative / visual** | Audit voice, meta-headings, stale embedded image copy, disconnected charts | Re-storyboard and repair affected scenes; rerun skeptical-reader and pixel tests |
| **P3 polish** | Spacing, line breaks, non-substantive animation | Fix without changing the locked promise, then recheck affected presentation |

### Do not use a single green badge

Report independently: **truth**, **human recognition**, **market proposition**, **story**, **claims**, **visual**, **browser behavior**, **owner acceptance**. This separation is what prevents mechanical success from masquerading as editorial success.

## Simple acceptance experiment for the next project

Prepare two drafts from the same verified product brief:
- **Control:** regular “read repo and build a landing page” instruction.
- **Treatment:** locked truth map → competing commercial angles → storyboard → adversarial review → CGM build.

Give them to readers who have not seen the repo. Collect free-response interpretations, then compare to an owner-authored answer key and count unsupported claims, wrong-scope summaries, rewrites and discarded assets. Save both the successes and failures. Do not predeclare which variant wins.

See [FRAMEWORK](FRAMEWORK.md) for the work sequence and [templates/REVIEW_RECORD.md](templates/REVIEW_RECORD.md) for recording outcomes.

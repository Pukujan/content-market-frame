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

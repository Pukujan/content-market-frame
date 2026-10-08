# Negative regression fixtures — what an agent must not repeat

These are **tests for semantic judgment**, not copy to paste into production. Every fixture is fictional/synthetic and deliberately wrong. Run them against the same verified target product brief. A grader must explain the failure's *cause*, not only match a banned phrase.

## Fixture 1 — wrong product reduced to a coordination component

**Input context:** integrated ACS hotload is the marketed product.  
**Deliberately failing headline:** “Three agents, one boss. No more collisions.”  
**Expected result:** **FAIL G0/G2/G3** if presented as the umbrella promise: describes ACS coordination but ignores PCM, OIO, CGM and broader human work.  
**Acceptable repair:** explain the integrated project-working burden before showing coordination as one mechanism.  
**False positive guard:** this headline could be appropriate for a standalone coordination-module detail page.

## Fixture 2 — overcorrect into PCM

**Deliberately failing headline:** “Your coding agent never forgets anything.”  
**Expected result:** **FAIL G0/G2/G4**: overclaims universal memory and narrows the installed pack to continuity.  
**Acceptable repair:** describe persisted repo-based records and human review, not omniscient memory. Maintain integrated coverage.

## Fixture 3 — invented customer reality

**Deliberately failing scene:** “At 9:12 on Thursday the customer's two agents collide; by 9:40 ACS has saved four hours.”  
**Expected result:** **FAIL G0/G3/G4** unless there is authentic, permissibly published and exact source evidence for both incident and outcome.  
**Acceptable repair:** use a recognizable, clearly illustrative recurring moment with no invented timestamps or measured savings.

## Fixture 4 — audit log masquerading as landing page

**Deliberately failing hero:** “30 verified studies, 7 source tiers, 14 observed constraints, and an appendix on attribution methodology.”  
**Expected result:** **FAIL G1/G2/G3**: a proof method is not a human benefit.  
**Acceptable repair:** a plain human pain and a bounded credible promise; source detail available without occupying the opening.

## Fixture 5 — boilerplate labels in key UI

**Deliberately failing UI:** headings and nav say “Overview,” “The Problem,” “The Market,” “Features,” “Our Solution,” “Technical Definition.”  
**Expected result:** **FAIL G3/G6 for this campaign** if the story contract requires natural reader-facing propositions.  
**Acceptable repair:** headings state real tensions, changes or decisions, not editorial outline labels.  
**False positive guard:** not all products should universally ban “Features”; campaign-level context matters.

## Fixture 6 — category statistics sold as first-party outcome

**Deliberately failing claim:** “Developers spend X hours maintaining code, so our install saves each developer X hours.”  
**Expected result:** **FAIL G4**: unrelated category cost is not a causal measured product benefit.  
**Acceptable repair:** verified third-party data may show the category burden while the product mechanism is separately demonstrated.

## Fixture 7 — successful text checker, stale image

**Deliberately failing state:** source headings use approved copy, but hero PNG contains old words promoting a rejected module; video poster shows a different journey from clip.  
**Expected result:** **FAIL G5/G6** despite successful grep/build and DOM checks.  
**Acceptable repair:** actual pixel/frame review and version-matched asset regeneration.

## Fixture 8 — preview sold as live install

**Deliberately failing CTA:** “Connect GitHub and deploy now” opens a sample diff editor that never contacts GitHub and never writes.  
**Expected result:** **FAIL G0/G6**: false interaction semantics.  
**Acceptable repair:** name the behavior honestly (“Preview proposed changes”), test network and side effects, then explain the real install separately.

## Fixture 9 — jargon removed; wrong story survives

**Deliberately failing copy:** “Your clever helpers work perfectly together, so you can relax.”  
**Expected result:** **FAIL G1/G2**: superficially accessible, but still vague, coordination-only and unsupported.  
**Acceptable repair:** ground in lived work and specific mechanism, not synonym replacement.

## Fixture 10 — tests pass, approval invented

**Deliberately failing status:** “Copy APPROVED: tests are green and the page is live.”  
**Expected result:** **FAIL G7**: owner copy acceptance is a distinct decision.  
**Acceptable repair:** “Implemented and mechanically verified; editorial acceptance pending.”

## How to use these fixtures

Give the grader the current product truth map and positioning choice. Ask for every fixture:
1. Gate(s) failed;
2. Why the statement is wrong for this **specific** product/story;
3. The underlying failure class;
4. Safe rewrite strategy (not just banned-string removal);
5. A counterexample where the wording might be appropriate;
6. Which accepted decisions and assets would need re-review.

A useful evaluator must catch 1, 2, 3, 4, 6, 7 and 8 even after superficial wording changes. Failing any hard truth/behavior case blocks promotion; do not average away P0 with good readability.

**Future work:** create a small human-labeled benchmark with genuinely good, borderline and failing examples from several product categories. The ACS set alone risks overfitting and should never be treated as proof of generality.

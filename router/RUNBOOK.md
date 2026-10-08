# Run the framing router on any repository

**Router:** [router.v1.json](router.v1.json)  
**Run record:** [run.schema.json](run.schema.json)  
**CLI:** [scripts/frame.py](../scripts/frame.py)  
**Reference run:** [ACS Version B draft](../examples/acs-version-b.run.json)  
**Status:** v0.1 working implementation. It standardizes handoffs and gates; it does **not** automate judgment or editorial approval.

## Purpose and ownership

This router lives in **content-market-frame** upstream of [CGM](https://github.com/Pukujan/content-generation-modules). CGM continues owning brand, content context, writing routes, visual direction, image generation, filenames and HTML demos. This repo owns pre-generation decisions: human problems, integrated product scope, market positioning, chosen narrative, scene intention, source claims and critical review.

A structurally valid run file does not prove that its marketing story is good.

## 1. Create a run (draft, no approval)

Run these commands from the repo root:

~~~bash
python scripts/frame.py init \
  --run-id another-product-story-v1 \
  --project-id another-project \
  --repo https://github.com/OWNER/REPO \
  --ref ACTUAL_COMMIT_SHA \
  --subject "The product or integrated bundle being marketed" \
  --objective "Develop a truthful human-first product story" \
  --out runs/another-product-story-v1.json
~~~

Do not place private evidence in a public repo. For private projects keep the run record in a private folder outside the public checkout.

## 2. Operate one stage at a time

The machine route lives in [router.v1.json](router.v1.json):

| Stage | Question | Essential output |
| --- | --- | --- |
| S0 intake | Which product, audience hypothesis, sources and privacy constraints? | Scope and source index |
| S1 truth | What does the repo own, integrate, actually implement or only specify? | Source-linked truth and limitations |
| S2 human | What is the person's trigger, job, workaround and real friction? | Human situation and uncertainty |
| S3 position | Which of three alternative value propositions deserves to lead? | Three angles, objections, reviewer choice |
| S4 story | What buyer beliefs should change in which order? | Narrative spine and scene cards |
| S5 creative handoff | Which accepted claims, visuals, video and CTA behaviors go to CGM/builder? | Locked brief and media contract |
| S6 QA | Do human interpretation, factual claims, pixels and behavior agree? | Separate structural and editorial verdicts |

The user/product task UX track is optional and distinct from the buyer-belief marketing storyboard.

Load only the active stage, a compact handoff packet, and source excerpts needed to answer its question. Don't pass a huge transcript or the whole CGM repository into each agent.

~~~bash
python scripts/frame.py validate runs/another-product-story-v1.json
python scripts/frame.py pack runs/another-product-story-v1.json > next-packet.json
~~~

Packets are capped at 450 words. If over the budget, the CLI refuses instead of silently truncating the decision record.

## 3. Acceptance is an explicit recorded event

Statuses are **draft, review, accepted, rejected, stale**, with additional decision-level **proposed** and **superseded**. Product facts have their own epistemic statuses.

For accepted decisions, record **reviewed_by** and **approval_ref**. S3, S4 and S6 require corresponding **approved_by** and **approval_ref** in their accepted gates. The CLI never approves anything. These fields record claimed reviewer authorization; their existence is not cryptographic proof. Agents must not invent or infer approvals.

Only advance **active_stage** after earlier stage gates are accepted. Validation rejects skipped stages and broken references. Before S3, freeze the concrete source revision; drafts can use an explicitly unpinned marker.

## 4. When a premise is corrected, invalidate its descendants

~~~bash
python scripts/frame.py invalidate runs/another-product-story-v1.json \
  --decision D1 \
  --reason "The page sells one component instead of the integrated product" \
  --out runs/another-product-story-v2.json
~~~

The old revision remains. The chosen decision and dependent scenes become STALE, later gates reopen, and the history records why. Create a new decision rather than silently overwriting the rejected explanation.

## 5. Generate only from an accepted creative packet

After S3 and S4 are explicitly accepted, hand CGM and any app builder: exact approved text, audience, product truth, story spine, scene-to-belief map, claim limits, forbidden old concepts, image and video roles, responsive rules and real CTA behavior. The builder cannot choose a different story merely because it finds an older asset convenient.

CGM owns the writing and image generation. This router owns upstream story and framing selection and their provenance.

## 6. Verify different truths with different gates

**Structural validation:** schema/IDs/references/approvals/context budget.  
**Product validation:** source revisions, implementation contract, honest CTA/network behavior.  
**Semantic validation:** recognizable human cost, correct product breadth, coherent commercial message.  
**Visual validation:** still pixels, image text, moving frames, poster/clip consistency, responsive crops.  
**Editorial acceptance:** explicit human review. Mechanical passing is not editorial approval.

## Local validation commands

~~~bash
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/frame.py validate examples/acs-version-b.run.json
python scripts/frame.py pack examples/acs-version-b.run.json
~~~

The GitHub workflow in [.github/workflows/frame-validation.yml](../.github/workflows/frame-validation.yml) runs these structural checks. No image models, app builders or API keys are required.

## ACS Version B — parked until framing is reviewed

The current public ACS page is **Baseline A**, favored by the owner over earlier failures but not signed off as final. The run is [acs-version-b.run.json](../examples/acs-version-b.run.json). The planning document is [ACS_VERSION_B_PLAN.md](../plans/ACS_VERSION_B_PLAN.md). Nothing in this router authorizes changing, generating, or deploying Version B.

See [CONTEXT_PROTOCOL.md](CONTEXT_PROTOCOL.md) for context preservation and [QA_GATES.md](../QA_GATES.md) for deeper semantic checks.

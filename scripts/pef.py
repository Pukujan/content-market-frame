#!/usr/bin/env python3
"""PEF v0.1: targeted ambiguity review and guarded ABA specification compilation.

Only uses the Python standard library. This does NOT call a model, accept
human approval, run ABA or publish a site. It refuses to compile unapproved
or source-unpinned experience drafts. Source/evidence checks are structural.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import frame

MAX_QUESTIONS = 3
SEVERITY = {"critical": 0, "high": 1, "medium": 2, "low": 3}
PRE_BUILD_STAGES = frame.STAGES[:frame.STAGES.index("S6_qa")]


def read_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def encoded(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def hash_data(value: object) -> str:
    return hashlib.sha256(encoded(value)).hexdigest()


def audit_questions(run: dict, qa: dict) -> list[str]:
    errors = frame.validate_run(run)
    if qa.get("schema_version") != "pef.questions.v1":
        errors.append("QA schema version must be pef.questions.v1")
    if qa.get("run_id") != run.get("run_id"):
        errors.append("QA run_id mismatch")
    questions = qa.get("questions")
    if not isinstance(questions, list):
        return errors + ["QA questions must be a list"]
    facts = {f["id"] for f in run["facts"]}
    decisions = {d["id"] for d in run["decisions"]}
    seen = set()
    for q in questions:
        if not isinstance(q, dict):
            errors.append("QA question must be an object")
            continue
        qid = q.get("id")
        if not isinstance(qid, str) or not re.fullmatch(r"Q[0-9]+", qid):
            errors.append(f"Invalid QA id {qid}")
        if qid in seen:
            errors.append(f"Duplicate QA id {qid}")
        seen.add(qid)
        status = q.get("status")
        if status not in ("open", "answered", "deferred"):
            errors.append(f"{qid}: invalid status")
        if q.get("impact") not in SEVERITY:
            errors.append(f"{qid}: invalid impact")
        if not isinstance(q.get("blocking"), bool):
            errors.append(f"{qid}: blocking must be boolean")
        if q.get("impact") == "critical" and not q.get("blocking"):
            errors.append(f"{qid}: critical uncertainty must block")
        for field in ("question", "why_ambiguous", "consequence"):
            if not isinstance(q.get(field), str) or not q[field].strip():
                errors.append(f"{qid}: missing {field}")
        refs = q.get("evidence_fact_ids", [])
        drefs = q.get("affected_decision_ids", [])
        if not isinstance(refs, list) or not isinstance(drefs, list):
            errors.append(f"{qid}: evidence/decision refs must be lists")
            continue
        errors.extend(f"{qid}: unknown fact {r}" for r in refs if r not in facts)
        errors.extend(f"{qid}: unknown decision {r}" for r in drefs if r not in decisions)
        opts = q.get("options", [])
        if not isinstance(opts, list) or not (2 <= len(opts) <= 4):
            errors.append(f"{qid}: provide 2–4 possible answers")
            continue
        ids = [o.get("id") for o in opts if isinstance(o, dict)]
        if len(ids) != len(opts) or len(ids) != len(set(ids)):
            errors.append(f"{qid}: option IDs missing/duplicated")
        if q.get("recommended_option_id") not in ids:
            errors.append(f"{qid}: recommendation must reference an option")
        if status == "answered":
            a = q.get("answer")
            if not isinstance(a, dict) or not all(a.get(k) for k in ("choice_id", "answered_by", "answer_ref")):
                errors.append(f"{qid}: answered requires choice, reviewer, provenance")
            elif a.get("choice_id") not in ids:
                errors.append(f"{qid}: selected option does not exist")
            elif a.get("choice_id") == "other" and not str(a.get("note", "")).strip():
                errors.append(f"{qid}: other answer requires a concrete correction")
        elif q.get("answer"):
            errors.append(f"{qid}: non-answered item cannot carry answer/approval")
    return errors


def question_packet(run: dict, qa: dict) -> dict:
    errors = audit_questions(run, qa)
    if errors:
        raise ValueError("; ".join(errors))
    unanswered = sorted(
        (q for q in qa["questions"] if q["status"] != "answered"),
        key=lambda q: (not q["blocking"], SEVERITY[q["impact"]], q["id"])
    )
    selected = unanswered[:MAX_QUESTIONS]
    facts = {f["id"]: f for f in run["facts"]}
    return {
        "schema_version": "pef.owner-review.v1",
        "run_id": run["run_id"],
        "questions": [
            {
                "id": q["id"], "impact": q["impact"], "blocking": q["blocking"],
                "question": q["question"], "why_ambiguous": q["why_ambiguous"],
                "consequence": q["consequence"],
                "evidence": [
                    {"fact_id": ref, "status": facts[ref]["status"], "source_refs": facts[ref]["source_refs"]}
                    for ref in q["evidence_fact_ids"]
                ],
                "options": q["options"], "suggested": q["recommended_option_id"],
                "answer_instruction": "Choose an option, correct it or defer. A skipped answer is never approval."
            }
            for q in selected
        ],
        "remaining_unanswered": len(unanswered)-len(selected),
        "blocking_total": sum(1 for q in unanswered if q["blocking"]),
        "note": "This is a decision review, not a marketing survey. Answer records require independent owner provenance."
    }


def validate_experience(run: dict, qa: dict, brief: dict) -> list[str]:
    errors = audit_questions(run, qa)
    if brief.get("schema_version") != "pef.experience.v1":
        errors.append("Experience schema version must be pef.experience.v1")
    if brief.get("run_id") != run.get("run_id"):
        errors.append("Experience run_id mismatch")
    if brief.get("source_revision") != run["project"]["source_ref"]:
        errors.append("Experience revision does not match source run")
    if not re.fullmatch(r"[0-9a-f]{40}", run["project"]["source_ref"]):
        errors.append("Source revision must be a concrete 40-character commit SHA")
    for stage in PRE_BUILD_STAGES:
        gate = run["gates"][stage]
        if gate["status"] != "accepted":
            errors.append(f"Cannot send to ABA: {stage} is not accepted")
        if stage in ("S3_position", "S4_story", "S5_creative_handoff"):
            if not gate.get("approved_by") or not gate.get("approval_ref"):
                errors.append(f"Cannot send to ABA: {stage} needs recorded human signoff")
    for q in qa.get("questions", []):
        if q.get("blocking") and q.get("status") != "answered":
            errors.append(f"Blocking owner QA unresolved: {q.get('id')}")
    if errors:
        return errors

    reviewed = brief.get("review", {})
    if reviewed.get("status") != "approved":
        errors.append("Experience Brief not approved")
    if not reviewed.get("approved_by") or not reviewed.get("approval_ref"):
        errors.append("Experience Brief missing reviewer and approval reference")
    creative_gate = run["gates"]["S5_creative_handoff"]
    if (reviewed.get("approved_by"), reviewed.get("approval_ref")) != (creative_gate.get("approved_by"), creative_gate.get("approval_ref")):
        errors.append("Experience Brief approval does not match S5 creative signoff")

    decisions = {d["id"]: d for d in run["decisions"]}
    facts = {f["id"]: f for f in run["facts"]}
    scenes = {s["id"]: s for s in run["scenes"]}
    claims = {c["id"]: c for c in run["claims"]}
    position = brief.get("position", {})
    posid = position.get("decision_id")
    if posid not in decisions or decisions[posid].get("status") != "accepted" or decisions[posid].get("kind") != "positioning":
        errors.append(f"Selected positioning decision not accepted: {posid}")
    for q in qa.get("questions", []):
        if q.get("blocking"):
            for did in q.get("affected_decision_ids", []):
                if decisions[did]["status"] != "accepted":
                    errors.append(f"QA {q['id']} affects unaccepted decision {did}")
    for fid in brief.get("intent", {}).get("evidence_fact_ids", []):
        if fid not in facts:
            errors.append(f"Intent references missing fact {fid}")
    if brief.get("intent", {}).get("user_need_status") == "observed_user_research":
        ids = brief["intent"].get("evidence_fact_ids", [])
        if not ids or not any(
            facts[fid]["status"] == "observed" and facts[fid].get("source_refs")
            for fid in ids if fid in facts
        ):
            errors.append("Observed user need requires observed evidence; owner direction does not qualify")
    for cid in position.get("claim_ids", []):
        c = claims.get(cid)
        if not c or c.get("status") != "verified" or not c.get("source_refs"):
            errors.append(f"Unverified or unreferenced marketing claim {cid}")
    for b in brief.get("buyer_journey", []):
        scene = scenes.get(b.get("scene_id"))
        if not scene or scene.get("status") != "accepted":
            errors.append(f"Buyer scene unaccepted: {b.get('scene_id')}")
        else:
            for did in scene.get("depends_on_decisions", []):
                if decisions.get(did, {}).get("status") != "accepted":
                    errors.append(f"Scene {scene['id']} depends on unaccepted decision {did}")
            for cid in scene.get("claim_ids", []):
                if claims.get(cid, {}).get("status") != "verified":
                    errors.append(f"Scene {scene['id']} has unverified claim {cid}")
    for v in brief.get("creative", {}).get("visual_roles", []):
        if v.get("scene_id") not in {x["scene_id"] for x in brief.get("buyer_journey", [])}:
            errors.append(f"Visual references scene not in buyer journey: {v.get('scene_id')}")
    tasks = {t["id"] for t in brief.get("ux_tasks", [])}
    for t in brief.get("service_touchpoints", []):
        if t.get("task_id") not in tasks:
            errors.append(f"Service touchpoint references missing task {t.get('task_id')}")
    cta = brief.get("cta", {})
    if cta.get("behavior") != "none" and (not cta.get("behavior_verified") or not cta.get("authority_ref")):
        errors.append("CTA action is not source-verified; cannot pass to builder")
    if cta.get("behavior") == "local_action" and not brief.get("service_touchpoints"):
        errors.append("Local action requires a service blueprint touchpoint")
    if not brief.get("buyer_journey"):
        errors.append("No buyer journey")
    if not brief.get("creative", {}).get("acceptance_tests"):
        errors.append("No design acceptance tests")
    return errors


def render_spec(run: dict, qa: dict, brief: dict) -> str:
    errors = validate_experience(run, qa, brief)
    if errors:
        raise ValueError("; ".join(errors))
    source = run["project"]
    decision = next(d for d in run["decisions"] if d["id"] == brief["position"]["decision_id"])
    lines = [
        "# ABA input: approved Product & Experience Brief",
        "",
        "**Implementation owner:** App Builder Automation. This document is INPUT, not an app and not release authorization.",
        f"**Project:** {source['product_subject']}",
        f"**Source:** {source['repo']} @ {source['source_ref']}",
        f"**Run:** {run['run_id']}",
        f"**Accepted position:** {decision['id']} — {decision['statement']}",
        f"**Owner acceptance reference:** {brief['review']['approval_ref']}",
        "",
        "## Human purpose and experience",
        f"- Creator's purpose: {brief['intent']['creator_purpose']}",
        f"- User need ({brief['intent']['user_need_status']}): {brief['intent']['user_need']}",
        f"- Actor: {brief['audience']['actor']}",
        f"- Job: {brief['audience']['job']}",
        f"- Trigger: {brief['audience']['trigger']}",
        f"- Current workaround: {brief['audience']['workaround']}",
        f"- Promise: {brief['position']['promise']}",
        *[f"- Boundary: {x}" for x in brief['position']['limitations']],
        "",
        "## Page outline and approved wording",
        f"- Hero: {brief['creative']['headline']}",
        *[f"- Section: {x}" for x in brief['creative']['outline']],
        "",
        "## Buyer belief storyboard"
    ]
    lines += [f"- {x['scene_id']}: {x['message']} — expected change: {x['belief_change']}" for x in brief['buyer_journey']]
    lines += ["", "## Product/UX tasks and states"]
    lines += [f"- {x['id']}: {x['scenario']}; success: {x['success']}; states: {', '.join(x['states'])}" for x in brief['ux_tasks']] or ["- No interactive product task specified; do not invent one."]
    lines += ["", "## Service blueprint trace"]
    lines += [f"- {x['task_id']}: {x['visible']} → {x['backstage']} ({x['authority_ref']}); limits: {x['limitation']}" for x in brief['service_touchpoints']] or ["- No backstage actions specified."]
    lines += ["", "## Visual roles"]
    lines += [f"- {x['scene_id']}: {x['purpose']}" for x in brief['creative']['visual_roles']] or ["- No generated visual assets specified."]
    lines += ["", "## CTA and permissions"]
    lines += [f"- Label: {brief['cta']['label']}", f"- Behavior: {brief['cta']['behavior']}",
              f"- Side effects: {brief['cta']['side_effects']}",
              f"- Authority: {brief['cta'].get('authority_ref', 'none')}"]
    lines += ["", "## Approved claim references"]
    claims = {c["id"]: c for c in run["claims"]}
    lines += [f"- {cid}: {claims[cid]['wording']} | sources: {', '.join(claims[cid]['source_refs'])}" for cid in brief['position']['claim_ids']] or ["- No quantitative or observed-outcome claims approved."]
    lines += ["", "## Acceptance checks"]
    lines += [f"- {x}" for x in brief['creative']['acceptance_tests']]
    lines += ["", "## Rejected historical framing"]
    lines += [f"- {x}" for x in brief['creative'].get('forbidden_inherited_patterns', [])]
    lines += ["", "## Builder boundary",
              "- ABA chooses and implements its supported frontend stack. Do not build a competing CGM HTML demo.",
              "- Preserve the EXACT approved headline, core promise, audience, claims, CTA and side effects.",
              "- Builder-internal blueprint acceptance is NOT owner/editorial approval.",
              "- Reject substantive design or product reinterpretations before code generation.",
              "- Build in an isolated workspace. No deployment, real side effects or changes to Baseline A without separate authorization.",
              "- Verify running browser behavior, accessibility, responsive screenshots and task states; technical checks alone are insufficient.",
              "- The owner/editor separately reviews the rendered design and decides publication."]
    return "\n".join(lines) + "\n"


def cli(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("questions", "validate-qa", "check-brief"):
        cmd = sub.add_parser(name)
        cmd.add_argument("run", type=Path)
        cmd.add_argument("qa", type=Path)
        if name == "check-brief":
            cmd.add_argument("brief", type=Path)
    compile_p = sub.add_parser("compile-aba")
    compile_p.add_argument("run", type=Path)
    compile_p.add_argument("qa", type=Path)
    compile_p.add_argument("brief", type=Path)
    compile_p.add_argument("--out", type=Path, required=True)
    compile_p.add_argument("--manifest", type=Path)
    args = p.parse_args(argv)
    run, qa = read_json(args.run), read_json(args.qa)
    errors = audit_questions(run, qa) if args.cmd != "check-brief" else validate_experience(run, qa, read_json(args.brief))
    if args.cmd == "compile-aba":
        errors = validate_experience(run, qa, read_json(args.brief))
    if errors:
        for e in errors:
            print(f"BLOCKED: {e}", file=sys.stderr)
        return 1
    if args.cmd == "validate-qa":
        print("QA VALID — record is structurally consistent; no human approval inferred")
    elif args.cmd == "questions":
        print(json.dumps(question_packet(run, qa), ensure_ascii=False, indent=2))
    elif args.cmd == "check-brief":
        print("BRIEF VALID — input gates recorded; no real builder execution or customer validation inferred")
    elif args.cmd == "compile-aba":
        brief = read_json(args.brief)
        spec = render_spec(run, qa, brief)
        manifest_path = args.manifest or args.out.with_suffix(".manifest.json")
        if args.out == manifest_path or args.out.exists() or manifest_path.exists():
            print("BLOCKED: output exists or collides; refusing overwrite", file=sys.stderr)
            return 2
        manifest = {
            "schema_version": "pef.aba-handoff.v1", "run_id":run["run_id"],
            "run_sha256": hash_data(run), "questions_sha256": hash_data(qa),
            "experience_sha256": hash_data(brief),
            "spec_sha256": hashlib.sha256(spec.encode("utf-8")).hexdigest(),
            "approved_position": brief["position"]["decision_id"],
            "creative_approval_ref": brief["review"]["approval_ref"],
            "builder":"app-builder-automation", "status":"compiled_not_executed",
            "deployment_authorized": False
        }
        args.out.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(spec, encoding="utf-8")
        manifest_path.write_bytes(encoded(manifest))
        print(f"ABA INPUT COMPILED: {args.out}; manifest: {manifest_path}. No ABA execution authorized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())

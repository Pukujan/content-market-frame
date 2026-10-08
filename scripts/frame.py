#!/usr/bin/env python3
"""Content Market Frame: portable, context-lean run records (stdlib only).

This is a small workflow helper, not a language-model judge or JSON Schema engine.
Validate structural invariants, create handoff packets, and invalidate stale decisions.
Owner approval is recorded, never inferred or granted by this program.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

STAGES = (
    "S0_intake", "S1_truth", "S2_human", "S3_position",
    "S4_story", "S5_creative_handoff", "S6_qa"
)
FACT_STATES = {"observed", "owner_direction", "inferred", "proposed", "unknown", "disputed", "rejected"}
DECISION_STATES = {"proposed", "accepted", "rejected", "superseded", "stale"}
GATE_STATES = {"draft", "review", "accepted", "rejected", "stale"}
SENSITIVE = {"private"}
MAX_HANDOFF_WORDS = 450
HUMAN_APPROVAL_STAGES = {"S3_position", "S4_story", "S6_qa"}


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def make_run(run_id: str, project_id: str, repo: str, source_ref: str,
             subject: str, objective: str, visibility: str = "public") -> dict:
    return {
        "schema_version": "cmf.run.v1",
        "run_id": run_id,
        "project": {
            "id": project_id, "repo": repo, "source_ref": source_ref,
            "visibility": visibility, "product_subject": subject
        },
        "objective": objective,
        "active_stage": STAGES[0],
        "gates": {stage: {"status": "draft", "reason": "Not reviewed"} for stage in STAGES},
        "facts": [], "decisions": [], "rejections": [], "scenes": [], "claims": [],
        "handoff": {
            "summary": "", "fact_ids": [], "decision_ids": [],
            "open_questions": [], "next_action": "Verify product scope and evidence"
        },
        "history": [{"at": utc_now(), "action": "initialized", "detail": "Run created; nothing approved"}]
    }


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def save(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate_run(run: dict) -> list[str]:
    errors = []
    if not isinstance(run, dict):
        return ["Run must be a JSON object"]
    required = (
        "schema_version", "run_id", "project", "objective", "active_stage",
        "gates", "facts", "decisions", "rejections", "scenes", "claims",
        "handoff", "history"
    )
    errors.extend(f"Missing {k}" for k in required if k not in run)
    if errors:
        return errors
    if run["schema_version"] != "cmf.run.v1":
        errors.append("schema_version must be cmf.run.v1")
    if run["active_stage"] not in STAGES:
        errors.append("Unknown active_stage")
    project = run["project"]
    if not isinstance(project, dict):
        return errors + ["project must be an object"]
    for k in ("id", "repo", "source_ref", "visibility", "product_subject"):
        if not isinstance(project.get(k), str) or not project.get(k):
            errors.append(f"project.{k} must be a non-empty string")
    if project.get("visibility") not in ("public", "private", "mixed"):
        errors.append("Invalid project visibility")
    for k in ("facts", "decisions", "rejections", "scenes", "claims", "history"):
        if not isinstance(run[k], list):
            errors.append(f"{k} must be a list")
    if errors:
        return errors

    gates = run["gates"]
    if not isinstance(gates, dict) or set(gates) != set(STAGES):
        return errors + ["gates must have exactly the seven declared stage keys"]
    for stage in STAGES:
        gate = gates[stage]
        if not isinstance(gate, dict) or gate.get("status") not in GATE_STATES:
            errors.append(f"Invalid gate state at {stage}")
            continue
        if gate["status"] == "accepted" and stage in HUMAN_APPROVAL_STAGES:
            if not gate.get("approved_by") or not gate.get("approval_ref"):
                errors.append(f"{stage} accepted without approved_by and approval_ref")
    if not isinstance(run["handoff"], dict):
        return errors + ["handoff must be an object"]
    h = run["handoff"]
    for k in ("summary", "next_action"):
        if not isinstance(h.get(k), str):
            errors.append(f"handoff.{k} must be a string")
    for k in ("fact_ids", "decision_ids", "open_questions"):
        if not isinstance(h.get(k), list):
            errors.append(f"handoff.{k} must be a list")
    if errors:
        return errors

    ids = {}
    for collection, prefix in (
        ("facts", "F"), ("decisions", "D"), ("rejections", "R"),
        ("scenes", "SC"), ("claims", "C")
    ):
        local = set()
        for item in run[collection]:
            if not isinstance(item, dict) or not isinstance(item.get("id"), str):
                errors.append(f"{collection} has entry missing id")
                continue
            key = item["id"]
            if not re.fullmatch(rf"{prefix}[0-9]+", key):
                errors.append(f"Invalid {collection} id: {key}")
            if key in local:
                errors.append(f"Duplicate {collection} id: {key}")
            local.add(key)
        ids[collection] = local

    for fact in run["facts"]:
        if fact.get("status") not in FACT_STATES:
            errors.append(f"Invalid fact status: {fact.get('id')}")
        if not isinstance(fact.get("source_refs"), list):
            errors.append(f"Missing fact sources: {fact.get('id')}")
        elif fact.get("status") in ("observed", "owner_direction") and not fact["source_refs"]:
            errors.append(f"Observed/owner fact needs source ref: {fact.get('id')}")
        if project.get("visibility") == "public" and fact.get("visibility") == "private":
            errors.append(f"Private source content in public run: {fact.get('id')}")
    for decision in run["decisions"]:
        if decision.get("status") not in DECISION_STATES:
            errors.append(f"Invalid decision status: {decision.get('id')}")
        if decision.get("status") == "accepted":
            if not decision.get("reviewed_by") or not decision.get("approval_ref"):
                errors.append(f"Accepted decision lacks reviewer and approval ref: {decision.get('id')}")
        for ref in decision.get("fact_ids", []):
            if ref not in ids["facts"]:
                errors.append(f"Decision {decision.get('id')} references missing fact {ref}")
        for ref in decision.get("supersedes", []):
            if ref not in ids["decisions"]:
                errors.append(f"Decision {decision.get('id')} supersedes missing decision {ref}")
    for rejection in run["rejections"]:
        for ref in rejection.get("affected_decision_ids", []):
            if ref not in ids["decisions"]:
                errors.append(f"Rejection {rejection.get('id')} references missing decision {ref}")
    for scene in run["scenes"]:
        if scene.get("status") not in GATE_STATES:
            errors.append(f"Invalid scene status: {scene.get('id')}")
        for ref in scene.get("depends_on_decisions", []):
            if ref not in ids["decisions"]:
                errors.append(f"Scene {scene.get('id')} references missing decision {ref}")
        for ref in scene.get("claim_ids", []):
            if ref not in ids["claims"]:
                errors.append(f"Scene {scene.get('id')} references missing claim {ref}")
        if scene.get("status") == "accepted" and any(
            d.get("status") != "accepted"
            for d in run["decisions"] if d["id"] in scene.get("depends_on_decisions", [])
        ):
            errors.append(f"Accepted scene depends on unaccepted decision: {scene.get('id')}")
    for ref in h["fact_ids"]:
        if ref not in ids["facts"]:
            errors.append(f"Handoff references missing fact {ref}")
    for ref in h["decision_ids"]:
        if ref not in ids["decisions"]:
            errors.append(f"Handoff references missing decision {ref}")
    for stage in STAGES[:STAGES.index(run["active_stage"])]:
        if gates[stage]["status"] != "accepted":
            errors.append(f"Cannot be at {run['active_stage']}: previous gate {stage} not accepted")
    return errors


def packet(run: dict) -> dict:
    facts = {item["id"]: item for item in run["facts"]}
    decisions = {item["id"]: item for item in run["decisions"]}
    h = run["handoff"]
    out = {
        "run_id": run["run_id"],
        "target_stage": run["active_stage"],
        "source_repo": run["project"]["repo"],
        "source_ref": run["project"]["source_ref"],
        "product_subject": run["project"]["product_subject"],
        "summary": h["summary"],
        "facts": [
            {"id": f["id"], "status": f["status"], "statement": f["statement"], "sources": f["source_refs"]}
            for ref in h["fact_ids"] if (f := facts.get(ref)) is not None
        ],
        "decisions": [
            {"id": d["id"], "status": d["status"], "kind": d["kind"], "statement": d["statement"]}
            for ref in h["decision_ids"] if (d := decisions.get(ref)) is not None
        ],
        "rejections": [
            {"class": r["failure_class"], "why": r["why"]}
            for r in run["rejections"][-5:]
        ],
        "open_questions": h["open_questions"],
        "next_action": h["next_action"],
        "gate_status": {k: v["status"] for k, v in run["gates"].items()},
        "rule": "Follow source refs as needed. Never infer approval from generation or tests. Do not load raw conversation by default."
    }
    words = len(json.dumps(out, ensure_ascii=False).split())
    if words > MAX_HANDOFF_WORDS:
        raise ValueError(f"Packet has {words} words, budget is {MAX_HANDOFF_WORDS}; summarize deliberately, do not silently truncate")
    return out


def invalidate(run: dict, decision_id: str, reason: str) -> list[str]:
    decisions = {d["id"]: d for d in run["decisions"]}
    if decision_id not in decisions:
        raise ValueError(f"No such decision: {decision_id}")
    affected = {decision_id}
    changed = True
    while changed:
        changed = False
        for d in run["decisions"]:
            if d["id"] not in affected and any(x in affected for x in d.get("supersedes", [])):
                affected.add(d["id"])
                changed = True
    for ref in affected:
        decisions[ref]["status"] = "stale"
    stale_scenes = []
    for scene in run["scenes"]:
        if any(ref in affected for ref in scene.get("depends_on_decisions", [])):
            scene["status"] = "stale"
            stale_scenes.append(scene["id"])
    for stage in STAGES[3:]:
        run["gates"][stage]["status"] = "stale"
        run["gates"][stage]["reason"] = f"Invalidated: {decision_id} — {reason}"
        run["gates"][stage].pop("approved_by", None)
        run["gates"][stage].pop("approval_ref", None)
    run["active_stage"] = "S3_position"
    run["history"].append({
        "at": utc_now(), "action": "invalidated",
        "detail": f"{decision_id}: {reason}; downstream decisions {sorted(affected)} and scenes {stale_scenes} stale"
    })
    return stale_scenes


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="Create a new draft run; no gates accepted")
    init.add_argument("--run-id", required=True)
    init.add_argument("--project-id", required=True)
    init.add_argument("--repo", required=True)
    init.add_argument("--ref", required=True)
    init.add_argument("--subject", required=True)
    init.add_argument("--objective", required=True)
    init.add_argument("--visibility", choices=("public", "private", "mixed"), default="public")
    init.add_argument("--out", required=True, type=Path)
    val = sub.add_parser("validate", help="Validate references, approval gates, privacy and stage invariants")
    val.add_argument("run", type=Path)
    pack = sub.add_parser("pack", help="Emit an explicit bounded agent handoff packet to stdout")
    pack.add_argument("run", type=Path)
    inv = sub.add_parser("invalidate", help="Mark a decision and its dependent scenes/gates stale")
    inv.add_argument("run", type=Path)
    inv.add_argument("--decision", required=True)
    inv.add_argument("--reason", required=True)
    inv.add_argument("--out", type=Path, help="Recommended: write a new revision instead of overwriting")
    args = p.parse_args(argv)
    if args.command == "init":
        if args.out.exists():
            p.error("Output exists; refusing to overwrite")
        save(args.out, make_run(args.run_id, args.project_id, args.repo, args.ref,
                                args.subject, args.objective, args.visibility))
        print(f"DRAFT run created: {args.out}")
        return 0

    run = load(args.run)
    errors = validate_run(run)
    if errors:
        for error in errors:
            print(f"INVALID: {error}", file=sys.stderr)
        return 1
    if args.command == "validate":
        print(f"VALID: {run['run_id']} at {run['active_stage']}; no editorial approval inferred")
    elif args.command == "pack":
        try:
            print(json.dumps(packet(run), ensure_ascii=False, indent=2))
        except ValueError as exc:
            print(f"PACKET BLOCKED: {exc}", file=sys.stderr)
            return 2
    elif args.command == "invalidate":
        if not args.reason.strip():
            p.error("reason cannot be blank")
        stale_scenes = invalidate(run, args.decision, args.reason)
        target = args.out or args.run
        if target != args.run and target.exists():
            p.error("Output exists; refusing to overwrite")
        save(target, run)
        print(f"Marked {len(stale_scenes)} dependent scenes STALE in {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

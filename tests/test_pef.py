"""PEF acceptance, privacy, traceability and builder-safety regression tests."""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import frame
import pef


class PefTests(unittest.TestCase):
    def setUp(self):
        self.run = frame.make_run("test-only-pef", "example", "https://github.com/example/product",
                                  "a" * 40, "Example integrated product",
                                  "Explain a user's needs and design a truthful experience")
        self.run["facts"] = [
            {"id": "F1", "statement": "A particular user task was observed",
             "status": "observed", "source_refs": ["https://example.test/research"], "visibility": "public"},
            {"id": "F2", "statement": "The owner directs a specific problem focus",
             "status": "owner_direction", "source_refs": ["issue/test-only"], "visibility": "public"}
        ]
        self.run["decisions"] = [
            {"id": "D1", "kind": "positioning", "status": "accepted",
             "statement": "Lead with the actual human job", "reason": "Owner preference",
             "fact_ids": ["F1", "F2"], "reviewed_by": "test-reviewer", "approval_ref": "test-only/owner-position"},
            {"id": "D2", "kind": "story", "status": "accepted",
             "statement": "Show the problem and then the useful mechanism", "reason": "Story QA",
             "fact_ids": ["F1"], "reviewed_by": "test-reviewer", "approval_ref": "test-only/owner-story"}
        ]
        self.run["claims"] = [{
            "id": "C1", "wording": "The product exposes a reviewed setup status",
            "claim_type": "mechanism", "source_refs": ["https://example.test/contracts"],
            "status": "verified"
        }]
        self.run["scenes"] = [{
            "id": "SC1", "question": "Why care?", "belief_change": "Understand project friction",
            "visual_job": "Show actual project context",
            "depends_on_decisions": ["D1","D2"], "claim_ids": ["C1"], "status": "accepted"
        }]
        for stage in pef.PRE_BUILD_STAGES:
            self.run["gates"][stage] = {"status": "accepted", "reason": "Test-only gate"}
        for s in ("S3_position", "S4_story", "S5_creative_handoff"):
            self.run["gates"][s].update(approved_by="test-reviewer", approval_ref="test-only/owner-creative")
        self.run["active_stage"] = "S6_qa"
        self.qa = {
            "schema_version": "pef.questions.v1", "run_id": self.run["run_id"],
            "questions": [{
                "id": "Q1", "status": "answered", "impact": "high", "blocking": True,
                "question": "Which customer group is primary?",
                "why_ambiguous": "Two plausible audiences",
                "consequence": "Change the protagonist and CTA",
                "evidence_fact_ids": ["F1"], "affected_decision_ids": ["D1"],
                "options": [{"id": "A", "label": "Individual worker"},{"id": "B", "label": "Team lead"}],
                "recommended_option_id": "A",
                "answer": {"choice_id": "A", "answered_by": "test-reviewer", "answer_ref": "test-only/owner-Q1"}
            }]
        }
        self.brief = {
            "schema_version": "pef.experience.v1", "run_id": self.run["run_id"],
            "source_revision": self.run["project"]["source_ref"],
            "intent": {"creator_purpose": "Make real project work less fragmented",
                       "user_need": "See and use the right current project status",
                       "user_need_status": "observed_user_research", "evidence_fact_ids": ["F1"]},
            "audience": {"actor": "An individual maintainer", "job": "Resume an ongoing project safely",
                         "trigger": "A later session starts", "workaround": "Read lots of prior chat"},
            "position": {"decision_id": "D1", "promise": "Return attention to the real project",
                         "claim_ids": ["C1"], "limitations": ["No quantified time savings claimed"]},
            "buyer_journey": [{"scene_id": "SC1", "belief_change": "Understand recurring friction",
                               "message": "Work stalls when context disappears"}],
            "ux_tasks": [{"id": "T1", "scenario": "A reader previews the setup process",
                          "success": "Can distinguish preview from local installation",
                          "states": ["default", "loading", "ready", "error"]}],
            "service_touchpoints": [{
                "task_id": "T1", "visible": "Read-only setup example",
                "backstage": "Local display with no mutations", "authority_ref": "https://example.test/contracts",
                "limitation": "Does not install anything"
            }],
            "creative": {"headline": "Get back to the work", "outline": ["Friction", "Mechanism", "Safe next step"],
                         "visual_roles": [{"scene_id": "SC1", "purpose": "Show interrupted work"}],
                         "acceptance_tests": ["Preview must not write to a repo"],
                         "forbidden_inherited_patterns": ["Process-audit hero"]},
            "cta": {"label": "Preview the workflow", "behavior": "read_only_preview",
                    "behavior_verified": True, "side_effects": "None",
                    "authority_ref": "https://example.test/contracts"},
            "review": {"status": "approved", "approved_by": "test-reviewer",
                       "approval_ref": "test-only/owner-creative"}
        }

    def test_approved_structural_fixture_compiles(self):
        self.assertEqual([], frame.validate_run(self.run))
        self.assertEqual([], pef.audit_questions(self.run, self.qa))
        self.assertEqual([], pef.validate_experience(self.run, self.qa, self.brief))
        spec = pef.render_spec(self.run, self.qa, self.brief)
        self.assertIn("App Builder Automation", spec)
        self.assertIn("No deployment", spec)
        self.assertNotIn("CGM HTML demo", spec.split("## Builder boundary")[0])
        self.assertEqual(spec, pef.render_spec(self.run, self.qa, self.brief))

    def test_unaccepted_marketing_gate_blocks(self):
        self.run["gates"]["S4_story"]["status"] = "review"
        self.assertTrue(any("S4_story" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_no_owner_provenance_blocks(self):
        self.run["gates"]["S5_creative_handoff"].pop("approval_ref")
        self.assertTrue(any("signoff" in e or "approval" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_unpinned_source_blocks(self):
        self.run["project"]["source_ref"] = "UNPINNED: main"
        self.brief["source_revision"] = "UNPINNED: main"
        self.assertTrue(any("concrete" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_unanswered_blocking_qa_blocks(self):
        self.qa["questions"][0]["status"] = "open"
        self.qa["questions"][0].pop("answer")
        self.assertTrue(any("Blocking owner QA" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_answer_qa_not_approval_of_decision(self):
        self.run["decisions"][0]["status"] = "proposed"
        self.assertTrue(any("positioning decision not accepted" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_observed_user_need_cannot_be_owner_only(self):
        self.run["facts"][0]["status"] = "owner_direction"
        self.assertTrue(any("Observed user need" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_claim_must_be_verified(self):
        self.run["claims"][0]["status"] = "unverified"
        self.assertTrue(any("Unverified" in e or "unverified" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_stale_scene_blocks(self):
        self.run["scenes"][0]["status"] = "stale"
        self.assertTrue(any("scene unaccepted" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_readonly_preview_must_be_verified(self):
        self.brief["cta"]["behavior_verified"] = False
        self.assertTrue(any("CTA action" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_local_action_needs_service_touchpoint(self):
        self.brief["cta"]["behavior"] = "local_action"
        self.brief["service_touchpoints"] = []
        self.assertTrue(any("service blueprint" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_wrong_brief_revision_blocks(self):
        self.brief["source_revision"] = "b" * 40
        self.assertTrue(any("revision" in e for e in pef.validate_experience(self.run, self.qa, self.brief)))

    def test_qa_answer_requires_provenance(self):
        self.qa["questions"][0]["answer"].pop("answer_ref")
        self.assertTrue(any("provenance" in e for e in pef.audit_questions(self.run, self.qa)))

    def test_qa_correction_requires_explanation(self):
        self.qa["questions"][0]["options"].append({"id": "other", "label": "Something different"})
        self.qa["questions"][0]["answer"]["choice_id"] = "other"
        self.assertTrue(any("concrete correction" in e for e in pef.audit_questions(self.run, self.qa)))

    def test_open_qa_packet_is_bounded(self):
        for i in range(1, 7):
            q = dict(self.qa["questions"][0])
            q["id"] = f"Q{i}"
            q["status"] = "open"
            q.pop("answer", None)
            q["impact"] = "critical" if i == 6 else "low"
            self.qa["questions"].append(q)
        self.qa["questions"].pop(0)
        packet = pef.question_packet(self.run, self.qa)
        self.assertEqual(3, len(packet["questions"]))
        self.assertEqual("Q6", packet["questions"][0]["id"])
        self.assertEqual(3, packet["remaining_unanswered"])
        self.assertEqual(6, packet["blocking_total"])

    def test_nonblocking_qa_does_not_silently_approve(self):
        self.qa["questions"][0]["status"] = "deferred"
        self.qa["questions"][0].pop("answer")
        self.qa["questions"][0]["blocking"] = False
        self.assertEqual([], pef.validate_experience(self.run, self.qa, self.brief))
        self.assertEqual("deferred", self.qa["questions"][0]["status"])

    def test_cli_compiles_with_manifest_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for key, value in (("run", self.run), ("qa", self.qa), ("brief", self.brief)):
                (root / f"{key}.json").write_text(json.dumps(value), encoding="utf-8")
            path = root / "aba.md"
            argv = ["compile-aba", root / "run.json", root / "qa.json", root / "brief.json", "--out", path]
            self.assertEqual(0, pef.cli(list(map(str, argv))))
            manifest = json.loads((root / "aba.manifest.json").read_text())
            self.assertEqual("compiled_not_executed", manifest["status"])
            self.assertFalse(manifest["deployment_authorized"])
            self.assertEqual(2, pef.cli(list(map(str, argv))))


if __name__ == "__main__":
    unittest.main()

"""Regression tests for the context-lean framing router (no network or API needed)."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "frame.py"
SPEC = importlib.util.spec_from_file_location("frame", MODULE)
frame = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(frame)


class RouterTests(unittest.TestCase):
    def run_record(self):
        return frame.make_run(
            "sample-001", "example-project", "https://github.com/example/project",
            "commit-abc", "An example repo-installed product",
            "Create a human-centered product story before generating a page"
        )

    def test_fresh_run_is_draft_and_valid(self):
        record = self.run_record()
        self.assertEqual([], frame.validate_run(record))
        self.assertTrue(all(v["status"] == "draft" for v in record["gates"].values()))
        self.assertEqual("S0_intake", record["active_stage"])

    def test_accepted_human_gate_requires_provenance(self):
        record = self.run_record()
        record["gates"]["S3_position"]["status"] = "accepted"
        self.assertTrue(any("approved_by" in x for x in frame.validate_run(record)))
        record["gates"]["S3_position"]["approved_by"] = "human-editor"
        record["gates"]["S3_position"]["approval_ref"] = "decision/approval-123"
        self.assertEqual([], frame.validate_run(record))

    def test_cannot_skip_unaccepted_stages(self):
        record = self.run_record()
        record["active_stage"] = "S3_position"
        errors = frame.validate_run(record)
        self.assertTrue(any("previous gate" in x for x in errors))

    def test_public_record_does_not_embed_private_fact(self):
        record = self.run_record()
        record["facts"].append({
            "id": "F1", "statement": "Sensitive raw owner details",
            "status": "observed", "source_refs": ["private-source"],
            "visibility": "private"
        })
        self.assertTrue(any("Private source" in x for x in frame.validate_run(record)))

    def test_observed_fact_requires_source(self):
        record = self.run_record()
        record["facts"].append({
            "id": "F1", "statement": "Undocumented assertion",
            "status": "observed", "source_refs": [], "visibility": "public"
        })
        self.assertTrue(any("needs source" in x for x in frame.validate_run(record)))

    def test_accepted_decision_needs_explicit_review(self):
        record = self.run_record()
        record["decisions"].append({
            "id": "D1", "kind": "positioning", "status": "accepted",
            "statement": "Lead with human needs", "reason": "Recognizable pain",
            "fact_ids": []
        })
        self.assertTrue(any("Accepted decision lacks" in x for x in frame.validate_run(record)))

    def test_broken_reference_rejected(self):
        record = self.run_record()
        record["handoff"]["fact_ids"] = ["F999"]
        self.assertTrue(any("missing fact" in x for x in frame.validate_run(record)))

    def test_packet_only_relevant_refs(self):
        record = self.run_record()
        record["facts"] = [
            {"id": "F1", "statement": "The current contract records a local install",
             "status": "observed", "source_refs": ["https://example.org/source"],
             "visibility": "public"},
            {"id": "F2", "statement": "Irrelevant historical long fact",
             "status": "inferred", "source_refs": [], "visibility": "public"}
        ]
        record["handoff"]["fact_ids"] = ["F1"]
        packet = frame.packet(record)
        self.assertEqual(["F1"], [f["id"] for f in packet["facts"]])
        self.assertNotIn("F2", json.dumps(packet))
        self.assertLessEqual(len(json.dumps(packet).split()), frame.MAX_HANDOFF_WORDS)

    def test_packet_refuses_excess_context(self):
        record = self.run_record()
        record["handoff"]["summary"] = "word " * (frame.MAX_HANDOFF_WORDS + 5)
        with self.assertRaisesRegex(ValueError, "budget"):
            frame.packet(record)

    def test_correction_invalidates_downstream_scenes(self):
        record = self.run_record()
        record["decisions"] = [{
            "id": "D1", "kind": "positioning", "status": "proposed",
            "statement": "Old project framing", "reason": "Working hypothesis", "fact_ids": []
        }]
        record["scenes"] = [{
            "id": "SC1", "question": "Why care?", "belief_change": "Old story",
            "visual_job": "Show old focus", "depends_on_decisions": ["D1"],
            "claim_ids": [], "status": "draft"
        }]
        stale = frame.invalidate(record, "D1", "Owner rejected old premise")
        self.assertEqual(["SC1"], stale)
        self.assertEqual("stale", record["scenes"][0]["status"])
        self.assertEqual("stale", record["decisions"][0]["status"])
        self.assertEqual("stale", record["gates"]["S4_story"]["status"])
        self.assertEqual("S3_position", record["active_stage"])

    def test_round_trip_in_local_file(self):
        record = self.run_record()
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "run.json"
            frame.save(path, record)
            self.assertEqual(record, frame.load(path))
            self.assertEqual([], frame.validate_run(frame.load(path)))


if __name__ == "__main__":
    unittest.main()

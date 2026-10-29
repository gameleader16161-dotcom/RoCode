"""RoCode behavior and installation checks. Copyright (c) 2026 QFR Studios."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "skills" / "rocode" / "scripts" / "brief.py"


def module_from(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


brief = module_from("rocode_brief_tests", CLI)
installer = module_from("rocode_installer_tests", ROOT / "scripts" / "install.py")
package = module_from("rocode_package_tests", ROOT / "scripts" / "check_package.py")


def temporary_workspace():
    scratch = ROOT / "work" / "tests"
    scratch.mkdir(parents=True, exist_ok=True)
    return tempfile.TemporaryDirectory(dir=scratch)


class BriefTests(unittest.TestCase):
    def setUp(self):
        self.temp = temporary_workspace()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "brief.json"

    def run_cli(self, *arguments, code=0):
        result = subprocess.run([sys.executable, str(CLI), "--file", str(self.path), *arguments],
                                text=True, encoding="utf-8", capture_output=True)
        self.assertEqual(result.returncode, code, result.stderr)
        return json.loads(result.stdout) if code == 0 else result.stderr

    def test_style_is_first_and_saved_answer_advances(self):
        self.run_cli("init")
        self.assertEqual(self.run_cli("next")["next"]["field"], "style")
        self.run_cli("set", "style", "كلاسيكي")
        self.assertEqual(self.run_cli("next")["next"]["field"], "treatment")
        self.assertEqual(brief.load(self.path)["decisions"]["style"]["value"], "كلاسيكي")

    def test_multiple_answers_are_not_reasked(self):
        self.run_cli("init")
        for field in ["style", "treatment", "gameplay", "setting", "scope", "devices"]:
            self.run_cli("set", field, "provided together")
        result = self.run_cli("next")
        self.assertEqual(result["next"]["field"], "audience")
        self.assertTrue(result["can_offer_build"])

    def test_proposal_is_not_a_user_answer(self):
        self.run_cli("init")
        self.run_cli("set", "style", "futuristic", "--source", "proposed")
        self.assertEqual(self.run_cli("next")["next"]["field"], "style")
        self.assertFalse(self.run_cli("next")["can_offer_build"])

    def test_agreed_mode_rejects_missing_core_choices(self):
        self.run_cli("init")
        self.run_cli("ready", "--mode", "agreed", "--user-quote", "Start", code=2)
        self.assertEqual(brief.load(self.path)["phase"], "interview")

    def test_explicit_delegation_allows_start_and_keeps_unknowns_honest(self):
        self.run_cli("init")
        result = self.run_cli("ready", "--mode", "delegated", "--user-quote", "اختار الباقي وابدأ")
        self.assertEqual(result["phase"], "ready")
        self.assertIn("style", result["unresolved"])
        self.assertEqual(brief.load(self.path)["decisions"], {})
        self.assertIsNone(self.run_cli("next")["next"])

    def test_start_now_ends_questions_without_fake_answers(self):
        self.run_cli("init")
        self.run_cli("ready", "--mode", "start-now", "--user-quote", "Enough questions, start")
        self.assertIsNone(self.run_cli("next")["next"])

    def test_empty_start_quote_rejected(self):
        self.run_cli("init")
        self.run_cli("ready", "--mode", "delegated", "--user-quote", "  ", code=2)

    def test_changed_choice_invalidates_checkpoint_and_preserves_history(self):
        self.run_cli("init")
        self.run_cli("set", "style", "classic")
        self.run_cli("ready", "--mode", "delegated", "--user-quote", "Start")
        self.run_cli("set", "style", "futuristic")
        data = brief.load(self.path)
        self.assertEqual(data["phase"], "interview")
        self.assertIsNone(data["checkpoint"])
        self.assertEqual(data["history"][-1]["previous"]["value"], "classic")

    def test_no_gui_skips_gui_style(self):
        data = brief.new_brief("map")
        data["decisions"]["gui"] = {"value": "none", "source": "user"}
        self.assertNotIn("gui_style", dict(brief.pending(data)))

    def test_proposed_no_gui_does_not_silently_skip_branch(self):
        data = brief.new_brief("map")
        data["decisions"]["gui"] = {"value": "none", "source": "proposed"}
        self.assertIn("gui_style", dict(brief.pending(data)))

    def test_gui_interview_skips_geography(self):
        self.run_cli("init", "--kind", "gui")
        keys = dict(brief.pending(brief.load(self.path)))
        self.assertNotIn("setting", keys)
        self.assertNotIn("zones", keys)
        self.assertNotIn("landmark", keys)
        self.assertIn("gui_style", keys)

    def test_init_cannot_destroy_previous_answers(self):
        self.run_cli("init")
        self.run_cli("set", "style", "classic")
        before = self.path.read_bytes()
        self.run_cli("init", code=2)
        self.assertEqual(before, self.path.read_bytes())

    def test_empty_answer_rejected(self):
        self.run_cli("init")
        self.run_cli("set", "style", " ", code=2)

    def test_corrupt_schema_reports_failure(self):
        self.path.write_text('{"schema_version": 900}', encoding="utf-8")
        self.run_cli("validate", code=2)

    def test_checkpoint_required_for_ready_phase(self):
        data = brief.new_brief("map")
        data["phase"] = "ready"
        with self.assertRaises(ValueError):
            brief.validate(data)


class InstallAndPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = temporary_workspace()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.source = ROOT / "skills" / "rocode"

    def test_local_install_includes_attribution_and_nested_resources(self):
        destination = installer.install(self.source, self.folder / "skills")
        self.assertTrue((destination / "references" / "interview.md").is_file())
        self.assertEqual((destination / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())
        self.assertIn("QFR Studios", (destination / "NOTICE").read_text())

    def test_existing_install_never_overwritten(self):
        parent = self.folder / "skills"
        destination = installer.install(self.source, parent)
        sentinel = destination / "user-note.txt"
        sentinel.write_text("preserve me")
        with self.assertRaises(FileExistsError):
            installer.install(self.source, parent)
        self.assertEqual(sentinel.read_text(), "preserve me")

    def test_nested_destination_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(self.source, self.source / "nested")

    def test_missing_source_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(self.folder, self.folder / "skills")

    def test_package_integrity(self):
        self.assertEqual(package.check(), [])


if __name__ == "__main__":
    unittest.main()

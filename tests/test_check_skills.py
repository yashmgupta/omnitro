import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("check_skills", ROOT / "scripts" / "check_skills.py")
check_skills = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_skills)


class SkillChecks(unittest.TestCase):
    def run_check(self, text, directory="example"):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / directory / "SKILL.md"
            path.parent.mkdir()
            path.write_text(text, encoding="utf-8")
            return check_skills.check(path)

    def test_valid_single_line_description(self):
        self.assertEqual(self.run_check("---\nname: example\ndescription: Help research.\n---\n# Instructions\n"), [])

    def test_valid_folded_description(self):
        self.assertEqual(self.run_check("---\nname: example\ndescription: >\n  Help research\n  and analysis.\nlicense: CC-BY-4.0\n---\n# Instructions\n"), [])

    def test_invalid_names_and_missing_instructions(self):
        errors = self.run_check("---\nname: Bad_Name\ndescription: Test.\n---\n")
        self.assertTrue(any("invalid skill name" in error for error in errors))
        self.assertTrue(any("parent directory" in error for error in errors))
        self.assertTrue(any("instructions are empty" in error for error in errors))

    def test_missing_and_long_descriptions(self):
        for description in ("", "x" * 1025):
            errors = self.run_check(f"---\nname: example\ndescription: {description}\n---\n# Instructions\n")
            self.assertTrue(any("description must" in error for error in errors))

    def test_missing_delimiter_and_duplicate_field(self):
        self.assertTrue(self.run_check("name: example"))
        errors = self.run_check("---\nname: example\nname: example\ndescription: Test.\n---\n# Instructions\n")
        self.assertTrue(any("duplicate metadata" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

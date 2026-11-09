import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("build_index", ROOT / "scripts" / "build_index.py")
build_index = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_index)


class IndexBuilder(unittest.TestCase):
    def setUp(self):
        self.skills = build_index.load_skills()
        self.categories = build_index.load_categories()

    def test_every_skill_categorized_exactly_once(self):
        self.assertEqual(build_index.validate(self.skills, self.categories), [])

    def test_uncategorized_skill_is_reported(self):
        skills = dict(self.skills)
        skills["ghost-skill"] = {"name": "ghost-skill"}
        errors = build_index.validate(skills, self.categories)
        self.assertTrue(any("ghost-skill" in e for e in errors))

    def test_unknown_category_member_is_reported(self):
        cats = {"X": {"summary": "s", "skills": ["does-not-exist"]}}
        self.assertTrue(build_index.validate({}, cats))

    def test_generated_files_are_current(self):
        outputs = build_index.render(self.skills, self.categories)
        for name, text in outputs.items():
            self.assertEqual((ROOT / name).read_text(encoding="utf-8"), text, f"{name} is stale")

    def test_json_index_is_well_formed(self):
        data = json.loads(build_index.render(self.skills, self.categories)["skills-index.json"])
        self.assertEqual(data["count"], len(self.skills))
        self.assertEqual(sum(len(c["skills"]) for c in data["categories"]), len(self.skills))

    def test_folded_description_is_parsed(self):
        self.assertGreater(len(self.skills["statistical-power"]["description"]), 40)
        self.assertNotEqual(self.skills["statistical-power"]["description"], ">")


if __name__ == "__main__":
    unittest.main()

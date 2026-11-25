"""Checks on this skill's SKILL.md and examples. Run: python3 -m unittest discover -s tests"""
import pathlib, re, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = next(p for p in (ROOT / "skills").iterdir() if p.is_dir())
TEXT = (SKILL / "SKILL.md").read_text()
FRONT = re.match(r"---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n", TEXT, re.S)
# Invented-proof phrases the copy must never carry (a count, a rating, a results promise).
PROOF = re.compile(r"\b\d[\d,]* (?:owners|customers|people|users|businesses) (?:use|love|trust|picked|bought)|"
                   r"\brated \d|\b\d(?:\.\d)? stars?\b|guaranteed (?:views|results|leads)|go viral\b", re.I)


class Skill(unittest.TestCase):
    def test_name_follows_the_skill_rules(self):
        name = FRONT.group(1)
        self.assertLessEqual(len(name), 64)
        self.assertRegex(name, r"^[a-z0-9]+(-[a-z0-9]+)*$")
        self.assertNotIn("claude", name)
        self.assertNotIn("anthropic", name)

    def test_description_says_when_to_use_and_what_it_never_does(self):
        d = FRONT.group(2)
        self.assertLessEqual(len(d), 1024, "skill descriptions are capped at 1024 characters")
        self.assertIn("Use when", d)
        self.assertRegex(d, r"\bnever\b|\bdoesn't\b|\bNever\b")

    def test_one_job_and_the_rules_are_stated(self):
        self.assertIn("ONE job", TEXT)
        self.assertTrue("## Rules" in TEXT or "## Hard rules" in TEXT, "the skill states its rules")

    def test_worked_example_exists(self):
        for side in ("before", "after"):
            files = [p for p in (ROOT / "examples" / side).iterdir() if p.name != ".gitkeep"]
            self.assertTrue(files, f"examples/{side} holds the worked example")

    def test_no_invented_proof_in_skill_readme_or_examples(self):
        paths = [SKILL / "SKILL.md", ROOT / "README.md"] + list((ROOT / "examples").rglob("*.md"))
        for p in paths:
            self.assertIsNone(PROOF.search(p.read_text()), f"invented-proof wording in {p.relative_to(ROOT)}")

    def test_proof_check_negative_control(self):
        self.assertIsNotNone(PROOF.search("Rated 5 stars by 200 owners"))
        self.assertIsNotNone(PROOF.search("1,200 owners use it"))


if __name__ == "__main__":
    unittest.main()

"""Structure checks every Terramore skill repo keeps. Run: python3 -m unittest discover -s tests"""
import pathlib, re, subprocess, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SECRET = re.compile(r"sk_live_[A-Za-z0-9]{20,}|rk_live_[A-Za-z0-9]{20,}|sk-ant-[A-Za-z0-9_-]{40,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY")


def skill_dirs():
    return [p for p in (ROOT / "skills").iterdir() if p.is_dir()]


class Structure(unittest.TestCase):
    def test_one_skill_with_frontmatter(self):
        dirs = skill_dirs()
        self.assertEqual(len(dirs), 1, "one skill per repo")
        text = (dirs[0] / "SKILL.md").read_text()
        m = re.match(r"---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n", text, re.S)
        self.assertIsNotNone(m, "SKILL.md starts with name + description frontmatter")
        self.assertEqual(m.group(1), dirs[0].name, "frontmatter name matches the folder")
        self.assertGreater(len(m.group(2)), 60, "description says what it does and when to use it")

    def test_required_files(self):
        for f in ["README.md", "LICENSE", "TESTED.md", "GO_LIVE.md", ".gitignore"]:
            self.assertTrue((ROOT / f).exists(), f)

    def test_no_secrets_in_files(self):
        for p in ROOT.rglob("*"):
            if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts and p.suffix not in {".png", ".jpg", ".mp4", ".pyc"}:
                self.assertIsNone(SECRET.search(p.read_text(errors="ignore")), f"key-shaped text in {p.relative_to(ROOT)}")

    def test_no_env_files_tracked(self):
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.split()
        self.assertFalse([f for f in out if re.search(r"(^|/)\.env", f)], ".env files are never committed")

    def test_negative_control(self):
        self.assertIsNotNone(SECRET.search("-----BEGIN " + "PRIVATE KEY-----"), "the secret check must catch a known-bad line")


if __name__ == "__main__":
    unittest.main()

# Go-live checklist (the same rule Dream Mode passed)

A skill goes on terramore.io/skills (moved into the website's lib/skills.ts) only when every line is true:

- [ ] Repo is public, MIT, and README sections are filled (no "…" left).
- [ ] `python3 -m unittest discover -s tests` passes on a fresh clone.
- [ ] TESTED.md says what was and wasn't tested, with the date.
- [ ] Examples use made-up businesses only.
- [ ] No keys, .env files or personal data anywhere in the history (`git log -p | grep -E "sk_live_|PRIVATE KEY|AKIA"` finds nothing).
- [ ] Credits name every source and its licence.
- [ ] The website entry links this repo, and its tracked link is set (`?s=<platform>`).

First, after "Use this template": rename `skills/your-skill-name` and every `your-skill-name` to the skill's name (lowercase, hyphens).

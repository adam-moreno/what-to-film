# What was tested

2026-11-25, version 0.1.0.

**Tested**

- **Claude Code CLI 2.1.332, macOS 15.3.1, project install, from a FRESH CLONE of this repository.** The skill folder was copied into a new, empty project's `.claude/skills/`, with only project settings loaded (`--setting-sources project`) and only the Read tool allowed. Invoked headless as `/what-to-film` with `examples/before/owner-notes.md` (a made-up landscaper), asking it not to save the file yet.
  - It gave 15 ideas, 3 in each of the 5 buckets. Each had a first line and either the customer question it came from or a "check" mark.
  - It added no numbers and no tree-removal ideas (the owner said to avoid them). It asked before saving and wrote no file.
  - The output is `examples/after/what-to-film-list.md`, unedited.
- **Unit tests** (`python3 -m unittest discover -s tests`): 11 pass, from the fresh clone. The invented-proof check fails on a known-bad line ("Rated 5 stars by 200 owners").

**Not tested**

- The "top up my list" return visit (reading and refilling a saved `what-to-film.md`).
- A personal install in `~/.claude/skills/` (same mechanism as the project install, but not run).
- The Claude Code desktop app, web app and IDE extensions; the Claude apps' skill upload; the Agent SDK.
- Windows and Linux.
- Other businesses and trades, and more than one run. One run on one made-up business is not evidence that every output will be this good. Read what it gives you.
- Whether its output gets more views or customers. Nothing here measures that.

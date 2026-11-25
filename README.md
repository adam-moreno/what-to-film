# what-to-film

**A list of video ideas you can actually film, made from the questions your customers ask.** A free Claude skill from Terramore.

- **What you give it:** what you do, and the questions customers ask you.
- **What you get back:** five buckets of video ideas (how-to, behind the scenes, before and after, myths, questions), each with the first line to say on camera.
- **What it never does:** film, schedule or post anything, or make a posting calendar.

## What it does

You tell Claude what you sell and the questions you hear on the phone, at the door and in reviews. It sorts video ideas into five buckets, three per bucket, and gives each one:

- a short title;
- the first sentence to say on camera;
- the customer question it came from.

Before-and-after ideas also say what to film before you start, since you can't go back for the before shot.

If you say yes, it saves the list as `what-to-film.md` in your folder. Next time, say "top up my list". It moves what you filmed to a Filmed section and refills each bucket. There are no dates, so nothing goes stale if you skip a week.

## Requirements

- Claude Code (tested with 2.1.332 on macOS).
- Nothing else to install. No scripts.

## Install

Ask Claude: "Install the what-to-film skill from github.com/adam-moreno/what-to-film."

Or by hand. **For you, on every project:**

```sh
git clone https://github.com/adam-moreno/what-to-film.git
mkdir -p ~/.claude/skills
cp -R what-to-film/skills/what-to-film ~/.claude/skills/
```

**For one project:** copy `skills/what-to-film` into that project's `.claude/skills/` folder.

Start a new Claude Code session afterwards so the skill is picked up.

## Use

Type `/what-to-film`, or just ask: "what should I film this week?", "give me video ideas for my plumbing business", "top up my video idea list".

## Example: before and after

Real input and output from `examples/`. Made-up businesses only, never a real client.

- `examples/before/owner-notes.md`: a made-up landscaper (Quillstone Landscaping) with six customer questions and one thing to avoid (tree removal).
- `examples/after/what-to-film-list.md`: what the skill gave back in one real run. That's 15 ideas, each tied to one of the six questions, or marked "check: do customers ask about this?". No numbers were added, because none were given.

One idea from that run:

> **Mulch volcano fixed.** First line: "Somebody piled mulch up this tree like a volcano. Let's fix it." (from: "…The last guy piled it up against my tree.")
> *Before you start:* film a close-up of the mulch piled on the trunk before you touch it.

## Limitations

- **The ideas are only as good as the questions you give it.** With fewer than five, it asks for more, and it marks any question it adds as one for you to check.
- **It doesn't know what's trending.** It works from your questions and your work, on purpose.
- **It doesn't say how a video will do.** No view or follower predictions.
- **How-to ideas stay safe.** It won't suggest homeowners do licensed or dangerous work (gas, electrical panels, roofs, tree felling). Those become "signs it's time to call a pro".
- **Tested once on one made-up business** (see `TESTED.md`).

## Privacy

No telemetry. Nothing leaves your computer except what Claude Code itself sends to Claude. It writes one file, `what-to-film.md`, and only when you say yes.

## Credits

None: written by Terramore.

## Tests

`python3 -m unittest discover -s tests`

## License

MIT. Made by Terramore (terramore.io). Want the video side done for you? Terramore Studio: terramore.io/studio

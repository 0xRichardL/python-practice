# Learning Progress: Python Foundations

> Guide: [PYTHON_FOUNDATIONS_GUIDE.md](./PYTHON_FOUNDATIONS_GUIDE.md)
> Last updated: 2026-10-09 16:10 +07

## Status

| Field | Value |
| --- | --- |
| Overall status | in progress |
| Accumulated reported active time | 0 minutes |
| Current unit | LG-02 — Values and names (next) |
| Next action | Begin LG-02 with a direct example of names referring to objects, then apply mutation versus rebinding to one small list example. |

## Unit checklist

- [x] LG-01 — Run the workspace — `completed`
- [ ] LG-02 — Values and names — `not started`
- [ ] LG-03 — Decisions and repetition — `not started`
- [ ] LG-04 — Functions — `not started`
- [ ] LG-05 — Collections — `not started`
- [ ] LG-06 — Errors and text files — `not started`
- [ ] LG-07 — Modules, CLI, and JSON — `not started`
- [ ] LG-08 — Build one task-list CLI — `not started`
- [ ] LG-09 — Recall and debug — `not started`

## Current checkpoint

### Last demonstrated evidence

- LG-01 completed: identified the script path and `hello` as `sys.argv[1]`; created and ran a script, REPL, and module with expected output; compared base Python (`False`) with `uv run` virtual-environment Python (`True`); located the official `sys.executable` documentation page.

### Recent misconceptions or fragile knowledge

- None observed.

### Incomplete knowledge or work

- None for LG-01.

### Open questions

- None.

### Retrieval prompts

- At LG-02, what changes when a name is rebound versus when a shared list is mutated?

### Exact re-entry prompt

> Begin LG-02 with a direct example of two names referring to one list. Explain mutation versus rebinding, then ask for one nearby application rather than a series of simple guesses.

## Adaptations

- 2026-10-09: Learner clarified that LG-01 should stay current and be taught faster with example code and commands; do not use simple prediction or command-recall quizzes. The brief LG-02 switch was reversed before teaching LG-02.
- 2026-10-09: After running the shown commands, learner requested a walkthrough of the fundamentals checklist and emphasized that the repository setup was created for them. Continue LG-01 through an explanation of the actual setup files.
- 2026-10-09: For LG-01, replaced command-recall quiz with direct execution, environment comparison, and a learner-located official documentation page at the learner's request.
- 2026-10-09: Learner clarified a durable teaching preference: provide the knowledge, examples, commands, and relevant documentation directly. Do not assign documentation searches or simple recall quizzes as learning tasks; use one meaningful code application when needed to verify understanding. The LG-01 lookup is complete, but should not be repeated as a teaching pattern.

## Session log

### Session 1 — 2026-10-09

- Planned time: 45 minutes.
- Actual active time: not reported.
- Units worked: LG-01.
- Learner evidence: Correctly identified the script path and `sys.argv[1]`; created a working argument-printing script. LG-01 mastery remains incomplete.
- Misconceptions or uncertainty: None observed.
- Unresolved work: LG-01 REPL result and official documentation lookup; learner execution of the shown script and module commands.
- Research notes: Confirmed `sys.argv` in the official Python reference and `uv run --locked` behavior in the official uv documentation.
- Next prompt: Show the exact LG-01 code and commands, let the learner run them, and inspect the output and official documentation page.

### Session 2 — 2026-10-09

- Planned time: 15 minutes.
- Actual active time: not reported.
- Units worked: LG-01, completed.
- Learner evidence: Reported expected REPL, script, and module output; identified `sys.argv[1]`; compared base and virtual-environment interpreters (`False`, `True`); found `https://docs.python.org/3/library/sys.html#sys.executable` independently.
- Misconceptions or uncertainty: None observed; learner prefers example code and commands over simple recall questions.
- Unresolved work: None for LG-01.
- Research notes: Official Python `venv` and `sys.executable` documentation; official uv locking and syncing documentation.
- Next prompt: Begin LG-02 with a direct example of two names referring to one list. Explain mutation versus rebinding, then use one nearby application.

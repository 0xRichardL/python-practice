# Learning Progress: Python Foundations

> Guide: [PYTHON_FOUNDATIONS_GUIDE.md](./PYTHON_FOUNDATIONS_GUIDE.md)
> Last updated: 2026-10-13 18:21 +07

## Status

| Field | Value |
| --- | --- |
| Overall status | in progress |
| Accumulated reported active time | 0 minutes reported; actual time unknown |
| Current unit | LG-02 — Values and names (in progress; reopened) |
| Next action | Teach the missing basic type model and verify it with a short application quiz. |

## Unit checklist

- [x] LG-01 — Run the workspace — completed
- [ ] LG-02 — Values and names — in progress
- [x] LG-03 — Decisions and repetition — completed
- [x] LG-04 — Functions — completed
- [ ] LG-05 — Collections — not started
- [ ] LG-06 — Errors and text files — not started
- [ ] LG-07 — Modules, CLI, and JSON — not started
- [ ] LG-08 — Build one task-list CLI — not started
- [ ] LG-09 — Recall and debug — not started

## Current checkpoint

### Last demonstrated evidence

- LG-01: Ran the REPL, script, and module; identified the argument and environment; found the official sys.executable page.
- LG-02: Correctly explained eight examples covering equality/identity, aliasing, truthiness, floating point, text/bytes, and f-strings.
- LG-03: Wrote and checked the classifier at boundaries, numbered and empty loops, range cases, and an indexed while search. Traced target 5 through indices 0 and 1, gave the correct output, and explained that break stops a while True loop while an empty indexed loop runs zero times.
- LG-04: Refactored the classifier into two returning functions; eight score boundaries and the formatter return value passed a direct check. Demonstrated positional, reordered keyword, and mixed calls. Corrected the mutable default, then answered a four-item quiz correctly on shared defaults, explicit-list mutation, local rebinding, and returned values.

### Recent misconceptions or fragile knowledge

- None unresolved.

### Incomplete knowledge or work

- LG-02: Explain what `None` and the basic types (`bool`, `int`, `float`, `str`, `bytes`) represent, identify the type of example values, and apply the ideas to a fresh variation. The eight recorded predictions do not establish this yet.

### Open questions

- None.

### Retrieval prompts

- None.

### Exact re-entry prompt

> Resume LG-02 with the missing basic type model (`None`, `bool`, `int`, `float`, `str`, `bytes`), then use a short application quiz. Do not repeat the eight examples already demonstrated. Ask for available active-learning time only if resuming after 2026-10-13.

## Adaptations

- Teach the rule and a complete example before asking for learner code. Use focused exercise files; do not assign documentation searches or repeat equivalent recall questions.
- Use short scenario quizzes for mastery checks instead of open-ended explanations when possible.
- Prefer descriptive filenames for focused demos. Keep the LG-04 note and direct-run exercise in `concepts/basics/functions/`; the learner does not plan to import that exercise.
- Keep the while-loop lesson to the two core stopping patterns.

## Session log

### Session 1 — 2026-10-09

- Planned: 45 minutes; actual active time: not reported. LG-01 started with a working argument-printing script.

### Session 2 — 2026-10-09

- Planned: 15 minutes; actual active time: not reported. LG-01 completed through REPL, script, module, environment, and documentation evidence.

### Session 3 — 2026-10-12

- Planned: 60 minutes; actual active time: not reported. LG-02 practiced through eight examples and explanations of the surprising results; completion was later reopened because basic type knowledge was not demonstrated.

### Session 4 — 2026-10-13

- Planned: about 1.5 hours; actual active time: not reported. LG-03 completed through the classifier, numbered and empty loops, range, indexed search, target-5 hand trace, and a correct break explanation. The learner requested a concise two-pattern while-loop reference.

### Session 5 — 2026-10-13

- Planned: 45 minutes; actual active time: not reported. LG-04 completed with a classifier refactor, positional and keyword calls, a corrected mutable-default demonstration, and a four-item scenario quiz answered correctly. The learner chose a separate functions topic, a descriptive exercise filename, and a direct-run script; the assistant refactored the demo for readability. Next: resume the reopened LG-02 type model.

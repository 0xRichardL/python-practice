# Learning Progress: Python Foundations

> Guide: [PYTHON_FOUNDATIONS_GUIDE.md](./PYTHON_FOUNDATIONS_GUIDE.md)
> Last updated: 2026-10-15

## Status

| Field | Value |
| --- | --- |
| Overall status | in progress |
| Accumulated reported active time | 0 minutes reported; actual time unknown |
| Current unit | LG-07 — Modules, CLI, and JSON (not started) |

## Unit checklist

- [x] LG-01 — Run the workspace — completed
- [x] LG-02 — Values and names — completed
- [x] LG-03 — Decisions and repetition — completed
- [x] LG-04 — Functions — completed
- [x] LG-05 — Collections — completed
- [x] LG-06 — Errors and text files — completed
- [ ] LG-07 — Modules, CLI, and JSON — not started
- [ ] LG-08 — Build one task-list CLI — not started
- [ ] LG-09 — Recall and debug — not started

## Current checkpoint

### Demonstrated evidence

- LG-01–LG-04: Ran Python in the workspace; explained values, names, aliasing, and types; wrote and checked loops, a classifier, functions, and a mutable-default fix.
- LG-05: Added, found, and updated task dictionaries in `collections/list_type.py`; explained collection choice, shallow slices, `zip`, and `enumerate`. The focused demo and Ruff checks passed.
- LG-06: Added specific missing-file, decode, and malformed-integer handlers to `errors_and_text_files/main.py`. The reader reports all three prepared cases and continues after errors. The learner explained `with` cleanup and `else`/`finally`; the script and Ruff checks passed.

### Open or fragile knowledge

- None unresolved. LG-07 has not started.

### Exact next action

> Ask for available active-learning time, then start LG-07 with a guarded module, one CLI command, and a JSON round trip. Do not repeat completed-unit checks.

## Adaptations

- The learner shortened LG-06 from 2.5 hours to 30 minutes because the original estimate was too long. The guide now plans 22 hours total; mastery evidence stayed the same.
- Teach the rule and a complete example before learner code. Prepare focused exercise files, use short scenario checks, avoid repeat quizzes, and provide documentation answers directly unless source-finding practice is requested.
- LG-02 was extended at the learner's request: one direct-run file per type, numbered cases, separated output, and explanatory comments. Its mastery evidence remains valid.
- Keep the LG-04 note and direct-run exercise in `concepts/basics/functions/`; the learner does not plan to import that exercise.
- LG-05 uses separate runnable collection files. The aggregate collection and values-and-names demos were removed at the learner's request; task-search code remains in `collections/list_type.py`. Its append already counted as add evidence, and `zip` was taught before quizzing it.
- An LG-05 deferral from a separate session was recorded here by mistake. The learner clarified that this chat's LG-05 work was active; its evidence was retained and the unit was completed.

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

### Session 6 — 2026-10-14

- Planned: 3 hours; actual active time: not reported. LG-02 was completed, including the learner-requested six-type deep dive and quiz corrections. The value-and-name demos were prepared, organized, commented, and checked. The prepared LG-05 examples ran and passed lint. A separate session ended after the learner reported zero active time remaining; its deferral did not apply to the LG-05 work continuing in this chat. Evidence from this chat is recorded in the checkpoint above.

### Session 7 — 2026-10-14

- Planned: remaining time from this chat's 3-hour allocation; actual active time: not reported. LG-05 completed through separate collection demos, task-dictionary append/search/update, shallow-slice and set explanations, `zip` and `enumerate` checks, and a corrected list comprehension. The two aggregate demo files were removed at the learner's request while preserving the task search in `list_type.py`. Focused collection checks passed; `make check` remains blocked by pre-existing formatting in `concepts/basics/functions/functions.md`.

### Session 8 — 2026-10-15

- Planned: 30 minutes; actual active time: not reported. LG-06 completed with a UTF-8 text reader that reports missing and malformed files separately. The learner explained `with` cleanup and the `else`/`finally` behavior. The focused script and Ruff checks pass. The LG-06 estimate and guide total were updated at the learner's request.

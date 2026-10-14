# Learning Progress: Python Foundations

> Guide: [PYTHON_FOUNDATIONS_GUIDE.md](./PYTHON_FOUNDATIONS_GUIDE.md)
> Last updated: 2026-10-14 20:17 +07

## Status

| Field | Value |
| --- | --- |
| Overall status | in progress |
| Accumulated reported active time | 0 minutes reported; actual time unknown |
| Current unit | LG-06 — Errors and text files (not started) |
| Next action | Start LG-06 with a focused UTF-8 text reader and specific missing-file versus malformed-content errors. |

## Unit checklist

- [x] LG-01 — Run the workspace — completed
- [x] LG-02 — Values and names — completed
- [x] LG-03 — Decisions and repetition — completed
- [x] LG-04 — Functions — completed
- [x] LG-05 — Collections — completed
- [ ] LG-06 — Errors and text files — not started
- [ ] LG-07 — Modules, CLI, and JSON — not started
- [ ] LG-08 — Build one task-list CLI — not started
- [ ] LG-09 — Recall and debug — not started

## Current checkpoint

### Last demonstrated evidence

- LG-01: Ran the REPL, script, and module; identified the argument and environment; found the official sys.executable page.
- LG-02: Correctly explained eight examples covering equality/identity, aliasing, truthiness, floating point, text/bytes, and f-strings.
- LG-02: In a fresh quiz, correctly identified `bool`, `int`, `float`, `str`, `bytes`, and `NoneType`; chose `is None` to distinguish missing from zero; and explained that decoding bytes produces text.
- LG-02 deep dive: Correctly applied `None` method-return behavior; `bool` truthiness and dictionary-key overlap; negative integer floor division and remainder after one correction; float NaN and tolerance after one correction; Unicode normalization, slicing, and splitting; and bytes indexing, slicing, strict UTF-8 failure, and lossy replacement after a fresh correction check.
- LG-03: Wrote and checked the classifier at boundaries, numbered and empty loops, range cases, and an indexed while search. Traced target 5 through indices 0 and 1, gave the correct output, and explained that break stops a while True loop while an empty indexed loop runs zero times.
- LG-04: Refactored the classifier into two returning functions; eight score boundaries and the formatter return value passed a direct check. Demonstrated positional, reordered keyword, and mixed calls. Corrected the mutable default, then answered a four-item quiz correctly on shared defaults, explicit-list mutation, local rebinding, and returned values.
- LG-05: Correctly explained that a list slice creates a separate outer list while both lists share nested dictionaries. Correctly distinguished tuple item replacement from mutation of a contained list, `dict` missing-key failure from `.get()` fallback, and why a set cannot model ordered task records.
- LG-05: Wrote a loop that finds `"write"`, marks its dictionary done, and reports when no title matches. The normal run produced the expected changed task and passed Ruff; the example is now in `collections/list_type.py`.
- LG-05: Appended a task dictionary in `collections/list_type.py`, satisfying the add step. After instruction, correctly stated that fully consuming unequal-length `zip(..., strict=True)` raises an error.
- LG-05: Correctly reasoned that an empty search leaves `found` false and a missing title changes no dictionary. Corrected a comprehension to filter `search_tasks`, observed `['plan']`, and explained that `enumerate(..., start=1)` produces numbered tuples. The focused list demo runs and passes Ruff and format checks.

### Recent misconceptions or fragile knowledge

- None unresolved. The initial comprehension used the earlier `tasks` list, whose one dictionary had already been marked done; the learner switched to `search_tasks` and verified the result.

### Incomplete knowledge or work

- LG-06 has not started.

### Open questions

- None.

### Retrieval prompts

- None.

### Exact re-entry prompt

> Ask for available active-learning time, then start LG-06. Teach a small UTF-8 text reader with `with` and `Path.open()`, distinguishing a missing file from malformed content. Prepare the hands-on code file before teaching, use short quizzes for verification, and follow LG-06's mastery evidence. LG-05 is complete; do not repeat its checks.

## Adaptations

- Teach the rule and a complete example before asking for learner code. Use focused exercise files; do not assign documentation searches or repeat equivalent recall questions.
- Use short scenario quizzes for mastery checks instead of open-ended explanations when possible.
- Prefer descriptive filenames for focused demos. Keep the LG-04 note and direct-run exercise in `concepts/basics/functions/`; the learner does not plan to import that exercise.
- Keep the while-loop lesson to the two core stopping patterns.
- For the 2026-10-14 session, prepare hands-on files before teaching and use short quizzes for verification.
- Keep separate runnable files for each collection type (`list_type.py`, `tuple_type.py`, `dict_type.py`, `set_type.py`). The aggregate `collections/main.py` and `values_and_names/main.py` were removed at the learner's request; the learner's task search code was retained in `list_type.py`.
- The learner explicitly requested a deeper LG-02 review, with one file per type and no module guards. This extended LG-02 beyond its original estimate; the original LG-02 evidence remains valid.
- The learner requested numbered cases and separated terminal output for the value-and-name demos; all seven scripts were updated and checked.
- The learner requested more explanatory comments in those scripts; comments now state the rule or failure behind each case without changing behavior.
- A separate session's LG-05 deferral was applied to this progress file by mistake. The learner clarified that this chat's LG-05 work was active; its verified evidence was retained and the unit was later completed.
- Teach `zip` explicitly before quizzing it; the learner identified that the earlier `zip` question came before instruction.
- Count the task-dictionary append already completed in `collections/list_type.py` toward LG-05's add evidence; the learner requested no duplicate fourth-task step.

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

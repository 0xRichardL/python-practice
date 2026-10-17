# Learning Progress: Python Foundations

> Guide: [PYTHON_FOUNDATIONS_GUIDE.md](./PYTHON_FOUNDATIONS_GUIDE.md), version 2
> Last updated: 2026-10-17

## Status

| Field | Value |
| --- | --- |
| Overall status | in progress |
| Known active time | About 2 hours on 2026-10-17; earlier sessions' actual time is unknown |
| Plan and budget | 17.5 hours planned across LG-01–LG-09; 22-hour active-learning budget, with 4.5 hours unallocated in the plan; actual time remaining is unknown |
| Current unit | LG-09 — Recall and debug (not started) |

## Unit checklist

- [x] LG-01 — Run the workspace — completed
- [x] LG-02 — Values and names — completed
- [x] LG-03 — Decisions and repetition — completed
- [x] LG-04 — Functions — completed
- [x] LG-05 — Collections — completed
- [x] LG-06 — Errors and text files — completed
- [x] LG-07 — Modules, CLI, and JSON — completed
- [x] LG-08 — Build one task-list CLI — completed
- [ ] LG-09 — Recall and debug — not started

## Completed-unit evidence

| Unit | Learner evidence and verification |
| --- | --- |
| LG-01 | Ran REPL, script, and `-m` examples; explained the Python environment and workspace commands (Session 2). |
| LG-02 | Explained six basic types, names and aliasing, equality versus identity, truthiness, encoding, and floating-point behavior; corrected quiz answers (Sessions 3 and 6). |
| LG-03 | Wrote and traced conditionals and loops, including an indexed search and `break` (Session 4). |
| LG-04 | Refactored a classifier into functions; explained arguments, return values, annotations, defaults, and the mutable-default pitfall (Session 5). |
| LG-05 | Added, searched, and updated task dictionaries; explained collection choices, shallow slices, `zip`, `enumerate`, and a comprehension (Session 7). |
| LG-06 | Built a UTF-8 number reader with specific file, decode, and value-error handlers; explained `with`, `else`, and `finally`. The prior invalid-UTF-8 check lacks a retained fixture (Session 8). |
| LG-07 | Explained import versus guarded execution, parsed values, `choices`, and help/error exit statuses. Built `add_task(path, title)` with JSON persistence. Temporary-copy checks passed imported use, file-path and `-m` runs, clean help, missing-title error, and corrupt-file preservation; Ruff passed (Sessions 9–11). |
| LG-08 | Built `add`, numbered `list`, and one-based `done` operations. Temporary-copy checks passed separate-run persistence, help, invalid-number errors, and malformed-JSON preservation. Three nearby pytest tests use `tmp_path` for normal persistence, out-of-range handling, and corrupt-file preservation; focused pytest and Ruff lint/format passed (Session 13). |

## Current checkpoint

- **Completed:** LG-08. The CLI works across separate runs, handles malformed JSON without overwriting it, and has passing normal and failure tests.
- **Completed check:** Replayed LG-06 with a temporary invalid-UTF-8 file; `read_number()` raised `UnicodeDecodeError` as expected. This did not reopen LG-06.
- **LG-08 verification:** Temporary-copy checks passed help, `add`, `list`, `done 1`, separate-run JSON persistence, non-integer and out-of-range errors (status 2), and malformed-JSON preservation (status 1). The real `tasks.json` includes a learner change marking its first task done; preserve it.
- **Next action:** Begin LG-09 with a from-memory explanation of the CLI-to-JSON flow. Then check empty-list, repeated-`done`, and missing-file behavior, trace and fix one observed or introduced bug, rerun focused tests and `make check`.
- **Separate housekeeping:** `json/main.py` calls a missing file "skipped" although it creates one; `run_workspace/run_workspace.md` links to the wrong relative `main.py` path. These do not block the guide.

## Adaptations

- The learner shortened LG-06 from 2.5 hours to 30 minutes because the original estimate was too long. The guide now plans 17.5 hours within the 22-hour budget; the LG-06 mastery evidence stayed the same.
- Teach the rule and a complete example before learner code. Prepare focused exercise files, use short scenario checks, avoid repeat quizzes, and provide documentation answers directly unless source-finding practice is requested.
- LG-02 was extended at the learner's request: one direct-run file per type, numbered cases, separated output, and explanatory comments. Its mastery evidence remains valid.
- Keep the LG-04 note and direct-run exercise in `concepts/basics/functions/`; the learner does not plan to import that exercise.
- LG-05 uses separate runnable collection files. The aggregate collection and values-and-names demos were removed at the learner's request; task-search code remains in `collections/list_type.py`. Its append already counted as add evidence, and `zip` was taught before quizzing it.
- An LG-05 deferral from a separate session was recorded here by mistake. The learner clarified that this chat's LG-05 work was active; its evidence was retained and the unit was completed.
- During LG-07, the learner requested extra focus on saving and loading JSON.
- The learner asked for basic knowledge before code or documentation and separate folders/files for JSON, modules, and CLI arguments. The premature integrated task-list scaffold and combined note were replaced by focused concept demos.
- For CLI arguments, explain `ArgumentParser` creation, `add_argument`, and `parse_args` with a complete example before asking the learner to infer parsed values.
- The learner requested a complete integrated example before any task-list implementation prompt. An analogous JSON-backed notes CLI was shown in conversation, and an empty `task_list/main.py` was prepared at the learner's request.
- The learner pointed out that `choices` had not been taught before the task-list instructions used it. The CLI note and runnable demo now teach a two-value choice, its default, and the invalid-choice error before task-list use.
- The learner requested short teaching turns without questions that leave the assistant waiting for a reply. Present the next concept and exact action directly, then continue when the learner returns.
- Guide version 2 makes knowledge and mastery evidence explicit, pins Python documentation to 3.14, and treats the original three-day grouping as optional. Unit IDs and recorded completion evidence remain unchanged. Supply relevant documentation and ask for application rather than assigning a documentation search.
- During LG-08, the learner clarified they had no testing knowledge; teach pytest basics with a working example before assigning the guide's two tests.

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

### Session 9 — 2026-10-15

- Planned: 2 hours; actual active time: not reported. LG-07 began with extra attention to JSON. At the learner's request, modules, CLI arguments, and JSON gained separate concept notes and runnable demos. The learner practiced JSON string and file conversion; the premature integrated task-list scaffold was removed while component basics were taught.

### Session 10 — 2026-10-16

- Planned: 60 minutes; actual active time: not reported. The learner fixed the malformed-JSON fallthrough; temporary-file checks confirmed the corrupt file is preserved and a missing file starts a task list. The learner correctly explained file-path and `-m` entry points and why an import skips guarded code. `ArgumentParser` basics were explained, but no CLI application answer or integrated `add` command was completed. The learner paused the session here.

### Session 11 — 2026-10-17

- Planned: 45 minutes initially, with a later 10-minute teaching window. Actual: about 2 hours active, excluding lunch. Session ended at the learner's request.
- Covered `argparse` options, `choices`, parsed values, and exit statuses, with a complete JSON-backed CLI example before the exercise. The learner built `add_task(path, title)` and fixed malformed-JSON handling and help parsing order.
- Temporary-copy checks passed imported use, file-path and `-m` persistence, help and error cases, corrupt-file preservation, and Ruff. LG-07 is complete. A separate LG-06 invalid-UTF-8 fixture check remains before the data-boundary milestone.

### Session 12 — 2026-10-17

- Planned: 1 hour; actual active time: not reported. LG-08 started and remains in progress.
- Replayed the LG-06 invalid-UTF-8 check with a temporary file; `read_number()` raised `UnicodeDecodeError` as expected. Reviewed the current `add` implementation and created a concise LG-08 reference note.
- Teaching pause: optional positional parsing and per-command validation were introduced. Next, the learner should adapt the parser and implement `list`; `done` and tests remain for later in the allocation.

### Session 13 — 2026-10-17

- Planned: continuation of the 1-hour LG-08 allocation; actual active time: not reported.
- The learner built numbered `list` and one-based `done`, with separate conversion and range errors. Temporary-copy checks passed help, add/list/done across runs, invalid-number errors, and malformed-JSON preservation. The real `tasks.json` includes a learner change marking its first task done; it was preserved.
- Pytest basics were taught at the learner's request. The learner wrote and refined three tests using `tmp_path` and `pytest.raises`; all 3 passed. Ruff lint and format checks passed for the task-list code and tests. LG-08 completed; LG-09 is next.

Slice: US-02 Retry after an incorrect answer + US-03 See correct and attempted counts (Answer Checker).
Acceptance criterion: After a first wrong answer the answer stays hidden and a second try is accepted; after a second wrong answer the correct answer is shown and no third try is allowed.
Rule: The logic layer owns the two-attempt rule, the reveal gate, and the attempted/correct counts (a problem counts as attempted once).
Data: The data layer stores every Attempt (session, problem, try, answer, correct) and one stored ending per finished problem.
Design decision: The interface keeps no try counter, no reveal decision, and no input rule. The logic layer reports the try number and the ending, and the store keeps them, so the state survives closing the program.

# DataMan Text-Only Prototype: Answer Checker

Started from the M4 Bonus template.

**Files I changed**
- `app.py`: now runs several problems and shows the score; the input check moved out to the logic layer; removed the Memory Bank menu option.
- `dataman/logic.py`: removed `MemoryBank` / `SetFull`; added `parse_answer`, `score`, `unfinished`, stored endings, and a per-session `curator_report`.
- `dataman/store.py`: added seed problems, `attempts_in`, `save_result` / `result_for`; the JSON file now also keeps endings.
- `tests/test_logic.py`: replaced the bonus tests with my own tests for this slice.
- Removed the bonus files (`check.py`, `exercise/`).

## The design decision, and where the code holds it
- `app.py` never counts tries and never decides when to reveal. It calls `session.next_try()` and reads `Outcome.status` and `Outcome.revealed_answer`.
- The input rule ("a non-number is not an attempt") is `logic.parse_answer`, not interface code.
- `PracticeSession.next_try()` counts stored attempts; `submit()` writes the ending with `store.save_result(...)`.

## How to run
```
python app.py                    # data survives a restart (dataman_store.json)
python app.py --store memory     # data lives in RAM
python -m unittest -v            # tests call the logic layer, never the interface
```
To start over, delete `dataman_store.json`.

## Traceability
| Source | Shown by |
|---|---|
| US-02 / FR-03: retry after a wrong answer | `test_first_miss_hides_answer_and_allows_second_try`, `test_correct_on_retry_is_a_second_try_success` |
| Two-attempt limit and reveal after the second miss | `test_second_miss_reveals_and_blocks_third_try` |
| US-03 / FR-04: attempted counts a problem once | `test_attempted_counts_a_problem_once`, `test_wrong_answer_does_not_raise_correct` |
| Every ending is stored; curator can tell them apart | `test_every_ending_is_stored`, `test_curator_report_tells_outcomes_apart` |
| State survives a restart | `test_state_survives_a_restart` |
| Logic has no `input()` / `print()` | `test_logic_layer_has_no_input_or_print` |

## What is stubbed
- The data layer is a stand-in for a database: three seed problems in `store.py`, and a JSON file for persistence.
- One fixed learner/session (`maya-1`); no real identity, sign-in, or authorization.
- Not in this slice: Practice Sets and the 10-problem limit, resume across devices, parent/teacher reporting.

## What is still uncertain
- Q-01: what saved practice should include, and for how long.
- Whether a learner who quits after a first miss should resume at try 2 (this prototype does).
- Who counts as an authorized curator, and whether two curators may see the same history.
- Whether a non-number should ever count as a try (this prototype says no).

## What running the program changed
- I ran it, typed `abc`, and it said "Enter a whole number" and stayed on try 1, so a non-number is not an attempt. I decided to keep that rule and moved the check into the logic layer so a test can prove it.
- I missed P1 once, pressed Ctrl+C, and ran the program again. It asked "P1 try 2 of 2", so it remembered the first miss from `dataman_store.json`. That confirmed the try number can come from stored attempts instead of the screen.
- After I got P1 right on the second try, the curator report showed "second-try success" with both attempts, even after I restarted the program again. The template had guessed this ending from the attempt count, so I changed it to store the ending when a problem finishes.
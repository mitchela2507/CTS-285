"""Acceptance criteria shown by calling the logic layer directly (no interface).
Run from the project folder:  python -m unittest -v
"""
import ast
import inspect
import os
import tempfile
import unittest

from dataman import logic
from dataman.logic import PracticeSession, InvalidAnswer, AttemptsExhausted
from dataman.store import JsonFileStore, MemoryStore

S = "test-session"


def session(store, pid="P1"):
    problem = next(p for p in logic.problems(store) if p.id == pid)
    return PracticeSession(store, S, problem)


class TwoAttemptRule(unittest.TestCase):
    def setUp(self):
        self.store = MemoryStore()

    def test_first_miss_hides_answer_and_allows_second_try(self):  # US-02
        out = session(self.store).submit(5)
        self.assertEqual(out.status, "retry")
        self.assertIsNone(out.revealed_answer)
        self.assertEqual(session(self.store).next_try(), 2)

    def test_second_miss_reveals_and_blocks_third_try(self):
        s = session(self.store)
        s.submit(5)
        out = s.submit(6)
        self.assertEqual((out.status, out.revealed_answer), ("reveal", 56))
        with self.assertRaises(AttemptsExhausted):
            s.submit(56)

    def test_correct_on_retry_is_a_second_try_success(self):  # US-02
        s = session(self.store)
        s.submit(5)
        self.assertEqual(s.submit(56).ending, logic.SECOND_TRY)


class Counts(unittest.TestCase):  # US-03
    def setUp(self):
        self.store = MemoryStore()

    def test_attempted_counts_a_problem_once(self):
        s = session(self.store)
        s.submit(5)
        s.submit(56)
        self.assertEqual(logic.score(self.store, S), {"attempted": 1, "correct": 1})

    def test_wrong_answer_does_not_raise_correct(self):
        session(self.store).submit(5)
        self.assertEqual(logic.score(self.store, S), {"attempted": 1, "correct": 0})


class InputAndEndings(unittest.TestCase):
    def setUp(self):
        self.store = MemoryStore()

    def test_non_number_is_not_an_attempt(self):
        with self.assertRaises(InvalidAnswer):
            logic.parse_answer("abc")
        self.assertEqual(session(self.store).next_try(), 1)

    def test_every_ending_is_stored(self):
        session(self.store, "P1").submit(56)
        s2 = session(self.store, "P2"); s2.submit(1); s2.submit(36)
        s3 = session(self.store, "P3"); s3.submit(1); s3.submit(2)
        got = {pid: self.store.result_for(S, pid) for pid in ("P1", "P2", "P3")}
        self.assertEqual(got, {"P1": logic.FIRST_TRY, "P2": logic.SECOND_TRY,
                               "P3": logic.TWO_MISSES})

    def test_curator_report_tells_outcomes_apart(self):
        session(self.store, "P1").submit(56)
        s3 = session(self.store, "P3"); s3.submit(1); s3.submit(2)
        labels = {r["problem_id"]: r["label"]
                  for r in logic.curator_report(self.store, S)["problems"]}
        self.assertEqual(labels, {"P1": logic.FIRST_TRY, "P3": logic.TWO_MISSES})


class StateAndLayers(unittest.TestCase):
    def test_state_survives_a_restart(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "store.json")
            session(JsonFileStore(path)).submit(5)           # miss, then "quit"
            reopened = session(JsonFileStore(path))          # run the program again
            self.assertEqual(reopened.next_try(), 2)
            self.assertFalse(reopened.is_finished())

    def test_logic_layer_has_no_input_or_print(self):
        calls = {n.func.id for n in ast.walk(ast.parse(inspect.getsource(logic)))
                 if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
        self.assertNotIn("input", calls)
        self.assertNotIn("print", calls)


if __name__ == "__main__":
    unittest.main()
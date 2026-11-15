"""Business-logic layer.

Rules live here. This file never calls input() or print().
It reaches data only through a store object (see store.py).

Design decision: the interface keeps no try counter, no reveal decision and no
input rule. The logic layer reports the try number and the ending, and the
store keeps every attempt and every ending as a record.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

MAX_ATTEMPTS = 2  # Rule: exactly two tries per problem.

FIRST_TRY = "first-try success"
SECOND_TRY = "second-try success"
TWO_MISSES = "two misses"


@dataclass(frozen=True)
class Problem:
    id: str
    prompt: str
    answer: int


@dataclass(frozen=True)
class Outcome:
    """What the interface needs in order to draw a screen. Nothing more."""
    status: str                   # "correct" | "retry" | "reveal"
    try_number: int               # the try that was just used
    revealed_answer: int | None   # set only when status == "reveal"
    ending: str | None            # set only when the problem is now finished


class InvalidAnswer(Exception):
    """The input is not a whole number. It does not use up a try."""


class AttemptsExhausted(Exception):
    """A finished problem was given another answer."""


def parse_answer(raw: str) -> int:
    text = raw.strip()
    if not re.fullmatch(r"-?\d+", text):
        raise InvalidAnswer("Enter a whole number.")
    return int(text)


def problems(store) -> list[Problem]:
    return [Problem(**p) for p in store.problems()]


def unfinished(store, session_id: str) -> list[Problem]:
    return [p for p in problems(store)
            if store.result_for(session_id, p.id) is None]


def score(store, session_id: str) -> dict:
    """US-03: attempted counts a problem once, on its first attempt."""
    rows = store.attempts_in(session_id)
    return {
        "attempted": len({r["problem_id"] for r in rows}),
        "correct": sum(1 for r in rows if r["correct"]),
    }


class PracticeSession:
    """One learner, one problem. State comes from the store, not from memory."""

    def __init__(self, store, session_id: str, problem: Problem):
        self.store = store
        self.session_id = session_id
        self.problem = problem

    def attempts(self) -> list[dict]:
        return self.store.attempts_for(self.session_id, self.problem.id)

    def is_finished(self) -> bool:
        return self.store.result_for(self.session_id, self.problem.id) is not None

    def next_try(self) -> int:
        return len(self.attempts()) + 1

    def submit(self, answer: int) -> Outcome:
        if self.is_finished():
            raise AttemptsExhausted(self.problem.id)
        try_number = self.next_try()          # recorded before judging
        correct = answer == self.problem.answer
        self.store.save_attempt(
            self.session_id, self.problem.id, try_number, answer, correct)

        if correct:
            ending = FIRST_TRY if try_number == 1 else SECOND_TRY
            status, revealed = "correct", None
        elif try_number >= MAX_ATTEMPTS:
            ending, status, revealed = TWO_MISSES, "reveal", self.problem.answer
        else:
            return Outcome("retry", try_number, None, None)

        self.store.save_result(self.session_id, self.problem.id, ending)
        return Outcome(status, try_number, revealed, ending)


def curator_report(store, session_id: str) -> dict:
    """Curator view: the score, plus each problem's stored ending and attempts."""
    rows = []
    for p in problems(store):
        attempts = store.attempts_for(session_id, p.id)
        if not attempts:
            continue
        rows.append({
            "problem_id": p.id,
            "label": store.result_for(session_id, p.id) or "in progress",
            "attempts": attempts,
        })
    return {"score": score(store, session_id), "problems": rows}
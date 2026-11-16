"""Stubbed data layer.

Two stand-ins for a database. Both give the logic layer the same methods.
Swap one for the other and logic.py does not change.
This layer stores and returns records. It makes no decisions.
"""
import json
from pathlib import Path

SEED_PROBLEMS = [
    {"id": "P1", "prompt": "7 x 8", "answer": 56},
    {"id": "P2", "prompt": "9 x 4", "answer": 36},
    {"id": "P3", "prompt": "12 / 3", "answer": 4},
]


class MemoryStore:
    """Lives in RAM. Gone when the program ends."""

    def __init__(self):
        self._attempts: list[dict] = []
        self._results: list[dict] = []   # one stored ending per finished problem

    def problems(self):
        return [dict(p) for p in SEED_PROBLEMS]

    def save_attempt(self, session_id, problem_id, try_number, answer, correct):
        self._attempts.append({
            "session_id": session_id, "problem_id": problem_id,
            "try": try_number, "answer": answer, "correct": correct,
        })

    def attempts_for(self, session_id, problem_id):
        return [dict(a) for a in self._attempts
                if a["session_id"] == session_id and a["problem_id"] == problem_id]

    def attempts_in(self, session_id):
        return [dict(a) for a in self._attempts if a["session_id"] == session_id]

    def save_result(self, session_id, problem_id, ending):
        self._results.append(
            {"session_id": session_id, "problem_id": problem_id, "ending": ending})

    def result_for(self, session_id, problem_id):
        for r in self._results:
            if r["session_id"] == session_id and r["problem_id"] == problem_id:
                return r["ending"]
        return None


class JsonFileStore(MemoryStore):
    """Same methods. Writes to a file, so evidence survives a restart."""

    def __init__(self, path="dataman_store.json"):
        super().__init__()
        self.path = Path(path)
        if self.path.exists():
            raw = json.loads(self.path.read_text())
            self._attempts = raw.get("attempts", [])
            self._results = raw.get("results", [])

    def _flush(self):
        self.path.write_text(json.dumps(
            {"attempts": self._attempts, "results": self._results}, indent=2))

    def save_attempt(self, *args):
        super().save_attempt(*args)
        self._flush()

    def save_result(self, *args):
        super().save_result(*args)
        self._flush()
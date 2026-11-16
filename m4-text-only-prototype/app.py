"""Text interface layer. This is the only file that uses input() and print().

Run:  python app.py                 (data survives a restart, in dataman_store.json)
      python app.py --store memory  (data lives in RAM)
To start over, delete dataman_store.json.
"""
import argparse

from dataman import logic
from dataman.store import JsonFileStore, MemoryStore

SESSION = "maya-1"


def practice(store):
    todo = logic.unfinished(store, SESSION)
    if not todo:
        print("All problems are finished. Choose 'report'.")
        return
    for problem in todo:
        session = logic.PracticeSession(store, SESSION, problem)
        while not session.is_finished():
            raw = input(f"{problem.id} try {session.next_try()} of "
                        f"{logic.MAX_ATTEMPTS}: {problem.prompt} = ")
            try:
                out = session.submit(logic.parse_answer(raw))
            except logic.InvalidAnswer as err:
                print(err)
                continue
            if out.status == "correct":
                print("Correct.")
            elif out.status == "retry":
                print("EEE -- Try again.")
            else:
                print(f"EEE -- The answer is {out.revealed_answer}.")
            s = logic.score(store, SESSION)
            print(f"  Score: {s['correct']} correct / {s['attempted']} attempted")


def report(store):
    rep = logic.curator_report(store, SESSION)
    s = rep["score"]
    print(f"Curator report for {SESSION}: "
          f"{s['correct']} correct / {s['attempted']} attempted")
    for row in rep["problems"]:
        print(f"  {row['problem_id']}: {row['label']}")
        for r in row["attempts"]:
            print(f"    try {r['try']}: answered {r['answer']} -> "
                  f"{'correct' if r['correct'] else 'wrong'}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", choices=["memory", "json"], default="json")
    args = parser.parse_args()
    store = JsonFileStore() if args.store == "json" else MemoryStore()
    actions = {"practice": practice, "report": report}
    try:
        while True:
            choice = input("practice / report / quit > ").strip().lower()
            if choice == "quit":
                break
            if choice in actions:
                actions[choice](store)
    except (EOFError, KeyboardInterrupt):
        print("\nBye.")


if __name__ == "__main__":
    main()
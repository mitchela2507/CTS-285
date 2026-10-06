# M3 Product Owner Decision Record

## Scenario
StudyTrack release planning under constrained capacity.

## Round 1 — Capacity 13
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

**Why this release slice was defensible:**
I picked ST-01 through ST-04, which comes to 10 of the 13 points. All four are high value and ready to build, and together they cover the release goal: students can create tasks, mark them done, and recover when they fall behind. ST-01 has no dependencies and the other three build on it, so the slice hangs together instead of being a random pile of stories. I included ST-04 because keyboard accessibility is cheap now and a pain to fix later. I also left 3 points open on purpose. The only things that would fit were low-value, and I'd rather keep that room in case something changes than spend it just to hit 13.

**One intentional deferral and why:**
I deferred ST-08, the parent progress dashboard. It's only medium value, it depends on ST-05, which isn't in this release, and the scope and privacy expectations still aren't settled. If we built it now, we'd probably end up redoing it. It's a "not yet" rather than a "never." Once ST-05 is done and the stakeholders clarify what parents should see, it can come back.

## Complication
Capacity dropped from 13 to 10 points. Keyboard accessibility testing revealed that task entry cannot reliably be completed with keyboard navigation, so ST-04 became release-critical.

## Revised Release Slice — Capacity 10
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

### Removed after complication
- None

### Added after complication
- None

**What changed and why:**
Not much changed in the selection, but the reasoning did. Capacity dropped to 10 points, which is exactly what my slice already used, so I didn't have to cut anything. The bigger change is that accessibility testing showed students can't reliably use the task-entry flow with a keyboard. That turned ST-04 from a nice early win into a release blocker, since it fixes the exact flow that failed. I kept ST-01 through ST-04 and made sure ST-04 is treated as required for release, not something to trim if we run short.

**Tradeoff accepted:**
I'm using all 10 points with no buffer, so if anything takes longer than expected, we'll feel it right away. I also left out ST-05, the weekly progress summary, so students can mark tasks complete but won't get a summary view yet. I accepted that because the release goal is about planning and recovering from missed work, and every story in the slice supports that. Adding ST-05 would have meant cutting a high-value story, which didn't make sense.

## Transfer to DataMan
Before finalizing your DataMan backlog, review whether any item is high value but not ready, depends on unresolved work, consumes disproportionate effort, or should move because it reduces risk or unlocks other work.

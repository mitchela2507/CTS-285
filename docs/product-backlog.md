# DataMan Product Backlog

> Replace every bracketed prompt with your own work. Delete the prompts, this note, and any unused story blocks before you submit.
> Save this file as `docs/product-backlog.md`. Use that exact folder, file name, and lowercase spelling.

## Sources

This backlog uses these files from my repository:

- `docs/requirements.md`
- `docs/decisions/m3-backlog-triage-record.md`
- `docs/decisions/m3-product-owner-decision-record.md`

[If you revised `docs/requirements.md` after Module 2, state that here in one sentence.]

## Priority Order

List every story ID from highest priority to lowest. The story blocks below must appear in this same order.

1. US-01 — Immediate answer feedback
2. US-02 — Retry after an incorrect answer
3. US-03 — See correct and attempted counts
4. US-04 — Return to saved practice
5. US-05 — Reach DataMan through a web browser
6. US-06 — Store problems for a learner
7. US-07 — Practice without a printed manual
8. US-08 — Keep work when a session is interrupted
9. US-09 — Parent and teacher visibility into practice
10. US-10 — Same core features on every supported device

## Stories

### US-01 — Immediate answer feedback

**Requirement ID:** FR-02

**User Story:** As a student practicing math, I want to be told right away whether my answer is correct so that I know how I am doing while the problem is still fresh.

**Acceptance Criteria:**

- Given a math problem is shown to a learner, when the learner submits a correct answer, then the learner is told the answer is correct before the next problem is shown.
- Given a math problem is shown to a learner, when the learner submits an incorrect answer, then the learner is told the answer is incorrect before the next problem is shown.
- Given a learner has submitted an answer, when the feedback appears, then no further action from the learner is needed to see it.

**Relative Effort:** S — It is one clear check-and-respond behavior, smaller than the saving, storing, and reporting stories in this backlog.
**Dependency / Constraint:** None

**Priority:** 1

**Readiness:** Move Forward

**Priority Rationale:** High value, small effort, no dependency, and low uncertainty. It is the core of the original Answer Checker (E-02) and stakeholders named it as important (E-05). Other stories (US-02, US-03, US-07) build on it, so it also unlocks work. This matches the triage lesson that high-value, unblocked, ready work goes first.

---

### US-02 — Retry after an incorrect answer

**Requirement ID:** FR-03

**User Story:** As a student who got a problem wrong, I want to try the same problem again so that I can learn from my mistake instead of moving on without understanding it.

**Acceptance Criteria:**

- Given a learner has been told an answer is incorrect, when the learner wants to try again, then the same problem is still available to answer.
- Given a learner is retrying a problem, when the learner submits a new answer, then the learner receives correct or incorrect feedback for that new answer.
- Given a learner answers the retry correctly, when the feedback appears, then the learner is told the answer is correct.

**Relative Effort:** S — It reuses the feedback behavior from US-01 and adds only the ability to answer the same problem again.

**Dependency / Constraint:** [dependency, constraint, or None]

**Priority:** [rank]

**Readiness:** [Move Forward / Refine / Defer]

**Priority Rationale:** [reason]

---

<!-- A non-functional requirement (NFR) can become its own story. It can also become a constraint or an acceptance criterion on another story. If you use it as a constraint, put its ID in that story's Requirement ID field. -->

## Open Questions Carried Forward

List each open question or assumption from `docs/requirements.md` that affects this backlog. Do not turn an unresolved question into a confirmed story.

- **[Q-__]:** [Which story waits on this question, or why no story exists for it yet.]

## Revisions After Triage and Release Planning

State what changed in this backlog because of your triage record and your Product Owner decision record.

- [Story ID — what changed — which record caused the change.]
- [If nothing changed, say so, and say why the original decision still holds.]

## Before You Submit

- [ ] The file path is exactly `docs/product-backlog.md`.
- [ ] All bracketed prompts and unused story blocks are deleted.
- [ ] Every story has all eight required fields: Story ID, Requirement ID, User Story, Acceptance Criteria, Relative Effort, Dependency / Constraint, Priority, Priority Rationale.
- [ ] Every Requirement ID exists in `docs/requirements.md`.
- [ ] Each acceptance criterion states a result another person can observe and check.
- [ ] The story blocks follow the Priority Order list.
- [ ] Large or uncertain stories are marked Refine or Defer, not hidden as Move Forward.
- [ ] No story or criterion names a framework, database, or screen layout, unless a requirement makes it a constraint.
- [ ] The file renders correctly on GitHub.
- [ ] The change is committed with a message that describes it.

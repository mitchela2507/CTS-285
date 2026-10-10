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

**Dependency / Constraint:** Dependency — US-01 must exist first

**Priority:** 2

**Readiness:** Move Forward

**Priority Rationale:** High value (E-02, E-05), small effort, and low uncertainty. Its only dependency is US-01, which is ranked first. Together US-01 and US-02 form the smallest usable practice loop, so this ranks above work that is larger or still blocked.

---
### US-03 — See correct and attempted counts
 
**Requirement ID:** FR-04
**User Story:** As a student, I want to see how many answers I got right and how many problems I have tried so that I can tell how my practice is going.
 
**Acceptance Criteria:**
 
- Given a learner starts a practice activity, when no problems have been answered, then the learner sees zero correct and zero attempted.
- Given a learner submits a first answer to a new problem, when the answer is checked, then the attempted count goes up by one.
- Given a learner submits a correct answer, when the answer is checked, then the correct count goes up by one.
- Given a learner submits an incorrect answer, when the answer is checked, then the correct count does not change.
  
**Relative Effort:** S — It adds two running counts to the existing answer flow and is smaller than saving or reporting work.

**Dependency / Constraint:** Dependency — US-01 must exist first.

**Priority:** 3

**Readiness:** Move Forward

**Priority Rationale:** Medium-to-high value (E-05, E-03), small effort, and one ready dependency. It ranks below US-01 and US-02 because it adds visibility but does not complete the practice loop. It stays inside the release slice because it is limited to counts during one activity; the broader progress summary was left out in the release planning decision.

---

### US-04 — Return to saved practice
 
**Requirement ID:** FR-01

**User Story:** As a student who pauses practice, I want my earlier work to still be there when I come back so that I do not have to start over.
 
**Acceptance Criteria:**
 
- Given a learner has answered some problems in a practice activity, when the learner leaves and comes back later, then the learner sees the practice as it was when they left.
- Given a learner returns to saved practice, when the practice opens, then the correct and attempted counts match what they were when the learner left.
- Given a learner returns to saved practice, when the practice opens, then the learner can continue from where they stopped.
These criteria are provisional until Q-01 defines what the saved practice state includes and how long it stays available.
 
**Relative Effort:** M — It is larger than the feedback stories because it must preserve more than one thing, and smaller than before because the interruption case is split into US-08.

**Dependency / Constraint:** Dependency — The way a learner is recognized when returning must be decided first, and Q-01 must be answered.

**Priority:** 4

**Readiness:** Refine

**Priority Rationale:** High value, because teachers specifically asked for it (E-04). It ranks below the ready stories because its identity dependency and the scope in Q-01 are unresolved, so building now risks rework. It ranks above the other Refine stories because it has the strongest stakeholder evidence. High value is kept visible, but value alone does not make it ready.

---
 
### US-05 — Reach DataMan through a web browser
 
**Requirement ID:** NFR-01

**User Story:** As a student using whatever device I have, I want to open DataMan in a web browser so that I can practice at school or at home.
 
**Acceptance Criteria:**
 
- Given a device type is on the confirmed support list, when a learner opens DataMan in a web browser on that device, then the learner can reach and begin a practice activity.
- Given a device type is not on the confirmed support list, when the support list is reviewed, then it is clear that the device is outside the confirmed scope.
These criteria cannot be finalized until Q-04 confirms the support list.
 
**Relative Effort:** M — It touches every device type in scope, though the work per device is not yet known.

**Dependency / Constraint:** Constraint — The supported device types are unconfirmed (Q-04). Chromebooks, phones, tablets, and home computers appear in E-06 but are not confirmed.

**Priority:** 5

**Readiness:** Refine

**Priority Rationale:** Medium value and a constraint that affects every other story, but the device list is unconfirmed. Refining the list first is cheap and prevents rework. It ranks below US-04 because stakeholders gave stronger evidence for saved practice.

---

### US-06 — Store problems for a learner
 
**Requirement ID:** FR-06
**User Story:** As a parent or teacher, I want to store math problems for a learner so that the learner can practice them later.
 
**Acceptance Criteria:**
 
- Given an authorized parent, teacher, or other authorized user, when they enter a math problem for a learner, then that problem is available for the learner to practice later.
- Given a problem has been stored for a learner, when that learner starts practice, then the stored problem can be answered with feedback.
- Given a user who is not authorized, when they try to store a problem for a learner, then the problem is not stored.

**Relative Effort:** M — It adds a second type of user and a way to prepare problems, which is more than the learner-only stories.

**Dependency / Constraint:** Constraint — Only authorized users may store problems, but who counts as authorized is not defined, and Q-06 leaves open whether the original 10-problem limit applies.

**Priority:** 6

**Readiness:** Refine

**Priority Rationale:** Medium value (E-03) but it extends the original experience rather than completing the core practice loop. The authorization rule and Q-06 are unresolved, so it should be refined before commitment. It ranks below US-04 and US-05 because those affect the learner's main experience.

---

### US-07 — Practice without a printed manual
 
**Requirement ID:** NFR-03
**User Story:** As a student, I want to complete practice without needing a printed manual so that I can start on my own.
 
**Acceptance Criteria:**
 
- Given a first-time learner with no printed manual and no outside instructions, when the learner is asked to complete one practice problem, then the learner submits an answer and sees feedback.
- Given a usability check with first-time learners, when each learner attempts a practice activity, then an observer records whether the learner needed outside help.

**Relative Effort:** S — It adds no new capability and checks that the stories above are understandable on first use.

**Dependency / Constraint:** Dependency — US-01 and US-02 must exist so first-time learners have something to try.

**Priority:** 7

**Readiness:** Refine

**Priority Rationale:** Medium value and small effort, but "clear and understandable" has no agreed pass level yet. It ranks after the stories that create the experience it evaluates.

---
 
### US-08 — Keep work when a session is interrupted
 
**Requirement ID:** FR-01
**User Story:** As a student whose practice gets interrupted, I want my work kept even if I never signed out so that a lost connection or closed window does not erase it.
 
**Acceptance Criteria:**
 
- Given a learner has answered some problems, when the session ends before the learner signs out, then the learner's work up to that point is still there on return.
- Given a learner has answered no problems, when the session ends before sign-out, then returning shows a fresh practice activity.
These criteria are provisional until Q-01 and Q-05 are answered.
 
**Relative Effort:** M — It must work at any moment during practice, not only when the learner leaves on purpose.

**Dependency / Constraint:** Dependency — US-04 must exist first, and the identity/session approach must be decided (Q-01, Q-05).

**Priority:** 8

**Readiness:** Defer

**Priority Rationale:** High value, because interrupted sessions were raised by stakeholders (E-06), but it builds on US-04 and shares its unresolved identity decision. Refining US-04 first resolves most of the uncertainty. Deferring means "not yet," and it should return after US-04 is ready.

---
 
### US-09 — Parent and teacher visibility into practice
 
**Requirement ID:** FR-05
**User Story:** As a parent or teacher, I want to understand what a learner practiced and whether progress is happening so that I can support the learner.
 
**Acceptance Criteria:**
 
- Given a learner has completed a practice activity, when a parent or teacher looks at the information provided, then they can tell what the learner practiced.
- Given a learner has completed a practice activity, when a parent or teacher looks at the information provided, then they can tell whether the learner is improving.
These criteria are provisional until Q-02 and Q-03 confirm what information is needed and how it is provided.
 
**Relative Effort:** L — The scope is unconfirmed and it depends on activity information from several other stories.

**Dependency / Constraint:** Dependency — US-03 must exist first, and Q-02 and Q-03 must be answered.

**Priority:** 9

**Readiness:** Defer

**Priority Rationale:** Stakeholders want this (E-05), but the amount and method of information are unknown. It is large and uncertain, so it should not be hidden as ready work. It ranks below the saving stories because those have clearer evidence.

---

### US-10 — Same core features on every supported device
 
**Requirement ID:** NFR-02
**User Story:** As a student who uses more than one device, I want the same core practice features on each one so that practice feels the same everywhere.
 
**Acceptance Criteria:**
 
- Given a core feature from US-01 through US-03 works on one supported device type, when a learner uses another supported device type, then the same feature works there.
- Given the confirmed device list, when each device type is checked, then any missing core feature is recorded.
These criteria cannot be finalized until Q-04 confirms the support list.
 
**Relative Effort:** L — It must be checked across every supported device and may reveal additional work.

**Dependency / Constraint:** Dependency — US-01, US-02, US-03, and US-05 must exist first, and Q-04 must be answered.

**Priority:** 10

**Readiness:** Defer

**Priority Rationale:** It supports consistency but cannot be checked until the core features exist and the device list is confirmed. It is lowest because it depends on the most unfinished work and the least confirmed information.

## Open Questions Carried Forward

List each open question or assumption from `docs/requirements.md` that affects this backlog. Do not turn an unresolved question into a confirmed story.

- **Q-01:** US-04 and US-08 wait on this. Their criteria are provisional until we know what the saved practice state includes and how long it stays available.
- **Q-02:** US-09 waits on this. No story describes specific information for parents or teachers yet.
- **Q-03:** US-09 waits on this. A reporting dashboard is not confirmed, so no dashboard story exists.
- **Q-04:** US-05 and US-10 wait on this. The device support list is unconfirmed.
- **Q-05:** US-08 depends on this. No story exists for moving between devices mid-session until it is answered.
- **Q-06:** US-06 waits on this. The 10-problem limit and which original activities must be preserved are unconfirmed, so no criterion assumes them.

## Revisions After Triage and Release Planning

State what changed in this backlog because of your triage record and your Product Owner decision record.

- **US-01, US-02 — kept at ranks 1 and 2, marked Move Forward** — The triage record moved forward the high-value, ready, low-risk items (immediate feedback and retry), and the Product Owner record built its release around ready, high-value work. Both still trace to FR-02 and FR-03 and were left unchanged because they already passed the six lenses.
- **US-04, US-08 — FR-01 split into two stories** — The triage record deferred the large persistence item because its identity dependency was unresolved. Splitting the single large saving story into return-to-saved-practice (Refine) and interrupted-session (Defer) keeps the value visible while exposing what is blocked. Both keep FR-01 as the Requirement ID.
- **US-09 — marked Defer, with no dashboard story** — The triage record deferred the parent and teacher summary and the analytics dashboard because scope and reporting needs were unclear. Q-02 and Q-03 are still open here, so I did not turn them into a confirmed story.
- **US-03 — limited to counts during one activity** — The Product Owner record left out the broader progress summary to protect capacity. The counts story stays small and does not include a summary view.
- **US-04 through US-10 — Readiness labels added** — Both records showed that high value is not the same as ready. Items with unresolved questions or dependencies are marked Refine or Defer.
- **Keyboard accessibility — no story added** — The Product Owner record showed a keyboard accessibility issue becoming release-critical. `docs/requirements.md` has no validated accessibility requirement, so I did not create an unsupported story. This needs stakeholder confirmation and a new requirement before it can be backlogged.

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

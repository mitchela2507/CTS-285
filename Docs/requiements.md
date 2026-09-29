# DataMan Requirements Register

> Replace all bracketed prompts with your own project evidence and requirements. Delete the prompts before submitting.

## Project Context

The DataMan modernization project is focused on updating the original DataMan learning experience as a web application while keeping the main purpose of the original system. The primary users are students who practice independently, often with a teacher or parent nearby. The project is intended to give students a simple way to practice math, receive feedback, see their progress, and return to their saved practice without losing their work.

## Evidence Notes

Use at least four concise evidence statements. Label the source of each.

- **E-01 — Source:** DataMan Manual — Introduction and Story  
  **Evidence:** DataMan was designed as a learning tool for children and students to provide math drill, practice, exploration, and learning games. The manual identifies elementary and middle-school students as the intended users.

- **E-02 — Source:** DataMan Manual — Answer Checker  
  **Evidence:** The Answer Checker allows a learner to enter a math problem and answer and then provides feedback about whether the answer is correct. The learner can make another attempt if the first answer is incorrect.

- **E-03 — Source:** DataMan Manual — Memory Bank 
  **Evidence:** The Memory Bank allows parents, teachers, or friends to store up to 10 math problems for a child to practice later. The stored problems are presented one at a time and the learner's score is tracked.

- **E-04 — Source:** M2 Elicitation Simulation — Stakeholder Elicitation  
  **Evidence:** Teachers reported that students may pause their practice and return later, so stakeholders want a learner's saved practice state to remain available after leaving and returning to the application.

- **E-05 — Source:** M2 Elicitation Simulation — Stakeholder Elicitation  
  **Evidence:** Stakeholders identified immediate answer feedback, repeated practice after an incorrect response, and a clear way for learners to see progress as important parts of the original DataMan experience.

- **E-06 — Source:** M2 Elicitation Simulation — Complication  
  **Evidence:** Students may use DataMan on school Chromebooks, phones, tablets, and home computers. Some practice sessions may also be interrupted before students intentionally sign out.

[Add additional evidence notes if needed.]

## Functional Requirements

Write at least four functional requirements. Each requirement should describe a capability or behavior the system must provide.

### FR-01
**Requirement:** The system must automatically save a learner's practice state so the learner can return later without losing previous work.  
**Source/Rationale:** Teachers reported that students may pause practice and return later, and stakeholders want the learner's saved practice state to remain available. The M2 decision also revised this requirement to account for interrupted sessions.

### FR-02
**Requirement:** The system must provide immediate feedback indicating whether a learner's answer is correct or incorrect.  
**Source/Rationale:** The DataMan manual describes the Answer Checker as providing feedback about whether an entered answer is correct. Stakeholders also identified immediate answer feedback as an important part of the original DataMan experience.

### FR-03
**Requirement:** The system must allow a learner to continue practicing after an incorrect response.  
**Source/Rationale:** The DataMan manual shows that learners can make another attempt after an incorrect answer, and stakeholders identified repeated practice after an incorrect response as a central part of the original experience.

### FR-04
**Requirement:** The system must provide a way for learners to see their practice progress. 
**Source/Rationale:** Stakeholders identified a clear way for learners to see progress as an important part of the original DataMan experience. The DataMan manual also describes activities that track and display learner scores.

### FR-05
**Requirement:** The system must provide information that allows parents or teachers to understand what the learner practiced and whether progress is occurring. 
**Source/Rationale:** Parents and teachers stated that they want to understand learner activity and progress. The specific method for providing this information has not yet been confirmed.

### FR-06
**Requirement:** The system must allow authorized users to store math problems for a learner to practice later. 
**Source/Rationale:** The DataMan manual describes the Memory Bank as allowing parents, teachers, or friends to store math problems for a child to practice later.

[Add additional functional requirements if needed.]

## Non-Functional Requirements

Write at least three non-functional requirements. Each requirement should describe a measurable quality, constraint, or condition the system must satisfy.

### NFR-01
**Requirement:** The system must preserve a learner's saved practice state when the learner leaves the application and returns later.  
**Source/Rationale:** Teachers reported that students may pause practice and return later, and the M2 decision record identifies reliable preservation of saved practice state as a quality constraint.

### NFR-02
**Requirement:** The system must preserve a learner's practice state when a practice session is interrupted before the learner intentionally signs out. 
**Source/Rationale:** The M2 simulation revealed that some sessions may be interrupted before students intentionally sign out. The decision record revised the saved-practice requirement to account for interrupted sessions.

### NFR-03
**Requirement:** The system must provide a simple user experience that allows learners to practice without unnecessary navigation. 
**Source/Rationale:** Stakeholders stated that the modernized experience should be understandable without a printed manual and should avoid making the learner navigate unnecessary screens.

### NFR-04
**Requirement:** The system must support no more than 10 stored math problems at one time insid eof The Memory Bank game.  
**Source/Rationale:** The DataMan manual specifies that the original Memory Bank can store up to 10 problems.

[Add additional non-functional requirements if needed.]

## Open Questions / Assumptions

Do not turn an unsupported idea into a confirmed requirement. Record unresolved items here until evidence supports a decision.

- **Q-01:** [What still needs to be clarified or confirmed?]
- **Q-02:** [What still needs to be clarified or confirmed?]
- **Q-03:**
- **Q-04:**
- **Q-05:**
- **Q-06:**

[Add or remove items as appropriate.]

## Final Quality Check

Before submitting, confirm that each requirement is:

- [ ] Clear enough for another team member to interpret consistently.
- [ ] Supported by evidence, a stakeholder need, or a confirmed project constraint.
- [ ] Testable or verifiable later.
- [ ] Solution-neutral enough for this stage of the project.
- [ ] Focused on one main capability or quality.
- [ ] Classified correctly as functional or non-functional.

Also confirm:

- [ ] At least four functional requirements are included.
- [ ] At least three non-functional requirements are included.
- [ ] Every confirmed requirement has a source/rationale.
- [ ] Open questions and assumptions are separated from confirmed requirements.
- [ ] The simulation decision record is saved at `docs/decisions/m2-elicitation-decision-record.md`.
- [ ] This file is saved as `docs/requirements.md`, committed, and synced to GitHub.

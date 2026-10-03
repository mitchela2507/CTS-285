# DataMan Requirements Register

## Project Context

The DataMan modernization project is focused on updating the original DataMan learning experience as a web application while keeping the main purpose of the original system. The primary users are students who practice independently, often with a teacher or parent nearby. The project is intended to give students a simple way to practice math, receive feedback, see their progress, and return to their saved practice without losing their work.

## Evidence Notes

- **E-01 — Source:** DataMan Manual — Introduction and Story  
  **Evidence:** DataMan was designed as a learning tool for children and students to provide math drill, practice, exploration, and learning games. The manual identifies elementary and middle-school students as the intended users.

- **E-02 — Source:** DataMan Manual — Answer Checker  
  **Evidence:** The Answer Checker allows a learner to enter a math problem and answer and then provides feedback about whether the answer is correct. The learner can make another attempt if the first answer is incorrect.

- **E-03 — Source:** DataMan Manual — Memory Bank 
  **Evidence:** The Memory Bank allows parents, teachers, or friends to store up to 10 math problems for a child to practice later. The stored problems are presented one at a time and the learner's score is tracked.

- **E-04 — Source:** M2 Elicitation Simulation — Stakeholder Elicitation  
  **Evidence:** Teachers reported that students may pause their practice and return later, so stakeholders want a learner's saved practice state to remain available after leaving and returning to the application.

- **E-05 — Source:** M2 Elicitation Simulation — Stakeholder Elicitation  
  **Evidence:** Stakeholders identified immediate answer feedback, repeated practice after an incorrect response, and a clear way for learners to see progress as important parts of the original DataMan experience. Parents and teachers also want to understand what the learner practiced and whether progress is occurring.

- **E-06 — Source:** M2 Elicitation Simulation — Complication  
  **Evidence:** Students may use DataMan on school Chromebooks, phones, tablets, and home computers. Some practice sessions may also be interrupted before students intentionally sign out.



## Functional Requirements

### FR-01
**Requirement:** The system must automatically save a learner's practice state so the learner can return later without losing previous work.  
**Source/Rationale:** E-04 identifies the need for learners to return to their practice later. E-06 explains that sessions may be interrupted before the learner signs out, making it important to preserve the learner's work.

### FR-02
**Requirement:** The system must provide immediate feedback indicating whether a learner's answer is correct or incorrect.  
**Source/Rationale:** E-02 describes the Answer Checker's feedback behavior, and E-05 identifies immediate answer feedback as an important part of the original DataMan experience.

### FR-03
**Requirement:** The system must allow a learner to make another attempt on the same problem after an incorrect response.
**Source/Rationale:** E-02 states that the learner can make another attempt after an incorrect answer, and E-05 identifies repeated practice after an incorrect response as an important part of the original experience.

### FR-04
**Requirement:** The system must show the learner the number of correct answers and the number of problems attempted during a practice activity.
**Source/Rationale:** E-05 identifies seeing progress as an important part of the original DataMan experience, and E-03 states that the Memory Bank tracks the learner's score.

### FR-05
**Requirement:** The system must provide information that allows parents or teachers to understand what the learner practiced and whether progress is occurring.
**Source/Rationale:** E-05 states that parents and teachers want to understand learner activity and progress. The specific method for providing this information has not yet been confirmed.

### FR-06
**Requirement:** The system must allow parents, teachers, or other users authorized by the project to store math problems for a learner to practice later.
**Source/Rationale:** E-03 describes the DataMan Memory Bank as allowing parents, teachers, or friends to store math problems for a child to practice later.



## Non-Functional Requirements

### NFR-01
**Requirement:** The system must support access through a web browser on the device types confirmed for project support.
**Source/Rationale:** E-06 identifies school Chromebooks, phones, tablets, and home computers as devices students may use to access DataMan. The exact device and access requirements still need to be confirmed.

### NFR-02
**Requirement:** The system must provide the same core practice features on each device type selected for project support.
**Source/Rationale:** E-06 identifies several devices that students may use. Providing the same core practice features across the devices selected for support would help maintain a consistent experience. The required devices have not yet been confirmed.

### NFR-03
**Requirement:** The system must be usable by learners without requiring a printed manual to complete their practice activities.
**Source/Rationale:** E-05 identifies a clear and understandable learner experience as an important part of the DataMan experience.


## Open Questions / Assumptions

- **Q-01:** What specific information should be included in a learner's saved practice state, and how long should it remain available?
- **Q-02:** What specific information should parents and teachers be able to see about learner activity and progress?
- **Q-03:** What method should be used to provide parents and teachers with information about learner activity and progress? A detailed reporting dashboard has not been confirmed.
- **Q-04:** What specific device and access conditions must the modernized system support?
- **Q-05:** How should the system handle a learner moving between different devices during an unfinished practice session?
- **Q-06:** Which original DataMan activities and limits, such as the Memory Bank's 10-problem limit, must be preserved in the modernized system, and which activities can be changed or removed?

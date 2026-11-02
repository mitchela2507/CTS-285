# M4 Design Investigation Record

## Product Slice
US-02 — Retry after an incorrect answer; US-03 — See correct and attempted counts

## Initial Question
What attempt state must exist for each problem so the design can tell try 1 from try 2, and how should that state affect the correct and attempted counts when a learner retries?

## Planned Evidence
Field/state table + acceptance-criteria trace

## Evidence Actually Used
- Use-case boundary / actor-goal framing
- Behavior/state flow and two-attempt simulation
- Data-model/schema and Memory Bank constraint stress tests
- Interface/wireframe comparison and state audit
- Design complication and critique

## Findings
### Use-Case Boundary / Question Framing
Learner  —  practice a math problem and learn from a mistake by trying it again. Question: What must the learner see after the first wrong attempt so that the answer stays hidden, a second try is clearly available, and the counts don’t change unexpectedly?

### Behavior / State
The behavior run answered how a first miss differs from a second miss. After two wrong answers the observer showed try_number 2, status complete_after_second_miss, reveal_allowed true and feedback “EEE + reveal.” After a correct first try it showed try_number 1, status correct, reveal_allowed false and feedback “correct.” So the same wrong answer has different consequences depending on the try number, and the system has to record the try number before it judges the answer. The run also showed that reporting can tell correct-on-try-1 from correct-on-try-2 only if the try number is kept beyond the screen, which sharpens my question about what each Attempt record must store. The two-attempt limit and the second-miss reveal are not stated in US-02 or FR-03, so this evidence exposed a rule my backlog doesn’t yet specify. I did not observe the correct-on-second-try path, so what it shows for counts is still open.

### Data / Persistence
A screen sketch would show a problem, an answer box and feedback, but not what has to be stored behind it. The repair step showed that the rushed model could not represent the behavior: a single learner_answer on Problem would overwrite the first try, a comma-separated problem list in PracticeSet would hide set membership, and a lone final_score would lose which problems were missed. When I inspected my relationship claims (Learner to Attempt 1:M, Problem to Attempt 1:M, Practice Set to Problem M:N), the tool confirmed that attempt history was preserved, problems could be reused, and set membership could be counted. The ceiling test also showed that the 10-problem limit has to be enforced beyond the screen: the eleventh problem was rejected, and the tool noted that a future Flask route must not be able to create an invalid 11-item set.

### Memory Bank Constraint
When I tried to add an eleventh problem, the Constraint observer rejected it. This taught me that the design has to define what happens at the limit, and that the rule can’t depend on one screen, because a future Flask route must not be able to create an invalid 11-item set. I chose business logic with storage support as the place to enforce the rule, and the tool confirmed it as a defensible boundary: business logic owns the rule, storage reinforces integrity, and the interface only communicates the consequence to the user. The limit is checked before membership is created, so it is a rule about the relationship between a Practice Set and its Problems, not about a single interface. My backlog’s Q-06 still leaves open whether the original 10-problem limit must be preserved at all.

**Constraint boundary selected:** both

### Interaction
The wireframes showed that the interface can’t be the source of the practice state. Approach A shows a score but not the try number, so a learner can’t tell a first try from a second. Approach B shows “Try 2 of 2” and feedback with text and a symbol, but it also offers a Retry button on the second try, which conflicts with the rule that a second miss reveals the answer. That told me the interface must display the outcome and next action returned by the business logic, not decide them itself. The interface audit covered visible feedback, state, recovery, persistence and another actor’s retrieval path, and neither wireframe shows how a curator retrieves results. The retrieval test compared three paths. A live score panel is simple during practice but a curator cannot retrieve results later. A stored session summary supports later score retrieval but may lose which problems were missed or how many tries they took. Only learner history, session and problem attempts supports retrieval of score, missed problems and try history, at the cost of more structure. That matches my Memory Bank lab, where the curator query returned P2 and P5, so I would accept the extra structure because the requirement is to see which problems were missed, not just a score.

## Layer Boundary Notes
**Business behavior that should remain outside the interface:**
The two-attempt rule: recording the try number, deciding whether the answer is correct, allowing a retry after the first miss, and allowing the reveal only after the second miss. The observer’s consequence note makes the point: if reveal lived only in interface code, another interface could behave differently by accident. The rule should return the outcome and state (try number, status, reveal allowed, feedback) so the text interface, and later Flask, only display what they are told.

**Data that can be stubbed now:**
I can keep three things in memory: a list of Attempt records (attempt_id, session_id, problem_id, try_number, submitted_answer, correct), a list of PracticeSetProblem memberships (set_id, problem_id), and a Session/Result record tied to the learner. The business logic would read and write them only through a small set of functions, such as save_attempt, get_attempts_for_session and add_problem_to_set. The two-attempt rule and the 10-problem limit would live in that logic, with the membership count checked before a problem is added, so the interface only communicates the result. Later, the in-memory lists can be replaced by a database with storage-level integrity checks, without changing the rules or the text interface.

## New Complication
**Response:** Revise state boundary

I chose to revise the state boundary. In the behavior lab, the observer showed that reporting can distinguish correct-on-try-1 from correct-on-try-2 only if the try number survives beyond the screen. In the Memory Bank lab, the curator query returned P2 and P5 only because each Attempt record kept problem identity, try number and session. If the process closes after Try 1 and the try number lived only in the interface, that history would be lost, so the Attempt state has to be persisted behind the business logic so resume and reporting use the same source of truth. This is more work than keeping the design as it was, but it is the only option the evidence supports.

## Build-Readiness Decision
**Disposition:** Revise

**Design decision:**
Revise US-02 and US-03 before coding. Add acceptance criteria for the two-attempt rule: after a first incorrect answer the answer stays hidden and a second try is accepted, and after a second incorrect answer the correct answer is revealed and no further retry is offered. Keep the try number in Attempt records (problem_id, try_number, correct, session_id) behind the business logic, so the interface only displays the outcome and state it returns. US-03’s attempted count should count a problem once, on its first attempt.

## Revision From Initial Thinking
I first treated US-02 and US-03 as two small, independent stories. The labs and Studio showed they share one piece of state, the try number for each problem, and that it can’t live only on the screen. I also found that US-02 does not mention the second-miss reveal or the two-attempt limit, even though the behavior evidence depended on them.

## Tradeoff Accepted
I accept the extra structure of separate Attempt records and a data boundary instead of a simple score on the screen. I also accept that cross-session resume stays in US-04 and US-08 instead of being built now.

## Unresolved Uncertainty
Q-01: what saved practice includes. It’s still unclear whether a learner interrupted after a first miss should resume at try 2. Whether two curators may see the same learner’s history is a product and privacy question that my current evidence can’t answer. It needs stakeholder input, and my requirements don’t yet define who counts as an authorized curator. I also haven’t tested the correct-on-second-try path for the counts.

## Next Question
When a learner closes the program after a first miss, should returning resume at try 2 with the same problem, and what must be stored so US-04 can do that without changing the Attempt records I’m defining now? A separate question for stakeholders is who may view a learner’s attempt history, since that decides what the curator retrieval path may expose.

## Three-Layer Prototype Bridge
Text interface: input and output only. It shows the problem, accepts the learner’s answer, and displays what the business logic returns: the try number, the feedback (EEE for incorrect, correct), the revealed answer after the second miss, and the correct and attempted counts. It decides nothing about when to reveal, when to allow a retry, or whether a set is full.

Business logic: the rules. It records the try number before judging the answer, decides correct or incorrect, allows a retry after the first miss, and allows the reveal only after the second miss. It counts a problem as attempted once, on its first attempt, and checks the 10-problem limit before a problem joins a set. It returns the outcome and state (try number, status, reveal allowed, feedback) to the interface.

Stubbed data layer: in-memory stand-ins for problems, Attempt records (problem_id, try_number, correct, session_id), PracticeSetProblem memberships, and Session/Result records tied to the learner. It is reached only through replaceable access functions, such as save_attempt, get_attempts_for_session and add_problem_to_set, so a database or Flask route can replace it later without changing the rules or the interface.

## Trace Back to Product Work
US-02 — FR-03 (E-02, E-05): “the same problem is still available to answer” after an incorrect result. FR-03 and E-02 say “another attempt” but set no limit. US-03 — FR-04 (E-03, E-05): attempted count increases when a learner submits an answer “for the first time.” Neither story says what happens after a second incorrect answer, or whether a retry changes the counts.

# M4 Investigation Brief

## Product Slice
US-02 — Retry after an incorrect answer; US-03 — See correct and attempted counts

## Trace to Product Work
US-03 says the attempted count increases when a learner submits an answer “for the first time,” while US-02 lets the learner answer the same problem again after an incorrect result. Together these mean the design must distinguish try 1 from try 2 for the same problem. My backlog doesn’t say where that attempt state is held, whether a retry changes the counts, or what happens after a second incorrect answer. I need to understand this before the practice loop (FR-03, FR-04) can be designed reliably.

## Initial Design Question
**Question type:** Data / State

What attempt state must exist for each problem so the design can tell try 1 from try 2, and how should that state affect the correct and attempted counts when a learner retries?

## Why This Question Matters
US-02 lets the learner answer the same problem again, and US-03 counts a problem as attempted only the first time it’s answered. If I code the retry flow and the counts separately, I could easily build them with conflicting assumptions, for example counting every retry as a new attempt or losing the first-try result when the learner answers again. My backlog also doesn’t say what happens after a second incorrect answer, so I’d be guessing at the stopping point. Fixing that after the feedback, retry and count behavior were already built would mean reworking all three, and the open attempt-state decision could ripple into US-07’s first-use check as well.

## Planned Evidence
- Field or state table
- Acceptance-criteria trace

## Why This Evidence Is a Reasonable Starting Point
My question is about what attempt state must exist for each problem and how a retry affects the correct and attempted counts. A field or state table is the smallest evidence that answers that: it shows what is tracked and how each value changes on a first try, a retry, and a second incorrect answer. An acceptance-criteria trace then checks that table against US-02 and US-03, so I can see whether each criterion is supported or whether the two stories make conflicting assumptions. I’m not starting with an ERD because the question concerns state within one practice activity, not relationships between entities. I’m open to changing the evidence if the table shows the question is really about something else.

## Studio Check
During the DataMan Design Studio, record whether the evidence actually answered the question, whether you needed different evidence, and what new question emerged.

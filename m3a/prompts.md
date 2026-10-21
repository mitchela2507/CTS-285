# AI Prompt Log — Fall Break Adventure

This document logs the staged prompts used during the planning, designing, and testing of *The Lost Artifact of Blackwood Manor*.

## Stage 1: Player Interview & Requirements

**Prompt:**

> "Here are the sides for the assignment, and the zip with all necessary materials. I would like you to perform the interviewer role with ME as the customer. Ask me the 5 interview questions from Step 1 one by one and then design and build the game."

**What the AI gave me:**
Asked the 5 core player interview questions sequentially and waited for user input after each response.

**What I kept, changed, or threw away:**
Kept all answers as raw player evidence (E01 through E06) to populate Section 1 of `brief.md`.

## Stage 2: Drafting Brief & Requirements

**Prompt:**

> "Here are my answers to your interview questions... Now draft the brief.md file matching the exact template with user stories, acceptance criteria, budget, state table, and flowchart."

**What the AI gave me:**
Translated raw customer evidence into structured User Stories (US1–US5), Acceptance Checks, Budget/Cut list, a passage map flowchart, and state tracking tables.

**What I kept, changed, or threw away:**
Kept the entire structure and matched it directly to `brief-template.md`. Verified that every user story linked back to a recorded evidence ID.

## Stage 3: Code Implementation & State Management

**Prompt:**

> "Build the Python implementation (`adventure_start.py`) with structured `passage_` functions, `ask()` helper for input validation, inventory tracking, and 3 distinct endings."

**What the AI gave me:**
Complete, working Python code containing passage functions, a global `inventory` array, clean loop validation in `ask()`, and 3 branching endings.

**What I kept, changed, or threw away:**
Kept the complete function layout. Confirmed that inventory item tracking (`key`) gated access to `passage_desk_drawer` as outlined in the planning table.

## Stage 4: Narrative Flow & State Verification

**Prompt:**

> "Check the passage connections and inventory tracking in `adventure_start.py` to make sure all choices lead to a valid passage and that the game loop completes properly."

**What the AI gave me:**
A detailed breakdown verifying that each choice leads to a valid passage function, confirming that state tracking works correctly, and explaining the state variable table in Section 6.

**What I kept, changed, or threw away:**
Recorded 5 of 5 passed acceptance checks in Section 8 of `brief.md` and finalized the project decision as "Accept".
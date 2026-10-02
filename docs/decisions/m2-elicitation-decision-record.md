# M2 Elicitation Decision Record

## Investigation Path
1. What exactly do stakeholders mean by “students shouldn’t lose their work”?
   Evidence revealed: Teachers report that students may pause practice and return later. They want a learner’s saved practice state to remain available after leaving and returning to the application.
2. What do parents or teachers need to understand about learner activity?
   Evidence revealed: Adults want to understand what the learner practiced and whether progress is occurring, but stakeholders have not yet agreed on a detailed reporting dashboard.
3. Who will use the system and in what setting?
   Evidence revealed: The primary learner is a student practicing independently, often with a teacher or parent nearby. Exact device and access conditions have not yet been confirmed.

## Initial Position
**Supported evidence:**
Students need to be able to leave their practice and return later without losing their saved practice state. Adults such as teachers or parents also need to understand what the learner practiced and whether progress is occurring. The primary learner is a student practicing independently, often with a teacher or parent nearby.

**Remaining uncertainty:**
It is still uncertain how the saved practice state should work, such as exactly what information needs to be saved and how long it should remain available. It is also uncertain what specific information parents and teachers should see because stakeholders have not agreed on a detailed reporting dashboard. The exact devices and access conditions are also still unknown.

**Likely functional requirement:**
The system shall save a learner’s practice state so the learner can return later and continue their practice without losing their previous work.

**Likely non-functional requirement / quality constraint:**
The system should preserve a learner's saved practice state reliably when the learner leaves and later returns to the application.

**Assumption or proposed solution I am not treating as confirmed:**
I am not treating a detailed parent or teacher reporting dashboard as a confirmed requirement because stakeholders have only said that adults need to understand learner activity and progress. They have not confirmed that a dashboard is the solution.

**Why my initial position is defensible:**
My initial position is defensible because the requirements are based on evidence gathered directly from stakeholders. The need to preserve saved practice state is supported by teachers reporting that students may pause and return later. The need for adults to understand learner activity and progress is also supported, but the exact reporting features remain uncertain. I am not adding specific technologies, devices, or dashboard features that stakeholders have not confirmed.

## Complication
Students may use DataMan on school Chromebooks, phones, tablets, and home computers. Some sessions may be interrupted before intentional sign-out.

**What this affects:**
This affects the saved-practice requirement and the quality constraint because the system may need to preserve a student's work even when a session is interrupted unexpectedly. It also shows that the system needs to work across different types of devices.

**What I revised, if anything:**
I would revise the functional requirement slightly where the system shall automatically save a learner's practice state so the learner can return later without losing their work, including after an interrupted session.

**Final decision and reasoning:**
Revise: I would revise the saved-practice requirement to include interrupted sessions. The new information provides evidence that students may use different devices and may leave the application unexpectedly. Because of this, simply requiring students to leave and return later does not fully address the situation. The requirement should account for automatically preserving their practice state when a session is interrupted. I would still defer decisions about the exact devices, reporting dashboard, and technical solution until more evidence is gathered.

## Next Project Action
Use this evidence to update the DataMan Requirements Register and preserve any unresolved questions as open assumptions or follow-up items.

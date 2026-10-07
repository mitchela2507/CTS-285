# M3 Backlog Triage Decision Record

## Round 1 and Revised Decisions
| ID | Backlog Item | Round 1 | Revised | Value | Effort | Dependency | Risk |
|---|---|---|---|---|---|---|---|
| S1 | Immediate answer feedback | Move Forward | Move Forward | High | Small | None | Low |
| S2 | Preserve learner progress between sessions | Refine | Defer | High | Large | Identity/session approach | Medium |
| S3 | Decorative theme selector | Defer | Defer | Low | Small | None | Low |
| S4 | Parent/teacher activity summary | Refine | Defer | Medium | Medium | Activity data | Medium |
| S5 | Retry after an incorrect response | Move Forward | Move Forward | High | Small | Answer-checking flow | Low |
| S6 | Advanced analytics dashboard | Defer | Defer | Medium | Large | Reporting model | High |

## Complication
The account/session approach is not ready, increasing uncertainty for work that assumes persistent identity. The instructor stakeholder also states that immediate answer feedback is required for the first usable release.

## Decisions Changed After New Information
- S2: Refine → Defer
- S4: Refine → Defer

## Reflection Prompts for Canvas
1. Which one decision was hardest to make, and what tradeoff mattered most?
   - The hardest call was S4, the parent/teacher activity summary. It had medium value and a real stakeholder interest, but the reporting depth wasn't settled and it depended on activity data. The tradeoff was responding to stakeholder visibility needs versus committing effort to a story whose scope was still unclear. I chose Refine at first because the need was real but the details weren't ready for development.
2. Which decision changed after the complication, and why? If none changed, explain why your original decisions still held.
   - S2 and S4 both changed from Refine to Defer. The team learned the account/session approach wasn't ready, and both stories depend on recognizing a learner across sessions. Their value didn't drop, but their readiness did, and refining them further would likely have meant rework. Neither was required for the first usable release, so deferring them let the team focus on S1 and S5. S1 stayed at Move Forward, and the instructor's requirement confirmed it was the right call.
3. What will you carry into your DataMan product backlog before the Product Owner Sprint Simulation?
   - I'll separate value from readiness when prioritizing, since a high-value item can still be blocked. I'll name dependencies explicitly on each story and treat unresolved ones, like identity or data models, as decisions to make early. I'll also record why an item was deferred and what would bring it back, so "not now" doesn't turn into "never" by accident.

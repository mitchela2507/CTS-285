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

1. [US-__]
2. [US-__]
3. [US-__]
4. [US-__]

## Stories

<!-- Copy one story block for each story. Do not change the field labels. -->

### US-01 — [Short title]

**Requirement ID:** [FR-__ or NFR-__ from `docs/requirements.md`. If the story traces to more than one requirement, list each ID.]

**User Story:** As a [user or role], I want [capability or outcome] so that [value or reason].

**Acceptance Criteria:**

- Given [starting condition], when [action or event], then [observable result].
- [Write one line for each condition. Each line must state a result that another person can see and check.]

**Relative Effort:** [S / M / L] — [One sentence. Compare this story to the other stories in this backlog, not to hours or days.]

**Dependency / Constraint:** [The story, decision, or constraint that must exist first. Write "None" if there is none.]

**Priority:** [Rank number from the Priority Order list.]

**Readiness:** [Move Forward / Refine / Defer]

**Priority Rationale:** [Why this rank is defensible. Name the factors you used: value, effort, dependency, risk, uncertainty, or stakeholder need.]

---

### US-02 — [Short title]

**Requirement ID:** [FR-__ / NFR-__]

**User Story:** As a [user or role], I want [capability or outcome] so that [value or reason].

**Acceptance Criteria:**

- Given [starting condition], when [action or event], then [observable result].

**Relative Effort:** [S / M / L] — [comparison]

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

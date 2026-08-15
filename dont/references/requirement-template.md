# Document Templates

Produce a document only after the user picks A or C in the delivery choice (document only / document and start building; see SKILL.md). The document expands the constraint summary already delivered in the final summary (goal and success metric, P0 feature list, out-of-scope list, acceptance criteria, key risks). First confirm the document type and audience, then use the matching template. Save the document as a Markdown (.md) file; confirm the filename and location with the user. If the target file already exists, ask for explicit confirmation before overwriting. Write in the user's language and produce detailed, complete content covering every section.

## Type Selection

Present a short menu first and expand only when needed (progressive disclosure).

Default options:
- Requirements document - for product managers, clients, or stakeholders.
- Development document - for developers implementing the project.
- Process document - for business, user, or operational flows.
- Other - show the full list below.

Full list (shown when "Other" is chosen):
- Test & acceptance document - for QA and sign-off.
- Project plan - for tracking schedule, tasks, and resources.
- Decision & evaluation record - for documenting why this was chosen.
- User manual - for end users.
- Custom - ask what it is for and who reads it.

## Requirements Document (PM / Client)

- Title: project name and one-line summary.
- Goals: primary goal and success metrics.
- Target users: primary user(s) and main job-to-be-done.
- Scope: in scope for v1; explicitly out of scope.
- Core features (MVP): feature list with priority P0 (must) / P1 (should) / P2 (nice).
- Non-functional requirements: performance, security, data/privacy, accessibility, compatibility.
- Acceptance criteria: how each core feature is verified.
- Risks: top risks and mitigations.
- Open questions: unresolved items from the interview.

## Development Document (Developers)

- Title and overview.
- Technical approach: stack, architecture, key decisions.
- Modules/components: responsibilities and boundaries.
- Data model: entities, relationships, storage.
- Interfaces/APIs: endpoints or contracts.
- Implementation steps: ordered tasks; the first step should be actionable today.
- Milestones: v1 (MVP) -> v2 -> later.
- Environment & constraints: platforms, deployment, dependencies.

## Process Document (Flows)

- Title and purpose of the process.
- Actors: who participates.
- Main flow: numbered step-by-step flow.
- Branches: edge cases, exceptions, failure paths.
- States: state transitions if applicable.
- Rules: business rules, permissions, validation.
- Open questions.

## Test & Acceptance Document (QA / Sign-off)

- Scope and objectives of testing.
- Test environment: platforms, versions, data.
- Test cases: ID, prerequisites, steps, expected result.
- Acceptance criteria: pass conditions for each core feature.
- Known gaps and deferred items.

## Project Plan (Schedule & Resources)

- Goal and scope summary.
- Milestones: v1 (MVP) -> v2 -> later, with target dates.
- Task breakdown: tasks, owners, dependencies.
- Schedule and resources: timeline, people, budget.
- Risks and mitigations.
- Communication and collaboration (optional).

## Decision & Evaluation Record (Why)

- Background and the question being decided.
- Candidate options: including existing solutions (name, link, pros, cons).
- Evaluation dimensions: cost/benefit, feasibility, existing solutions, purpose.
- Suggested conclusion and reasons.
- Final decision: filled in after the user decides.
- Next actions.

## User Manual (End Users)

- Product introduction.
- Quick start: install and launch.
- Feature guide: how to use each feature.
- FAQ.
- Support and contact.

Keep every section detailed and complete; trim only if the user asks.

# Question Tiers

Question banks and exit rules for each stage. Ask one or a few questions at a time, prefer choice-style questions, and go deeper when an answer is vague or important. Stop early when the user asks for a direct conclusion. In every round, number questions (1., 2., 3.) and letter options (A., B., C.), and invite shorthand answers like "1A" or "A1" (see SKILL.md > Conversation Format).

## Stage 1 - Intent Understanding

Purpose: understand the shallow intent first, then restate an optimized understanding for confirmation.

Flow:
1. Ask 2-4 shallow questions about the idea.
2. Restate the intent in optimized, clearer wording.
3. Confirm with the user; note any unknowns.

Question bank (ask 2-4):
- What exactly do you want to build? One-sentence description?
- Which product type fits best: website, app, frontend, backend, tool, skill, agent, other?
- Who is it for: yourself, a specific group, or everyone?
- What problem does it solve, or what need does it serve?
- Why do you want to build it now?

Exit: the user confirms the restatement, or corrects it once and the correction is clear.

## Stage 2 - Requirement Analysis (5W2H)

Purpose: fill only the gaps left after Stage 1, using 5W2H.

Flow:
1. Start from what Stage 1 already established; do not re-ask clear dimensions.
2. Ask only the dimensions that are unknown or ambiguous.
3. When the needed dimensions are settled, output a short 5W2H recap table: dimension and status (clear / pending / not applicable).

Question bank (ask only the relevant dimensions):
- What: what exactly is the product or feature? Core scope?
- Why: why build it? What is the purpose (learning, commercial, portfolio, personal)?
- When: when does it need to be ready? Any deadline or timing constraints?
- Where: where will it run or be used (platform, region, market)?
- Who: who are the target users? Who maintains it?
- How: how should it work? Preferred approach or stack?
- How much: how much time, budget, or scale? How many features, users, or data?
- Technical level can be asked here when a dimension (e.g. How) needs it to give advice; it is not limited to Stage 3.

Exit: What, Why, and Who are clear; the remaining dimensions are marked known or unknown.

## Stage 3 - Background Research

Purpose: find existing solutions first, then understand the user's background.

Flow:
1. Search for existing solutions, similar products, and similar-feature artifacts (no platform limit, GitHub primary, including agents and skills). Follow [search-and-comparison.md](search-and-comparison.md). Do not ask permission to search by default; if the user has asked for confirmation before actions, or the platform requires it, ask first. The user can interrupt or skip it anytime.
2. If relevant results are found, present a comparison table (up to 5 candidates); do not ask for a path choice here - that belongs to Stage 4 (Decision Conclusion).
3. Then ask about the user's background.

Background question bank (ask 3-6):
- How much time can you invest: weeks, months, or hobby-level effort?
- What is your budget, if any?
- What is your technical level? A. Beginner (follow tutorials) B. Intermediate (can build small projects) C. Advanced (professional) - this determines how technical the explanations should be (see SKILL.md > Technical-Level Adaptation).
- Are there development environment constraints (platform, language, deployment, company policy)?
- Would you rather maintain something you built, or start from an existing project?

Exit: the competitive landscape is known and the user's constraints are clear.

## Stage 4 - Decision Conclusion

Purpose: synthesize and give a suggestive conclusion with reasons.

- Frame the conclusion as a recommendation, not a final verdict: "I suggest ...".
- Options: build / don't build / use existing / adapt existing.
- Give 2-4 evidence-based reasons, and a concrete alternative if the suggestion is not to build.
- Let the user make the final call; if they disagree, ask what changed and re-evaluate.

Exit: the user acknowledges the suggestion and decides, or asks to continue.
If the suggestion is not to build, present alternatives and end the workflow; do not proceed to Stage 5.

## Stage 5 - Requirement Deepening

Purpose: deepen the requirements only after the user decides to build.

Question bank (ask 5-10, choosing by product type):
- Goals & success: what does success look like? How would you measure it?
- Users: who exactly uses it? What is the main job-to-be-done?
- Core features (MVP): what is the minimum set of features to be usable?
- Priority: which features are must-have vs nice-to-have? Ask the user to rank them.
- Scope boundaries: what is explicitly out of scope for v1?
- Non-functional: performance, security, data/privacy, accessibility, mobile support?
- Tech preferences/constraints: languages, frameworks, platforms, existing code, deployment?
- Content/data: where does the data come from? Who maintains it?
- Risks: what could make this fail? What is hardest to build?

Exit: the MVP feature list is clear and prioritized, and scope/constraints are defined.

After all questions are done: deliver a final summary - the conclusion in one or two sentences, a one-line technical route (what technology or base project to use and how to proceed), a compact constraint summary (goal and success metric, P0 feature list, out-of-scope list, acceptance criteria, key risks), plus 2-3 targeted improvement suggestions by product type (see improvement-checklist.md) - then present the delivery choice:
- A. Document only - produce a document now; decide about development later.
- B. Conclusion only - no document.
- C. Document and start building - produce the document, then end the skill workflow; subsequent development is normal agent work outside the skill.

For A or C, confirm the document type and audience. Present a short menu first (progressive disclosure):
- Requirements document - product managers or clients: goals, target users, features, priorities, scope, acceptance criteria.
- Development document - developers: technical approach, architecture, modules, interfaces, data model, implementation steps.
- Process document - business, user, or operational flows with steps, branches, and rules.
- Other - expand to: test & acceptance document (QA/sign-off), project plan (schedule, tasks, milestones, resources), decision & evaluation record (why this option was chosen), user manual (end-user guide), custom (ask what it is for and who will read it).

Confirm the filename and location, save the document as a Markdown (.md) file, and produce it only after explicit agreement (see requirement-template.md).

## Skipping & Shortcuts

- If the user says "直接给结论", "just decide", "skip", or similar, move immediately to the decision stage using available information and state what was skipped.
- If the user interrupts with new information, incorporate it and continue from the current stage.

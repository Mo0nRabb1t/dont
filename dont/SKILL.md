---
name: dont
description: Clarify and evaluate development-related ideas through staged multi-turn questioning, then deliver a suggestive verdict with reasons and implementation guidance. Use when the user wants to build or make a software product (website, app, frontend, backend, tool, skill, agent, or other), asks whether an idea or an existing project is worth doing, or asks to organize or analyze requirements. Runs a progressive interview in five stages (intent understanding, requirement analysis, background research, decision conclusion, requirement deepening), adapts to the user's language (English default), and researches existing solutions with GitHub as the primary source and no platform restrictions, including agents and skills. The skill ends once a conclusion or document is delivered; actual development is outside its scope.
---

# D.O.N.T (Do or Not To)

Clarify any development idea through staged, multi-turn dialogue and conclude with a clear recommendation and an actionable plan.

## Scope

D.O.N.T only supports decision-making and requirement clarification for development ideas. The workflow ends once a conclusion or document is delivered. Subsequent development, implementation, and maintenance are outside the skill's scope; if the user continues into development, treat it as normal agent work, not part of this skill. Existing-project continuation is also outside this skill's scope; if asked whether to continue an existing project, treat it as normal agent work.

## Core Behavior

- Ask one or a few questions at a time (keep each round to 3-5 questions); adapt the number to the answers, preferring more and more detailed questions.
- Mix question formats: multiple-choice where possible, open-ended for key details.
- Allow the user to interrupt, skip a stage, or request a direct conclusion at any time; honor that immediately.
- User instructions and preferences take priority over this skill's defaults; honor explicit user constraints (e.g. "ask before acting").
- Respond in the user's input language; default to English when the input is ambiguous.
- Always number questions and letter options so the user can reply with shorthand; never present unlabeled options.

## Conversation Format

- Number questions sequentially within each round: 1., 2., 3. Label every option with a letter: A., B., C.
- Tell the user they can reply with shorthand: "1A" or "A1" both mean question 1, option A. Separate multiple answers with spaces, e.g. "1A 2B 3C" or "A1 B2 C3"; the order inside a pair does not matter.
- For open-ended questions, keep the number and accept either free text or a targeted answer like "3: <answer>".
- Accept shorthand, full free text, or a mix; never require the user to repeat the question.
- End each round with a one-line format hint in the user's language, e.g. "Reply format: 1A 2B 3C".
- End each reply with a one-line session summary in the user's language, e.g. `已确认: ... | 待确认: ...`; update it every round and use it to avoid re-asking answered questions.

Example (adapt the wording to the user's language):

1. Who is the target user?
   A. Myself / friends (personal tool)
   B. General users
   C. A specific group (budget travelers, students, frequent flyers)
2. What is the core pain point compared with existing apps?
   A. Low prices are hidden and need constant re-checking
   B. Comparison is incomplete or not cheap enough
   C. Better, lighter, ad-free experience
   D. Other (describe it)

Reply: "1A 2B" or "A1 B2" - question number plus option letter, either order.

## Response Style

- Open each reply with content, not process narration: a short restatement when confirming, otherwise the questions themselves.
- Keep replies to content only: no stage or round announcements, no "I will now ..." narration; a minimal transition like "Next:" is enough.
- Skip answer echoes and filler prefixes ("received", "noted"); go straight to the substance.
- Keep the reply-format hint to one short line.

## Technical-Level Adaptation

- Determine the user's technical level early (beginner, intermediate, or advanced) from the background questions; confirm it if unclear.
- Adapt every explanation to that level:
  - Beginner: explain each technical term in plain language the first time it appears (e.g. "Flutter (a cross-platform app framework)"), avoid unexplained acronyms, and keep recommendations high-level.
  - Intermediate/advanced: use standard professional terms directly.
- Re-check the level if the user's later answers suggest a different one.
- Apply this especially to existing-solution comparisons (Stage 3), the decision recommendation (Stage 4), and the development document (Stage 5).

## Workflow

Follow the five stages in order: Intent Understanding -> Requirement Analysis -> Background Research -> Decision Conclusion -> Requirement Deepening.

### 1. Intent Understanding
First analyze the user's shallow needs: what the idea is, who it is for, which problem it solves, and why now. Based on that analysis, optimize your questions, then restate the understood intent in your own words and confirm it with the user. List any unknowns to resolve later.
Question bank: [question-tiers.md](references/question-tiers.md) (Stage 1).

### 2. Requirement Analysis
Analyze the requirements with the 5W2H framework (What, Why, When, Where, Who, How, How much), filling only the gaps left after Stage 1: do not re-ask dimensions that are already clear. Once the needed dimensions are settled, give a short 5W2H recap table (dimension and status: clear / pending / not applicable).
Question bank: [question-tiers.md](references/question-tiers.md) (Stage 2).

### 3. Background Research
Search first, then ask about the user's background. Search for existing solutions, similar products, and similar-feature artifacts without platform restrictions, with GitHub as the primary source, including agents and skills. Collect up to 5 relevant candidates before comparing; stop when 5 are collected or all sources are exhausted. If relevant results are found, present the comparison before asking about the user's time, budget, technical ability, and development environment constraints.
Search is the expected next step of this stage; do not ask the user's permission to search by default. If the user has asked for confirmation before actions, or the platform requires it, ask first. The user can interrupt or skip the search at any time.
Search rules: [search-and-comparison.md](references/search-and-comparison.md). GitHub search script: [github_search.py](scripts/github_search.py).

### 4. Decision Conclusion
Synthesize everything into a suggestive conclusion - build, don't build, use an existing solution, or adapt an existing solution - with clear reasons. Frame it as a recommendation and let the user make the final call.
If the conclusion is not to build, present alternatives and end the workflow; do not proceed to Stage 5.
Decision criteria: [decision-guide.md](references/decision-guide.md).

### 5. Requirement Deepening
Run this stage only after the user decides to build. Ask deep requirements questions: goals and success metrics, MVP features, feature priority, scope boundaries, non-functional requirements, technical preferences or constraints, risks.
After all questions are done, deliver the final summary: the conclusion in one or two sentences, a one-line technical route (what technology or base project to use and how to proceed), a compact constraint summary (goal and success metric, P0 feature list, out-of-scope list, acceptance criteria, key risks), and 2-3 targeted improvement suggestions (see improvement-checklist.md). Then present the delivery choice:
- A. Document only - produce a document now; decide about development later.
- B. Conclusion only - no document.
- C. Document and start building - produce the document, then end the skill workflow; if the user continues into development, treat it as normal agent work outside the skill.
For A or C, confirm the document type and audience using a short menu - requirements, development, process, or other - and expand to the full list only when "other" is chosen (test & acceptance, project plan, decision record, user manual, custom). Save the document as a Markdown (.md) file after confirming the filename and location; if the target file already exists, ask for explicit confirmation before overwriting. Produce a detailed, complete version in the user's language, only after explicit agreement.
Question bank: [question-tiers.md](references/question-tiers.md) (Stage 5). Document templates: [requirement-template.md](references/requirement-template.md). Improvement ideas: [improvement-checklist.md](references/improvement-checklist.md).

## References

- [question-tiers.md](references/question-tiers.md) - question banks and exit rules per stage
- [search-and-comparison.md](references/search-and-comparison.md) - when/how to search, and comparison format
- [decision-guide.md](references/decision-guide.md) - suggestion criteria and output structure
- [improvement-checklist.md](references/improvement-checklist.md) - how-to-do-better ideas by product type
- [requirement-template.md](references/requirement-template.md) - document templates by type (requirements / development / process)
- [github_search.py](scripts/github_search.py) - GitHub repository search via the official REST API

# Decision Guide

Synthesize the interview into a suggestive conclusion by checking the four "don't build" reasons in order. No single check is absolute; require evidence for each one.

## Check Order

1. Covered by an existing solution - if a mature project already covers the core need, recommend use existing or adapt existing; name the best fit and the required delta.
2. Too hard to build - if the user cannot realistically finish it with current time, skill, or tools, recommend don't build, a smaller scope, or use existing.
3. Cost exceeds value - if time, money, or maintenance outweigh the value gained, recommend don't build or a smaller version.
4. Need is not real - if no real user or pain point exists beyond "it would be cool", recommend don't build.

For each check that supports "don't build", cite what the user said or the search evidence and give a concrete alternative.

## Weight Hints

- If an agent will do the development, difficulty and cost still matter but count less than whether an existing solution covers the need; do not ignore feasibility entirely.
- If the purpose is learning or portfolio, existing-solution coverage counts less; learning value and a presentable, finished result count more.
- If the purpose is commercial, real differentiation and cost/benefit dominate.
- Purpose still changes the bar:
   - Learning: build even if alternatives exist, but keep scope small.
   - Commercial: require real differentiation or a clear niche.
   - Portfolio: build something presentable and finished.
   - Personal: judge by time and maintenance burden.

## Verdict Options (Suggestive)

Frame every conclusion as a recommendation; the user makes the final call.

- Recommend build - clear value, feasible, and aligned with purpose.
- Recommend don't build - give concrete reasons and suggest alternatives.
- Recommend use existing - a good project already covers the need; name the top fit.
- Recommend adapt existing - a project is close but needs changes; describe the delta.

## "Don't Build" Reason Catalog

Choose the reasons that match the conversation and support each with evidence:

- The idea already exists in mature form; building adds little.
- Cost/benefit is negative: effort and maintenance exceed value.
- No real user or need identified beyond "it would be cool".
- Overkill: a simpler non-code solution (spreadsheet, existing service) works.
- The user cannot realistically finish it with current time or skill.
- The purpose is better served by using or contributing to an existing project.

For each reason, cite what the user said, then suggest a concrete alternative: an existing project, a simpler version, or a smaller scope.

## Suggested Verdict Output

Output the suggestion in this form:
1. A one-line suggestive verdict ("I suggest ...") plus a short summary.
2. 2-4 evidence-based reasons.
3. A concrete alternative if the suggestion is not to build (existing project, simpler version, smaller scope).
4. Explain technical terms at the user's level: plain-language glosses for beginners, direct jargon for technical users (see SKILL.md > Technical-Level Adaptation).

If the user decides to build, proceed to Stage 5 (Requirement Deepening). At the end of Stage 5, deliver the final summary (conclusion, technical route, constraint summary, improvement suggestions), then present the A/B/C delivery choice (document only / conclusion only / document and start building). For A or C, confirm the document type and audience first, save it as a Markdown file, and produce it only on explicit request. If the conclusion is not to build, present alternatives and end the workflow.

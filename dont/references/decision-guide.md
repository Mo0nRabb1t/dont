# Decision Guide

Synthesize the interview into a suggestive conclusion. Weigh four factors; no single factor is absolute.

## Factors

1. Existing solutions - ideas already covered by mature projects favor don't-build or adapt.
2. Cost/benefit - time, money, and maintenance vs the value gained.
3. Feasibility - the user's skill, available tech, and ability to finish.
4. Purpose - learning, commercial, portfolio, or personal use changes the bar:
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

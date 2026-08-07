# Search & Comparison

Search in Stage 3 (Background Research), before asking about the user's background. Search is the expected next step of this stage; do not ask the user for permission to search by default. If the user has asked for confirmation before actions, or the platform requires it, ask first. The user can interrupt or skip the search at any time.

## Scope & Priority

- No platform restrictions: search GitHub, the general web (Google, Baidu, etc.), product directories, and any other relevant source.
- GitHub is the primary source: repos, topics, awesome lists. Prefer [github_search.py](../scripts/github_search.py) (official REST Search API, sorted by stars) when it can be run; fall back to web/browser search otherwise.
- Include agents and skills: search for existing agents, skills, and similar AI products, not only code projects.
- Collect up to 5 relevant candidates before comparing; do not stop at the first hit. Stop when 5 relevant candidates are collected or when all sources are exhausted. If nothing relevant is found anywhere, stop and tell the user; do not keep hunting.

"Relevant" means a project, product, agent, or skill that substantially covers the idea's core purpose, not merely similar keywords.

## Example Queries

- GitHub: `python github_search.py "<idea>" --limit 5`, or `<idea> app`, `<idea> open source`, `<idea> agent`, `<idea> skill`, topic pages, `awesome <idea>`
- Web: `<idea> existing solution alternative`, `<idea> similar product`
- Adapt queries to the user's language and product type.

## Presenting Results

When relevant results are found, present a comparison BEFORE asking about the user's background:

| Name | Link | What it is | Pros | Cons | Fit for this idea |

Present the collected set (up to 5 candidates) in a comparison table. Add one line noting which might fit best and why. If results are stale or questionable, say so. Do not ask the user to choose a path from the table - the use / adapt / build judgment belongs to Stage 4 (Decision Conclusion). After the table, proceed directly to the background questions (time, budget, technical ability, environment constraints - see question-tiers.md, Stage 3).

Fit column: keep it factual and dual-dimension - note both how ready-to-use the project is (releases or install packages, maintenance activity, setup difficulty) and how customizable it is (plugins/extensibility, code quality, fork-friendliness). Once the user's technical level is known, Stage 4 re-weights these dimensions in the recommendation: beginners favor ready-to-use projects; technical users favor customization potential.

Adapt the comparison to the user's technical level: for beginners, gloss each technical term in plain language the first time it appears (e.g. "Flutter - a cross-platform app framework"); for technical users, use the terms directly (see SKILL.md > Technical-Level Adaptation).

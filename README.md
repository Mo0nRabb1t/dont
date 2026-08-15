# D.O.N.T

> "Do or Not To" - a skill for agents that helps you decide whether to build a development idea.
> Through staged, multi-turn questioning, it progressively pins down your intent and ends with a suggestive conclusion and implementation guidance.
> One-sentence summary: should I do it? If not, here are the reasons; if yes, here is the way.

English | [中文](./README.CN.md)

## What D.O.N.T Does

When you have a development idea (website, app, frontend, backend, tool, skill, agent, etc.) but are not sure whether it is worth building, how to build it, or what features it needs, D.O.N.T walks you through staged multi-turn questions and delivers a clear conclusion.

## Core Idea

**Should I do it? If not, here are the reasons; if yes, here is the way.**

- Should I: Stage 4 gives a suggestive conclusion (build / don't build / use existing / adapt), and you make the final call.
- If not: it gives reasons and alternatives.
- If yes: it gives the way - requirement deepening, a technical route, a constraint summary, and documents on request.

## Scope

D.O.N.T only supports decision-making and requirement clarification for development ideas. Once a conclusion or document is delivered, the skill's job is done; actual development, implementation, and maintenance are outside its scope.

## Core Mechanism

Five-stage progressive interview:

| Stage | Focus |
| --- | --- |
| 1. Intent Understanding | Analyze shallow needs, refine questions, then restate and confirm |
| 2. Requirement Analysis | Fill only the gaps with 5W2H and output a recap table |
| 3. Background Research | Search and compare existing solutions first (GitHub-first, any platform, incl. agents and skills), then ask about time, budget, skills, environment |
| 4. Decision Conclusion | Give a suggestive conclusion with reasons; you make the final call |
| 5. Requirement Deepening | Deepen requirements only after you decide to build; deliver a final summary (conclusion, technical route, constraint summary, improvements) and offer A/B/C delivery options |

Highlights:

- **Adaptive questioning**: question count adjusts to the answers (preferring more, detailed questions); the user can say "just decide" to skip ahead at any time.
- **Fast answers**: questions are numbered and options lettered, so you can reply with shorthand like `1A 2B 3C` (or `A1 B2 C3`) to answer several questions at once.
- **Existing-solution search**: GitHub-first with no platform restrictions (including agents and skills); collects up to 5 candidates before comparing, then asks about your background, and gives up only if nothing relevant is found. It searches directly by default, but asks first if you have asked for confirmation before actions.
- **Output**: starts with a suggestive verdict and reasons; after you confirm you want to build, it deepens the requirements and delivers a final summary with a technical route, constraint summary, and improvement suggestions, then offers A/B/C (A. document only / B. conclusion only / C. document and start building); when a document is chosen, it confirms the type with a short menu (requirements / development / process / other) and saves it as a Markdown file.
- **Language adaptive**: follows the user's input language, defaulting to English.
- **Technical-level adaptive**: the skill confirms your technical level early and explains in plain language for beginners or uses professional terms directly for technical users.
- **User preference first**: your instructions and preferences take priority over the skill's defaults (e.g. it asks first if you have asked for confirmation before actions).

## Installation

D.O.N.T follows the standard SKILL.md spec and can be used by multiple agents. Run the commands below from the repository root, and replace `<skills-dir>` with the skills directory of the agent you use (a common layout is `%USERPROFILE%\.codex\skills` on Windows, or `~/.codex/skills` on macOS/Linux).

Windows - copy:

```powershell
New-Item -ItemType Directory -Path "<skills-dir>" -Force | Out-Null
Copy-Item -Recurse .\dont "<skills-dir>"
```

Windows - directory junction (keeps the source in the repo, so it stays in sync with git):

```powershell
New-Item -ItemType Directory -Path "<skills-dir>" -Force | Out-Null
New-Item -ItemType Junction -Path "<skills-dir>\dont" -Target (Join-Path (Get-Location) 'dont')
```

macOS / Linux:

```bash
mkdir -p <skills-dir>
cp -r ./dont <skills-dir>/
```

Verify the install: `Test-Path "<skills-dir>\dont\SKILL.md"` on Windows, or `ls <skills-dir>/dont/SKILL.md` on macOS/Linux.

## Usage

Start a new conversation and say:

- "I want to build an AI pet-raising app"
- "Should I build this idea?"
- "Help me clarify the requirements for X"

Some agents support the `$skill` syntax; you can invoke it explicitly with `$dont`. For agents that do not, just describe the idea and the skill will trigger.

## Directory Structure

```
dont/
├── SKILL.md                      # Core workflow (five stages)
├── agents/
│   └── openai.yaml               # UI metadata
├── scripts/
│   └── github_search.py          # GitHub repository search helper
└── references/
    ├── question-tiers.md         # Question banks and exit rules per stage
    ├── search-and-comparison.md  # Search rules and comparison format
    ├── decision-guide.md         # Decision criteria and output structure
    ├── improvement-checklist.md  # How-to-do-better checklist
    └── requirement-template.md   # Document templates by type (requirements / development / process / etc.), user consent required
```

## License

[MIT](./LICENSE)

## Feedback

Found a problem or have an idea for improvement? Open an Issue or submit a PR.

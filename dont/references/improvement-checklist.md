# Improvement Checklist

Use these to answer "how to make it better". Pick the relevant sections; do not dump everything.

## General (all products)

- UX: spend most effort on the core flow; make the happy path obvious and fast.
- Performance: measure before optimizing; fix the top 1-2 bottlenecks.
- Security & privacy: auth, secrets, data validation, least privilege.
- Maintainability: small modules, docs for non-obvious decisions, CI.
- Feedback loop: ship a small version, get real feedback, iterate.

## Website

- SEO and meta tags, accessibility, responsive layout, loading states, analytics.

## App (mobile/desktop)

- Onboarding, offline behavior, permission rationale, store basics, crash reporting.

## Frontend

- Component structure, state management, error/empty/loading states, i18n, design tokens.

## Backend/API

- Consistent versioned API design, rate limiting, logging, monitoring, backups, migrations.

## Skill/Agent

- Clear triggering description, minimal context footprint, progressive disclosure, deterministic scripts where possible, validate with real tasks.

## Tool/CLI

- Good defaults, help text, exit codes, config over flags, tests.

## Growth & Validation

- Define one success metric; identify the smallest audience to validate with; plan the first three feedback sessions.

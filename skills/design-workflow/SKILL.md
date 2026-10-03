---
name: design-workflow
description: Use when designing or redesigning interfaces, auditing UX, exploring layouts and visual directions, building interactive prototypes, or documenting a design system.
---

# Design Workflow

Choose the mode first. R = redesign an existing interface; N = add screens within an established product style; G = establish a new product and visual direction.

This skill orchestrates the seven sibling skills below. Use the client's skill mechanism when available; otherwise read the sibling file at ../<skill-name>/SKILL.md relative to this skill directory. Resolve paths from the installed skill, never from a hardcoded user directory. No memory provider, external design service, publishing account, or server is required.

## Shared rules

- Separate observed facts, owner decisions, assumptions, and illustrative demo values. Never present invented product rules or data as facts.
- Read the approved product design canon before choosing aesthetics. It takes precedence over generic design recommendations. Without a canon, offer choices.
- Before a final prototype, present 3–4 layout concepts; for a new style, present three visual directions with the same content so they are comparable.
- Discovery describes user-visible fields, actions, permissions and states. It does not create an API/database specification.
- Keep user data out of examples, screenshots and public artifacts. Local HTML is the default; remote delivery requires an explicit request and configured tool.
- Record decisions in the user's chosen project document when appropriate. If the user requests persistent memory, use their available tool with their consent; its absence never blocks any phase.
- Do not mix personal settings, operational queues, administrative controls and infrastructure merely because they fit one page.

## R — Redesign

1. Read references/audit.md. Before live recon, follow agent-browser’s runtime prerequisite check: the skill does not install its CLI/browser. Recon the actual interface through agent-browser when browser access exists. Use an isolated session, desktop and mobile widths, screenshots and fresh DOM snapshots after navigation. Do not reuse a personal browser profile implicitly. If access is unavailable, use supplied screenshots/source and report coverage gaps.
2. Inventory every observed control: role, content, dependency, permission and state. Check hidden sections and duplicate concepts. If a snapshot has encoding damage, scripts/decode_mojibake.py is a conditional repair tool: explicit input/output, preserve the original, inspect the result before trusting it.
3. Use ux-heuristics for an evidence-backed scorecard and ux-principles for additional root-cause explanations. Every finding needs location, evidence, severity and a concrete fix. Use ui-ux-pro-max conditionally for a specific visual, accessibility or implementation question; verify recommendation fit.
4. Use frontend-design and web-artifacts to show 3–4 layout concepts with real content. The user chooses the structure.
5. Build an interactive prototype in the existing approved style. If no style is approved, enter G's visual-direction step first. Cover navigation, primary actions, empty/loading/error states and mobile layout. Distinguish simulated actions from real integration.
6. Iterate on feedback, then document accepted changes with design-system-docs where they affect the canon.

## N — New screens in an existing product

1. Read references/discovery.md and the current design canon. Identify the goal, user journey, available fields, actual rules, permissions, dependencies and all states from code, project documents and the owner.
2. Apply ux-heuristics and ux-principles prospectively. Query ui-ux-pro-max when a concrete design or detected-stack question needs it.
3. Present 3–4 layout concepts using frontend-design and web-artifacts while preserving the approved style.
4. Prototype the selected option and iterate. Use design-system-docs to record accepted new component rules; do not silently replace the established canon.

## G — New product or visual direction

1. Run discovery from references/discovery.md. Identify users, jobs, content and page relationships before styling.
2. Use frontend-design to create three distinct visual directions with the same representative content; deliver them through web-artifacts. ui-ux-pro-max --design-system can supply recommendations, never an automatically accepted canon.
3. The user selects a direction. design-system-docs records the selected HTML/CSS/screenshots into DESIGN.md, clearly marking inferred values and unimplemented states. references/canon-clean-saas.md is one optional style example, never the default.
4. Design 2–3 representative screens using N, then extract the demonstrated components into the project's actual implementation stack.
5. Report decisions, validation and remaining gaps. Do not claim a complete design system based only on untested tokens.

## Dependency map

| Skill | Role | Status |
|---|---|---|
| agent-browser | live recon and browser verification | conditional on access and task |
| ux-heuristics | structured audit / prospective checks | required for substantive UX work |
| ux-principles | laws and principles explaining structure | required for substantive UX work |
| ui-ux-pro-max | searchable local guidance and stack advice | conditional on design question |
| frontend-design | visual direction and composition | required when producing visuals |
| web-artifacts | concepts, interactive HTML and delivery | required when producing HTML artifacts |
| design-system-docs | document the chosen canon | required in G after selection; conditional in R/N |

## Delivery check

Confirm the artifact opens without a server in local mode, primary controls work, mobile content fits, focus is visible and the approved direction is respected. List missing evidence and simulated behavior. Remote publication is never an automatic completion step.

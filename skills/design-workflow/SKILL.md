---
name: design-workflow
description: Use when designing or redesigning interfaces, auditing UX, exploring layouts and visual directions, building interactive prototypes or UI Kits, or resolving component drift between a design system and screens.
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

## UI Kit first — executable SSOT

Before detailed section prototypes in **any mode**, read references/ui-kit-ssot.md completely. Reuse the approved project's implemented library when it exists; otherwise build a minimal UI Kit from inspected references, the owner's description and project needs. Share reference links and distinguish borrowed principles from proposed adaptations.

The UI Kit is a live catalogue of the **same component implementations** used by the sections, not separately drawn examples. Shared tokens, responsive grid, spacing, forms, icons, states and interaction rules belong there. DESIGN.md documents this source; it does not replace it.

Order: discovery → comparable low-fidelity concepts / visual directions → owner selection → implemented UI Kit and owner approval (or confirmed existing approved kit) → one section at a time → verification and feedback. Rough wireframes may precede the kit; polished section components may not. If a chosen concept introduces an element, implement and demonstrate it in the kit **before** its first section use, then reuse it elsewhere. Never defer extraction until 2–3 finished screens.

Under a deadline, deliver fewer components/screens and report gaps. Matching screenshots, shared token names, copying markup/CSS, or a promise to unify later do not establish SSOT. Preserve accepted UX while replacing drifted component implementations in the authorized prototype scope; production migration remains a separate decision.

## R — Redesign

1. Read references/audit.md. Before live recon, follow agent-browser’s runtime prerequisite check: the skill does not install its CLI/browser. Recon the actual interface through agent-browser when browser access exists. Use an isolated session, desktop and mobile widths, screenshots and fresh DOM snapshots after navigation. Do not reuse a personal browser profile implicitly. If access is unavailable, use supplied screenshots/source and report coverage gaps.
2. Inventory every observed control: role, content, dependency, permission and state. Check hidden sections and duplicate concepts. If a snapshot has encoding damage, scripts/decode_mojibake.py is a conditional repair tool: explicit input/output, preserve the original, inspect the result before trusting it.
3. Use ux-heuristics for an evidence-backed scorecard and ux-principles for additional root-cause explanations. Every finding needs location, evidence, severity and a concrete fix. Use ui-ux-pro-max conditionally for a specific visual, accessibility or implementation question; verify recommendation fit.
4. Use frontend-design and web-artifacts to show 3–4 layout concepts with real content. The user chooses the structure.
5. Establish or confirm the approved executable UI Kit first. If no style is approved, enter G's visual-direction step first. Build the selected section using the kit, covering navigation, primary actions, empty/loading/error states and mobile layout. Distinguish simulated actions from real integration.
6. Iterate on feedback, then document accepted changes with design-system-docs where they affect the canon.

## N — New screens in an existing product

1. Read references/discovery.md and the current design canon. Identify the goal, user journey, available fields, actual rules, permissions, dependencies and all states from code, project documents and the owner.
2. Apply ux-heuristics and ux-principles prospectively. Query ui-ux-pro-max when a concrete design or detected-stack question needs it.
3. Present 3–4 layout concepts using frontend-design and web-artifacts while preserving the approved style.
4. Confirm the implemented UI Kit and fill required gaps there before prototyping the selected section. Reuse its components; iterate one section at a time and verify existing consumers after kit changes. Use design-system-docs to record accepted rules and source mappings; do not silently replace the established canon.

## G — New product or visual direction

1. Run discovery from references/discovery.md. Identify users, jobs, content and page relationships before styling.
2. Use frontend-design to create three distinct visual directions with the same representative content; deliver them through web-artifacts. ui-ux-pro-max --design-system can supply recommendations, never an automatically accepted canon.
3. The user selects a direction. Implement and demonstrate its minimal UI Kit, including grid/spacing, forms and interaction states, then obtain approval before detailed sections. design-system-docs records source mappings and accepted rules into DESIGN.md, clearly marking inferred values and missing states. references/canon-clean-saas.md is one optional style example, never the default.
4. Prototype sections iteratively using N and the approved kit. Extend the kit first for new components; never create section-local copies to extract later. For multiple directions, share behavioral contracts while deliberately varying approved component visuals and page composition, not just palettes.
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
| design-system-docs | document canon and executable source mappings | required when establishing or extending a kit; reuse existing docs otherwise |

## Delivery check

Confirm the artifact opens without a server in local mode, primary controls work, mobile content fits, focus is visible and the approved direction is respected. Verify UI Kit and sections consume the same source, and demonstrate one shared-component change reaching both without page-specific edits. Check spacing/grid, form states and reduced motion using references/ui-kit-ssot.md. List missing evidence and simulated behavior. Remote publication is never an automatic completion step.

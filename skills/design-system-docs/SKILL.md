---
name: design-system-docs
description: Use when extracting or updating a DESIGN.md design canon from selected HTML/CSS, UI source, screenshots, or an approved prototype.
---

# Design System Docs

Document the selected design into DESIGN.md. No design service, project ID, remote account or specific framework is required.

Use templates/DESIGN.md as a scaffold and examples/DESIGN.md as an explicitly fictional illustration. Read an existing DESIGN.md before updating it; preserve accepted choices and resolve actual contradictions with the user.

## Inputs and evidence

Record the inspected source paths and, where available, revision/hash, viewport and theme. HTML/CSS yields exact implemented values; screenshots yield estimates. Label every inferred value, owner decision and proposal. If only one theme or component state exists, record the gap instead of inventing its counterpart.

Never alter the selected prototype merely to fit the documentation. Write to the user's chosen project location; DESIGN.md in the project root is a reasonable default only when no location is specified.

## Workflow

1. Identify product scope, chosen direction, source coverage and existing canon.
2. Describe atmosphere and visual hierarchy in concrete terms.
3. Extract semantic color tokens: light/dark values where implemented, intended role, evidence. Record contrast measurements only if actually measured; otherwise mark contrast verification pending.
4. Extract font families/fallbacks, weights, type scale, line heights, spacing, layout/grid/breakpoints, radii, borders, shadows and icon conventions. Do not fabricate missing tokens.
5. Document component anatomy and implemented states: default, hover, focus, selected, disabled, loading, empty and error as applicable. Mark absent states as gaps.
6. Document interactions, navigation, validation, destructive actions/undo, keyboard/focus, touch targets, theme behavior and reduced-motion rules.
7. Separate observed implementation, accepted decisions, assumptions, proposals and unresolved questions. Add a short change log and verification coverage.
8. Return the actual document path and relevant gaps.

frontend-design chooses/explores visual direction; ui-ux-pro-max gives recommendations; this skill records the chosen result. Neither recommendation becomes an accepted rule without evidence or an owner decision.

# UI Kit: executable single source of truth

## Establish the source before sections

1. Inspect the existing library, DESIGN.md, source, tests, approved screens and project constraints. Keep an approved kit; fill gaps rather than replacing it with a new library.
2. If no implemented kit exists, derive a minimal one from references, an owner description, or the product's needs. Provide reference links and explain concrete choices. A reference is not blanket permission to copy its layout or brand.
3. Choose the project's actual stack or a lightweight prototype stack. Reuse suitable accessible primitives; no forced framework, CSS utility library or component package. Define one shared source for tokens, layout primitives, components and behavior. Map each catalogue example and section consumer to it in DESIGN.md.
4. Demonstrate the minimum components needed by the next section, all applicable states and responsive behavior. Obtain owner approval unless this implemented kit is already approved. An incomplete kit can be approved for a clearly stated slice; do not claim completeness.
5. Build one section, validate, gather feedback. New element? Extend the kit first, demonstrate its states, then compose it into the section. Update the catalogue and docs in the same change and check previous consumers. Section-specific data/content and composition remain in sections; reusable anatomy, styling and behavior do not.

The catalogue must call the same implementations as sections. Tokens alone and screenshots are not a component library. A standalone HTML delivery can bundle shared source into each output at build time; generated duplication is acceptable only when one source drives the outputs and is verified. If file:// forbids module imports, use shared classic scripts or a build step, not independently edited copies. Do not add a server requirement to otherwise offline artifacts.

Example source ownership (adapt names to the stack):

```text
ui/tokens.css         semantic tokens, spacing, density, motion
ui/layout.css         shell, container, grid, stack, toolbar
ui/components.js      field, button, combobox, table, feedback
ui-kit.html           calls ui/components.js
sections/*.html       calls ui/components.js with section data
DESIGN.md             source paths, contracts, decisions, gaps
```

## Grid and spacing are part of the kit

- Define a named spacing scale and semantic usages: page gutters, section gaps, toolbar gaps, field spacing, cell padding, density. Choose values for this product; do not sprinkle unrelated magic numbers.
- Specify shell/sidebar, content widths, columns, gutters, breakpoints and responsive rules. Reusable container/grid/stack primitives implement these rules.
- Check long labels, narrow available content with expanded sidebar, wrapping filters and custom dates. Reset native element defaults where needed. Avoid nested full-page surfaces without a semantic reason; a card inside a canvas must have intentional padding and hierarchy.
- Dense data may differ from form density, but both use documented tokens. Alignment, icon sizing/centering and minimum touch targets are component rules, not per-page patches.

## Forms and feedback

Demonstrate typography, colors, links, buttons, fields, labels/help/errors, checkbox/radio/toggle, choice controls, navigation, tables and feedback as needed by the next section. Include default, hover, focus-visible, active/selected, disabled, loading, empty and error states where applicable. Keep labels and selected values stable during loading; prevent duplicate submits. Include button loaders, progress and skeletons for relevant workflows; never show indefinite loading without an error/retry path.

Use a usable **combobox** for project choice fields needing search, richer options or remote data, not a default browser select dressed per page. Document single/multiple choice, clear behavior, optional icons/descriptions and grouping. Support local filtering or an API loader as required, keyboard arrows/Enter/Escape, visible focus, accessible names/roles and preserved selection. Remote search needs debounce/cancellation or stale-response protection, loading, empty, error/retry and paging when appropriate. Simulated API data must be labelled. Small bounded choices can use an approved kit-native select or segmented control when appropriate; do not impose a combobox on every choice.

Document table sorting contracts (local vs API), resize/persistence, overflow and row states when the product requires them. Notifications, including toasts when selected, share severity, dismiss/retry and accessible live-region rules. Blocking errors stay visible near the affected action; a toast is not their only explanation.

## Minimal motion

Define shared duration/easing tokens and restrained hover, focus and action feedback for buttons, forms, toggles, menus and other interactive elements. Animate color/opacity/transform without layout jumps; focus-visible remains immediate. A toggle thumb transition, subtle pressed state or optional ripple is enough. Respect prefers-reduced-motion: remove nonessential movement/ripples and retain static state changes and readable loading status. Animation must not hide failure, change state semantics or delay actions.

## Acceptance: prove reuse, not resemblance

- Record component → canonical source → catalogue demo → section consumers. Inspect imports/shared renderer calls or build dependencies; screenshots alone cannot prove this boundary.
- Change one shared component in a controlled test and verify both a kit example and at least one section consumer update without consumer-specific edits. Test rendering and interaction, not merely source strings. Restore a temporary visual probe after verification.
- Exercise search/select/clear, keyboard focus, loading/error/retry, button action and reduced motion. Test component changes against already prototyped sections, at desktop, narrow content and mobile widths, and every promised theme/direction.
- Keep navigation between kit and sections. Share implementations while allowing different page compositions; changing palette alone does not deliver a different UX.
- Report untested states, disconnected examples, simulated APIs and pending migrations honestly. Do not call an implementation SSOT while separate copies remain.

| Temptation | Required response |
|---|---|
| Three screens are urgent; extract afterwards | Deliver a smaller shared slice first; report remaining screens |
| Existing showcase looks identical | Check executable ownership and consumer calls |
| New control only occurs on this page | Add the reusable control to the kit before the page uses it |
| Shared tokens are enough | Share component anatomy, behavior and layout primitives too |
| Legacy pages already took days | Preserve accepted UX and migrate components in scope; do not copy the drift |

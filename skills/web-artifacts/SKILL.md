---
name: web-artifacts
description: Use when creating interactive HTML prototypes, layout comparisons, visual reports, diagrams or presentations, with local standalone delivery and optional explicitly requested remote hosting.
---

# Web Artifacts

Create reviewable HTML artifacts. Local mode works without a server or publishing service.

## Choose design and delivery

Read ../frontend-design/SKILL.md for new visual work, respecting any approved project canon. Read references/mobile-first.md for layout requirements. references/synthwave-theme.md is an optional style example only when explicitly selected.

Default: one self-contained HTML file. Use inline CSS, classic inline JavaScript, embedded data, inline SVG and data URLs for embedded assets. No runtime CDN, module imports, fetch calls, external fonts, local sibling asset requests or service workers. Keep interactive state in memory; file URL storage behavior is not portable. Export/import JSON explicitly when persistence is needed.

Resolve optional project .design-workflow.json from the project root. If absent, use local mode and artifacts/design as the suggested output folder. This file is a convention interpreted by the agent, not a native client setting or an automatically executed adapter. Output paths are relative to the project; confirm any destination outside it. Never store credentials in this file. See ../../docs/configuration.md.

## Build and validate

1. Establish content, purpose, approved visual direction and simulated behavior. Mark demo data. A concept comparison keeps content constant across alternatives.
2. Build semantic mobile-first HTML with visible labels, keyboard focus, sufficient touch targets, responsive tables/diagrams and reduced-motion support.
3. Prefer plain HTML/CSS/JS. Use references/cdn.md only for optional library guidance; its network examples do not meet the default standalone contract. Pre-render diagrams into inline SVG or embed a verified licensed bundle when a library is actually needed.
4. Inspect source and test desktop/mobile, navigation, principal controls, empty/error states and horizontal overflow. If no browser is available, state the missing runtime check.
5. Save with the bundled helper, resolving its absolute path from this installed skill:

   python "<skill-directory>/scripts/save_local.py" --input "<draft.html>" --output "<project>/artifacts/design/prototype.html"

   python3 or py -3 are alternatives. --overwrite explicitly replaces an existing destination; --open explicitly opens the file URL. Without these flags it neither overwrites nor launches a browser. The helper rejects common runtime network/resource patterns; it is a conservative contract check, not a sandbox for arbitrary JavaScript.
6. Return the actual file path and file:// URL. Explain simulated integrations and checks performed. templates/bare.html is a minimal starting point; templates/interactive-demo.html demonstrates local interactions.

## Optional remote delivery

Remote hosting is conditional on the user's explicit request and their available configured tool. Save a local review copy first. Read references/remote-delivery.md, inspect the actual connector schema, verify access with a harmless read, and follow that connector's permission rules. Configuration alone does not authorize an upload.

Do not guess tool names, endpoints or supported update operations. If access is missing or upload fails, retain the local artifact and report the blocker. Never claim remote success without a confirming tool response.

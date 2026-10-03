# Licenses, provenance and modifications

The owner-approved MIT license in LICENSE covers the original local workflow/artifact materials and newly authored integration. Bundled third-party components retain their individual MIT/Apache-2.0 licenses; the root MIT license does not replace upstream licenses.

| Component and files | Established provenance | License and evidence |
|---|---|---|
| ux-heuristics: SKILL.md, heuristics.md, README.md | [sanmidable/ux-heuristics](https://github.com/sanmidable/ux-heuristics), named by the original README | MIT; exact local LICENSE retained |
| ux-principles: SKILL.md, laws.md, principles.md, README.md | [sanmidable/ux-principles](https://github.com/sanmidable/ux-principles), named by the original README | MIT; exact local LICENSE retained |
| ui-ux-pro-max: all 73 original skill/data/reference/script/test/fixture files | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/09170eec67eefd46a7ae85de61b40c194020f997); all 73 originals match Git blobs after CRLF→LF normalization | [MIT at that revision](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/09170eec67eefd46a7ae85de61b40c194020f997/LICENSE), Copyright (c) 2024 Next Level Builder; full license included |
| agent-browser: original SKILL.md, 6 references, 3 templates | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/4d8097a56fe9990eb2e5cecb6d167eb6897eda06); all 10 originals match this historical revision after CRLF→LF normalization | [Apache-2.0 at that revision](https://github.com/vercel-labs/agent-browser/blob/4d8097a56fe9990eb2e5cecb6d167eb6897eda06/LICENSE), Copyright 2025 Vercel Inc.; full license included |
| frontend-design: SKILL.md | Anthropic [official frontend-design plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design/skills/frontend-design); selected current installed official copy | LICENSE.txt retained; Apache-2.0 |
| design-system-docs: adapted workflow/README/example plus new template | local design-md README identified [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills); portable adaptation rewritten around selected HTML/CSS/screenshots | [upstream Apache-2.0](https://github.com/google-labs-code/stitch-skills/blob/main/LICENSE) retained as LICENSE; this is an adaptation, not an exact upstream snapshot |
| design-workflow: SKILL.md, 3 references, decode script | user-provided local custom workflow; portable copy and neutral examples | MIT under root LICENSE |
| web-artifacts: original workflow, references, bare scaffold; new local saver/demo/remote guidance | user-provided local artifact workflow and this adaptation | MIT under root LICENSE |
| root scripts/docs/manifests | authored for this portable adaptation | MIT under root LICENSE |

Modification notice (2026-10-03): vendor-neutral R/N/G orchestration; selected design → DESIGN.md without a design service; local single-file HTML fallback; installed-path search commands; anonymized examples; optional canon/theme renamed; canon precedence; clarified screenshot audit fallback and finding caps; portable verification and client manifests. Unchanged upstream copyright/attribution remains intact.

Evidence: docs/evidence/source-provenance.json lists verified UI/browser Git paths and commits. SOURCE_MANIFEST.json records all 107 original resource hashes without personal absolute paths; FILE_MANIFEST.json records the adapted distribution. Global source files were not changed.

UI catalog provenance is preserved in data/data-provenance.json, google-font-licenses.json and phosphor-icons-upstream.json. Font author names are attribution, not owner private data. This package contains metadata, not automatically downloaded font or icon binaries. Any future embedded font/library must carry its own exact license and notices. MIT for catalog software does not relicense external assets merely referenced by it.

No package secrets, personal project domains, user-machine paths or private project identifiers are included. Publisher metadata uses only the confirmed public GitHub handle.

# Portable design workflow — approved design and implementation plan

Goal: prepare and verify a portable eight-skill package; publish the reviewed state in the owner-authorized public repository. Do not install globally.

Approved scope: design-workflow, agent-browser, ux-heuristics, ux-principles,
ui-ux-pro-max, design-system-docs, web-artifacts, frontend-design.
No specific memory provider or API-design skill is required. Global source files stay untouched.

Architecture: portable skills/ trees plus small client-specific manifests where documented.
Prototype delivery defaults to a self-contained HTML file. Remote delivery is an explicit,
optional adapter selected by the user; no automatic upload or bundled remote endpoint.
The chosen product canon takes priority over aesthetic exploration on later screens.

Implementation:
1. Copy complete source trees excluding VCS/cache; record input hashes and license gaps.
2. Rewrite workflow/documentation/artifact instructions; anonymize all dependent references.
3. Test a local writer before implementation: save file URL, reject runtime networking,
   preserve existing output, permit ordinary source hyperlinks.
4. Add provider-neutral config and a serverless sample; adapt script paths to skill location.
5. Check package links, source preservation, clean copied layout, data search and browser behavior.
6. Document only verified client commands; transfer final files to the authorized target.

Validation evidence is kept in docs/validation.md and FILE_MANIFEST.json.
Upstream MIT/Apache licenses are preserved and source provenance verified. Owner-approved MIT covers original owner materials and integration; third-party licenses remain separate. Native runtime loading and upstream-only maintenance tooling remain verification gaps, explicitly documented.

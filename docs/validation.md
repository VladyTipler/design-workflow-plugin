# Проверки и оставшиеся ограничения

## v0.2.0 — UI Kit SSOT

- PASS: 6 executable package/unit tests, including runtime-state exclusion and real hash-mismatch detection; 137 portable UI regressions.
- PASS: skill frontmatter validator; package resources, relative links, anonymization and regenerated fingerprints.
- Consumer-agent baseline reproduced screen-first extraction; fresh agents after changes enforce kit-first ownership and reuse an existing approved library. Follow-up G scenario confirmed the stale discovery rule was removed. Evidence and reusable scenarios: [ui-kit-workflow-evaluation.md](evidence/ui-kit-workflow-evaluation.md).
- New verification covers workflow behavior, not implementation of an application UI Kit. No new application/API or production integration is claimed.
- Native Codex installation is a release action, verified separately through CLI status and cached source hashes. Existing standalone local skills are not silently overwritten; use the plugin-qualified skill in a new session. Historical client/browser results below remain scoped to v0.1.0.

Фактические результаты 2026-10-03:
- PASS: 8 навыков, наличие всех 107 исходных ресурсов, относительные Markdown/resource links, manifests, обезличивание и SHA256 текущего манифеста.
- PASS: 4 unit tests HTML-сохранителя, включая SVG resources; 137 portable UI tests.
- PASS: validate_data.py — 12 domain файлов, 22 stack файла и ui-reasoning.csv.
- PASS: 15 Chromium browser checks: offline file://, desktop 1440×1000, mobile 390×844, add/filter/complete/undo, empty/validation, dark theme, keyboard focus, кнопки ≥44px, отсутствие overflow/HTTP runtime resources/page errors. См. docs/evidence/browser-results.json (относительно корня пакета).
- PASS: screenshots desktop.png/mobile.png просмотрены.
- PASS: isolated complete copy with spaces and unrelated cwd — package, unit/UI/catalog/search/save checks; no global installation.
- PASS: Claude Code 2.1.198 strict plugin and marketplace validation, no warnings.
- PASS: 107 original source fingerprints unchanged; targeted anonymization and common secret-token scans found no matches.
- Source verification: UI 73/73 and agent-browser 10/10 originals match official Git blobs after line-ending normalization; frontend LICENSE matches official upstream.

Область проверки: восемь SKILL.md, вложенные ресурсы и manifest paths, обезличивание, локальный HTML-сохранитель, runtime/catalog тесты UI, распаковка в изолированный каталог с пробелами, браузерное открытие file://.

Четыре исходных maintenance-набора сохранены, но не запускаются portable runner:
- test_catalog_refresh.py: отсутствуют upstream scripts/refresh-google-fonts.py и refresh-icon-catalog.py.
- test_catalog_summary_line_endings.py: отсутствует scripts/generate-catalog-summary.py.
- test_relevance_evaluator.py: отсутствует scripts/evaluate-relevance.py.
- test_skill_script_paths.py: исходный тест предполагает два upstream дерева .claude/skills и cli/assets/skills и generate-catalog-summary.py. Переносимые paths проверяются отдельным scripts/verify_package.py.

Это не успешный запуск полного upstream suite. Необходимые runtime modules/data сохранены; upstream maintenance repository не реконструировался по догадкам.

Native загрузка/установка в Codex, Claude Code и ZCode не выполнялась. Документация и локальный validator подтверждают формат только в пределах указанных результатов. Проверка file:// не подтверждает другие проекты, авторизацию или production-интеграции.

Upstream licenses установлены и сохранены. MIT для авторских частей одобрена владельцем; bundled third-party MIT/Apache-2.0 notices сохранены. Глобальная установка не выполнялась; native end-to-end остаётся непроверенным. CI не настроен; проверки выполнены локально.

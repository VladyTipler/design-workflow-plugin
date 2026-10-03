# Карта зависимостей

    design-workflow
    ├── agent-browser — условно: live-recon / runtime browser checks
    ├── ux-heuristics — аудит / проектные UX-проверки
    ├── ux-principles — объяснение причин и UX-паттерны
    ├── ui-ux-pro-max — условно: конкретный вопрос / стек / visual guidance
    ├── frontend-design — создание визуального решения
    ├── web-artifacts — создание HTML
    │   └── frontend-design — направление, с приоритетом канона
    └── design-system-docs — G после выбора; R/N при изменении канона

design-workflow: references/audit.md, discovery.md, canon-clean-saas.md; условный scripts/decode_mojibake.py.
agent-browser: все 6 references и 3 shell templates; CLI/browser внешние, условные.
ux-heuristics: heuristics.md, README.md, LICENSE.
ux-principles: laws.md, principles.md, README.md, LICENSE.
ui-ux-pro-max: 39 data-файлов (в том числе 22 stack CSV), 2 references, 5 scripts, 13 tests, 13 fixtures и README. search.py → core.py, design_system.py, reasoning_contract.py → data; validate_data.py — обслуживание данных.
frontend-design: SKILL.md, LICENSE.txt.
web-artifacts: mobile-first.md, cdn.md, synthwave-theme.md, remote-delivery.md; bare.html и interactive-demo.html; save_local.py.
design-system-docs: SKILL.md, README.md, templates/DESIGN.md, examples/DESIGN.md.

Внешние ссылки каталога UI — атрибуция/источники рекомендаций; они не являются runtime-загрузками. Ссылки на Python/браузер/лицензии — условные инструменты и provenance, а не дополнительные bundled skills.

Файлы исходного комплекта сохранены в SOURCE_MANIFEST.json с исходными SHA256; текущий полный набор и SHA256 — FILE_MANIFEST.json. Опциональный канон и тема переименованы и обезличены. Нерешённые maintenance-ссылки и лицензии перечислены в validation и THIRD_PARTY_NOTICES.

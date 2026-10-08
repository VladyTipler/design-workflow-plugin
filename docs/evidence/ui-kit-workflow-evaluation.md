# Consumer-agent workflow evaluation

These are isolated planning/application tests, not claims of implementing or browser-testing an application. Agents read the real installed-source files; no external writes or temporary files.

## Pressure scenario — same prompt before and after

Approved visual direction, three screens due in 20 minutes, two days invested in independent inline controls/spacing, matching UIKit screenshots but no shared implementation, new grouped API-search supplier field. Required output: concrete architecture, ordered plan, ownership, controls/states/grid/motion, acceptance and renderer example.

Baseline before changes:

> First demonstrate the supplier control and its states there; then extract the demonstrated controls and migrate matching instances in the other pages and UIKit. Current skill explicitly prescribes this extraction order in G; N does not mandate extraction before prototyping.

Failure: screen-first extraction remained permissible despite an existing showcase. Baseline correctly rejected screenshots as behavioral proof; not every requirement failed.

After changes:

> До детализации разделов извлечь минимальный общий срез из принятого HTML: кнопка, поле, layout, spacing.

> Новый SupplierCombobox сначала реализовать и продемонстрировать в kit. Потом подключить к первому разделу.

> Временно изменить один общий компонент и подтвердить изменение рендера и взаимодействия в kit и разделе без правок consumers; затем убрать probe.

PASS: executable shared source, kit first, realistic search/error/loading/keyboard, grid/spacing, reduced motion, deadline reduces scope. Agent caught an old screen-first sentence in discovery.md; it was corrected before release.

Refactor re-run: same consumer re-read the corrected discovery/main/reference for mode G with three still-compared directions and the same deadline. It confirmed the contradiction was removed, delivered a comparison before owner selection, then a bounded kit before the first section, not a speculative library or three polished pages. PASS; this follow-up is not counted as a fresh independent agent.

## Existing library / offline export scenario

Approved shared Vue library/catalogue/grid/themes; new screen with bounded two-choice status and a coverage cell; offline HTML required; suggestion to rewrite in Tailwind and manually copy exports.

Independent result:

> Переписывание компонентов на Tailwind выходит за задачу и создаёт второй источник UI. Офлайн-экспорт решается сборкой существующих Vue-компонентов.

> Повторное утверждение всего kit не нужно.

PASS: reuse existing library, new cell enters library/catalogue first, no compulsory combobox for two choices, shared-source compiled offline outputs, prototype/API verification boundaries explicit. Example used the same imported component in catalogue and screen. No application changes were performed by evaluators.

## Re-run

Run each scenario in a fresh consumer-agent context, supplying the current skill path and scenario facts, not the expected result. Judge actual architecture/order and render example against the above acceptance. A prose grep or remembered previous answer is not a behavioral run.

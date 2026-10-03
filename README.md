# Design Workflow

Переносимый комплект из восьми навыков: аудит UX, выбор структуры и визуального направления, интерактивный HTML-прототип и документирование выбранного дизайна. Локальный результат — один HTML-файл, открываемый через file:// без сервера и CDN.

Версия 0.1.0. Сторонние лицензии и точное происхождение файлов: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Авторские workflow и обвязка — [MIT](LICENSE); сторонние компоненты сохраняют свои MIT/Apache-2.0 лицензии. MIT не заменяет лицензии сторонних файлов. Установка в пользовательские каталоги при подготовке не выполнялась.

## Состав

| Skill | Назначение |
|---|---|
| design-workflow | режимы R: redesign, N: новые экраны, G: новый продукт |
| agent-browser | условный live-recon и проверка в браузере |
| ux-heuristics | десять эвристик и аудит с доказательствами |
| ux-principles | UX-законы и причины проблем |
| ui-ux-pro-max | локальный поиск рекомендаций, данные, Python-скрипты |
| frontend-design | композиция и визуальные направления |
| web-artifacts | интерактивный standalone HTML, условное удалённое размещение |
| design-system-docs | DESIGN.md из выбранного HTML/CSS/скриншотов |

Никакой внешний сервис дизайна, памяти или публикации не обязателен. Полная карта: [docs/dependencies.md](docs/dependencies.md). Все вложенные references, scripts, templates, data, tests и fixtures сохранены, кроме обезличивания и явно описанных адаптаций.

## Использование

После загрузки попросите: «Используй design-workflow: предложи варианты структуры, затем сделай интерактивный локальный прототип». Сначала выбирается направление; утверждённый канон продукта имеет приоритет.

При отсутствии поддержки плагинов дайте агенту путь к skills/design-workflow/SKILL.md и разрешите чтение соседних skills. Это ручное использование инструкций, а не подтверждение автоматического обнаружения в любом клиенте.

Python 3 нужен только для локальных вспомогательных скриптов. agent-browser и совместимый браузер нужны только для live-recon/runtime-проверки; пакет ничего не устанавливает. .sh-шаблоны agent-browser требуют совместимую оболочку.

## Установка всего плагина

Нативные установки ниже добавляют все восемь skills. Не устанавливайте зависимости по одной. Команды доступны в проверенных CLI Codex 0.156.1 и Claude Code 2.1.198; более старые версии могут отличаться. Подготовка не меняла глобальные настройки клиентов. Проверенные источники и ограничения: [docs/compatibility.md](docs/compatibility.md).

### Codex

    codex plugin marketplace add VladyTipler/design-workflow-plugin
    codex plugin add design-workflow@design-workflow-local
    codex plugin list --marketplace design-workflow-local --json

Откройте новую сессию и проверьте наличие design-workflow в списке skills; попросите использовать этот навык. В desktop поверхности источник может появляться в Plugins Directory; установка/включение зависит от версии клиента.

Обновление Git marketplace:

    codex plugin marketplace upgrade design-workflow-local

Если клиент не обновил установленную копию, переустановите через remove/add. Удаление:

    codex plugin remove design-workflow@design-workflow-local
    codex plugin marketplace remove design-workflow-local

Для локального каталога вместо GitHub shorthand передайте абсолютный путь в marketplace add. Используйте один источник с этим именем. Root plugin.json и skills/ соответствуют Agent Plugins; .codex-plugin/plugin.json — compatibility overlay. Marketplace находится в .agents/plugins/marketplace.json.

### Claude Code

    claude plugin marketplace add VladyTipler/design-workflow-plugin --scope project
    claude plugin install design-workflow@design-workflow-local --scope project
    claude plugin list --json
    claude plugin details design-workflow

В новой сессии вызовите /design-workflow:design-workflow; details должен показывать восемь skills. Вместо project можно явно выбрать local или user scope.

Обновление:

    claude plugin marketplace update design-workflow-local
    claude plugin update design-workflow@design-workflow-local --scope project

Удаление:

    claude plugin uninstall design-workflow@design-workflow-local --scope project

Источник marketplace можно удалить через /plugin → Marketplaces. Для временной загрузки локального каталога без установки:

    claude --plugin-dir "<absolute-plugin-directory>"

Используются .claude-plugin/plugin.json, .claude-plugin/marketplace.json и корневой skills/. Проверка:

    claude plugin validate "<absolute-plugin-directory>" --strict

### ZCode

Откройте workspace → Settings → Plugins → Create → Add marketplace. Укажите VladyTipler/design-workflow-plugin, GitHub URL или абсолютный путь локального каталога. В Personal выберите design-workflow → Install и Enable.

В Settings → Skills → Plugin skills проверьте восемь навыков; в поле ввода откройте / и выберите design-workflow из Skills. Обновление: Marketplace sources → Refresh this marketplace, затем Manage installed → Check for updates. Удаление: Manage installed → детали плагина → Uninstall; Disable временно выключает навыки.

Используются .zcode-plugin/plugin.json и корневой marketplace.json. Нативная загрузка в ZCode ещё не проверялась end-to-end; формат сверён с официальной документацией и реальным zai-org/zcode-plugins.

### Клиенты без нативного plugin loader

    git clone https://github.com/VladyTipler/design-workflow-plugin.git

Дайте агенту путь к skills/design-workflow/SKILL.md в полном клоне и разрешите читать соседние skills и docs. Сохраняйте весь каталог: отдельное копирование только SKILL.md теряет ресурсы. Это manual skill-bundle fallback, не native plugin install и не гарантия автоматического обнаружения.

Обновление клона: git pull --ff-only. Удаление fallback: перестаньте ссылаться на этот каталог; удалять чужие настройки не нужно.

## Зависимости

- Для чтения и выполнения методик: клиент с доступом к Markdown и файлам проекта.
- Python 3: только scripts поиска UI, валидации и сохранения HTML; сторонние Python packages не нужны.
- Отдельная программа agent-browser и Chrome/Chromium: условно, для live-recon и runtime-проверки. Навык из плагина не устанавливает программу или браузер; setup описан ниже.
- Совместимая POSIX оболочка: только если используются .sh-примеры agent-browser.
- Удалённый hosting/tool: только по явному запросу; local HTML работает без него. Пример project config: .design-workflow.example.json.

### agent-browser: отдельная программа

Bundled skill — инструкции, а не исполняемый CLI. Для автоматизации нужны agent-browser в PATH (или подтверждённая локальная установка проекта) и доступный Chrome/Chromium. Для npm-способа нужны Node.js/npm; сверяйте engines выбранной версии: [текущий upstream manifest](https://github.com/vercel-labs/agent-browser/blob/main/package.json) указывает Node.js ≥24. Native daemon не требует отдельной установки Playwright или Rust toolchain.

Проверка CLI и запуска браузера в отдельной сессии:

    agent-browser --version
    agent-browser --help
    agent-browser --session design-workflow-check open about:blank
    agent-browser --session design-workflow-check snapshot
    agent-browser --session design-workflow-check close

Используйте изолированную конфигурацию, без подключения к личному профилю. Отсутствие команды и неудачный запуск браузера — разные причины: версия CLI сама по себе не подтверждает наличие браузера.

Установка **только при соответствующем разрешении пользователя**:

    npm install -g agent-browser
    agent-browser install

Вторая команда скачивает Chrome for Testing. Альтернатива внутри выбранного проекта:

    npm install agent-browser
    npx agent-browser install

После локальной установки запускайте CLI через npm scripts или npx. Не используйте npx как проверку отсутствующей программы: он может скачать пакет.

macOS: вместо npm можно использовать brew install agent-browser, затем agent-browser install. Windows: используйте npm-способ в PowerShell/CMD. Linux: если отсутствуют системные библиотеки браузера, agent-browser install --with-deps устанавливает и их; могут потребоваться повышенные права. --with-deps относится только к Linux.

Если CLI/browser отсутствует или установка не разрешена, сообщите точный пробел и предложите setup либо доступный альтернативный browser tool. Продолжайте создание standalone HTML и анализ предоставленных скриншотов/кода; runtime-проверку пометьте как невыполненную. Этот плагин ничего не устанавливает автоматически.

Источники: [официальная установка](https://agent-browser.dev/installation), [upstream README](https://github.com/vercel-labs/agent-browser#installation).

## Локальная проверка

Из корня пакета:

    python -B scripts/verify_package.py
    python -B -m unittest discover -s tests -v
    python -B scripts/run_ui_tests.py
    python -B skills/ui-ux-pro-max/scripts/validate_data.py
    python -B skills/web-artifacts/scripts/save_local.py --input skills/web-artifacts/templates/interactive-demo.html --output artifacts/design/demo.html

Последняя команда возвращает file:// URL; --open открывает браузер, --overwrite разрешает замену. Скрипт не является защитной песочницей для произвольного JavaScript.

[Конфигурация](docs/configuration.md), [проверки и ограничения](docs/validation.md), [манифест файлов](FILE_MANIFEST.json). Изменённые оригиналы и новые файлы отличимы по SOURCE_MANIFEST.json и контрольным суммам.

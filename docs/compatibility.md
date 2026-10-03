# Форматы клиентов и проверенные источники

Проверено 2026-10-03. Manifest validation и наличие CLI-команд не заменяют загрузку навыков в действующей клиентской сессии. Глобальная установка не выполнялась.

| Клиент | Native layout | Что реально проверено |
|---|---|---|
| Codex | root plugin.json с Agent Plugins schema; .codex-plugin/plugin.json fallback; .agents/plugins/marketplace.json | официальная спецификация, реальный marketplace/remotion example, help CLI 0.156.1 для add/list/remove/marketplace add/upgrade/remove |
| Claude Code | .claude-plugin/plugin.json + marketplace.json; root skills/ | официальные docs, frontend-design example, help 2.1.198, strict local validator |
| ZCode | .zcode-plugin/plugin.json; root marketplace.json; root skills/ | официальные docs и zai-org/zcode-plugins marketplace; приложение здесь не запускалось |

Официальные инструкции:
- [OpenAI package/marketplace specification](https://developers.openai.com/plugins/build/plugins).
- [Claude plugins](https://code.claude.com/docs/en/plugins) и [marketplaces](https://code.claude.com/docs/en/plugin-marketplaces).
- [ZCode plugin format and management](https://zcode.z.ai/en/docs/plugin).

Реальные репозитории, которые были прочитаны для сравнения:
- [openai/plugins](https://github.com/openai/plugins), включая [marketplace](https://github.com/openai/plugins/blob/main/.agents/plugins/marketplace.json) и [Remotion manifest](https://github.com/openai/plugins/blob/main/plugins/remotion/.codex-plugin/plugin.json). Проверены source descriptors и skills path.
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official), включая [frontend-design manifest](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/frontend-design/.claude-plugin/plugin.json) и marketplace. Проверены metadata directory и root skill discovery.
- [zai-org/zcode-plugins](https://github.com/zai-org/zcode-plugins), включая [marketplace.json](https://github.com/zai-org/zcode-plugins/blob/main/marketplace.json). Проверены относительные источники, версии и отдельный native каталог из документации.

Пакет не копирует команды, hooks или MCP servers из этих примеров. Его проектный config — договорённость для агента, не native userConfig. При изменении клиента ориентироваться на его актуальную документацию и help.

Команда claude plugin details подтверждена локальным help. Список installed plugins сам по себе не подтверждает runtime-discovery всех восьми skills; это проверяется в новой сессии после установки. Для Codex/ZCode также нужен фактический список навыков в клиенте.

Обновления должны менять version в manifests и marketplace вместе. Codex upgrade обновляет Git marketplace snapshot; локальный источник обновляется через git pull в клоне. Если loader держит старую копию, переустановить именно этот плагин или следовать механизму refresh текущей версии клиента.

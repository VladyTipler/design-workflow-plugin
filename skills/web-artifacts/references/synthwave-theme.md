# Synthwave — необязательный пример темы

Применять только при явном выборе этого направления. Утверждённый канон продукта имеет приоритет. Для нового направления сначала использовать frontend-design. Нижеприведённые значения иллюстративны; контраст проверять отдельно.

## Палитра

| Роль | Hex | Использование |
|---|---|---|
| Фон страницы | `#0f0d1e` | body, html |
| Поверхности (карточки) | `#1a1530` | секции, cards, table rows |
| Поверхности hover/active | `#251f3f` | hover-состояния, alt rows |
| Граница тонкая | `#2d2548` | разделители, борды |
| Текст основной | `#e8e6f0` | заголовки, body |
| Текст приглушённый | `#a8a3c0` | подзаголовки, captions |
| Текст decorative | `#7c728c` | подписи, footer |
| Акцент primary | `#ff007c` | CTA, ссылки, выделение |
| Акцент secondary | `#7c3aed` | заголовки секций, бейджи |
| Cyan | `#06b6d4` | информация, нейтральные данные |
| Success | `#22c55e` | положительные метрики, ✓ |
| Warning | `#f59e0b` | предупреждения, в работе |
| Error | `#ef4444` | негативные метрики, ✗ |

## Шрифт

```css
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #e8e6f0;
  background: #0f0d1e;
}
```

Для standalone-прототипа использовать локальные fallback-шрифты или лицензированный встроенный файл; runtime CDN не требуется.

## Базовый CSS-блок (адаптировать только для выбранного направления)

```css
*, *::before, *::after { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #e8e6f0;
  background: #0f0d1e;
  padding: 20px 16px;
  min-height: 100vh;
}
h1, h2, h3 { color: #ffffff; margin: 0 0 12px; line-height: 1.3; }
h1 { font-size: 28px; }
h2 { font-size: 22px; color: #ff007c; }
h3 { font-size: 18px; color: #7c3aed; }
p { margin: 0 0 12px; }
a { color: #ff007c; text-decoration: none; }
a:hover { text-decoration: underline; }
code { background: #1a1530; padding: 2px 6px; border-radius: 4px; font-size: 14px; }
hr { border: none; border-top: 1px solid #2d2548; margin: 24px 0; }
.muted { color: #a8a3c0; }
.container { max-width: 100%; margin: 0 auto; }
@media (min-width: 768px) {
  body { padding: 32px; }
  .container { max-width: 760px; }
  h1 { font-size: 36px; }
}
```

## Бейджи / статус-чипы

```html
<span class="badge badge-success">Done</span>
<span class="badge badge-warning">In progress</span>
<span class="badge badge-error">Failed</span>
<span class="badge badge-info">Info</span>
```

```css
.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.3px;
}
.badge-success { background: rgba(34,197,94,0.15); color: #22c55e; }
.badge-warning { background: rgba(245,158,11,0.15); color: #f59e0b; }
.badge-error { background: rgba(239,68,68,0.15); color: #ef4444; }
.badge-info { background: rgba(6,182,212,0.15); color: #06b6d4; }
```

## Карточка

```html
<div class="card">
  <div class="card-title">Заголовок</div>
  <div class="card-body">Контент</div>
</div>
```

```css
.card {
  background: #1a1530;
  border: 1px solid #2d2548;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 12px;
}
.card-title { font-size: 14px; color: #a8a3c0; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
.card-body { font-size: 16px; color: #e8e6f0; }
```

## KPI-карточка

```html
<div class="kpi">
  <div class="kpi-label">Подписчики</div>
  <div class="kpi-value">1496</div>
  <div class="kpi-delta positive">+12%</div>
</div>
```

```css
.kpi {
  background: #1a1530;
  border-radius: 12px;
  padding: 20px;
  border-left: 3px solid #ff007c;
}
.kpi-label { font-size: 13px; color: #a8a3c0; text-transform: uppercase; letter-spacing: 0.5px; }
.kpi-value { font-size: 32px; font-weight: 700; color: #ffffff; margin: 6px 0; }
.kpi-delta { font-size: 14px; font-weight: 600; }
.kpi-delta.positive { color: #22c55e; }
.kpi-delta.negative { color: #ef4444; }
```

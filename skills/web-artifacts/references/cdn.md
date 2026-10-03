# CDN-шпаргалка

По умолчанию standalone file://: inline CSS, классический inline JS, встроенные данные и SVG. Примеры CDN ниже — только для отдельно выбранного сетевого режима и НЕ соответствуют локальному offline-контракту.

Для локального режима сначала использовать обычный HTML/CSS/JS. Если библиотека нужна, встроить проверенный лицензированный bundle с атрибуцией и фиксированной версией; не скачивать автоматически. Диаграммы можно предварительно отрендерить в SVG с Mermaid CLI и вставить inline. ES modules и загрузка соседних файлов через fetch не являются переносимым file:// fallback. Устаревшие/нефиксированные CDN-ссылки ниже — справочные, не рекомендации установки.

## Tailwind (CSS utility framework)

**Для прототипов и одноразовых артефактов:**
```html
<script src="https://cdn.tailwindcss.com"></script>
```

Внимание: это JIT-runtime ~50-80kb gzip. Для прод-нагрузки тяжеловат, но для артефактов ок. Если хочешь — кастомизация конфига:
```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          primary: '#ff007c',
          surface: '#1a1530',
          base: '#0f0d1e'
        }
      }
    }
  }
</script>
```

## Chart.js (графики)

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

Минимальный пример (mobile-safe):
```html
<div style="position: relative; height: 280px;">
  <canvas id="myChart"></canvas>
</div>
<script>
new Chart(document.getElementById('myChart'), {
  type: 'bar',  // или 'line', 'pie', 'doughnut', 'radar'
  data: {
    labels: ['Янв', 'Фев', 'Март'],
    datasets: [{
      label: 'Метрика',
      data: [12, 19, 3],
      backgroundColor: '#ff007c'
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: { labels: { color: '#e8e6f0' } } },
    scales: {
      x: { ticks: { color: '#a8a3c0' }, grid: { color: '#251f3f' } },
      y: { ticks: { color: '#a8a3c0' }, grid: { color: '#251f3f' } }
    }
  }
});
</script>
```

## Mermaid (диаграммы из текста)

```html
<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
  mermaid.initialize({ startOnLoad: true, theme: 'dark', themeVariables: { primaryColor: '#ff007c' } });
</script>

<pre class="mermaid">
graph LR
  A[Start] --> B{Decision}
  B -->|Yes| C[OK]
  B -->|No| D[Stop]
</pre>
```

Поддерживаемые типы: flowchart, sequenceDiagram, classDiagram, stateDiagram, erDiagram, gantt, pie, mindmap, timeline, c4Context.

## reveal.js (презентации)

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/black.css">
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
<script>
  Reveal.initialize({
    hash: true,
    touch: true,
    transition: 'slide'
  });
</script>
```

Структура слайдов:
```html
<div class="reveal">
  <div class="slides">
    <section>Слайд 1</section>
    <section>Слайд 2</section>
  </div>
</div>
```

## D3.js (если реально нужно — обычно не нужно)

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
```

Для большинства задач хватит Chart.js. D3 — когда нужны кастомные визуализации (force-directed graphs, sankey, etc.).

## marked.js (Markdown → HTML)

```html
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
  document.getElementById('content').innerHTML = marked.parse('# Hello\n\n**bold**');
</script>
```

## highlight.js (подсветка кода)

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js@11/styles/atom-one-dark.min.css">
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11/lib/core.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11/lib/languages/javascript.min.js"></script>
<script>hljs.highlightAll();</script>
```

## Иконки — Lucide (SVG inline через CDN)

```html
<script src="https://unpkg.com/lucide@latest"></script>
<i data-lucide="check"></i>
<script>lucide.createIcons();</script>
```

Или просто inline SVG из https://lucide.dev — копируешь нужный значок прямо в HTML, не нужен JS.

## Производительность

Для артефакта с одним графиком: только Chart.js + base HTML/CSS = ~50kb gzip → грузится за 1с даже на 3G.
Для презентации: reveal.js + css = ~100kb gzip.
Не подключай libs «на всякий случай» — каждая лишняя secunda загрузки = пользователь закрыл вкладку.

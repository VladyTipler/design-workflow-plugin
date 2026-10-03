# Mobile-first правила для артефактов

## Контекст

Артефакт может открываться с телефона или во встроенном WebView. Проверять минимум ширину 390px и более широкий desktop; дополнительные размеры выбирать по аудитории продукта.

## Жёсткие правила (нарушение = брак)

### 1. Viewport meta

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

Без этого Safari отрендерит как desktop 980px и пользователь будет щипать.

### 2. Базовый шрифт ≥ 16px

```css
body { font-size: 16px; line-height: 1.6; }
```

Меньше → iOS Safari при тапе на input делает zoom. Раздражает.

### 3. Box-sizing border-box (везде)

```css
*, *::before, *::after { box-sizing: border-box; }
```

Без этого `padding` ломает ширину контейнеров на мобилке.

### 4. Безопасные отступы

```css
body { padding: 16px; }  /* мин 16px по бокам */
.container { max-width: 100%; padding: 0 16px; margin: 0 auto; }
```

На десктопе обогатить:
```css
@media (min-width: 768px) {
  .container { max-width: 720px; padding: 0; }
}
```

### 5. Таблицы

**Вариант A — wrap в скролл-контейнер** (для широких):

```html
<div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 0 -16px; padding: 0 16px;">
  <table style="min-width: 600px;">...</table>
</div>
```

`margin: 0 -16px` вытягивает скролл-зону на края экрана, скролл становится естественным.

**Вариант B — превратить в карточки** (для 2-3 колонок):

```html
<div class="card">
  <div class="card-row"><span class="label">Имя:</span> <span class="value">Пример</span></div>
  <div class="card-row"><span class="label">Возраст:</span> <span class="value">31</span></div>
</div>
```

```css
/* цвета подставь из своей aesthetic direction (frontend-design) */
.card { background: var(--surface); padding: 16px; border-radius: var(--radius, 12px); margin-bottom: 12px; }
.card-row { display: flex; justify-content: space-between; padding: 8px 0; }
.card-row .label { color: var(--muted); }
.card-row .value { color: var(--fg); font-weight: 600; }
```

### 6. Кнопки и тап-таргеты

Минимум 44×44px (Apple HIG, реально работает).

```css
.btn {
  display: inline-block;
  padding: 14px 20px;
  min-height: 44px;
  border-radius: 8px;
  font-size: 16px;
}
```

Не используй `padding: 4px 8px` для кнопок — будет неудобно тапать.

### 7. Графики Chart.js

```html
<div style="position: relative; height: 280px; width: 100%;">
  <canvas id="chart"></canvas>
</div>
```

```javascript
// цвета (legend, ticks, grid) подставь под свою aesthetic direction
const FG = getComputedStyle(document.documentElement).getPropertyValue('--fg').trim() || '#111';
const MUTED = getComputedStyle(document.documentElement).getPropertyValue('--muted').trim() || '#6b7280';
const BORDER = getComputedStyle(document.documentElement).getPropertyValue('--border').trim() || '#e5e5e5';

new Chart(document.getElementById('chart'), {
  type: 'bar',
  data: {...},
  options: {
    responsive: true,
    maintainAspectRatio: false,  // КРИТИЧНО, иначе график не уважает height контейнера
    plugins: {
      legend: { labels: { color: FG } }
    },
    scales: {
      x: { ticks: { color: MUTED }, grid: { color: BORDER } },
      y: { ticks: { color: MUTED }, grid: { color: BORDER } }
    }
  }
});
```

### 8. Картинки

```css
img { max-width: 100%; height: auto; display: block; }
```

Никаких фиксированных пиксельных width на картинках.

### 9. Сетка / Flex

```css
.grid {
  display: grid;
  grid-template-columns: 1fr;  /* mobile: 1 колонка */
  gap: 16px;
}

@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

### 10. Long text

`overflow-wrap: anywhere` для URL и длинных слов, иначе они выходят за viewport:

```css
.text-content { overflow-wrap: anywhere; word-break: break-word; }
```

## Проверка

Открой в Chrome DevTools → Toggle device toolbar → iPhone 12 Pro (390×844).

Если:
- Нужен горизонтальный скролл на странице — **брак**
- Шрифт мелкий, тяжело читать — **брак**
- Кнопки тяжело тапать — **брак**
- Графики не помещаются — **брак**

Прежде чем отдавать пользователю — мысленно открой 390px и пройдись глазами.

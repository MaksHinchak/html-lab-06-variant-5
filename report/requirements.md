# Відповідність лабораторній №6, варіант 5

| Вимога | Реалізація |
| --- | --- |
| Статичний малюнок, 40% | `#static-drawing`: 2 кола, 6 прямокутників, ромб; синя заливка, чорні контури та осі |
| Текст по кривій, 10% | `#headline-curve` + `textPath` |
| Зміна кольору, 10% | `#animated-left-circle`, `animate attributeName="fill"` |
| Переміщення, 10% | `#animated-translate`, `animateTransform type="translate"` |
| Обертання, 10% | `#animated-rotate`, `type="rotate"` навколо центра ромба |
| Зміна розміру, 10% | `#animated-scale`, `type="scale"` від 1 до 0.72 й назад |
| Перекіс, 10% | `#animated-skew`, `type="skewX"` від -25° до 25° |
| Зовнішні SVG | object, embed, iframe у розділі вбудовування |
| Теги SVG | svg, defs, symbol, use, g, line, circle, ellipse, rect, polyline, polygon, path, text, textPath, title, desc |
| Керування | Пауза/продовження, перезапуск; початкова пауза за prefers-reduced-motion |
| Доступність | title, desc, aria-labelledby, підписи кнопок та iframe, повідомлення стану |

Координати фігур звірено з синіми векторними об’єктами на сторінці 8 методички. Матеріали джерела намальовані приблизно; реалізація використовує цілі координати схеми. Файл `variant5-reference.png` містить фрагмент саме варіанта 5.

У методичці є неточні назви: SVG має `symbol`, а не `symbols`; перетворення задається атрибутом `transform`, а анімація перетворень — тегом `animateTransform`. Застарілий HTML-тег `param` залишено як навчальний приклад із локальним поясненням для IDE. Він не змінює роботу SVG.

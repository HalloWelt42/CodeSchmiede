---
schema_version: 1
id: w044-erben-lassen
revision: 1
titel: Erben lassen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- vererbung
- inherit
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="hinweis">Achtung: <span>heißer</span> Fisch!</p>

  <p>Heute mit <span>Musik</span>.</p>

  '
ziel_css: ".hinweis {\n  color: gold;\n}\n\nspan {\n  color: gray;\n}\n\n.hinweis span {\n  color: inherit;\n}\n"
hints:
- kosten: 0
  text: Im Hinweis soll der span die Farbe seines Absatzes übernehmen. Eine genauere Regel mit dem Wert inherit macht das.
- kosten: 2
  text: ".hinweis span {\n  color: inherit;\n}"
starter_code: ".hinweis {\n  color: gold;\n}\n\nspan {\n  color: gray;\n}\n"
---

Alle `span` sind grau, das passt. Nur im Hinweis soll das Wort wieder die goldene Farbe seines Absatzes tragen.

## Vorgaben

- Klasse `hinweis`: Schriftfarbe `gold` (steht schon da)
- `span`: Schriftfarbe `gray` (steht schon da)
- `span` im Hinweis: erbt die Farbe seines Absatzes (`inherit`)

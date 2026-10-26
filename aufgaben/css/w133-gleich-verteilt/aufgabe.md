---
schema_version: 1
id: w133-gleich-verteilt
revision: 1
titel: Gleiche Lücken
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- space-evenly
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"reihe\">\n  <div>Hering</div>\n  <div>Makrele</div>\n  <div>Sardine</div>\n</div>\n"
ziel_css: ".reihe {\n  display: flex;\n  justify-content: space-evenly;\n  background-color: #2b3442;\n}\n\n.reihe div {\n\
  \  background-color: teal;\n  padding: 10px;\n}\n"
hints:
- kosten: 0
  text: Auch am Rand soll eine Lücke so groß wie dazwischen sein.
- kosten: 2
  text: 'justify-content: space-evenly;'
starter_code: ".reihe {\n  display: flex;\n  justify-content: space-between;\n  background-color: #2b3442;\n}\n\n.reihe div\
  \ {\n  background-color: teal;\n  padding: 10px;\n}\n"
---

Die äußeren Fische kleben am Rand. Alle Lücken sollen gleich groß sein, auch die am Rand.

## Vorgaben

- Klasse `reihe`: `justify-content: space-evenly`

---
schema_version: 1
id: w122-luecken
revision: 1
titel: Lücken statt Ränder
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- gap
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"reihe\">\n  <div>Hering</div>\n  <div>Makrele</div>\n  <div>Sardine</div>\n</div>\n"
ziel_css: ".reihe {\n  display: flex;\n  gap: 16px;\n}\n\n.reihe div {\n  background-color: teal;\n  padding: 10px;\n}\n"
hints:
- kosten: 0
  text: gap gehört zum Behälter.
- kosten: 2
  text: 'gap: 16px;'
starter_code: ".reihe {\n  display: flex;\n}\n\n.reihe div {\n  background-color: teal;\n  padding: 10px;\n}\n"
---

Die Kästen kleben aneinander. Leg 16 Pixel Lücke dazwischen, aber nicht an den Rand.

## Vorgaben

- Klasse `reihe`: Lücke `16px`

---
schema_version: 1
id: w154-genau-platziert
revision: 1
titel: Genau platziert
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- grid-row
- grid-column
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"brett\">\n  <div class=\"schatz\">Schatz</div>\n</div>\n"
ziel_css: ".brett {\n  display: grid;\n  grid-template-columns: repeat(4, 1fr);\n  grid-template-rows: repeat(3, 80px);\n\
  \  background-color: #2b3442;\n}\n\n.schatz {\n  grid-column: 3 / 5;\n  grid-row: 2 / 4;\n  background-color: gold;\n  color:\
  \ #2b3442;\n}\n"
hints:
- kosten: 0
  text: Spalten 3 und 4 liegen zwischen den Linien 3 und 5, die Zeilen 2 und 3 zwischen 2 und 4.
- kosten: 2
  text: "grid-column: 3 / 5;\n  grid-row: 2 / 4;"
starter_code: ".brett {\n  display: grid;\n  grid-template-columns: repeat(4, 1fr);\n  grid-template-rows: repeat(3, 80px);\n\
  \  background-color: #2b3442;\n}\n\n.schatz {\n  background-color: gold;\n  color: #2b3442;\n}\n"
---

Auf der Schatzkarte liegt der Schatz unten rechts: in den Spalten 3 und 4 und den Zeilen 2 und 3.

## Vorgaben

- Klasse `schatz`: Spalten von Linie 3 bis 5, Zeilen von Linie 2 bis 4

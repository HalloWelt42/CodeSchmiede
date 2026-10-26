---
schema_version: 1
id: w171-der-erste
revision: 1
titel: Der Erste
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- first-child
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"liste\">\n  <li>Hering</li>\n  <li>Makrele</li>\n  <li>Sardine</li>\n  <li>Lachs</li>\n  <li>Dorsch</li>\n\
  \  <li>Scholle</li>\n</ul>\n"
ziel_css: ".liste li {\n  padding: 6px;\n  background-color: #1f6f8b;\n}\n\n.liste li:first-child {\n  background-color: gold;\n\
  \  color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: Das erste Kind seiner Liste.
- kosten: 2
  text: .liste li:first-child {
starter_code: ".liste li {\n  padding: 6px;\n  background-color: #1f6f8b;\n}\n"
---

Der erste Fisch der Liste ist der Fang des Tages und wird golden.

## Vorgaben

- das erste `li` der Liste: Hintergrund `gold`, Schrift `#2b3442`

---
schema_version: 1
id: w141-drei-spalten
revision: 1
titel: Drei Spalten
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- grid
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"fach\">\n  <div>Hering</div>\n  <div>Makrele</div>\n  <div>Sardine</div>\n  <div>Lachs</div>\n  <div>Scholle</div>\n\
  \  <div>Dorsch</div>\n</div>\n"
ziel_css: ".fach {\n  display: grid;\n  grid-template-columns: 120px 120px 120px;\n}\n\n.fach div {\n  background-color: teal;\n\
  \  border: 1px solid #2b3442;\n  padding: 8px;\n}\n"
hints:
- kosten: 0
  text: Der Behälter wird zum Raster mit drei Spalten zu je 120 Pixeln.
- kosten: 2
  text: ".fach {\n  display: grid;\n  grid-template-columns: 120px 120px 120px;\n}"
starter_code: ".fach div {\n  background-color: teal;\n  border: 1px solid #2b3442;\n  padding: 8px;\n}\n"
---

Sechs Fische sollen in einem Raster aus drei Spalten liegen, je 120 Pixel breit.

## Vorgaben

- Klasse `fach`: Raster mit den Spalten `120px 120px 120px`

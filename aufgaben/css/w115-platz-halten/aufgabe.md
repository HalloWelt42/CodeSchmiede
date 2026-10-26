---
schema_version: 1
id: w115-platz-halten
revision: 1
titel: Platz halten
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- display
- opacity
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"regal\">\n  <div class=\"dose\">Sardinen</div>\n  <div class=\"dose leer\">leer</div>\n  <div class=\"\
  dose\">Thunfisch</div>\n</div>\n"
ziel_css: ".dose {\n  display: inline-block;\n  width: 120px;\n  height: 120px;\n  margin: 6px;\n  background-color: #c98c55;\n\
  \  color: #2b3442;\n}\n\n.leer {\n  opacity: 0;\n}\n"
hints:
- kosten: 0
  text: Mit display none rückt der Thunfisch nach links. Die Lücke im Regal soll bleiben.
- kosten: 2
  text: ".leer {\n  opacity: 0;\n}"
starter_code: ".dose {\n  display: inline-block;\n  width: 120px;\n  height: 120px;\n  margin: 6px;\n  background-color: #c98c55;\n\
  \  color: #2b3442;\n}\n\n.leer {\n  display: none;\n}\n"
---

Die leere Dose soll unsichtbar sein, aber ihre Lücke im Regal soll bleiben, damit Pit weiß, wo nachgefüllt werden muss.

## Vorgaben

- Klasse `leer`: unsichtbar, der Platz bleibt

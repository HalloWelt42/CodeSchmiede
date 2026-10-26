---
schema_version: 1
id: w121-in-eine-reihe
revision: 1
titel: In eine Reihe!
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- flex
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"leiste\">\n  <div>Fisch</div>\n  <div>Getränke</div>\n  <div>Eis</div>\n  <div>Über uns</div>\n</div>\n"
ziel_css: ".leiste {\n  display: flex;\n}\n\n.leiste div {\n  background-color: teal;\n  padding: 10px;\n  margin-right: 6px;\n\
  }\n"
hints:
- kosten: 0
  text: Eine Angabe beim Behälter reicht.
- kosten: 2
  text: ".leiste {\n  display: flex;\n}"
starter_code: ".leiste div {\n  background-color: teal;\n  padding: 10px;\n  margin-right: 6px;\n}\n"
---

Die Einträge der Leiste stehen untereinander. Mit einer einzigen Angabe beim Behälter stehen sie in einer Reihe.

## Vorgaben

- Klasse `leiste`: `display: flex`

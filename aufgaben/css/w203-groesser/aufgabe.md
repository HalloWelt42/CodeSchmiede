---
schema_version: 1
id: w203-groesser
revision: 1
titel: Der Hauptgewinn
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- scale
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"reihe\">\n  <div>Los 1</div>\n  <div class=\"gewinn\">Hauptgewinn</div>\n  <div>Los 3</div>\n</div>\n"
ziel_css: ".reihe {\n  display: flex;\n  gap: 40px;\n  margin: 40px;\n}\n\n.reihe div {\n  padding: 14px;\n  background-color:\
  \ teal;\n}\n\n.reihe .gewinn {\n  transform: scale(1.6);\n  background-color: gold;\n  color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: Vergrößern auf das 1,6-Fache.
- kosten: 2
  text: 'transform: scale(1.6);'
starter_code: ".reihe {\n  display: flex;\n  gap: 40px;\n  margin: 40px;\n}\n\n.reihe div {\n  padding: 14px;\n  background-color:\
  \ teal;\n}\n\n.reihe .gewinn {\n  background-color: gold;\n  color: #2b3442;\n}\n"
---

Beim Fischfest wird der Hauptgewinn größer gezeigt als die anderen Lose.

## Vorgaben

- `.reihe .gewinn`: Größe `scale(1.6)`

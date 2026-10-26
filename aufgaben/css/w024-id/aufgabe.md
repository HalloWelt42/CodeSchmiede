---
schema_version: 1
id: w024-id
revision: 1
titel: Der Fang des Tages
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- id
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul>\n  <li>Hering</li>\n  <li id=\"fang\">Riesenmakrele</li>\n  <li>Sardinen</li>\n</ul>\n"
ziel_css: "#fang {\n  color: black;\n  background-color: gold;\n}\n"
hints:
- kosten: 0
  text: Im HTML steht id, nicht class. Für eine id nimmt man die Raute statt des Punkts.
- kosten: 2
  text: '#fang {'
starter_code: ".fang {\n  color: black;\n  background-color: gold;\n}\n"
---

Die Riesenmakrele ist der Fang des Tages und soll golden leuchten. Die Regel ist schon geschrieben, trifft aber nicht.

## Vorgaben

- das Element mit der id `fang`: Schriftfarbe `black`, Hintergrundfarbe `gold`

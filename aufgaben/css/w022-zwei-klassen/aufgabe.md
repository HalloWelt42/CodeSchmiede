---
schema_version: 1
id: w022-zwei-klassen
revision: 1
titel: Hering und Makrele
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul>\n  <li class=\"hering\">Hering im Eismantel</li>\n  <li class=\"makrele\">Makrele am Stiel</li>\n  <li class=\"\
  hering\">Hering vom Grill</li>\n</ul>\n"
ziel_css: ".hering {\n  color: skyblue;\n}\n\n.makrele {\n  color: tomato;\n}\n"
hints:
- kosten: 0
  text: Für die Makrele brauchst du eine zweite Regel mit ihrer Klasse.
- kosten: 2
  text: ".makrele {\n  color: tomato;\n}"
starter_code: ".hering {\n  color: skyblue;\n}\n"
---

Alle Heringe sind schon himmelblau. Jetzt bekommt die Makrele ihre eigene Farbe.

## Vorgaben

- Klasse `hering`: Schriftfarbe `skyblue` (steht schon da)
- Klasse `makrele`: Schriftfarbe `tomato`

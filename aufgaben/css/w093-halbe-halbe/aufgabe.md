---
schema_version: 1
id: w093-halbe-halbe
revision: 1
titel: Halbe-halbe
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- prozent
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"theke\">\n  <p class=\"links\">Hering</p>\n  <p class=\"rechts\">Makrele</p>\n</div>\n"
ziel_css: ".theke {\n  width: 360px;\n  background-color: #2b3442;\n  padding: 10px;\n}\n\n.links {\n  width: 50%;\n  background-color:\
  \ teal;\n}\n\n.rechts {\n  width: 75%;\n  background-color: purple;\n}\n"
hints:
- kosten: 0
  text: Prozent beziehen sich auf die Theke. Hering bekommt die Hälfte, Makrele drei Viertel.
- kosten: 2
  text: 'width: 50%; und width: 75%;'
starter_code: ".theke {\n  width: 360px;\n  background-color: #2b3442;\n  padding: 10px;\n}\n\n.links {\n  background-color:\
  \ teal;\n}\n\n.rechts {\n  background-color: purple;\n}\n"
---

Auf der Theke liegen zwei Streifen. Der Hering bekommt die Hälfte der Breite, die Makrele drei Viertel.

## Vorgaben

- Klasse `theke`: wie bisher
- Klasse `links`: Breite `50%`
- Klasse `rechts`: Breite `75%`

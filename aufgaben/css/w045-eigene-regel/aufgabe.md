---
schema_version: 1
id: w045-eigene-regel
revision: 1
titel: Eigene Regel schlägt Erbe
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- vererbung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div id=\"karte\">\n  <h2>Speisekarte</h2>\n  <p>Hering</p>\n  <p>Makrele</p>\n</div>\n"
ziel_css: "#karte {\n  color: gold;\n}\n\np {\n  color: skyblue;\n}\n"
hints:
- kosten: 0
  text: Die Absätze erben gold. Eine eigene Regel für p schlägt jede geerbte Farbe, auch die von einer id.
- kosten: 2
  text: "p {\n  color: skyblue;\n}"
starter_code: "#karte {\n  color: gold;\n}\n"
---

Die Karte vererbt Gold an alles. Die Absätze sollen trotzdem himmelblau sein, mit einer ganz schlichten Regel.

## Vorgaben

- id `karte`: Schriftfarbe `gold` (steht schon da)
- Absätze: Schriftfarbe `skyblue`

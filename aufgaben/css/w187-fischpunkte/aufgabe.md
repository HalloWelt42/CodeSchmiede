---
schema_version: 1
id: w187-fischpunkte
revision: 1
titel: Fische als Punkte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- marker
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"liste\">\n  <li>Hering</li>\n  <li>Makrele</li>\n  <li>Sardine</li>\n</ul>\n"
ziel_css: ".liste li::marker {\n  content: \"~ \";\n  color: #38bdf8;\n  font-weight: bold;\n}\n"
hints:
- kosten: 0
  text: Die Punkte sind ::marker. Er bekommt einen neuen Inhalt und eine Farbe.
- kosten: 2
  text: ".liste li::marker {\n  content: \"~ \";\n  color: #38bdf8;\n  font-weight: bold;\n}"
starter_code: '/* Andere Listenpunkte */

  '
---

Statt runder Punkte bekommen die Fische kleine blaue Wellen.

## Vorgaben

- `.liste li::marker`: Inhalt `"~ "`, Farbe `#38bdf8`, fett

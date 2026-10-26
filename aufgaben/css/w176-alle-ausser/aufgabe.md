---
schema_version: 1
id: w176-alle-ausser
revision: 1
titel: Alle außer einem
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- not
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"liste\">\n  <li>Hering</li>\n  <li class=\"weg\">Eisscholle</li>\n  <li>Makrele</li>\n  <li class=\"\
  weg\">Tintenfisch</li>\n  <li>Sardine</li>\n</ul>\n"
ziel_css: ".liste li {\n  padding: 6px;\n}\n\n.liste li:not(.weg) {\n  background-color: #3fb950;\n  color: #0b1d3a;\n}\n"
hints:
- kosten: 0
  text: Alle li, die nicht die Klasse weg tragen.
- kosten: 2
  text: .liste li:not(.weg) {
starter_code: ".liste li {\n  padding: 6px;\n}\n"
---

Alles, was noch da ist, leuchtet grün. Was weg ist, bleibt ohne Hintergrund. Schreib eine einzige Regel mit `:not`.

## Vorgaben

- `li` ohne die Klasse `weg`: Hintergrund `#3fb950`, Schrift `#0b1d3a`

---
schema_version: 1
id: w103-eingedrueckt
revision: 1
titel: Eingedrückt
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- box-shadow
- inset
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="feld">Name eintragen</p>

  '
ziel_css: ".feld {\n  width: 240px;\n  padding: 12px;\n  background-color: #e3f1f8;\n  color: #555;\n  border-radius: 6px;\n\
  \  box-shadow: inset 0 3px 8px #2b3442;\n}\n"
hints:
- kosten: 0
  text: Ein Schatten nach innen, mit dem Wort inset vorne.
- kosten: 2
  text: 'box-shadow: inset 0 3px 8px #2b3442;'
starter_code: ".feld {\n  width: 240px;\n  padding: 12px;\n  background-color: #e3f1f8;\n  color: #555;\n  border-radius:\
  \ 6px;\n}\n"
---

Das Feld soll aussehen, als wäre es in die Seite eingedrückt.

## Vorgaben

- Klasse `feld`: wie bisher, dazu Schatten nach innen `0 3px 8px #2b3442`

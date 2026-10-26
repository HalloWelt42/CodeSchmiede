---
schema_version: 1
id: w111-leiste
revision: 1
titel: Eine Leiste
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- display
- inline
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<ul class=\"leiste\">\n  <li>Fisch</li>\n  <li>Getränke</li>\n  <li>Eis</li>\n  <li>Über uns</li>\n</ul>\n"
ziel_css: ".leiste li {\n  display: inline;\n  margin-right: 24px;\n}\n"
hints:
- kosten: 0
  text: Listeneinträge sind Blöcke. Als inline rücken sie in eine Zeile.
- kosten: 2
  text: 'display: inline;'
starter_code: ".leiste li {\n  margin-right: 24px;\n}\n"
---

Aus der Liste soll eine Leiste werden: alle Einträge in einer Zeile.

## Vorgaben

- Einträge der Leiste: `display: inline`, Außenabstand rechts `24px` (steht schon da)

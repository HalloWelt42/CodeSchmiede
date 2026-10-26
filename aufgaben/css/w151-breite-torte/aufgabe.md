---
schema_version: 1
id: w151-breite-torte
revision: 1
titel: Die breite Torte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- grid-column
- span
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"tisch\">\n  <div class=\"torte\">Torte</div>\n  <div>Hering</div>\n  <div>Lachs</div>\n  <div>Dorsch</div>\n\
  \  <div>Aal</div>\n  <div>Sprotte</div>\n</div>\n"
ziel_css: ".tisch {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  gap: 4px;\n}\n\n.tisch div {\n  background-color:\
  \ teal;\n  padding: 8px;\n}\n\n.tisch .torte {\n  grid-column: span 3;\n  background-color: crimson;\n}\n"
hints:
- kosten: 0
  text: Die Torte soll sich über alle drei Spalten spannen.
- kosten: 2
  text: 'grid-column: span 3;'
starter_code: ".tisch {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  gap: 4px;\n}\n\n.tisch div {\n  background-color:\
  \ teal;\n  padding: 8px;\n}\n\n.tisch .torte {\n  background-color: crimson;\n}\n"
---

Die Torte für das Fischfest braucht den ganzen ersten Tisch, über alle drei Spalten.

## Vorgaben

- Torte (`.tisch .torte`): über drei Spalten gespannt

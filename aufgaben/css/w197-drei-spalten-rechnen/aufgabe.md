---
schema_version: 1
id: w197-drei-spalten-rechnen
revision: 1
titel: Drei gleiche Spalten
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- calc
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"reihe\">\n  <div>Hering</div>\n  <div>Makrele</div>\n  <div>Sardine</div>\n</div>\n"
ziel_css: ":root {\n  --luecke: 12px;\n}\n\n.reihe {\n  display: flex;\n  gap: var(--luecke);\n}\n\n.reihe div {\n  width:\
  \ calc((100% - 2 * var(--luecke)) / 3);\n  padding: 10px 0;\n  text-align: center;\n  background-color: teal;\n}\n"
hints:
- kosten: 0
  text: Von der vollen Breite gehen zwei Lücken ab, der Rest wird durch drei geteilt.
- kosten: 2
  text: 'width: calc((100% - 2 * var(--luecke)) / 3);'
starter_code: ":root {\n  --luecke: 12px;\n}\n\n.reihe {\n  display: flex;\n  gap: var(--luecke);\n}\n\n.reihe div {\n  padding:\
  \ 10px 0;\n  text-align: center;\n  background-color: teal;\n}\n"
---

Drei Kästen sollen gleich breit sein und genau in die Reihe passen. Rechne die Breite aus: volle Breite minus zwei Lücken, durch drei.

## Vorgaben

- `.reihe div`: Breite `calc((100% - 2 * var(--luecke)) / 3)`

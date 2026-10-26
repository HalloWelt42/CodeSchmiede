---
schema_version: 1
id: w193-ersatzwert
revision: 1
titel: Vertippt
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- var
- ersatz
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="a">Hering</p>

  <p class="b">Makrele</p>

  '
ziel_css: ":root {\n  --fisch: skyblue;\n}\n\n.a {\n  color: var(--fisch);\n}\n\n.b {\n  color: var(--fish, tomato);\n}\n"
hints:
- kosten: 0
  text: Die Variable --fish gibt es nicht. Ein Ersatzwert nach einem Komma rettet die Angabe.
- kosten: 2
  text: 'color: var(--fish, tomato);'
starter_code: ":root {\n  --fisch: skyblue;\n}\n\n.a {\n  color: var(--fisch);\n}\n\n.b {\n  color: var(--fish);\n}\n"
---

Pit hat sich bei der Makrele vertippt, und die Farbe fällt weg. Lass den Tippfehler stehen, aber gib einen Ersatzwert tomato an.

## Vorgaben

- `.b`: `var(--fish, tomato)`

---
schema_version: 1
id: w117-schmale-ueberschrift
revision: 1
titel: Nur so breit wie nötig
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- inline-block
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h2>Heute frisch</h2>

  <p>Hering im Eismantel</p>

  <h2>Getränke</h2>

  <p>Eiswasser</p>

  '
ziel_css: "h2 {\n  display: inline-block;\n  padding: 4px 12px;\n  margin: 10px 0 0;\n  background-color: #ffd166;\n  color:\
  \ #2b3442;\n  border-radius: 6px;\n}\n\np {\n  margin: 6px 0 0;\n}\n"
hints:
- kosten: 0
  text: Als Block ist die Überschrift so breit wie die Bühne. inline-block macht sie nur so breit wie ihr Text.
- kosten: 2
  text: 'display: inline-block;'
starter_code: "h2 {\n  padding: 4px 12px;\n  margin: 10px 0 0;\n  background-color: #ffd166;\n  color: #2b3442;\n  border-radius:\
  \ 6px;\n}\n\np {\n  margin: 6px 0 0;\n}\n"
---

Die goldenen Überschriften sollen nur so breit sein wie ihr Text, nicht über die ganze Bühne.

## Vorgaben

- `h2`: `display: inline-block`, alles andere bleibt

---
schema_version: 1
id: w153-ganze-breite
revision: 1
titel: Von Linie zu Linie
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- grid-column
- linien
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"plan\">\n  <div>A</div>\n  <div>B</div>\n  <div>C</div>\n  <div class=\"fuss\">Fuß</div>\n</div>\n"
ziel_css: ".plan {\n  display: grid;\n  grid-template-columns: 1fr 2fr 1fr;\n  gap: 4px;\n}\n\n.plan div {\n  background-color:\
  \ teal;\n  padding: 8px;\n  height: 60px;\n}\n\n.plan .fuss {\n  grid-column: 1 / -1;\n  background-color: purple;\n}\n"
hints:
- kosten: 0
  text: Von der ersten bis zur letzten Linie, ohne zu zählen.
- kosten: 2
  text: 'grid-column: 1 / -1;'
starter_code: ".plan {\n  display: grid;\n  grid-template-columns: 1fr 2fr 1fr;\n  gap: 4px;\n}\n\n.plan div {\n  background-color:\
  \ teal;\n  padding: 8px;\n  height: 60px;\n}\n\n.plan .fuss {\n  background-color: purple;\n}\n"
---

Der Fuß soll von der ersten bis zur letzten Linie reichen, über die ganze Breite.

## Vorgaben

- Fuß (`.plan .fuss`): `grid-column: 1 / -1`

---
schema_version: 1
id: w215-reihenfolge
revision: 1
titel: Die Reihenfolge zählt
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- media
- kaskade
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h2>Speisekarte</h2>

  <p>Heute mit Musik.</p>

  '
ziel_css: "h2 {\n  color: skyblue;\n}\n\n@media (min-width: 500px) {\n  h2 {\n    color: gold;\n    font-size: 40px;\n  }\n\
  }\n"
hints:
- kosten: 0
  text: Die Regel außerhalb steht später und gewinnt bei der Farbe. Stell die Media Query ans Ende.
- kosten: 2
  text: 'Erst h2 { color: skyblue; }, dann die Media Query.'
starter_code: "@media (min-width: 500px) {\n  h2 {\n    color: gold;\n    font-size: 40px;\n  }\n}\n\nh2 {\n  color: skyblue;\n\
  }\n"
---

Auf breiten Fenstern soll die Überschrift gold sein. Die Größe wirkt schon, die Farbe nicht. Ändere keine Angabe, nur die Reihenfolge.

## Vorgaben

- die Media Query steht nach der Regel `h2 { color: skyblue; }`

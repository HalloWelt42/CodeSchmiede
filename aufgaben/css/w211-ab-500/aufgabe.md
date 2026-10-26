---
schema_version: 1
id: w211-ab-500
revision: 1
titel: Ab 500 Pixeln
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- media
- min-width
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Fischwagen</h1>

  <p>Heute frisch</p>

  '
ziel_css: "h1 {\n  color: white;\n}\n\n@media (min-width: 500px) {\n  h1 {\n    color: gold;\n    font-size: 48px;\n  }\n\
  }\n"
hints:
- kosten: 0
  text: Die Bühne ist 600 Pixel breit. Mindestens 800 trifft nicht zu.
- kosten: 2
  text: '@media (min-width: 500px) {'
starter_code: "h1 {\n  color: white;\n}\n\n@media (min-width: 800px) {\n  h1 {\n    color: gold;\n    font-size: 48px;\n \
  \ }\n}\n"
---

Auf breiten Bildschirmen soll die Überschrift groß und golden sein. Pit hat die Grenze aber so hoch gesetzt, dass sie auf der 600 Pixel breiten Bühne nicht greift. Setz sie auf 500 Pixel.

## Vorgaben

- die Media Query gilt ab `min-width: 500px`

---
schema_version: 1
id: w162-in-die-ecke
revision: 1
titel: In die Ecke
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- position
- absolute
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Fischwagen</h1>

  <p class="geoeffnet">Geöffnet</p>

  <p>Heute mit Musik.</p>

  '
ziel_css: ".geoeffnet {\n  position: absolute;\n  top: 10px;\n  right: 10px;\n  padding: 6px 12px;\n  margin: 0;\n  background-color:\
  \ #3fb950;\n  color: #0b1d3a;\n}\n"
hints:
- kosten: 0
  text: Aus dem Fluss nehmen und mit top und right in die obere rechte Ecke setzen.
- kosten: 2
  text: "position: absolute;\n  top: 10px;\n  right: 10px;"
starter_code: ".geoeffnet {\n  padding: 6px 12px;\n  margin: 0;\n  background-color: #3fb950;\n  color: #0b1d3a;\n}\n"
---

Das Schild Geöffnet soll in die obere rechte Ecke der Bühne, mit 10 Pixeln Abstand zu beiden Rändern.

## Vorgaben

- Klasse `geoeffnet`: `position: absolute`, `top: 10px`, `right: 10px`

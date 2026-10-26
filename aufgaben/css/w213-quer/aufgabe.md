---
schema_version: 1
id: w213-quer
revision: 1
titel: Quer gehalten
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- media
- orientation
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="bild">Panorama vom Eisberg</div>

  '
ziel_css: ".bild {\n  height: 120px;\n  padding: 10px;\n  background-color: #38bdf8;\n  color: #0b1d3a;\n}\n\n@media (orientation:\
  \ landscape) {\n  .bild {\n    height: 300px;\n    background: linear-gradient(to bottom, #38bdf8, #0b4f8a);\n  }\n}\n"
hints:
- kosten: 0
  text: Die Bühne ist breiter als hoch.
- kosten: 2
  text: '@media (orientation: landscape) {'
starter_code: ".bild {\n  height: 120px;\n  padding: 10px;\n  background-color: #38bdf8;\n  color: #0b1d3a;\n}\n\n@media (orientation:\
  \ portrait) {\n  .bild {\n    height: 300px;\n    background: linear-gradient(to bottom, #38bdf8, #0b4f8a);\n  }\n}\n"
---

Das Panorama soll groß erscheinen, wenn das Fenster quer liegt. Pit hat die Ausrichtung verwechselt.

## Vorgaben

- die Media Query fragt `orientation: landscape` ab

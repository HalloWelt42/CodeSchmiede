---
schema_version: 1
id: w094-viertel-buehne
revision: 1
titel: Ein Viertel der Bühne
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- vw
- vh
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="fenster">Ausblick</div>

  '
ziel_css: ".fenster {\n  width: 50vw;\n  height: 50vh;\n  background-color: #38bdf8;\n  color: #0b1d3a;\n}\n"
hints:
- kosten: 0
  text: Pit hat px statt vw und vh geschrieben.
- kosten: 2
  text: "width: 50vw;\n  height: 50vh;"
starter_code: ".fenster {\n  width: 50px;\n  height: 50px;\n  background-color: #38bdf8;\n  color: #0b1d3a;\n}\n"
---

Das Fenster soll halb so breit und halb so hoch wie die Bühne sein, gemessen am Fenster, nicht in Pixeln.

## Vorgaben

- Klasse `fenster`: Breite `50vw`, Höhe `50vh`

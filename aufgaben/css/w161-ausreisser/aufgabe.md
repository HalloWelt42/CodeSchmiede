---
schema_version: 1
id: w161-ausreisser
revision: 1
titel: Der Ausreißer
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- position
- relative
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="a">Hering</p>

  <p class="b">Makrele</p>

  <p class="c">Sardine</p>

  '
ziel_css: "p {\n  width: 220px;\n  padding: 6px;\n  background-color: teal;\n}\n\n.b {\n  position: relative;\n  left: 60px;\n\
  \  background-color: crimson;\n}\n"
hints:
- kosten: 0
  text: 'Verschieben, ohne dass die anderen es merken: position relative und ein Versatz.'
- kosten: 2
  text: "position: relative;\n  left: 60px;"
starter_code: "p {\n  width: 220px;\n  padding: 6px;\n  background-color: teal;\n}\n\n.b {\n  background-color: crimson;\n\
  }\n"
---

Die Makrele tanzt aus der Reihe: 60 Pixel nach rechts. Die anderen bleiben, wo sie sind.

## Vorgaben

- Klasse `b`: `position: relative`, `left: 60px`

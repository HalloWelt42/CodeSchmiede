---
schema_version: 1
id: w096-untergrenze
revision: 1
titel: Nicht zu schmal
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- min-width
- min-height
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="marke">neu</p>

  <p class="marke">ausverkauft</p>

  '
ziel_css: ".marke {\n  width: 10%;\n  min-width: 120px;\n  min-height: 3em;\n  background-color: crimson;\n  text-align: center;\n\
  }\n"
hints:
- kosten: 0
  text: 'Zwei Untergrenzen: eine für die Breite in Pixeln, eine für die Höhe in em.'
- kosten: 2
  text: "min-width: 120px;\n  min-height: 3em;"
starter_code: ".marke {\n  width: 10%;\n  background-color: crimson;\n  text-align: center;\n}\n"
---

Zehn Prozent sind für die Marken zu schmal, das Wort ausverkauft passt nicht hinein. Setz Untergrenzen für Breite und Höhe.

## Vorgaben

- Klasse `marke`: wie bisher, dazu Breite mindestens `120px`, Höhe mindestens `3em`

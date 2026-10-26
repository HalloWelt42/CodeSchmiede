---
schema_version: 1
id: w086-sprechblase
revision: 1
titel: Pit sagt
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- border-radius
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="blase">Frisch!</p>

  '
ziel_css: ".blase {\n  width: 100px;\n  padding: 30px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n  border-radius:\
  \ 40px 40px 40px 0;\n}\n"
hints:
- kosten: 0
  text: Vier Werte, von oben links im Uhrzeigersinn. Nur unten links bleibt spitz.
- kosten: 2
  text: 'border-radius: 40px 40px 40px 0;'
starter_code: ".blase {\n  width: 100px;\n  padding: 30px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n}\n"
---

Pits Sprechblase soll rund sein, nur unten links spitz, wo sie auf Pit zeigt.

## Vorgaben

- Klasse `blase`: wie bisher, dazu Ecken `40px`, nur unten links `0`

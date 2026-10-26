---
schema_version: 1
id: w095-obergrenze
revision: 1
titel: Nicht zu breit
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- max-width
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="hinweis">Bitte nicht die Pinguine füttern, sie haben schon gegessen.</p>

  '
ziel_css: ".hinweis {\n  width: 90%;\n  max-width: 320px;\n  padding: 1em;\n  background-color: #fbf4e2;\n  color: #2b3442;\n\
  }\n"
hints:
- kosten: 0
  text: Eine Obergrenze für die Breite.
- kosten: 2
  text: 'max-width: 320px;'
starter_code: ".hinweis {\n  width: 90%;\n  padding: 1em;\n  background-color: #fbf4e2;\n  color: #2b3442;\n}\n"
---

Der Hinweis ist auf der Bühne viel zu breit. Er soll höchstens 320 Pixel breit werden.

## Vorgaben

- Klasse `hinweis`: wie bisher, dazu Breite höchstens `320px`

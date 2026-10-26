---
schema_version: 1
id: w105-sonnenuntergang
revision: 1
titel: Sonnenuntergang
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- linear-gradient
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="himmel">Feierabend am Fischwagen</div>

  '
ziel_css: ".himmel {\n  height: 200px;\n  padding: 16px;\n  background: linear-gradient(to bottom, #ffb347, #ff5e62, #2b1a4a);\n\
  }\n"
hints:
- kosten: 0
  text: Ein Verlauf mit drei Farben von oben nach unten, bei background statt background-color.
- kosten: 2
  text: 'background: linear-gradient(to bottom, #ffb347, #ff5e62, #2b1a4a);'
starter_code: ".himmel {\n  height: 200px;\n  padding: 16px;\n  background-color: #ff5e62;\n}\n"
---

Der Himmel ist einfarbig rot. Er soll von Orange über Rot zu Nachtlila verlaufen.

## Vorgaben

- Klasse `himmel`: Höhe und Polster wie bisher, Hintergrund als Verlauf nach unten: `#ffb347`, `#ff5e62`, `#2b1a4a`

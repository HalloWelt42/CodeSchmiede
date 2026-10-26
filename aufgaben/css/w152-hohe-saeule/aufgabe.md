---
schema_version: 1
id: w152-hohe-saeule
revision: 1
titel: Die hohe Säule
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- grid-row
- span
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"wand\">\n  <div class=\"saeule\">Leuchtturm</div>\n  <div>1</div>\n  <div>2</div>\n  <div>3</div>\n\
  \  <div>4</div>\n</div>\n"
ziel_css: ".wand {\n  display: grid;\n  grid-template-columns: 120px 1fr 1fr;\n  grid-template-rows: 80px 80px;\n  gap: 4px;\n\
  }\n\n.wand div {\n  background-color: teal;\n  padding: 8px;\n}\n\n.wand .saeule {\n  grid-row: span 2;\n  background-color:\
  \ #ffd166;\n  color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: Der Leuchtturm soll zwei Zeilen hoch werden.
- kosten: 2
  text: 'grid-row: span 2;'
starter_code: ".wand {\n  display: grid;\n  grid-template-columns: 120px 1fr 1fr;\n  grid-template-rows: 80px 80px;\n  gap:\
  \ 4px;\n}\n\n.wand div {\n  background-color: teal;\n  padding: 8px;\n}\n\n.wand .saeule {\n  background-color: #ffd166;\n\
  \  color: #2b3442;\n}\n"
---

Der Leuchtturm links soll über beide Zeilen reichen, die Zahlen daneben füllen den Rest.

## Vorgaben

- Leuchtturm (`.wand .saeule`): über zwei Zeilen gespannt

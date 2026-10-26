---
schema_version: 1
id: w207-gespiegelt
revision: 1
titel: Spiegelbild
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- scale
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"wasser\">\n  <p class=\"name\">Pinguin</p>\n  <p class=\"name spiegel\">Pinguin</p>\n</div>\n"
ziel_css: ".wasser {\n  width: 260px;\n  padding: 10px;\n  background: linear-gradient(to bottom, #0b1d3a 50%, #0b4f8a 50%);\n\
  }\n\n.name {\n  margin: 0;\n  font-size: 56px;\n  text-align: center;\n  color: #ffd166;\n}\n\n.spiegel {\n  transform:\
  \ scale(1, -1);\n  opacity: 0.4;\n}\n"
hints:
- kosten: 0
  text: 'Ein negativer Wert bei scale spiegelt. Senkrecht spiegeln heißt: die Höhe mal minus eins.'
- kosten: 2
  text: 'transform: scale(1, -1);'
starter_code: ".wasser {\n  width: 260px;\n  padding: 10px;\n  background: linear-gradient(to bottom, #0b1d3a 50%, #0b4f8a\
  \ 50%);\n}\n\n.name {\n  margin: 0;\n  font-size: 56px;\n  text-align: center;\n  color: #ffd166;\n}\n\n.spiegel {\n  opacity:\
  \ 0.4;\n}\n"
---

Das Wort spiegelt sich im Wasser: Die untere Zeile steht auf dem Kopf. Mit scale und einem negativen Wert für die Höhe geht das.

## Vorgaben

- Klasse `spiegel`: `transform: scale(1, -1)`

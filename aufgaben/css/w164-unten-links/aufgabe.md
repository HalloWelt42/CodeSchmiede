---
schema_version: 1
id: w164-unten-links
revision: 1
titel: Unten links
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- position
- bottom
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"bild\">\n  Riesenhering\n  <span class=\"unterschrift\">Foto: Pia</span>\n</div>\n"
ziel_css: ".bild {\n  position: relative;\n  width: 240px;\n  height: 140px;\n  padding: 10px;\n  background-color: #38bdf8;\n\
  \  color: #0b1d3a;\n}\n\n.unterschrift {\n  position: absolute;\n  bottom: 8px;\n  left: 8px;\n  font-size: 14px;\n  background-color:\
  \ #fbf4e2;\n  padding: 4px 10px;\n}\n"
hints:
- kosten: 0
  text: Die Unterschrift gehört in die untere linke Ecke des Bildes.
- kosten: 2
  text: "position: absolute;\n  bottom: 8px;\n  left: 8px;"
starter_code: ".bild {\n  position: relative;\n  width: 240px;\n  height: 140px;\n  padding: 10px;\n  background-color: #38bdf8;\n\
  \  color: #0b1d3a;\n}\n\n.unterschrift {\n  font-size: 14px;\n  background-color: #fbf4e2;\n  padding: 4px 10px;\n}\n"
---

Die Unterschrift des Fotos soll unten links im Bild stehen, 8 Pixel vom Rand.

## Vorgaben

- Klasse `unterschrift`: `position: absolute`, `bottom: 8px`, `left: 8px`

---
schema_version: 1
id: w147-eiswuerfelfach
revision: 1
titel: Das Eiswürfelfach
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- grid
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"fach\">\n  <div></div>\n  <div></div>\n  <div></div>\n  <div></div>\n  <div></div>\n  <div></div>\n\
  \  <div></div>\n  <div></div>\n  <div></div>\n  <div></div>\n  <div></div>\n  <div></div>\n</div>\n"
ziel_css: ".fach {\n  display: grid;\n  grid-template-columns: repeat(4, 80px);\n  grid-template-rows: repeat(3, 80px);\n\
  \  gap: 8px;\n  padding: 8px;\n  width: 344px;\n  background-color: #38bdf8;\n  border-radius: 12px;\n}\n\n.fach div {\n\
  \  background-color: #e3f1f8;\n  border-radius: 8px;\n}\n"
hints:
- kosten: 0
  text: Vier mal drei Fächer zu je 80 Pixeln, mit Lücken und Polster.
- kosten: 3
  text: repeat(4, 80px) für die Spalten, repeat(3, 80px) für die Zeilen.
starter_code: '/* Das Eiswürfelfach */

  '
---

Pits Eiswürfelfach: vier Spalten, drei Reihen, jedes Fach 80 mal 80 Pixel.

## Vorgaben

- Klasse `fach`: Raster mit vier Spalten und drei Zeilen zu je `80px`, Lücke `8px`, Polster `8px`, Breite `344px`, Hintergrund `#38bdf8`, Eckenradius `12px`
- Fächer (`.fach div`): Hintergrund `#e3f1f8`, Eckenradius `8px`

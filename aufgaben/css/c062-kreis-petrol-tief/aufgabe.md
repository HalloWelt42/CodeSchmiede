---
schema_version: 1
id: c062-kreis-petrol-tief
revision: 1
titel: "Kreis petrol-tief"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [border-radius, kreis, farbe]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="kreis"></div>
ziel_css: |
  .kreis {
    width: 80px;
    height: 80px;
    background-color: #2dd4bf;
    border-radius: 50%;
  }
asserts:
  - selector: ".kreis"
    property: width
    expected: "80px"
  - selector: ".kreis"
    property: height
    expected: "80px"
  - selector: ".kreis"
    property: background-color
    expected: "rgb(45, 212, 191)"
  - selector: ".kreis"
    property: border-radius
    expected: "50%"
hints:
  - kosten: 0
    text: |
      80x80 px, `border-radius: 50%`, Hintergrund #2dd4bf.
starter_code: |
  .kreis {
    /* ... */
  }
---

# Kreis petrol-tief

Mache einen 80px-Kreis mit Hintergrundfarbe #2dd4bf.

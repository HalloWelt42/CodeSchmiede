---
schema_version: 1
id: c064-kreis-sand
revision: 1
titel: "Kreis sand"
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
    background-color: #fbbf24;
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
    expected: "rgb(251, 191, 36)"
  - selector: ".kreis"
    property: border-radius
    expected: "50%"
hints:
  - kosten: 0
    text: |
      80x80 px, `border-radius: 50%`, Hintergrund #fbbf24.
starter_code: |
  .kreis {
    /* ... */
  }
---

# Kreis sand

Mache einen 80px-Kreis mit Hintergrundfarbe #fbbf24.

---
schema_version: 1
id: c005-bg-orange
revision: 1
titel: "Hintergrund Orange"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags: [background, farbe, box-modell]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="box"></div>
ziel_css: |
  .box {
    width: 200px;
    height: 100px;
    background-color: #fb923c;
  }
asserts:
  - selector: ".box"
    property: background-color
    expected: "rgb(251, 146, 60)"
  - selector: ".box"
    property: width
    expected: "200px"
  - selector: ".box"
    property: height
    expected: "100px"
hints:
  - kosten: 0
    text: |
      Setze `background-color` auf den Orange-Ton.
      Box ist 200 x 100 px.
  - kosten: 2
    text: |
      Hex #fb923c -- der Browser liefert spaeter `rgb(251, 146, 60)`.
starter_code: |
  .box {
    /* ... */
  }
---

# Hintergrund Orange

Die `.box` soll 200 x 100 px gross sein und einen Orange-Hintergrund
(#fb923c) bekommen.

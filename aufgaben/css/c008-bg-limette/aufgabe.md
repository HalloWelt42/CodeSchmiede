---
schema_version: 1
id: c008-bg-limette
revision: 1
titel: "Hintergrund Limette"
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
    background-color: #a3e635;
  }
asserts:
  - selector: ".box"
    property: background-color
    expected: "rgb(163, 230, 53)"
  - selector: ".box"
    property: width
    expected: "200px"
  - selector: ".box"
    property: height
    expected: "100px"
hints:
  - kosten: 0
    text: |
      Setze `background-color` auf den Limette-Ton.
      Box ist 200 x 100 px.
  - kosten: 2
    text: |
      Hex #a3e635 -- der Browser liefert spaeter `rgb(163, 230, 53)`.
starter_code: |
  .box {
    /* ... */
  }
---

# Hintergrund Limette

Die `.box` soll 200 x 100 px gross sein und einen Limette-Hintergrund
(#a3e635) bekommen.

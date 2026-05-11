---
schema_version: 1
id: c006-bg-rot
revision: 1
titel: "Hintergrund Rot"
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
    background-color: #ef4444;
  }
asserts:
  - selector: ".box"
    property: background-color
    expected: "rgb(239, 68, 68)"
  - selector: ".box"
    property: width
    expected: "200px"
  - selector: ".box"
    property: height
    expected: "100px"
hints:
  - kosten: 0
    text: |
      Setze `background-color` auf den Rot-Ton.
      Box ist 200 x 100 px.
  - kosten: 2
    text: |
      Hex #ef4444 -- der Browser liefert spaeter `rgb(239, 68, 68)`.
starter_code: |
  .box {
    /* ... */
  }
---

# Hintergrund Rot

Die `.box` soll 200 x 100 px gross sein und einen Rot-Hintergrund
(#ef4444) bekommen.

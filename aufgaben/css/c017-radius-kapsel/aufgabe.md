---
schema_version: 1
id: c017-radius-kapsel
revision: 1
titel: "Border-Radius Pille (999px)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [border-radius, box-modell]
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
    height: 60px;
    background-color: #2dd4bf;
    border-radius: 999px;
  }
asserts:
  - selector: ".box"
    property: border-radius
    expected: "999px"
  - selector: ".box"
    property: width
    expected: "200px"
  - selector: ".box"
    property: height
    expected: "60px"
hints:
  - kosten: 0
    text: |
      `border-radius: 999px` macht den gewuenschten Effekt.
  - kosten: 2
    text: |
      Bei Prozent: 50% bei einer quadratischen Box ergibt einen Kreis.
starter_code: |
  .box {
    /* ... */
  }
---

# Border-Radius Pille (999px)

Setze `border-radius` so, dass Pille (999px) entsteht.
Die Box ist 200px x 60px px, Petrol-Hintergrund.

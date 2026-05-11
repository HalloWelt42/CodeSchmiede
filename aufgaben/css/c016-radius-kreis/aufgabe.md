---
schema_version: 1
id: c016-radius-kreis
revision: 1
titel: "Border-Radius perfekter Kreis (50%)"
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
    width: 100px;
    height: 100px;
    background-color: #2dd4bf;
    border-radius: 50%;
  }
asserts:
  - selector: ".box"
    property: border-radius
    expected: "50%"
  - selector: ".box"
    property: width
    expected: "100px"
  - selector: ".box"
    property: height
    expected: "100px"
hints:
  - kosten: 0
    text: |
      `border-radius: 50%` macht den gewuenschten Effekt.
  - kosten: 2
    text: |
      Bei Prozent: 50% bei einer quadratischen Box ergibt einen Kreis.
starter_code: |
  .box {
    /* ... */
  }
---

# Border-Radius perfekter Kreis (50%)

Setze `border-radius` so, dass perfekter Kreis (50%) entsteht.
Die Box ist 100px x 100px px, Petrol-Hintergrund.

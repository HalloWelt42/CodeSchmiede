---
schema_version: 1
id: c022-schmal
revision: 1
titel: "Box schmal 40x200"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags: [width, height, box-modell]
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
    width: 40px;
    height: 200px;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".box"
    property: width
    expected: "40px"
  - selector: ".box"
    property: height
    expected: "200px"
hints:
  - kosten: 0
    text: |
      Setze `width: 40px` und `height: 200px` auf der Box.
starter_code: |
  .box {
    /* ... */
  }
---

# Box schmal 40x200

Setze die Box auf 40px breit und 200px hoch.

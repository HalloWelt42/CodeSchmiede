---
schema_version: 1
id: c019-fest-200
revision: 1
titel: "Box fest 200x150"
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
    width: 200px;
    height: 150px;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".box"
    property: width
    expected: "200px"
  - selector: ".box"
    property: height
    expected: "150px"
hints:
  - kosten: 0
    text: |
      Setze `width: 200px` und `height: 150px` auf der Box.
starter_code: |
  .box {
    /* ... */
  }
---

# Box fest 200x150

Setze die Box auf 200px breit und 150px hoch.

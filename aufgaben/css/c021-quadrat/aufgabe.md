---
schema_version: 1
id: c021-quadrat
revision: 1
titel: "Box quadratisch 120"
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
    width: 120px;
    height: 120px;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".box"
    property: width
    expected: "120px"
  - selector: ".box"
    property: height
    expected: "120px"
hints:
  - kosten: 0
    text: |
      Setze `width: 120px` und `height: 120px` auf der Box.
starter_code: |
  .box {
    /* ... */
  }
---

# Box quadratisch 120

Setze die Box auf 120px breit und 120px hoch.

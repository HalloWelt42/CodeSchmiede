---
schema_version: 1
id: c020-fest-300
revision: 1
titel: "Box fest 300x80"
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
    width: 300px;
    height: 80px;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".box"
    property: width
    expected: "300px"
  - selector: ".box"
    property: height
    expected: "80px"
hints:
  - kosten: 0
    text: |
      Setze `width: 300px` und `height: 80px` auf der Box.
starter_code: |
  .box {
    /* ... */
  }
---

# Box fest 300x80

Setze die Box auf 300px breit und 80px hoch.

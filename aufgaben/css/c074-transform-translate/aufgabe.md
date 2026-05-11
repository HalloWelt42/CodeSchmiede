---
schema_version: 1
id: c074-transform-translate
revision: 1
titel: "Transform: verschoben (10,20)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [transform, animation]
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
    transform: translate(10px, 20px);
  }
asserts:
  - selector: ".box"
    property: transform
    expected: "matrix(1, 0, 0, 1, 10, 20)"
hints:
  - kosten: 0
    text: |
      Setze: `transform: translate(10px, 20px);`.
starter_code: |
  .box {
    /* ... */
  }
---

# Transform: verschoben (10,20)

Wende auf die Box folgende Transformation an: verschoben (10,20).

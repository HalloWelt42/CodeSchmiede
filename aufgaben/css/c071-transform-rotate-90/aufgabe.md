---
schema_version: 1
id: c071-transform-rotate-90
revision: 1
titel: "Transform: Rotation 90°"
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
    transform: rotate(90deg);
  }
asserts:
  - selector: ".box"
    property: transform
    expected: "matrix(0, 1, -1, 0, 0, 0)"
hints:
  - kosten: 0
    text: |
      Setze: `transform: rotate(90deg);`.
starter_code: |
  .box {
    /* ... */
  }
---

# Transform: Rotation 90°

Wende auf die Box folgende Transformation an: Rotation 90°.

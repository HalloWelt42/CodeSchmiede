---
schema_version: 1
id: c072-transform-scale-2
revision: 1
titel: "Transform: doppelte Größe"
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
    transform: scale(2);
  }
asserts:
  - selector: ".box"
    property: transform
    expected: "matrix(2, 0, 0, 2, 0, 0)"
hints:
  - kosten: 0
    text: |
      Setze: `transform: scale(2);`.
starter_code: |
  .box {
    /* ... */
  }
---

# Transform: doppelte Größe

Wende auf die Box folgende Transformation an: doppelte Größe.

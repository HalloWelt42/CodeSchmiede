---
schema_version: 1
id: c069-position-sticky
revision: 1
titel: "Position: sticky"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [position, layout]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="rahmen" style="position: relative; width: 300px; height: 200px; background: #22262d;"><div class="box"></div></div>
ziel_css: |
  .box {
    position: sticky;
    width: 100px;
    height: 100px;
    top: 10px;
    left: 20px;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".box"
    property: position
    expected: "sticky"
  - selector: ".box"
    property: top
    expected: "10px"
  - selector: ".box"
    property: left
    expected: "20px"
hints:
  - kosten: 0
    text: |
      `position: sticky` plus `top: 10px` und `left: 20px`.
starter_code: |
  .box {
    /* ... */
  }
---

# Position: sticky

Box ist sticky positioniert mit top:10 left:20.

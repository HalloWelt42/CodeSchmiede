---
schema_version: 1
id: c178-shadow-klein
revision: 1
titel: "Box-Shadow: kleiner Schatten"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [box-shadow, schatten]
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
    height: 100px;
    background-color: #22262d;
    border-radius: 6px;
    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.3);
  }
asserts:
  - selector: ".box"
    property: box-shadow
    expected: "rgba(0, 0, 0, 0.3) 0px 1px 3px 0px"
hints:
  - kosten: 0
    text: |
      `box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.3);`.
starter_code: |
  .box {
    /* ... */
  }
---

# Box-Shadow: kleiner Schatten

Gib der Box einen kleiner Schatten.

---
schema_version: 1
id: c180-shadow-gross
revision: 1
titel: "Box-Shadow: großer Schatten"
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
    box-shadow: 0px 12px 32px rgba(0, 0, 0, 0.5);
  }
asserts:
  - selector: ".box"
    property: box-shadow
    expected: "rgba(0, 0, 0, 0.5) 0px 12px 32px 0px"
hints:
  - kosten: 0
    text: |
      `box-shadow: 0px 12px 32px rgba(0, 0, 0, 0.5);`.
starter_code: |
  .box {
    /* ... */
  }
---

# Box-Shadow: großer Schatten

Gib der Box einen großer Schatten.

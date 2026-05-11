---
schema_version: 1
id: c195-margin-drei-werte
revision: 1
titel: "Margin: 3 Werte 4/8/16"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [margin, box-modell]
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
    margin: 4px 8px 16px;
    width: 160px;
    height: 60px;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".box"
    property: margin-top
    expected: "4px"
  - selector: ".box"
    property: margin-right
    expected: "8px"
  - selector: ".box"
    property: margin-bottom
    expected: "16px"
  - selector: ".box"
    property: margin-left
    expected: "8px"
hints:
  - kosten: 0
    text: |
      `margin: 4px 8px 16px;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Margin: 3 Werte 4/8/16

Setze: 3 Werte 4/8/16.

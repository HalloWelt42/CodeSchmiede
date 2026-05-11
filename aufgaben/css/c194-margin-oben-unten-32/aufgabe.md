---
schema_version: 1
id: c194-margin-oben-unten-32
revision: 1
titel: "Margin: oben/unten 32, sonst 0"
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
    margin: 32px 0;
    width: 160px;
    height: 60px;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".box"
    property: margin-top
    expected: "32px"
  - selector: ".box"
    property: margin-left
    expected: "0px"
hints:
  - kosten: 0
    text: |
      `margin: 32px 0;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Margin: oben/unten 32, sonst 0

Setze: oben/unten 32, sonst 0.

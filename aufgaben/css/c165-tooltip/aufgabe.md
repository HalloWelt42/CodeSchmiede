---
schema_version: 1
id: c165-tooltip
revision: 1
titel: "Tooltip-Bubble (statisch)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [tooltip, bubble, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="tip">Hilfetext hier</div>
ziel_css: |
  .tip {
    display: inline-block;
    padding: 6px 10px;
    background-color: #1a1d23;
    color: #e7ecf1;
    font-size: 12px;
    border-radius: 4px;
    border: 1px solid #2dd4bf;
  }
asserts:
  - selector: ".tip"
    property: display
    expected: "inline-block"
  - selector: ".tip"
    property: padding-top
    expected: "6px"
  - selector: ".tip"
    property: background-color
    expected: "rgb(26, 29, 35)"
  - selector: ".tip"
    property: border-top-color
    expected: "rgb(45, 212, 191)"
  - selector: ".tip"
    property: border-radius
    expected: "4px"
hints:
  - kosten: 0
    text: |
      inline-block, kleines Padding, dunkler Hintergrund, Petrol-Rand.
starter_code: |
  .tip {
    /* ... */
  }
---

# Tooltip-Bubble

Kleine Sprechblase als Tooltip.

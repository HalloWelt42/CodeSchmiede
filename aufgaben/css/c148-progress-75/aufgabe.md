---
schema_version: 1
id: c148-progress-75
revision: 1
titel: "Progress: 75%"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [progress-bar, fortschritt, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="bar"><div class="fortschritt"></div></div>
ziel_css: |
  .bar {
    width: 300px;
    height: 8px;
    background-color: #22262d;
    border-radius: 4px;
    overflow: hidden;
  }
  .fortschritt {
    width: 75%;
    height: 100%;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".bar"
    property: width
    expected: "300px"
  - selector: ".bar"
    property: height
    expected: "8px"
  - selector: ".bar"
    property: border-radius
    expected: "4px"
  - selector: ".bar"
    property: overflow
    expected: "hidden"
  - selector: ".fortschritt"
    property: width
    expected: "225px"
  - selector: ".fortschritt"
    property: background-color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      Innen-Element width: 75%, sonst Petrol.
starter_code: |
  .bar {
    /* ... */
  }
  .fortschritt {
    /* ... */
  }
---

# Progress: 75%

Fortschrittsbalken bei 75% Füllung.

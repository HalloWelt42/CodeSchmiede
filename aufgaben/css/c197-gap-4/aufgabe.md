---
schema_version: 1
id: c197-gap-4
revision: 1
titel: "Gap: 4px"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags: [gap, flexbox]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="rahmen"><div class="kind"></div><div class="kind"></div><div class="kind"></div></div>
ziel_css: |
  .rahmen {
    display: flex;
    gap: 4px;
    padding: 8px;
    width: 320px;
    background-color: #22262d;
  }
  .kind {
    width: 40px;
    height: 40px;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".rahmen"
    property: display
    expected: "flex"
  - selector: ".rahmen"
    property: gap
    expected: "4px"
hints:
  - kosten: 0
    text: |
      `gap: 4px` zwischen den Flex-Kindern.
starter_code: |
  .rahmen {
    /* ... */
  }
  .kind {
    /* ... */
  }
---

# Gap: 4px

3 Quadrate mit 4px Abstand in einer Reihe.

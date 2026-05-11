---
schema_version: 1
id: c116-grid-col-span-2
revision: 1
titel: "Grid-Zelle: Spalte spannt 2"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [grid, span]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="grid"><div class="gross"></div><div class="klein"></div><div class="klein"></div><div class="klein"></div></div>
ziel_css: |
  .grid {
    display: grid;
    grid-template-columns: 80px 80px 80px;
    grid-template-rows: 60px 60px;
    gap: 8px;
  }
  .gross {
    background-color: #2dd4bf;
    grid-column: span 2;
  }
  .klein {
    background-color: #22262d;
  }
asserts:
  - selector: ".gross"
    property: grid-column-start
    expected: "span 2"
  - selector: ".gross"
    property: grid-column-end
    expected: "auto"
hints:
  - kosten: 0
    text: |
      `grid-column: span 2;`.
starter_code: |
  .grid {
    /* ... */
  }
  .gross {
    /* ... */
  }
  .klein {
    /* ... */
  }
---

# Grid-Zelle: Spalte spannt 2

Die .gross-Zelle soll Spalte spannt 2.

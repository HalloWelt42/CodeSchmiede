---
schema_version: 1
id: c038-grid-auto-1fr
revision: 1
titel: "Grid: fest links, rest rechts"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [grid, layout]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="grid"><div class="zelle"></div><div class="zelle"></div></div>
ziel_css: |
  .grid {
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 0px;
    width: 400px;
  }
  .zelle {
    background-color: #2dd4bf;
    height: 60px;
  }
asserts:
  - selector: ".grid"
    property: display
    expected: "grid"
  - selector: ".grid"
    property: grid-template-columns
    expected: "120px 280px"
  - selector: ".grid"
    property: gap
    expected: "0px"
  - selector: ".grid"
    property: width
    expected: "400px"
hints:
  - kosten: 0
    text: |
      `display: grid` plus `grid-template-columns: 120px 1fr`.
  - kosten: 3
    text: |
      Container ist 400px breit, gap 0px.
starter_code: |
  .grid {
    /* ... */
  }
  .zelle {
    /* ... */
  }
---

# Grid: fest links, rest rechts

Erstelle ein CSS-Grid mit fest links, rest rechts.
Container: 400px breit. Zellen sind 60px hoch und petrol.

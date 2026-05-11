---
schema_version: 1
id: c040-grid-viertel-rest
revision: 1
titel: "Grid: Viertel + Rest"
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
    grid-template-columns: 1fr 3fr;
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
    expected: "100px 300px"
  - selector: ".grid"
    property: gap
    expected: "0px"
  - selector: ".grid"
    property: width
    expected: "400px"
hints:
  - kosten: 0
    text: |
      `display: grid` plus `grid-template-columns: 1fr 3fr`.
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

# Grid: Viertel + Rest

Erstelle ein CSS-Grid mit Viertel + Rest.
Container: 400px breit. Zellen sind 60px hoch und petrol.

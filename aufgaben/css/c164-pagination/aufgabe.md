---
schema_version: 1
id: c164-pagination
revision: 1
titel: "Pagination"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [pagination, nav, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="pg"><button class="seite">1</button><button class="seite aktiv">2</button><button class="seite">3</button><button class="seite">4</button></div>
ziel_css: |
  .pg {
    display: flex;
    gap: 4px;
  }
  .seite {
    width: 32px;
    height: 32px;
    background-color: #22262d;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    border-radius: 4px;
    cursor: pointer;
  }
  .aktiv {
    background-color: #2dd4bf;
    color: #1a1d23;
    border-color: #2dd4bf;
    font-weight: 700;
  }
asserts:
  - selector: ".pg"
    property: display
    expected: "flex"
  - selector: ".pg"
    property: gap
    expected: "4px"
  - selector: ".seite"
    property: width
    expected: "32px"
  - selector: ".seite"
    property: border-radius
    expected: "4px"
  - selector: ".aktiv"
    property: background-color
    expected: "rgb(45, 212, 191)"
  - selector: ".aktiv"
    property: font-weight
    expected: "700"
hints:
  - kosten: 0
    text: |
      Flex-Reihe mit 32x32 Buttons, aktive Seite in Petrol.
starter_code: |
  .pg {
    /* ... */
  }
  .seite {
    /* ... */
  }
  .aktiv {
    /* ... */
  }
---

# Pagination

Seiten-Navigation mit hervorgehobener aktiver Seite.

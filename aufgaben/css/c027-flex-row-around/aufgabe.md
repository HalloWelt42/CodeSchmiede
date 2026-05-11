---
schema_version: 1
id: c027-flex-row-around
revision: 1
titel: "Flex: Abstand drumherum"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [flexbox, layout]
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
    width: 400px;
    height: 120px;
    background-color: #22262d;
    display: flex;
    justify-content: space-around;
    align-items: stretch;
  }
  .kind {
    width: 60px;
    height: 60px;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".rahmen"
    property: display
    expected: "flex"
  - selector: ".rahmen"
    property: justify-content
    expected: "space-around"
  - selector: ".rahmen"
    property: align-items
    expected: "stretch"
  - selector: ".kind"
    property: width
    expected: "60px"
hints:
  - kosten: 0
    text: |
      Auf dem Container `.rahmen`: `display: flex`, dann
      `justify-content: space-around` und `align-items: stretch`.
starter_code: |
  .rahmen {
    /* ... */
  }
  .kind {
    /* ... */
  }
---

# Flex: Abstand drumherum

Drei Petrol-Quadrate sollen im Container so angeordnet werden:
**Abstand drumherum**.

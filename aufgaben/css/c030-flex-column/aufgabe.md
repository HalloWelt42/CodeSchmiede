---
schema_version: 1
id: c030-flex-column
revision: 1
titel: "Flex: vertikale Spalte"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [flexbox, column]
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
    width: 200px;
    background-color: #22262d;
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 12px;
  }
  .kind {
    height: 40px;
    background-color: #2dd4bf;
  }
asserts:
  - selector: ".rahmen"
    property: display
    expected: "flex"
  - selector: ".rahmen"
    property: flex-direction
    expected: "column"
  - selector: ".rahmen"
    property: gap
    expected: "8px"
  - selector: ".rahmen"
    property: padding-top
    expected: "12px"
hints:
  - kosten: 0
    text: |
      `flex-direction: column` stapelt vertikal. `gap: 8px` setzt den Abstand.
starter_code: |
  .rahmen {
    /* ... */
  }
  .kind {
    /* ... */
  }
---

# Flex: vertikale Spalte

Drei Kinder sollen vertikal mit 8px Abstand und 12px Innenabstand angeordnet sein.

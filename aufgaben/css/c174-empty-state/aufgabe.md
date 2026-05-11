---
schema_version: 1
id: c174-empty-state
revision: 1
titel: "Empty-State (Platzhalter)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [empty-state, platzhalter, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="leer"><div class="symbol">∅</div><div class="text">Noch keine Daten</div></div>
ziel_css: |
  .leer {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 32px;
    color: #9ca3af;
    text-align: center;
    gap: 12px;
  }
  .symbol {
    font-size: 48px;
    color: #3a4049;
  }
  .text {
    font-size: 14px;
  }
asserts:
  - selector: ".leer"
    property: display
    expected: "flex"
  - selector: ".leer"
    property: flex-direction
    expected: "column"
  - selector: ".leer"
    property: align-items
    expected: "center"
  - selector: ".leer"
    property: gap
    expected: "12px"
  - selector: ".leer"
    property: padding-top
    expected: "32px"
  - selector: ".symbol"
    property: color
    expected: "rgb(58, 64, 73)"
hints:
  - kosten: 0
    text: |
      flex-column zentriert mit Symbol oben und Text darunter.
starter_code: |
  .leer {
    /* ... */
  }
  .symbol {
    /* ... */
  }
  .text {
    /* ... */
  }
---

# Empty-State

Freundlicher Platzhalter für leere Listen.

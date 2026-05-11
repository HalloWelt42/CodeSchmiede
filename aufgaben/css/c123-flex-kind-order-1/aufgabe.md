---
schema_version: 1
id: c123-flex-kind-order-1
revision: 1
titel: "Flex-Kind: Reihenfolge 1"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [flexbox, flex-grow, flex-shrink, order]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="rahmen"><div class="kind"></div><div class="kind markiert"></div><div class="kind"></div></div>
ziel_css: |
  .rahmen {
    display: flex;
    width: 300px;
    background-color: #22262d;
    padding: 8px;
  }
  .kind {
    height: 40px;
    background-color: #2dd4bf;
    margin: 4px;
  }
  .markiert {
    order: 1;
  }
asserts:
  - selector: ".markiert"
    property: order
    expected: "1"
hints:
  - kosten: 0
    text: |
      Auf dem Flex-Kind: `order: 1;`.
starter_code: |
  .rahmen {
    /* ... */
  }
  .kind {
    /* ... */
  }
  .markiert {
    /* ... */
  }
---

# Flex-Kind: Reihenfolge 1

Das markierte Kind soll: Reihenfolge 1.

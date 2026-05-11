---
schema_version: 1
id: c122-flex-kind-basis-100
revision: 1
titel: "Flex-Kind: Basis 100px"
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
    flex-basis: 100px;
  }
asserts:
  - selector: ".markiert"
    property: flex-basis
    expected: "100px"
hints:
  - kosten: 0
    text: |
      Auf dem Flex-Kind: `flex-basis: 100px;`.
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

# Flex-Kind: Basis 100px

Das markierte Kind soll: Basis 100px.

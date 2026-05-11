---
schema_version: 1
id: c121-flex-kind-shrink-0
revision: 1
titel: "Flex-Kind: schrumpft nicht"
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
    flex-shrink: 0;
  }
asserts:
  - selector: ".markiert"
    property: flex-shrink
    expected: "0"
hints:
  - kosten: 0
    text: |
      Auf dem Flex-Kind: `flex-shrink: 0;`.
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

# Flex-Kind: schrumpft nicht

Das markierte Kind soll: schrumpft nicht.

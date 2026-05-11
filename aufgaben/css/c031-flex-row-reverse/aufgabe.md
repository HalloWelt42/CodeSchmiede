---
schema_version: 1
id: c031-flex-row-reverse
revision: 1
titel: "Flex: row-reverse"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [flexbox, reverse]
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
    background-color: #22262d;
    display: flex;
    flex-direction: row-reverse;
    gap: 8px;
    padding: 12px;
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
    property: flex-direction
    expected: "row-reverse"
hints:
  - kosten: 0
    text: |
      `flex-direction: row-reverse` kehrt die Reihenfolge um.
starter_code: |
  .rahmen {
    /* ... */
  }
  .kind {
    /* ... */
  }
---

# Flex: row-reverse

Die Kinder sollen in umgekehrter Reihenfolge erscheinen (DOM A,B,C -> visuell C,B,A).

---
schema_version: 1
id: c046-typo-letter-2
revision: 1
titel: "Typo: Buchstaben 2px Abstand"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags: [typography, schrift]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="text">Hallo Welt</div>
ziel_css: |
  .text {
    width: 300px;
    padding: 16px;
    background-color: #22262d;
    color: #e7ecf1;
    letter-spacing: 2px;
  }
asserts:
  - selector: ".text"
    property: letter-spacing
    expected: "2px"
hints:
  - kosten: 0
    text: |
      Setze `letter-spacing: 2px;`.
starter_code: |
  .text {
    /* ... */
  }
---

# Typo: Buchstaben 2px Abstand

Style den Text so: Buchstaben 2px Abstand.

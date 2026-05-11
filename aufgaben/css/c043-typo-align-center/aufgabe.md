---
schema_version: 1
id: c043-typo-align-center
revision: 1
titel: "Typo: Text zentriert"
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
    text-align: center;
  }
asserts:
  - selector: ".text"
    property: text-align
    expected: "center"
hints:
  - kosten: 0
    text: |
      Setze `text-align: center;`.
starter_code: |
  .text {
    /* ... */
  }
---

# Typo: Text zentriert

Style den Text so: Text zentriert.

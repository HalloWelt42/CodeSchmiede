---
schema_version: 1
id: c044-typo-align-right
revision: 1
titel: "Typo: Text rechtsbündig"
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
    text-align: right;
  }
asserts:
  - selector: ".text"
    property: text-align
    expected: "right"
hints:
  - kosten: 0
    text: |
      Setze `text-align: right;`.
starter_code: |
  .text {
    /* ... */
  }
---

# Typo: Text rechtsbündig

Style den Text so: Text rechtsbündig.

---
schema_version: 1
id: c041-typo-weight-300
revision: 1
titel: "Typo: Schrift dünn (300)"
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
    font-weight: 300;
  }
asserts:
  - selector: ".text"
    property: font-weight
    expected: "300"
hints:
  - kosten: 0
    text: |
      Setze `font-weight: 300;`.
starter_code: |
  .text {
    /* ... */
  }
---

# Typo: Schrift dünn (300)

Style den Text so: Schrift dünn (300).

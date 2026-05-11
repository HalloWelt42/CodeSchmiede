---
schema_version: 1
id: c042-typo-weight-700
revision: 1
titel: "Typo: Schrift fett (700)"
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
    font-weight: 700;
  }
asserts:
  - selector: ".text"
    property: font-weight
    expected: "700"
hints:
  - kosten: 0
    text: |
      Setze `font-weight: 700;`.
starter_code: |
  .text {
    /* ... */
  }
---

# Typo: Schrift fett (700)

Style den Text so: Schrift fett (700).

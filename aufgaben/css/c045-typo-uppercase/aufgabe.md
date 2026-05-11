---
schema_version: 1
id: c045-typo-uppercase
revision: 1
titel: "Typo: Text in Großbuchstaben"
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
    text-transform: uppercase;
  }
asserts:
  - selector: ".text"
    property: text-transform
    expected: "uppercase"
hints:
  - kosten: 0
    text: |
      Setze `text-transform: uppercase;`.
starter_code: |
  .text {
    /* ... */
  }
---

# Typo: Text in Großbuchstaben

Style den Text so: Text in Großbuchstaben.

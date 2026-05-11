---
schema_version: 1
id: c050-display-block
revision: 1
titel: "Anzeige: block"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags: [display, opacity]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <span class="box">X</span>
ziel_css: |
  .box {
    width: 100px;
    height: 100px;
    background-color: #2dd4bf;
    display: block;
  }
asserts:
  - selector: ".box"
    property: display
    expected: "block"
hints:
  - kosten: 0
    text: |
      Setze `display: block;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Anzeige: block

Sorge dafür, dass die Box block ist.

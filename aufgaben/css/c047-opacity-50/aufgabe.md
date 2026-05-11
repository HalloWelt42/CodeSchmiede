---
schema_version: 1
id: c047-opacity-50
revision: 1
titel: "Anzeige: halbtransparent (0.5)"
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
    opacity: 0.5;
  }
asserts:
  - selector: ".box"
    property: opacity
    expected: "0.5"
hints:
  - kosten: 0
    text: |
      Setze `opacity: 0.5;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Anzeige: halbtransparent (0.5)

Sorge dafür, dass die Box halbtransparent (0.5) ist.

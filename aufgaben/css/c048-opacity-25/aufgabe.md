---
schema_version: 1
id: c048-opacity-25
revision: 1
titel: "Anzeige: stark transparent (0.25)"
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
    opacity: 0.25;
  }
asserts:
  - selector: ".box"
    property: opacity
    expected: "0.25"
hints:
  - kosten: 0
    text: |
      Setze `opacity: 0.25;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Anzeige: stark transparent (0.25)

Sorge dafür, dass die Box stark transparent (0.25) ist.

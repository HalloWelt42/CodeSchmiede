---
schema_version: 1
id: c053-border-dashed
revision: 1
titel: "Rahmen: gestrichelter Rand 2px"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [border, rahmen]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="box"></div>
ziel_css: |
  .box {
    width: 200px;
    height: 100px;
    background-color: #22262d;
    border: 2px dashed #2dd4bf;
  }
asserts:
  - selector: ".box"
    property: border-top-style
    expected: "dashed"
  - selector: ".box"
    property: border-top-width
    expected: "2px"
hints:
  - kosten: 0
    text: |
      Setze: `border: 2px dashed #2dd4bf;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Rahmen: gestrichelter Rand 2px

Gib der Box einen gestrichelter Rand 2px.

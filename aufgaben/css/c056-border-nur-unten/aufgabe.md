---
schema_version: 1
id: c056-border-nur-unten
revision: 1
titel: "Rahmen: nur unten 2px"
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
    border-bottom: 2px solid #2dd4bf;
  }
asserts:
  - selector: ".box"
    property: border-bottom-width
    expected: "2px"
  - selector: ".box"
    property: border-top-width
    expected: "0px"
hints:
  - kosten: 0
    text: |
      Setze: `border-bottom: 2px solid #2dd4bf;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Rahmen: nur unten 2px

Gib der Box einen nur unten 2px.

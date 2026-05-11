---
schema_version: 1
id: c061-margin-nur-oben
revision: 1
titel: "Margin: nur oben 32px"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags: [margin, box-modell]
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
    margin-top: 32px;
    width: 200px;
    background-color: #2dd4bf;
    height: 50px;
  }
asserts:
  - selector: ".box"
    property: margin-top
    expected: "32px"
  - selector: ".box"
    property: margin-bottom
    expected: "0px"
hints:
  - kosten: 0
    text: |
      Setze: `margin-top: 32px;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Margin: nur oben 32px

Setze den Außenabstand: nur oben 32px.

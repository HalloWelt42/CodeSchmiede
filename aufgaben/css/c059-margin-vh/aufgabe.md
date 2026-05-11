---
schema_version: 1
id: c059-margin-vh
revision: 1
titel: "Margin: vertikal 12px, horizontal 24px"
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
    margin: 12px 24px;
    width: 200px;
    background-color: #2dd4bf;
    height: 50px;
  }
asserts:
  - selector: ".box"
    property: margin-top
    expected: "12px"
  - selector: ".box"
    property: margin-left
    expected: "24px"
hints:
  - kosten: 0
    text: |
      Setze: `margin: 12px 24px;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Margin: vertikal 12px, horizontal 24px

Setze den Außenabstand: vertikal 12px, horizontal 24px.

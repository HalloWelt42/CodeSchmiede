---
schema_version: 1
id: c052-border-2px
revision: 1
titel: "Rahmen: 2px durchgezogen orange"
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
    border: 2px solid #fb923c;
  }
asserts:
  - selector: ".box"
    property: border-top-width
    expected: "2px"
  - selector: ".box"
    property: border-top-style
    expected: "solid"
  - selector: ".box"
    property: border-top-color
    expected: "rgb(251, 146, 60)"
hints:
  - kosten: 0
    text: |
      Setze: `border: 2px solid #fb923c;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Rahmen: 2px durchgezogen orange

Gib der Box einen 2px durchgezogen orange.

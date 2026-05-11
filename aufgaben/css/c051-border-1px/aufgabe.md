---
schema_version: 1
id: c051-border-1px
revision: 1
titel: "Rahmen: 1px durchgezogener Rand"
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
    border: 1px solid #2dd4bf;
  }
asserts:
  - selector: ".box"
    property: border-top-width
    expected: "1px"
  - selector: ".box"
    property: border-top-style
    expected: "solid"
  - selector: ".box"
    property: border-top-color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      Setze: `border: 1px solid #2dd4bf;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Rahmen: 1px durchgezogener Rand

Gib der Box einen 1px durchgezogener Rand.

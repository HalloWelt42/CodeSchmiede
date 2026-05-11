---
schema_version: 1
id: c018-radius-nur-oben
revision: 1
titel: "Border-Radius nur oben"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [border-radius, ecken]
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
    background-color: #2dd4bf;
    border-radius: 12px 12px 0 0;
  }
asserts:
  - selector: ".box"
    property: border-top-left-radius
    expected: "12px"
  - selector: ".box"
    property: border-top-right-radius
    expected: "12px"
  - selector: ".box"
    property: border-bottom-left-radius
    expected: "0px"
  - selector: ".box"
    property: border-bottom-right-radius
    expected: "0px"
hints:
  - kosten: 0
    text: |
      border-radius akzeptiert pro Ecke einen Wert: top-left, top-right, bottom-right, bottom-left (im Uhrzeigersinn).
  - kosten: 2
    text: |
      `border-radius: 12px 12px 0 0;` rundet nur die oberen Ecken.
starter_code: |
  .box {
    /* ... */
  }
---

# Border-Radius nur oben

Nur die oberen Ecken sollen 12px abgerundet sein, untere bleiben spitz.

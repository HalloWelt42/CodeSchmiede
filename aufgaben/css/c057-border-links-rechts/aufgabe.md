---
schema_version: 1
id: c057-border-links-rechts
revision: 1
titel: "Rahmen: links und rechts"
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
    border-left: 4px solid #fb923c;
    border-right: 4px solid #fb923c;
  }
asserts:
  - selector: ".box"
    property: border-left-width
    expected: "4px"
  - selector: ".box"
    property: border-right-width
    expected: "4px"
  - selector: ".box"
    property: border-top-width
    expected: "0px"
hints:
  - kosten: 0
    text: |
      Setze: `border-left: 4px solid #fb923c;
        border-right: 4px solid #fb923c;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Rahmen: links und rechts

Gib der Box einen links und rechts.

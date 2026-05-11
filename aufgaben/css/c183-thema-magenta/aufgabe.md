---
schema_version: 1
id: c183-thema-magenta
revision: 1
titel: "Themen-Karte: Magenta"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [karte, farbe, thema]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="karte">Magenta</div>
ziel_css: |
  .karte {
    width: 240px;
    padding: 16px;
    background-color: #d946ef;
    color: #1a1d23;
    border-radius: 6px;
    font-weight: 600;
  }
asserts:
  - selector: ".karte"
    property: background-color
    expected: "rgb(217, 70, 239)"
  - selector: ".karte"
    property: width
    expected: "240px"
  - selector: ".karte"
    property: padding-top
    expected: "16px"
  - selector: ".karte"
    property: border-radius
    expected: "6px"
  - selector: ".karte"
    property: font-weight
    expected: "600"
hints:
  - kosten: 0
    text: |
      240px breit, Padding 16px, Hintergrund #d946ef.
starter_code: |
  .karte {
    /* ... */
  }
---

# Themen-Karte: Magenta

Karte in Magenta-Hintergrund.

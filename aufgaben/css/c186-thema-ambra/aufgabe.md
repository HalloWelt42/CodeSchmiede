---
schema_version: 1
id: c186-thema-ambra
revision: 1
titel: "Themen-Karte: Ambra"
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
  <div class="karte">Ambra</div>
ziel_css: |
  .karte {
    width: 240px;
    padding: 16px;
    background-color: #f59e0b;
    color: #1a1d23;
    border-radius: 6px;
    font-weight: 600;
  }
asserts:
  - selector: ".karte"
    property: background-color
    expected: "rgb(245, 158, 11)"
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
      240px breit, Padding 16px, Hintergrund #f59e0b.
starter_code: |
  .karte {
    /* ... */
  }
---

# Themen-Karte: Ambra

Karte in Ambra-Hintergrund.

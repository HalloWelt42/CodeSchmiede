---
schema_version: 1
id: c188-thema-azur
revision: 1
titel: "Themen-Karte: Azur"
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
  <div class="karte">Azur</div>
ziel_css: |
  .karte {
    width: 240px;
    padding: 16px;
    background-color: #06b6d4;
    color: #1a1d23;
    border-radius: 6px;
    font-weight: 600;
  }
asserts:
  - selector: ".karte"
    property: background-color
    expected: "rgb(6, 182, 212)"
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
      240px breit, Padding 16px, Hintergrund #06b6d4.
starter_code: |
  .karte {
    /* ... */
  }
---

# Themen-Karte: Azur

Karte in Azur-Hintergrund.

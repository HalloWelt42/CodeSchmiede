---
schema_version: 1
id: c184-thema-indigo
revision: 1
titel: "Themen-Karte: Indigo"
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
  <div class="karte">Indigo</div>
ziel_css: |
  .karte {
    width: 240px;
    padding: 16px;
    background-color: #6366f1;
    color: #1a1d23;
    border-radius: 6px;
    font-weight: 600;
  }
asserts:
  - selector: ".karte"
    property: background-color
    expected: "rgb(99, 102, 241)"
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
      240px breit, Padding 16px, Hintergrund #6366f1.
starter_code: |
  .karte {
    /* ... */
  }
---

# Themen-Karte: Indigo

Karte in Indigo-Hintergrund.

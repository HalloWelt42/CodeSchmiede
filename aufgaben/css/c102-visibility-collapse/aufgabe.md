---
schema_version: 1
id: c102-visibility-collapse
revision: 1
titel: "Visibility: zusammen"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags: [visibility, anzeige]
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
    width: 80px;
    height: 80px;
    background-color: #2dd4bf;
    visibility: collapse;
  }
asserts:
  - selector: ".box"
    property: visibility
    expected: "collapse"
hints:
  - kosten: 0
    text: |
      `visibility: collapse`.
starter_code: |
  .box {
    /* ... */
  }
---

# Visibility: zusammen

Element soll zusammen sein (Platz bleibt erhalten).

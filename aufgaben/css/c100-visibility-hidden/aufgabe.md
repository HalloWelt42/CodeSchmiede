---
schema_version: 1
id: c100-visibility-hidden
revision: 1
titel: "Visibility: unsichtbar"
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
    visibility: hidden;
  }
asserts:
  - selector: ".box"
    property: visibility
    expected: "hidden"
hints:
  - kosten: 0
    text: |
      `visibility: hidden`.
starter_code: |
  .box {
    /* ... */
  }
---

# Visibility: unsichtbar

Element soll unsichtbar sein (Platz bleibt erhalten).

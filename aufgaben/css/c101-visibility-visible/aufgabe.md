---
schema_version: 1
id: c101-visibility-visible
revision: 1
titel: "Visibility: sichtbar"
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
    visibility: visible;
  }
asserts:
  - selector: ".box"
    property: visibility
    expected: "visible"
hints:
  - kosten: 0
    text: |
      `visibility: visible`.
starter_code: |
  .box {
    /* ... */
  }
---

# Visibility: sichtbar

Element soll sichtbar sein (Platz bleibt erhalten).

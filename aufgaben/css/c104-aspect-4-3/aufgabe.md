---
schema_version: 1
id: c104-aspect-4-3
revision: 1
titel: "Seitenverhältnis: 4:3"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [aspect-ratio, layout]
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
    background-color: #2dd4bf;
    aspect-ratio: 4 / 3;
  }
asserts:
  - selector: ".box"
    property: width
    expected: "200px"
  - selector: ".box"
    property: aspect-ratio
    expected: "4 / 3"
hints:
  - kosten: 0
    text: |
      `aspect-ratio: 4 / 3;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Seitenverhältnis: 4:3

Box 200px breit, Höhe folgt 4:3.

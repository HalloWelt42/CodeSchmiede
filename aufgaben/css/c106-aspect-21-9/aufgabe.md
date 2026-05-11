---
schema_version: 1
id: c106-aspect-21-9
revision: 1
titel: "Seitenverhältnis: 21:9 (ultrawide)"
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
    aspect-ratio: 21 / 9;
  }
asserts:
  - selector: ".box"
    property: width
    expected: "200px"
  - selector: ".box"
    property: aspect-ratio
    expected: "21 / 9"
hints:
  - kosten: 0
    text: |
      `aspect-ratio: 21 / 9;`.
starter_code: |
  .box {
    /* ... */
  }
---

# Seitenverhältnis: 21:9 (ultrawide)

Box 200px breit, Höhe folgt 21:9 (ultrawide).

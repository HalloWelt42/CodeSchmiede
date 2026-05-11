---
schema_version: 1
id: c077-zindex-5
revision: 1
titel: "z-index: 5"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [z-index, position]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="rahmen" style="position: relative; width: 200px; height: 150px; background: #22262d;"><div class="obenauf"></div></div>
ziel_css: |
  .obenauf {
    position: absolute;
    top: 20px;
    left: 20px;
    width: 80px;
    height: 80px;
    background-color: #2dd4bf;
    z-index: 5;
  }
asserts:
  - selector: ".obenauf"
    property: z-index
    expected: "5"
  - selector: ".obenauf"
    property: position
    expected: "absolute"
hints:
  - kosten: 0
    text: |
      `z-index: 5` und `position: absolute`.
starter_code: |
  .obenauf {
    /* ... */
  }
---

# z-index: 5

Element liegt auf z-index 5.

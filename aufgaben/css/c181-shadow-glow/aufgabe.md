---
schema_version: 1
id: c181-shadow-glow
revision: 1
titel: "Box-Shadow: Petrol-Glow"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [box-shadow, schatten]
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
    height: 100px;
    background-color: #22262d;
    border-radius: 6px;
    box-shadow: 0px 0px 16px rgba(45, 212, 191, 0.6);
  }
asserts:
  - selector: ".box"
    property: box-shadow
    expected: "rgba(45, 212, 191, 0.6) 0px 0px 16px 0px"
hints:
  - kosten: 0
    text: |
      `box-shadow: 0px 0px 16px rgba(45, 212, 191, 0.6);`.
starter_code: |
  .box {
    /* ... */
  }
---

# Box-Shadow: Petrol-Glow

Gib der Box einen Petrol-Glow.

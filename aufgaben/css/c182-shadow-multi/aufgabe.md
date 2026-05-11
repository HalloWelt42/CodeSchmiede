---
schema_version: 1
id: c182-shadow-multi
revision: 1
titel: "Box-Shadow: zwei Schatten"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [box-shadow, multi-shadow]
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
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.4), 0px 0px 16px rgba(45, 212, 191, 0.3);
  }
asserts:
  - selector: ".box"
    property: box-shadow
    expected: "rgba(0, 0, 0, 0.4) 0px 4px 8px 0px, rgba(45, 212, 191, 0.3) 0px 0px 16px 0px"
hints:
  - kosten: 0
    text: |
      Zwei box-shadow-Werte mit Komma trennen.
starter_code: |
  .box {
    /* ... */
  }
---

# Box-Shadow: zwei Schatten

Kombination aus normalem Schatten unten und Petrol-Glow drumherum.

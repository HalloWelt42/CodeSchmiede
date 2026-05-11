---
schema_version: 1
id: c139-card-shadow
revision: 1
titel: "Card: mit weichem Schatten"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [card, shadow, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="card">Schatten-Karte</div>
ziel_css: |
  .card {
    width: 240px;
    padding: 20px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 6px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.4);
  }
asserts:
  - selector: ".card"
    property: width
    expected: "240px"
  - selector: ".card"
    property: padding-top
    expected: "20px"
  - selector: ".card"
    property: border-radius
    expected: "6px"
  - selector: ".card"
    property: box-shadow
    expected: "rgba(0, 0, 0, 0.4) 0px 4px 12px 0px"
hints:
  - kosten: 0
    text: |
      `box-shadow: 0 4px 12px rgba(0,0,0,0.4)` für weichen Schatten.
starter_code: |
  .card {
    /* ... */
  }
---

# Card mit Schatten

240px Karte mit weichem Schatten unten.

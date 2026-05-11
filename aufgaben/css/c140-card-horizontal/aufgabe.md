---
schema_version: 1
id: c140-card-horizontal
revision: 1
titel: "Card: horizontales Layout"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [card, flexbox, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="card"><div class="bild"></div><div class="inhalt">Inhalt</div></div>
ziel_css: |
  .card {
    display: flex;
    width: 320px;
    background-color: #22262d;
    border-radius: 6px;
    overflow: hidden;
  }
  .bild {
    width: 100px;
    height: 100px;
    background-color: #2dd4bf;
    flex-shrink: 0;
  }
  .inhalt {
    flex: 1;
    padding: 16px;
    color: #e7ecf1;
  }
asserts:
  - selector: ".card"
    property: display
    expected: "flex"
  - selector: ".card"
    property: width
    expected: "320px"
  - selector: ".card"
    property: border-radius
    expected: "6px"
  - selector: ".card"
    property: overflow
    expected: "hidden"
  - selector: ".bild"
    property: width
    expected: "100px"
  - selector: ".bild"
    property: flex-shrink
    expected: "0"
hints:
  - kosten: 0
    text: |
      card als flex, bild fix 100px (flex-shrink:0), inhalt flex:1.
starter_code: |
  .card {
    /* ... */
  }
  .bild {
    /* ... */
  }
  .inhalt {
    /* ... */
  }
---

# Card: horizontales Layout

Bild links, Inhalt rechts -- per Flexbox.

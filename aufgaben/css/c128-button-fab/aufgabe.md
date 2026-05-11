---
schema_version: 1
id: c128-button-fab
revision: 1
titel: "Floating-Action-Button (Kreis)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [button, fab, kreis, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <button class="fab">+</button>
ziel_css: |
  .fab {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background-color: #2dd4bf;
    color: #1a1d23;
    border: none;
    font-size: 24px;
    font-weight: 700;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
  }
asserts:
  - selector: ".fab"
    property: width
    expected: "56px"
  - selector: ".fab"
    property: height
    expected: "56px"
  - selector: ".fab"
    property: border-radius
    expected: "50%"
  - selector: ".fab"
    property: background-color
    expected: "rgb(45, 212, 191)"
  - selector: ".fab"
    property: display
    expected: "flex"
hints:
  - kosten: 0
    text: |
      56x56, border-radius 50%, flex-zentriert.
starter_code: |
  .fab {
    /* ... */
  }
---

# FAB (Floating Action Button)

Kreisrunder Aktion-Button (Material-Stil).

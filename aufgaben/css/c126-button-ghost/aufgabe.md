---
schema_version: 1
id: c126-button-ghost
revision: 1
titel: "Button: Ghost"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [button, ghost, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <button class="btn">Mehr</button>
ziel_css: |
  .btn {
    background-color: transparent;
    border: none;
    color: #e7ecf1;
    padding: 8px 16px;
    font-weight: 500;
    cursor: pointer;
  }
asserts:
  - selector: ".btn"
    property: background-color
    expected: "rgba(0, 0, 0, 0)"
  - selector: ".btn"
    property: border-top-style
    expected: "none"
  - selector: ".btn"
    property: color
    expected: "rgb(231, 236, 241)"
  - selector: ".btn"
    property: padding-top
    expected: "8px"
  - selector: ".btn"
    property: padding-left
    expected: "16px"
  - selector: ".btn"
    property: font-weight
    expected: "500"
hints:
  - kosten: 0
    text: |
      transparenter Hintergrund, kein Border, heller Text.
starter_code: |
  .btn {
    /* ... */
  }
---

# Button: Ghost

Ghost-Button ohne sichtbaren Hintergrund und Rahmen, nur Text.

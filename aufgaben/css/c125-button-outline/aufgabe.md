---
schema_version: 1
id: c125-button-outline
revision: 1
titel: "Button: Outline"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [button, outline, border, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <button class="btn">Aktion</button>
ziel_css: |
  .btn {
    background-color: transparent;
    border: 2px solid #2dd4bf;
    color: #2dd4bf;
    padding: 8px 20px;
    border-radius: 4px;
    font-weight: 600;
    cursor: pointer;
  }
asserts:
  - selector: ".btn"
    property: background-color
    expected: "rgba(0, 0, 0, 0)"
  - selector: ".btn"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: ".btn"
    property: border-top-color
    expected: "rgb(45, 212, 191)"
  - selector: ".btn"
    property: border-top-width
    expected: "2px"
  - selector: ".btn"
    property: border-radius
    expected: "4px"
  - selector: ".btn"
    property: font-weight
    expected: "600"
hints:
  - kosten: 0
    text: |
      transparenter Hintergrund, 2px Border in Petrol, 8/20 Padding.
starter_code: |
  .btn {
    /* ... */
  }
---

# Button: Outline

Button ohne Füllfarbe, mit 2px Petrol-Rahmen und Petrol-Text.

---
schema_version: 1
id: c127-button-icon
revision: 1
titel: "Button: Icon-only quadratisch"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [button, icon, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <button class="btn">+</button>
ziel_css: |
  .btn {
    width: 40px;
    height: 40px;
    background-color: #2dd4bf;
    color: #1a1d23;
    border: none;
    border-radius: 4px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    font-weight: 700;
    cursor: pointer;
  }
asserts:
  - selector: ".btn"
    property: width
    expected: "40px"
  - selector: ".btn"
    property: height
    expected: "40px"
  - selector: ".btn"
    property: display
    expected: "flex"
  - selector: ".btn"
    property: justify-content
    expected: "center"
  - selector: ".btn"
    property: align-items
    expected: "center"
  - selector: ".btn"
    property: border-radius
    expected: "4px"
hints:
  - kosten: 0
    text: |
      40x40, flex-zentriert, Petrol-Hintergrund.
starter_code: |
  .btn {
    /* ... */
  }
---

# Button: Icon-only quadratisch

Quadratischer Icon-Button mit Inhalt mittig.

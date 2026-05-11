---
schema_version: 1
id: c159-form-checkbox
revision: 1
titel: "Form: Checkbox-Style"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [form, checkbox, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="check"></div>
ziel_css: |
  .check {
    width: 20px;
    height: 20px;
    background-color: #22262d;
    border: 2px solid #2dd4bf;
    border-radius: 4px;
  }
asserts:
  - selector: ".check"
    property: width
    expected: "20px"
  - selector: ".check"
    property: height
    expected: "20px"
  - selector: ".check"
    property: border-top-color
    expected: "rgb(45, 212, 191)"
  - selector: ".check"
    property: border-radius
    expected: "4px"
hints:
  - kosten: 0
    text: |
      20x20, 2px Petrol-Border, 4px Radius.
starter_code: |
  .check {
    /* ... */
  }
---

# Form: Checkbox-Style

Klassische Checkbox-Form (visuell, ohne Funktion).

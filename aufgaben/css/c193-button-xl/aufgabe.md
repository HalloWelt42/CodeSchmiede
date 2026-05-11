---
schema_version: 1
id: c193-button-xl
revision: 1
titel: "Button-Größe: extra groß"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [button, groesse, padding]
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
    padding: 16px 32px;
    font-size: 18px;
    background-color: #2dd4bf;
    color: #1a1d23;
    border: none;
    border-radius: 4px;
    font-weight: 600;
    cursor: pointer;
  }
asserts:
  - selector: ".btn"
    property: padding-top
    expected: "16px"
  - selector: ".btn"
    property: padding-left
    expected: "32px"
  - selector: ".btn"
    property: font-size
    expected: "18px"
  - selector: ".btn"
    property: background-color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      Padding 16px 32px, font-size 18px.
starter_code: |
  .btn {
    /* ... */
  }
---

# Button-Größe: extra groß

Button in Größe extra groß.

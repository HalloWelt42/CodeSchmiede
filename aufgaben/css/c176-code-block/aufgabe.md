---
schema_version: 1
id: c176-code-block
revision: 1
titel: "Code-Block"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [code-block, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <pre class="code">def hallo():
      return "welt"</pre>
ziel_css: |
  .code {
    margin: 0;
    padding: 16px;
    background-color: #1a1d23;
    color: #2dd4bf;
    font-family: monospace;
    border-radius: 6px;
    overflow-x: auto;
  }
asserts:
  - selector: ".code"
    property: padding-top
    expected: "16px"
  - selector: ".code"
    property: background-color
    expected: "rgb(26, 29, 35)"
  - selector: ".code"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: ".code"
    property: border-radius
    expected: "6px"
  - selector: ".code"
    property: overflow-x
    expected: "auto"
hints:
  - kosten: 0
    text: |
      Dunkler Hintergrund, Petrol-Schrift, Monospace-Font, abgerundet.
starter_code: |
  .code {
    /* ... */
  }
---

# Code-Block

Monospace-Block für Quellcode mit dunklem Hintergrund.

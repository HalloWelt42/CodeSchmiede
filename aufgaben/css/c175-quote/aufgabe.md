---
schema_version: 1
id: c175-quote
revision: 1
titel: "Quote-Block"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [quote, blockquote, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <blockquote class="zitat">Code ist Poesie.</blockquote>
ziel_css: |
  .zitat {
    margin: 0;
    padding: 12px 20px;
    border-left: 4px solid #2dd4bf;
    background-color: #22262d;
    color: #e7ecf1;
    font-style: italic;
  }
asserts:
  - selector: ".zitat"
    property: padding-top
    expected: "12px"
  - selector: ".zitat"
    property: padding-left
    expected: "20px"
  - selector: ".zitat"
    property: border-left-color
    expected: "rgb(45, 212, 191)"
  - selector: ".zitat"
    property: border-left-width
    expected: "4px"
  - selector: ".zitat"
    property: font-style
    expected: "italic"
hints:
  - kosten: 0
    text: |
      Linker Petrol-Streifen (4px), kursiver Text.
starter_code: |
  .zitat {
    /* ... */
  }
---

# Quote-Block

Zitat mit linkem Petrol-Streifen und kursivem Text.

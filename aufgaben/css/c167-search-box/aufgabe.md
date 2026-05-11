---
schema_version: 1
id: c167-search-box
revision: 1
titel: "Search-Box"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [search, form, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="suche"><input class="feld" placeholder="Suchen..."><button class="kn">Go</button></div>
ziel_css: |
  .suche {
    display: flex;
    width: 320px;
  }
  .feld {
    flex: 1;
    padding: 8px 12px;
    background-color: #22262d;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    border-right: none;
    border-radius: 4px 0 0 4px;
  }
  .kn {
    padding: 8px 16px;
    background-color: #2dd4bf;
    color: #1a1d23;
    border: none;
    border-radius: 0 4px 4px 0;
    cursor: pointer;
    font-weight: 600;
  }
asserts:
  - selector: ".suche"
    property: display
    expected: "flex"
  - selector: ".suche"
    property: width
    expected: "320px"
  - selector: ".feld"
    property: border-top-left-radius
    expected: "4px"
  - selector: ".feld"
    property: border-top-right-radius
    expected: "0px"
  - selector: ".kn"
    property: border-top-right-radius
    expected: "4px"
  - selector: ".kn"
    property: background-color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      flex-Container, Feld+Button mit asymmetrischem border-radius.
starter_code: |
  .suche {
    /* ... */
  }
  .feld {
    /* ... */
  }
  .kn {
    /* ... */
  }
---

# Search-Box

Suchfeld mit angeschlossenem Button (gemeinsame Form).

---
schema_version: 1
id: c154-nav-tabs
revision: 1
titel: "Navigation: Tab-Leiste"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [nav, tabs, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="tabs"><button class="tab aktiv">Eins</button><button class="tab">Zwei</button><button class="tab">Drei</button></div>
ziel_css: |
  .tabs {
    display: flex;
    border-bottom: 1px solid #3a4049;
  }
  .tab {
    background-color: transparent;
    border: none;
    border-bottom: 2px solid transparent;
    padding: 8px 16px;
    color: #9ca3af;
    cursor: pointer;
    font-weight: 500;
  }
  .aktiv {
    color: #2dd4bf;
    border-bottom-color: #2dd4bf;
  }
asserts:
  - selector: ".tabs"
    property: display
    expected: "flex"
  - selector: ".tab"
    property: background-color
    expected: "rgba(0, 0, 0, 0)"
  - selector: ".tab"
    property: border-bottom-width
    expected: "2px"
  - selector: ".aktiv"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: ".aktiv"
    property: border-bottom-color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      Tabs als flex, jeder Tab transparent mit 2px-Border-Bottom. Aktiver in Petrol.
starter_code: |
  .tabs {
    /* ... */
  }
  .tab {
    /* ... */
  }
  .aktiv {
    /* ... */
  }
---

# Navigation: Tab-Leiste

Horizontale Tabs mit Petrol-Unterstrich beim aktiven Tab.

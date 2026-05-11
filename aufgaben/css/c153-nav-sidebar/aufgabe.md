---
schema_version: 1
id: c153-nav-sidebar
revision: 1
titel: "Navigation: Sidebar"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [nav, sidebar, flex-column, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <aside class="sidebar"><a class="eintrag aktiv">Dashboard</a><a class="eintrag">Aufgaben</a><a class="eintrag">Pfade</a></aside>
ziel_css: |
  .sidebar {
    display: flex;
    flex-direction: column;
    width: 200px;
    padding: 16px;
    background-color: #22262d;
    gap: 4px;
    height: 300px;
  }
  .eintrag {
    padding: 8px 12px;
    color: #9ca3af;
    text-decoration: none;
    border-radius: 4px;
  }
  .aktiv {
    background-color: #2dd4bf;
    color: #1a1d23;
    font-weight: 600;
  }
asserts:
  - selector: ".sidebar"
    property: display
    expected: "flex"
  - selector: ".sidebar"
    property: flex-direction
    expected: "column"
  - selector: ".sidebar"
    property: width
    expected: "200px"
  - selector: ".sidebar"
    property: gap
    expected: "4px"
  - selector: ".aktiv"
    property: background-color
    expected: "rgb(45, 212, 191)"
  - selector: ".aktiv"
    property: font-weight
    expected: "600"
hints:
  - kosten: 0
    text: |
      Sidebar als flex-column, 200px breit. Aktiver Eintrag in Petrol.
starter_code: |
  .sidebar {
    /* ... */
  }
  .eintrag {
    /* ... */
  }
  .aktiv {
    /* ... */
  }
---

# Navigation: Sidebar

Vertikale Navigationsleiste mit hervorgehobenem aktivem Eintrag.

---
schema_version: 1
id: c152-nav-header
revision: 1
titel: "Navigation: Header-Leiste"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [nav, header, flexbox, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <header class="header"><div class="logo">Logo</div><nav class="menu"><a class="link">Home</a><a class="link">Über</a><a class="link">Kontakt</a></nav></header>
ziel_css: |
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 56px;
    padding: 0 24px;
    background-color: #22262d;
    border-bottom: 1px solid #3a4049;
  }
  .logo {
    color: #2dd4bf;
    font-weight: 700;
    font-size: 18px;
  }
  .menu {
    display: flex;
    gap: 24px;
  }
  .link {
    color: #e7ecf1;
    text-decoration: none;
    font-weight: 500;
  }
asserts:
  - selector: ".header"
    property: display
    expected: "flex"
  - selector: ".header"
    property: justify-content
    expected: "space-between"
  - selector: ".header"
    property: align-items
    expected: "center"
  - selector: ".header"
    property: height
    expected: "56px"
  - selector: ".menu"
    property: display
    expected: "flex"
  - selector: ".menu"
    property: gap
    expected: "24px"
  - selector: ".logo"
    property: color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      Header als flex space-between, 56px hoch. Menu als flex mit gap.
starter_code: |
  .header {
    /* ... */
  }
  .logo {
    /* ... */
  }
  .menu {
    /* ... */
  }
  .link {
    /* ... */
  }
---

# Navigation: Header-Leiste

Logo links, Menu rechts -- typische Top-Navigation.

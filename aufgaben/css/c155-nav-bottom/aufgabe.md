---
schema_version: 1
id: c155-nav-bottom
revision: 1
titel: "Navigation: Bottom-Bar"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [nav, bottom-bar, mobile, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <nav class="bottom"><button class="kn">A</button><button class="kn">B</button><button class="kn">C</button></nav>
ziel_css: |
  .bottom {
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 320px;
    height: 60px;
    background-color: #22262d;
    border-top: 1px solid #3a4049;
  }
  .kn {
    background-color: transparent;
    border: none;
    color: #9ca3af;
    cursor: pointer;
  }
asserts:
  - selector: ".bottom"
    property: display
    expected: "flex"
  - selector: ".bottom"
    property: justify-content
    expected: "space-around"
  - selector: ".bottom"
    property: height
    expected: "60px"
  - selector: ".bottom"
    property: border-top-width
    expected: "1px"
  - selector: ".kn"
    property: background-color
    expected: "rgba(0, 0, 0, 0)"
hints:
  - kosten: 0
    text: |
      flex space-around, 60px hoch, oben 1px Border.
starter_code: |
  .bottom {
    /* ... */
  }
  .kn {
    /* ... */
  }
---

# Navigation: Bottom-Bar

Mobile-Style Bottom-Navigation mit drei Buttons.

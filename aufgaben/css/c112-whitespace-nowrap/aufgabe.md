---
schema_version: 1
id: c112-whitespace-nowrap
revision: 1
titel: "White-Space: kein Umbruch"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [white-space, text]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="text">Ein Beispieltext mit mehreren Wörtern</div>
ziel_css: |
  .text {
    width: 200px;
    padding: 12px;
    background-color: #22262d;
    color: #e7ecf1;
    white-space: nowrap;
  }
asserts:
  - selector: ".text"
    property: white-space
    expected: "nowrap"
hints:
  - kosten: 0
    text: |
      `white-space: nowrap`.
starter_code: |
  .text {
    /* ... */
  }
---

# White-Space: kein Umbruch

Text-Umbruch: kein Umbruch.

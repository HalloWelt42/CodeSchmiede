---
schema_version: 1
id: c115-whitespace-normal
revision: 1
titel: "White-Space: normal (default)"
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
    white-space: normal;
  }
asserts:
  - selector: ".text"
    property: white-space
    expected: "normal"
hints:
  - kosten: 0
    text: |
      `white-space: normal`.
starter_code: |
  .text {
    /* ... */
  }
---

# White-Space: normal (default)

Text-Umbruch: normal (default).

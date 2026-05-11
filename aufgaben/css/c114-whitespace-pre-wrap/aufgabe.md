---
schema_version: 1
id: c114-whitespace-pre-wrap
revision: 1
titel: "White-Space: umbrechen + Whitespace"
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
    white-space: pre-wrap;
  }
asserts:
  - selector: ".text"
    property: white-space
    expected: "pre-wrap"
hints:
  - kosten: 0
    text: |
      `white-space: pre-wrap`.
starter_code: |
  .text {
    /* ... */
  }
---

# White-Space: umbrechen + Whitespace

Text-Umbruch: umbrechen + Whitespace.

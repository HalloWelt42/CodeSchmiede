---
schema_version: 1
id: c108-text-line-through
revision: 1
titel: "Text: durchgestrichen"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags: [text-decoration, schrift]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="text">Hallo Welt</div>
ziel_css: |
  .text {
    padding: 16px;
    background-color: #22262d;
    color: #2dd4bf;
    text-decoration: line-through;
  }
asserts:
  - selector: ".text"
    property: text-decoration-line
    expected: "line-through"
hints:
  - kosten: 0
    text: |
      Setze: `text-decoration: line-through;`.
starter_code: |
  .text {
    /* ... */
  }
---

# Text: durchgestrichen

Text soll durchgestrichen sein.

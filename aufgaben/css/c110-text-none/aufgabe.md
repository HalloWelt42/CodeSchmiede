---
schema_version: 1
id: c110-text-none
revision: 1
titel: "Text: ohne Dekoration"
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
    text-decoration: none;
  }
asserts:
  - selector: ".text"
    property: text-decoration-line
    expected: "none"
hints:
  - kosten: 0
    text: |
      Setze: `text-decoration: none;`.
starter_code: |
  .text {
    /* ... */
  }
---

# Text: ohne Dekoration

Text soll ohne Dekoration sein.

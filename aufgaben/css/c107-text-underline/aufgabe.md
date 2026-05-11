---
schema_version: 1
id: c107-text-underline
revision: 1
titel: "Text: unterstrichen"
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
    text-decoration: underline;
  }
asserts:
  - selector: ".text"
    property: text-decoration-line
    expected: "underline"
hints:
  - kosten: 0
    text: |
      Setze: `text-decoration: underline;`.
starter_code: |
  .text {
    /* ... */
  }
---

# Text: unterstrichen

Text soll unterstrichen sein.

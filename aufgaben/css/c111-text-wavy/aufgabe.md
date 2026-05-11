---
schema_version: 1
id: c111-text-wavy
revision: 1
titel: "Text: wellenförmig unterstrichen"
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
    text-decoration: underline wavy;
  }
asserts:
  - selector: ".text"
    property: text-decoration-line
    expected: "underline"
  - selector: ".text"
    property: text-decoration-style
    expected: "wavy"
hints:
  - kosten: 0
    text: |
      Setze: `text-decoration: underline wavy;`.
starter_code: |
  .text {
    /* ... */
  }
---

# Text: wellenförmig unterstrichen

Text soll wellenförmig unterstrichen sein.

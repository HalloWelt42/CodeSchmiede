---
schema_version: 1
id: c087-cursor-wait
revision: 1
titel: "Cursor: warten (Sanduhr)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags: [cursor, ux]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="kn">Hover</div>
ziel_css: |
  .kn {
    width: 120px;
    height: 40px;
    background-color: #2dd4bf;
    cursor: wait;
  }
asserts:
  - selector: ".kn"
    property: cursor
    expected: "wait"
hints:
  - kosten: 0
    text: |
      `cursor: wait`.
starter_code: |
  .kn {
    /* ... */
  }
---

# Cursor: warten (Sanduhr)

Über dem Element soll der warten (Sanduhr)-Cursor erscheinen.

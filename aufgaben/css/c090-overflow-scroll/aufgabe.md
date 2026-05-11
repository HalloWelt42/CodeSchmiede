---
schema_version: 1
id: c090-overflow-scroll
revision: 1
titel: "Overflow: immer scrollen"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags: [overflow, layout]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="rahmen">Ein langer Text, der definitiv nicht in die Box passt und somit das Overflow-Verhalten zeigt.</div>
ziel_css: |
  .rahmen {
    width: 200px;
    height: 80px;
    background-color: #22262d;
    color: #e7ecf1;
    overflow: scroll;
  }
asserts:
  - selector: ".rahmen"
    property: overflow
    expected: "scroll"
hints:
  - kosten: 0
    text: |
      `overflow: scroll`.
starter_code: |
  .rahmen {
    /* ... */
  }
---

# Overflow: immer scrollen

Überlaufender Inhalt soll immer scrollen.

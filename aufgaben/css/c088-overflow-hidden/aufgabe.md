---
schema_version: 1
id: c088-overflow-hidden
revision: 1
titel: "Overflow: verstecken"
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
    overflow: hidden;
  }
asserts:
  - selector: ".rahmen"
    property: overflow
    expected: "hidden"
hints:
  - kosten: 0
    text: |
      `overflow: hidden`.
starter_code: |
  .rahmen {
    /* ... */
  }
---

# Overflow: verstecken

Überlaufender Inhalt soll verstecken.

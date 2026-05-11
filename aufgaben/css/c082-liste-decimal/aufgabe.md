---
schema_version: 1
id: c082-liste-decimal
revision: 1
titel: "Liste: mit Zahlen"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags: [liste, list-style]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <ul class="liste"><li>Eins</li><li>Zwei</li><li>Drei</li></ul>
ziel_css: |
  .liste {
    padding: 16px;
    background-color: #22262d;
    color: #e7ecf1;
    list-style-type: decimal;
  }
asserts:
  - selector: ".liste"
    property: list-style-type
    expected: "decimal"
hints:
  - kosten: 0
    text: |
      Setze: `list-style-type: decimal;`.
starter_code: |
  .liste {
    /* ... */
  }
---

# Liste: mit Zahlen

Formatiere die Liste mit Zahlen.

---
schema_version: 1
id: c083-liste-circle
revision: 1
titel: "Liste: mit Kreisen"
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
    list-style-type: circle;
  }
asserts:
  - selector: ".liste"
    property: list-style-type
    expected: "circle"
hints:
  - kosten: 0
    text: |
      Setze: `list-style-type: circle;`.
starter_code: |
  .liste {
    /* ... */
  }
---

# Liste: mit Kreisen

Formatiere die Liste mit Kreisen.

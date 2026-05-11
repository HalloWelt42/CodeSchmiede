---
schema_version: 1
id: c080-liste-none
revision: 1
titel: "Liste: ohne Aufzaehlungszeichen"
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
    list-style: none;
  }
asserts:
  - selector: ".liste"
    property: list-style-type
    expected: "none"
hints:
  - kosten: 0
    text: |
      Setze: `list-style: none;`.
starter_code: |
  .liste {
    /* ... */
  }
---

# Liste: ohne Aufzaehlungszeichen

Formatiere die Liste ohne Aufzaehlungszeichen.

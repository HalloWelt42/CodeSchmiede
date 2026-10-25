---
schema_version: 1
id: c129-button-block
revision: 3
titel: "Button: volle Breite"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [button, block, width-100]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <button class="btn">Bestätigen</button>
ziel_css: |
  .btn {
    display: block;
    width: 100%;
    background-color: #fa8072;
    color: #1a1d23;
    padding: 12px;
    border: none;
    border-radius: 4px;
    font-weight: 600;
    cursor: pointer;
  }
hints:
  - kosten: 0
    text: |
      display: block, width: 100% nimmt komplette Eltern-Breite ein.
starter_code: |
  .btn {
    /* ... */
  }
---

# Button: volle Breite

Block-Button auf voller Container-Breite.

---
schema_version: 1
id: c126-button-ghost
revision: 3
titel: "Button: Ghost"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [button, ghost, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <button class="btn">Mehr</button>
ziel_css: |
  .btn {
    background-color: transparent;
    border: none;
    color: #e7ecf1;
    padding: 8px 16px;
    font-weight: 500;
    cursor: pointer;
  }
hints:
  - kosten: 0
    text: |
      transparenter Hintergrund, kein Border, heller Text.
starter_code: |
  .btn {
    /* ... */
  }
---

# Button: Ghost

Ghost-Button ohne sichtbaren Hintergrund und Rahmen, nur Text.

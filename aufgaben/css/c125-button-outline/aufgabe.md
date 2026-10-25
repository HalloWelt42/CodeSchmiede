---
schema_version: 1
id: c125-button-outline
revision: 3
titel: "Button: Outline"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [button, outline, border, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <button class="btn">Aktion</button>
ziel_css: |
  .btn {
    background-color: transparent;
    border: 2px solid #fbbf24;
    color: #fbbf24;
    padding: 8px 20px;
    border-radius: 4px;
    font-weight: 600;
    cursor: pointer;
  }
hints:
  - kosten: 0
    text: |
      transparenter Hintergrund, 2px Border in Gold, 8/20 Padding.
starter_code: |
  .btn {
    /* ... */
  }
---

# Button: Outline

Button ohne Füllfarbe, mit 2px Gold-Rahmen und Gold-Text.

---
schema_version: 1
id: c166-chat-bubble
revision: 3
titel: "Chat-Bubble (eigene Nachricht)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [chat, bubble, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="bubble">Hallo!</div>
ziel_css: |
  .bubble {
    display: inline-block;
    max-width: 240px;
    padding: 8px 12px;
    background-color: #fa8072;
    color: #1a1d23;
    border-radius: 16px 16px 4px 16px;
  }
hints:
  - kosten: 0
    text: |
      Lachs-Bubble mit asymmetrischem Border-Radius (oben rechts spitz).
starter_code: |
  .bubble {
    /* ... */
  }
---

# Chat-Bubble

Eigene Chat-Nachricht mit klassischer Bubble-Form.

---
schema_version: 1
id: c166-chat-bubble
revision: 1
titel: "Chat-Bubble (eigene Nachricht)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [chat, bubble, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
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
    background-color: #2dd4bf;
    color: #1a1d23;
    border-radius: 16px 16px 4px 16px;
  }
asserts:
  - selector: ".bubble"
    property: display
    expected: "inline-block"
  - selector: ".bubble"
    property: max-width
    expected: "240px"
  - selector: ".bubble"
    property: background-color
    expected: "rgb(45, 212, 191)"
  - selector: ".bubble"
    property: border-top-left-radius
    expected: "16px"
  - selector: ".bubble"
    property: border-top-right-radius
    expected: "16px"
  - selector: ".bubble"
    property: border-bottom-right-radius
    expected: "4px"
  - selector: ".bubble"
    property: border-bottom-left-radius
    expected: "16px"
hints:
  - kosten: 0
    text: |
      Petrol-Bubble mit asymmetrischem Border-Radius (oben rechts spitz).
starter_code: |
  .bubble {
    /* ... */
  }
---

# Chat-Bubble

Eigene Chat-Nachricht mit klassischer Bubble-Form.

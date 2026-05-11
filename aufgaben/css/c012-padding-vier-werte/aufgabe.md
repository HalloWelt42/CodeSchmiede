---
schema_version: 1
id: c012-padding-vier-werte
revision: 1
titel: "Padding 4 Werte: 4 8 12 16"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [padding, box-modell]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="box">Inhalt</div>
ziel_css: |
  .box {
    width: 200px;
    background-color: #2dd4bf;
    padding: 4px 8px 12px 16px;
  }
asserts:
  - selector: ".box"
    property: padding-top
    expected: "4px"
  - selector: ".box"
    property: padding-right
    expected: "8px"
  - selector: ".box"
    property: padding-bottom
    expected: "12px"
  - selector: ".box"
    property: padding-left
    expected: "16px"
hints:
  - kosten: 0
    text: |
      Padding-Shorthand:
       - 1 Wert -> alle Seiten
       - 2 Werte -> vertikal | horizontal
       - 3 Werte -> oben | horizontal | unten
       - 4 Werte -> oben | rechts | unten | links (im Uhrzeigersinn)
  - kosten: 2
    text: |
      Hier brauchst du: 4 Werte: 4 8 12 16.
starter_code: |
  .box {
    /* ... */
  }
---

# Padding 4 Werte: 4 8 12 16

Setze das Padding der `.box` so, dass 4 Werte: 4 8 12 16 entsteht.
Farbe und Breite sind bereits Petrol / 200px.

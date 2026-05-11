---
schema_version: 1
id: c011-padding-oben-anders
revision: 1
titel: "Padding oben 4px, sonst 16px"
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
    padding: 4px 16px 16px;
  }
asserts:
  - selector: ".box"
    property: padding-top
    expected: "4px"
  - selector: ".box"
    property: padding-right
    expected: "16px"
  - selector: ".box"
    property: padding-bottom
    expected: "16px"
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
      Hier brauchst du: oben 4px, sonst 16px.
starter_code: |
  .box {
    /* ... */
  }
---

# Padding oben 4px, sonst 16px

Setze das Padding der `.box` so, dass oben 4px, sonst 16px entsteht.
Farbe und Breite sind bereits Petrol / 200px.

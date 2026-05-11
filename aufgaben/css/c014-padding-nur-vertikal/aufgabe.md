---
schema_version: 1
id: c014-padding-nur-vertikal
revision: 1
titel: "Padding nur vertikal 20px"
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
    padding-top: 20px;
    padding-bottom: 20px;
  }
asserts:
  - selector: ".box"
    property: padding-top
    expected: "20px"
  - selector: ".box"
    property: padding-bottom
    expected: "20px"
  - selector: ".box"
    property: padding-left
    expected: "0px"
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
      Hier brauchst du: nur vertikal 20px.
starter_code: |
  .box {
    /* ... */
  }
---

# Padding nur vertikal 20px

Setze das Padding der `.box` so, dass nur vertikal 20px entsteht.
Farbe und Breite sind bereits Petrol / 200px.

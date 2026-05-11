---
schema_version: 1
id: c138-card-basis
revision: 1
titel: "Card: einfache Karte"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [card, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <article class="card"><h3 class="titel">Titel</h3><p class="text">Lorem ipsum dolor sit amet.</p></article>
ziel_css: |
  .card {
    width: 280px;
    padding: 16px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 8px;
    border: 1px solid #3a4049;
  }
  .titel {
    margin: 0 0 8px;
    color: #2dd4bf;
  }
  .text {
    margin: 0;
    color: #9ca3af;
  }
asserts:
  - selector: ".card"
    property: width
    expected: "280px"
  - selector: ".card"
    property: padding-top
    expected: "16px"
  - selector: ".card"
    property: border-radius
    expected: "8px"
  - selector: ".card"
    property: background-color
    expected: "rgb(34, 38, 45)"
  - selector: ".card"
    property: border-top-color
    expected: "rgb(58, 64, 73)"
  - selector: ".titel"
    property: color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      280px breit, 16px Padding, 8px Radius, dunkler Hintergrund.
starter_code: |
  .card {
    /* ... */
  }
  .titel {
    /* ... */
  }
  .text {
    /* ... */
  }
---

# Card: einfache Karte

Dunkle Karte mit Titel in Petrol und gedämpftem Text.

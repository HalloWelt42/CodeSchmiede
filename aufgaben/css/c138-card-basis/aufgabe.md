---
schema_version: 1
id: c138-card-basis
revision: 3
titel: "Card: einfache Karte"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [card, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
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
    color: #38bdf8;
  }
  .text {
    margin: 0;
    color: #9ca3af;
  }
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

Dunkle Karte mit Titel in Azur und gedämpftem Text.

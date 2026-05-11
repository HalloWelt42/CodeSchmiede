---
schema_version: 1
id: c169-rating
revision: 1
titel: "Sterne-Rating (5 Sterne)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [rating, sterne, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="rating"><span class="stern aktiv">★</span><span class="stern aktiv">★</span><span class="stern aktiv">★</span><span class="stern aktiv">★</span><span class="stern">★</span></div>
ziel_css: |
  .rating {
    display: flex;
    gap: 2px;
    font-size: 20px;
  }
  .stern {
    color: #3a4049;
  }
  .aktiv {
    color: #fbbf24;
  }
asserts:
  - selector: ".rating"
    property: display
    expected: "flex"
  - selector: ".rating"
    property: gap
    expected: "2px"
  - selector: ".rating .stern:not(.aktiv)"
    property: color
    expected: "rgb(58, 64, 73)"
  - selector: ".aktiv"
    property: color
    expected: "rgb(251, 191, 36)"
hints:
  - kosten: 0
    text: |
      Flex-Reihe mit 2px Gap. Inaktive Sterne grau, aktive gold.
starter_code: |
  .rating {
    /* ... */
  }
  .stern {
    /* ... */
  }
  .aktiv {
    /* ... */
  }
---

# Sterne-Rating

4 von 5 Sternen aktiv (gold), Rest grau.

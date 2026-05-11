---
schema_version: 1
id: c150-loader-ring
revision: 1
titel: "Loader: Spinner-Ring"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [loader, spinner, border, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="spinner"></div>
ziel_css: |
  .spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #22262d;
    border-top-color: #2dd4bf;
    border-radius: 50%;
  }
asserts:
  - selector: ".spinner"
    property: width
    expected: "40px"
  - selector: ".spinner"
    property: height
    expected: "40px"
  - selector: ".spinner"
    property: border-top-color
    expected: "rgb(45, 212, 191)"
  - selector: ".spinner"
    property: border-right-color
    expected: "rgb(34, 38, 45)"
  - selector: ".spinner"
    property: border-radius
    expected: "50%"
hints:
  - kosten: 0
    text: |
      Kreis (border-radius 50%) mit transparent-grauem Border, oben in Petrol.
starter_code: |
  .spinner {
    /* ... */
  }
---

# Loader: Spinner-Ring

Kreisförmiger Spinner mit petrolfarbenem Top-Border.

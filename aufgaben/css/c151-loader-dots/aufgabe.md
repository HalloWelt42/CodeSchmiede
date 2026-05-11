---
schema_version: 1
id: c151-loader-dots
revision: 1
titel: "Loader: Drei Punkte"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [loader, dots, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="dots"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
ziel_css: |
  .dots {
    display: flex;
    gap: 8px;
  }
  .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: #2dd4bf;
    display: inline-block;
  }
asserts:
  - selector: ".dots"
    property: display
    expected: "flex"
  - selector: ".dots"
    property: gap
    expected: "8px"
  - selector: ".dot"
    property: width
    expected: "12px"
  - selector: ".dot"
    property: border-radius
    expected: "50%"
  - selector: ".dot"
    property: background-color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      Drei Petrol-Punkte (12px Kreise) nebeneinander mit 8px Gap.
starter_code: |
  .dots {
    /* ... */
  }
  .dot {
    /* ... */
  }
---

# Loader: Drei Punkte

Drei Petrol-Punkte als Lade-Indikator.

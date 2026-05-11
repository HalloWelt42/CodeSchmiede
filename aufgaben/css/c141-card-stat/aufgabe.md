---
schema_version: 1
id: c141-card-stat
revision: 1
titel: "Card: Statistik-Kachel"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [card, kpi, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="kachel"><div class="zahl">1.234</div><div class="label">Aktive Nutzer</div></div>
ziel_css: |
  .kachel {
    width: 200px;
    padding: 24px;
    background-color: #22262d;
    border-radius: 6px;
    text-align: center;
  }
  .zahl {
    font-size: 32px;
    font-weight: 700;
    color: #2dd4bf;
  }
  .label {
    margin-top: 8px;
    color: #9ca3af;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
asserts:
  - selector: ".kachel"
    property: padding-top
    expected: "24px"
  - selector: ".kachel"
    property: text-align
    expected: "center"
  - selector: ".kachel"
    property: border-radius
    expected: "6px"
  - selector: ".zahl"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: ".zahl"
    property: font-weight
    expected: "700"
  - selector: ".label"
    property: text-transform
    expected: "uppercase"
hints:
  - kosten: 0
    text: |
      Zahl zentral und groß in Petrol, Label klein in Großbuchstaben darunter.
starter_code: |
  .kachel {
    /* ... */
  }
  .zahl {
    /* ... */
  }
  .label {
    /* ... */
  }
---

# Card: Statistik-Kachel

KPI-Kachel mit großer Zahl und kleinem Label.

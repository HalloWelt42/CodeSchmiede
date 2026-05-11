---
schema_version: 1
id: l003-pricing-trio
revision: 1
titel: "Layout 03: Pricing-Trio mit hervorgehobener Mitte"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 10
tags: [layout, lernpfad, grid, card, pricing]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="preise"><div class="plan">Basis</div><div class="plan empfohlen">Pro</div><div class="plan">Premium</div></div>
ziel_css: |
  .preise {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    width: 480px;
    padding: 8px;
    background-color: #1a1d23;
    align-items: center;
  }
  .plan {
    background-color: #22262d;
    color: #e7ecf1;
    padding: 24px;
    border-radius: 8px;
    text-align: center;
    font-weight: 700;
    border: 1px solid #3a4049;
  }
  .empfohlen {
    background-color: #2dd4bf;
    color: #1a1d23;
    transform: scale(1.08);
    border-color: #2dd4bf;
  }
asserts:
  - selector: ".preise"
    property: display
    expected: "grid"
  - selector: ".preise"
    property: grid-template-columns
    expected: "146.656px 146.656px 146.656px"
  - selector: ".preise"
    property: align-items
    expected: "center"
  - selector: ".empfohlen"
    property: transform
    expected: "matrix(1.08, 0, 0, 1.08, 0, 0)"
hints:
  - kosten: 0
    text: |
      Drei gleichbreite Spalten via Grid. Die mittlere Karte bekommt einen Petrol-Hintergrund und wird leicht größer skaliert -- klassisches 'empfohlener Tarif'-Pattern.
  - kosten: 5
    text: |
      Auf .preise: `display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; align-items: center;` und auf .empfohlen: `background: #2dd4bf; transform: scale(1.08);`
starter_code: |
  .preise {
    width: 480px;
    padding: 8px;
    background-color: #1a1d23;
    /* hier: 3-Spalten-Grid, gap 12px, vertikal zentriert */
  }
  .plan {
    background-color: #22262d;
    color: #e7ecf1;
    padding: 24px;
    border-radius: 8px;
    text-align: center;
    font-weight: 700;
    border: 1px solid #3a4049;
  }
  .empfohlen {
    border-color: #2dd4bf;
    /* Petrol-Hintergrund, dunkler Text, leichte Skalierung */
  }
---

# Layout 03: Pricing-Trio

## Aufgabe

Drei Tarifkarten nebeneinander.
Die mittlere ('Pro') ist hervorgehoben: Petrol-Hintergrund und 8% größer
als die anderen (per transform: scale).

## Aha

Durch transform: scale
bleibt das Grid-Layout intakt -- die Karte 'wirkt' größer, das umliegende
Layout ändert sich nicht. Mit align-items: center auf dem Container sitzen
die kleineren Karten vertikal zentriert.

## Wozu in der Praxis?

SaaS-Landing-Pages, Abo-Modelle, Vergleichstabellen.

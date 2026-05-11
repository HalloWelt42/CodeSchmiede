---
schema_version: 1
id: g012-grid-auto-fit
revision: 1
titel: "Grid 12: Galerie ohne Media-Query -- auto-fit + minmax"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 5
tags: [grid, lernpfad]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="setzkasten"><div class="kachel k1">1</div><div class="kachel k2">2</div><div class="kachel k3">3</div><div class="kachel k4">4</div><div class="kachel k5">5</div><div class="kachel k6">6</div><div class="kachel k7">7</div><div class="kachel k8">8</div></div>
ziel_css: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
    gap: 8px;
  }
  .kachel {
    background-color: #2dd4bf;
    color: #1a1d23;
    padding: 12px;
    font-weight: 700;
    text-align: center;
  }
asserts:
  - selector: ".setzkasten"
    property: grid-template-columns
    expected: "108.664px 108.664px 108.664px"
hints:
  - kosten: 0
    text: |
      CSS-Grid ist 2-dimensional (Zeilen UND Spalten gleichzeitig).
      Im Gegensatz zu Flexbox musst du dem Container das Raster-Muster
      vorgeben -- erst dann wissen die Zellen, wohin sie gehören.
  - kosten: 3
    text: |
      `grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));`
starter_code: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    /* Galerie: so viele 80px-Spalten wie reinpassen, Rest aufdehnen */
    gap: 8px;
  }
  .kachel {
    background-color: #2dd4bf;
    color: #1a1d23;
    padding: 12px;
    font-weight: 700;
    text-align: center;
  }
---

# Grid 12: Beliebig viele Kacheln, mind. 80px breit, fuellen die verfügbare Breite

## Aufgabe

Im Setzkasten-Rahmen sollen die Kacheln so angeordnet werden, dass
**beliebig viele kacheln, mind. 80px breit, fuellen die verfügbare breite**.

Schreibe die fehlende(n) Grid-Anweisung(en) in `.setzkasten`.

## Aha

`repeat(auto-fit, minmax(80px, 1fr))` ist das **wichtigste Pattern in
modernem CSS**: der Browser zählt selber, wieviele 80px-Spalten in den
Container passen, und dehnt sie auf den Rest auf. Bei breitem Bildschirm
viele Spalten, bei schmalem wenige -- ohne dass du eine einzige Media-Query
schreiben musst.

## Wozu in der Praxis?

Produkt-Galerien, Foto-Grids, Card-Listen, Dashboard-Kacheln. Mit zwei
Zeilen CSS hast du ein voll responsives Layout. Bei `auto-fill` statt
`auto-fit` bleiben leere Spuren stehen, mit `auto-fit` werden sie
kollabiert. Praxis: meist `auto-fit`.

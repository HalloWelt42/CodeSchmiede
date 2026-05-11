---
schema_version: 1
id: l005-galerie-auto-fit
revision: 1
titel: "Layout 05: Galerie ohne Media-Query (auto-fit + minmax)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [layout, lernpfad, grid, auto-fit, responsiv]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="galerie"><div class="bild b1">1</div><div class="bild b2">2</div><div class="bild b3">3</div><div class="bild b4">4</div><div class="bild b5">5</div><div class="bild b6">6</div><div class="bild b7">7</div><div class="bild b8">8</div></div>
ziel_css: |
  .galerie {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
    gap: 8px;
    width: 480px;
    padding: 8px;
    background-color: #1a1d23;
  }
  .bild {
    aspect-ratio: 1 / 1;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    border-radius: 6px;
  }
asserts:
  - selector: ".galerie"
    property: display
    expected: "grid"
  - selector: ".galerie"
    property: grid-template-columns
    expected: "110px 110px 110px 110px"
  - selector: ".bild"
    property: aspect-ratio
    expected: "1 / 1"
hints:
  - kosten: 0
    text: |
      Wieviele Spalten passen rein? Das berechnet auto-fit selber. minmax(100px, 1fr) heisst: Spalten sind mind. 100px breit, dehnen sich aber auf den Rest. Zusammen ergibt sich ein responsives Grid ohne eine Media-Query.
  - kosten: 5
    text: |
      Auf .galerie: `grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));`
starter_code: |
  .galerie {
    display: grid;
    /* hier: auto-fit-Grid mit minmax(100px, 1fr) */
    gap: 8px;
    width: 480px;
    padding: 8px;
    background-color: #1a1d23;
  }
  .bild {
    aspect-ratio: 1 / 1;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    border-radius: 6px;
  }
---

# Layout 05: Responsive Galerie

## Aufgabe

8 quadratische Kacheln,
die sich automatisch an die Container-Breite anpassen -- ohne dass du eine
Media-Query schreibst.

## Aha

`repeat(auto-fit, minmax(MIN, 1fr))` ist
das wichtigste Grid-Pattern. Der Browser zählt wieviele MIN-Spalten in den
Container passen und dehnt sie dann auf den Rest. Mit aspect-ratio bleiben
die Kacheln quadratisch, egal wie breit der Container wird.

## Wozu in der
Praxis?

Produktgalerien, Foto-Wand, Dashboard-KPIs, Markenlogos.

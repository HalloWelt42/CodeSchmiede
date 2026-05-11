---
schema_version: 1
id: g003-grid-fr-verteilung
revision: 1
titel: "Grid 03: Spalten im Verhältnis 1:2:1"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 10
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
  <div class="setzkasten"><div class="kachel k1">1</div><div class="kachel k2">2</div><div class="kachel k3">3</div></div>
ziel_css: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
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
    expected: "85.5px 171px 85.5px"
hints:
  - kosten: 0
    text: |
      CSS-Grid ist 2-dimensional (Zeilen UND Spalten gleichzeitig).
      Im Gegensatz zu Flexbox musst du dem Container das Raster-Muster
      vorgeben -- erst dann wissen die Zellen, wohin sie gehören.
  - kosten: 3
    text: |
      `grid-template-columns: 1fr 2fr 1fr;`
starter_code: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    /* 1:2:1-Verhaeltnis */
  }
  .kachel {
    background-color: #2dd4bf;
    color: #1a1d23;
    padding: 12px;
    font-weight: 700;
    text-align: center;
  }
---

# Grid 03: Die mittlere Spalte ist doppelt so breit wie die aeusseren

## Aufgabe

Im Setzkasten-Rahmen sollen die Kacheln so angeordnet werden, dass
**die mittlere spalte ist doppelt so breit wie die aeusseren**.

Schreibe die fehlende(n) Grid-Anweisung(en) in `.setzkasten`.

## Aha

Die `fr`-Einheit verteilt **Rest-Platz** im Verhaeltnis ihrer Werte.
`1fr 2fr 1fr` heisst: der Mittelplatz bekommt doppelt so viel wie
die aeusseren. Mische fr mit px und der Browser rechnet: Pixel-Werte
werden zuerst abgezogen, dann der Rest per fr verteilt.

## Wozu in der Praxis?

Klassisches Sidebar-Layout: `200px 1fr` -- die Sidebar ist fix, der
Hauptbereich nimmt den Rest. Oder ein Hero-Layout: `1fr 2fr 1fr` mit
Spacing links/rechts und doppeltem Content in der Mitte.

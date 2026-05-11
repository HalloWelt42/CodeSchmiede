---
schema_version: 1
id: g001-grid-aktivieren
revision: 1
titel: "Grid 01: Grid einschalten"
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
  <div class="setzkasten"><div class="kachel k1">1</div><div class="kachel k2">2</div><div class="kachel k3">3</div><div class="kachel k4">4</div></div>
ziel_css: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    grid-template-columns: 1fr 1fr;
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
    property: display
    expected: "grid"
  - selector: ".setzkasten"
    property: grid-template-columns
    expected: "172px 172px"
hints:
  - kosten: 0
    text: |
      CSS-Grid ist 2-dimensional (Zeilen UND Spalten gleichzeitig).
      Im Gegensatz zu Flexbox musst du dem Container das Raster-Muster
      vorgeben -- erst dann wissen die Zellen, wohin sie gehören.
  - kosten: 3
    text: |
      `display: grid;` und `grid-template-columns: 1fr 1fr;`
starter_code: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    /* Grid aktivieren und zwei Spalten anlegen */
  }
  .kachel {
    background-color: #2dd4bf;
    color: #1a1d23;
    padding: 12px;
    font-weight: 700;
    text-align: center;
  }
---

# Grid 01: Vier Kacheln in einem Grid landen (statt blockweise zu stapeln)

## Aufgabe

Im Setzkasten-Rahmen sollen die Kacheln so angeordnet werden, dass
**vier kacheln in einem grid landen (statt blockweise zu stapeln)**.

Schreibe die fehlende(n) Grid-Anweisung(en) in `.setzkasten`.

## Aha

Mit `display: grid` wird der Container zum Raster. Erst die Anweisung
`grid-template-columns` sagt, **wieviele Spalten und wie breit**.
`1fr 1fr` heisst: zwei gleichbreite Spalten, die den Platz teilen.

## Wozu in der Praxis?

Dashboards, KPI-Kacheln, Produktgalerien -- alles wo etwas in einer
klaren tabellarischen Anordnung erscheint, sitzt in einem Grid.
Im Gegensatz zu Flexbox musst du das Raster vorgeben.

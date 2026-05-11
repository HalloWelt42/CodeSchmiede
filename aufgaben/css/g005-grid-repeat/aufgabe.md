---
schema_version: 1
id: g005-grid-repeat
revision: 1
titel: "Grid 05: Mit repeat() -- vier gleichbreite Spalten"
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
  <div class="setzkasten"><div class="kachel k1">1</div><div class="kachel k2">2</div><div class="kachel k3">3</div><div class="kachel k4">4</div><div class="kachel k5">5</div><div class="kachel k6">6</div><div class="kachel k7">7</div><div class="kachel k8">8</div></div>
ziel_css: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
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
    expected: "80px 80px 80px 80px"
hints:
  - kosten: 0
    text: |
      CSS-Grid ist 2-dimensional (Zeilen UND Spalten gleichzeitig).
      Im Gegensatz zu Flexbox musst du dem Container das Raster-Muster
      vorgeben -- erst dann wissen die Zellen, wohin sie gehören.
  - kosten: 3
    text: |
      `grid-template-columns: repeat(4, 1fr);`
starter_code: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    /* vier gleichbreite Spalten via repeat() */
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

# Grid 05: Vier Spalten über repeat() statt vier einzelne Werte

## Aufgabe

Im Setzkasten-Rahmen sollen die Kacheln so angeordnet werden, dass
**vier spalten über repeat() statt vier einzelne werte**.

Schreibe die fehlende(n) Grid-Anweisung(en) in `.setzkasten`.

## Aha

`repeat(N, ...)` ist Tippsparen: `repeat(4, 1fr)` ist identisch zu
`1fr 1fr 1fr 1fr`. Bei 12 Spalten (Bootstrap-Style) ist das ein
Lebensretter. Wert kann auch komplexer sein: `repeat(3, 100px 1fr)`
wechselt zwischen festen und flexiblen Spalten.

## Wozu in der Praxis?

12-Spalten-Grids für Layout-Systeme. Wochentage-Anzeige (7 Spalten
im Kalender). Stundenleiste, Vor-Auswahl in Komponenten.

---
schema_version: 1
id: g011-grid-minmax
revision: 1
titel: "Grid 11: Spalte mit Mindest-/Maximalbreite -- minmax()"
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
    grid-template-columns: minmax(80px, 200px) 1fr 1fr;
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
    expected: "200px 64px 64px"
hints:
  - kosten: 0
    text: |
      CSS-Grid ist 2-dimensional (Zeilen UND Spalten gleichzeitig).
      Im Gegensatz zu Flexbox musst du dem Container das Raster-Muster
      vorgeben -- erst dann wissen die Zellen, wohin sie gehören.
  - kosten: 3
    text: |
      `grid-template-columns: minmax(80px, 200px) 1fr 1fr;`
starter_code: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    /* erste Spalte: min 80px, max 200px; danach 2x 1fr */
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

# Grid 11: Eine Spalte zwischen 80px (Minimum) und 200px (Maximum), die sich an den Rest anpasst

## Aufgabe

Im Setzkasten-Rahmen sollen die Kacheln so angeordnet werden, dass
**eine spalte zwischen 80px (minimum) und 200px (maximum), die sich an den rest anpasst**.

Schreibe die fehlende(n) Grid-Anweisung(en) in `.setzkasten`.

## Aha

`minmax(min, max)` ist eine Spaltenbreite mit unteren und oberen Grenzen.
Solange genug Platz da ist, nimmt die Spalte die Max-Größe. Bei Engpass
schrumpft sie -- aber nie unter Min. Das macht Layouts robust ohne
Media-Query.

## Wozu in der Praxis?

Sidebar, die mindestens 80px breit bleibt damit Icons reinpassen, aber
nicht über 300px geht damit der Hauptinhalt nicht erstickt: 
`grid-template-columns: minmax(80px, 300px) 1fr;`.

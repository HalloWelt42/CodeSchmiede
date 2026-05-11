---
schema_version: 1
id: g009-grid-zwei-dimensionen
revision: 1
titel: "Grid 09: 2D-Positionierung -- grid-row + grid-column"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [grid, lernpfad, grid-row, grid-column]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="setzkasten"><div class="kachel sidebar">Side</div><div class="kachel haupt">Main</div><div class="kachel">x</div><div class="kachel">y</div></div>
ziel_css: |
  .setzkasten {
    display: grid;
    grid-template-columns: 100px 1fr;
    grid-template-rows: 80px 80px;
    gap: 8px;
    width: 360px;
    background-color: #22262d;
    padding: 8px;
  }
  .kachel {
    background-color: #2dd4bf;
    color: #1a1d23;
    padding: 12px;
    font-weight: 700;
    text-align: center;
  }
  .sidebar {
    grid-row: 1 / 3;
    background-color: #a78bfa;
  }
  .haupt {
    grid-column: 2;
    background-color: #fb923c;
  }
asserts:
  - selector: ".sidebar"
    property: grid-row-start
    expected: "1"
  - selector: ".sidebar"
    property: grid-row-end
    expected: "3"
hints:
  - kosten: 0
    text: |
      `grid-row` funktioniert analog zu `grid-column`: `1 / 3` heisst von Zeilen-
      linie 1 bis 3 -- also über 2 Zeilen. Eine Sidebar kann so volle Höhe einnehmen.
  - kosten: 4
    text: |
      Setze auf `.sidebar`: `grid-row: 1 / 3;`
starter_code: |
  .setzkasten {
    display: grid;
    grid-template-columns: 100px 1fr;
    grid-template-rows: 80px 80px;
    gap: 8px;
    width: 360px;
    background-color: #22262d;
    padding: 8px;
  }
  .kachel {
    background-color: #2dd4bf;
    color: #1a1d23;
    padding: 12px;
    font-weight: 700;
    text-align: center;
  }
  .sidebar {
    background-color: #a78bfa;
    /* ueber beide Zeilen ziehen */
  }
  .haupt {
    grid-column: 2;
    background-color: #fb923c;
  }
---

# Grid 09: 2D-Positionierung

## Aufgabe

Klassisches App-Layout: links eine **schmale Sidebar** über
die ganze Höhe (zwei Zeilen). Rechts ein Hauptbereich oben und kleinere
Kacheln darunter.

## Aha

Grid laesst dich beliebige Zellen-Positionen explizit angeben.
Das macht 2D-Layouts moeglich, die mit Flexbox sehr umstaendlich wären.
Ein klassischer Use-Case ist die Sidebar, die über mehrere Reihen geht.

## Wozu in der Praxis?

Mail-Clients (Ordner-Sidebar | Liste | Vorschau), IDEs (Datei-Tree | Editor
| Output), Admin-Panels -- alle leben von solchen 2D-Layouts.

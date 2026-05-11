---
schema_version: 1
id: g002-grid-feste-breiten
revision: 1
titel: "Grid 02: Drei feste Spaltenbreiten"
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
    grid-template-columns: 80px 120px 160px;
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
    expected: "80px 120px 160px"
hints:
  - kosten: 0
    text: |
      CSS-Grid ist 2-dimensional (Zeilen UND Spalten gleichzeitig).
      Im Gegensatz zu Flexbox musst du dem Container das Raster-Muster
      vorgeben -- erst dann wissen die Zellen, wohin sie gehören.
  - kosten: 3
    text: |
      `grid-template-columns: 80px 120px 160px;`
starter_code: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    /* drei Spalten: 80px, 120px, 160px */
  }
  .kachel {
    background-color: #2dd4bf;
    color: #1a1d23;
    padding: 12px;
    font-weight: 700;
    text-align: center;
  }
---

# Grid 02: Drei Spalten in 80px / 120px / 160px nebeneinander

## Aufgabe

Im Setzkasten-Rahmen sollen die Kacheln so angeordnet werden, dass
**drei spalten in 80px / 120px / 160px nebeneinander**.

Schreibe die fehlende(n) Grid-Anweisung(en) in `.setzkasten`.

## Aha

Du kannst beliebig viele Werte hinter `grid-template-columns` schreiben --
der Browser zählt sie als Spaltenanzahl. Pixelwerte machen die Spalten
**fix**, unabhängig von der Container-Breite.

## Wozu in der Praxis?

Formulare mit Label-Spalte (fixe Breite) + Input-Spalte (breiter) +
Hinweis-Spalte (schmal). Auch klassische Tabellen-Layouts profitieren
von festen Pixelbreiten für Zahlen oder Status-Icons.

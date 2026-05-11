---
schema_version: 1
id: g007-grid-spalten-bereich
revision: 1
titel: "Grid 07: Spalten 1 bis 4 explizit -- grid-column: 1 / 4"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [grid, lernpfad, grid-column, linien]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="setzkasten"><div class="kachel banner">Banner</div><div class="kachel">A</div><div class="kachel">B</div><div class="kachel">C</div></div>
ziel_css: |
  .setzkasten {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
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
  .banner {
    grid-column: 1 / 4;
    background-color: #a78bfa;
  }
asserts:
  - selector: ".banner"
    property: grid-column-start
    expected: "1"
  - selector: ".banner"
    property: grid-column-end
    expected: "4"
hints:
  - kosten: 0
    text: |
      Spaltenlinien werden ab 1 nummeriert. Bei 3 Spalten gibt es **4 Linien**
      (links von Spalte 1, zwischen 1 und 2, zwischen 2 und 3, rechts von 3).
      `grid-column: 1 / 4` heisst: starte an Linie 1, ende an Linie 4 -- also voll.
  - kosten: 4
    text: |
      Setze auf `.banner`: `grid-column: 1 / 4;`
starter_code: |
  .setzkasten {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
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
  .banner {
    background-color: #a78bfa;
    /* von Linie 1 bis Linie 4 spannen */
  }
---

# Grid 07: Spalten-Linien als Bereich

## Aufgabe

Der Banner oben soll **die volle Breite über alle drei Spalten**
einnehmen, die drei Kacheln darunter normal in jeweils einer Spalte.

## Aha

Mit `grid-column: <start> / <end>` setzt du explizit, an welcher
Grid-Linie ein Item beginnt und endet. Linien beginnen bei 1; bei N Spalten
gibt es N+1 Linien. `grid-column: 1 / -1` ist ein Trick: -1 ist immer die
letzte Linie -- damit funktioniert es egal wieviele Spalten der Container hat.

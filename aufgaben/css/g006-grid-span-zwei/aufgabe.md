---
schema_version: 1
id: g006-grid-span-zwei
revision: 1
titel: "Grid 06: Eine Kachel über zwei Spalten -- span 2"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [grid, lernpfad, grid-column, span]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="setzkasten"><div class="kachel breit">groß</div><div class="kachel">2</div><div class="kachel">3</div><div class="kachel">4</div></div>
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
  .breit {
    grid-column: span 2;
    background-color: #fb923c;
  }
asserts:
  - selector: ".breit"
    property: grid-column-end
    expected: "auto"
hints:
  - kosten: 0
    text: |
      Per Default sitzt jede Zelle in einer Spalte. Mit `grid-column: span N`
      spannst du eine Zelle über N Spalten.
  - kosten: 4
    text: |
      Setze auf `.breit`: `grid-column: span 2;`
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
  .breit {
    background-color: #fb923c;
    /* ueber zwei Spalten ziehen */
  }
---

# Grid 06: Eine Kachel über zwei Spalten

## Aufgabe

Der Setzkasten hat 3 Spalten. **Die erste Kachel (orange)
soll über 2 Spalten gehen**, die anderen drei normal in jeweils einer.
Da der Container 4 Kacheln + Span hat, ergeben sich 2 Reihen.

## Aha

`grid-column: span 2` weist ein einzelnes Item an, zwei
Spalten breit zu werden. Die nachfolgenden Items rutschen automatisch
weiter, das Grid bleibt sauber.

## Wozu in der Praxis?

Eine Featured-Karte in einer Galerie, die hervorgehoben wird durch
doppelte Breite. Oder ein Hero-Banner über alle Spalten in einem
Bento-Box-Layout.

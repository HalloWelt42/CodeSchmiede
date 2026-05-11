---
schema_version: 1
id: g008-grid-rows
revision: 1
titel: "Grid 08: Zeilenhöhen festlegen -- grid-template-rows"
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
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 100px 50px;
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
asserts:
  - selector: ".setzkasten"
    property: grid-template-rows
    expected: "100px 50px"
hints:
  - kosten: 0
    text: |
      CSS-Grid ist 2-dimensional (Zeilen UND Spalten gleichzeitig).
      Im Gegensatz zu Flexbox musst du dem Container das Raster-Muster
      vorgeben -- erst dann wissen die Zellen, wohin sie gehören.
  - kosten: 3
    text: |
      `grid-template-rows: 100px 50px;`
starter_code: |
  .setzkasten {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    /* zwei Zeilen: erste 100px, zweite 50px */
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
---

# Grid 08: Erste Zeile 100px hoch, zweite Zeile 50px, automatisches Verteilen

## Aufgabe

Im Setzkasten-Rahmen sollen die Kacheln so angeordnet werden, dass
**erste zeile 100px hoch, zweite zeile 50px, automatisches verteilen**.

Schreibe die fehlende(n) Grid-Anweisung(en) in `.setzkasten`.

## Aha

Analog zu `grid-template-columns` gibt's `grid-template-rows` für Zeilen-
höhen. Mit beiden zusammen hast du das volle 2D-Raster im Griff. Wenn du
die Zeilen weglaesst, dehnen sie sich automatisch dem Inhalt an.

## Wozu in der Praxis?

Header-Layout: erste Zeile 80px (Navigation), zweite Zeile `1fr` (Inhalt),
dritte Zeile 40px (Footer). Mit `grid-template-rows: 80px 1fr 40px` ist
das Layout in einer Zeile fertig -- klassisches App-Shell-Pattern.

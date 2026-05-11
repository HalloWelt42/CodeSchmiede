---
schema_version: 1
id: g004-grid-luecken
revision: 1
titel: "Grid 04: Lücken zwischen Kacheln -- gap"
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
  <div class="setzkasten"><div class="kachel k1">1</div><div class="kachel k2">2</div><div class="kachel k3">3</div><div class="kachel k4">4</div><div class="kachel k5">5</div><div class="kachel k6">6</div></div>
ziel_css: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
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
    property: gap
    expected: "12px"
hints:
  - kosten: 0
    text: |
      CSS-Grid ist 2-dimensional (Zeilen UND Spalten gleichzeitig).
      Im Gegensatz zu Flexbox musst du dem Container das Raster-Muster
      vorgeben -- erst dann wissen die Zellen, wohin sie gehören.
  - kosten: 3
    text: |
      `gap: 12px;`
starter_code: |
  .setzkasten {
    width: 360px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    /* 12px Luecke zwischen den Zellen */
  }
  .kachel {
    background-color: #2dd4bf;
    color: #1a1d23;
    padding: 12px;
    font-weight: 700;
    text-align: center;
  }
---

# Grid 04: Zwischen den Kacheln entsteht 12px Abstand, links und rechts UND oben und unten

## Aufgabe

Im Setzkasten-Rahmen sollen die Kacheln so angeordnet werden, dass
**zwischen den kacheln entsteht 12px abstand, links und rechts und oben und unten**.

Schreibe die fehlende(n) Grid-Anweisung(en) in `.setzkasten`.

## Aha

`gap` setzt sowohl horizontale als auch vertikale Lücken in einem.
Mit zwei Werten (`gap: 8px 12px`) trennst du vertikal/horizontal.
Wichtig: gap wirkt NUR zwischen Zellen -- nicht am Rand. Aussenrand
übernimmt weiterhin `padding` am Container.

## Wozu in der Praxis?

Galerien, Card-Grids, Dashboard-Kacheln -- überall wo gleichmaessige
Abstaende ohne mathematische Magie gewuenscht sind. Vor `gap` musste
man mit negativen Margins jonglieren -- jetzt ist es eine Zeile.

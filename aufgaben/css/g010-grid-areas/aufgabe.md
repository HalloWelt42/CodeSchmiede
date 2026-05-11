---
schema_version: 1
id: g010-grid-areas
revision: 1
titel: "Grid 10: Benannte Bereiche -- grid-template-areas"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [grid, lernpfad, grid-area, template-areas]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="seite"><header class="kopf">Header</header><nav class="navi">Nav</nav><main class="haupt">Inhalt</main><footer class="fuss">Footer</footer></div>
ziel_css: |
  .seite {
    display: grid;
    grid-template-columns: 100px 1fr;
    grid-template-rows: 50px 1fr 40px;
    grid-template-areas:
      "kopf kopf"
      "navi haupt"
      "fuss fuss";
    gap: 6px;
    width: 360px;
    height: 220px;
    background-color: #22262d;
    padding: 6px;
  }
  .kopf { grid-area: kopf; background-color: #fb923c; }
  .navi { grid-area: navi; background-color: #a78bfa; }
  .haupt { grid-area: haupt; background-color: #2dd4bf; }
  .fuss { grid-area: fuss; background-color: #9ca3af; }
  .kopf, .navi, .haupt, .fuss {
    color: #1a1d23;
    padding: 8px;
    font-weight: 700;
    text-align: center;
  }
asserts:
  - selector: ".kopf"
    property: grid-area
    expected: "kopf"
  - selector: ".haupt"
    property: grid-area
    expected: "haupt"
hints:
  - kosten: 0
    text: |
      Mit `grid-template-areas` zeichnest du das Layout direkt als ASCII-Art im
      CSS -- jede Zelle bekommt einen Namen, jedes Item wird per `grid-area`-Property
      einer Zelle zugeordnet.
  - kosten: 5
    text: |
      Setze auf die Items: `grid-area: kopf` / `grid-area: navi` / `grid-area: haupt` / `grid-area: fuss`
starter_code: |
  .seite {
    display: grid;
    grid-template-columns: 100px 1fr;
    grid-template-rows: 50px 1fr 40px;
    grid-template-areas:
      "kopf kopf"
      "navi haupt"
      "fuss fuss";
    gap: 6px;
    width: 360px;
    height: 220px;
    background-color: #22262d;
    padding: 6px;
  }
  .kopf { background-color: #fb923c; /* Area zuweisen */ }
  .navi { background-color: #a78bfa; /* Area zuweisen */ }
  .haupt { background-color: #2dd4bf; /* Area zuweisen */ }
  .fuss { background-color: #9ca3af; /* Area zuweisen */ }
  .kopf, .navi, .haupt, .fuss {
    color: #1a1d23;
    padding: 8px;
    font-weight: 700;
    text-align: center;
  }
---

# Grid 10: Benannte Bereiche

## Aufgabe

Klassisches App-Shell-Layout: Header oben (über beide Spalten),
Nav links, Hauptbereich rechts, Footer unten (wieder beide Spalten). Die
Container-Definition mit Areas ist schon da -- du musst nur den vier Items
ihre Area zuweisen.

## Aha

`grid-template-areas` ist Layout-als-Bild: du **siehst** die
Anordnung direkt im CSS. Jeder String ist eine Zeile, jedes Wort eine
Zelle. Wiederholte Namen verbinden Zellen zu größeren Bereichen.
Ein Punkt (`.`) markiert eine leere Zelle.

## Wozu in der Praxis?

Holy-Grail-Layout (Header + 3 Spalten + Footer), responsives Umordnen mit
Media-Queries (nur das areas-Bild ändern, nichts am HTML), Print-Layouts.

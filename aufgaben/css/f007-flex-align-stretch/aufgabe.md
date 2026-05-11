---
schema_version: 1
id: f007-flex-align-stretch
revision: 1
titel: "Flexbox 07: Auf volle Höhe ziehen -- align-items: stretch"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [flexbox, lernpfad]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="teich"><div class="frosch a">A</div><div class="frosch b">B</div><div class="frosch c">C</div></div>
ziel_css: |
  .teich {
    width: 400px;
    height: 120px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
  }
  .frosch {
    width: 60px;
    height: 60px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    margin: 4px;
  }
  .teich {
    display: flex;
    align-items: stretch;
  }
asserts:
  - selector: ".teich"
    property: display
    expected: "flex"
  - selector: ".teich"
    property: align-items
    expected: "stretch"
hints:
  - kosten: 0
    text: |
      Flexbox-Eltern muss `display: flex` haben, damit `justify-content`, `align-items` & Co. greifen.
      Diese Aufgabe lehrt EINE Property -- die anderen kommen in den nächsten Levels.
  - kosten: 3
    text: |
      `display: flex;
        align-items: stretch;`
starter_code: |
  .teich {
    display: flex;
    /* Items auf volle Hoehe ziehen */
  }
---

# Flexbox 07: Froesche dehnen sich vertikal auf die volle Teich-Höhe

## Aufgabe

Im Teich-Rahmen sollen die drei Froesche so angeordnet werden, dass
**froesche dehnen sich vertikal auf die volle teich-höhe**.

Schreib **nur** die fehlende Flexbox-Anweisung in `.teich` -- der Rest
(Größe, Farbe, Quadrate) ist schon da.

## Aha

`stretch` ist der **Default** von `align-items`. Items ohne fixe Höhe
wachsen automatisch auf die volle Quer-Achsen-Größe. Drei Karten in
einer Flex-Reihe sind so ohne Tricks gleich hoch.

## Wozu in der Praxis?

Wenn drei Spalten in einer Sektion gleich hoch wirken sollen -- z.B. drei
Feature-Karten nebeneinander, die unterschiedlich viel Text enthalten --
dann sorgt `stretch` dafür, dass keine Karte 'hochsteht'.

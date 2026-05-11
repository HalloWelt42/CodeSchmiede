---
schema_version: 1
id: f008-flex-direction-column
revision: 1
titel: "Flexbox 08: Vertikale Spalte -- flex-direction: column"
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
    flex-direction: column;
  }
asserts:
  - selector: ".teich"
    property: display
    expected: "flex"
  - selector: ".teich"
    property: flex-direction
    expected: "column"
hints:
  - kosten: 0
    text: |
      Flexbox-Eltern muss `display: flex` haben, damit `justify-content`, `align-items` & Co. greifen.
      Diese Aufgabe lehrt EINE Property -- die anderen kommen in den nächsten Levels.
  - kosten: 3
    text: |
      `display: flex;
        flex-direction: column;`
starter_code: |
  .teich {
    display: flex;
    /* von Reihe (row) zu Spalte (column) wechseln */
  }
---

# Flexbox 08: Die Froesche stapeln sich vertikal statt nebeneinander zu stehen

## Aufgabe

Im Teich-Rahmen sollen die drei Froesche so angeordnet werden, dass
**die froesche stapeln sich vertikal statt nebeneinander zu stehen**.

Schreib **nur** die fehlende Flexbox-Anweisung in `.teich` -- der Rest
(Größe, Farbe, Quadrate) ist schon da.

## Aha

Mit `column` **dreht sich die Haupt-Achse um 90°**: justify-content arbeitet
jetzt vertikal, align-items horizontal. Das ist auch der Grund warum man
in vertikalen Layouts oft zwischen 'oben/unten' und 'links/rechts' verwechselt.

## Wozu in der Praxis?

Vertikale Navigation, Form-Felder untereinander, Chat-Bubbles in einer
Konversation -- überall wo Inhalte vertikal stapeln, ist `flex-direction:
column` das Werkzeug der Wahl.

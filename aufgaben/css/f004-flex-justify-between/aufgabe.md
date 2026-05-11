---
schema_version: 1
id: f004-flex-justify-between
revision: 1
titel: "Flexbox 04: Gleichmaessige Lücken mit space-between"
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
    justify-content: space-between;
  }
asserts:
  - selector: ".teich"
    property: display
    expected: "flex"
  - selector: ".teich"
    property: justify-content
    expected: "space-between"
hints:
  - kosten: 0
    text: |
      Flexbox-Eltern muss `display: flex` haben, damit `justify-content`, `align-items` & Co. greifen.
      Diese Aufgabe lehrt EINE Property -- die anderen kommen in den nächsten Levels.
  - kosten: 3
    text: |
      `display: flex;
        justify-content: space-between;`
starter_code: |
  .teich {
    display: flex;
    /* den Platz zwischen den Items gleichmaessig verteilen */
  }
---

# Flexbox 04: Der erste Frosch links, der letzte rechts, die Lücken dazwischen sind gleich groß

## Aufgabe

Im Teich-Rahmen sollen die drei Froesche so angeordnet werden, dass
**der erste frosch links, der letzte rechts, die lücken dazwischen sind gleich groß**.

Schreib **nur** die fehlende Flexbox-Anweisung in `.teich` -- der Rest
(Größe, Farbe, Quadrate) ist schon da.

## Aha

Bei `space-between` kleben das erste und das letzte Item an den Rändern,
der gesamte Rest-Platz wird **gleichmaessig zwischen** den Items aufgeteilt.
Aussenrand ist 0.

## Wozu in der Praxis?

Logo links, Menue rechts -- der klassische Header-Stil. Auch für Pricing-
Tabellen, Footer-Spalten und Tag-Reihen das Standard-Werkzeug.

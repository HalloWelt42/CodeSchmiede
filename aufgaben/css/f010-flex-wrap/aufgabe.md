---
schema_version: 1
id: f010-flex-wrap
revision: 1
titel: "Flexbox 10: Umbruch in neue Zeile -- flex-wrap: wrap"
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
  <div class="teich"><div class="frosch a">A</div><div class="frosch b">B</div><div class="frosch c">C</div><div class="frosch d">D</div></div>
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
    flex-wrap: wrap;
  }
asserts:
  - selector: ".teich"
    property: display
    expected: "flex"
  - selector: ".teich"
    property: flex-wrap
    expected: "wrap"
hints:
  - kosten: 0
    text: |
      Flexbox-Eltern muss `display: flex` haben, damit `justify-content`, `align-items` & Co. greifen.
      Diese Aufgabe lehrt EINE Property -- die anderen kommen in den nächsten Levels.
  - kosten: 3
    text: |
      `display: flex;
        flex-wrap: wrap;`
starter_code: |
  .teich {
    display: flex;
    /* erlauben, dass Items in neue Zeilen umbrechen */
  }
---

# Flexbox 10: Vier Froesche, der vierte landet in einer zweiten Zeile, weil er nicht mehr in die erste passt

## Aufgabe

Im Teich-Rahmen sollen die drei Froesche so angeordnet werden, dass
**vier froesche, der vierte landet in einer zweiten zeile, weil er nicht mehr in die erste passt**.

Schreib **nur** die fehlende Flexbox-Anweisung in `.teich` -- der Rest
(Größe, Farbe, Quadrate) ist schon da.

## Aha

Standardmaessig ist `flex-wrap: nowrap` -- Items schrumpfen lieber, als
umzubrechen. Mit `wrap` brechen sie sauber in neue Zeilen um, sobald der
Platz nicht reicht.

## Wozu in der Praxis?

Tag-Clouds, responsive Galerien, Toolbar mit vielen Buttons auf schmalen
Bildschirmen -- überall wo eine Reihe zu lang werden kann, ist `flex-wrap`
die simple Antwort, ohne Media-Queries schreiben zu müssen.

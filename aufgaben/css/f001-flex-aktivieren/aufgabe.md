---
schema_version: 1
id: f001-flex-aktivieren
revision: 1
titel: "Flexbox 01: Flexbox einschalten"
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
  }
asserts:
  - selector: ".teich"
    property: display
    expected: "flex"
hints:
  - kosten: 0
    text: |
      Flexbox-Eltern muss `display: flex` haben, damit `justify-content`, `align-items` & Co. greifen.
      Diese Aufgabe lehrt EINE Property -- die anderen kommen in den nächsten Levels.
  - kosten: 3
    text: |
      `display: flex;`
starter_code: |
  .teich {
    /* hier eine Zeile einfuegen, damit der Teich zum Flexbox-Container wird */
  }
---

# Flexbox 01: Drei Froesche nebeneinander in einer Reihe stehen (statt untereinander)

## Aufgabe

Im Teich-Rahmen sollen die drei Froesche so angeordnet werden, dass
**drei froesche nebeneinander in einer reihe stehen (statt untereinander)**.

Schreib **nur** die fehlende Flexbox-Anweisung in `.teich` -- der Rest
(Größe, Farbe, Quadrate) ist schon da.

## Aha

Sobald du `display: flex` auf einen Container schreibst, werden alle direkten
Kinder zu Flex-Items. Standardmaessig stehen sie dann in einer Reihe von links
nach rechts und beginnen am linken Rand.

## Wozu in der Praxis?

Jede Navigations-Leiste, jede Card-Reihe, jede Toolbar nutzt `display: flex`.
Ohne Flexbox stehen Block-Elemente untereinander -- mit Flexbox lassen sie
sich beliebig anordnen, ohne dass man `float` oder `inline-block` quaelen muss.

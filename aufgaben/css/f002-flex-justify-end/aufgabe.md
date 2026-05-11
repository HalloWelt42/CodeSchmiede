---
schema_version: 1
id: f002-flex-justify-end
revision: 1
titel: "Flexbox 02: Alles rechts mit justify-content: flex-end"
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
    justify-content: flex-end;
  }
asserts:
  - selector: ".teich"
    property: display
    expected: "flex"
  - selector: ".teich"
    property: justify-content
    expected: "flex-end"
hints:
  - kosten: 0
    text: |
      Flexbox-Eltern muss `display: flex` haben, damit `justify-content`, `align-items` & Co. greifen.
      Diese Aufgabe lehrt EINE Property -- die anderen kommen in den nächsten Levels.
  - kosten: 3
    text: |
      `display: flex;
        justify-content: flex-end;`
starter_code: |
  .teich {
    display: flex;
    /* alles nach rechts schieben */
  }
---

# Flexbox 02: Drei Froesche stehen am rechten Rand

## Aufgabe

Im Teich-Rahmen sollen die drei Froesche so angeordnet werden, dass
**drei froesche stehen am rechten rand**.

Schreib **nur** die fehlende Flexbox-Anweisung in `.teich` -- der Rest
(Größe, Farbe, Quadrate) ist schon da.

## Aha

`justify-content` arbeitet auf der **Haupt-Achse** (bei row also horizontal).
`flex-end` schiebt alle Items ans Ende -- aber sie bleiben in ihrer Reihenfolge.

## Wozu in der Praxis?

Damit verschiebst du z.B. das User-Menue in einer Topbar nach rechts,
während das Logo links bleibt -- ein klassisches Layout-Pattern.

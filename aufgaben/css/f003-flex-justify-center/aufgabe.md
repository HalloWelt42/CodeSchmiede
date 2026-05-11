---
schema_version: 1
id: f003-flex-justify-center
revision: 1
titel: "Flexbox 03: Mittig mit justify-content: center"
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
  <div class="bahn"><div class="kachel a">A</div><div class="kachel b">B</div><div class="kachel c">C</div></div>
ziel_css: |
  .bahn {
    width: 400px;
    height: 120px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
  }
  .kachel {
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
  .bahn {
    display: flex;
    justify-content: center;
  }
asserts:
  - selector: ".bahn"
    property: display
    expected: "flex"
  - selector: ".bahn"
    property: justify-content
    expected: "center"
hints:
  - kosten: 0
    text: |
      Flexbox-Eltern muss `display: flex` haben, damit `justify-content`, `align-items` & Co. greifen.
      Diese Aufgabe lehrt EINE Property -- die anderen kommen in den nächsten Levels.
  - kosten: 3
    text: |
      `display: flex;
        justify-content: center;`
starter_code: |
  .bahn {
    display: flex;
    /* alle Items horizontal zentrieren */
  }
---

# Flexbox 03: Drei Kacheln sammeln sich in der Mitte

## Aufgabe

Im Bahn-Rahmen sollen die drei Kacheln so angeordnet werden, dass
**drei froesche sammeln sich in der mitte**.

Schreib **nur** die fehlende Flexbox-Anweisung in `.bahn` -- der Rest
(Größe, Farbe, Quadrate) ist schon da.

## Aha

`center` zieht alle Items in die Mitte der Haupt-Achse -- der **Abstand**
links und rechts entsteht automatisch, du brauchst keinen `margin`.

## Wozu in der Praxis?

Modale Dialoge, leere Zustände ('Noch keine Daten...'), Logo-Reihen --
alles wo Inhalte in der Mitte stehen sollen, nutzt diese Property.

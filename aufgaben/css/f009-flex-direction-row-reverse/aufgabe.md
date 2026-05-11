---
schema_version: 1
id: f009-flex-direction-row-reverse
revision: 1
titel: "Flexbox 09: Umgekehrte Reihenfolge -- row-reverse"
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
    flex-direction: row-reverse;
  }
asserts:
  - selector: ".bahn"
    property: display
    expected: "flex"
  - selector: ".bahn"
    property: flex-direction
    expected: "row-reverse"
hints:
  - kosten: 0
    text: |
      Flexbox-Eltern muss `display: flex` haben, damit `justify-content`, `align-items` & Co. greifen.
      Diese Aufgabe lehrt EINE Property -- die anderen kommen in den nächsten Levels.
  - kosten: 3
    text: |
      `display: flex;
        flex-direction: row-reverse;`
starter_code: |
  .bahn {
    display: flex;
    /* Reihenfolge der Items umdrehen */
  }
---

# Flexbox 09: Die DOM-Reihenfolge ist A-B-C, aber visuell siehst du C-B-A

## Aufgabe

Im Bahn-Rahmen sollen die drei Kacheln so angeordnet werden, dass
**die dom-reihenfolge ist a-b-c, aber visuell siehst du c-b-a**.

Schreib **nur** die fehlende Flexbox-Anweisung in `.bahn` -- der Rest
(Größe, Farbe, Quadrate) ist schon da.

## Aha

`row-reverse` kehrt die visuelle Reihenfolge um, **ohne den HTML-Code zu
verändern**. Das ist wichtig für Accessibility: Screen-Reader lesen
trotzdem die DOM-Reihenfolge A-B-C.

## Wozu in der Praxis?

Bei RTL-Sprachen (Arabisch, Hebraeisch) wechseln Layouts auf row-reverse.
Auch für Karussells, die nach links scrollen, oder Animation-Reihenfolgen
ist das ein Standard-Trick -- ohne den HTML-Code zu ändern.

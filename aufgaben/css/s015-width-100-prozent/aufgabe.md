---
schema_version: 1
id: s015-width-100-prozent
revision: 1
titel: "Grundlagen 15: width 100% -- Container voll ausnuetzen"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [grundlagen, lernpfad]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="container"><input class="feld" placeholder="Ueberall hin"></div>
ziel_css: |
  .container {
    width: 300px;
    padding: 12px;
    background-color: #22262d;
  }
  .feld {
    width: 100%;
    box-sizing: border-box;
    padding: 8px;
    background-color: #1a1d23;
    color: #e7ecf1;
    border: 1px solid #3a4049;
  }
asserts:
  - selector: ".feld"
    property: width
    expected: "276px"
  - selector: ".feld"
    property: box-sizing
    expected: "border-box"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `width: 100%; box-sizing: border-box;` -- letzteres ist schon gesetzt
starter_code: |
  .container {
    width: 300px;
    padding: 12px;
    background-color: #22262d;
  }
  .feld {
    box-sizing: border-box;
    padding: 8px;
    background-color: #1a1d23;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    /* hier dafuer sorgen, dass das Feld die volle Container-Breite einnimmt */
  }
---

# Grundlagen 15: Das Eingabefeld soll die volle Breite des Containers einnehmen, nicht nur die Default-Browser-Breite

## Aufgabe

Das Eingabefeld soll die volle Breite des Containers einnehmen, nicht nur die Default-Browser-Breite

## Aha

`width: 100%` macht ein Element so breit wie sein Eltern-Element
(genauer: dessen Inhaltsbreite). Bei `box-sizing: border-box` ist
Padding inklusive -- bei `content-box` würde das Feld überlaufen,
weil das Padding noch dazukommt. Daher gehen die beiden Properties
praktisch immer Hand in Hand.

## Wozu in der Praxis?

Form-Felder, die im ganzen Container 'liegen', Card-Footer-Buttons,
Bilder die volle Breite einnehmen sollen -- `width: 100%` ist das
Standard-Werkzeug. Mit `max-width` kombiniert: nimmt 100%, aber
nicht mehr als z.B. 600px.

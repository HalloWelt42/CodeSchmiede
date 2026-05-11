---
schema_version: 1
id: s013-box-sizing-border-box
revision: 1
titel: "Grundlagen 13: box-sizing -- Padding INNERHALB der Breite"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 10
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
  <div class="bsbb">200px breit -- inkl. Padding</div>
ziel_css: |
  .bsbb {
    box-sizing: border-box;
    width: 200px;
    padding: 20px;
    background-color: #2dd4bf;
    color: #1a1d23;
  }
asserts:
  - selector: ".bsbb"
    property: box-sizing
    expected: "border-box"
  - selector: ".bsbb"
    property: width
    expected: "200px"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `box-sizing: border-box;`
starter_code: |
  .bsbb {
    width: 200px;
    padding: 20px;
    background-color: #2dd4bf;
    color: #1a1d23;
    /* Padding soll IN der Breite enthalten sein -- box-sizing setzen */
  }
---

# Grundlagen 13: Mit border-box bleibt die Box trotz Padding genau 200px breit

## Aufgabe

Mit border-box bleibt die Box trotz Padding genau 200px breit

## Aha

Standard ist `box-sizing: content-box` -- da kommt das Padding ZU
der width dazu. Eine Box mit `width: 200px; padding: 20px` ist also
tatsächlich 240px breit. Mit `box-sizing: border-box` bleibt die
Box bei 200px -- das Padding wird vom Inhalt abgezogen. Das ist
intuitiver und der Grund, warum praktisch jedes Projekt mit
`* { box-sizing: border-box; }` startet.

## Wozu in der Praxis?

Ohne border-box muss man bei jeder Breitenrechnung Padding und Border
abziehen -- ein Albtraum bei responsiven Layouts. `box-sizing: border-
box` global setzen ist seit Jahren Best-Practice.

---
schema_version: 1
id: s014-border-radius
revision: 1
titel: "Grundlagen 14: Border-Radius -- abgerundete Ecken"
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
  <div class="rahmen">Mit Rahmen und Radius</div>
ziel_css: |
  .rahmen {
    width: 200px;
    padding: 16px;
    background-color: #22262d;
    color: #e7ecf1;
    border: 2px solid #2dd4bf;
    border-radius: 8px;
  }
asserts:
  - selector: ".rahmen"
    property: border-top-width
    expected: "2px"
  - selector: ".rahmen"
    property: border-top-color
    expected: "rgb(45, 212, 191)"
  - selector: ".rahmen"
    property: border-radius
    expected: "8px"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `border: 2px solid #2dd4bf; border-radius: 8px;`
starter_code: |
  .rahmen {
    width: 200px;
    padding: 16px;
    background-color: #22262d;
    color: #e7ecf1;
    /* hier 2px Petrol-Rahmen und 8px abgerundete Ecken */
  }
---

# Grundlagen 14: Die Box bekommt 2px Rahmen in Petrol und 8px Radius an den Ecken

## Aufgabe

Die Box bekommt 2px Rahmen in Petrol und 8px Radius an den Ecken

## Aha

`border` ist die Shorthand für Width, Style und Color in einem.
`border-radius` rundet die Ecken ab -- ein einzelner Wert wirkt auf
alle vier Ecken. Mit vier Werten (`border-radius: 8px 0 0 8px`)
bestimmst du jede Ecke einzeln (im Uhrzeigersinn von oben links).

## Wozu in der Praxis?

Borders trennen Cards von ihrem Hintergrund. Border-Radius weicht
harte rechteckige Optik auf -- praktisch jedes moderne UI nutzt
abgerundete Ecken bei Buttons, Cards, Inputs.

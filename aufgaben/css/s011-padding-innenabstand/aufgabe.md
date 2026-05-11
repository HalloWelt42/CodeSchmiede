---
schema_version: 1
id: s011-padding-innenabstand
revision: 1
titel: "Grundlagen 11: Padding -- Innenabstand zur Grenze"
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
  <div class="hervor">Inhalt mit Luft drumherum</div>
ziel_css: |
  .hervor {
    padding: 24px;
    background-color: #2dd4bf;
    color: #1a1d23;
    width: 200px;
  }
asserts:
  - selector: ".hervor"
    property: padding-top
    expected: "24px"
  - selector: ".hervor"
    property: padding-left
    expected: "24px"
  - selector: ".hervor"
    property: padding-right
    expected: "24px"
  - selector: ".hervor"
    property: padding-bottom
    expected: "24px"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `padding: 24px;`
starter_code: |
  .hervor {
    background-color: #2dd4bf;
    color: #1a1d23;
    width: 200px;
    /* hier 24px Padding rundum hinzufuegen */
  }
---

# Grundlagen 11: Die Box bekommt 24px Padding rundum -- Inhalt rückt vom Rand weg

## Aufgabe

Die Box bekommt 24px Padding rundum -- Inhalt rückt vom Rand weg

## Aha

**Padding** ist der Abstand zwischen Inhalt und Rahmen einer Box.
Es vergrößert die sichtbare Box (es sei denn, du nutzt `box-sizing:
border-box`). Padding ist **innerhalb** der Hintergrundfarbe -- wer
den Hintergrund der Box sieht, sieht auch das Padding.

## Wozu in der Praxis?

Ohne Padding klebt der Text an den Rändern -- haesslich und schwer
zu lesen. Buttons, Cards, Eingabefelder, Modals: alles braucht Padding.
Faustregel: 8/12/16/24/32 px sind die häufigsten Werte.

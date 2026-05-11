---
schema_version: 1
id: s006-adjacent-selektor
revision: 1
titel: "Grundlagen 06: Direkter Nachbar (+)"
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
  <article><h2>Titel</h2><p>Einleitung</p><p>Normaler Absatz</p><p>Noch normal</p></article>
ziel_css: |
  h2 + p {
    font-size: 18px;
    font-style: italic;
  }
asserts:
  - selector: "h2 + p"
    property: font-size
    expected: "18px"
  - selector: "h2 + p"
    property: font-style
    expected: "italic"
  - selector: "article p:nth-child(3)"
    property: font-style
    expected: "normal"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `h2 + p { font-size: 18px; font-style: italic; }`
starter_code: |
  /* Direkter Nachbar mit + */
---

# Grundlagen 06: Nur ein `<p>` direkt NACH einem `<h2>` soll Einleitungs-Stil bekommen (größer, italic)

## Aufgabe

Nur ein `<p>` direkt NACH einem `<h2>` soll Einleitungs-Stil bekommen (größer, italic)

## Aha

Der **Adjacent-Sibling-Selektor** `+` wählt nur das **direkt folgende**
Geschwister-Element vom selben Eltern. Hier: das `<p>`, das exakt nach
einem `<h2>` kommt -- nicht das übernächste.

## Wozu in der Praxis?

Klassischer Einsatz: ein Absatz nach einer Überschrift bekommt
anderen Stil (Lead-Paragraph). Auch für Form-Validierung:
`input:invalid + .fehlermeldung { display: block; }`.

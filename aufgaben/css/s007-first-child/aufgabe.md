---
schema_version: 1
id: s007-first-child
revision: 1
titel: "Grundlagen 07: Pseudoklasse :first-child"
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
  <ul><li>Erste Aufgabe</li><li>Zweite</li><li>Dritte</li></ul>
ziel_css: |
  li:first-child {
    font-weight: 700;
  }
asserts:
  - selector: "li:first-child"
    property: font-weight
    expected: "700"
  - selector: "li:nth-child(2)"
    property: font-weight
    expected: "400"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `li:first-child { font-weight: 700; }`
starter_code: |
  /* :first-child trifft das erste Kind seines Eltern-Elements */
---

# Grundlagen 07: Nur das ERSTE `<li>` in der Liste soll fett werden -- die anderen normal

## Aufgabe

Nur das ERSTE `<li>` in der Liste soll fett werden -- die anderen normal

## Aha

Pseudoklassen beginnen mit `:` und beschreiben einen **Zustand** oder
eine **Position** eines Elements. `:first-child` matched, wenn das
Element das erste Kind seines Eltern-Elements ist.

## Wozu in der Praxis?

Erstes Element in einer Tab-Bar markieren, Trennlinien zwischen
Listen-Eintraegen mit `:not(:first-child) { border-top: 1px solid }`,
Inhaltsverzeichnis mit Sondersystem für den ersten Punkt.

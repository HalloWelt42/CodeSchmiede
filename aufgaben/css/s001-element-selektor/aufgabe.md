---
schema_version: 1
id: s001-element-selektor
revision: 1
titel: "Grundlagen 01: Alle Notizen mit Element-Selektor faerben"
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
  <article><p>Erste Notiz</p><p>Zweite Notiz</p><p>Dritte Notiz</p></article>
ziel_css: |
  p {
    color: rgb(45, 212, 191);
  }
asserts:
  - selector: "article p:nth-child(1)"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: "article p:nth-child(3)"
    property: color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `p { color: rgb(45, 212, 191); }`
starter_code: |
  /* Schreibe einen Element-Selektor fuer alle <p> */
---

# Grundlagen 01: Alle `<p>`-Elemente sollen petrolfarben werden -- ohne Klassen, nur durch Element-Auswahl

## Aufgabe

Alle `<p>`-Elemente sollen petrolfarben werden -- ohne Klassen, nur durch Element-Auswahl

## Aha

Der einfachste Selektor ist der **Element-Selektor**: einfach den HTML-Tag-
Namen schreiben. Er trifft jedes Element dieses Typs auf der Seite.

## Wozu in der Praxis?

`body { font-family: ... }` und `a { color: ... }` sind klassische
Beispiele. Element-Selektoren bilden meist die Basis-Typografie eines
Designs -- alles weitere wird per Klasse oder Pseudoklasse verfeinert.

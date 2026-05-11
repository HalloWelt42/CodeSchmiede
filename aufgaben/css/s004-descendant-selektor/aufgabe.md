---
schema_version: 1
id: s004-descendant-selektor
revision: 1
titel: "Grundlagen 04: Verschachtelte Auswahl (Descendant)"
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
  <nav><a>Home</a><a>Ueber</a></nav><footer><a>Impressum</a></footer>
ziel_css: |
  nav a {
    color: rgb(45, 212, 191);
  }
asserts:
  - selector: "nav a:nth-child(1)"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: "nav a:nth-child(2)"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: "footer a"
    property: color
    expected: "rgb(231, 236, 241)"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `nav a { color: rgb(45, 212, 191); }`
starter_code: |
  /* Descendant: zwei Selektoren mit Leerzeichen dazwischen */
---

# Grundlagen 04: Nur `<a>`-Elemente innerhalb der `<nav>` sollen petrol werden -- der Footer-Link bleibt grau

## Aufgabe

Nur `<a>`-Elemente innerhalb der `<nav>` sollen petrol werden -- der Footer-Link bleibt grau

## Aha

Mit einem **Leerzeichen** zwischen Selektoren waehlst du nur Elemente
AUS einem Eltern-Element: `nav a` trifft alle `<a>` innerhalb von `<nav>`,
egal wie tief verschachtelt.

## Wozu in der Praxis?

Sehr oft: `header nav a`, `article p`, `.card .titel`. Damit kann man
denselben Element-Typ in verschiedenen Kontexten verschieden stylen --
ein Link im Header sieht anders aus als einer im Body-Text.

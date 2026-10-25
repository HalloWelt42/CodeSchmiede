---
schema_version: 1
id: s005-child-selektor
revision: 3
titel: "Grundlagen 05: Nur direkte Kinder (>)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [grundlagen, lernpfad]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <ul><li>Eins<ol><li>Verschachtelt</li></ol></li><li>Zwei</li><li>Drei</li></ul>
ziel_css: |
  ul > li {
    color: rgb(251, 146, 60);
  }
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizität und Quellreihenfolge.
  - kosten: 3
    text: |
      `ul > li { color: rgb(251, 146, 60); }`
starter_code: |
  /* Direct-child mit > */
---

# Grundlagen 05: Nur direkte Kind-`<li>` der `<ul>` sollen orange werden - die verschachtelten `<li>` bleiben grau

## Aufgabe

Nur direkte Kind-`<li>` der `<ul>` sollen orange werden - die verschachtelten `<li>` bleiben grau

## Aha

Mit `>` zwischen zwei Selektoren wählst du nur **direkte Kinder**.
Im Gegensatz zum Descendant-Selektor (Leerzeichen) gehst du nicht
tief in die Verschachtelung - nur die nächste Ebene zählt.
Achtung: das verschachtelte li ist hier orange weil es per Inheritance
die Farbe vom Eltern-li erbt - nicht weil der Selektor matcht.

## Wozu in der Praxis?

Klassisch in Menü-Strukturen: nur die Top-Level-Einträge bekommen
die Hauptfarbe, Submenü-Einträge werden separat gestyled. Auch
für Tabellen-Headers (`thead > tr > th`) sehr nützlich.

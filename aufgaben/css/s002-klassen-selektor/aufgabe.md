---
schema_version: 1
id: s002-klassen-selektor
revision: 1
titel: "Grundlagen 02: Nur die markierten Notizen faerben (Klasse)"
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
  <article><p>Normal</p><p class="wichtig">Wichtig</p><p>Normal</p><p class="wichtig">Wichtig</p></article>
ziel_css: |
  .wichtig {
    color: rgb(251, 146, 60);
  }
asserts:
  - selector: "article p:nth-child(2)"
    property: color
    expected: "rgb(251, 146, 60)"
  - selector: "article p:nth-child(4)"
    property: color
    expected: "rgb(251, 146, 60)"
  - selector: "article p:nth-child(1)"
    property: color
    expected: "rgb(231, 236, 241)"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `.wichtig { color: rgb(251, 146, 60); }`
starter_code: |
  /* Klassen-Selektor: Punkt + Klassenname */
---

# Grundlagen 02: Nur die `<p>`-Elemente mit Klasse 'wichtig' sollen orange werden

## Aufgabe

Nur die `<p>`-Elemente mit Klasse 'wichtig' sollen orange werden

## Aha

Der **Klassen-Selektor** beginnt mit einem Punkt: `.wichtig`.
Eine Klasse kann an beliebig vielen Elementen hängen -- so kannst du
Stile gezielt nur dort anwenden, wo du sie brauchst.

## Wozu in der Praxis?

Klassen sind das Brot-und-Butter-Werkzeug von CSS. Praktisch jeder
wiederverwendbare Stil bekommt eine Klasse: `.btn`, `.card`, `.alert`.
Frameworks wie Tailwind treiben das auf die Spitze.

---
schema_version: 1
id: s010-inheritance
revision: 1
titel: "Grundlagen 10: Vererbung -- color erbt sich auf Kinder"
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
  <article><h2>Titel</h2><p>Erster <span>Span</span> Absatz</p><ul><li>Listen-Eintrag</li></ul></article>
ziel_css: |
  article {
    color: rgb(45, 212, 191);
  }
asserts:
  - selector: "article"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: "article h2"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: "article p span"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: "article ul li"
    property: color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `article { color: rgb(45, 212, 191); }`
starter_code: |
  /* Nur article ansprechen -- alles darin erbt automatisch */
---

# Grundlagen 10: Setze color nur auf `<article>` -- alle Texte darin werden automatisch petrol

## Aufgabe

Setze color nur auf `<article>` -- alle Texte darin werden automatisch petrol

## Aha

Manche CSS-Properties **erben sich** automatisch auf Kind-Elemente:
`color`, `font-family`, `font-size`, `line-height`, `text-align`.
Andere wie `background`, `border`, `padding` erben sich NICHT --
die musst du pro Element neu setzen.

## Wozu in der Praxis?

Globale Typografie auf `body` setzen, dann erben alle Elemente.
Designs werden so konsistent ohne Wiederholung. `inherit` als
expliziter Wert zwingt eine Property zur Vererbung, falls nötig.

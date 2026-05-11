---
schema_version: 1
id: s008-nth-child
revision: 1
titel: "Grundlagen 08: Zebra-Streifen mit :nth-child(odd)"
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
  <table><tr><td>1</td></tr><tr><td>2</td></tr><tr><td>3</td></tr><tr><td>4</td></tr></table>
ziel_css: |
  tr:nth-child(odd) {
    background-color: rgb(34, 38, 45);
  }
asserts:
  - selector: "tr:nth-child(1)"
    property: background-color
    expected: "rgb(34, 38, 45)"
  - selector: "tr:nth-child(3)"
    property: background-color
    expected: "rgb(34, 38, 45)"
  - selector: "tr:nth-child(2)"
    property: background-color
    expected: "rgba(0, 0, 0, 0)"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `tr:nth-child(odd) { background-color: rgb(34, 38, 45); }`
starter_code: |
  /* :nth-child mit Schluesselwort odd, even oder Formel 2n+1 */
---

# Grundlagen 08: Jede zweite Tabellenzeile soll einen leicht abgesetzten Hintergrund bekommen

## Aufgabe

Jede zweite Tabellenzeile soll einen leicht abgesetzten Hintergrund bekommen

## Aha

`:nth-child()` ist die maechtigste Pseudoklasse für Position. Du
kannst Schlüsselwörter (`odd`, `even`) oder Formeln (`2n`, `3n+1`)
verwenden -- jedes 2., 3., oder n-te Element treffen.

## Wozu in der Praxis?

Zebra-Streifen in Tabellen sind der Klassiker. Aber auch Galerien
(jedes 4. Bild quer), Kalender (jedes 7. = Sonntag), Pricing-Tabellen
(mittlerer Eintrag highlighted) profitieren.

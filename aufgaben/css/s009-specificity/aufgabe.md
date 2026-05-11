---
schema_version: 1
id: s009-specificity
revision: 1
titel: "Grundlagen 09: Specificity-Konflikt -- Klasse schlaegt Element"
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
  <p class="hervor">Test-Text</p>
ziel_css: |
  p {
    color: rgb(231, 236, 241);
  }
  .hervor {
    color: rgb(45, 212, 191);
  }
asserts:
  - selector: ".hervor"
    property: color
    expected: "rgb(45, 212, 191)"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `.hervor { color: rgb(45, 212, 191); }`
starter_code: |
  p {
    color: rgb(231, 236, 241);
  }
  /* Hier eine Regel fuer .hervor schreiben, die p ueberschreibt */
---

# Grundlagen 09: Beide Regeln greifen -- aber die Klassen-Regel gewinnt, weil sie spezifischer ist

## Aufgabe

Beide Regeln greifen -- aber die Klassen-Regel gewinnt, weil sie spezifischer ist

## Aha

**Specificity** entscheidet bei Konflikten, welche Regel gewinnt.
Faustformel: ID (100) > Klasse/Pseudoklasse (10) > Element (1).
Eine Klassen-Regel überschreibt also IMMER eine Element-Regel,
egal in welcher Reihenfolge sie im Stylesheet stehen.

## Wozu in der Praxis?

Wenn ein Stil 'nicht greift' liegt es fast immer an Specificity.
Der DevTools-Inspector zeigt durchgestrichene Properties an, wenn
eine spezifischere Regel sie überschreibt -- super zum Debuggen.

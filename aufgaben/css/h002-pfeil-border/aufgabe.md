---
schema_version: 1
id: h002-pfeil-border
revision: 1
titel: "Challenge 02: Pfeil aus transparenten Borders"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 12
tags: [challenge, lernpfad, border-trick]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="pfeil"></div>
ziel_css: |
  .pfeil {
    width: 0;
    height: 0;
    border-top: 20px solid transparent;
    border-bottom: 20px solid transparent;
    border-left: 30px solid #2dd4bf;
  }
asserts:
  - selector: ".pfeil"
    property: width
    expected: "30px"
  - selector: ".pfeil"
    property: border-top-color
    expected: "rgba(0, 0, 0, 0)"
  - selector: ".pfeil"
    property: border-bottom-color
    expected: "rgba(0, 0, 0, 0)"
  - selector: ".pfeil"
    property: border-left-color
    expected: "rgb(45, 212, 191)"
  - selector: ".pfeil"
    property: border-left-width
    expected: "30px"
hints:
  - kosten: 0
    text: |
      Trick: Ein div mit width: 0, height: 0 und einem dicken Border ist visuell nur die Border. Wenn drei Border transparent sind und eine farbig, entsteht ein Dreieck. Hier soll der Pfeil nach rechts zeigen -- also farbig links, transparent oben/unten.
  - kosten: 6
    text: |
      `width: 0; height: 0; border-top: 20px solid transparent; border-bottom: 20px solid transparent; border-left: 30px solid #2dd4bf;`
starter_code: |
  .pfeil {
    /* width und height 0, drei transparente Borders + eine farbige links */
  }
---

# Challenge 02: Pfeil aus Borders

## Ziel

Erzeuge einen petrolfarbenen Pfeil, der nach **rechts** zeigt -- ohne
clip-path, ohne SVG, nur mit width/height/border.

## Aha

Wenn ein Element width: 0 und height: 0 hat, gibt es technisch keine
Innenflaeche. Die Borders treffen sich dann in der Mitte und bilden
Trapeze. Mit drei transparenten Borders entsteht ein einzelnes
Dreieck -- das ist der klassische 'CSS-Triangle-Trick'.

## Wozu in der Praxis?

Tooltip-Spitzen, Dropdown-Indikatoren, Speech-Bubble-Tails, Carousel-Pfeile.
Auch wenn heute oft SVG genutzt wird -- der Border-Trick ist Klassiker und
vollkommen ressourcenfrei (kein zusaetzliches Asset).

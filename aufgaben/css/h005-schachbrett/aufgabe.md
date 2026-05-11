---
schema_version: 1
id: h005-schachbrett
revision: 1
titel: "Challenge 05: Schachbrett-Hintergrund (repeating-Gradient)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [challenge, lernpfad, gradient, muster]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="brett"></div>
ziel_css: |
  .brett {
    width: 240px;
    height: 240px;
    background-color: #e7ecf1;
    background-image:
      linear-gradient(45deg, #1a1d23 25%, transparent 25%),
      linear-gradient(-45deg, #1a1d23 25%, transparent 25%),
      linear-gradient(45deg, transparent 75%, #1a1d23 75%),
      linear-gradient(-45deg, transparent 75%, #1a1d23 75%);
    background-size: 40px 40px;
    background-position: 0 0, 0 20px, 20px -20px, -20px 0px;
  }
asserts:
  - selector: ".brett"
    property: width
    expected: "240px"
  - selector: ".brett"
    property: background-size
    expected: "40px 40px, 40px 40px, 40px 40px, 40px 40px"
  - selector: ".brett"
    property: background-color
    expected: "rgb(231, 236, 241)"
hints:
  - kosten: 0
    text: |
      Klassisches CSS-Trick-Muster: vier überlagerte linear-gradients mit 45/-45deg ergeben Schachbrettfelder. Mit background-size definierst du die Feldgröße, background-position verschiebt die einzelnen Gradient-Layer gegeneinander.
  - kosten: 8
    text: |
      background-image akzeptiert eine Komma-Liste von Gradients, die übereinandergelegt werden. background-size + background-position regeln das Wiederhol-Raster.
starter_code: |
  .brett {
    width: 240px;
    height: 240px;
    background-color: #e7ecf1;
    /* vier linear-gradients fuer das Schachbrett-Muster, 40px-Tiles */
  }
---

# Challenge 05: Schachbrett

## Ziel

Ein 240x240-Quadrat mit hellem Hintergrund und dunklen Schachbrett-Feldern
(jeweils 20x20 px), nur per CSS-Gradients -- kein Bild.

## Aha

background-image akzeptiert mehrere Gradients in einer Komma-Liste. Jeder
Gradient wird als eigener Layer behandelt. Mit `background-size` legst du
die Kachel-Größe fest, mit `background-position` verschiebst du die
Layer gegeneinander. Vier 45-Grad-Gradients zusammen ergeben das
Schachbrett-Muster.

## Wozu in der Praxis?

Transparenz-Indikator (z.B. in Bildbearbeitungs-Tools), dekorative
Muster, Editor-Hintergruende. Praktisch alle 'gemusterten' Hintergruende
kommen via Gradient ohne ein Bild laden zu müssen.

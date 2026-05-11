---
schema_version: 1
id: h003-verlauf-diagonal
revision: 1
titel: "Challenge 03: Diagonaler Verlauf"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 8
tags: [challenge, lernpfad, gradient]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="kasten"></div>
ziel_css: |
  .kasten {
    width: 240px;
    height: 120px;
    background-image: linear-gradient(135deg, #2dd4bf 0%, #6366f1 100%);
  }
asserts:
  - selector: ".kasten"
    property: background-image
    expected: "linear-gradient(rgb(45, 212, 191) 0%, rgb(99, 102, 241) 100%)"
hints:
  - kosten: 0
    text: |
      linear-gradient(<winkel>, <farbe1>, <farbe2>) erzeugt einen Farbverlauf. Bei 135deg geht der Verlauf von oben-links nach unten-rechts (Diagonale).
  - kosten: 4
    text: |
      `background-image: linear-gradient(135deg, #2dd4bf 0%, #6366f1 100%);`
starter_code: |
  .kasten {
    width: 240px;
    height: 120px;
    /* hier: linearer Verlauf 135deg von #2dd4bf nach #6366f1 */
  }
---

# Challenge 03: Diagonaler Verlauf

## Ziel

Eine 240x120-Box mit einem diagonalen Farbverlauf von Petrol (oben-links)
nach Indigo (unten-rechts).

## Aha

linear-gradient ist ein Bild im Sinne von background-image -- es geht
nicht auf background-color. Wichtig: Winkel im CSS arbeiten anders als in
Mathematik: 0deg ist nach OBEN, 90deg ist nach RECHTS, 135deg geht nach
rechts-unten (Diagonale). Mit mehreren color-stops (50%, 80%, ...) kann man
komplexere Verlaeufe bauen.

## Wozu in der Praxis?

Hero-Hintergruende, Buttons (Hover-Glanz), Card-Effekte, Avatar-Standards
ohne Bild.

---
schema_version: 1
id: l004-split-login
revision: 1
titel: "Layout 04: Split-Screen mit Bild und Formular"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [layout, lernpfad, split, flexbox]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="split"><div class="visual">Bild</div><div class="form">Login-Form</div></div>
ziel_css: |
  .split {
    display: flex;
    width: 480px;
    height: 320px;
    border-radius: 8px;
    overflow: hidden;
  }
  .visual {
    flex: 1;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    font-size: 20px;
  }
  .form {
    flex: 1;
    background-color: #22262d;
    color: #e7ecf1;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 600;
  }
asserts:
  - selector: ".split"
    property: display
    expected: "flex"
  - selector: ".split"
    property: overflow
    expected: "hidden"
  - selector: ".visual"
    property: flex-grow
    expected: "1"
  - selector: ".form"
    property: flex-grow
    expected: "1"
hints:
  - kosten: 0
    text: |
      Zwei Spalten je 50% breit, beide mit eigenem Hintergrund. Container hat overflow: hidden damit der border-radius an den Aussen-Ecken sauber schneidet.
  - kosten: 4
    text: |
      Auf .split: `display: flex; overflow: hidden;` und auf .visual und .form jeweils `flex: 1;`
starter_code: |
  .split {
    width: 480px;
    height: 320px;
    border-radius: 8px;
    /* hier: flex-Container, overflow versteckt damit Radius sauber schneidet */
  }
  .visual {
    background-color: #2dd4bf;
    color: #1a1d23;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    font-size: 20px;
    /* je 1 Anteil */
  }
  .form {
    background-color: #22262d;
    color: #e7ecf1;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 600;
    /* je 1 Anteil */
  }
---

# Layout 04: Split-Screen

## Aufgabe

Zwei gleich breite Spalten -- links Petrol-Bild-Platzhalter, rechts
die Form. Die Aussen-Ecken sind abgerundet, ohne dass die inneren
Farben überlaufen.

## Aha

flex: 1 ist Kurzform für
flex-grow: 1 / flex-shrink: 1 / flex-basis: 0. Zwei Items mit
je flex: 1 teilen sich den Platz haelftig.

Der Trick mit overflow:
hidden auf dem Container: damit der border-radius greift, ohne
dass die Kind-Hintergruende drüber stehen.

## Wozu in der Praxis?

Login-Seiten, Onboarding, Editorial-Layouts mit Bild + Text.

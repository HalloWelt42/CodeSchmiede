---
schema_version: 1
id: c170-stepper
revision: 1
titel: "Stepper-Indikator (3 Schritte)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [stepper, wizard, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="step"><span class="punkt aktiv">1</span><span class="linie"></span><span class="punkt">2</span><span class="linie"></span><span class="punkt">3</span></div>
ziel_css: |
  .step {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .punkt {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background-color: #22262d;
    color: #9ca3af;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    border: 2px solid #3a4049;
  }
  .aktiv {
    background-color: #2dd4bf;
    color: #1a1d23;
    border-color: #2dd4bf;
  }
  .linie {
    flex: 1;
    height: 2px;
    background-color: #3a4049;
    min-width: 40px;
  }
asserts:
  - selector: ".step"
    property: display
    expected: "flex"
  - selector: ".step"
    property: gap
    expected: "8px"
  - selector: ".punkt"
    property: border-radius
    expected: "50%"
  - selector: ".punkt"
    property: width
    expected: "32px"
  - selector: ".aktiv"
    property: background-color
    expected: "rgb(45, 212, 191)"
  - selector: ".linie"
    property: height
    expected: "2px"
hints:
  - kosten: 0
    text: |
      Flex-Reihe mit Punkten (Kreis 32px) und Linien dazwischen.
starter_code: |
  .step {
    /* ... */
  }
  .punkt {
    /* ... */
  }
  .aktiv {
    /* ... */
  }
  .linie {
    /* ... */
  }
---

# Stepper-Indikator

3-Schritt-Anzeige mit Verbindungslinien (Schritt 1 aktiv).

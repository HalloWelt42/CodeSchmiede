---
schema_version: 1
id: c170-stepper
revision: 3
titel: "Stepper-Indikator (3 Schritte)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [stepper, wizard, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
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
    background-color: #f472b6;
    color: #1a1d23;
    border-color: #f472b6;
  }
  .linie {
    flex: 1;
    height: 2px;
    background-color: #3a4049;
    min-width: 40px;
  }
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

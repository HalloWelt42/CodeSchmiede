---
schema_version: 1
id: f015-flex-align-self
revision: 1
titel: "Flexbox 15: Ein Item anders ausrichten -- align-self"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [flexbox, lernpfad, align-self]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="teich"><div class="frosch">A</div><div class="frosch oben">B (oben)</div><div class="frosch">C</div></div>
ziel_css: |
  .teich {
    display: flex;
    align-items: center;
    width: 400px;
    height: 120px;
    background-color: #22262d;
    padding: 8px;
    gap: 8px;
  }
  .frosch {
    width: 80px;
    height: 60px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
  }
  .oben {
    align-self: flex-start;
    background-color: #fb923c;
  }
asserts:
  - selector: ".teich"
    property: align-items
    expected: "center"
  - selector: ".oben"
    property: align-self
    expected: "flex-start"
hints:
  - kosten: 0
    text: |
      Auf dem Container regelt `align-items` ALLE Items. Mit `align-self` auf
      einem einzelnen Item kannst du das **für dieses eine Item überschreiben**.
  - kosten: 4
    text: |
      Setze auf `.oben`: `align-self: flex-start;`
starter_code: |
  .teich {
    display: flex;
    align-items: center;
    width: 400px;
    height: 120px;
    background-color: #22262d;
    padding: 8px;
    gap: 8px;
  }
  .frosch {
    width: 80px;
    height: 60px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
  }
  .oben {
    background-color: #fb923c;
    /* nur dieses Item nach oben ausrichten */
  }
---

# Flexbox 15: Ein Item anders ausrichten

## Aufgabe

Der Teich richtet alle Froesche vertikal **mittig** aus.
**B soll als Ausnahme oben kleben** -- während A und C in der Mitte
bleiben.

## Aha

`align-self` ist die Item-Variante von `align-items`. Auf einem einzelnen
Flex-Item gesetzt, überschreibt es den Container-Wert nur für dieses Item.

## Wozu in der Praxis?

Header-Layouts: Logo zentriert vertikal, aber ein 'Sale!'-Badge soll oben
in der Ecke kleben. Oder Form-Felder mit Label: Submit-Button rechts unten
ausrichten während andere Buttons in der Mitte sitzen.

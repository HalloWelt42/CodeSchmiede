---
schema_version: 1
id: f014-flex-order
revision: 1
titel: "Flexbox 14: Reihenfolge ändern -- order"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [flexbox, lernpfad, order]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="teich"><div class="frosch">A</div><div class="frosch vorne">B (zuerst)</div><div class="frosch">C</div></div>
ziel_css: |
  .teich {
    display: flex;
    width: 400px;
    height: 80px;
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
  .vorne {
    order: -1;
    background-color: #fb923c;
  }
asserts:
  - selector: ".vorne"
    property: order
    expected: "-1"
hints:
  - kosten: 0
    text: |
      Jedes Flex-Item hat einen `order`-Wert (Default 0). Items werden nach
      `order` sortiert -- niedrige Werte zuerst. Negative Werte gehen ganz nach vorn.
  - kosten: 4
    text: |
      Setze auf `.vorne`: `order: -1;`
starter_code: |
  .teich {
    display: flex;
    width: 400px;
    height: 80px;
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
  .vorne {
    background-color: #fb923c;
    /* hier dafuer sorgen, dass dieses Item visuell zuerst kommt */
  }
---

# Flexbox 14: Reihenfolge ändern

## Aufgabe

Im DOM steht die Reihenfolge A-B-C. **B soll visuell aber
ganz links erscheinen** (B-A-C), ohne dass der HTML-Code geändert wird.

## Aha

`order` verändert nur die **visuelle** Reihenfolge -- die DOM-Reihenfolge
und damit Screen-Reader und Tab-Reihenfolge bleiben unverändert.
Achtung: Das kann für Accessibility heikel sein, wenn man übertreibt.

## Wozu in der Praxis?

Bei einer Card mit Bild oben (Mobile) und Bild rechts (Desktop) kann man
via Media-Query und `order` denselben HTML-Block in beiden Layouts nutzen.
Auch in Form-Layouts (Label vor/nach Input je nach Sprache).

---
schema_version: 1
id: c002-karte-zentriert
revision: 1
titel: Karte mittig per Flexbox
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [flexbox, zentrierung, layout]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- Flex-Center-Klassiker.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="rahmen">
    <div class="karte">Hallo</div>
  </div>
ziel_css: |
  .rahmen {
    width: 400px;
    height: 240px;
    background: rgb(34, 38, 45);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .karte {
    width: 160px;
    height: 100px;
    background: rgb(45, 212, 191);
    color: rgb(26, 29, 35);
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 600;
    border-radius: 6px;
  }
asserts:
  - selector: ".rahmen"
    property: display
    expected: "flex"
  - selector: ".rahmen"
    property: justify-content
    expected: "center"
  - selector: ".rahmen"
    property: align-items
    expected: "center"
  - selector: ".rahmen"
    property: width
    expected: "400px"
  - selector: ".rahmen"
    property: height
    expected: "240px"
  - selector: ".karte"
    property: width
    expected: "160px"
  - selector: ".karte"
    property: background-color
    expected: "rgb(45, 212, 191)"
  - selector: ".karte"
    property: border-radius
    expected: "6px"
hints:
  - kosten: 0
    text: |
      Auf dem Container `.rahmen`: `display: flex` plus
      `justify-content: center` (horizontal) und
      `align-items: center` (vertikal).
  - kosten: 4
    text: |
      Die Karte selbst bekommt feste Breite/Höhe und Hintergrundfarbe.
      Der Container muss eine Höhe haben, sonst kann es vertikal
      nichts zentrieren.
starter_code: |
  .rahmen {
    /* Hier zentrieren */
  }
  .karte {
    /* Karte stylen */
  }
---

# Karte mittig per Flexbox

Zentriere die `.karte` im Container `.rahmen` -- horizontal und
vertikal -- per Flexbox.

## Vorgaben

- Container: 400 × 240 px, dunkler Hintergrund
- Karte: 160 × 100 px, Petrol-Hintergrund, leicht abgerundet (6px)
- Karte sitzt exakt mittig im Container

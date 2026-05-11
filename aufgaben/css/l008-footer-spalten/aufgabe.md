---
schema_version: 1
id: l008-footer-spalten
revision: 1
titel: "Layout 08: Footer mit vier Link-Spalten"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [layout, lernpfad, footer, grid]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <footer class="fuss"><div class="block">Firma</div><div class="block">Produkt</div><div class="block">Hilfe</div><div class="block">Rechtliches</div></footer>
ziel_css: |
  .fuss {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    padding: 24px;
    background-color: #22262d;
    color: #e7ecf1;
    width: 480px;
    border-top: 1px solid #3a4049;
  }
  .block {
    font-size: 14px;
    font-weight: 600;
    color: #9ca3af;
  }
asserts:
  - selector: ".fuss"
    property: display
    expected: "grid"
  - selector: ".fuss"
    property: grid-template-columns
    expected: "96px 96px 96px 96px"
  - selector: ".fuss"
    property: gap
    expected: "16px"
  - selector: ".fuss"
    property: border-top-width
    expected: "1px"
hints:
  - kosten: 0
    text: |
      Vier gleich breite Spalten via repeat(4, 1fr). Heller Trenn-Strich oben grenzt den Footer vom Body ab.
  - kosten: 3
    text: |
      `grid-template-columns: repeat(4, 1fr);`
starter_code: |
  .fuss {
    display: grid;
    /* hier: 4 gleichbreite Spalten, 16px gap */
    padding: 24px;
    background-color: #22262d;
    color: #e7ecf1;
    width: 480px;
    /* hier: oben eine 1px-Linie als Trenner */
  }
  .block {
    font-size: 14px;
    font-weight: 600;
    color: #9ca3af;
  }
---

# Layout 08: Footer mit vier Spalten

## Aufgabe

Klassischer Webseiten-Footer mit vier Spalten Links nebeneinander.
Oben eine duenne Trenn-Linie zum Hauptinhalt.

## Aha

repeat(4, 1fr) ist die einfachste Art, eine gleichmaessige Spalten-
Aufteilung zu erreichen. Mit gap: 16px haben die Spalten ausreichend
Luft zwischen sich, ohne dass du margin schreiben musst.

## Wozu in der Praxis?

Praktisch jede Website hat genau so einen Footer.

---
schema_version: 1
id: l007-artikel-mit-toc
revision: 1
titel: "Layout 07: Artikel mit Inhaltsverzeichnis-Sidebar"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [layout, lernpfad, grid, sidebar]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="seite"><aside class="toc">TOC</aside><article class="text">Artikel-Text</article></div>
ziel_css: |
  .seite {
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 24px;
    width: 480px;
    padding: 16px;
    background-color: #1a1d23;
  }
  .toc {
    background-color: #22262d;
    color: #9ca3af;
    padding: 16px;
    border-radius: 4px;
    font-size: 14px;
    position: sticky; top: 16px;
    align-self: start;
  }
  .text {
    background-color: #22262d;
    color: #e7ecf1;
    padding: 16px;
    border-radius: 4px;
    min-height: 240px;
  }
asserts:
  - selector: ".seite"
    property: display
    expected: "grid"
  - selector: ".seite"
    property: grid-template-columns
    expected: "120px 304px"
  - selector: ".toc"
    property: position
    expected: "sticky"
  - selector: ".toc"
    property: align-self
    expected: "start"
hints:
  - kosten: 0
    text: |
      Zwei-Spalten-Layout: TOC fix 120px breit links, Artikel-Text rechts. Damit das TOC beim Scrollen sichtbar bleibt: position: sticky + align-self: start (sonst dehnt es sich Grid-bedingt).
  - kosten: 5
    text: |
      Auf .toc: `position: sticky; top: 16px; align-self: start;`
starter_code: |
  .seite {
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 24px;
    width: 480px;
    padding: 16px;
    background-color: #1a1d23;
  }
  .toc {
    background-color: #22262d;
    color: #9ca3af;
    padding: 16px;
    border-radius: 4px;
    font-size: 14px;
    /* hier: sticky + align-self: start, damit es beim Scroll klebt */
  }
  .text {
    background-color: #22262d;
    color: #e7ecf1;
    padding: 16px;
    border-radius: 4px;
    min-height: 240px;
  }
---

# Layout 07: Artikel + TOC

## Aufgabe

Schmale Sidebar links als Inhaltsverzeichnis, Haupt-Text rechts. Die
Sidebar soll beim Scrollen am oberen Rand kleben (sticky).

## Aha

Position sticky braucht ZWEI Sachen um zu funktionieren: 1) top-Wert
gesetzt, 2) das Eltern-Element darf nicht overflow: hidden haben.
Plus: in Grid muss das Item mit `align-self: start` versehen sein,
sonst dehnt es sich (default stretch) auf volle Höhe und sticky
hat keinen Effekt.

## Wozu in der Praxis?

Doku-Seiten, lange Artikel, Tutorial-Inhalte.

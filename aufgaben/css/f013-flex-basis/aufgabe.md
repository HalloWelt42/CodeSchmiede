---
schema_version: 1
id: f013-flex-basis
revision: 1
titel: "Flexbox 13: Start-Breite -- flex-basis"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [flexbox, lernpfad, flex-basis]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="bahn"><div class="kachel">A</div><div class="kachel breit">B (Basis 200px)</div><div class="kachel">C</div></div>
ziel_css: |
  .bahn {
    display: flex;
    width: 400px;
    height: 80px;
    background-color: #22262d;
    padding: 8px;
    gap: 8px;
  }
  .kachel {
    height: 60px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    flex-basis: 60px;
  }
  .breit {
    flex-basis: 200px;
    background-color: #a78bfa;
  }
asserts:
  - selector: ".breit"
    property: flex-basis
    expected: "200px"
hints:
  - kosten: 0
    text: |
      `flex-basis` ist die **Wunsch-Startbreite** eines Flex-Items, bevor
      `flex-grow` und `flex-shrink` den Rest verteilen. Ähnlich wie `width`,
      aber spezifisch für Flexbox.
  - kosten: 4
    text: |
      Setze auf `.breit`: `flex-basis: 200px;`
starter_code: |
  .bahn {
    display: flex;
    width: 400px;
    height: 80px;
    background-color: #22262d;
    padding: 8px;
    gap: 8px;
  }
  .kachel {
    height: 60px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    flex-basis: 60px;
  }
  .breit {
    background-color: #a78bfa;
    /* hier die Start-Breite auf 200px setzen */
  }
---

# Flexbox 13: Start-Breite

## Aufgabe

Alle drei Kacheln starten mit 60px Basis. **Der mittlere
soll mit 200px starten** -- er nimmt damit von Anfang an mehr Platz ein.

## Aha

`flex-basis` ist die **Vorschlags-Breite** -- der Browser nutzt sie als
Ausgangspunkt und passt sie dann mit `flex-grow`/`flex-shrink` an. Wenn
`flex-basis: auto` (Default), wird die natuerliche Breite des Inhalts genommen.

## Wozu in der Praxis?

Bei drei Karten in einer Reihe: jeder Karte 'startet mit 280px' (`flex-basis:
280px`), schrumpft wenn der Container schmal wird, waechst wenn breit -- das
ist die Grundlage von responsiven Card-Grids ohne Media-Queries.

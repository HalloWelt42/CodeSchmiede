---
schema_version: 1
id: h001-halbkreis
revision: 3
titel: "Challenge 01: Halbkreis nur mit border-radius"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 10
tags: [challenge, lernpfad, border-radius, trick]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="halbkreis"></div>
ziel_css: |
  .halbkreis {
    width: 120px;
    height: 60px;
    background-color: #f472b6;
    border-radius: 120px 120px 0 0;
  }
hints:
  - kosten: 0
    text: |
      border-radius akzeptiert pro Ecke einen Wert (im Uhrzeigersinn ab oben links). Mit großen Werten oben und 0 unten entsteht ein Halbkreis - Tasse von der Seite.
  - kosten: 5
    text: |
      `border-radius: 120px 120px 0 0;` oder `border-radius: 100% 100% 0 0;`
starter_code: |
  .halbkreis {
    width: 120px;
    height: 60px;
    background-color: #f472b6;
    /* oben rund, unten spitz */
  }
---

# Challenge 01: Halbkreis

## Ziel

Erzeuge mit einem einzigen leeren div einen oben-runden, unten-flachen
Halbkreis (wie die Kuppel einer Iglu oder die obere Hälfte einer Murmel).

## Aha

Border-radius ist nicht auf 'gleichmäßig abgerundet' beschränkt.
Die vier Ecken werden im Uhrzeigersinn ab oben-links spezifiziert - mit 0
auf einer Ecke wird sie scharf, mit großen Werten extrem rund.

## Wozu in der Praxis?

Datenvisualisierung (Gauges), Loader, Diagramm-Caps, dekorative Elemente.

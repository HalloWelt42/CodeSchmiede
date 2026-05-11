---
schema_version: 1
id: c001-button-pill
revision: 1
titel: Pill-Button mit Petrol-Akzent
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [button, padding, border-radius, farbe]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- klassischer Pill-Button.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <button class="btn">Klick mich</button>
ziel_css: |
  .btn {
    background: rgb(45, 212, 191);
    color: rgb(26, 29, 35);
    padding: 12px 24px;
    border: none;
    border-radius: 999px;
    font-weight: 600;
    cursor: pointer;
  }
asserts:
  - selector: ".btn"
    property: background-color
    expected: "rgb(45, 212, 191)"
  - selector: ".btn"
    property: color
    expected: "rgb(26, 29, 35)"
  - selector: ".btn"
    property: padding-top
    expected: "12px"
  - selector: ".btn"
    property: padding-left
    expected: "24px"
  - selector: ".btn"
    property: border-radius
    expected: "999px"
  - selector: ".btn"
    property: border-top-style
    expected: "none"
  - selector: ".btn"
    property: font-weight
    expected: "600"
hints:
  - kosten: 0
    text: |
      `border-radius: 999px` macht aus jedem Rechteck eine Pille.
      Achte auf Padding (vertikal/horizontal), Hintergrund-Farbe,
      und `border: none`.
  - kosten: 3
    text: |
      Eigenschaften: background, color, padding, border, border-radius,
      font-weight. Sieben Werte, sieben Asserts.
starter_code: |
  .btn {
    /* Dein CSS hier */
  }
---

# Pill-Button mit Petrol-Akzent

Style den Button so, dass er rund (Pille), petrol-türkis und mit
fettem dunklem Text erscheint -- ohne Rahmen, mit grosszügigem
Innenabstand.

## Vorgaben

- Hintergrund: `rgb(45, 212, 191)` (Codeschmiede-Petrol)
- Schrift: `rgb(26, 29, 35)`, fett (600)
- Innenabstand: 12px oben/unten, 24px links/rechts
- Form: vollständig abgerundet (Pille)
- Kein sichtbarer Rahmen

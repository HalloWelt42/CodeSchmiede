---
schema_version: 1
id: c001-button-pill
revision: 3
titel: Pill-Button mit Lavendel-Akzent
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [button, padding, border-radius, farbe]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - klassischer Pill-Button.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <button class="btn">Klick mich</button>
ziel_css: |
  .btn {
    background: rgb(167, 139, 250);
    color: rgb(26, 29, 35);
    padding: 12px 24px;
    border: none;
    border-radius: 999px;
    font-weight: 600;
    cursor: pointer;
  }
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

# Pill-Button mit Lavendel-Akzent

Style den Button so, dass er rund (Pille), lavendelfarben und mit
fettem dunklem Text erscheint - ohne Rahmen, mit großzügigem
Innenabstand.

## Vorgaben

- Hintergrund: `rgb(167, 139, 250)` (Codeschmiede-Lavendel)
- Schrift: `rgb(26, 29, 35)`, fett (600)
- Innenabstand: 12px oben/unten, 24px links/rechts
- Form: vollständig abgerundet (Pille)
- Kein sichtbarer Rahmen

---
schema_version: 1
id: c003-grid-zwei-spalten
revision: 3
titel: Zwei-Spalten-Grid mit Lücke
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 14
schaetz_minuten: 7
tags: [grid, layout, gap]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Grid-Basics.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="grid">
    <div class="zelle">A</div>
    <div class="zelle">B</div>
    <div class="zelle">C</div>
    <div class="zelle">D</div>
  </div>
ziel_css: |
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    width: 400px;
  }
  .zelle {
    background: rgb(56, 189, 248);
    color: rgb(26, 29, 35);
    padding: 24px;
    text-align: center;
    font-weight: 600;
    border-radius: 4px;
  }
hints:
  - kosten: 0
    text: |
      `display: grid` plus `grid-template-columns: 1fr 1fr` für zwei
      gleich breite Spalten. Lücken via `gap`.
  - kosten: 4
    text: |
      Die `.zelle` braucht background, color, padding (24px),
      text-align: center und font-weight: 600.
starter_code: |
  .grid {
    /* Grid mit zwei Spalten */
  }
  .zelle {
    /* Zelle stylen */
  }
---

# Zwei-Spalten-Grid mit Lücke

Vier Zellen sollen in einem 2x2-Grid angeordnet sein, mit gleichmäßigen
Lücken dazwischen.

## Vorgaben

- Container: 400px breit, 2 gleichbreite Spalten, 16px gap
- Zellen: Azur-Hintergrund, 24px Padding, zentrierter fetter Text
- 4 Zellen → 2 Reihen × 2 Spalten ergeben sich automatisch

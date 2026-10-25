---
schema_version: 1
id: c151-loader-dots
revision: 3
titel: "Loader: Drei Punkte"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [loader, dots, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="dots"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
ziel_css: |
  .dots {
    display: flex;
    gap: 8px;
  }
  .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: #fbbf24;
    display: inline-block;
  }
hints:
  - kosten: 0
    text: |
      Drei Gold-Punkte (12px Kreise) nebeneinander mit 8px Gap.
starter_code: |
  .dots {
    /* ... */
  }
  .dot {
    /* ... */
  }
---

# Loader: Drei Punkte

Drei Gold-Punkte als Lade-Indikator.

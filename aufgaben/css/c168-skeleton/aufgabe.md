---
schema_version: 1
id: c168-skeleton
revision: 3
titel: "Skeleton-Loader (statisch)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [skeleton, loader, platzhalter, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="skel"></div>
ziel_css: |
  .skel {
    width: 280px;
    height: 14px;
    background-color: #3a4049;
    border-radius: 4px;
    opacity: 0.6;
  }
hints:
  - kosten: 0
    text: |
      Schmale graue Leiste mit Opacity 0.6.
starter_code: |
  .skel {
    /* ... */
  }
---

# Skeleton-Loader

Grauer Platzhalter, der eine ladende Textzeile imitiert.

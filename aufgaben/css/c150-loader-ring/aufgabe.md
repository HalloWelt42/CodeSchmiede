---
schema_version: 1
id: c150-loader-ring
revision: 3
titel: "Loader: Spinner-Ring"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [loader, spinner, border, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="spinner"></div>
ziel_css: |
  .spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #22262d;
    border-top-color: #e879f9;
    border-radius: 50%;
  }
hints:
  - kosten: 0
    text: |
      Kreis (border-radius 50%) mit transparent-grauem Border, oben in Magenta.
starter_code: |
  .spinner {
    /* ... */
  }
---

# Loader: Spinner-Ring

Kreisförmiger Spinner mit magentafarbenem Top-Border.

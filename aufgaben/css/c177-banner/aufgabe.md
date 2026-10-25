---
schema_version: 1
id: c177-banner
revision: 3
titel: "Banner: Hinweis mit Icon"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [banner, info, flex, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="banner"><span class="icon">i</span><span class="text">Wichtiger Hinweis: heute Wartung um 18:00 Uhr.</span></div>
ziel_css: |
  .banner {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    background-color: #0891b2;
    color: #1a1d23;
    border-radius: 4px;
    font-weight: 500;
  }
  .icon {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background-color: #1a1d23;
    color: #0891b2;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    flex-shrink: 0;
  }
hints:
  - kosten: 0
    text: |
      Flex-Banner mit Icon-Kreis links und Text rechts.
starter_code: |
  .banner {
    /* ... */
  }
  .icon {
    /* ... */
  }
---

# Banner mit Icon

Info-Banner mit kreisrundem Icon und Text in einer Zeile.

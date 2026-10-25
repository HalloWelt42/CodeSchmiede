---
schema_version: 1
id: c161-hero-center
revision: 3
titel: "Hero: zentriertes Banner"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [hero, banner, flex-center, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <section class="hero"><h1 class="titel">Willkommen</h1></section>
ziel_css: |
  .hero {
    width: 600px;
    height: 200px;
    background-color: #22262d;
    color: #e7ecf1;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .titel {
    margin: 0;
    color: #c0ca33;
    font-size: 32px;
    font-weight: 700;
  }
hints:
  - kosten: 0
    text: |
      Hero als flex-center, 600x200. Titel in Oliv fett.
starter_code: |
  .hero {
    /* ... */
  }
  .titel {
    /* ... */
  }
---

# Hero: zentriertes Banner

Großes Banner mit zentriertem Oliv-Titel.

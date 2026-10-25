---
schema_version: 1
id: c164-pagination
revision: 3
titel: "Pagination"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [pagination, nav, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="pg"><button class="seite">1</button><button class="seite aktiv">2</button><button class="seite">3</button><button class="seite">4</button></div>
ziel_css: |
  .pg {
    display: flex;
    gap: 4px;
  }
  .seite {
    width: 32px;
    height: 32px;
    background-color: #22262d;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    border-radius: 4px;
    cursor: pointer;
  }
  .aktiv {
    background-color: #f59e0b;
    color: #1a1d23;
    border-color: #f59e0b;
    font-weight: 700;
  }
hints:
  - kosten: 0
    text: |
      Flex-Reihe mit 32x32 Buttons, aktive Seite in Bernstein.
starter_code: |
  .pg {
    /* ... */
  }
  .seite {
    /* ... */
  }
  .aktiv {
    /* ... */
  }
---

# Pagination

Seiten-Navigation mit hervorgehobener aktiver Seite.

---
schema_version: 1
id: c162-layout-zwei-spalten
revision: 3
titel: "Layout: zwei Spalten 30/70"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [layout, grid, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="layout"><aside class="seite">Sidebar</aside><main class="haupt">Inhalt</main></div>
ziel_css: |
  .layout {
    display: grid;
    grid-template-columns: 30% 70%;
    gap: 16px;
    width: 600px;
    height: 200px;
  }
  .seite {
    background-color: #22262d;
    color: #e7ecf1;
    padding: 16px;
  }
  .haupt {
    background-color: #e879f9;
    color: #1a1d23;
    padding: 16px;
  }
hints:
  - kosten: 0
    text: |
      Grid mit 30%/70%-Spalten, gap 16px.
starter_code: |
  .layout {
    /* ... */
  }
  .seite {
    /* ... */
  }
  .haupt {
    /* ... */
  }
---

# Layout: zwei Spalten 30/70

Klassisches Sidebar-Layout via CSS-Grid.

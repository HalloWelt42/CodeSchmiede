---
schema_version: 1
id: c095-filter-contrast
revision: 1
titel: "Filter: Kontrast 2x"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [filter, effekt]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="bild"></div>
ziel_css: |
  .bild {
    width: 120px;
    height: 120px;
    background-color: #2dd4bf;
    filter: contrast(2);
  }
asserts:
  - selector: ".bild"
    property: filter
    expected: "contrast(2)"
hints:
  - kosten: 0
    text: |
      `filter: contrast(2);`.
starter_code: |
  .bild {
    /* ... */
  }
---

# Filter: Kontrast 2x

Wende Filter Kontrast 2x an.

---
schema_version: 1
id: c094-filter-brightness
revision: 1
titel: "Filter: heller (1.5)"
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
    filter: brightness(1.5);
  }
asserts:
  - selector: ".bild"
    property: filter
    expected: "brightness(1.5)"
hints:
  - kosten: 0
    text: |
      `filter: brightness(1.5);`.
starter_code: |
  .bild {
    /* ... */
  }
---

# Filter: heller (1.5)

Wende Filter heller (1.5) an.

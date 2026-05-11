---
schema_version: 1
id: c098-filter-saturate
revision: 1
titel: "Filter: Sättigung 0.5"
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
    filter: saturate(0.5);
  }
asserts:
  - selector: ".bild"
    property: filter
    expected: "saturate(0.5)"
hints:
  - kosten: 0
    text: |
      `filter: saturate(0.5);`.
starter_code: |
  .bild {
    /* ... */
  }
---

# Filter: Sättigung 0.5

Wende Filter Sättigung 0.5 an.

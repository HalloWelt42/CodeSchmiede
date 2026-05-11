---
schema_version: 1
id: c131-tag-orange
revision: 1
titel: "Tag: Orange-Tag"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [tag, badge, pill, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <span class="tag">NEU</span>
ziel_css: |
  .tag {
    display: inline-block;
    background-color: #fb923c;
    color: #1a1d23;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
asserts:
  - selector: ".tag"
    property: background-color
    expected: "rgb(251, 146, 60)"
  - selector: ".tag"
    property: border-radius
    expected: "999px"
  - selector: ".tag"
    property: padding-top
    expected: "4px"
  - selector: ".tag"
    property: padding-left
    expected: "10px"
  - selector: ".tag"
    property: text-transform
    expected: "uppercase"
  - selector: ".tag"
    property: display
    expected: "inline-block"
hints:
  - kosten: 0
    text: |
      inline-block, kleines Padding, 999px-Radius, uppercase.
starter_code: |
  .tag {
    /* ... */
  }
---

# Tag: Orange-Tag

Kleines Pill-Tag in Orange-Tag mit Großbuchstaben.

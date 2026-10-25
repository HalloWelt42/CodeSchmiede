---
schema_version: 1
id: c029-flex-row-beides
revision: 3
titel: "Flex: horizontal+vertikal mittig"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [flexbox, layout]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="rahmen"><div class="kind"></div><div class="kind"></div><div class="kind"></div></div>
ziel_css: |
  .rahmen {
    width: 400px;
    height: 120px;
    background-color: #22262d;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .kind {
    width: 60px;
    height: 60px;
    background-color: #a78bfa;
  }
hints:
  - kosten: 0
    text: |
      Auf dem Container `.rahmen`: `display: flex`, dann
      `justify-content: center` und `align-items: center`.
starter_code: |
  .rahmen {
    /* ... */
  }
  .kind {
    /* ... */
  }
---

# Flex: horizontal+vertikal mittig

Drei Lavendel-Quadrate sollen im Container so angeordnet werden:
**horizontal+vertikal mittig**.

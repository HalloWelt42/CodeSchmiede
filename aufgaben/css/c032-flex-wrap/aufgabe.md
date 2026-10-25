---
schema_version: 1
id: c032-flex-wrap
revision: 3
titel: "Flex: wrap"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [flexbox, wrap]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="rahmen"><div class="kind"></div><div class="kind"></div><div class="kind"></div><div class="kind"></div></div>
ziel_css: |
  .rahmen {
    width: 200px;
    background-color: #22262d;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    padding: 12px;
  }
  .kind {
    width: 80px;
    height: 40px;
    background-color: #38bdf8;
  }
hints:
  - kosten: 0
    text: |
      `flex-wrap: wrap` erlaubt Umbruch in neue Zeilen.
starter_code: |
  .rahmen {
    /* ... */
  }
  .kind {
    /* ... */
  }
---

# Flex: wrap

Kinder sollen umbrechen, wenn sie nicht in eine Zeile passen.

---
schema_version: 1
id: c176-code-block
revision: 3
titel: "Code-Block"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [code-block, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <pre class="code">def hallo():
      return "welt"</pre>
ziel_css: |
  .code {
    margin: 0;
    padding: 16px;
    background-color: #1a1d23;
    color: #f59e0b;
    font-family: monospace;
    border-radius: 6px;
    overflow-x: auto;
  }
hints:
  - kosten: 0
    text: |
      Dunkler Hintergrund, Bernstein-Schrift, Monospace-Font, abgerundet.
starter_code: |
  .code {
    /* ... */
  }
---

# Code-Block

Monospace-Block für Quellcode mit dunklem Hintergrund.

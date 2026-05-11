---
schema_version: 1
id: c172-sticky-footer
revision: 1
titel: "Sticky-Footer-Layout"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [layout, sticky-footer, flex-column, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="seite"><header class="kopf">Header</header><main class="haupt">Inhalt</main><footer class="fuss">Footer</footer></div>
ziel_css: |
  .seite {
    display: flex;
    flex-direction: column;
    width: 400px;
    height: 300px;
  }
  .kopf {
    background-color: #22262d;
    color: #e7ecf1;
    padding: 12px;
  }
  .haupt {
    flex: 1;
    background-color: #1a1d23;
    color: #e7ecf1;
    padding: 12px;
  }
  .fuss {
    background-color: #22262d;
    color: #9ca3af;
    padding: 12px;
    font-size: 12px;
  }
asserts:
  - selector: ".seite"
    property: display
    expected: "flex"
  - selector: ".seite"
    property: flex-direction
    expected: "column"
  - selector: ".seite"
    property: height
    expected: "300px"
  - selector: ".haupt"
    property: flex-grow
    expected: "1"
hints:
  - kosten: 0
    text: |
      Seite als flex-column. Haupt mit flex:1 dehnt sich zwischen Header und Footer.
starter_code: |
  .seite {
    /* ... */
  }
  .kopf {
    /* ... */
  }
  .haupt {
    /* ... */
  }
  .fuss {
    /* ... */
  }
---

# Sticky-Footer-Layout

Footer klebt am unteren Rand, Inhalt füllt den Rest.

---
schema_version: 1
id: c173-modal
revision: 1
titel: "Modal-Dialog"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [modal, dialog, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="hintergrund"><div class="dialog"><h3 class="titel">Bestätigen</h3><p class="text">Wirklich löschen?</p></div></div>
ziel_css: |
  .hintergrund {
    width: 500px;
    height: 300px;
    background-color: rgba(0, 0, 0, 0.6);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .dialog {
    width: 320px;
    padding: 24px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 8px;
    box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.4);
  }
  .titel {
    margin: 0 0 8px;
    color: #2dd4bf;
  }
  .text {
    margin: 0;
    color: #9ca3af;
  }
asserts:
  - selector: ".hintergrund"
    property: background-color
    expected: "rgba(0, 0, 0, 0.6)"
  - selector: ".hintergrund"
    property: display
    expected: "flex"
  - selector: ".dialog"
    property: width
    expected: "320px"
  - selector: ".dialog"
    property: padding-top
    expected: "24px"
  - selector: ".dialog"
    property: border-radius
    expected: "8px"
  - selector: ".dialog"
    property: box-shadow
    expected: "rgba(0, 0, 0, 0.4) 0px 8px 24px 0px"
hints:
  - kosten: 0
    text: |
      Halbtransparenter Backdrop (rgba 60%). Dialog 320px breit, abgerundet, Schatten.
starter_code: |
  .hintergrund {
    /* ... */
  }
  .dialog {
    /* ... */
  }
  .titel {
    /* ... */
  }
  .text {
    /* ... */
  }
---

# Modal-Dialog

Klassischer Dialog mit halbtransparentem Hintergrund.

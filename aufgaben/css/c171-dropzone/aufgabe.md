---
schema_version: 1
id: c171-dropzone
revision: 1
titel: "Drop-Zone (gestrichelt)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [drop-zone, upload, border-dashed, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="drop">Datei hier ablegen</div>
ziel_css: |
  .drop {
    width: 320px;
    height: 160px;
    border: 2px dashed #2dd4bf;
    border-radius: 8px;
    background-color: #22262d;
    color: #9ca3af;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
asserts:
  - selector: ".drop"
    property: width
    expected: "320px"
  - selector: ".drop"
    property: height
    expected: "160px"
  - selector: ".drop"
    property: border-top-style
    expected: "dashed"
  - selector: ".drop"
    property: border-top-color
    expected: "rgb(45, 212, 191)"
  - selector: ".drop"
    property: display
    expected: "flex"
  - selector: ".drop"
    property: justify-content
    expected: "center"
hints:
  - kosten: 0
    text: |
      320x160, gestrichelter Petrol-Rand, Inhalt zentriert.
starter_code: |
  .drop {
    /* ... */
  }
---

# Drop-Zone

Gestrichelte Box als Datei-Upload-Ziel.

---
schema_version: 1
id: c144-alert-warn
revision: 1
titel: "Alert: Warnung"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [alert, notification, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="alert">Warnung-Meldung</div>
ziel_css: |
  .alert {
    padding: 12px 16px;
    background-color: #22262d;
    color: #e7ecf1;
    border-left: 4px solid #fb923c;
    border-radius: 4px;
  }
asserts:
  - selector: ".alert"
    property: padding-top
    expected: "12px"
  - selector: ".alert"
    property: padding-left
    expected: "16px"
  - selector: ".alert"
    property: border-radius
    expected: "4px"
  - selector: ".alert"
    property: border-left-color
    expected: "rgb(251, 146, 60)"
  - selector: ".alert"
    property: border-left-width
    expected: "4px"
hints:
  - kosten: 0
    text: |
      Linker Streifen 4px in Warnung-Farbe.
starter_code: |
  .alert {
    /* ... */
  }
---

# Alert: Warnung

Benachrichtigung mit linkem Farbstreifen (Warnung).

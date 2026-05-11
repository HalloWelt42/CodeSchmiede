---
schema_version: 1
id: c157-form-textarea
revision: 1
titel: "Form: Textarea"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [form, textarea, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <textarea class="eingabe" placeholder="Notiz"></textarea>
ziel_css: |
  .eingabe {
    width: 280px;
    height: 120px;
    padding: 12px;
    background-color: #22262d;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    border-radius: 4px;
    resize: vertical;
  }
asserts:
  - selector: ".eingabe"
    property: width
    expected: "280px"
  - selector: ".eingabe"
    property: height
    expected: "120px"
  - selector: ".eingabe"
    property: padding-top
    expected: "12px"
  - selector: ".eingabe"
    property: resize
    expected: "vertical"
hints:
  - kosten: 0
    text: |
      280x120, padding 12, resize: vertical.
starter_code: |
  .eingabe {
    /* ... */
  }
---

# Form: Textarea

Mehrzeiliges Eingabefeld mit fester Größe und nur vertikalem Resize.

---
schema_version: 1
id: c156-form-input
revision: 3
titel: "Form: Text-Input"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [form, input, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <input class="eingabe" placeholder="Name">
ziel_css: |
  .eingabe {
    width: 240px;
    padding: 8px 12px;
    background-color: #22262d;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    border-radius: 4px;
    font-size: 14px;
  }
hints:
  - kosten: 0
    text: |
      240px breit, 8/12 Padding, 4px Radius, dunkler Hintergrund + dezenter Border.
starter_code: |
  .eingabe {
    /* ... */
  }
---

# Form: Text-Input

Dunkles Eingabefeld mit dezentem Border und 4px Radius.

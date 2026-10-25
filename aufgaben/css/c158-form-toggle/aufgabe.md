---
schema_version: 1
id: c158-form-toggle
revision: 3
titel: "Form: Toggle-Switch (statisch)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [form, toggle, switch, komponente]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <label class="switch"><span class="track"><span class="thumb"></span></span></label>
ziel_css: |
  .switch {
    display: inline-block;
  }
  .track {
    display: block;
    width: 48px;
    height: 24px;
    background-color: #38bdf8;
    border-radius: 999px;
    position: relative;
  }
  .thumb {
    position: absolute;
    top: 2px;
    left: 26px;
    width: 20px;
    height: 20px;
    background-color: #1a1d23;
    border-radius: 50%;
  }
hints:
  - kosten: 0
    text: |
      Track 48x24 mit 999px Radius. Thumb 20x20 Kreis, absolut positioniert rechts.
starter_code: |
  .switch {
    /* ... */
  }
  .track {
    /* ... */
  }
  .thumb {
    /* ... */
  }
---

# Form: Toggle-Switch (statisch)

Ein/Aus-Schalter im 'an'-Zustand (statisches Layout, ohne Interaktion).

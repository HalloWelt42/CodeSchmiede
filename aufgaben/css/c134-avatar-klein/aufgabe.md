---
schema_version: 1
id: c134-avatar-klein
revision: 1
titel: "Avatar: klein (32px)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [avatar, kreis, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="avatar">A</div>
ziel_css: |
  .avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
  }
asserts:
  - selector: ".avatar"
    property: width
    expected: "32px"
  - selector: ".avatar"
    property: height
    expected: "32px"
  - selector: ".avatar"
    property: border-radius
    expected: "50%"
  - selector: ".avatar"
    property: display
    expected: "flex"
  - selector: ".avatar"
    property: justify-content
    expected: "center"
  - selector: ".avatar"
    property: align-items
    expected: "center"
hints:
  - kosten: 0
    text: |
      32x32, 50% Radius, flex-zentriert.
starter_code: |
  .avatar {
    /* ... */
  }
---

# Avatar klein

Kreisförmiger Avatar mit Initiale in 32px.

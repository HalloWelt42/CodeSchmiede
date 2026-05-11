---
schema_version: 1
id: c163-breadcrumb
revision: 1
titel: "Breadcrumb-Pfad"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [breadcrumb, nav, komponente]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <nav class="bc"><a class="link">Home</a><span class="sep">/</span><a class="link">Aufgaben</a><span class="sep">/</span><span class="aktuell">Detail</span></nav>
ziel_css: |
  .bc {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
  }
  .link {
    color: #2dd4bf;
    text-decoration: none;
  }
  .sep {
    color: #9ca3af;
  }
  .aktuell {
    color: #e7ecf1;
    font-weight: 600;
  }
asserts:
  - selector: ".bc"
    property: display
    expected: "flex"
  - selector: ".bc"
    property: gap
    expected: "8px"
  - selector: ".link"
    property: color
    expected: "rgb(45, 212, 191)"
  - selector: ".aktuell"
    property: font-weight
    expected: "600"
hints:
  - kosten: 0
    text: |
      Flex-Reihe mit gap 8px, Links in Petrol, aktueller Eintrag fett.
starter_code: |
  .bc {
    /* ... */
  }
  .link {
    /* ... */
  }
  .sep {
    /* ... */
  }
  .aktuell {
    /* ... */
  }
---

# Breadcrumb-Pfad

Navigations-Pfad mit Trennern und hervorgehobenem aktuellem Eintrag.

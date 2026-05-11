---
schema_version: 1
id: l001-app-shell-grid
revision: 1
titel: "Layout 01: App-Shell mit grid-template-areas"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [layout, lernpfad, grid, template-areas]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="app"><header class="kopf">Header</header><nav class="seite">Sidebar</nav><main class="haupt">Inhalt</main><footer class="fuss">Footer</footer></div>
ziel_css: |
  .app {
    display: grid;
    grid-template-columns: 160px 1fr;
    grid-template-rows: 60px 1fr 40px;
    grid-template-areas:
      "kopf kopf"
      "seite haupt"
      "fuss fuss";
    width: 480px;
    height: 320px;
    gap: 4px;
    background-color: #1a1d23;
  }
  .kopf { grid-area: kopf; background-color: #2dd4bf; color: #1a1d23; }
  .seite { grid-area: seite; background-color: #22262d; color: #e7ecf1; }
  .haupt { grid-area: haupt; background-color: #2a2f37; color: #e7ecf1; }
  .fuss { grid-area: fuss; background-color: #22262d; color: #9ca3af; }
  .kopf, .seite, .haupt, .fuss {
    display: flex; align-items: center; justify-content: center;
    font-weight: 600;
  }
asserts:
  - selector: ".app"
    property: display
    expected: "grid"
  - selector: ".app"
    property: grid-template-rows
    expected: "60px 212px 40px"
  - selector: ".kopf"
    property: grid-area
    expected: "kopf"
  - selector: ".haupt"
    property: grid-area
    expected: "haupt"
hints:
  - kosten: 0
    text: |
      Klassisches App-Layout: Header oben (über alles), Sidebar links, Inhalt rechts, Footer unten (über alles).
      Mit grid-template-areas zeichnest du das Layout direkt im CSS.
  - kosten: 5
    text: |
      grid-template-areas:
        "kopf kopf"
        "seite haupt"
        "fuss fuss";
starter_code: |
  .app {
    display: grid;
    grid-template-columns: 160px 1fr;
    grid-template-rows: 60px 1fr 40px;
    /* hier grid-template-areas mit 3 Zeilen je 2 Spalten */
    width: 480px;
    height: 320px;
    gap: 4px;
    background-color: #1a1d23;
  }
  .kopf { background-color: #2dd4bf; color: #1a1d23; /* Area */ }
  .seite { background-color: #22262d; color: #e7ecf1; /* Area */ }
  .haupt { background-color: #2a2f37; color: #e7ecf1; /* Area */ }
  .fuss { background-color: #22262d; color: #9ca3af; /* Area */ }
  .kopf, .seite, .haupt, .fuss {
    display: flex; align-items: center; justify-content: center;
    font-weight: 600;
  }
---

# Layout 01: App-Shell mit grid-template-areas

## Aufgabe

Klassische App-Struktur in 3 Zeilen und 2 Spalten:
- Header oben (volle Breite)
- Sidebar links (160px), Inhalt rechts (Rest)
- Footer unten (volle Breite)

## Aha

Mit grid-template-areas siehst du das Layout direkt im CSS
als ASCII-Skizze. Jedes Item bekommt per `grid-area` einen Namen
zugewiesen -- die Zuordnung ist deklarativ und auf einen Blick lesbar.

## Wozu in der Praxis?

Admin-Panels, Mail-Clients, IDEs, Dashboards --
praktisch jede Web-App startet mit so einer Shell.

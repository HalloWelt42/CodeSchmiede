---
schema_version: 1
id: l009-topbar-drei-zonen
revision: 1
titel: "Layout 09: Topbar mit Logo, Menu und Avatar"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 7
tags: [layout, lernpfad, navigation, flexbox]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <header class="topbar"><div class="logo">Marke</div><nav class="menu"><a class="link">Home</a><a class="link">Preise</a><a class="link">Doku</a></nav><div class="avatar">JS</div></header>
ziel_css: |
  .topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
    height: 60px;
    background-color: #22262d;
    border-bottom: 1px solid #3a4049;
    width: 600px;
  }
  .logo {
    color: #2dd4bf;
    font-weight: 700;
    font-size: 18px;
  }
  .menu {
    display: flex;
    gap: 24px;
  }
  .link {
    color: #e7ecf1;
    font-weight: 500;
  }
  .avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background-color: #2dd4bf;
    color: #1a1d23;
    font-weight: 700;
    display: flex; justify-content: center; align-items: center;
  }
asserts:
  - selector: ".topbar"
    property: display
    expected: "flex"
  - selector: ".topbar"
    property: justify-content
    expected: "space-between"
  - selector: ".topbar"
    property: align-items
    expected: "center"
  - selector: ".menu"
    property: display
    expected: "flex"
  - selector: ".menu"
    property: gap
    expected: "24px"
  - selector: ".avatar"
    property: border-radius
    expected: "50%"
hints:
  - kosten: 0
    text: |
      Drei Elemente in einer Zeile: Logo links, Menu mittig (wandert mit), Avatar rechts. Mit justify-content: space-between kleben Logo und Avatar an den Rändern, das Menu landet in der Mitte. Menu selbst auch flex für Gap zwischen Links.
  - kosten: 5
    text: |
      Auf .topbar: `display: flex; justify-content: space-between; align-items: center;`
      Auf .menu: `display: flex; gap: 24px;`
starter_code: |
  .topbar {
    padding: 0 20px;
    height: 60px;
    background-color: #22262d;
    border-bottom: 1px solid #3a4049;
    width: 600px;
    /* hier: flex mit space-between und vertikal zentriert */
  }
  .logo {
    color: #2dd4bf;
    font-weight: 700;
    font-size: 18px;
  }
  .menu {
    /* hier: flex-Reihe mit 24px gap zwischen den Links */
  }
  .link {
    color: #e7ecf1;
    font-weight: 500;
  }
  .avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background-color: #2dd4bf;
    color: #1a1d23;
    font-weight: 700;
    display: flex; justify-content: center; align-items: center;
  }
---

# Layout 09: Topbar in drei Zonen

## Aufgabe

Eine klassische Topbar: Marken-Logo links, Hauptmenue in der Mitte,
User-Avatar rechts.

## Aha

space-between mit drei Items verteilt: erstes ganz links, letztes
ganz rechts, mittlere(s) Item(s) bekommen den verteilten Restplatz.
Bei genau drei Items wirkt das wie 'mittig'.

## Wozu in der Praxis?

Praktisch jede SaaS-App, jede Marketing-Site, jedes Dashboard.

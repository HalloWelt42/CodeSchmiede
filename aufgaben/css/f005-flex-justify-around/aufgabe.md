---
schema_version: 1
id: f005-flex-justify-around
revision: 1
titel: "Flexbox 05: Mit Aussenrand -- space-around"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [flexbox, lernpfad]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="bahn"><div class="kachel a">A</div><div class="kachel b">B</div><div class="kachel c">C</div></div>
ziel_css: |
  .bahn {
    width: 400px;
    height: 120px;
    background-color: #22262d;
    border: 1px solid #3a4049;
    padding: 8px;
  }
  .kachel {
    width: 60px;
    height: 60px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    margin: 4px;
  }
  .bahn {
    display: flex;
    justify-content: space-around;
  }
asserts:
  - selector: ".bahn"
    property: display
    expected: "flex"
  - selector: ".bahn"
    property: justify-content
    expected: "space-around"
hints:
  - kosten: 0
    text: |
      Flexbox-Eltern muss `display: flex` haben, damit `justify-content`, `align-items` & Co. greifen.
      Diese Aufgabe lehrt EINE Property -- die anderen kommen in den nächsten Levels.
  - kosten: 3
    text: |
      `display: flex;
        justify-content: space-around;`
starter_code: |
  .bahn {
    display: flex;
    /* jedes Item bekommt links + rechts den gleichen Rand */
  }
---

# Flexbox 05: Jeder Kachel hat links und rechts gleich viel Platz

## Aufgabe

Im Bahn-Rahmen sollen die drei Kacheln so angeordnet werden, dass
**jeder kachel hat links und rechts gleich viel platz**.

Schreib **nur** die fehlende Flexbox-Anweisung in `.bahn` -- der Rest
(Größe, Farbe, Quadrate) ist schon da.

## Aha

`space-around` gibt jedem Item links und rechts die selbe **Polsterung**.
Achtung: die Polsterungen zwischen zwei Items addieren sich -- die
Mittel-Lücken sind doppelt so groß wie die zum Aussenrand.

## Wozu in der Praxis?

Bottom-Tab-Bars in Mobile-Apps nutzen `space-around` -- damit jeder Button
rundum gleichmaessig Platz hat, auch zum Rand der App hin.

---
schema_version: 1
id: f011-flex-grow
revision: 1
titel: "Flexbox 11: Ein Item waechst -- flex-grow: 1"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [flexbox, lernpfad, flex-grow]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="bahn"><div class="kachel fest">A</div><div class="kachel flex">B (waechst)</div><div class="kachel fest">C</div></div>
ziel_css: |
  .bahn {
    display: flex;
    width: 400px;
    height: 100px;
    background-color: #22262d;
    padding: 8px;
    gap: 8px;
  }
  .kachel {
    height: 60px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
  }
  .fest {
    width: 60px;
  }
  .flex {
    flex-grow: 1;
  }
asserts:
  - selector: ".flex"
    property: flex-grow
    expected: "1"
  - selector: ".bahn"
    property: display
    expected: "flex"
hints:
  - kosten: 0
    text: |
      `flex-grow` auf einem Item gibt an, **wieviel vom Restplatz** das Item nimmt.
      Alle Items mit `flex-grow: 0` (Default) bleiben bei ihrer Wunsch-Breite.
  - kosten: 4
    text: |
      Setze auf `.flex`: `flex-grow: 1;`
starter_code: |
  .bahn {
    display: flex;
    width: 400px;
    height: 100px;
    background-color: #22262d;
    padding: 8px;
    gap: 8px;
  }
  .kachel {
    height: 60px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
  }
  .fest {
    width: 60px;
  }
  .flex {
    /* hier dafuer sorgen, dass dieses Item den Rest-Platz nimmt */
  }
---

# Flexbox 11: Ein Item waechst

## Aufgabe

A und C haben feste Breiten. **B (das mittlere) soll den
gesamten Rest-Platz fuellen** -- egal wie breit der Container ist.

## Aha

`flex-grow: 1` auf einem Item heisst: 'nimm den ganzen Rest für
dich'. Mehrere Items mit `flex-grow: 1` teilen sich den Rest gleichmaessig.
Mit `flex-grow: 2` vs `flex-grow: 1` bekommt das eine das Doppelte.

## Wozu in der Praxis?

Sidebar (fest) + Hauptinhalt (waechst) ist das klassische Beispiel. Auch
ein Such-Input neben einem 'Suchen'-Button: Input mit `flex-grow: 1` dehnt
sich aus, der Button bleibt schmal.

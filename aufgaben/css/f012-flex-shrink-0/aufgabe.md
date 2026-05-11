---
schema_version: 1
id: f012-flex-shrink-0
revision: 1
titel: "Flexbox 12: Schrumpfen verhindern -- flex-shrink: 0"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [flexbox, lernpfad, flex-shrink]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="bahn"><div class="kachel">A</div><div class="kachel fix">B (bleibt)</div><div class="kachel">C</div></div>
ziel_css: |
  .bahn {
    display: flex;
    width: 280px;
    height: 80px;
    background-color: #22262d;
    padding: 8px;
    gap: 8px;
  }
  .kachel {
    width: 120px;
    height: 60px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
  }
  .fix {
    flex-shrink: 0;
    background-color: #fb923c;
  }
asserts:
  - selector: ".fix"
    property: flex-shrink
    expected: "0"
hints:
  - kosten: 0
    text: |
      Standard ist `flex-shrink: 1` -- alle Items schrumpfen gleichmaessig wenn
      der Platz knapp wird. Mit `flex-shrink: 0` schrumpft das Item NICHT.
  - kosten: 4
    text: |
      Setze auf `.fix`: `flex-shrink: 0;`
starter_code: |
  .bahn {
    display: flex;
    width: 280px;
    height: 80px;
    background-color: #22262d;
    padding: 8px;
    gap: 8px;
  }
  .kachel {
    width: 120px;
    height: 60px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
  }
  .fix {
    background-color: #fb923c;
    /* hier verhindern, dass dieses Item schrumpft */
  }
---

# Flexbox 12: Schrumpfen verhindern

## Aufgabe

Die drei Kacheln wollen 120px breit sein, der Bahn ist aber
nur 280px breit. Standardmaessig schrumpfen alle drei. **B (in der Mitte)
soll aber seine volle Breite behalten** -- A und C schrumpfen dafür.

## Aha

`flex-shrink: 0` schuetzt ein Item davor, schmaler als seine Wunschbreite zu
werden. Andere Items in der Reihe schrumpfen entsprechend mehr.

## Wozu in der Praxis?

Avatare in einem Chat-Layout -- der Avatar (40px-Kreis) darf NIE schrumpfen,
auch wenn die Nachrichten daneben lang sind. Auch Icons in Toolbars: `flex-
shrink: 0` haelt sie quadratisch und klickbar.

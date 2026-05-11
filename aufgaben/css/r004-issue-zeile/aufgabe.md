---
schema_version: 1
id: r004-issue-zeile
revision: 1
titel: "Repro 04: Issue-Tracker-Zeile mit Status und Labels"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 10
tags: [repro, lernpfad, flexbox, tracker]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="issue"><span class="statuspunkt"></span><span class="id">CS-128</span><span class="titel">Schwebendes Schema-Panel implementieren</span><span class="label">Frontend</span><span class="prio">P1</span></div>
ziel_css: |
  .issue {
    display: flex;
    align-items: center;
    gap: 10px;
    width: 580px;
    padding: 10px 14px;
    background-color: #22262d;
    color: #e7ecf1;
    border-bottom: 1px solid #3a4049;
  }
  .statuspunkt {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #fbbf24;
    flex-shrink: 0;
  }
  .id {
    font-family: monospace;
    font-size: 12px;
    color: #9ca3af;
  }
  .titel {
    flex: 1;
    font-weight: 500;
  }
  .label {
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 4px;
    background-color: rgba(45, 212, 191, 0.18);
    color: #2dd4bf;
  }
  .prio {
    width: 28px;
    height: 20px;
    border-radius: 4px;
    background-color: #ef4444;
    color: #ffffff;
    font-size: 11px;
    font-weight: 700;
    display: inline-flex;
    justify-content: center;
    align-items: center;
  }
asserts:
  - selector: ".issue"
    property: display
    expected: "flex"
  - selector: ".statuspunkt"
    property: border-radius
    expected: "50%"
  - selector: ".titel"
    property: flex-grow
    expected: "1"
  - selector: ".label"
    property: background-color
    expected: "rgba(45, 212, 191, 0.18)"
  - selector: ".prio"
    property: background-color
    expected: "rgb(239, 68, 68)"
hints:
  - kosten: 0
    text: |
      Flex-Reihe mit fuenf Items. Der Titel waechst (flex: 1), die anderen behalten ihre Größe. Das Label hat einen halbtransparenten Hintergrund (rgba) damit der Petrol-Ton subtil wirkt.
  - kosten: 6
    text: |
      `.titel { flex: 1; }` und `.label { background-color: rgba(45, 212, 191, 0.18); color: #2dd4bf; }`
starter_code: |
  .issue {
    /* flex-Zeile, vertikal zentriert, 10px gap */
    width: 580px;
    padding: 10px 14px;
    background-color: #22262d;
    color: #e7ecf1;
    border-bottom: 1px solid #3a4049;
  }
  .statuspunkt {
    width: 8px;
    height: 8px;
    background-color: #fbbf24;
    /* Kreis-Form, nicht schrumpfen */
  }
  .id { font-family: monospace; font-size: 12px; color: #9ca3af; }
  .titel {
    font-weight: 500;
    /* den Rest-Platz fuellen */
  }
  .label {
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 4px;
    color: #2dd4bf;
    /* Petrol-Hintergrund mit Alpha 0.18 */
  }
  .prio {
    width: 28px;
    height: 20px;
    border-radius: 4px;
    background-color: #ef4444;
    color: #ffffff;
    font-size: 11px;
    font-weight: 700;
    display: inline-flex;
    justify-content: center;
    align-items: center;
  }
---

# Repro 04: Issue-Tracker-Zeile

## Aufgabe

Kompakte Zeile in einem
Issue-Tracker: Status-Punkt, ID, Titel (dehnt sich aus), Label-Badge,
Prioritaets-Box.

## Aha

rgba mit Alpha-Wert unter 1 erzeugt halbtransparente Farben. Bei `rgba(45,
212, 191, 0.18)` siehst du den Petrol-Ton nur schwach -- ideal für subtile
Badge-Hintergruende, die nicht vom Text ablenken aber trotzdem als visuelle
Markierung dienen.

## Wozu in der Praxis?

Ticket-Listen in Tracker-Tools, Task-Boards, Kommentar-Listen.

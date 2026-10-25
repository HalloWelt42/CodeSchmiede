---
schema_version: 1
id: r006-stat-trio
revision: 3
titel: "Repro 06: Dashboard-KPI-Trio"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 10
tags: [repro, lernpfad, dashboard, grid]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="kpis"><div class="kpi"><div class="kennzahl">1.284</div><div class="klabel">Aktive Nutzer</div><div class="ktrend pos">+12%</div></div><div class="kpi"><div class="kennzahl">€47.5K</div><div class="klabel">Umsatz</div><div class="ktrend pos">+8%</div></div><div class="kpi"><div class="kennzahl">3.2%</div><div class="klabel">Stornoquote</div><div class="ktrend neg">-1%</div></div></div>
ziel_css: |
  .kpis {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    width: 600px;
    padding: 8px;
    background-color: #1a1d23;
  }
  .kpi {
    padding: 16px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .kennzahl {
    font-size: 28px;
    font-weight: 700;
    color: #f472b6;
  }
  .klabel {
    font-size: 12px;
    color: #9ca3af;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .ktrend {
    margin-top: 8px;
    font-size: 13px;
    font-weight: 600;
  }
  .ktrend.pos { color: #22c55e; }
  .ktrend.neg { color: #ef4444; }
hints:
  - kosten: 0
    text: |
      Drei gleichbreite Karten via Grid. Jede Karte ist intern eine flex-column mit Kennzahl (groß), Label (klein uppercase), Trend (grün oder rot je nach Vorzeichen).
  - kosten: 6
    text: |
      `.kpis: grid-template-columns: repeat(3, 1fr); gap: 12px;` und `.ktrend.pos { color: #22c55e; } .ktrend.neg { color: #ef4444; }`
starter_code: |
  .kpis {
    /* 3-Spalten-Grid */
    gap: 12px;
    width: 600px;
    padding: 8px;
    background-color: #1a1d23;
  }
  .kpi {
    padding: 16px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .kennzahl {
    font-size: 28px;
    font-weight: 700;
    /* Rosa-Farbe */
  }
  .klabel {
    font-size: 12px;
    color: #9ca3af;
    /* uppercase, etwas mehr Letter-Spacing */
  }
  .ktrend { margin-top: 8px; font-size: 13px; font-weight: 600; }
  .ktrend.pos { /* Gruen */ }
  .ktrend.neg { /* Rot */ }
---

# Repro 06: Dashboard-KPI-Trio

## Aufgabe

Drei KPI-Kacheln nebeneinander:
große Kennzahl in Rosa, kleines Label darunter (uppercase), Trend-Anzeige
darunter (grün positiv, rot negativ).

## Aha

Die Trend-Zeile nutzt zwei Klassen (`ktrend pos` oder `ktrend neg`) - die
Basis-Klasse legt Schrift und Abstand fest, die Modifier-Klasse die Farbe.
Das ist das BEM-Pattern: Block + Modifier, gut wartbar.

## Wozu in der Praxis?

Admin-Dashboards, Analytics, Sales-Reports.

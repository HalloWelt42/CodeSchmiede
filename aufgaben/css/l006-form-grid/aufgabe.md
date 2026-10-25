---
schema_version: 1
id: l006-form-grid
revision: 3
titel: "Layout 06: Form-Layout mit Labels (Grid 1fr 2fr)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [layout, lernpfad, form, grid]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <form class="formular"><label class="label">Name</label><input class="feld" placeholder="..."><label class="label">E-Mail</label><input class="feld" placeholder="..."><label class="label">Nachricht</label><input class="feld" placeholder="..."></form>
ziel_css: |
  .formular {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 12px 16px;
    width: 400px;
    padding: 16px;
    background-color: #22262d;
    border-radius: 8px;
  }
  .label {
    color: #e7ecf1;
    font-weight: 600;
    display: flex; align-items: center;
  }
  .feld {
    padding: 8px 12px;
    background-color: #1a1d23;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    border-radius: 4px;
  }
hints:
  - kosten: 0
    text: |
      Form als 2-Spalten-Grid mit Verhältnis 1:2 - Labels schmal links, Felder breiter rechts. gap erlaubt unterschiedliche Werte für Reihen und Spalten.
  - kosten: 4
    text: |
      `grid-template-columns: 1fr 2fr; gap: 12px 16px;`
starter_code: |
  .formular {
    display: grid;
    /* hier: 1:2-Spalten, gap 12px vertikal + 16px horizontal */
    width: 400px;
    padding: 16px;
    background-color: #22262d;
    border-radius: 8px;
  }
  .label {
    color: #e7ecf1;
    font-weight: 600;
    display: flex; align-items: center;
  }
  .feld {
    padding: 8px 12px;
    background-color: #1a1d23;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    border-radius: 4px;
  }
---

# Layout 06: Form mit Label-Grid

## Aufgabe

Klassisches Form-Layout: Labels links, Eingabefelder rechts. Die Spalten
stehen im Verhältnis 1:2.

## Aha

gap akzeptiert zwei Werte: erst
die Reihen-Lücke (12px), dann die Spalten-Lücke (16px). Damit kontrollierst
du Vertikal- und Horizontal-Abstände separat.

Labels sitzen in einem
Flex-Container, damit sie vertikal zentriert auf Höhe der Inputs sind -
sonst würden sie oben kleben.

## Wozu in der Praxis?

Settings-Seiten, Kontaktformulare, Profil-Editoren.

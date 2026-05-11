---
schema_version: 1
id: s003-shop-getraenke
revision: 1
titel: "Shop: Getraenke unter 2 Euro"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [select, where, join, kategorie]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- JOIN + WHERE.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
dataset: shop
schema_hinweis: |
  produkte(id, name, kategorie_id, preis, lager, marke)
  kategorien(id, name)
erwartete_spalten: ["name", "preis"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Apfelsaft 1L", 1.89]
  - ["Cola 1L", 1.29]
hints:
  - kosten: 0
    text: |
      Verknuepfe `produkte` per JOIN mit `kategorien` (Kategorie-Name = 'Getränke')
      und filtere `preis < 2.0`.
  - kosten: 4
    text: |
      `SELECT p.name, p.preis FROM produkte p JOIN kategorien k ON p.kategorie_id = k.id
       WHERE k.name = 'Getränke' AND p.preis < 2.0 ORDER BY p.id;`
starter_code: |
  SELECT p.name, p.preis FROM produkte p
  JOIN ___ ON ___
  WHERE ___ AND ___
  ORDER BY p.id;
---

# Shop: Getraenke unter 2 Euro

Finde alle Produkte aus der Kategorie **Getraenke**, die weniger
als 2 Euro kosten. Liefere `name` und `preis`, sortiert nach Produkt-ID.

2 Zeilen werden erwartet.

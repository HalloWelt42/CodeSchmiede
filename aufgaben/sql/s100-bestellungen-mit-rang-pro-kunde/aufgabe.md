---
schema_version: 1
id: s100-bestellungen-mit-rang-pro-kunde
revision: 1
titel: "Shop: Bestellungen mit Rang pro Kunde"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [window-function, row-number, partition-by]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- SQL-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
dataset: shop
schema_hinweis: |
  kategorien(id, name)
  produkte(id, name, kategorie_id, preis, lager, marke)
  kunden(id, name, ort, plz, alter_jahre)
  bestellungen(id, kunde_id, bestellt_am, status)
  bestellpositionen(bestellung_id, produkt_id, menge, einzelpreis)
erwartete_spalten: ["id", "kunde_id", "bestellt_am", "rang"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, 1, "2025-04-01", 1]
  - [2, 1, "2025-04-15", 2]
  - [3, 2, "2025-03-10", 1]
  - [4, 2, "2025-04-20", 2]
  - [5, 3, "2025-04-05", 1]
  - [6, 3, "2025-04-22", 2]
  - [7, 4, "2025-04-12", 1]
  - [8, 5, "2025-03-25", 1]
  - [9, 5, "2025-04-18", 2]
  - [10, 6, "2025-04-08", 1]
  - [11, 7, "2025-04-02", 1]
  - [12, 8, "2025-04-21", 1]
  - [13, 9, "2025-03-30", 1]
  - [14, 10, "2025-04-10", 1]
  - [15, 11, "2025-04-14", 1]
  - [16, 12, "2025-04-19", 1]
hints:
  - kosten: 0
    text: |
      ROW_NUMBER mit PARTITION BY kunde_id.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellungen mit Kunde-Rang

Jede Bestellung bekommt fortlaufende Nummer pro Kunde (1 = erste Bestellung).

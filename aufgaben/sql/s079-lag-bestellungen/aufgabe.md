---
schema_version: 1
id: s079-lag-bestellungen
revision: 1
titel: "Shop: Tage seit letzter Bestellung"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [window-function, lag, partition-by]
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
erwartete_spalten: ["id", "kunde_id", "bestellt_am", "vorher"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, 1, "2025-04-01", null]
  - [2, 1, "2025-04-15", "2025-04-01"]
  - [3, 2, "2025-03-10", null]
  - [4, 2, "2025-04-20", "2025-03-10"]
  - [5, 3, "2025-04-05", null]
  - [6, 3, "2025-04-22", "2025-04-05"]
  - [7, 4, "2025-04-12", null]
  - [8, 5, "2025-03-25", null]
  - [9, 5, "2025-04-18", "2025-03-25"]
  - [10, 6, "2025-04-08", null]
  - [11, 7, "2025-04-02", null]
  - [12, 8, "2025-04-21", null]
  - [13, 9, "2025-03-30", null]
  - [14, 10, "2025-04-10", null]
  - [15, 11, "2025-04-14", null]
  - [16, 12, "2025-04-19", null]
hints:
  - kosten: 0
    text: |
      `LAG(spalte) OVER (PARTITION BY ... ORDER BY ...)` gibt den vorigen Wert pro Partition.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Tage seit letzter Bestellung

Pro Bestellung: ID, Kunde, Datum + Datum der vorherigen Bestellung dieses Kunden (NULL bei erster).

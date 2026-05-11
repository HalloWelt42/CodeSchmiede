---
schema_version: 1
id: s172-shop-cumsum-status
revision: 1
titel: "Shop: laufender Bestellzaehler pro Status"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [window-function, count-over, partition-by]
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
erwartete_spalten: ["id", "status", "bestellt_am", "lfd"]
sortierung_egal: false
erwartetes_ergebnis:
  - [3, "geliefert", "2025-03-10", 1]
  - [8, "geliefert", "2025-03-25", 2]
  - [13, "geliefert", "2025-03-30", 3]
  - [1, "geliefert", "2025-04-01", 4]
  - [11, "geliefert", "2025-04-02", 5]
  - [5, "geliefert", "2025-04-05", 6]
  - [14, "geliefert", "2025-04-10", 7]
  - [7, "geliefert", "2025-04-12", 8]
  - [9, "geliefert", "2025-04-18", 9]
  - [16, "offen", "2025-04-19", 1]
  - [4, "offen", "2025-04-20", 2]
  - [12, "offen", "2025-04-21", 3]
  - [6, "storniert", "2025-04-22", 1]
  - [10, "versandt", "2025-04-08", 1]
  - [15, "versandt", "2025-04-14", 2]
  - [2, "versandt", "2025-04-15", 3]
hints:
  - kosten: 0
    text: |
      COUNT(*) OVER (PARTITION BY status ORDER BY ...)
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Laufender Zähler pro Status

Jede Bestellung bekommt fortlaufenden Zähler innerhalb ihres Status.

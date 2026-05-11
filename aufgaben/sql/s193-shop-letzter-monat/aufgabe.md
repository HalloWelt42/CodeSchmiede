---
schema_version: 1
id: s193-shop-letzter-monat
revision: 1
titel: "Shop: nur letzter Monat"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [where, date]
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
erwartete_spalten: ["id", "kunde_id", "bestellt_am", "status"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, 1, "2025-04-01", "geliefert"]
  - [11, 7, "2025-04-02", "geliefert"]
  - [5, 3, "2025-04-05", "geliefert"]
  - [10, 6, "2025-04-08", "versandt"]
  - [14, 10, "2025-04-10", "geliefert"]
  - [7, 4, "2025-04-12", "geliefert"]
  - [15, 11, "2025-04-14", "versandt"]
  - [2, 1, "2025-04-15", "versandt"]
  - [9, 5, "2025-04-18", "geliefert"]
  - [16, 12, "2025-04-19", "offen"]
  - [4, 2, "2025-04-20", "offen"]
  - [12, 8, "2025-04-21", "offen"]
  - [6, 3, "2025-04-22", "storniert"]
hints:
  - kosten: 0
    text: |
      Datum-String-Vergleich.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellungen ab April 2025

Alle Bestellungen ab dem 1. April 2025.

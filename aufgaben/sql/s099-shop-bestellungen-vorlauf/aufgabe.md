---
schema_version: 1
id: s099-shop-bestellungen-vorlauf
revision: 1
titel: "Shop: Vorlauf zwischen Bestellungen pro Kunde"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 20
schaetz_minuten: 12
tags: [window-function, lag, julianday]
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
erwartete_spalten: ["id", "kunde_id", "bestellt_am", "tage_seit_letzter"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, 1, "2025-04-01", null]
  - [2, 1, "2025-04-15", 14]
  - [3, 2, "2025-03-10", null]
  - [4, 2, "2025-04-20", 41]
  - [5, 3, "2025-04-05", null]
  - [6, 3, "2025-04-22", 17]
  - [7, 4, "2025-04-12", null]
  - [8, 5, "2025-03-25", null]
  - [9, 5, "2025-04-18", 24]
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
      LAG fuer vorherigen Termin, julianday-Differenz fuer Tage.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Vorlauf zwischen Bestellungen

Pro Bestellung: Tage seit der letzten Bestellung desselben Kunden (NULL bei erster).

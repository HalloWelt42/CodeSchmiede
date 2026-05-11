---
schema_version: 1
id: s071-shop-status-zaehlen-pivot
revision: 1
titel: "Shop: Bestellungen pro Status als Pivot"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [pivot, case, sum, report]
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
erwartete_spalten: ["offen", "versandt", "geliefert", "storniert"]
sortierung_egal: false
erwartetes_ergebnis:
  - [3, 3, 9, 1]
hints:
  - kosten: 0
    text: |
      Pivot per `SUM(CASE WHEN status = 'x' THEN 1 ELSE 0 END)` als eigene Spalte je Status.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Pivot: Bestellungen pro Status

Eine Zeile mit vier Spalten (`offen`, `versandt`, `geliefert`, `storniert`), je Status die Anzahl.

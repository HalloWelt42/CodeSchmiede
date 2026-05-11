---
schema_version: 1
id: s147-shop-status-pro-monat
revision: 1
titel: "Shop: Status pro Monat (Pivot)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [case, sum, group-by, date, pivot]
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
erwartete_spalten: ["monat", "offen", "versandt", "geliefert", "storniert"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["2025-03", 0, 0, 3, 0]
  - ["2025-04", 3, 3, 6, 1]
hints:
  - kosten: 0
    text: |
      Pivot per CASE WHEN, gruppiert pro Monat.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Status pro Monat

Monat + Anzahl pro Status als eigene Spalten, chronologisch.

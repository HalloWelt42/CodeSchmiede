---
schema_version: 1
id: s195-shop-zwischensumme-bestellung-status
revision: 1
titel: "Shop: Zwischensumme + Status"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, group-by, sum]
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
erwartete_spalten: ["id", "status", "summe"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, "geliefert", 8.07]
  - [2, "versandt", 7.77]
  - [3, "geliefert", 9.78]
  - [4, "offen", 3.87]
  - [5, "geliefert", 7.97]
  - [6, "storniert", 2.2]
  - [7, "geliefert", 6.94]
  - [8, "geliefert", 12.76]
  - [9, "geliefert", 4.87]
  - [10, "versandt", 7.88]
  - [11, "geliefert", 12.66]
  - [12, "offen", 6.56]
  - [13, "geliefert", 9.47]
  - [14, "geliefert", 3.69]
  - [15, "versandt", 12.47]
  - [16, "offen", 3.28]
hints:
  - kosten: 0
    text: |
      GROUP BY b.id, b.status.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellungen mit Summe + Status

Bestellung-ID + Status + Gesamtsumme, sortiert nach ID.

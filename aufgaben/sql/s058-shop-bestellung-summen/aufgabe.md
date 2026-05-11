---
schema_version: 1
id: s058-shop-bestellung-summen
revision: 1
titel: "Shop: Bestellsumme pro Bestellung"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [sum, group-by, berechnung]
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
erwartete_spalten: ["bestellung_id", "gesamt"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, 8.07]
  - [2, 7.77]
  - [3, 9.78]
  - [4, 3.87]
  - [5, 7.97]
  - [6, 2.2]
  - [7, 6.94]
  - [8, 12.76]
  - [9, 4.87]
  - [10, 7.88]
  - [11, 12.66]
  - [12, 6.56]
  - [13, 9.47]
  - [14, 3.69]
  - [15, 12.47]
  - [16, 3.28]
hints:
  - kosten: 0
    text: |
      `SUM(menge * einzelpreis)` plus `ROUND(..., 2)`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellsumme pro Bestellung

ID + Gesamtsumme jeder Bestellung in EUR (auf 2 Nachkommastellen).

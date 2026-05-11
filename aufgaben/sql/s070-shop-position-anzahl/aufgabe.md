---
schema_version: 1
id: s070-shop-position-anzahl
revision: 1
titel: "Shop: Anzahl Positionen pro Bestellung"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [group-by, count]
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
erwartete_spalten: ["bestellung_id", "positionen"]
sortierung_egal: false
erwartetes_ergebnis:
  - [3, 4]
  - [1, 3]
  - [5, 3]
  - [8, 3]
  - [9, 3]
  - [2, 2]
  - [7, 2]
  - [10, 2]
  - [11, 2]
  - [12, 2]
  - [13, 2]
  - [14, 2]
  - [15, 2]
  - [16, 2]
  - [4, 1]
  - [6, 1]
hints:
  - kosten: 0
    text: |
      GROUP BY bestellung_id.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Positionen pro Bestellung

Bestell-ID + wieviele Positionen, hauefigste zuerst.

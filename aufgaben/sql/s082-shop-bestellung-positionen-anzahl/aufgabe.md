---
schema_version: 1
id: s082-shop-bestellung-positionen-anzahl
revision: 1
titel: "Shop: Bestellungen mit mehr als 2 Positionen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [group-by, having]
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
hints:
  - kosten: 0
    text: |
      GROUP BY + HAVING COUNT(*) > 2.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellungen mit > 2 Positionen

Bestellungs-ID + Positionsanzahl für Bestellungen mit mehr als 2 Positionen.

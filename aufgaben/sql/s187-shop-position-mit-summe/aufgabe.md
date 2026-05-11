---
schema_version: 1
id: s187-shop-position-mit-summe
revision: 1
titel: "Shop: Bestellpositionen mit Zwischensumme"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [math, berechnung]
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
erwartete_spalten: ["bestellung_id", "produkt_id", "menge", "einzelpreis", "zwischensumme"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, 1, 6, 0.45, 2.7]
  - [1, 9, 2, 1.29, 2.58]
  - [1, 13, 1, 2.79, 2.79]
  - [2, 3, 1, 3.99, 3.99]
  - [2, 17, 2, 1.89, 3.78]
  - [3, 5, 4, 0.65, 2.6]
  - [3, 6, 2, 1.2, 2.4]
  - [3, 7, 1, 1.49, 1.49]
  - [3, 12, 1, 3.29, 3.29]
  - [4, 18, 3, 1.29, 3.87]
  - [5, 2, 5, 0.3, 1.5]
  - [5, 19, 2, 1.99, 3.98]
  - [5, 20, 1, 2.49, 2.49]
  - [6, 4, 4, 0.55, 2.2]
  - [7, 14, 2, 1.49, 2.98]
  - [7, 15, 4, 0.99, 3.96]
  - [8, 11, 2, 2.49, 4.98]
  - [8, 13, 1, 2.79, 2.79]
  - [8, 16, 1, 4.99, 4.99]
  - [9, 1, 4, 0.45, 1.8]
  - [9, 9, 1, 1.29, 1.29]
  - [9, 10, 2, 0.89, 1.78]
  - [10, 5, 6, 0.65, 3.9]
  - [10, 8, 2, 1.99, 3.98]
  - [11, 12, 3, 3.29, 9.87]
  - [11, 13, 1, 2.79, 2.79]
  - [12, 18, 2, 1.29, 2.58]
  - [12, 19, 2, 1.99, 3.98]
  - [13, 3, 2, 3.99, 7.98]
  - [13, 7, 1, 1.49, 1.49]
  - [14, 2, 6, 0.3, 1.8]
  - [14, 17, 1, 1.89, 1.89]
  - [15, 11, 1, 2.49, 2.49]
  - [15, 16, 2, 4.99, 9.98]
  - [16, 8, 1, 1.99, 1.99]
  - [16, 9, 1, 1.29, 1.29]
hints:
  - kosten: 0
    text: |
      Einfaches `menge * einzelpreis`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Zwischensumme pro Position

Alle Spalten + zusätzliche Zwischensumme menge * einzelpreis.

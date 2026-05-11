---
schema_version: 1
id: s116-shop-bestellungen-juenger-30
revision: 1
titel: "Shop: Bestellungen junger Kunden"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [join, where]
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
erwartete_spalten: ["id", "name", "alter_jahre", "bestellt_am"]
sortierung_egal: false
erwartetes_ergebnis:
  - [5, "Carla Diaz", 28, "2025-04-05"]
  - [7, "Daniel Engel", 19, "2025-04-12"]
  - [16, "Leon Wolf", 26, "2025-04-19"]
  - [12, "Hugo Meier", 22, "2025-04-21"]
  - [6, "Carla Diaz", 28, "2025-04-22"]
hints:
  - kosten: 0
    text: |
      JOIN + WHERE k.alter_jahre < 30.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellungen junger Kunden

Bestellung-ID + Kunde + Alter + Datum, chronologisch.

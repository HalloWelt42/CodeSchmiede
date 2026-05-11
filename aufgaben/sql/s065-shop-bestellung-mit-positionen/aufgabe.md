---
schema_version: 1
id: s065-shop-bestellung-mit-positionen
revision: 1
titel: "Shop: Bestellung + Positionen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 6
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
erwartete_spalten: ["id", "name", "produkt", "menge"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, "Alex Becker", "Apfel Boskoop", 6]
  - [1, "Alex Becker", "Brot Roggen 500g", 1]
  - [1, "Alex Becker", "Vollmilch 1L", 2]
hints:
  - kosten: 0
    text: |
      Mehrfach-JOIN, WHERE auf Bestellungs-ID.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Positionen einer Bestellung

Fuer Bestellung 1: ID, Kunden-Name, Produktname, Menge.

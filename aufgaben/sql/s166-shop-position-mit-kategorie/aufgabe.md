---
schema_version: 1
id: s166-shop-position-mit-kategorie
revision: 1
titel: "Shop: Positionen mit Produkt + Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join-multi, where]
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
erwartete_spalten: ["id", "produkt", "kategorie", "menge"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, "Apfel Boskoop", "Obst", 6]
  - [1, "Brot Roggen 500g", "Backwaren", 1]
  - [1, "Vollmilch 1L", "Milchprodukte", 2]
  - [3, "Gouda Scheiben 200g", "Milchprodukte", 1]
  - [3, "Gurke", "Gemuese", 2]
  - [3, "Karotte 1kg", "Gemuese", 1]
  - [3, "Tomate Strauch", "Gemuese", 4]
  - [5, "Banane", "Obst", 5]
  - [5, "Kekse 200g", "Suesswaren", 1]
  - [5, "Schokolade 100g", "Suesswaren", 2]
  - [7, "Brötchen 5er-Pack", "Backwaren", 2]
  - [7, "Croissant", "Backwaren", 4]
  - [8, "Brot Roggen 500g", "Backwaren", 1]
  - [8, "Butter 250g", "Milchprodukte", 2]
  - [8, "Mineralwasser 6x1L", "Getraenke", 1]
  - [9, "Apfel Boskoop", "Obst", 4]
  - [9, "Joghurt Natur 500g", "Milchprodukte", 2]
  - [9, "Vollmilch 1L", "Milchprodukte", 1]
  - [11, "Brot Roggen 500g", "Backwaren", 1]
  - [11, "Gouda Scheiben 200g", "Milchprodukte", 3]
  - [13, "Erdbeeren 500g", "Obst", 2]
  - [13, "Karotte 1kg", "Gemuese", 1]
  - [14, "Apfelsaft 1L", "Getraenke", 1]
  - [14, "Banane", "Obst", 6]
hints:
  - kosten: 0
    text: |
      Vier JOINs hintereinander.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Positionen aus gelieferten Bestellungen

Bestell-ID, Produkt, Kategorie, Menge -- nur gelieferte Bestellungen.

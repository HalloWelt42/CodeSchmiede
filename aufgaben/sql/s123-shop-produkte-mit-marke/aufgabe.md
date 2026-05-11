---
schema_version: 1
id: s123-shop-produkte-mit-marke
revision: 1
titel: "Shop: Produkt + Marke kombiniert"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [string, concat, pipe-pipe]
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
erwartete_spalten: ["bezeichnung"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Apfel Boskoop (Bio-Hof Schulz)"]
  - ["Apfelsaft 1L (FruchtFest)"]
  - ["Banane (Tropico)"]
  - ["Brokkoli (GartenFrisch)"]
  - ["Brot Roggen 500g (Bauernbäckerei)"]
  - ["Brötchen 5er-Pack (Bauernbäckerei)"]
  - ["Butter 250g (Alpenglück)"]
  - ["Cola 1L (BlubberCo)"]
  - ["Croissant (Pariser Art)"]
  - ["Erdbeeren 500g (Bio-Hof Schulz)"]
  - ["Gouda Scheiben 200g (KäseHof)"]
  - ["Gurke (GartenFrisch)"]
  - ["Joghurt Natur 500g (Alpenglück)"]
  - ["Karotte 1kg (Bio-Hof Schulz)"]
  - ["Kekse 200g (KekseRoll)"]
  - ["Mineralwasser 6x1L (AquaPur)"]
  - ["Orange Navel (Citrus Plus)"]
  - ["Schokolade 100g (KakaoLuxus)"]
  - ["Tomate Strauch (GartenFrisch)"]
  - ["Vollmilch 1L (Alpenglück)"]
hints:
  - kosten: 0
    text: |
      `||` ist String-Konkatenation in SQLite.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Produkt + Marke

Für jedes Produkt: Bezeichnung `Name (Marke)` als einzelne Spalte, alphabetisch.

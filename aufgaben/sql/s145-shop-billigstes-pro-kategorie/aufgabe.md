---
schema_version: 1
id: s145-shop-billigstes-pro-kategorie
revision: 1
titel: "Shop: Billigstes Produkt pro Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [cte, window-function, top-per-group]
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
erwartete_spalten: ["kategorie", "name", "preis"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Backwaren", "Croissant", 0.99]
  - ["Gemüse", "Tomate Strauch", 0.65]
  - ["Getränke", "Cola 1L", 1.29]
  - ["Milchprodukte", "Joghurt Natur 500g", 0.89]
  - ["Obst", "Banane", 0.3]
  - ["Süßwaren", "Schokolade 100g", 1.99]
hints:
  - kosten: 0
    text: |
      ROW_NUMBER OVER PARTITION + WHERE rn = 1.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Billigstes Produkt pro Kategorie

Kategorie + Name + Preis des billigsten Produkts.

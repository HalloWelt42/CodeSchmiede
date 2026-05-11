---
schema_version: 1
id: s089-shop-mittelpreis-kategorie
revision: 1
titel: "Shop: Produkt vs. Kategorie-Durchschnitt"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [window-function, avg-over, partition-by]
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
erwartete_spalten: ["name", "preis", "kat_schnitt"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Apfel Boskoop", 0.45, 1.32]
  - ["Banane", 0.3, 1.32]
  - ["Erdbeeren 500g", 3.99, 1.32]
  - ["Orange Navel", 0.55, 1.32]
  - ["Brokkoli", 1.99, 1.33]
  - ["Gurke", 1.2, 1.33]
  - ["Karotte 1kg", 1.49, 1.33]
  - ["Tomate Strauch", 0.65, 1.33]
  - ["Butter 250g", 2.49, 1.99]
  - ["Gouda Scheiben 200g", 3.29, 1.99]
  - ["Joghurt Natur 500g", 0.89, 1.99]
  - ["Vollmilch 1L", 1.29, 1.99]
  - ["Brot Roggen 500g", 2.79, 1.76]
  - ["Brötchen 5er-Pack", 1.49, 1.76]
  - ["Croissant", 0.99, 1.76]
  - ["Apfelsaft 1L", 1.89, 2.72]
  - ["Cola 1L", 1.29, 2.72]
  - ["Mineralwasser 6x1L", 4.99, 2.72]
  - ["Kekse 200g", 2.49, 2.24]
  - ["Schokolade 100g", 1.99, 2.24]
hints:
  - kosten: 0
    text: |
      `AVG(preis) OVER (PARTITION BY kategorie_id)`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Produkt vs. Kategorie-Schnitt

Für jedes Produkt: Name, Preis, Durchschnittspreis seiner Kategorie.

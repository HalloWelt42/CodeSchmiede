---
schema_version: 1
id: s179-shop-marge-fiktiv-2
revision: 1
titel: "Shop: 5% Mehrwertsteuer hinzurechnen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [math, round]
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
erwartete_spalten: ["name", "preis", "brutto"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Apfel Boskoop", 0.45, 0.47]
  - ["Apfelsaft 1L", 1.89, 1.98]
  - ["Banane", 0.3, 0.32]
  - ["Brokkoli", 1.99, 2.09]
  - ["Brot Roggen 500g", 2.79, 2.93]
  - ["Brötchen 5er-Pack", 1.49, 1.56]
  - ["Butter 250g", 2.49, 2.61]
  - ["Cola 1L", 1.29, 1.35]
  - ["Croissant", 0.99, 1.04]
  - ["Erdbeeren 500g", 3.99, 4.19]
  - ["Gouda Scheiben 200g", 3.29, 3.45]
  - ["Gurke", 1.2, 1.26]
  - ["Joghurt Natur 500g", 0.89, 0.93]
  - ["Karotte 1kg", 1.49, 1.56]
  - ["Kekse 200g", 2.49, 2.61]
  - ["Mineralwasser 6x1L", 4.99, 5.24]
  - ["Orange Navel", 0.55, 0.58]
  - ["Schokolade 100g", 1.99, 2.09]
  - ["Tomate Strauch", 0.65, 0.68]
  - ["Vollmilch 1L", 1.29, 1.35]
hints:
  - kosten: 0
    text: |
      preis * 1.05 + ROUND.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Preis + 5% Steuer

Name + Netto-Preis + Brutto-Preis (Netto * 1.05).

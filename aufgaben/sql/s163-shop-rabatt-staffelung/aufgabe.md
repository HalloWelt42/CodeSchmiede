---
schema_version: 1
id: s163-shop-rabatt-staffelung
revision: 1
titel: "Shop: Mengen-Rabatt simuliert"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [join, case, berechnung]
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
erwartete_spalten: ["name", "menge", "einzelpreis", "preis"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Apfel Boskoop", 6, 0.45, 2.43]
  - ["Apfel Boskoop", 4, 0.45, 1.8]
  - ["Apfelsaft 1L", 2, 1.89, 3.78]
  - ["Apfelsaft 1L", 1, 1.89, 1.89]
  - ["Banane", 6, 0.3, 1.62]
  - ["Banane", 5, 0.3, 1.35]
  - ["Brokkoli", 2, 1.99, 3.98]
  - ["Brokkoli", 1, 1.99, 1.99]
  - ["Brot Roggen 500g", 1, 2.79, 2.79]
  - ["Brot Roggen 500g", 1, 2.79, 2.79]
  - ["Brot Roggen 500g", 1, 2.79, 2.79]
  - ["Brötchen 5er-Pack", 2, 1.49, 2.98]
  - ["Butter 250g", 2, 2.49, 4.98]
  - ["Butter 250g", 1, 2.49, 2.49]
  - ["Cola 1L", 3, 1.29, 3.87]
  - ["Cola 1L", 2, 1.29, 2.58]
  - ["Croissant", 4, 0.99, 3.96]
  - ["Erdbeeren 500g", 2, 3.99, 7.98]
  - ["Erdbeeren 500g", 1, 3.99, 3.99]
  - ["Gouda Scheiben 200g", 3, 3.29, 9.87]
  - ["Gouda Scheiben 200g", 1, 3.29, 3.29]
  - ["Gurke", 2, 1.2, 2.4]
  - ["Joghurt Natur 500g", 2, 0.89, 1.78]
  - ["Karotte 1kg", 1, 1.49, 1.49]
  - ["Karotte 1kg", 1, 1.49, 1.49]
  - ["Kekse 200g", 1, 2.49, 2.49]
  - ["Mineralwasser 6x1L", 2, 4.99, 9.98]
  - ["Mineralwasser 6x1L", 1, 4.99, 4.99]
  - ["Orange Navel", 4, 0.55, 2.2]
  - ["Schokolade 100g", 2, 1.99, 3.98]
  - ["Schokolade 100g", 2, 1.99, 3.98]
  - ["Tomate Strauch", 6, 0.65, 3.51]
  - ["Tomate Strauch", 4, 0.65, 2.6]
  - ["Vollmilch 1L", 2, 1.29, 2.58]
  - ["Vollmilch 1L", 1, 1.29, 1.29]
  - ["Vollmilch 1L", 1, 1.29, 1.29]
hints:
  - kosten: 0
    text: |
      CASE WHEN menge >= 5 -> 10% Rabatt.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Mengenrabatt

Produkt + Menge + Einzelpreis + Endpreis (ab 5 Stück 10% Rabatt).

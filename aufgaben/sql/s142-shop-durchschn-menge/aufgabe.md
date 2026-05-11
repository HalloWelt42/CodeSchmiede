---
schema_version: 1
id: s142-shop-durchschn-menge
revision: 1
titel: "Shop: Durchschnittliche Mengen pro Produkt"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, avg, group-by]
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
erwartete_spalten: ["name", "schnitt_menge"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Banane", 5.5]
  - ["Apfel Boskoop", 5.0]
  - ["Tomate Strauch", 5.0]
  - ["Croissant", 4.0]
  - ["Orange Navel", 4.0]
  - ["Cola 1L", 2.5]
  - ["Brötchen 5er-Pack", 2.0]
  - ["Gouda Scheiben 200g", 2.0]
  - ["Gurke", 2.0]
  - ["Joghurt Natur 500g", 2.0]
  - ["Schokolade 100g", 2.0]
  - ["Apfelsaft 1L", 1.5]
  - ["Brokkoli", 1.5]
  - ["Butter 250g", 1.5]
  - ["Erdbeeren 500g", 1.5]
  - ["Mineralwasser 6x1L", 1.5]
  - ["Vollmilch 1L", 1.33]
  - ["Brot Roggen 500g", 1.0]
  - ["Karotte 1kg", 1.0]
  - ["Kekse 200g", 1.0]
hints:
  - kosten: 0
    text: |
      JOIN + AVG(menge) + GROUP BY Produkt.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Durchschnittliche Bestellmenge pro Produkt

Produktname + Mittelwert der Mengen, höchste zuerst.

---
schema_version: 1
id: s188-shop-produkt-mit-aktivitaet
revision: 1
titel: "Shop: Produkte mit Bestellaktivität"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [left-join, group-by, coalesce]
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
erwartete_spalten: ["name", "verkauft"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Banane", 11]
  - ["Apfel Boskoop", 10]
  - ["Tomate Strauch", 10]
  - ["Cola 1L", 5]
  - ["Croissant", 4]
  - ["Gouda Scheiben 200g", 4]
  - ["Orange Navel", 4]
  - ["Schokolade 100g", 4]
  - ["Vollmilch 1L", 4]
  - ["Apfelsaft 1L", 3]
  - ["Brokkoli", 3]
  - ["Brot Roggen 500g", 3]
  - ["Butter 250g", 3]
  - ["Erdbeeren 500g", 3]
  - ["Mineralwasser 6x1L", 3]
  - ["Brötchen 5er-Pack", 2]
  - ["Gurke", 2]
  - ["Joghurt Natur 500g", 2]
  - ["Karotte 1kg", 2]
  - ["Kekse 200g", 1]
hints:
  - kosten: 0
    text: |
      LEFT JOIN + COALESCE(SUM(menge), 0) für Produkte ohne Bestellungen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Produkt-Aktivität

Jedes Produkt + Stückzahl verkauft (0 wenn nie), häufigste zuerst.

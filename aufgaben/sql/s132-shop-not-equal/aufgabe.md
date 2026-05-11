---
schema_version: 1
id: s132-shop-not-equal
revision: 1
titel: "Shop: alles ausser Suesswaren"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [join, where, not-equal]
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
erwartete_spalten: ["name", "kategorie"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Apfel Boskoop", "Obst"]
  - ["Apfelsaft 1L", "Getraenke"]
  - ["Banane", "Obst"]
  - ["Brokkoli", "Gemuese"]
  - ["Brot Roggen 500g", "Backwaren"]
  - ["Brötchen 5er-Pack", "Backwaren"]
  - ["Butter 250g", "Milchprodukte"]
  - ["Cola 1L", "Getraenke"]
  - ["Croissant", "Backwaren"]
  - ["Erdbeeren 500g", "Obst"]
  - ["Gouda Scheiben 200g", "Milchprodukte"]
  - ["Gurke", "Gemuese"]
  - ["Joghurt Natur 500g", "Milchprodukte"]
  - ["Karotte 1kg", "Gemuese"]
  - ["Mineralwasser 6x1L", "Getraenke"]
  - ["Orange Navel", "Obst"]
  - ["Tomate Strauch", "Gemuese"]
  - ["Vollmilch 1L", "Milchprodukte"]
hints:
  - kosten: 0
    text: |
      `!=` oder `<>` als Ungleich-Operator.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Shop ohne Suesswaren

Produkte aus allen Kategorien außer Suesswaren.

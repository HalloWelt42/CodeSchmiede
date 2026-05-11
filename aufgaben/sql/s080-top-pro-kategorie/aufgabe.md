---
schema_version: 1
id: s080-top-pro-kategorie
revision: 1
titel: "Shop: Teuerstes Produkt pro Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 20
schaetz_minuten: 10
tags: [cte, window-function, row-number, top-per-group]
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
  - ["Backwaren", "Brot Roggen 500g", 2.79]
  - ["Gemuese", "Brokkoli", 1.99]
  - ["Getraenke", "Mineralwasser 6x1L", 4.99]
  - ["Milchprodukte", "Gouda Scheiben 200g", 3.29]
  - ["Obst", "Erdbeeren 500g", 3.99]
  - ["Suesswaren", "Kekse 200g", 2.49]
hints:
  - kosten: 0
    text: |
      CTE mit ROW_NUMBER OVER PARTITION BY -- aussen WHERE rn = 1.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Teuerstes Produkt pro Kategorie

Pro Kategorie das hochpreisigste Produkt mit Preis.

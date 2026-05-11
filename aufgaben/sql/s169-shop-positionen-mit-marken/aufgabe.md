---
schema_version: 1
id: s169-shop-positionen-mit-marken
revision: 1
titel: "Shop: Mengen pro Marke"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, sum, group-by]
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
erwartete_spalten: ["marke", "gesamtmenge"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Bio-Hof Schulz", 15]
  - ["GartenFrisch", 15]
  - ["Tropico", 11]
  - ["Alpenglück", 9]
  - ["Bauernbäckerei", 5]
  - ["BlubberCo", 5]
  - ["Citrus Plus", 4]
  - ["KakaoLuxus", 4]
  - ["KäseHof", 4]
  - ["Pariser Art", 4]
  - ["AquaPur", 3]
  - ["FruchtFest", 3]
  - ["KekseRoll", 1]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY marke + SUM(menge).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Mengen pro Marke

Marke + verkaufte Stückzahl, höchste zuerst.

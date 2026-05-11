---
schema_version: 1
id: s115-shop-marken-umsatz
revision: 1
titel: "Shop: Umsatz pro Marke"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
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
erwartete_spalten: ["marke", "umsatz"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Bio-Hof Schulz", 19.45]
  - ["AquaPur", 14.97]
  - ["GartenFrisch", 14.87]
  - ["Alpenglueck", 14.41]
  - ["KaeseHof", 13.16]
  - ["Bauernbaeckerei", 11.35]
  - ["KakaoLuxus", 7.96]
  - ["BlubberCo", 6.45]
  - ["FruchtFest", 5.67]
  - ["Pariser Art", 3.96]
  - ["Tropico", 3.3]
  - ["KekseRoll", 2.49]
  - ["Citrus Plus", 2.2]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY marke + SUM(menge*einzelpreis).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Umsatz pro Marke

Marke + Gesamtumsatz, hoechste zuerst.

---
schema_version: 1
id: s064-shop-marken
revision: 1
titel: "Shop: Anzahl Produkte pro Marke"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [group-by, count]
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
erwartete_spalten: ["marke", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Alpenglück", 3]
  - ["Bio-Hof Schulz", 3]
  - ["GartenFrisch", 3]
  - ["Bauernbäckerei", 2]
  - ["AquaPur", 1]
  - ["BlubberCo", 1]
  - ["Citrus Plus", 1]
  - ["FruchtFest", 1]
  - ["KakaoLuxus", 1]
  - ["KekseRoll", 1]
  - ["KäseHof", 1]
  - ["Pariser Art", 1]
  - ["Tropico", 1]
hints:
  - kosten: 0
    text: |
      GROUP BY marke.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Produkte pro Marke

Marken-Name + Anzahl Produkte, hauefigste Marke zuerst.

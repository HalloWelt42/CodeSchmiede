---
schema_version: 1
id: s144-shop-marken-anzahl-produkte
revision: 1
titel: "Shop: Marken mit min. 3 Produkten"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [group-by, having]
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
hints:
  - kosten: 0
    text: |
      HAVING COUNT(*) >= 3.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Marken mit min. 3 Produkten

Marke + Anzahl, häufigste zuerst.

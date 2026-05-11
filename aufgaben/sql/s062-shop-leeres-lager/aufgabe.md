---
schema_version: 1
id: s062-shop-leeres-lager
revision: 1
titel: "Shop: Produkte mit niedrigem Lager"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [where, sort]
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
erwartete_spalten: ["name", "lager"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Brot Roggen 500g", 50]
  - ["Croissant", 60]
  - ["Brötchen 5er-Pack", 80]
  - ["Erdbeeren 500g", 80]
  - ["Brokkoli", 90]
hints:
  - kosten: 0
    text: |
      WHERE lager < 100.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Niedriger Lagerbestand

Produkte mit weniger als 100 Einheiten im Lager, knappste zuerst.

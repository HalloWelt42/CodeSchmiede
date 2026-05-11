---
schema_version: 1
id: s133-shop-or-bedingung
revision: 1
titel: "Shop: Bio- oder GartenFrisch-Marken"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [where, or, like]
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
erwartete_spalten: ["name", "marke"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Apfel Boskoop", "Bio-Hof Schulz"]
  - ["Erdbeeren 500g", "Bio-Hof Schulz"]
  - ["Karotte 1kg", "Bio-Hof Schulz"]
  - ["Brokkoli", "GartenFrisch"]
  - ["Gurke", "GartenFrisch"]
  - ["Tomate Strauch", "GartenFrisch"]
hints:
  - kosten: 0
    text: |
      OR + LIKE-Pattern.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bio- oder GartenFrisch

Produkte mit Marke 'Bio-*' oder 'GartenFrisch'.

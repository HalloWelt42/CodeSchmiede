---
schema_version: 1
id: s035-produkte-billig
revision: 1
titel: "Shop: Produkte unter 1 Euro"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [where, vergleich]
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
erwartete_spalten: ["name", "preis"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Banane", 0.3]
  - ["Apfel Boskoop", 0.45]
  - ["Orange Navel", 0.55]
  - ["Tomate Strauch", 0.65]
  - ["Joghurt Natur 500g", 0.89]
  - ["Croissant", 0.99]
hints:
  - kosten: 0
    text: |
      `WHERE preis < 1.0`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Shop: billige Produkte

Name + Preis aller Produkte unter 1 EUR.

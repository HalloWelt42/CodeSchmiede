---
schema_version: 1
id: s061-shop-bestseller
revision: 1
titel: "Shop: meistbestellte Produkte"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join, group-by, sum, limit]
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
erwartete_spalten: ["name", "gesamtmenge"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Banane", 11]
  - ["Apfel Boskoop", 10]
  - ["Tomate Strauch", 10]
  - ["Cola 1L", 5]
  - ["Croissant", 4]
hints:
  - kosten: 0
    text: |
      Summe der `menge` pro Produkt, sortiert absteigend, Top 5.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Top 5 Bestseller

Produktname + verkaufte Gesamtmenge, höchste zuerst.

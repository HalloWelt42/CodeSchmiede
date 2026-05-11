---
schema_version: 1
id: s168-shop-produkte-nicht-bestellt
revision: 1
titel: "Shop: Produkte, die nie bestellt wurden"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [subquery, not-in]
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
erwartete_spalten: ["name"]
sortierung_egal: false
erwartetes_ergebnis:
  []
hints:
  - kosten: 0
    text: |
      NOT IN mit Subquery.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Nie bestellte Produkte

Produkte, die in keiner Bestellung vorkommen.

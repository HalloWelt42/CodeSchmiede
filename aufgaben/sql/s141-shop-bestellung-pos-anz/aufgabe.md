---
schema_version: 1
id: s141-shop-bestellung-pos-anz
revision: 1
titel: "Shop: Bestellung mit meisten Positionen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [group-by, order, limit]
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
erwartete_spalten: ["bestellung_id", "positionen"]
sortierung_egal: false
erwartetes_ergebnis:
  - [3, 4]
hints:
  - kosten: 0
    text: |
      GROUP BY + ORDER DESC + LIMIT 1.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellung mit meisten Positionen

Eine Zeile: ID + Anzahl Positionen der größten Bestellung.

---
schema_version: 1
id: s146-shop-kunden-stadt-bestellungen
revision: 1
titel: "Shop: Bestellungen pro Stadt"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [join, group-by]
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
erwartete_spalten: ["ort", "bestellungen"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Berlin", 4]
  - ["Hamburg", 3]
  - ["München", 3]
  - ["Köln", 2]
  - ["Dresden", 1]
  - ["Frankfurt", 1]
  - ["Leipzig", 1]
  - ["Stuttgart", 1]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY ort.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellungen pro Stadt

Stadt + Anzahl Bestellungen, häufigste zuerst.

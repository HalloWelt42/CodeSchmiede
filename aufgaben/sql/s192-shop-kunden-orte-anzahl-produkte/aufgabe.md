---
schema_version: 1
id: s192-shop-kunden-orte-anzahl-produkte
revision: 1
titel: "Shop: Produkte pro Ort"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join-multi, count-distinct]
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
erwartete_spalten: ["ort", "produkte"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Berlin", 8]
  - ["Hamburg", 6]
  - ["Köln", 6]
  - ["München", 5]
  - ["Dresden", 2]
  - ["Frankfurt", 2]
  - ["Leipzig", 2]
  - ["Stuttgart", 2]
hints:
  - kosten: 0
    text: |
      Drei JOINs + COUNT(DISTINCT produkt_id).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Unterschiedliche Produkte pro Stadt

Stadt + Anzahl unterschiedlicher Produkte, häufigste zuerst.

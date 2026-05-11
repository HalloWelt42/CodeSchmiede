---
schema_version: 1
id: s067-shop-kunden-ohne-bestellung
revision: 1
titel: "Shop: Kunden ohne Bestellung"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [left-join, anti-join, is-null]
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
      LEFT JOIN + WHERE rechte Spalte IS NULL.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Kunden ohne Bestellung

Namen aller Kunden, die noch nichts bestellt haben.

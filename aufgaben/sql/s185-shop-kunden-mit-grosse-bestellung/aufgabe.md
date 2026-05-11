---
schema_version: 1
id: s185-shop-kunden-mit-grosse-bestellung
revision: 1
titel: "Shop: Kunden mit große Bestellung"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 7
tags: [join, group-by, having, distinct]
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
      GROUP BY Bestellung + HAVING Summe.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Kunden mit min. einer Bestellung > 15 EUR

Distinkte Kunden mit mindestens einer Bestellung > 15 EUR Umsatz.

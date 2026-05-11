---
schema_version: 1
id: s068-shop-orte-anzahl
revision: 1
titel: "Shop: Kunden pro Ort"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [group-by, count]
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
erwartete_spalten: ["ort", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Berlin", 3]
  - ["Hamburg", 2]
  - ["München", 2]
  - ["Dresden", 1]
  - ["Frankfurt", 1]
  - ["Köln", 1]
  - ["Leipzig", 1]
  - ["Stuttgart", 1]
hints:
  - kosten: 0
    text: |
      GROUP BY ort.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Kunden pro Ort

Wieviele Kunden in welchem Ort, hauefigster Ort zuerst.

---
schema_version: 1
id: s066-shop-durchschnittspreis-pro-kategorie
revision: 1
titel: "Shop: Durchschnittspreis pro Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, group-by, avg]
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
erwartete_spalten: ["kategorie", "schnitt"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Getraenke", 2.72]
  - ["Suesswaren", 2.24]
  - ["Milchprodukte", 1.99]
  - ["Backwaren", 1.76]
  - ["Gemuese", 1.33]
  - ["Obst", 1.32]
hints:
  - kosten: 0
    text: |
      JOIN + AVG + GROUP BY.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Durchschnittspreis pro Kategorie

Kategorie + gerundeter Durchschnittspreis, teuerste Kategorie zuerst.

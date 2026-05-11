---
schema_version: 1
id: s037-anzahl-pro-kategorie-shop
revision: 1
titel: "Shop: Anzahl Produkte pro Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, group-by, count]
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
erwartete_spalten: ["name", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Gemuese", 4]
  - ["Milchprodukte", 4]
  - ["Obst", 4]
  - ["Backwaren", 3]
  - ["Getraenke", 3]
  - ["Suesswaren", 2]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY auf Kategorie-Name.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Shop: Produkte pro Kategorie

Kategorie-Name + Anzahl Produkte, hauefigste zuerst.

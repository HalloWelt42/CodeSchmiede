---
schema_version: 1
id: s170-shop-kunden-mit-mehreren-kategorien
revision: 1
titel: "Shop: Kunden mit mind. 3 Kategorien"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [join-multi, count-distinct, having]
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
erwartete_spalten: ["name", "kategorien"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Alex Becker", 4]
  - ["Elena Vogel", 4]
  - ["Beate Frank", 3]
hints:
  - kosten: 0
    text: |
      HAVING auf COUNT(DISTINCT kategorie_id).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Vielseitige Kunden

Kunden, die aus min. 3 Kategorien bestellt haben.

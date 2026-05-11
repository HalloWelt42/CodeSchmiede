---
schema_version: 1
id: s148-shop-grosser-bestellungen
revision: 1
titel: "Shop: Grosse Bestellungen (Umsatz > 10 EUR)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [join, group-by, having]
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
erwartete_spalten: ["id", "name", "umsatz"]
sortierung_egal: false
erwartetes_ergebnis:
  - [8, "Elena Vogel", 12.76]
  - [11, "Gisela Hahn", 12.66]
  - [15, "Karin Berger", 12.47]
hints:
  - kosten: 0
    text: |
      HAVING auf aggregierten Umsatz.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Grosse Bestellungen

Bestellung-ID + Kunde + Umsatz für Bestellungen mit > 10 EUR Umsatz.

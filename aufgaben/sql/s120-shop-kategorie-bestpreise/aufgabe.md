---
schema_version: 1
id: s120-shop-kategorie-bestpreise
revision: 1
titel: "Shop: billigstes und teuerstes Produkt pro Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, min, max, group-by]
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
erwartete_spalten: ["kategorie", "min_preis", "max_preis"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Backwaren", 0.99, 2.79]
  - ["Gemüse", 0.65, 1.99]
  - ["Getränke", 1.29, 4.99]
  - ["Milchprodukte", 0.89, 3.29]
  - ["Obst", 0.3, 3.99]
  - ["Süßwaren", 1.99, 2.49]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY + MIN/MAX in einer Zeile.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Min/Max-Preis pro Kategorie

Kategorie + niedrigster und höchster Preis, alphabetisch.

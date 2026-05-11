---
schema_version: 1
id: s199-shop-warenkorb-ueber-zeit
revision: 1
titel: "Shop: Bestellungen + Warenkorb-Größe pro Tag"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join, group-by, sum, count-distinct]
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
erwartete_spalten: ["tag", "bestellungen", "gesamt_stueck"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["2025-03-10", 1, 8]
  - ["2025-03-25", 1, 4]
  - ["2025-03-30", 1, 3]
  - ["2025-04-01", 1, 9]
  - ["2025-04-02", 1, 4]
  - ["2025-04-05", 1, 8]
  - ["2025-04-08", 1, 8]
  - ["2025-04-10", 1, 7]
  - ["2025-04-12", 1, 6]
  - ["2025-04-14", 1, 3]
  - ["2025-04-15", 1, 3]
  - ["2025-04-18", 1, 7]
  - ["2025-04-19", 1, 2]
  - ["2025-04-20", 1, 3]
  - ["2025-04-21", 1, 4]
  - ["2025-04-22", 1, 4]
hints:
  - kosten: 0
    text: |
      Tageweise gruppieren, Bestellungen + Stück zählen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Tagesaktivität

Pro Tag: Anzahl Bestellungen + verkaufte Stückzahl.

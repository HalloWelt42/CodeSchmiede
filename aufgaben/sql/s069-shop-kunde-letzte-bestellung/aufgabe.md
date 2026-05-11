---
schema_version: 1
id: s069-shop-kunde-letzte-bestellung
revision: 1
titel: "Shop: letzte Bestellung pro Kunde"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, max, group-by]
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
erwartete_spalten: ["name", "letzte"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Carla Diaz", "2025-04-22"]
  - ["Hugo Meier", "2025-04-21"]
  - ["Beate Frank", "2025-04-20"]
  - ["Leon Wolf", "2025-04-19"]
  - ["Elena Vogel", "2025-04-18"]
  - ["Alex Becker", "2025-04-15"]
  - ["Karin Berger", "2025-04-14"]
  - ["Daniel Engel", "2025-04-12"]
  - ["Jan Petersen", "2025-04-10"]
  - ["Frank Berger", "2025-04-08"]
  - ["Gisela Hahn", "2025-04-02"]
  - ["Iris Schaefer", "2025-03-30"]
hints:
  - kosten: 0
    text: |
      MAX(Datum) + GROUP BY pro Kunde.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Letzte Bestellung pro Kunde

Name + spaetestes Bestelldatum, neueste zuerst.

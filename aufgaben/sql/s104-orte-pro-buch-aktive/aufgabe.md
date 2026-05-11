---
schema_version: 1
id: s104-orte-pro-buch-aktive
revision: 1
titel: "Shop: Orte pro Produkt (Bestellungen)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [group-concat, distinct, join]
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
erwartete_spalten: ["name", "orte"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Apfel Boskoop", "Berlin,Koeln"]
  - ["Apfelsaft 1L", "Berlin,Muenchen"]
  - ["Banane", "Muenchen"]
  - ["Brokkoli", "Frankfurt,Dresden"]
  - ["Brot Roggen 500g", "Berlin,Koeln,Hamburg"]
  - ["Brötchen 5er-Pack", "Berlin"]
  - ["Butter 250g", "Koeln,Leipzig"]
  - ["Cola 1L", "Hamburg,Stuttgart"]
  - ["Croissant", "Berlin"]
  - ["Erdbeeren 500g", "Berlin"]
  - ["Gouda Scheiben 200g", "Hamburg"]
  - ["Gurke", "Hamburg"]
  - ["Joghurt Natur 500g", "Koeln"]
  - ["Karotte 1kg", "Hamburg,Berlin"]
  - ["Kekse 200g", "Muenchen"]
  - ["Mineralwasser 6x1L", "Koeln,Leipzig"]
  - ["Orange Navel", "Muenchen"]
  - ["Schokolade 100g", "Muenchen,Stuttgart"]
  - ["Tomate Strauch", "Hamburg,Frankfurt"]
  - ["Vollmilch 1L", "Berlin,Koeln,Dresden"]
hints:
  - kosten: 0
    text: |
      GROUP_CONCAT(DISTINCT ...) entfernt Duplikate.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Orte pro Produkt

Produktname + komma-getrennte Liste aller Orte, in die das Produkt bestellt wurde (jeder Ort einmal).

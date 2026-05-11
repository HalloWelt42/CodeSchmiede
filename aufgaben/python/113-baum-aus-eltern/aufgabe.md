---
schema_version: 1
id: 113-baum-aus-eltern
revision: 1
titel: Baum aus Eltern-IDs aufbauen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [dict, baum, listen, sortieren]
pfade: [python_algorithmen2]
voraussetzungen: [022-wortzaehler]
quelle:
  url: null
  notiz: Inspiration aus Exercism (tree-building), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: baue_baum
hints:
  - kosten: 0
    text: |
      Eingabe: Liste von Records `{"id": X, "parent": Y}`. Ausgabe:
      Dict-Baum `{"id": X, "kinder": [...]}`. Wurzel hat id == parent.
  - kosten: 12
    text: |
      Validieren: IDs müssen 0..n-1 sein. Wurzel id=0 muss parent=0
      haben. Bei Fehler -> {}. Erst Knoten anlegen, dann Kinder
      einsortieren -- nach ID aufsteigend.
tests_sichtbar:
  - input: [[{"id": 0, "parent": 0}]]
    expected: { "id": 0, "kinder": [] }
  - input: [[{"id": 0, "parent": 0}, {"id": 1, "parent": 0}]]
    expected: { "id": 0, "kinder": [{ "id": 1, "kinder": [] }] }
  - input: [[]]
    expected: {}
  - input: [[{"id": 1, "parent": 0}]]
    expected: {}
tests_versteckt:
  - input: [[{"id": 0, "parent": 0}, {"id": 1, "parent": 0}, {"id": 2, "parent": 0}]]
    expected: { "id": 0, "kinder": [{ "id": 1, "kinder": [] }, { "id": 2, "kinder": [] }] }
  - input: [[{"id": 0, "parent": 0}, {"id": 1, "parent": 0}, {"id": 2, "parent": 1}, {"id": 3, "parent": 1}]]
    expected: { "id": 0, "kinder": [{ "id": 1, "kinder": [{ "id": 2, "kinder": [] }, { "id": 3, "kinder": [] }] }] }
  - input: [[{"id": 5, "parent": 0}]]
    expected: {}
  - input: [[{"id": 0, "parent": 5}]]
    expected: {}
starter_code: |
  def baue_baum(records: list[dict]) -> dict:
      # Deine Lösung hier -- Records mit "id" + "parent", Ergebnis
      # ist Dict-Baum mit "id" + "kinder" (Liste).
      pass
---

# Baum aus Eltern-IDs aufbauen

Schreibe eine Funktion `baue_baum(records)`, die aus einer flachen
Liste von Knoten-Records einen **verschachtelten Baum** aufbaut.

## Validierungs-Regeln

- IDs müssen genau `0, 1, ..., n-1` sein (keine Lücken)
- Wurzel ist die einzige Node mit `parent == id` (und das muss 0 sein)
- Jeder Knoten außer der Wurzel hat `parent < id`
- Bei einer Verletzung → `{}`

## Sortierung

Kinder pro Knoten nach ID aufsteigend.

## Hintergrund

Klassisches Pattern: **flache DB-Darstellung mit Eltern-Referenz** in
einen **verschachtelten Baum** verwandeln. Standardproblem für
Sortier-und-Sammel-Aufgaben in Daten-Pipelines.

---
schema_version: 1
id: 117-klassen-sortierung
revision: 1
titel: Schüler in Klassen sortieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [dict, listen, gruppierung, sortieren]
pfade: [python_dicts]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (grade-school), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: sortiere_schueler
hints:
  - kosten: 0
    text: |
      Eingabe: Liste `[{"name": ..., "klasse": ...}]`. Ausgabe: Dict
      `{klasse: [namen sortiert]}`. Klassen-Schlüssel als Strings.
  - kosten: 10
    text: |
      `defaultdict(list)`, einsortieren, am Ende jede Liste sortieren.
      Conversion zu plain dict mit gleichen sortierten Werten.
tests_sichtbar:
  - input: [[{"name": "Anna", "klasse": 5}, {"name": "Tom", "klasse": 5}]]
    expected: { "5": ["Anna", "Tom"] }
  - input: [[]]
    expected: {}
  - input: [[{"name": "Lukas", "klasse": 7}]]
    expected: { "7": ["Lukas"] }
  - input: [[{"name": "Tom", "klasse": 5}, {"name": "Anna", "klasse": 5}]]
    expected: { "5": ["Anna", "Tom"] }
tests_versteckt:
  - input: [[{"name": "Tom", "klasse": 5}, {"name": "Lisa", "klasse": 6}, {"name": "Anna", "klasse": 5}, {"name": "Ben", "klasse": 6}]]
    expected: { "5": ["Anna", "Tom"], "6": ["Ben", "Lisa"] }
  - input: [[{"name": "Charlie", "klasse": 1}]]
    expected: { "1": ["Charlie"] }
  - input: [[{"name": "B", "klasse": 1}, {"name": "A", "klasse": 1}, {"name": "C", "klasse": 1}]]
    expected: { "1": ["A", "B", "C"] }
starter_code: |
  def sortiere_schueler(eintraege: list[dict]) -> dict[str, list[str]]:
      # Deine Lösung hier -- pro Klasse Namen alphabetisch.
      pass
---

# Schüler in Klassen sortieren

Schreibe eine Funktion `sortiere_schüler(eintraege)`, die eine
Liste von Schüler-Records nach Klasse gruppiert und die Namen pro
Klasse alphabetisch sortiert.

## Eingabe

```python
[
  {"name": "Tom", "klasse": 5},
  {"name": "Anna", "klasse": 5},
  {"name": "Lisa", "klasse": 6},
]
```

## Ausgabe

```python
{
  "5": ["Anna", "Tom"],
  "6": ["Lisa"],
}
```

Klassen-Schlüssel werden als Strings zurückgegeben (JSON-kompatibel).

## Hintergrund

Klassisches **Group-By**-Pattern, wie es in jeder Daten-Pipeline,
SQL oder Pandas-Aggregation vorkommt. In Python gibt es keinen
eingebauten group-by, aber `defaultdict(list)` ist die Standard-Lösung.

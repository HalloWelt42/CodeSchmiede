---
schema_version: 1
id: 287-bibliothek
revision: 1
titel: Bibliothek mit Buchausleihen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 28
schaetz_minuten: 12
tags: [oop, klassen, dict, set]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Mehr-Methoden-Klasse intern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ausleihen
hints:
  - kosten: 0
    text: |
      Eine Bibliothek hat einen Bestand (Liste von Bücher-Titeln,
      jeder einmal). Operationen:
      ["leihen", titel] → entfernt aus Bestand falls da
      ["zurück", titel] → fuegt zum Bestand hinzu falls nicht da
      ["prüfen", titel] → kein State-Change, gibt aktuellen Bestand zurück
      Liefere den finalen Bestand als sortierte Liste.
  - kosten: 20
    text: |
      Klasse Bibliothek mit set intern.
      Prüfen ist no-op für State, taucht in tests aber als reine Aktion auf.
tests_sichtbar:
  - input: [["A", "B", "C"], [["leihen", "B"]]]
    expected: ["A", "C"]
  - input: [["A", "B"], []]
    expected: ["A", "B"]
  - input: [[], [["zurueck", "A"]]]
    expected: ["A"]
  - input: [["A"], [["leihen", "A"], ["zurueck", "A"]]]
    expected: ["A"]
tests_versteckt:
  - input: [["A", "B", "C"], [["leihen", "Z"]]]
    expected: ["A", "B", "C"]
  - input: [["A", "B", "C"], [["zurueck", "A"]]]
    expected: ["A", "B", "C"]
  - input: [["B", "A"], [["pruefen", "A"]]]
    expected: ["A", "B"]
  - input: [["X"], [["leihen", "X"], ["leihen", "X"], ["zurueck", "X"]]]
    expected: ["X"]
  - input: [[], [["zurueck", "A"], ["zurueck", "B"], ["zurueck", "C"], ["leihen", "B"]]]
    expected: ["A", "C"]
  - input: [["Buch1", "Buch2", "Buch3"], [["leihen", "Buch1"], ["leihen", "Buch2"], ["leihen", "Buch3"]]]
    expected: []
starter_code: |
  def ausleihen(bestand: list[str], operationen: list) -> list[str]:
      # Tipp: Bibliothek als Klasse mit set intern
      pass
---

# Bibliothek mit Buchausleihen

Implementiere `ausleihen(bestand, operationen)` -- eine Bibliothek
hat einen Bestand (jeder Titel einmal), eine Liste von Operationen
modifiziert ihn:

| Operation              | Wirkung                                |
|------------------------|----------------------------------------|
| `["leihen", titel]`    | entfernt titel aus dem Bestand (falls vorhanden) |
| `["zurück", titel]`   | fuegt titel zum Bestand hinzu (falls nicht da)   |
| `["prüfen", titel]`   | keine Änderung -- nur Lese-Op       |

Liefere den **finalen Bestand** als **alphabetisch sortierte** Liste.

## Beispiele

| Bestand          | Ops                                | Ergebnis     |
|------------------|------------------------------------|--------------|
| `["A","B","C"]`  | `[["leihen","B"]]`                 | `["A","C"]`  |
| `["A","B","C"]`  | `[["leihen","Z"]]`                 | `["A","B","C"]` (Z war nicht da) |
| `["A","B","C"]`  | `[["zurück","A"]]`                | `["A","B","C"]` (A war schon da) |
| `["A"]`          | `[["leihen","A"],["zurück","A"]]` | `["A"]`      |
| `[]`             | `[["zurück","A"]]`                | `["A"]`      |

## Idee -- Set + Methoden

```python
class Bibliothek:
    def __init__(self, bestand):
        self.bücher = set(bestand)

    def leihen(self, titel):
        self.bücher.discard(titel)  # discard wirft KEIN KeyError

    def zurück(self, titel):
        self.bücher.add(titel)


def ausleihen(bestand, operationen):
    bib = Bibliothek(bestand)
    for op in operationen:
        if op[0] == "leihen":
            bib.leihen(op[1])
        elif op[0] == "zurück":
            bib.zurück(op[1])
        # "prüfen" ignorieren
    return sorted(bib.bücher)
```

`set.discard(x)` ist wie `set.remove(x)`, wirft aber **keinen
Fehler**, wenn das Element nicht da ist -- ideal für "lösche falls
vorhanden". `set.add(x)` ist idempotent (fuegt nicht doppelt).

## Erweiterung -- Mehrfache Exemplare

In einer echten Bibliothek gibt es Bücher in **mehreren Exemplaren**:
"Der Herr der Ringe" 5x da, davon 3 ausgeliehen. Dafür braucht man
ein `dict[titel, anzahl]` statt eines Sets -- der Sprung von Set zu
Dict ist klein, das Konzept aber maechtig.

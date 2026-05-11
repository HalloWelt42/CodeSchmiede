---
schema_version: 1
id: 119-anagramm-finder
revision: 1
titel: Anagramme aus Liste finden
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, listen, sortieren, vergleich]
pfade: [python_strings3]
voraussetzungen: [008-anagramm-pruefen]
quelle:
  url: null
  notiz: Inspiration aus Exercism (anagram), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: finde_anagramme
hints:
  - kosten: 0
    text: |
      Liefere die Worte aus `kandidaten`, die Anagramme von `wort`
      sind -- Groß-/Kleinschreibung egal. Aber: das Wort selbst
      (gleiche Buchstaben gleich groß/klein) ist KEIN Anagramm.
  - kosten: 15
    text: |
      Sortier-Schlüssel: `sorted(w.lower())`. Vergleiche pro
      Kandidat. Filtere selbe Wort raus (case-insensitive).
tests_sichtbar:
  - input: ["listen", ["enlists", "google", "inlets", "banana"]]
    expected: ["inlets"]
  - input: ["solemn", ["lemons", "cherry", "melons"]]
    expected: ["lemons", "melons"]
  - input: ["diaper", ["hello", "world"]]
    expected: []
  - input: ["LISTEN", ["Listen", "Silent"]]
    expected: ["Silent"]
tests_versteckt:
  - input: ["", []]
    expected: []
  - input: ["a", ["A"]]
    expected: []
  - input: ["BANANA", ["banana"]]
    expected: []
  - input: ["allergy", ["gallery", "ballerina", "regally", "clergy", "largely"]]
    expected: ["gallery", "regally", "largely"]
  - input: ["mass", ["last", "amass", "gnat"]]
    expected: []
starter_code: |
  def finde_anagramme(wort: str, kandidaten: list[str]) -> list[str]:
      # Deine Lösung hier -- Reihenfolge wie in `kandidaten`. Selbes Wort
      # (case-insensitive) zählt nicht als Anagramm.
      pass
---

# Anagramme aus Liste finden

Schreibe eine Funktion `finde_anagramme(wort, kandidaten)`, die alle
Wörter aus `kandidaten` zurückgibt, die **Anagramme** von `wort` sind.

- Groß-/Kleinschreibung wird ignoriert beim Vergleich
- Das Wort selbst (gleiche Buchstaben in gleicher Reihenfolge,
  case-insensitive) zählt **nicht** als Anagramm
- Reihenfolge der Treffer wie in der Eingabe-Liste

## Beispiele

| Wort      | Kandidaten                                  | Treffer            |
|-----------|---------------------------------------------|--------------------|
| `listen`  | `[enlists, google, inlets, banana]`         | `[inlets]`         |
| `solemn`  | `[lemons, cherry, melons]`                  | `[lemons, melons]` |
| `LISTEN`  | `[Listen, Silent]`                          | `[Silent]`         |
| `BANANA`  | `[banana]`                                  | `[]` (selbes Wort) |

## Hintergrund

Verwandt mit Aufgabe 109 (Anagramm-Gruppen), aber gerichteter:
Hier sucht man Anagramme zu einem **bestimmten** Wort. Klassische
Datenstruktur-Übung im Algorithmen-Kurs.

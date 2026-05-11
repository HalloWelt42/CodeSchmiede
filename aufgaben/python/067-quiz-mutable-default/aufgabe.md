---
schema_version: 1
id: 067-quiz-mutable-default
revision: 1
titel: Mutable Default -- was passiert?
sprache: python
task_type: output_quiz
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 5
tags: [quiz, defaults, falle, output]
pfade: [python_quiz]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Python-Stolperfalle
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
hints: []
quiz:
  code: |
    def add(x, lst=[]):
        lst.append(x)
        return lst

    print(add(1))
    print(add(2))
    print(add(3))
  optionen:
    - "[1]\n[2]\n[3]"
    - "[1]\n[1, 2]\n[1, 2, 3]"
    - "[1]\n[1, 2]\n[2, 3]"
    - "[]\n[]\n[]"
  richtig_index: 1
---

# Mutable Default -- was passiert?

Schau dir den Code genau an. Was wird ausgegeben?

## Hintergrund

In Python wird der **Default-Wert eines Parameters genau einmal**
ausgewertet -- beim Definieren der Funktion. Wenn der Default ein
**veraenderliches Objekt** ist (Liste, Dict, Set, ...), teilen sich
**alle Aufrufe** dasselbe Objekt.

Das ist eine der **klassischsten Stolperfallen** in Python und ein
Standard-Test in Code-Reviews.


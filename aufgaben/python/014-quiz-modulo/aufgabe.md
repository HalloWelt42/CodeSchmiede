---
schema_version: 1
id: 014-quiz-modulo
revision: 1
titel: Was gibt der Modulo-Code aus?
sprache: python
task_type: output_quiz
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [quiz, modulo, output, lesen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Erste Output-Quiz-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
hints: []
quiz:
  code: |
    for i in range(5):
        if i % 2 == 0:
            print(i)
  optionen:
    - "0\n1\n2\n3\n4"
    - "0\n2\n4"
    - "1\n3"
    - "2\n4"
  richtig_index: 1
---

# Was gibt der Modulo-Code aus?

Lies den Code aufmerksam und wähle die korrekte Ausgabe.

Diese Aufgabe trainiert deinen **Blick fürs Code-Lesen** -- ohne Editor,
ohne Tipp-Arbeit. Schaffst du es, die Schleife im Kopf laufen zu lassen?

## Hinweise

- `range(5)` liefert die Zahlen 0, 1, 2, 3, 4.
- `i % 2 == 0` ist `True`, wenn `i` gerade ist.
- `print(i)` gibt jede Zahl in eine eigene Zeile.

---
schema_version: 1
id: 068-quiz-late-binding
revision: 1
titel: Late-Binding-Closure
sprache: python
task_type: output_quiz
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 20
schaetz_minuten: 6
tags: [quiz, closures, falle, output]
pfade: [python_quiz]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Python-Falle, oft im Interview
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
hints: []
quiz:
  code: |
    funktionen = []
    for i in range(3):
        funktionen.append(lambda: i)
    for f in funktionen:
        print(f())
  optionen:
    - "0\n1\n2"
    - "2\n2\n2"
    - "0\n0\n0"
    - "1\n2\n3"
  richtig_index: 1
---

# Late-Binding-Closure

Was wird hier ausgegeben?

## Hintergrund

In Python "merkt" sich eine **Closure** den **Namen** der Variable,
nicht den **Wert**. Wenn die Lambda spaeter aufgerufen wird, schaut
sie nach, **was `i` jetzt ist** -- und `i` ist nach der Schleife `2`.

Alle drei Lambdas zeigen also auf dasselbe `i` und liefern den
letzten Wert.

## Workaround

Um den Wert zur Definitionszeit zu binden:

```python
funktionen.append(lambda i=i: i)
```

Der Default-Parameter `i=i` erzeugt eine eigene lokale Variable in
jeder Lambda -- die wird zur Definitionszeit ausgewertet.

## Hinweis

Diese Falle ist so beruehmt, dass viele moderne Linter und IDEs
warnen, sobald sie eine Lambda in einer Schleife sehen.

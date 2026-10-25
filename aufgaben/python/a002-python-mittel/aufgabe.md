---
schema_version: 1
id: a002-python-mittel
revision: 1
titel: Python, Mittel
sprache: python
task_type: ausgabe_sprint
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 15
schaetz_minuten: 2
tags: [ausgabe-sprint, code-lesen]
voraussetzungen: []
quelle:
  url: null
  notiz: Ausgabe-Sprint, Python, Mittel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
hints: []
sprint:
  fragen: 10
  sekunden: 90
  sterne: [6, 8, 10]
  schnipsel:
    - code: "x = [1, 2, 3]\ny = x\ny.append(4)\nprint(len(x))"
      optionen: ["None", "3", "Fehler", "4"]
      richtig: 3
      warum: "y ist kein neues Objekt, sondern ein zweiter Name für dieselbe Liste."
    - code: "print(0.1 + 0.2 == 0.3)"
      optionen: ["0.3", "False", "Fehler", "True"]
      richtig: 1
      warum: "0.1 und 0.2 sind binär nicht genau darstellbar; die Summe ist 0.30000000000000004."
    - code: "print(bool([]), bool([0]))"
      optionen: ["True True", "False True", "False False", "True False"]
      richtig: 1
      warum: "Eine leere Liste ist falsch, eine Liste mit einem Element wahr, egal welches."
    - code: "for i in range(2, 8, 3):\n    print(i, end=\" \")"
      optionen: ["3 6", "2 5 8", "2 4 6", "2 5"]
      richtig: 3
      warum: "range endet vor 8: erst 2, dann 5, die 8 gehört nicht mehr dazu."
    - code: "a, b = 5, 2\nprint(a // b, a % b)"
      optionen: ["2 1", "2.5 1", "3 1", "2 2"]
      richtig: 0
      warum: "// ist die ganzzahlige Division, % der Rest."
    - code: "print(max(\"Apfel\", \"apfel\"))"
      optionen: ["apfel", "Apfel", "Fehler", "True"]
      richtig: 0
      warum: "Texte vergleicht Python Zeichen für Zeichen; Kleinbuchstaben stehen im Zeichensatz hinter den Großbuchstaben."
    - code: "d = {\"a\": 1}\nprint(d.get(\"b\", 0) + 1)"
      optionen: ["Fehler", "2", "None", "1"]
      richtig: 3
      warum: "get liefert die Vorgabe 0, wenn der Schlüssel fehlt."
    - code: "print(sorted([3, 1, 2])[-1])"
      optionen: ["1", "3", "2", "[3]"]
      richtig: 1
      warum: "-1 ist das letzte Element der sortierten Liste."
    - code: "def f(x, l=[]):\n    l.append(x)\n    return len(l)\nf(1)\nprint(f(2))"
      optionen: ["[1, 2]", "1", "Fehler", "2"]
      richtig: 3
      warum: "Der Vorgabewert [] entsteht einmal beim Anlegen der Funktion und wird von allen Aufrufen geteilt."
    - code: "print([i * i for i in range(4) if i % 2])"
      optionen: ["[1, 9]", "[1, 4, 9]", "[0, 4]", "[0, 1, 4, 9]"]
      richtig: 0
      warum: "i % 2 ist nur für ungerade i wahr: 1 und 3, quadriert 1 und 9."
    - code: "s = {1, 2, 2, 3}\nprint(len(s))"
      optionen: ["Fehler", "4", "3", "2"]
      richtig: 2
      warum: "Eine Menge hält jeden Wert nur einmal."
    - code: "t = (1, 2)\nt[0] = 5\nprint(t)"
      optionen: ["(5, 2)", "[5, 2]", "Fehler", "(1, 2)"]
      richtig: 2
      warum: "Tupel lassen sich nicht ändern: TypeError."
    - code: "print(\"a,b,,c\".split(\",\"))"
      optionen: ["['a', 'b', 'c']", "['a,b,,c']", "['a', 'b', '', 'c']", "Fehler"]
      richtig: 2
      warum: "Zwischen zwei Kommas steht ein leerer Text, der mitgezählt wird."
    - code: "print(list(zip([1, 2, 3], \"ab\")))"
      optionen: ["[(1, 'a'), (2, 'b'), (3, None)]", "[1, 'a', 2, 'b']", "[(1, 'a'), (2, 'b')]", "Fehler"]
      richtig: 2
      warum: "zip hört auf, sobald die kürzere Folge zu Ende ist."
    - code: "x = 10\ndef f():\n    x = 5\nf()\nprint(x)"
      optionen: ["10", "Fehler", "5", "None"]
      richtig: 0
      warum: "x = 5 in der Funktion legt ein neues, lokales x an; das äußere bleibt 10."
    - code: "print(3 > 2 > 1)"
      optionen: ["Fehler", "False", "1", "True"]
      richtig: 3
      warum: "Vergleiche lassen sich verketten: 3 > 2 und 2 > 1."
    - code: "print(None or \"Gast\")"
      optionen: ["Gast", "None", "False", "Fehler"]
      richtig: 0
      warum: "or liefert den ersten wahren Wert; None ist falsch."
    - code: "print([1, 2] * 2)"
      optionen: ["[1, 2, 1, 2]", "Fehler", "[[1, 2], [1, 2]]", "[2, 4]"]
      richtig: 0
      warum: "Eine Liste mal einer Zahl wiederholt ihre Elemente."
    - code: "a = [1, 2, 3]\nprint(a[5:])"
      optionen: ["[]", "[3]", "Fehler", "None"]
      richtig: 0
      warum: "Ein Ausschnitt außerhalb der Liste ist leer, kein Fehler; nur a[5] wäre einer."
    - code: "print(type(3 / 1).__name__)"
      optionen: ["Fehler", "number", "float", "int"]
      richtig: 2
      warum: "/ liefert immer eine Kommazahl, auch wenn die Division aufgeht."
    - code: "n = [3, 1, 2]\nn.sort()\nprint(n.sort())"
      optionen: ["Fehler", "[3, 1, 2]", "None", "[1, 2, 3]"]
      richtig: 2
      warum: "sort sortiert an Ort und Stelle und gibt None zurück."
---

# Python, Mittel

Zehn kurze Python-Schnipsel, 90 Sekunden: Was gibt der Code aus? Richtige Antworten in Folge bilden eine Kette.
Nach der Runde steht bei jeder Frage die richtige Antwort mit einer kurzen Erklärung.

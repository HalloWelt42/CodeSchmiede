---
schema_version: 1
id: a001-python-anfaenger
revision: 1
titel: Python, Anfänger
sprache: python
task_type: ausgabe_sprint
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 2
tags: [ausgabe-sprint, code-lesen]
voraussetzungen: []
quelle:
  url: null
  notiz: Ausgabe-Sprint, Python, Anfänger
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
hints: []
sprint:
  fragen: 10
  sekunden: 90
  sterne: [6, 8, 10]
  schnipsel:
    - code: "print(3 * \"ab\")"
      optionen: ["Fehler", "ab3", "ababab", "3ab"]
      richtig: 2
      warum: "Ein Text mal einer ganzen Zahl wiederholt den Text."
    - code: "print(7 // 2)"
      optionen: ["3.5", "4", "3.0", "3"]
      richtig: 3
      warum: "// teilt ganzzahlig und rundet dabei ab."
    - code: "print(7 / 2)"
      optionen: ["3", "3.5", "3,5", "4"]
      richtig: 1
      warum: "/ teilt immer mit Kommastellen, auch bei ganzen Zahlen."
    - code: "print(2 ** 3)"
      optionen: ["23", "9", "8", "6"]
      richtig: 2
      warum: "** ist die Potenz: 2 hoch 3."
    - code: "print(10 % 3)"
      optionen: ["0", "1", "3", "3.33"]
      richtig: 1
      warum: "% liefert den Rest der ganzzahligen Division: 10 = 3 * 3 + 1."
    - code: "print(\"Code\"[1])"
      optionen: ["d", "Co", "o", "C"]
      richtig: 2
      warum: "Die Zählung beginnt bei 0, Stelle 1 ist das zweite Zeichen."
    - code: "print(len(\"Hallo Welt\"))"
      optionen: ["9", "2", "11", "10"]
      richtig: 3
      warum: "Das Leerzeichen zählt als Zeichen mit."
    - code: "print(\"Code\"[-1])"
      optionen: ["Fehler", "e", "d", "C"]
      richtig: 1
      warum: "Negative Stellen zählen von hinten, -1 ist das letzte Zeichen."
    - code: "x = 5\nx += 2\nprint(x)"
      optionen: ["5", "2", "7", "52"]
      richtig: 2
      warum: "x += 2 ist kurz für x = x + 2."
    - code: "print(\"5\" + \"3\")"
      optionen: ["8", "Fehler", "5 + 3", "53"]
      richtig: 3
      warum: "Zwei Texte werden mit + aneinandergehängt, nicht addiert."
    - code: "print(\"5\" + 3)"
      optionen: ["5 3", "Fehler", "53", "8"]
      richtig: 1
      warum: "Text und Zahl lassen sich nicht mit + verbinden: TypeError."
    - code: "print(int(\"12\") + 1)"
      optionen: ["Fehler", "121", "12", "13"]
      richtig: 3
      warum: "int(\"12\") macht aus dem Text die Zahl 12."
    - code: "print(round(2.5))"
      optionen: ["3.0", "2.5", "2", "3"]
      richtig: 2
      warum: "Bei genau ,5 rundet Python zur geraden Zahl."
    - code: "print(bool(\"\"), bool(\"0\"))"
      optionen: ["False False", "True False", "False True", "True True"]
      richtig: 2
      warum: "Ein leerer Text ist falsch, jeder andere wahr, auch \"0\"."
    - code: "for i in range(3):\n    print(i, end=\" \")"
      optionen: ["1 2 3", "1 2", "0 1 2 3", "0 1 2"]
      richtig: 3
      warum: "range(3) liefert 0, 1 und 2; die 3 selbst nicht."
    - code: "print(max(3, 9, 4))"
      optionen: ["9", "3", "4", "16"]
      richtig: 0
      warum: "max liefert den größten Wert."
    - code: "print(\"abc\".upper())"
      optionen: ["ABC", "aBC", "Abc", "abc"]
      richtig: 0
      warum: "upper macht alle Buchstaben groß."
    - code: "liste = [1, 2, 3]\nprint(liste[1])"
      optionen: ["[1]", "2", "1", "3"]
      richtig: 1
      warum: "Die Zählung beginnt bei 0, Stelle 1 ist das zweite Element."
    - code: "print(1 == 1.0)"
      optionen: ["1.0", "True", "Fehler", "False"]
      richtig: 1
      warum: "Ganzzahl und Kommazahl mit gleichem Wert sind gleich."
    - code: "print(not True or True)"
      optionen: ["None", "False", "Fehler", "True"]
      richtig: 3
      warum: "not bindet stärker als or: (not True) or True ist True."
    - code: "print(len([1, [2, 3]]))"
      optionen: ["2", "1", "3", "Fehler"]
      richtig: 0
      warum: "Die innere Liste ist ein einziges Element."
    - code: "print(\"Hallo\"[1:3])"
      optionen: ["Ha", "al", "allo", "all"]
      richtig: 1
      warum: "Der Ausschnitt beginnt bei Stelle 1 und endet vor Stelle 3."
---

# Python, Anfänger

Zehn kurze Python-Schnipsel, 90 Sekunden: Was gibt der Code aus? Richtige Antworten in Folge bilden eine Kette.
Nach der Runde steht bei jeder Frage die richtige Antwort mit einer kurzen Erklärung.

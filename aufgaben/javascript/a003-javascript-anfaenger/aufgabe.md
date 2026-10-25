---
schema_version: 1
id: a003-javascript-anfaenger
revision: 1
titel: JavaScript, Anfänger
sprache: javascript
task_type: ausgabe_sprint
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 2
tags: [ausgabe-sprint, code-lesen]
voraussetzungen: []
quelle:
  url: null
  notiz: Ausgabe-Sprint, JavaScript, Anfänger
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
hints: []
sprint:
  fragen: 10
  sekunden: 90
  sterne: [6, 8, 10]
  schnipsel:
    - code: "console.log(\"5\" + 3)"
      optionen: ["Fehler", "NaN", "53", "8"]
      richtig: 2
      warum: "Ist eine Seite ein Text, hängt + zusammen statt zu addieren."
    - code: "console.log(\"5\" - 3)"
      optionen: ["2", "NaN", "Fehler", "53"]
      richtig: 0
      warum: "- gibt es nur für Zahlen, also wird \"5\" zur Zahl 5."
    - code: "console.log(typeof null)"
      optionen: ["undefined", "null", "Fehler", "object"]
      richtig: 3
      warum: "Eine alte Eigenheit der Sprache: typeof null ist \"object\"."
    - code: "console.log(0.1 + 0.2 === 0.3)"
      optionen: ["false", "true", "Fehler", "0.3"]
      richtig: 0
      warum: "0.1 und 0.2 sind binär nicht genau darstellbar; die Summe ist 0.30000000000000004."
    - code: "console.log([1, 2, 3].length)"
      optionen: ["undefined", "3", "4", "2"]
      richtig: 1
      warum: "length ist die Zahl der Elemente."
    - code: "let x = 5;\nx++;\nconsole.log(x);"
      optionen: ["6", "5", "7", "NaN"]
      richtig: 0
      warum: "x++ erhöht x um eins."
    - code: "console.log(\"Code\"[0])"
      optionen: ["C", "Code", "o", "undefined"]
      richtig: 0
      warum: "Die Zählung beginnt bei 0."
    - code: "console.log(10 % 4)"
      optionen: ["0", "4", "2.5", "2"]
      richtig: 3
      warum: "% liefert den Rest: 10 = 2 * 4 + 2."
    - code: "console.log(Math.max(3, 9, 4))"
      optionen: ["3", "4", "16", "9"]
      richtig: 3
      warum: "Math.max liefert den größten Wert."
    - code: "console.log(\"abc\".toUpperCase())"
      optionen: ["abc", "ABC", "aBC", "Abc"]
      richtig: 1
      warum: "toUpperCase macht alle Buchstaben groß."
    - code: "console.log(1 == \"1\")"
      optionen: ["Fehler", "1", "false", "true"]
      richtig: 3
      warum: "== wandelt vor dem Vergleich um: \"1\" wird zur Zahl 1."
    - code: "console.log(1 === \"1\")"
      optionen: ["true", "Fehler", "undefined", "false"]
      richtig: 3
      warum: "=== wandelt nicht um; Zahl und Text sind verschieden."
    - code: "console.log([1, 2, 3].indexOf(4))"
      optionen: ["undefined", "0", "4", "-1"]
      richtig: 3
      warum: "indexOf liefert -1, wenn der Wert fehlt."
    - code: "const a = [1, 2];\na.push(3);\nconsole.log(a.length);"
      optionen: ["Fehler", "2", "4", "3"]
      richtig: 3
      warum: "const verbietet nur eine neue Zuweisung; die Liste selbst darf wachsen."
    - code: "console.log(Boolean(\"\"))"
      optionen: ["false", "undefined", "\"\"", "true"]
      richtig: 0
      warum: "Ein leerer Text ist falsch."
    - code: "console.log(7 / 2)"
      optionen: ["3.5", "3", "3,5", "4"]
      richtig: 0
      warum: "/ teilt mit Kommastellen; ganzzahlig teilt es nur mit Math.floor."
    - code: "console.log(Math.floor(-2.5))"
      optionen: ["-2", "-2.5", "-3", "2"]
      richtig: 2
      warum: "floor rundet immer nach unten, bei negativen Zahlen also weg von null."
    - code: "console.log(\"Hallo\".slice(1, 3))"
      optionen: ["al", "all", "Ha", "alo"]
      richtig: 0
      warum: "slice beginnt bei Stelle 1 und endet vor Stelle 3."
    - code: "let s = 0;\nfor (let i = 1; i <= 3; i++) s += i;\nconsole.log(s);"
      optionen: ["5", "6", "3", "0"]
      richtig: 1
      warum: "Die Schleife addiert 1, 2 und 3."
    - code: "console.log(typeof NaN)"
      optionen: ["undefined", "object", "number", "NaN"]
      richtig: 2
      warum: "NaN heißt nicht eine Zahl, ist aber selbst vom Typ number."
    - code: "console.log(2 ** 10)"
      optionen: ["2048", "1024", "20", "100"]
      richtig: 1
      warum: "** ist die Potenz: 2 hoch 10."
    - code: "console.log(\"3\" * \"4\")"
      optionen: ["NaN", "34", "Fehler", "12"]
      richtig: 3
      warum: "* gibt es nur für Zahlen, also werden beide Texte zu Zahlen."
---

# JavaScript, Anfänger

Zehn kurze JavaScript-Schnipsel, 90 Sekunden: Was gibt der Code aus? Richtige Antworten in Folge bilden eine Kette.
Nach der Runde steht bei jeder Frage die richtige Antwort mit einer kurzen Erklärung.

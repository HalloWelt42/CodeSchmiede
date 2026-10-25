---
schema_version: 1
id: a004-javascript-mittel
revision: 1
titel: JavaScript, Mittel
sprache: javascript
task_type: ausgabe_sprint
runner_type: docker_javascript
schwierigkeit: mittel
schwierigkeit_score: 15
schaetz_minuten: 2
tags: [ausgabe-sprint, code-lesen]
voraussetzungen: []
quelle:
  url: null
  notiz: Ausgabe-Sprint, JavaScript, Mittel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
hints: []
sprint:
  fragen: 10
  sekunden: 90
  sterne: [6, 8, 10]
  schnipsel:
    - code: "console.log([10, 1, 3].sort().join(\" \"))"
      optionen: ["3 1 10", "1 10 3", "10 3 1", "1 3 10"]
      richtig: 1
      warum: "Ohne Vergleichsfunktion sortiert sort als Text: \"10\" steht vor \"3\"."
    - code: "console.log(0.1 * 3)"
      optionen: ["0.3", "0.30000000000000004", "Fehler", "0.33"]
      richtig: 1
      warum: "0.1 ist binär nicht genau darstellbar; der Fehler wird beim Malnehmen sichtbar."
    - code: "console.log(typeof [])"
      optionen: ["object", "array", "undefined", "list"]
      richtig: 0
      warum: "Listen sind Objekte; ob etwas eine Liste ist, prüft Array.isArray."
    - code: "console.log([1, 2, 3] == \"1,2,3\")"
      optionen: ["Fehler", "true", "undefined", "false"]
      richtig: 1
      warum: "== wandelt die Liste in den Text \"1,2,3\" um."
    - code: "let a = [1, 2];\nlet b = a;\nb.push(3);\nconsole.log(a.length);"
      optionen: ["2", "3", "undefined", "Fehler"]
      richtig: 1
      warum: "b ist keine Kopie, sondern ein zweiter Name für dieselbe Liste."
    - code: "console.log(parseInt(\"12px\"))"
      optionen: ["Fehler", "12px", "12", "NaN"]
      richtig: 2
      warum: "parseInt liest Ziffern, bis etwas anderes kommt."
    - code: "console.log(Number(\"12px\"))"
      optionen: ["Fehler", "0", "NaN", "12"]
      richtig: 2
      warum: "Number verlangt, dass der ganze Text eine Zahl ist."
    - code: "console.log(null ?? \"Gast\", 0 || \"leer\")"
      optionen: ["null leer", "Gast leer", "null 0", "Gast 0"]
      richtig: 1
      warum: "?? ersetzt nur null und undefined, || jeden falschen Wert, auch 0."
    - code: "console.log(0 ?? 5)"
      optionen: ["Fehler", "null", "5", "0"]
      richtig: 3
      warum: "?? greift nur bei null und undefined; 0 bleibt."
    - code: "const o = { a: 1 };\nconst k = { ...o, a: 2 };\nconsole.log(o.a, k.a);"
      optionen: ["2 1", "2 2", "1 2", "1 1"]
      richtig: 2
      warum: "Die Ausbreitung kopiert o; a: 2 überschreibt nur in der Kopie."
    - code: "console.log([1, 2, 3].map(x => x * 2).filter(x => x > 2).join(\",\"))"
      optionen: ["4,6", "2,4,6", "6", "4"]
      richtig: 0
      warum: "map verdoppelt zu 2, 4, 6; filter behält, was größer als 2 ist."
    - code: "console.log(\"abc\".split(\"\").reverse().join(\"\"))"
      optionen: ["abc", "Fehler", "cba", "c,b,a"]
      richtig: 2
      warum: "Zerlegen, umdrehen, wieder zusammensetzen."
    - code: "let i = 0;\nconst f = () => i++;\nf();\nf();\nconsole.log(i);"
      optionen: ["1", "0", "undefined", "2"]
      richtig: 3
      warum: "Jeder Aufruf erhöht dasselbe äußere i."
    - code: "console.log([...\"hallo\"].length)"
      optionen: ["4", "5", "undefined", "1"]
      richtig: 1
      warum: "Die Ausbreitung zerlegt den Text in einzelne Zeichen."
    - code: "console.log(typeof (() => {}))"
      optionen: ["object", "function", "undefined", "arrow"]
      richtig: 1
      warum: "Pfeilfunktionen sind Funktionen."
    - code: "for (var i = 0; i < 3; i++) {}\nconsole.log(i);"
      optionen: ["3", "2", "undefined", "Fehler"]
      richtig: 0
      warum: "var gilt in der ganzen Funktion, nicht nur in der Schleife; nach der Schleife ist i 3."
    - code: "for (let j = 0; j < 3; j++) {}\nconsole.log(j);"
      optionen: ["3", "2", "undefined", "Fehler"]
      richtig: 3
      warum: "let gilt nur in der Schleife; danach gibt es j nicht: ReferenceError."
    - code: "console.log([3, 1, 2].sort((a, b) => a - b)[0])"
      optionen: ["3", "1", "2", "Fehler"]
      richtig: 1
      warum: "Mit Vergleichsfunktion sortiert sort nach Zahlen aufsteigend."
    - code: "console.log(Math.round(-2.5))"
      optionen: ["-2.5", "-3", "-2", "2"]
      richtig: 2
      warum: "Math.round rundet bei ,5 nach oben, bei negativen Zahlen also Richtung null."
    - code: "console.log(isNaN(\"abc\"), Number.isNaN(\"abc\"))"
      optionen: ["false true", "true true", "true false", "false false"]
      richtig: 2
      warum: "isNaN wandelt erst in eine Zahl um, Number.isNaN prüft nur, ob der Wert selbst NaN ist."
    - code: "const z = [1, 2, 3];\nz.length = 1;\nconsole.log(z);"
      optionen: ["Fehler", "[ 1 ]", "[ 1, 2, 3 ]", "1"]
      richtig: 1
      warum: "Eine kleinere length kürzt die Liste."
---

# JavaScript, Mittel

Zehn kurze JavaScript-Schnipsel, 90 Sekunden: Was gibt der Code aus? Richtige Antworten in Folge bilden eine Kette.
Nach der Runde steht bei jeder Frage die richtige Antwort mit einer kurzen Erklärung.

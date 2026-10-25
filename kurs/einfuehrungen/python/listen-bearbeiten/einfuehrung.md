---
id: py-listen-bearbeiten
sprache: python
titel: Listen bearbeiten
kurz: Anhängen, herausnehmen, sortieren, auswerten und Listen in einer Zeile bauen.
fuehrt_ein: [listenmethoden, auswerten, abstraktion]
lernziele:
  - Listen mit append, insert, remove und pop verändern
  - Listen mit sum, min, max und sorted auswerten und mit sort ordnen
  - eine neue Liste in einer Zeile aus einer alten bauen
karte: Ich räume Listen auf wie ein Profi
bilder:
  - schluessel: karte_py_listen_bearbeiten
    art: sammelkarte
    sprache: python
    motiv: Ein Koch schneidet eine lange Salami in Scheiben und ordnet sie der Größe nach
---

## Anhängen und herausnehmen

Listen haben eigene Methoden, die sie direkt verändern: `append(x)` hängt hinten an, `insert(i, x)` schiebt an Stelle i ein, `remove(x)` nimmt den ersten Wert x heraus, `pop()` nimmt das letzte Element heraus und gibt es zurück. Anders als bei Text ändert sich die Liste selbst.

```beispiel
id: veraendern
code: |
  schlange = ["Pit", "Pia"]
  schlange.append("Paul")
  schlange.insert(0, "Polly")
  schlange.remove("Pit")
  letzter = schlange.pop()
  print(schlange)
  print(letzter)
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        ['Polly', 'Pia']
        Paul
      richtig: true
      erklaerung: Richtig. Paul kommt hinten dran, Polly nach vorn, Pit geht, und pop holt Paul wieder hinten heraus.
    - text: |-
        ['Polly', 'Pia', 'Paul']
        Paul
      erklaerung: pop nimmt das letzte Element nicht nur, es entfernt es auch aus der Liste.
    - text: |-
        ['Pit', 'Pia', 'Paul']
        Polly
      erklaerung: Die Methoden verändern die Liste selbst; Polly steht vorn, Pit ist entfernt.
```

```falle
titel: Ergebnis von append aufheben
text: "`schlange = schlange.append(\"Paul\")` macht die Liste kaputt: append ändert die Liste und liefert `None` zurück. Einfach `schlange.append(\"Paul\")` schreiben."
```

```frage
frageart: luecke
id: luecke-append
text: Ergänze die Methode, die "Lachs" hinten anhängt.
code: vorrat.___("Lachs")
antworten: [["append"]]
erklaerung: Richtig, append hängt hinten an.
hinweis: Das englische Wort für "anhängen".
```

## Auswerten und ordnen

Für Zahlenlisten gibt es fertige Helfer: `sum` zählt zusammen, `min` und `max` finden das Kleinste und Größte. `sorted(liste)` liefert eine neue, sortierte Liste; `liste.sort()` sortiert die Liste selbst. Mit `reverse=True` geht es absteigend.

```beispiel
id: auswerten
code: |
  faenge = [3, 9, 2, 7]
  print(sum(faenge), min(faenge), max(faenge))
  print(sorted(faenge))
  print(faenge)
  faenge.sort(reverse=True)
  print(faenge)
vorhersage:
  art: eintippen
  erklaerung: "21 2 9, dann die sortierte Kopie [2, 3, 7, 9]; faenge selbst ist noch unverändert [3, 9, 2, 7], bis sort es absteigend ordnet: [9, 7, 3, 2]."
```

```frage
frageart: auswahl
id: sorted-oder-sort
text: Was ist der Unterschied zwischen `sorted(liste)` und `liste.sort()`?
optionen:
  - text: sorted liefert eine neue Liste, sort ordnet die Liste selbst.
    richtig: true
    erklaerung: Richtig. sorted lässt das Original in Ruhe.
  - text: Es gibt keinen.
    erklaerung: Doch, sort verändert die Liste, sorted nicht.
  - text: sort liefert eine neue Liste, sorted ordnet die Liste selbst.
    erklaerung: Genau umgekehrt.
```

## Listen in einer Zeile bauen

Oft entsteht eine neue Liste aus einer alten: jedes Element verdoppelt, nur die großen, alle in Großbuchstaben. Dafür gibt es eine Kurzschreibweise in eckigen Klammern, die Listenabstraktion: `[ausdruck for x in liste]`, mit Bedingung `[ausdruck for x in liste if bedingung]`.

```beispiel
id: abstraktion
code: |
  faenge = [3, 9, 2, 7]
  doppelt = [f * 2 for f in faenge]
  grosse = [f for f in faenge if f > 4]
  print(doppelt)
  print(grosse)
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        [6, 18, 4, 14]
        [9, 7]
      richtig: true
      erklaerung: Richtig. Jedes Element verdoppelt; dann nur die, die größer als 4 sind.
    - text: |-
        [6, 18, 4, 14]
        [9, 7, 3, 2]
      erklaerung: Die Bedingung if f > 4 lässt nur die großen Fänge durch.
    - text: |-
        [3, 9, 2, 7, 3, 9, 2, 7]
        [9, 7]
      erklaerung: f * 2 rechnet mit jedem Element, es verdoppelt nicht die Liste.
```

```merke
text: "`[f * 2 for f in faenge]` liest sich wie: für jedes f in faenge nimm f mal 2. Dasselbe ginge mit leerer Liste, for und append, nur länger."
```

```frage
frageart: fehlerstelle
id: fehler-append-none
text: Das Programm soll [1, 2, 3] ausgeben, gibt aber None aus. Welche Zeile?
code: |
  zahlen = [1, 2]
  zahlen = zahlen.append(3)
  print(zahlen)
zeile: 2
erklaerung: Genau. append verändert die Liste und liefert None; die Zuweisung überschreibt die Liste damit.
hinweis: Was liefert append zurück?
```

```augenzwinkern
text: Sortieren, filtern, verdoppeln, in einer Zeile. Dein Notenbuch sieht inzwischen ordentlicher aus als so mancher Schreibtisch.
```

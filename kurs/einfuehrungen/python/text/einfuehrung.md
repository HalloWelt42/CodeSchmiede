---
id: py-text
sprache: python
titel: Text
kurz: Text zusammensetzen, Werte einsetzen, Zeichen zählen, herauspicken und umbauen.
fuehrt_ein: [fstring, laenge, index, scheiben, textmethoden]
lernziele:
  - Text mit + verbinden und mit * wiederholen
  - Werte mit f-Strings in Text einsetzen
  - die Länge eines Texts bestimmen und einzelne Zeichen über ihren Index holen
  - Ausschnitte nehmen und Text mit Methoden wie upper und replace umbauen
karte: Ich fädle Buchstaben auf wie Perlen
bilder:
  - schluessel: karte_py_text
    art: sammelkarte
    sprache: python
    motiv: Buchstaben als bunte Perlen auf einer Kette, eine Ente zählt sie mit dem Schnabel ab
---

## Text verbinden und wiederholen

Die Rechenzeichen aus dem letzten Kapitel funktionieren auch mit Text, nur anders: `+` klebt zwei Texte aneinander, `*` wiederholt einen Text. Leerzeichen setzt `+` keine, die musst du selbst mitliefern.

```beispiel
id: verbinden
code: |
  vorname = "Pia"
  gruss = "Hallo " + vorname + "!"
  print(gruss)
  print("Fisch" * 3)
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Hallo Pia!
        FischFischFisch
      richtig: true
      erklaerung: Richtig. Das Leerzeichen steckt im Text "Hallo ", und * wiederholt ohne Abstand.
    - text: |-
        HalloPia!
        FischFischFisch
      erklaerung: Das Leerzeichen steht im Text "Hallo " mit drin, es geht also nicht verloren.
    - text: |-
        Hallo Pia!
        Fisch Fisch Fisch
      erklaerung: Anders als print mit Kommas setzt * keine Leerzeichen dazwischen.
```

```falle
titel: Text plus Zahl
text: "`\"Alter: \" + 5` geht schief, Python verbindet keinen Text mit einer Zahl (`TypeError`). Dafür gibt es gleich die f-Strings, oder du gibst beides mit Komma an print."
```

```frage
frageart: auswahl
id: text-mal
text: Was gibt `print("ha" * 3)` aus?
als_code: true
optionen:
  - text: hahaha
    richtig: true
    erklaerung: Richtig, dreimal ha ohne Abstand.
  - text: ha ha ha
    erklaerung: "* setzt keine Leerzeichen dazwischen."
  - text: ha3
    erklaerung: Mit + würde man zwei Texte verbinden; * wiederholt.
```

## Werte einsetzen mit f-Strings

Ein `f` vor dem Anführungszeichen macht einen f-String: Darin setzt Python alles, was in geschweiften Klammern steht, als Wert ein. Das klappt auch mit Zahlen und sogar mit kleinen Rechnungen.

```beispiel
id: fstring
code: |
  name = "Pit"
  fische = 4
  print(f"{name} hat {fische} Fische.")
  print(f"Doppelt so viele: {fische * 2}")
vorhersage:
  art: eintippen
  erklaerung: "In den geschweiften Klammern steht ein Name oder eine Rechnung; Python setzt den Wert ein: Pit hat 4 Fische. und Doppelt so viele: 8"
```

```merke
text: "`f\"...{wert}...\"` setzt Werte in Text ein, egal ob Text oder Zahl. Ohne das `f` vorn bleiben die Klammern einfach stehen."
```

```frage
frageart: luecke
id: luecke-fstring
text: Ergänze den Buchstaben, damit Python den Wert einsetzt.
code: print(___"Ich bin {alter} Jahre alt")
antworten: [["f"]]
erklaerung: Richtig, das f vor dem Anführungszeichen macht daraus einen f-String.
hinweis: Ein einzelner Buchstabe direkt vor dem Anführungszeichen.
```

## Wie lang ist ein Text?

`len` zählt die Zeichen eines Texts, Leerzeichen und Satzzeichen eingeschlossen. Das Ergebnis ist eine Zahl, mit der du weiterrechnen kannst.

```beispiel
id: laenge
code: |
  wort = "Pinguin"
  satz = "Pinguine sind toll!"
  print(len(wort))
  print(len(satz))
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        7
        19
      richtig: true
      erklaerung: Richtig. Auch die Leerzeichen und das Ausrufezeichen zählen mit.
    - text: |-
        7
        17
      erklaerung: Die beiden Leerzeichen zählen mit, auch wenn man sie nicht sieht.
    - text: |-
        6
        18
      erklaerung: len zählt ab 1, nicht ab 0. Ein Text mit sieben Buchstaben hat die Länge 7.
```

```frage
frageart: auswahl
id: leerer-text
text: Was gibt `print(len(""))` aus?
als_code: true
optionen:
  - text: '0'
    richtig: true
    erklaerung: Richtig. Ein leerer Text hat keine Zeichen.
  - text: '2'
    erklaerung: Die Anführungszeichen gehören nicht zum Text, sie zeigen nur, wo er anfängt und aufhört.
  - text: Fehler
    erklaerung: Ein leerer Text ist erlaubt und hat die Länge 0.
```

## Einzelne Zeichen holen

```alltag
text: Auf einer Perlenkette sitzt jede Perle an ihrem Platz. Zählt man die Plätze, fängt Python bei 0 an, nicht bei 1. Die erste Perle hat den Platz 0, die zweite den Platz 1.
zeichnung: perlenkette
```

In eckigen Klammern hinter einem Text steht die Nummer des Zeichens, sein Index. Negative Zahlen zählen von hinten: `[-1]` ist das letzte Zeichen.

| Zeichen | P | i | n | g | u |
|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 |
| von hinten | -5 | -4 | -3 | -2 | -1 |

```beispiel
id: index
code: |
  tier = "Pingu"
  print(tier[0])
  print(tier[3])
  print(tier[-1])
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        P
        g
        u
      richtig: true
      erklaerung: Richtig. Index 0 ist das erste Zeichen, 3 das vierte, -1 das letzte.
    - text: |-
        P
        n
        u
      erklaerung: Der Index zählt ab 0. tier[3] ist das vierte Zeichen, das g.
    - text: |-
        i
        g
        P
      erklaerung: tier[0] ist das erste Zeichen, und -1 zählt von hinten.
```

```falle
titel: Über das Ende hinaus
text: "Ein Text mit 5 Zeichen hat die Indizes 0 bis 4. `tier[5]` gibt es nicht, Python meldet `IndexError`."
```

```frage
frageart: fehlerstelle
id: fehler-index
text: Das Programm soll den letzten Buchstaben von "Eis" ausgeben, meldet aber IndexError. Welche Zeile?
code: |
  wort = "Eis"
  print(wort[0])
  print(wort[3])
zeile: 3
erklaerung: Genau. "Eis" hat die Indizes 0, 1 und 2; den letzten erreichst du mit wort[2] oder wort[-1].
hinweise:
  2: wort[0] ist das E, das klappt.
hinweis: Wie viele Zeichen hat "Eis", und ab welcher Zahl zählt der Index?
```

## Ausschnitte nehmen

Mit einem Doppelpunkt in den eckigen Klammern schneidest du ein Stück heraus: `text[start:ende]`. Das Zeichen an `start` ist dabei, das an `ende` nicht mehr. Fehlt eine Zahl, geht es vom Anfang oder bis zum Ende.

```beispiel
id: ausschnitt
code: |
  wort = "Eisbaer"
  print(wort[0:3])
  print(wort[3:])
  print(wort[:2])
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Eis
        baer
        Ei
      richtig: true
      erklaerung: Richtig. 0 bis vor 3 ist Eis, ab 3 bis zum Ende ist baer, bis vor 2 ist Ei.
    - text: |-
        Eisb
        baer
        Eis
      erklaerung: Das Zeichen am Ende-Index gehört nicht mehr dazu. wort[0:3] sind die Zeichen 0, 1 und 2.
    - text: |-
        Eis
        sbaer
        Ei
      erklaerung: wort[3:] beginnt beim Index 3, das ist das b.
```

```frage
frageart: luecke
id: luecke-ausschnitt
text: Ergänze die Zahl so, dass "Pin" ausgegeben wird.
code: print("Pinguin"[0:___])
antworten: [["3"]]
erklaerung: Richtig, die Zeichen 0, 1 und 2; das Zeichen an Index 3 ist nicht mehr dabei.
hinweis: Das Ende gehört nicht mehr zum Ausschnitt.
```

## Text umbauen mit Methoden

Text bringt eigene Werkzeuge mit, die Methoden. Man ruft sie mit einem Punkt auf: `text.upper()` macht Großbuchstaben, `text.lower()` kleine, `text.replace("a", "b")` tauscht aus, `text.strip()` schneidet Leerzeichen am Rand ab. Der alte Text bleibt dabei unverändert, du bekommst einen neuen zurück.

```beispiel
id: methoden
code: |
  ruf = "  achtung, eisbaer!  "
  sauber = ruf.strip()
  print(sauber.upper())
  print(sauber.replace("eisbaer", "pinguin"))
  print(ruf)
vorhersage:
  art: eintippen
  erklaerung: "strip entfernt die Leerzeichen am Rand, upper macht ACHTUNG, EISBAER!, replace tauscht das Wort; ruf selbst bleibt unverändert, mitsamt seinen Leerzeichen."
```

```falle
titel: Ergebnis nicht aufgehoben
text: "`name.upper()` allein ändert name nicht. Wer das Ergebnis behalten will, schreibt `name = name.upper()`."
```

```frage
frageart: ordnen
id: ordnen-umbauen
text: Erst den Text anlegen, dann die Leerzeichen am Rand entfernen, dann in Großbuchstaben ausgeben. Bring die Zeilen in Reihenfolge.
zeilen:
  - eis = "  vanille  "
  - eis = eis.strip()
  - print(eis.upper())
erklaerung: Richtig. Und weil strip einen neuen Text liefert, wird er wieder unter eis abgelegt.
hinweis: Ein Name braucht seinen Wert, bevor eine Methode darauf arbeitet.
```

```augenzwinkern
text: Ab jetzt kannst du einen Pinguin in Großbuchstaben anschreien. Er wird es trotzdem nicht lesen.
```

---
id: sql-join
sprache: sql
titel: Tabellen verbinden
kurz: Was zusammengehört, steht in verschiedenen Tabellen; mit JOIN die passenden Zeilen verbinden und mit LEFT JOIN auch die ohne Partner behalten.
fuehrt_ein: [join, left_join]
lernziele:
  - erklären, warum Daten auf mehrere Tabellen verteilt sind
  - zwei Tabellen mit JOIN und einer Bedingung hinter ON verbinden
  - Tabellen Kürzel geben und gleichnamige Spalten mit dem Kürzel davor unterscheiden
  - mit LEFT JOIN auch Zeilen ohne passenden Partner behalten
  - verbinden, filtern und gruppieren in einer Abfrage
karte: Ich knote zusammen, was zusammengehört
datensatz: pinguinzoo
bilder:
  - schluessel: karte_sql_join
    art: sammelkarte
    sprache: sql
    motiv: Ein Pinguin verbindet mit einem roten Faden eine Pinguin-Karteikarte mit einer Kolonie-Karteikarte
---

## Zwei Kästen, ein Faden

```alltag
text: Auf Pits Karteikarte steht nur "Kolonie Nord". Wo die Nordkolonie liegt, steht auf der Karte der Kolonie im anderen Kasten. Wer beides wissen will, legt die beiden Karten nebeneinander und knotet sie mit einem Faden zusammen.
zeichnung: faden
```

Daten stehen in mehreren Tabellen, damit nichts doppelt gepflegt werden muss: dass die Nordkolonie am Packeis liegt, steht genau einmal in der Tabelle kolonien, nicht bei jedem der vier Pinguine. Zum Abfragen verbindet man die Tabellen wieder.

`JOIN` hängt an jede Zeile der ersten Tabelle die passenden Zeilen der zweiten. Was passt, sagt die Bedingung hinter `ON`: hier soll die Kolonie des Pinguins gleich dem Namen der Kolonie sein. Weil beide Tabellen eine Spalte name haben, schreibt man den Tabellennamen davor: `pinguine.name`, `kolonien.name`.

```beispiel
id: lage
code: |
  SELECT pinguine.name, kolonien.lage
  FROM pinguine
  JOIN kolonien ON pinguine.kolonie = kolonien.name;
vorhersage:
  art: auswahl
  frage: Wie viele Zeilen hat das Ergebnis?
  vergleich: zeilen
  optionen:
    - text: 8 Zeilen
      richtig: true
      erklaerung: Richtig. Jeder der acht Pinguine findet genau eine passende Kolonie.
    - text: 4 Zeilen
      erklaerung: Vier Kolonien gibt es, aber je Pinguin entsteht eine Zeile.
    - text: 32 Zeilen
      erklaerung: So viele wären es, wenn jeder Pinguin mit jeder Kolonie verbunden würde. ON lässt nur die passenden Paare zu.
```

```frage
frageart: auswahl
id: wozu-on
text: Was legt die Bedingung hinter ON fest?
optionen:
  - text: Welche Zeilen der beiden Tabellen zusammengehören
    richtig: true
    erklaerung: Richtig, nur Paare, für die sie stimmt, werden verbunden.
  - text: Welche Spalten ins Ergebnis kommen
    erklaerung: Das bestimmt SELECT.
  - text: In welcher Reihenfolge die Zeilen stehen
    erklaerung: Dafür gibt es ORDER BY.
```

## Kürzel und gleiche Namen

Tabellennamen immer auszuschreiben wird lang. Darum bekommt jede Tabelle hinter FROM und JOIN ein Kürzel: `FROM pinguine p` heißt, dass p für pinguine steht. Spiel das Beispiel ab: nach dem JOIN stehen die Spalten beider Tabellen nebeneinander, die gleichnamigen mit Kürzel davor. Und gleichnamige Spalten im Ergebnis bekommen mit AS eigene Namen, sonst hießen beide name.

```beispiel
id: pfleger
code: |
  SELECT p.name AS pinguin, pf.name AS pfleger
  FROM pinguine p
  JOIN pfleger pf ON pf.kolonie = p.kolonie
  WHERE p.kolonie = 'Süd';
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Pia | Hannes
        Pepe | Hannes
      richtig: true
      erklaerung: Richtig. Im Süden pflegt Hannes, und beide Südpinguine bekommen ihn als Partner.
    - text: Hannes | Hannes
      erklaerung: p.name ist der Name des Pinguins, pf.name der des Pflegers.
    - text: |-
        Pia | Hannes
        Pepe | Hannes
        Pia | Jonas
        Pepe | Jonas
      erklaerung: Jonas hat keine Kolonie eingetragen. NULL ist nie gleich Süd, also passt er zu niemandem.
```

```falle
titel: Mehrdeutige Spalte
text: "`SELECT name FROM pinguine JOIN kolonien ON kolonie = name` meldet `ambiguous column name: name`. Die Datenbank weiß nicht, welches name gemeint ist. Bei gleichnamigen Spalten gehört immer das Kürzel davor."
```

```frage
frageart: luecke
id: luecke-on
text: Ergänze, damit zu jeder Fütterung der Name des Pinguins kommt.
code: |
  SELECT f.tag, p.name, f.menge
  FROM fuetterungen f
  JOIN pinguine p ___ p.id = f.pinguin_id;
antworten: [["ON", "on"]]
erklaerung: Richtig, hinter ON steht, welche Zeilen zusammengehören.
hinweis: Das kleine Wort vor der Bedingung eines JOIN.
```

## Verbinden, sieben, gruppieren

Nach dem JOIN ist die verbundene Tabelle eine Tabelle wie jede andere: WHERE, GROUP BY, HAVING und ORDER BY arbeiten wie gewohnt. So lässt sich etwa für jeden Pinguin mit Namen ausrechnen, wie viele Fische er bekommen hat, obwohl in der Tabelle fuetterungen nur seine Nummer steht.

```beispiel
id: fische-je-name
code: |
  SELECT p.name, SUM(f.menge) AS fische
  FROM pinguine p
  JOIN fuetterungen f ON f.pinguin_id = p.id
  GROUP BY p.name
  ORDER BY fische DESC
  LIMIT 3;
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Paul | 15
        Pit | 14
        Pia | 9
      richtig: true
      erklaerung: Richtig. Paul bekam 8 und 7 Fische, Pit 6, 5 und 3, Pia 4 und 5.
    - text: |-
        3 | 15
        1 | 14
        2 | 9
      erklaerung: Das wären die Nummern aus fuetterungen. Durch den JOIN kennt die Abfrage die Namen.
    - text: |-
        Paul | 8
        Pit | 6
        Pia | 5
      erklaerung: Das wäre MAX, die größte einzelne Portion. SUM zählt alle Portionen eines Pinguins zusammen.
```

## Auch ohne Partner: LEFT JOIN

Die Westkolonie hat keine Pinguine. Bei einem JOIN fällt sie deshalb ganz heraus, denn sie findet keinen Partner. `LEFT JOIN` behält jede Zeile der linken Tabelle, also der vor dem JOIN; wo kein Partner da ist, stehen in den Spalten der rechten Tabelle NULL.

```beispiel
id: alle-kolonien
code: |
  SELECT k.name AS kolonie, COUNT(p.id) AS pinguine
  FROM kolonien k
  LEFT JOIN pinguine p ON p.kolonie = k.name
  GROUP BY k.name
  ORDER BY k.name;
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Nord | 4
        Ost | 2
        Süd | 2
        West | 0
      richtig: true
      erklaerung: Richtig. LEFT JOIN behält West, und COUNT(p.id) zählt dort keinen Pinguin, denn p.id ist NULL.
    - text: |-
        Nord | 4
        Ost | 2
        Süd | 2
      erklaerung: So wäre es mit JOIN. LEFT JOIN behält auch die Westkolonie ohne Partner.
    - text: |-
        Nord | 4
        Ost | 2
        Süd | 2
        West | 1
      erklaerung: Das käme bei COUNT(*) heraus, denn West hat eine Zeile, nur ohne Pinguin. COUNT(p.id) lässt NULL aus.
```

```merke
text: "JOIN tabelle ON bedingung verbindet die passenden Zeilen zweier Tabellen. Kürzel wie p und k sparen Schreibarbeit, bei gleichnamigen Spalten sind sie Pflicht. LEFT JOIN behält jede Zeile der linken Tabelle, ohne Partner mit NULL."
```

```frage
frageart: fehlerstelle
id: fehler-mehrdeutig
text: Diese Abfrage meldet "ambiguous column name". In welcher Zeile?
code: |
  SELECT p.name,
         lage,
         name
  FROM pinguine p
  JOIN kolonien k ON k.name = p.kolonie;
zeile: 3
erklaerung: Genau. name gibt es in beiden Tabellen; gemeint ist k.name oder p.name. lage gibt es nur in kolonien, da reicht der Name.
hinweis: Welche Spalte steht ohne Kürzel da und kommt in beiden Tabellen vor?
```

```frage
frageart: ordnen
id: ordnen-join
text: Bring die Zeilen in Reihenfolge, damit jeder Pfleger mit der Lage seiner Kolonie kommt, auch Jonas.
zeilen:
  - SELECT pf.name, k.lage
  - FROM pfleger pf
  - LEFT JOIN kolonien k ON k.name = pf.kolonie;
erklaerung: Richtig. Jonas bekommt bei der Lage NULL, bleibt aber dabei.
hinweis: Die Tabelle, von der alle Zeilen bleiben sollen, steht vor LEFT JOIN.
```

```augenzwinkern
text: Die Westkolonie freut sich über jeden LEFT JOIN. Es ist die einzige Gelegenheit, bei der sie in einer Liste auftaucht.
```

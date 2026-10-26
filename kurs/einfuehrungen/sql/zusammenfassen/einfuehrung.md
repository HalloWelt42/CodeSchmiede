---
id: sql-zusammenfassen
sprache: sql
titel: Zusammenfassen
kurz: Viele Zeilen, eine Antwort; zählen, summieren und Durchschnitt, Minimum und Maximum berechnen.
fuehrt_ein: [aggregat]
lernziele:
  - mit COUNT(*) Zeilen zählen und wissen, dass COUNT(spalte) NULL auslässt
  - mit SUM, AVG, MIN und MAX über alle Zeilen rechnen
  - zusammenfassen und vorher mit WHERE filtern
  - wissen, dass das Ergebnis nur noch eine Zeile hat
karte: Ich mache aus vielen Zeilen eine
datensatz: pinguinzoo
bilder:
  - schluessel: karte_sql_zusammenfassen
    art: sammelkarte
    sprache: sql
    motiv: Ein Pinguin vor einer Tafel mit Strichliste, daneben ein Eimer voller Fische
---

## Zählen statt aufzählen

```alltag
text: Der Futtermeister will nicht jede Fütterung einzeln sehen. Er will wissen, wie oft gefüttert wurde und wie viele Fische es insgesamt waren. Dafür macht er Striche an der Tafel und zählt sie am Ende zusammen.
zeichnung: strichliste
```

Funktionen wie `COUNT`, `SUM` oder `AVG` fassen alle Zeilen zu einer einzigen zusammen. `COUNT(*)` zählt die Zeilen. Das Ergebnis ist eine Tabelle mit genau einer Zeile; mit AS bekommt die Spalte einen vernünftigen Namen.

```beispiel
id: zaehlen
code: |
  SELECT COUNT(*) AS anzahl
  FROM pinguine;
vorhersage:
  art: auswahl
  optionen:
    - text: "8"
      richtig: true
      erklaerung: Richtig. Acht Zeilen, also acht Pinguine, in einer einzigen Ergebniszeile.
    - text: |-
        1
        2
        3
        4
        5
        6
        7
        8
      erklaerung: COUNT nummeriert nicht durch, es liefert eine einzige Zahl.
    - text: "6"
      erklaerung: Sechs sind es bei den Spalten. COUNT(*) zählt Zeilen.
```

Steht in den Klammern eine Spalte statt `*`, zählt COUNT nur die Zeilen, in denen dort etwas steht; NULL wird ausgelassen. Mit `COUNT(DISTINCT spalte)` zählt es jeden Wert nur einmal.

```beispiel
id: bekannt
code: |
  SELECT COUNT(*) AS alle, COUNT(lieblingsfisch) AS bekannt
  FROM pinguine;
vorhersage:
  art: auswahl
  optionen:
    - text: 8 | 6
      richtig: true
      erklaerung: Richtig. Bei zwei Pinguinen ist der Lieblingsfisch NULL, die zählt COUNT(lieblingsfisch) nicht.
    - text: 8 | 8
      erklaerung: COUNT mit einer Spalte lässt NULL aus.
    - text: 8 | 3
      erklaerung: Das wäre COUNT(DISTINCT lieblingsfisch), jeder Fisch einmal.
```

```frage
frageart: auswahl
id: wie-viele-zeilen
text: Wie viele Zeilen hat das Ergebnis von `SELECT COUNT(*) FROM fuetterungen`?
optionen:
  - text: Eine
    richtig: true
    erklaerung: Richtig, in ihr steht die Zahl 12.
  - text: Zwölf
    erklaerung: Zwölf ist der Wert in der einen Ergebniszeile.
  - text: Keine
    erklaerung: Auch eine Zählung braucht eine Zeile, in der das Ergebnis steht.
```

## Rechnen über alle Zeilen

`SUM(spalte)` zählt die Werte zusammen, `AVG(spalte)` bildet den Durchschnitt, `MIN` und `MAX` finden den kleinsten und den größten Wert. Mehrere dürfen nebeneinander stehen. Auch hier wird NULL ausgelassen.

```beispiel
id: gewichte
code: |
  SELECT AVG(gewicht_kg) AS schnitt,
         MIN(gewicht_kg) AS leichtester,
         MAX(gewicht_kg) AS schwerster
  FROM pinguine;
vorhersage:
  art: auswahl
  optionen:
    - text: 4.125 | 2.9 | 5.1
      richtig: true
      erklaerung: Richtig. Im Schnitt 4,125 Kilo, Pünktchen ist der leichteste, Paul der schwerste.
    - text: 33.0 | 2.9 | 5.1
      erklaerung: 33 Kilo wiegen alle zusammen, das wäre SUM. AVG teilt noch durch acht.
    - text: 4.125 | Pünktchen | Paul
      erklaerung: MIN und MAX liefern den kleinsten und größten Wert der Spalte, nicht den Namen.
```

```frage
frageart: luecke
id: luecke-summe
text: Ergänze, damit herauskommt, wie viele Fische insgesamt verfüttert wurden.
code: |
  SELECT ___(menge) AS fische
  FROM fuetterungen;
antworten: [["SUM", "sum"]]
erklaerung: Richtig, SUM zählt alle Mengen zusammen.
hinweis: Gesucht ist die Summe.
```

## Erst sieben, dann zählen

Zusammengefasst wird erst nach WHERE. Wer also wissen will, wie viele Fische es am 21. Oktober gab, filtert zuerst die Zeilen dieses Tages und rechnet dann. Spiel das Beispiel ab: SELECT bekommt nur noch die Zeilen, die durchs Sieb gefallen sind.

```beispiel
id: ein-tag
code: |
  SELECT COUNT(*) AS fuetterungen, SUM(menge) AS fische
  FROM fuetterungen
  WHERE tag = '2026-10-21';
vorhersage:
  art: auswahl
  optionen:
    - text: 4 | 18
      richtig: true
      erklaerung: Richtig. Vier Fütterungen am 21. mit 5, 3, 6 und 4 Fischen.
    - text: 12 | 58
      erklaerung: Das wären alle Tage. WHERE siebt vorher aus.
    - text: 4 | 4
      erklaerung: SUM zählt die Mengen zusammen, nicht die Zeilen.
```

```falle
titel: Einzelne Spalten neben der Summe
text: "`SELECT name, AVG(gewicht_kg) FROM pinguine` fasst alles zu einer Zeile zusammen. Welcher Name soll da stehen? SQLite nimmt einfach irgendeinen, andere Datenbanken melden einen Fehler. Wer je Kolonie oder je Pinguin zusammenfassen will, braucht GROUP BY aus dem nächsten Kapitel."
```

```merke
text: "COUNT(*) zählt Zeilen, COUNT(spalte) nur die ohne NULL. SUM, AVG, MIN, MAX rechnen über alle Zeilen, die nach WHERE übrig sind. Heraus kommt genau eine Zeile."
```

```frage
frageart: fehlerstelle
id: fehler-klammern
text: Diese Abfrage meldet einen Fehler. In welcher Zeile?
code: |
  SELECT COUNT(*) AS anzahl,
         SUM(menge) AS fische,
         MAX menge AS groesste
  FROM fuetterungen;
zeile: 3
erklaerung: Genau. Auch MAX braucht Klammern um die Spalte, also `MAX(menge)`.
hinweis: Wo fehlen die Klammern einer Funktion?
```

```frage
frageart: ordnen
id: ordnen-bericht
text: Bring die Zeilen in Reihenfolge, damit herauskommt, wie viele Hering-Fütterungen es gab und wie groß die größte war.
zeilen:
  - SELECT COUNT(*) AS fuetterungen, MAX(menge) AS groesste
  - FROM fuetterungen
  - WHERE fisch = 'Hering';
erklaerung: Richtig. Erst sieben, dann zusammenfassen; geschrieben wird trotzdem SELECT zuerst.
hinweis: SELECT, FROM, WHERE.
```

```augenzwinkern
text: Der Futtermeister hat ausgerechnet, dass die Pinguine in drei Tagen 58 Fische gegessen haben. Die Möwen behaupten, es waren 59.
```

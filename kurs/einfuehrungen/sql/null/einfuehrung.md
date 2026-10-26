---
id: sql-null
sprache: sql
titel: Wenn nichts drinsteht
kurz: NULL heißt unbekannt; warum = NULL nie stimmt, wie IS NULL hilft und wie COALESCE Lücken füllt.
fuehrt_ein: [null_werte]
lernziele:
  - erklären, dass NULL für einen unbekannten Wert steht und nicht für 0 oder einen leeren Text
  - mit IS NULL und IS NOT NULL nach fehlenden Werten suchen
  - verstehen, warum Vergleiche mit NULL Zeilen verschwinden lassen
  - mit COALESCE einen Ersatzwert für NULL einsetzen
karte: Ich weiß, dass ich nichts weiß
datensatz: pinguinzoo
bilder:
  - schluessel: karte_sql_null
    art: sammelkarte
    sprache: sql
    motiv: Ein Pinguin kratzt sich am Kopf vor einer Karteikarte, auf der ein Feld leer ist und ein Fragezeichen schwebt
---

## Unbekannt ist nicht leer

```alltag
text: Auf Pinas Karteikarte ist das Feld Lieblingsfisch leer. Das heißt nicht, dass sie keinen Fisch mag, sondern dass es noch niemand herausgefunden hat. Für so ein "weiß noch keiner" hat SQL einen eigenen Wert, NULL.
zeichnung: fragezeichen
```

`NULL` ist kein Text und keine Zahl. Es ist nicht 0 und nicht der leere Text `''`, sondern heißt: hier fehlt der Wert. In der Tabelle pinguine fehlt bei Pina und Pünktchen der Lieblingsfisch, in der Tabelle pfleger bei Jonas die Kolonie.

Die Tücke: ein Vergleich mit etwas Unbekanntem ergibt wieder unbekannt. Ist Pinas Lieblingsfisch gleich NULL? Das weiß niemand. WHERE lässt aber nur Zeilen durch, bei denen die Bedingung sicher stimmt.

```beispiel
id: gleich-null
code: |
  SELECT name
  FROM pinguine
  WHERE lieblingsfisch = NULL;
vorhersage:
  art: auswahl
  frage: Wie viele Zeilen hat das Ergebnis?
  vergleich: zeilen
  optionen:
    - text: 0 Zeilen
      richtig: true
      erklaerung: Richtig, und das überrascht fast jeden. Etwas mit unbekannt zu vergleichen ergibt unbekannt, nie wahr.
    - text: 2 Zeilen
      erklaerung: So wäre es gemeint, aber = NULL stimmt nie. Dafür gibt es gleich IS NULL.
    - text: Fehler
      erklaerung: Die Abfrage läuft ohne Fehler, sie findet nur nichts.
```

```frage
frageart: auswahl
id: was-ist-null
text: Was bedeutet NULL in der Spalte lieblingsfisch?
optionen:
  - text: Der Lieblingsfisch ist nicht bekannt
    richtig: true
    erklaerung: Richtig, NULL heißt, dass der Wert fehlt.
  - text: Der Pinguin mag keinen Fisch
    erklaerung: Das wäre eine Aussage. NULL sagt nur, dass niemand es weiß.
  - text: Der Lieblingsfisch heißt NULL
    erklaerung: Dann stünde dort der Text 'NULL' in Hochkommas. NULL ohne Hochkommas ist kein Text.
```

## Fragen nach dem Nichts: IS NULL

Wer fehlende Werte finden will, fragt mit `IS NULL`. Das Gegenteil heißt `IS NOT NULL`. Beide sind keine Vergleiche mit einem Wert, sondern fragen: steht hier etwas oder nicht?

```beispiel
id: ist-null
code: |
  SELECT name
  FROM pinguine
  WHERE lieblingsfisch IS NULL;
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Pina
        Pünktchen
      richtig: true
      erklaerung: Richtig. Bei den beiden fehlt der Lieblingsfisch.
    - text: "(keine Zeile)"
      erklaerung: Das war = NULL. IS NULL findet die fehlenden Werte.
    - text: |-
        Pit
        Pia
        Paul
        Pepe
        Polly
        Pablo
      erklaerung: Das wäre IS NOT NULL, die Pinguine mit bekanntem Lieblingsfisch.
```

```frage
frageart: luecke
id: luecke-not-null
text: Ergänze, damit alle Pfleger kommen, die fest zu einer Kolonie gehören.
code: |
  SELECT name
  FROM pfleger
  WHERE kolonie ___;
antworten: [["IS NOT NULL", "is not null"]]
erklaerung: Richtig. Greta, Hannes und Ida; Jonas springt überall ein.
hinweis: Gesucht sind die Pfleger, bei denen die Kolonie nicht fehlt.
```

## Wo die Zeilen hin sind

Erinnerst du dich an die Übung "Bloß kein Hering"? Dort fielen Pina und Pünktchen heraus, obwohl Hering nicht ihr Lieblingsfisch ist. Jetzt ist klar, warum: ob ein unbekannter Fisch ungleich Hering ist, weiß niemand. Wer die Unbekannten dabeihaben will, sagt es ausdrücklich mit `OR ... IS NULL`.

```beispiel
id: ungleich
code: |
  SELECT name, lieblingsfisch
  FROM pinguine
  WHERE lieblingsfisch <> 'Hering'
     OR lieblingsfisch IS NULL;
vorhersage:
  art: auswahl
  frage: Wie viele Zeilen hat das Ergebnis?
  vergleich: zeilen
  optionen:
    - text: 5 Zeilen
      richtig: true
      erklaerung: Richtig. Drei mit anderem Lieblingsfisch und die zwei Unbekannten.
    - text: 3 Zeilen
      erklaerung: So viele wären es ohne die zweite Zeile. Mit OR IS NULL kommen Pina und Pünktchen dazu.
    - text: 8 Zeilen
      erklaerung: Pit, Paul und Pablo mögen Hering und bleiben draußen.
```

```falle
titel: NULL frisst Rechnungen
text: "Wer mit NULL rechnet oder Text verbindet, bekommt wieder NULL: `NULL + 1` ist NULL, und `'mag ' || lieblingsfisch` ergibt bei Pina NULL statt eines halben Satzes."
```

## Lücken füllen mit COALESCE

`COALESCE(wert, ersatz)` liefert den Wert, wenn er da ist, und sonst den Ersatz. Damit bekommt die Besuchertafel statt einer Lücke ein freundliches "unbekannt". Man kann auch mehrere Werte angeben, dann gilt der erste, der nicht NULL ist.

```beispiel
id: ersatz
code: |
  SELECT name, COALESCE(kolonie, 'springt ein') AS einsatz
  FROM pfleger;
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Greta | Nord
        Hannes | Süd
        Ida | Ost
        Jonas | springt ein
      richtig: true
      erklaerung: Richtig. Wo die Kolonie bekannt ist, steht sie da; bei Jonas der Ersatz.
    - text: |-
        Greta | springt ein
        Hannes | springt ein
        Ida | springt ein
        Jonas | springt ein
      erklaerung: COALESCE nimmt den Ersatz nur, wenn der Wert fehlt.
    - text: |-
        Greta | Nord
        Hannes | Süd
        Ida | Ost
        Jonas | NULL
      erklaerung: Genau diese Lücke füllt COALESCE mit dem Ersatz.
```

```merke
text: "NULL heißt unbekannt. Vergleiche mit NULL stimmen nie, darum fragt man mit IS NULL und IS NOT NULL. Rechnen mit NULL ergibt NULL. COALESCE(wert, ersatz) füllt die Lücke."
```

```frage
frageart: fehlerstelle
id: fehler-null
text: Die Abfrage soll alle Pinguine mit unbekanntem Lieblingsfisch finden, liefert aber nichts. In welcher Zeile liegt der Fehler?
code: |
  SELECT name,
         kolonie
  FROM pinguine
  WHERE lieblingsfisch = NULL;
zeile: 4
erklaerung: Genau. = NULL stimmt nie; richtig ist `WHERE lieblingsfisch IS NULL`.
hinweis: Wie fragt man nach einem fehlenden Wert?
```

```frage
frageart: ordnen
id: ordnen-coalesce
text: Bring die Zeilen in Reihenfolge, damit jeder Pinguin aus der Ostkolonie mit Lieblingsfisch oder "unbekannt" erscheint.
zeilen:
  - SELECT name, COALESCE(lieblingsfisch, 'unbekannt') AS fisch
  - FROM pinguine
  - WHERE kolonie = 'Ost';
erklaerung: Richtig. Pablo mag Hering, bei Pünktchen steht unbekannt.
hinweis: SELECT, FROM, WHERE.
```

```augenzwinkern
text: Pina hat übrigens einen Lieblingsfisch. Sie verrät ihn nur nicht, weil ihr das Rätselraten der Pfleger so gefällt.
```

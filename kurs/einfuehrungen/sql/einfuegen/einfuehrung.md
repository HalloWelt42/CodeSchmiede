---
id: sql-einfuegen
sprache: sql
titel: Zeilen einfügen
kurz: Bisher wurde nur gefragt, jetzt wird geschrieben; mit INSERT neue Zeilen anlegen, einzeln, mehrere auf einmal oder aus einer Abfrage.
fuehrt_ein: [insert]
lernziele:
  - mit INSERT INTO ... VALUES eine neue Zeile anlegen
  - Spalten weglassen und wissen, was dann drinsteht
  - verstehen, warum NOT NULL das Weglassen verbietet
  - mehrere Zeilen mit einer Anweisung einfügen
  - mit INSERT ... SELECT Zeilen aus einer Abfrage einfügen
karte: Ich lege eine neue Karte an
datensatz: pinguinzoo
bilder:
  - schluessel: karte_sql_einfuegen
    art: sammelkarte
    sprache: sql
    motiv: Ein Pinguin steckt eine frisch beschriebene Karteikarte in einen Karteikasten
---

## Eine neue Karte

```alltag
text: Ein Neuzugang ist da! Der Pfleger schreibt eine neue Karteikarte, Feld für Feld, und steckt sie in den Kasten. Danach sieht jeder, der im Kasten blättert, den neuen Pinguin. INSERT ist das Einstecken.
zeichnung: neue-karte
```

Bis hierher hat jede Abfrage nur gelesen. Ab jetzt ändern die Anweisungen die Tabellen. Keine Sorge: jedes Beispiel und jede Übung läuft auf einer frischen Kopie des Pinguinzoos, beim nächsten Ausführen ist alles wieder wie vorher.

`INSERT INTO tabelle (spalten) VALUES (werte)` legt eine neue Zeile an. Die Werte stehen in derselben Reihenfolge wie die Spalten davor, Texte wie immer in Hochkommas. Ein Skript darf mehrere Anweisungen haben, jede endet mit einem Semikolon. Hier zeigt eine Abfrage hinterher, was passiert ist.

```beispiel
id: pelle
code: |
  INSERT INTO pinguine (id, name, kolonie, gewicht_kg, geburtsjahr, lieblingsfisch)
  VALUES (9, 'Pelle', 'West', 3.1, 2025, 'Sardine');

  SELECT COUNT(*) AS anzahl FROM pinguine;
vorhersage:
  art: auswahl
  optionen:
    - text: "9"
      richtig: true
      erklaerung: Richtig. Acht waren es, Pelle ist der neunte. Spiel das Skript ab, im Schritt INSERT ist seine Zeile markiert.
    - text: "8"
      erklaerung: Die Abfrage läuft nach dem INSERT, Pelle ist da schon in der Tabelle.
    - text: "1"
      erklaerung: COUNT(*) zählt alle Zeilen der Tabelle, nicht nur die neue.
```

```frage
frageart: auswahl
id: reihenfolge-werte
text: "In `INSERT INTO kolonien (name, lage, wassertemperatur) VALUES (...)`: welche Werte passen?"
als_code: true
optionen:
  - text: "('Mitte', 'Lagune', 6.5)"
    richtig: true
    erklaerung: Richtig, in derselben Reihenfolge wie die Spalten.
  - text: "(6.5, 'Mitte', 'Lagune')"
    erklaerung: Die Werte müssen der Reihenfolge der Spalten folgen; zuerst kommt name.
  - text: "(Mitte, Lagune, 6.5)"
    erklaerung: Texte brauchen Hochkommas, sonst sucht die Datenbank Spalten dieses Namens.
```

## Spalten weglassen

Man muss nicht jede Spalte nennen. Was fehlt, bekommt NULL, oder einen Vorgabewert, wenn die Tabelle einen hat. Eine Ausnahme ist die Nummer: eine Spalte `id INTEGER PRIMARY KEY` füllt die Datenbank selbst mit der nächsten freien Zahl.

```beispiel
id: karla
code: |
  INSERT INTO pfleger (name) VALUES ('Karla');

  SELECT * FROM pfleger WHERE name = 'Karla';
vorhersage:
  art: auswahl
  optionen:
    - text: 5 | Karla | NULL
      richtig: true
      erklaerung: Richtig. Die id vergibt die Datenbank, die Kolonie ist nicht angegeben, also NULL.
    - text: NULL | Karla | NULL
      erklaerung: Eine Spalte INTEGER PRIMARY KEY füllt die Datenbank selbst, mit der nächsten freien Nummer.
    - text: Fehler
      erklaerung: Die Kolonie darf in der Tabelle pfleger fehlen; Karla springt dann überall ein, wie Jonas.
```

```falle
titel: NOT NULL lässt nichts weg
text: "In der Tabelle pinguine steht bei kolonie `NOT NULL`: dort muss etwas stehen. `INSERT INTO pinguine (name) VALUES ('Pelle')` scheitert deshalb mit `NOT NULL constraint failed: pinguine.kolonie`, und die Zeile kommt gar nicht erst in die Tabelle."
```

```frage
frageart: fehlerstelle
id: fehler-not-null
text: Dieses Skript bricht ab. In welcher Zeile?
code: |
  INSERT INTO pfleger (name, kolonie)
  VALUES ('Karla', 'West');
  INSERT INTO pinguine (name, kolonie)
  VALUES ('Pelle', 'West');
zeile: 3
erklaerung: Genau. Gewicht und Geburtsjahr sind bei pinguine Pflicht (NOT NULL), die Anweisung ab Zeile 3 lässt sie weg. Die erste Anweisung klappt.
hinweis: Welche Tabelle verlangt mehr Angaben, als dastehen?
```

## Mehrere Zeilen auf einmal

Hinter VALUES dürfen mehrere Klammern stehen, mit Komma getrennt. Jede wird eine Zeile, alle in einer Anweisung.

```beispiel
id: zwei-fuetterungen
code: |
  INSERT INTO fuetterungen (pinguin_id, tag, fisch, menge)
  VALUES (4, '2026-10-23', 'Sardine', 3),
         (8, '2026-10-23', 'Sardine', 2);

  SELECT tag, SUM(menge) AS fische
  FROM fuetterungen
  GROUP BY tag
  ORDER BY tag;
vorhersage:
  art: auswahl
  frage: Wie viele Zeilen hat das Ergebnis der Abfrage?
  vergleich: zeilen
  optionen:
    - text: 4 Zeilen
      richtig: true
      erklaerung: Richtig. Zu den drei Tagen kommt der 23. Oktober mit 5 Fischen.
    - text: 3 Zeilen
      erklaerung: Die neuen Fütterungen haben einen neuen Tag, der bildet eine eigene Gruppe.
    - text: 14 Zeilen
      erklaerung: 14 Fütterungen sind es jetzt, aber GROUP BY macht daraus eine Zeile je Tag.
```

```frage
frageart: luecke
id: luecke-values
text: Ergänze, damit zwei Kolonien auf einmal dazukommen.
code: |
  INSERT INTO kolonien (name, lage, wassertemperatur)
  ___ ('Mitte', 'Lagune', 6.5),
      ('Insel', 'Vulkanstrand', 12.0);
antworten: [["VALUES", "values"]]
erklaerung: Richtig, hinter VALUES stehen die Zeilen, jede in Klammern.
hinweis: Das Wort vor den Werten.
```

## Einfügen aus einer Abfrage

Statt VALUES darf auch eine Abfrage stehen. Jede Zeile ihres Ergebnisses wird eingefügt. So bekommt jeder Pinguin mit bekanntem Lieblingsfisch am 23. Oktober zwei Stück davon, mit einer einzigen Anweisung.

```beispiel
id: fruehstueck
code: |
  INSERT INTO fuetterungen (pinguin_id, tag, fisch, menge)
  SELECT id, '2026-10-23', lieblingsfisch, 2
  FROM pinguine
  WHERE lieblingsfisch IS NOT NULL;

  SELECT COUNT(*) AS neu FROM fuetterungen WHERE tag = '2026-10-23';
vorhersage:
  art: eintippen
  frage: Wie viele Fütterungen gibt es am 23. Oktober? Tipp die Zahl ein.
  erklaerung: Sechs Pinguine haben einen bekannten Lieblingsfisch, jeder bekommt eine Fütterung.
```

```merke
text: "INSERT INTO tabelle (spalten) VALUES (werte) legt Zeilen an, mehrere Klammern hinter VALUES legen mehrere an, eine Abfrage statt VALUES fügt ihr Ergebnis ein. Weggelassene Spalten werden NULL, eine id INTEGER PRIMARY KEY zählt selbst weiter, NOT NULL verbietet das Weglassen."
```

```frage
frageart: ordnen
id: ordnen-insert
text: Bring die Zeilen in Reihenfolge, damit die neue Kolonie Mitte entsteht.
zeilen:
  - INSERT INTO kolonien
  - "  (name, lage, wassertemperatur)"
  - "VALUES ('Mitte', 'Lagune', 6.5);"
erklaerung: Richtig. Erst die Tabelle, dann die Spalten, dann die Werte.
hinweis: VALUES kommt zum Schluss.
```

```augenzwinkern
text: Pelle wurde in diesem Kapitel ungefähr zweihundertmal eingefügt. Zum Glück auf frischen Kopien, sonst bräuchte die Westkolonie ein größeres Becken.
```

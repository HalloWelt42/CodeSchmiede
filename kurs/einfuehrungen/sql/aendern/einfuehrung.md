---
id: sql-aendern
sprache: sql
titel: Werte ändern
kurz: Mit UPDATE Werte in vorhandenen Zeilen ändern, auch gerechnet und mehrere auf einmal; und warum das WHERE dabei lebenswichtig ist.
fuehrt_ein: [update]
lernziele:
  - mit UPDATE ... SET ... WHERE gezielt Werte ändern
  - neue Werte aus den alten ausrechnen
  - mehrere Spalten in einer Anweisung ändern
  - wissen, dass UPDATE ohne WHERE jede Zeile ändert, und vorher mit SELECT prüfen
  - die Zeilen für ein UPDATE mit einer Unterabfrage auswählen
karte: Ich radiere und schreibe neu
datensatz: pinguinzoo
bilder:
  - schluessel: karte_sql_aendern
    art: sammelkarte
    sprache: sql
    motiv: Ein Pinguin mit Radiergummi und Bleistift korrigiert ein Feld auf einer Karteikarte
---

## Radieren und neu schreiben

```alltag
text: Pina hat sich entschieden, sie liebt Sardinen. Der Pfleger zieht ihre Karte heraus, radiert das leere Feld und schreibt Sardine hinein. Die Karte bleibt dieselbe, nur ein Feld ist neu. Das ist UPDATE.
zeichnung: radiergummi
```

`UPDATE tabelle SET spalte = wert WHERE bedingung` ändert in allen Zeilen, für die die Bedingung stimmt, den Wert der Spalte. Neue Zeilen entstehen dabei nicht, es werden nur vorhandene überschrieben. Spiel das Beispiel ab: im Schritt UPDATE steht der alte Wert durchgestrichen neben dem neuen.

```beispiel
id: pina
code: |
  UPDATE pinguine
  SET lieblingsfisch = 'Sardine'
  WHERE id = 4;

  SELECT name FROM pinguine WHERE lieblingsfisch IS NULL;
vorhersage:
  art: auswahl
  optionen:
    - text: Pünktchen
      richtig: true
      erklaerung: Richtig. Pina hat jetzt einen Lieblingsfisch, nur bei Pünktchen ist er noch unbekannt.
    - text: |-
        Pina
        Pünktchen
      erklaerung: Das UPDATE läuft vor der Abfrage; Pinas Lieblingsfisch ist dann Sardine.
    - text: "(keine Zeile)"
      erklaerung: Geändert wurde nur die Zeile mit id 4, also Pina.
```

```frage
frageart: auswahl
id: was-macht-update
text: Wie viele Zeilen hat die Tabelle pinguine nach einem UPDATE, das drei Zeilen ändert?
optionen:
  - text: Gleich viele wie vorher
    richtig: true
    erklaerung: Richtig. UPDATE ändert Werte, es legt nichts an und löscht nichts.
  - text: Drei mehr
    erklaerung: Neue Zeilen entstehen nur mit INSERT.
  - text: Drei weniger
    erklaerung: Löschen geht mit DELETE, nicht mit UPDATE.
```

## Rechnen und mehrere Spalten

Hinter SET darf eine Rechnung mit dem alten Wert stehen: `SET menge = menge + 1` legt bei jeder getroffenen Zeile einen Fisch drauf. Mehrere Spalten ändert man mit Komma: `SET fisch = 'Lachs', menge = 4`.

```beispiel
id: extra-sardine
code: |
  UPDATE fuetterungen
  SET menge = menge + 1
  WHERE fisch = 'Sardine';

  SELECT SUM(menge) AS fische FROM fuetterungen;
vorhersage:
  art: auswahl
  frage: Vorher waren es 58 Fische. Wie viele sind es danach?
  optionen:
    - text: "61"
      richtig: true
      erklaerung: Richtig. Drei Fütterungen mit Sardinen bekommen je einen Fisch mehr.
    - text: "59"
      erklaerung: Das UPDATE trifft jede Sardinen-Fütterung, und davon gibt es drei.
    - text: "70"
      erklaerung: Nur die Sardinen-Fütterungen bekommen einen mehr, nicht alle zwölf.
```

```frage
frageart: luecke
id: luecke-set
text: Ergänze, damit Fütterung 6 zu vier Lachsen wird.
code: |
  UPDATE fuetterungen
  ___ fisch = 'Lachs', menge = 4
  WHERE id = 6;
antworten: [["SET", "set"]]
erklaerung: Richtig, hinter SET stehen die neuen Werte, mit Komma getrennt.
hinweis: Das Wort vor den neuen Werten.
```

## Das WHERE ist lebenswichtig

Ohne WHERE gilt die Änderung für jede Zeile der Tabelle. Die Datenbank fragt nicht nach, ob das so gemeint war. Darum die Gewohnheit von Profis: erst ein SELECT mit demselben WHERE schreiben und nachsehen, welche Zeilen herauskommen, dann daraus das UPDATE machen.

```beispiel
id: ohne-where
code: |
  UPDATE kolonien
  SET wassertemperatur = 0;

  SELECT name FROM kolonien WHERE wassertemperatur = 0;
vorhersage:
  art: auswahl
  frage: In wie vielen Kolonien ist das Wasser danach 0 Grad warm?
  vergleich: zeilen
  optionen:
    - text: 4 Kolonien
      richtig: true
      erklaerung: Richtig, in allen. Ohne WHERE trifft UPDATE jede Zeile; jetzt friert die Ostkolonie am Sandstrand.
    - text: 0 Kolonien
      erklaerung: Ohne WHERE gibt es keine Einschränkung, also trifft es jede Zeile.
    - text: 1 Kolonie
      erklaerung: UPDATE ändert nicht nur die erste Zeile, sondern alle, die passen; ohne WHERE sind das alle.
```

```falle
titel: Vergessenes WHERE
text: "`UPDATE pinguine SET kolonie = 'West'` schickt alle acht Pinguine in die Westkolonie, nicht nur den einen, den man meinte. Erst `SELECT * FROM pinguine WHERE ...` laufen lassen, dann SELECT * durch UPDATE ... SET ersetzen."
```

## Wen es trifft, entscheidet eine Abfrage

Im WHERE eines UPDATE ist alles erlaubt, was du kennst, auch eine Unterabfrage. So bekommen alle Pinguine mit unbekanntem Lieblingsfisch, die schon einmal Sardinen gegessen haben, Sardine als Lieblingsfisch.

```beispiel
id: sardinenfreunde
code: |
  UPDATE pinguine
  SET lieblingsfisch = 'Sardine'
  WHERE lieblingsfisch IS NULL
    AND id IN (SELECT pinguin_id FROM fuetterungen WHERE fisch = 'Sardine');

  SELECT name FROM pinguine WHERE lieblingsfisch = 'Sardine';
vorhersage:
  art: auswahl
  frage: Wer hat danach Sardine als Lieblingsfisch?
  optionen:
    - text: |-
        Pina
        Pünktchen
      richtig: true
      erklaerung: Richtig. Beide hatten keinen Lieblingsfisch und haben Sardinen bekommen.
    - text: |-
        Pit
        Pina
        Pünktchen
      erklaerung: Pit hat auch Sardinen bekommen, aber sein Lieblingsfisch ist bekannt; IS NULL schließt ihn aus.
    - text: "(keine Zeile)"
      erklaerung: Pina und Pünktchen erfüllen beide Bedingungen.
```

```merke
text: "UPDATE tabelle SET spalte = wert, ... WHERE bedingung ändert die Werte in allen passenden Zeilen; der neue Wert darf aus dem alten gerechnet sein. Ohne WHERE trifft es jede Zeile. Erst mit SELECT nachsehen, dann ändern."
```

```frage
frageart: fehlerstelle
id: fehler-where
text: Das Skript soll nur Pauls Gewicht auf 5,3 Kilo setzen, setzt aber alle Pinguine auf 5,3 Kilo. Wo fehlt etwas?
code: |
  SELECT name, gewicht_kg
  FROM pinguine
  WHERE name = 'Paul';
  UPDATE pinguine
  SET gewicht_kg = 5.3;
zeile: 5
erklaerung: Genau. Das SELECT hat brav nachgesehen, aber dem UPDATE fehlt sein WHERE name = 'Paul'.
hinweis: Welche Anweisung ändert etwas, und was fehlt ihr?
```

```frage
frageart: ordnen
id: ordnen-update
text: Bring die Zeilen in Reihenfolge, damit Polly einen Fisch mehr pro Fütterung bekommt.
zeilen:
  - UPDATE fuetterungen
  - SET menge = menge + 1
  - WHERE pinguin_id = 6;
erklaerung: Richtig. UPDATE, SET, WHERE.
hinweis: Erst die Tabelle, dann was sich ändert, dann wo.
```

```augenzwinkern
text: Die Ostkolonie hat nach dem UPDATE ohne WHERE eine Beschwerde eingereicht. Sie wurde abgelehnt, weil beim nächsten Ausführen ohnehin alles wieder warm war.
```

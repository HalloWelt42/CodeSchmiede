---
id: sql-unterabfragen
sprache: sql
titel: Abfragen in Abfragen
kurz: Eine Abfrage liefert die Zahl oder die Liste, mit der eine andere weiterarbeitet; in WHERE, im SELECT und hinter FROM.
fuehrt_ein: [unterabfrage]
lernziele:
  - eine Unterabfrage in Klammern schreiben, die einen einzelnen Wert liefert, und damit vergleichen
  - mit IN und einer Unterabfrage gegen eine ganze Liste prüfen
  - die NULL-Falle bei NOT IN kennen
  - je Zeile eine Unterabfrage im SELECT rechnen lassen, die sich auf die äußere Zeile bezieht
  - das Ergebnis einer Abfrage hinter FROM wie eine Tabelle benutzen
karte: Ich frage erst nach, dann antworte ich
datensatz: pinguinzoo
bilder:
  - schluessel: karte_sql_unterabfragen
    art: sammelkarte
    sprache: sql
    motiv: Ein Pinguin öffnet eine Kiste, in der eine kleinere Kiste mit einem Zettel liegt
---

## Erst nachrechnen, dann vergleichen

```alltag
text: Die Frage "Welche Pinguine sind schwerer als der Durchschnitt?" kann der Pfleger nicht in einem Schritt beantworten. Erst rechnet er auf einem Zettel den Durchschnitt aus, dann legt er den Zettel neben die Waage. Eine Unterabfrage ist dieser Zettel.
zeichnung: kisten
```

Eine Unterabfrage ist eine ganze SELECT-Abfrage in runden Klammern, die mitten in einer anderen steht. Liefert sie genau einen Wert, eine Zeile mit einer Spalte, darf man mit ihr vergleichen wie mit einer Zahl. Die Datenbank rechnet sie zuerst aus und setzt das Ergebnis ein.

```beispiel
id: ueber-schnitt
code: |
  SELECT name, gewicht_kg
  FROM pinguine
  WHERE gewicht_kg > (SELECT AVG(gewicht_kg) FROM pinguine);
vorhersage:
  art: auswahl
  frage: Der Durchschnitt liegt bei 4,125 Kilo. Wie viele Zeilen hat das Ergebnis?
  vergleich: zeilen
  optionen:
    - text: 4 Zeilen
      richtig: true
      erklaerung: Richtig. Pit, Paul, Pepe und Polly wiegen mehr als 4,125 Kilo.
    - text: 1 Zeile
      erklaerung: Die Unterabfrage liefert eine Zahl, aber die äußere Abfrage vergleicht jeden Pinguin damit.
    - text: Fehler
      erklaerung: WHERE AVG(...) ginge nicht, aber in einer eigenen Abfrage in Klammern darf AVG stehen.
```

```frage
frageart: auswahl
id: warum-klammern
text: "Warum geht `WHERE gewicht_kg > AVG(gewicht_kg)` nicht, mit einer Unterabfrage aber schon?"
optionen:
  - text: Weil WHERE keine Zusammenfassung kennt, die Unterabfrage aber eine eigene, vollständige Abfrage ist
    richtig: true
    erklaerung: Richtig. Die Unterabfrage fasst für sich alle Pinguine zusammen und liefert eine einzige Zahl.
  - text: Weil AVG nur in Klammern funktioniert
    erklaerung: Klammern hat AVG in beiden Fällen; es geht um die eigene Abfrage mit SELECT und FROM.
  - text: Weil > nur mit Zahlen geht
    erklaerung: AVG liefert ja eine Zahl; das Problem ist, dass WHERE einzelne Zeilen prüft.
```

## Gegen eine Liste prüfen: IN

Liefert die Unterabfrage eine ganze Spalte, passt sie hinter `IN`, wie eine Liste von Werten. So findet man etwa alle Pinguine, die irgendwann Sardinen bekommen haben, ohne einen JOIN zu schreiben.

```beispiel
id: sardinen
code: |
  SELECT name
  FROM pinguine
  WHERE id IN (SELECT pinguin_id
               FROM fuetterungen
               WHERE fisch = 'Sardine');
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Pit
        Pina
        Pünktchen
      richtig: true
      erklaerung: Richtig. Die Unterabfrage liefert die Nummern 4, 8 und 1, die äußere Abfrage holt die Namen dazu.
    - text: |-
        4
        8
        1
      erklaerung: Das liefert die Unterabfrage. Die äußere Abfrage gibt aber name aus.
    - text: |-
        Pina
        Pünktchen
      erklaerung: Auch Pit hat am 22. Oktober Sardinen bekommen.
```

```falle
titel: NOT IN und NULL
text: "`WHERE name NOT IN (SELECT kolonie FROM pfleger)` sucht Kolonien ohne Pfleger und findet gar nichts, nicht einmal West. Schuld ist Jonas mit NULL: ob West ungleich NULL ist, weiß niemand. Abhilfe: in der Unterabfrage `WHERE kolonie IS NOT NULL`."
```

```frage
frageart: luecke
id: luecke-in
text: Ergänze, damit alle Pinguine aus Kolonien mit eiskaltem Wasser kommen.
code: |
  SELECT name
  FROM pinguine
  WHERE kolonie ___ (SELECT name FROM kolonien WHERE wassertemperatur < 0);
antworten: [["IN", "in"]]
erklaerung: Richtig, die Unterabfrage liefert eine Liste von Kolonien.
hinweis: Das Wort, mit dem man gegen eine Liste prüft.
```

## Je Zeile nachfragen

Eine Unterabfrage darf auch hinter SELECT stehen und für jede Zeile einen Wert liefern. Dann darf sie sich auf die äußere Zeile beziehen: `f.pinguin_id = p.id` meint den Pinguin, um den es gerade geht. Die Datenbank fragt also je Pinguin einmal nach.

```beispiel
id: mahlzeiten
code: |
  SELECT p.name,
         (SELECT COUNT(*)
          FROM fuetterungen f
          WHERE f.pinguin_id = p.id) AS mahlzeiten
  FROM pinguine p
  WHERE p.kolonie = 'Nord';
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Pit | 3
        Paul | 2
        Pina | 1
        Polly | 1
      richtig: true
      erklaerung: Richtig. Für jeden Pinguin des Nordens zählt die Unterabfrage seine Fütterungen.
    - text: |-
        Pit | 12
        Paul | 12
        Pina | 12
        Polly | 12
      erklaerung: Das wäre ohne f.pinguin_id = p.id; dann zählte sie jedes Mal alle Fütterungen.
    - text: "12"
      erklaerung: Die Unterabfrage steht im SELECT und liefert je Zeile einen Wert, die äußere Abfrage hat vier Zeilen.
```

## Eine Abfrage als Tabelle

Auch hinter FROM darf eine Unterabfrage stehen. Ihr Ergebnis ist dann eine Tabelle, mit der die äußere Abfrage weiterarbeitet. So lassen sich zwei Zusammenfassungen stapeln: erst die Fische je Tag, dann der Durchschnitt dieser Tagessummen.

```beispiel
id: tagesschnitt
code: |
  SELECT ROUND(AVG(fische), 1) AS schnitt
  FROM (SELECT tag, SUM(menge) AS fische
        FROM fuetterungen
        GROUP BY tag);
vorhersage:
  art: auswahl
  optionen:
    - text: "19.3"
      richtig: true
      erklaerung: Richtig. Die Tage hatten 23, 18 und 17 Fische, im Schnitt 19,3.
    - text: "4.8"
      erklaerung: Das wäre der Schnitt je Fütterung. Hier wird je Tag summiert und dann gemittelt.
    - text: |-
        2026-10-20 | 23
        2026-10-21 | 18
        2026-10-22 | 17
      erklaerung: Das ist die innere Abfrage. Die äußere fasst ihre Zeilen zu einer zusammen.
```

```merke
text: "Eine Unterabfrage steht in Klammern. Liefert sie einen Wert, vergleicht man mit ihr; liefert sie eine Spalte, prüft man mit IN. Im SELECT darf sie sich auf die äußere Zeile beziehen, hinter FROM ist sie eine Tabelle. Bei NOT IN auf NULL achten."
```

```frage
frageart: fehlerstelle
id: fehler-klammer-fehlt
text: Diese Abfrage meldet einen Fehler. In welcher Zeile?
code: |
  SELECT name,
         geburtsjahr
  FROM pinguine
  WHERE geburtsjahr = SELECT MIN(geburtsjahr) FROM pinguine;
zeile: 4
erklaerung: Genau. Eine Unterabfrage braucht runde Klammern, also `= (SELECT MIN(geburtsjahr) FROM pinguine)`.
hinweis: Woran erkennt die Datenbank, wo die innere Abfrage anfängt und aufhört?
```

```frage
frageart: ordnen
id: ordnen-unterabfrage
text: Bring die Zeilen in Reihenfolge, damit die größte Fütterung herauskommt.
zeilen:
  - SELECT tag, fisch, menge
  - FROM fuetterungen
  - WHERE menge = (SELECT MAX(menge) FROM fuetterungen);
erklaerung: Richtig. Die Unterabfrage findet die größte Menge, die äußere die Fütterung dazu.
hinweis: Die Unterabfrage steckt in der WHERE-Zeile.
```

```augenzwinkern
text: Pit hat gelernt, dass man in SQL vor jeder Antwort erst einmal nachfragen darf. Seitdem fragt er bei jeder Fütterung nach, ob es noch Nachschlag gibt.
```

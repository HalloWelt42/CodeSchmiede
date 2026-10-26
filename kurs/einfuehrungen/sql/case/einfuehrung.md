---
id: sql-case
sprache: sql
titel: Wenn, dann, sonst
kurz: Mit CASE je Zeile einen Wert nach Bedingungen wählen, Werte in Klassen einteilen und nach Bedingungen zählen.
fuehrt_ein: [case]
lernziele:
  - mit CASE WHEN ... THEN ... ELSE ... END je Zeile einen Wert wählen
  - wissen, dass die erste zutreffende Bedingung gewinnt
  - wissen, dass ohne ELSE NULL herauskommt
  - mit CASE innerhalb von SUM oder COUNT nach Bedingungen zählen
karte: Ich zeige jedem seinen Weg
datensatz: pinguinzoo
bilder:
  - schluessel: karte_sql_case
    art: sammelkarte
    sprache: sql
    motiv: Ein Pinguin steht vor einem Wegweiser mit drei Armen, die in verschiedene Richtungen zeigen
---

## Je Zeile entscheiden

```alltag
text: Am Eingang zur Waage steht ein Wegweiser. Wer mindestens 4,5 Kilo wiegt, geht nach links zu den Schweren, wer mindestens 3,5 Kilo wiegt, geradeaus zu den Mittleren, alle anderen nach rechts. CASE ist dieser Wegweiser, für jede Zeile einzeln.
zeichnung: wegweiser
```

`CASE` prüft der Reihe nach die Bedingungen hinter `WHEN`. Bei der ersten, die stimmt, nimmt es den Wert hinter `THEN`. Stimmt keine, gilt der Wert hinter `ELSE`. `END` schließt das Ganze ab, und mit AS bekommt die neue Spalte ihren Namen. CASE darf überall stehen, wo ein Wert stehen darf: hinter SELECT, in WHERE, in ORDER BY.

```beispiel
id: klassen
code: |
  SELECT name, gewicht_kg,
         CASE WHEN gewicht_kg >= 4.5 THEN 'schwer'
              WHEN gewicht_kg >= 3.5 THEN 'mittel'
              ELSE 'leicht'
         END AS klasse
  FROM pinguine
  WHERE kolonie = 'Nord';
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Pit | 4.2 | mittel
        Paul | 5.1 | schwer
        Pina | 3.5 | mittel
        Polly | 4.6 | schwer
      richtig: true
      erklaerung: Richtig. Paul und Polly sind schwer, Pit und Pina mittel; Pina liegt mit genau 3,5 Kilo auf der Grenze und gehört dazu.
    - text: |-
        Pit | 4.2 | mittel
        Paul | 5.1 | schwer
        Pina | 3.5 | leicht
        Polly | 4.6 | schwer
      erklaerung: ">= 3.5 heißt mindestens 3,5; Pina wiegt genau 3,5 Kilo und ist damit mittel."
    - text: |-
        Pit | 4.2 | mittel
        Paul | 5.1 | mittel
        Pina | 3.5 | mittel
        Polly | 4.6 | mittel
      erklaerung: Die erste Bedingung ist die für schwer; Paul und Polly erfüllen sie und landen dort.
```

```frage
frageart: auswahl
id: kein-else
text: "Was steht bei `CASE WHEN wassertemperatur < 0 THEN 'Eis' END` für die Ostkolonie mit 9,5 Grad?"
optionen:
  - text: "NULL"
    richtig: true
    erklaerung: Richtig. Ohne ELSE gibt es keinen Ersatz, also NULL.
  - text: Eis
    erklaerung: 9,5 ist nicht kleiner als null, die Bedingung stimmt nicht.
  - text: Ein leerer Text
    erklaerung: Einen leeren Text gäbe es nur mit ELSE ''. Ohne ELSE kommt NULL.
```

## Die Reihenfolge entscheidet

CASE hört bei der ersten zutreffenden Bedingung auf. Wer die weite Bedingung vor die enge schreibt, erreicht die enge nie. Darum stehen die strengsten Bedingungen zuerst.

```beispiel
id: falsch-herum
code: |
  SELECT name,
         CASE WHEN gewicht_kg >= 3.5 THEN 'mittel'
              WHEN gewicht_kg >= 4.5 THEN 'schwer'
              ELSE 'leicht'
         END AS klasse
  FROM pinguine
  WHERE kolonie = 'Nord';
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Pit | mittel
        Paul | mittel
        Pina | mittel
        Polly | mittel
      richtig: true
      erklaerung: Richtig, und so war es nicht gemeint. Wer 4,5 Kilo wiegt, wiegt auch mindestens 3,5 und bleibt schon bei mittel stehen.
    - text: |-
        Pit | mittel
        Paul | schwer
        Pina | mittel
        Polly | schwer
      erklaerung: So wäre es gemeint. CASE hält aber bei der ersten passenden Bedingung an, und die ist hier die weite.
    - text: |-
        Pit | schwer
        Paul | schwer
        Pina | schwer
        Polly | schwer
      erklaerung: Die erste Bedingung liefert mittel, nicht schwer.
```

```falle
titel: Weit vor eng
text: "Steht die weite Bedingung `>= 3.5` vor der engen `>= 4.5`, kommt CASE nie bis zur engen. Die Abfrage läuft ohne Fehler, sie rechnet nur falsch. Darum die strengste Bedingung zuerst."
```

## Nach Bedingungen zählen

CASE in einer Zusammenfassung macht aus einer Summe eine Summe unter Bedingung: `SUM(CASE WHEN fisch = 'Hering' THEN menge ELSE 0 END)` zählt nur die Heringe zusammen, alle anderen Fütterungen tragen 0 bei. So entsteht in einer Zeile ein kleiner Bericht mit mehreren Spalten.

```beispiel
id: bericht
code: |
  SELECT tag,
         SUM(CASE WHEN fisch = 'Hering' THEN menge ELSE 0 END) AS hering,
         SUM(menge) AS alle
  FROM fuetterungen
  GROUP BY tag
  ORDER BY tag;
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        2026-10-20 | 14 | 23
        2026-10-21 | 9 | 18
        2026-10-22 | 0 | 17
      richtig: true
      erklaerung: Richtig. Am 22. gab es keinen Hering, dort steht dank ELSE 0 eine 0.
    - text: |-
        2026-10-20 | 14 | 23
        2026-10-21 | 9 | 18
        2026-10-22 | NULL | 17
      erklaerung: Mit ELSE 0 trägt jede Fütterung ohne Hering 0 bei; die Summe ist 0, nicht NULL.
    - text: |-
        2026-10-20 | 2 | 4
        2026-10-21 | 2 | 4
        2026-10-22 | 0 | 4
      erklaerung: Das wäre gezählt statt summiert. SUM zählt die Mengen zusammen.
```

```frage
frageart: luecke
id: luecke-end
text: Ergänze, damit die Abfrage läuft.
code: |
  SELECT name,
         CASE WHEN geburtsjahr >= 2021 THEN 'jung' ELSE 'erfahren' ___ AS stufe
  FROM pinguine;
antworten: [["END", "end"]]
erklaerung: Richtig, END schließt jedes CASE ab.
hinweis: Jedes CASE braucht ein Ende.
```

```merke
text: "CASE WHEN bedingung THEN wert ... ELSE wert END wählt je Zeile einen Wert. Die erste zutreffende Bedingung gewinnt, ohne ELSE kommt NULL. In SUM oder COUNT zählt CASE nur, was eine Bedingung erfüllt."
```

```frage
frageart: fehlerstelle
id: fehler-then
text: Diese Abfrage meldet einen Fehler. In welcher Zeile?
code: |
  SELECT name,
         CASE WHEN wassertemperatur < 0 THEN 'eisig'
              WHEN wassertemperatur < 5 'frisch'
              ELSE 'mild'
         END AS gefuehl
  FROM kolonien;
zeile: 3
erklaerung: Genau. Zu jedem WHEN gehört ein THEN vor dem Wert.
hinweis: Was fehlt zwischen Bedingung und Wert?
```

```frage
frageart: ordnen
id: ordnen-case
text: Bring die Zeilen in Reihenfolge, damit jede Kolonie eine Einschätzung ihres Wassers bekommt.
zeilen:
  - SELECT name,
  - "       CASE WHEN wassertemperatur < 0 THEN 'eisig'"
  - "            WHEN wassertemperatur < 5 THEN 'frisch'"
  - "            ELSE 'mild'"
  - "       END AS gefuehl"
  - FROM kolonien;
erklaerung: Richtig. Erst die strengste Bedingung, dann die weitere, zuletzt ELSE und END.
hinweis: Unter null ist strenger als unter fünf.
```

```augenzwinkern
text: Der Wegweiser zeigt seit Jahren zuverlässig in drei Richtungen. Pünktchen geht trotzdem immer dorthin, wo es Sardinen gibt.
```

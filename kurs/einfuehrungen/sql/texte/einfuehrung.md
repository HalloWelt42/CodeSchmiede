---
id: sql-texte
sprache: sql
titel: Texte durchsuchen
kurz: Mit LIKE nach Mustern suchen statt nach genauen Werten, und Texte mit UPPER, LENGTH, SUBSTR und REPLACE bearbeiten.
fuehrt_ein: [like, textfunktionen]
lernziele:
  - mit LIKE und % nach Anfang, Ende oder Mitte eines Textes suchen
  - mit _ genau ein beliebiges Zeichen offenlassen
  - wissen, dass LIKE bei A bis Z nicht auf Groß und klein achtet, = aber schon
  - Texte mit UPPER, LOWER, LENGTH, SUBSTR und REPLACE umformen
karte: Ich finde, was so ähnlich aussieht
datensatz: pinguinzoo
bilder:
  - schluessel: karte_sql_texte
    art: sammelkarte
    sprache: sql
    motiv: Ein Pinguin hält eine Schablone mit Löchern über eine Reihe Namensschilder
---

## Suchen mit Lücken: LIKE

```alltag
text: Der Pfleger weiß nur noch, dass der Name mit "Pa" anfing. Er legt eine Schablone über die Namensschilder, in der nur die ersten beiden Buchstaben fest sind, der Rest ist ein Loch. LIKE ist diese Schablone.
zeichnung: schablone
```

`=` vergleicht ganz genau. `LIKE` vergleicht mit einem Muster, in dem Platzhalter stehen dürfen: `%` steht für beliebig viele Zeichen, auch für gar keines. `'Pa%'` heißt also "fängt mit Pa an", `'%a'` heißt "hört mit a auf", und `'%eis%'` heißt "enthält irgendwo eis".

```beispiel
id: anfang
code: |
  SELECT name
  FROM pinguine
  WHERE name LIKE 'Pa%';
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Paul
        Pablo
      richtig: true
      erklaerung: Richtig. Beide Namen fangen mit Pa an, was danach kommt, ist egal.
    - text: "(keine Zeile)"
      erklaerung: Mit = wäre das so, denn niemand heißt genau Pa. LIKE mit % lässt den Rest offen.
    - text: |-
        Paul
        Pablo
        Pia
        Pina
      erklaerung: Pia und Pina fangen mit Pi an, nicht mit Pa.
```

```frage
frageart: auswahl
id: muster-ende
text: Welches Muster findet alle Namen, die auf a enden?
als_code: true
optionen:
  - text: "'%a'"
    richtig: true
    erklaerung: Richtig, vorn darf alles stehen, am Ende muss a kommen.
  - text: "'a%'"
    erklaerung: Das findet Namen, die mit a anfangen.
  - text: "'%a%'"
    erklaerung: Das findet jeden Namen mit einem a irgendwo, auch Paul.
```

## Genau ein Zeichen: _ und Groß und klein

Der Unterstrich `_` steht für genau ein beliebiges Zeichen. `'P_t'` passt auf Pit oder Pat, aber nicht auf Pitt. Vier Unterstriche `'____'` finden alle Texte mit genau vier Zeichen.

Anders als `=` achtet LIKE bei den Buchstaben A bis Z nicht auf Groß und klein: `'pi%'` findet auch Pit. Bei Umlauten macht SQLite das aber nicht mit, `'ü'` und `'Ü'` bleiben verschieden.

```beispiel
id: klein
code: |
  SELECT name
  FROM pinguine
  WHERE name LIKE 'pi%';
vorhersage:
  art: auswahl
  frage: Wie viele Zeilen hat das Ergebnis?
  vergleich: zeilen
  optionen:
    - text: 3 Zeilen
      richtig: true
      erklaerung: Richtig. Pit, Pia und Pina; LIKE nimmt es mit dem kleinen p nicht so genau.
    - text: 0 Zeilen
      erklaerung: Mit = wäre die Schreibweise wichtig. LIKE achtet bei A bis Z nicht auf Groß und klein.
    - text: 2 Zeilen
      erklaerung: Auch Pina fängt mit Pi an.
```

```frage
frageart: luecke
id: luecke-unterstrich
text: Ergänze das Muster, damit alle Pinguine mit genau drei Buchstaben im Namen kommen.
code: |
  SELECT name
  FROM pinguine
  WHERE name LIKE ___;
antworten: [["'___'"]]
erklaerung: Richtig, drei Unterstriche für drei Zeichen.
hinweis: Ein Unterstrich steht für genau ein Zeichen; das Muster braucht Hochkommas.
```

```falle
titel: LIKE ohne Platzhalter
text: "`WHERE name LIKE 'Pa'` sucht genau den Text Pa und findet hier niemanden. Ohne `%` oder `_` arbeitet LIKE fast wie =."
```

## Texte umbauen

Für Texte gibt es eine Werkzeugkiste aus Funktionen. Man schreibt den Namen der Funktion, dahinter in Klammern, womit sie arbeiten soll:

- `UPPER(text)` und `LOWER(text)`: alles groß oder alles klein
- `LENGTH(text)`: wie viele Zeichen der Text hat
- `SUBSTR(text, start, laenge)`: ein Stück aus dem Text, gezählt ab 1
- `REPLACE(text, alt, neu)`: ersetzt jedes Vorkommen von alt durch neu, mit genauer Schreibweise

Funktionen dürfen hinter SELECT stehen und genauso in WHERE.

```beispiel
id: laenge
code: |
  SELECT name, LENGTH(name) AS laenge
  FROM pinguine
  WHERE LENGTH(name) > 4;
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Polly | 5
        Pablo | 5
        Pünktchen | 9
      richtig: true
      erklaerung: Richtig. Nur Namen mit mehr als vier Zeichen bleiben übrig.
    - text: |-
        Paul | 4
        Pina | 4
        Pepe | 4
        Polly | 5
        Pablo | 5
        Pünktchen | 9
      erklaerung: Vier ist nicht größer als vier; Paul, Pina und Pepe fallen heraus.
    - text: Pünktchen | 9
      erklaerung: Polly und Pablo haben fünf Zeichen, das ist mehr als vier.
```

```beispiel
id: stueck
code: |
  SELECT name, SUBSTR(name, 1, 2) AS anfang
  FROM pfleger;
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Greta | Gr
        Hannes | Ha
        Ida | Id
        Jonas | Jo
      richtig: true
      erklaerung: Richtig. Ab dem ersten Zeichen zwei Stück.
    - text: |-
        Greta | re
        Hannes | an
        Ida | da
        Jonas | on
      erklaerung: SQL zählt ab 1, das erste Zeichen ist also Nummer 1.
    - text: |-
        Greta | G
        Hannes | H
        Ida | I
        Jonas | J
      erklaerung: Die 2 am Ende ist die Länge des Stücks, nicht die Stelle, an der es endet.
```

```falle
titel: Umlaute bleiben klein
text: "`UPPER('Pünktchen')` ergibt in SQLite `PüNKTCHEN`. UPPER und LOWER ändern nur die Buchstaben A bis Z; ä, ö, ü bleiben, wie sie sind."
```

```merke
text: "LIKE sucht mit Mustern: % für beliebig viele Zeichen, _ für genau eines; bei A bis Z ist Groß und klein egal. UPPER, LOWER, LENGTH, SUBSTR und REPLACE bauen Texte um, hinter SELECT und in WHERE."
```

```frage
frageart: fehlerstelle
id: fehler-muster
text: Diese Abfrage meldet einen Fehler. In welcher Zeile?
code: |
  SELECT name,
         LENGTH(name) AS laenge
  FROM pinguine
  WHERE name LIKE P%;
zeile: 4
erklaerung: Genau. Auch ein Muster ist ein Text und braucht Hochkommas, also `LIKE 'P%'`.
hinweis: Wo steht ein Text ohne Hochkommas?
```

```frage
frageart: ordnen
id: ordnen-ersetzen
text: Bring die Zeilen in Reihenfolge, damit aus jeder Eishöhle eine Schneehöhle wird.
zeilen:
  - SELECT name,
  - "       REPLACE(lage, 'Eis', 'Schnee') AS winterlage"
  - FROM kolonien;
erklaerung: Richtig. Aus Eishöhle wird Schneehöhle; Packeis bleibt, denn dort steht eis klein.
hinweis: Die Spalten stehen hinter SELECT, die Tabelle kommt zum Schluss.
```

```augenzwinkern
text: Pünktchen ist es gewohnt, dass Datenbanken seinen Namen nicht ganz großschreiben können. Und die Pünktchen sind sowieso das Beste daran.
```

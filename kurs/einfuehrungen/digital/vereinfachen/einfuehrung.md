---
id: digital-vereinfachen
sprache: digital
titel: Schaltungen vereinfachen
kurz: Aus einer Wahrheitstabelle die kürzeste Formel finden, über Nachbarn, den Würfel der Belegungen und das KV-Diagramm.
fuehrt_ein: [minterm, nachbarn, wuerfel, kv_diagramm, block, egal_feld]
lernziele:
  - aus einer Wahrheitstabelle eine Formel mit einem Term je 1 aufschreiben
  - zwei Nachbarn, die sich in einem Eingang unterscheiden, zu einem kürzeren Term zusammenfassen
  - ein KV-Diagramm mit zwei, drei und vier Eingängen lesen, auch über den Rand
  - Blöcke aus 1, 2, 4 und 8 Feldern einkreisen und ihren Term ablesen
  - Egal-Felder nutzen, um Blöcke zu vergrößern
  - aus den Blöcken einen Schaltplan bauen und erkennen, wann das KV-Diagramm nicht hilft
karte: Ich mache aus jeder Wahrheitstabelle eine kurze Schaltung
bilder:
  - schluessel: karte_digital_vereinfachen
    art: sammelkarte
    sprache: digital
    motiv: Ein Pinguin faltet einen Pappwürfel auseinander, auf dessen Ecken kleine leuchtende Lämpchen sitzen
---

## Jede 1 ein eigener Baustein

Aus den Schaltungen kennst du die Wahrheitstabelle: für jede Belegung der Eingänge steht dort, ob der Ausgang 1 ist. Daraus lässt sich immer eine Schaltung bauen, ganz ohne Nachdenken: Für jede Zeile mit einer 1 ein UND, das genau diese Zeile erkennt, und alle zusammen mit ODER.

Die Zeile A = 0, B = 0, C = 1 wird so zu Ā·B̄·C: A ist 0, also überstrichen (NICHT A), B auch, C ist 1. So ein Term heißt **Minterm**, weil er nur eine einzige Zeile trifft.

```kv
id: minterme
eingaenge: [A, B, C]
werte: "01010111"
start: raster
formeln:
  - titel: Jede 1 einzeln
    formel: "!A !B C + !A B C + A !B C + A B !C + A B C"
```

```frage
frageart: auswahl
id: minterm-lesen
text: "Welcher Term trifft genau die Zeile A = 1, B = 0, C = 1?"
optionen:
  - text: "A·B̄·C"
    richtig: true
    erklaerung: Richtig. A und C sind 1 und bleiben stehen, B ist 0 und bekommt den Strich.
  - text: "Ā·B·C̄"
    erklaerung: Das ist genau das Gegenteil, die Zeile 0, 1, 0.
  - text: "A·C"
    erklaerung: A·C trifft zwei Zeilen, 101 und 111. Ein Minterm nennt jeden Eingang.
```

Das klappt immer, ist aber teuer: fünf Einsen, fünf UND mit je drei Eingängen, dazu NICHT und ODER. Aus Bausteinen mit zwei Eingängen gebaut, wie in den Schaltungen, braucht die Tabelle oben so siebzehn Bausteine. Es geht viel kürzer.

```merke
text: "Jede Zeile mit einer 1 wird ein UND aus allen Eingängen (die mit 0 überstrichen), alle zusammen ein ODER. Richtig ist das immer, kurz fast nie."
```

## Nachbarn fassen sich zusammen

Schau dir zwei Minterme an, die sich nur in einem Eingang unterscheiden: A·B·C und A·B·C̄. Der erste gilt, wenn C 1 ist, der zweite, wenn C 0 ist. Zusammen gelten sie also immer, wenn A und B 1 sind, egal was C ist. Aus zwei Termen mit drei Buchstaben wird einer mit zwei: **A·B**.

```alltag
text: "Im Treppenhaus brennt Licht, wenn es dunkel ist und jemand den Taster drückt, bei Regen. Und wenn es dunkel ist und jemand drückt, ohne Regen. Dann kommt es auf den Regen offenbar gar nicht an."
zeichnung: treppenhaus
```

Solche Paare heißen **Nachbarn**: Belegungen, die sich in genau einem Eingang unterscheiden. Nachbarn mit 1 lassen sich immer zusammenfassen, und der Eingang, in dem sie sich unterscheiden, fällt weg.

```kv
id: zwei-nachbarn
eingaenge: [A, B]
werte: "0011"
start: raster
formeln:
  - titel: Einzeln
    formel: "A !B + A B"
  - titel: Zusammengefasst
    formel: "A"
```

```frage
frageart: auswahl
id: zusammenfassen
text: "Was ergibt Ā·B·C + Ā·B·C̄ zusammengefasst?"
optionen:
  - text: "Ā·B"
    richtig: true
    erklaerung: Richtig. Die beiden unterscheiden sich nur in C, also fällt C weg.
  - text: "B·C"
    erklaerung: C ist gerade der Eingang, der wechselt. Er fällt weg, A bleibt.
  - text: "Ā·B·C"
    erklaerung: Das ist nur einer der beiden. Zusammen gelten sie für C = 0 und C = 1.
```

## Der Würfel der Belegungen

Bei drei Eingängen gibt es acht Belegungen. Stell dir jede als Ecke eines Würfels vor: A, B und C sind die drei Richtungen. Zwei Ecken, die durch eine Kante verbunden sind, unterscheiden sich in genau einem Eingang. Sie sind also genau die Nachbarn, die man zusammenfassen kann.

```kv
id: wuerfel
eingaenge: [A, B, C]
werte: "01010111"
start: wuerfel
formeln:
  - titel: Jede 1 einzeln
    formel: "!A !B C + !A B C + A !B C + A B !C + A B C"
  - titel: Große Blöcke
    formel: "C + A B"
```

Klick rechts auf eine Ecke: ihre drei Nachbarn leuchten. Und klick auf "Große Blöcke": Die vier Ecken mit C = 1 bilden eine ganze Seitenfläche des Würfels, das ist der Term C. Die Kante zwischen 110 und 111 ist A·B.

```frage
frageart: auswahl
id: wie-viele-nachbarn
text: "Wie viele Nachbarn hat jede Ecke bei drei Eingängen?"
optionen:
  - text: "3"
    richtig: true
    erklaerung: Richtig, an jeder Ecke eines Würfels treffen drei Kanten zusammen, eine je Eingang.
  - text: "2"
    erklaerung: Das wären zwei Eingänge, ein Quadrat. Beim Würfel kommt die dritte Richtung dazu.
  - text: "7"
    erklaerung: Das sind alle anderen Ecken. Nachbarn sind nur die, die sich in einem Eingang unterscheiden.
```

```augenzwinkern
text: "Bei vier Eingängen wäre es ein Würfel in vier Dimensionen. Den kann sich niemand vorstellen, darum gibt es den nächsten Abschnitt."
```

## Vom Würfel zum Raster

Ein Würfel ist schön zum Verstehen, aber mühsam zum Zeichnen. Also klappen wir ihn auf: die Ecken mit A = 0 in die obere Zeile, die mit A = 1 in die untere. Schieb rechts den Regler und sieh zu.

```alltag
text: "Eine Würfelverpackung aus Pappe kann man aufschneiden und flach hinlegen. Dann sieht man alle Seiten auf einmal, aber zwei Kanten, die vorher zusammengehörten, liegen plötzlich am linken und am rechten Rand."
zeichnung: pappwuerfel
```

```kv
id: aufklappen
eingaenge: [A, B, C]
werte: "01010111"
start: wuerfel
regler: true
formeln:
  - titel: Jede 1 einzeln
    formel: "!A !B C + !A B C + A !B C + A B !C + A B C"
  - titel: Große Blöcke
    formel: "C + A B"
```

```frage
frageart: auswahl
id: nachbarn-am-rand
text: "Welche Felder sind Nachbarn von ABC = 010 (obere Zeile, ganz rechts)?"
optionen:
  - text: "011, 000 und 110"
    richtig: true
    erklaerung: "Richtig. 011 liegt links daneben, 110 darunter, und 000 ganz links am anderen Rand: dort war der Würfel zusammengeklebt."
  - text: "nur 011 und 110"
    erklaerung: "Die sieht man sofort. Aber 010 hat am Würfel drei Kanten; die dritte führt über den Rand zu 000."
  - text: "011, 001 und 110"
    erklaerung: "001 unterscheidet sich von 010 in zwei Eingängen (B und C). Das ist kein Nachbar, auch wenn es nah aussieht."
```

```merke
text: "Die Spalten heißen nicht 00, 01, 10, 11, sondern 00, 01, 11, 10. Nur so unterscheiden sich Spalten, die nebeneinanderliegen, in genau einem Eingang. Die erste und die letzte Spalte sind auch Nachbarn: dort war der Würfel zusammengeklebt."
```

## Blöcke einkreisen

Im KV-Diagramm sieht man Nachbarn auf einen Blick: Felder, die nebeneinander oder untereinander liegen, auch über den Rand. Ein **Block** ist ein Rechteck aus 1, 2, 4 oder 8 Feldern, in dem nur Einsen liegen. Jeder Block ist ein Term: Was in allen seinen Feldern gleich ist, steht im Term, was wechselt, fällt weg.

```kv
id: mehrheit
eingaenge: [A, B, C]
werte: "00010111"
start: raster
formeln:
  - titel: Drei Blöcke
    formel: "A B + A C + B C"
```

Die Regeln für eine kurze Formel sind einfach: Jede 1 muss in einem Block liegen, keine 0 darf hinein. Jeder Block so groß wie möglich, denn je größer der Block, desto weniger Buchstaben. Und kein Block mehr als nötig. Blöcke dürfen sich überlappen.

```frage
frageart: auswahl
id: block-lesen
text: "Ein Block umfasst die Felder 101 und 111. Welcher Term ist das?"
optionen:
  - text: "A·C"
    richtig: true
    erklaerung: Richtig. A ist in beiden 1, C auch, B wechselt und fällt weg.
  - text: "A·B·C"
    erklaerung: Das wäre nur das Feld 111. B wechselt im Block, also fällt B weg.
  - text: "B"
    erklaerung: Gerade B wechselt. Es bleibt, was gleich ist.
```

```falle
titel: Drei Felder sind kein Block
text: "Drei Einsen in einer Reihe sind kein Block, denn 3 ist keine Zweierpotenz. Nimm zwei Blöcke aus je zwei Feldern, die sich in der Mitte überlappen."
```

## Egal-Felder als Joker

Manche Belegungen kommen nie vor. Eine 7-Segment-Anzeige bekommt die Ziffern 0 bis 9 als vier Bits, aber 10 bis 15 gibt es nicht. Was der Ausgang dort macht, ist egal, und im KV-Diagramm steht ein **x**. Ein x darf in einen Block, wenn der dadurch größer wird, muss aber nicht.

```kv
id: segment-e
eingaenge: [A, B, C, D]
werte: "1010001010xxxxxx"
start: raster
formeln:
  - titel: Ohne Joker
    formel: "!A !B !D + !B !C !D + !A C !D"
  - titel: Mit Jokern
    formel: "!B !D + C !D"
```

Bei vier Eingängen ist das Raster vier mal vier, und auch oben und unten sind Nachbarn. Die vier Ecken gehören damit zusammen: der Block B̄·D̄ oben ist genau das.

```frage
frageart: auswahl
id: joker
text: "Muss jedes x in einem Block liegen?"
optionen:
  - text: "Nein, nur wenn der Block dadurch größer wird"
    richtig: true
    erklaerung: Richtig. Ein x ist ein Joker, kein Auftrag.
  - text: "Ja, wie jede 1"
    erklaerung: Ein x heißt egal. Liegt es in keinem Block, ist der Ausgang dort eben 0, und auch das ist erlaubt.
  - text: "Nein, x darf nie in einen Block"
    erklaerung: Doch, gerade dafür sind sie da. Sie machen Blöcke größer und Formeln kürzer.
```

## Vom Block zum Schaltplan

Aus der Formel wird wieder eine Schaltung: ein NICHT für jeden überstrichenen Eingang, ein UND für jeden Block, ein ODER für alles zusammen. Aus siebzehn Bausteinen sind für das Beispiel vom Anfang zwei geworden: C ODER (A UND B).

```kv
id: zum-plan
eingaenge: [A, B, C]
werte: "01010111"
start: raster
plan: true
formeln:
  - titel: Jede 1 einzeln
    formel: "!A !B C + !A B C + A !B C + A B !C + A B C"
  - titel: Große Blöcke
    formel: "C + A B"
```

```falle
titel: Das Schachbrett
text: "Bei der Summe eines Volladdierers liegen die Einsen wie auf einem Schachbrett: keine zwei sind Nachbarn. Das KV-Diagramm kann nichts zusammenfassen. Mit XOR braucht man trotzdem nur zwei Bausteine. Das KV-Diagramm findet die kürzeste Formel aus UND, ODER und NICHT, nicht die kürzeste Schaltung überhaupt."
```

```frage
frageart: auswahl
id: bausteine-zaehlen
text: "Wie viele Bausteine braucht B̄·D̄ + C·D̄ mit Bausteinen aus zwei Eingängen?"
optionen:
  - text: "5: zwei NICHT, zwei UND, ein ODER"
    richtig: true
    erklaerung: Richtig. D̄ wird nur einmal gebaut und von beiden UND benutzt.
  - text: "6"
    erklaerung: D̄ kommt zweimal vor, braucht aber nur ein NICHT.
  - text: "3"
    erklaerung: Die beiden NICHT für B und D zählen mit.
```

```augenzwinkern
text: "Ein KV-Diagramm ist wie Aufräumen: Erst sieht man nur Kram, dann passen auf einmal vier Sachen in eine Kiste."
```

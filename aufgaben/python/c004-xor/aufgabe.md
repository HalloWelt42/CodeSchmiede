---
schema_version: 1
id: c004-xor
revision: 1
titel: XOR mit kurzem Schlüssel
sprache: python
task_type: codes
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 60
schaetz_minuten: 40
tags: [codes, bytes, bitoperationen]
voraussetzungen: []
quelle:
  url: null
  notiz: Codes knacken, Level 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 15
hints:
  - kosten: 1
    text: "`bytes.fromhex(geheim)` macht aus dem Hex-Text Bytes. XOR ist sein eigenes Gegenteil: `b ^ k ^ k == b`. Mit `.decode(errors=\"replace\")` wird aus den Bytes wieder Text, auch wenn ein Versuch Unsinn ergibt."
  - kosten: 1
    text: "Wie bei Vigenère: Bei Schlüssellänge n gehört jedes n-te Byte zum selben Schlüsselbyte. Probier für jede Spalte alle 256 Bytes und gib Punkte für Kleinbuchstaben und Leerzeichen: Text besteht fast nur daraus."
  - kosten: 1
    text: "Die Länge: Ein Vielfaches der richtigen Länge passt genauso gut. Nimm deshalb die kleinste Länge, deren Punkte fast so hoch sind wie die besten."
starter_code: |
  def zurueck(geheim, wort):
      # geheim ist Hex, jedes Byte XOR mit dem Byte des Worts an derselben Stelle (reihum)
      return geheim


  def knacke(geheim):
      return geheim
codes:
  verfahren: xor
  sichtbar:
    - name: Probe
      klar: "Hallo Welt! Wer das lesen kann, hat XOR schon verstanden."
      schluessel: ab
      funktion: zurueck
      mit: [ab]
    - name: Nachricht 1
      schluessel: Code
      klar: >-
        Lieber Max, das Treffen findet am Donnerstag in der Bibliothek statt, gleich neben den
        Comics. Bring bitte deinen Laptop mit, wir wollen die neue Version vom Spiel ausprobieren.
        Und erzähl niemandem davon, sonst wollen alle mitspielen. Gruß, Lena
    - name: Nachricht 2
      schluessel: k3y
      klar: >-
        Die Wetterstation auf dem Dach meldet: Temperatur 18 Grad, Wind aus Westen, leichter Regen.
        Morgen soll es sonniger werden, am Wochenende kommt dann der erste richtige Sommertag des
        Jahres. Zeit, das Fahrrad aus dem Keller zu holen und die Reifen aufzupumpen.
  versteckt:
    - name: Nachricht 3
      schluessel: Z
      klar: >-
        Ein einziges Byte als Schlüssel ist schnell geknackt: es gibt nur 256 Möglichkeiten,
        und nur eine davon ergibt lesbaren Text. Darum sind kurze Schlüssel eine schlechte Idee.
    - name: Nachricht 4
      schluessel: Kiel
      klar: >-
        Die Fähre nach Norwegen legt um zwei Uhr ab. Wer mitfahren will, sollte eine halbe Stunde
        vorher am Terminal sein, mit Ausweis und Fahrkarte. An Bord gibt es ein Restaurant, ein
        kleines Kino und eine Aussichtsplattform, von der man bei klarem Wetter Wale sehen kann.
    - name: Nachricht 5
      schluessel: s3cr3t
      klar: >-
        Ein Schlüssel mit sechs Zeichen ist schon besser, aber nicht gut. Solange der Schlüssel viel
        kürzer ist als der Text, wiederholt er sich, und jede Wiederholung ist eine Spur. Nur ein
        Schlüssel, der so lang ist wie die Nachricht und nie wieder benutzt wird, ist wirklich sicher.
  teilschritte:
    - titel: Mit Schlüssel zurück
      text: "`zurueck(geheim, \"ab\")` macht aus der Probe wieder Text: jedes Byte XOR mit dem Byte des Schlüssels an derselben Stelle."
    - titel: Schlüssel finden
      text: "`knacke(geheim)` findet Länge und Bytes des Schlüssels selbst."
      nachrichten: [Nachricht 1, Nachricht 2]
    - titel: Alle Nachrichten
      text: "Zum Schluss die versteckten Nachrichten, mit Schlüsseln von einem bis sechs Zeichen."
      nachrichten: alle
  sterne: {ms: 700, zeichen: 900}
---

# XOR mit kurzem Schlüssel

Computer verschlüsseln nicht Buchstaben, sondern Bytes. Das einfachste Werkzeug dafür ist XOR (`^` in Python): Es kippt genau die Bits, die im Schlüssel gesetzt sind. Zweimal mit demselben Schlüssel gekippt, ist alles wieder wie vorher. Praktisch, und darum sehr beliebt.

Die Nachrichten sind mit einem kurzen Wort verschlüsselt, das sich reihum wiederholt, und kommen als Hex-Text an: zwei Zeichen je Byte. Diesmal mit Groß- und Kleinbuchstaben, Ziffern und Umlauten, denn Bytes ist das alles egal.

Schreib `knacke(geheim)`. Kleiner Trost: Was du hier knackst, ist dieselbe Idee wie bei Vigenère, nur mit 256 statt 26 Möglichkeiten je Stelle.

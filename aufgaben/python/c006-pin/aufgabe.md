---
schema_version: 1
id: c006-pin
revision: 1
titel: PIN gegen Prüfwert
sprache: python
task_type: codes
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 40
schaetz_minuten: 25
tags: [codes, hashlib, schleifen, formatierung]
voraussetzungen: []
quelle:
  url: null
  notiz: Codes knacken, Level 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 15
hints:
  - kosten: 1
    text: "`hashlib.sha256(pin.encode()).hexdigest()` macht aus dem Text einer PIN ihren Prüfwert."
  - kosten: 1
    text: "Probier alle PINs von 0000 bis 9999. Aus der Zahl 42 wird mit `f\"{zahl:04d}\"` der Text \"0042\": die führenden Nullen gehören zur PIN."
starter_code: |
  import hashlib


  def pruefwert(pin):
      # SHA-256 des Texts der PIN, als Hex
      return pin


  def knacke(geheim):
      return "0000"
codes:
  verfahren: pin
  sichtbar:
    - name: Probe
      klar: "1234"
      funktion: pruefwert
      richtung: verschluesseln
    - name: Fahrradschloss
      klar: "4711"
    - name: Haustür
      klar: "2580"
  versteckt:
    - name: Spind
      klar: "0042"
    - name: Tresor
      klar: "9999"
    - name: Garage
      klar: "1000"
    - name: Handy
      klar: "0815"
  teilschritte:
    - titel: Prüfwert rechnen
      text: "`pruefwert(\"1234\")` liefert den SHA-256 der PIN als Hex, so wie die App ihn speichert."
    - titel: Alle durchprobieren
      text: "`knacke(geheim)` probiert jede PIN, bis ihr Prüfwert passt."
      nachrichten: [Fahrradschloss, Haustür]
    - titel: Alle Schlösser
      text: "Zum Schluss die versteckten Prüfwerte, auch PINs mit führenden Nullen."
      nachrichten: alle
  sterne: {ms: 600, zeichen: 220}
---

# PIN gegen Prüfwert

Eine gute App speichert eine PIN nie im Klartext, sondern nur einen Prüfwert: einen SHA-256, aus dem sich die PIN nicht zurückrechnen lässt. Bei der Anmeldung rechnet die App den Prüfwert der eingegebenen PIN aus und vergleicht. Klingt sicher.

Ist es aber nicht, wenn es nur 10.000 mögliche PINs gibt. Zurückrechnen muss man dann gar nicht: einfach alle ausprobieren, bis ein Prüfwert passt. Ein Computer schafft das schneller, als du "Moment mal" sagen kannst.

Schreib `knacke(geheim)`, die zu einem Prüfwert die PIN als Text mit vier Ziffern liefert. Und merk dir, was das heißt: Ein Prüfwert schützt nur, wenn es sehr viele Möglichkeiten gibt. Darum sperren Geräte nach ein paar Fehlversuchen, darum mischen echte Systeme eine Zufallszahl (Salz) dazu und rechnen absichtlich langsam.
